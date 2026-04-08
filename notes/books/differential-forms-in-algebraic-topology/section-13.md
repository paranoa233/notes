## §13 Monodromy

When Is a Locally Constant Presheaf Constant?

In the preceding section we saw that the compact vertical cohomology \( {H}_{cv}^{ * }\left( E\right) \) of a vector bundle \( E \) may be computed as the cohomology of the base with coefficients in the presheaf \( {\mathcal{H}}_{cv}^{n} \) . When the presheaf \( {\mathcal{H}}_{cv}^{n} \) is the constant presheaf \( {\mathbb{R}}^{n},{H}_{cv}^{ * }\left( E\right) \) is expressible in terms of the de Rham cohomology of the base manifold (Proposition 10.6). In this case the problem of computing \( {H}_{cv}^{ * }\left( E\right) \) is greatly simplified. It is therefore important to determine the conditions under which a presheaf such as \( {\mathcal{H}}_{cv}^{n} \) is constant.

First we need to review some basic definitions from the theory of simplicial complexes (see, for instance, Munkres [2]). Recall that if an n-simplex in an Euclidean space has vertices \( {v}_{0},\ldots ,{v}_{n} \) , then its barycenter is the point \( \left( {{v}_{0} + \cdots  + {v}_{n}}\right) /\left( {n + 1}\right) \) . For example, the barycenter of an edge is its midpoint and the barycenter of a triangle (a 2-simplex) is its center. The first barycentric subdivision of a simplex \( \sigma \) is the simplicial complex having all the barycenters of \( \sigma \) as vertices. By applying the barycentric subdivision to each simplex of a simplical complex \( K \) , we obtain a new simplicial complex \( {K}^{\prime } \) , called the first barycentric subdivision of \( K \) . The support of \( K \) , denoted \( \left| K\right| \) , is the underlying topological space of \( K \) , and the \( k \) -skeleton of \( K \) is the subcomplex consisting of all the simplices of dimension less than or equal to \( k \) . The complex \( K \) and its barycentric subdivision \( {K}^{\prime } \) have the same support. The star of a vertex \( v \) in \( K \) , denoted \( \mathrm{{st}}\left( v\right) \) , is the union of all the closed simplices in \( K \) having \( v \) as a vertex.

Next we introduce the notion of a presheaf on a good cover. Let \( X \) be a topological space and \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) a good cover of \( X \) . The presheaf \( \mathcal{F} \) on \( \mathfrak{U} \) is defined to be a functor \( \mathcal{F} \) on the subcategory of \( \operatorname{Open}\left( X\right) \) consisting of all finite intersections \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) of open sets in \( \mathfrak{U} \) . Equivalently, if \( N\left( \mathfrak{U}\right) \) is the nerve of \( \mathfrak{U} \) , the presheaf \( \mathcal{F} \) on \( \mathfrak{U} \) is the assignment of an appropriate group to the barycenter of each simplex in \( N\left( \mathfrak{U}\right) \) ; for example, the group attached to the barycenter of the 2-simplex representing \( U \cap  V \cap  \mathrm{W} \) is \( \mathcal{F}\left( {U \cap  V \cap  W}\right) \) . Each inclusion, say \( U \cap  V \rightarrow  U \) , becomes an arrow in the picture, \( \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( {U \cap  V}\right) \) , and the transitivity of the arrows says that Figure 13.1 is a commutative diagram.

![bo_d7b6f8alb0pc73dd9avg_152_463_1532_710_449_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_152_463_1532_710_449_0.jpg)

Figure 13.1

Two presheaves \( \mathcal{F} \) and \( \mathcal{G} \) are isomorphic relative to a good cover \( \mathfrak{U} = \; \left\{  {U}_{\alpha }\right\} \) if for each \( W = {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) there is an isomorphism

\[
{h}_{W} : \mathcal{F}\left( W\right)  \rightarrow  \mathcal{G}\left( W\right)
\]

compatible with all arrows. In other words, there is a natural equivalence of functors \( \mathcal{F} \rightarrow  \mathcal{G} \) where \( \mathcal{F} \) and \( \mathcal{G} \) are regarded as functors on the subcategory of \( \operatorname{Open}\left( X\right) \) consisting of all finite intersections \( {U}_{{\alpha }_{0}\ldots {\alpha }_{n}} \) of open sets in \( \mathfrak{U} \) . The constant presheaf with group \( G \) on a good cover \( \mathfrak{U} \) is defined as in Section 10; it associates to every open set \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) the group of locally constant and hence constant functions: \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \rightarrow  G \) . Thus, for a constant presheaf on a good cover, all the groups are \( G \) and all the arrows are the identity map. We say that a presheaf \( \mathcal{F} \) is locally constant on a good cover \( \mathfrak{U} \) if all the groups are isomorphic and all the arrows are isomorphisms.

Of course, if two presheaves \( \mathcal{F} \) and \( \mathcal{G} \) are isomorphic on a good cover \( \mathfrak{U} \) , then the cohomology groups \( {H}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) and \( {H}^{ * }\left( {\mathfrak{U},\mathcal{G}}\right) \) are isomorphic.

![bo_d7b6f8alb0pc73dd9avg_153_637_1018_378_376_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_153_637_1018_378_376_0.jpg)

Figure 13.2

EXAMPLE 13.1 (A locally constant presheaf on \( \mathfrak{U} \) which is not constant). Let \( \mathfrak{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) be a good cover of the circle \( {S}^{1} \) (see Figure 13.2). Define a presheaf \( \mathcal{F} \) by

\[
\mathcal{F}\left( U\right)  = \mathbb{Z}\text{ for all open sets }U\text{ , }
\]

\[
{\rho }_{01}^{0} = {\rho }_{01}^{1} = {\rho }_{12}^{1} = {\rho }_{12}^{2} = 1,
\]

\[
{\rho }_{02}^{2} =  - 1,{\rho }_{02}^{0} = 1
\]

\( \mathcal{F} \) is locally constant but not constant on \( \mathfrak{U} \) because \( {\rho }_{02}^{2} \) is not the identity.

Let \( \mathcal{F} \) be a locally constant presheaf with group \( G \) on a good cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) . Fix isomorphisms

\[
{\phi }_{\alpha } : \mathcal{F}\left( {U}_{\alpha }\right) \overset{ \sim  }{ \rightarrow  }G
\]

If \( {U}_{\alpha } \) and \( {U}_{\beta } \) intersect, then from the diagram

![bo_d7b6f8alb0pc73dd9avg_154_700_375_268_400_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_154_700_375_268_400_0.jpg)

we obtain an automorphism of \( G \) , namely \( {\phi }_{\beta }{\left( {\rho }_{\alpha \beta }^{\beta }\right) }^{-1}{\rho }_{\alpha \beta }^{\alpha }{\phi }_{\alpha }^{-1} \) . Write \( {\rho }_{\beta }^{\alpha } \) : \( \mathcal{F}\left( {U}_{\alpha }\right)  \rightarrow  \mathcal{F}\left( {U}_{\beta }\right) \) for the isomorphism \( {\left( {\rho }_{\alpha \beta }^{\beta }\right) }^{-1} \circ  {\rho }_{\alpha \beta }^{\alpha } \) . Choose some vertex \( {U}_{0} \) as the base point of the nerve \( N\left( \mathfrak{U}\right) \) . For \( {U}_{0}{U}_{1}\ldots {U}_{r}{U}_{0} \) a loop based at \( {U}_{0} \) we get an automorphism of \( G \) by following along the edges

![bo_d7b6f8alb0pc73dd9avg_154_706_999_234_547_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_154_706_999_234_547_0.jpg)

This gives a map from \( \left\{  {\text{ loops at }{U}_{0}}\right\} \) to Aut \( G \) . We claim that if a loop bounds a 2-chain, then the associated automorphism of \( G \) is the identity. Consider the example of the 2-simplex as shown in Figure 13.3.

![bo_d7b6f8alb0pc73dd9avg_154_626_1714_412_337_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_154_626_1714_412_337_0.jpg)

Figure 13.3

![bo_d7b6f8alb0pc73dd9avg_155_267_286_1073_1512_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_155_267_286_1073_1512_0.jpg)

Figure 13.4

The associated automorphism of the loop \( {U}_{0}{U}_{1}{U}_{2} \) is \( {\phi }_{0}\left( {{\rho }_{0}^{2}{\rho }_{2}^{1}{\rho }_{1}^{0}}\right) {\phi }_{0}^{-1} \) so it is a matter of showing that \( {\rho }_{0}^{2}{\rho }_{2}^{1}{\rho }_{1}^{0} \) is the identity. This is clear from the sequence of pictures in Figure 13.4, where we use heavy solid lines to indicate maps which, by the commutativity of the arrows, are all equal to \( {\rho }_{0}^{2}{\rho }_{2}^{1}{\rho }_{1}^{0} \)

More generally, the same procedure shows that the map \( {\rho }_{0}^{\alpha }\ldots {\rho }_{\beta }^{0} \) around any bounding loop is the identity. Hence there is a homomorphism

\[
\rho  : {\pi }_{1}\left( {N\left( \mathfrak{U}\right) }\right)  = \frac{\{ \text{ loops }\} }{\{ \text{ bounding loops }\} } \rightarrow  \text{ Aut }G,
\]

called the monodromy representation of the presheaf \( \mathcal{F} \) . Here \( {\pi }_{1}\left( {N\left( \mathfrak{U}\right) }\right) \) denotes the edge path group of the nerve \( N\left( \mathfrak{U}\right) \) as a simplicial complex.

Theorem 13.2. Let \( \mathfrak{U} \) be a good cover on a connected topological space \( X \) and \( N\left( \mathfrak{U}\right) \) its nerve. If \( {\pi }_{1}\left( {N\left( \mathfrak{U}\right) }\right)  = 0 \) , then every locally constant presheaf on \( \mathfrak{U} \) is constant.

Proof. Suppose \( {\pi }_{1}\left( {N\left( \mathfrak{U}\right) }\right)  = 0 \) , i.e., every loop bounds some 2-chain. For each open set \( {U}_{\alpha } \) , choose a path from \( {U}_{0} \) to \( {U}_{\alpha } \) , say \( {U}_{0}{U}_{{\alpha }_{1}}\ldots {U}_{{\alpha }_{r}}{U}_{\alpha } \) , and define \( {\psi }_{\alpha } = {\phi }_{0}{\left( {\rho }_{\alpha }^{{\alpha }_{r}}\ldots {\rho }_{{\alpha }_{2}}^{{\alpha }_{1}}{\rho }_{{\alpha }_{1}}^{0}\right) }^{-1} : \mathcal{F}\left( {U}_{\alpha }\right)  \rightarrow  G \) .

\( {\phi }_{0} \)

\[
\mathcal{F}\left( {U}_{0}\right) \overset{ \sim  }{ \rightarrow  }G
\]

\[
\text{ ↓ }
\]

\[
\mathcal{F}\left( {U}_{\alpha }\right)
\]

\( {\psi }_{\alpha } \) is well-defined independent of the chosen path, because as we have seen, around a bounding loop the map \( {\rho }_{0}^{\alpha }\ldots {\rho }_{\beta }^{0} \) is the identity.

Now carry out the barycentric subdivision of the nerve \( N\left( \mathfrak{U}\right) \) to get a new simplicial complex \( K \) so that every open set \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) corresponds to a vertex of \( K \) . Clearly \( {\pi }_{1}\left( {N\left( \mathfrak{U}\right) }\right)  = {\pi }_{1}\left( K\right) \) . By the same procedure as in the preceding paragraph we can define isomorphisms

\[
{\psi }_{{\alpha }_{0}\ldots {\alpha }_{p}} : \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \rightarrow  G
\]

for all nonempty \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) . The maps \( {\psi }_{{\alpha }_{0}\ldots {\alpha }_{p}} \) give an isomorphism of the presheaf \( \mathcal{F} \) to the constant presheaf \( G \) on the cover \( \mathfrak{U} \) .

REMARK 13.2.1. If the group \( G \) of a locally constant presheaf has no automorphisms except the identity, then there is no monodromy. In particular, every locally constant presheaf with group \( {\mathbb{Z}}_{2} \) is constant.

REMARK 13.3. Recall that a simplicial map between two simplicial complexes \( K \) and \( L \) is a map \( f \) from the vertices of \( K \) to the vertices of \( L \) such that if \( {v}_{0},\ldots ,{v}_{n} \) span a simplex in \( K \) , then \( f\left( {v}_{0}\right) ,\ldots , f\left( {v}_{n}\right) \) span a simplex in \( L \) . A simplicial map \( f \) from \( K \) to \( L \) induces a map \( f : \left| K\right|  \rightarrow  \left| L\right| \) by linearity:

\[
f\left( {\sum {\lambda }_{i}{v}_{i}}\right)  = \sum {\lambda }_{i}{f}_{i}\left( {v}_{i}\right) .
\]

By abuse of language we refer to either of these maps as a simplicial map.

For the proof of the next theorem we assemble here some standard facts from the theory of simplicial complexes.

(a) The edge path group of a simplicial complex is the same as that of its 2-skeleton (Seifert and Threlfall [1, §44, p. 167]).

(b) The edge path group of a simplicial complex is the same as the topological fundamental group of its support (Seifert and Threlfall [1, §44, p. 165]).

(c) (The Simplicial Approximation Theorem). Let \( K \) and \( L \) be two simplicial complexes. Then every map \( f : \left| K\right|  \rightarrow  \left| L\right| \) is homotopic to a simplicial map \( g : \left| {K}^{\left( k\right) }\right|  \rightarrow  \left| L\right| \) for some integer \( k \) , where \( {K}^{\left( k\right) } \) is the \( k \) -th barycentric subdivision of \( K \) (Croom [1, p. 49]).

Because of (b) we also refer to the edge path group of a simplicial complex as its fundamental group.

None of these facts are difficult to prove. They all depend on the following very intuitive principle from obstruction theory.

The Extension Principle. A map from the union of all the faces of a cube into a contractible space can be extended to the entire cube.

ASIDE. With a little homotopy theory the extension principle can be refined as follows. Let \( X \) be a topological space and \( {I}^{k} \) the unit \( k \) -dimensional cube. If \( {\pi }_{a}\left( X\right)  = 0 \) for all \( q \leq  k - 1 \) , then any maps from the boundary of \( {I}^{k} \) into \( X \) can be extended to the entire cube \( {I}^{k} \) .

In section 5 we defined a good cover on a manifold to be an open cover \( \left\{  {U}_{\alpha }\right\} \) for which all finite intersections \( {U}_{{\alpha }_{0}} \cap  \cdots  \cap  {U}_{{\alpha }_{p}} \) are diffeomorphic to a Euclidean space. By a good cover on a topological space we shall mean an open cover for which all finite intersections are contractible.

REMARK. Thus, on a manifold there are two notions of a good cover. These two notions are not equivalent. Let us call a noncompact boundaryless manifold an open manifold. Then there are contractible open 3-manifolds not homeomorphic to \( {\mathbb{R}}^{3} \) . In 1935 J. H. C. Whitehead found the first example of such a manifold [J. H. C. Whitehead, A certain n-manifold whose group is unity, Quart. J. Math. Oxford 6 (1935), 268-279]. D. R. McMillan, Jr. constructed infinitely many more in [D. R. McMillan, Jr., Some contractible open 3-manifolds, Transactions of the A. M. S. 102 (1962), 372-382]. For an open cover on a manifold to be a good cover we will always require the more restrictive hypothesis that the finite nonempty intersections be diffeomorphic to \( {\mathbb{R}}^{n} \) . This is because in order to prove Poincaré duality, whether by the Mayer-Vietoris argument of Section 5 or by the tic-tac-toe game of Section 12, we need the compact Poincaré lemma (Corollary 4.7), which is not always true for an open set with merely the homotopy type of \( {\mathbb{R}}^{n} \) .

Theorem 13.4. Suppose the topological space \( X \) has a good cover \( \mathfrak{U} \) . Then the fundamental group of \( X \) is isomorphic to the fundamental group \( {\pi }_{1}\left( {N\left( \mathfrak{U}\right) }\right) \) of the nerve of the good cover.

Proof. Write \( {N}_{2}\left( \mathfrak{U}\right) \) for the 2-skeleton of the nerve \( N\left( \mathfrak{U}\right) \) . Let \( {U}_{i},{U}_{ij} \) , and \( {U}_{ijk} \) be the barycenters of the vertices, edges, and faces of \( {N}_{2}\left( \mathfrak{U}\right) \) and let \( {N}_{2}^{\prime }\left( \mathfrak{U}\right) \) be its barycentric subdivision. As the first step in the proof of the theorem we will define a map \( f \) from \( \left| {{N}_{2}^{\prime }\left( U\right) }\right| \) to \( X \) . We will then show that this map induces an isomorphism of fundamental groups.

To this end choose a point \( {p}_{i} \) in each open set \( {U}_{i} \) in \( \mathfrak{U} \) , a point \( {p}_{ij} \) in each nonempty pairwise intersection \( {U}_{ij} \) , and a point \( {p}_{ijk} \) in each nonempty triple intersection \( {U}_{ijk} \) . Also, fix a contraction \( {c}_{i} \) of \( {U}_{i} \) to \( {p}_{i} \) and a contraction \( {c}_{ij} \) of \( {U}_{ij} \) to \( {p}_{ij} \) . These contractions exist because \( \mathfrak{U} \) is a good cover. By decree the map \( f \) sends \( {U}_{i},{U}_{ij} \) , and \( {U}_{ijk} \) to \( {p}_{i},{p}_{ij} \) , and \( {p}_{ijk} \) respectively.

![bo_d7b6f8alb0pc73dd9avg_158_584_902_492_314_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_158_584_902_492_314_0.jpg)

Figure 13.5

Next we define \( f \) on the edges of \( \left| {{N}_{2}^{\prime }\left( \mathfrak{U}\right) }\right| \) . The contraction \( {c}_{i} \) takes \( {p}_{ij} \) to \( {p}_{i} \) and gives a well-defined path between \( {p}_{i} \) and \( {p}_{ij} \) . Similarly, the contraction \( {c}_{j} \) gives a well-defined path between \( {p}_{j} \) and \( {p}_{ij} \) (see Figure 13.5). Furthermore, for each point \( {p}_{ijk} \) the six contractions \( {c}_{i},{c}_{j},{c}_{k},{c}_{ij},{c}_{ik} \) , and \( {c}_{jk} \) produce six paths in \( X \) joining \( {p}_{ijk} \) to \( {p}_{i},{p}_{j},{p}_{k},{p}_{ij},{p}_{ik} \) , and \( {p}_{jk} \) respectively (see Figure 13.6).

![bo_d7b6f8alb0pc73dd9avg_158_594_1571_485_477_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_158_594_1571_485_477_0.jpg)

Figure 13.6

The map \( f \) shall send the edges of \( \left| {{N}_{2}^{\prime }\left( \mathfrak{U}\right) }\right| \) to the paths just defined; for example, the edge \( {U}_{i}{U}_{ijk} \) is sent to the path joining \( {p}_{i} \) and \( {p}_{ijk} \) .

Finally we define \( f \) on the faces of \( \left| {{N}_{2}^{\prime }\left( \mathfrak{U}\right) }\right| \) . Since each "triangle" \( {p}_{i}{p}_{ij}{p}_{ijk} \) lies entirely inside the open set \( {U}_{i} \) (such a triangle may be degenerate; i.e., it may only be a point or a segment), the triangle may be "filled in" in a well-defined manner: to fill in the triangle \( {p}_{i}{p}_{ij}{p}_{ijk} \) , use the contraction \( {c}_{i} \) to contract the edge \( {p}_{ij}{p}_{ijk} \) to \( {p}_{i} \) (see Figure 13.6). This "filled-in" triangle will be the image of the triangle \( {U}_{i}{U}_{j}{U}_{ijk} \) under \( f \) . In summary, with the choice of the points \( {p}_{i},{p}_{ij},{p}_{ijk} \) and the contractions \( {c}_{i},{c}_{ij} \) fixed, we have defined a map \( f : \left| {{N}_{2}^{\prime }\left( \mathfrak{U}\right) }\right|  \rightarrow  X \) . We will now show that the induced map of fundamental groups, \( {f}_{ * } : {\pi }_{1}\left( \left| {{N}_{2}^{\prime }\left( \mathfrak{U}\right) }\right| \right)  \rightarrow  {\pi }_{1}\left( X\right) \) is an isomorphism.

STEP 1 (Surjectivity of \( {f}_{ * } \) ). Take \( {p}_{0} \) in \( {U}_{0} \) to be the base point of \( X \) . Let \( \gamma  : {S}^{1} \rightarrow  X \) be a loop in \( X \) based at \( {p}_{0} \) . We would like to deform \( \gamma \) to a map of the form \( {f}_{ * }\left( \overrightarrow{\gamma }\right) \) , where \( \overrightarrow{\gamma } : {S}^{1} \rightarrow  \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \) is a loop in \( \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \) based at \( {U}_{0} \) .

Regard \( {S}^{1} \) as the unit interval \( I \) with its endpoints identified. To define \( \overline{\gamma } \) , we first subdivide the unit interval into equal pieces, so that it becomes a simplicial complex \( K \) with vertices \( {q}_{0},\ldots ,{q}_{n} \) (Figure 13.7).

![bo_d7b6f8alb0pc73dd9avg_159_430_1069_768_76_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_159_430_1069_768_76_0.jpg)

Figure 13.7

By making the pieces sufficiently small, we can ensure that the star of \( {q}_{i} \) in the barycentric subdivision \( {K}^{\prime } \) of \( K \) is mapped entirely into an open set \( {U}_{\alpha \left( i\right) } \) :

\[
\gamma \left( {\operatorname{st}\left( {q}_{i}\right) }\right)  \subset  {U}_{\alpha \left( i\right) }\text{ . }
\]

To simplify the notation, write \( j \) instead of \( i + 1 \) , so that \( {q}_{i}{q}_{j} \) is a 1- simplex in \( K \) . Let \( {q}_{ij} \) be the midpoint of \( {q}_{i}{q}_{j} \) . Define \( \overline{\gamma } : {S}^{1} \rightarrow  \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \) by sending the segment \( {q}_{i}{q}_{j} \) to the segment \( {U}_{\alpha \left( i\right) }{U}_{\alpha \left( j\right) } \) ; it follows that \( \overline{\gamma }\left( {q}_{i}\right)  = \; {U}_{\alpha \left( i\right) } \) and \( {f}_{ * }\left( \overline{\gamma }\right) \left( {q}_{i}\right)  = {p}_{\alpha \left( i\right) } \) .

Next define a map \( F \) on the sides of the square \( {I}^{2} \) by (see Figure 13.8)

\[
{\left. F\right| }_{\text{ bottom side }} = F\left( {x,0}\right)  = \gamma \left( x\right) ,
\]

\[
{\left. F\right| }_{\text{ top side }} = F\left( {x,1}\right)  = {f}_{ * }\overline{\gamma }\left( x\right) ,
\]

and

\[
{\left. F\right| }_{\text{ vertical sides }} = F\left( {0, t}\right)  = F\left( {1, t}\right)  = {p}_{0}.
\]

The problem now is to extend \( F : \partial {I}^{2} \rightarrow  X \) to the entire square. Subdivide the square by joining with vertical segments the vertices \( \left( {{q}_{i},0}\right) ,\left( {{q}_{ij},0}\right) \) on the bottom edge to the corresponding vertices on the top edge. Since \( F\left( {{q}_{i},0}\right)  = \gamma \left( {q}_{i}\right) \) and \( F\left( {{q}_{i},1}\right)  = {f}_{ * }\widetilde{\gamma }\left( {q}_{i}\right)  = {p}_{\alpha \left( i\right) } \) , they both lie in \( {U}_{\alpha \left( i\right) } \) . Since \( {U}_{\alpha \left( i\right) } \) is contractible, by the extension principle \( F \) can be extended to the

![bo_d7b6f8alb0pc73dd9avg_160_625_305_397_391_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_160_625_305_397_391_0.jpg)

Figure 13.8

vertical segment \( \left\{  {q}_{i}\right\}   \times  I \) . Similarly, \( F \) can be extended to the vertical segment \( \left\{  {q}_{ij}\right\}   \times  I \) . Thus in Figure 13.8, \( F \) is defined on the boundary of each rectangle and maps that boundary entirely into a contractible open set \( {U}_{\alpha } \) . By the extension principle again, \( F \) can be extended over each rectangle. In this way \( F \) is extended to the entire square \( {I}^{2} \) .

STEP 2 (Injectivity of \( {f}_{ * } \) ). Suppose \( \gamma  : I \rightarrow  \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \) is a loop such that \( {f}_{ * }\left( \gamma \right) \) is null-homotopic in \( X \) . This means there is a map \( H \) from the square \( {I}^{2} \) to \( X \) as in Figure 13.9.

![bo_d7b6f8alb0pc73dd9avg_160_629_1140_398_402_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_160_629_1140_398_402_0.jpg)

Figure 13.9

By the simplicial approximation theorem we may assume that \( \gamma \) is a simplicial map from some subdivision \( L \) of the top edge of the square to \( \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \) . Now subdivide the square \( {I}^{2} \) repeatedly to get a triangulation \( K \) with the property that if \( {q}_{i} \) is a vertex of \( K \) and \( \operatorname{st}\left( {q}_{i}\right) \) is the star of \( {q}_{i} \) in the barycentric subdivision \( {K}^{\prime } \) , then

\[
H\left( {\operatorname{st}\left( {q}_{i}\right) }\right)  \subset  {U}_{\alpha \left( i\right) }
\]

for some open set \( {U}_{\alpha \left( i\right) } \) in \( \mathfrak{U} \) . In the process of the subdivision new vertices are introduced on the top edge only by repeated bisection of the edge; furthermore, the function \( \alpha \) on the vertices of the top edge may be chosen as follows. Consider for example the 1-simplex \( {q}_{1}{q}_{2} \) . If \( {q}_{k} \) is a new vertex to the left of the midpoint \( {q}_{12} \) , choose \( \alpha \left( k\right)  = \alpha \left( 1\right) \) ; otherwise, choose \( \alpha \left( k\right)  = \alpha \left( 2\right) \) .

Define

\[
\bar{H} : {I}^{2} = \left| K\right|  \rightarrow  \left| {{N}_{2}^{\prime }\left( \mathcal{U}\right) }\right|
\]

to be the simplicial map with

\[
\bar{H}\left( {q}_{i}\right)  = {U}_{\alpha \left( i\right) }.
\]

The restriction \( \beta \) of \( \bar{H} \) to the top edge of the square agrees with \( \gamma \) on the vertices of \( L \) . Furthermore, by construction \( \beta \) is homotopic to \( \gamma \) in \( \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \) , and \( \bar{H} \) is a null-homotopy for \( \beta \) . Therefore, \( {f}_{ * } : {\pi }_{1}\left( \left| {{N}_{2}\left( \mathfrak{U}\right) }\right| \right)  \rightarrow  {\pi }_{1}\left( X\right) \) is injective. Since the nerve \( N\left( \mathfrak{U}\right) \) and its 2-skeleton \( {N}_{2}\left( \mathfrak{U}\right) \) have the same fundamental group (Remark 13.3 (a)), the theorem is proved.

## Examples of Monodromy

EXAMPLE 13.5. Let \( {S}^{1} \) be the unit circle in the complex plane with good cover \( \mathfrak{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) as in Figure 13.10. The map \( \pi  : z \rightarrow  {z}^{2} \) defines a fiber bundle \( \pi  : {S}^{1} \rightarrow  {S}^{1} \) each of whose fibers consists of two distinct points. Let \( F = \{ A, B\} \) be the fiber above the point 1 . The cohomology \( {H}^{ * }\left( F\right) \) consists of all functions on \( \{ A, B\} \) , i.e., \( {H}^{ * }\left( F\right)  = \left\{  {\left( {a, b}\right)  \in  {\mathbb{R}}^{2}}\right\} \) .

Fix an isomorphism \( {H}^{ * }\left( {{\pi }^{-1}{U}_{0}}\right)  \simeq  {H}^{ * }\left( F\right) \) . We have the diagram

![bo_d7b6f8alb0pc73dd9avg_161_644_1164_355_789_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_161_644_1164_355_789_0.jpg)

If we start with a generator, say \( \left( {1,0}\right) \) , of \( {H}^{ * }\left( F\right) \) and follow it around the diagram, we do not end up with the same generator; in fact, we get \( \left( {0,1}\right) \) . In general \( \left( {a, b}\right) \) goes to \( \left( {b, a}\right) \) . Therefore the presheaf \( {\mathcal{H}}^{ * }\left( U\right)  = {H}^{ * }\left( {{\pi }^{-1}U}\right) \) is not a constant presheaf.

![bo_d7b6f8alb0pc73dd9avg_162_283_301_1089_430_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_162_283_301_1089_430_0.jpg)

Figure 13.10

Exercise 13.6. Since \( {H}_{d} \) of the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) in Example 13.5 has only one nonzero row, we see by the generalized Mayer-Vietoris principle and Proposition 12.1 that

\[
{H}^{ * }\left( {S}^{1}\right)  = {H}_{D}^{ * }\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) }\right\}   = {H}_{\delta }{H}_{d} = {H}^{ * }\left( {\mathfrak{U},{\mathcal{H}}^{0}}\right) .
\]

Compute the Čech cohomology \( {H}^{ * }\left( {\mathfrak{U},{\mathcal{H}}^{0}}\right) \) directly.

Example 13.7. The universal covering \( \pi  : {\mathbb{R}}^{1} \rightarrow  {S}^{1} \) given by \( \pi \left( x\right)  = {e}^{2\pi ix} \) is a fiber bundle with fiber a countable set of points. The action of the loop downstairs on the homology \( {H}_{0} \) (fiber) is translation by \( 1 : x \mapsto  x + 1 \) . In cohomology a loop downstairs sends the function on the fiber with support at \( x \) to the function with support at \( x + 1 \) . (See Figure 13.11.)

![bo_d7b6f8alb0pc73dd9avg_162_666_1302_317_614_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_162_666_1302_317_614_0.jpg)

Figure 13.11

Exercise 13.8. As in Example 13.5, with \( \mathfrak{U} \) being the usual good cover of \( {S}^{1} \) ,

\[
{H}^{ * }\left( {\mathbb{R}}^{1}\right)  = {H}_{D}^{ * }\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) }\right\}   = {H}_{\delta }{H}_{d} = {H}^{ * }\left( {\mathfrak{U},{\mathcal{H}}^{0}}\right) .
\]

Compute \( {H}^{ * }\left( {\mathfrak{U},{\mathcal{H}}^{0}}\right) \) directly.

EXAMPLE 13.9. In the previous two examples, the fundamental group of the base acts on \( {H}_{0} \) of the fiber. We now give an example in which it acts on \( {H}_{2} \) .

The wedge \( {S}^{m} \vee  {S}^{n} \) of two spheres \( {S}^{m} \) and \( {S}^{n} \) is the union of \( {S}^{m} \) and \( {S}^{n} \) with one point identified. Let \( X \) be \( {S}^{1} \vee  {S}^{2} \) as shown in Figure 13.12 and let \( \widetilde{X} \) be the universal covering of \( X \) . Note that although \( {H}^{ * }\left( X\right) \) is finite, \( {H}^{ * }\left( \widetilde{X}\right) \) is infinite. We define a fiber bundle over the circle \( {S}^{1} \) with fiber \( \widetilde{X} \) by setting.

\[
E = \widetilde{X} \times  I/\left( {x,0}\right)  \sim  \left( {s\left( x\right) ,1}\right)
\]

where \( s \) is the deck transformation of the universal cover \( \widetilde{X} \) which shifts everything one unit up. The projection \( \pi  : E \rightarrow  {S}^{1} \) is given by \( \pi \left( {\widetilde{x}, t}\right)  = t \) . The fundamental group of the base \( {\pi }_{1}\left( {S}^{1}\right) \) acts on \( {H}_{2} \) (fiber) by shifting each sphere one up.

Exercise 13.10. Find the homotopy type of the space \( E \) .

![bo_d7b6f8alb0pc73dd9avg_163_260_1029_1132_1042_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_163_260_1029_1132_1042_0.jpg)

Figure 13.12
