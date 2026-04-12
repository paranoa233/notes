## Chapter 2 Riemannian Metrics

In this chapter we officially define Riemannian metrics, and discuss some of the basic computational techniques associated with them. After the definitions, we describe a few standard methods for constructing Riemannian manifolds as subman-ifolds, products, and quotients of other Riemannian manifolds. Then we introduce some of the elementary geometric constructions provided by Riemannian metrics, the most important of which is the Riemannian distance function, which turns every connected Riemannian manifold into a metric space.

At the end of the chapter, we discuss some important generalizations of Riemannian metrics-most importantly, the pseudo-Riemannian metrics, followed by brief mentions of sub-Riemannian and Finsler metrics.

Before you read this chapter, it would be a good idea to skim through the three appendices after Chapter 12 to get an idea of the prerequisite material that will be assumed throughout this book.

## Definitions

Everything we know about the Euclidean geometry of \( {\mathbb{R}}^{n} \) can be derived from its dot product, which is defined for \( v = \left( {{v}^{1},\ldots ,{v}^{n}}\right) \) and \( w = \left( {{w}^{1},\ldots ,{w}^{n}}\right) \) by

\[
v \cdot  w = \mathop{\sum }\limits_{{i = 1}}^{n}{v}^{i}{w}^{i}
\]

The dot product has a natural generalization to arbitrary vector spaces. Given a vector space \( V \) (which we always assume to be real), an inner product on \( V \) is a map \( V \times  V \rightarrow  \mathbb{R} \) , typically written \( \left( {v, w}\right)  \mapsto  \langle v, w\rangle \) , that satisfies the following properties for all \( v, w, x \in  V \) and \( a, b \in  \mathbb{R} \) :

(i) SYMMETRY: \( \langle v, w\rangle  = \langle w, v\rangle \) .

(ii) BILINEARITY: \( \langle {av} + {bw}, x\rangle  = a\langle v, x\rangle  + b\langle w, x\rangle  = \langle x,{av} + {bw}\rangle \) . (iii) POSITIVE DEFINITENESS: \( \langle v, v\rangle  \geq  0 \) , with equality if and only if \( v = 0 \) .

A vector space endowed with a specific inner product is called an inner product space.

An inner product on \( V \) allows us to make sense of geometric quantities such as lengths of vectors and angles between vectors. First, we define the length or norm of a vector \( v \in  V \) as

\[
\left| v\right|  = \langle v, v{\rangle }^{1/2} \tag{2.1}
\]

The following identity shows that an inner product is completely determined by knowledge of the lengths of all vectors.

Lemma 2.1 (Polarization Identity). Suppose \( \langle  \cdot  , \cdot  \rangle \) is an inner product on a vector space \( V \) . Then for all \( v, w \in  V \) ,

\[
\langle v, w\rangle  = \frac{1}{4}\left( {\langle v + w, v + w\rangle -\langle v - w, v - w\rangle }\right) . \tag{2.2}
\]

- Exercise 2.2. Prove the preceding lemma.

The angle between two nonzero vectors \( v, w \in  V \) is defined as the unique \( \theta  \in \; \left\lbrack  {0,\pi }\right\rbrack \) satisfying

\[
\cos \theta  = \frac{\langle v, w\rangle }{\left| v\right| \left| w\right| } \tag{2.3}
\]

Two vectors \( v, w \in  V \) are said to be orthogonal if \( \langle v, w\rangle  = 0 \) , which means that either their angle is \( \pi /2 \) or one of the vectors is zero. If \( S \subseteq  V \) is a linear subspace, the set \( {S}^{ \bot  } \subseteq  V \) , consisting of all vectors in \( V \) that are orthogonal to every vector in \( S \) , is also a linear subspace, called the orthogonal complement of \( S \) .

Vectors \( {v}_{1},\ldots ,{v}_{k} \) are called orthonormal if they are of length 1 and pairwise orthogonal, or equivalently if \( \left\langle  {{v}_{i},{v}_{j}}\right\rangle   = {\delta }_{ij} \) (where \( {\delta }_{ij} \) is the Kronecker delta symbol defined in Appendix B; see (B.1)). The following well-known proposition shows that every finite-dimensional inner product space has an orthonormal basis.

Proposition 2.3 (Gram-Schmidt Algorithm). Let \( V \) be an \( n \) -dimensional inner product space, and suppose \( \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) is any ordered basis for \( V \) . Then there is an orthonormal ordered basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) satisfying the following conditions:

\[
\operatorname{span}\left( {{b}_{1},\ldots ,{b}_{k}}\right)  = \operatorname{span}\left( {{v}_{1},\ldots ,{v}_{k}}\right) \;\text{ for each }k = 1,\ldots , n. \tag{2.4}
\]

Proof. The basis vectors \( {b}_{1},\ldots ,{b}_{n} \) are defined recursively by

\[
{b}_{1} = \frac{{v}_{1}}{\left| {v}_{1}\right| } \tag{2.5}
\]

\[
{b}_{j} = \frac{{v}_{j} - \mathop{\sum }\limits_{{i = 1}}^{{j - 1}}\left\langle  {{v}_{j},{b}_{i}}\right\rangle  {b}_{i}}{\left| {v}_{j} - \mathop{\sum }\limits_{{i = 1}}^{{j - 1}}\left\langle  {v}_{j},{b}_{i}\right\rangle  {b}_{i}\right| },\;2 \leq  j \leq  n. \tag{2.6}
\]

Because \( {v}_{1} \neq  0 \) and \( {v}_{j} \notin  \operatorname{span}\left( {{b}_{1},\ldots ,{b}_{j - 1}}\right) \) for each \( j \geq  2 \) , the denominators are all nonzero. These vectors satisfy (2.4) by construction, and are orthonormal by direct computation.

If two vector spaces \( V \) and \( W \) are both equipped with inner products, denoted by \( \langle  \cdot  , \cdot  {\rangle }_{V} \) and \( \langle  \cdot  , \cdot  {\rangle }_{W} \) , respectively, then a map \( F : V \rightarrow  W \) is called a linear isometry if it is a vector space isomorphism that preserves inner products: \( {\left\langle  F\left( v\right) , F\left( {v}^{\prime }\right) \right\rangle  }_{W} = {\left\langle  v,{v}^{\prime }\right\rangle  }_{V} \) . If \( V \) and \( W \) are inner product spaces of dimension \( n \) , then given any choices of orthonormal bases \( \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) for \( V \) and \( \left( {{w}_{1},\ldots ,{w}_{n}}\right) \) for \( W \) , the linear map \( F : V \rightarrow  W \) determined by \( F\left( {v}_{i}\right)  = {w}_{i} \) is easily seen to be a linear isometry. Thus all inner product spaces of the same finite dimension are linearly isometric to each other.

## Riemannian Metrics

To extend these geometric ideas to abstract smooth manifolds, we define a structure that amounts to a smoothly varying choice of inner product on each tangent space.

Let \( M \) be a smooth manifold. A Riemannian metric on \( M \) is a smooth covariant 2-tensor field \( g \in  {\mathcal{T}}^{2}\left( M\right) \) whose value \( {g}_{p} \) at each \( p \in  M \) is an inner product on \( {T}_{p}M \) ; thus \( g \) is a symmetric 2-tensor field that is positive definite in the sense that \( {g}_{p}\left( {v, v}\right)  \geq  0 \) for each \( p \in  M \) and each \( v \in  {T}_{p}M \) , with equality if and only if \( v = 0 \) . A Riemannian manifold is a pair \( \left( {M, g}\right) \) , where \( M \) is a smooth manifold and \( g \) is a specific choice of Riemannian metric on \( M \) . If \( M \) is understood to be endowed with a specific Riemannian metric, we sometimes say " \( M \) is a Riemannian manifold."

The next proposition shows that Riemannian metrics exist in great abundance.

Proposition 2.4. Every smooth manifold admits a Riemannian metric.

- Exercise 2.5. Use a partition of unity to prove the preceding proposition.

We will give a number of examples of Riemannian metrics, along with several systematic methods for constructing them, later in this chapter and in the next.

If \( M \) is a smooth manifold with boundary, a Riemannian metric on \( M \) is defined in exactly the same way: a smooth symmetric 2-tensor field \( g \) that is positive definite everywhere. A Riemannian manifold with boundary is a pair \( \left( {M, g}\right) \) , where \( M \) is a smooth manifold with boundary and \( g \) is a Riemannian metric on \( M \) . Many of the results we will discuss in this book work equally well for manifolds with or without boundary, with the same proofs, and in such cases we will state them in that generality. But when the treatment of a boundary would involve additional difficulties, we will generally restrict attention to the case of manifolds without boundary, since that is our primary interest. Many problems involving Riemannian manifolds with boundary can be addressed by embedding into a larger manifold without boundary and extending the Riemannian metric arbitrarily to the larger manifold; see Proposition A. 31 in Appendix A.

A Riemannian metric is not the same as a metric in the sense of metric spaces (though, as we will see later in this chapter, the two concepts are related). In this book, when we use the word "metric" without further qualification, it always refers to a Riemannian metric.

Let \( g \) be a Riemannian metric on a smooth manifold \( M \) with or without boundary. Because \( {g}_{p} \) is an inner product on \( {T}_{p}M \) for each \( p \in  M \) , we often use the following angle-bracket notation for \( v, w \in  {T}_{p}M \) :

\[
\langle v, w{\rangle }_{g} = {g}_{p}\left( {v, w}\right) .
\]

Using this inner product, we can define lengths of tangent vectors, angles between nonzero tangent vectors, and orthogonality of tangent vectors as described above. The length of a vector \( v \in  {T}_{p}M \) is denoted by \( {\left| v\right| }_{g} = \langle v, v{\rangle }_{g}^{1/2} \) . If the metric is understood, we sometimes omit it from the notation, and write \( \langle v, w\rangle \) and \( \left| v\right| \) in place of \( \langle v, w{\rangle }_{g} \) and \( {\left| v\right| }_{g} \) , respectively.

The starting point for Riemannian geometry is the following fundamental example.

Example 2.6 (The Euclidean Metric). The Euclidean metric is the Riemannian metric \( \bar{g} \) on \( {\mathbb{R}}^{n} \) whose value at each \( x \in  {\mathbb{R}}^{n} \) is just the usual dot product on \( {T}_{x}{\mathbb{R}}^{n} \) under the natural identification \( {T}_{x}{\mathbb{R}}^{n} \cong  {\mathbb{R}}^{n} \) . This means that for \( v, w \in  {T}_{x}{\mathbb{R}}^{n} \) written in standard coordinates \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) as \( v = \mathop{\sum }\limits_{i}{v}^{i}{\partial }_{i}{\left| {}_{x}, w = \mathop{\sum }\limits_{j}{w}^{j}{\partial }_{j}\right| }_{x} \) , we have

\[
\langle v, w{\rangle }_{\bar{g}} = \mathop{\sum }\limits_{{i = 1}}^{n}{v}^{i}{w}^{i}.
\]

When working with \( {\mathbb{R}}^{n} \) as a Riemannian manifold, we always assume we are using the Euclidean metric unless otherwise specified.

## Isometries

Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian manifolds with or without boundary. An isometry from \( \left( {M, g}\right) \) to \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a diffeomorphism \( \varphi  : M \rightarrow  \widetilde{M} \) such that \( {\varphi }^{ * }\widetilde{g} = g \) . Unwinding the definitions shows that this is equivalent to the requirement that \( \varphi \) be a smooth bijection and each differential \( d{\varphi }_{p} : {T}_{p}M \rightarrow  {T}_{\varphi \left( p\right) }\widetilde{M} \) be a linear isometry. We say \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are isometric if there exists an isometry between them.

A composition of isometries and the inverse of an isometry are again isometries, so being isometric is an equivalence relation on the class of Riemannian manifolds with or without boundary. Our subject, Riemannian geometry, is concerned primarily with properties of Riemannian manifolds that are preserved by isometries.

If \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian manifolds, a map \( \varphi  : M \rightarrow  \widetilde{M} \) is a local isometry if each point \( p \in  M \) has a neighborhood \( U \) such that \( {\left. \varphi \right| }_{U} \) is an isometry onto an open subset of \( \widetilde{M} \) .

Exercise 2.7. Prove that if \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian manifolds of the same dimension, a smooth map \( \varphi  : M \rightarrow  M \) is a local isometry if and only if \( {\varphi }^{ * }\widetilde{g} = g \) .

A Riemannian \( n \) -manifold is said to be flat if it is locally isometric to a Euclidean space, that is, if every point has a neighborhood that is isometric to an open set in \( {\mathbb{R}}^{n} \) with its Euclidean metric. Problem 2-1 shows that all Riemannian 1-manifolds are flat; but we will see later that this is far from the case in higher dimensions.

An isometry from \( \left( {M, g}\right) \) to itself is called an isometry of \( \left( {M, g}\right) \) . The set of all isometries of \( \left( {M, g}\right) \) is a group under composition, called the isometry group of \( \left( {M, g}\right) \) ; it is denoted by \( \operatorname{Iso}\left( {M, g}\right) \) , or sometimes just \( \operatorname{Iso}\left( M\right) \) if the metric is understood.

A deep theorem of Sumner B. Myers and Norman E. Steenrod [MS39] shows that if \( M \) has finitely many components, then \( \operatorname{Iso}\left( {M, g}\right) \) has a topology and smooth structure making it into a finite-dimensional Lie group acting smoothly on \( M \) . We will neither prove nor use the Myers-Steenrod theorem, but if you are interested, a good source for the proof is [Kob72].

## Local Representations for Metrics

Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with or without boundary. If \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) are any smooth local coordinates on an open subset \( U \subseteq  M \) , then \( g \) can be written locally in \( U \) as

\[
g = {g}_{ij}d{x}^{i} \otimes  d{x}^{j} \tag{2.7}
\]

for some collection of \( {n}^{2} \) smooth functions \( {g}_{ij} \) for \( i, j = 1,\ldots , n \) . (Here and throughout the book, we use the Einstein summation convention; see p. 375.) The component functions of this tensor field constitute a matrix-valued function \( \left( {g}_{ij}\right) \) , characterized by \( {g}_{ij}\left( p\right)  = \left\langle  {{\left. {\partial }_{i}\right| }_{p},{\left. {\partial }_{j}\right| }_{p}}\right\rangle \) , where \( {\partial }_{i} = \partial /\partial {x}^{i} \) is the \( i \) th coordinate vector field; this matrix is symmetric in \( i \) and \( j \) and depends smoothly on \( p \in  U \) . If \( v = {v}^{i}{\partial }_{i}{ \mid  }_{p} \) is a vector in \( {T}_{p}M \) such that \( {g}_{ij}\left( p\right) {v}^{j} = 0 \) , it follows that \( \langle v, v\rangle  = {g}_{ij}\left( p\right) {v}^{i}{v}^{j} = 0 \) , which implies \( v = 0 \) ; thus the matrix \( \left( {{g}_{ij}\left( p\right) }\right) \) is always nonsingular. The notation for \( g \) can be shortened by expressing it in terms of the symmetric product (see Appendix B): using the symmetry of \( {g}_{ij} \) , we compute

\[
g = {g}_{ij}d{x}^{i} \otimes  d{x}^{j}
\]

\[
= \frac{1}{2}\left( {{g}_{ij}d{x}^{i} \otimes  d{x}^{j} + {g}_{ji}d{x}^{i} \otimes  d{x}^{j}}\right)
\]

\[
= \frac{1}{2}\left( {{g}_{ij}d{x}^{i} \otimes  d{x}^{j} + {g}_{ij}d{x}^{j} \otimes  d{x}^{i}}\right)
\]

\[
= {g}_{ij}d{x}^{i}d{x}^{j}\text{ . }
\]

For example, the Euclidean metric on \( {\mathbb{R}}^{n} \) (Example 2.6) can be expressed in standard coordinates in several ways:

\[
\bar{g} = \mathop{\sum }\limits_{i}d{x}^{i}d{x}^{i} = \mathop{\sum }\limits_{i}{\left( d{x}^{i}\right) }^{2} = {\delta }_{ij}d{x}^{i}d{x}^{j}. \tag{2.8}
\]

The matrix of \( \bar{g} \) in these coordinates is thus \( {\bar{g}}_{ij} = {\delta }_{ij} \) .

More generally, if \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) is any smooth local frame for \( {TM} \) on an open subset \( U \subseteq  M \) and \( \left( {{\varepsilon }^{1},\ldots ,{\varepsilon }^{n}}\right) \) is its dual coframe, we can write \( g \) locally in \( U \) as

\[
g = {g}_{ij}{\varepsilon }^{i}{\varepsilon }^{j} \tag{2.9}
\]

where \( {g}_{ij}\left( p\right)  = \left\langle  {{\left. {E}_{i}\right| }_{p},{\left. {E}_{j}\right| }_{p}}\right\rangle \) , and the matrix-valued function \( \left( {g}_{ij}\right) \) is symmetric and smooth as before.

A Riemannian metric \( g \) acts on smooth vector fields \( X, Y \in  \mathfrak{X}\left( M\right) \) to yield a real-valued function \( \langle X, Y\rangle \) . In terms of any smooth local frame, this function is expressed locally by \( \langle X, Y\rangle  = {g}_{ij}{X}^{i}{Y}^{j} \) and therefore is smooth. Similarly, we obtain a nonnegative real-valued function \( \left| X\right|  = \langle X, X{\rangle }^{1/2} \) , which is continuous everywhere and smooth on the open subset where \( X \neq  0 \) .

A local frame \( \left( {E}_{i}\right) \) for \( M \) on an open set \( U \) is said to be an orthonormal frame if the vectors \( {\left. {E}_{1}\right| }_{p},\ldots ,{\left. {E}_{n}\right| }_{p} \) are an orthonormal basis for \( {T}_{p}M \) at each \( p \in  U \) . Equivalently, \( \left( {E}_{i}\right) \) is an orthonormal frame if and only if

\[
\left\langle  {{E}_{i},{E}_{j}}\right\rangle   = {\delta }_{ij},
\]

in which case \( g \) has the local expression

\[
g = {\left( {\varepsilon }^{1}\right) }^{2} + \cdots  + {\left( {\varepsilon }^{n}\right) }^{2},
\]

where \( {\left( {\varepsilon }^{i}\right) }^{2} \) denotes the symmetric product \( {\varepsilon }^{i}{\varepsilon }^{i} = {\varepsilon }^{i} \otimes  {\varepsilon }^{i} \) .

Proposition 2.8 (Existence of Orthonormal Frames). Let \( \left( {M, g}\right) \) be a Riemannian n-manifold with or without boundary. If \( \left( {X}_{j}\right) \) is any smooth local frame for TM over an open subset \( U \subseteq  M \) , then there is a smooth orthonormal frame \( \left( {E}_{j}\right) \) over \( U \) such that \( \operatorname{span}\left( {{\left. {E}_{1}\right| }_{p},\ldots ,{\left. {E}_{k}\right| }_{p}}\right)  = \operatorname{span}\left( {{\left. {X}_{1}\right| }_{p},\ldots ,{\left. {X}_{k}\right| }_{p}}\right) \) for each \( k = 1,\ldots , n \) and each \( p \in  U \) . In particular, for every \( p \in  M \) , there is a smooth orthonormal frame \( \left( {E}_{j}\right) \) defined on some neighborhood of \( p \) .

Proof. Applying the Gram-Schmidt algorithm to the vectors \( \left( {{\left. {X}_{1}\right| }_{p},\ldots ,{\left. {X}_{n}\right| }_{p}}\right) \) at each \( p \in  U \) , we obtain an ordered \( n \) -tuple of rough orthonormal vector fields \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) over \( U \) satisfying the span conditions. Because the vectors whose norms appear in the denominators of (2.5)-(2.6) are nowhere vanishing, those formulas show that each vector field \( {E}_{j} \) is smooth. The last statement of the proposition follows by applying this construction to any smooth local frame in a neighborhood of \( p \) .

Warning: A common mistake made by beginners is to assume that one can find coordinates near \( p \) such that the coordinate frame \( \left( {\partial }_{i}\right) \) is orthonormal. Proposition 2.8 does not show this. In fact, as we will see in Chapter 7, this is possible only when the metric is flat, that is, locally isometric to the Euclidean metric.

For a Riemannian manifold \( \left( {M, g}\right) \) with or without boundary, we define the unit tangent bundle to be the subset \( {UTM} \subseteq  {TM} \) consisting of unit vectors:

\[
{UTM} = \left\{  {\left( {p, v}\right)  \in  {TM} : {\left| v\right| }_{g} = 1}\right\}  . \tag{2.10}
\]

Proposition 2.9 (Properties of the Unit Tangent Bundle). If \( \left( {M, g}\right) \) is a Riemannian manifold with or without boundary, its unit tangent bundle UTM is a smooth, properly embedded codimension-1 submanifold with boundary in TM, with \( \partial \left( {UTM}\right)  = {\pi }^{-1}\left( {\partial M}\right) \) (where \( \pi  : {UTM} \rightarrow  M \) is the canonical projection). The unit tangent bundle is connected if and only if \( M \) is connected, and compact if and only if \( M \) is compact.

Exercise 2.10. Use local orthonormal frames to prove the preceding proposition.

## Methods for Constructing Riemannian Metrics

Many examples of Riemannian manifolds arise naturally as submanifolds, products, and quotients of other Riemannian manifolds. In this section, we introduce some of the tools for constructing such metrics.

## Riemannian Submanifolds

Every submanifold of a Riemannian manifold automatically inherits a Riemannian metric, and many interesting Riemannian metrics are defined in this way. The key fact is the following lemma.

Lemma 2.11. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian manifold with or without boundary, \( M \) is a smooth manifold with or without boundary, and \( F : M \rightarrow  \widetilde{M} \) is a smooth map. The smooth 2-tensor field \( g = {F}^{ * }\widetilde{g} \) is a Riemannian metric on \( M \) if and only if \( F \) is an immersion.

Exercise 2.12. Prove Lemma 2.11.

Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian manifold with or without boundary. Given a smooth immersion \( F : M \rightarrow  \widetilde{M} \) , the metric \( g = {F}^{ * }\widetilde{g} \) is called the metric induced by \( \mathbf{F} \) . On the other hand, if \( M \) is already endowed with a given Riemannian metric \( g \) , an immersion or embedding \( F : M \rightarrow  \widetilde{M} \) satisfying \( {F}^{ * }\widetilde{g} = g \) is called an isometric immersion or isometric embedding, respectively. Which terminology is used depends on whether the metric on \( M \) is considered to be given independently of the immersion or not.

The most important examples of induced metrics occur on submanifolds. Suppose \( M \subseteq  \widetilde{M} \) is an (immersed or embedded) submanifold, with or without boundary. The induced metric on \( \mathbf{M} \) is the metric \( g = {\iota }^{ * }\widetilde{g} \) induced by the inclusion map \( \iota  : M \hookrightarrow  \widetilde{M} \) . With this metric, \( M \) is called a Riemannian submanifold (or Riemannian submanifold with boundary) of \( \widetilde{M} \) . We always consider submanifolds (with or without boundary) of Riemannian manifolds to be endowed with the induced metrics unless otherwise specified.

If \( \left( {M, g}\right) \) is a Riemannian submanifold of \( \left( {\widetilde{M},\widetilde{g}}\right) \) , then for every \( p \in  M \) and \( v, w \in \; {T}_{p}M \) , the definition of the induced metric reads

\[
{g}_{p}\left( {v, w}\right)  = {\widetilde{g}}_{p}\left( {d{\iota }_{p}\left( v\right) , d{\iota }_{p}\left( w\right) }\right) .
\]

Because we usually identify \( {T}_{p}M \) with its image in \( {T}_{p}\widetilde{M} \) under \( d{\iota }_{p} \) , and think of \( d{\iota }_{p} \) as an inclusion map, what this really amounts to is \( {g}_{p}\left( {v, w}\right)  = {\widetilde{g}}_{p}\left( {v, w}\right) \) for \( v, w \in  {T}_{p}M \) . In other words, the induced metric \( g \) is just the restriction of \( \widetilde{g} \) to vectors tangent to \( M \) . Many of the examples of Riemannian metrics that we will encounter are obtained in this way, starting with the following.

Example 2.13 (Spheres). For each positive integer \( n \) , the unit \( n \) -sphere \( {\mathbb{S}}^{n} \subseteq  {\mathbb{R}}^{n + 1} \) is an embedded \( n \) -dimensional submanifold. The Riemannian metric induced on \( {\mathbb{S}}^{n} \) by the Euclidean metric is denoted by \( \overset{ \circ  }{g} \) and known as the round metric or standard metric on \( {\mathbb{S}}^{n} \) .

The next lemma describes one of the most important tools for studying Riemannian submanifolds. If \( \left( {\widetilde{M},\widetilde{g}}\right) \) is an \( m \) -dimensional smooth Riemannian manifold and \( M \subseteq  \widetilde{M} \) is an \( n \) -dimensional submanifold (both with or without boundary), a local frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) for \( \widetilde{M} \) on an open subset \( \widetilde{U} \subseteq  \widetilde{M} \) is said to be adapted to \( M \) if the first \( n \) vector fields \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) are tangent to \( M \) . In case \( \widetilde{M} \) has empty boundary (so that slice coordinates are available), adapted local orthonormal frames are easy to find.

Proposition 2.14 (Existence of Adapted Orthonormal Frames). Let \( \left( {\widetilde{M},\widetilde{g}}\right) \) be a Riemannian manifold (without boundary), and let \( M \subseteq  \widetilde{M} \) be an embedded smooth submanifold with or without boundary. Given \( p \in  M \) , there exist a neighborhood \( \widetilde{U} \) of \( p \) in \( \widetilde{M} \) and a smooth orthonormal frame for \( \widetilde{M} \) on \( \widetilde{U} \) that is adapted to \( M \) .

Exercise 2.15. Prove the preceding proposition. [Hint: Apply the Gram-Schmidt algorithm to a coordinate frame in slice coordinates (see Prop. A.22).]

Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian manifold and \( M \subseteq  \widetilde{M} \) is a smooth submanifold with or without boundary in \( \widetilde{M} \) . Given \( p \in  M \) , a vector \( v \in  {T}_{p}\widetilde{M} \) is said to be normal to \( M \) if \( \langle v, w\rangle  = 0 \) for every \( w \in  {T}_{p}M \) . The space of all vectors normal to \( M \) at \( p \) is a subspace of \( {T}_{p}\widetilde{M} \) , called the normal space at \( p \) and denoted by \( {N}_{p}M = {\left( {T}_{p}M\right) }^{ \bot  } \) . At each \( p \in  M \) , the ambient tangent space \( {T}_{p}\widetilde{M} \) splits as an orthogonal direct sum \( {T}_{p}\widetilde{M} = {T}_{p}M \oplus  {N}_{p}M \) . A section \( N \) of the ambient tangent bundle \( {\left. T\widetilde{M}\right| }_{M} \) is called a normal vector field along \( M \) if \( {N}_{p} \in  {N}_{p}M \) for each \( p \in  M \) . The set

\[
{NM} = \mathop{\coprod }\limits_{{p \in  M}}{N}_{p}M
\]

is called the normal bundle of \( M \) .

Proposition 2.16 (The Normal Bundle). If \( \widetilde{M} \) is a Riemannian \( m \) -manifold and \( M \subseteq  \widetilde{M} \) is an immersed or embedded n-dimensional submanifold with or without boundary, then NM is a smooth rank- \( \left( {m - n}\right) \) vector subbundle of the ambient tangent bundle \( {\left. T\widetilde{M}\right| }_{M} \) . There are smooth bundle homomorphisms

\[
{\pi }^{\top } : {\left. T\widetilde{M}\right| }_{M} \rightarrow  {TM},\;{\pi }^{ \bot  } : {\left. T\widetilde{M}\right| }_{M} \rightarrow  {NM},
\]

called the tangential and normal projections, that for each \( p \in  M \) restrict to orthogonal projections from \( {T}_{p}\widetilde{M} \) to \( {T}_{p}M \) and \( {N}_{p}M \) , respectively.

Proof. Given any point \( p \in  M \) , Theorem A. 16 shows that there is a neighborhood \( U \) of \( p \) in \( M \) that is embedded in \( \widetilde{M} \) , and then Proposition 2.14 shows that there is a smooth orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) that is adapted to \( U \) on some neighborhood \( \widetilde{U} \) of \( p \) in \( \widetilde{M} \) . This means that the restrictions of \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) to \( \widetilde{U} \cap  U \) form a local orthonormal frame for \( M \) . Given such an adapted frame, the restrictions of the last \( m - n \) vector fields \( \left( {{E}_{n + 1},\ldots ,{E}_{m}}\right) \) to \( M \) form a smooth local frame for \( {NM} \) , so it follows from Lemma A.34 that \( {NM} \) is a smooth subbundle.

The bundle homomorphisms \( {\pi }^{\top } \) and \( {\pi }^{ \bot  } \) are defined pointwise as orthogonal projections onto the tangent and normal spaces, respectively, which shows that they are uniquely defined. In terms of an adapted orthonormal frame, they can be written

\[
{\pi }^{\top }\left( {{X}^{1}{E}_{1} + \cdots  + {X}^{m}{E}_{m}}\right)  = {X}^{1}{E}_{1} + \cdots  + {X}^{n}{E}_{n},
\]

\[
{\pi }^{ \bot  }\left( {{X}^{1}{E}_{1} + \cdots  + {X}^{m}{E}_{m}}\right)  = {X}^{n + 1}{E}_{n + 1} + \cdots  + {X}^{m}{E}_{m},
\]

which shows that they are smooth.

In case \( \widetilde{M} \) is a manifold with boundary, the preceding constructions do not always work, because there is not a fully general construction of slice coordinates in that case. However, there is a satisfactory result in case the submanifold is the boundary itself, using boundary coordinates in place of slice coordinates.

Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with boundary. We will always consider \( \partial M \) to be a Riemannian submanifold with the induced metric.

Proposition 2.17 (Existence of Outward-Pointing Normal). If \( \left( {M, g}\right) \) is a smooth Riemannian manifold with boundary, the normal bundle to \( \partial M \) is a smooth rank-1 vector bundle over \( \partial M \) , and there is a unique smooth outward-pointing unit normal vector field along all of \( \partial M \) .

Exercise 2.18. Prove this proposition. [Hint: Use the paragraph preceding Prop. B.17 as a starting point.]

Computations on a submanifold \( M \subseteq  \widetilde{M} \) are usually carried out most conveniently in terms of a smooth local parametrization: this is a smooth map \( X : U \rightarrow \; \widetilde{M} \) , where \( U \) is an open subset of \( {\mathbb{R}}^{n} \) (or \( {\mathbb{R}}_{ + }^{n} \) in case \( M \) has a boundary), such that \( X\left( U\right) \) is an open subset of \( M \) , and such that \( X \) , regarded as a map from \( U \) into \( M \) , is a diffeomorphism onto its image. Note that we can think of \( X \) either as a map into \( M \) or as a map into \( \widetilde{M} \) ; both maps are typically denoted by the same symbol \( X \) . If we put \( V = X\left( U\right)  \subseteq  M \) and \( \varphi  = {X}^{-1} : V \rightarrow  U \) , then \( \left( {V,\varphi }\right) \) is a smooth coordinate chart on \( M \) .

Suppose \( \left( {M, g}\right) \) is a Riemannian submanifold of \( \left( {\widetilde{M},\widetilde{g}}\right) \) and \( X : U \rightarrow  \widetilde{M} \) is a smooth local parametrization of \( M \) . The coordinate representation of \( g \) in these coordinates is given by the following 2-tensor field on \( U \) :

\[
{\left( {\varphi }^{-1}\right) }^{ * }g = {X}^{ * }g = {X}^{ * }{\iota }^{ * }\widetilde{g} = {\left( \iota  \circ  X\right) }^{ * }\widetilde{g}.
\]

Since \( \iota  \circ  X \) is just the map \( X \) itself, regarded as a map into \( \widetilde{M} \) , this is really just \( {X}^{ * }\widetilde{g} \) . The simplicity of the formula for the pullback of a tensor field makes this expression exceedingly easy to compute, once a coordinate expression for \( \widetilde{g} \) is known. For example, if \( M \) is an immersed \( n \) -dimensional Riemannian submanifold of \( {\mathbb{R}}^{m} \) and \( X : U \rightarrow  {\mathbb{R}}^{m} \) is a smooth local parametrization of \( M \) , the induced metric on \( U \) is just

\[
g = {X}^{ * }\bar{g} = \mathop{\sum }\limits_{{i = 1}}^{m}{\left( d{X}^{i}\right) }^{2} = \mathop{\sum }\limits_{{i = 1}}^{m}{\left( \mathop{\sum }\limits_{{j = 1}}^{n}\frac{\partial {X}^{i}}{\partial {u}^{j}}d{u}^{j}\right) }^{2} = \mathop{\sum }\limits_{{i = 1}}^{m}\mathop{\sum }\limits_{{j, k = 1}}^{n}\frac{\partial {X}^{i}}{\partial {u}^{j}}\frac{\partial {X}^{i}}{\partial {u}^{k}}d{u}^{j}d{u}^{k}.
\]

Example 2.19 (Metrics in Graph Coordinates). If \( U \subseteq  {\mathbb{R}}^{n} \) is an open set and \( f : U \rightarrow  \mathbb{R} \) is a smooth function, then the graph of \( f \) is the subset \( \Gamma \left( f\right)  = \; \{ \left( {x, f\left( x\right) }\right)  : x \in  U\}  \subseteq  {\mathbb{R}}^{n + 1} \) , which is an embedded submanifold of dimension \( n \) . It has a global parametrization \( X : U \rightarrow  {\mathbb{R}}^{n + 1} \) called a graph parametrization, given by \( X\left( u\right)  = \left( {u, f\left( u\right) }\right) \) ; the corresponding coordinates \( \left( {{u}^{1},\ldots ,{u}^{n}}\right) \) on \( M \) are called graph coordinates. In graph coordinates, the induced metric of \( \Gamma \left( f\right) \) is

\[
{X}^{ * }\bar{g} = {X}^{ * }\left( {{\left( d{x}^{1}\right) }^{2} + \cdots  + {\left( d{x}^{n + 1}\right) }^{2}}\right)  = {\left( d{u}^{1}\right) }^{2} + \cdots  + {\left( d{u}^{n}\right) }^{2} + d{f}^{2}.
\]

Applying this to the upper hemisphere of \( {\mathbb{S}}^{2} \) with the parametrization \( X : {\mathbb{B}}^{2} \rightarrow  {\mathbb{R}}^{3} \) given by

\[
X\left( {u, v}\right)  = \left( {u, v,\sqrt{1 - {u}^{2} - {v}^{2}}}\right) ,
\]

we see that the round metric on \( {\mathbb{S}}^{2} \) can be written locally as

\[
\overset{ \circ  }{g} = {X}^{ * }\bar{g} = d{u}^{2} + d{v}^{2} + {\left( \frac{{udu} + {vdv}}{\sqrt{1 - {u}^{2} - {v}^{2}}}\right) }^{2}
\]

\[
= \frac{\left( {1 - {v}^{2}}\right) d{u}^{2} + \left( {1 - {u}^{2}}\right) d{v}^{2} + {2uvdudv}}{1 - {u}^{2} - {v}^{2}}.
\]

Example 2.20 (Surfaces of Revolution). Let \( H \) be the half-plane \( \{ \left( {r, z}\right)  : r > 0\} \) , and suppose \( C \subseteq  H \) is an embedded 1-dimensional submanifold. The surface of revolution determined by \( C \) is the subset \( {S}_{C} \subseteq  {\mathbb{R}}^{3} \) given by

\[
{S}_{C} = \left\{  {\left( {x, y, z}\right)  : \left( {\sqrt{{x}^{2} + {y}^{2}}, z}\right)  \in  C}\right\}  .
\]

The set \( C \) is called its generating curve (see Fig. 2.1). Every smooth local parametrization \( \gamma \left( t\right)  = \left( {a\left( t\right) , b\left( t\right) }\right) \) for \( C \) yields a smooth local parametrization for \( {S}_{C} \) of the form

\[
X\left( {t,\theta }\right)  = \left( {a\left( t\right) \cos \theta , a\left( t\right) \sin \theta , b\left( t\right) }\right) , \tag{2.11}
\]

provided that \( \left( {t,\theta }\right) \) is restricted to a sufficiently small open set in the plane. The \( t \) -coordinate curves \( t \mapsto  X\left( {t,{\theta }_{0}}\right) \) are called meridians, and the \( \theta \) -coordinate curves \( \theta  \mapsto  X\left( {{t}_{0},\theta }\right) \) are called latitude circles. The induced metric on \( {S}_{C} \) is

\[
{X}^{ * }\bar{g} = d{\left( a\left( t\right) \cos \theta \right) }^{2} + d{\left( a\left( t\right) \sin \theta \right) }^{2} + d{\left( b\left( t\right) \right) }^{2}
\]

\[
= {\left( {a}^{\prime }\left( t\right) \cos \theta dt - a\left( t\right) \sin \theta d\theta \right) }^{2}
\]

\[
+ {\left( {a}^{\prime }\left( t\right) \sin \theta dt + a\left( t\right) \cos \theta d\theta \right) }^{2} + {\left( {b}^{\prime }\left( t\right) dt\right) }^{2}
\]

\[
= \left( {{a}^{\prime }{\left( t\right) }^{2} + {b}^{\prime }{\left( t\right) }^{2}}\right) d{t}^{2} + a{\left( t\right) }^{2}d{\theta }^{2}.
\]

![bo_d7dtff491nqc73eq8m7g_32_311_205_907_540_0.jpg](images/bo_d7dtff491nqc73eq8m7g_32_311_205_907_540_0.jpg)

Fig. 2.1: A surface of revolution

In particular, if \( \gamma \) is a unit-speed curve (meaning that \( {\left| {\gamma }^{\prime }\left( t\right) \right| }^{2} = {a}^{\prime }{\left( t\right) }^{2} + {b}^{\prime }{\left( t\right) }^{2} \equiv  1 \) ), this reduces to \( d{t}^{2} + a{\left( t\right) }^{2}d{\theta }^{2} \) .

Here are some examples of surfaces of revolution and their induced metrics.

- If \( C \) is the semicircle \( {r}^{2} + {z}^{2} = 1 \) , parametrized by \( \gamma \left( \varphi \right)  = \left( {\sin \varphi ,\cos \varphi }\right) \) for \( 0 < \; \varphi  < \pi \) , then \( {S}_{C} \) is the unit sphere (minus the north and south poles). The map \( X\left( {\varphi ,\theta }\right)  = \left( {\sin \varphi \cos \theta ,\sin \varphi \sin \theta ,\cos \varphi }\right) \) constructed above is called the spherical coordinate parametrization, and the induced metric is \( d{\varphi }^{2} + {\sin }^{2}{\varphi d}{\theta }^{2} \) . (This example is the source of the terminology for meridians and latitude circles.)

- If \( C \) is the circle \( {\left( r - 2\right) }^{2} + {z}^{2} = 1 \) , parametrized by \( \gamma \left( t\right)  = \left( {2 + \cos t,\sin t}\right) \) , we obtain a torus of revolution, whose induced metric is \( d{t}^{2} + {\left( 2 + \cos t\right) }^{2}d{\theta }^{2} \) .

- If \( C \) is a vertical line parametrized by \( \gamma \left( t\right)  = \left( {1, t}\right) \) , then \( {S}_{C} \) is the unit cylinder \( {x}^{2} + {y}^{2} = 1 \) , and the induced metric is \( d{t}^{2} + d{\theta }^{2} \) . Note that this means that the parametrization \( X : {\mathbb{R}}^{2} \rightarrow  {\mathbb{R}}^{3} \) is an isometric immersion.

Example 2.21 (The \( n \) -Torus as a Riemannian Submanifold). The smooth covering map \( X : {\mathbb{R}}^{n} \rightarrow  {\mathbb{T}}^{n} \) described in Example A. 52 restricts to a smooth local parametrization on any sufficiently small open subset of \( {\mathbb{R}}^{n} \) , and the induced metric is equal to the Euclidean metric in \( \left( {u}^{i}\right) \) coordinates, and therefore the induced metric on \( {\mathbb{T}}^{n} \) is flat.

---

Exercise 2.22. Verify the claims in Examples 2.19-2.21.

---

## Riemannian Products

Next we consider products. If \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are Riemannian manifolds, the product manifold \( {M}_{1} \times  {M}_{2} \) has a natural Riemannian metric \( g = {g}_{1} \oplus  {g}_{2} \) , called the product metric, defined by

\[
{g}_{\left( {p}_{1},{p}_{2}\right) }\left( {\left( {{v}_{1},{v}_{2}}\right) ,\left( {{w}_{1},{w}_{2}}\right) }\right)  = {\left. {g}_{1}\right| }_{{p}_{1}}\left( {{v}_{1},{w}_{1}}\right)  + {\left. {g}_{2}\right| }_{{p}_{2}}\left( {{v}_{2},{w}_{2}}\right) , \tag{2.12}
\]

where \( \left( {{v}_{1},{v}_{2}}\right) \) and \( \left( {{w}_{1},{w}_{2}}\right) \) are elements of \( {T}_{{p}_{1}}{M}_{1} \oplus  {T}_{{p}_{2}}{M}_{2} \) , which is naturally identified with \( {T}_{\left( {p}_{1},{p}_{2}\right) }\left( {{M}_{1} \times  {M}_{2}}\right) \) . Smooth local coordinates \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) for \( {M}_{1} \) and \( \left( {{x}^{n + 1},\ldots ,{x}^{n + m}}\right) \) for \( {M}_{2} \) give coordinates \( \left( {{x}^{1},\ldots ,{x}^{n + m}}\right) \) for \( {M}_{1} \times  {M}_{2} \) . In terms of these coordinates, the product metric has the local expression \( g = \; {g}_{ij}d{x}^{i}d{x}^{j} \) , where \( \left( {g}_{ij}\right) \) is the block diagonal matrix

\[
\left( {g}_{ij}\right)  = \left( \begin{matrix} {\left( {g}_{1}\right) }_{ab} & 0 \\  0 & {\left( {g}_{2}\right) }_{cd} \end{matrix}\right) ;
\]

here the indices \( a, b \) run from 1 to \( n \) , and \( c, d \) run from \( n + 1 \) to \( n + m \) . Product metrics on products of three or more Riemannian manifolds are defined similarly.

Exercise 2.23. Show that the induced metric on \( {\mathbb{T}}^{n} \) described in Exercise 2.21 is equal to the product metric obtained from the usual induced metric on \( {\mathbb{S}}^{1} \subseteq  {\mathbb{R}}^{2} \) .

Here is an important generalization of product metrics. Suppose \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are two Riemannian manifolds, and \( f : {M}_{1} \rightarrow  {\mathbb{R}}^{ + } \) is a strictly positive smooth function. The warped product \( {M}_{1}{ \times  }_{f}{M}_{2} \) is the product manifold \( {M}_{1} \times  {M}_{2} \) endowed with the Riemannian metric \( g = {g}_{1} \oplus  {f}^{2}{g}_{2} \) , defined by

\[
{g}_{\left( {p}_{1},{p}_{2}\right) }\left( {\left( {{v}_{1},{v}_{2}}\right) ,\left( {{w}_{1},{w}_{2}}\right) }\right)  = {\left. {g}_{1}\right| }_{{p}_{1}}\left( {{v}_{1},{w}_{1}}\right)  + {\left. f{\left( {p}_{1}\right) }^{2}{g}_{2}\right| }_{{p}_{2}}\left( {{v}_{2},{w}_{2}}\right) ,
\]

where \( \left( {{v}_{1},{v}_{2}}\right) ,\left( {{w}_{1},{w}_{2}}\right)  \in  {T}_{{p}_{1}}{M}_{1} \oplus  {T}_{{p}_{2}}{M}_{2} \) as before. (Despite the similarity with the notation for product metrics, \( {g}_{1} \oplus  {f}^{2}{g}_{2} \) is generally not a product metric unless \( f \) is constant.) A wide variety of metrics can be constructed in this way; here are just a few examples.

## Example 2.24 (Warped Products).

(a) With \( f \equiv  1 \) , the warped product \( {M}_{1}{ \times  }_{f}{M}_{2} \) is just the space \( {M}_{1} \times  {M}_{2} \) with the product metric.

(b) Every surface of revolution can be expressed as a warped product, as follows. Let \( H \) be the half-plane \( \{ \left( {r, z}\right)  : r > 0\} \) , let \( C \subseteq  H \) be an embedded smooth 1-dimensional submanifold, and let \( {S}_{C} \subseteq  {\mathbb{R}}^{3} \) denote the corresponding surface of revolution as in Example 2.20. Endow \( C \) with the Riemannian metric induced from the Euclidean metric on \( H \) , and let \( {\mathbb{S}}^{1} \) be endowed with its standard metric. Let \( f : C \rightarrow  \mathbb{R} \) be the distance to the \( z \) -axis: \( f\left( {r, z}\right)  = r \) . Then Problem 2-3 shows that \( {S}_{C} \) is isometric to the warped product \( C{ \times  }_{f}{\mathbb{S}}^{1} \) .

(c) If we let \( \rho \) denote the standard coordinate function on \( {\mathbb{R}}^{ + } \subseteq  \mathbb{R} \) , then the map \( \Phi \left( {\rho ,\omega }\right)  = {\rho \omega } \) gives an isometry from the warped product \( {\mathbb{R}}^{ + }{ \times  }_{\rho }{\mathbb{S}}^{n - 1} \) to \( {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) with its Euclidean metric (see Problem 2-4).

## Riemannian Submersions

Unlike submanifolds and products of Riemannian manifolds, which automatically inherit Riemannian metrics of their own, quotients of Riemannian manifolds inherit Riemannian metrics only under very special circumstances. In this section, we see what those circumstances are.

Suppose \( \widetilde{M} \) and \( M \) are smooth manifolds, \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth submersion, and \( \widetilde{g} \) is a Riemannian metric on \( \widetilde{M} \) . By the submersion level set theorem (Corollary A.25), each fiber \( {\widetilde{M}}_{y} = {\pi }^{-1}\left( y\right) \) is a properly embedded smooth submanifold of \( \widetilde{M} \) . At each point \( x \in  \widetilde{M} \) , we define two subspaces of the tangent space \( {T}_{x}\widetilde{M} \) as follows: the vertical tangent space at \( x \) is

\[
{V}_{x} = \operatorname{Ker}d{\pi }_{x} = {T}_{x}\left( {\widetilde{M}}_{\pi \left( x\right) }\right)
\]

(that is, the tangent space to the fiber containing \( x \) ), and the horizontal tangent space at \( x \) is its orthogonal complement:

\[
{H}_{x} = {\left( {V}_{x}\right) }^{ \bot  }.
\]

Then the tangent space \( {T}_{x}\widetilde{M} \) decomposes as an orthogonal direct sum \( {T}_{x}\widetilde{M} = \; {H}_{x} \oplus  {V}_{x} \) . Note that the vertical space is well defined for every submersion, because it does not refer to the metric; but the horizontal space depends on the metric.

A vector field on \( \widetilde{M} \) is said to be a horizontal vector field if its value at each point lies in the horizontal space at that point; a vertical vector field is defined similarly. Given a vector field \( X \) on \( M \) , a vector field \( \widetilde{X} \) on \( \widetilde{M} \) is called a horizontal lift of \( X \) if \( \widetilde{X} \) is horizontal and \( \pi \) -related to \( X \) . (The latter property means that \( d{\pi }_{x}\left( {\widetilde{X}}_{x}\right)  = \; {X}_{\pi \left( x\right) } \) for each \( x \in  \widetilde{M} \) .)

The next proposition is the principal tool for doing computations on Riemannian submersions.

Proposition 2.25 (Properties of Horizontal Vector Fields). Let \( \widetilde{M} \) and \( M \) be smooth manifolds, let \( \pi  : \widetilde{M} \rightarrow  M \) be a smooth submersion, and let \( \widetilde{g} \) be a Riemannian metric on \( \widetilde{M} \) .

(a) Every smooth vector field \( W \) on \( \widetilde{M} \) can be expressed uniquely in the form \( W = {W}^{H} + {W}^{V} \) , where \( {W}^{H} \) is horizontal, \( {W}^{V} \) is vertical, and both \( {W}^{H} \) and \( {W}^{V} \) are smooth.

(b) Every smooth vector field on \( M \) has a unique smooth horizontal lift to \( \widetilde{M} \) .

(c) For every \( x \in  \widetilde{M} \) and \( v \in  {H}_{x} \) , there is a vector field \( X \in  \mathfrak{X}\left( M\right) \) whose horizontal lift \( \widetilde{X} \) satisfies \( {\widetilde{X}}_{x} = v \) .

Proof. Let \( p \in  \widetilde{M} \) be arbitrary. Because \( \pi \) is a smooth submersion, the rank theorem (Theorem A.15) shows that there exist smooth coordinate charts \( \left( {\widetilde{U},\left( {x}^{i}\right) }\right) \) centered at \( p \) and \( \left( {U,\left( {u}^{j}\right) }\right) \) centered at \( \pi \left( p\right) \) in which \( \pi \) has the coordinate representation

\[
\pi \left( {{x}^{1},\ldots ,{x}^{n},{x}^{n + 1},\ldots ,{x}^{m}}\right)  = \left( {{x}^{1},\ldots ,{x}^{n}}\right) ,
\]

where \( m = \dim \widetilde{M} \) and \( n = \dim M \) . It follows that at each point \( q \in  \widetilde{U} \) , the vertical space \( {V}_{q} \) is spanned by the vectors \( {\left. {\partial }_{n + 1}\right| }_{q},\ldots ,{\left. {\partial }_{m}\right| }_{q} \) . (It probably will not be the case, however, that the horizontal space is spanned by the other \( n \) basis vectors.) If we apply the Gram-Schmidt algorithm to the ordered frame \( \left( {{\partial }_{n + 1},\ldots ,{\partial }_{m},{\partial }_{1},\ldots ,{\partial }_{n}}\right) \) , we obtain a smooth orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) on \( \widetilde{U} \) such that \( {V}_{q} \) is spanned by \( \left( {{\left. {E}_{1}\right| }_{q},\ldots ,{\left. {E}_{m - n}\right| }_{q}}\right) \) at each \( q \in  \widetilde{U} \) . It follows that \( {H}_{q} \) is spanned by \( \left( {{E}_{m - n + 1}{\left| {}_{q},\ldots ,{E}_{m}\right| }_{q}}\right) \) .

Now let \( W \in  \mathfrak{X}\left( \widetilde{M}\right) \) be arbitrary. At each point \( q \in  \widetilde{M},{W}_{q} \) can be written uniquely as a sum of a vertical vector plus a horizontal vector, thus defining a decomposition \( W = {W}^{V} + {W}^{H} \) into rough vertical and horizontal vector fields. To see that they are smooth, just note that in a neighborhood of each point we can express \( W \) in terms of a frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) of the type constructed above as \( W = {W}^{1}{E}_{1} + \cdots  + {W}^{m}{E}_{m} \) with smooth coefficients \( \left( {W}^{i}\right) \) , and then it follows that \( {W}^{V} = {W}^{1}{E}_{1} + \cdots  + {W}^{m - n}{E}_{m - n} \) and \( {W}^{H} = {W}^{m - n + 1}{E}_{m - n + 1} + \cdots  + {W}^{m}{E}_{m} \) , both of which are smooth.

The proofs of (b) and (c) are left to Problem 2-5.

The fact that every horizontal vector at a point of \( \widetilde{M} \) can be extended to a horizontal lift on all of \( \widetilde{M} \) (part (c) of the preceding proposition) is highly useful for computations. It is important to be aware, though, that not every horizontal vector field on \( \widetilde{M} \) is a horizontal lift, as the next exercise shows.

Exercise 2.26. Let \( \pi  : {\mathbb{R}}^{2} \rightarrow  \mathbb{R} \) be the projection map \( \pi \left( {x, y}\right)  = x \) , and let \( W \) be the smooth vector field \( y{\partial }_{x} \) on \( {\mathbb{R}}^{2} \) . Show that \( W \) is horizontal, but there is no vector field on \( \mathbb{R} \) whose horizontal lift is equal to \( W \) .

Now we can identify some quotients of Riemannian manifolds that inherit metrics of their own. Let us begin by describing what such a metric should look like.

Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) and \( \left( {M, g}\right) \) are Riemannian manifolds, and \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth submersion. Then \( \pi \) is said to be a Riemannian submersion if for each \( x \in  \widetilde{M} \) , the differential \( d{\pi }_{x} \) restricts to a linear isometry from \( {H}_{x} \) onto \( {T}_{\pi \left( x\right) }M \) . In other words, \( {\widetilde{g}}_{x}\left( {v, w}\right)  = {g}_{\pi \left( x\right) }\left( {d{\pi }_{x}\left( v\right) , d{\pi }_{x}\left( w\right) }\right) \) whenever \( v, w \in  {H}_{x} \) .

## Example 2.27 (Riemannian Submersions).

(a) The projection \( \pi  : {\mathbb{R}}^{n + k} \rightarrow  {\mathbb{R}}^{n} \) onto the first \( n \) coordinates is a Riemannian submersion if \( {\mathbb{R}}^{n + k} \) and \( {\mathbb{R}}^{n} \) are both endowed with their Euclidean metrics.

(b) If \( M \) and \( N \) are Riemannian manifolds and \( M \times  N \) is endowed with the product metric, then both projections \( {\pi }_{M} : M \times  N \rightarrow  M \) and \( {\pi }_{N} : M \times  N \rightarrow  N \) are Riemannian submersions.

(c) If \( M{ \times  }_{f}N \) is a warped product manifold, then the projection \( {\pi }_{M} : M{ \times  }_{f}N \rightarrow \; M \) is a Riemannian submersion, but \( {\pi }_{N} \) typically is not.

Given a Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) and a surjective submersion \( \pi  : \widetilde{M} \rightarrow  M \) , it is almost never the case that there is a metric on \( M \) that makes \( \pi \) into a Riemannian submersion. It is not hard to see why: for this to be the case, whenever \( {p}_{1},{p}_{2} \in  \widetilde{M} \) are two points in the same fiber \( {\pi }^{-1}\left( y\right) \) , the linear maps \( {\left( {\left. d{\pi }_{{p}_{i}}\right| }_{{H}_{{p}_{i}}}\right) }^{-1} : {T}_{y}M \rightarrow \; {H}_{{p}_{i}} \) both have to pull \( \widetilde{g} \) back to the same inner product on \( {T}_{y}M \) .

There is, however, an important special case in which there is such a metric. Suppose \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth surjective submersion, and \( G \) is a group acting on \( \widetilde{M} \) . (See Appendix C for a review of the basic definitions and terminology regarding group actions on manifolds.) We say that the action is vertical if every element \( \varphi  \in  G \) takes each fiber to itself, meaning that \( \pi \left( {\varphi  \cdot  p}\right)  = \pi \left( p\right) \) for all \( p \in  \widetilde{M} \) . The action is transitive on fibers if for each \( p, q \in  \widetilde{M} \) such that \( \pi \left( p\right)  = \pi \left( q\right) \) , there exists \( \varphi  \in  G \) such that \( \varphi  \cdot  p = q \) .

If in addition \( \widetilde{M} \) is endowed with a Riemannian metric, the action is said to be an isometric action or an action by isometries, and the metric is said to be invariant under \( \mathbf{G} \) , if the map \( x \mapsto  \varphi  \cdot  x \) is an isometry for each \( \varphi  \in  G \) . In that case, provided the action is effective (so that different elements of \( G \) define different isometries of \( \widetilde{M} \) ), we can identify \( G \) with a subgroup of \( \operatorname{Iso}\left( {\widetilde{M}, g}\right) \) . Since an isometry is, in particular, a diffeomorphism, every isometric action is an action by diffeomorphisms.

Theorem 2.28. Let \( \left( {\widetilde{M},\widetilde{g}}\right) \) be a Riemannian manifold, let \( \pi  : \widetilde{M} \rightarrow  M \) be a surjective smooth submersion, and let \( G \) be a group acting on \( \widetilde{M} \) . If the action is isometric, vertical, and transitive on fibers, then there is a unique Riemannian metric on M such that \( \pi \) is a Riemannian submersion.

Proof. Problem 2-6.

The next corollary describes one important situation to which the preceding theorem applies.

Corollary 2.29. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian manifold, and \( G \) is a Lie group acting smoothly, freely, properly, and isometrically on \( \widetilde{M} \) . Then the orbit space \( M = \; \widetilde{M}/G \) has a unique smooth manifold structure and Riemannian metric such that \( \pi \) is a Riemannian submersion.

Proof. Under the given hypotheses, the quotient manifold theorem (Thm. C.17) shows that \( M \) has a unique smooth manifold structure such that the quotient map \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth submersion. It follows easily from the definitions in that case that the given action of \( G \) on \( \widetilde{M} \) is vertical and transitive on fibers. Since the action is also isometric, Theorem 2.28 shows that \( M \) inherits a unique Riemannian metric making \( \pi \) into a Riemannian submersion.

Here is an important example of a Riemannian metric defined in this way. A larger class of such metrics is described in Problem 2-7.

Example 2.30 (The Fubini-Study Metric). Let \( n \) be a positive integer, and consider the complex projective space \( {\mathbb{{CP}}}^{n} \) defined in Example C.19. That example shows that the map \( \pi  : {\mathbb{C}}^{n + 1} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{{CP}}}^{n} \) sending each point in \( {\mathbb{C}}^{n + 1} \smallsetminus  \{ 0\} \) to its span is a surjective smooth submersion. Identifying \( {\mathbb{C}}^{n + 1} \) with \( {\mathbb{R}}^{{2n} + 2} \) endowed with its Euclidean metric, we can view the unit sphere \( {\mathbb{S}}^{{2n} + 1} \) with its round metric \( \overset{ \circ  }{g} \) as an embedded Riemannian submanifold of \( {\mathbb{C}}^{n + 1} \smallsetminus  \{ 0\} \) . Let \( p : {\mathbb{S}}^{{2n} + 1} \rightarrow  {\mathbb{{CP}}}^{n} \) denote the restriction of the map \( \pi \) . Then \( p \) is smooth, and it is surjective, because every 1-dimensional complex subspace contains elements of unit norm. We need to show that it is a submersion. Let \( {z}_{0} \in  {\mathbb{S}}^{{2n} + 1} \) and set \( {\zeta }_{0} = p\left( {z}_{0}\right)  \in  {\mathbb{{CP}}}^{n} \) . Since \( \pi \) is a smooth submersion, it has a smooth local section \( \sigma  : U \rightarrow  {\mathbb{C}}^{n + 1} \) defined on a neighborhood \( U \) of \( {\zeta }_{0} \) and satisfying \( \sigma \left( {\zeta }_{0}\right)  = {z}_{0} \) (Thm. A.17). Let \( v : {\mathbb{C}}^{n + 1} \smallsetminus  \{ 0\}  \rightarrow  {\mathbb{S}}^{{2n} + 1} \) be the radial projection onto the sphere:

\[
v\left( z\right)  = \frac{z}{\left| z\right| }.
\]

Since dividing an element of \( {\mathbb{C}}^{n + 1} \) by a nonzero scalar does not change its span, it follows that \( p \circ  v = \pi \) . Therefore, if we set \( \widetilde{\sigma } = v \circ  \sigma \) , we have \( p \circ  \widetilde{\sigma } = p \circ  v \circ  \sigma  = \; \pi  \circ  \sigma  = {\operatorname{Id}}_{U} \) , so \( \widetilde{\sigma } \) is a local section of \( p \) . By Theorem A.17, this shows that \( p \) is a submersion.

Define an action of \( {\mathbb{S}}^{1} \) on \( {\mathbb{S}}^{{2n} + 1} \) by complex multiplication:

\[
\lambda  \cdot  \left( {{z}^{1},\ldots ,{z}^{n + 1}}\right)  = \left( {\lambda {z}^{1},\ldots ,\lambda {z}^{n + 1}}\right) ,
\]

for \( \lambda  \in  {\mathbb{S}}^{1} \) (viewed as a complex number of norm 1) and \( z = \left( {{z}^{1},\ldots ,{z}^{n + 1}}\right)  \in \; {\mathbb{S}}^{{2n} + 1} \) . This is easily seen to be isometric, vertical, and transitive on fibers of \( p \) . By Theorem 2.28, therefore, there is a unique metric on \( {\mathbb{{CP}}}^{n} \) such that the map \( p : {\mathbb{S}}^{{2n} + 1} \rightarrow  {\mathbb{{CP}}}^{n} \) is a Riemannian submersion. This metric is called the Fubini-Study metric; you will have a chance to study its geometric properties in Problems 3-19 and 8-13. ‖

## Riemannian Coverings

Another important special case of Riemannian submersions occurs in the context of covering maps. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) and \( \left( {M, g}\right) \) are Riemannian manifolds. A smooth covering map \( \pi  : \widetilde{M} \rightarrow  M \) is called a Riemannian covering if it is a local isometry.

Proposition 2.31. Suppose \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth normal covering map, and \( \widetilde{g} \) is any metric on \( \widetilde{M} \) that is invariant under all covering automorphisms. Then there is a unique metric \( g \) on \( M \) such that \( \pi \) is a Riemannian covering.

Proof. Proposition A. 49 shows that \( \pi \) is a surjective smooth submersion. The automorphism group acts vertically by definition, and Proposition C. 21 shows that it acts transitively on fibers when the covering is normal. It then follows from Theorem 2.28 that there is a unique metric \( g \) on \( M \) such that \( \pi \) is a Riemannian submersion.

Since a Riemannian submersion between manifolds of the same dimension is a local isometry, it follows that \( \pi \) is a Riemannian covering.

Proposition 2.32. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Riemannian manifold, and \( \Gamma \) is a discrete Lie group acting smoothly, freely, properly, and isometrically on \( \widetilde{M} \) . Then \( \widetilde{M}/\Gamma \) has a unique Riemannian metric such that the quotient map \( \pi  : \widetilde{M} \rightarrow  \widetilde{M}/\Gamma \) is a normal Riemannian covering.

Proof. Proposition C. 23 shows that \( \pi \) is a smooth normal covering map, and Proposition 2.31 shows that \( M = \widetilde{M}/\Gamma \) has a unique Riemannian metric such that \( \pi \) is a Riemannian covering.

Corollary 2.33. Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are connected Riemannian manifolds, \( \pi  : \widetilde{M} \rightarrow  M \) is a normal Riemannian covering map, and \( \Gamma  = {\operatorname{Aut}}_{\pi }\left( \widetilde{M}\right) \) . Then \( M \) is isometric to \( \widetilde{M}/\Gamma \) .

Proof. Proposition C. 20 shows that with the discrete topology, \( \Gamma \) is a discrete Lie group acting smoothly, freely, and properly on \( \widetilde{M} \) , and then Proposition C. 23 shows that \( \widetilde{M}/\Gamma \) is a smooth manifold and the quotient map \( q : \widetilde{M} \rightarrow  \widetilde{M}/\Gamma \) is a smooth normal covering map. The fact that both \( \pi \) and \( q \) are normal coverings implies that \( \Gamma \) acts transitively on the fibers of both maps, so the two maps are constant on each other's fibers. Proposition A. 19 then implies that there is a diffeomorphism \( F : M \rightarrow  \widetilde{M}/\Gamma \) that satisfies \( q \circ  F = \pi \) . Because both \( q \) and \( \pi \) are local isometries, \( F \) is too, and because it is bijective it is a global isometry.

Example 2.34. The two-element group \( \Gamma  = \{  \pm  1\} \) acts smoothly, freely, properly, and isometrically on \( {\mathbb{S}}^{n} \) by multiplication. Example C. 24 shows that the quotient space is diffeomorphic to the real projective space \( {\mathbb{{RP}}}^{n} \) and the quotient map \( q : {\mathbb{S}}^{n} \rightarrow  {\mathbb{{RP}}}^{n} \) is a smooth normal covering map. Because the action is isometric, Proposition 2.32 shows that there is a unique metric on \( {\mathbb{{RP}}}^{n} \) such that \( q \) is a Riemannian covering.

Example 2.35 (The Open Möbius Band). The open Möbius band is the quotient space \( M = {\mathbb{R}}^{2}/\mathbb{Z} \) , where \( \mathbb{Z} \) acts on \( {\mathbb{R}}^{2} \) by \( n \cdot  \left( {x, y}\right)  = \left( {x + n,{\left( -1\right) }^{n}y}\right) \) . This action is smooth, free, proper, and isometric, and therefore \( M \) inherits a flat Riemannian metric such that the quotient map is a Riemannian covering. (See Problem 2-8.) //

Exercise 2.36. Let \( {\mathbb{T}}^{n} \subseteq  {\mathbb{R}}^{2n} \) be the \( n \) -torus with its induced metric. Show that the map \( X : {\mathbb{R}}^{n} \rightarrow  {\mathbb{T}}^{n} \) of Example 2.21 is a Riemannian covering.

## Basic Constructions on Riemannian Manifolds

Every Riemannian metric yields an abundance of useful constructions on manifolds, besides the obvious ones of lengths of vectors and angles between them. In this section we describe the most basic ones. Throughout this section \( M \) is a smooth manifold with or without boundary.

## Raising and Lowering Indices

One elementary but important property of Riemannian metrics is that they allow us to convert vectors to covectors and vice versa. Given a Riemannian metric \( g \) on \( M \) , we define a bundle homomorphism \( \widehat{g} : {TM} \rightarrow  {T}^{ * }M \) by setting

\[
\widehat{g}\left( v\right) \left( w\right)  = {g}_{p}\left( {v, w}\right)
\]

for all \( p \in  M \) and \( v, w \in  {T}_{p}M \) . If \( X \) and \( Y \) are smooth vector fields on \( M \) , this yields

\[
\widehat{g}\left( X\right) \left( Y\right)  = g\left( {X, Y}\right) ,
\]

which implies, first, that \( \widehat{g}\left( X\right) \left( Y\right) \) is linear over \( {C}^{\infty }\left( M\right) \) in \( Y \) and thus \( \widehat{g}\left( X\right) \) is a smooth covector field by the tensor characterization lemma (Lemma B.6); and second, that the covector field \( \widehat{g}\left( X\right) \) is linear over \( {C}^{\infty }\left( M\right) \) as a function of \( X \) , and thus \( \widehat{g} \) is a smooth bundle homomorphism.

Given a smooth local frame \( \left( {E}_{i}\right) \) and its dual coframe \( \left( {\varepsilon }^{i}\right) \) , let \( g = {g}_{ij}{\varepsilon }^{i}{\varepsilon }^{j} \) be the local expression for \( g \) . If \( X = {X}^{i}{E}_{i} \) is a smooth vector field, the covector field \( \widehat{g}\left( X\right) \) has the coordinate expression

\[
\widehat{g}\left( X\right)  = \left( {{g}_{ij}{X}^{i}}\right) {\varepsilon }^{j}.
\]

Thus the matrix of \( \widehat{g} \) in any local frame is the same as the matrix of \( g \) itself.

Given a vector field \( X \) , it is standard practice to denote the components of the covector field \( \widehat{g}\left( X\right) \) by

\[
{X}_{j} = {g}_{ij}{X}^{i}
\]

so that

\[
\widehat{g}\left( X\right)  = {X}_{j}{\varepsilon }^{j},
\]

and we say that \( \widehat{g}\left( X\right) \) is obtained from \( X \) by lowering an index. With this in mind, the covector field \( \widehat{g}\left( X\right) \) is denoted by \( {X}^{\flat } \) and called \( X \) flat, borrowing from the musical notation for lowering a tone.

Because the matrix \( \left( {g}_{ij}\right) \) is nonsingular at each point, the map \( \widehat{g} \) is invertible, and the matrix of \( {\widehat{g}}^{-1} \) is just the inverse matrix of \( \left( {g}_{ij}\right) \) . We denote this inverse matrix by \( \left( {g}^{ij}\right) \) , so that \( {g}^{ij}{g}_{jk} = {g}_{kj}{g}^{ji} = {\delta }_{k}^{i} \) . The symmetry of \( {g}_{ij} \) easily implies that \( \left( {g}^{ij}\right) \) is also symmetric in \( i \) and \( j \) . In terms of a local frame, the inverse map \( {\widehat{g}}^{-1} \) is given by

\[
{\widehat{g}}^{-1}\left( \omega \right)  = {\omega }^{i}{E}_{i}
\]

where

\[
{\omega }^{i} = {g}^{ij}{\omega }_{j} \tag{2.13}
\]

If \( \omega \) is a covector field, the vector field \( {\widehat{g}}^{-1}\left( \omega \right) \) is called (what else?) \( \omega \) sharp and denoted by \( {\omega }^{\sharp } \) , and we say that it is obtained from \( \omega \) by raising an index. The two inverse isomorphisms \( b \) and \( \sharp \) are known as the musical isomorphisms.

Probably the most important application of the sharp operator is to extend the classical gradient operator to Riemannian manifolds. If \( g \) is a Riemannian metric on \( M \) and \( f : M \rightarrow  \mathbb{R} \) is a smooth function, the gradient of \( \mathbf{f} \) is the vector field grad \( f = {\left( df\right) }^{\sharp } \) obtained from \( {df} \) by raising an index. Unwinding the definitions, we see that grad \( f \) is characterized by the fact that

\[
d{f}_{p}\left( w\right)  = \left\langle  {\operatorname{grad}{\left. f\right| }_{p}, w}\right\rangle  \;\text{ for all }p \in  M, w \in  {T}_{p}M, \tag{2.14}
\]

and has the local basis expression

\[
\operatorname{grad}f = \left( {{g}^{ij}{E}_{i}f}\right) {E}_{j}.
\]

Thus if \( \left( {E}_{i}\right) \) is an orthonormal frame, then grad \( f \) is the vector field whose components are the same as the components of \( {df} \) ; but in other frames, this will not be the case.

The next proposition shows that the gradient has the same geometric interpretation on a Riemannian manifold as it does in Euclidean space. If \( f \) is a smooth real-valued function on a smooth manifold \( M \) , recall that a point \( p \in  M \) is called a regular point of \( f \) if \( d{f}_{p} \neq  0 \) , and a critical point of \( f \) otherwise; and a level set \( {f}^{-1}\left( c\right) \) is called a regular level set if every point of \( {f}^{-1}\left( c\right) \) is a regular point of \( f \) (see Appendix A). Corollary A. 26 shows that each regular level set is an embedded smooth hypersurface in \( M \) .

Proposition 2.37. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( f \in  {C}^{\infty }\left( M\right) \) , and \( \mathcal{R} \subseteq  M \) is the set of regular points of \( f \) . For each \( c \in  \mathbb{R} \) , the set \( {M}_{c} = {f}^{-1}\left( c\right)  \cap  \mathcal{R} \) , if nonempty, is an embedded smooth hypersurface in \( M \) , and grad \( f \) is everywhere normal to \( {M}_{c} \) .

Proof. Problem 2-9.

The flat and sharp operators can be applied to tensors of any rank, in any index position, to convert tensors from covariant to contravariant or vice versa. Formally, this operation is defined as follows: if \( F \) is any \( \left( {k, l}\right) \) -tensor and \( i \in  \{ 1,\ldots , k + l\} \) is any covariant index position for \( F \) (meaning that the \( i \) th argument is a vector, not a covector), we can form a new tensor \( {F}^{\sharp } \) of type \( \left( {k + 1, l - 1}\right) \) by setting

\[
{F}^{\sharp }\left( {{\alpha }_{1},\ldots ,{\alpha }_{k + l}}\right)  = F\left( {{\alpha }_{1},\ldots ,{\alpha }_{i - 1},{\alpha }_{i}^{\sharp },{\alpha }_{i + 1},\ldots ,{\alpha }_{k + l}}\right)
\]

whenever \( {\alpha }_{1},\ldots ,{\alpha }_{k + 1} \) are vectors or covectors as appropriate. In any local frame, the components of \( {F}^{\sharp } \) are obtained by multiplying the components of \( F \) by \( {g}^{kl} \) and contracting one of the indices of \( {g}^{kl} \) with the \( i \) th index of \( F \) . Similarly, if \( i \) is a contravariant index position, we can define a \( \left( {k - 1, l + 1}\right) \) -tensor \( {F}^{\flat } \) by

\[
{F}^{b}\left( {{\alpha }_{1},\ldots ,{\alpha }_{k + l}}\right)  = F\left( {{\alpha }_{1},\ldots ,{\alpha }_{i - 1},{\alpha }_{i}^{b},{\alpha }_{i + 1},\ldots ,{\alpha }_{k + l}}\right) .
\]

In components, it is computed by multiplying by \( {g}_{kl} \) and contracting.

For example, if \( A \) is a mixed 3-tensor given in terms of a local frame by

\[
A = {A}_{i}{}^{j}{}_{k}{\varepsilon }^{i} \otimes  {E}_{j} \otimes  {\varepsilon }^{k}
\]

(see (B.6)), we can lower its middle index to obtain a covariant 3-tensor \( {A}^{b} \) with components

\[
{A}_{ijk} = {g}_{jl}{A}_{i}{}^{l}{}_{k}.
\]

To avoid overly cumbersome notation, we use the symbols \( {F}^{\sharp } \) and \( {F}^{\flat } \) without explicitly specifying which index position the sharp or flat operator is to be applied to; when there is more than one choice, we will always stipulate in words what is meant.

Another important application of the flat and sharp operators is to extend the trace operator introduced in Appendix B to covariant tensors. If \( h \) is any covariant \( k \) -tensor field on a Riemannian manifold with \( k \geq  2 \) , we can raise one of its indices (say the last one for definiteness) and obtain a \( \left( {1, k - 1}\right) \) -tensor \( {h}^{\sharp } \) . The trace of \( {h}^{\sharp } \) is thus a well-defined covariant \( \left( {k - 2}\right) \) -tensor field (see Exercise B.3). We define the trace of \( h \) with respect to \( g \) as

\[
{\operatorname{tr}}_{g}h = \operatorname{tr}\left( {h}^{\sharp }\right) .
\]

Sometimes we may wish to raise an index other than the last, or to take the trace on a pair of indices other than the last covariant and contravariant ones. In each such case, we will say in words what is meant.

The most important case is that of a covariant 2-tensor field. In this case, \( {h}^{\sharp } \) is a \( \left( {1,1}\right) \) -tensor field, which can equivalently be regarded as an endomorphism field, and \( {\operatorname{tr}}_{g}h \) is just the ordinary trace of this endomorphism field. In terms of a basis, this is

\[
{\operatorname{tr}}_{g}h = {h}_{i}{}^{i} = {g}^{ij}{h}_{ij}
\]

In particular, in an orthonormal frame this is the ordinary trace of the matrix \( \left( {h}_{ij}\right) \) (the sum of its diagonal entries); but if the frame is not orthonormal, then this trace is different from the ordinary trace.

Exercise 2.38. If \( g \) is a Riemannian metric on \( M \) and \( \left( {E}_{i}\right) \) is a local frame on \( M \) , there is a potential ambiguity about what the expression \( \left( {g}^{ij}\right) \) represents: we have defined it to mean the inverse matrix of \( \left( {g}_{ij}\right) \) , but one could also interpret it as the components of the contravariant 2-tensor field \( {g}^{\# \# } \) obtained by raising both of the indices of \( g \) . Show that these two interpretations lead to the same result.

## Inner Products of Tensors

A Riemannian metric yields, by definition, an inner product on tangent vectors at each point. Because of the musical isomorphisms between vectors and covectors, it is easy to carry the inner product over to covectors as well.

Suppose \( g \) is a Riemannian metric on \( M \) , and \( x \in  M \) . We can define an inner product on the cotangent space \( {T}_{x}^{ * }M \) by

\[
\langle \omega ,\eta {\rangle }_{g} = {\left\langle  {\omega }^{\sharp },{\eta }^{\sharp }\right\rangle  }_{g}.
\]

(Just as with inner products of vectors, we might sometimes omit \( g \) from the notation when the metric is understood.) To see how to compute this, we just use the basis formula (2.13) for the sharp operator, together with the relation \( {g}_{kl}{g}^{ki} = {g}_{lk}{g}^{ki} = \; {\delta }_{l}^{i} \) , to obtain

\[
\langle \omega ,\eta \rangle  = {g}_{kl}\left( {{g}^{ki}{\omega }_{i}}\right) \left( {{g}^{lj}{\eta }_{j}}\right)
\]

\[
= {\delta }_{l}^{i}{g}^{lj}{\omega }_{i}{\eta }_{j}
\]

\[
= {g}^{ij}{\omega }_{i}{\eta }_{j}.
\]

In other words, the inner product on covectors is represented by the inverse matrix \( \left( {g}^{ij}\right) \) . Using our conventions for raising and lowering indices, this can also be written

\[
\langle \omega ,\eta \rangle  = {\omega }_{i}{\eta }^{i} = {\omega }^{j}{\eta }_{j}.
\]

- Exercise 2.39. Let \( \left( {M, g}\right) \) be a Riemannian manifold with or without boundary, let \( \left( {E}_{i}\right) \) be a local frame for \( M \) , and let \( \left( {\varepsilon }^{i}\right) \) be its dual coframe. Show that the following are equivalent:

(a) \( \left( {E}_{i}\right) \) is orthonormal.

(b) \( \left( {\varepsilon }^{i}\right) \) is orthonormal.

(c) \( {\left( {\varepsilon }^{i}\right) }^{\sharp } = {E}_{i} \) for each \( i \) .

This construction can be extended to tensor bundles of any rank, as the following proposition shows. First a bit of terminology: if \( E \rightarrow  M \) is a smooth vector bundle, a smooth fiber metric on \( \mathbf{E} \) is an inner product on each fiber \( {E}_{p} \) that varies smoothly, in the sense that for any (local) smooth sections \( \sigma ,\tau \) of \( E \) , the inner product \( \langle \sigma ,\tau \rangle \) is a smooth function.

Proposition 2.40 (Inner Products of Tensors). Let \( \left( {M, g}\right) \) be an \( n \) -dimensional Riemannian manifold with or without boundary. There is a unique smooth fiber metric on each tensor bundle \( {T}^{\left( k, l\right) }{TM} \) with the property that if \( {\alpha }_{1},\ldots ,{\alpha }_{k + l} \) , \( {\beta }_{1},\ldots ,{\beta }_{k + l} \) are vector or covector fields as appropriate, then

\[
\left\langle  {{\alpha }_{1} \otimes  \cdots  \otimes  {\alpha }_{k + l},{\beta }_{1} \otimes  \cdots  \otimes  {\beta }_{k + l}}\right\rangle   = \left\langle  {{\alpha }_{1},{\beta }_{1}}\right\rangle   \cdot  \ldots  \cdot  \left\langle  {{\alpha }_{k + l},{\beta }_{k + l}}\right\rangle  . \tag{2.15}
\]

With this inner product, if \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) is a local orthonormal frame for \( {TM} \) and \( \left( {{\varepsilon }^{1},\ldots ,{\varepsilon }^{n}}\right) \) is the corresponding dual coframe, then the collection of tensor fields \( {E}_{{i}_{1}} \otimes  \cdots  \otimes  {E}_{{i}_{k}} \otimes  {\varepsilon }^{{j}_{1}} \otimes  \cdots  \otimes  {\varepsilon }^{{j}_{l}} \) as all the indices range from 1 to n forms a local orthonormal frame for \( {T}^{\left( k, l\right) }\left( {{T}_{p}M}\right) \) . In terms of any (not necessarily orthonormal) frame, this fiber metric satisfies

\[
\langle F, G\rangle  = {g}_{{i}_{1}{r}_{1}}\cdots {g}_{{i}_{k}{r}_{k}}{g}^{{j}_{1}{s}_{1}}\cdots {g}^{{j}_{l}{s}_{l}}{F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{G}_{{s}_{1}\ldots {s}_{l}}^{{r}_{1}\ldots {r}_{k}}. \tag{2.16}
\]

If \( F \) and \( G \) are both covariant, this can be written

\[
\langle F, G\rangle  = {F}_{{j}_{1}\ldots {j}_{l}}{G}^{{j}_{1}\ldots {j}_{l}},
\]

where the last factor on the right represents the components of \( G \) with all of its indices raised:

\[
{G}^{{j}_{1}\ldots {j}_{l}} = {g}^{{j}_{1}{s}_{1}}\cdots {g}^{{j}_{l}{s}_{l}}{G}_{{s}_{1}\ldots {s}_{l}}.
\]

Proof. Problem 2-11.

## The Volume Form and Integration

Another important construction provided by a metric on an oriented manifold is a canonical volume form.

Proposition 2.41 (The Riemannian Volume Form). Let \( \left( {M, g}\right) \) be an oriented Riemannian n-manifold with or without boundary. There is a unique n-form \( d{V}_{g} \) on \( M \) , called the Riemannian volume form, characterized by any one of the following three equivalent properties:

(a) If \( \left( {{\varepsilon }^{1},\ldots ,{\varepsilon }^{n}}\right) \) is any local oriented orthonormal coframe for \( {T}^{ * }M \) , then

\[
d{V}_{g} = {\varepsilon }^{1} \land  \cdots  \land  {\varepsilon }^{n}.
\]

(b) If \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) is any local oriented orthonormal frame for \( {TM} \) , then

\[
d{V}_{g}\left( {{E}_{1},\ldots ,{E}_{n}}\right)  = 1.
\]

(c) If \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) are any oriented local coordinates, then

\[
d{V}_{g} = \sqrt{\det \left( {g}_{ij}\right) }d{x}^{1} \land  \cdots  \land  d{x}^{n}.
\]

Proof. Problem 2-12.

The significance of the Riemannian volume form is that it allows us to integrate functions on an oriented Riemannian manifold, not just differential forms. If \( f \) is a continuous, compactly supported real-valued function on an oriented Riemannian \( n \) -manifold \( \left( {M, g}\right) \) with or without boundary, then \( {fd}{V}_{g} \) is a compactly supported \( n \) -form. Therefore, the integral \( {\int }_{M}{fd}{V}_{g} \) makes sense, and we define it to be the integral of \( f \) over \( M \) . Similarly, if \( M \) is compact, the volume of \( M \) is defined to be

\[
\operatorname{Vol}\left( M\right)  = {\int }_{M}d{V}_{g} = {\int }_{M}{1d}{V}_{g}.
\]

In particular, if \( D \subseteq  M \) is a regular domain (a closed, embedded codimension-0 submanifold with boundary), we can apply these definitions to \( D \) with its induced metric and thereby make sense of the integral of \( f \) over \( D \) and, in case \( D \) is compact, the volume of \( D \) .

The notation \( d{V}_{g} \) is chosen to emphasize the similarity of the integral \( {\int }_{M}{fd}{V}_{g} \) with the standard integral of a function over an open subset of \( {\mathbb{R}}^{n} \) . It is not meant to imply that \( d{V}_{g} \) is an exact form; in fact, if \( M \) is a compact oriented manifold without boundary, then \( d{V}_{g} \) is never exact, because its integral over \( M \) is positive, and exact forms integrate to zero by Stokes's theorem.

Because there are two conventions in common use for the wedge product (see p. 401), it should be noted that properties (a) and (c) of Proposition 2.41 are the same regardless of which convention is used; but property (b) holds only for the determinant convention that we use. If the Alt convention is used, the number 1 should be replaced by \( 1/n \) ! in that formula.

- Exercise 2.42. Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are oriented Riemannian manifolds, and \( \varphi  : M \rightarrow  \widetilde{M} \) is an orientation-preserving isometry. Prove that \( {\varphi }^{ * }d{V}_{\widetilde{g}} = d{V}_{g} \) .

For Riemannian hypersurfaces, we have the following important characterization of the volume form on the hypersurface in terms of that of the ambient manifold. If \( X \) is a vector field and \( \mu \) is a differential form, recall that \( X \bot  \mu \) denotes interior multiplication of \( \mu \) by \( X \) (see p. 401).

Proposition 2.43. Suppose \( M \) is a hypersurface in an oriented Riemannian manifold \( \left( {\widetilde{M},\widetilde{g}}\right) \) and \( g \) is the induced metric on \( M \) . Then \( M \) is orientable if and only if there exists a global unit normal vector field \( N \) for \( M \) , and in that case the volume form of \( \left( {M, g}\right) \) is given by

\[
{\left. d{V}_{g} = \left( N\lrcorner d{V}_{\widetilde{g}}\right) \right| }_{M}. \tag{2.17}
\]

Proof. Problem 2-13.

When \( M \) is not orientable, we can still define integrals of functions, but now we have to use densities instead of differential forms (see pp. 405-406).

Proposition 2.44 (The Riemannian Density). If \( \left( {M, g}\right) \) is any Riemannian manifold, then there is a unique smooth positive density \( \mu \) on \( M \) , called the Riemannian density, with the property that

\[
\mu \left( {{E}_{1},\ldots ,{E}_{n}}\right)  = 1 \tag{2.18}
\]

for every local orthonormal frame \( \left( {E}_{i}\right) \) .

- Exercise 2.45. Prove this proposition by showing that \( \mu \) can be defined in terms of any local orthonormal frame by

\[
\mu  = \left| {{\varepsilon }^{1} \land  \cdots  \land  {\varepsilon }^{n}}\right| .
\]

Let \( \left( {M, g}\right) \) be a Riemannian manifold (with or without boundary). If \( M \) is oriented and \( d{V}_{g} \) is its Riemannian volume form, then its Riemannian density is easily seen to be equal to \( \left| {d{V}_{g}}\right| \) . On the other hand, the Riemannian density is defined whether \( M \) is oriented or not. It is customary to denote the Riemannian density by the same notation \( d{V}_{g} \) that we use for the Riemannian volume form, and to specify when necessary whether the notation refers to a density or a form. In either case, we can define the integral of a compactly supported smooth function \( f : M \rightarrow  \mathbb{R} \) as \( {\int }_{M}{fd}{V}_{g} \) . This is to be interpreted as the integral of a density when \( M \) is nonorientable; when \( M \) is orientable, it can be interpreted either as the integral of a density or as the integral of an \( n \) -form (with respect to some choice of orientation), because both give the same result.

## The Divergence and the Laplacian

In advanced calculus, you have undoubtedly been introduced to three important differential operators involving vector fields on \( {\mathbb{R}}^{3} \) : the gradient (which takes real-valued functions to vector fields), divergence (vector fields to functions), and curl (vector fields to vector fields). We have already described how the gradient operator can be generalized to Riemannian manifolds (see equation (2.14)); now we can show that the divergence operator also generalizes easily to that setting. Problem 2-27 describes a similar, but more limited, generalization of the curl.

Suppose \( \left( {M, g}\right) \) is an oriented Riemannian \( n \) -manifold with or without boundary, and \( d{V}_{g} \) is its volume form. If \( X \) is a smooth vector field on \( M \) , then \( X \bot  d{V}_{g} \) is an \( \left( {n - 1}\right) \) -form. The exterior derivative of this \( \left( {n - 1}\right) \) -form is a smooth \( n \) -form, so it can be expressed as a smooth function multiplied by \( d{V}_{g} \) . That function is called the divergence of \( X \) , and denoted by div \( X \) ; thus it is characterized by the following formula:

\[
d\left( {X\lrcorner d{V}_{g}}\right)  = \left( {\operatorname{div}X}\right) d{V}_{g}. \tag{2.19}
\]

Even if \( M \) is nonorientable, in a neighborhood of each point we can choose an orientation and define the divergence by (2.19), and then note that reversing the orientation changes the sign of \( d{V}_{g} \) on both sides of the equation, so div \( X \) is well defined, independently of the choice of orientation. In this way, we can define the divergence operator on any Riemannian manifold with or without boundary, by requiring that it satisfy (2.19) for any choice of orientation in a neighborhood of each point.

The most important application of the divergence operator is the divergence theorem, which you will be asked to prove in Problem 2-22.

Using the divergence operator, we can define another important operator, this one acting on real-valued functions. The Laplacian (or Laplace-Beltrami operator) is the linear operator \( \Delta  : {C}^{\infty }\left( M\right)  \rightarrow  {C}^{\infty }\left( M\right) \) defined by

\[
{\Delta u} = \operatorname{div}\left( {\operatorname{grad}u}\right) . \tag{2.20}
\]

(Note that many books, including [LeeSM] and the first edition of this book, define the Laplacian as \( - \operatorname{div}\left( {\operatorname{grad}u}\right) \) . The main reason for choosing the negative sign is so that the operator will have nonnegative eigenvalues; see Problem 2-24. But the definition we give here is much more common in Riemannian geometry.)

The next proposition gives alternative formulas for these operators.

Proposition 2.46. Let \( \left( {M, g}\right) \) be a Riemannian manifold with or without boundary, and let \( \left( {x}^{i}\right) \) be any smooth local coordinates on an open set \( U \subseteq  M \) . The coordinate representations of the divergence and Laplacian are as follows:

\[
\operatorname{div}\left( {{X}^{i}\frac{\partial }{\partial {x}^{i}}}\right)  = \frac{1}{\sqrt{\det g}}\frac{\partial }{\partial {x}^{i}}\left( {{X}^{i}\sqrt{\det g}}\right) ,
\]

\[
{\Delta u} = \frac{1}{\sqrt{\det g}}\frac{\partial }{\partial {x}^{i}}\left( {{g}^{ij}\sqrt{\det g}\frac{\partial u}{\partial {x}^{j}}}\right) ,
\]

where \( \det g = \det \left( {g}_{kl}\right) \) is the determinant of the component matrix of \( g \) in these coordinates. On \( {\mathbb{R}}^{n} \) with the Euclidean metric and standard coordinates, these reduce to

\[
\operatorname{div}\left( {{X}^{i}\frac{\partial }{\partial {x}^{i}}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial {X}^{i}}{\partial {x}^{i}}
\]

\[
{\Delta u} = \mathop{\sum }\limits_{{i = 1}}^{n}\frac{{\partial }^{2}u}{{\left( \partial {x}^{i}\right) }^{2}}
\]

Proof. Problem 2-21.

## Lengths and Distances

Perhaps the most important tool that a Riemannian metric gives us is the ability to measure lengths of curves and distances between points. Throughout this section, \( \left( {M, g}\right) \) denotes a Riemannian manifold with or without boundary.

Without further qualification, a curve in \( M \) always means a parametrized curve, that is, a continuous map \( \gamma  : I \rightarrow  M \) , where \( I \subseteq  \mathbb{R} \) is some interval. Unless otherwise specified, we will not worry about whether the interval is bounded or unbounded, or whether it includes endpoints or not. To say that \( \gamma \) is a smooth curve is to say that it is smooth as a map from the manifold (with boundary) \( I \) to \( M \) . If \( I \) has one or two endpoints and \( M \) has empty boundary, then \( \gamma \) is smooth if and only if it extends to a smooth curve defined on some open interval containing \( I \) . (If \( \partial M \neq  \varnothing \) , then smoothness of \( \gamma \) has to be interpreted as meaning that each coordinate representation of \( \gamma \) has a smooth extension to an open interval.) A curve segment is a curve whose domain is a compact interval.

A smooth curve \( \gamma  : I \rightarrow  M \) has a well-defined velocity \( {\gamma }^{\prime }\left( t\right)  \in  {T}_{\gamma \left( t\right) }M \) for each \( t \in  I \) . We say that \( \gamma \) is a regular curve if \( {\gamma }^{\prime }\left( t\right)  \neq  0 \) for \( t \in  I \) . This implies that \( \gamma \) is an immersion, so its image has no "corners" or "kinks."

We wish to use curve segments as "measuring tapes" to define distances between points in a connected Riemannian manifold. Many aspects of the theory become technically much simpler if we work with a slightly larger class of curve segments instead of just the regular ones. We now describe the appropriate class of curves.

If \( \left\lbrack  {a, b}\right\rbrack   \subseteq  \mathbb{R} \) is a closed bounded interval, a partition of \( \left\lbrack  {a, b}\right\rbrack \) is a finite sequence \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) of real numbers such that \( a = {a}_{0} < {a}_{1} < \cdots  < {a}_{k} = b \) . Each interval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) is called a subinterval of the partition. If \( M \) is a smooth manifold with or without boundary, a (continuous) curve segment \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is said to be piecewise regular if there exists a partition \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) of \( \left\lbrack  {a, b}\right\rbrack \) such that \( {\left. \gamma \right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  } \) is a regular curve segment (meaning it is smooth with nonvanishing velocity) for \( i = 1,\ldots , k \) . For brevity, we refer to a piecewise regular curve segment as an admissible curve, and any partition \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) such that \( {\left. \gamma \right| }_{\left\lbrack  {a}_{i - 1},{a}_{i}\right\rbrack  } \) is smooth for each \( i \) an admissible partition for \( \gamma \) . (There are many admissible partitions for a given admissible curve, because we can always add more points to the partition.) It is also convenient to consider any map \( \gamma  : \{ a\}  \rightarrow  M \) whose domain is a single real number to be an admissible curve.

Suppose \( \gamma \) is an admissible curve and \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) is an admissible partition for it. At each of the intermediate partition points \( {a}_{1},\ldots ,{a}_{k - 1} \) , there are two one-sided velocity vectors, which we denote by

\[
{\gamma }^{\prime }\left( {a}_{i}^{ - }\right)  = \mathop{\lim }\limits_{{t \nearrow  {a}_{i}}}{\gamma }^{\prime }\left( t\right)
\]

\[
{\gamma }^{\prime }\left( {a}_{i}^{ + }\right)  = \mathop{\lim }\limits_{{t \searrow  {a}_{i}}}{\gamma }^{\prime }\left( t\right)
\]

They are both nonzero, but they need not be equal.

If \( \gamma  : I \rightarrow  M \) is a smooth curve, we define a reparametrization of \( \gamma \) to be a curve of the form \( \widetilde{\gamma } = \gamma  \circ  \varphi  : {I}^{\prime } \rightarrow  M \) , where \( {I}^{\prime } \subseteq  \mathbb{R} \) is another interval and \( \varphi  : {I}^{\prime } \rightarrow  I \) is a diffeomorphism. Because intervals are connected, \( \varphi \) is either strictly increasing or strictly decreasing on \( {I}^{\prime } \) . We say that \( \widetilde{\gamma } \) is a forward reparametrization if \( \varphi \) is increasing, and a backward reparametrization if it is decreasing.

For an admissible curve \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) , we define a reparametrization of \( \gamma \) a little more broadly, as a curve of the form \( \widetilde{\gamma } = \gamma  \circ  \varphi \) , where \( \varphi  : \left\lbrack  {c, d}\right\rbrack   \rightarrow  \left\lbrack  {a, b}\right\rbrack \) is a homeomorphism for which there is a partition \( \left( {{c}_{0},\ldots ,{c}_{k}}\right) \) of \( \left\lbrack  {c, d}\right\rbrack \) such that the restriction of \( \varphi \) to each subinterval \( \left\lbrack  {{c}_{i - 1},{c}_{i}}\right\rbrack \) is a diffeomorphism onto its image.

If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is an admissible curve, we define the length of \( \gamma \) to be

\[
{L}_{g}\left( \gamma \right)  = {\int }_{a}^{b}{\left| {\gamma }^{\prime }\left( t\right) \right| }_{g}{dt}
\]

The integrand is bounded and continuous everywhere on \( \left\lbrack  {a, b}\right\rbrack \) except possibly at the finitely many points where \( \gamma \) is not smooth, so this integral is well defined.

Proposition 2.47 (Properties of Lengths). Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with or without boundary, and \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is an admissible curve.

(a) ADDITIVITY OF LENGTH: If \( a < c < b \) , then

\[
{L}_{g}\left( \gamma \right)  = {L}_{g}\left( {\left. \gamma \right| }_{\left\lbrack  a, c\right\rbrack  }\right)  + {L}_{g}\left( {\left. \gamma \right| }_{\left\lbrack  c, b\right\rbrack  }\right) .
\]

(b) PARAMETER INDEPENDENCE: If \( \widetilde{\gamma } \) is a reparametrization of \( \gamma \) , then \( {L}_{g}\left( \gamma \right)  = \; {L}_{g}\left( \widetilde{\gamma }\right) \) .

(c) ISOMETRY INVARIANCE: If \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are Riemannian manifolds (with or without boundary) and \( \varphi  : M \rightarrow  \widetilde{M} \) is a local isometry, then \( {L}_{g}\left( \gamma \right)  = \; {L}_{\widetilde{g}}\left( {\varphi  \circ  \gamma }\right) \) .

- Exercise 2.48. Prove Proposition 2.47.

Suppose \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is an admissible curve. The arc-length function of \( \gamma \) is the function \( s : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) defined by

\[
s\left( t\right)  = {L}_{g}\left( {\left. \gamma \right| }_{\left\lbrack  a, t\right\rbrack  }\right)  = {\int }_{a}^{t}{\left| {\gamma }^{\prime }\left( u\right) \right| }_{g}{du}.
\]

It is continuous everywhere, and it follows from the fundamental theorem of calculus that it is smooth wherever \( \gamma \) is, with derivative \( {s}^{\prime }\left( t\right)  = \left| {{\gamma }^{\prime }\left( t\right) }\right| \) .

For this reason, if \( \gamma  : I \rightarrow  M \) is any smooth curve (not necessarily a curve segment), we define the speed of \( \gamma \) at any time \( t \in  I \) to be the scalar \( \left| {{\gamma }^{\prime }\left( t\right) }\right| \) . We say that \( \gamma \) is a unit-speed curve if \( \left| {{\gamma }^{\prime }\left( t\right) }\right|  = 1 \) for all \( t \) , and a constant-speed curve if \( \left| {{\gamma }^{\prime }\left( t\right) }\right| \) is constant. If \( \gamma \) is a piecewise smooth curve, we say that \( \gamma \) has unit speed if \( \left| {{\gamma }^{\prime }\left( t\right) }\right|  = 1 \) wherever \( \gamma \) is smooth.

If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is a unit-speed admissible curve, then its arc-length function has the simple form \( s\left( t\right)  = t - a \) . If, in addition, its parameter interval is of the form \( \left\lbrack  {0, b}\right\rbrack \) for some \( b > 0 \) , then the arc-length function is \( s\left( t\right)  = t \) . For this reason, a unit-speed admissible curve whose parameter interval is of the form \( \left\lbrack  {0, b}\right\rbrack \) is said to be parametrized by arc length.

Proposition 2.49. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold with or without boundary.

(a) Every regular curve in \( M \) has a unit-speed forward reparametrization.

(b) Every admissible curve in \( M \) has a unique forward reparametrization by arc length.

Proof. Suppose \( \gamma  : I \rightarrow  M \) is a regular curve. Choose an arbitrary \( {t}_{0} \in  I \) , and define \( s : I \rightarrow  \mathbb{R} \) by

\[
s\left( t\right)  = {\int }_{{t}_{0}}^{t}{\left| {\gamma }^{\prime }\left( u\right) \right| }_{g}{du}.
\]

Since \( {s}^{\prime }\left( t\right)  = {\left| {\gamma }^{\prime }\left( t\right) \right| }_{g} > 0 \) , it follows that \( s \) is a strictly increasing local diffeomorphism, and thus maps \( I \) diffeomorphically onto an interval \( {I}^{\prime } \subseteq  \mathbb{R} \) . If we let \( \varphi  = {s}^{-1} : {I}^{\prime } \rightarrow  I \) , then \( \widetilde{\gamma } = \gamma  \circ  \varphi \) is a forward reparametrization of \( \gamma \) , and the chain rule gives

\[
{\left| {\widetilde{\gamma }}^{\prime }\left( t\right) \right| }_{g} = {\left| {\varphi }^{\prime }\left( s\right) {\gamma }^{\prime }\left( \varphi \left( s\right) \right) \right| }_{g} = \frac{1}{{s}^{\prime }\left( {\varphi \left( s\right) }\right) }{\left| {\gamma }^{\prime }\left( \varphi \left( s\right) \right) \right| }_{g} = 1.
\]

Thus \( \widetilde{\gamma } \) is a unit-speed reparametrization of \( \gamma \) .

Now let \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) be an admissible curve. We prove the existence statement in part (b) by induction on the number of smooth segments in an admissible partition. If \( \gamma \) has only one smooth segment, then it is a regular curve segment, and (b) follows by applying (a) in the special case \( I = \left\lbrack  {a, b}\right\rbrack \) and choosing \( {t}_{0} = a \) . Assuming that the result is true for admissible curves with \( k \) smooth segments, suppose \( \gamma \) has an admissible partition \( \left( {{a}_{0},\ldots ,{a}_{k + 1}}\right) \) . The inductive hypothesis gives piecewise regular homeomorphisms \( \varphi  : \left\lbrack  {0, c}\right\rbrack   \rightarrow  \left\lbrack  {a,{a}_{k}}\right\rbrack \) and \( \psi  : \left\lbrack  {0, d}\right\rbrack   \rightarrow  \left\lbrack  {{a}_{k}, b}\right\rbrack \) such that \( \gamma  \circ  \varphi \) is an arc-length reparametrization of \( {\left. \gamma \right| }_{\left\lbrack  a,{a}_{k}\right\rbrack  } \) and \( \gamma  \circ  \psi \) is an arc-length reparametrization of \( {\left. \gamma \right| }_{\left\lbrack  {a}_{k}, b\right\rbrack  } \) . If we define \( \widetilde{\varphi } : \left\lbrack  {0, c + d}\right\rbrack   \rightarrow  \left\lbrack  {a, b}\right\rbrack \) by

\[
\widetilde{\varphi }\left( s\right)  = \left\{  \begin{array}{ll} \varphi \left( s\right) , & s \in  \left\lbrack  {0, c}\right\rbrack  , \\  \psi \left( {s - c}\right) , & s \in  \left\lbrack  {c, c + d}\right\rbrack  , \end{array}\right.
\]

then \( \gamma  \circ  \widetilde{\varphi } \) is a reparametrization of \( \gamma \) by arc length.

To prove uniqueness, suppose that \( \widetilde{\gamma } = \gamma  \circ  \varphi \) and \( \widehat{\gamma } = \gamma  \circ  \psi \) are both forward reparametrizations of \( \gamma \) by arc length. Since both have the same length, it follows that \( \varphi \) and \( \psi \) both have the same parameter domain \( \left\lbrack  {0, c}\right\rbrack \) , and thus both are piecewise regular homeomorphisms from \( \left\lbrack  {0, c}\right\rbrack \) to \( \left\lbrack  {a, b}\right\rbrack \) . If we define \( \eta  = {\varphi }^{-1} \circ  \psi  : \left\lbrack  {0, c}\right\rbrack   \rightarrow  \left\lbrack  {0, c}\right\rbrack \) , then \( \eta \) is a piecewise regular increasing homeomorphism satisfying \( \widehat{\gamma } = \gamma  \circ  \varphi  \circ  \eta  = \widetilde{\gamma } \circ  \eta \) . The fact that both \( \widetilde{\gamma } \) and \( \widehat{\gamma } \) are of unit speed implies the following equality for all \( s \in  \left\lbrack  {0, c}\right\rbrack \) except the finitely many values at which \( \widetilde{\gamma } \) or \( \eta \) is not smooth:

\[
1 = {\left| {\widehat{\gamma }}^{\prime }\left( s\right) \right| }_{g} = {\left| {\widetilde{\gamma }}^{\prime }\left( \eta \left( s\right) \right) {\eta }^{\prime }\left( s\right) \right| }_{g} = {\left| {\widetilde{\gamma }}^{\prime }\left( \eta \left( s\right) \right) \right| }_{g}{\eta }^{\prime }\left( s\right)  = {\eta }^{\prime }\left( s\right) .
\]

Since \( \eta \) is continuous and \( \eta \left( 0\right)  = 0 \) , it follows that \( \eta \left( s\right)  = s \) for all \( s \in  \left\lbrack  {0, c}\right\rbrack \) , and thus \( \widetilde{\gamma } = \widehat{\gamma } \) .

## The Riemannian Distance Function

We are now in a position to introduce one of the most important concepts from classical geometry into the Riemannian setting: distances between points.

Suppose \( \left( {M, g}\right) \) is a connected Riemannian manifold with or without boundary. For each pair of points \( p, q \in  M \) , we define the Riemannian distance from \( p \) to \( \mathbf{q} \) , denoted by \( {d}_{g}\left( {p, q}\right) \) , to be the infimum of the lengths of all admissible curves from \( p \) to \( q \) . The following proposition guarantees that \( {d}_{g}\left( {p, q}\right) \) is a well-defined nonnegative real number for each \( p, q \in  M \) .

Proposition 2.50. If \( M \) is a connected smooth manifold (with or without boundary), then any two points of \( M \) can be joined by an admissible curve.

Proof. Let \( p, q \in  M \) be arbitrary. Since a connected manifold is path-connected, \( p \) and \( q \) can be connected by a continuous path \( c : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) . By compactness, there is a partition of \( \left\lbrack  {a, b}\right\rbrack \) such that \( c\left( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack  \right) \) is contained in a single smooth coordinate ball (or half-ball in case \( \partial M \neq  \varnothing \) ) for each \( i \) . Then we may replace each such curve segment by a straight-line path in coordinates, yielding an admissible curve \( \gamma \) between the same points (Fig. 2.2).

For convenience, if \( \left( {M, g}\right) \) is a disconnected Riemannian manifold, we also let \( {d}_{g}\left( {p, q}\right) \) denote the Riemannian distance from \( p \) to \( q \) , provided that \( p \) and \( q \) lie in the same connected component of \( M \) . (See also Problem 2-30.)

![bo_d7dtff491nqc73eq8m7g_50_521_183_486_305_0.jpg](images/bo_d7dtff491nqc73eq8m7g_50_521_183_486_305_0.jpg)

Fig. 2.2: Any two points can be connected by an admissible curve

Proposition 2.51 (Isometry Invariance of the Riemannian Distance Function). Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are connected Riemannian manifolds with or without boundary, and \( \varphi  : M \rightarrow  M \) is an isometry. Then \( {d}_{\widetilde{g}}\left( {\varphi \left( x\right) ,\varphi \left( y\right) }\right)  = {d}_{g}\left( {x, y}\right) \) for all \( x, y \in  M \) .

- Exercise 2.52. Prove the preceding proposition.

(Note that unlike lengths of curves, Riemannian distances are not necessarily preserved by local isometries; see Problem 2-31.)

We wish to show that the Riemannian distance function turns \( M \) into a metric space, whose metric topology is the same as its original manifold topology. To do so, we need the following lemmas.

Lemma 2.53. Let \( g \) be a Riemannian metric on an open subset \( W \subseteq  {\mathbb{R}}^{n} \) or \( {\mathbb{R}}_{ + }^{n} \) , and let \( \bar{g} \) denote the Euclidean metric on \( W \) . For every compact subset \( K \subseteq  W \) , there are positive constants \( c, C \) such that for all \( x \in  K \) and all \( v \in  {T}_{x}{\mathbb{R}}^{n} \) ,

\[
{\left. c\left| v\right| \right| }_{\bar{g}} \leq  {\left| v\right| }_{g} \leq  {\left. C\left| v\right| \right| }_{\bar{g}}. \tag{2.21}
\]

Proof. Define a continuous function \( F : {TW} \rightarrow  \mathbb{R} \) by \( F\left( {x, v}\right)  = {\left| v\right| }_{g} = {g}_{x}{\left( v, v\right) }^{1/2} \) for \( x \in  W \) and \( v \in  {T}_{x}{\mathbb{R}}^{n} \) . Let \( K \subseteq  W \) be any compact subset, and define \( L \subseteq  T{\mathbb{R}}^{n} \) by

\[
L = \left\{  {\left( {x, v}\right)  \in  T{\mathbb{R}}^{n} : x \in  K,{\left| v\right| }_{\bar{g}} = 1}\right\}  .
\]

Under the canonical identification of \( T{\mathbb{R}}^{n} \) with \( {\mathbb{R}}^{n} \times  {\mathbb{R}}^{n}, L \) is equal to the product set \( K \times  {\mathbb{S}}^{n - 1} \) , which is compact. Since \( F \) is positive on \( L \) , there are positive constants \( c, C \) such that

\[
c \leq  {\left| v\right| }_{g} \leq  C\;\text{ for all }\left( {x, v}\right)  \in  L.
\]

For each \( x \in  K \) and \( v \in  {T}_{x}{\mathbb{R}}^{n} \) with \( v \neq  0 \) , we can write \( v = \lambda \widehat{v} \) , where \( \lambda  = {\left| v\right| }_{\bar{g}} \) and \( \widehat{v} = v/\lambda \) . Then \( \left( {x,\widehat{v}}\right)  \in  L \) , and it follows from the homogeneity of \( {\left| \cdot \right| }_{g} \) that

\[
{\left| v\right| }_{g} = \lambda {\left| \widehat{v}\right| }_{g} \leq  {\lambda C} = C{\left| v\right| }_{\bar{g}}.
\]

The same inequality holds trivially when \( v = 0 \) . Arguing similarly in the other direction, we conclude that (2.21) holds for all \( x \in  K \) and \( v \in  {T}_{x}{\mathbb{R}}^{n} \) .

![bo_d7dtff491nqc73eq8m7g_51_208_186_1092_468_0.jpg](images/bo_d7dtff491nqc73eq8m7g_51_208_186_1092_468_0.jpg)

The next lemma shows how to transfer this result to Riemannian manifolds.

Lemma 2.54. Let \( \left( {M, g}\right) \) be a Riemannian manifold with or without boundary and let \( {d}_{g} \) be its Riemannian distance function. Suppose \( U \) is an open subset of \( M \) and \( p \in  U \) . Then \( p \) has a coordinate neighborhood \( V \subseteq  U \) with the property that there are positive constants \( C, D \) satisfying the following inequalities:

(a) If \( q \in  V \) , then \( {d}_{g}\left( {p, q}\right)  \leq  C{d}_{\bar{g}}\left( {p, q}\right) \) , where \( \bar{g} \) is the Euclidean metric in the given coordinates on \( V \) .

(b) If \( q \in  M \smallsetminus  V \) , then \( {d}_{g}\left( {p, q}\right)  \geq  D \) .

Proof. Let \( W \) be any neighborhood of \( p \) contained in \( U \) on which there exist smooth coordinates \( \left( {x}^{i}\right) \) . Using these coordinates, we can identify \( W \) with an open subset of \( {\mathbb{R}}^{n} \) or \( {\mathbb{R}}_{ + }^{n} \) . Let \( K \) be a compact subset of \( W \) containing a neighborhood \( V \) of \( p \) , chosen as follows: If \( p \) is an interior point of \( M \) , let \( K \) be the closed Euclidean ball \( {\bar{B}}_{\varepsilon }\left( 0\right) \) , with \( \varepsilon  > 0 \) chosen small enough that \( K \subseteq  W \) , and let \( V = {B}_{\varepsilon }\left( 0\right) \) . If \( p \in  \partial M \) , let \( K \) be a closed half-ball \( {\bar{B}}_{\varepsilon }\left( 0\right)  \cap  {\mathbb{R}}_{ + }^{n} \) with \( \varepsilon \) chosen similarly, and let \( V = \; {B}_{\varepsilon }\left( 0\right)  \cap  {\mathbb{R}}_{ + }^{n} \) . Let \( \bar{g} = \mathop{\sum }\limits_{i}{\left( d{x}^{i}\right) }^{2} \) denote the Euclidean metric in these coordinates, and let \( c, C \) be constants satisfying (2.21). If \( \gamma \) is any admissible curve whose image lies entirely in \( V \) , it follows that

\[
c{L}_{\bar{g}}\left( \gamma \right)  \leq  {L}_{g}\left( \gamma \right)  \leq  C{L}_{\bar{g}}\left( \gamma \right) . \tag{2.22}
\]

To prove (a), suppose \( q \in  V \) . Letting \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  V \) be a parametrization of the line segment from \( p \) to \( q \) , we conclude from (2.22) that

\[
{d}_{g}\left( {p, q}\right)  \leq  {L}_{g}\left( \gamma \right)  \leq  C{L}_{\bar{g}}\left( \gamma \right)  = C{d}_{\bar{g}}\left( {p, q}\right) .
\]

To prove (b), suppose \( q \in  M \smallsetminus  V \) . If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) is any admissible curve from \( p \) to \( q \) , let \( {t}_{0} \) denote the infimum of times \( t \in  \left\lbrack  {a, b}\right\rbrack \) such that \( \gamma \left( t\right)  \notin  V \) . It follows that \( \gamma \left( \left\lbrack  {a,{t}_{0}}\right\rbrack  \right)  \subseteq  K \) and \( {d}_{\bar{g}}\left( {p,\gamma \left( {t}_{0}\right) }\right)  = \varepsilon \) by continuity (Fig. 2.3), so (2.22) implies

\[
{L}_{g}\left( \gamma \right)  \geq  {L}_{g}\left( {\left. \gamma \right| }_{\left\lbrack  a,{t}_{0}\right\rbrack  }\right)  \geq  c{L}_{\bar{g}}\left( {\left. \gamma \right| }_{\left\lbrack  a,{t}_{0}\right\rbrack  }\right)  \geq  c{d}_{\bar{g}}\left( {p,\gamma \left( {t}_{0}\right) }\right)  = {c\varepsilon }.
\]

Taking the infimum over all such curves \( \gamma \) , we obtain (b) with \( D = {c\varepsilon } \) .

Theorem 2.55 (Riemannian Manifolds as Metric Spaces). Let \( \left( {M, g}\right) \) be a connected Riemannian manifold with or without boundary. With the distance function \( {d}_{g}, M \) is a metric space whose metric topology is the same as the given manifold topology.

Proof. It is immediate from the definition of \( {d}_{g} \) that \( {d}_{g}\left( {p, q}\right)  = {d}_{g}\left( {q, p}\right)  \geq  0 \) and \( {d}_{g}\left( {p, p}\right)  = 0 \) . On the other hand, suppose \( p, q \in  M \) are distinct. Let \( U \subseteq  M \) be an open set that contains \( p \) but not \( q \) , and choose a coordinate neighborhood \( V \) of \( p \) contained in \( U \) and satisfying the conclusion of Lemma 2.54. Then Lemma 2.54(b) shows that \( {d}_{g}\left( {p, q}\right)  \geq  D > 0 \) .

The triangle inequality follows from the fact that an admissible curve from \( p \) to \( q \) can be combined with one from \( q \) to \( r \) (possibly changing the starting time of the parametrization of the second) to yield one from \( p \) to \( r \) whose length is the sum of the lengths of the two given curves (Fig. 2.4). (This is one reason for defining distance using piecewise regular curves instead of just regular ones.) This completes the proof that \( {d}_{g} \) turns \( M \) into a metric space.

It remains to show that the metric topology is the same as the manifold topology. Suppose first that \( U \subseteq  M \) is open in the manifold topology. For each \( p \in  U \) , we can choose a coordinate neighborhood \( V \) of \( p \) contained in \( U \) with positive constants \( C, D \) satisfying the conclusions of Lemma 2.54. The contrapositive of part (b) of that lemma says \( {d}_{g}\left( {p, q}\right)  < D \Rightarrow  q \in  V \subseteq  U \) , which means that the metric ball of radius \( D \) is contained in \( U \) . Thus \( U \) is open in the metric topology induced by \( {d}_{g} \) .

On the other hand, suppose \( {U}^{\prime } \) is open in the metric topology. Given \( p \in  {U}^{\prime } \) , choose \( \delta  > 0 \) such that the \( {d}_{g} \) -metric ball of radius \( \delta \) around \( p \) is contained in \( {U}^{\prime } \) . Let \( V \) be any neighborhood of \( p \) that is open in the manifold topology and satisfies the conclusions of Lemma 2.54, with corresponding constants \( C, D \) . (We are not claiming that \( V \subseteq  {U}^{\prime } \) .) Choose \( \varepsilon \) small enough that \( {C\varepsilon } < \delta \) . Lemma 2.54(a) shows that if \( q \) is a point of \( V \) such that \( {d}_{\bar{g}}\left( {p, q}\right)  < \varepsilon \) , then \( {d}_{g}\left( {p, q}\right)  \leq  {C\varepsilon } < \delta \) , and thus \( q \) lies in the metric ball of radius \( \delta \) about \( p \) , and hence in \( {U}^{\prime } \) . Since the set \( \{ q \in \; V : {d}_{\bar{g}}\left( {p, q}\right)  < \varepsilon \} \) is open in the given manifold topology, this shows that \( {U}^{\prime } \) is also open in the manifold topology.

Thanks to the preceding theorem, it makes sense to apply all the concepts of the theory of metric spaces to a connected Riemannian manifold \( \left( {M, g}\right) \) . For example, we say that \( M \) is (metrically) complete if every Cauchy sequence in \( M \) converges. A subset \( A \subseteq  M \) is bounded if there is a constant \( C \) such that \( {d}_{g}\left( {p, q}\right)  \leq  C \) for all \( p, q \in  A \) ; if this is the case, the diameter of \( \mathbf{A} \) is the smallest such constant:

\[
\operatorname{diam}\left( A\right)  = \sup \left\{  {{d}_{g}\left( {p, q}\right)  : p, q \in  A}\right\}  .
\]

Since every compact metric space is bounded, every compact connected Riemannian manifold with or without boundary has finite diameter. (Note that the unit sphere with the Riemannian distance determined by the round metric has diameter \( \pi \) , not 2, since the Riemannian distance between antipodal points is \( \pi \) . See Problem 6-2.)

## Pseudo-Riemannian Metrics

From the point of view of geometry, Riemannian metrics are by far the most important structures that manifolds carry. However, there is a generalization of Riemannian metrics that has become especially important because of its application to physics.

Before defining this generalization, we begin with some linear-algebraic preliminaries. Suppose \( V \) is a finite-dimensional vector space, and \( q \) is a symmetric covariant 2-tensor on \( V \) (also called a symmetric bilinear form). Just as for an inner product, there is a linear map \( \widehat{q} : V \rightarrow  {V}^{ * } \) defined by

\[
\widehat{q}\left( v\right) \left( w\right)  = q\left( {v, w}\right) \text{ for all }v, w \in  V.
\]

We say that \( q \) is nondegenerate if \( \widehat{q} \) is an isomorphism.

Lemma 2.56. Suppose \( q \) is a symmetric covariant 2-tensor on a finite-dimensional vector space \( V \) . The following are equivalent:

(a) \( q \) is nondegenerate.

(b) For every nonzero \( v \in  V \) , there is some \( w \in  V \) such that \( q\left( {v, w}\right)  \neq  0 \) .

(c) If \( q = {q}_{ij}{\varepsilon }^{i}{\varepsilon }^{j} \) in terms of some basis \( \left( {\varepsilon }^{j}\right) \) for \( {V}^{ * } \) , then the matrix \( \left( {q}_{ij}\right) \) is invertible.

Exercise 2.57. Prove the preceding lemma.

Every inner product is a nondegenerate symmetric bilinear form, as is every symmetric bilinear form that is negative definite (which is defined by obvious analogy with positive definite). But there are others that are neither positive definite nor negative definite, as we will see below.

We use the term scalar product to denote any nondegenerate symmetric bilinear form on a finite-dimensional vector space \( V \) , and reserve the term inner product for the special case of a positive definite scalar product. A scalar product space is a finite-dimensional vector space endowed with a scalar product. When convenient, we will often use a notation like \( \langle  \cdot  , \cdot  \rangle \) to denote a scalar product. We say that vectors \( v, w \in  V \) are orthogonal if \( \langle v, w\rangle  = 0 \) , just as in the case of an inner product. Given a vector \( v \in  V \) , we define the norm of \( v \) to be \( \left| v\right|  = {\left| \langle v, v\rangle \right| }^{1/2} \) . Note that in the indefinite case, it is possible for a nonzero vector to be orthogonal to itself, and thus to have norm zero. Thus \( \left| v\right| \) is not technically a norm in the sense defined on page 47 below, but it is customary to call it "the norm of \( v \) " anyway.

Exercise 2.58. Prove that the polarization identity (2.2) holds for every scalar product.

If \( S \subseteq  V \) is any linear subspace, the set of vectors in \( V \) that are orthogonal to every vector in \( S \) is a linear subspace denoted by \( {S}^{ \bot  } \) .

Lemma 2.59. Suppose \( \left( {V, q}\right) \) is a finite-dimensional scalar product space, and \( S \subseteq \; V \) is a linear subspace.

(a) \( \dim S + \dim {S}^{ \bot  } = \dim V \) .

(b) \( {\left( {S}^{ \bot  }\right) }^{ \bot  } = S \) .

Proof. Define a linear map \( \Phi  : V \rightarrow  {S}^{ * } \) by \( \Phi \left( v\right)  = {\left. \widehat{q}\left( v\right) \right| }_{S} \) . Note that \( v \in  \operatorname{Ker}\Phi \) if and only if \( q\left( {v, x}\right)  = \widehat{q}\left( v\right) \left( x\right)  = 0 \) for all \( x \in  S \) , so \( \operatorname{Ker}\Phi  = {S}^{ \bot  } \) . If \( \varphi  \in  {S}^{ * } \) is arbitrary, there is a covector \( \widetilde{\varphi } \in  {V}^{ * } \) whose restriction to \( S \) is equal to \( \varphi \) . (For example, such a covector is easily constructed after choosing a basis for \( S \) and extending it to a basis for \( V \) .) Since \( \widehat{q} \) is an isomorphism, there exists \( v \in  V \) such that \( \widehat{q}\left( v\right)  = \widetilde{\varphi } \) . It follows that \( \Phi \left( v\right)  = \varphi \) , and therefore \( \Phi \) is surjective. By the rank-nullity theorem, the dimension of \( {S}^{ \bot  } = \operatorname{Ker}\Phi \) is equal to \( \dim V - \dim {S}^{ * } = \dim V - \dim S \) . This proves (a).

To prove (b), note that every \( v \in  S \) is orthogonal to every element of \( {S}^{ \bot  } \) by definition, so \( S \subseteq  {\left( {S}^{ \bot  }\right) }^{ \bot  } \) . Because these finite-dimensional vector spaces have the same dimension by part (a), they are equal.

An ordered \( k \) -tuple \( \left( {{v}_{1},\ldots ,{v}_{k}}\right) \) of elements of \( V \) is said to be orthonormal if \( \left| {v}_{i}\right|  = 1 \) for each \( i \) and \( \left\langle  {{v}_{i},{v}_{j}}\right\rangle   = 0 \) for \( i \neq  j \) , or equivalently, if \( \left\langle  {{v}_{i},{v}_{j}}\right\rangle   =  \pm  {\delta }_{ij} \) for each \( i \) and \( j \) . We wish to prove that every scalar product space has an orthonormal basis. Note that the usual Gram-Schmidt algorithm does not always work in this situation, because the vectors that appear in the denominators in (2.5)-(2.6) might have vanishing norms. In order to get around this problem, we introduce the following definitions. If \( \left( {V, q}\right) \) is a finite-dimensional scalar product space, a subspace \( S \subseteq  V \) is said to be nondegenerate if the restriction of \( q \) to \( S \times  S \) is nondegenerate. An ordered \( k \) -tuple of vectors \( \left( {{v}_{1},\ldots ,{v}_{k}}\right) \) in \( V \) is said to be nondegenerate if for each \( j = 1,\ldots , k \) , the vectors \( \left( {{v}_{1},\ldots ,{v}_{j}}\right) \) span a nondegenerate \( j \) -dimensional subspace of \( V \) . For example, every orthonormal basis is nondegenerate.

Lemma 2.60. Suppose \( \left( {V, q}\right) \) is a finite-dimensional scalar product space, and \( S \subseteq \; V \) is a linear subspace. The following are equivalent:

(a) \( S \) is nondegenerate.

(b) \( {S}^{ \bot  } \) is nondegenerate.

(c) \( S \cap  {S}^{ \bot  } = \{ 0\} \) .

(d) \( V = S \oplus  {S}^{ \bot  } \) .

- Exercise 2.61. Prove the preceding lemma.

Lemma 2.62 (Completion of Nondegenerate Bases). Suppose \( \left( {V, q}\right) \) is an \( n \) - dimensional scalar product space, and \( \left( {{v}_{1},\ldots ,{v}_{k}}\right) \) is a nondegenerate \( k \) -tuple in \( V \) with \( 0 \leq  k < n \) . Then there exist vectors \( {v}_{k + 1},\ldots ,{v}_{n} \in  V \) such that \( \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) is a nondegenerate basis for \( V \) .

Proof. Let \( S = \operatorname{span}\left( {{v}_{1},\ldots ,{v}_{k}}\right)  \subseteq  V \) . Because \( k < n,{S}^{ \bot  } \) is a nontrivial subspace of \( V \) , and Lemma 2.60 shows that \( {S}^{ \bot  } \) is nondegenerate and \( V = S \oplus  {S}^{ \bot  } \) . By the nondegeneracy of \( {S}^{ \bot  } \) , there must be a vector in \( {S}^{ \bot  } \) with nonzero length, because otherwise the polarization identity would imply that all inner products of pairs of elements of \( S \) would be zero. If \( {v}_{k + 1} \in  {S}^{ \bot  } \) is any vector with nonzero length, then \( \left( {{v}_{1},\ldots ,{v}_{k + 1}}\right) \) is easily seen to be a nondegenerate \( \left( {k + 1}\right) \) -tuple. Repeating this argument for \( {v}_{k + 2},\ldots ,{v}_{n} \) completes the proof.

Proposition 2.63 (Gram-Schmidt Algorithm for Scalar Products). Suppose \( \left( {V, q}\right) \) is an \( n \) -dimensional scalar product space. If \( \left( {v}_{i}\right) \) is a nondegenerate basis for \( V \) , then there is an orthonormal basis \( \left( {b}_{i}\right) \) with the property that \( \operatorname{span}\left( {{b}_{1},\ldots ,{b}_{k}}\right)  = \; \operatorname{span}\left( {{v}_{1},\ldots ,{v}_{k}}\right) \) for each \( k = 1,\ldots , n \) .

Proof. As in the positive definite case, the basis \( \left( {b}_{i}\right) \) is constructed recursively, starting with \( {b}_{1} = {v}_{1}/\left| {v}_{1}\right| \) and noting that the assumption that \( {v}_{1} \) spans a nondegenerate subspace ensures that \( \left| {v}_{1}\right|  \neq  0 \) . At the inductive step, assuming we have constructed \( \left( {{b}_{1},\ldots ,{b}_{k}}\right) \) , we first set

\[
z = {v}_{k + 1} - \mathop{\sum }\limits_{{i = 1}}^{k}\frac{\left\langle  {v}_{k + 1},{b}_{i}\right\rangle  }{\left\langle  {b}_{i},{b}_{i}\right\rangle  }{b}_{i}.
\]

Each denominator \( \left\langle  {{b}_{i},{b}_{i}}\right\rangle \) is equal to \( \pm  1 \) , so this defines \( z \) as a nonzero element of \( V \) orthogonal to \( {b}_{1},\ldots ,{b}_{k} \) , and with the property that \( \operatorname{span}\left( {{b}_{1},\ldots ,{b}_{k}, z}\right)  = \; \operatorname{span}\left( {{v}_{1},\ldots ,{v}_{k + 1}}\right) \) . If \( \langle z, z\rangle  = 0 \) , then \( z \) is orthogonal to \( \operatorname{span}\left( {{v}_{1},\ldots ,{v}_{k + 1}}\right) \) , contradicting the nondegeneracy assumption. Thus we can complete the inductive step by putting \( {b}_{k + 1} = z/\left| z\right| \) .

Corollary 2.64. Suppose \( \left( {V, q}\right) \) is an \( n \) -dimensional scalar product space. There is a basis \( \left( {\beta }^{i}\right) \) for \( {V}^{ * } \) with respect to which \( q \) has the expression

\[
q = {\left( {\beta }^{1}\right) }^{2} + \cdots  + {\left( {\beta }^{r}\right) }^{2} - {\left( {\beta }^{r + 1}\right) }^{2} - \cdots  - {\left( {\beta }^{r + s}\right) }^{2}, \tag{2.23}
\]

for some nonnegative integers \( r, s \) with \( r + s = n \) .

Proof. Let \( \left( {b}_{i}\right) \) be an orthonormal basis for \( V \) , and let \( \left( {\beta }^{i}\right) \) be the dual basis for \( {V}^{ * } \) . A computation shows that \( q \) has a basis expression of the form (2.23), but perhaps with the positive and negative terms in a different order. Reordering the basis so that the positive terms come first, we obtain (2.23).

It turns out that the numbers \( r \) and \( s \) in (2.23) are independent of the choice of basis. The key to proving this is the following classical result from linear algebra.

Proposition 2.65 (Sylvester's Law of Inertia). Suppose \( \left( {V, q}\right) \) is a finite-dimensional scalar product space. If \( q \) has the representation (2.23) in some basis, then the number \( r \) is the maximum dimension among all subspaces on which the restriction of \( q \) is positive definite, and thus \( r \) and \( s \) are independent of the choice of basis.

Proof. Problem 2-33.

The integer \( s \) in the expression (2.23) (the number of negative terms) is called the index of \( q \) , and the ordered pair \( \left( {r, s}\right) \) is called the signature of \( q \) .

Now suppose \( M \) is a smooth manifold. A pseudo-Riemannian metric on \( M \) (called by some authors a semi-Riemannian metric) is a smooth symmetric 2-tensor field \( g \) that is nondegenerate at each point of \( M \) , and with the same signature everywhere. Every Riemannian metric is also a pseudo-Riemannian metric.

Proposition 2.66 (Orthonormal Frames for Pseudo-Riemannian Manifolds). Let \( \left( {M, g}\right) \) be a pseudo-Riemannian manifold. For each \( p \in  M \) , there exists a smooth orthonormal frame on a neighborhood of \( p \) in \( M \) .

Exercise 2.67. Prove the preceding proposition.

Exercise 2.68. Suppose \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are pseudo-Riemannian manifolds of signatures \( \left( {{r}_{1},{s}_{1}}\right) \) and \( \left( {{r}_{2},{s}_{2}}\right) \) , respectively. Show that \( \left( {{M}_{1} \times  {M}_{2},{g}_{1} \oplus  {g}_{2}}\right) \) is a pseudo-Riemannian manifold of signature \( \left( {{r}_{1} + {r}_{2},{s}_{1} + {s}_{2}}\right) \) .

For nonnegative integers \( r \) and \( s \) , we define the pseudo-Euclidean space of signature \( \left( {r, s}\right) \) , denoted by \( {\mathbb{R}}^{r, s} \) , to be the manifold \( {\mathbb{R}}^{r + s} \) , with standard coordinates denoted by \( \left( {{\xi }^{1},\ldots ,{\xi }^{r},{\tau }^{1},\ldots ,{\tau }^{s}}\right) \) , and with the pseudo-Riemannian metric \( {\bar{q}}^{\left( r, s\right) } \) defined by

\[
{\bar{q}}^{\left( r, s\right) } = {\left( d{\xi }^{1}\right) }^{2} + \cdots  + {\left( d{\xi }^{r}\right) }^{2} - {\left( d{\tau }^{1}\right) }^{2} - \cdots  - {\left( d{\tau }^{s}\right) }^{2}. \tag{2.24}
\]

By far the most important pseudo-Riemannian metrics (other than the Riemannian ones) are the Lorentz metrics, which are pseudo-Riemannian metrics of index 1, and thus signature \( \left( {r,1}\right) \) . (Some authors, especially in the physics literature, prefer to use signature \( \left( {1, r}\right) \) ; either one can be converted to the other by multiplying the metric by -1 , so there is no significant difference.)

The pseudo-Euclidean metric \( {\bar{q}}^{\left( r,1\right) } \) is a Lorentz metric called the Minkowski metric, and the Lorentz manifold \( {\mathbb{R}}^{r,1} \) is called \( \left( {\mathbf{r} + \mathbf{1}}\right) \) -dimensional Minkowski space. If we denote standard coordinates on \( {\mathbb{R}}^{r,1} \) by \( \left( {{\xi }^{1},\ldots ,{\xi }^{r},\tau }\right) \) , then the Min-kowski metric is given by

\[
{\bar{q}}^{\left( r,1\right) } = {\left( d{\xi }^{1}\right) }^{2} + \cdots  + {\left( d{\xi }^{r}\right) }^{2} - {\left( d\tau \right) }^{2}. \tag{2.25}
\]

In the special case of \( {\mathbb{R}}^{3,1} \) , the Minkowski metric is the fundamental invariant of Albert Einstein's special theory of relativity, which can be expressed succinctly by saying that if gravity is ignored, then spacetime is accurately modeled by \( \left( {3 + 1}\right) \) - dimensional Minkowski space, and the laws of physics have the same form in every coordinate system in which the Minkowski metric has the expression (2.25). The differing physical characteristics of "space" (the \( {\xi }^{i} \) directions) and "time" (the \( \tau \) direction) arise from the fact that they are subspaces on which the metric is positive definite and negative definite, respectively. The general theory of relativity includes gravitational effects by allowing the Lorentz metric to vary from point to point.

Many, but not all, results from the theory of Riemannian metrics apply equally well to pseudo-Riemannian metrics. Throughout this book, we will attempt to point out which results carry over directly to pseudo-Riemannian metrics, which ones can be adapted with minor modifications, and which ones do not carry over at all. As a rule of thumb, proofs that depend only on the nondegeneracy of the metric tensor, such as properties of the musical isomorphisms and existence and uniqueness of geodesics, work fine in the pseudo-Riemannian setting, while proofs that use positivity in an essential way, such as those involving lengths of curves, do not.

One notable result that does not carry over to the pseudo-Riemannian case is Proposition 2.4, about the existence of metrics. For example, the following result characterizes those manifolds that admit Lorentz metrics.

Theorem 2.69. A smooth manifold \( M \) admits a Lorentz metric if and only if it admits a rank-1 tangent distribution (i.e., a rank-1 subbundle of TM).

Proof. Problem 2-34.

With some more sophisticated tools from algebraic topology, it can be shown that every noncompact connected smooth manifold admits a Lorentz metric, and a compact connected smooth manifold admits a Lorentz metric if and only if its Euler characteristic is zero (see [O'N83, p. 149]). It follows that no even-dimensional sphere admits a Lorentz metric, because \( {\mathbb{S}}^{2n} \) has Euler characteristic equal to 2 .

For a thorough treatment of pseudo-Riemannian metrics from a mathematical point of view, see the excellent book [O'N83]; a more physical treatment can be found in [HE73].

## Pseudo-Riemannian Submanifolds

The theory of submanifolds is only slightly more complicated in the pseudo-Riemannian case. If \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a pseudo-Riemannian manifold, a smooth submani-fold \( \iota  : M \hookrightarrow  \widetilde{M} \) is called a pseudo-Riemannian submanifold of \( \widetilde{\mathbf{M}} \) if \( {\iota }^{ * }\widetilde{g} \) is nondegenerate with constant signature. If this is the case, we always consider \( M \) to be endowed with the induced pseudo-Riemannian metric \( {\iota }^{ * }\widetilde{g} \) . In the special case in which \( {\iota }^{ * }\widetilde{g} \) is positive definite, \( M \) is called a Riemannian submanifold.

The nondegeneracy hypothesis is not automatically satisfied: for example, if \( M \subseteq  {\mathbb{R}}^{1,1} \) is the submanifold \( \{ \left( {\xi ,\tau }\right)  : \xi  = \tau \} \) and \( \iota  : M \rightarrow  {\mathbb{R}}^{1,1} \) is inclusion, then the pullback tensor \( {\iota }^{ * }{\bar{q}}^{\left( 1,1\right) } \) is identically zero on \( M \) .

For hypersurfaces (submanifolds of codimension 1), the nondegeneracy condition is easy to check. If \( M \subseteq  \widetilde{M} \) is a smooth submanifold and \( p \in  M \) , then a vector \( v \in  {T}_{p}\widetilde{M} \) is said to be normal to \( M \) if \( \langle v, x\rangle  = 0 \) for all \( x \in  {T}_{p}M \) , just as in the Riemannian case. The space of all normal vectors at \( p \) is a subspace of \( {T}_{p}\widetilde{M} \) denoted by \( {N}_{p}M \) .

Proposition 2.70. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a pseudo-Riemannian manifold of signature \( \left( {r, s}\right) \) . Let \( M \) be a smooth hypersurface in \( \widetilde{M} \) , and let \( \iota  : M \hookrightarrow  \widetilde{M} \) be the inclusion map. Then the pullback tensor field \( {\iota }^{ * }\widetilde{g} \) is nondegenerate if and only if \( \widetilde{g}\left( {v, v}\right)  \neq  0 \) for every \( p \in  M \) and every nonzero normal vector \( v \in  {N}_{p}M \) . If \( \widetilde{g}\left( {v, v}\right)  > 0 \) for every nonzero normal vector to \( M \) , then \( M \) is a pseudo-Riemannian submanifold of signature \( \left( {r - 1, s}\right) \) ; and if \( \widetilde{g}\left( {v, v}\right)  < 0 \) for every such vector, then \( M \) is a pseudo-Riemannian submanifold of signature \( \left( {r, s - 1}\right) \) .

Proof. Given \( p \in  M \) , Lemma 2.60 shows that \( {T}_{p}M \) is a nondegenerate subspace of \( {T}_{p}\widetilde{M} \) if and only if the one-dimensional subspace \( {\left( {T}_{p}M\right) }^{ \bot  } = {N}_{p}M \) is nondegenerate, which is the case if and only if every nonzero \( v \in  {N}_{p}M \) satisfies \( \widetilde{g}\left( {v, v}\right)  \neq  0 \) .

Now suppose \( \widetilde{g}\left( {v, v}\right)  > 0 \) for every nonzero normal vector \( v \) . Let \( p \in  M \) be arbitrary, and let \( v \) be a nonzero element of \( {N}_{p}M \) . Writing \( n = \dim \widetilde{M} \) , we can complete \( v \) to a nondegenerate basis \( \left( {v,{w}_{2},\ldots ,{w}_{n}}\right) \) for \( {T}_{p}\widetilde{M} \) by Lemma 2.62, and then use the Gram-Schmidt algorithm to find an orthonormal basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( {T}_{p}\widetilde{M} \) such that \( \operatorname{span}\left( {b}_{1}\right)  = {N}_{p}M \) . It follows that \( \operatorname{span}\left( {{b}_{2},\ldots ,{b}_{n}}\right)  = {T}_{p}M \) . If \( \left( {\beta }^{j}\right) \) is the dual basis to \( \left( {b}_{i}\right) \) , then \( {\widetilde{g}}_{p} \) has a basis representation of the form \( {\left( {\beta }^{1}\right) }^{2} \pm \; {\left( {\beta }^{2}\right) }^{2} \pm  \cdots  \pm  {\left( {\beta }^{n}\right) }^{2} \) , with a total of \( r \) positive terms and \( s \) negative ones, and with a positive sign on the first term \( {\left( {\beta }^{1}\right) }^{2} \) . Therefore, \( {\iota }^{ * }{\widetilde{g}}_{p} =  \pm  {\left( {\beta }^{2}\right) }^{2} \pm  \cdots  \pm  {\left( {\beta }^{n}\right) }^{2} \) has signature \( \left( {r - 1, s}\right) \) . The argument for the case \( \widetilde{g}\left( {v, v}\right)  < 0 \) is similar.

If \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a pseudo-Riemannian manifold and \( f \in  {C}^{\infty }\left( M\right) \) , then the gradient of \( \mathbf{f} \) is defined as the smooth vector field grad \( f = {\left( df\right) }^{\sharp } \) just as in the Riemannian case.

Corollary 2.71. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a pseudo-Riemannian manifold of signature \( \left( {r, s}\right) , f \in  {C}^{\infty }\left( \widetilde{M}\right) \) , and \( M = {f}^{-1}\left( c\right) \) for some \( c \in  \mathbb{R} \) . If \( \widetilde{g}\left( {\operatorname{grad}f,\operatorname{grad}f}\right)  > 0 \) everywhere on \( M \) , then \( M \) is an embedded pseudo-Riemannian submanifold of \( \widetilde{M} \) of signature \( \left( {r - 1, s}\right) \) ; and if \( \widetilde{g}\left( {\operatorname{grad}f,\operatorname{grad}f}\right)  < 0 \) everywhere on \( M \) , then \( M \) is an embedded pseudo-Riemannian submanifold of \( \widetilde{M} \) of signature \( \left( {r, s - 1}\right) \) . In either case, grad \( f \) is everywhere normal to \( M \) .

Proof. Problem 2-35.

Proposition 2.72 (Pseudo-Riemannian Adapted Orthonormal Frames). Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a pseudo-Riemannian manifold, and \( M \subseteq  \widetilde{M} \) is an embedded pseudo-Riemannian or Riemannian submanifold. For each \( p \in  M \) , there exists a smooth orthonormal frame on a neighborhood of \( p \) in \( \widetilde{M} \) that is adapted to \( M \) .

Proof. Write \( m = \dim \widetilde{M} \) and \( n = \dim M \) , and let \( p \in  M \) be arbitrary. Proposition 2.66 shows that there is a smooth orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) for \( M \) on some neighborhood of \( p \) in \( M \) . Then by Lemma 2.62, we can find vectors \( {v}_{n + 1},\ldots ,{v}_{m} \in  {T}_{p}\widetilde{M} \) such that \( \left( {{\left. {E}_{1}\right| }_{p},\ldots ,{\left. {E}_{n}\right| }_{p},{v}_{n + 1},\ldots ,{v}_{m}}\right) \) is a nondegenerate basis for \( {T}_{p}\widetilde{M} \) . Now extend \( {v}_{n + 1},\ldots ,{v}_{m} \) arbitrarily to smooth vector fields \( {V}_{n + 1},\ldots ,{V}_{m} \) on a neighborhood of \( p \) in \( \widetilde{M} \) . By continuity, the ordered \( m \) -tuple \( \left( {{E}_{1},\ldots ,{E}_{n},{V}_{n + 1},\ldots ,{V}_{m}}\right) \) will be a nondegenerate frame for \( \widetilde{M} \) in some (possibly smaller) neighborhood of \( p \) . Applying the Gram-Schmidt algorithm (Prop. 2.63) to this local frame yields a smooth local orthonormal frame \( \left( {{E}_{1},\ldots ,{E}_{m}}\right) \) for \( \widetilde{M} \) with the property that \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) restricts to a local orthonormal frame for \( M \) .

The next corollary is proved in the same way as Proposition 2.16.

Corollary 2.73 (Normal Bundle to a Pseudo-Riemannian Submanifold). Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a pseudo-Riemannian manifold, and \( M \subseteq  \widetilde{M} \) is an embedded pseudo-Riemannian or Riemannian submanifold. The set of vectors normal to \( M \) is a smooth vector subbundle of \( {\left. T\widetilde{M}\right| }_{M} \) , called the normal bundle to \( M \) .

## Other Generalizations of Riemannian Metrics

Pseudo-Riemannian metrics are obtained by relaxing the positivity requirement for Riemannian metrics. In addition, there are other useful generalizations that result when we relax other requirements. In this section we touch briefly on two of those generalizations. We will not treat these anywhere else in the book, but it is useful to know the definitions.

## Sub-Riemannian Metrics

The first generalization arises when we relax the requirement that the metric be defined on the whole tangent space.

A sub-Riemannian metric (also sometimes known as a singular Riemannian metric or Carnot-Carathéodory metric) on a smooth manifold \( M \) is a smooth fiber metric on a smooth tangent distribution \( S \subseteq  {TM} \) (i.e., a vector subbundle of \( {TM} \) ). Since lengths make sense only for vectors in \( S \) , the only curves whose lengths can be measured are those whose velocity vectors lie everywhere in \( S \) . Therefore, one usually imposes some condition on \( S \) that guarantees that any two nearby points can be connected by such a curve. This is, in a sense, the opposite of the Frobenius integrability condition, which would restrict every such curve to lie in a single leaf of a foliation.

Sub-Riemannian metrics arise naturally in the study of the abstract models of real submanifolds of complex space \( {\mathbb{C}}^{n} \) , called CR manifolds (short for Cauchy-Riemann manifolds). CR manifolds are real manifolds endowed with a tangent distribution \( S \subseteq  {TM} \) whose fibers carry the structure of complex vector spaces (with an additional integrability condition that need not concern us here). In the model case of a submanifold \( M \subseteq  {\mathbb{C}}^{n}, S \) is the set of vectors tangent to \( M \) that remain tangent after multiplication by \( i = \sqrt{-1} \) in the ambient complex coordinates. If \( S \) is sufficiently far from being integrable, choosing a fiber metric on \( S \) results in a sub-Riemannian metric whose geometric properties closely reflect the complex-analytic properties of \( M \) as a subset of \( {\mathbb{C}}^{n} \) .

Another motivation for studying sub-Riemannian metrics arises from control theory. In this subject, one is given a manifold with a vector field depending on parameters called controls, with the goal being to vary the controls so as to obtain a solution curve with desired properties, often one that minimizes some function such as arc length. If the vector field is constrained to be everywhere tangent to a distribution \( S \) on the manifold (for example, in the case of a robot arm whose motion is restricted by the orientations of its hinges), then the function can often be modeled as a sub-Riemannian metric and optimal solutions modeled as sub-Riemannian geodesics.

A useful introduction to the geometry of sub-Riemannian metrics is provided in the article [Str86].

## Finsler Metrics

Another important generalization arises from relaxing the requirement that norms of vectors be defined in terms of an inner product on each tangent space.

In general, a norm on a vector space \( V \) is a real-valued function on \( V \) , usually written \( v \mapsto  \left| v\right| \) , that satisfies

(i) HOMOGENEITY: \( \left| {cv}\right|  = \left| c\right| \left| v\right| \) for \( v \in  V \) and \( c \in  \mathbb{R} \) ;

(ii) POSITIVITY: \( \left| v\right|  \geq  0 \) for \( v \in  V \) , with equality if and only if \( v = 0 \) ;

(iii) TRIANGLE INEQUALITY: \( \left| {v + w}\right|  \leq  \left| v\right|  + \left| w\right| \) for \( v, w \in  V \) .

For example, the length function associated with an inner product is a norm.

Now suppose \( M \) is a smooth manifold. A Finsler metric on \( M \) is a continuous function \( F : {TM} \rightarrow  \mathbb{R} \) , smooth on the set of nonzero vectors, whose restriction to each tangent space \( {T}_{p}M \) is a norm. Again, the norm function associated with a Riemannian metric is a special case.

The inventor of Riemannian geometry himself, Bernhard Riemann, clearly envisaged an important role in \( n \) -dimensional geometry for what we now call Finsler metrics; he restricted his investigations to the "Riemannian" case purely for simplicity (see [Spi79, Vol. 2]). However, it was not until the late twentieth century that Finsler metrics began to be studied seriously from a geometric point of view.

The recent upsurge of interest in Finsler metrics has been motivated in part by the fact that two different Finsler metrics appear very naturally in the theory of several complex variables. For certain bounded open sets in \( {\mathbb{C}}^{n} \) (the ones with smooth, strictly convex boundaries, for example), the Kobayashi metric and the Carathéodory metric are intrinsically defined, biholomorphically invariant Finsler metrics. Combining differential-geometric and complex-analytic methods has led to striking new insights into both the function theory and the geometry of such domains. We do not treat Finsler metrics further in this book, but you can consult one of the recent books on the subject [AP94, BCS00, JP13].

## Problems

2-1. Show that every Riemannian 1-manifold is flat. (Used on pp. 13, 193.)

2-2. Suppose \( V \) and \( W \) are finite-dimensional real inner product spaces of the same dimension, and \( F : V \rightarrow  W \) is any map (not assumed to be linear or even continuous) that preserves the origin and all distances: \( F\left( 0\right)  = 0 \) and \( \left| {F\left( x\right)  - F\left( y\right) }\right|  = \left| {x - y}\right| \) for all \( x, y \in  V \) . Prove that \( F \) is a linear isometry. [Hint: First show that \( F \) preserves inner products, and then show that it is linear.] (Used on p. 187.)

2-3. Given a smooth embedded 1-dimensional submanifold \( C \subseteq  H \) as in Example 2.24(b), show that the surface of revolution \( {S}_{C} \subseteq  {\mathbb{R}}^{3} \) with its induced metric is isometric to the warped product \( C{ \times  }_{a}{\mathbb{S}}^{1} \) , where \( a : C \rightarrow  \mathbb{R} \) is the distance to the \( z \) -axis.

2-4. Let \( \rho  : {\mathbb{R}}^{ + } \rightarrow  \mathbb{R} \) be the restriction of the standard coordinate function, and let \( {\mathbb{R}}^{ + }{ \times  }_{\rho }{\mathbb{S}}^{n - 1} \) denote the resulting warped product (see Example 2.24(c)). Define \( \Phi  : {\mathbb{R}}^{ + }{ \times  }_{\rho }{\mathbb{S}}^{n - 1} \rightarrow  {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) by \( \Phi \left( {\rho ,\omega }\right)  = {\rho \omega } \) . Show that \( \Phi \) is an isometry between the warped product metric and the Euclidean metric on \( {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) . (Used on p. 293.)

2-5. Prove parts (b) and (c) of Proposition 2.25 (properties of horizontal vector fields). (Used on p. 146.)

2-6. Prove Theorem 2.28 (if \( \pi  : \widetilde{M} \rightarrow  M \) is a surjective smooth submersion, and a group acts on \( \widetilde{M} \) isometrically, vertically, and transitively on fibers, then \( M \) inherits a unique Riemannian metric such that \( \pi \) is a Riemannian submersion).

2-7. For \( 0 < k < n \) , the set \( {\mathrm{G}}_{k}\left( {\mathbb{R}}^{n}\right) \) of \( k \) -dimensional linear subspaces of \( {\mathbb{R}}^{n} \) is called a Grassmann manifold or Grassmannian. The group \( \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) acts transitively on \( {\mathrm{G}}_{k}\left( {\mathbb{R}}^{n}\right) \) in an obvious way, and \( {\mathrm{G}}_{k}\left( {\mathbb{R}}^{n}\right) \) has a unique smooth manifold structure making this action smooth (see [LeeSM, Example 21.21]).

(a) Let \( {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n}\right) \) denote the set of orthonormal ordered \( k \) -tuples of vectors in \( {\mathbb{R}}^{n} \) . By arranging the vectors in \( k \) columns, we can view \( {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n}\right) \) as a subset of the vector space \( \mathrm{M}\left( {n \times  k,\mathbb{R}}\right) \) of all \( n \times  k \) real matrices. Prove that \( {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n}\right) \) is a smooth submanifold of \( \mathrm{M}\left( {n \times  k,\mathbb{R}}\right) \) of dimension \( k\left( {{2n} - k - 1}\right) /2 \) , called a Stiefel manifold. [Hint: Consider the map \( \Phi  : \mathrm{M}\left( {n \times  k,\mathbb{R}}\right)  \rightarrow  \mathrm{M}\left( {k \times  k,\mathbb{R}}\right) \) given by \( \Phi \left( A\right)  = {A}^{T}A \) .]

(b) Show that the map \( \pi  : {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n}\right)  \rightarrow  {\mathrm{G}}_{k}\left( {\mathbb{R}}^{n}\right) \) that sends a \( k \) -tuple to its span is a surjective smooth submersion.

(c) Give \( {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n}\right) \) the Riemannian metric induced from the Euclidean metric on \( \mathrm{M}\left( {n \times  k,\mathbb{R}}\right) \) . Show that the right action of \( \mathrm{O}\left( k\right) \) on \( {\mathrm{V}}_{k}\left( {\mathbb{R}}^{n}\right) \) by matrix multiplication on the right is isometric, vertical, and transitive on fibers of \( \pi \) , and thus there is a unique metric on \( {\mathrm{G}}_{k}\left( {\mathbb{R}}^{n}\right) \) such that \( \pi \) is a Riemannian submersion. [Hint: It might help to note that the Euclidean inner product on \( \mathrm{M}\left( {n \times  k,\mathbb{R}}\right) \) can be written in the form \( \langle A, B\rangle  = \operatorname{tr}\left( {{A}^{T}B}\right) \) .]

(Used on p. 82.)

2-8. Prove that the action of \( \mathbb{Z} \) on \( {\mathbb{R}}^{2} \) defined in Example 2.35 is smooth, free, proper, and isometric, and therefore the open Möbius band inherits a flat Riemannian metric such that the quotient map is a Riemannian covering.

2-9. Prove Proposition 2.37 (the gradient is orthogonal to regular level sets).

2-10. Suppose \( \left( {M, g}\right) \) is a Riemannian manifold, \( f \in  {C}^{\infty }\left( M\right) \) , and \( X \in  \mathfrak{X}\left( M\right) \) is a nowhere-vanishing vector field. Prove that \( X = \operatorname{grad}f \) if and only if \( {Xf} \equiv  {\left| X\right| }_{g}^{2} \) and \( X \) is orthogonal to the level sets of \( f \) at all regular points of f. (Used on pp. 161, 180.)

2-11. Prove Proposition 2.40 (inner products on tensor bundles).

2-12. Prove Proposition 2.41 (existence and uniqueness of the Riemannian volume form).

2-13. Prove Proposition 2.43 (characterizing the volume form of a Riemannian hypersurface). [Hint: To prove (2.17), use an adapted orthonormal frame.]

2-14. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) and \( \left( {M, g}\right) \) are compact connected Riemannian manifolds, and \( \pi  : \widetilde{M} \rightarrow  M \) is a \( k \) -sheeted Riemannian covering. Prove that \( \operatorname{Vol}\left( \widetilde{M}\right)  = \; k \cdot  \operatorname{Vol}\left( M\right) \) . (Used on p. 363.)

2-15. Suppose \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are oriented Riemannian manifolds of dimensions \( {k}_{1} \) and \( {k}_{2} \) , respectively. Let \( f : {M}_{1} \rightarrow  {\mathbb{R}}^{ + } \) be a smooth function, and let \( g = {g}_{1} \oplus  {f}^{2}{g}_{2} \) be the corresponding warped product metric on \( {M}_{1}{ \times  }_{f}{M}_{2} \) . Prove that the Riemannian volume form of \( g \) is given by

\[
d{V}_{g} = {f}^{{k}_{2}}d{V}_{{g}_{1}} \land  d{V}_{{g}_{2}},
\]

where \( f, d{V}_{{g}_{1}} \) , and \( d{V}_{{g}_{2}} \) are understood to be pulled back to \( {M}_{1} \times  {M}_{2} \) by the projection maps. (Used on p. 295.)

2-16. Let \( \left( {M, g}\right) \) be a Riemannian \( n \) -manifold. Show that for each \( k = 1,\ldots , n \) , there is a unique fiber metric \( \langle  \cdot  , \cdot  {\rangle }_{g} \) on the bundle \( {\Lambda }^{k}{T}^{ * }M \) that satisfies

\[
{\left\langle  {\omega }^{1} \land  \cdots  \land  {\omega }^{k},{\eta }^{1} \land  \cdots  \land  {\eta }^{k}\right\rangle  }_{g} = \det \left( {\left\langle  {\omega }^{i},{\eta }^{j}\right\rangle  }_{g}\right) \tag{2.26}
\]

whenever \( {\omega }^{1},\ldots ,{\omega }^{k},{\eta }^{1},\ldots ,{\eta }^{k} \) are covectors at a point \( p \in  M \) . [Hint: Define the inner product locally by declaring the set of \( k \) -covectors

\[
\left\{  {{\left. {\varepsilon }^{{i}_{1}} \land  \cdots  \land  {\varepsilon }^{{i}_{k}}\right| }_{p} : {i}_{1} < \cdots  < {i}_{k}}\right\}
\]

to be an orthonormal basis for \( {\Lambda }^{k}\left( {{T}_{p}^{ * }M}\right) \) whenever \( \left( {\varepsilon }^{i}\right) \) is a local orthonormal coframe for \( {T}^{ * }M \) , and then prove that the resulting inner product satisfies (2.26) and is independent of the choice of frame.]

2-17. Because we regard the bundle \( {\Lambda }^{k}{T}^{ * }M \) of \( k \) -forms as a subbundle of the bundle \( {T}^{k}{T}^{ * }M \) of covariant \( k \) -tensors, we have two inner products to choose from on \( k \) -forms: the one defined in Problem 2-16, and the restriction of the tensor inner product defined in Proposition 2.40. For this problem, we use the notation \( \langle  \cdot  , \cdot  \rangle \) to denote the inner product of Problem 2-16, and \( \langle \langle  \cdot  , \cdot  \rangle \rangle \) to denote the restriction of the tensor inner product.

(a) Using the convention for the wedge product that we use in this book (see p. 400), prove that

\[
\langle  \cdot  , \cdot  {\rangle }_{g} = \frac{1}{k!}\langle \langle  \cdot  , \cdot  {\rangle }_{g}.
\]

(b) Show that if the Alt convention is used for the wedge product (p. 401), the formula becomes

\[
\langle  \cdot  , \cdot  {\rangle }_{g} = k!\langle \langle  \cdot  , \cdot  {\rangle }_{g}.
\]

2-18. Let \( \left( {M, g}\right) \) be an oriented Riemannian \( n \) -manifold.

(a) For each \( k = 0,\ldots , n \) , show that there is a unique smooth bundle homomorphism \( *  : {\Lambda }^{k}{T}^{ * }M \rightarrow  {\Lambda }^{n - k}{T}^{ * }M \) , called the Hodge star operator, satisfying

\[
\omega  \land   * \eta  = \langle \omega ,\eta {\rangle }_{g}d{V}_{g}
\]

for all smooth \( k \) -forms \( \omega ,\eta \) , where \( \langle  \cdot  , \cdot  {\rangle }_{g} \) is the inner product on \( k \) - forms defined in Problem 2-16. (For \( k = 0 \) , interpret the inner product as ordinary multiplication.) [Hint: First prove uniqueness, and then define * locally by setting

\[
* \left( {{\varepsilon }^{{i}_{1}} \land  \cdots  \land  {\varepsilon }^{{i}_{k}}}\right)  =  \pm  {\varepsilon }^{{j}_{1}} \land  \cdots  \land  {\varepsilon }^{{j}_{n - k}}
\]

in terms of an orthonormal coframe \( \left( {\varepsilon }^{i}\right) \) , where the indices \( {j}_{1},\ldots ,{j}_{n - k} \) are chosen such that \( \left( {{i}_{1},\ldots ,{i}_{k},{j}_{1},\ldots ,{j}_{n - k}}\right) \) is some permutation of \( \left( {1,\ldots , n}\right) \) .]

(b) Show that \( *  : {\Lambda }^{0}{T}^{ * }M \rightarrow  {\Lambda }^{n}{T}^{ * }M \) is given by \( * f = {fd}{V}_{g} \) .

(c) Show that \( *  * \omega  = {\left( -1\right) }^{k\left( {n - k}\right) }\omega \) if \( \omega \) is a \( k \) -form.

2-19. Regard \( {\mathbb{R}}^{n} \) as a Riemannian manifold with the Euclidean metric and the standard orientation, and let * denote the Hodge star operator defined in Problem 2-18.

(a) Calculate \( * d{x}^{i} \) for \( i = 1,\ldots , n \) .

(b) Calculate \( * \left( {d{x}^{i} \land  d{x}^{j}}\right) \) in the case \( n = 4 \) .

2-20. Let \( M \) be an oriented Riemannian 4-manifold. A 2-form \( \omega \) on \( M \) is said to be self-dual if \( * \omega  = \omega \) , and anti-self-dual if \( * \omega  =  - \omega \) .

(a) Show that every 2-form \( \omega \) on \( M \) can be written uniquely as a sum of a self-dual form and an anti-self-dual form.

(b) On \( M = {\mathbb{R}}^{4} \) with the Euclidean metric, determine the self-dual and anti-self-dual forms in standard coordinates.

2-21. Prove Proposition 2.46 (the coordinate formulas for the divergence and the Laplacian).

2-22. Suppose \( \left( {M, g}\right) \) is a compact Riemannian manifold with boundary.

(a) Prove the following divergence theorem for \( X \in  \mathfrak{X}\left( M\right) \) :

\[
{\int }_{M}\left( {\operatorname{div}X}\right) d{V}_{g} = {\int }_{\partial M}\langle X, N{\rangle }_{g}d{V}_{\widehat{g}},
\]

where \( N \) is the outward unit normal to \( \partial M \) and \( \widehat{g} \) is the induced metric on \( \partial M \) . [Hint: Prove it first in the case that \( M \) is orientable, and then apply that case to the orientation covering of \( M \) (Prop. B.18).]

(b) Show that the divergence operator satisfies the following product rule for \( u \in  {C}^{\infty }\left( M\right) \) and \( X \in  \mathfrak{X}\left( M\right) \) :

\[
\operatorname{div}\left( {uX}\right)  = u\operatorname{div}X + \langle \operatorname{grad}u, X{\rangle }_{g},
\]

and deduce the following "integration by parts" formula:

\[
{\int }_{M}\langle \operatorname{grad}u, X{\rangle }_{g}d{V}_{g} = {\int }_{\partial M}u\langle X, N{\rangle }_{g}d{V}_{\widehat{g}} - {\int }_{M}u\operatorname{div}{Xd}{V}_{g}.
\]

What does this say when \( M \) is a compact interval in \( \mathbb{R} \) ?

(Used on p. 149.)

2-23. Let \( \left( {M, g}\right) \) be a compact Riemannian manifold with or without boundary. A function \( u \in  {C}^{\infty }\left( M\right) \) is said to be harmonic if \( {\Delta u} = 0 \) , where \( \Delta \) is the Laplacian defined on page 32.

(a) Prove Green's identities:

\[
{\int }_{M}{u\Delta vd}{V}_{g} = {\int }_{\partial M}{uNvd}{V}_{\widehat{g}} - {\int }_{M}\langle \operatorname{grad}u,\operatorname{grad}v{\rangle }_{g}d{V}_{g},
\]

\[
{\int }_{M}\left( {{u\Delta v} - {v\Delta u}}\right) d{V}_{g} = {\int }_{\partial M}\left( {{uNv} - {vNu}}\right) d{V}_{\widehat{g}},
\]

where \( N \) is the outward unit normal vector field on \( \partial M \) and \( \widehat{g} \) is the induced metric on \( \partial M \) .

(b) Show that if \( M \) is connected, \( \partial M \neq  \varnothing \) , and \( u, v \) are harmonic functions on \( M \) whose restrictions to \( \partial M \) agree, then \( u \equiv  v \) .

(c) Show that if \( M \) is connected and \( \partial M = \varnothing \) , then the only harmonic functions on \( M \) are the constants, and every smooth function \( u \) satisfies \( {\int }_{M}{\Delta ud}{V}_{g} = 0. \)

(Used on pp. 149, 223.)

2-24. Let \( \left( {M, g}\right) \) be a compact Riemannian manifold (without boundary). A real number \( \lambda \) is called an eigenvalue of \( M \) if there exists a smooth function \( u \) on \( M \) , not identically zero, such that \( - {\Delta u} = {\lambda u} \) . In this case, \( u \) is called an eigenfunction corresponding to \( \lambda \) .

(a) Prove that 0 is an eigenvalue of \( M \) , and that all other eigenvalues are strictly positive.

(b) Show that if \( u \) and \( v \) are eigenfunctions corresponding to distinct eigenvalues, then \( {\int }_{M}{uvd}{V}_{g} = 0 \) .

(Used on p. 149.)

2-25. Let \( \left( {M, g}\right) \) be a compact connected Riemannian \( n \) -manifold with nonempty boundary. A number \( \lambda  \in  \mathbb{R} \) is called a Dirichlet eigenvalue for \( M \) if there exists a smooth real-valued function \( u \) on \( M \) , not identically zero, such that \( - {\Delta u} = {\lambda u} \) and \( {\left. u\right| }_{\partial M} = 0 \) . Similarly, \( \lambda \) is called a Neumann eigenvalue if there exists such a \( u \) satisfying \( - {\Delta u} = {\lambda u} \) and \( {\left. Nu\right| }_{\partial M} = 0 \) , where \( N \) is the outward unit normal.

(a) Show that every Dirichlet eigenvalue is strictly positive.

(b) Show that 0 is a Neumann eigenvalue, and all other Neumann eigenvalues are strictly positive.

2-26. DIRICHLET'S PRINCIPLE: Suppose \( \left( {M, g}\right) \) is a compact connected Riemannian \( n \) -manifold with nonempty boundary. Prove that a function \( u \in \; {C}^{\infty }\left( M\right) \) is harmonic if and only if it minimizes \( {\int }_{M}{\left| \operatorname{grad}u\right| }^{2}d{V}_{g} \) among all smooth functions with the same boundary values. [Hint: For any function \( f \in  {C}^{\infty }\left( M\right) \) that vanishes on \( \partial M \) , expand \( {\int }_{M}{\left| \operatorname{grad}\left( u + \varepsilon f\right) \right| }^{2}d{V}_{g} \) and use Problem 2-22.]

2-27. Suppose \( \left( {M, g}\right) \) is an oriented Riemannian 3-manifold.

(a) Define \( \beta  : {TM} \rightarrow  {\Lambda }^{2}{T}^{ * }M \) by \( \beta \left( X\right)  = X \sqcup  d{V}_{g} \) . Show that \( \beta \) is a smooth bundle isomorphism, and thus we can define the curl of a vector field \( X \in  \mathfrak{X}\left( M\right) \) by

\[
\operatorname{curl}X = {\beta }^{-1}d\left( {X}^{b}\right) .
\]

(b) Show that the following diagram commutes:(2.27)

![bo_d7dtff491nqc73eq8m7g_65_406_1077_751_252_0.jpg](images/bo_d7dtff491nqc73eq8m7g_65_406_1077_751_252_0.jpg)

where \( * \left( f\right)  = {fd}{V}_{g} \) , and use this to prove that \( \operatorname{curl}\left( {\operatorname{grad}f}\right)  = 0 \) for every \( f \in  {C}^{\infty }\left( M\right) \) , and \( \operatorname{div}\left( {\operatorname{curl}X}\right)  = 0 \) for every \( X \in  \mathfrak{X}\left( M\right) \) .

(c) Compute the formula for the curl in standard coordinates on \( {\mathbb{R}}^{3} \) with the Euclidean metric.

2-28. Let \( \left( {M, g}\right) \) be an oriented Riemannian manifold and let * denote its Hodge star operator (Problem 2-18). Show that for every \( X \in  \mathfrak{X}\left( M\right) \) ,

\[
X\lrcorner d{V}_{g} =  * \left( {X}^{b}\right)
\]

\[
\operatorname{div}X =  * d * \left( {X}^{b}\right) ,
\]

and, when \( \dim M = 3 \) ,

\[
\operatorname{curl}X = {\left( *d\left( {X}^{b}\right) \right) }^{\sharp },
\]

where the curl of a vector field is defined as in Problem 2-27.

2-29. Let \( \left( {M, g}\right) \) be a compact oriented Riemannian \( n \) -manifold. For \( 1 \leq  k \leq  n \) , define a map \( {d}^{ * } : {\Omega }^{\bar{k}}\left( M\right)  \rightarrow  {\Omega }^{k - 1}\left( M\right) \) by \( {d}^{ * }\omega  = {\left( -1\right) }^{n\left( {k + 1}\right)  + 1} * d * \omega \) , where * is the Hodge star operator defined in Problem 2-18. Extend this definition to 0 -forms by defining \( {d}^{ * }\omega  = 0 \) for \( \omega  \in  {\Omega }^{0}\left( M\right) \) .

(a) Show that \( {d}^{ * } \circ  {d}^{ * } = 0 \) .

(b) Show that the formula

\[
\left( {\omega ,\eta }\right)  = {\int }_{M}\langle \omega ,\eta {\rangle }_{g}d{V}_{g}
\]

defines an inner product on \( {\Omega }^{k}\left( M\right) \) for each \( k \) , where \( \langle  \cdot  , \cdot  {\rangle }_{g} \) is the inner product on forms defined in Problem 2-16.

(c) Show that \( \left( {{d}^{ * }\omega ,\eta }\right)  = \left( {\omega ,{d\eta }}\right) \) for all \( \omega  \in  {\Omega }^{k}\left( M\right) \) and \( \eta  \in  {\Omega }^{k - 1}\left( M\right) \) .

2-30. Suppose \( \left( {M, g}\right) \) is a (not necessarily connected) Riemannian manifold. Show that there is a distance function \( d \) on \( M \) that induces the given topology and restricts to the Riemannian distance on each component of \( M \) . (Used on p. 187.)

2-31. Suppose \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) are connected Riemannian manifolds, and \( \varphi  : M \rightarrow  M \) is a local isometry. Show that \( {d}_{\widetilde{g}}\left( {\varphi \left( x\right) ,\varphi \left( y\right) }\right)  \leq  {d}_{g}\left( {x, y}\right) \) for all \( x, y \in  M \) . Give an example to show that equality need not hold. (Used on p. 37.)

2-32. Let \( \left( {M, g}\right) \) be a Riemannian manifold and \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) a smooth curve segment. For each continuous function \( f : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R} \) , we define the integral of \( f \) with respect to arc length, denoted by \( {\int }_{\gamma }{fds} \) , by

\[
{\int }_{\gamma }{fds} = {\int }_{a}^{b}f\left( t\right) {\left| {\gamma }^{\prime }\left( t\right) \right| }_{g}{dt}
\]

(a) Show that \( {\int }_{\gamma }{fds} \) is independent of parametrization in the following sense: if \( \varphi  : \left\lbrack  {c, d}\right\rbrack   \rightarrow  \left\lbrack  {a, b}\right\rbrack \) is a diffeomorphism, then

\[
{\int }_{a}^{b}f\left( t\right) {\left| {\gamma }^{\prime }\left( t\right) \right| }_{g}{dt} = {\int }_{c}^{d}\widetilde{f}\left( u\right) {\left| {\widetilde{\gamma }}^{\prime }\left( u\right) \right| }_{g}{du},
\]

where \( \widetilde{f} = f \circ  \varphi \) and \( \widetilde{\gamma } = \gamma  \circ  \varphi \) .

(b) Suppose now that \( \gamma \) is a smooth embedding, so that \( C = \gamma \left( \left\lbrack  {a, b}\right\rbrack  \right) \) is an embedded submanifold with boundary in \( M \) . Show that

\[
{\int }_{\gamma }{fds} = {\int }_{C}\left( {f \circ  {\gamma }^{-1}}\right) d\widetilde{V},
\]

where \( d\widetilde{V} \) is the Riemannian volume element on \( C \) associated with the induced metric and the orientation determined by \( \gamma \) .

(Used on p. 273.)

2-33. Prove Proposition 2.65 (Sylvester's law of inertia). 2-34. Prove Theorem 2.69 (existence of Lorentz metrics), as follows.

(a) For sufficiency, assume that \( D \subseteq  {TM} \) is a 1-dimensional distribution, and choose any Riemannian metric \( g \) on \( M \) . Show that locally it is possible to choose a \( g \) -orthonormal frame \( \left( {E}_{i}\right) \) and dual coframe \( \left( {\varepsilon }^{i}\right) \) such that \( {E}_{1} \) spans \( D \) ; and then show that the Lorentz metric \( - {\left( {\varepsilon }^{1}\right) }^{2} + {\left( {\varepsilon }^{2}\right) }^{2} + \; \cdots  + {\left( {\varepsilon }^{n}\right) }^{2} \) is independent of the choice of frame.

(b) To prove necessity, suppose that \( g \) is a Lorentz metric on \( M \) , and let \( {g}_{0} \) be any Riemannian metric. Show that for each \( p \in  M \) , there are exactly two \( {g}_{0} \) -unit vectors \( {v}_{0}, - {v}_{0} \) on which the function \( v \mapsto  g\left( {v, v}\right) \) takes its minimum among all unit vectors in \( {T}_{p}M \) , and use Lagrange multipliers to conclude that there exists a number \( \lambda \left( p\right)  < 0 \) such that \( g\left( {{v}_{0}, w}\right)  = \lambda \left( p\right) {g}_{0}\left( {{v}_{0}, w}\right) \) for all \( w \in  {T}_{p}M \) . You may use the following standard result from perturbation theory: if \( U \) is an open subset of \( {\mathbb{R}}^{n} \) and \( A : U \rightarrow  \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) is a smooth matrix-valued function such that \( A\left( x\right) \) is symmetric and has exactly one negative eigenvalue for each \( x \in  U \) , then there exist smooth functions \( \lambda  : U \rightarrow  \left( {-\infty ,0}\right) \) and \( X : U \rightarrow \; {\mathbb{R}}^{n} \smallsetminus  \{ 0\} \) such that \( A\left( x\right) X\left( x\right)  = \lambda \left( x\right) X\left( x\right) \) for all \( x \in  U \) .

2-35. Prove Corollary 2.71 (about level sets in pseudo-Riemannian manifolds). (Used on p. 63.)
