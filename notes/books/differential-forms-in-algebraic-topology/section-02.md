## §2 The Mayer-Vietoris Sequence

In this section we extend the definition of the de Rham cohomology from \( {\mathbb{R}}^{n} \) to any differentiable manifold and introduce a basic technique for computing the de Rham cohomology, the Mayer-Vietoris sequence. But first we have to discuss the functorial nature of the de Rham complex.

The Functor \( {\Omega }^{ * } \)

Let \( {x}_{1},\ldots ,{x}_{m} \) and \( {y}_{1},\ldots ,{y}_{n} \) be the standard coordinates on \( {\mathbb{R}}^{m} \) and \( {\mathbb{R}}^{n} \) respectively. A smooth map \( f : {\mathbb{R}}^{m} \rightarrow  {\mathbb{R}}^{n} \) induces a pullback map on \( {C}^{\infty } \) functions \( {f}^{ * } : {\Omega }^{0}\left( {\mathbb{R}}^{n}\right)  \rightarrow  {\Omega }^{0}\left( {\mathbb{R}}^{m}\right) \) via

\[
{f}^{ * }\left( g\right)  = g \circ  f
\]

We would like to extend this pullback map to all forms \( {f}^{ * } : {\Omega }^{ * }\left( {\mathbb{R}}^{n}\right)  \rightarrow \; {\Omega }^{ * }\left( {\mathbb{R}}^{m}\right) \) in such a way that it commutes with \( d \) . The commutativity with \( d \) defines \( {f}^{ * } \) uniquely:

\[
{f}^{ * }\left( {\sum {g}_{I}d{y}_{{i}_{1}}\ldots d{y}_{{i}_{q}}}\right)  = \sum \left( {{g}_{I} \circ  f}\right) d{f}_{{i}_{1}}\ldots d{f}_{{i}_{q}},
\]

where \( {f}_{i} = {y}_{i} \circ  f \) is the \( i \) -th component of the function \( f \) .

Proposition 2.1. With the above definition of the pullback map \( {f}^{ * } \) on forms, \( {f}^{ * } \) commutes with d.

Proof. The proof is essentially an application of the chain rule.

\[
d{f}^{ * }\left( {{g}_{I}d{y}_{{i}_{1}}\ldots d{y}_{{i}_{q}}}\right)  = d\left( {\left( {{g}_{I} \circ  f}\right) d{f}_{{i}_{1}}\ldots d{f}_{{i}_{q}}}\right)  = d\left( {{g}_{I} \circ  f}\right) d{f}_{{i}_{1}}\ldots d{f}_{{i}_{q}}.
\]

\[
{f}^{ * }d\left( {{g}_{I}d{y}_{{i}_{1}}\ldots d{y}_{{i}_{q}}}\right)  = {f}^{ * }\left( {\mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial {g}_{I}}{\partial {y}_{i}}d{y}_{i}d{y}_{{i}_{1}}\ldots d{y}_{{i}_{q}}}\right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{n}\left( {\left( {\frac{\partial {g}_{I}}{\partial {y}_{i}} \circ  f}\right) d{f}_{i}}\right) d{f}_{{i}_{1}}\ldots d{f}_{{i}_{q}}
\]

\[
= d\left( {{g}_{I} \circ  f}\right) d{f}_{{i}_{1}}\ldots d{f}_{{i}_{q}}.
\]

Let \( {x}_{1},\ldots ,{x}_{n} \) be the standard coordinate system and \( {u}_{1},\ldots {u}_{n} \) a new coordinate system on \( {\mathbb{R}}^{n} \) , i.e., there is a diffeomorphism \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) such that \( {u}_{i} = {x}_{i} \circ  f = {f}^{ * }\left( {x}_{i}\right) \) . By the chain rule, if \( g \) is a smooth function on \( {\mathbb{R}}^{n} \) , then

\[
\mathop{\sum }\limits_{i}\frac{\partial g}{\partial {u}_{i}}d{u}_{i} = \mathop{\sum }\limits_{{i, j}}\frac{\partial g}{\partial {u}_{i}}\frac{\partial {u}_{i}}{\partial {x}_{j}}d{x}_{j} = \mathop{\sum }\limits_{j}\frac{\partial g}{\partial {x}_{j}}d{x}_{j}.
\]

So \( {dg} \) is independent of the coordinate system.

Exercise 2.1.1. More generally show that if \( \omega  = \sum {g}_{I}d{u}_{I} \) , then \( {d\omega } = \sum d{g}_{I} \; d{u}_{I} \) .

Thus the exterior derivative \( d \) is independent of the coordinate system on \( {\mathbb{R}}^{n} \) .

Recall that a category consists of a class of objects and for any two objects \( A \) and \( B \) , a set \( \operatorname{Hom}\left( {A, B}\right) \) of morphisms from \( A \) to \( B \) , satisfying the following properties. If \( f \) is a morphism from \( A \) to \( B \) and \( g \) a morphism from \( B \) to \( C \) , then the composite morphism \( g \circ  f \) from \( A \) to \( C \) is defined; furthermore, the composition operation is required to be associative and to have an identity \( {1}_{A} \) in \( \operatorname{Hom}\left( {A, A}\right) \) for every object \( A \) . The class of all groups together with the group homomorphisms is an example of a category.

A covariant functor \( F \) from a category \( \mathcal{K} \) to a category \( \mathcal{L} \) associates to every object \( A \) in \( \mathcal{K} \) an object \( F\left( A\right) \) in \( \mathcal{L} \) , and every morphism \( f : A \rightarrow  B \) in \( \mathcal{K} \) a morphism \( F\left( f\right)  : F\left( A\right)  \rightarrow  F\left( B\right) \) in \( \mathcal{L} \) such that \( F \) preserves composition and the identity:

\[
F\left( {g \circ  f}\right)  = F\left( g\right)  \circ  F\left( f\right)
\]

\[
F\left( {1}_{A}\right)  = {1}_{F\left( A\right) }.
\]

If \( F \) reverses the arrows, i.e., \( F\left( f\right)  : F\left( B\right)  \rightarrow  F\left( A\right) \) , it is said to be a contravariant functor.

In this fancier language the discussion above may be summarized as follows: \( {\Omega }^{ * } \) is a contravariant functor from the category of Euclidean spaces \( {\left\{  {\mathbb{R}}^{n}\right\}  }_{n \in  \mathbb{Z}} \) and smooth maps: \( {\mathbb{R}}^{m} \rightarrow  {\mathbb{R}}^{n} \) to the category of commutative differential graded algebras and their homomorphisms. It is the unique such functor that is the pullback of functions on \( {\Omega }^{0}\left( {\mathbb{R}}^{n}\right) \) . Here the commutativity of the graded algebra refers to the fact that

\[
{\tau \omega } = {\left( -1\right) }^{\deg \tau \deg \omega }{\omega \tau }.
\]

The functor \( {\Omega }^{ * } \) may be extended to the category of differentiable manifolds. For the fundamentals of manifold theory we recommend de Rham [1, Chap. I]. Recall that a differentiable structure on a manifold is given by an atlas, i.e., an open cover \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  A} \) of \( M \) in which each open set \( {U}_{\alpha } \) is homeomorphic to \( {\mathbb{R}}^{n} \) via a homeomorphism \( {\phi }_{\alpha } : {U}_{\alpha } \simeq  {\mathbb{R}}^{n} \) , and on the overlaps \( {U}_{\alpha } \cap  {U}_{\beta } \) the transition functions

\[
{g}_{\alpha \beta } = {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1} : {\phi }_{\beta }\left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)  \rightarrow  {\phi }_{\alpha }\left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)
\]

are diffeomorphisms of open subsets of \( {\mathbb{R}}^{n} \) ; furthermore, the atlas is required to be maximal with respect to inclusions. All manifolds will be assumed to be Hausdorff and to have a countable basis. The collection \( {\left\{  \left( {U}_{\alpha },{\phi }_{\alpha }\right) \right\}  }_{\alpha  \in  A} \) is called a coordinate open cover of \( M \) and \( {\phi }_{\alpha } \) is the trivialization of \( {U}_{\alpha } \) . Let \( {u}_{1},\ldots ,{u}_{n} \) be the standard coordinates on \( {\mathbb{R}}^{n} \) . We can write \( {\phi }_{\alpha } = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) , where \( {x}_{i} = {u}_{i} \circ  {\phi }_{\alpha } \) are a coordinate system on \( {U}_{\alpha } \) . A function \( f \) on \( {U}_{\alpha } \) is differentiable if \( f \circ  {\phi }_{\alpha }^{-1} \) is a differentiable function on \( {\mathbb{R}}^{n} \) . If \( f \) is a differentiable function on \( {U}_{\alpha } \) , the partial derivative \( \partial f/\partial {x}_{i} \) is defined to be the \( i \) -th partial of the pullback function \( f \circ  {\phi }_{\alpha }^{-1} \) on \( {\mathbb{R}}^{n} \) :

\[
\frac{\partial f}{\partial {x}_{i}}\left( p\right)  = \frac{\partial \left( {f \circ  {\phi }_{\alpha }^{-1}}\right) }{\partial {u}_{i}}\left( {{\phi }_{\alpha }\left( p\right) }\right) .
\]

The tangent space to \( M \) at \( p \) , written \( {T}_{p}M \) , is the vector space over \( \mathbb{R} \) spanned by the operators \( \partial /\partial {x}_{1}\left( p\right) ,\ldots ,\partial /\partial {x}_{n}\left( p\right) \) , and a smooth vector field on \( {U}_{\alpha } \) is a linear combination \( {X}_{\alpha } = \sum {f}_{i}\partial /\partial {x}_{i} \) where the \( {f}_{i} \) ’s are smooth functions on \( {U}_{\alpha } \) . Relative to another coordinate system \( \left( {{y}_{1},\ldots ,{y}_{n}}\right) ,{X}_{\alpha } = \; \sum {g}_{j}\partial /\partial {y}_{i} \) where \( \partial /\partial {x}_{i} \) and \( \partial /\partial {y}_{j} \) satisfy the chain rule:

\[
\frac{\partial }{\partial {x}_{i}} = \sum \frac{\partial {y}_{j}}{\partial {x}_{i}}\frac{\partial }{\partial {y}_{j}}.
\]

A \( {\mathrm{C}}^{\infty } \) vector field on \( M \) may be viewed as a collection of vector fields \( {X}_{\alpha } \) on \( {U}_{\alpha } \) which agree on the overlaps \( {U}_{\alpha } \cap  {U}_{\beta } \) .

A differential form \( \omega \) on \( M \) is a collection of forms \( {\omega }_{U} \) for \( U \) in the atlas defining \( M \) , which are compatible in the following sense: if \( i \) and \( j \) are the inclusions

![bo_d7b6f8alb0pc73dd9avg_31_684_1313_275_161_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_31_684_1313_275_161_0.jpg)

then \( {i}^{ * }{\omega }_{U} = {j}^{ * }{\omega }_{V} \) in \( {\Omega }^{ * }\left( {U \cap  V}\right) \) . By the functoriality of \( {\Omega }^{ * } \) , the exterior derivative and the wedge product extend to differential forms on a manifold. Just as for \( {\mathbb{R}}^{n} \) a smooth map of differentiable manifolds \( f : M \rightarrow  N \) induces in a natural way a pullback map on forms \( {f}^{ * } : {\Omega }^{ * }\left( N\right)  \rightarrow  {\Omega }^{ * }\left( M\right) \) . In this way \( {\Omega }^{ * } \) becomes a contravariant functor on the category of differentiable manifolds.

A partition of unity on a manifold \( M \) is a collection of non-negative \( {C}^{\infty } \) functions \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  I} \) such that

(a) Every point has a neighborhood in which \( \sum {\rho }_{\alpha } \) is a finite sum.

(b) \( \sum {\rho }_{\alpha } = 1 \) .

The basic technical tool in the theory of differentiable manifolds is the existence of a partition of unity. This result assumes two forms:

(1) Given an open cover \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) of \( M \) , there is a partition of unity \( {\left\{  {\rho }_{\alpha }\right\}  }_{\alpha  \in  I} \) such that the support of \( {\rho }_{\alpha } \) is contained in \( {U}_{\alpha } \) . We say in this case that \( \left\{  {\rho }_{\alpha }\right\} \) is a partition of unity subordinate to the open cover \( \left\{  {U}_{\alpha }\right\} \) .

(2) Given an open cover \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) of \( M \) , there is a partition of unity \( {\left\{  {\rho }_{\beta }\right\}  }_{\beta  \in  J} \) with compact support, but possibly with an index set \( J \) different from \( I \) , such that the support of \( {\rho }_{\beta } \) is contained in some \( {U}_{\alpha } \) .

For a proof see Warner [1, p. 10] or de Rham [1, p. 3].

Note that in (1) the support of \( {\rho }_{\alpha } \) is not assumed to be compact and the index set of \( \left\{  {\rho }_{\alpha }\right\} \) is the same as that of \( \left\{  {U}_{\alpha }\right\} \) , while in (2) the reverse is true. We usually cannot demand simultaneously compact support and the same index set on a noncompact manifold \( M \) . For example, consider the open cover of \( {\mathbb{R}}^{1} \) consisting of precisely one open set, namely \( {\mathbb{R}}^{1} \) itself. This open cover clearly does not have a partition of unity with compact support subordinate to it.

## The Mayer-Vietoris Sequence

The Mayer-Vietoris sequence allows one to compute the cohomology of the union of two open sets. Suppose \( M = U \cup  V \) with \( U, V \) open. Then there is a sequence of inclusions

\[
M \leftarrow  U \coprod  V\underset{{\partial }_{1}}{ \leftleftarrows  }U \cap  V
\]

where \( U \coprod  V \) is the disjoint union of \( U \) and \( V \) and \( {\partial }_{0} \) and \( {\partial }_{1} \) are the inclusions of \( U \cap  V \) in \( V \) and in \( U \) respectively. Applying the contravariant functor \( {\Omega }^{ * } \) , we get a sequence of restrictions of forms

\[
{\Omega }^{ * }\left( M\right)  \rightarrow  {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right) \overset{{\partial }_{0}^{ * }}{\underset{{\partial }_{1}^{ * }}{ \rightrightarrows  }}{\Omega }^{ * }\left( {U \cap  V}\right)
\]

where by the restriction of a form to a submanifold we mean its image under the pullback map induced by the inclusion. By taking the difference of the last two maps, we obtain the Mayer-Vietoris sequence

(2.2)

\[
0 \rightarrow  {\Omega }^{ * }\left( M\right)  \rightarrow  {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right)  \rightarrow  {\Omega }^{ * }\left( {U \cap  V}\right)  \rightarrow  0
\]

\[
\left( {\omega ,\tau }\right) \; \mapsto  \;\tau  - \omega
\]

Proposition 2.3. The Mayer-Vietoris sequence is exact.

Proof. The exactness is clear except at the last step. We first consider the case of functions on \( M = {\mathbb{R}}^{1} \) . Let \( f \) be a \( {C}^{\infty } \) function on \( U \cap  V \) as shown in Figure 2.1. We must write \( f \) as the difference of a function on \( U \) and a function on \( V \) . Let \( \left\{  {{\rho }_{U},{\rho }_{V}}\right\} \) be a partition of unity subordinate to the open cover \( \{ U, V\} \) . Note that \( {\rho }_{V}f \) is a function on \( U \) -to get a function on an open set we must multiply by the partition function of the other open set. Since

\[
\left( {{\rho }_{U}f}\right)  - \left( {-{\rho }_{V}f}\right)  = f
\]

we see that \( {\Omega }^{0}\left( U\right)  \oplus  {\Omega }^{0}\left( V\right)  \rightarrow  {\Omega }^{0}\left( {\mathbb{R}}^{1}\right) \) is surjective. For a general manifold \( M \) , if \( \omega  \in  {\Omega }^{q}\left( {U \cap  V}\right) \) , then \( \left( {-{\rho }_{V}\omega ,{\rho }_{U}\omega }\right) \) in \( {\Omega }^{q}\left( U\right)  \oplus  {\Omega }^{q}\left( V\right) \) maps onto \( \omega \) .

![bo_d7b6f8alb0pc73dd9avg_33_380_298_868_535_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_33_380_298_868_535_0.jpg)

Figure 2.1

The Mayer-Vietoris sequence

\[
0 \rightarrow  {\Omega }^{ * }\left( M\right)  \rightarrow  {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right)  \rightarrow  {\Omega }^{ * }\left( {U \cap  V}\right)  \rightarrow  0
\]

induces a long exact sequence in cohomology, also called a Mayer-Vietoris sequence:(2.4)

![bo_d7b6f8alb0pc73dd9avg_33_388_1300_855_230_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_33_388_1300_855_230_0.jpg)

We recall again the definition of the coboundary operator \( {d}^{ * } \) in this explicit instance. The short exact sequence gives rise to a diagram with exact rows

![bo_d7b6f8alb0pc73dd9avg_33_309_1636_1014_359_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_33_309_1636_1014_359_0.jpg)

Let \( \omega  \in  {\Omega }^{q}\left( {U \cap  V}\right) \) be a closed form. By the exactness of the rows, there is a \( \xi  \in  {\Omega }^{q}\left( U\right)  \oplus  {\Omega }^{q}\left( V\right) \) which maps to \( \omega \) , namely, \( \xi  = \left( {-{\rho }_{V}\omega ,{\rho }_{U}\omega }\right) \) . By the commutativity of the diagram and the fact that \( {d\omega } = 0,{d\xi } \) goes to 0 in \( {\Omega }^{q + 1}\left( {U \cap  V}\right) \) , i.e., \( - d\left( {{\rho }_{V}\omega }\right) \) and \( d\left( {{\rho }_{U}\omega }\right) \) agree on the overlap \( U \cap  V \) . Hence \( {d\xi } \) is the image of an element in \( {\Omega }^{q + 1}\left( M\right) \) . This element is easily seen to be closed and represents \( {d}^{ * }\left\lbrack  \omega \right\rbrack \) . As remarked earlier, it can be shown that \( {d}^{ * }\left\lbrack  \omega \right\rbrack \) is independent of the choices in this construction. Explicitly we see that the coboundary operator is given by

(2.5)

\[
{d}^{ * }\left\lbrack  \omega \right\rbrack   = \left\{  \begin{matrix} \left\lbrack  {-d\left( {{\rho }_{V}\omega }\right) }\right\rbrack  & \text{ on } & U \\  \left\lbrack  {d\left( {{\rho }_{U}\omega }\right) }\right\rbrack  & \text{ on } & V. \end{matrix}\right.
\]

We define the support of a form \( \omega \) on a manifold \( M \) to be Supp \( \omega \; = \overline{\{ p \in  M \mid  \omega \left( p\right)  \neq  0\} } \) . Note that in the Mayer-Vietoris sequence \( {d}^{ * }\omega  \in \; H * \left( M\right) \) has support in \( U \cap  V \) .

EXAMPLE 2.6 (The cohomology of the circle). Cover the circle with two open sets \( U \) and \( V \) as shown in Figure 2.2. The Mayer-Vietoris sequence gives

![bo_d7b6f8alb0pc73dd9avg_34_406_931_861_287_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_34_406_931_861_287_0.jpg)

The difference map \( \delta \) sends \( \left( {\omega ,\tau }\right) \) to \( \left( {\tau  - \omega ,\tau  - \omega }\right) \) , so im \( \delta \) is 1- dimensional. It follows that ker \( \delta \) is also 1-dimensional. Therefore,

\[
{H}^{0}\left( {S}^{1}\right)  = \ker \delta  = \mathbb{R}
\]

\[
{H}^{1}\left( {S}^{1}\right)  = \text{ coker }\delta  = \mathbb{R}.
\]

We now find an explicit representative for the generator of \( {H}^{1}\left( {S}^{1}\right) \) . If \( \alpha  \in  {\Omega }^{0}\left( {U \cap  V}\right) \) is a closed 0 -form which is not the image under \( \delta \) of a closed form in \( {\Omega }^{0}\left( U\right)  \oplus  {\Omega }^{0}\left( V\right) \) , then \( {d}^{ * }\alpha \) will represent a generator of \( {H}^{1}\left( {S}^{1}\right) \) . As \( \alpha \) we may take the function which is 1 on the upper piece of \( U \cap  V \) and 0 on

![bo_d7b6f8alb0pc73dd9avg_34_486_1648_710_433_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_34_486_1648_710_433_0.jpg)

Figure 2.2

![bo_d7b6f8alb0pc73dd9avg_35_315_286_983_1254_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_35_315_286_983_1254_0.jpg)

Figure 2.3 the lower piece (see Figure 2.3). Now \( \alpha \) is the image of \( \left( {-{\rho }_{V}\alpha ,{\rho }_{U}\alpha }\right) \) . Since \( - d\left( {{\rho }_{V}\alpha }\right) \) and \( d{\rho }_{U}\alpha \) agree on \( U \cap  V \) , they represent a global form on \( {S}^{1} \) ; this form is \( {d}^{ * }\alpha \) . It is a bump 1-form with support in \( U \cap  V \) .

## The Functor \( {\Omega }_{c}^{ * } \) and the Mayer-Vietoris Sequence for Compact Supports

Again, before taking up the Mayer-Vietoris sequence for compactly supported cohomology, we need to discuss the functorial properties of \( {\Omega }_{c}^{ * }\left( M\right) \) , the algebra of forms with compact support on the manifold \( M \) . In general the pullback by a smooth map of a form with compact support need not have compact support; for example, consider the pullback of functions under the projection \( M \times  \mathbb{R} \rightarrow  M \) . So \( {\Omega }_{c}^{ * } \) is not a functor on the category of manifolds and smooth maps. However if we consider not all smooth maps, but only an appropriate subset of smooth maps, then \( {\Omega }_{c}^{ * } \) can be made into a functor. There are two ways in which this can be done.

(a) \( {\Omega }_{c}^{ * } \) is a contravariant functor under proper maps. (A map is proper if the inverse image of every compact set is compact.)

(b) \( {\Omega }_{c}^{ * } \) is a covariant functor under inclusions of open sets.

If \( j : U \rightarrow  M \) is the inclusion of the open subset \( U \) in the manifold \( M \) , then \( {j}_{ * } : {\Omega }_{c}^{ * }\left( U\right)  \rightarrow  {\Omega }_{c}^{ * }\left( M\right) \) is the map which extends a form on \( U \) by zero to a form on \( M \) .

It is the covariant nature of \( {\Omega }_{c}^{ * } \) which we shall exploit to prove Poincaré duality for noncompact manifolds. So from now on we assume that \( {\Omega }_{c}^{ * } \) refers to the covariant functor in (b). There is also a Mayer-Vietoris sequence for this functor. As before, let \( M \) be covered by two open sets \( U \) and \( V \) . The sequence of inclusions

\[
M \leftarrow  U \coprod  V \leftleftarrows  U \cap  V
\]

gives rise to a sequence of forms with compact support

\[
{\Omega }_{c}^{ * }\left( M\right) \underset{\text{ sum }}{ \leftarrow  }{\Omega }_{c}^{ * }\left( U\right)  \oplus  {\Omega }_{c}^{ * }\left( V\right) \underset{\text{ inclusion }}{\underset{\text{ signed }}{ \leftrightarrows  }}{\Omega }_{c}^{ * }\left( {U \cap  V}\right)
\]

\[
\left( {-{j}_{ * }\omega ,{j}_{ * }\omega }\right)  \leftarrow  \omega
\]

Proposition 2.7. The Mayer-Vietoris sequence of forms with compact support

\[
0 \leftarrow  {\Omega }_{c}^{ * }\left( M\right)  \leftarrow  {\Omega }_{c}^{ * }\left( U\right)  \oplus  {\Omega }_{c}^{ * }\left( V\right)  \leftarrow  {\Omega }_{c}^{ * }\left( {U \cap  V}\right)  \leftarrow  0
\]

is exact.

Proof. This time exactness is easy to check at every step. We do it for the last step. Let \( \omega \) be a form in \( {\Omega }_{c}^{ * }\left( M\right) \) . Then \( \omega \) is the image of \( \left( {{\rho }_{U}\omega ,{\rho }_{V}\omega }\right) \) in \( {\Omega }_{c}^{ * }\left( U\right) \bigoplus {\Omega }_{c}^{ * }\left( V\right) \) . The form \( {\rho }_{U}\omega \) has compact support because Supp \( {\rho }_{U}\omega \) C Supp \( {\rho }_{U} \cap \) Supp \( \omega \) and by a lemma from general topology, a closed subset of a compact set in a Hausdorff space is compact. This shows the surjectivity of the map \( {\Omega }_{c}^{ * }\left( U\right) \bigoplus {\Omega }_{c}^{ * }\left( V\right)  \rightarrow  {\Omega }_{c}^{ * }\left( M\right) \) . Note that whereas in the previous Mayer-Vietoris sequence we multiply by \( {\rho }_{V} \) to get a form on \( U \) , here \( {\rho }_{U}\omega \) is a form on \( U \) .

Again the Mayer-Vietoris sequence gives rise to a long exact sequence in cohomology:

(2.8)

\[
\begin{array}{l} {C}_{{H}_{c}^{q + 1}}\left( M\right)  \leftarrow  {H}_{c}^{q + 1}\left( U\right)  \oplus  {H}_{c}^{q + 1}\left( V\right)  \leftarrow  {H}_{c}^{q + 1}\left( {U \cap  V}\right)  \oplus  \\  {d}_{ * } \\  {H}_{c}^{q}\left( M\right)  \leftarrow  {H}_{c}^{q}\left( U\right)  \oplus  {H}_{c}^{q}\left( V\right)  \leftarrow  {H}_{c}^{q}\left( {U \cap  V}\right)  \end{array}
\]

![bo_d7b6f8alb0pc73dd9avg_37_401_300_807_363_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_37_401_300_807_363_0.jpg)

Figure 2.4

EXAMPLE 2.9 (The cohomology with compact support of the circle). Of course since \( {S}^{1} \) is compact, the cohomology with compact support \( {H}_{c}^{ * }\left( {S}^{1}\right) \) should be the same as the ordinary de Rham cohomology \( {H}^{ * }\left( {S}^{1}\right) \) . Nonetheless, as an illustration we will compute \( {H}_{c}^{ * }\left( {S}^{1}\right) \) from the Mayer-Vietoris sequence for compact supports:

![bo_d7b6f8alb0pc73dd9avg_37_256_955_844_241_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_37_256_955_844_241_0.jpg)

Here the map \( \delta \) sends \( \omega  = \left( {{\omega }_{1},{\omega }_{2}}\right)  \in  {H}_{c}^{1}\left( {U \cap  V}\right) \) to \( \left( {-{\left( {j}_{U}\right) }_{ * }\omega ,{\left( {j}_{V}\right) }_{ * }\omega }\right)  \in \; {H}_{c}^{1}\left( U\right)  \oplus  {H}_{c}^{1}\left( V\right) \) , where \( {j}_{U} \) and \( {j}_{V} \) are the inclusions of \( U \cap  V \) in \( U \) and in \( V \) respectively. Since im \( \delta \) is 1-dimensional,

\[
{H}_{c}^{0}\left( {S}^{1}\right)  = \ker \delta  = \mathbb{R}
\]

\[
{H}_{c}^{1}\left( {S}^{1}\right)  = \text{ coker }\delta  = \mathbb{R}.
\]
