## Appendix B Review of Tensors

Of all the constructions in smooth manifold theory, the ones that play the most fundamental roles in Riemannian geometry are tensors and tensor fields. Most of the technical machinery of Riemannian geometry is built up using tensors; indeed, Riemannian metrics themselves are tensor fields. This appendix offers a brief review of their definitions and properties. For a more detailed exposition of the material summarized here, see [LeeSM].

## Tensors on a Vector Space

We begin with tensors on a finite-dimensional vector space. There are many ways of constructing tensors on a vector space, but for simplicity we will stick with the most concrete description, as real-valued multilinear functions. The simplest tensors are just linear functionals, also called covectors.

## Covectors

Let \( V \) be an \( n \) -dimensional vector space (all of our vector spaces are assumed to be real). When we work with bases for \( V \) , it is usually important to consider ordered bases, so will assume that each basis comes endowed with a specific ordering. We use parentheses to denote ordered \( k \) -tuples, and braces to denote unordered ones, so an ordered basis is designated by either \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) or \( \left( {b}_{i}\right) \) , and the corresponding unordered basis by \( \left\{  {{b}_{1},\ldots ,{b}_{n}}\right\} \) or \( \left\{  {b}_{i}\right\} \) .

The dual space of \( V \) , denoted by \( {V}^{ * } \) , is the space of linear maps from \( V \) to \( \mathbb{R} \) . Elements of the dual space are called covectors or linear functionals on \( V \) . Under the operations of pointwise addition and multiplication by constants, \( {V}^{ * } \) is a vector space.

Suppose \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) is an ordered basis for \( V \) . For each \( i = 1,\ldots , n \) , define a covector \( {\beta }^{i} \in  {V}^{ * } \) by

\[
{\beta }^{i}\left( {b}_{j}\right)  = {\delta }_{j}^{i},
\]

where \( {\delta }_{j}^{i} \) is the Kronecker delta symbol, defined by

\[
{\delta }_{j}^{i} = \left\{  \begin{array}{ll} 1 & \text{ if }i = j \\  0 & \text{ if }i \neq  j \end{array}\right. \tag{B.1}
\]

It is a standard exercise to prove that \( \left( {{\beta }^{1},\ldots ,{\beta }^{n}}\right) \) is a basis for \( {V}^{ * } \) , called the dual basis to \( \left( {b}_{i}\right) \) . Therefore, \( {V}^{ * } \) is finite-dimensional, and its dimension is the same as that of \( V \) . Every covector \( \omega  \in  {V}^{ * } \) can thus be written in terms of the dual basis as

\[
\omega  = {\omega }_{j}{\beta }^{j}, \tag{B.2}
\]

where the components \( {\omega }_{j} \) are defined by \( {\omega }_{j} = \omega \left( {b}_{j}\right) \) . The action of \( \omega \) on an arbitrary vector \( v = {v}^{i}{b}_{i} \in  V \) is then given by

\[
\omega \left( v\right)  = {\omega }_{j}{v}^{j}. \tag{B.3}
\]

(Here and throughout the rest of this appendix we use the Einstein summation convention; see p. 375.)

Every vector \( v \in  V \) uniquely determines a linear functional on \( {V}^{ * } \) , by \( \omega  \mapsto  \omega \left( v\right) \) . Because we are assuming \( V \) to be finite-dimensional, it is straightforward to show that this correspondence gives a canonical (basis-independent) isomorphism between \( V \) and \( {V}^{* * } \) (the dual space of \( {V}^{ * } \) ). Given \( \omega  \in  {V}^{ * } \) and \( v \in  V \) , we can denote the natural action of \( \omega \) on \( v \) either by the traditional functional notation \( \omega \left( v\right) \) , or by either of the more symmetric notations \( \langle \omega , v\rangle \) or \( \langle v,\omega \rangle \) . The latter notations are meant to emphasize that it does not matter whether we think of the resulting number as the effect of the linear functional \( \omega \) acting on the vector \( v \) , or as the effect of \( v \in  {V}^{* * } \) acting on the covector \( \omega \) . Note that when applied to a vector and a covector, this pairing makes sense without any choice of an inner product on \( V \) .

## Higher-Rank Tensors on a Vector Space

Now we generalize from linear functionals to multilinear ones. If \( {V}_{1},\ldots ,{V}_{k} \) and \( W \) are vector spaces, a map \( F : {V}_{1} \times  \cdots  \times  {V}_{k} \rightarrow  W \) is said to be multilinear if it is linear as a function of each variable separately, when all the others are held fixed:

\[
F\left( {{v}_{1},\ldots , a{v}_{i} + {a}^{\prime }{v}_{i}^{\prime },\ldots ,{v}_{k}}\right)  = {aF}\left( {{v}_{1},\ldots ,{v}_{i},\ldots ,{v}_{k}}\right)  + {a}^{\prime }F\left( {{v}_{1},\ldots ,{v}_{i}^{\prime },\ldots ,{v}_{k}}\right) .
\]

Given a finite-dimensional vector space \( V \) , a covariant \( k \) -tensor on \( V \) is a multilinear map

\[
F : \underset{k\text{ copies }}{\underbrace{V \times  \cdots  \times  V}} \rightarrow  \mathbb{R}
\]

Similarly, a contravariant \( k \) -tensor on \( V \) is a multilinear map

\[
F : \underset{k\text{ copies }}{\underbrace{{V}^{ * } \times  \cdots  \times  {V}^{ * }}} \rightarrow  \mathbb{R}.
\]

We often need to consider tensors of mixed types as well. A mixed tensor of type \( \left( {\mathbf{k},\mathbf{l}}\right) \) , also called a k-contravariant, l-covariant tensor, is a multilinear map

\[
F : \underset{k\text{ copies }}{\underbrace{{V}^{ * } \times  \cdots  \times  {V}^{ * }}} \times  \underset{l\text{ copies }}{\underbrace{V \times  \cdots  \times  V}} \rightarrow  \mathbb{R}.
\]

Actually, in many cases it is necessary to consider real-valued multilinear functions whose arguments consist of \( k \) covectors and \( l \) vectors, but not necessarily in the order implied by the definition above; such an object is still called a tensor of type \( \left( {k, l}\right) \) . For any given tensor, we will make it clear which arguments are vectors and which are covectors.

The spaces of tensors on \( V \) of various types are denoted by

\[
{T}^{k}\left( {V}^{ * }\right)  = \{ \text{ covariant }k\text{ -tensors on }V\}
\]

\[
{T}^{k}\left( V\right)  = \{ \text{ contravariant }k\text{ -tensors on }V\}
\]

\[
{T}^{\left( k, l\right) }\left( V\right)  = \{ \text{ mixed }\left( {k, l}\right) \text{ -tensors on }V\} .
\]

The rank of a tensor is the number of arguments (vectors and/or covectors) it takes. By convention, a 0-tensor is just a real number. (You should be aware that the notation conventions for describing the spaces of covariant, contravariant, and mixed tensors are not universally agreed upon. Be sure to look closely at each author's conventions.)

## Tensor Products

There is a natural product, called the tensor product, linking the various tensor spaces over \( V \) : if \( F \in  {T}^{\left( k, l\right) }\left( V\right) \) and \( G \in  {T}^{\left( p, q\right) }\left( V\right) \) , the tensor \( F \otimes  G \in \; {T}^{\left( k + p, l + q\right) }\left( V\right) \) is defined by

\[
F \otimes  G\left( {{\omega }^{1},\ldots ,{\omega }^{k + p},{v}_{1},\ldots ,{v}_{l + q}}\right)
\]

\[
= F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{v}_{1},\ldots ,{v}_{l}}\right) G\left( {{\omega }^{k + 1},\ldots ,{\omega }^{k + p},{v}_{l + 1},\ldots ,{v}_{l + q}}\right) .
\]

The tensor product is associative, so we can unambiguously form tensor products of three or more tensors on \( V \) . If \( \left( {b}_{i}\right) \) is a basis for \( V \) and \( \left( {\beta }^{j}\right) \) is the associated dual basis, then a basis for \( {T}^{\left( k, l\right) }\left( V\right) \) is given by the set of all tensors of the form

\[
{b}_{{i}_{1}} \otimes  \cdots  \otimes  {b}_{{i}_{k}} \otimes  {\beta }^{{j}_{1}} \otimes  \cdots  \otimes  {\beta }^{{j}_{l}}, \tag{B.4}
\]

as the indices \( {i}_{p},{j}_{q} \) range from 1 to \( n \) . These tensors act on basis elements by

\[
{b}_{{i}_{1}} \otimes  \cdots  \otimes  {b}_{{i}_{k}} \otimes  {\beta }^{{j}_{1}} \otimes  \cdots  \otimes  {\beta }^{{j}_{l}}\left( {{\beta }^{{s}_{1}},\ldots ,{\beta }^{{s}_{k}},{b}_{{r}_{1}},\ldots ,{b}_{{r}_{l}}}\right)  = {\delta }_{{i}_{1}}^{{s}_{1}}\cdots {\delta }_{{i}_{k}}^{{s}_{k}}{\delta }_{{r}_{1}}^{{j}_{1}}\cdots {\delta }_{{r}_{l}}^{{j}_{l}}.
\]

It follows that \( {T}^{\left( k, l\right) }\left( V\right) \) has dimension \( {n}^{k + l} \) , where \( n = \dim V \) . Every tensor \( F \in \; {T}^{\left( k, l\right) }\left( V\right) \) can be written in terms of this basis (using the summation convention) as

\[
F = {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{b}_{{i}_{1}} \otimes  \cdots  \otimes  {b}_{{i}_{k}} \otimes  {\beta }^{{j}_{1}} \otimes  \cdots  \otimes  {\beta }^{{j}_{l}}, \tag{B.5}
\]

where

\[
{F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}} = F\left( {{\beta }^{{i}_{1}},\ldots ,{\beta }^{{i}_{k}},{b}_{{j}_{1}},\ldots ,{b}_{{j}_{l}}}\right) .
\]

If the arguments of a mixed tensor \( F \) occur in a nonstandard order, then the horizontal as well as vertical positions of the indices are significant and reflect which arguments are vectors and which are covectors. For example, if \( A \) is a \( \left( {1,2}\right) \) -tensor whose first argument is a vector, second is a covector, and third is a vector, its basis expression would be written

\[
A = {A}_{i}^{j}{}_{k}{\beta }^{i} \otimes  {b}_{j} \otimes  {\beta }^{k},
\]

where

\[
{A}_{i}^{j}{}^{j}{}_{k} = A\left( {{b}_{i},{\beta }^{j},{b}_{k}}\right) . \tag{B.6}
\]

There are obvious identifications among some of these tensor spaces:

\[
{T}^{\left( 0,0\right) }\left( V\right)  = {T}^{0}\left( V\right)  = {T}^{0}\left( {V}^{ * }\right)  = \mathbb{R}
\]

\[
{T}^{\left( 1,0\right) }\left( V\right)  = {T}^{1}\left( V\right)  = V
\]

\[
{T}^{\left( 0,1\right) }\left( V\right)  = {T}^{1}\left( {V}^{ * }\right)  = {V}^{ * }, \tag{B.7}
\]

\[
{T}^{\left( k,0\right) }\left( V\right)  = {T}^{k}\left( V\right)
\]

\[
{T}^{\left( 0, k\right) }\left( V\right)  = {T}^{k}\left( {V}^{ * }\right) .
\]

A less obvious, but extremely important, identification is the following:

\[
{T}^{\left( 1,1\right) }\left( V\right)  \cong  \operatorname{End}\left( V\right)
\]

where \( \operatorname{End}\left( V\right) \) denotes the space of linear maps from \( V \) to itself (also called the endomorphisms of \( V \) ). This is a special case of the following proposition.

Proposition B.1. Let \( V \) be a finite-dimensional vector space. There is a natural (basis-independent) isomorphism between \( {T}^{\left( k + 1, l\right) }\left( V\right) \) and the space of multilinear maps

\[
\underset{k\text{ copies }}{\underbrace{{V}^{ * } \times  \cdots  \times  {V}^{ * }}} \times  \underset{l\text{ copies }}{\underbrace{V \times  \cdots  \times  V}} \rightarrow  V.
\]

---

Exercise B.2. Prove Proposition B.1. [Hint: In the special case \( k = 0, l = 1 \) , consider the map \( \Phi  : \operatorname{End}\left( V\right)  \rightarrow  {T}^{\left( 1,1\right) }\left( V\right) \) defined by letting \( {\Phi A} \) be the \( \left( {1,1}\right) \) -tensor defined by \( {\Phi A}\left( {\omega , v}\right)  = \omega \left( {Av}\right) \) . The general case is similar.]

---

We can use the result of Proposition B. 1 to define a natural operation called trace or contraction, which lowers the rank of a tensor by 2 . In one special case, it is easy to describe: the operator \( \operatorname{tr} : {T}^{\left( 1,1\right) }\left( V\right)  \rightarrow  \mathbb{R} \) is just the trace of \( F \) when it is regarded as an endomorphism of \( V \) , or in other words the sum of the diagonal entries of any matrix representation of \( F \) . Since the trace of a linear endomorphism is basis-independent, this is well defined. More generally, we define tr: \( {T}^{\left( k + 1, l + 1\right) }\left( V\right)  \rightarrow  {T}^{\left( k, l\right) }\left( V\right) \) by letting \( \left( {\operatorname{tr}F}\right) \left( {{\omega }^{1},\ldots ,{\omega }^{k},{v}_{1},\ldots ,{v}_{l}}\right) \) be the trace of the \( \left( {1,1}\right) \) -tensor

\[
F\left( {{\omega }^{1},\ldots ,{\omega }^{k},\cdot ,{v}_{1},\ldots ,{v}_{l}, \cdot  }\right)  \in  {T}^{\left( 1,1\right) }\left( V\right) .
\]

In terms of a basis, the components of tr \( F \) are

\[
{\left( \operatorname{tr}F\right) }_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}} = {F}_{{j}_{1}\ldots {j}_{l}m}^{{i}_{1}\ldots {i}_{k}m}.
\]

In other words, just set the last upper and lower indices equal and sum. Even more generally, we can contract a given tensor on any pair of indices as long as one is contravariant and one is covariant. There is no general notation for this operation, so we just describe it in words each time it arises. For example, we can contract the tensor \( A \) with components given by (B.6) on its first and second indices to obtain a covariant 1-tensor \( B \) whose components are \( {B}_{k} = {A}_{i}{}^{i}{}_{k} \) .

Exercise B.3. Show that the trace on any pair of indices (one upper and one lower) is a well-defined linear map from \( {T}^{\left( k + 1, l + 1\right) }\left( V\right) \) to \( {T}^{\left( k, l\right) }\left( V\right) \) .

## Symmetric Tensors

There are two classes of tensors that play particularly important roles in differential geometry: the symmetric and alternating tensors. Here we discuss the symmetric ones; we will take up alternating tensors later in this appendix when we discuss differential forms.

If \( V \) is a finite-dimensional vector space, a covariant tensor \( F \in  {T}^{k}\left( {V}^{ * }\right) \) is said to be symmetric if its value is unchanged by interchanging any pair of arguments:

\[
F\left( {{v}_{1},\ldots ,{v}_{i},\ldots ,{v}_{j},\ldots ,{v}_{k}}\right)  = F\left( {{v}_{1},\ldots ,{v}_{j},\ldots ,{v}_{i},\ldots ,{v}_{k}}\right)
\]

whenever \( 1 \leq  i < j \leq  k \) . It follows immediately that the value is unchanged under every rearrangement of the arguments. If we denote the components of \( F \) with respect to a basis by \( {F}_{{i}_{1}\ldots {i}_{k}} \) , then \( F \) is symmetric if and only if its components are unchanged by every permutation of the indices \( {i}_{1},\ldots ,{i}_{k} \) . Every 0-tensor and every 1-tensor are vacuously symmetric. The set of symmetric \( k \) -tensors on \( V \) is a linear subspace of \( {T}^{k}\left( {V}^{ * }\right) \) , which we denote by \( {\sum }^{k}\left( {V}^{ * }\right) \) .

A tensor product of symmetric tensors is generally not symmetric. However, there is a natural product of symmetric tensors that does yield symmetric tensors. Given a covariant \( k \) -tensor \( F \) , the symmetrization of \( F \) is the \( k \) -tensor \( \operatorname{Sym}F \) defined by

\[
\left( {\operatorname{Sym}F}\right) \left( {{v}_{1},\ldots ,{v}_{k}}\right)  = \frac{1}{k!}\mathop{\sum }\limits_{{\sigma  \in  {S}_{k}}}F\left( {{v}_{\sigma \left( 1\right) },\ldots ,{v}_{\sigma \left( k\right) }}\right) ,
\]

where \( {S}_{k} \) is the group of all permutations of \( \{ 1,\ldots , k\} \) , called the symmetric group on \( k \) elements. It is easy to check that \( \operatorname{Sym}F \) is symmetric, and \( \operatorname{Sym}F = F \) if and only if \( F \) is symmetric. Then if \( F \) and \( G \) are symmetric tensors on \( V \) , of ranks \( k \) and \( l \) , respectively, their symmetric product is defined to be the \( \left( {k + l}\right) \) -tensor \( {FG} \) (denoted by juxtaposition without an explicit product symbol) given by

\[
{FG} = \operatorname{Sym}\left( {F \otimes  G}\right) .
\]

The most important special case is the symmetric product of two 1-tensors, which can be characterized as follows: if \( \omega \) and \( \eta \) are covectors, then

\[
{\omega \eta } = \frac{1}{2}\left( {\omega  \otimes  \eta  + \eta  \otimes  \omega }\right) .
\]

(To prove this, just evaluate both sides on an arbitrary pair of vectors \( \left( {v, w}\right) \) , and use the definition of \( {\omega \eta } \) .) If \( \omega \) is any 1 -tensor, the notation \( {\omega }^{2} \) means the symmetric product \( {\omega \omega } \) , which in turn is equal to \( \omega  \otimes  \omega \) .

## Tensor Bundles and Tensor Fields

On a smooth manifold \( M \) with or without boundary, we can perform the same linear-algebraic constructions on each tangent space \( {T}_{p}M \) that we perform on any vector space, yielding tensors at \( p \) . The disjoint union of tensor spaces of a particular type at all points of the manifold yields a vector bundle, called a tensor bundle.

The most fundamental tensor bundle is the cotangent bundle, defined as

\[
{T}^{ * }M = \mathop{\coprod }\limits_{{p \in  M}}{T}_{p}^{ * }M
\]

More generally, the bundle of \( \left( {k, l}\right) \) -tensors on \( M \) is defined as

\[
{T}^{\left( k, l\right) }{TM} = \mathop{\coprod }\limits_{{p \in  M}}{T}^{\left( k, l\right) }\left( {{T}_{p}M}\right) .
\]

As special cases, the bundle of covariant \( k \) -tensors is denoted by \( {T}^{k}{T}^{ * }M = \; {T}^{\left( 0, k\right) }{TM} \) , and the bundle of contravariant \( k \) -tensors is denoted by \( {T}^{k}{TM} = \; {T}^{\left( k,0\right) }{TM} \) . Similarly, the bundle of symmetric \( k \) -tensors is

\[
{\sum }^{k}{T}^{ * }M = \mathop{\coprod }\limits_{{p \in  M}}{\sum }^{k}\left( {{T}_{p}^{ * }M}\right) .
\]

There are the usual identifications among these bundles that follow from (B.7): for example, \( {T}^{1}{TM} = {T}^{\left( 1,0\right) }{TM} = {TM} \) and \( {T}^{1}{T}^{ * }M = {T}^{\left( 0,1\right) }{TM} = {\sum }^{1}{T}^{ * }M = \; {T}^{ * }M \) .

Exercise B.4. Show that each tensor bundle is a smooth vector bundle over \( M \) , with a local trivialization over every open subset that admits a smooth local frame for \( {TM} \) .

A tensor field on \( M \) is a section of some tensor bundle over \( M \) (see p. 383 for the definition of a section of a bundle). A section of \( {T}^{1}{T}^{ * }M = {T}^{\left( 0,1\right) }{TM} \) (a covariant 1-tensor field) is also called a covector field. As we do with vector fields, we write the value of a tensor field \( F \) at \( p \in  M \) as \( {F}_{p} \) or \( {\left. F\right| }_{p} \) . Because covariant tensor fields are the most common and important tensor fields we work with, we use the following shorthand notation for the space of all smooth covariant \( k \) -tensor fields:

\[
{\mathcal{T}}^{k}\left( M\right)  = \Gamma \left( {{T}^{k}{T}^{ * }M}\right)
\]

The space of smooth 0-tensor fields is just \( {C}^{\infty }\left( M\right) \) .

Let \( \left( {E}_{i}\right)  = \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) be any smooth local frame for \( {TM} \) over an open subset \( U \subseteq  M \) . Associated with such a frame is the dual coframe, which we typically denote by \( \left( {{\varepsilon }^{1},\ldots ,{\varepsilon }^{n}}\right) \) ; these are smooth covector fields satisfying \( {\varepsilon }^{i}\left( {E}_{j}\right)  = \; {\delta }_{j}^{i} \) . For example, given a coordinate frame \( \left( {\partial /\partial {x}^{1},\ldots ,\partial /\partial {x}^{n}}\right) \) over some open subset \( U \subseteq  M \) , the dual coframe is \( \left( {d{x}^{1},\ldots , d{x}^{n}}\right) \) , where \( d{x}^{i} \) is the differential of the coordinate function \( {x}^{i} \) .

In terms of any smooth local frame \( \left( {E}_{i}\right) \) and its dual coframe \( \left( {\varepsilon }^{i}\right) \) , the tensor fields \( {E}_{{i}_{1}} \otimes  \cdots  \otimes  {E}_{{i}_{k}} \otimes  {\varepsilon }^{{j}_{1}} \otimes  \cdots  \otimes  {\varepsilon }^{{j}_{l}} \) form a smooth local frame for \( {T}^{\left( k, l\right) }\left( {{T}^{ * }M}\right) \) . In particular, in local coordinates \( \left( {x}^{i}\right) \) , a \( \left( {k, l}\right) \) -tensor field \( F \) has a coordinate expression of the form

\[
F = {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{\partial }_{{i}_{1}} \otimes  \cdots  \otimes  {\partial }_{{i}_{k}} \otimes  d{x}^{{j}_{1}} \otimes  \cdots  \otimes  d{x}^{{j}_{l}}, \tag{B.8}
\]

where each coefficient \( {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}} \) is a smooth real-valued function on \( U \) .

Exercise B.5. Suppose \( F : M \rightarrow  {T}^{\left( k, l\right) }{TM} \) is a rough \( \left( {k, l}\right) \) -tensor field. Show that \( F \) is smooth on an open set \( U \subseteq  M \) if and only if whenever \( {\omega }^{1},\ldots ,{\omega }^{k} \) are smooth covec-tor fields and \( {\mathbf{X}}_{1},\ldots ,{\mathbf{X}}_{l} \) are smooth vector fields defined on \( \mathbf{U} \) , the real-valued function \( F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{X}_{1},\ldots ,{X}_{l}}\right) \) , defined on \( U \) by

\[
F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{X}_{1},\ldots ,{X}_{l}}\right) \left( p\right)  = {F}_{p}\left( {{\left. {\omega }^{1}\right| }_{p},\ldots ,{\left. {\omega }^{k}\right| }_{p},{\left. {X}_{1}\right| }_{p},\ldots ,{\left. {X}_{l}\right| }_{p}}\right) ,
\]

is smooth.

An important property of tensor fields is that they are multilinear over the space of smooth functions. Suppose \( F \in  \Gamma \left( {{T}^{\left( k, l\right) }{TM}}\right) \) is a smooth tensor field. Given smooth covector fields \( {\omega }^{1},\ldots ,{\omega }^{k} \in  {\mathcal{T}}^{1}\left( M\right) \) and smooth vector fields \( {X}_{1},\ldots ,{X}_{l} \in \; \mathcal{X}\left( M\right) \) , Exercise B. 5 shows that the function \( F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{X}_{1},\ldots ,{X}_{l}}\right) \) is smooth, and thus \( F \) induces a map

\[
\widetilde{F} : \underset{k\text{ factors }}{\underbrace{{\mathcal{T}}^{1}\left( M\right)  \times  \cdots  \times  {\mathcal{T}}^{1}\left( M\right) }} \times  \underset{l\text{ factors }}{\underbrace{\mathfrak{X}\left( M\right)  \times  \cdots  \times  \mathfrak{X}\left( M\right) }} \rightarrow  {C}^{\infty }\left( M\right) .
\]

It is easy to check that this map is multilinear over \( {C}^{\infty }\left( M\right) \) , that is, for all functions \( u, v \in  {C}^{\infty }\left( M\right) \) and smooth vector or covector fields \( \alpha ,\beta \) ,

\[
\widetilde{F}\left( {\ldots ,{u\alpha } + {v\beta },\ldots }\right)  = u\widetilde{F}\left( {\ldots ,\alpha ,\ldots }\right)  + v\widetilde{F}\left( {\ldots ,\beta ,\ldots }\right) .
\]

Even more important is the converse: as the next lemma shows, every such map that is multilinear over \( {C}^{\infty }\left( M\right) \) defines a tensor field. (This lemma is stated and proved in [LeeSM] for covariant tensor fields, but the same argument works in the case of mixed tensors.)

Lemma B.6 (Tensor Characterization Lemma). [LeeSM, Lemma 12.24] A map

\[
\mathcal{F} : \underset{k\text{ factors }}{\underbrace{{\mathcal{T}}^{1}\left( M\right)  \times  \cdots  \times  {\mathcal{T}}^{1}\left( M\right) }} \times  \underset{l\text{ factors }}{\underbrace{\mathfrak{X}\left( M\right)  \times  \cdots  \times  \mathfrak{X}\left( M\right) }} \rightarrow  {C}^{\infty }\left( M\right)
\]

is induced by a smooth \( \left( {k, l}\right) \) -tensor field as above if and only if it is multilinear over \( {C}^{\infty }\left( M\right) \) . Similarly, a map

\[
\mathcal{F} : \underset{k\text{ factors }}{\underbrace{{\mathcal{T}}^{1}\left( M\right)  \times  \cdots  \times  {\mathcal{T}}^{1}\left( M\right) }} \times  \underset{l\text{ factors }}{\underbrace{\mathfrak{X}\left( M\right)  \times  \cdots  \times  \mathfrak{X}\left( M\right) }} \rightarrow  \mathfrak{X}\left( M\right)
\]

is induced by a smooth \( \left( {k + 1, l}\right) \) -tensor field as in Proposition B. 1 if and only if it is multilinear over \( {C}^{\infty }\left( M\right) \) .

Because of this result, it is common to use the same symbol for both a tensor field and the multilinear map on sections that it defines, and to refer to either of these objects as a tensor field.

## Pullbacks of Tensor Fields

Suppose \( F : M \rightarrow  N \) is a smooth map and \( A \) is a covariant \( k \) -tensor field on \( N \) . For every \( p \in  M \) , we define a tensor \( d{F}_{p}^{ * }\left( A\right)  \in  {T}^{k}\left( {{T}_{p}^{ * }M}\right) \) , called the pointwise pullback of \( \mathbf{A} \) by \( \mathbf{F} \) at \( \mathbf{p} \) , by

\[
d{F}_{p}^{ * }\left( A\right) \left( {{v}_{1},\ldots ,{v}_{k}}\right)  = A\left( {d{F}_{p}\left( {v}_{1}\right) ,\ldots , d{F}_{p}\left( {v}_{k}\right) }\right)
\]

for \( {v}_{1},\ldots ,{v}_{k} \in  {T}_{p}M \) ; and we define the pullback of \( A \) by \( F \) to be the tensor field \( {F}^{ * }A \) on \( M \) defined by

\[
{\left( {F}^{ * }A\right) }_{p} = d{F}_{p}^{ * }\left( {A}_{F\left( p\right) }\right) .
\]

Proposition B.7 (Properties of Tensor Pullbacks). [LeeSM, Prop. 12.25] Suppose \( F : M \rightarrow  N \) and \( G : P \rightarrow  M \) are smooth maps, \( A \) and \( B \) are covariant tensor fields on \( N \) , and \( f \) is a real-valued function on \( N \) .

(a) \( {F}^{ * }\left( {fB}\right)  = \left( {f \circ  F}\right) {F}^{ * }B \) .

(b) \( {F}^{ * }\left( {A \otimes  B}\right)  = {F}^{ * }A \otimes  {F}^{ * }B \) .

(c) \( {F}^{ * }\left( {A + B}\right)  = {F}^{ * }A + {F}^{ * }B \) .

(d) \( {F}^{ * }B \) is a (continuous) tensor field, and it is smooth if \( B \) is smooth.

(e) \( {\left( F \circ  G\right) }^{ * }B = {G}^{ * }\left( {{F}^{ * }B}\right) \) .

(f) \( {\left( {\operatorname{Id}}_{N}\right) }^{ * }B = B \) .

If \( f \) is a continuous real-valued function (i.e., a 0 -tensor field), the pullback \( {F}^{ * }f \) is just the composition \( f \circ  F \) .

The following proposition shows how pullbacks are computed in local coordinates.

Proposition B.8. [LeeSM, Cor. 12.28] Let \( F : M \rightarrow  N \) be smooth, and let \( B \) be a covariant \( k \) -tensor field on \( N \) . If \( p \in  M \) and \( \left( {y}^{i}\right) \) are smooth coordinates for \( N \) on a neighborhood of \( F\left( p\right) \) , then \( {F}^{ * }B \) has the following expression in a neighborhood of \( p \) :

\[
{F}^{ * }\left( {{B}_{{i}_{1}\ldots {i}_{k}}d{y}^{{i}_{1}} \otimes  \cdots  \otimes  d{y}^{{i}_{k}}}\right)  = \left( {{B}_{{i}_{1}\ldots {i}_{k}} \circ  F}\right) d\left( {{y}^{{i}_{1}} \circ  F}\right)  \otimes  \cdots  \otimes  d\left( {{y}^{{i}_{k}} \circ  F}\right) .
\]

## Lie Derivatives of Tensor Fields

We can extend the notion of Lie derivatives to tensor fields. This can be done for mixed tensor fields of any rank, but for simplicity we restrict attention to covariant tensor fields. Suppose \( X \) is a smooth vector field on \( M \) and \( \theta \) is its flow. If \( A \) is a smooth covariant tensor field on \( M \) , the Lie derivative of \( A \) with respect to \( X \) is the smooth covariant tensor field \( {\mathcal{L}}_{X}A \) defined by

\[
{\left( {\mathcal{L}}_{X}A\right) }_{p} = {\left. \frac{d}{dt}\right| }_{t = 0}{\left( {\theta }_{t}^{ * }A\right) }_{p} = \mathop{\lim }\limits_{{t \rightarrow  0}}\frac{d{\left( {\theta }_{t}\right) }_{p}^{ * }\left( {A}_{{\theta }_{t}\left( p\right) }\right)  - {A}_{p}}{t}.
\]

Proposition B.9. [LeeSM, Thm. 12.32] Suppose \( M \) is a smooth manifold, \( X \in \; \mathfrak{X}\left( M\right) \) , and \( A \) is a smooth covariant \( k \) -tensor field on \( M \) . For all smooth vector fields \( {Z}_{1},\ldots ,{Z}_{k} \) ,

\[
\left( {{\mathcal{L}}_{X}A}\right) \left( {{Z}_{1},\ldots ,{Z}_{k}}\right)  = X\left( {A\left( {{Z}_{1},\ldots ,{Z}_{k}}\right) }\right)
\]

\[
- A\left( {{\mathcal{L}}_{X}{Z}_{1},{Z}_{2},\ldots ,{Z}_{k}}\right)  - A\left( {{Z}_{1},{\mathcal{L}}_{X}{Z}_{2},\ldots ,{Z}_{k}}\right)  - \cdots  - A\left( {{Z}_{1},\ldots ,{\mathcal{L}}_{X}{Z}_{k}}\right) .
\]

As we did for vector fields, we say that a covariant tensor field \( A \) is invariant under a flow \( \mathbf{\theta } \) if \( {\left( {\theta }_{t}\right) }^{ * }A = A \) wherever it is defined. The next proposition is a tensor analogue of Proposition A.47.

Proposition B.10. [LeeSM, Thm. 12.37] Let \( M \) be a smooth manifold and \( X \in \; \mathcal{X}\left( M\right) \) . A smooth covariant tensor field is invariant under the flow of \( X \) if and only if its Lie derivative with respect to \( X \) is identically zero.

## Differential Forms and Integration

In addition to symmetric tensors, the other class of tensors that play a special role in differential geometry is that of alternating tensors, which we now define. Let \( V \) be a finite-dimensional vector space. If \( F \) is a covariant \( k \) -tensor on \( V \) , we say that \( F \) is alternating if its value changes sign whenever two different arguments are interchanged:

\[
F\left( {{v}_{1},\ldots ,{v}_{i},\ldots ,{v}_{j},\ldots ,{v}_{k}}\right)  =  - F\left( {{v}_{1},\ldots ,{v}_{j},\ldots ,{v}_{i},\ldots ,{v}_{k}}\right) .
\]

The set of alternating covariant \( k \) -tensors on \( V \) is a linear subspace of \( {T}^{k}\left( {V}^{ * }\right) \) , denoted by \( {\Lambda }^{k}\left( {V}^{ * }\right) \) . If \( F \in  {\Lambda }^{k}\left( {V}^{ * }\right) \) , then the effect of an arbitrary permutation of its arguments is given by

\[
F\left( {{v}_{\sigma \left( 1\right) },\ldots ,{v}_{\sigma \left( k\right) }}\right)  = \left( {\operatorname{sgn}\sigma }\right) F\left( {{v}_{1},\ldots ,{v}_{k}}\right) ,
\]

where \( \operatorname{sgn}\sigma \) represents the \( \operatorname{sign} \) of the permutation \( \sigma  \in  {S}_{k} \) , which is +1 if \( \sigma \) is even (i.e., can be written as a composition of an even number of transpositions), and -1 if \( \sigma \) is odd. The components of \( F \) with respect to any basis change sign similarly under a permutation of the indices. All 0-tensors and 1-tensors are alternating.

Analogously to the symmetrization operator defined above, if \( F \) is any covariant \( k \) -tensor on \( V \) , we define the alternation of \( F \) by

\[
\left( {\operatorname{Alt}F}\right) \left( {{v}_{1},\ldots ,{v}_{k}}\right)  = \frac{1}{k!}\mathop{\sum }\limits_{{\sigma  \in  {S}_{k}}}\left( {\operatorname{sgn}\sigma }\right) F\left( {{v}_{\sigma \left( 1\right) },\ldots ,{v}_{\sigma \left( k\right) }}\right) . \tag{B.9}
\]

Again, it is easy to check that Alt \( F \) is alternating, and Alt \( F = F \) if and only if \( F \) is alternating. Given \( \omega  \in  {\Lambda }^{k}\left( {V}^{ * }\right) \) and \( \eta  \in  {\Lambda }^{l}\left( {V}^{ * }\right) \) , we define their wedge product by

\[
\omega  \land  \eta  = \frac{\left( {k + l}\right) !}{k!l!}\operatorname{Alt}\left( {\omega  \otimes  \eta }\right) .
\]

It is immediate that \( \omega  \land  \eta \) is an alternating \( \left( {k + l}\right) \) -tensor. The wedge product is easily seen to be bilinear and anticommutative, which means that

\[
\omega  \land  \eta  = {\left( -1\right) }^{kl}\eta  \land  \omega ,\;\text{ for }\omega  \in  {\Lambda }^{k}\left( {V}^{ * }\right) \text{ and }\eta  \in  {\Lambda }^{l}\left( {V}^{ * }\right) .
\]

It is also the case, although not so easy to see, that it is associative; see [LeeSM, Prop. 14.11] for a proof. If \( \left( {b}_{i}\right) \) is a basis for \( V \) and \( \left( {\beta }^{i}\right) \) is the dual basis, the wedge products \( {\beta }^{{i}_{1}} \land  \cdots  \land  {\beta }^{{i}_{k}} \) , as \( \left( {{i}_{1},\ldots ,{i}_{k}}\right) \) range over strictly increasing multi-indices, form a basis for \( {\Lambda }^{k}\left( {V}^{ * }\right) \) , which therefore has dimension \( \left( \begin{array}{l} n \\  k \end{array}\right)  = n!/\left( {k!\left( {n - k}\right) !}\right) \) , where \( n = \dim V \) . In terms of these basis elements, the wedge product satisfies

\[
{\beta }^{{i}_{1}} \land  \cdots  \land  {\beta }^{{i}_{k}}\left( {{b}_{{j}_{1}},\ldots ,{b}_{{j}_{k}}}\right)  = \det \left( {\delta }_{{j}_{q}}^{{i}_{p}}\right) .
\]

More generally, if \( {\omega }^{1},\ldots ,{\omega }^{k} \) are any covectors and \( {v}_{1},\ldots ,{v}_{k} \) are any vectors, then

\[
{\omega }^{1} \land  \cdots  \land  {\omega }^{k}\left( {{v}_{1},\ldots ,{v}_{k}}\right)  = \det \left( {{\omega }^{i}\left( {v}_{j}\right) }\right) . \tag{B.10}
\]

The wedge product can be defined analogously for contravariant alternating tensors \( \alpha  \in  {\Lambda }^{p}\left( V\right) ,\beta  \in  {\Lambda }^{q}\left( V\right) \) , simply by regarding \( \alpha ,\beta \) , and \( \alpha  \land  \beta \) as alternating multilinear functionals on \( {V}^{ * } \) .

The convention we use for the wedge product is referred to in [LeeSM] as the determinant convention. There is another convention that is also in common use, the Alt convention, which amounts to multiplying the right-hand side of (B.10) by a factor of \( 1/k \) !. The choice of which definition to use is a matter of taste, though there are various reasons to justify each choice depending on the context. The determinant convention is most common in introductory differential geometry texts, and is used, for example, in [Boo86, Cha06, dC92, LeeJeff09, LeeSM, Pet16, Spi79, Tu11]. The Alt convention is used in [KN96] and is more common in complex differential geometry.

Given an alternating \( k \) -tensor \( \omega  \in  {\Lambda }^{k}\left( {V}^{ * }\right) \) and a vector \( v \in  V \) , we define an alternating \( \left( {k - 1}\right) \) -tensor \( v\lrcorner \omega \) by

\[
\left( {v\lrcorner \omega }\right) \left( {{w}_{1},\ldots ,{w}_{k - 1}}\right)  = \omega \left( {v,{w}_{1},\ldots ,{w}_{k - 1}}\right) .
\]

The operation \( \omega  \mapsto  v \bot  \omega \) is known as interior multiplication by \( v \) , and is also denoted by \( \omega  \mapsto  {i}_{v}\omega \) . By convention, \( v \bot  \omega  = 0 \) when \( \omega \) is a 0 -tensor. Direct computation shows that \( {i}_{v} \circ  {i}_{v} = 0 \) , and \( {i}_{v} \) satisfies the following product rule for an alternating \( k \) -tensor \( \omega \) and an alternating \( l \) -tensor \( \eta \) :

\[
{i}_{v}\left( {\omega  \land  \eta }\right)  = \left( {{i}_{v}\omega }\right)  \land  \eta  + {\left( -1\right) }^{k}\omega  \land  \left( {{i}_{v}\eta }\right) . \tag{B.11}
\]

If \( M \) is a smooth manifold with or without boundary, the subbundle of \( {T}^{k}{T}^{ * }M \) consisting of alternating tensors is denoted by \( {\Lambda }^{k}{T}^{ * }M \) , and an alternating tensor field on \( M \) is called a differential \( k \) -form, or just a \( k \) -form. The space of all smooth \( k \) -forms is denoted by \( {\Omega }^{k}\left( M\right)  = \Gamma \left( {{\Lambda }^{k}{T}^{ * }M}\right) \) . Because every 1-tensor field is alternating, \( {\Omega }^{1}\left( M\right) \) is the same as the space \( {\mathcal{T}}^{1}\left( M\right) \) of smooth covector fields.

## Exterior Derivatives

The most important operation on differential forms is the exterior derivative, defined as follows. Suppose \( M \) is a smooth \( n \) -manifold with or without boundary, and \( \left( {x}^{i}\right) \) are any smooth local coordinates on \( M \) . A smooth \( k \) -form \( \omega \) can be expressed in these coordinates as

\[
\omega  = \mathop{\sum }\limits_{{{j}_{1} < \cdots  < {j}_{k}}}{\omega }_{{j}_{1}\ldots {j}_{k}}d{x}^{{j}_{1}} \land  \cdots  \land  d{x}^{{j}_{k}},
\]

and then we define the exterior derivative of \( \omega \) , denoted by \( {d\omega } \) , to be the \( \left( {k + 1}\right) \) - form defined in coordinates by

\[
{d\omega } = \mathop{\sum }\limits_{{{j}_{1} < \cdots  < {j}_{k}}}\mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial {\omega }_{{j}_{1}\ldots {j}_{k}}}{\partial {x}^{i}}d{x}^{i} \land  d{x}^{{j}_{1}} \land  \cdots  \land  d{x}^{{j}_{k}}.
\]

For a 0 -form \( f \) (a smooth real-valued function), this reduces to

\[
{df} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}^{i}}d{x}^{i}
\]

which is exactly the differential of \( f \) defined by (A.4).

Proposition B.11 (Properties of Exterior Differentiation). [LeeSM, Thm. 14.24] Suppose \( M \) is a smooth \( n \) -manifold with or without boundary.

(a) For each \( k = 0,\ldots , n \) , the operator \( d : {\Omega }^{k}\left( M\right)  \rightarrow  {\Omega }^{k + 1}\left( M\right) \) is well defined, independently of coordinates.

(b) \( d \) is linear over \( \mathbb{R} \) .

(c) \( d \circ  d \equiv  0 \) .

(d) If \( \omega  \in  {\Omega }^{k}\left( M\right) \) and \( \eta  \in  {\Omega }^{l}\left( M\right) \) , then

\[
d\left( {\omega  \land  \eta }\right)  = {d\omega } \land  \eta  + {\left( -1\right) }^{k}\omega  \land  {d\eta }.
\]

Proposition B. 12 (Exterior Derivative of a 1-form). [LeeSM, Prop. 14.29] If \( \omega \) is a smooth 1-form and \( X, Y \) are vector fields, then

\[
{d\omega }\left( {X, Y}\right)  = X\left( {\omega \left( Y\right) }\right)  - Y\left( {\omega \left( X\right) }\right)  - \omega \left( \left\lbrack  {X, Y}\right\rbrack  \right) .
\]

Proposition B.13 (Naturality of the Exterior Derivative). [LeeSM, Prop. 14.26] If \( F : M \rightarrow  N \) is a smooth map, then for each \( k \) , the pullback map \( {F}^{ * } : {\Omega }^{k}\left( N\right)  \rightarrow \; {\Omega }^{k}\left( M\right) \) commutes with \( d \) : for all \( \omega  \in  {\Omega }^{k}\left( N\right) \) ,

\[
{F}^{ * }\left( {d\omega }\right)  = d\left( {{F}^{ * }\omega }\right) . \tag{B.12}
\]

A smooth differential form \( \omega  \in  {\Omega }^{k}\left( M\right) \) is closed if \( {d\omega } = 0 \) , and exact if there exists a smooth \( \left( {k - 1}\right) \) -form \( \eta \) on \( M \) such that \( \omega  = {d\eta } \) . The fact that \( d \circ  d = \) 0 implies that every exact form is closed, but the converse is not true in general. However, the next lemma gives an important special case in which it is true. If \( V \) is a vector space, a subset \( S \subseteq  V \) is said to be star-shaped with respect to a point \( x \in  S \) if for every \( y \in  S \) , the line segment from \( x \) to \( y \) is contained in \( S \) .

Lemma B.14 (The Poincaré Lemma). [LeeSM, Thm. 17.14] If \( U \) is a star-shaped open subset of \( {\mathbb{R}}^{n} \) , then for \( k \geq  1 \) , every closed \( k \) -form on \( U \) is exact.

## Orientations

If \( V \) is a finite-dimensional vector space, an orientation of \( V \) is an equivalence class of ordered bases for \( V \) , where two ordered bases are considered equivalent if the transition matrix that expresses one basis in terms of the other has positive determinant. Every vector space has exactly two orientations. Once an orientation is chosen, a basis is said to be positively oriented if it belongs to the chosen orientation, and negatively oriented if not. The standard orientation of \( {\mathbb{R}}^{n} \) is the one determined by the standard basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) , where \( {e}_{i} \) is the vector \( \left( {0,\ldots ,1,\ldots ,0}\right) \) with 1 in the \( i \) th place and zeros elsewhere.

If \( M \) is a smooth manifold, an orientation for \( M \) is a choice of orientation for each tangent space that is continuous in the sense that in a neighborhood of every point there is a (continuous) local frame that determines the given orientation at each point of the neighborhood. If there exists an orientation for \( M \) , we say that \( M \) is orientable. An oriented manifold is a smooth orientable manifold together with a choice of orientation. If \( M \) is an oriented \( n \) -manifold, then a smooth coordinate chart \( \left( {U,\left( {x}^{i}\right) }\right) \) is said to be an oriented chart if the coordinate frame \( \left( {\partial /\partial {x}^{1},\ldots ,\partial /\partial {x}^{n}}\right) \) is positively oriented at each point. Exactly the same definitions apply to manifolds with boundary.

Proposition B. 15 (Orientation Determined by an \( n \) -Form). [LeeSM, Prop. 15.5] Let \( M \) be an \( n \) -manifold with or without boundary. Every nonvanishing \( n \) -form \( \mu  \in  {\Omega }^{n}\left( M\right) \) determines a unique orientation of \( M \) by declaring an ordered basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( {T}_{p}M \) to be positively oriented if and only if \( {\mu }_{p}\left( {{b}_{1},\ldots ,{b}_{n}}\right)  > 0 \) . Conversely, if \( M \) is oriented, there is a smooth nonvanishing \( n \) -form that determines the orientation in this way.

Because of this proposition, a nonvanishing \( n \) -form on a smooth \( n \) -manifold is called an orientation form. If in addition \( M \) is oriented and \( \mu \) determines the given orientation, we say that \( \mu \) is positively oriented.

Suppose \( M \) and \( N \) are both smooth \( n \) -manifolds with or without boundary and \( F : M \rightarrow  N \) is a local diffeomorphism. If \( N \) is oriented, we define the pullback orientation on \( M \) induced by \( \mathbf{F} \) to be the orientation determined by \( {F}^{ * }\mu \) , where \( \mu \) is any positively oriented orientation form for \( N \) . If both \( M \) and \( N \) are oriented, we say that \( F \) is orientation-preserving if the pullback orientation is equal to the given orientation on \( M \) , and orientation-reversing if the pullback orientation is the opposite orientation.

Proposition B.16 (Orientation of a Hypersurface). [LeeSM, Prop. 15.21] Suppose \( M \) is an oriented smooth \( n \) -manifold with or without boundary, \( S \subseteq  M \) is a smooth immersed hypersurface, and \( N \) is a continuous vector field along \( S \) (i.e., a continuous map \( N : S \rightarrow  {TM} \) such that \( {N}_{p} \in  {T}_{p}M \) for each \( p \in  S \) ). If \( N \) is nowhere tangent to \( S \) , then \( S \) has a unique orientation determined by the \( \left( {n - 1}\right) \) - form \( {\iota }^{ * }\left( {N\lrcorner \mu }\right) \) , where \( \iota  : S \hookrightarrow  M \) is inclusion and \( \mu \) is any positively oriented orientation form for \( M \) .

A special case of the preceding proposition occurs when \( M \) is a manifold with boundary and the hypersurface in question is the boundary of \( M \) . In that case we declare a vector field \( N \) along \( \partial M \) to be outward-pointing if for each \( p \in  \partial M \) , there is a smooth curve \( \gamma  : ( - \varepsilon ,0\rbrack  \rightarrow  M \) such that \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = {N}_{p} \) , and \( {N}_{p} \notin  {T}_{p}\left( {\partial M}\right) \) . We can always construct a global smooth outward-pointing vector field by taking \( - \partial /\partial {x}^{n} \) in boundary coordinates in a neighborhood of each boundary point, and gluing together with a partition of unity. Since an outward-pointing vector field is nowhere tangent to \( \partial M \) , we have the following proposition.

Proposition B.17 (Induced Orientation on a Boundary). [LeeSM, Prop. 15.24] If \( M \) is an oriented smooth manifold with boundary, then \( \partial M \) is orientable, and it has a canonical orientation (called the induced orientation or Stokes orientation) determined by \( {\iota }^{ * }\left( {N\lrcorner \mu }\right) \) , where \( \iota  : \partial M \hookrightarrow  M \) is inclusion, \( N \) is any outward-pointing vector field along \( \partial M \) , and \( \mu \) is any positively oriented orientation form for \( M \) .

Proposition B.18 (Orientation Covering Theorem). [LeeSM, Thm. 15.41] If \( M \) is a connected, nonorientable smooth manifold, then there exist an oriented smooth manifold \( \widehat{M} \) and a two-sheeted smooth covering map \( \widehat{\pi } : \widehat{M} \rightarrow  M \) , called the orientation covering of \( M \) .

Corollary B.19. Every simply connected smooth manifold is orientable.

Proof. Corollary A. 59 shows that a simply connected manifold does not admit two-sheeted covering maps.

## Integration of Differential Forms

Suppose first that \( \omega \) is a (continuous) \( n \) -form on an open subset \( U \subseteq  {\mathbb{R}}^{n} \) or \( {\mathbb{R}}_{ + }^{n} \) . It can be written \( \omega  = {fd}{x}^{1} \land  \cdots  \land  d{x}^{n} \) for some continuous real-valued function \( f \) , and we define the integral of \( \omega \) over \( \mathbf{U} \) to be the ordinary multiple integral

\[
{\int }_{U}\omega  = {\int }_{U}f\left( {{x}^{1},\ldots ,{x}^{n}}\right) d{x}^{1}\cdots d{x}^{n},
\]

provided the integral is well defined. This will always be the case, for example, if \( f \) is continuous and has compact support in \( U \) .

In general, if \( \omega \) is a compactly supported \( n \) -form on a smooth \( n \) -manifold \( M \) with or without boundary, we define the integral of \( \omega \) over \( M \) by choosing finitely many oriented smooth coordinate charts \( {\left\{  {U}_{i}\right\}  }_{i = 1}^{k} \) whose domains cover the support of \( \omega \) , together with a smooth partition of unity \( {\left\{  {\psi }_{1}\right\}  }_{i = 1}^{k} \) subordinate to this cover, and defining

\[
{\int }_{M}\omega  = \mathop{\sum }\limits_{{i = 1}}^{k}{\int }_{{\widehat{U}}_{i}}{\left( {\varphi }_{i}^{-1}\right) }^{ * }\left( {{\psi }_{i}\omega }\right) ,
\]

where \( {\widehat{U}}_{i} = {\varphi }_{i}\left( {U}_{i}\right) \) , and the integrals on the right-hand side are defined as above. Proposition 16.5 in [LeeSM] shows that this definition does not depend on the choice of oriented charts or partition of unity.

Proposition B.20 (Properties of Integrals of Forms). [LeeSM, Prop. 16.6] Suppose \( M \) and \( N \) are nonempty oriented smooth n-manifolds with or without boundary, and \( \omega ,\eta \) are compactly supported \( n \) -forms on \( M \) .

(a) LINEARITY: If \( a, b \in  \mathbb{R} \) , then

\[
{\int }_{M}{a\omega } + {b\eta } = a{\int }_{M}\omega  + b{\int }_{M}\eta .
\]

(b) ORIENTATION REVERSAL: If \( - M \) denotes \( M \) with the opposite orientation, then

\[
{\int }_{-M}\omega  =  - {\int }_{M}\omega
\]

(c) POSITIVITY: If \( \omega \) is a positively oriented orientation form, then \( {\int }_{M}\omega  > 0 \) .

(d) DIFFEOMORPHISM INVARIANCE: If \( F : N \rightarrow  M \) is an orientation-preserving or orientation-reversing diffeomorphism, then

\[
{\int }_{M}\omega  = \left\{  \begin{matrix} {\int }_{N}{F}^{ * }\omega & \text{ if }F\text{ is orientation-preserving, } \\   - {\int }_{N}{F}^{ * }\omega & \text{ if }F\text{ is orientation-reversing. } \end{matrix}\right.
\]

Theorem B.21 (Stokes's Theorem). [LeeSM, Thm. 16.11] If M is an oriented smooth \( n \) -manifold with boundary and \( \omega \) is a compactly supported smooth \( \left( {n - 1}\right) \) - form on \( M \) , then

\[
{\int }_{M}{d\omega } = {\int }_{\partial M}\omega \tag{B.13}
\]

In the statement of this theorem, \( \partial M \) is understood to have the Stokes orientation, and the right-hand side is interpreted as the integral of the pullback of \( \omega \) to \( \partial M \) .

The following special case is frequently useful.

Corollary B.22. [LeeSM, Cor. 16.13] Suppose \( M \) is a compact oriented smooth n-manifold (without boundary). Then the integral of every exact \( n \) -form on \( M \) is zero.

## Densities

On an oriented \( n \) -manifold with or without boundary, \( n \) -forms are the natural objects to integrate. But in order to integrate on a nonorientable manifold, we need closely related objects called densities.

If \( V \) is an \( n \) -dimensional real vector space, a density on \( V \) is a function

\[
\mu  : \underset{n\text{ copies }}{\underbrace{V \times  \cdots  \times  V}} \rightarrow  \mathbb{R}
\]

satisfying the following formula for every linear map \( T : V \rightarrow  V \) :

\[
\mu \left( {T{v}_{1},\ldots , T{v}_{n}}\right)  = \left| {\det T}\right| \mu \left( {{v}_{1},\ldots ,{v}_{n}}\right) . \tag{B.14}
\]

A density \( \mu \) is said to be positive if \( \mu \left( {{v}_{1},\ldots ,{v}_{n}}\right)  > 0 \) whenever \( \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) is a basis of \( V \) ; it is clear from (B.14) that if this is true for some basis, then it is true for every one. Every nonzero alternating \( n \) -tensor \( \mu \) determines a positive density \( \left| \mu \right| \) by the formula

\[
\left| \mu \right| \left( {{v}_{1},\ldots ,{v}_{n}}\right)  = \left| {\mu \left( {{v}_{1},\ldots ,{v}_{n}}\right) }\right| .
\]

The set \( \mathcal{D}\left( V\right) \) of all densities on \( V \) is a 1-dimensional vector space, spanned by \( \left| \mu \right| \) for any nonzero alternating \( n \) -tensor \( \mu \) .

When \( M \) is a smooth manifold with or without boundary, the set

\[
\mathcal{D}M = \mathop{\coprod }\limits_{{p \in  M}}\mathcal{D}\left( {{T}_{p}M}\right)
\]

is called the density bundle of \( M \) . It is a smooth rank-1 vector bundle, with \( \left| {d{x}^{1} \land  \cdots  \land  d{x}^{n}}\right| \) as a smooth local frame over any smooth coordinate chart. A density on \( M \) is a (smooth) section \( \mu \) of \( {DM} \) ; in any local coordinates, it can be written

\[
\mu  = u\left| {d{x}^{1} \land  \cdots  \land  d{x}^{n}}\right|
\]

for some locally defined smooth function \( u \) .

Under smooth maps, densities pull back in the same way as differential forms: Suppose \( F : M \rightarrow  N \) is a smooth map between \( n \) -manifolds with or without boundary, and \( \mu \) is a density on \( N \) . The pullback of \( \mu \) is the density \( {F}^{ * }\mu \) on \( M \) defined by

\[
{\left( {F}^{ * }\mu \right) }_{p}\left( {{v}_{1},\ldots ,{v}_{n}}\right)  = {\mu }_{F\left( p\right) }\left( {d{F}_{p}\left( {v}_{1}\right) ,\ldots , d{F}_{p}\left( {v}_{n}\right) }\right) .
\]

In coordinates, this satisfies

\[
{F}^{ * }\left( {u\left| {d{y}^{1} \land  \cdots  \land  d{y}^{n}}\right| }\right)  = \left( {u \circ  F}\right) \left| {\det {DF}}\right| \left| {d{x}^{1} \land  \cdots  \land  d{x}^{n}}\right| , \tag{B.15}
\]

where \( {DF} \) represents the matrix of partial derivatives of \( F \) in these coordinates.

Because the pullback formula (B.15) is exactly analogous to the change of variables formula for multiple integrals, we can define the integral of a compactly supported density on a smooth manifold with or without boundary in exactly the same way as the integral of an \( n \) -form is defined on an oriented manifold, except that now there is no need to have an orientation. Thus if \( \mu  = u\left| {d{x}^{1}\cdots d{x}^{n}}\right| \) is a smooth density that is compactly supported in an open set \( V \subseteq  {\mathbb{R}}^{n} \) , we define the integral of \( \mu \) by

\[
{\int }_{V}\mu  = {\int }_{V}{ud}{x}^{1}\cdots d{x}^{n}
\]

It follows from (B.15) that the value of this integral is diffeomorphism-invariant, so we can define the integral of a compactly supported density on a smooth manifold with or without boundary by breaking it up with a partition of unity and integrating each term in coordinates as above.
