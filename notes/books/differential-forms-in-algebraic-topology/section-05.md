## §5 The Mayer-Vietoris Argument

The Mayer-Vietoris sequence relates the cohomology of a union to those of the subsets. Together with the Five Lemma, this gives a method of proof which proceeds by induction on the cardinality of an open cover, called the Mayer-Vietoris argument. As evidence of its power and versatility, we derive from it the finite dimensionality of the de Rham cohomology, Poincaré duality, the Künneth formula, the Leray-Hirsch theorem, and the Thom isomorphism, all for manifolds with finite good covers.

## Existence of a Good Cover

Let \( M \) be a manifold of dimension \( n \) . An open cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) of \( M \) is called a good cover if all nonempty finite intersections \( {U}_{{\alpha }_{0}} \cap  \cdots  \cap  {U}_{{\alpha }_{p}} \) are diffeomorphic to \( {\mathbb{R}}^{n} \) . A manifold which has a finite good cover is said to be of finite type.

Theorem 5.1. Every manifold has a good cover. If the manifold is compact, then the cover may be chosen to be finite.

To prove this theorem we will need a little differential geometry. A Riemannian structure on a manifold \( M \) is a smoothly varying metric \( \langle \) , \( \rangle \) on the tangent space of \( M \) at each point; it is smoothly varying in the following sense: if \( X \) and \( Y \) are two smooth vector fields on \( M \) , then \( \langle X, Y\rangle \) is a smooth function on \( M \) . Every manifold can be given a Riemannian structure by the following splicing procedure. Let \( \left\{  {U}_{\alpha }\right\} \) be a coordinate open cover of \( M,\langle ,{\rangle }_{\alpha } \) a Riemannian metric on \( {U}_{\alpha } \) , and \( \left\{  {\rho }_{\alpha }\right\} \) a partition of unity subordinate to \( \left\{  {U}_{\alpha }\right\} \) . Then \( \langle \) , \( \rangle  = \sum {\rho }_{\alpha }\langle \) , \( {\rangle }_{\alpha } \) is a Riemannian metric on \( M \) .

Proof of Theorem 5.1. Endow \( M \) with a Riemannian structure. Now we quote the theorem in differential geometry that every point in a Riemannian manifold has a geodesically convex neighborhood (Spivak [1, Ex. 32(f), p. 491]). The intersection of any two such neighborhoods is again geodesically convex. Since a geodesically convex neighborhood in a Riemannian manifold of dimension \( n \) is diffeomorphic to \( {\mathbb{R}}^{n} \) , an open cover consisting of geodesically convex neighborhoods will be a good cover.

Given two covers \( \mathfrak{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) and \( \mathfrak{B} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) , if every \( {V}_{\beta } \) is contained in some \( {U}_{\alpha } \) , we say that \( \mathfrak{B} \) is a refinement of \( \mathfrak{U} \) and write \( \mathfrak{U} < \mathfrak{B} \) . To be more precise we specify a refinement by a map \( \phi  : J \rightarrow  I \) such that \( {V}_{\beta } \subset  {U}_{\phi \left( \beta \right) } \) . By a slight modification of the above proof we can show that every open cover on a manifold has a refinement which is a good cover: simply take the geodesically convex neighborhoods around each point to be inside some open set of the given cover.

A directed set is a set \( I \) with a relation \( < \) satisfying

(a) (reflexivity) \( a < a \) for all \( a \in  I \) .

(b) (transitivity) if \( a < b \) and \( b < c \) , then \( a < c \) .

(c) (upper bound) for any \( a, b \in  I \) , there is an element \( c \) in \( I \) such that \( a < c \) and \( b < c \) .

The set of open covers on a manifold is a directed set, since any two open covers always have a common refinement. A subset \( J \) of a directed set \( I \) is cofinal in \( I \) if for every \( i \) in \( I \) there is a \( j \) in \( J \) such that \( i < j \) . It is clear that \( J \) is also a directed set.

Corollary 5.2. The good covers are cofinal in the set of all covers of a manifold M.

Finite Dimensionality of de Rham Cohomology

Proposition 5.3.1. If the manifold \( M \) has a finite good cover, then its cohomology is finite dimensional.

Proof. From the Mayer-Vietoris sequence

\[
\cdots  \rightarrow  {H}^{q - 1}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{q}\left( {U \cup  V}\right) \overset{r}{ \rightarrow  }{H}^{q}\left( U\right) \bigoplus {H}^{q}\left( V\right)  \rightarrow  \cdots
\]

we get

\[
{H}^{q}\left( {U \cup  V}\right)  \simeq  \ker r \oplus  \operatorname{im}r \simeq  \operatorname{im}{d}^{ * } \oplus  \operatorname{im}r.
\]

Thus,

(*) if \( {H}^{q}\left( U\right) ,{H}^{q}\left( V\right) \) and \( {H}^{q - 1}\left( {U \cap  V}\right) \) are finite-dimensional, then so is \( {H}^{q}\left( {U \cup  V}\right) \) .

For a manifold which is diffeomorphic to \( {\mathbb{R}}^{n} \) , the finite dimensionality of \( {H}^{ * }\left( M\right) \) follows from the Poincaré lemma (4.1.1). We now proceed by induction on the cardinality of a good cover. Suppose the cohomology of any manifold having a good cover with at most \( p \) open sets is finite dimensional. Consider a manifold having a good cover \( \left\{  {{U}_{0},\ldots ,{U}_{p}}\right\} \) with \( p + 1 \) open sets. Now \( \left( {{U}_{0} \cup  \ldots  \cup  {U}_{p - 1}}\right)  \cap  {U}_{p} \) has a good cover with \( p \) open sets, namely \( \left\{  {{U}_{0p},{U}_{1p},\ldots ,{U}_{p - 1, p}}\right\} \) . By hypothesis, the \( q \) th cohomology of \( {U}_{0} \cup  \ldots  \cup  {U}_{p - 1},{U}_{p} \) and \( \left( {{U}_{0} \cup  \ldots  \cup  {U}_{p - 1}}\right)  \cap  {U}_{p} \) are finite dimensional; from Remark (*), so is the \( q \) th cohomology of \( {U}_{0} \cup  \ldots  \cup  {U}_{p} \) . This completes the induction.

Similarly,

Proposition 5.3.2. If the manifold \( M \) has a finite good cover, then its compact cohomology is finite dimensional.

Poincaré Duality on an Orientable Manifold

A pairing between two finite-dimensional vector spaces

\[
\langle ,\rangle  : V \otimes  W \rightarrow  \mathbb{R}
\]

is said to be nondegenerate if \( \langle v, w\rangle  = 0 \) for all \( w \in  W \) implies \( v = 0 \) and \( \langle v, w\rangle  = 0 \) for all \( v \in  V \) implies \( w = 0 \) ; equivalently, the map \( v \mapsto  \langle v,\rangle \) should define an injection \( V \hookrightarrow  {W}^{ * } \) and the map \( w \mapsto  \langle , w\rangle \) also defines an injection \( W \hookrightarrow  {V}^{ * } \) .

Lemma. Let \( V \) and \( W \) be finite-dimensional vector spaces. The pairing \( \langle \) , \( \rangle  : V \otimes  W \rightarrow  \mathbb{R} \) is nondegenerate if and only if the map \( v \mapsto  \langle v \) , \( \rangle \) defines an isomorphism \( V\overset{ \sim  }{ \rightarrow  }{W}^{ * } \) .

Proof. \( \left(  \Rightarrow  \right) \) Since \( V \hookrightarrow  {W}^{ * } \) and \( W \hookrightarrow  {V}^{ * } \) are injective,

\[
\dim V \leq  \dim {W}^{ * } = \dim W \leq  \dim {V}^{ * } = \dim V
\]

hence, \( \dim V = \dim {W}^{ * } \) and \( V \hookrightarrow  {W}^{ * } \) must be an isomorphism. \( \left(  \Leftarrow  \right) \) is left to the reader.

Because the wedge product is an antiderivation, it descends to cohomology; by Stokes' theorem, integration also descends to cohomology. So for an oriented manifold \( M \) there is a pairing

\[
\int  : {H}^{q}\left( M\right)  \otimes  {H}_{c}^{n - q}\left( M\right)  \rightarrow  \mathbb{R}
\]

given by the integral of the wedge product of two forms. Our first version of Poincaré duality asserts that this pairing is nondegenerate whenever \( M \) is orientable and has a finite good cover; equivalently,

(5.4)

\[
{H}^{q}\left( M\right)  \simeq  {\left( {H}_{c}^{n - q}\left( M\right) \right) }^{ * }.
\]

Note that by (5.3.1) and (5.3.2) both \( {H}^{q}\left( M\right) \) and \( {H}_{c}^{n - q}\left( M\right) \) are finite-dimensional.

A couple of lemmas will be needed in the proof of Poincaré duality.

Exercise 5.5. Prove the Five Lemma: given a commutative diagram of Abelian groups and group homomorphisms in which the rows are exact, if the maps \( \alpha ,\beta ,\delta \) and \( \varepsilon \) are isomorphisms, then so is the middle one \( \gamma \) .

![bo_d7b6f8alb0pc73dd9avg_54_454_1929_789_236_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_54_454_1929_789_236_0.jpg)

Lemma 5.6. The two Mayer-Vietoris sequences (2.4) and (2.8) may be paired together to form a sign-commutative diagram

![bo_d7b6f8alb0pc73dd9avg_55_258_535_1105_342_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_55_258_535_1105_342_0.jpg)

Here sign-commutativity means, for instance, that

\[
{\int }_{U \cap  V}\omega  \land  {d}_{ * }\tau  =  \pm  {\int }_{U \cup  V}\left( {{d}^{ * }\omega }\right)  \land  \tau
\]

for \( \omega  \in  {H}^{q}\left( {U \cap  V}\right) ,\tau  \in  {H}_{c}^{n - q - 1}\left( {U \cup  V}\right) \) . This lemma is equivalent to saying that the pairing induces a map from the upper exact sequence to the dual of the lower exact sequence such that the following diagram is sign-commutative:

\[
\rightarrow  \;{H}^{q}\left( {U \cup  V}\right) \; \rightarrow  \;{H}^{q}\left( U\right)  \oplus  {H}^{q}\left( V\right) \; \rightarrow  \;{H}^{q}\left( {U \cap  V}\right) \; \rightarrow
\]

\[
\rightarrow  {H}_{c}^{n - q}{\left( U \cup  V\right) }^{ * } \rightarrow  {H}_{c}^{n - q}{\left( U\right) }^{ * } \oplus  {H}_{c}^{n - q}{\left( V\right) }^{ * } \rightarrow  {H}_{c}^{n - q}{\left( U \cap  V\right) }^{ * } \rightarrow  .
\]

Proof. The first two squares are in fact commutative as is straightforward to check. We will show the sign-commutativity of the third square.

Recall from (2.5) and (2.7) that \( {d}^{ * }\omega \) is a form in \( {H}^{q + 1}\left( {U \cup  V}\right) \) such that

\[
{\left. {d}^{ * }\omega \right| }_{U} =  - d\left( {{\rho }_{V}\omega }\right)
\]

\[
{\left. {d}^{ * }\omega \right| }_{V} = d\left( {{\rho }_{U}\omega }\right)
\]

and \( {d}_{ * }\tau \) is a form in \( {H}_{c}^{n - q}\left( {U \cap  V}\right) \) such that

(-(extension by 0 of \( {d}_{ * }\tau \) to \( U \) ),(extension by 0 of \( {d}_{ * }\tau \) to \( V \) ))

\[
= \left( {d\left( {{\rho }_{U}\tau }\right) , d\left( {{\rho }_{V}\tau }\right) }\right) \text{ . }
\]

Note that \( d\left( {{\rho }_{V}\tau }\right)  = \left( {d{\rho }_{V}}\right) \tau \) because \( \tau \) is closed; similarly, \( d\left( {{\rho }_{V}\omega }\right)  = \left( {d{\rho }_{V}}\right) \omega \) .

\[
{\int }_{U \cap  V}\omega  \land  {d}_{ * }\tau  = {\int }_{U \cap  V}\omega  \land  \left( {d{\rho }_{V}}\right) \tau  = {\left( -1\right) }^{\deg \omega }{\int }_{U \cap  V}\left( {d{\rho }_{V}}\right) \omega  \land  \tau .
\]

Since \( {d}^{ * }\omega \) has support in \( U \cap  V \) ,

\[
{\int }_{U \cup  V}{d}^{ * }\omega  \land  \tau  =  - {\int }_{U \cap  V}\left( {d{\rho }_{V}}\right) \omega  \land  \tau .
\]

Therefore,

\[
{\int }_{U \cap  V}\omega  \land  {d}_{ * }\tau  = {\left( -1\right) }^{\deg \omega  + 1}{\int }_{U \cup  V}{d}^{ * }\omega  \land  \tau .
\]

By the Five Lemma if Poincaré duality holds for \( U, V \) , and \( U \cap  V \) , then it holds for \( U \cup  V \) . We now proceed by induction on the cardinality of a good cover. For \( M \) diffeomorphic to \( {\mathbb{R}}^{n} \) , Poincaré duality follows from the two Poincaré lemmas

\[
{H}^{ * }\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimension }0 \\  0 & \text{ elsewhere } \end{array}\right.
\]

and

\[
{H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimension }n \\  0 & \text{ elsewhere. } \end{array}\right.
\]

Next suppose Poincaré duality holds for any manifold having a good cover with at most \( p \) open sets, and consider a manifold having a good cover \( \left\{  {{U}_{0},\ldots ,{U}_{p}}\right\} \) with \( p + 1 \) open sets. Now \( \left( {{U}_{0} \cup  \cdots  \cup  {U}_{p - 1}}\right)  \cap  {U}_{p} \) has a good cover with \( p \) open sets, namely \( \left\{  {{U}_{0p},{U}_{1p},\ldots ,{U}_{p - 1, p}}\right\} \) . By hypothesis Poincaré duality holds for \( {U}_{0} \cup  \ldots  \cup  {U}_{p - 1},\;{U}_{p} \) , and \( \left( {{U}_{0} \cup  \ldots  \cup  {U}_{p - 1}}\right) \; \cap  {U}_{p} \) , so it holds for \( {U}_{0} \cup  \ldots  \cup  {U}_{p - 1} \cup  {U}_{p} \) as well. This induction argument proves Poincaré duality for any orientable manifold having a finite good cover.

REMARK 5.7. The finiteness assumption on the good cover is in fact not necessary. By a closer analysis of the topology of a manifold, the Mayer-Vietoris argument above can be extended to any orientable manifold (Greub, Halperin, and Vanstone [1, p. 198 and p. 14]). The statement is as follows: if \( M \) is an orientable manifold of dimension \( n \) , whose cohomology is not necessarily finite dimensional, then

\[
{H}^{q}\left( M\right)  \simeq  {\left( {H}_{c}^{n - q}\left( M\right) \right) }^{ * }\;,\;\text{ for any integer }q\text{ . }
\]

However, the reverse implication \( {H}_{c}^{q}\left( M\right)  \simeq  {\left( {H}^{n - q}\left( M\right) \right) }^{ * } \) is not always true. The asymmetry comes from the fact that the dual of a direct sum is a direct product, but the dual of a direct product is not a direct sum. For example, consider the infinite disjoint union

\[
M = \mathop{\coprod }\limits_{{i = 1}}^{\infty }{M}_{i}
\]

where the \( {M}_{i} \) ’s are all manifolds of finite type of the same dimension \( n \) . Then the de Rham cohomology is a direct product

(5.7.1)

\[
{H}^{q}\left( M\right)  = \mathop{\prod }\limits_{i}{H}^{q}\left( {M}_{i}\right)
\]

but the compact cohomology is a direct sum

(5.7.2)

\[
{H}_{c}^{q}\left( M\right)  = {\bigoplus }_{i}{H}_{c}^{q}\left( {M}_{i}\right)
\]

Taking the dual of the compact cohomology \( {H}_{c}^{q}\left( M\right) \) gives a direct product

(5.7.3)

\[
{\left( {H}_{c}^{q}\left( M\right) \right) }^{ * } = \mathop{\prod }\limits_{i}{H}_{c}^{q}\left( {M}_{i}\right)
\]

So by (5.7.1) and (5.7.3), it follows from Poincaré duality for the manifolds of finite type \( {M}_{i} \) , that

\[
{H}^{q}\left( M\right)  = {\left( {H}_{c}^{n - q}\left( M\right) \right) }^{ * }.
\]

Corollary 5.8. If \( M \) is a connected oriented manifold of dimension \( n \) , then \( {H}_{c}^{n}\left( M\right)  \simeq  \mathbb{R} \) . In particular if \( M \) is compact oriented and connected, \( {H}^{n}\left( M\right)  \simeq  \mathbb{R}. \)

Let \( f : M \rightarrow  N \) be a map between two compact oriented manifolds of dimension \( n \) . Then there is an induced map in cohomology

\[
{f}^{ * } : {H}^{n}\left( N\right)  \rightarrow  {H}^{n}\left( M\right)
\]

The degree of \( f \) is defined to be \( {\int }_{M}{f}^{ * }\omega \) , where \( \omega \) is the generator of \( {H}^{n}\left( N\right) \) . By the same argument as for the degree of a proper map between two Euclidean spaces, the degree of a map between two compact oriented manifolds is an integer and is equal to the number of points, counted with multiplicity \( \pm  1 \) , in the inverse image of any regular point in \( N \) .

## The Künneth Formula and the Leray-Hirsch Theorem

The Künneth formula states that the cohomology of the product of two manifolds \( M \) and \( F \) is the tensor product

(5.9)

\[
{H}^{ * }\left( {M \times  F}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) .
\]

This means

\( {H}^{n}\left( {M \times  F}\right)  = {\bigoplus }_{p + q = n}{H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) \; \) for every nonnegative integer \( n. \)

More generally we are interested in the cohomology of a fiber bundle.

Definition. Let \( G \) be a topological group which acts effectively on a space \( F \) on the left. A surjection \( \pi  : E \rightarrow  B \) between topological spaces is a fiber bundle with fiber \( F \) and structure group \( G \) if \( B \) has an open cover \( \left\{  {U}_{\alpha }\right\} \) such that there are fiber-preserving homeomorphisms

\[
{\phi }_{\alpha } : {\left. E\right| }_{{U}_{\alpha }} \simeq  {U}_{\alpha } \times  F
\]

and the transitions functions are continuous functions with values in \( G \) :

\[
{g}_{\alpha \beta }\left( x\right)  = {\phi }_{\alpha }{\phi }_{\beta }^{-1}{|}_{\{ x\}  \times  F} \in  G.
\]

Sometimes the total space \( E \) is referred to as the fiber bundle. A fiber bundle with structure group \( G \) is also called a \( G \) -bundle. If \( x \in  B \) , the set \( {E}_{x} = {\pi }^{-1}\left( x\right) \) is called the fiber at \( x \) .

Since we are working with de Rham theory, the spaces \( E, B \) , and \( F \) will be assumed to be \( {C}^{\infty } \) manifolds and the maps \( {C}^{\infty } \) maps. We may also speak of a fiber bundle without mentioning its structure group; in that case, the group is understood to be the group of diffeomorphisms of \( F \) , denoted \( \operatorname{Diff}\left( F\right) \) .

REMARK. The action of a group \( G \) on a space \( F \) is said to be effective if the only element of \( G \) which acts trivially on \( F \) is the identity, i.e., if \( g \cdot  y = y \) for all \( y \) in \( F \) , then \( g = 1 \in  G \) . In the \( {C}^{\infty } \) case, this is equivalent to saying that the kernel of the natural map \( G \rightarrow  \operatorname{Diff}\left( F\right) \) is the identity or that \( G \) is a subgroup of \( \operatorname{Diff}\left( F\right) \) , the group of diffeomorphisms of \( F \) . In the definition of a fiber bundle the action of \( G \) on \( F \) is required to be effective in order that the diffeomorphism

\[
{\left. {\phi }_{\alpha }{\phi }_{\beta }^{-1}\right| }_{\{ x\}  \times  F}
\]

of \( F \) can be identified unambiguously with an element of \( G \) .

The transition functions \( {g}_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow  G \) satisfy the cocycle condition :

\[
{g}_{\alpha \beta } \cdot  {g}_{\beta \gamma } = {g}_{\alpha \gamma }.
\]

Given a cocycle \( \left\{  {g}_{\alpha \beta }\right\} \) with values in \( G \) we can construct a fiber bundle \( E \) having \( \left\{  {g}_{\alpha \beta }\right\} \) as its transition functions by setting

(5.10)

\[
E = \left( {\coprod {U}_{\alpha } \times  F}\right) /\left( {x, y}\right)  \sim  \left( {x,{g}_{\alpha \beta }\left( x\right) y}\right)
\]

for \( \left( {x, y}\right) \) in \( {U}_{\beta } \times  F \) and \( \left( {x,{g}_{\alpha \beta }\left( x\right) y}\right) \) in \( {U}_{\alpha } \times  F \) .

The following proof of the Künneth formula assumes that \( M \) has a finite good cover. This assumption is necessary for the induction argument.

The two natural projections

![bo_d7b6f8alb0pc73dd9avg_58_697_1820_269_185_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_58_697_1820_269_185_0.jpg)

give rise to a map on forms

\[
\omega  \otimes  \phi  \mapsto  {\pi }^{ * }\omega  \land  {\rho }^{ * }\phi
\]

which induces a map in cohomology (exercise)

\[
\psi  : {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right)  \rightarrow  {H}^{ * }\left( {M \times  F}\right) .
\]

We will show that \( \psi \) is an isomorphism.

If \( M = {\mathbb{R}}^{m} \) , this is simply the Poincaré lemma.

In the following we will regard \( M \times  F \) as a product bundle over \( M \) . Let \( U \) and \( V \) be open sets in \( M \) and \( n \) a fixed integer. From the Mayer-Vietoris sequence

\[
\cdots  \rightarrow  {H}^{p}\left( {U \cup  V}\right)  \rightarrow  {H}^{p}\left( U\right)  \oplus  {H}^{p}\left( V\right)  \rightarrow  {H}^{p}\left( {U \cap  V}\right) \cdots
\]

we get an exact sequence by tensoring with \( {H}^{n - p}\left( F\right) \)

\[
\cdots  \rightarrow  {H}^{p}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right)  \rightarrow  \left( {{H}^{p}\left( U\right)  \otimes  {H}^{n - p}\left( F\right) }\right)  \oplus  \left( {{H}^{p}\left( V\right)  \otimes  {H}^{n - p}\left( F\right) }\right)
\]

\[
\rightarrow  {H}^{p}\left( {U \cap  V}\right)  \otimes  {H}^{n - p}\left( F\right)  \rightarrow  \cdots
\]

since tensoring with a vector space preserves exactness. Summing over all integers \( p \) yields the exact sequence

\[
\cdots  \rightarrow  {\bigoplus }_{p = 0}^{n}{H}^{p}\left( {U \cup  V}\right)  \otimes  {H}^{n - p}\left( F\right)
\]

\[
\rightarrow  {\bigoplus }_{p = 0}^{n}\left( {{H}^{p}\left( U\right)  \otimes  {H}^{n - p}\left( F\right) }\right)  \oplus  \left( {{H}^{p}\left( V\right)  \otimes  {H}^{n - p}\left( F\right) }\right)
\]

\[
\rightarrow  {\bigoplus }_{p = 0}^{n}{H}^{p}\left( {U \cap  V}\right)  \otimes  {H}^{n - p}\left( F\right)  \rightarrow  \cdots .
\]

The following diagram is commutative

![bo_d7b6f8alb0pc73dd9avg_59_261_1411_1177_194_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_59_261_1411_1177_194_0.jpg)

The commutativity is clear except possibly for the square

![bo_d7b6f8alb0pc73dd9avg_59_278_1697_948_242_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_59_278_1697_948_242_0.jpg)

which we now check. Let \( \omega  \otimes  \phi \) be in \( {H}^{p}\left( {U \cap  V}\right)  \otimes  {H}^{n - p}\left( F\right) \) . Then

\[
\psi {d}^{ * }\left( {\omega  \otimes  \phi }\right)  = {\pi }^{ * }\left( {{d}^{ * }\omega }\right)  \land  {\rho }^{ * }\phi
\]

\[
{d}^{ * }\psi \left( {\omega  \otimes  \phi }\right)  = {d}^{ * }\left( {{\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right) .
\]

Recall from (2.5) that if \( \left\{  {{\rho }_{U},{\rho }_{V}}\right\} \) is a partition of unity subordinate to \( \{ U, V\} \) then

\[
{d}^{ * }\omega  = \begin{cases}  - d\left( {{\rho }_{V}\omega }\right) & \text{ on }U \\  d\left( {{\rho }_{U}\omega }\right) & \text{ on }V. \end{cases}
\]

Since the pullback functions \( \left\{  {{\pi }^{ * }{\rho }_{U},{\pi }^{ * }{\rho }_{V}}\right\} \) form a partition of unity on \( \left( {U \cup  V}\right)  \times  F \) subordinate to the cover \( \{ U \times  F, V \times  F\} \) , on \( \left( {U \cap  V}\right)  \times  F \)

\[
{d}^{ * }\left( {{\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right)  = d\left( {\left( {{\pi }^{ * }{\rho }_{U}}\right) {\pi }^{ * }\omega  \land  {\rho }^{ * }\phi }\right)
\]

\[
= \left( {d{\pi }^{ * }\left( {{\rho }_{U}\omega }\right) }\right)  \land  {\rho }^{ * }\phi \;\text{ since }\phi \text{ is closed }
\]

\[
= {\pi }^{ * }\left( {{d}^{ * }\omega }\right)  \land  {\rho }^{ * }\phi .
\]

So the diagram is commutative.

By the Five Lemma if the theorem is true for \( U, V \) , and \( U \cap  V \) , then it is also true for \( U \cup  V \) . The Künneth formula now follows by induction on the cardinality of a good cover, as in the proof of Poincaré duality.

Let \( \pi  : E \rightarrow  M \) be a fiber bundle with fiber \( F \) . Suppose there are cohomology classes \( {e}_{1},\ldots ,{e}_{r} \) on \( E \) which restrict to a basis of the cohomology of each fiber. Then we can define a map

\[
\psi  : {H}^{ * }\left( M\right)  \otimes  \mathbb{R}\left\{  {{e}_{1},\ldots ,{e}_{r}}\right\}   \rightarrow  {H}^{ * }\left( E\right) .
\]

The same argument as the Künneth formula gives

Theorem 5.11 (Leray-Hirsch). Let \( E \) be a fiber bundle over \( M \) with fiber \( F \) . Suppose \( M \) has a finite good cover. If there are global cohomology classes \( {e}_{1},\ldots ,{e}_{r} \) on \( E \) which when restricted to each fiber freely generate the cohomology of the fiber, then \( {H}^{ * }\left( E\right) \) is a free module over \( {H}^{ * }\left( M\right) \) with basis \( \left\{  {{e}_{1},\ldots }\right. \) , \( \left. {e}_{r}\right\} \) , i.e.

\[
{H}^{ * }\left( E\right)  \simeq  {H}^{ * }\left( M\right)  \otimes  \mathbb{R}\left\{  {{e}_{1},\ldots ,{e}_{r}}\right\}   \simeq  {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) .
\]

Exercise 5.12 Künneth formula for compact cohomology. The Künneth formula for compact cohomology states that for any manifolds \( M \) and \( N \) having a finite good cover.

\[
{H}_{c}^{ * }\left( {M \times  N}\right)  = {H}_{c}^{ * }\left( M\right)  \otimes  {H}_{c}^{ * }\left( N\right)
\]

(a) In case \( M \) and \( N \) are orientable, show that this is a consequence of Poincaré duality and the Künneth formula for de Rham cohomology.

(b) Using the Mayer-Vietoris argument prove the Künneth formula for compact cohomology for any \( M \) and \( N \) having a finite good cover.

## The Poincaré Dual of a Closed Oriented Submanifold

Let \( M \) be an oriented manifold of dimension \( n \) and \( S \) a closed oriented submanifold of dimension \( k \) ; here by "closed" we mean as a subspace of \( M \) . Figure 5.1 is a closed submanifold of \( {\mathbb{R}}^{2} - \{ 0\} \) , but Figure 5-2 is not. To every closed oriented submanifold \( i : S \hookrightarrow  M \) of dimension \( k \) , one can associate a unique cohomology class \( \left\lbrack  {\eta }_{s}\right\rbrack \) in \( {H}^{n - k}\left( M\right) \) , called its Poincare dual, as follows. Let \( \omega \) be a closed \( k \) -form with compact support on \( M \) . Since \( S \) is closed in \( M,\operatorname{Supp}\left( {\left. \omega \right| }_{s}\right) \) is closed not only in \( S \) , but also in \( M \) . Now because \( \operatorname{Supp}\left( {\left. \omega \right| }_{S}\right)  \subset  \left( {\operatorname{Supp}\omega }\right)  \cap  S \) is a closed subset of a compact set, \( {i}^{ * }\omega \) also has compact support on \( S \) , so the integral \( {\int }_{S}{i}^{ * }\omega \) is defined. By Stokes’s theorem integration over \( S \) induces a linear functional on \( {H}_{c}^{k}\left( M\right) \) . It follows by Poincaré duality: \( {\left( {H}_{c}^{k}\left( M\right) \right) }^{ * } \simeq  {H}^{n - k}\left( M\right) \) , that integration over \( S \) corresponds to a unique cohomology class \( \left\lbrack  {\eta }_{s}\right\rbrack \) in \( {H}^{n - k}\left( M\right) \) . We will often call both the cohomology class \( \left\lbrack  {\eta }_{S}\right\rbrack \) and a form representing it the Poincaré dual of \( S \) . By definition the Poincaré dual \( {\eta }_{S} \) is the unique cohomology class in \( {H}^{n - k}\left( M\right) \) satisfying

(5.13)

\[
{\int }_{S}{i}^{ * }\omega  = {\int }_{M}\omega  \land  {\eta }_{S}
\]

for any \( \omega \) in \( {H}_{c}^{k}\left( M\right) \) .

![bo_d7b6f8alb0pc73dd9avg_61_408_441_783_287_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_61_408_441_783_287_0.jpg)

Now suppose \( S \) is a compact oriented submanifold of dimension \( k \) in \( M \) . Since a compact subset of a Hausdorff space is closed, \( S \) is also a closed oriented submanifold and hence has a Poincaré dual \( {\eta }_{s} \in  {H}^{n - k}\left( M\right) \) . This \( {\eta }_{s} \) we will call the closed Poincaré dual of \( S \) , to distinguish it from the compact Poincaré dual to be defined below. Because \( S \) is compact, one can in fact integrate over \( S \) not only \( k \) -forms with compact support on \( M \) , but any \( k \) -form on \( M \) . In this way \( S \) defines a linear functional on \( {H}^{k}\left( M\right) \) and so by Poincaré duality corresponds to a unique cohomology class \( \left\lbrack  {\eta }_{S}^{\prime }\right\rbrack \) in \( {H}_{c}^{n - k}\left( M\right) \) , the compact Poincaré dual of \( S \) . We must assume here that \( M \) has a finite good cover; otherwise, the duality \( {\left( {H}^{k}\left( M\right) \right) }^{ * } \simeq  {H}_{c}^{n - k}\left( M\right) \) does not hold. The compact Poincare dual \( \left\lbrack  {\eta }_{S}^{\prime }\right\rbrack \) is uniquely characterized by

(5.14)

\[
{\int }_{S}{i}^{ * }\omega  = {\int }_{M}\omega  \land  {\eta }_{S}^{\prime },
\]

for any \( \omega  \in  {H}^{k}\left( M\right) \) . If (5.14) holds for any closed \( k \) -form \( \omega \) , then it certainly holds for any closed \( k \) -form \( \omega \) with compact support. So as a form, \( {\eta }_{S}^{\prime } \) is also the closed Poincaré dual of \( S \) , i.e., the natural map \( {H}_{c}^{n - k}\left( M\right)  \rightarrow  {H}^{n - k}\left( M\right) \) sends the compact Poincaré dual to the closed Poincaré dual. Therefore we can in fact demand the closed Poincaré dual of a compact oriented sub-manifold to have compact support. However, as cohomology classes, \( \left\lbrack  {\eta }_{s}\right\rbrack   \in \; {H}^{n - k}\left( M\right) \) and \( \left\lbrack  {\eta }_{s}^{\prime }\right\rbrack   \in  {H}_{c}^{n - k}\left( M\right) \) could be quite different, as the following examples demonstrate.

EXAMPLE 5.15 (The Poincaré duals of a point \( P \) on \( {\mathbb{R}}^{n} \) ). Since \( {H}^{n}\left( {\mathbb{R}}^{n}\right)  = 0 \) , the closed Poincaré dual \( {\eta }_{P} \) is trivial and can be represented by any closed \( n \) -form on \( {R}^{n} \) , but the compact Poincaré dual is the nontrivial class in \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) represented by a bump form with total integral 1 .

EXAMPLE-EXERCISE 5.16 (The ray and the circle in \( {\mathbb{R}}^{2} - \{ 0\} \) ). Let \( x, y \) be the standard coordinates and \( r,\theta \) the polar coordinates on \( {\mathbb{R}}^{2} - \{ 0\} \) .

(a) Show that the Poincaré dual of the ray \( \{ \left( {x,0}\right)  \mid  x > 0\} \) in \( {\mathbb{R}}^{2} - \{ 0\} \) is \( {d\theta }/{2\pi } \) in \( {H}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) .

(b) Show that the closed Poincaré dual of the unit circle in \( {H}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is 0, but the compact Poincaré dual is the nontrivial generator \( \rho \left( r\right) {dr} \) in \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) where \( \rho \left( r\right) \) is a bump function with total integral 1 . (By a bump function we mean a smooth function whose support is contained in some disc and whose graph looks like a "bump".)

Thus the generator of \( {H}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is represented by the ray and the generator of \( {H}_{c}^{1}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) by the circle (see Figure 5.3).

REMARK 5.17. The two Poincaré duals of a compact oriented submanifold correspond to the two homology theories--closed homology and compact homology. Closed homology has now fallen into disuse, while compact homology is known these days as the homology of singular chains. In Example-Exercise 5.16, the generator of \( {H}_{1,\text{ closed }}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is the ray, while the generator of \( {H}_{1,\text{ compact }}\left( {{\mathbb{R}}^{2}-\{ 0\} }\right) \) is the circle. (The circle is a boundary in closed homology since the punctured closed disk is a closed 2-chain in \( {\mathbb{R}}^{2} - \{ 0\} \) .) In general Poincaré duality sets up an isomorphism between closed homology and de Rham cohomology, and between compact homology and compact de Rham cohomology.

Let \( S \) be a compact oriented submanifold of dimension \( k \) in \( M \) . If \( W \subset  M \) is an open subset containing \( S \) , then the compact Poincaré dual of \( S \) in \( W,{\eta }_{S, W}^{\prime } \in  {H}_{c}^{n - k}\left( W\right) \) , extends by 0 to a form \( {\eta }_{S}^{\prime } \) in \( {H}_{c}^{n - k}\left( M\right) .{\eta }_{S} \) is clearly the compact Poincaré dual of \( S \) in \( M \) because

\[
{\int }_{S}{i}^{ * }\omega  = {\int }_{W}\omega  \land  {\eta }_{S, W}^{\prime } = {\int }_{M}\omega  \land  {\eta }_{S}^{\prime }.
\]

![bo_d7b6f8alb0pc73dd9avg_62_284_1720_1110_421_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_62_284_1720_1110_421_0.jpg)

Figure 5.3

Thus, the support of the compact Poincaré dual of S in M may be shrunk into any open neighborhood of \( S \) . This is called the localization principle. For a noncompact closed oriented submanifold \( S \) the localization principle also holds. We will take it up in Proposition 6.25.

In this book we will mean by the Poincaré dual the closed Poincaré dual. However, as we have seen, if the submanifold is compact, we can demand that its closed Poincaré dual have compact support, even as a cohomology class in \( {H}^{n - k}\left( M\right) \) . Of course, on a compact manifold \( M \) , there is no distinction between the closed and the compact Poincaré duals.
