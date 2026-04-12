# 2.3 The Formal Viewpoint

Sometimes it is good to step back from the forest of details and look for general patterns. In this rather brief section we will first describe the general pattern of homology by axioms, then we will look at some common formal features shared by many of the constructions we have made, using the language of categories and functors which has become common in much of modern mathematics.

## Axioms for Homology

For simplicity let us restrict attention to CW complexes and focus on reduced homology to avoid mentioning relative homology. A (reduced) homology theory assigns to each nonempty CW complex \( X \) a sequence of abelian groups \( {\widetilde{h}}_{n}\left( X\right) \) and to each map \( f : X \rightarrow  Y \) between CW complexes a sequence of homomorphisms \( {f}_{ * } : {\widetilde{h}}_{n}\left( X\right)  \rightarrow  {\widetilde{h}}_{n}\left( Y\right) \) such that \( {\left( fg\right) }_{ * } = {f}_{ * }{g}_{ * } \) and \( {\mathbb{1}}_{ * } = \mathbb{1} \) , and so that the following three axioms are satisfied.

(1) If \( f \simeq  g : X \rightarrow  Y \) , then \( {f}_{ * } = {g}_{ * } : {\widetilde{h}}_{n}\left( X\right)  \rightarrow  {\widetilde{h}}_{n}\left( Y\right) \) .

(2) There are boundary homomorphisms \( \partial  : {\widetilde{h}}_{n}\left( {X/A}\right)  \rightarrow  {\widetilde{h}}_{n - 1}\left( A\right) \) defined for each CW pair \( \left( {X, A}\right) \) , fitting into an exact sequence

\[
\cdots \overset{\partial }{ \rightarrow  }{\widetilde{h}}_{n}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }{\widetilde{h}}_{n}\left( X\right) \overset{{q}_{ * }}{ \rightarrow  }{\widetilde{h}}_{n}\left( {X/A}\right) \overset{\partial }{ \rightarrow  }{\widetilde{h}}_{n - 1}\left( A\right) \overset{{i}_{ * }}{ \rightarrow  }\cdots
\]

where \( i \) is the inclusion and \( q \) is the quotient map. Furthermore the boundary maps are natural: For \( f : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) inducing a quotient map \( \bar{f} : X/A \rightarrow  Y/B \) , there are commutative diagrams

![bo_d7dtv0s91nqc73eq8nv0_168_669_1437_456_208_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_168_669_1437_456_208_0.jpg)

(3) For a wedge sum \( X = \mathop{\bigvee }\limits_{\alpha }{X}_{\alpha } \) with inclusions \( {i}_{\alpha } : {X}_{\alpha } \hookrightarrow  X \) , the direct sum map \( { \oplus  }_{\alpha }{i}_{\alpha  * } : { \oplus  }_{\alpha }{\widetilde{h}}_{n}\left( {X}_{\alpha }\right)  \rightarrow  {\widetilde{h}}_{n}\left( X\right) \) is an isomorphism for each \( n \) .

Negative values for the subscripts \( n \) are permitted. Ordinary singular homology is zero in negative dimensions by definition, but interesting homology theories with nontrivial groups in negative dimensions do exist.

The third axiom may seem less substantial than the first two, and indeed for finite wedge sums it can be deduced from the first two axioms, though not in general for infinite wedge sums, as an example in the Exercises shows.

It is also possible, and not much more difficult, to give axioms for unreduced homology theories. One supposes one has relative groups \( {h}_{n}\left( {X, A}\right) \) defined, specializing to absolute groups by setting \( {h}_{n}\left( X\right)  = {h}_{n}\left( {X,\varnothing }\right) \) . Axiom (1) is replaced by its obvious relative form, and axiom (2) is broken into two parts, the first hypothesizing a long exact sequence involving these relative groups, with natural boundary maps, the second stating some version of excision, for example \( {h}_{n}\left( {X, A}\right)  \approx  {h}_{n}\left( {X/A, A/A}\right) \) if one is dealing with CW pairs. In axiom (3) the wedge sum is replaced by disjoint union.

These axioms for unreduced homology are essentially the same as those originally laid out in the highly influential book [Eilenberg & Steenrod 1952], except that axiom (3) was omitted since the focus there was on finite complexes, and there was another axiom specifying that the groups \( {h}_{n}\left( \text{ point }\right) \) are zero for \( n \neq  0 \) , as is true for singular homology. This axiom was called the 'dimension axiom', presumably because it specifies that a point has nontrivial homology only in dimension zero. It can be regarded as a normalization axiom, since one can trivially define a homology theory where it fails by setting \( {h}_{n}\left( {X, A}\right)  = {H}_{n + k}\left( {X, A}\right) \) for a fixed nonzero integer \( k \) . At the time there were no interesting homology theories known for which the dimension axiom did not hold, but soon thereafter topologists began studying a homology theory called 'bordism' having the property that the bordism groups of a point are nonzero in infinitely many dimensions. Axiom (3) seems to have appeared first in [Milnor 1962].

Reduced and unreduced homology theories are essentially equivalent. From an unreduced theory \( h \) one gets a reduced theory \( \widetilde{h} \) by setting \( {\widetilde{h}}_{n}\left( X\right) \) equal to the kernel of the canonical map \( {h}_{n}\left( X\right)  \rightarrow  {h}_{n}\left( \text{ point }\right) \) . In the other direction, one sets \( {h}_{n}\left( X\right)  = {\widetilde{h}}_{n}\left( {X}_{ + }\right) \) where \( {X}_{ + } \) is the disjoint union of \( X \) with a point. We leave it as an exercise to show that these two transformations between reduced and unreduced homology are inverses of each other. Just as with ordinary homology, one has \( {h}_{n}\left( X\right)  \approx  {\widetilde{h}}_{n}\left( X\right)  \oplus  {h}_{n}\left( {x}_{0}\right) \) for any point \( {x}_{0} \in  X \) , since the long exact sequence of the pair \( \left( {X,{x}_{0}}\right) \) splits via the retraction of \( X \) onto \( {x}_{0} \) . Note that \( {\widetilde{h}}_{n}\left( {x}_{0}\right)  = 0 \) for all \( n \) , as can be seen by looking at the long exact sequence of reduced homology groups of the pair \( \left( {{x}_{0},{x}_{0}}\right) \) .

The groups \( {h}_{n}\left( {x}_{0}\right)  \approx  {\widetilde{h}}_{n}\left( {S}^{0}\right) \) are called the coefficients of the homology theories \( h \) and \( \widetilde{h} \) , by analogy with the case of singular homology with coefficients. One can trivially realize any sequence of abelian groups \( {G}_{i} \) as the coefficient groups of a homology theory by setting \( {h}_{n}\left( {X, A}\right)  = {\bigoplus }_{i}{H}_{n - i}\left( {X, A;{G}_{i}}\right) \) .

In general, homology theories are not uniquely determined by their coefficient groups, but this is true for singular homology: If \( h \) is a homology theory defined for CW pairs, whose coefficient groups \( {h}_{n}\left( {x}_{0}\right) \) are zero for \( n \neq  0 \) , then there are natural isomorphisms \( {h}_{n}\left( {X, A}\right)  \approx  {H}_{n}\left( {X, A;G}\right) \) for all CW pairs \( \left( {X, A}\right) \) and all \( n \) , where \( G = {h}_{0}\left( {x}_{0}\right) \) . This will be proved in Theorem 4.59.

We have seen how Mayer-Vietoris sequences can be quite useful for singular homology, and in fact every homology theory has Mayer-Vietoris sequences, at least for CW complexes. These can be obtained directly from the axioms in the following way. For a CW complex \( X = A \cup  B \) with \( A \) and \( B \) subcomplexes, the inclusion \( \left( {B, A \cap  B}\right)  \hookrightarrow  \left( {X, A}\right) \) induces a commutative diagram of exact sequences

\[
\cdots  \rightarrow  {h}_{n + 1}\left( {B, A \cap  B}\right)  \rightarrow  {h}_{n}\left( {A \cap  B}\right)  \rightarrow  {h}_{n}\left( B\right)  \rightarrow  {h}_{n}\left( {B, A \cap  B}\right)  \rightarrow  \cdots
\]

\[
\downarrow   \approx  \; \downarrow  \; \downarrow  \; \downarrow   \approx
\]

\[
\cdots  \rightarrow  {h}_{n + 1}\left( {X, A}\right)  \rightarrow  {h}_{n}\left( A\right)  \rightarrow  {h}_{n}\left( X\right)  \rightarrow  {h}_{n}\left( {X, A}\right)  \rightarrow  \cdots
\]

The vertical maps between relative groups are isomorphisms since \( B/\left( {A \cap  B}\right)  = X/A \) . Then it is a purely algebraic fact, whose proof is Exercise 38 at the end of the previous section, that a diagram such as this with every third vertical map an isomorphism gives rise to a long exact sequence involving the remaining nonisomorphic terms. In the present case this takes the form of a Mayer-Vietoris sequence

\[
\cdots  \rightarrow  {h}_{n}\left( {A \cap  B}\right) \overset{\varphi }{ \rightarrow  }{h}_{n}\left( A\right)  \oplus  {h}_{n}\left( B\right) \overset{\psi }{ \rightarrow  }{h}_{n}\left( X\right) \overset{\partial }{ \rightarrow  }{h}_{n - 1}\left( {A \cap  B}\right)  \rightarrow  \cdots
\]

## Categories and Functors

Formally, singular homology can be regarded as a sequence of functions \( {H}_{n} \) that assign to each space \( X \) an abelian group \( {H}_{n}\left( X\right) \) and to each map \( f : X \rightarrow  Y \) a homomorphism \( {H}_{n}\left( f\right)  = {f}_{ * } : {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) , and similarly for relative homology groups. This sort of situation arises quite often, and not just in algebraic topology, so it is useful to introduce some general terminology for it. Roughly speaking, 'functions' like \( {H}_{n} \) are called ’functors’, and the domains and ranges of these functors are called ’categories’. Thus for \( {H}_{n} \) the domain category consists of topological spaces and continuous maps, or in the relative case, pairs of spaces and continuous maps of pairs, and the range category consists of abelian groups and homomorphisms. A key point is that one is interested not only in the objects in the category, for example spaces or groups, but also in the maps, or 'morphisms', between these objects.

Now for the precise definitions. A category \( \mathcal{C} \) consists of three things:

(1) A collection \( \mathrm{{Ob}}\left( \mathcal{C}\right) \) of objects.

(2) Sets \( \operatorname{Mor}\left( {X, Y}\right) \) of morphisms for each pair \( X, Y \in  \mathrm{{Ob}}\left( \mathcal{C}\right) \) , including a distinguished ’identity’ morphism \( \mathbb{1} = {\mathbb{1}}_{X} \in  \operatorname{Mor}\left( {X, X}\right) \) for each \( X \) .

(3) A ’composition of morphisms’ function \( \circ   : \operatorname{Mor}\left( {X, Y}\right)  \times  \operatorname{Mor}\left( {Y, Z}\right)  \rightarrow  \operatorname{Mor}\left( {X, Z}\right) \) for each triple \( X, Y, Z \in  \mathrm{{Ob}}\left( \mathcal{C}\right) \) , satisfying \( f \circ  \mathbb{1} = f,\mathbb{1} \circ  f = f \) , and \( \left( {f \circ  g}\right)  \circ  h = \; f \circ  \left( {g \circ  h}\right) \) .

There are plenty of obvious examples, such as:

- The category of topological spaces, with continuous maps as the morphisms. Or we could restrict to special classes of spaces such as CW complexes, keeping continuous maps as the morphisms. We could also restrict the morphisms, for example to homeomorphisms.

- The category of groups, with homomorphisms as morphisms. Or the subcategory of abelian groups, again with homomorphisms as the morphisms. Generalizing this is the category of modules over a fixed ring, with morphisms the module homomorphisms.

- The category of sets, with arbitrary functions as the morphisms. Or the morphisms could be restricted to injections, surjections, or bijections.

There are also many categories where the morphisms are not simply functions, for example:

- Any group \( G \) can be viewed as a category with only one object and with \( G \) as the morphisms of this object, so that condition (3) reduces to two of the three axioms for a group. If we require only these two axioms, associativity and a left and right identity, we have a 'group without inverses', usually called a monoid since it is the same thing as a category with one object.

- A partially ordered set \( \left( {X, \leq  }\right) \) can be considered a category where the objects are the elements of \( X \) and there is a unique morphism from \( x \) to \( y \) whenever \( x \leq  y \) . The relation \( x \leq  x \) gives the morphism 11 and transitivity gives the composition \( \operatorname{Mor}\left( {x, y}\right)  \times  \operatorname{Mor}\left( {y, z}\right)  \rightarrow  \operatorname{Mor}\left( {x, z}\right) \) . The condition that \( x \leq  y \) and \( y \leq  x \) implies \( x = y \) says that there is at most one morphism between any two objects.

- There is a 'homotopy category' whose objects are topological spaces and whose morphisms are homotopy classes of maps, rather than actual maps. This uses the fact that composition is well-defined on homotopy classes: \( {f}_{0}{g}_{0} \simeq  {f}_{1}{g}_{1} \) if \( {f}_{0} \simeq  {f}_{1} \) and \( {g}_{0} \simeq  {g}_{1} \) .

- Chain complexes are the objects of a category, with chain maps as morphisms. This category has various interesting subcategories, obtained by restricting the objects. For example, we could take chain complexes whose groups are zero in negative dimensions, or zero outside a finite range. Or we could restrict to exact sequences, or short exact sequences. In each case we take morphisms to be chain maps, which are commutative diagrams. Going a step further, there is a category whose objects are short exact sequences of chain complexes and whose morphisms are commutative diagrams of maps between such short exact sequences.

A functor \( F \) from a category \( \mathcal{C} \) to a category \( \mathcal{D} \) assigns to each object \( X \) in \( \mathcal{C} \) an object \( F\left( X\right) \) in \( \mathcal{D} \) and to each morphism \( f \in  \operatorname{Mor}\left( {X, Y}\right) \) in \( \mathcal{C} \) a morphism \( F\left( f\right)  \in \; \operatorname{Mor}\left( {F\left( X\right) , F\left( Y\right) }\right) \) in \( \mathcal{D} \) , such that \( F\left( \mathbb{1}\right)  = \mathbb{1} \) and \( F\left( {f \circ  g}\right)  = F\left( f\right)  \circ  F\left( g\right) \) . In the case of the singular homology functor \( {H}_{n} \) , the latter two conditions are the familiar properties \( {\mathbb{1}}_{ * } = \mathbb{1} \) and \( {\left( fg\right) }_{ * } = {f}_{ * }{g}_{ * } \) of induced maps. Strictly speaking, what we have just defined is a covariant functor. A contravariant functor would differ from this by assigning to \( f \in  \operatorname{Mor}\left( {X, Y}\right) \) a ’backwards’ morphism \( F\left( f\right)  \in  \operatorname{Mor}\left( {F\left( Y\right) , F\left( X\right) }\right) \) with \( F\left( \mathbb{1}\right)  = \mathbb{1} \) and \( F\left( {f \circ  g}\right)  = F\left( g\right)  \circ  F\left( f\right) \) . A classical example of this is the dual vector space functor, which assigns to a vector space \( V \) over a fixed scalar field \( K \) the dual vector space \( F\left( V\right)  = {V}^{ * } \) of linear maps \( V \rightarrow  K \) , and to each linear transformation \( f : V \rightarrow  W \) the dual map \( F\left( f\right)  = {f}^{ * } : {W}^{ * } \rightarrow  {V}^{ * } \) , going in the reverse direction. In the next chapter we will study the contravariant version of homology, called cohomology.

A number of the constructions we have studied in this chapter are functors:

- The singular chain complex functor assigns to a space \( X \) the chain complex of singular chains in \( X \) and to a map \( f : X \rightarrow  Y \) the induced chain map. This is a functor from the category of spaces and continuous maps to the category of chain complexes and chain maps.

- The algebraic homology functor assigns to a chain complex its sequence of homology groups and to a chain map the induced homomorphisms on homology. This is a functor from the category of chain complexes and chain maps to the category whose objects are sequences of abelian groups and whose morphisms are sequences of homomorphisms.

- The composition of the two preceding functors is the functor assigning to a space its singular homology groups.

- The first example above, the singular chain complex functor, can itself be regarded as the composition of two functors. The first functor assigns to a space \( X \) its singular complex \( S\left( X\right) \) , a \( \Delta \) -complex, and the second functor assigns to a \( \Delta \) -complex its simplicial chain complex. This is what the two functors do on objects, and what they do on morphisms can be described in the following way. A map of spaces \( f : X \rightarrow  Y \) induces a map \( {f}_{ * } : S\left( X\right)  \rightarrow  S\left( Y\right) \) by composing singular simplices \( {\Delta }^{n} \rightarrow  X \) with \( f \) . The map \( {f}_{ * } \) is a map between \( \Delta \) -complexes taking the distinguished characteristic maps in the domain \( \Delta \) -complex to the distinguished characteristic maps in the target \( \Delta \) -complex. Call such maps \( \Delta \) -maps and let them be the morphisms in the category of \( \Delta \) -complexes. Note that a \( \Delta \) -map induces a chain map between simplicial chain complexes, taking basis elements to basis elements, so we have a simplicial chain complex functor taking the category of \( \Delta \) -complexes and \( \Delta \) -maps to the category of chain complexes and chain maps.

- There is a functor assigning to a pair of spaces \( \left( {X, A}\right) \) the associated long exact sequence of homology groups. Morphisms in the domain category are maps of pairs, and in the target category morphisms are maps between exact sequences forming commutative diagrams. This functor is the composition of two functors, the first assigning to \( \left( {X, A}\right) \) a short exact sequence of chain complexes, the second assigning to such a short exact sequence the associated long exact sequence of homology groups. Morphisms in the intermediate category are the evident commutative diagrams.

Another sort of process we have encountered is the transformation of one functor into another, for example:

- Boundary maps \( {H}_{n}\left( {X, A}\right)  \rightarrow  {H}_{n - 1}\left( A\right) \) in singular homology, or indeed in any homology theory.

- Change-of-coefficient homomorphisms \( {H}_{n}\left( {X;{G}_{1}}\right)  \rightarrow  {H}_{n}\left( {X;{G}_{2}}\right) \) induced by a homomorphism \( {G}_{1} \rightarrow  {G}_{2} \) , as in the proof of Lemma 2.49.

In general, if one has two functors \( F, G : \mathcal{C} \rightarrow  \mathcal{D} \) then a natural transformation \( T \) from \( F \) to \( G \) assigns a morphism \( {T}_{X} : F\left( X\right)  \rightarrow  G\left( X\right) \) to each object \( X \in  \mathcal{C} \) , in such a way that for each morphism \( f : X \rightarrow  Y \) in \( \mathcal{C} \) the square at the right commutes. The case that \( F \) and \( G \) are contravariant rather than covariant is similar.

![bo_d7dtv0s91nqc73eq8nv0_173_1237_317_350_203_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_173_1237_317_350_203_0.jpg)

We have been describing the passage from topology to the abstract world of categories and functors, but there is also a nice path in the opposite direction:

- To each category \( \mathcal{C} \) there is associated a \( \Delta \) -complex \( B\mathcal{C} \) called the classifying space of \( \mathcal{C} \) , whose \( n \) -simplices are the strings \( {X}_{0} \rightarrow  {X}_{1} \rightarrow  \cdots  \rightarrow  {X}_{n} \) of morphisms in \( \mathcal{C} \) . The faces of this simplex are obtained by deleting an \( {X}_{i} \) , and then composing the two adjacent morphisms if \( i \neq  0, n \) . Thus when \( n = 2 \) the three faces of \( {X}_{0} \rightarrow  {X}_{1} \rightarrow  {X}_{2} \) are \( {X}_{0} \rightarrow  {X}_{1},{X}_{1} \rightarrow  {X}_{2} \) , and the composed morphism \( {X}_{0} \rightarrow  {X}_{2} \) . In case \( \mathcal{C} \) has a single object and the morphisms of \( \mathcal{C} \) form a group \( G \) , then \( B\mathcal{C} \) is the same as the \( \Delta \) -complex \( {BG} \) constructed in Example 1B.7, a \( K\left( {G,1}\right) \) . In general, the space \( {BC} \) need not be a \( K\left( {G,1}\right) \) , however. For example, if we start with a \( \Delta \) -complex \( X \) and regard its set of simplices as a partially ordered set \( \mathcal{C}\left( X\right) \) under the relation of inclusion of faces, then \( B\mathcal{C}\left( X\right) \) is the barycentric subdivision of \( X \) .

- A functor \( F : \mathcal{C} \rightarrow  \mathcal{D} \) induces a map \( B\mathcal{C} \rightarrow  B\mathcal{D} \) . This is the \( \Delta \) -map that sends an \( n \) -simplex \( {X}_{0} \rightarrow  {X}_{1} \rightarrow  \cdots  \rightarrow  {X}_{n} \) to the \( n \) -simplex \( F\left( {X}_{0}\right)  \rightarrow  F\left( {X}_{1}\right)  \rightarrow  \cdots  \rightarrow  F\left( {X}_{n}\right) \) .

- A natural transformation from a functor \( F \) to a functor \( G \) induces a homotopy between the induced maps of classifying spaces. We leave this for the reader to make explicit, using the subdivision of \( {\Delta }^{n} \times  I \) into \( \left( {n + 1}\right) \) -simplices described earlier in the chapter.

## Exercises

1. If \( {T}_{n}\left( {X, A}\right) \) denotes the torsion subgroup of \( {H}_{n}\left( {X, A;\mathbb{Z}}\right) \) , show that the functors \( \left( {X, A}\right)  \mapsto  {T}_{n}\left( {X, A}\right) \) , with the obvious induced homomorphisms \( {T}_{n}\left( {X, A}\right)  \rightarrow  {T}_{n}\left( {Y, B}\right) \) and boundary maps \( {T}_{n}\left( {X, A}\right)  \rightarrow  {T}_{n - 1}\left( A\right) \) , do not define a homology theory. Do the same for the ’mod torsion’ functor \( M{T}_{n}\left( {X, A}\right)  = {H}_{n}\left( {X, A;\mathbb{Z}}\right) /{T}_{n}\left( {X, A}\right) \) .

2. Define a candidate for a reduced homology theory on CW complexes by \( {\widetilde{h}}_{n}\left( X\right)  = \; \mathop{\prod }\limits_{i}{\widetilde{H}}_{i}\left( X\right) /{\bigoplus }_{i}{\widetilde{H}}_{i}\left( X\right) \) . Thus \( {\widetilde{h}}_{n}\left( X\right) \) is independent of \( n \) and is zero if \( X \) is finite-dimensional, but is not identically zero, for example for \( X = \mathop{\bigvee }\limits_{i}{S}^{i} \) . Show that the axioms for a homology theory are satisfied except that the wedge axiom fails.

3. Show that if \( \widetilde{h} \) is a reduced homology theory, then \( {\widetilde{h}}_{n}\left( \text{ point }\right)  = 0 \) for all \( n \) . Deduce that there are suspension isomorphisms \( {\widetilde{h}}_{n}\left( X\right)  \approx  {\widetilde{h}}_{n + 1}\left( {SX}\right) \) for all \( n \) .

4. Show that the wedge axiom for homology theories follows from the other axioms in the case of finite wedge sums.

## Additional Topics
