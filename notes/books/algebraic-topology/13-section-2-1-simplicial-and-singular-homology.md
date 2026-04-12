# 2.1 Simplicial and Singular Homology

## Chapter 2

## Homology

The fundamental group \( {\pi }_{1}\left( X\right) \) is especially useful when studying spaces of low dimension, as one would expect from its definition which involves only maps from low-dimensional spaces into \( X \) , namely loops \( I \rightarrow  X \) and homotopies of loops, maps \( I \times  I \rightarrow  X \) . The definition in terms of objects that are at most 2-dimensional manifests itself for example in the fact that when \( X \) is a CW complex, \( {\pi }_{1}\left( X\right) \) depends only on the 2-skeleton of \( X \) . In view of the low-dimensional nature of the fundamental group, we should not expect it to be a very refined tool for dealing with high-dimensional spaces. Thus it cannot distinguish between spheres \( {S}^{n} \) with \( n \geq  2 \) . This limitation to low dimensions can be removed by considering the natural higher-dimensional analogs of \( {\pi }_{1}\left( X\right) \) , the homotopy groups \( {\pi }_{n}\left( X\right) \) , which are defined in terms of maps of the \( n \) -dimensional cube \( {I}^{n} \) into \( X \) and homotopies \( {I}^{n} \times  I \rightarrow  X \) of such maps. Not surprisingly, when \( X \) is a CW complex, \( {\pi }_{n}\left( X\right) \) depends only on the \( \left( {n + 1}\right) \) -skeleton of \( X \) . And as one might hope, homotopy groups do indeed distinguish spheres of all dimensions since \( {\pi }_{i}\left( {S}^{n}\right) \) is 0 for \( i < n \) and \( \mathbb{Z} \) for \( i = n \) .

However, the higher-dimensional homotopy groups have the serious drawback that they are extremely difficult to compute in general. Even for simple spaces like spheres, the calculation of \( {\pi }_{i}\left( {S}^{n}\right) \) for \( i > n \) turns out to be a huge problem. Fortunately there is a more computable alternative to homotopy groups: the homology groups \( {H}_{n}\left( X\right) \) . Like \( {\pi }_{n}\left( X\right) \) , the homology group \( {H}_{n}\left( X\right) \) for a CW complex \( X \) depends only on the \( \left( {n + 1}\right) \) -skeleton. For spheres, the homology groups \( {H}_{i}\left( {S}^{n}\right) \) are isomorphic to the homotopy groups \( {\pi }_{i}\left( {S}^{n}\right) \) in the range \( 1 \leq  i \leq  n \) , but homology groups have the advantage that \( {H}_{i}\left( {S}^{n}\right)  = 0 \) for \( i > n \) .

The computability of homology groups does not come for free, unfortunately. The definition of homology groups is decidedly less transparent than the definition of homotopy groups, and once one gets beyond the definition there is a certain amount of technical machinery to be set up before any real calculations and applications can be given. In the exposition below we approach the definition of \( {H}_{n}\left( X\right) \) by two preliminary stages, first giving a few motivating examples nonrigorously, then constructing a restricted model of homology theory called simplicial homology, before plunging into the general theory, known as singular homology. After the definition of singular homology has been assimilated, the real work of establishing its basic properties begins. This takes close to 20 pages, and there is no getting around the fact that it is a substantial effort. This takes up most of the first section of the chapter, with small digressions only for two applications to classical theorems of Brouwer: the fixed point theorem and 'invariance of dimension'.

The second section of the chapter gives more applications, including the homology definition of Euler characteristic and Brouwer's notion of degree for maps \( {S}^{n} \rightarrow  {S}^{n} \) . However, the main thrust of this section is toward developing techniques for calculating homology groups efficiently. The maximally efficient method is known as cellular homology, whose power comes perhaps from the fact that it is 'homology squared' - homology defined in terms of homology. Another quite useful tool is Mayer-Vietoris sequences, the analog for homology of van Kampen's theorem for the fundamental group.

An interesting feature of homology that begins to emerge after one has worked with it for a while is that it is the basic properties of homology that are used most often, and not the actual definition itself. This suggests that an axiomatic approach to homology might be possible. This is indeed the case, and in the third section of the chapter we list axioms which completely characterize homology groups for CW complexes. One could take the viewpoint that these rather algebraic axioms are all that really matters about homology groups, that the geometry involved in the definition of homology is secondary, needed only to show that the axiomatic theory is not vacuous. The extent to which one adopts this viewpoint is a matter of taste, and the route taken here of postponing the axioms until the theory is well-established is just one of several possible approaches.

The chapter then concludes with three optional sections of Additional Topics. The first is rather brief, relating \( {H}_{1}\left( X\right) \) to \( {\pi }_{1}\left( X\right) \) , while the other two contain a selection of classical applications of homology. These include the \( n \) -dimensional version of the Jordan curve theorem and the 'invariance of domain' theorem, both due to Brouwer, along with the Lefschetz fixed point theorem.

## The Idea of Homology

The difficulty with the higher homotopy groups \( {\pi }_{n} \) is that they are not directly computable from a cell structure as \( {\pi }_{1} \) is. For example, the 2-sphere has no cells in dimensions greater than 2, yet its \( n \) -dimensional homotopy group \( {\pi }_{n}\left( {S}^{2}\right) \) is nonzero for infinitely many values of \( n \) . Homology groups, by contrast, are quite directly related to cell structures, and may indeed be regarded as simply an algebraization of the first layer of geometry in cell structures: how cells of dimension \( n \) attach to cells of dimension \( n - 1 \) .

Let us look at some examples to see what the idea is. Consider the graph \( {X}_{1} \) shown in the figure, consisting of two vertices joined by four edges. When studying the fundamental group of \( {X}_{1} \) we consider loops formed by sequences of edges, starting and ending at a fixed basepoint. For example, at the basepoint \( x \) , the loop \( a{b}^{-1} \) travels forward along the edge \( a \) , then backward along \( b \) , as indicated by the exponent -1 . A more complicated loop would be \( a{c}^{-1}b{d}^{-1}c{a}^{-1} \) . A salient feature of the fundamental group is that it is generally nonabelian, which both enriches and complicates the theory. Suppose we simplify matters by abelianizing. Thus for example the two loops \( a{b}^{-1} \) and \( {b}^{-1}a \) are to be regarded as equal if we make \( a \) commute with \( {b}^{-1} \) . These two loops \( a{b}^{-1} \) and \( {b}^{-1}a \) are really the same circle, just with a different choice of starting and ending point: \( x \) for \( a{b}^{-1} \) and \( y \) for \( {b}^{-1}a \) . The same thing happens for all loops: Rechoosing the basepoint in a loop just permutes its letters cyclically, so a byproduct of abelianizing is that we no longer have to pin all our loops down to a fixed basepoint. Thus loops become cycles, without a chosen basepoint.

![bo_d7dtv0s91nqc73eq8nv0_107_1209_202_380_353_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_107_1209_202_380_353_0.jpg)

Having abelianized, let us switch to additive notation, so cycles become linear combinations of edges with integer coefficients, such as \( a - b + c - d \) . Let us call these linear combinations chains of edges. Some chains can be decomposed into cycles in several different ways, for example \( \left( {a - c}\right)  + \left( {b - d}\right)  = \left( {a - d}\right)  + \left( {b - c}\right) \) , and if we adopt an algebraic viewpoint then we do not want to distinguish between these different decompositions. Thus we broaden the meaning of the term 'cycle' to be simply any linear combination of edges for which at least one decomposition into cycles in the previous more geometric sense exists.

What is the condition for a chain to be a cycle in this more algebraic sense? A geometric cycle, thought of as a path traversed in time, is distinguished by the property that it enters each vertex the same number of times that it leaves the vertex. For an arbitrary chain \( {ka} + \ell b + {mc} + {nd} \) , the net number of times this chain enters \( y \) is \( k + \ell  + m + n \) since each of \( a, b, c \) , and \( d \) enters \( y \) once. Similarly, each of the four edges leaves \( x \) once, so the net number of times the chain \( {ka} + \ell b + {mc} + {nd} \) enters \( x \) is \( - k - \ell  - m - n \) . Thus the condition for \( {ka} + \ell b + {mc} + {nd} \) to be a cycle is simply \( k + \ell  + m + n = 0 \) .

To describe this result in a way that would generalize to all graphs, let \( {C}_{1} \) be the free abelian group with basis the edges \( a, b, c, d \) and let \( {C}_{0} \) be the free abelian group with basis the vertices \( x, y \) . Elements of \( {C}_{1} \) are chains of edges, or 1-dimensional chains, and elements of \( {C}_{0} \) are linear combinations of vertices, or 0-dimensional chains. Define a homomorphism \( \partial  : {C}_{1} \rightarrow  {C}_{0} \) by sending each basis element \( a, b, c, d \) to \( y - x \) , the vertex at the head of the edge minus the vertex at the tail. Thus we have \( \partial \left( {{ka} + \ell b + {mc} + {nd}}\right)  = \left( {k + \ell  + m + n}\right) y - \left( {k + \ell  + m + n}\right) x \) , and the cycles are precisely the kernel of \( \partial \) . It is a simple calculation to verify that \( a - b, b - c \) , and \( c - d \) form a basis for this kernel. Thus every cycle in \( {X}_{1} \) is a unique linear combination of these three most obvious cycles. By means of these three basic cycles we convey the geometric information that the graph \( {X}_{1} \) has three visible ’holes’, the empty spaces between the four edges.

Let us now enlarge the preceding graph \( {X}_{1} \) by attaching a 2-cell \( A \) along the cycle \( a - b \) , producing a 2-dimensional cell complex \( {X}_{2} \) . If we think of the 2-cell \( A \) as being oriented clockwise, then we can regard its boundary as the cycle \( a - b \) . This cycle is now homotopically trivial since we can contract it to a point by sliding over \( A \) . In other words, it no longer encloses a hole in \( {X}_{2} \) . This suggests that we form a quotient of the group of cycles in the preceding example by factoring out the subgroup generated by \( a - b \) . In this quotient the cycles \( a - c \) and \( b - c \) , for example, become equivalent, consistent with the fact that they are homotopic in \( {X}_{2} \) .

![bo_d7dtv0s91nqc73eq8nv0_108_1223_420_367_357_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_108_1223_420_367_357_0.jpg)

Algebraically, we can define now a pair of homomorphisms \( {C}_{2}\overset{{\partial }_{2}}{ \rightarrow  }{C}_{1}\overset{{\partial }_{1}}{ \rightarrow  }{C}_{0} \) where \( {C}_{2} \) is the infinite cyclic group generated by \( A \) and \( {\partial }_{2}\left( A\right)  = a - b \) . The map \( {\partial }_{1} \) is the boundary homomorphism in the previous example. The quotient group we are interested in is \( \operatorname{Ker}{\partial }_{1}/\operatorname{Im}{\partial }_{2} \) , the kernel of \( {\partial }_{1} \) modulo the image of \( {\partial }_{2} \) , or in other words, the 1-dimensional cycles modulo those that are boundaries, the multiples of \( a - b \) . This quotient group is the homology group \( {H}_{1}\left( {X}_{2}\right) \) . The previous example can be fit into this scheme too by taking \( {C}_{2} \) to be zero since there are no 2-cells in \( {X}_{1} \) , so in this case \( {H}_{1}\left( {X}_{1}\right)  = \operatorname{Ker}{\partial }_{1}/\operatorname{Im}{\partial }_{2} = \operatorname{Ker}{\partial }_{1} \) , which as we saw was free abelian on three generators. In the present example, \( {H}_{1}\left( {X}_{2}\right) \) is free abelian on two generators, \( b - c \) and \( c - d \) , expressing the geometric fact that by filling in the 2-cell \( A \) we have reduced the number of 'holes' in our space from three to two.

Suppose we enlarge \( {X}_{2} \) to a space \( {X}_{3} \) by attaching a second 2-cell \( B \) along the same cycle \( a - b \) . This gives a 2-dimensional chain group \( {C}_{2} \) consisting of linear combinations of \( A \) and \( B \) , and the boundary homomorphism \( {\partial }_{2} : {C}_{2} \rightarrow  {C}_{1} \) sends both \( A \) and \( B \) to \( a - b \) . The homology group \( {H}_{1}\left( {X}_{3}\right)  = \operatorname{Ker}{\partial }_{1}/\operatorname{Im}{\partial }_{2} \) is the same as for \( {X}_{2} \) , but now \( {\partial }_{2} \) has a nontrivial kernel, the infinite cyclic group generated by \( A - B \) . We view \( A - B \) as a 2-dimensional cycle, generating the homology group \( {H}_{2}\left( {X}_{3}\right)  = \operatorname{Ker}{\partial }_{2} \approx  \mathbb{Z} \) . Topologically, the cycle \( A - B \) is the sphere formed by the cells \( A \) and \( B \) together with their common boundary circle. This spherical cycle detects the presence of a ’hole’ in \( {X}_{3} \) , the missing interior of the sphere. However, since this hole is enclosed by a sphere rather than a circle, it is of a different sort from the holes detected by \( {H}_{1}\left( {X}_{3}\right)  \approx  \mathbb{Z} \times  \mathbb{Z} \) , which are detected by the cycles \( b - c \) and \( c - d \) .

![bo_d7dtv0s91nqc73eq8nv0_108_1215_1541_371_359_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_108_1215_1541_371_359_0.jpg)

Let us continue one more step and construct a complex \( {X}_{4} \) from \( {X}_{3} \) by attaching a 3-cell \( C \) along the 2-sphere formed by \( A \) and \( B \) . This creates a chain group \( {C}_{3} \) generated by this 3-cell \( C \) , and we define a boundary homomorphism \( {\partial }_{3} : {C}_{3} \rightarrow  {C}_{2} \) sending \( C \) to \( A - B \) since the cycle \( A - B \) should be viewed as the boundary of \( C \) in the same way that the 1-dimensional cycle \( a - b \) is the boundary of \( A \) . Now we have a sequence of three boundary homomorphisms \( {C}_{3}\xrightarrow[]{{\partial }_{3}}{C}_{2}\xrightarrow[]{{\partial }_{2}}{C}_{1}\xrightarrow[]{{\partial }_{1}}{C}_{0} \) and the quotient \( {H}_{2}\left( {X}_{4}\right)  = \operatorname{Ker}{\partial }_{2}/\operatorname{Im}{\partial }_{3} \) has become trivial. Also \( {H}_{3}\left( {X}_{4}\right)  = \operatorname{Ker}{\partial }_{3} = 0 \) . The group \( {H}_{1}\left( {X}_{4}\right) \) is the same as \( {H}_{1}\left( {X}_{3}\right) \) , namely \( \mathbb{Z} \times  \mathbb{Z} \) , so this is the only nontrivial homology group of \( {X}_{4} \) .

It is clear what the general pattern of the examples is. For a cell complex \( X \) one has chain groups \( {C}_{n}\left( X\right) \) which are free abelian groups with basis the \( n \) -cells of \( X \) , and there are boundary homomorphisms \( {\partial }_{n} : {C}_{n}\left( X\right)  \rightarrow  {C}_{n - 1}\left( X\right) \) , in terms of which one defines the homology group \( {H}_{n}\left( X\right)  = \operatorname{Ker}{\partial }_{n}/\operatorname{Im}{\partial }_{n + 1} \) . The major difficulty is how to define \( {\partial }_{n} \) in general. For \( n = 1 \) this is easy: The boundary of an oriented edge is the vertex at its head minus the vertex at its tail. The next case \( n = 2 \) is also not hard, at least for cells attached along cycles that are simply loops of edges, for then the boundary of the cell is this cycle of edges, with the appropriate signs taking orientations into account. But for larger \( n \) , matters become more complicated. Even if one restricts attention to cell complexes formed from polyhedral cells with nice attaching maps, there is still the matter of orientations to sort out.

The best solution to this problem seems to be to adopt an indirect approach. Arbitrary polyhedra can always be subdivided into special polyhedra called simplices (the triangle and the tetrahedron are the 2-dimensional and 3-dimensional instances) so there is no loss of generality, though initially there is some loss of efficiency, in restricting attention entirely to simplices. For simplices there is no difficulty in defining boundary maps or in handling orientations. So one obtains a homology theory, called simplicial homology, for cell complexes built from simplices. Still, this is a rather restricted class of spaces, and the theory itself has a certain rigidity that makes it awkward to work with.

The way around these obstacles is to step back from the geometry of spaces decomposed into simplices and to consider instead something which at first glance seems wildly more complicated, the collection of all possible continuous maps of simplices into a given space \( X \) . These maps generate tremendously large chain groups \( {C}_{n}\left( X\right) \) , but the quotients \( {H}_{n}\left( X\right)  = \operatorname{Ker}{\partial }_{n}/\operatorname{Im}{\partial }_{n + 1} \) , called singular homology groups, turn out to be much smaller, at least for reasonably nice spaces \( X \) . In particular, for spaces like those in the four examples above, the singular homology groups coincide with the homology groups we computed from the cellular chains. And as we shall see later in this chapter, singular homology allows one to define these nice cellular homology groups for all cell complexes, and in particular to solve the problem of defining the boundary maps for cellular chains.

The most important homology theory in algebraic topology, and the one we shall be studying almost exclusively, is called singular homology. Since the technical apparatus of singular homology is somewhat complicated, we will first introduce a more primitive version called simplicial homology in order to see how some of the apparatus works in a simpler setting before beginning the general theory.

The natural domain of definition for simplicial homology is a class of spaces we call \( \Delta \) -complexes, which are a mild generalization of the more classical notion of a simplicial complex. Historically, the modern definition of singular homology was first given in [Eilenberg 1944], and \( \Delta \) -complexes were introduced soon thereafter in [Eilenberg-Zilber 1950] where they were called semisimplicial complexes. Within a few years this term came to be applied to what Eilenberg and Zilber called complete semisimplicial complexes, and later there was yet another shift in terminology as the latter objects came to be called simplicial sets. In theory this frees up the term semisimplicial complex to have its original meaning, but to avoid potential confusion it seems best to introduce a new name, and the term \( \Delta \) -complex has at least the virtue of brevity.

## Δ-Complexes

The torus, the projective plane, and the Klein bottle can each be obtained from a square by identifying opposite edges in the way indicated by the arrows in the following figures:

![bo_d7dtv0s91nqc73eq8nv0_110_209_1400_1385_341_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_110_209_1400_1385_341_0.jpg)

Cutting a square along a diagonal produces two triangles, so each of these surfaces can also be built from two triangles by identifying their edges in pairs. In similar fashion a polygon with any number of sides can be cut along diagonals into triangles, so in fact all closed surfaces can be constructed from triangles by identifying edges. Thus we have a single building block, the triangle, from which all surfaces can be constructed. Using only triangles we could also construct a large class of 2-dimensional spaces that are not surfaces in the strict sense, by allowing more than two edges to be identified together at a time.

![bo_d7dtv0s91nqc73eq8nv0_110_1240_1863_347_342_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_110_1240_1863_347_342_0.jpg)

The idea of a \( \Delta \) -complex is to generalize constructions like these to any number of dimensions. The \( n \) -dimensional analog of the triangle is the \( n \) -simplex. This is the smallest convex set in a Euclidean space \( {\mathbb{R}}^{m} \) containing \( n + 1 \) points \( {v}_{0},\cdots ,{v}_{n} \) that do not lie in a hyperplane of dimension less than \( n \) , where by a hyperplane we mean the set of solutions of a system of linear equations. An equivalent condition would be that the difference vectors \( {v}_{1} - {v}_{0},\cdots ,{v}_{n} - {v}_{0} \) are linearly independent. The points \( {v}_{i} \) are the vertices of the simplex, and the simplex itself is denoted \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) . For example, there is the standard \( n \) -simplex

\[
{\Delta }^{n} = \left\{  {\left( {{t}_{0},\cdots ,{t}_{n}}\right)  \in  {\mathbb{R}}^{n + 1} \mid  \mathop{\sum }\limits_{i}{t}_{i} = 1\text{ and }{t}_{i} \geq  0\text{ for all }i}\right\}
\]

![bo_d7dtv0s91nqc73eq8nv0_111_915_275_674_331_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_111_915_275_674_331_0.jpg)

![bo_d7dtv0s91nqc73eq8nv0_111_1305_687_275_261_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_111_1305_687_275_261_0.jpg)

whose vertices are the unit vectors along the coordinate axes.

For purposes of homology it will be important to keep track of the order of the vertices of a simplex, so ’ \( n \) -simplex’ will really mean ’ \( n \) -simplex with an ordering of its vertices’. A by-product of ordering the vertices of a simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) is that this determines orientations of the edges \( \left\lbrack  {{v}_{i},{v}_{j}}\right\rbrack \) according to increasing subscripts, as shown in the two preceding figures. Specifying the ordering of the vertices also determines a canonical linear homeomorphism from the standard \( n \) -simplex \( {\Delta }^{n} \) onto any other \( n \) -simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) , preserving the order of vertices, namely, \( \left( {{t}_{0},\cdots ,{t}_{n}}\right)  \mapsto  \mathop{\sum }\limits_{i}{t}_{i}{v}_{i} \) . The coefficients \( {t}_{i} \) are the barycentric coordinates of the point \( \mathop{\sum }\limits_{i}{t}_{i}{v}_{i} \) in \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) .

If we delete one of the \( n + 1 \) vertices of an \( n \) -simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) , then the remaining \( n \) vertices span an \( \left( {n - 1}\right) \) -simplex, called a face of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) . We adopt the following convention:

The vertices of a face, or of any subsimplex spanned by a subset of the vertices, will always be ordered according to their order in the larger simplex.

The union of all the faces of \( {\Delta }^{n} \) is the boundary of \( {\Delta }^{n} \) , written \( \partial {\Delta }^{n} \) . The open simplex \( {\overset{ \circ  }{\Delta }}^{n} \) is \( {\Delta }^{n} - \partial {\Delta }^{n} \) , the interior of \( {\Delta }^{n} \) .

A Δ-complex structure on a space \( X \) is a collection of maps \( {\sigma }_{\alpha } : {\Delta }^{n} \rightarrow  X \) , with \( n \) depending on the index \( \alpha \) , such that:

(i) The restriction \( {\sigma }_{\alpha } \mid  {\Delta }^{n} \) is injective, and each point of \( X \) is in the image of exactly one such restriction \( {\sigma }_{\alpha } \mid  {\Delta }^{n} \) .

(ii) Each restriction of \( {\sigma }_{\alpha } \) to a face of \( {\Delta }^{n} \) is one of the maps \( {\sigma }_{\beta } : {\Delta }^{n - 1} \rightarrow  X \) . Here we are identifying the face of \( {\Delta }^{n} \) with \( {\Delta }^{n - 1} \) by the canonical linear homeomorphism between them that preserves the ordering of the vertices.

(iii) A set \( A \subset  X \) is open iff \( {\sigma }_{\alpha }^{-1}\left( A\right) \) is open in \( {\Delta }^{n} \) for each \( {\sigma }_{\alpha } \) . Among other things, this last condition rules out trivialities like regarding all the points of \( X \) as individual vertices. The earlier decompositions of the torus, projective plane, and Klein bottle into two triangles, three edges, and one or two vertices define \( \Delta \) -complex structures with a total of six \( {\sigma }_{\alpha } \) ’s for the torus and Klein bottle and seven for the projective plane. The orientations on the edges in the pictures are compatible with a unique ordering of the vertices of each simplex, and these orderings determine the maps \( {\sigma }_{\alpha } \) .

A consequence of (iii) is that \( X \) can be built as a quotient space of a collection of disjoint simplices \( {\Delta }_{\alpha }^{n} \) , one for each \( {\sigma }_{\alpha } : {\Delta }^{n} \rightarrow  X \) , the quotient space obtained by identifying each face of a \( {\Delta }_{\alpha }^{n} \) with the \( {\Delta }_{\beta }^{n - 1} \) corresponding to the restriction \( {\sigma }_{\beta } \) of \( {\sigma }_{\alpha } \) to the face in question, as in condition (ii). One can think of building the quotient space inductively, starting with a discrete set of vertices, then attaching edges to these to produce a graph, then attaching 2-simplices to the graph, and so on. From this viewpoint we see that the data specifying a \( \Delta \) -complex can be described purely combinatorially as collections of \( n \) -simplices \( {\Delta }_{\alpha }^{n} \) for each \( n \) together with functions associating to each face of each \( n \) -simplex \( {\Delta }_{\alpha }^{n} \) an \( \left( {n - 1}\right) \) -simplex \( {\Delta }_{\beta }^{n - 1} \) .

More generally, \( \Delta \) -complexes can be built from collections of disjoint simplices by identifying various subsimplices spanned by subsets of the vertices, where the identifications are performed using the canonical linear homeomorphisms that preserve the orderings of the vertices. The earlier \( \Delta \) -complex structures on a torus, projective plane, or Klein bottle can be obtained in this way, by identifying pairs of edges of two 2-simplices. If one starts with a single 2-simplex and identifies all three edges to a single edge, preserving the orientations given by the ordering of the vertices, this produces a \( \Delta \) -complex known as the ’dunce hat’. By contrast, if the three edges of a 2-simplex are identified preserving a cyclic orientation of the three edges, as in the first figure at the right, this does not produce a \( \Delta \) -complex structure, although if the 2-simplex is subdivided into three smaller 2-simplices about a central vertex, then one does obtain a \( \Delta \) -complex structure on the quotient space.

![bo_d7dtv0s91nqc73eq8nv0_112_1045_1477_544_235_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_112_1045_1477_544_235_0.jpg)

Thinking of a \( \Delta \) -complex \( X \) as a quotient space of a collection of disjoint simplices, it is not hard to see that \( X \) must be a Hausdorff space. Condition (iii) then implies that each restriction \( {\sigma }_{\alpha } \mid  {\Delta }^{n} \) is a homeomorphism onto its image, which is thus an open simplex in \( X \) . It follows from Proposition A. 2 in the Appendix that these open simplices \( {\sigma }_{\alpha }\left( {\Delta }^{n}\right) \) are the cells \( {e}_{\alpha }^{n} \) of a CW complex structure on \( X \) with the \( {\sigma }_{\alpha } \) ’s as characteristic maps. We will not need this fact at present, however.

## Simplicial Homology

Our goal now is to define the simplicial homology groups of a \( \Delta \) -complex \( X \) . Let \( {\Delta }_{n}\left( X\right) \) be the free abelian group with basis the open \( n \) -simplices \( {e}_{\alpha }^{n} \) of \( X \) . Elements of \( {\Delta }_{n}\left( X\right) \) , called \( n \) -chains, can be written as finite formal sums \( \mathop{\sum }\limits_{\alpha }{n}_{\alpha }{e}_{\alpha }^{n} \) with coefficients \( {n}_{\alpha } \in  \mathbb{Z} \) . Equivalently, we could write \( \mathop{\sum }\limits_{\alpha }{n}_{\alpha }{\sigma }_{\alpha } \) where \( {\sigma }_{\alpha } : {\Delta }^{n} \rightarrow  X \) is the characteristic map of \( {e}_{\alpha }^{n} \) , with image the closure of \( {e}_{\alpha }^{n} \) as described above. Such a sum \( \mathop{\sum }\limits_{\alpha }{n}_{\alpha }{\sigma }_{\alpha } \) can be thought of as a finite collection, or ’chain’, of \( n \) -simplices in \( X \) with integer multiplicities, the coefficients \( {n}_{\alpha } \) .

As one can see in the next figure, the boundary of the \( n \) -simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) consists of the various \( \left( {n - 1}\right) \) -dimensional simplices \( \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) , where the ’hat’ symbol \( {}^{ \land  } \) over \( {v}_{i} \) indicates that this vertex is deleted from the sequence \( {v}_{0},\cdots ,{v}_{n} \) . In terms of chains, we might then wish to say that the boundary of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) is the \( \left( {n - 1}\right) \) -chain formed by the sum of the faces \( \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) . However, it turns out to be better to insert certain signs and instead let the boundary of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) be \( \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) . Heuristically, the signs are inserted to take orientations into account, so that all the faces of a simplex are coherently oriented, as indicated in the following figure:

![bo_d7dtv0s91nqc73eq8nv0_113_241_896_1344_555_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_113_241_896_1344_555_0.jpg)

In the last case, the orientations of the two hidden faces are also counterclockwise when viewed from outside the 3-simplex.

With this geometry in mind we define for a general \( \Delta \) -complex \( X \) a boundary homomorphism \( {\partial }_{n} : {\Delta }_{n}\left( X\right)  \rightarrow  {\Delta }_{n - 1}\left( X\right) \) by specifying its values on basis elements:

\[
{\partial }_{n}\left( {\sigma }_{\alpha }\right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\sigma }_{\alpha }\left| \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack  \right|
\]

Note that the right side of this equation does indeed lie in \( {\Delta }_{n - 1}\left( X\right) \) since each restriction \( {\sigma }_{\alpha } \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) is the characteristic map of an \( \left( {n - 1}\right) \) -simplex of \( X \) .

Lemma 2.1. The composition \( {\Delta }_{n}\left( X\right) \xrightarrow[]{{\partial }_{n}}{\Delta }_{n - 1}\left( X\right) \xrightarrow[]{{\partial }_{n - 1}}{\Delta }_{n - 2}\left( X\right) \) is zero.

Proof: We have \( {\partial }_{n}\left( \sigma \right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) , and hence

\[
{\partial }_{n - 1}{\partial }_{n}\left( \sigma \right)  = \mathop{\sum }\limits_{{j < i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j}\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{j > i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j - 1}\sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{n}}\right\rbrack
\]

The latter two summations cancel since after switching \( i \) and \( j \) in the second sum, it becomes the negative of the first.

The algebraic situation we have now is a sequence of homomorphisms of abelian groups

\[
\cdots  \rightarrow  {C}_{n + 1}\xrightarrow[]{{\partial }_{n + 1}}{C}_{n}\xrightarrow[]{{\partial }_{n}}{C}_{n - 1} \rightarrow  \cdots  \rightarrow  {C}_{1}\xrightarrow[]{{\partial }_{1}}{C}_{0}\xrightarrow[]{{\partial }_{0}}0
\]

with \( {\partial }_{n}{\partial }_{n + 1} = 0 \) for each \( n \) . Such a sequence is called a chain complex. Note that we have extended the sequence by a 0 at the right end, with \( {\partial }_{0} = 0 \) . The equation \( {\partial }_{n}{\partial }_{n + 1} = 0 \) is equivalent to the inclusion \( \operatorname{Im}{\partial }_{n + 1} \subset  \operatorname{Ker}{\partial }_{n} \) , where \( \operatorname{Im} \) and \( \operatorname{Ker} \) denote image and kernel. So we can define the \( {n}^{th} \) homology group of the chain complex to be the quotient group \( {H}_{n} = \operatorname{Ker}{\partial }_{n}/\operatorname{Im}{\partial }_{n + 1} \) . Elements of \( \operatorname{Ker}{\partial }_{n} \) are called cycles and elements of \( \operatorname{Im}{\partial }_{n + 1} \) are called boundaries. Elements of \( {H}_{n} \) are cosets of \( \operatorname{Im}{\partial }_{n + 1} \) , called homology classes. Two cycles representing the same homology class are said to be homologous. This means their difference is a boundary.

Returning to the case that \( {C}_{n} = {\Delta }_{n}\left( X\right) \) , the homology group \( \operatorname{Ker}{\partial }_{n}/\operatorname{Im}{\partial }_{n + 1} \) will be denoted \( {H}_{n}^{\Delta }\left( X\right) \) and called the \( {n}^{th} \) simplicial homology group of \( X \) .

Example 2.2. \( X = {S}^{1} \) , with one vertex \( v \) and one edge \( e \) . Then \( {\Delta }_{0}\left( {S}^{1}\right) \) and \( {\Delta }_{1}\left( {S}^{1}\right) \) are both \( \mathbb{Z} \) and the boundary map \( {\partial }_{1} \) is zero since \( \partial e = v - v \) . The groups \( {\Delta }_{n}\left( {S}^{1}\right) \) are 0 for \( n \geq  2 \) since there are no simplices in these dimensions. Hence

\[
{H}_{n}^{\Delta }\left( {S}^{1}\right)  \approx  \left\{  \begin{array}{ll} \mathbb{Z} & \text{ for }n = 0,1 \\  0 & \text{ for }n \geq  2 \end{array}\right.
\]

![bo_d7dtv0s91nqc73eq8nv0_114_1425_1035_165_208_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_114_1425_1035_165_208_0.jpg)

This is an illustration of the general fact that if the boundary maps in a chain complex are all zero, then the homology groups of the complex are isomorphic to the chain groups themselves.

Example 2.3. \( X = T \) , the torus with the \( \Delta \) -complex structure pictured earlier, having one vertex, three edges \( a, b \) , and \( c \) , and two 2-simplices \( U \) and \( L \) . As in the previous example, \( {\partial }_{1} = 0 \) so \( {H}_{0}^{\Delta }\left( T\right)  \approx  \mathbb{Z} \) . Since \( {\partial }_{2}U = a + b - c = {\partial }_{2}L \) and \( \{ a, b, a + b - c\} \) is a basis for \( {\Delta }_{1}\left( T\right) \) , it follows that \( {H}_{1}^{\Delta }\left( T\right)  \approx  \mathbb{Z} \oplus  \mathbb{Z} \) with basis the homology classes \( \left\lbrack  a\right\rbrack \) and \( \left\lbrack  b\right\rbrack \) . Since there are no 3-simplices, \( {H}_{2}^{\Delta }\left( T\right) \) is equal to \( \operatorname{Ker}{\partial }_{2} \) , which is infinite cyclic generated by \( U - L \) since \( \partial \left( {{pU} + {qL}}\right)  = \left( {p + q}\right) \left( {a + b - c}\right)  = 0 \) only if \( p =  - q \) . Thus

\[
{H}_{n}^{\Delta }\left( T\right)  \approx  \left\{  \begin{array}{ll} \mathbb{Z} \oplus  \mathbb{Z} & \text{ for }n = 1 \\  \mathbb{Z} & \text{ for }n = 0,2 \\  0 & \text{ for }n \geq  3 \end{array}\right.
\]

Example 2.4. \( X = {\mathbb{{RP}}}^{2} \) , as pictured earlier, with two vertices \( v \) and \( w \) , three edges \( a, b \) , and \( c \) , and two 2-simplices \( U \) and \( L \) . Then \( \operatorname{Im}{\partial }_{1} \) is generated by \( w - v \) , so \( {H}_{0}^{\Delta }\left( X\right)  \approx  \mathbb{Z} \) with either vertex as a generator. Since \( {\partial }_{2}U =  - a + b + c \) and \( {\partial }_{2}L = a - b + c \) , we see that \( {\partial }_{2} \) is injective, so \( {H}_{2}^{\Delta }\left( X\right)  = 0 \) . Further, \( \operatorname{Ker}{\partial }_{1} \approx  \mathbb{Z} \oplus  \mathbb{Z} \) with basis \( a - b \) and \( c \) , and \( \operatorname{Im}{\partial }_{2} \) is an index-two subgroup of \( \operatorname{Ker}{\partial }_{1} \) since we can choose \( c \) and \( a - b + c \) as a basis for \( \operatorname{Ker}{\partial }_{1} \) and \( a - b + c \) and \( {2c} = \left( {a - b + c}\right)  + \left( {-a + b + c}\right) \) as a basis for \( \operatorname{Im}{\partial }_{2} \) . Thus \( {H}_{1}^{\Delta }\left( X\right)  \approx  {\mathbb{Z}}_{2} \) .

Example 2.5. We can obtain a \( \Delta \) -complex structure on \( {S}^{n} \) by taking two copies of \( {\Delta }^{n} \) and identifying their boundaries via the identity map. Labeling these two \( n \) -simplices \( U \) and \( L \) , then it is obvious that \( \operatorname{Ker}{\partial }_{n} \) is infinite cyclic generated by \( U - L \) . Thus \( {H}_{n}^{\Delta }\left( {S}^{n}\right)  \approx  \mathbb{Z} \) for this \( \Delta \) -complex structure on \( {S}^{n} \) . Computing the other homology groups would be more difficult.

Many similar examples could be worked out without much trouble, such as the other closed orientable and nonorientable surfaces. However, the calculations do tend to increase in complexity before long, particularly for higher-dimensional complexes.

Some obvious general questions arise: Are the groups \( {H}_{n}^{\Delta }\left( X\right) \) independent of the choice of \( \Delta \) -complex structure on \( X \) ? In other words, if two \( \Delta \) -complexes are homeomorphic, do they have isomorphic homology groups? More generally, do they have isomorphic homology groups if they are merely homotopy equivalent? To answer such questions and to develop a general theory it is best to leave the rather rigid simplicial realm and introduce the singular homology groups. These have the added advantage that they are defined for all spaces, not just \( \Delta \) -complexes. At the end of this section, after some theory has been developed, we will show that simplicial and singular homology groups coincide for \( \Delta \) -complexes.

Traditionally, simplicial homology is defined for simplicial complexes, which are the \( \Delta \) -complexes whose simplices are uniquely determined by their vertices. This amounts to saying that each \( n \) -simplex has \( n + 1 \) distinct vertices, and that no other \( n \) -simplex has this same set of vertices. Thus a simplicial complex can be described combinatorially as a set \( {X}_{0} \) of vertices together with sets \( {X}_{n} \) of \( n \) -simplices, which are \( \left( {n + 1}\right) \) -element subsets of \( {X}_{0} \) . The only requirement is that each \( \left( {k + 1}\right) \) -element subset of the vertices of an \( n \) -simplex in \( {X}_{n} \) is a \( k \) -simplex, in \( {X}_{k} \) . From this combinatorial data a \( \Delta \) -complex \( X \) can be constructed, once we choose a partial ordering of the vertices \( {X}_{0} \) that restricts to a linear ordering on the vertices of each simplex in \( {X}_{n} \) . For example, we could just choose a linear ordering of all the vertices. This might perhaps involve invoking the Axiom of Choice for large vertex sets.

An exercise at the end of this section is to show that every \( \Delta \) -complex can be subdivided to be a simplicial complex. In particular, every \( \Delta \) -complex is then homeomorphic to a simplicial complex.

Compared with simplicial complexes, \( \Delta \) -complexes have the advantage of simpler computations since fewer simplices are required. For example, to put a simplicial complex structure on the torus one needs at least 14 triangles, 21 edges, and 7 vertices, and for \( {\mathbb{{RP}}}^{2} \) one needs at least 10 triangles,15 edges, and 6 vertices. This would slow down calculations considerably!

## Singular Homology

A singular \( n \) -simplex in a space \( X \) is by definition just a map \( \sigma  : {\Delta }^{n} \rightarrow  X \) . The word 'singular' is used here to express the idea that \( \sigma \) need not be a nice embedding but can have 'singularities' where its image does not look at all like a simplex. All that is required is that \( \sigma \) be continuous. Let \( {C}_{n}\left( X\right) \) be the free abelian group with basis the set of singular \( n \) -simplices in \( X \) . Elements of \( {C}_{n}\left( X\right) \) , called \( n \) -chains, or more precisely singular \( n \) -chains, are finite formal sums \( \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i} \) for \( {n}_{i} \in  \mathbb{Z} \) and \( {\sigma }_{i} : {\Delta }^{n} \rightarrow  X \) . A boundary map \( {\partial }_{n} : {C}_{n}\left( X\right)  \rightarrow  {C}_{n - 1}\left( X\right) \) is defined by the same formula as before:

\[
{\partial }_{n}\left( \sigma \right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\sigma \left| \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack  \right|
\]

Implicit in this formula is the canonical identification of \( \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) with \( {\Delta }^{n - 1} \) , preserving the ordering of vertices, so that \( \sigma  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) is regarded as a map \( {\Delta }^{n - 1} \rightarrow  X \) , that is, a singular \( \left( {n - 1}\right) \) -simplex.

Often we write the boundary map \( {\partial }_{n} \) from \( {C}_{n}\left( X\right) \) to \( {C}_{n - 1}\left( X\right) \) simply as \( \partial \) when this does not lead to serious ambiguities. The proof of Lemma 2.1 applies equally well to singular simplices, showing that \( {\partial }_{n}{\partial }_{n + 1} = 0 \) or more concisely \( {\partial }^{2} = 0 \) , so we can define the singular homology group \( {H}_{n}\left( X\right)  = \operatorname{Ker}{\partial }_{n}/\operatorname{Im}{\partial }_{n + 1} \) .

It is evident from the definition that homeomorphic spaces have isomorphic singular homology groups \( {H}_{n} \) , in contrast with the situation for \( {H}_{n}^{\Delta } \) . On the other hand, since the groups \( {C}_{n}\left( X\right) \) are so large, the number of singular \( n \) -simplices in \( X \) usually being uncountable, it is not at all clear that for a \( \Delta \) -complex \( X \) with finitely many simplices, \( {H}_{n}\left( X\right) \) should be finitely generated for all \( n \) , or that \( {H}_{n}\left( X\right) \) should be zero for \( n \) larger than the dimension of \( X \) - two properties that are trivial for \( {H}_{n}^{\Delta }\left( X\right) \) .

Though singular homology looks so much more general than simplicial homology, it can actually be regarded as a special case of simplicial homology by means of the following construction. For an arbitrary space \( X \) , define the singular complex \( S\left( X\right) \) to be the \( \Delta \) -complex with one \( n \) -simplex \( {\Delta }_{\sigma }^{n} \) for each singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) , with \( {\Delta }_{\sigma }^{n} \) attached in the obvious way to the \( \left( {n - 1}\right) \) -simplices of \( S\left( X\right) \) that are the restrictions of \( \sigma \) to the various \( \left( {n - 1}\right) \) -simplices in \( \partial {\Delta }^{n} \) . It is clear from the definitions that \( {H}_{n}^{\Delta }\left( {S\left( X\right) }\right) \) is identical with \( {H}_{n}\left( X\right) \) for all \( n \) , and in this sense the singular homology group \( {H}_{n}\left( X\right) \) is a special case of a simplicial homology group. One can regard \( S\left( X\right) \) as a \( \Delta \) -complex model for \( X \) , although it is usually an extremely large object compared to \( X \) .

Cycles in singular homology are defined algebraically, but they can be given a somewhat more geometric interpretation in terms of maps from finite \( \Delta \) -complexes. To see this, note first that a singular \( n \) -chain \( \xi \) can always be written in the form \( \mathop{\sum }\limits_{i}{\varepsilon }_{i}{\sigma }_{i} \) with \( {\varepsilon }_{i} =  \pm  1 \) , allowing repetitions of the singular \( n \) -simplices \( {\sigma }_{i} \) . Given such an \( n \) -chain \( \xi  = \mathop{\sum }\limits_{i}{\varepsilon }_{i}{\sigma }_{i} \) , when we compute \( \partial \xi \) as a sum of singular \( \left( {n - 1}\right) \) -simplices with signs \( \pm  1 \) , there may be some canceling pairs consisting of two identical singular \( \left( {n - 1}\right) \) -simplices with opposite signs. Choosing a maximal collection of such canceling pairs, construct an \( n \) -dimensional \( \Delta \) -complex \( {K}_{\xi } \) from a disjoint union of \( n \) -simplices \( {\Delta }_{i}^{n} \) , one for each \( {\sigma }_{i} \) , by identifying the pairs of \( \left( {n - 1}\right) \) -dimensional faces corresponding to the chosen canceling pairs. The \( {\sigma }_{i} \) ’s then induce a map \( {K}_{\xi } \rightarrow  X \) . If \( \xi \) is a cycle, all the \( \left( {n - 1}\right) \) -dimensional faces of the \( {\Delta }_{i}^{n} \) ’s are identified in pairs. Thus \( {K}_{\xi } \) is a manifold, locally homeomorphic to \( {\mathbb{R}}^{n} \) , near all points in the complement of the \( \left( {n - 2}\right) \) -skeleton \( {K}_{\xi }^{n - 2} \) of \( {K}_{\xi } \) . All the \( n \) -simplices of \( {K}_{\xi } \) can be coherently oriented by taking the signs of the \( {\sigma }_{i} \) ’s into account, so \( {K}_{\xi } - {K}_{\xi }^{n - 2} \) is actually an oriented manifold. A closer inspection shows that \( {K}_{\xi } \) is also a manifold near points in the interiors of \( \left( {n - 2}\right) \) -simplices, so the nonmanifold points of \( {K}_{\xi } \) in fact lie in the \( \left( {n - 3}\right) \) -skeleton. However, near points in the interiors of \( \left( {n - 3}\right) \) -simplices it can very well happen that \( {K}_{\xi } \) is not a manifold.

In particular, elements of \( {H}_{1}\left( X\right) \) are represented by collections of oriented loops in \( X \) , and elements of \( {H}_{2}\left( X\right) \) are represented by maps of closed oriented surfaces into \( X \) . With a bit more work it can be shown that an oriented 1-cycle \( \mathop{\coprod }\limits_{\alpha }{S}_{\alpha }^{1} \rightarrow  X \) is zero in \( {H}_{1}\left( X\right) \) iff it extends to a map of a compact oriented surface with boundary \( \mathop{\coprod }\limits_{\alpha }{S}_{\alpha }^{1} \) into \( X \) . The analogous statement for 2-cycles is also true. In the early days of homology theory it may have been believed, or at least hoped, that this close connection with manifolds continued in all higher dimensions, but this has turned out not to be the case. There is a sort of homology theory built from manifolds, called bordism, but it is quite a bit more complicated than the homology theory we are studying here.

After these preliminary remarks let us begin to see what can be proved about singular homology.

Proposition 2.6. Corresponding to the decomposition of a space \( X \) into its path-components \( {X}_{\alpha } \) there is an isomorphism of \( {H}_{n}\left( X\right) \) with the direct sum \( { \oplus  }_{\alpha }{H}_{n}\left( {X}_{\alpha }\right) \) .

Proof: Since a singular simplex always has path-connected image, \( {C}_{n}\left( X\right) \) splits as the direct sum of its subgroups \( {C}_{n}\left( {X}_{\alpha }\right) \) . The boundary maps \( {\partial }_{n} \) preserve this direct sum decomposition, taking \( {C}_{n}\left( {X}_{\alpha }\right) \) to \( {C}_{n - 1}\left( {X}_{\alpha }\right) \) , so Ker \( {\partial }_{n} \) and \( \operatorname{Im}{\partial }_{n + 1} \) split similarly as direct sums, hence the homology groups also split, \( {H}_{n}\left( X\right)  \approx  {\bigoplus }_{\alpha }{H}_{n}\left( {X}_{\alpha }\right) \) .

Proposition 2.7. If \( X \) is nonempty and path-connected, then \( {H}_{0}\left( X\right)  \approx  \mathbb{Z} \) . Hence for any space \( X,{H}_{0}\left( X\right) \) is a direct sum of \( \mathbb{Z} \) ’s, one for each path-component of \( X \) .

Proof: By definition, \( {H}_{0}\left( X\right)  = {C}_{0}\left( X\right) /\operatorname{Im}{\partial }_{1} \) since \( {\partial }_{0} = 0 \) . Define a homomorphism \( \varepsilon  : {C}_{0}\left( X\right)  \rightarrow  \mathbb{Z} \) by \( \varepsilon \left( {\mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i}}\right)  = \mathop{\sum }\limits_{i}{n}_{i} \) . This is obviously surjective if \( X \) is nonempty. The claim is that \( \operatorname{Ker}\varepsilon  = \operatorname{Im}{\partial }_{1} \) if \( X \) is path-connected, and hence \( \varepsilon \) induces an isomorphism \( {H}_{0}\left( X\right)  \approx  \mathbb{Z} \) .

To verify the claim, observe first that \( \operatorname{Im}{\partial }_{1} \subset  \operatorname{Ker}\varepsilon \) since for a singular 1-simplex \( \sigma  : {\Delta }^{1} \rightarrow  X \) we have \( \varepsilon {\partial }_{1}\left( \sigma \right)  = \varepsilon \left( {\sigma \left| {\left\lbrack  {v}_{1}\right\rbrack   - \sigma }\right| \left\lbrack  {v}_{0}\right\rbrack  }\right)  = 1 - 1 = 0 \) . For the reverse inclusion Ker \( \varepsilon  \subset  \operatorname{Im}{\partial }_{1} \) , suppose \( \varepsilon \left( {\mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i}}\right)  = 0 \) , so \( \mathop{\sum }\limits_{i}{n}_{i} = 0 \) . The \( {\sigma }_{i} \) ’s are singular 0 -simplices, which are simply points of \( X \) . Choose a path \( {\tau }_{i} : I \rightarrow  X \) from a basepoint \( {x}_{0} \) to \( {\sigma }_{i}\left( {v}_{0}\right) \) and let \( {\sigma }_{0} \) be the singular 0-simplex with image \( {x}_{0} \) . We can view \( {\tau }_{i} \) as a singular 1-simplex, a map \( {\tau }_{i} : \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack   \rightarrow  X \) , and then we have \( \partial {\tau }_{i} = {\sigma }_{i} - {\sigma }_{0} \) . Hence \( \partial \left( {\mathop{\sum }\limits_{i}{n}_{i}{\tau }_{i}}\right)  = \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i} - \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{0} = \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i} \) since \( \mathop{\sum }\limits_{i}{n}_{i} = 0 \) . Thus \( \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i} \) is a boundary, which shows that \( \operatorname{Ker}\varepsilon  \subset  \operatorname{Im}{\partial }_{1} \) .

Proposition 2.8. If \( X \) is a point, then \( {H}_{n}\left( X\right)  = 0 \) for \( n > 0 \) and \( {H}_{0}\left( X\right)  \approx  \mathbb{Z} \) .

Proof: In this case there is a unique singular \( n \) -simplex \( {\sigma }_{n} \) for each \( n \) , and \( \partial \left( {\sigma }_{n}\right)  = \; \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\sigma }_{n - 1} \) , a sum of \( n + 1 \) terms, which is therefore0for \( n \) odd and \( {\sigma }_{n - 1} \) for \( n \) even, \( n \neq  0 \) . Thus we have the chain complex

\[
\cdots  \rightarrow  \mathbb{Z}\overset{ \approx  }{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z}\overset{ \approx  }{ \rightarrow  }\mathbb{Z}\overset{0}{ \rightarrow  }\mathbb{Z} \rightarrow  0
\]

with boundary maps alternately isomorphisms and trivial maps, except at the last \( \mathbb{Z} \) . The homology groups of this complex are trivial except for \( {H}_{0} \approx  \mathbb{Z} \) .

It is often very convenient to have a slightly modified version of homology for which a point has trivial homology groups in all dimensions, including zero. This is done by defining the reduced homology groups \( {\widetilde{H}}_{n}\left( X\right) \) to be the homology groups of the augmented chain complex

\[
\cdots  \rightarrow  {C}_{2}\left( X\right) \overset{{\partial }_{2}}{ \rightarrow  }{C}_{1}\left( X\right) \overset{{\partial }_{1}}{ \rightarrow  }{C}_{0}\left( X\right) \overset{\varepsilon }{ \rightarrow  }\mathbb{Z} \rightarrow  0
\]

where \( \varepsilon \left( {\mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i}}\right)  = \mathop{\sum }\limits_{i}{n}_{i} \) as in the proof of Proposition 2.7. Here we had better require \( X \) to be nonempty, to avoid having a nontrivial homology group in dimension -1 . Since \( \varepsilon {\partial }_{1} = 0,\varepsilon \) vanishes on \( \operatorname{Im}{\partial }_{1} \) and hence induces a map \( {H}_{0}\left( X\right)  \rightarrow  \mathbb{Z} \) with kernel \( {\widetilde{H}}_{0}\left( X\right) \) , so \( {H}_{0}\left( X\right)  \approx  {\widetilde{H}}_{0}\left( X\right)  \oplus  \mathbb{Z} \) . Obviously \( {H}_{n}\left( X\right)  \approx  {\widetilde{H}}_{n}\left( X\right) \) for \( n > 0 \) .

Formally, one can think of the extra \( \mathbb{Z} \) in the augmented chain complex as generated by the unique map \( \left\lbrack  \varnothing \right\rbrack   \rightarrow  X \) where \( \left\lbrack  \varnothing \right\rbrack \) is the empty simplex, with no vertices. The augmentation map \( \varepsilon \) is then the usual boundary map since \( \partial \left\lbrack  {v}_{0}\right\rbrack   = \left\lbrack  {\widehat{v}}_{0}\right\rbrack   = \left\lbrack  \varnothing \right\rbrack \) .

Readers who know about the fundamental group \( {\pi }_{1}\left( X\right) \) may wish to make a detour here to look at \( \text{ § }2. \) A where it is shown that \( {H}_{1}\left( X\right) \) is the abelianization of \( {\pi }_{1}\left( X\right) \) whenever \( X \) is path-connected. This result will not be needed elsewhere in the chapter, however.

## Homotopy Invariance

The first substantial result we will prove about singular homology is that homotopy equivalent spaces have isomorphic homology groups. This will be done by showing that a map \( f : X \rightarrow  Y \) induces a homomorphism \( {f}_{ * } : {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) for each \( n \) , and that \( {f}_{ * } \) is an isomorphism if \( f \) is a homotopy equivalence.

For a map \( f : X \rightarrow  Y \) , an induced homomorphism \( {f}_{\sharp } : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( Y\right) \) is defined by composing each singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) with \( f \) to get a singular \( n \) -simplex

\( {f}_{\sharp }\left( \sigma \right)  = {f\sigma } : {\Delta }^{n} \rightarrow  Y \) , then extending \( {f}_{\sharp } \) linearly via \( {f}_{\sharp }\left( {\mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i}}\right)  = \mathop{\sum }\limits_{i}{n}_{i}{f}_{\sharp }\left( {\sigma }_{i}\right)  = \; \mathop{\sum }\limits_{i}{n}_{i}f{\sigma }_{i} \) . The maps \( {f}_{\sharp } : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( Y\right) \) satisfy \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) since

\[
{f}_{\sharp }\partial \left( \sigma \right)  = {f}_{\sharp }\left( {\mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\sigma \left| \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack  \right) }\right.
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{f\sigma } \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack   = \partial {f}_{\sharp }\left( \sigma \right)
\]

Thus we have a diagram

![bo_d7dtv0s91nqc73eq8nv0_119_428_461_951_193_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_119_428_461_951_193_0.jpg)

such that in each square the composition \( {f}_{\sharp }\partial \) equals the composition \( \partial {f}_{\sharp } \) . A diagram of maps with the property that any two compositions of maps starting at one point in the diagram and ending at another are equal is called a commutative diagram. In the present case commutativity of the diagram is equivalent to the commutativity relation \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) , but commutative diagrams can contain commutative triangles, pentagons, etc., as well as commutative squares.

The fact that the maps \( {f}_{\sharp } : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( Y\right) \) satisfy \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) is also expressed by saying that the \( {f}_{\sharp } \) ’s define a chain map from the singular chain complex of \( X \) to that of \( Y \) . The relation \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) implies that \( {f}_{\sharp } \) takes cycles to cycles since \( \partial \alpha  = 0 \) implies \( \partial \left( {{f}_{\sharp }\alpha }\right)  = {f}_{\sharp }\left( {\partial \alpha }\right)  = 0 \) . Also, \( {f}_{\sharp } \) takes boundaries to boundaries since \( {f}_{\sharp }\left( {\partial \beta }\right)  = \partial \left( {{f}_{\sharp }\beta }\right) \) . Hence \( {f}_{\sharp } \) induces a homomorphism \( {f}_{ * } : {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) . An algebraic statement of what we have just proved is:

Proposition 2.9. A chain map between chain complexes induces homomorphisms between the homology groups of the two complexes.

Two basic properties of induced homomorphisms which are important in spite of being rather trivial are:

(i) \( {\left( fg\right) }_{ * } = {f}_{ * }{g}_{ * } \) for a composed mapping \( X\overset{g}{ \rightarrow  }Y\overset{f}{ \rightarrow  }Z \) . This follows from associativity of compositions \( {\Delta }^{n}\overset{\sigma }{ \rightarrow  }X\overset{g}{ \rightarrow  }Y\overset{f}{ \rightarrow  }Z \) .

(ii) \( {\mathbb{1}}_{ * } = \mathbb{1} \) where1denotes the identity map of a space or a group.

Less trivially, we have:

Theorem 2.10. If two maps \( f, g : X \rightarrow  Y \) are homotopic, then they induce the same homomorphism \( {f}_{ * } = {g}_{ * } : {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) .

In view of the formal properties \( {\left( fg\right) }_{ * } = {f}_{ * }{g}_{ * } \) and \( {\mathbb{1}}_{ * } = \mathbb{1} \) , this immediately implies:

|| Corollary 2.11. The maps \( {f}_{ * } : {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) induced by a homotopy equivalence \( f : X \rightarrow  Y \) are isomorphisms for all \( n \) .

For example, if \( X \) is contractible then \( {\widetilde{H}}_{n}\left( X\right)  = 0 \) for all \( n \) .

Proof of 2.10: The essential ingredient is a procedure for subdividing \( {\Delta }^{n} \times  I \) into simplices. The figure shows the cases \( n = 1,2 \) . In \( {\Delta }^{n} \times  I \) , let \( {\Delta }^{n} \times  \{ 0\}  = \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) and \( {\Delta }^{n} \times  \{ 1\}  = \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) , where \( {v}_{i} \) and \( {w}_{i} \) have the same image under the projection \( {\Delta }^{n} \times  I \rightarrow  {\Delta }^{n} \) . We can pass from \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) to \( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) by interpolating a sequence of \( n \) -simplices, each obtained from the preceding one by moving one vertex \( {v}_{i} \) up to \( {w}_{i} \) , starting with \( {v}_{n} \) and working backwards to \( {v}_{0} \) . Thus the first step is to move \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) up to \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n - 1},{w}_{n}}\right\rbrack \) , then the second step is to move this up to \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n - 2},{w}_{n - 1},{w}_{n}}\right\rbrack \) , and so on. In the typical step \( \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i + 1},\cdots ,{w}_{n}}\right\rbrack \) moves up to \( \left\lbrack  {{v}_{0},\cdots ,{v}_{i - 1},{w}_{i},\cdots ,{w}_{n}}\right\rbrack \) . The region between these two \( n \) -simplices is exactly the \( \left( {n + 1}\right) \) -simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i},\cdots ,{w}_{n}}\right\rbrack \) which has \( \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i + 1},\cdots ,{w}_{n}}\right\rbrack \) as its lower face and \( \left\lbrack  {{v}_{0},\cdots ,{v}_{i - 1},{w}_{i},\cdots ,{w}_{n}}\right\rbrack \) as its upper face. Altogether, \( {\Delta }^{n} \times  I \) is the union of the \( \left( {n + 1}\right) \) -simplices \( \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i},\cdots ,{w}_{n}}\right\rbrack \) , each intersecting the next in an \( n \) -simplex face.

![bo_d7dtv0s91nqc73eq8nv0_120_1191_173_395_684_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_120_1191_173_395_684_0.jpg)

Given a homotopy \( F : X \times  I \rightarrow  Y \) from \( f \) to \( g \) and a singular simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) , we can form the composition \( F \circ  \left( {\sigma  \times  \mathbb{1}}\right)  : {\Delta }^{n} \times  I \rightarrow  X \times  I \rightarrow  Y \) . Using this, we can define prism operators \( P : {C}_{n}\left( X\right)  \rightarrow  {C}_{n + 1}\left( Y\right) \) by the following formula:

\[
P\left( \sigma \right)  = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}F \circ  \left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i},\cdots ,{w}_{n}}\right\rbrack
\]

We will show that these prism operators satisfy the basic relation

\[
\partial P = {g}_{\sharp } - {f}_{\sharp } - P\partial
\]

Geometrically, the left side of this equation represents the boundary of the prism, and the three terms on the right side represent the top \( {\Delta }^{n} \times  \{ 1\} \) , the bottom \( {\Delta }^{n} \times  \{ 0\} \) , and the sides \( \partial {\Delta }^{n} \times  I \) of the prism. To prove the relation we calculate

\[
\partial P\left( \sigma \right)  = \mathop{\sum }\limits_{{j \leq  i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j}{F}^{ \circ  }\left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{i},{w}_{i},\cdots ,{w}_{n}}\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{j \geq  i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j + 1}{F}^{ \circ  }\left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i},\cdots ,{\widehat{w}}_{j},\cdots ,{w}_{n}}\right\rbrack
\]

The terms with \( i = j \) in the two sums cancel except for \( F \circ  \left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{\widehat{v}}_{0},{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) , which is \( g \circ  \sigma  = {g}_{\sharp }\left( \sigma \right) \) , and \( - F \circ  \left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{n},{\widehat{w}}_{n}}\right\rbrack \) , which is \( - f \circ  \sigma  =  - {f}_{\sharp }\left( \sigma \right) \) . The terms with \( i \neq  j \) are exactly \( - P\partial \left( \sigma \right) \) since

\[
P\partial \left( \sigma \right)  = \mathop{\sum }\limits_{{i < j}}{\left( -1\right) }^{i}{\left( -1\right) }^{j}{F}^{ \circ  }\left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{v}_{0},\cdots ,{v}_{i},{w}_{i},\cdots ,{\widehat{w}}_{j},\cdots ,{w}_{n}}\right\rbrack
\]

\[
+ \mathop{\sum }\limits_{{i > j}}{\left( -1\right) }^{i - 1}{\left( -1\right) }^{j}{F}^{ \circ  }\left( {\sigma  \times  \mathbb{1}}\right)  \mid  \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{j},\cdots ,{v}_{i},{w}_{i},\cdots ,{w}_{n}}\right\rbrack
\]

Now we can finish the proof of the theorem. If \( \alpha  \in  {C}_{n}\left( X\right) \) is a cycle, then we have \( {g}_{\sharp }\left( \alpha \right)  - {f}_{\sharp }\left( \alpha \right)  = \partial P\left( \alpha \right)  + P\partial \left( \alpha \right)  = \partial P\left( \alpha \right) \) since \( \partial \alpha  = 0 \) . Thus \( {g}_{\sharp }\left( \alpha \right)  - {f}_{\sharp }\left( \alpha \right) \) is a boundary, so \( {g}_{\sharp }\left( \alpha \right) \) and \( {f}_{\sharp }\left( \alpha \right) \) determine the same homology class, which means that \( {g}_{ * } \) equals \( {f}_{ * } \) on the homology class of \( \alpha \) .

The relationship \( \partial P + P\partial  = {g}_{\sharp } - {f}_{\sharp } \) is expressed by saying \( P \) is a chain homotopy between the chain maps \( {f}_{\sharp } \) and \( {\mathcal{G}}_{\sharp } \) . We have just shown:

Proposition 2.12. Chain-homotopic chain maps induce the same homomorphism on homology.

There are also induced homomorphisms \( {f}_{ * } : {\widetilde{H}}_{n}\left( X\right)  \rightarrow  {\widetilde{H}}_{n}\left( Y\right) \) for reduced homology groups since \( {f}_{\sharp }\varepsilon  = \varepsilon {f}_{\sharp } \) where \( {f}_{\sharp } \) is the identity map on the added groups \( \mathbb{Z} \) in the augmented chain complexes. The properties of induced homomorphisms we proved above hold equally well in the setting of reduced homology, with the same proofs.

## Exact Sequences and Excision

If there was always a simple relationship between the homology groups of a space \( X \) , a subspace \( A \) , and the quotient space \( X/A \) , then this could be a very useful tool in understanding the homology groups of spaces such as CW complexes that can be built inductively from successively more complicated subspaces. Perhaps the simplest possible relationship would be if \( {H}_{n}\left( X\right) \) contained \( {H}_{n}\left( A\right) \) as a subgroup and the quotient group \( {H}_{n}\left( X\right) /{H}_{n}\left( A\right) \) was isomorphic to \( {H}_{n}\left( {X/A}\right) \) . While this does hold in some cases, if it held in general then homology theory would collapse totally since every space \( X \) can be embedded as a subspace of a space with trivial homology groups, namely the cone \( {CX} = \left( {X \times  I}\right) /\left( {X\times \{ 0\} }\right) \) , which is contractible.

It turns out that this overly simple model does not have to be modified too much to get a relationship that is valid in fair generality. The novel feature of the actual relationship is that it involves the groups \( {H}_{n}\left( X\right) ,{H}_{n}\left( A\right) \) , and \( {H}_{n}\left( {X/A}\right) \) for all values of \( n \) simultaneously. In practice this is not as bad as it might sound, and in addition it has the pleasant side effect of sometimes allowing higher-dimensional homology groups to be computed in terms of lower-dimensional groups which may already be known, for example by induction.

In order to formulate the relationship we are looking for, we need an algebraic definition which is central to algebraic topology. A sequence of homomorphisms

\[
\cdots  \rightarrow  {A}_{n + 1}\xrightarrow[]{{\alpha }_{n + 1}}{A}_{n}\xrightarrow[]{{\alpha }_{n}}{A}_{n - 1} \rightarrow  \cdots
\]

is said to be exact if \( \operatorname{Ker}{\alpha }_{n} = \operatorname{Im}{\alpha }_{n + 1} \) for each \( n \) . The inclusions \( \operatorname{Im}{\alpha }_{n + 1} \subset  \operatorname{Ker}{\alpha }_{n} \) are equivalent to \( {\alpha }_{n}{\alpha }_{n + 1} = 0 \) , so the sequence is a chain complex, and the opposite inclusions \( \operatorname{Ker}{\alpha }_{n} \subset  \operatorname{Im}{\alpha }_{n + 1} \) say that the homology groups of this chain complex are trivial.

A number of basic algebraic concepts can be expressed in terms of exact sequences, for example:

(i) \( 0 \rightarrow  A\overset{\alpha }{ \rightarrow  }B \) is exact iff \( \operatorname{Ker}\alpha  = 0 \) , i.e., \( \alpha \) is injective.

(ii) \( A\overset{\alpha }{ \rightarrow  }B \rightarrow  0 \) is exact iff \( \operatorname{Im}\alpha  = B \) , i.e., \( \alpha \) is surjective.

(iii) \( 0 \rightarrow  A\overset{\alpha }{ \rightarrow  }B \rightarrow  0 \) is exact iff \( \alpha \) is an isomorphism, by (i) and (ii).

(iv) \( 0 \rightarrow  A\overset{\alpha }{ \rightarrow  }B\overset{\beta }{ \rightarrow  }C \rightarrow  0 \) is exact iff \( \alpha \) is injective, \( \beta \) is surjective, and \( \operatorname{Ker}\beta  = \; \operatorname{Im}\alpha \) , so \( \beta \) induces an isomorphism \( C \approx  B/\operatorname{Im}\alpha \) . This can be written \( C \approx  B/A \) if we think of \( \alpha \) as an inclusion of \( A \) as a subgroup of \( B \) .

An exact sequence \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) as in (iv) is called a short exact sequence.

Exact sequences provide the right tool to relate the homology groups of a space, a subspace, and the associated quotient space:

Theorem 2.13. If \( X \) is a space and \( A \) is a nonempty closed subspace that is a deformation retract of some neighborhood in \( X \) , then there is an exact sequence

\[
\cdots  \rightarrow  {\widetilde{H}}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n}\left( X\right) \overset{{j}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n}\left( {X/A}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( X\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {\widetilde{H}}_{0}\left( {X/A}\right)  \rightarrow  0
\]

where \( i \) is the inclusion \( A \hookrightarrow  X \) and \( j \) is the quotient map \( X \rightarrow  X/A \) .

The map \( \partial \) will be constructed in the course of the proof. The idea is that an element \( x \in  {\widetilde{H}}_{n}\left( {X/A}\right) \) can be represented by a chain \( \alpha \) in \( X \) with \( \partial \alpha \) a cycle in \( A \) whose homology class is \( \partial x \in  {\widetilde{H}}_{n - 1}\left( A\right) \) .

Pairs of spaces \( \left( {X, A}\right) \) satisfying the hypothesis of the theorem will be called good pairs. For example, if \( X \) is a CW complex and \( A \) is a nonempty subcomplex, then \( \left( {X, A}\right) \) is a good pair by Proposition A. 5 in the Appendix.

Corollary 2.14. \( {\widetilde{H}}_{n}\left( {S}^{n}\right)  \approx  \mathbb{Z} \) and \( {\widetilde{H}}_{i}\left( {S}^{n}\right)  = 0 \) for \( i \neq  n \) .

Proof: For \( n > 0 \) take \( \left( {X, A}\right)  = \left( {{D}^{n},{S}^{n - 1}}\right) \) so \( X/A = {S}^{n} \) . The terms \( {\widetilde{H}}_{i}\left( {D}^{n}\right) \) in the long exact sequence for this pair are zero since \( {D}^{n} \) is contractible. Exactness of the sequence then implies that the maps \( {\widetilde{H}}_{i}\left( {S}^{n}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{i - 1}\left( {S}^{n - 1}\right) \) are isomorphisms for \( i > 0 \) and that \( {\widetilde{H}}_{0}\left( {S}^{n}\right)  = 0 \) . The result now follows by induction on \( n \) , starting with the case of \( {S}^{0} \) where the result holds by Propositions 2.6 and 2.8.

As an application of this calculation we have the following classical theorem of Brouwer, the 2-dimensional case of which was proved in §1.1.

Corollary 2.15. \( \partial {D}^{n} \) is not a retract of \( {D}^{n} \) . Hence every map \( f : {D}^{n} \rightarrow  {D}^{n} \) has a fixed point.

Proof: If \( r : {D}^{n} \rightarrow  \partial {D}^{n} \) is a retraction, then \( {ri} = \mathbb{1} \) for \( i : \partial {D}^{n} \rightarrow  {D}^{n} \) the inclusion map. The composition \( {\widetilde{H}}_{n - 1}\left( {\partial {D}^{n}}\right) \overset{{i}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( {D}^{n}\right) \overset{{r}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( {\partial {D}^{n}}\right) \) is then the identity map on \( {\widetilde{H}}_{n - 1}\left( {\partial {D}^{n}}\right)  \approx  \mathbb{Z} \) . But \( {i}_{ * } \) and \( {r}_{ * } \) are both 0 since \( {\widetilde{H}}_{n - 1}\left( {D}^{n}\right)  = 0 \) , and we have a contradiction. The statement about fixed points follows as in Theorem 1.9.

The derivation of the exact sequence of homology groups for a good pair \( \left( {X, A}\right) \) will be rather a long story. We will in fact derive a more general exact sequence which holds for arbitrary pairs \( \left( {X, A}\right) \) , but with the homology groups of the quotient space \( X/A \) replaced by relative homology groups, denoted \( {H}_{n}\left( {X, A}\right) \) . These turn out to be quite useful for many other purposes as well.

## Relative Homology Groups

It sometimes happens that by ignoring a certain amount of data or structure one obtains a simpler, more flexible theory which, almost paradoxically, can give results not readily obtainable in the original setting. A familiar instance of this is arithmetic \( {\;\operatorname{mod}\;n} \) , where one ignores multiples of \( n \) . Relative homology is another example. In this case what one ignores is all singular chains in a subspace of the given space.

Relative homology groups are defined in the following way. Given a space \( X \) and a subspace \( A \subset  X \) , let \( {C}_{n}\left( {X, A}\right) \) be the quotient group \( {C}_{n}\left( X\right) /{C}_{n}\left( A\right) \) . Thus chains in \( A \) are trivial in \( {C}_{n}\left( {X, A}\right) \) . Since the boundary map \( \partial  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n - 1}\left( X\right) \) takes \( {C}_{n}\left( A\right) \) to \( {C}_{n - 1}\left( A\right) \) , it induces a quotient boundary map \( \partial  : {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n - 1}\left( {X, A}\right) \) . Letting \( n \) vary, we have a sequence of boundary maps

\[
\cdots  \rightarrow  {C}_{n}\left( {X, A}\right) \overset{\partial }{ \rightarrow  }{C}_{n - 1}\left( {X, A}\right)  \rightarrow  \cdots
\]

The relation \( {\partial }^{2} = 0 \) holds for these boundary maps since it holds before passing to quotient groups. So we have a chain complex, and the homology groups Ker \( \partial /\operatorname{Im}\partial \) of this chain complex are by definition the relative homology groups \( {H}_{n}\left( {X, A}\right) \) . By considering the definition of the relative boundary map we see:

- Elements of \( {H}_{n}\left( {X, A}\right) \) are represented by relative cycles: \( n \) -chains \( \alpha  \in  {C}_{n}\left( X\right) \) such that \( \partial \alpha  \in  {C}_{n - 1}\left( A\right) \) .

- A relative cycle \( \alpha \) is trivial in \( {H}_{n}\left( {X, A}\right) \) iff it is a relative boundary: \( \alpha  = \partial \beta  + y \) for some \( \beta  \in  {C}_{n + 1}\left( X\right) \) and \( \gamma  \in  {C}_{n}\left( A\right) \) .

These properties make precise the intuitive idea that \( {H}_{n}\left( {X, A}\right) \) is ’homology of \( X \) modulo \( {A}^{\prime } \) .

The quotient \( {C}_{n}\left( X\right) /{C}_{n}\left( A\right) \) could also be viewed as a subgroup of \( {C}_{n}\left( X\right) \) , the subgroup with basis the singular \( n \) -simplices \( \sigma  : {\Delta }^{n} \rightarrow  X \) whose image is not contained in \( A \) . However, the boundary map does not take this subgroup of \( {C}_{n}\left( X\right) \) to the corresponding subgroup of \( {C}_{n - 1}\left( X\right) \) , so it is usually better to regard \( {C}_{n}\left( {X, A}\right) \) as a quotient rather than a subgroup of \( {C}_{n}\left( X\right) \) .

Our goal now is to show that the relative homology groups \( {H}_{n}\left( {X, A}\right) \) for any pair \( \left( {X, A}\right) \) fit into a long exact sequence

\[
\cdots  \rightarrow  {H}_{n}\left( A\right)  \rightarrow  {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n - 1}\left( A\right)  \rightarrow  {H}_{n - 1}\left( X\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {H}_{0}\left( {X, A}\right)  \rightarrow  0
\]

This will be entirely a matter of algebra. To start the process, consider the diagram

![bo_d7dtv0s91nqc73eq8nv0_124_435_196_929_196_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_124_435_196_929_196_0.jpg)

where \( i \) is inclusion and \( j \) is the quotient map. The diagram is commutative by the definition of the boundary maps. Letting \( n \) vary, and drawing these short exact sequences vertically rather than horizontally, we have a large commutative diagram of the form shown at the right, where the columns are exact and the rows are chain complexes which we denote \( A \) , \( B \) , and \( C \) . Such a diagram is called a short exact sequence of chain complexes. We will show that when we pass to homology groups, this short exact sequence of chain complexes stretches out into a long exact sequence of homology groups

\[
\cdots  \rightarrow  {H}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( B\right) \overset{{j}_{ * }}{ \rightarrow  }{H}_{n}\left( C\right) \overset{\partial }{ \rightarrow  }{H}_{n - 1}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n - 1}\left( B\right)  \rightarrow  \cdots
\]

![bo_d7dtv0s91nqc73eq8nv0_124_856_504_733_460_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_124_856_504_733_460_0.jpg)

where \( {H}_{n}\left( A\right) \) denotes the homology group Ker \( \partial /\operatorname{Im}\partial \) at \( {A}_{n} \) in the chain complex \( A \) , and \( {H}_{n}\left( B\right) \) and \( {H}_{n}\left( C\right) \) are defined similarly.

The commutativity of the squares in the short exact sequence of chain complexes means that \( i \) and \( j \) are chain maps. These therefore induce maps \( {i}_{ * } \) and \( {j}_{ * } \) on homology. To define the boundary map \( \partial  : {H}_{n}\left( C\right)  \rightarrow  {H}_{n - 1}\left( A\right) \) , let \( c \in  {C}_{n} \) be a cycle. Since \( j \) is onto, \( c = j\left( b\right) \) for some \( b \in  {B}_{n} \) . The element \( \partial b \in  {B}_{n - 1} \) is in \( \operatorname{Ker}j \) since \( j\left( {\partial b}\right)  = \partial j\left( b\right)  = \partial c = 0 \) . So \( \partial b = i\left( a\right) \) for some \( a \in  {A}_{n - 1} \) since \( \operatorname{Ker}j = \operatorname{Im}i \) . Note that \( \partial a = 0 \) since \( i\left( {\partial a}\right)  = \; \partial i\left( a\right)  = \partial \partial b = 0 \) and \( i \) is injective. We define \( \partial  : {H}_{n}\left( C\right)  \rightarrow  {H}_{n - 1}\left( A\right) \) by sending the homology class of \( c \) to the homology class of \( a \) , \( \partial \left\lbrack  c\right\rbrack   = \left\lbrack  a\right\rbrack \) . This is well-defined since:

![bo_d7dtv0s91nqc73eq8nv0_124_1334_1474_246_325_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_124_1334_1474_246_325_0.jpg)

- The element \( a \) is uniquely determined by \( \partial b \) since \( i \) is injective.

- A different choice \( {b}^{\prime } \) for \( b \) would have \( j\left( {b}^{\prime }\right)  = j\left( b\right) \) , so \( {b}^{\prime } - b \) is in \( \operatorname{Ker}j = \operatorname{Im}i \) . Thus \( {b}^{\prime } - b = i\left( {a}^{\prime }\right) \) for some \( {a}^{\prime } \) , hence \( {b}^{\prime } = b + i\left( {a}^{\prime }\right) \) . The effect of replacing \( b \) by \( b + i\left( {a}^{\prime }\right) \) is to change \( a \) to the homologous element \( a + \partial {a}^{\prime } \) since \( i\left( {a + \partial {a}^{\prime }}\right)  = \; i\left( a\right)  + i\left( {\partial {a}^{\prime }}\right)  = \partial b + \partial i\left( {a}^{\prime }\right)  = \partial \left( {b + i\left( {a}^{\prime }\right) }\right) . \)

- A different choice of \( c \) within its homology class would have the form \( c + \partial {c}^{\prime } \) . Since \( {c}^{\prime } = j\left( {b}^{\prime }\right) \) for some \( {b}^{\prime } \) , we then have \( c + \partial {c}^{\prime } = c + \partial j\left( {b}^{\prime }\right)  = c + j\left( {\partial {b}^{\prime }}\right)  = \; j\left( {b + \partial {b}^{\prime }}\right) \) , so \( b \) is replaced by \( b + \partial {b}^{\prime } \) , which leaves \( \partial b \) and therefore also \( a \) unchanged.

The map \( \partial  : {H}_{n}\left( C\right)  \rightarrow  {H}_{n - 1}\left( A\right) \) is a homomorphism since if \( \partial \left\lbrack  {c}_{1}\right\rbrack   = \left\lbrack  {a}_{1}\right\rbrack \) and \( \partial \left\lbrack  {c}_{2}\right\rbrack   = \; \left\lbrack  {a}_{2}\right\rbrack \) via elements \( {b}_{1} \) and \( {b}_{2} \) as above, then \( j\left( {{b}_{1} + {b}_{2}}\right)  = j\left( {b}_{1}\right)  + j\left( {b}_{2}\right)  = {c}_{1} + {c}_{2} \) and \( i\left( {{a}_{1} + {a}_{2}}\right)  = i\left( {a}_{1}\right)  + i\left( {a}_{2}\right)  = \partial {b}_{1} + \partial {b}_{2} = \partial \left( {{b}_{1} + {b}_{2}}\right) \) , so \( \partial \left( {\left\lbrack  {c}_{1}\right\rbrack   + \left\lbrack  {c}_{2}\right\rbrack  }\right)  = \left\lbrack  {a}_{1}\right\rbrack   + \left\lbrack  {a}_{2}\right\rbrack \) .

Theorem 2.16. The sequence of homology groups

\[
\cdots  \rightarrow  {H}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( B\right) \overset{{j}_{ * }}{ \rightarrow  }{H}_{n}\left( C\right) \overset{\partial }{ \rightarrow  }{H}_{n - 1}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n - 1}\left( B\right)  \rightarrow  \cdots
\]

is exact.

Proof: There are six things to verify:

\( \operatorname{Im}{i}_{ * } \subset  \operatorname{Ker}{j}_{ * } \) . This is immediate since \( {ji} = 0 \) implies \( {j}_{ * }{i}_{ * } = 0 \) .

\( \operatorname{Im}{j}_{ * } \subset  \operatorname{Ker}\partial \) . We have \( \partial {j}_{ * } = 0 \) since in this case \( \partial b = 0 \) in the definition of \( \partial \) .

\( \operatorname{Im}\partial  \subset  \operatorname{Ker}{i}_{ * } \) . Here \( {i}_{ * }\partial  = 0 \) since \( {i}_{ * }\partial \) takes \( \left\lbrack  c\right\rbrack \) to \( \left\lbrack  {\partial b}\right\rbrack   = 0 \) .

\( \operatorname{Ker}{j}_{ * } \subset  \operatorname{Im}{i}_{ * } \) . A homology class in \( \operatorname{Ker}{j}_{ * } \) is represented by a cycle \( b \in  {B}_{n} \) with \( j\left( b\right) \) a boundary, so \( j\left( b\right)  = \partial {c}^{\prime } \) for some \( {c}^{\prime } \in  {C}_{n + 1} \) . Since \( j \) is surjective, \( {c}^{\prime } = j\left( {b}^{\prime }\right) \) for some \( {b}^{\prime } \in  {B}_{n + 1} \) . We have \( j\left( {b - \partial {b}^{\prime }}\right)  = j\left( b\right)  - j\left( {\partial {b}^{\prime }}\right)  = j\left( b\right)  - \partial j\left( {b}^{\prime }\right)  = 0 \) since \( \partial j\left( {b}^{\prime }\right)  = \partial {c}^{\prime } = j\left( b\right) \) . So \( b - \partial {b}^{\prime } = i\left( a\right) \) for some \( a \in  {A}_{n} \) . This \( a \) is a cycle since \( i\left( {\partial a}\right)  = \partial i\left( a\right)  = \partial \left( {b - \partial {b}^{\prime }}\right)  = \partial b = 0 \) and \( i \) is injective. Thus \( {i}_{ * }\left\lbrack  a\right\rbrack   = \left\lbrack  {b - \partial {b}^{\prime }}\right\rbrack   = \left\lbrack  b\right\rbrack \) , showing that \( {i}_{ * } \) maps onto \( \operatorname{Ker}{j}_{ * } \) .

Ker \( \partial  \subset  \operatorname{Im}{j}_{ * } \) . In the notation used in the definition of \( \partial \) , if \( c \) represents a homology class in Ker \( \partial \) , then \( a = \partial {a}^{\prime } \) for some \( {a}^{\prime } \in  {A}_{n} \) . The element \( b - i\left( {a}^{\prime }\right) \) is a cycle since \( \partial \left( {b - i\left( {a}^{\prime }\right) }\right)  = \partial b - \partial i\left( {a}^{\prime }\right)  = \partial b - i\left( {\partial {a}^{\prime }}\right)  = \partial b - i\left( a\right)  = 0 \) . And \( j\left( {b - i\left( {a}^{\prime }\right) }\right)  = \; j\left( b\right)  - {ji}\left( {a}^{\prime }\right)  = j\left( b\right)  = c \) , so \( {j}_{ * } \) maps \( \left\lbrack  {b - i\left( {a}^{\prime }\right) }\right\rbrack \) to \( \left\lbrack  c\right\rbrack \) .

\( \operatorname{Ker}{i}_{ * } \subset  \operatorname{Im}\partial \) . Given a cycle \( a \in  {A}_{n - 1} \) such that \( i\left( a\right)  = \partial b \) for some \( b \in  {B}_{n} \) , then \( j\left( b\right) \) is a cycle since \( \partial j\left( b\right)  = j\left( {\partial b}\right)  = {ji}\left( a\right)  = 0 \) , and \( \partial \) takes \( \left\lbrack  {j\left( b\right) }\right\rbrack \) to \( \left\lbrack  a\right\rbrack \) .

This theorem represents the beginnings of the subject of homological algebra. The method of proof is sometimes called diagram chasing.

Returning to topology, the preceding algebraic theorem yields a long exact sequence of homology groups:

\[
\cdots  \rightarrow  {H}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( X\right) \overset{{j}_{ * }}{ \rightarrow  }{H}_{n}\left( {X, A}\right) \overset{\partial }{ \rightarrow  }{H}_{n - 1}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n - 1}\left( X\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {H}_{0}\left( {X, A}\right)  \rightarrow  0
\]

The boundary map \( \partial  : {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n - 1}\left( A\right) \) has a very simple description: If a class \( \left\lbrack  \alpha \right\rbrack   \in  {H}_{n}\left( {X, A}\right) \) is represented by a relative cycle \( \alpha \) , then \( \partial \left\lbrack  \alpha \right\rbrack \) is the class of the cycle \( \partial \alpha \) in \( {H}_{n - 1}\left( A\right) \) . This is immediate from the algebraic definition of the boundary homomorphism in the long exact sequence of homology groups associated to a short exact sequence of chain complexes.

This long exact sequence makes precise the idea that the groups \( {H}_{n}\left( {X, A}\right) \) measure the difference between the groups \( {H}_{n}\left( X\right) \) and \( {H}_{n}\left( A\right) \) . In particular, exactness implies that if \( {H}_{n}\left( {X, A}\right)  = 0 \) for all \( n \) , then the inclusion \( A \hookrightarrow  X \) induces isomorphisms \( {H}_{n}\left( A\right)  \approx  {H}_{n}\left( X\right) \) for all \( n \) , by the remark (iii) following the definition of exactness. The converse is also true according to an exercise at the end of this section.

There is a completely analogous long exact sequence of reduced homology groups for a pair \( \left( {X, A}\right) \) with \( A \neq  \varnothing \) . This comes from applying the preceding algebraic machinery to the short exact sequence of chain complexes formed by the short exact sequences \( 0 \rightarrow  {C}_{n}\left( A\right)  \rightarrow  {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( {X, A}\right)  \rightarrow  0 \) in nonnegative dimensions, augmented by the short exact sequence \( 0 \rightarrow  \mathbb{Z}\overset{\mathbb{1}}{ \rightarrow  }\mathbb{Z} \rightarrow  0 \rightarrow  0 \) in dimension -1 . In particular this means that \( {\widetilde{H}}_{n}\left( {X, A}\right) \) is the same as \( {H}_{n}\left( {X, A}\right) \) for all \( n \) , when \( A \neq  \varnothing \) .

Example 2.17. In the long exact sequence of reduced homology groups for the pair \( \left( {{D}^{n},\partial {D}^{n}}\right) \) , the maps \( {H}_{i}\left( {{D}^{n},\partial {D}^{n}}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{i - 1}\left( {S}^{n - 1}\right) \) are isomorphisms for all \( i > 0 \) since the remaining terms \( {\widetilde{H}}_{i}\left( {D}^{n}\right) \) are zero for all \( i \) . Thus we obtain the calculation

\[
{H}_{i}\left( {{D}^{n},\partial {D}^{n}}\right)  \approx  \left\{  \begin{array}{ll} \mathbb{Z} & \text{ for }i = n \\  0 & \text{ otherwise } \end{array}\right.
\]

Example 2.18. Applying the long exact sequence of reduced homology groups to a pair \( \left( {X,{x}_{0}}\right) \) with \( {x}_{0} \in  X \) yields isomorphisms \( {H}_{n}\left( {X,{x}_{0}}\right)  \approx  {\widetilde{H}}_{n}\left( X\right) \) for all \( n \) since \( {\widetilde{H}}_{n}\left( {x}_{0}\right)  = 0 \) for all \( n \) .

There are induced homomorphisms for relative homology just as there are in the nonrelative, or ’absolute’, case. A map \( f : X \rightarrow  Y \) with \( f\left( A\right)  \subset  B \) , or more concisely \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) , induces homomorphisms \( {f}_{\sharp } : {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n}\left( {Y, B}\right) \) since the chain map \( {f}_{\sharp } : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( Y\right) \) takes \( {C}_{n}\left( A\right) \) to \( {C}_{n}\left( B\right) \) , so we get a well-defined map on quotients, \( {f}_{\sharp } : {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n}\left( {Y, B}\right) \) . The relation \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) holds for relative chains since it holds for absolute chains. By Proposition 2.9 we then have induced homomorphisms \( {f}_{ * } : {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {Y, B}\right) . \)

Proposition 2.19. If two maps \( f, g : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) are homotopic through maps of pairs \( \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) , then \( {f}_{ * } = {g}_{ * } : {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {Y, B}\right) \) .

Proof: The prism operator \( P \) from the proof of Theorem 2.10 takes \( {C}_{n}\left( A\right) \) to \( {C}_{n + 1}\left( B\right) \) , hence induces a relative prism operator \( P : {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n + 1}\left( {Y, B}\right) \) . Since we are just passing to quotient groups, the formula \( \partial P + P\partial  = {g}_{\sharp } - {f}_{\sharp } \) remains valid. Thus the maps \( {f}_{\sharp } \) and \( {g}_{\sharp } \) on relative chain groups are chain homotopic, and hence they induce the same homomorphism on relative homology groups.

An easy generalization of the long exact sequence of a pair \( \left( {X, A}\right) \) is the long exact sequence of a triple \( \left( {X, A, B}\right) \) , where \( B \subset  A \subset  X \) :

\[
\cdots  \rightarrow  {H}_{n}\left( {A, B}\right)  \rightarrow  {H}_{n}\left( {X, B}\right)  \rightarrow  {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n - 1}\left( {A, B}\right)  \rightarrow  \cdots
\]

This is the long exact sequence of homology groups associated to the short exact sequence of chain complexes formed by the short exact sequences

\[
0 \rightarrow  {C}_{n}\left( {A, B}\right)  \rightarrow  {C}_{n}\left( {X, B}\right)  \rightarrow  {C}_{n}\left( {X, A}\right)  \rightarrow  0
\]

For example, taking \( B \) to be a point, the long exact sequence of the triple \( \left( {X, A, B}\right) \) becomes the long exact sequence of reduced homology for the pair \( \left( {X, A}\right) \) .

## Excision

A fundamental property of relative homology groups is given by the following Excision Theorem, describing when the relative groups \( {H}_{n}\left( {X, A}\right) \) are unaffected by deleting, or excising, a subset \( Z \subset  A \) .

Theorem 2.20. Given subspaces \( Z \subset  A \subset  X \) such that the closure of \( Z \) is contained in the interior of \( A \) , then the inclusion \( \left( {X - Z, A - Z}\right)  \hookrightarrow  \left( {X, A}\right) \) induces isomorphisms \( {H}_{n}\left( {X - Z, A - Z}\right)  \rightarrow  {H}_{n}\left( {X, A}\right) \) for all \( n \) . Equivalently, for subspaces \( A, B \subset  X \) whose interiors cover \( X \) , the inclusion \( \left( {B, A \cap  B}\right)  \hookrightarrow  \left( {X, A}\right) \) induces isomorphisms \( {H}_{n}\left( {B, A \cap  B}\right)  \rightarrow  {H}_{n}\left( {X, A}\right) \) for all \( n. \)

The translation between the two versions is obtained by setting \( B = X - Z \) and \( Z = X - B \) . Then \( A \cap  B = A - Z \) and the condition \( \operatorname{cl}Z \subset  \operatorname{int}A \) is equivalent to \( X = \operatorname{int}A \cup  \operatorname{int}B \) since \( X - \operatorname{int}B = \operatorname{cl}Z \) .

![bo_d7dtv0s91nqc73eq8nv0_127_1243_790_343_241_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_127_1243_790_343_241_0.jpg)

The proof of the excision theorem will involve a rather lengthy technical detour involving a construction known as barycentric subdivision, which allows homology groups to be computed using small singular simplices. In a metric space 'smallness' can be defined in terms of diameters, but for general spaces it will be defined in terms of covers.

For a space \( X \) , let \( \mathcal{U} = \left\{  {U}_{j}\right\} \) be a collection of subspaces of \( X \) whose interiors form an open cover of \( X \) , and let \( {C}_{n}^{\mathcal{U}}\left( X\right) \) be the subgroup of \( {C}_{n}\left( X\right) \) consisting of chains \( \mathop{\sum }\limits_{i}{n}_{i}{\sigma }_{i} \) such that each \( {\sigma }_{i} \) has image contained in some set in the cover \( \mathcal{U} \) . The boundary map \( \partial  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n - 1}\left( X\right) \) takes \( {C}_{n}^{\mathcal{U}}\left( X\right) \) to \( {C}_{n - 1}^{\mathcal{U}}\left( X\right) \) , so the groups \( {C}_{n}^{\mathcal{U}}\left( X\right) \) form a chain complex. We denote the homology groups of this chain complex by \( {H}_{n}^{\mathcal{U}}\left( X\right) \) .

Proposition 2.21. The inclusion \( \iota  : {C}_{n}^{\mathcal{U}}\left( X\right)  \hookrightarrow  {C}_{n}\left( X\right) \) is a chain homotopy equivalence, that is, there is a chain map \( \rho  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}^{\mathcal{U}}\left( X\right) \) such that \( {\iota \rho } \) and \( {\rho \iota } \) are chain homotopic to the identity. Hence \( \iota \) induces isomorphisms \( {H}_{n}^{\mathcal{U}}\left( X\right)  \approx  {H}_{n}\left( X\right) \) for all \( n \) .

Proof: The barycentric subdivision process will be performed at four levels, beginning with the most geometric and becoming increasingly algebraic.

(1) Barycentric Subdivision of Simplices. The points of a simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) are the linear combinations \( \mathop{\sum }\limits_{i}{t}_{i}{v}_{i} \) with \( \mathop{\sum }\limits_{i}{t}_{i} = 1 \) and \( {t}_{i} \geq  0 \) for each \( i \) . The barycenter or ’center of gravity’ of the simplex \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) is the point \( b = \mathop{\sum }\limits_{i}{t}_{i}{v}_{i} \) whose barycentric coordinates \( {t}_{i} \) are all equal, namely \( {t}_{i} = 1/\left( {n + 1}\right) \) for each \( i \) . The barycentric subdivision of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) is the decomposition of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) into the \( n \) -simplices \( \left\lbrack  {b,{w}_{0},\cdots ,{w}_{n - 1}}\right\rbrack \) where, inductively, \( \left\lbrack  {{w}_{0},\cdots ,{w}_{n - 1}}\right\rbrack \) is an \( \left( {n - 1}\right) \) -simplex in the barycentric subdivision of a face \( \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) . The induction starts with the case \( n = 0 \) when the barycentric subdivision of \( \left\lbrack  {v}_{0}\right\rbrack \) is defined to be just \( \left\lbrack  {v}_{0}\right\rbrack \) itself. The next two cases \( n = 1,2 \) and part of the case \( n = 3 \) are shown in the figure. It follows from the inductive definition that the vertices of simplices in the barycentric subdivision of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) are exactly the barycenters of all the \( k \) -dimensional faces \( \left\lbrack  {{v}_{{i}_{0}},\cdots ,{v}_{{i}_{k}}}\right\rbrack \) of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) for \( 0 \leq  k \leq  n \) . When \( k = 0 \) this gives the original vertices \( {v}_{i} \) since the barycenter of a 0 -simplex is itself. The barycenter of \( \left\lbrack  {{v}_{{i}_{0}},\cdots ,{v}_{{i}_{k}}}\right\rbrack \) has barycentric coordinates \( {t}_{i} = 1/\left( {k + 1}\right) \) for \( i = {i}_{0},\cdots ,{i}_{k} \) and \( {t}_{i} = 0 \) otherwise.

![bo_d7dtv0s91nqc73eq8nv0_128_763_261_824_337_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_128_763_261_824_337_0.jpg)

The \( n \) -simplices of the barycentric subdivision of \( {\Delta }^{n} \) , together with all their faces, do in fact form a \( \Delta \) -complex structure on \( {\Delta }^{n} \) , indeed a simplicial complex structure, though we shall not need to know this in what follows.

A fact we will need is that the diameter of each simplex of the barycentric subdivision of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) is at most \( n/\left( {n + 1}\right) \) times the diameter of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) . Here the diameter of a simplex is by definition the maximum distance between any two of its points, and we are using the metric from the ambient Euclidean space \( {\mathbb{R}}^{m} \) containing \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) . The diameter of a simplex equals the maximum distance between any of its vertices because the distance between two points \( v \) and \( \mathop{\sum }\limits_{i}{t}_{i}{v}_{i} \) of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) satisfies the inequality

\[
\left| {v - \mathop{\sum }\limits_{i}{t}_{i}{v}_{i}}\right|  = \left| {\mathop{\sum }\limits_{i}{t}_{i}\left( {v - {v}_{i}}\right) }\right|  \leq  \mathop{\sum }\limits_{i}{t}_{i}\left| {v - {v}_{i}}\right|  \leq  \mathop{\sum }\limits_{i}{t}_{i}\mathop{\max }\limits_{j}\left| {v - {v}_{j}}\right|  = \mathop{\max }\limits_{j}\left| {v - {v}_{j}}\right|
\]

To obtain the bound \( n/\left( {n + 1}\right) \) on the ratio of diameters, we therefore need to verify that the distance between any two vertices \( {w}_{j} \) and \( {w}_{k} \) of a simplex \( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) of the barycentric subdivision of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) is at most \( n/\left( {n + 1}\right) \) times the diameter of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) . If neither \( {w}_{j} \) nor \( {w}_{k} \) is the barycenter \( b \) of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) , then these two points lie in a proper face of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) and we are done by induction on \( n \) . So we may suppose \( {w}_{j} \) , say, is the barycenter \( b \) , and then by the previous displayed inequality we may take \( {w}_{k} \) to be a vertex \( {v}_{i} \) . Let \( {b}_{i} \) be the barycenter of \( \left\lbrack  {{v}_{0},\cdots ,{\widehat{v}}_{i},\cdots ,{v}_{n}}\right\rbrack \) , with all barycentric coordinates equal to \( 1/n \) except for \( {t}_{i} = 0 \) . Then we have \( b = \frac{1}{n + 1}{v}_{i} + \frac{n}{n + 1}{b}_{i} \) . The sum of the two coefficients is 1, so \( b \) lies on the line segment \( \left\lbrack  {{v}_{i},{b}_{i}}\right\rbrack \) from \( {v}_{i} \) to \( {b}_{i} \) , and the distance from \( b \) to \( {v}_{i} \) is \( n/\left( {n + 1}\right) \) times the length of \( \left\lbrack  {{v}_{i},{b}_{i}}\right\rbrack \) . Hence the distance from \( b \) to \( {v}_{i} \) is bounded by \( n/\left( {n + 1}\right) \) times the diameter of \( \left\lbrack  {{v}_{0},\cdots ,{v}_{n}}\right\rbrack \) .

![bo_d7dtv0s91nqc73eq8nv0_128_1121_1863_468_191_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_128_1121_1863_468_191_0.jpg)

The significance of the factor \( n/\left( {n + 1}\right) \) is that by repeated barycentric subdivision we can produce simplices of arbitrarily small diameter since \( {\left( n/\left( n + 1\right) \right) }^{r} \) approaches 0 as \( r \) goes to infinity. It is important that the bound \( n/\left( {n + 1}\right) \) does not depend on the shape of the simplex since repeated barycentric subdivision produces simplices of many different shapes.

(2) Barycentric Subdivision of Linear Chains. The main part of the proof will be to construct a subdivision operator \( S : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( X\right) \) and show this is chain homotopic to the identity map. First we will construct \( S \) and the chain homotopy in a more restricted linear setting.

For a convex set \( Y \) in some Euclidean space, the linear maps \( {\Delta }^{n} \rightarrow  Y \) generate a subgroup of \( {C}_{n}\left( Y\right) \) that we denote \( L{C}_{n}\left( Y\right) \) , the linear chains. The boundary map \( \partial  : {C}_{n}\left( Y\right)  \rightarrow  {C}_{n - 1}\left( Y\right) \) takes \( L{C}_{n}\left( Y\right) \) to \( L{C}_{n - 1}\left( Y\right) \) , so the linear chains form a subcom-plex of the singular chain complex of \( Y \) . We can uniquely designate a linear map \( \lambda  : {\Delta }^{n} \rightarrow  Y \) by \( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) where \( {w}_{i} \) is the image under \( \lambda \) of the \( {i}^{th} \) vertex of \( {\Delta }^{n} \) . To avoid having to make exceptions for 0-simplices it will be convenient to augment the complex \( {LC}\left( Y\right) \) by setting \( L{C}_{-1}\left( Y\right)  = \mathbb{Z} \) generated by the empty simplex \( \left\lbrack  \varnothing \right\rbrack \) , with \( \partial \left\lbrack  {w}_{0}\right\rbrack   = \left\lbrack  \varnothing \right\rbrack \) for all 0 -simplices \( \left\lbrack  {w}_{0}\right\rbrack \) .

Each point \( b \in  Y \) determines a homomorphism \( b : L{C}_{n}\left( Y\right)  \rightarrow  L{C}_{n + 1}\left( Y\right) \) defined on basis elements by \( b\left( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack  \right)  = \left\lbrack  {b,{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) . Geometrically, the homomorphism \( b \) can be regarded as a cone operator, sending a linear chain to the cone having the linear chain as the base of the cone and the point \( b \) as the tip of the cone. Applying the usual formula for \( \partial \) , we obtain the relation \( \partial b\left( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack  \right)  = \; \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack   - b\left( {\partial \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack  }\right) \) . By linearity it follows that \( \partial b\left( \alpha \right)  = \alpha  - b\left( {\partial \alpha }\right) \) for all \( \alpha  \in  L{C}_{n}\left( Y\right) \) . This expresses algebraically the geometric fact that the boundary of a cone consists of its base together with the cone on the boundary of its base. The relation \( \partial b\left( \alpha \right)  = \alpha  - b\left( {\partial \alpha }\right) \) can be rewritten as \( \partial b + b\partial  = \mathbb{1} \) , so \( b \) is a chain homotopy between the identity map and the zero map on the augmented chain complex \( {LC}\left( Y\right) \) .

Now we define a subdivision homomorphism \( S : L{C}_{n}\left( Y\right)  \rightarrow  L{C}_{n}\left( Y\right) \) by induction on \( n \) . Let \( \lambda  : {\Delta }^{n} \rightarrow  Y \) be a generator of \( L{C}_{n}\left( Y\right) \) and let \( {b}_{\lambda } \) be the image of the barycenter of \( {\Delta }^{n} \) under \( \lambda \) . Then the inductive formula for \( S \) is \( S\left( \lambda \right)  = {b}_{\lambda }\left( {S\partial \lambda }\right) \) where \( {b}_{\lambda } : L{C}_{n - 1}\left( Y\right)  \rightarrow  L{C}_{n}\left( Y\right) \) is the cone operator defined in the preceding paragraph. The induction starts with \( S\left( \left\lbrack  \varnothing \right\rbrack  \right)  = \left\lbrack  \varnothing \right\rbrack \) , so \( S \) is the identity on \( L{C}_{-1}\left( Y\right) \) . It is also the identity on \( L{C}_{0}\left( Y\right) \) , since when \( n = 0 \) the formula for \( S \) becomes \( S\left( \left\lbrack  {w}_{0}\right\rbrack  \right)  = {w}_{0}\left( {S\partial \left\lbrack  {w}_{0}\right\rbrack  }\right)  = {w}_{0}\left( {S\left( \left\lbrack  \varnothing \right\rbrack  \right) }\right)  = {w}_{0}\left( \left\lbrack  \varnothing \right\rbrack  \right)  = \left\lbrack  {w}_{0}\right\rbrack \) . When \( \lambda \) is an embedding, with image a genuine \( n \) -simplex \( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) , then \( S\left( \lambda \right) \) is the sum of the \( n \) -simplices in the barycentric subdivision of \( \left\lbrack  {{w}_{0},\cdots ,{w}_{n}}\right\rbrack \) , with certain signs that could be computed explicitly. This is apparent by comparing the inductive definition of \( S \) with the inductive definition of the barycentric subdivision of a simplex.

Let us check that the maps \( S \) satisfy \( \partial S = S\partial \) , and hence give a chain map from the chain complex \( {LC}\left( Y\right) \) to itself. Since \( S = \mathbb{1} \) on \( L{C}_{0}\left( Y\right) \) and \( L{C}_{-1}\left( Y\right) \) , we certainly have \( \partial S = S\partial \) on \( L{C}_{0}\left( Y\right) \) . The result for larger \( n \) is given by the following calculation, in which we omit some parentheses to unclutter the formulas:

\[
\partial {S\lambda } = \partial {b}_{\lambda }\left( {S\partial \lambda }\right)
\]

\[
= S\partial \lambda  - {b}_{\lambda }\partial \left( {S\partial \lambda }\right) \;\text{ since }\partial {b}_{\lambda } = \mathbb{1} - {b}_{\lambda }\partial
\]

\[
= S\partial \lambda  - {b}_{\lambda }S\left( {\partial \partial \lambda }\right) \;\text{ since }\partial S\left( {\partial \lambda }\right)  = S\partial \left( {\partial \lambda }\right) \text{ by induction on }n
\]

\[
= S\partial \lambda \;\text{ since }\partial \partial  = 0
\]

We next build a chain homotopy \( T : L{C}_{n}\left( Y\right)  \rightarrow  L{C}_{n + 1}\left( Y\right) \) between \( S \) and the identity, fitting into a diagram

![bo_d7dtv0s91nqc73eq8nv0_130_255_556_1287_185_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_130_255_556_1287_185_0.jpg)

We define \( T \) on \( L{C}_{n}\left( Y\right) \) inductively by setting \( T = 0 \) for \( n =  - 1 \) and letting \( {T\lambda } = \; {b}_{\lambda }\left( {\lambda  - T\partial \lambda }\right) \) for \( n \geq  0 \) . The geometric motivation for this formula is an inductively defined subdivision of \( {\Delta }^{n} \times  I \) obtained by joining all simplices in \( {\Delta }^{n} \times  \{ 0\}  \cup  \partial {\Delta }^{n} \times  I \) to the barycenter of \( {\Delta }^{n} \times  \{ 1\} \) , as indicated in the figure in the case \( n = 2 \) . What \( T \) actually does is take the image of this subdivision under the projection \( {\Delta }^{n} \times  I \rightarrow  {\Delta }^{n} \) .

![bo_d7dtv0s91nqc73eq8nv0_130_937_853_642_266_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_130_937_853_642_266_0.jpg)

The chain homotopy formula \( \partial T + T\partial  = \mathbb{1} - S \) is trivial on \( L{C}_{-1}\left( Y\right) \) where \( T = 0 \) and \( S = \mathbb{1} \) . Verifying the formula on \( L{C}_{n}\left( Y\right) \) with \( n \geq  0 \) is done by the calculation

\[
\partial {T\lambda } = \partial {b}_{\lambda }\left( {\lambda  - T\partial \lambda }\right)
\]

\[
= \lambda  - T\partial \lambda  - {b}_{\lambda }\partial \left( {\lambda  - T\partial \lambda }\right) \;\text{ since }\partial {b}_{\lambda } = \mathbb{1} - {b}_{\lambda }\partial
\]

\[
= \lambda  - T\partial \lambda  - {b}_{\lambda }\left\lbrack  {\partial \lambda  - \partial T\left( {\partial \lambda }\right) }\right\rbrack
\]

\[
= \lambda  - T\partial \lambda  - {b}_{\lambda }\left\lbrack  {S\left( {\partial \lambda }\right)  + T\partial \left( {\partial \lambda }\right) }\right\rbrack  \;\text{ by induction on }n
\]

\[
= \lambda  - T\partial \lambda  - {S\lambda }\;\text{ since }\partial \partial  = 0\text{ and }{S\lambda } = {b}_{\lambda }\left( {S\partial \lambda }\right)
\]

Now we can discard the group \( L{C}_{-1}\left( Y\right) \) and the relation \( \partial T + T\partial  = \mathbb{1} - S \) still holds since \( T \) was zero on \( L{C}_{-1}\left( Y\right) \) .

(3) Barycentric Subdivision of General Chains. Define \( S : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( X\right) \) by setting \( {S\sigma } = {\sigma }_{\sharp }S{\Delta }^{n} \) for a singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) . Since \( S{\Delta }^{n} \) is the sum of the \( n \) -simplices in the barycentric subdivision of \( {\Delta }^{n} \) , with certain signs, \( {S\sigma } \) is the corresponding signed sum of the restrictions of \( \sigma \) to the \( n \) -simplices of the barycentric subdivision of \( {\Delta }^{n} \) . The operator \( S \) is a chain map since

\[
\partial {S\sigma } = \partial {\sigma }_{\sharp }S{\Delta }^{n} = {\sigma }_{\sharp }\partial S{\Delta }^{n} = {\sigma }_{\sharp }S\partial {\Delta }^{n}
\]

\[
= {\sigma }_{\sharp }S\left( {\mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\Delta }_{i}^{n}}\right) \;\text{ where }{\Delta }_{i}^{n}\text{ is the }{i}^{th}\text{ face of }{\Delta }^{n}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\sigma }_{\sharp }S{\Delta }_{i}^{n}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}S\left( {\sigma  \mid  {\Delta }_{i}^{n}}\right)
\]

\[
= S\left( {\mathop{\sum }\limits_{i}{\left( -1\right) }^{i}\sigma  \mid  {\Delta }_{i}^{n}}\right)  = S\left( {\partial \sigma }\right)
\]

In similar fashion we define \( T : {C}_{n}\left( X\right)  \rightarrow  {C}_{n + 1}\left( X\right) \) by \( {T\sigma } = {\sigma }_{\sharp }T{\Delta }^{n} \) , and this gives a chain homotopy between \( S \) and the identity, since the formula \( \partial T + T\partial  = \mathbb{1} - S \) holds by the calculation

\[
\partial {T\sigma } = \partial {\sigma }_{\sharp }T{\Delta }^{n} = {\sigma }_{\sharp }\partial T{\Delta }^{n} = {\sigma }_{\sharp }\left( {{\Delta }^{n} - S{\Delta }^{n} - T\partial {\Delta }^{n}}\right)  = \sigma  - {S\sigma } - {\sigma }_{\sharp }T\partial {\Delta }^{n}
\]

\[
= \sigma  - {S\sigma } - T\left( {\partial \sigma }\right)
\]

where the last equality follows just as in the previous displayed calculation, with \( S \) replaced by \( T \) .

(4) Iterated Barycentric Subdivision. A chain homotopy between 11 and the iterate \( {S}^{m} \) is given by the operator \( {D}_{m} = \mathop{\sum }\limits_{{0 \leq  i < m}}T{S}^{i} \) since

\[
\partial {D}_{m} + {D}_{m}\partial  = \mathop{\sum }\limits_{{0 \leq  i < m}}\left( {\partial T{S}^{i} + T{S}^{i}\partial }\right)  = \mathop{\sum }\limits_{{0 \leq  i < m}}\left( {\partial T{S}^{i} + T\partial {S}^{i}}\right)  =
\]

\[
\mathop{\sum }\limits_{{0 \leq  i < m}}\left( {\partial T + T\partial }\right) {S}^{i} = \mathop{\sum }\limits_{{0 \leq  i < m}}\left( {\mathbb{1} - S}\right) {S}^{i} = \mathop{\sum }\limits_{{0 \leq  i < m}}\left( {{S}^{i} - {S}^{i + 1}}\right)  = \mathbb{1} - {S}^{m}
\]

For each singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) there exists an \( m \) such that \( {S}^{m}\left( \sigma \right) \) lies in \( {C}_{n}^{\mathcal{U}}\left( X\right) \) since the diameter of the simplices of \( {S}^{m}\left( {\Delta }^{n}\right) \) will be less than a Lebesgue number of the cover of \( {\Delta }^{n} \) by the open sets \( {\sigma }^{-1}\left( {\operatorname{int}{U}_{j}}\right) \) if \( m \) is large enough. (Recall that a Lebesgue number for an open cover of a compact metric space is a number \( \varepsilon  > 0 \) such that every set of diameter less than \( \varepsilon \) lies in some set of the cover; such a number exists by an elementary compactness argument.) We cannot expect the same number \( m \) to work for all \( \sigma \) ’s, so let us define \( m\left( \sigma \right) \) to be the smallest \( m \) such that \( {S}^{m}\sigma \) is in \( {C}_{n}^{u}\left( X\right) \) .

We now define \( D : {C}_{n}\left( X\right)  \rightarrow  {C}_{n + 1}\left( X\right) \) by setting \( {D\sigma } = {D}_{m\left( \sigma \right) }\sigma \) for each singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) . For this \( D \) we would like to find a chain map \( \rho  : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( X\right) \) with image in \( {C}_{n}^{\mathcal{U}}\left( X\right) \) satisfying the chain homotopy equation

(*)

\[
\partial D + D\partial  = \mathbb{1} - \rho
\]

A quick way to do this is simply to regard this equation as defining \( \rho \) , so we let \( \rho  = \mathbb{1} - \partial D - D\partial \) . It follows easily that \( \rho \) is a chain map since

\[
\partial \rho \left( \sigma \right)  = \partial \sigma  - {\partial }^{2}{D\sigma } - \partial D\partial \sigma  = \partial \sigma  - \partial D\partial \sigma
\]

\[
\text{ and }\rho \left( {\partial \sigma }\right)  = \partial \sigma  - \partial D\partial \sigma  - D{\partial }^{2}\sigma  = \partial \sigma  - \partial D\partial \sigma
\]

To check that \( \rho \) takes \( {C}_{n}\left( X\right) \) to \( {C}_{n}^{\mathcal{U}}\left( X\right) \) we compute \( \rho \left( \sigma \right) \) more explicitly:

\[
\rho \left( \sigma \right)  = \sigma  - \partial {D\sigma } - D\left( {\partial \sigma }\right)
\]

\[
= \sigma  - \partial {D}_{m\left( \sigma \right) }\sigma  - D\left( {\partial \sigma }\right)
\]

\[
= {S}^{m\left( \sigma \right) }\sigma  + {D}_{m\left( \sigma \right) }\left( {\partial \sigma }\right)  - D\left( {\partial \sigma }\right) \;\text{ since }\;\partial {D}_{m} + {D}_{m}\partial  = \mathbb{1} - {S}^{m}
\]

The term \( {S}^{m\left( \sigma \right) }\sigma \) lies in \( {C}_{n}^{\mathfrak{U}}\left( X\right) \) by the definition of \( m\left( \sigma \right) \) . The remaining terms \( {D}_{m\left( \sigma \right) }\left( {\partial \sigma }\right)  - D\left( {\partial \sigma }\right) \) are linear combinations of terms \( {D}_{m\left( \sigma \right) }\left( {\sigma }_{j}\right)  - {D}_{m\left( {\sigma }_{j}\right) }\left( {\sigma }_{j}\right) \) for \( {\sigma }_{j} \) the restriction of \( \sigma \) to a face of \( {\Delta }^{n} \) , so \( m\left( {\sigma }_{j}\right)  \leq  m\left( \sigma \right) \) and hence the difference \( {D}_{m\left( \sigma \right) }\left( {\sigma }_{j}\right)  - {D}_{m\left( {\sigma }_{j}\right) }\left( {\sigma }_{j}\right) \) consists of terms \( T{S}^{i}\left( {\sigma }_{j}\right) \) with \( i \geq  m\left( {\sigma }_{j}\right) \) , and these terms lie in \( {C}_{n}^{\mathcal{U}}\left( X\right) \) since \( T \) takes \( {C}_{n - 1}^{\mathcal{U}}\left( X\right) \) to \( {C}_{n}^{\mathcal{U}}\left( X\right) \) .

Viewing \( \rho \) as a chain map \( {C}_{n}\left( X\right)  \rightarrow  {C}_{n}^{\mathcal{U}}\left( X\right) \) , the equation \( \left( *\right) \) says that \( \partial D + D\partial  = \; \mathbb{1} - \imath \rho \) for \( \iota  : {C}_{n}^{\mathcal{U}}\left( X\right)  \hookrightarrow  {C}_{n}\left( X\right) \) the inclusion. Furthermore, \( {\rho \iota } = \mathbb{1} \) since \( D \) is identically zero on \( {C}_{n}^{\mathcal{U}}\left( X\right) \) , as \( m\left( \sigma \right)  = 0 \) if \( \sigma \) is in \( {C}_{n}^{\mathcal{U}}\left( X\right) \) , hence the summation defining \( {D\sigma } \) is empty. Thus we have shown that \( \rho \) is a chain homotopy inverse for \( \iota \) .

Proof of the Excision Theorem: We prove the second version, involving a decomposition \( X = A \cup  B \) . For the cover \( \mathcal{U} = \{ A, B\} \) we introduce the suggestive notation \( {C}_{n}\left( {A + B}\right) \) for \( {C}_{n}^{\mathcal{U}}\left( X\right) \) , the sums of chains in \( A \) and chains in \( B \) . At the end of the preceding proof we had formulas \( \partial D + D\partial  = \mathbb{1} - {\iota \rho } \) and \( {\rho \iota } = \mathbb{1} \) . All the maps appearing in these formulas take chains in \( A \) to chains in \( A \) , so they induce quotient maps when we factor out chains in \( A \) . These quotient maps automatically satisfy the same two formulas, so the inclusion \( {C}_{n}\left( {A + B}\right) /{C}_{n}\left( A\right)  \hookrightarrow  {C}_{n}\left( X\right) /{C}_{n}\left( A\right) \) induces an isomorphism on homology. The map \( {C}_{n}\left( B\right) /{C}_{n}\left( {A \cap  B}\right)  \rightarrow  {C}_{n}\left( {A + B}\right) /{C}_{n}\left( A\right) \) induced by inclusion is obviously an isomorphism since both quotient groups are free with basis the singular \( n \) -simplices in \( B \) that do not lie in \( A \) . Hence we obtain the desired isomorphism \( {H}_{n}\left( {B, A \cap  B}\right)  \approx  {H}_{n}\left( {X, A}\right) \) induced by inclusion.

All that remains in the proof of Theorem 2.13 is to replace relative homology groups with absolute homology groups. This is achieved by the following result.

Proposition 2.22. For good pairs \( \left( {X, A}\right) \) , the quotient map \( q : \left( {X, A}\right)  \rightarrow  \left( {X/A, A/A}\right) \) induces isomorphisms \( {q}_{ * } : {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {X/A, A/A}\right)  \approx  {\widetilde{H}}_{n}\left( {X/A}\right) \) for all \( n \) .

Proof: Let \( V \) be a neighborhood of \( A \) in \( X \) that deformation retracts onto \( A \) . We have a commutative diagram

\[
{H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {X, V}\right)  \leftarrow  {H}_{n}\left( {X - A, V - A}\right)
\]

\[
{q}_{ * }\;{q}_{ * }\;{q}_{ * }\;{q}_{ * }
\]

\[
{H}_{n}\left( {X/A, A/A}\right)  \rightarrow  {H}_{n}\left( {X/A, V/A}\right)  \leftarrow  {H}_{n}\left( {X/A - A/A, V/A - A/A}\right)
\]

The upper left horizontal map is an isomorphism since in the long exact sequence of the triple \( \left( {X, V, A}\right) \) the groups \( {H}_{n}\left( {V, A}\right) \) are zero for all \( n \) , because a deformation retraction of \( V \) onto \( A \) gives a homotopy equivalence of pairs \( \left( {V, A}\right)  \simeq  \left( {A, A}\right) \) , and \( {H}_{n}\left( {A, A}\right)  = 0 \) . The deformation retraction of \( V \) onto \( A \) induces a deformation retraction of \( V/A \) onto \( A/A \) , so the same argument shows that the lower left horizontal map is an isomorphism as well. The other two horizontal maps are isomorphisms directly from excision. The right-hand vertical map \( {q}_{ * } \) is an isomorphism since \( q \) restricts to a homeomorphism on the complement of \( A \) . From the commutativity of the diagram it follows that the left-hand \( {q}_{ * } \) is an isomorphism.

This proposition shows that relative homology can be expressed as reduced absolute homology in the case of good pairs \( \left( {X, A}\right) \) , but in fact there is a way of doing this for arbitrary pairs. Consider the space \( X \cup  {CA} \) where \( {CA} \) is the cone \( \left( {A \times  I}\right) /\left( {A\times \{ 0\} }\right) \) whose base \( A \times  \{ 1\} \) we identify with \( A \subset  X \) . Using terminology introduced in Chapter \( 0, X \cup  {CA} \) can also be described as the mapping cone of the inclusion \( A \hookrightarrow  X \) . The assertion is that \( {H}_{n}\left( {X, A}\right) \) is isomorphic to \( {\widetilde{H}}_{n}\left( {X \cup  {CA}}\right) \) for all \( n \) via the sequence of isomorphisms

\[
{\widetilde{H}}_{n}\left( {X \cup  {CA}}\right)  \approx  {H}_{n}\left( {X \cup  {CA},{CA}}\right)  \approx  {H}_{n}\left( {X \cup  {CA}-\{ p\} ,{CA}-\{ p\} }\right)  \approx  {H}_{n}\left( {X, A}\right)
\]

![bo_d7dtv0s91nqc73eq8nv0_133_1304_204_281_213_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_133_1304_204_281_213_0.jpg)

where \( p \in  {CA} \) is the tip of the cone. The first isomorphism comes from the exact sequence of the pair, using the fact that \( {CA} \) is contractible. The second isomorphism is excision, and the third comes from a deformation retraction of \( {CA} - \{ p\} \) onto \( A \) .

Here is an application of the preceding proposition:

Example 2.23. Let us find explicit cycles representing generators of the infinite cyclic groups \( {H}_{n}\left( {{D}^{n},\partial {D}^{n}}\right) \) and \( {\widetilde{H}}_{n}\left( {S}^{n}\right) \) . Replacing \( \left( {{D}^{n},\partial {D}^{n}}\right) \) by the equivalent pair \( \left( {{\Delta }^{n},\partial {\Delta }^{n}}\right) \) , we will show by induction on \( n \) that the identity map \( {i}_{n} : {\Delta }^{n} \rightarrow  {\Delta }^{n} \) , viewed as a singular \( n \) -simplex, is a cycle generating \( {H}_{n}\left( {{\Delta }^{n},\partial {\Delta }^{n}}\right) \) . That it is a cycle is clear since we are considering relative homology. When \( n = 0 \) it certainly represents a generator. For the induction step, let \( \Lambda  \subset  {\Delta }^{n} \) be the union of all but one of the \( \left( {n - 1}\right) \) -dimensional faces of \( {\Delta }^{n} \) . Then we claim there are isomorphisms

\[
{H}_{n}\left( {{\Delta }^{n},\partial {\Delta }^{n}}\right) \overset{ \approx  }{ \rightarrow  }{H}_{n - 1}\left( {\partial {\Delta }^{n},\Lambda }\right) \overset{ \approx  }{ \leftarrow  }{H}_{n - 1}\left( {{\Delta }^{n - 1},\partial {\Delta }^{n - 1}}\right)
\]

The first isomorphism is a boundary map in the long exact sequence of the triple \( \left( {{\Delta }^{n},\partial {\Delta }^{n},\Lambda }\right) \) , whose third terms \( {H}_{i}\left( {{\Delta }^{n},\Lambda }\right) \) are zero since \( {\Delta }^{n} \) deformation retracts onto \( \Lambda \) , hence \( \left( {{\Delta }^{n},\Lambda }\right)  \simeq  \left( {\Lambda ,\Lambda }\right) \) . The second isomorphism is induced by the inclusion \( i : {\Delta }^{n - 1} \rightarrow  \partial {\Delta }^{n} \) as the face not contained in \( \Lambda \) . When \( n = 1, i \) induces an isomorphism on relative homology since this is true already at the chain level. When \( n > 1,\partial {\Delta }^{n - 1} \) is nonempty so we are dealing with good pairs and \( i \) induces a homeomorphism of quotients \( {\Delta }^{n - 1}/\partial {\Delta }^{n - 1} \approx  \partial {\Delta }^{n}/\Lambda \) . The induction step then follows since the cycle \( {i}_{n} \) is sent under the first isomorphism to the cycle \( \partial {i}_{n} \) which equals \( \pm  {i}_{n - 1} \) in \( {C}_{n - 1}\left( {\partial {\Delta }^{n},\Lambda }\right) \) .

To find a cycle generating \( {\widetilde{H}}_{n}\left( {S}^{n}\right) \) let us regard \( {S}^{n} \) as two \( n \) -simplices \( {\Delta }_{1}^{n} \) and \( {\Delta }_{2}^{n} \) with their boundaries identified in the obvious way, preserving the ordering of vertices. The difference \( {\Delta }_{1}^{n} - {\Delta }_{2}^{n} \) , viewed as a singular \( n \) -chain, is then a cycle, and we claim it represents a generator of \( {\widetilde{H}}_{n}\left( {S}^{n}\right) \) . To see this, consider the isomorphisms

\[
{\widetilde{H}}_{n}\left( {S}^{n}\right)  \rightarrow  {H}_{n}\left( {{S}^{n},{\Delta }_{2}^{n}}\right)  \leftarrow  {H}_{n}\left( {{\Delta }_{1}^{n},\partial {\Delta }_{1}^{n}}\right)
\]

where the first isomorphism comes from the long exact sequence of the pair \( \left( {{S}^{n},{\Delta }_{2}^{n}}\right) \) and the second isomorphism is justified in the nontrivial cases \( n > 0 \) by passing to quotients as before. Under these isomorphisms the cycle \( {\Delta }_{1}^{n} - {\Delta }_{2}^{n} \) in the first group corresponds to the cycle \( {\Delta }_{1}^{n} \) in the third group, which represents a generator of this group as we have seen, so \( {\Delta }_{1}^{n} - {\Delta }_{2}^{n} \) represents a generator of \( {\widetilde{H}}_{n}\left( {S}^{n}\right) \) .

The preceding proposition implies that the excision property holds also for sub-complexes of CW complexes:

Corollary 2.24. If the CW complex \( X \) is the union of subcomplexes \( A \) and \( B \) , then the inclusion \( \left( {B, A \cap  B}\right)  \hookrightarrow  \left( {X, A}\right) \) induces isomorphisms \( {H}_{n}\left( {B, A \cap  B}\right)  \rightarrow  {H}_{n}\left( {X, A}\right) \) for all \( n \) .

Proof: Since CW pairs are good, Proposition 2.22 allows us to pass to the quotient spaces \( B/\left( {A \cap  B}\right) \) and \( X/A \) which are homeomorphic, assuming we are not in the trivial case \( A \cap  B = \varnothing \) .

Here is another application of the preceding proposition:

Corollary 2.25. For a wedge sum \( \mathop{\bigvee }\limits_{\alpha }{X}_{\alpha } \) , the inclusions \( {i}_{\alpha } : {X}_{\alpha } \hookrightarrow  \mathop{\bigvee }\limits_{\alpha }{X}_{\alpha } \) induce an isomorphism \( { \oplus  }_{\alpha }{i}_{\alpha  * } : { \oplus  }_{\alpha }{\widetilde{H}}_{n}\left( {X}_{\alpha }\right)  \rightarrow  {\widetilde{H}}_{n}\left( {\mathop{\bigvee }\limits_{\alpha }{X}_{\alpha }}\right) \) , provided that the wedge sum is formed at basepoints \( {x}_{\alpha } \in  {X}_{\alpha } \) such that the pairs \( \left( {{X}_{\alpha },{x}_{\alpha }}\right) \) are good.

Proof: Since reduced homology is the same as homology relative to a basepoint, this follows from the proposition by taking \( \left( {X, A}\right)  = \left( {\mathop{\coprod }\limits_{\alpha }{X}_{\alpha },\mathop{\coprod }\limits_{\alpha }\left\{  {x}_{\alpha }\right\}  }\right) \) .

Here is an application of the machinery we have developed, a classical result of Brouwer from around 1910 known as 'invariance of dimension', which says in particular that \( {\mathbb{R}}^{m} \) is not homeomorphic to \( {\mathbb{R}}^{n} \) if \( m \neq  n \) .

Theorem 2.26. If nonempty open sets \( U \subset  {\mathbb{R}}^{m} \) and \( V \subset  {\mathbb{R}}^{n} \) are homeomorphic, then \( m = n \) .

Proof: For \( x \in  U \) we have \( {H}_{k}\left( {U, U-\{ x\} }\right)  \approx  {H}_{k}\left( {{\mathbb{R}}^{m},{\mathbb{R}}^{m}-\{ x\} }\right) \) by excision. From the long exact sequence for the pair \( \left( {{\mathbb{R}}^{m},{\mathbb{R}}^{m}-\{ x\} }\right) \) we get \( {H}_{k}\left( {{\mathbb{R}}^{m},{\mathbb{R}}^{m}-\{ x\} }\right)  \approx \; {\widetilde{H}}_{k - 1}\left( {{\mathbb{R}}^{m}-\{ x\} }\right) \) . Since \( {\mathbb{R}}^{m} - \{ x\} \) deformation retracts onto a sphere \( {S}^{m - 1} \) , we conclude that \( {H}_{k}\left( {U, U-\{ x\} }\right) \) is \( \mathbb{Z} \) for \( k = m \) and 0 otherwise. By the same reasoning, \( {H}_{k}\left( {V, V-\{ y\} }\right) \) is \( \mathbb{Z} \) for \( k = n \) and 0 otherwise. Since a homeomorphism \( h : U \rightarrow  V \) induces isomorphisms \( {H}_{k}\left( {U, U-\{ x\} }\right)  \rightarrow  {H}_{k}\left( {V, V-\{ h\left( x\right) \} }\right) \) for all \( k \) , we must have \( m = n \) .

Generalizing the idea of this proof, the local homology groups of a space \( X \) at a point \( x \in  X \) are defined to be the groups \( {H}_{n}\left( {X, X-\{ x\} }\right) \) . For any open neighborhood \( U \) of \( x \) , excision gives isomorphisms \( {H}_{n}\left( {X, X-\{ x\} }\right)  \approx  {H}_{n}\left( {U, U-\{ x\} }\right) \) assuming points are closed in \( X \) , and thus the groups \( {H}_{n}\left( {X, X-\{ x\} }\right) \) depend only on the local topology of \( X \) near \( x \) . A homeomorphism \( f : X \rightarrow  Y \) must induce isomorphisms \( {H}_{n}\left( {X, X-\{ x\} }\right)  \approx  {H}_{n}\left( {Y, Y-\{ f\left( x\right) \} }\right) \) for all \( x \) and \( n \) , so the local homology groups can be used to tell when spaces are not locally homeomorphic at certain points, as in the preceding proof. The exercises give some further examples of this.

## Naturality

The exact sequences we have been constructing have an extra property that will become important later at key points in many arguments, though at first glance this property may seem just an idle technicality, not very interesting. We shall discuss the property now rather than interrupting later arguments to check it when it is needed, but the reader may prefer to postpone a careful reading of this discussion.

The property is called naturality. For example, to say that the long exact sequence of a pair is natural means that for a map \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) , the diagram

\[
\cdots  \rightarrow  {H}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{H}_{n}\left( X\right) \overset{{j}_{ * }}{ \rightarrow  }{H}_{n}\left( {X, A}\right) \overset{\partial }{ \rightarrow  }{H}_{n - 1}\left( A\right)  \rightarrow  \cdots
\]

is commutative. Commutativity of the squares involving \( {i}_{ * } \) and \( {j}_{ * } \) follows from the obvious commutativity of the corresponding squares of chain groups, with \( {C}_{n} \) in place of \( {H}_{n} \) . For the other square, when we defined induced homomorphisms we saw that \( {f}_{\sharp }\partial  = \partial {f}_{\sharp } \) at the chain level. Then for a class \( \left\lbrack  \alpha \right\rbrack   \in  {H}_{n}\left( {X, A}\right) \) represented by a relative cycle \( \alpha \) , we have \( {f}_{ * }\partial \left\lbrack  \alpha \right\rbrack   = {f}_{ * }\left\lbrack  {\partial \alpha }\right\rbrack   = \left\lbrack  {{f}_{\sharp }\partial \alpha }\right\rbrack   = \left\lbrack  {\partial {f}_{\sharp }\alpha }\right\rbrack   = \partial \left\lbrack  {{f}_{\sharp }\alpha }\right\rbrack   = \partial {f}_{ * }\left\lbrack  \alpha \right\rbrack \) .

Alternatively, we could appeal to the general algebraic fact that the long exact sequence of homology groups associated to a short exact sequence of chain complexes is natural: For a commutative diagram of short exact sequences of chain complexes

![bo_d7dtv0s91nqc73eq8nv0_135_285_1228_1221_537_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_135_285_1228_1221_537_0.jpg)

the induced diagram

![bo_d7dtv0s91nqc73eq8nv0_135_320_1824_1161_185_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_135_320_1824_1161_185_0.jpg)

is commutative. Commutativity of the first two squares is obvious since \( {\beta i} = {i}^{\prime }\alpha \) implies \( {\beta }_{ * }{i}_{ * } = {i}_{ * }^{\prime }{\alpha }_{ * } \) and \( {\gamma j} = {j}^{\prime }\beta \) implies \( {\gamma }_{ * }{j}_{ * } = {j}_{ * }^{\prime }{\beta }_{ * } \) . For the third square, recall that the map \( \partial  : {H}_{n}\left( C\right)  \rightarrow  {H}_{n - 1}\left( A\right) \) was defined by \( \partial \left\lbrack  c\right\rbrack   = \left\lbrack  a\right\rbrack \) where \( c = j\left( b\right) \) and \( i\left( a\right)  = \partial b \) . Then \( \partial \left\lbrack  {y\left( c\right) }\right\rbrack   = \left\lbrack  {\alpha \left( a\right) }\right\rbrack \) since \( y\left( c\right)  = {\gamma j}\left( b\right)  = {j}^{\prime }\left( {\beta \left( b\right) }\right) \) and \( {i}^{\prime }\left( {\alpha \left( a\right) }\right)  = \; {\beta i}\left( a\right)  = \beta \partial \left( b\right)  = \partial \beta \left( b\right) \) . Hence \( \partial {\gamma }_{ * }\left\lbrack  c\right\rbrack   = {\alpha }_{ * }\left\lbrack  a\right\rbrack   = {\alpha }_{ * }\partial \left\lbrack  c\right\rbrack \) .

This algebraic fact also implies naturality of the long exact sequence of a triple and the long exact sequence of reduced homology of a pair.

Finally, there is the naturality of the long exact sequence in Theorem 2.13, that is, commutativity of the diagram

\[
\cdots  \rightarrow  {\widetilde{H}}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n}\left( X\right) \overset{{q}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n}\left( {X/A}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( A\right)  \rightarrow  \cdots
\]

\[
\left\lfloor  {{f}_{ * }\;\left\lfloor  {{f}_{ * }\;\left\lfloor  {{\bar{f}}_{ * }\;\left\lfloor  {\bar{f}}_{ * }\right. }\right. }\right. }\right.
\]

\[
\cdots  \rightarrow  {\widetilde{H}}_{n}\left( B\right) \overset{{i}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n}\left( Y\right) \overset{{q}_{ * }}{ \rightarrow  }{\widetilde{H}}_{n}\left( {Y/B}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( B\right)  \rightarrow  \cdots
\]

where \( i \) and \( q \) denote inclusions and quotient maps, and \( \bar{f} : X/A \rightarrow  Y/B \) is induced by \( f \) . The first two squares commute since \( {fi} = {if} \) and \( \bar{f}q = {qf} \) . The third square expands into

\[
{\widetilde{H}}_{n}\left( {X/A}\right) \xrightarrow[ \approx  ]{{j}_{ * }}{H}_{n}\left( {X/A, A/A}\right) \underset{ \approx  }{\overset{{q}_{ * }}{ \Leftarrow  }}{H}_{n}\left( {X, A}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( A\right)
\]

\[
\left\{  {\begin{array}{l} {\bar{f}}_{ * }\; \\  {\bar{f}}_{ * }\; \end{array}\;{f}_{ * }\;{f}_{ * }\;{f}_{ * }\;{f}_{ * }}\right.
\]

\[
{\widetilde{H}}_{n}\left( {Y/B}\right) \overset{{j}_{ * }}{\overbrace{ = }}{H}_{n}\left( {Y/B, B/B}\right) \overset{{q}_{ * }}{\overbrace{ = }}{H}_{n}\left( {Y, B}\right) \overset{\partial }{ \rightarrow  }{\widetilde{H}}_{n - 1}\left( B\right)
\]

We have already shown commutativity of the first and third squares, and the second square commutes since \( \bar{f}q = {qf} \) .

## The Equivalence of Simplicial and Singular Homology

We can use the preceding results to show that the simplicial and singular homology groups of \( \Delta \) -complexes are always isomorphic. For the proof it will be convenient to consider the relative case as well, so let \( X \) be a \( \Delta \) -complex with \( A \subset  X \) a sub-complex. Thus \( A \) is the \( \Delta \) -complex formed by any union of simplices of \( X \) . Relative groups \( {H}_{n}^{\Delta }\left( {X, A}\right) \) can be defined in the same way as for singular homology, via relative chains \( {\Delta }_{n}\left( {X, A}\right)  = {\Delta }_{n}\left( X\right) /{\Delta }_{n}\left( A\right) \) , and this yields a long exact sequence of simplicial homology groups for the pair \( \left( {X, A}\right) \) by the same algebraic argument as for singular homology. There is a canonical homomorphism \( {H}_{n}^{\Delta }\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {X, A}\right) \) induced by the chain map \( {\Delta }_{n}\left( {X, A}\right)  \rightarrow  {C}_{n}\left( {X, A}\right) \) sending each \( n \) -simplex of \( X \) to its characteristic map \( \sigma  : {\Delta }^{n} \rightarrow  X \) . The possibility \( A = \varnothing \) is not excluded, in which case the relative groups reduce to absolute groups.

Theorem 2.27. The homomorphisms \( {H}_{n}^{\Delta }\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {X, A}\right) \) are isomorphisms for all \( n \) and all \( \Delta \) -complex pairs \( \left( {X, A}\right) \) .

Proof: First we do the case that \( X \) is finite-dimensional and \( A \) is empty. For \( {X}^{k} \) the \( k \) -skeleton of \( X \) , consisting of all simplices of dimension \( k \) or less, we have a commutative diagram of exact sequences: Let us first show that the first and fourth vertical maps are isomorphisms for all \( n \) . The simplicial chain group \( {\Delta }_{n}\left( {{X}^{k},{X}^{k - 1}}\right) \) is zero for \( n \neq  k \) , and is free abelian with basis the \( k \) -simplices of \( X \) when \( n = k \) . Hence \( {H}_{n}^{\Delta }\left( {{X}^{k},{X}^{k - 1}}\right) \) has exactly the same description. The corresponding singular homology groups \( {H}_{n}\left( {{X}^{k},{X}^{k - 1}}\right) \) can be computed by considering the map \( \Phi  : \mathop{\coprod }\limits_{\alpha }\left( {{\Delta }_{\alpha }^{k},\partial {\Delta }_{\alpha }^{k}}\right)  \rightarrow  \left( {{X}^{k},{X}^{k - 1}}\right) \) formed by the characteristic maps \( {\Delta }^{k} \rightarrow  X \) for all the \( k \) -simplices of \( X \) . Since \( \Phi \) induces a homeomorphism of quotient spaces \( \mathop{\coprod }\limits_{\alpha }{\Delta }_{\alpha }^{k}/\mathop{\coprod }\limits_{\alpha }\partial {\Delta }_{\alpha }^{k} \approx  {X}^{k}/{X}^{k - 1} \) , it induces isomorphisms on all singular homology groups. Thus \( {H}_{n}\left( {{X}^{k},{X}^{k - 1}}\right) \) is zero for \( n \neq  k \) , while for \( n = k \) this group is free abelian with basis represented by the relative cycles given by the characteristic maps of all the \( k \) -simplices of \( X \) , in view of the fact that \( {H}_{k}\left( {{\Delta }^{k},\partial {\Delta }^{k}}\right) \) is generated by the identity map \( {\Delta }^{k} \rightarrow  {\Delta }^{k} \) , as we showed in Example 2.23. Therefore the map \( {H}_{k}^{\Delta }\left( {{X}^{k},{X}^{k - 1}}\right)  \rightarrow  {H}_{k}\left( {{X}^{k},{X}^{k - 1}}\right) \) is an isomorphism.

\[
{H}_{n + 1}^{\Delta }\left( {{X}^{k},{X}^{k - 1}}\right)  \rightarrow  {H}_{n}^{\Delta }\left( {X}^{k - 1}\right)  \rightarrow  {H}_{n}^{\Delta }\left( {X}^{k}\right)  \rightarrow  {H}_{n}^{\Delta }\left( {{X}^{k},{X}^{k - 1}}\right)  \rightarrow  {H}_{n - 1}^{\Delta }\left( {X}^{k - 1}\right)
\]

\[
\downarrow  \; \downarrow  \; \downarrow  \; \downarrow
\]

\[
{H}_{n + 1}\left( {{X}^{k},{X}^{k - 1}}\right)  \rightarrow  {H}_{n}\left( {X}^{k - 1}\right)  \rightarrow  {H}_{n}\left( {X}^{k}\right)  \rightarrow  {H}_{n}\left( {{X}^{k},{X}^{k - 1}}\right)  \rightarrow  {H}_{n - 1}\left( {X}^{k - 1}\right)
\]

By induction on \( k \) we may assume the second and fifth vertical maps in the preceding diagram are isomorphisms as well. The following frequently quoted basic algebraic lemma will then imply that the middle vertical map is an isomorphism, finishing the proof when \( X \) is finite-dimensional and \( A = \varnothing \) .

The Five-Lemma. In a commutative diagram of abelian groups as at the right, if the two rows are exact and \( \alpha ,\beta ,\delta \) , and \( \varepsilon \) are isomorphisms, then \( \gamma \) is an isomorphism also.

![bo_d7dtv0s91nqc73eq8nv0_137_1024_1009_568_179_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_137_1024_1009_568_179_0.jpg)

Proof: It suffices to show:

(a) \( \gamma \) is surjective if \( \beta \) and \( \delta \) are surjective and \( \varepsilon \) is injective.

(b) \( \gamma \) is injective if \( \beta \) and \( \delta \) are injective and \( \alpha \) is surjective.

The proofs of these two statements are straightforward diagram chasing. There is really no choice about how the argument can proceed, and it would be a good exercise for the reader to close the book now and reconstruct the proofs without looking.

To prove (a), start with an element \( {c}^{\prime } \in  {C}^{\prime } \) . Then \( {k}^{\prime }\left( {c}^{\prime }\right)  = \delta \left( d\right) \) for some \( d \in  D \) since \( \delta \) is surjective. Since \( \varepsilon \) is injective and \( \varepsilon \ell \left( d\right)  = {\ell }^{\prime }\delta \left( d\right)  = {\ell }^{\prime }{k}^{\prime }\left( {c}^{\prime }\right)  = 0 \) , we deduce that \( \ell \left( d\right)  = 0 \) , hence \( d = k\left( c\right) \) for some \( c \in  C \) by exactness of the upper row. The difference \( {c}^{\prime } - \gamma \left( c\right) \) maps to 0 under \( {k}^{\prime } \) since \( {k}^{\prime }\left( {c}^{\prime }\right)  - {k}^{\prime }\gamma \left( c\right)  = {k}^{\prime }\left( {c}^{\prime }\right)  - {\delta k}\left( c\right)  = \; {k}^{\prime }\left( {c}^{\prime }\right)  - \delta \left( d\right)  = 0 \) . Therefore \( {c}^{\prime } - \gamma \left( c\right)  = {j}^{\prime }\left( {b}^{\prime }\right) \) for some \( {b}^{\prime } \in  {B}^{\prime } \) by exactness. Since \( \beta \) is surjective, \( {b}^{\prime } = \beta \left( b\right) \) for some \( b \in  B \) , and then \( \gamma \left( {c + j\left( b\right) }\right)  = \gamma \left( c\right)  + {\gamma j}\left( b\right)  = \; \gamma \left( c\right)  + {j}^{\prime }\beta \left( b\right)  = \gamma \left( c\right)  + {j}^{\prime }\left( {b}^{\prime }\right)  = {c}^{\prime } \) , showing that \( \gamma \) is surjective.

To prove (b), suppose that \( \gamma \left( c\right)  = 0 \) . Since \( \delta \) is injective, \( {\delta k}\left( c\right)  = {k}^{\prime }\gamma \left( c\right)  = 0 \) implies \( k\left( c\right)  = 0 \) , so \( c = j\left( b\right) \) for some \( b \in  B \) . The element \( \beta \left( b\right) \) satisfies \( {j}^{\prime }\beta \left( b\right)  = \; {\gamma j}\left( b\right)  = \gamma \left( c\right)  = 0 \) , so \( \beta \left( b\right)  = {i}^{\prime }\left( {a}^{\prime }\right) \) for some \( {a}^{\prime } \in  {A}^{\prime } \) . Since \( \alpha \) is surjective, \( {a}^{\prime } = \alpha \left( a\right) \) for some \( a \in  A \) . Since \( \beta \) is injective, \( \beta \left( {i\left( a\right)  - b}\right)  = {\beta i}\left( a\right)  - \beta \left( b\right)  = {i}^{\prime }\alpha \left( a\right)  - \beta \left( b\right)  = \; {i}^{\prime }\left( {a}^{\prime }\right)  - \beta \left( b\right)  = 0 \) implies \( i\left( a\right)  - b = 0 \) . Thus \( b = i\left( a\right) \) , and hence \( c = j\left( b\right)  = {ji}\left( a\right)  = 0 \) since \( {ji} = 0 \) . This shows \( \gamma \) has trivial kernel.

Returning to the proof of the theorem, we next consider the case that \( X \) is infinite-dimensional, where we will use the following fact: A compact set in \( X \) can meet only finitely many open simplices of \( X \) , that is, simplices with their proper faces deleted. This is a general fact about CW complexes proved in the Appendix, but here is a direct proof for \( \Delta \) -complexes. If a compact set \( C \) intersected infinitely many open simplices, it would contain an infinite sequence of points \( {x}_{i} \) each lying in a different open simplex. Then the sets \( {U}_{i} = X - \mathop{\bigcup }\limits_{{j \neq  i}}\left\{  {x}_{j}\right\} \) , which are open since their preimages under the characteristic maps of all the simplices are clearly open, form an open cover of \( C \) with no finite subcover.

This can be applied to show the map \( {H}_{n}^{\Delta }\left( X\right)  \rightarrow  {H}_{n}\left( X\right) \) is surjective. Represent a given element of \( {H}_{n}\left( X\right) \) by a singular \( n \) -cycle \( z \) . This is a linear combination of finitely many singular simplices with compact images, meeting only finitely many open simplices of \( X \) , hence contained in \( {X}^{k} \) for some \( k \) . We have shown that \( {H}_{n}^{\Delta }\left( {X}^{k}\right)  \rightarrow  {H}_{n}\left( {X}^{k}\right) \) is an isomorphism, in particular surjective, so \( z \) is homologous in \( {X}^{k} \) (hence in \( X \) ) to a simplicial cycle. This gives surjectivity. Injectivity is similar: If a simplicial \( n \) -cycle \( z \) is the boundary of a singular chain in \( X \) , this chain has compact image and hence must lie in some \( {X}^{k} \) , so \( z \) represents an element of the kernel of \( {H}_{n}^{\Delta }\left( {X}^{k}\right)  \rightarrow  {H}_{n}\left( {X}^{k}\right) \) . But we know this map is injective, so \( z \) is a simplicial boundary in \( {X}^{k} \) , and therefore in \( X \) .

It remains to do the case of arbitrary \( X \) with \( A \neq  \varnothing \) , but this follows from the absolute case by applying the five-lemma to the canonical map from the long exact sequence of simplicial homology groups for the pair \( \left( {X, A}\right) \) to the corresponding long exact sequence of singular homology groups.

We can deduce from this theorem that \( {H}_{n}\left( X\right) \) is finitely generated whenever \( X \) is a \( \Delta \) -complex with finitely many \( n \) -simplices, since in this case the simplicial chain group \( {\Delta }_{n}\left( X\right) \) is finitely generated, hence also its subgroup of cycles and therefore also the latter group’s quotient \( {H}_{n}^{\Delta }\left( X\right) \) . If we write \( {H}_{n}\left( X\right) \) as the direct sum of cyclic groups, then the number of \( \mathbb{Z} \) summands is known traditionally as the \( {n}^{\text{ th }} \) Betti number of \( X \) , and integers specifying the orders of the finite cyclic summands are called torsion coefficients.

It is a curious historical fact that homology was not thought of originally as a sequence of groups, but rather as Betti numbers and torsion coefficients. One can after all compute Betti numbers and torsion coefficients from the simplicial boundary maps without actually mentioning homology groups. This computational viewpoint, with homology being numbers rather than groups, prevailed from when Poincaré first started serious work on homology around 1900, up until the 1920s when the more abstract viewpoint of groups entered the picture. During this period 'homology' meant primarily 'simplicial homology', and it was another 20 years before the shift to singular homology was complete, with the final definition of singular homology emerging only in a 1944 paper of Eilenberg, after contributions from quite a few others, particularly Alexander and Lefschetz. Within the next few years the rest of the basic structure of homology theory as we have presented it fell into place, and the first definitive treatment appeared in the classic book [Eilenberg & Steenrod 1952].

## Exercises

1. What familiar space is the quotient \( \Delta \) -complex of a 2-simplex \( \left\lbrack  {{v}_{0},{v}_{1},{v}_{2}}\right\rbrack \) obtained by identifying the edges \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack \) and \( \left\lbrack  {{v}_{1},{v}_{2}}\right\rbrack \) , preserving the ordering of vertices?

2. Show that the \( \Delta \) -complex obtained from \( {\Delta }^{3} \) by performing the order-preserving edge identifications \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack   \sim  \left\lbrack  {{v}_{1},{v}_{3}}\right\rbrack \) and \( \left\lbrack  {{v}_{0},{v}_{2}}\right\rbrack   \sim  \left\lbrack  {{v}_{2},{v}_{3}}\right\rbrack \) deformation retracts onto a Klein bottle. Also, find other pairs of identifications of edges that produce \( \Delta \) -complexes deformation retracting onto a torus, a 2-sphere, and \( {\mathbb{{RP}}}^{2} \) .

3. Construct a \( \Delta \) -complex structure on \( {\mathbb{{RP}}}^{n} \) as a quotient of a \( \Delta \) -complex structure on \( {S}^{n} \) having vertices the two vectors of length 1 along each coordinate axis in \( {\mathbb{R}}^{n + 1} \) .

4. Compute the simplicial homology groups of the triangular parachute obtained from \( {\Delta }^{2} \) by identifying its three vertices to a single point.

5. Compute the simplicial homology groups of the Klein bottle using the \( \Delta \) -complex structure described at the beginning of this section.

6. Compute the simplicial homology groups of the \( \Delta \) -complex obtained from \( n + 1 \) 2-simplices \( {\Delta }_{0}^{2},\cdots ,{\Delta }_{n}^{2} \) by identifying all three edges of \( {\Delta }_{0}^{2} \) to a single edge, and for \( i > 0 \) identifying the edges \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack \) and \( \left\lbrack  {{v}_{1},{v}_{2}}\right\rbrack \) of \( {\Delta }_{i}^{2} \) to a single edge and the edge \( \left\lbrack  {{v}_{0},{v}_{2}}\right\rbrack \) to the edge \( \left\lbrack  {{v}_{0},{v}_{1}}\right\rbrack \) of \( {\Delta }_{i - 1}^{2} \) .

7. Find a way of identifying pairs of faces of \( {\Delta }^{3} \) to produce a \( \Delta \) -complex structure on \( {S}^{3} \) having a single 3-simplex, and compute the simplicial homology groups of this \( \Delta \) -complex.

8. Construct a 3-dimensional \( \Delta \) -complex \( X \) from \( n \) tetrahedra \( {T}_{1},\cdots ,{T}_{n} \) by the following two steps. First arrange the tetrahedra in a cyclic pattern as in the figure, so that each \( {T}_{i} \) shares a common vertical face with its two neighbors \( {T}_{i - 1} \) and \( {T}_{i + 1} \) , subscripts being taken mod \( n \) . Then identify the bottom face of \( {T}_{i} \) with the top face of \( {T}_{i + 1} \) for each \( i \) . Show the simplicial homology groups of \( X \) in dimensions0,1,2,3are \( \mathbb{Z},{\mathbb{Z}}_{n},0,\mathbb{Z} \) , respectively. [The space \( X \) is an example of a lens space; see Example 2.43 for the general case.]

![bo_d7dtv0s91nqc73eq8nv0_139_1203_1530_387_252_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_139_1203_1530_387_252_0.jpg)

9. Compute the homology groups of the \( \Delta \) -complex \( X \) obtained from \( {\Delta }^{n} \) by identifying all faces of the same dimension. Thus \( X \) has a single \( k \) -simplex for each \( k \leq  n \) . 10. (a) Show the quotient space of a finite collection of disjoint 2-simplices obtained by identifying pairs of edges is always a surface, locally homeomorphic to \( {\mathbb{R}}^{2} \) .

(b) Show the edges can always be oriented so as to define a \( \Delta \) -complex structure on the quotient surface. [This is more difficult.]

11. Show that if \( A \) is a retract of \( X \) then the map \( {H}_{n}\left( A\right)  \rightarrow  {H}_{n}\left( X\right) \) induced by the inclusion \( A \subset  X \) is injective.

12. Show that chain homotopy of chain maps is an equivalence relation.

13. Verify that \( f \simeq  g \) implies \( {f}_{ * } = {g}_{ * } \) for induced homomorphisms of reduced homology groups.

14. Determine whether there exists a short exact sequence \( 0 \rightarrow  {\mathbb{Z}}_{4} \rightarrow  {\mathbb{Z}}_{8} \oplus  {\mathbb{Z}}_{2} \rightarrow  {\mathbb{Z}}_{4} \rightarrow  0 \) . More generally, determine which abelian groups \( A \) fit into a short exact sequence \( 0 \rightarrow  {\mathbb{Z}}_{{p}^{m}} \rightarrow  A \rightarrow  {\mathbb{Z}}_{{p}^{n}} \rightarrow  0 \) with \( p \) prime. What about the case of short exact sequences \( 0 \rightarrow  \mathbb{Z} \rightarrow  A \rightarrow  {\mathbb{Z}}_{n} \rightarrow  0? \)

15. For an exact sequence \( A \rightarrow  B \rightarrow  C \rightarrow  D \rightarrow  E \) show that \( C = 0 \) iff the map \( A \rightarrow  B \) is surjective and \( D \rightarrow  E \) is injective. Hence for a pair of spaces \( \left( {X, A}\right) \) , the inclusion \( A \hookrightarrow  X \) induces isomorphisms on all homology groups iff \( {H}_{n}\left( {X, A}\right)  = 0 \) for all \( n \) .

16. (a) Show that \( {H}_{0}\left( {X, A}\right)  = 0 \) iff \( A \) meets each path-component of \( X \) .

(b) Show that \( {H}_{1}\left( {X, A}\right)  = 0 \) iff \( {H}_{1}\left( A\right)  \rightarrow  {H}_{1}\left( X\right) \) is surjective and each path-component of \( X \) contains at most one path-component of \( A \) .

17. (a) Compute the homology groups \( {H}_{n}\left( {X, A}\right) \) when \( X \) is \( {S}^{2} \) or \( {S}^{1} \times  {S}^{1} \) and \( A \) is a finite set of points in \( X \) .

(b) Compute the groups \( {H}_{n}\left( {X, A}\right) \) and \( {H}_{n}\left( {X, B}\right) \) for \( X \) a closed orientable surface of genus two with \( A \) and \( B \) the circles shown. [What are \( X/A \) and \( X/B \) ?]

![bo_d7dtv0s91nqc73eq8nv0_140_1123_1137_449_154_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_140_1123_1137_449_154_0.jpg)

18. Show that for the subspace \( \mathbb{Q} \subset  \mathbb{R} \) , the relative homology group \( {H}_{1}\left( {\mathbb{R},\mathbb{Q}}\right) \) is free abelian and find a basis.

19. Compute the homology groups of the subspace of \( I \times  I \) consisting of the four boundary edges plus all points in the interior whose first coordinate is rational.

20. Show that \( {\widetilde{H}}_{n}\left( X\right)  \approx  {\widetilde{H}}_{n + 1}\left( {SX}\right) \) for all \( n \) , where \( {SX} \) is the suspension of \( X \) . More generally, thinking of \( {SX} \) as the union of two cones \( {CX} \) with their bases identified, compute the reduced homology groups of the union of any finite number of cones \( {CX} \) with their bases identified.

21. Making the preceding problem more concrete, construct explicit chain maps \( s : {C}_{n}\left( X\right)  \rightarrow  {C}_{n + 1}\left( {SX}\right) \) inducing isomorphisms \( {\widetilde{H}}_{n}\left( X\right)  \rightarrow  {\widetilde{H}}_{n + 1}\left( {SX}\right) \) .

22. Prove by induction on dimension the following facts about the homology of a finite-dimensional CW complex \( X \) , using the observation that \( {X}^{n}/{X}^{n - 1} \) is a wedge sum of \( n \) -spheres:

(a) If \( X \) has dimension \( n \) then \( {H}_{i}\left( X\right)  = 0 \) for \( i > n \) and \( {H}_{n}\left( X\right) \) is free.

(b) \( {H}_{n}\left( X\right) \) is free with basis in bijective correspondence with the \( n \) -cells if there are no cells of dimension \( n - 1 \) or \( n + 1 \) .

(c) If \( X \) has \( k \) n-cells, then \( {H}_{n}\left( X\right) \) is generated by at most \( k \) elements.

23. Show that the second barycentric subdivision of a \( \Delta \) -complex is a simplicial complex. Namely, show that the first barycentric subdivision produces a \( \Delta \) -complex with the property that each simplex has all its vertices distinct, then show that for a \( \Delta \) -complex with this property, barycentric subdivision produces a simplicial complex.

24. Show that each \( n \) -simplex in the barycentric subdivision of \( {\Delta }^{n} \) is defined by \( n \) inequalities \( {t}_{{i}_{0}} \leq  {t}_{{i}_{1}} \leq  \cdots  \leq  {t}_{{i}_{n}} \) in its barycentric coordinates, where \( \left( {{i}_{0},\cdots ,{i}_{n}}\right) \) is a permutation of \( \left( {0,\cdots , n}\right) \) .

25. Find an explicit, noninductive formula for the barycentric subdivision operator \( S : {C}_{n}\left( X\right)  \rightarrow  {C}_{n}\left( X\right) . \)

26. Show that \( {H}_{1}\left( {X, A}\right) \) is not isomorphic to \( {\widetilde{H}}_{1}\left( {X/A}\right) \) if \( X = \left\lbrack  {0,1}\right\rbrack \) and \( A \) is the sequence \( 1,{}^{1}/{}_{2},{}^{1}/{}_{3},\cdots \) together with its limit 0 . [See Example 1.25.]

27. Let \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) be a map such that both \( f : X \rightarrow  Y \) and the restriction \( f : A \rightarrow  B \) are homotopy equivalences.

(a) Show that \( {f}_{ * } : {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n}\left( {Y, B}\right) \) is an isomorphism for all \( n \) .

(b) For the case of the inclusion \( f : \left( {{D}^{n},{S}^{n - 1}}\right)  \hookrightarrow  \left( {{D}^{n},{D}^{n}-\{ 0\} }\right) \) , show that \( f \) is not a homotopy equivalence of pairs - there is no \( g : \left( {{D}^{n},{D}^{n}-\{ 0\} }\right)  \rightarrow  \left( {{D}^{n},{S}^{n - 1}}\right) \) such that \( {fg} \) and \( {gf} \) are homotopic to the identity through maps of pairs. [Observe that a homotopy equivalence of pairs \( \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) is also a homotopy equivalence for the pairs obtained by replacing \( A \) and \( B \) by their closures.]

28. Let \( X \) be the cone on the 1-skeleton of \( {\Delta }^{3} \) , the union of all line segments joining points in the six edges of \( {\Delta }^{3} \) to the barycenter of \( {\Delta }^{3} \) . Compute the local homology groups \( {H}_{n}\left( {X, X-\{ x\} }\right) \) for all \( x \in  X \) . Define \( \partial X \) to be the subspace of points \( x \) such that \( {H}_{n}\left( {X, X-\{ x\} }\right)  = 0 \) for all \( n \) , and compute the local homology groups \( {H}_{n}\left( {\partial X,\partial X-\{ x\} }\right) \) . Use these calculations to determine which subsets \( A \subset  X \) have the property that \( f\left( A\right)  \subset  A \) for all homeomorphisms \( f : X \rightarrow  X \) .

29. Show that \( {S}^{1} \times  {S}^{1} \) and \( {S}^{1} \vee  {S}^{1} \vee  {S}^{2} \) have isomorphic homology groups in all dimensions, but their universal covering spaces do not.

30. In each of the following commutative diagrams assume that all maps but one are isomorphisms. Show that the remaining map must be an isomorphism as well.

![bo_d7dtv0s91nqc73eq8nv0_141_487_1754_813_151_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_141_487_1754_813_151_0.jpg)

31. Using the notation of the five-lemma, give an example where the maps \( \alpha ,\beta ,\delta \) , and \( \varepsilon \) are zero but \( \gamma \) is nonzero. This can be done with short exact sequences in which all the groups are either \( \mathbb{Z} \) or 0 .
