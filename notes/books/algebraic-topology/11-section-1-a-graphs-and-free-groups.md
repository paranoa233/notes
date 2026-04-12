# 1.A Graphs and Free Groups

Since all groups can be realized as fundamental groups of spaces, this opens the way for using topology to study algebraic properties of groups. The topics in this section and the next give some illustrations of this principle, mainly using covering space theory.

We remind the reader that the Additional Topics which form the remainder of this chapter are not to be regarded as an essential part of the basic core of the book. Readers who are eager to move on to new topics should feel free to skip ahead.

By definition, a graph is a 1-dimensional CW complex, in other words, a space \( X \) obtained from a discrete set \( {X}^{0} \) by attaching a collection of 1-cells \( {e}_{\alpha } \) . Thus \( X \) is obtained from the disjoint union of \( {X}^{0} \) with closed intervals \( {I}_{\alpha } \) by identifying the two endpoints of each \( {I}_{\alpha } \) with points of \( {X}^{0} \) . The points of \( {X}^{0} \) are the vertices and the 1-cells the edges of \( X \) . Note that with this definition an edge does not include its endpoints, so an edge is an open subset of \( X \) . The two endpoints of an edge can be the same vertex, so the closure \( {\bar{e}}_{\alpha } \) of an edge \( {e}_{\alpha } \) is homeomorphic either to \( I \) or \( {S}^{1} \) .

Since \( X \) has the quotient topology from the disjoint union \( {X}^{0}\mathop{\coprod }\limits_{\alpha }{I}_{\alpha } \) , a subset of \( X \) is open (or closed) iff it intersects the closure \( {\bar{e}}_{\alpha } \) of each edge \( {e}_{\alpha } \) in an open (or closed) set in \( {\bar{e}}_{\alpha } \) . One says that \( X \) has the weak topology with respect to the subspaces \( {\bar{e}}_{\alpha } \) . In this topology a sequence of points in the interiors of distinct edges forms a closed subset, hence never converges. This is true in particular if the edges containing the sequence all have a common vertex and one tries to choose the sequence so that it gets 'closer and closer' to the vertex. Thus if there is a vertex that is the endpoint of infinitely many edges, then the weak topology cannot be a metric topology. An exercise at the end of this section is to show the converse, that the weak topology is a metric topology if each vertex is an endpoint of only finitely many edges.

A basis for the topology of \( X \) consists of the open intervals in the edges together with the path-connected neighborhoods of the vertices. A neighborhood of the latter sort about a vertex \( v \) is the union of connected open neighborhoods \( {U}_{\alpha } \) of \( v \) in \( {\bar{e}}_{\alpha } \) for all \( {\bar{e}}_{\alpha } \) containing \( v \) . In particular, we see that \( X \) is locally path-connected. Hence a graph is connected iff it is path-connected.

If \( X \) has only finitely many vertices and edges, then \( X \) is compact, being the continuous image of the compact space \( {X}^{0}\mathop{\coprod }\limits_{\alpha }{I}_{\alpha } \) . The converse is also true, and more generally, a compact subset \( C \) of a graph \( X \) can meet only finitely many vertices and edges of \( X \) . To see this, let the subspace \( D \subset  C \) consist of the vertices in \( C \) together with one point in each edge that \( C \) meets. Then \( D \) is a closed subset of \( X \) since it meets each \( {\bar{e}}_{\alpha } \) in a closed set. For the same reason, any subset of \( D \) is closed, so \( D \) has the discrete topology. But \( D \) is compact, being a closed subset of the compact space \( C \) , so \( D \) must be finite. By the definition of \( D \) this means that \( C \) can meet only finitely many vertices and edges.

A subgraph of a graph \( X \) is a subspace \( Y \subset  X \) that is a union of vertices and edges of \( X \) , such that \( {e}_{\alpha } \subset  Y \) implies \( {\bar{e}}_{\alpha } \subset  Y \) . The latter condition just says that \( Y \) is a closed subspace of \( X \) . A tree is a contractible graph. By a tree in a graph \( X \) we mean a subgraph that is a tree. We call a tree in \( X \) maximal if it contains all the vertices of \( X \) . This is equivalent to the more obvious meaning of maximality, as we will see below.

Proposition 1A.1. Every connected graph contains a maximal tree, and in fact any tree in the graph is contained in a maximal tree.

Proof: Let \( X \) be a connected graph. We will describe a construction that embeds an arbitrary subgraph \( {X}_{0} \subset  X \) as a deformation retract of a subgraph \( Y \subset  X \) that contains all the vertices of \( X \) . By choosing \( {X}_{0} \) to be any subtree of \( X \) , for example a single vertex, this will prove the proposition.

As a preliminary step, we construct a sequence of subgraphs \( {X}_{0} \subset  {X}_{1} \subset  {X}_{2} \subset  \cdots \) , letting \( {X}_{i + 1} \) be obtained from \( {X}_{i} \) by adjoining the closures \( {\bar{e}}_{\alpha } \) of all edges \( {e}_{\alpha } \subset  X - {X}_{i} \) having at least one endpoint in \( {X}_{i} \) . The union \( \mathop{\bigcup }\limits_{i}{X}_{i} \) is open in \( X \) since a neighborhood of a point in \( {X}_{i} \) is contained in \( {X}_{i + 1} \) . Furthermore, \( \mathop{\bigcup }\limits_{i}{X}_{i} \) is closed since it is a union of closed edges and \( X \) has the weak topology. So \( X = \mathop{\bigcup }\limits_{i}{X}_{i} \) since \( X \) is connected.

Now to construct \( Y \) we begin by setting \( {Y}_{0} = {X}_{0} \) . Then inductively, assuming that \( {Y}_{i} \subset  {X}_{i} \) has been constructed so as to contain all the vertices of \( {X}_{i} \) , let \( {Y}_{i + 1} \) be obtained from \( {Y}_{i} \) by adjoining one edge connecting each vertex of \( {X}_{i + 1} - {X}_{i} \) to \( {Y}_{i} \) , and let \( Y = \mathop{\bigcup }\limits_{i}{Y}_{i} \) . It is evident that \( {Y}_{i + 1} \) deformation retracts to \( {Y}_{i} \) , and we may obtain a deformation retraction of \( Y \) to \( {Y}_{0} = {X}_{0} \) by performing the deformation retraction of \( {Y}_{i + 1} \) to \( {Y}_{i} \) during the time interval \( \left\lbrack  {1/{2}^{i + 1},1/{2}^{i}}\right\rbrack \) . Thus a point \( x \in  {Y}_{i + 1} - {Y}_{i} \) is stationary until this interval, when it moves into \( {Y}_{i} \) and thereafter continues moving until it reaches \( {Y}_{0} \) . The resulting homotopy \( {h}_{t} : Y \rightarrow  Y \) is continuous since it is continuous on the closure of each edge and \( Y \) has the weak topology.

Given a maximal tree \( T \subset  X \) and a base vertex \( {x}_{0} \in  T \) , then each edge \( {e}_{\alpha } \) of \( X - T \) determines a loop \( {f}_{\alpha } \) in \( X \) that goes first from \( {x}_{0} \) to one endpoint of \( {e}_{\alpha } \) by a path in \( T \) , then across \( {e}_{\alpha } \) , then back to \( {x}_{0} \) by a path in \( T \) . Strictly speaking, we should first orient the edge \( {e}_{\alpha } \) in order to specify which direction to cross it. Note that the homotopy class of \( {f}_{\alpha } \) is independent of the choice of the paths in \( T \) since \( T \) is simply-connected.

Proposition 1A.2. For a connected graph \( X \) with maximal tree \( T,{\pi }_{1}\left( X\right) \) is a free group with basis the classes \( \left\lbrack  {f}_{\alpha }\right\rbrack \) corresponding to the edges \( {e}_{\alpha } \) of \( X - T \) .

In particular this implies that a maximal tree is maximal in the sense of not being contained in any larger tree, since adjoining any edge to a maximal tree produces a graph with nontrivial fundamental group. Another consequence is that a graph is a tree iff it is simply-connected.

Proof: The quotient map \( X \rightarrow  X/T \) is a homotopy equivalence by Proposition 0.17. The quotient \( X/T \) is a graph with only one vertex, hence is a wedge sum of circles, whose fundamental group we showed in Example 1.21 to be free with basis the loops given by the edges of \( X/T \) , which are the images of the loops \( {f}_{\alpha } \) in \( X \) .

Here is a very useful fact about graphs:

Lemma 1A.3. Every covering space of a graph is also a graph, with vertices and edges the lifts of the vertices and edges in the base graph.

Proof: Let \( p : X \rightarrow  X \) be the covering space. For the vertices of \( \widetilde{X} \) we take the discrete set \( {\widetilde{X}}^{0} = {p}^{-1}\left( {X}^{0}\right) \) . Writing \( X \) as a quotient space of \( {X}^{0}\mathop{\coprod }\limits_{\alpha }{I}_{\alpha } \) as in the definition of a graph and applying the path lifting property to the resulting maps \( {I}_{\alpha } \rightarrow  X \) , we get a unique lift \( {I}_{\alpha } \rightarrow  \widetilde{X} \) passing through each point in \( {p}^{-1}\left( x\right) \) , for \( x \in  {e}_{\alpha } \) . These lifts define the edges of a graph structure on \( \widetilde{X} \) . The resulting topology on \( \widetilde{X} \) is the same as its original topology since both topologies have the same basic open sets, the covering projection \( \widetilde{X} \rightarrow  X \) being a local homeomorphism.

We can now apply what we have proved about graphs and their fundamental groups to prove a basic fact of group theory:

Theorem 1A.4. Every subgroup of a free group is free.

Proof: Given a free group \( F \) , choose a graph \( X \) with \( {\pi }_{1}\left( X\right)  \approx  F \) , for example a wedge of circles corresponding to a basis for \( F \) . For each subgroup \( G \) of \( F \) there is by Proposition 1.36 a covering space \( p : \widetilde{X} \rightarrow  X \) with \( {p}_{ * }\left( {{\pi }_{1}\left( \widetilde{X}\right) }\right)  = G \) , hence \( {\pi }_{1}\left( \widetilde{X}\right)  \approx  G \) since \( {p}_{ * } \) is injective by Proposition 1.31. Since \( \widetilde{X} \) is a graph by the preceding lemma, the group \( G \approx  {\pi }_{1}\left( \widetilde{X}\right) \) is free by Proposition 1A.2.

The structure of trees can be elucidated by looking more closely at the constructions in the proof of Proposition 1A.1. If \( X \) is a tree and \( {v}_{0} \) is any vertex of \( X \) , then the construction of a maximal tree \( Y \subset  X \) starting with \( {Y}_{0} = \left\{  {v}_{0}\right\} \) yields an increasing sequence of subtrees \( {Y}_{n} \subset  X \) whose union is all of \( X \) since a tree has only one maximal subtree, namely itself. We can think of the vertices in \( {Y}_{n} - {Y}_{n - 1} \) as being at ’height’ \( n \) , with the edges of \( {Y}_{n} - {Y}_{n - 1} \) connecting these vertices to vertices of height \( n - 1 \) . In this way we get a ’height function’ \( h : X \rightarrow  \mathbb{R} \) assigning to each vertex its height, and monotone on edges.

![bo_d7dtv0s91nqc73eq8nv0_93_1285_1919_302_359_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_93_1285_1919_302_359_0.jpg)

For each vertex \( v \) of \( X \) there is exactly one edge leading downward from \( v \) , so by following these downward edges we obtain a path from \( v \) to the base vertex \( {v}_{0} \) . This is an example of an edgepath, which is a composition of finitely many paths each consisting of a single edge traversed monotonically. For any edgepath joining \( v \) to \( {v}_{0} \) other than the downward edgepath, the height function would not be monotone and hence would have local maxima, occurring when the edgepath backtracked, retracing some edge it had just crossed. Thus in a tree there is a unique nonbacktracking edgepath joining any two points. All the vertices and edges along this edgepath are distinct.

A tree can contain no subgraph homeomorphic to a circle, since two vertices in such a subgraph could be joined by more than one nonbacktracking edgepath. Conversely, if a connected graph \( X \) contains no circle subgraph, then it must be a tree. For if \( T \) is a maximal tree in \( X \) that is not equal to \( X \) , then the union of an edge of \( X - T \) with the nonbacktracking edgepath in \( T \) joining the endpoints of this edge is a circle subgraph of \( X \) . So if there are no circle subgraphs of \( X \) , we must have \( X = T \) , a tree.

For an arbitrary connected graph \( X \) and a pair of vertices \( {v}_{0} \) and \( {v}_{1} \) in \( X \) there is a unique nonbacktracking edgepath in each homotopy class of paths from \( {v}_{0} \) to \( {v}_{1} \) . This can be seen by lifting to the universal cover \( \widetilde{X} \) , which is a tree since it is simply-connected. Choosing a lift \( {\widetilde{v}}_{0} \) of \( {v}_{0} \) , a homotopy class of paths from \( {v}_{0} \) to \( {v}_{1} \) lifts to a homotopy class of paths starting at \( {\widetilde{v}}_{0} \) and ending at a unique lift \( {\widetilde{v}}_{1} \) of \( {v}_{1} \) . Then the unique nonbacktracking edgepath in \( \widetilde{X} \) from \( {\widetilde{v}}_{0} \) to \( {\widetilde{v}}_{1} \) projects to the desired nonbacktracking edgepath in \( X \) .

## Exercises

1. Let \( X \) be a graph in which each vertex is an endpoint of only finitely many edges. Show that the weak topology on \( X \) is a metric topology.

2. Show that a connected graph retracts onto any connected subgraph.

3. For a finite graph \( X \) define the Euler characteristic \( \chi \left( X\right) \) to be the number of vertices minus the number of edges. Show that \( \chi \left( X\right)  = 1 \) if \( X \) is a tree, and that the rank (number of elements in a basis) of \( {\pi }_{1}\left( X\right) \) is \( 1 - \chi \left( X\right) \) if \( X \) is connected.

4. If \( X \) is a finite graph and \( Y \) is a subgraph homeomorphic to \( {S}^{1} \) and containing the basepoint \( {x}_{0} \) , show that \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) has a basis in which one element is represented by the loop \( Y \) .

5. Construct a connected graph \( X \) and maps \( f, g : X \rightarrow  X \) such that \( {fg} = \mathbb{1} \) but \( f \) and \( g \) do not induce isomorphisms on \( {\pi }_{1} \) . [Note that \( {f}_{ * }{g}_{ * } = \mathbb{1} \) implies that \( {f}_{ * } \) is surjective and \( {g}_{ * } \) is injective.]

6. Let \( F \) be the free group on two generators and let \( {F}^{\prime } \) be its commutator subgroup. Find a set of free generators for \( {F}^{\prime } \) by considering the covering space of the graph \( {S}^{1} \vee  {S}^{1} \) corresponding to \( {F}^{\prime } \) .

7. If \( F \) is a finitely generated free group and \( N \) is a nontrivial normal subgroup of infinite index, show, using covering spaces, that \( N \) is not finitely generated.

8. Show that a finitely generated group has only a finite number of subgroups of a given finite index. [First do the case of free groups, using covering spaces of graphs. The general case then follows since every group is a quotient group of a free group.]

9. Using covering spaces, show that an index \( n \) subgroup \( H \) of a group \( G \) has at most \( n \) conjugate subgroups \( {gH}{g}^{-1} \) in \( G \) . Apply this to show that there exists a normal subgroup \( K \subset  G \) of finite index with \( K \subset  H \) . [For the latter statement, consider the intersection of all the conjugate subgroups \( {gH}{g}^{-1} \) . This is the maximal normal subgroup of \( G \) contained in \( H \) .]

10. Let \( X \) be the wedge sum of \( n \) circles, with its natural graph structure, and let \( \widetilde{X} \rightarrow  X \) be a covering space with \( Y \subset  \widetilde{X} \) a finite connected subgraph. Show there is a finite graph \( Z \supset  Y \) having the same vertices as \( Y \) , such that the projection \( Y \rightarrow  X \) extends to a covering space \( Z \rightarrow  X \) .

11. Apply the two preceding problems to show that if \( F \) is a finitely generated free group and \( x \in  F \) is not the identity element, then there is a normal subgroup \( H \subset  F \) of finite index such that \( x \notin  H \) . Hence \( x \) has nontrivial image in a finite quotient group of \( F \) . In this situation one says \( F \) is residually finite.

12. Let \( F \) be a finitely generated free group, \( H \subset  F \) a finitely generated subgroup, and \( x \in  F - H \) . Show there is a subgroup \( K \) of finite index in \( F \) such that \( K \supset  H \) and \( x \notin  K \) . [Apply Exercise 10.]

13. Let \( x \) be a nontrivial element of a finitely generated free group \( F \) . Show there is a finite-index subgroup \( H \subset  F \) in which \( x \) is one element of a basis. [Exercises 4 and 10 may be helpful.]

14. Show that the existence of maximal trees is equivalent to the Axiom of Choice.
