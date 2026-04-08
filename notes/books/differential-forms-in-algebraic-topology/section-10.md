## §10 Presheaves and Čech Cohomology

## Presheaves

The functor \( {\Omega }^{ * }\left( \right) \) which assigns to every open set \( U \) on a manifold the differential forms on \( U \) is an example of a presheaf. By definition a presheaf \( \mathcal{F} \) on a topological space \( X \) is a function that assigns to every open set \( U \) in

\( X \) an abelian group \( \mathcal{F}\left( U\right) \) and to every inclusion of open sets

\[
{i}_{U}^{V} : V \rightarrow  U
\]

a group homomorphism, called the restriction,

\[
\mathcal{F}\left( {i}_{U}^{V}\right)  : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right)
\]

satisfying the following properties:

(a) \( \mathcal{F}\left( {i}_{V}^{V}\right)  = \) identity map

(b) transitivity: \( \mathcal{F}\left( {i}_{V}^{W}\right) \mathcal{F}\left( {i}_{U}^{V}\right)  = \mathcal{F}\left( {i}_{U}^{W}\right) \) .

The restriction \( \mathcal{F}\left( {i}_{U}^{V}\right)  : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) is often denoted \( {\rho }_{V}^{U} \) . A homomorphism of two presheaves, \( f : \mathcal{F} \rightarrow  \mathcal{G} \) , is a collection of maps \( {f}_{U} : \mathcal{F}\left( U\right)  \rightarrow  \mathcal{G}\left( U\right) \) which commute with the restrictions:

\[
\mathcal{F}\left( U\right) \overset{{f}_{U}}{ \rightarrow  }\mathcal{G}\left( U\right)
\]

\[
{\rho }_{V}^{U} \downarrow  \; \downarrow  {\rho }_{V}^{U}
\]

\[
\mathcal{F}\left( V\right) \underset{{f}_{V}}{ \rightarrow  }\mathcal{G}\left( V\right)
\]

Let \( \operatorname{Open}\left( X\right) \) be the category whose objects are the open sets in \( X \) and whose morphisms are inclusions of open sets. In functorial language, a presheaf is simply a contravariant functor from the category \( \operatorname{Open}\left( X\right) \) to the category of Abelian groups, and a homomorphism of two presheaves, \( f : \mathcal{F} \rightarrow  \mathcal{G} \) , is a natural transformation from the functor \( \mathcal{F} \) to the functor \( \mathcal{G} \) .

We define the constant presheaf with group \( G \) to be the presheaf \( \mathcal{F} \) which associates to every open set \( U \) the locally constant functions: \( U \rightarrow  G \) , and to every inclusion of open sets \( V \subset  U \) the restriction of functions: \( \mathcal{F}\left( U\right)  \rightarrow  \mathcal{F}\left( V\right) \) .

EXAMPLE. By abuse of notation, the constant presheaf with group \( \mathbb{R} \) will also be denoted by \( \mathbb{R} \) .

EXAMPLE 10.1. Let \( \pi  : E \rightarrow  M \) be a fiber bundle with fiber \( F \) . Define a presheaf \( {\mathcal{H}}^{q} \) on \( M \) by \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}U}\right) \) , and if \( V \subset  U \) is an inclusion, let

\[
{\rho }_{V}^{U} : {H}^{q}\left( {{\pi }^{-1}U}\right)  \rightarrow  {H}^{q}\left( {{\pi }^{-1}V}\right)
\]

be the natural restriction map. For \( U \) contractible, \( {\pi }^{-1}U \simeq  U \times  F \) , so by the Künneth formula

\[
{\mathcal{H}}^{q}\left( U\right)  \simeq  {H}^{q}\left( {U \times  F}\right)  \simeq  {H}^{q}\left( F\right)
\]

Moreover, if \( V \subset  U \) is an inclusion of contractible open sets, then \( {\rho }_{V}^{U} : {H}^{q}\left( {{\pi }^{-1}U}\right)  \rightarrow  {H}^{q}\left( {{\pi }^{-1}V}\right) \) is an isomorphism. The presheaf \( {\mathcal{H}}^{q} \) is an example of a locally constant presheaf on a good cover, to be defined in Section 13.

## Čech Cohomology

Let \( \mathfrak{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  J} \) be an open cover of the topological space \( X \) . The 0 - cochains on \( U \) with values in the presheaf \( \mathcal{F} \) are functions which assign to each open set \( {U}_{\alpha } \) an element of \( \mathcal{F}\left( {U}_{\alpha }\right) \) , i.e., \( {C}^{0}\left( {\mathfrak{U},\mathcal{F}}\right)  = {\Pi }_{\alpha  \in  J}\mathcal{F}\left( {U}_{\alpha }\right) \) . Similarly the 1-cochains are elements of

\[
{C}^{1}\left( {\mathfrak{U},\mathcal{F}}\right)  = \mathop{\prod }\limits_{{\alpha  < \beta }}\mathcal{F}\left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)
\]

and so on.

The sequence of inclusions

\[
{U}_{\alpha }\overset{\overset{{\partial }_{0}}{ \leftarrow  }}{\underset{{\partial }_{1}}{ \leftarrow  }}{U}_{\alpha \beta }\overset{\overset{ \leftarrow  }{ \leftarrow  }}{\underset{{\partial }_{1}}{ \leftarrow  }}\cdots
\]

gives rise to a sequence of group homomorphisms

\[
\prod \mathcal{F}\left( {U}_{\alpha }\right) \overset{ \rightarrow  }{ \rightarrow  }\prod \mathcal{F}\left( {U}_{\alpha \beta }\right) \overset{ \rightarrow  }{ \rightarrow  }\cdots
\]

We define \( \delta  : {C}^{p}\left( {\mathfrak{u},\mathcal{F}}\right)  \rightarrow  {C}^{p + 1}\left( {\mathfrak{u},\mathcal{F}}\right) \) to be the alternating difference of the \( \mathcal{F}\left( {\partial }_{i}\right) \) ’s; for example,

\[
\delta  : {C}^{0}\left( {\mathfrak{U},\mathcal{F}}\right)  \rightarrow  {C}^{1}\left( {\mathfrak{U},\mathcal{F}}\right)
\]

is given by

\[
\delta  = \mathcal{F}\left( {\partial }_{0}\right)  - \mathcal{F}\left( {\partial }_{1}\right)
\]

In general

\[
\delta  : {C}^{p}\left( {\mathfrak{U},\mathcal{F}}\right)  \rightarrow  {C}^{p + 1}\left( {\mathfrak{U},\mathcal{F}}\right)
\]

is given by

\[
\delta  = \mathcal{F}\left( {\partial }_{0}\right)  - \mathcal{F}\left( {\partial }_{1}\right)  + \cdots  + {\left( -1\right) }^{p + 1}\mathcal{F}\left( {\partial }_{p + 1}\right) .
\]

Explicitly, if \( \omega  \in  {C}^{p}\left( {\mathfrak{U},\mathcal{F}}\right) \) , then

(10.2)

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}},
\]

where on the right-hand side the restriction of \( {\omega }_{{\alpha }_{0}\ldots {\widehat{a}}_{i}\ldots {\alpha }_{p + 1}} \) to \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} \) is suppressed. It follows from the transitivity of the restriction homomorphism that \( {\delta }^{2} = 0 \) (proof as in Proposition 8.3). Thus \( {C}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) is a differential complex with differential operator \( \delta \) . The cohomology of this complex, denoted by \( {H}_{\delta }{C}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) or \( {H}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) , is called the Čech cohomology of the cover \( \mathfrak{U} \) with values in \( \mathcal{F} \) .

REMARK 10.3. If \( \mathcal{F} \) is a covariant functor from the category \( \operatorname{Open}\left( X\right) \) to the category of Abelian groups, and \( \mathfrak{U} \) is an open cover of \( X \) , one can define analogously a chain complex \( {C}_{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) and its homology \( {H}_{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) . Apart from the direction of the arrows, the only difference from the case of a presheaf is in the definition of the coboundary operator \( \delta  : {C}_{p}\left( {\mathfrak{U},\mathcal{F}}\right)  \rightarrow \; {C}_{p - 1}\left( {\mathfrak{U},\mathcal{F}}\right) \) , which is now given by

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \in  \mathcal{F}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right) .
\]

One verifies easily that this \( \delta \) also satisfies \( {\delta }^{2} = 0 \) . The functor \( {\mathcal{H}}_{c}^{q} \) which associates to every open set \( U \) on a manifold the compact cohomology \( {H}_{c}^{q}\left( U\right) \) is covariant.

Because of the antisymmetry convention on the subscripts, in this formula there is no sign in the sum. Of course, if we had written each term \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \) with the subscript \( \alpha \) inserted in the \( i \) -th place, then there would be a sign: \( \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\alpha }_{\cdots }{\alpha }_{p - 1}} \) .

Returning to the discussion of the Čech cohomology of a presheaf \( \mathcal{F} \) , recall that the cover \( \mathfrak{V} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) is a refinement of the cover \( \mathfrak{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) , written \( \mathfrak{U} < \mathfrak{V} \) , if there is a map \( \phi  : J \rightarrow  I \) such that \( {V}_{\beta } \subset  {U}_{\phi \left( \beta \right) } \) . The refinement \( \phi \) induces a map

\[
{\phi }^{\# } : {C}^{q}\left( {\mathfrak{U},\mathcal{F}}\right)  \rightarrow  {C}^{q}\left( {\mathfrak{V},\mathcal{F}}\right)
\]

in the obvious manner:

\[
\left( {{\phi }^{\# }\omega }\right) \left( {V}_{{\beta }_{0}\ldots {\beta }_{q}}\right)  = \omega \left( {U}_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q}\right) }\right) .
\]

Lemma 10.4.1. \( {\phi }^{\# } \) is a chain map, i.e., it commutes with \( \delta \) .

\[
\text{ Proof. }\;\left( {\delta \left( {{\phi }^{\# }\omega }\right) }\right) \left( {V}_{{\beta }_{0}\ldots {\beta }_{q + 1}}\right)  = \sum {\left( -1\right) }^{i}\left( {{\phi }^{\# }\omega }\right) \left( {V}_{{\beta }_{0}\ldots {\beta }_{i}\ldots {\beta }_{q + 1}}\right)
\]

\[
= \sum {\left( -1\right) }^{i}\omega \left( {U}_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{i}\right) \ldots \phi \left( {\beta }_{q + 1}\right) }\right)
\]

\[
\left( {{\phi }^{\# }{\delta \omega }}\right) \left( {V}_{{\beta }_{0}\ldots {\beta }_{q + 1}}\right)  = \left( {\delta \omega }\right) \left( {U}_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{q + 1}\right) }\right)
\]

\[
= \sum {\left( -1\right) }^{i}\omega \left( {U}_{\phi \left( {\beta }_{0}\right) \ldots \widehat{\phi \left( {\beta }_{i}\right) }\ldots \phi \left( {\beta }_{q + 1}\right) }\right) .
\]

Lemma 10.4.2. Given \( \mathfrak{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) an open cover and \( \mathfrak{V} = {\left\{  {V}_{\beta }\right\}  }_{\beta  \in  J} \) a refinement, if \( \phi \) and \( \psi \) are two refinement maps: \( J \rightarrow  I \) , then there is a homotopy operator between \( {\phi }^{\# } \) and \( {\psi }^{\# } \) .

Proof. Define \( K : {C}^{q}\left( {\mathfrak{U},\mathcal{F}}\right)  \rightarrow  {C}^{q - 1}\left( {\mathfrak{B},\mathcal{F}}\right) \) by

\[
\left( {K\omega }\right) \left( {V}_{{\beta }_{0}\ldots {\beta }_{q - 1}}\right)  = \sum {\left( -1\right) }^{i}\omega \left( {U}_{\phi \left( {\beta }_{0}\right) \ldots \phi \left( {\beta }_{i}\right) \psi \left( {\beta }_{i}\right) \ldots \psi \left( {\beta }_{q - 1}\right) }\right) .
\]

Exercise 10.5. Show that

\[
{\psi }^{ * } - {\phi }^{ * } = {\delta K} + {K\delta }
\]

A direct system of groups is a collection of groups \( {\left\{  {G}_{i}\right\}  }_{i \in  I} \) indexed by a directed set \( I \) such that for any pair \( a < b \) there is a group homomorphism \( {f}_{b}^{a} : {G}_{a} \rightarrow  {G}_{b} \) satisfying

(1) \( {f}_{a}^{a} = \) identity,

(2) \( {f}_{c}^{a} = {f}_{c}^{b} \circ  {f}_{b}^{a} \) , if \( a < b < c \) .

On the disjoint union \( \coprod  {G}_{i} \) we introduce an equivalence relation \( \sim \) by decreeing two elements \( {g}_{a} \) in \( {G}_{a} \) and \( {g}_{b} \) in \( {G}_{b} \) to be equivalent if for some upper bound \( c \) of \( a \) and \( b \) , we have \( {f}_{c}^{a}\left( {g}_{a}\right)  = {f}_{c}^{b}\left( {g}_{b}\right) \) in \( {G}_{c} \) . The direct limit of the direct system, denoted by \( \mathop{\lim }\limits_{{i \in  I}}{G}_{i} \) , is the quotient of \( \coprod  {G}_{i} \) by the equivalence relation \( \sim \) ; in other words, two elements of \( \coprod  {G}_{i} \) represent the same element in the direct limit if they are "eventually equal". We make the direct limit into a group by defining \( \left\lbrack  {g}_{a}\right\rbrack   + \left\lbrack  {g}_{b}\right\rbrack   = \left\lbrack  {{f}_{c}^{a}\left( {g}_{a}\right)  + {f}_{c}^{b}\left( {g}_{b}\right) }\right\rbrack \) , where \( \left\lbrack  {g}_{a}\right\rbrack \) is the equivalence class of \( {g}_{a} \) .

It follows from the two lemmas above that if \( \mathfrak{u} < \mathfrak{V} \) , then there is a well-defined map in cohomology

\[
{H}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right)  \rightarrow  {H}^{ * }\left( {\mathfrak{V},\mathcal{F}}\right) ,
\]

making \( \{ {H}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right) {\} }_{\mathfrak{U}} \) into a direct system of groups. The direct limit of this direct system

\[
{H}^{ * }\left( {X,\mathcal{F}}\right)  = \mathop{\lim }\limits_{u}{H}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right)
\]

is the Čech cohomology of \( X \) with values in the presheaf \( \mathcal{F} \) .

Proposition 10.6. Let \( \mathbb{R} \) be the constant presheaf on a manifold \( M \) . Then the Čech cohomology of \( M \) with values in \( \mathbb{R} \) is isomorphic to the de Rham cohomology.

Proof. Since the good covers are cofinal in the set of all covers of \( M \) (Corollary 5.2), we can use only good covers in the direct limit

\[
{H}^{ * }\left( {M,\mathbb{R}}\right)  = \mathop{\lim }\limits_{\mathfrak{u}}{H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) .
\]

By Theorem 8.9,

\[
{H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right)  \simeq  {H}_{DR}^{ * }\left( M\right)
\]

for any good cover of \( M \) . Moreover, it is easily seen that this isomorphism is compatible with refinement of good covers. Therefore, there is an isomorphism

\[
{H}^{ * }\left( {M,\mathbb{R}}\right)  \simeq  {H}_{DR}^{ * }\left( M\right)
\]

Exercise 10.7 (Cohomology with Twisted Coefficients). Let \( \mathcal{F} \) be the presheaf on \( {S}^{1} \) which associates to every open set the group \( \mathbb{Z} \) . We define the restriction homomorphism on the good cover \( \mathfrak{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) (Figure 10.1) by

\[
{\rho }_{01}^{0} = {\rho }_{01}^{1} = 1
\]

\[
{\rho }_{12}^{1} = {\rho }_{12}^{2} = 1
\]

\[
{\rho }_{02}^{2} =  - 1,{\rho }_{02}^{0} = 1,
\]

where \( {\rho }_{ij}^{i} \) is the restriction from \( {U}_{i} \) to \( {U}_{i} \cap  {U}_{j} \) . Compute \( {H}^{ * }\left( {\mathfrak{U},\mathcal{F}}\right) \) . (Cf. presheaf on an open cover, p. 142.)

![bo_d7b6f8alb0pc73dd9avg_123_629_704_380_376_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_123_629_704_380_376_0.jpg)

Figure 10.1
