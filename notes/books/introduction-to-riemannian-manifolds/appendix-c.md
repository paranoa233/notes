## Appendix C Review of Lie Groups

Lie groups play many important roles in Riemannian geometry, both as examples of Riemannian manifolds and as isometry groups of other manifolds. In this appendix, we summarize the main facts about Lie groups that are used in this book. For details, consult [LeeSM], especially Chapters 7, 8, 20, and 21.

## Definitions and Properties

A Lie group is a smooth manifold \( G \) that is also a group in the algebraic sense, with the property that the multiplication map \( m : G \times  G \rightarrow  G \) given by \( m\left( {{\varphi }_{1},{\varphi }_{2}}\right)  = {\varphi }_{1}{\varphi }_{2} \) and the inversion map \( i : G \rightarrow  G \) given by \( i\left( \varphi \right)  = {\varphi }^{-1} \) are smooth. For generic Lie groups, we usually denote the identity element by \( e \) , unless there is a more specific common notation for a particular group.

Given a Lie group \( G \) , each \( \varphi  \in  G \) defines a map \( {L}_{\varphi } : G \rightarrow  G \) , called left translation, by \( {L}_{\varphi }\left( {\varphi }^{\prime }\right)  = \varphi {\varphi }^{\prime } \) . It is a diffeomorphism with inverse \( {L}_{{\varphi }^{-1}} \) . Similarly, right translation \( {R}_{\varphi } : G \rightarrow  G \) is the diffeomorphism \( {R}_{\varphi }\left( {\varphi }^{\prime }\right)  = {\varphi }^{\prime }\varphi \) , with inverse \( {R}_{{\varphi }^{-1}} \) .

A subgroup \( H \subseteq  G \) that is endowed with a topology and smooth structure making it into a Lie group and an immersed or embedded submanifold of \( G \) is called a Lie subgroup of \( \mathbf{G} \) .

If \( G \) and \( H \) are Lie groups, a group homomorphism \( F : G \rightarrow  H \) that is also a smooth map is called a Lie group homomorphism. It is a Lie group isomorphism if it has an inverse that is also a Lie group homomorphism. A Lie group isomorphism from \( G \) to itself is called an automorphism of \( G \) .

Proposition C.1. [LeeSM, Thms. 7.5 & 21.27] Suppose \( F : G \rightarrow  H \) is a Lie group homomorphism.

(a) \( F \) has constant rank.

(b) The kernel of \( F \) is an embedded Lie subgroup of \( G \) .

(c) The image of \( F \) is an immersed Lie subgroup of \( H \) .

## Example C. 2 (Lie Groups).

(a) Every countable group with the discrete topology is a zero-dimensional Lie group, called a discrete Lie group.

(b) \( {\mathbb{R}}^{n} \) and \( {\mathbb{C}}^{n} \) are Lie groups under addition.

(c) The sets \( {\mathbb{R}}^{ * },{\mathbb{R}}^{ + } \) , and \( {\mathbb{C}}^{ * } \) of nonzero real numbers, positive real numbers, and nonzero complex numbers, respectively, are Lie groups under multiplication.

(d) The unit circle \( {\mathbb{S}}^{1} \subseteq  \mathbb{C} \) is a 1-dimensional Lie group under complex multiplication, called the circle group.

(e) Given Lie groups \( {G}_{1},\ldots ,{G}_{k} \) , their direct product group is the Lie group whose underlying manifold is \( {G}_{1} \times  \cdots  \times  {G}_{k} \) , and whose multiplication is given by \( \left( {{g}_{1},\ldots ,{g}_{k}}\right) \left( {{g}_{1}^{\prime },\ldots ,{g}_{k}^{\prime }}\right)  = \left( {{g}_{1}{g}_{1}^{\prime },\ldots ,{g}_{k}{g}_{k}^{\prime }}\right) \) . For example, the n-torus is the \( n \) -fold product group \( {\widetilde{\mathbb{T}}}^{n} = {\mathbb{S}}^{1} \times  \cdots  \times  {\mathbb{S}}^{1} \) . The 2-torus is often simply called the torus.

(f) The general linear groups \( \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) and \( \mathrm{{GL}}\left( {n,\mathbb{C}}\right) \) , consisting of all invertible \( n \times  n \) real or complex matrices, respectively, are Lie groups under matrix multiplication. The identity element in both cases is the \( n \times  n \) identity matrix, denoted by \( {I}_{n} \) . More generally, if \( V \) is an \( n \) -dimensional real or complex vector space, the group \( \mathrm{{GL}}\left( V\right) \) of invertible linear maps from \( V \) to itself is a Lie group isomorphic to \( \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) or \( \mathrm{{GL}}\left( {n,\mathbb{C}}\right) \) .

(g) The real and complex special linear groups are the subgroups \( \operatorname{SL}\left( {n,\mathbb{R}}\right)  \subseteq \; \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) and \( \mathrm{{SL}}\left( {n,\mathbb{C}}\right)  \subseteq  \mathrm{{GL}}\left( {n,\mathbb{C}}\right) \) consisting of matrices of determinant 1 .

(h) The orthogonal group \( \mathrm{O}\left( n\right)  \subseteq  \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) is the subgroup consisting of orthogonal matrices, those that satisfy \( {A}^{T}A = {I}_{n} \) , where \( {A}^{T} \) is the transpose of \( A \) . The special orthogonal group is the subgroup \( \mathrm{{SO}}\left( n\right)  = \mathrm{O}\left( n\right)  \cap  \mathrm{{SL}}\left( {n,\mathbb{R}}\right) \) .

(i) Similarly, the unitary group \( \mathrm{U}\left( n\right)  \subseteq  \mathrm{{GL}}\left( {n,\mathbb{C}}\right) \) is the subgroup consisting of complex unitary matrices, those that satisfy \( {A}^{ * }A = {I}_{n} \) , where \( {A}^{ * } = {\bar{A}}^{T} \) is the conjugate transpose of \( A \) , called its adjoint. The special unitary group is \( \mathrm{{SU}}\left( n\right)  = \mathrm{U}\left( n\right)  \cap  \mathrm{{SL}}\left( {n,\mathbb{C}}\right) . \)

If \( G \) is a Lie group and \( V \) is a finite-dimensional vector space, a Lie group homomorphism \( \rho  : G \rightarrow  \mathrm{{GL}}\left( V\right) \) is called a (finite-dimensional) representation of \( G \) . It is said to be faithful if it is injective.

## The Lie Algebra of a Lie Group

Suppose \( G \) is a Lie group. A vector field \( X \) on \( G \) is said to be left-invariant if it is invariant under all left translations, meaning that \( {\left( {L}_{g}\right) }_{ * }X = X \) for every \( g \in  G \) . Similarly, \( X \) is right-invariant if it is invariant under all right translations.

We denote the set of all smooth left-invariant vector fields on \( G \) by Lie \( \left( G\right) \) . It is a vector subspace of \( \mathcal{X}\left( G\right) \) that is closed under Lie brackets (see [LeeSM, Prop. 8.33]). Thus it is an example of a Lie algebra: a vector space \( \mathfrak{g} \) endowed with a bilinear operation \( \left\lbrack  {\cdot , \cdot  }\right\rbrack   : \mathfrak{g} \times  \mathfrak{g} \rightarrow  \mathfrak{g} \) , called the bracket, that is antisymmetric (meaning \( \left\lbrack  {X, Y}\right\rbrack   =  - \left\lbrack  {Y, X}\right\rbrack  ) \) and satisfies the Jacobi identity:

\[
\left\lbrack  {X,\left\lbrack  {Y, Z}\right\rbrack  }\right\rbrack   + \left\lbrack  {Y,\left\lbrack  {Z, X}\right\rbrack  }\right\rbrack   + \left\lbrack  {Z,\left\lbrack  {X, Y}\right\rbrack  }\right\rbrack   = 0.
\]

With the Lie bracket structure that it inherits from \( \mathcal{X}\left( G\right) \) , the Lie algebra \( \operatorname{Lie}\left( G\right) \) is called the Lie algebra of \( G \) .

Proposition C.3. [LeeSM, Thm. 8.37] Let \( G \) be a Lie group with identity e. The evaluation map \( X \mapsto  {X}_{e} \) is a vector space isomorphism from \( \operatorname{Lie}\left( G\right) \) to \( {T}_{e}G \) , so \( \operatorname{Lie}\left( G\right) \) has the same dimension as \( G \) itself.

If \( \mathfrak{g} \) is a Lie algebra, a Lie subalgebra of \( \mathfrak{g} \) is a vector subspace \( \mathfrak{h} \subseteq  \mathfrak{g} \) that is closed under Lie brackets, and is thus a Lie algebra with the restriction of the same bracket operation. Given Lie algebras \( {\mathfrak{g}}_{1} \) and \( {\mathfrak{g}}_{2} \) , a Lie algebra homomorphism is a linear map \( F : {\mathfrak{g}}_{1} \rightarrow  {\mathfrak{g}}_{2} \) that preserves brackets: \( F\left( \left\lbrack  {X, Y}\right\rbrack  \right)  = \left\lbrack  {F\left( X\right) , F\left( Y\right) }\right\rbrack \) . A Lie algebra isomorphism is an invertible Lie algebra homomorphism, and a Lie algebra automorphism is a Lie algebra isomorphism from a Lie algebra to itself.

## Example C. 4 (Lie Algebras).

(a) If \( M \) is a smooth positive-dimensional manifold, the space \( \mathfrak{X}\left( M\right) \) of all smooth vector fields on \( M \) is an infinite-dimensional Lie algebra under the Lie bracket.

(b) The vector space \( \mathfrak{{gl}}\left( {n,\mathbb{R}}\right) \) of all \( n \times  n \) real matrices is an \( {n}^{2} \) -dimensional Lie algebra under the commutator bracket \( \left\lbrack  {A, B}\right\rbrack   = {AB} - {BA} \) . The canonical identification of both \( \mathfrak{{gl}}\left( {n,\mathbb{R}}\right) \) and \( \operatorname{Lie}\left( {\mathrm{{GL}}\left( {n,\mathbb{R}}\right) }\right) \) with the tangent space to \( \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) at the identity yields a Lie algebra isomorphism \( \mathfrak{{gl}}\left( {n,\mathbb{R}}\right)  \cong \) Lie(GL \( \left( {n,\mathbb{R}}\right) \) ) [LeeSM, Prop. 8.41].

(c) Similarly, the space \( \mathfrak{{gl}}\left( {n,\mathbb{C}}\right) \) of \( n \times  n \) complex matrices is a \( 2{n}^{2} \) -dimensional (real) Lie algebra under the commutator bracket, isomorphic to the Lie algebra of \( \operatorname{GL}\left( {n,\mathbb{C}}\right) \) [LeeSM, Prop. 8.48].

(d) The space \( \mathfrak{o}\left( n\right) \) of skew-symmetric \( n \times  n \) real matrices is a Lie subalgebra of \( \mathfrak{{gl}}\left( {n,\mathbb{R}}\right) \) , isomorphic to the Lie algebra of \( \mathrm{O}\left( n\right) \) [LeeSM, Example 8.47].

(e) If \( V \) is a vector space, the space \( \mathfrak{{gl}}\left( V\right) \) of all linear maps from \( V \) to itself is a Lie algebra under the commutator bracket \( \left\lbrack  {A, B}\right\rbrack   = A \circ  B - B \circ  A \) . In case \( V \) is finite-dimensional, \( \mathfrak{{gl}}\left( V\right) \) is isomorphic to the Lie algebra of the Lie group \( \mathrm{{GL}}\left( V\right) \) .

(f) A Lie algebra in which all brackets are zero is called an abelian Lie algebra. Every vector space can be made into an abelian Lie algebra by defining all brackets to be zero. The Lie algebra of a connected Lie group is abelian if and only if the group is abelian (see [LeeSM, Problems 8-25 and 20-7]).

The following proposition shows that every Lie group homomorphism induces a Lie algebra homomorphism between the respective Lie algebras.

Proposition C.5 (The Induced Lie Algebra Homomorphism). [LeeSM, Thm. 8.44] Let \( G \) and \( H \) be Lie groups, and let \( \mathfrak{g} \) and \( \mathfrak{h} \) be their Lie algebras. Given a Lie group homomorphism \( F : G \rightarrow  H \) , there is a unique Lie algebra homomorphism \( {F}_{ * } : \mathfrak{g} \rightarrow  \mathfrak{h} \) , called the induced Lie algebra homomorphism of \( F \) , with the property that for each \( X \in  \mathfrak{g} \) , the vector field \( {F}_{ * }X \in  \mathfrak{h} \) is \( F \) -related to \( X \) .

Proposition C.6 (Properties of Induced Homomorphisms). [LeeSM, Prop. 8.45] Let \( G, H, K \) be Lie groups.

(a) \( {\left( {\operatorname{Id}}_{G}\right) }_{ * } = {\operatorname{Id}}_{\operatorname{Lie}\left( G\right) } : \operatorname{Lie}\left( G\right)  \rightarrow  \operatorname{Lie}\left( G\right) \) .

(b) If \( {F}_{1} : G \rightarrow  H \) and \( {F}_{2} : H \rightarrow  K \) are Lie group homomorphisms, then

\[
{\left( {F}_{2} \circ  {F}_{1}\right) }_{ * } = {\left( {F}_{2}\right) }_{ * } \circ  {\left( {F}_{1}\right) }_{ * } : \operatorname{Lie}\left( G\right)  \rightarrow  \operatorname{Lie}\left( K\right) .
\]

(c) Isomorphic Lie groups have isomorphic Lie algebras.

## The Exponential Map of a Lie Group

If \( G \) is a Lie group, a Lie group homomorphism from \( \mathbb{R} \) (with its additive group structure) to \( G \) is called a one-parameter subgroup of \( G \) . (Note that the term "one-parameter subgroup" refers, confusingly, to a homomorphism, not to a Lie subgroup of \( G \) . But the image of a one-parameter subgroup is always a Lie subgroup of dimension at most 1.) Theorem 20.1 of [LeeSM] shows that for every \( X \in  \operatorname{Lie}\left( G\right) \) , the integral curve of \( X \) starting at the identity is a one-parameter subgroup, called the one-parameter subgroup generated by \( \mathbf{X} \) , and every one-parameter subgroup is of this form.

The exponential map of \( G \) is the map \( {\exp }^{G} : \operatorname{Lie}\left( G\right)  \rightarrow  G \) defined by setting \( {\exp }^{G}\left( X\right)  = \gamma \left( 1\right) \) , where \( \gamma \) is the integral curve of \( X \) starting at \( e \) . (The exponential map is more commonly denoted simply by exp, but we use the notation \( {\exp }^{G} \) to distinguish the Lie group exponential map from the Riemannian exponential map, introduced in Chapter 5.)

Proposition C. 7 (Properties of the Lie Group Exponential Map). [LeeSM, Props. 20.5 & 20.8] Let \( G \) be a Lie group and let \( \mathfrak{g} \) be its Lie algebra.

(a) \( {\exp }^{G} : \mathfrak{g} \rightarrow  G \) is smooth.

(b) For every \( X \in  \mathfrak{g} \) , the map \( \gamma  : \mathbb{R} \rightarrow  G \) defined by \( \gamma \left( t\right)  = {\exp }^{G}\left( {tX}\right) \) is the one-parameter subgroup generated by \( X \) .

(c) The differential \( {\left( d{\exp }^{G}\right) }_{0} : {T}_{0}\mathfrak{g} \rightarrow  {T}_{e}G \) is the identity map, under the canonical identifications of \( {T}_{0}\mathfrak{g} \) and \( {T}_{e}G \) with \( \mathfrak{g} \) .

The exponential map is the key ingredient in the proof of the following fundamental result.

Theorem C.8 (Closed Subgroup Theorem). [LeeSM, Thm. 20.12 & Cor. 20.13] Suppose \( G \) is a Lie group and \( H \subseteq  G \) is a subgroup in the algebraic sense. Then \( H \) is an embedded Lie subgroup of \( G \) if and only if it is closed in the topological sense.

An important special case of the closed subgroup theorem is that of a discrete subgroup, that is, a subgroup that is discrete in the subspace topology.

Proposition C.9. [LeeSM, Prop. 21.28] Every discrete subgroup of a Lie group is a closed Lie subgroup of dimension zero.

## Adjoint Representations

Let \( G \) be a Lie group and \( \mathfrak{g} \) its Lie algebra. For every \( \varphi  \in  G \) , conjugation by \( \varphi \) gives a Lie group automorphism \( {C}_{\varphi } : G \rightarrow  G \) , called an inner automorphism, by \( {C}_{\varphi }\left( \psi \right)  = {\varphi \psi }{\varphi }^{-1} \) . Let \( \operatorname{Ad}\left( \varphi \right)  = {\left( {C}_{\varphi }\right) }_{ * } : \mathfrak{g} \rightarrow  \mathfrak{g} \) be the induced Lie algebra automorphism. It follows from the definition that \( {C}_{{\varphi }_{1}} \circ  {C}_{{\varphi }_{2}} = {C}_{{\varphi }_{1}{\varphi }_{2}} \) , and therefore \( \operatorname{Ad}\left( {\varphi }_{1}\right)  \circ  \operatorname{Ad}\left( {\varphi }_{2}\right)  = \operatorname{Ad}\left( {{\varphi }_{1}{\varphi }_{2}}\right) \) ; in other words, \( \operatorname{Ad} : G \rightarrow  \operatorname{GL}\left( \mathfrak{g}\right) \) is a representation, called the adjoint representation of \( G \) . Proposition 20.24 in [LeeSM] shows that Ad is a smooth map.

## Example C.10 (Adjoint Representations of Lie Groups).

(a) If \( G \) is an abelian Lie group, then \( {C}_{\varphi } \) is the identity map for every \( \varphi  \in  G \) , so the adjoint representation is trivial: \( \operatorname{Ad}\left( \varphi \right)  = {\operatorname{Id}}_{\mathfrak{g}} \) for all \( \varphi  \in  G \) .

(b) Suppose \( G \) is a Lie subgroup of \( \operatorname{GL}\left( {n,\mathbb{R}}\right) \) . Then for each \( A \in  G \) , the conjugation map \( {C}_{A}\left( B\right)  = {AB}{A}^{-1} \) is the restriction to \( G \) of a linear map from the space \( \mathrm{M}\left( {n,\mathbb{R}}\right) \) of \( n \times  n \) matrices to itself. Its differential, therefore, is given by the same formula: \( \operatorname{Ad}\left( A\right) X = {AX}{A}^{-1} \) for every \( A \in  G \) and \( X \in  \operatorname{Lie}\left( G\right)  \subseteq \; \mathfrak{{gl}}\left( {n,\mathbb{R}}\right) \) .

There is also an adjoint representation for Lie algebras. If \( \mathfrak{g} \) is any Lie algebra, a representation of \( \mathfrak{g} \) is a Lie algebra homomorphism from \( \mathfrak{g} \) to \( \mathfrak{{gl}}\left( V\right) \) , the Lie algebra of all linear endomorphisms of some vector space \( V \) . For each \( X \in  \mathfrak{g} \) , define a map \( \operatorname{ad}\left( X\right)  : \mathfrak{g} \rightarrow  \mathfrak{g} \) by \( \operatorname{ad}\left( X\right) Y = \left\lbrack  {X, Y}\right\rbrack \) . This defines ad as a map from \( \mathfrak{g} \) to \( \mathfrak{{gl}}\left( \mathfrak{g}\right) \) , and a straightforward computation shows that it is a representation of \( \mathfrak{g} \) , called the adjoint representation of \( \mathfrak{g} \) .

The next proposition shows how the two adjoint representations are related.

Proposition C.11. [LeeSM, Thm. 20.27] Let \( G \) be a Lie group and \( \mathfrak{g} \) its Lie algebra, and let \( \mathrm{{Ad}} : G \rightarrow  \mathrm{{GL}}\left( \mathfrak{g}\right) \) and ad: \( \mathfrak{g} \rightarrow  \mathfrak{{gl}}\left( \mathfrak{g}\right) \) be their respective adjoint representations. The induced Lie algebra representation \( {\mathrm{{Ad}}}_{ * } : \mathfrak{g} \rightarrow  \mathfrak{{gl}}\left( \mathfrak{g}\right) \) is given by \( {\mathrm{{Ad}}}_{ * } = \) ad.

## Group Actions on Manifolds

The most important applications of Lie groups in differential geometry involve their actions on other manifolds.

First we consider actions by abstract groups, not necessarily endowed with a smooth manifold structure or even a topology. Let \( G \) be a group and \( M \) a set. A left action of \( G \) on \( M \) is a map \( G \times  M \rightarrow  M \) , usually written \( \left( {\varphi , p}\right)  \mapsto  \varphi  \cdot  p \) , satisfying \( {\varphi }_{1} \cdot  \left( {{\varphi }_{2} \cdot  p}\right)  = \left( {{\varphi }_{1}{\varphi }_{2}}\right)  \cdot  p \) and \( e \cdot  p = p \) for all \( {\varphi }_{1},{\varphi }_{2} \in  G \) and \( p \in  M \) , where \( e \) is the identity element of \( G \) . Similarly, a right action of \( G \) on \( M \) is a map \( M \times  G \rightarrow  M \) satisfying \( \left( {p \cdot  {\varphi }_{1}}\right)  \cdot  {\varphi }_{2} = p \cdot  \left( {{\varphi }_{1}{\varphi }_{2}}\right) \) and \( p \cdot  e = p \) . In some cases, it will be important to give a name to an action such as \( \theta  : G \times  M \rightarrow  M \) , in which case we write \( {\theta }_{\varphi }\left( p\right) \) in place of \( \varphi  \cdot  p \) , with a similar convention for right actions. Since right actions can be converted to left actions and vice versa by setting \( \varphi  \cdot  p = p \cdot  {\varphi }^{-1} \) , for most purposes we lose no real generality by restricting attention to left actions. (But there are also situations in which right actions arise naturally.)

Given an action of \( G \) on \( M \) , for each \( p \in  M \) the isotropy subgroup at \( p \) is the subgroup \( {G}_{p} \subseteq  G \) consisting of all elements that fix \( p \) : that is, \( {G}_{p} = \{ \varphi  \in  G \) : \( \varphi  \cdot  p = p\} \) . The group action is said to be free if \( \varphi  \cdot  p = p \) for some \( \varphi  \in  G \) and \( p \in  M \) implies \( \varphi  = e \) , or in other words, if \( {G}_{p} = \{ e\} \) for every \( p \) . It is said to be effective if \( {\varphi }_{1} \cdot  p = {\varphi }_{2} \cdot  p \) for all \( p \) if and only if \( {\varphi }_{1} = {\varphi }_{2} \) , or equivalently, if the only element of \( G \) that fixes every element of \( M \) is the identity. For effective actions, each element of \( G \) is uniquely determined by the map \( p \mapsto  \varphi  \cdot  p \) . In such cases, we will sometimes use the same notation \( \varphi \) to denote either the element \( \varphi  \in  G \) or the map \( p \mapsto  \varphi  \cdot  p \) . The action is said to be transitive if for every pair of points \( p, q \in  M \) , there exists \( \varphi  \in  G \) such that \( \varphi  \cdot  p = q \) .

If \( M \) is a smooth manifold, an action by a group \( G \) on \( M \) is said to be an action by diffeomorphisms if for each \( \varphi  \in  G \) , the map \( p \mapsto  \varphi  \cdot  p \) is a diffeomorphism of \( M \) . If \( G \) is a Lie group, an action of \( G \) on a smooth manifold \( M \) is said to be a smooth action if the defining map \( G \times  M \rightarrow  M \) is smooth. In this case, it is also an action by diffeomorphisms, because each map \( p \mapsto  \varphi  \cdot  p \) is smooth and has \( p \mapsto  {\varphi }^{-1} \cdot  p \) as an inverse. If \( G \) is any countable group, an action by \( G \) on \( M \) is an action by diffeomorphisms if and only if it is a smooth action when \( G \) is regarded as a 0-dimensional Lie group with the discrete topology.

Example C. 12 (Semidirect Products). Group actions provide an important way to construct Lie groups out of other Lie groups. Suppose \( H \) and \( N \) are Lie groups and \( \theta  : H \times  N \rightarrow  N \) is a smooth left action of \( H \) on \( N \) by automorphisms of \( N \) , meaning that for each \( h \in  H \) , the map \( {\theta }_{h} : N \rightarrow  N \) given by \( {\theta }_{h}\left( n\right)  = h \cdot  n \) is a Lie group automorphism. The semidirect product of \( H \) and \( N \) determined by \( \theta \) , denoted by \( N{ \rtimes  }_{\theta }H \) , is the Lie group whose underlying manifold is the Cartesian product \( N \times  H \) , and whose group multiplication is \( \left( {n, h}\right) \left( {{n}^{\prime },{h}^{\prime }}\right)  = \left( {n{\theta }_{h}\left( {n}^{\prime }\right) , h{h}^{\prime }}\right) \) . //

Exercise C.13. Verify that \( N{ \rtimes  }_{\theta }H \) is indeed a Lie group with the multiplication defined above, and with \( \left( {e, e}\right) \) as identity and \( {\left( n, h\right) }^{-1} = \left( {{\theta }_{{h}^{-1}}\left( {n}^{-1}\right) ,{h}^{-1}}\right) \) .

Now suppose \( G \) is a Lie group, and \( M \) and \( N \) are smooth manifolds endowed with \( G \) -actions (on the left, say). A map \( F : M \rightarrow  N \) is said to be equivariant with respect to the given \( G \) actions if \( F\left( {\varphi  \cdot  x}\right)  = \varphi  \cdot  F\left( x\right) \) for all \( \varphi  \in  G \) and \( x \in  M \) .

Theorem C. 14 (Equivariant Rank Theorem). [LeeSM, Thm. 7.25] Suppose \( M, N \) are smooth manifolds, and \( G \) is a Lie group acting smoothly and transitively on \( M \) and smoothly on \( N \) . If \( F : M \rightarrow  N \) is a smooth G-equivariant map, then \( F \) has constant rank. Thus, if \( F \) is surjective, it is a smooth submersion; if it is injective, it is a smooth immersion; and if it is bijective, it is a diffeomorphism.

A smooth action of \( G \) on \( M \) is said to be a proper action if the map \( G \times  M \rightarrow \; M \times  M \) defined by \( \left( {\varphi , x}\right)  \mapsto  \left( {\varphi  \cdot  x, x}\right) \) is a proper map, meaning that the preimage of every compact set is compact. The following characterization is usually the easiest way to prove that a given action is proper.

Proposition C.15. [LeeSM, Prop. 21.5] Suppose \( G \) is a Lie group acting smoothly on a smooth manifold \( M \) . The action is proper if and only if the following condition is satisfied: if \( \left( {p}_{i}\right) \) is a sequence in \( M \) and \( \left( {\varphi }_{i}\right) \) is a sequence in \( G \) such that both \( \left( {p}_{i}\right) \) and \( \left( {{\varphi }_{i} \cdot  {p}_{i}}\right) \) converge, then a subsequence of \( \left( {\varphi }_{i}\right) \) converges.

Corollary C.16. Every smooth action by a compact Lie group on a smooth manifold is proper.

Proof. If \( G \) is a compact Lie group, then every sequence in \( G \) has a convergent subsequence, so every smooth \( G \) -action is proper by the preceding proposition.

The next theorem is the most important application of proper actions. If a group \( G \) acts on a manifold \( M \) , then each \( p \in  M \) determines a subset \( G \cdot  p = \{ \varphi  \cdot  p : \varphi  \in  G\} \) , called the orbit of \( \mathbf{p} \) . Because two orbits are either identical or disjoint, the orbits form a partition of \( G \) . The set of orbits is denoted by \( M/G \) , and with the quotient topology it is called the orbit space of the action.

Theorem C.17 (Quotient Manifold Theorem). [LeeSM, Thm. 21.10] Suppose \( G \) is a Lie group acting smoothly, freely, and properly on a smooth manifold M. Then the orbit space \( M/G \) is a topological manifold whose dimension is equal to the difference \( \dim M - \dim G \) , and it has a unique smooth structure with the property that the quotient map \( \pi  : M \rightarrow  M/G \) is a smooth submersion.

Example C.18 (Real Projective Spaces). For each nonnegative integer \( n \) , the \( n \) - dimensional real projective space, denoted by \( {\mathbb{{RP}}}^{n} \) , is defined as the set of one-dimensional linear subspaces of \( {\mathbb{R}}^{n + 1} \) . It can be identified with the orbit space of \( {\mathbb{R}}^{n + 1} \smallsetminus  \{ 0\} \) under the action of the group \( {\mathbb{R}}^{ * } \) of nonzero real numbers given by scalar multiplication: \( \lambda  \cdot  \left( {{x}^{1},\ldots ,{x}^{n + 1}}\right)  = \left( {\lambda {x}^{1},\ldots ,\lambda {x}^{n + 1}}\right) \) . It is easy to check that this action is smooth and free. To see that it is proper, we use Proposition C.15. Suppose \( \left( {x}_{i}\right) \) is a sequence in \( {\mathbb{R}}^{n + 1} \smallsetminus  \{ 0\} \) and \( \left( {\lambda }_{i}\right) \) is a sequence in \( {\mathbb{R}}^{ * } \) such that \( {x}_{i} \rightarrow  x \in \; {\mathbb{R}}^{n + 1} \smallsetminus  \{ 0\} \) and \( {\lambda }_{i}{x}_{i} \rightarrow  y \in  {\mathbb{R}}^{n + 1} \smallsetminus  \{ 0\} \) . Then \( \left| {\lambda }_{i}\right|  = \left| {{\lambda }_{i}{x}_{i}}\right| /\left| {x}_{i}\right| \) converges to the nonzero real number \( \left| y\right| /\left| x\right| \) . Thus the numbers \( {\lambda }_{i} \) all lie in a compact set of the form \( \{ \lambda  : 1/C \leq  \left| \lambda \right|  \leq  C\} \) for some positive number \( C \) , so a subsequence converges to a nonzero real number. Therefore, by the quotient manifold theorem, \( {\mathbb{{RP}}}^{n} \) has a unique structure as a smooth \( n \) -dimensional manifold such that the quotient map \( {\mathbb{R}}^{n + 1} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{{RP}}}^{n} \) is a smooth submersion.

Example C.19 (Complex Projective Spaces). Similarly, the \( n \) -dimensional complex projective space, denoted by \( {\mathbb{{CP}}}^{n} \) , is the set of 1-dimensional complex subspaces of \( {\mathbb{C}}^{n + 1} \) , identified with the orbit space of \( {\mathbb{C}}^{n + 1} \smallsetminus  \{ 0\} \) under the \( {\mathbb{C}}^{ * } \) -action given by \( \lambda  \cdot  z = {\lambda z} \) . The same argument as in the preceding example shows that this action is smooth, free, and proper, so \( {\mathbb{{CP}}}^{n} \) is a smooth \( {2n} \) -dimensional manifold and the quotient map \( \pi  : {\mathbb{C}}^{n + 1} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{{CP}}}^{n} \) is a smooth submersion.

## Group Actions and Covering Spaces

There is a close connection between smooth covering maps and smooth group actions. To begin, suppose \( \widetilde{M} \) and \( M \) are smooth manifolds and \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth covering map. A covering automorphism of \( \pi \) is a diffeomorphism \( \varphi  : \widetilde{M} \rightarrow  \widetilde{M} \) such that \( \pi  \circ  \varphi  = \pi \) ; the set of all covering automorphisms is a group under composition, called the covering automorphism group and denoted by \( {\operatorname{Aut}}_{\pi }\left( \widetilde{M}\right) \) .

Proposition C.20. [LeeSM, Prop. 21.12] Let \( \pi  : \widetilde{M} \rightarrow  M \) be a smooth covering map. With the discrete topology, \( {\operatorname{Aut}}_{\pi }\left( \widetilde{M}\right) \) is a discrete Lie group acting smoothly, freely, and properly on \( \widetilde{M} \) .

Because of the requirement that a covering automorphism \( \varphi \) satisfy \( \pi  \circ  \varphi  = \pi \) , it follows that \( \varphi \) restricts to an action on each fiber of \( \pi \) . The next proposition describes the conditions in which this action is transitive. A covering map \( \pi  : \widetilde{M} \rightarrow  M \) is called a normal covering if the image of the homomorphism \( {\pi }_{ * } : {\pi }_{1}\left( {\widetilde{M},\widetilde{x}}\right)  \rightarrow \; {\pi }_{1}\left( {M,\pi \left( \widetilde{x}\right) }\right) \) is a normal subgroup of \( {\pi }_{1}\left( {M,\pi \left( \widetilde{x}\right) }\right) \) . (Note that every universal covering is a normal covering, because the trivial subgroup is always normal.)

Proposition C.21. [LeeTM, Cor. 12.5] If \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth covering map, then the automorphism group of \( \pi \) acts transitively on each fiber of \( \pi \) if and only if \( \pi \) is a normal covering.

The universal covering is the most important special case.

Proposition C.22 (Automorphisms of the Universal Covering). [LeeTM, Cor. 12.9] Suppose \( M \) is a connected smooth manifold and \( \pi  : \widetilde{M} \rightarrow  M \) is its universal covering. Then \( {\operatorname{Aut}}_{\pi }\left( \widetilde{M}\right) \) is isomorphic to the fundamental group of \( M \) , and it acts transitively on each fiber of \( \pi \) .

The next theorem, which is an application of the quotient manifold theorem, is a partial converse to Proposition C.20.

Proposition C.23. [LeeSM, Thm. 21.13] Suppose \( \widetilde{M} \) is a connected smooth manifold and \( \Gamma \) is a discrete Lie group acting smoothly, freely, and properly on \( \widetilde{M} \) . Then the orbit space \( \widetilde{M}/\Gamma \) has a unique smooth manifold structure such that the quotient map \( \widetilde{M} \rightarrow  \widetilde{M}/\Gamma \) is a smooth normal covering map.

Example C. 24 (The Universal Covering of \( {\mathbb{{RP}}}^{n} \) ). The two-element group \( \Gamma  = \; \{  \pm  1\} \) acts smoothly, freely, and properly on \( {\mathbb{S}}^{n} \) by multiplication, and thus \( {\mathbb{S}}^{n}/\Gamma \) is a smooth manifold and the quotient map \( \pi  : {\mathbb{S}}^{n} \rightarrow  {\mathbb{S}}^{n}/\Gamma \) is a two-sheeted smooth normal covering map. Note also that the quotient map \( {\mathbb{R}}^{n + 1} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{{RP}}}^{n} \) defined in Example C. 18 restricts to a surjective smooth map \( q : {\mathbb{S}}^{n} \rightarrow  {\mathbb{{RP}}}^{n} \) , which is a submersion because each point of \( {\mathbb{S}}^{n} \) is in the image of a smooth local section. Since \( q \) and \( \pi \) are constant on each other’s fibers, Proposition A. 19 shows that there is a diffeomorphism \( {\mathbb{S}}^{n}/\Gamma  \rightarrow  {\mathbb{{RP}}}^{n} \) , and \( q \) is equal to the composition \( {\mathbb{S}}^{n} \rightarrow  {\mathbb{S}}^{n}/\Gamma  \rightarrow \; {\mathbb{{RP}}}^{n} \) . Since this is a smooth normal covering map followed by a diffeomorphism, \( q \) is also a smooth normal covering map. Thus \( {\mathbb{S}}^{n} \) is the universal covering space of \( {\mathbb{{RP}}}^{n} \) , and the fundamental group of \( {\mathbb{{RP}}}^{n} \) is isomorphic to \( \{  \pm  1\} \) .
