## Appendix A Review of Smooth Manifolds

This book is designed for readers who already have a solid understanding of basic topology and smooth manifold theory, at roughly the level of [LeeTM] and [LeeSM]. In this appendix, we summarize the main ideas of these subjects that are used throughout the book. It is included here as a review, and to establish our notation and conventions.

## Topological Preliminaries

An n-dimensional topological manifold (or simply an n-manifold) is a second-countable Hausdorff topological space that is locally Euclidean of dimension \( n \) , meaning that every point has a neighborhood homeomorphic to an open subset of \( {\mathbb{R}}^{n} \) . Given an \( n \) -manifold \( M \) , a coordinate chart for \( M \) is a pair \( \left( {U,\varphi }\right) \) , where \( U \subseteq  M \) is an open set and \( \varphi  : U \rightarrow  \widehat{U} \) is a homeomorphism from \( U \) to an open subset \( \widehat{U} \subseteq  {\mathbb{R}}^{n} \) . If \( p \in  M \) and \( \left( {U,\varphi }\right) \) is a chart such that \( p \in  U \) , we say that \( \left( {U,\varphi }\right) \) is a chart containing \( p \) .

We also occasionally need to consider manifolds with boundary. An \( n \) -dimensional topological manifold with boundary is a second-countable Hausdorff space in which every point has a neighborhood homeomorphic either to an open subset of \( {\mathbb{R}}^{n} \) or to a (relatively) open subset of the half-space \( {\mathbb{R}}_{ + }^{n} = \left\{  {\left( {{x}^{1},\ldots ,{x}^{n}}\right)  \in  {\mathbb{R}}^{n}}\right. \) : \( \left. {{x}^{n} \geq  0}\right\} \) . A pair \( \left( {U,\varphi }\right) \) , where \( U \) is an open subset of \( M \) and \( \varphi \) is a homeomorphism from \( U \) to an open subset of \( {\mathbb{R}}^{n} \) or \( {\mathbb{R}}_{ + }^{n} \) , is called an interior chart if \( \varphi \left( U\right) \) is an open subset of \( {\mathbb{R}}^{n} \) or an open subset of \( {\mathbb{R}}_{ + }^{n} \) that does not meet \( \partial {\mathbb{R}}_{ + }^{n} = \left\{  {x \in  {\mathbb{R}}_{ + }^{n}}\right. \) : \( \left. {{x}^{n} = 0}\right\} \) ; and it is called a boundary chart if \( \varphi \left( U\right) \) is an open subset of \( {\mathbb{R}}_{ + }^{n} \) with \( \varphi \left( U\right)  \cap  \partial {\mathbb{R}}_{ + }^{n} \neq  \varnothing \) . A point \( p \in  M \) is called an interior point of \( M \) if it is in the domain of an interior chart, and it is a boundary point of \( \mathbf{M} \) if it is in the domain of a boundary chart taking \( p \) to a point of \( \partial {\mathbb{R}}_{ + }^{n} \) .

Notice that our convention is that a manifold without further qualification is always assumed to be a manifold without boundary, and the term "manifold with boundary" encompasses ordinary manifolds as a special case. But for clarity, we sometimes use redundant phrases such as "manifold without boundary" for an ordinary manifold, and "manifold with or without boundary" when we wish to emphasize that the discussion applies equally well in either case.

Proposition A.1. [LeeTM, Props. 4.23 & 4.64] Every topological manifold with or without boundary is locally path-connected and locally compact.

Proposition A.2. [LeeTM, Thm. 4.77] Every topological manifold with or without boundary is paracompact.

If \( M \) and \( N \) are topological spaces, a map \( F : M \rightarrow  N \) is said to be a closed map if for each closed subset \( K \subseteq  M \) , the image set \( F\left( K\right) \) is closed in \( N \) , and an open map if for each open subset \( U \subseteq  M \) , the image set \( F\left( U\right) \) is open in \( N \) . It is a quotient map if it is surjective and \( V \subseteq  N \) is open if and only if \( {F}^{-1}\left( V\right) \) is open.

Proposition A.3. [LeeTM, Prop. 3.69] Suppose \( M \) and \( N \) are topological spaces, and \( F : M \rightarrow  N \) is a continuous map that is either open or closed.

(a) If \( F \) is surjective, it is a quotient map.

(b) If \( F \) is injective, it is a topological embedding.

(c) If \( F \) is bijective, it is a homeomorphism.

The next lemma often gives a convenient shortcut for proving that a map is closed.

Lemma A. 4 (Closed Map Lemma). [LeeTM, Lemma 4.50] If \( F \) is a continuous map from a compact space to a Hausdorff space, then \( F \) is a closed map.

Here is another condition that is frequently useful for showing that a map is closed. A map \( F : M \rightarrow  N \) between topological spaces is called a proper map if for each compact subset \( K \subseteq  N \) , the preimage \( {F}^{-1}\left( K\right) \) is compact.

Proposition A. 5 (Proper Continuous Maps Are Closed). [LeeTM, Thm. 4.95] Suppose \( M \) is a topological space, \( N \) is a locally compact Hausdorff space, and \( F : M \rightarrow  N \) is continuous and proper. Then \( F \) is a closed map.

## Fundamental Groups

Many of the deepest theorems in Riemannian geometry express relations between local geometric properties and global topological properties. Because the global properties are frequently expressed in terms of fundamental groups, we summarize some basic definitions and properties here.

Suppose \( M \) and \( N \) are topological spaces. If \( {F}_{0},{F}_{1} : M \rightarrow  N \) are continuous maps, a homotopy from \( {F}_{0} \) to \( {F}_{1} \) is a continuous map \( H : M \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  N \) that satisfies \( H\left( {x,0}\right)  = {F}_{0}\left( x\right) \) and \( H\left( {x,1}\right)  = {F}_{1}\left( x\right) \) for all \( x \in  M \) . If there exists such a homotopy, we say that \( {F}_{0} \) and \( {F}_{1} \) are homotopic.

We are most interested in homotopies in the following situation. If \( M \) is a topological space, a path in \( M \) is a continuous map \( \alpha  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) . If \( p = \alpha \left( 0\right) \) and \( q = \alpha \left( 1\right) \) , we say that \( \alpha \) is a path from \( p \) to \( q \) . If \( {\alpha }_{0} \) and \( {\alpha }_{1} \) are both paths from \( p \) to

\( q \) , a path homotopy from \( {\alpha }_{0} \) to \( {\alpha }_{1} \) is a continuous map \( H : \left\lbrack  {0,1}\right\rbrack   \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) that satisfies

\[
H\left( {s,0}\right)  = {\alpha }_{0}\left( s\right) \text{ and }H\left( {s,1}\right)  = {\alpha }_{1}\left( s\right) \text{ for all }s \in  \left\lbrack  {0,1}\right\rbrack  ,
\]

\[
H\left( {0, t}\right)  = p\text{ and }H\left( {1, t}\right)  = q\text{ for all }t \in  \left\lbrack  {0,1}\right\rbrack  \text{ . }
\]

If there exists such a path homotopy, then \( {\alpha }_{0} \) and \( {\alpha }_{1} \) are said to be path-homotopic; this is an equivalence relation on the set of all paths in \( M \) from \( p \) to \( q \) . The equivalence class of a path \( \alpha \) , called its path class, is denoted by \( \left\lbrack  \alpha \right\rbrack \) .

Paths \( \alpha \) and \( \beta \) that satisfy \( \alpha \left( 1\right)  = \beta \left( 0\right) \) are said to be composable; in this case, their product is the path \( \alpha  \cdot  \beta  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) defined by

\[
\alpha  \cdot  \beta \left( s\right)  = \left\{  \begin{array}{ll} \alpha \left( {2s}\right) , & 0 \leq  s \leq  \frac{1}{2}, \\  \beta \left( {{2s} - 1}\right) , & \frac{1}{2} \leq  s \leq  1. \end{array}\right.
\]

Path products are well defined on path classes: if \( \left\lbrack  {\alpha }_{0}\right\rbrack   = \left\lbrack  {\alpha }_{1}\right\rbrack \) and \( \left\lbrack  {\beta }_{0}\right\rbrack   = \left\lbrack  {\beta }_{1}\right\rbrack \) , and \( {\alpha }_{0} \) and \( {\beta }_{0} \) are composable, then so are \( {\alpha }_{1} \) and \( {\beta }_{1} \) , and \( \left\lbrack  {{\alpha }_{0} \cdot  {\beta }_{0}}\right\rbrack   = \left\lbrack  {{\alpha }_{1} \cdot  {\beta }_{1}}\right\rbrack \) . Thus we obtain a well-defined product of path classes by \( \left\lbrack  \alpha \right\rbrack   \cdot  \left\lbrack  \beta \right\rbrack   = \left\lbrack  {\alpha  \cdot  \beta }\right\rbrack \) .

A path from a point \( p \) to itself is called a loop based at \( \mathbf{p} \) . If \( M \) is a topological space and \( p \in  M \) , then any two loops based at \( p \) are composable, and the set of path classes of loops based at \( p \) is a group under path class products, called the fundamental group of \( M \) based at \( \mathbf{p} \) and denoted by \( {\pi }_{1}\left( {M, p}\right) \) . The class of the constant path \( {c}_{p}\left( s\right)  \equiv  p \) is the identity element, and the class of the reverse path \( {\alpha }^{-1}\left( s\right)  = \alpha \left( {1 - s}\right) \) is the inverse of \( \left\lbrack  \alpha \right\rbrack \) . (Although multiplication of path classes is associative, path products themselves are not, so a multiple product such as \( \alpha  \cdot  \beta  \cdot  \gamma \) is to be interpreted as \( \left( {\alpha  \cdot  \beta }\right)  \cdot  \gamma \) .)

Proposition A. 6 (Induced Homomorphisms). [LeeTM, Prop. 7.24 & Cor. 7.26] Suppose \( M \) and \( N \) are topological spaces and \( p \in  M \) . If \( F : M \rightarrow  N \) is a continuous map, then the map \( {F}_{ * } : {\pi }_{1}\left( {M, p}\right)  \rightarrow  {\pi }_{1}\left( {N, F\left( p\right) }\right) \) defined by \( {F}_{ * }\left( \left\lbrack  \alpha \right\rbrack  \right)  = \left\lbrack  {F \circ  \alpha }\right\rbrack \) is a group homomorphism called the homomorphism induced by \( F \) . If \( F \) is a homeomorphism, then \( {F}_{ * } \) is an isomorphism.

A topological space \( M \) is said to be simply connected if it is path-connected and for some (hence every) point \( p \in  M \) , the fundamental group \( {\pi }_{1}\left( {M, p}\right) \) is trivial.

Exercise A.7. Show that if \( M \) is a simply connected topological space and \( p, q \) are any two points in \( M \) , then all paths in \( M \) from \( p \) to \( q \) are path-homotopic.

A continuous map \( F : M \rightarrow  N \) is said to be a homotopy equivalence if there is a continuous map \( G : N \rightarrow  M \) such that \( G \circ  F \) and \( F \circ  G \) are both homotopic to identity maps.

Proposition A. 8 (Homotopy Invariance of the Fundamental Group). [LeeTM, Thm. 7.40] Suppose \( M \) and \( N \) are topological spaces and \( F : M \rightarrow  N \) is a homotopy equivalence. Then for every point \( p \in  M \) , the induced homomorphism \( {F}_{ * } : {\pi }_{1}\left( {M, p}\right)  \rightarrow  {\pi }_{1}\left( {N, F\left( p\right) }\right) \) is an isomorphism.

## Smooth Manifolds and Smooth Maps

The setting for the study of Riemannian geometry is provided by smooth manifolds, which are topological manifolds endowed with an extra structure that allows us to differentiate functions and maps. First, we note that when \( U \) is an open subset of \( {\mathbb{R}}^{n} \) , a map \( F : U \rightarrow  {\mathbb{R}}^{k} \) is said to be smooth (or of class \( {C}^{\infty } \) ) if all of its component functions have continuous partial derivatives of all orders. More generally, if the domain \( U \) is an arbitrary subset of \( {\mathbb{R}}^{n} \) , not necessarily open (such as a relatively open subset of \( {\mathbb{R}}_{ + }^{n} \) ), then \( F \) is said to be smooth if for each \( x \in  U, F \) has a smooth extension to a neighborhood of \( x \) in \( {\mathbb{R}}^{n} \) . A diffeomorphism is a bijective smooth map whose inverse is also smooth.

If \( M \) is a topological \( n \) -manifold with or without boundary, then two coordinate charts \( \left( {U,\varphi }\right) ,\left( {V,\psi }\right) \) for \( M \) are said to be smoothly compatible if both of the transition maps \( \psi  \circ  {\varphi }^{-1} \) and \( \varphi  \circ  {\psi }^{-1} \) are smooth where they are defined (on \( \varphi \left( {U \cap  V}\right) \) and \( \psi \left( {U \cap  V}\right) \) , respectively). Since these maps are inverses of each other, it follows that both transition maps are in fact diffeomorphisms. An atlas for \( \mathbf{M} \) is a collection of coordinate charts whose domains cover \( M \) . It is called a smooth atlas if any two charts in the atlas are smoothly compatible. A smooth structure on \( \mathbf{M} \) is a smooth atlas that is maximal, meaning that it is not properly contained in any larger smooth atlas. A smooth manifold is a topological manifold endowed with a specific smooth structure; and similarly, a smooth manifold with boundary is a topological manifold with boundary endowed with a smooth structure. (We usually just say " \( M \) is a smooth manifold," or " \( M \) is a smooth manifold with boundary," with the smooth structure understood from the context.) If \( M \) is a set, a smooth manifold structure on \( M \) is a second countable, Hausdorff, locally Euclidean topology together with a smooth structure making it into a smooth manifold.

Exercise A.9. Let \( M \) be a topological manifold with or without boundary. Show that every smooth atlas for \( M \) is contained in a unique maximal smooth atlas, and two smooth atlases determine the same smooth structure if and only if their union is a smooth atlas.

The manifolds in this book are always assumed to be smooth. As in most parts of differential geometry, the theory still works under weaker differentiability assumptions (such as \( k \) times continuously differentiable), but such considerations are usually relevant only when one is treating questions of hard analysis that are beyond our scope.

If \( M \) is a smooth manifold with or without boundary, then every coordinate chart in the given maximal atlas is called a smooth coordinate chart for \( \mathbf{M} \) or just a smooth chart. The set \( U \) is called a smooth coordinate domain; if its image is an open ball in \( {\mathbb{R}}^{n} \) , it is called a smooth coordinate ball. If in addition \( \varphi \) extends to a smooth coordinate map \( {\varphi }^{\prime } : {U}^{\prime } \rightarrow  {\mathbb{R}}^{n} \) on an open set \( {U}^{\prime } \supseteq  \bar{U} \) such that \( {\varphi }^{\prime }\left( \bar{U}\right) \) is the closure of the open ball \( \varphi \left( U\right) \) in \( {\mathbb{R}}^{n} \) , then \( U \) is called a regular coordinate ball. In this case, \( \bar{U} \) is diffeomorphic to a closed ball and is thus compact.

Proposition A.10. [LeeSM, Prop. 1.19] Every smooth manifold has a countable basis of regular coordinate balls.

Given a smooth chart \( \left( {U,\varphi }\right) \) for \( M \) , the component functions of \( \varphi \) are called local coordinates for \( \mathbf{M} \) , and are typically written as \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) ,\left( {x}^{i}\right) \) , or \( x \) , depending on context. Although, formally speaking, a coordinate chart is a map from an open subset \( U \subseteq  M \) to \( {\mathbb{R}}^{n} \) , it is common when one is working in the domain of a specific chart to use the coordinate map to identify \( U \) with its image in \( {\mathbb{R}}^{n} \) , and to identify a point in \( U \) with its coordinate representation \( \left( {{x}^{1},\ldots ,{x}^{n}}\right)  \in  {\mathbb{R}}^{n} \) .

In this book, we always write coordinates with upper indices, as in \( \left( {x}^{i}\right) \) , and expressions with indices are interpreted using the Einstein summation convention: if in some monomial term the same index name appears exactly twice, once as an upper index and once as a lower index, then that term is understood to be summed over all possible values of that index (usually from 1 to the dimension of the space). Thus the expression \( {a}^{i}{v}_{i} \) is to be read as \( \mathop{\sum }\limits_{i}{a}^{i}{v}_{i} \) . As we will see below, index positions for other sorts of objects such as vectors and covectors are chosen whenever possible in such a way that summations that make mathematical sense obey the rule that each repeated index appears once up and once down in each term to be summed.

Because of the result of Exercise A.9, to define a smooth structure on a manifold, it suffices to exhibit a single smooth atlas for it. For example, \( {\mathbb{R}}^{n} \) is a topological \( n \) -manifold, and it has a smooth atlas consisting of the single chart \( \left( {{\mathbb{R}}^{n},{\operatorname{Id}}_{{\mathbb{R}}^{n}}}\right) \) . More generally, if \( V \) is an \( n \) -dimensional vector space, then every basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( V \) yields a linear basis isomorphism \( B : {\mathbb{R}}^{n} \rightarrow  V \) by \( B\left( {{x}^{1},\ldots ,{x}^{n}}\right)  = {x}^{i}{b}_{i} \) , whose inverse is a global coordinate chart, and it is easy to check that all such charts are smoothly compatible. Thus every finite-dimensional vector space has a natural smooth structure, which we call its standard smooth structure. We always consider \( {\mathbb{R}}^{n} \) or any other finite-dimensional vector space to be a smooth manifold with this structure unless otherwise specified.

If \( M \) is a smooth \( n \) -manifold with or without boundary and \( W \subseteq  M \) is an open subset, then \( W \) has a natural smooth structure consisting of all smooth charts \( \left( {U,\varphi }\right) \) for \( M \) such that \( U \subseteq  W \) , so every open subset of a smooth \( n \) -manifold is a smooth \( n \) - manifold in a natural way, and similarly for manifolds with boundary. If \( {M}_{1},\ldots ,{M}_{k} \) are smooth manifolds of dimensions \( {n}_{1},\ldots ,{n}_{k} \) , respectively, then their Cartesian product \( {M}_{1} \times  \cdots  \times  {M}_{k} \) has a natural smooth atlas consisting of charts of the form \( \left( {{U}_{1} \times  \cdots  \times  {U}_{k},{\varphi }_{1} \times  \cdots  \times  {\varphi }_{k}}\right) \) , where \( \left( {{U}_{i},{\varphi }_{i}}\right) \) is a smooth chart for \( {M}_{i} \) ; thus the product space is a smooth manifold of dimension \( {n}_{1} + \cdots  + {n}_{k} \) .

Suppose \( M \) and \( N \) are smooth manifolds with or without boundary. A map \( F : M \rightarrow  N \) is said to be smooth if for every \( p \in  M \) , there exist smooth charts \( \left( {U,\varphi }\right) \) for \( M \) containing \( p \) and \( \left( {V,\psi }\right) \) for \( N \) containing \( F\left( p\right) \) such that \( F\left( U\right)  \subseteq  V \) and the composite map \( \psi  \circ  F \circ  {\varphi }^{-1} \) is smooth from \( \varphi \left( U\right) \) to \( \psi \left( V\right) \) . In particular, if \( N \) is an open subset of \( {\mathbb{R}}^{k} \) or \( {\mathbb{R}}_{ + }^{k} \) with its standard smooth structure, we can take \( \psi \) to be the identity map of \( N \) , and then smoothness of \( F \) just means that each point of \( M \) is contained in the domain of a chart \( \left( {U,\varphi }\right) \) such that \( F \circ  {\varphi }^{-1} \) is smooth. It is an easy consequence of the definition that identity maps, constant maps, and compositions of smooth maps are all smooth. A map \( F : M \rightarrow  N \) is said to be a diffeomorphism if it is smooth and bijective and \( {F}^{-1} : N \rightarrow  M \) is also smooth.

If \( F : M \rightarrow  N \) is smooth, and \( \left( {U,\varphi }\right) \) and \( \left( {V,\psi }\right) \) are any smooth charts for \( M \) and \( N \) respectively, the map \( \widehat{F} = \psi  \circ  F \circ  {\varphi }^{-1} \) is a smooth map between appropriate subsets of \( {\mathbb{R}}^{n} \) or \( {\mathbb{R}}_{ + }^{n} \) , called a coordinate representation of \( F \) . Often, in keeping with the practice of using local coordinates to identify an open subset of a manifold with an open subset of \( {\mathbb{R}}^{n} \) , we identify the coordinate representation of \( F \) with (the restriction of) \( F \) itself, and write things like " \( F \) is given in local coordinates by \( F\left( {x, y}\right)  = \left( {{xy}, x - y}\right) \) ," when we really mean that \( \widehat{F} \) is given by this formula for suitable choices of charts in the domain and codomain.

We let \( {C}^{\infty }\left( {M, N}\right) \) denote the set of all smooth maps from \( M \) to \( N \) , and \( {C}^{\infty }\left( M\right) \) the vector space of all smooth functions from \( M \) to \( \mathbb{R} \) . For every function \( f : M \rightarrow  \mathbb{R} \) or \( {\mathbb{R}}^{k} \) , we define the support of \( f \) , denoted by supp \( f \) , to be the closure of the set \( \{ x \in  M : f\left( x\right)  \neq  0\} \) . If \( A \subseteq  M \) is a closed subset and \( U \subseteq  M \) is an open subset containing \( A \) , then a smooth bump function for \( A \) supported in \( U \) is a smooth function \( f : M \rightarrow  \mathbb{R} \) satisfying \( 0 \leq  f\left( x\right)  \leq  1 \) for all \( x \in  M,{\left. f\right| }_{A} \equiv  1 \) , and supp \( f \subseteq  U \) .

If \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  A} \) is an indexed open cover of \( M \) , then a smooth partition of unity subordinate to \( \mathcal{U} \) is an indexed family \( {\left\{  {\psi }_{\alpha }\right\}  }_{\alpha  \in  A} \) of functions \( {\psi }_{\alpha } \in  {C}^{\infty }\left( M\right) \) satisfying

- \( 0 \leq  {\psi }_{\alpha }\left( x\right)  \leq  1 \) for all \( \alpha  \in  A \) and all \( x \in  M \) .

- supp \( {\psi }_{\alpha } \subseteq  {U}_{\alpha } \) for each \( \alpha  \in  A \) .

- The family of supports \( {\left\{  \operatorname{supp}{\psi }_{\alpha }\right\}  }_{\alpha  \in  A} \) is locally finite: every point of \( M \) has a neighborhood that intersects supp \( {\psi }_{\alpha } \) for only finitely many values of \( \alpha \) .

- \( \mathop{\sum }\limits_{{\alpha  \in  A}}{\psi }_{\alpha }\left( x\right)  = 1 \) for all \( x \in  M \) .

Proposition A.11 (Existence of Partitions of Unity). [LeeSM, Thm. 2.23] If \( M \) is a smooth manifold with or without boundary and \( \mathcal{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  A} \) is an indexed open cover of \( M \) , then there exists a smooth partition of unity subordinate to \( \mathcal{U} \) .

Proposition A.12 (Existence of Smooth Bump Functions). [LeeSM, Prop. 2.25] If \( M \) is a smooth manifold with or without boundary, \( A \subseteq  M \) is a closed subset, and \( U \subseteq  M \) is an open subset containing \( A \) , then there exists a smooth bump function for \( A \) supported in \( U \) .

## Tangent Vectors

Let \( M \) be a smooth manifold with or without boundary. There are various equivalent ways of defining tangent vectors on \( M \) . The following definition is the most convenient to work with in practice. For every point \( p \in  M \) , a tangent vector at \( p \) is a linear map \( v : {C}^{\infty }\left( M\right)  \rightarrow  \mathbb{R} \) that is a derivation at \( \mathbf{p} \) , meaning that for all \( f, g \in  {C}^{\infty }\left( M\right) \) it satisfies the product rule

\[
v\left( {fg}\right)  = f\left( p\right) {vg} + g\left( p\right) {vf}. \tag{A.1}
\]

The set of all tangent vectors at \( p \) is denoted by \( {T}_{p}M \) and called the tangent space at \( p \) .

Suppose \( M \) is \( n \) -dimensional and \( \varphi  : U \rightarrow  \widehat{U} \subseteq  {\mathbb{R}}^{n} \) is a smooth coordinate chart on some open subset \( U \subseteq  M \) . Writing the coordinate functions of \( \varphi \) as \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) , we define the coordinate vectors \( \partial /{\left. \partial {x}^{1}\right| }_{p},\ldots ,\partial /{\left. \partial {x}^{n}\right| }_{p} \) by

\[
{\left. \frac{\partial }{\partial {x}^{i}}\right| }_{p}f = {\left. \frac{\partial }{\partial {x}^{i}}\right| }_{\varphi \left( p\right) }\left( {f \circ  {\varphi }^{-1}}\right) . \tag{A.2}
\]

These vectors form a basis for \( {T}_{p}M \) , which therefore has dimension \( n \) . When there can be no confusion about which coordinates are meant, we usually abbreviate \( \partial /{\left. \partial {x}^{i}\right| }_{p} \) by the notation \( {\left. {\partial }_{i}\right| }_{p} \) . Thus once a smooth coordinate chart has been chosen, every tangent vector \( v \in  {T}_{p}M \) can be written uniquely in the form

\[
v = {v}^{i}{\partial }_{i}{\left| {}_{p} = {v}^{1}{\partial }_{1}\right| }_{p} + \cdots  + {v}^{n}{\partial }_{n}{|}_{p}, \tag{A.3}
\]

where the components \( {v}^{1},\ldots ,{v}^{n} \) are obtained by applying \( v \) to the coordinate functions: \( {v}^{i} = v\left( {x}^{i}\right) \) .

On a finite-dimensional vector space \( V \) with its standard smooth manifold structure, there is a natural (basis-independent) identification of each tangent space \( {T}_{p}V \) with \( V \) itself, obtained by identifying a vector \( v \in  V \) with the derivation \( {\left. {D}_{v}\right| }_{p} \) , defined by

\[
{\left. {D}_{v}\right| }_{p}\left( f\right)  = {\left. \frac{d}{dt}\right| }_{t = 0}f\left( {p + {tv}}\right) .
\]

In terms of the coordinates \( \left( {x}^{i}\right) \) induced on \( V \) by any basis, this is the correspondence \( \left( {{v}^{1},\ldots ,{v}^{n}}\right)  \leftrightarrow  \mathop{\sum }\limits_{i}{v}^{i}{\left. {\partial }_{i}\right| }_{p} \) .

If \( F : M \rightarrow  N \) is a smooth map and \( p \) is any point in \( M \) , we define a linear map \( d{F}_{p} : {T}_{p}M \rightarrow  {T}_{F\left( p\right) }N \) , called the differential of \( F \) at \( p \) , by

\[
d{F}_{p}\left( v\right) f = v\left( {f \circ  F}\right) ,\;v \in  {T}_{p}M.
\]

Exercise A.13. Given a smooth map \( F : M \rightarrow  N \) and a point \( p \in  M \) , show that \( d{F}_{p} \) is a well-defined linear map from \( {T}_{p}M \) to \( {T}_{F\left( p\right) }N \) . Show that the differential of the identity is the identity, and the differential of a composition is given by \( d{\left( G \circ  F\right) }_{p} = \; d{G}_{F\left( p\right) } \circ  d{F}_{p} \) .

Once we have chosen local coordinates \( \left( {x}^{i}\right) \) for \( M \) and \( \left( {y}^{j}\right) \) for \( N \) , we find by unwinding the definitions that the coordinate representation of the differential is given by the Jacobian matrix of the coordinate representation of \( F \) , which is its matrix of first-order partial derivatives:

\[
d{F}_{p}\left( {{v}^{i}{\left. \frac{\partial }{\partial {x}^{i}}\right| }_{p}}\right)  = {\left. \frac{\partial {\widehat{F}}^{j}}{\partial {x}^{i}}\left( p\right) {v}^{i}{\left. \frac{\partial }{\partial {y}^{j}}\right| }_{F\left( p\right) }\right| }_{F\left( p\right) }.
\]

For every \( p \in  M \) , the dual vector space to \( {T}_{p}M \) is called the cotangent space at \( \mathbf{p} \) . This is the space \( {T}_{p}^{ * }M = {\left( {T}_{p}M\right) }^{ * } \) of real-valued linear functionals on \( {T}_{p}M \) , called (tangent) covectors at \( \mathbf{p} \) . For every \( f \in  {C}^{\infty }\left( M\right) \) and \( p \in  M \) , there is a covector \( d{f}_{p} \in  {T}_{p}^{ * }M \) called the differential of \( \mathbf{f} \) at \( \mathbf{p} \) , defined by

\[
d{f}_{p}\left( v\right)  = {vf}\text{ for all }v \in  {T}_{p}M\text{ . } \tag{A.4}
\]

## Submanifolds

The theory of submanifolds is founded on the inverse function theorem and its corollaries.

Theorem A.14 (Inverse Function Theorem for Manifolds). [LeeSM, Thm. 4.5] Suppose \( M \) and \( N \) are smooth manifolds and \( F : M \rightarrow  N \) is a smooth map. If the linear map \( d{F}_{p} \) is invertible at some point \( p \in  M \) , then there exist connected neighborhoods \( {U}_{0} \) of \( p \) and \( {V}_{0} \) of \( F\left( p\right) \) such that \( {\left. F\right| }_{{U}_{0}} : {U}_{0} \rightarrow  {V}_{0} \) is a diffeomorphism.

The most useful consequence of the inverse function theorem is the following. A smooth map \( F : M \rightarrow  N \) is said to have constant rank if the linear map \( d{F}_{p} \) has the same rank at every point \( p \in  M \) .

Theorem A.15 (Rank Theorem). [LeeSM, Thm. 4.12] Suppose \( M \) and \( N \) are smooth manifolds of dimensions \( m \) and \( n \) , respectively, and \( F : M \rightarrow  N \) is a smooth map with constant rank \( r \) . For each \( p \in  M \) there exist smooth charts \( \left( {U,\varphi }\right) \) for \( M \) centered at \( p \) and \( \left( {V,\psi }\right) \) for \( N \) centered at \( F\left( p\right) \) such that \( F\left( U\right)  \subseteq  V \) , in which \( F \) has a coordinate representation of the form

\[
\widehat{F}\left( {{x}^{1},\ldots ,{x}^{r},{x}^{r + 1},\ldots ,{x}^{m}}\right)  = \left( {{x}^{1},\ldots ,{x}^{r},0,\ldots ,0}\right) . \tag{A.5}
\]

Here are the most important types of constant-rank maps. In all of these definitions, \( M \) and \( N \) are smooth manifolds, and \( F : M \rightarrow  N \) is a smooth map.

- \( F \) is a submersion if its differential is surjective at each point, or equivalently if it has constant rank equal to \( \dim N \) .

- \( F \) is an immersion if its differential is injective at each point, or equivalently if it has constant rank equal to \( \dim M \) .

- \( F \) is a local diffeomorphism if every point \( p \in  M \) has a neighborhood \( U \) such that \( {\left. F\right| }_{U} \) is a diffeomorphism onto an open subset of \( N \) , or equivalently if \( F \) is both a submersion and an immersion.

- \( F \) is a smooth embedding if it is an injective immersion that is also a topological embedding (a homeomorphism onto its image, endowed with the subspace topology).

Theorem A.16 (Local Embedding Theorem). [LeeSM, Thm. 4.25] Every smooth immersion is locally an embedding: if \( F : M \rightarrow  N \) is a smooth immersion, then for every \( p \in  M \) , there is a neighborhood \( U \) of \( p \) in \( M \) such that \( {\left. F\right| }_{U} \) is an embedding.

Theorem A.17 (Local Section Theorem). [LeeSM, Thm. 4.26] Suppose \( M \) and \( N \) are smooth manifolds and \( \pi  : M \rightarrow  N \) is a smooth map. Then \( \pi \) is a smooth submersion if and only if every point of \( M \) is in the image of a smooth local section of \( \pi \) (a map \( \sigma  : U \rightarrow  M \) defined on some open subset \( U \subseteq  N \) , with \( \pi  \circ  \sigma  = {\mathrm{{Id}}}_{U} \) ).

Proposition A. 18 (Properties of Submersions). [LeeSM, Prop. 4.28] Let \( M \) and \( N \) be smooth manifolds and let \( \pi  : M \rightarrow  N \) be a smooth submersion.

(a) \( \pi \) is an open map.

(b) If \( \pi \) is surjective, it is a quotient map.

Proposition A.19 (Uniqueness of Smooth Quotients). [LeeSM, Thm. 4.31] Suppose \( M,{N}_{1} \) , and \( {N}_{2} \) are smooth manifolds, and \( {\pi }_{1} : M \rightarrow  {N}_{1} \) and \( {\pi }_{2} : M \rightarrow  {N}_{2} \) are surjective smooth submersions that are constant on each other's fibers. Then there exists a unique diffeomorphism \( F : {N}_{1} \rightarrow  {N}_{2} \) such that \( F \circ  {\pi }_{1} = {\pi }_{2} \) .

Theorem A.20 (Global Rank Theorem). [LeeSM, Thm. 4.14] Suppose \( M \) and \( N \) are smooth manifolds, and \( F : M \rightarrow  N \) is a smooth map of constant rank.

(a) If \( F \) is surjective, then it is a smooth submersion.

(b) If \( F \) is injective, then it is a smooth immersion.

(c) If \( F \) is bijective, then it is a diffeomorphism.

Suppose \( \widetilde{M} \) is a smooth manifold with or without boundary. An immersed \( n \) - dimensional submanifold of \( M \) is a subset \( M \subseteq  \widetilde{M} \) endowed with a topology that makes it into an \( n \) -dimensional topological manifold and a smooth structure such that the inclusion map \( M \hookrightarrow  \widetilde{M} \) is a smooth immersion. It is called an embedded submanifold if the inclusion is a smooth embedding, or equivalently if the given topology on \( M \) is the subspace topology. Immersed and embedded submanifolds with boundary are defined similarly. In each case, the codimension of \( M \) is the difference dim \( \widetilde{M} - \dim M \) . A submanifold of codimension 1 is known as a hypersurface. Without further qualification, the word submanifold means an immersed submanifold, which includes an embedded one as a special case.

An embedded submanifold with or without boundary is said to be properly embedded if the inclusion map is proper.

Proposition A.21. [LeeSM, Prop. 5.5] If \( \widetilde{M} \) is a smooth manifold with or without boundary, then an embedded submanifold \( M \subseteq  \widetilde{M} \) is properly embedded if and only if it is a closed subset of \( \widetilde{M} \) .

A properly embedded codimension-0 submanifold with boundary in \( \widetilde{M} \) is called a regular domain.

Proposition A.22 (Slice Coordinates). [LeeSM, Thms. 5.8 & 5.51] Let \( \widetilde{M} \) be a smooth m-manifold without boundary and let \( M \subseteq  \widetilde{M} \) be an embedded \( n \) - dimensional submanifold with or without boundary. Then for each \( p \in  M \) there exist a neighborhood \( \widetilde{U} \) of \( p \) in \( \widetilde{M} \) and smooth coordinates \( \left( {{x}^{1},\ldots ,{x}^{m}}\right) \) for \( \widetilde{M} \) on \( \widetilde{U} \) such that \( M \cap  \widetilde{U} \) is a set of one of the following forms:

\[
M \cap  \widetilde{U} = \left\{  \begin{array}{ll} \left\{  {x \in  \widetilde{U} : {x}^{n + 1} = \cdots  = {x}^{m} = 0}\right\}  & \text{ if }p \notin  \partial M, \\  \left\{  {x \in  \widetilde{U} : {x}^{n + 1} = \cdots  = {x}^{m} = 0\text{ and }{x}^{n} \geq  0}\right\}  & \text{ if }p \in  \partial M. \end{array}\right.
\]

In such a chart, \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) form smooth local coordinates for \( M \) .

Coordinates satisfying either of these conditions are called slice coordinates; when it is necessary to distinguish them, coordinates satisfying the second condition are referred to as boundary slice coordinates.

If \( M \) is an immersed submanifold, then Theorem A. 16 shows that every point of \( M \) has a neighborhood \( U \) in \( M \) that is embedded in \( \widetilde{M} \) , so we can construct slice coordinates for \( U \) (but they need not be slice coordinates for \( M \) ).

Exercise A.23. Suppose \( \widetilde{M} \) is a smooth manifold and \( M \subseteq  \widetilde{M} \) is an embedded sub-manifold. Show that every smooth function \( f : M \rightarrow  \mathbb{R} \) can be extended to a smooth function on a neighborhood of \( M \) in \( \widetilde{M} \) whose restriction to \( M \) is \( f \) ; and if \( M \) is also closed in \( \widetilde{M} \) , then the neighborhood can be taken to be all of \( \widetilde{M} \) . [Hint: Extend \( f \) locally in slice coordinates by letting it be independent of \( \left( {{x}^{n + 1},\ldots ,{x}^{m}}\right) \) , and patch together using a partition of unity.]

Here is the way that most submanifolds are presented. Suppose \( \Phi  : \widetilde{M} \rightarrow  N \) is any map. Every subset of the form \( {\Phi }^{-1}\left( {\{ y\} }\right)  \subseteq  \widetilde{M} \) for some \( y \in  N \) is called a level set of \( \Phi \) , or the fiber of \( \Phi \) over \( y \) . The simpler notation \( {\Phi }^{-1}\left( y\right) \) is also used for a level set when there is no likelihood of ambiguity.

Theorem A.24 (Constant-Rank Level Set Theorem). [LeeSM, Thm. 5.12] Suppose \( \widetilde{M} \) and \( N \) are smooth manifolds, and \( \Phi  : \widetilde{M} \rightarrow  N \) is a smooth map with constant rank \( r \) . Every level set of \( \Phi \) is a properly embedded submanifold of codimen-sion \( r \) in \( \widetilde{M} \) .

Corollary A.25 (Submersion Level Set Theorem). [LeeSM, Cor. 5.13] Suppose \( \widetilde{M} \) and \( N \) are smooth manifolds, and \( \Phi  : \widetilde{M} \rightarrow  N \) is a smooth submersion. Every level set of \( \Phi \) is a properly embedded submanifold of \( \widetilde{M} \) , whose codimension is equal to \( \dim N \) .

In fact, a map does not have to be a submersion, or even to have constant rank, for its level sets to be embedded submanifolds. If \( \Phi  : \widetilde{M} \rightarrow  N \) is a smooth map, a point \( p \in  \widetilde{M} \) is called a regular point of \( \Phi \) if the linear map \( d{\Phi }_{p} : {T}_{p}\widetilde{M} \rightarrow  {T}_{\Phi \left( p\right) }N \) is surjective, and \( p \) is called a critical point of \( \mathbf{\Phi } \) if it is not. A point \( c \in  N \) is called a regular value of \( \Phi \) if every point of \( {\Phi }^{-1}\left( c\right) \) is a regular point of \( \Phi \) , and a critical value otherwise. A level set \( {\Phi }^{-1}\left( c\right) \) is called a regular level set of \( \Phi \) if \( c \) is a regular value of \( \Phi \) .

Corollary A.26 (Regular Level Set Theorem). [LeeSM, Cor. 5.14] Let \( \widetilde{M} \) and \( N \) be smooth manifolds, and let \( \Phi  : \widetilde{M} \rightarrow  N \) be a smooth map. Every regular level set of \( \Phi \) is a properly embedded submanifold of \( \widetilde{M} \) whose codimension is equal to \( \dim N \) .

Suppose \( \widetilde{M} \) is a smooth manifold and \( M \subseteq  \widetilde{M} \) is an embedded codimension- \( k \) submanifold. A smooth map \( \Phi  : \widetilde{M} \rightarrow  {\mathbb{R}}^{k} \) is called a defining function for \( M \) if \( M \) is a regular level set of \( \Phi \) . More generally, if \( \Phi  : U \rightarrow  {\mathbb{R}}^{k} \) is a smooth map defined on an open subset \( U \subseteq  \widetilde{M} \) such that \( M \cap  U \) is a regular level set of \( \Phi \) , then \( \Phi \) is called a local defining function for \( M \) . The following is a partial converse to the submersion level set theorem.

Proposition A.27 (Existence of Local Defining Functions). [LeeSM, Prop. 5.16] Suppose \( \widetilde{M} \) is a smooth manifold and \( M \subseteq  \widetilde{M} \) is an embedded submanifold of codimension \( k \) . For each point \( p \in  M \) , there exist a neighborhood \( U \) of \( p \) in \( \widetilde{M} \) and a smooth submersion \( \Phi  : U \rightarrow  {\mathbb{R}}^{k} \) such that \( M \cap  U \) is a level set of \( \Phi \) .

If \( M \subseteq  \widetilde{M} \) is a submanifold (immersed or embedded), the inclusion map \( \iota  : M \hookrightarrow \; \widetilde{M} \) induces an injective linear map \( d{\iota }_{p} : {T}_{p}M \rightarrow  {T}_{p}\widetilde{M} \) for each \( p \in  M \) . It is standard practice to identify \( {T}_{p}M \) with its image \( d{\iota }_{p}\left( {{T}_{p}M}\right)  \subseteq  {T}_{p}\widetilde{M} \) , thus regarding \( {T}_{p}M \) as a subspace of \( {T}_{p}\widetilde{M} \) . The next proposition gives two handy ways to identify this subspace in the embedded case.

Proposition A.28 (Tangent Space to a Submanifold). [LeeSM, Props. 5.37 & 5.38] Suppose \( \widetilde{M} \) is a smooth manifold, \( M \subseteq  \widetilde{M} \) is an embedded submanifold, and \( p \in  M \) . As a subspace of \( {T}_{p}\widetilde{M} \) , the tangent space \( {T}_{p}M \) is characterized by

\[
{T}_{p}M = \left\{  {v \in  {T}_{p}\widetilde{M} : {vf} = 0\text{ whenever }f \in  {C}^{\infty }\left( \widetilde{M}\right) \text{ and }{\left. f\right| }_{M} = 0}\right\}  .
\]

If \( \Phi \) is a local defining function for \( M \) on a neighborhood of \( p \) , then

\[
{T}_{p}M = \operatorname{Ker}d{\Phi }_{p}.
\]

Proposition A.29 (Lagrange Multiplier Rule). Let \( \widetilde{M} \) be a smooth m-manifold and \( M \subseteq  \widetilde{M} \) be an embedded hypersurface. Suppose \( f \in  {C}^{\infty }\left( \widetilde{M}\right) \) , and \( p \in  M \) is a point at which \( f \) attains a local maximum or minimum value among points in \( M \) . If \( \Phi  : U \rightarrow  \mathbb{R} \) is a local defining function for \( M \) on a neighborhood \( U \) of \( p \) , then there is a real number \( \lambda \) (called a Lagrange multiplier) such that \( d{f}_{p} = {\lambda d}{\Phi }_{p} \) .

Exercise A.30. Prove the preceding proposition. [Hint: One way to proceed is to begin by showing that there are smooth functions \( {x}^{1},\ldots ,{x}^{m - 1} \) on a neighborhood of \( p \) such that \( \left( {{x}^{1},\ldots ,{x}^{m - 1},\Phi }\right) \) are local slice coordinates for \( M \) .]

In treating manifolds with boundary, many constructions can be simplified by viewing a manifold with boundary as being embedded in a larger manifold without boundary. Here is one way to do that.

If \( M \) is a topological manifold with nonempty boundary, the double of \( M \) is the quotient space \( D\left( M\right) \) formed from the disjoint union of two copies of \( M \) (say \( {M}_{1} \) and \( {M}_{2} \) ), by identifying each point in \( \partial {M}_{1} \) with the corresponding point in \( \partial {M}_{2} \) .

Proposition A.31. [LeeSM, Example 9.32] Suppose \( M \) is a smooth manifold with nonempty boundary. Then \( D\left( M\right) \) is a topological manifold without boundary, and it has a smooth structure such that the natural maps \( M \rightarrow  {M}_{1} \rightarrow  D\left( M\right) \) and \( M \rightarrow \; {M}_{2} \rightarrow  D\left( M\right) \) are smooth embeddings. Moreover, \( D\left( M\right) \) is compact if and only if \( M \) is compact, and connected if and only if \( M \) is connected.

## Vector Bundles

Suppose \( M \) is a smooth manifold with or without boundary. The tangent bundle of \( M \) , denoted by \( {TM} \) , is the disjoint union of the tangent spaces at all points of \( M \) : \( {TM} = \mathop{\coprod }\limits_{{p \in  M}}{T}_{p}M \) . This set can be thought of both as a union of vector spaces and as a manifold in its own right. This kind of structure, called a vector bundle, is extremely common in differential geometry, so we take some time to review the definitions and basic properties of vector bundles.

For any positive integer \( k \) , a smooth vector bundle of rank \( k \) is a pair of smooth manifolds \( E \) and \( M \) with or without boundary, together with a smooth surjective map \( \pi  : E \rightarrow  M \) satisfying the following conditions:

(i) For each \( p \in  M \) , the set \( {E}_{p} = {\pi }^{-1}\left( p\right) \) is endowed with the structure of a \( k \) -dimensional real vector space.

(ii) For each \( p \in  M \) , there exist a neighborhood \( U \) of \( p \) and a diffeomorphism \( \Phi  : {\pi }^{-1}\left( U\right)  \rightarrow  U \times  {\mathbb{R}}^{k} \) such that \( {\pi }_{U} \circ  \Phi  = \pi \) , where \( {\pi }_{U} : U \times  {\mathbb{R}}^{k} \rightarrow  U \) is the projection onto the first factor; and for each \( q \in  U,\Phi \) restricts to a linear isomorphism from \( {E}_{q} \) to \( \{ q\}  \times  {\mathbb{R}}^{k} \cong  {\mathbb{R}}^{k} \) .

The space \( M \) is called the base of the bundle, \( E \) is called its total space, and \( \pi \) is its projection. Each set \( {E}_{p} = {\pi }^{-1}\left( p\right) \) is called the fiber of \( E \) over \( p \) , and each diffeomorphism \( \Phi  : {\pi }^{-1}\left( U\right)  \rightarrow  U \times  {\mathbb{R}}^{k} \) described above is called a smooth local trivialization.

It frequently happens that we are presented with a collection of vector spaces (such as tangent spaces), one for each point in a manifold, that we would like to "glue together" to form a vector bundle. There is a shortcut for showing that such a collection forms a vector bundle without first constructing a smooth manifold structure on the total space. As the next lemma shows, all we need to do is to exhibit the maps that we wish to regard as local trivializations and check that they overlap correctly.

Lemma A.32 (Vector Bundle Chart Lemma). [LeeSM, Lemma 10.6] Let \( M \) be a smooth manifold with or without boundary, and suppose that for each \( p \in  M \) we are given a real vector space \( {E}_{p} \) of some fixed dimension \( k \) . Let \( E = \mathop{\coprod }\limits_{{p \in  M}}{E}_{p} \) (the disjoint union of all the spaces \( {E}_{p} \) ), and let \( \pi  : E \rightarrow  M \) be the map that takes each element of \( {E}_{p} \) to the point \( p \) . Suppose furthermore that we are given

(i) an indexed open cover \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  A} \) of \( M \) ;

(ii) for each \( \alpha  \in  A \) , a bijective map \( {\Phi }_{\alpha } : {\pi }^{-1}\left( {U}_{\alpha }\right)  \rightarrow  {U}_{\alpha } \times  {\mathbb{R}}^{k} \) whose restriction to each \( {E}_{p} \) is a linear isomorphism from \( {E}_{p} \) to \( \{ p\}  \times  {\mathbb{R}}^{k} \cong  {\mathbb{R}}^{k} \) ;

(iii) for each \( \alpha ,\beta  \in  A \) such that \( {U}_{\alpha } \cap  {U}_{\beta } \neq  \varnothing \) , a smooth map \( {\tau }_{\alpha \beta } : {U}_{\alpha } \cap  {U}_{\beta } \rightarrow \; \mathrm{{GL}}\left( {k,\mathbb{R}}\right) \) such that the composite map \( {\Phi }_{\alpha } \circ  {\Phi }_{\beta }^{-1} \) from \( \left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)  \times  {\mathbb{R}}^{k} \) to itself has the form

\[
{\Phi }_{\alpha } \circ  {\Phi }_{\beta }^{-1}\left( {p, v}\right)  = \left( {p,{\tau }_{\alpha \beta }\left( p\right) v}\right) . \tag{A.6}
\]

Then \( E \) has a unique smooth manifold structure making it a smooth vector bundle of rank \( k \) over \( M \) , with \( \pi \) as projection and the maps \( {\Phi }_{\alpha } \) as smooth local trivializations.

The smooth \( {GL}\left( {k,\mathbb{R}}\right) \) -valued maps \( {\tau }_{\alpha \beta } \) of this lemma are called transition functions for \( E \) .

If \( \pi  : E \rightarrow  M \) is a smooth vector bundle over \( M \) , then as section of \( E \) is a continuous map \( \sigma  : M \rightarrow  E \) such that \( \pi  \circ  \sigma  = {\operatorname{Id}}_{M} \) , or equivalently, \( \sigma \left( p\right)  \in  {E}_{p} \) for all \( p \) . If \( U \subseteq  M \) is an open set, then a local section of \( E \) over \( \mathbf{U} \) is a continuous map \( \sigma  : U \rightarrow  E \) satisfying the analogous equation \( \pi  \circ  \sigma  = {\operatorname{Id}}_{U} \) . A smooth (local or global) section of \( E \) is just a section that is smooth as a map between smooth manifolds. If we need to speak of "sections" that are not necessarily continuous, we use the following terminology: a rough (local) section of \( E \) is a map \( \sigma  : U \rightarrow  E \) defined on some open set \( U \subseteq  M \) , not necessarily smooth or even continuous, such that \( \pi  \circ  \sigma  = {\operatorname{Id}}_{U} \) .

A local frame for \( E \) is an ordered \( k \) -tuple \( \left( {{\sigma }_{1},\ldots ,{\sigma }_{k}}\right) \) of local sections over an open set \( U \) whose values at each \( p \in  U \) constitute a basis for \( {E}_{p} \) . It is called a global frame if \( U = M \) . If \( \tau \) is a (local or global) section of \( E \) and \( \left( {{\sigma }_{1},\ldots ,{\sigma }_{k}}\right) \) is a local frame for \( E \) over \( U \subseteq  M \) , then the value of \( \tau \) at each \( p \in  U \) can be written

\[
\tau \left( p\right)  = {\tau }^{i}\left( p\right) {\sigma }_{i}\left( p\right)
\]

for some functions \( {\tau }^{1},\ldots ,{\tau }^{k} : U \rightarrow  \mathbb{R} \) , called the component functions of \( \sigma \) with respect to the given frame.

The next lemma gives a criterion for smoothness that is usually easy to verify in practice.

Lemma A.33 (Local Frame Criterion for Smoothness). [LeeSM, Prop. 10.22] Let \( \pi  : E \rightarrow  M \) be a smooth vector bundle, and let \( \tau  : M \rightarrow  E \) be a rough section. If \( \left( {\sigma }_{i}\right) \) is a smooth local frame for \( E \) over an open subset \( U \subseteq  M \) , then \( \tau \) is smooth on \( U \) if and only if its component functions with respect to \( \left( {\sigma }_{i}\right) \) are smooth.

If \( E \rightarrow  M \) is a smooth vector bundle, then the set of smooth sections of \( E \) , denoted by \( \Gamma \left( E\right) \) , is a vector space (usually infinite-dimensional) under pointwise addition and multiplication by constants. Its zero element is the zero section \( \zeta \) defined by \( \zeta \left( p\right)  = 0 \in  {E}_{p} \) for all \( p \in  M \) . For every section \( \sigma \) of \( E \) , the support of \( \sigma \) is the closure of the set \( \{ p \in  M : \sigma \left( p\right)  \neq  0\} \) .

Given a smooth vector bundle \( {\pi }_{E} : E \rightarrow  M \) , a smooth subbundle of \( \mathbf{E} \) is a smooth vector bundle \( {\pi }_{D} : D \rightarrow  M \) , in which \( D \) is an embedded submanifold (with or without boundary) of \( E \) and \( {\pi }_{D} = {\left. {\pi }_{E}\right| }_{D} \) , such that for each \( p \in  M \) , the subset \( {D}_{p} = D \cap  {E}_{p} \) is a linear subspace of \( {E}_{p} \) , and the vector space structure on \( {D}_{p} \) is the one inherited from \( {E}_{p} \) . Given a collection of subspaces \( {D}_{p} \subseteq  {E}_{p} \) , one for each \( p \in  M \) , the following lemma gives a convenient condition for checking that their union is a smooth subbundle.

Lemma A.34 (Local Frame Criterion for Subbundles). [LeeSM, Lemma 10.32] Let \( \pi  : E \rightarrow  M \) be a smooth vector bundle, and suppose that for each \( p \in  M \) we are given a \( k \) -dimensional linear subspace \( {D}_{p} \subseteq  {E}_{p} \) . Suppose further that each \( p \in  M \) has a neighborhood \( U \) on which there are smooth local sections \( {\sigma }_{1},\ldots ,{\sigma }_{k} : U \rightarrow  E \) such that \( {\sigma }_{1}\left( q\right) ,\ldots ,{\sigma }_{k}\left( q\right) \) form a basis for \( {D}_{q} \) at each \( q \in  U \) . Then \( D = \mathop{\bigcup }\limits_{{p \in  M}}{D}_{p} \subseteq  E \) is a smooth subbundle of \( E \) .

Suppose \( \widetilde{M} \) is a smooth manifold with or without boundary, and \( M \subseteq  \widetilde{M} \) is an immersed or embedded submanifold with or without boundary. If \( E \rightarrow  \widetilde{M} \) is any smooth rank- \( k \) vector bundle over \( \widetilde{M} \) , we obtain a smooth vector bundle \( {\left. \pi \right| }_{M} : {\left. E\right| }_{M} \rightarrow  M \) of rank \( k \) over \( M \) , called the restriction of \( E \) to \( M \) , whose total space is \( {\left. E\right| }_{M} = {\pi }^{-1}\left( M\right) \) , whose fiber at each \( p \in  M \) is exactly the fiber of \( E \) , and whose local trivializations are the restrictions of the local trivializations of \( E \) . (See [LeeSM, Example 10.8].)

Every smooth section of \( E \) restricts to a smooth section of \( {\left. E\right| }_{M} \) . Conversely, the next exercise shows that in most cases, smooth sections of \( {\left. E\right| }_{M} \) extend to smooth sections of \( E \) , at least locally near \( M \) .

- Exercise A.35. Suppose \( \widetilde{M} \) is a smooth manifold, \( E \rightarrow  \widetilde{M} \) is a smooth vector bundle, and \( M \subseteq  \widetilde{M} \) is an embedded submanifold. Show that every smooth section of the restricted bundle \( {\left. E\right| }_{M} \) can be extended to a smooth section of \( E \) on a neighborhood of \( M \) in \( \widetilde{M} \) ; and if \( M \) is closed in \( \widetilde{M} \) , the neighborhood can be taken to be all of \( \widetilde{M} \) .

## The Tangent Bundle and Vector Fields

We continue to assume that \( M \) is a smooth manifold with or without boundary. In this section, we see how the theory of vector bundles applies to the particular case of the tangent bundle.

Given any smooth local coordinate chart \( \left( {U,\left( {x}^{i}\right) }\right) \) for \( M \) , we can define a local trivialization of \( {TM} \) over \( U \) by letting \( \Phi  : {\pi }^{-1}\left( U\right)  \rightarrow  U \times  {\mathbb{R}}^{n} \) be the map sending \( v \in  {T}_{p}M \) to \( \left( {p,\left( {{v}^{1},\ldots ,{v}^{n}}\right) }\right) \) , where \( {v}^{i}\partial /{\left. \partial {x}^{i}\right| }_{p} \) is the coordinate representation for \( v \) . Given another such chart \( \left( {\widetilde{U},\left( {\widetilde{x}}^{i}\right) }\right) \) for \( M \) , we obtain a corresponding local trivialization \( \widetilde{\Phi }\left( v\right)  = \left( {p,\left( {{\widetilde{v}}^{1},\ldots ,{\widetilde{v}}^{n}}\right) }\right) \) , where \( v = {\widetilde{v}}^{i}\partial /{\left. \partial {\widetilde{x}}^{i}\right| }_{p} \) . The transformation law for coordinate vectors shows that

\[
{\widetilde{v}}^{j} = \frac{\partial {\widetilde{x}}^{j}}{\partial {x}^{i}}\left( p\right) {v}^{i},
\]

so the transition function between two such charts is given by the smooth matrix-valued function \( \left( {\partial {\widetilde{x}}^{j}/\partial {x}^{i}}\right) \) . Thus the chart lemma shows that these local trivializa-tions turn \( {TM} \) into a smooth vector bundle.

A smooth coordinate chart \( \left( {x}^{i}\right) \) for \( M \) also yields smooth local coordinates \( \left( {{x}^{1},\ldots ,{x}^{n},{v}^{1},\ldots ,{v}^{n}}\right) \) on \( {\pi }^{-1}\left( U\right)  \subseteq  {TM} \) , called natural coordinates for \( \mathbf{{TM}} \) , by following the local trivialization \( \Phi \) with the map \( U \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \times  {\mathbb{R}}^{n} \) that sends \( \left( {p,\left( {{v}^{1},\ldots ,{v}^{n}}\right) }\right) \) to \( \left( {{x}^{1}\left( p\right) ,\ldots ,{x}^{n}\left( p\right) ,{v}^{1},\ldots ,{v}^{n}}\right) \) .

A section of \( {TM} \) is called a vector field on \( \mathbf{M} \) . To avoid confusion between the point \( p \in  M \) at which a vector field is evaluated and the action of the vector field on a function, we usually write the value of a vector field \( X \) at \( p \in  M \) as \( {X}_{p} \in  {T}_{p}M \) , or, if it is clearer (for example if \( X \) itself has one or more subscripts), as \( {\left. X\right| }_{p} \) .

For example, if \( \left( {U,\left( {x}^{i}\right) }\right) \) is a smooth coordinate chart for \( M \) , for each \( i \) we get a smooth coordinate vector field on \( U \) , denoted by \( \partial /\partial {x}^{i} \) (and often abbreviated by \( {\partial }_{i} \) if no confusion results), whose value at \( p \in  U \) is the coordinate vector \( \partial /{\left. \partial {x}^{i}\right| }_{p} \) defined above. Each coordinate vector field is smooth because its coordinate representation in natural coordinates is \( \left( {{x}^{1},\ldots ,{x}^{n}}\right)  \mapsto  \left( {{x}^{1},\ldots ,{x}^{n},0,\ldots ,0,1,0,\ldots ,0}\right) \) . The vector fields \( {\partial }_{1},\ldots ,{\partial }_{n} \) form a smooth local frame for \( {TM} \) , called a coordinate frame.

It follows from Lemma A.33 that a vector field is smooth if and only if its components are smooth with respect to some smooth local frame (such as a coordinate frame) in a neighborhood of each point. It is standard to use the notation \( \mathfrak{X}\left( M\right) \) as another name for \( \Gamma \left( {TM}\right) \) , the space of all smooth vector fields on \( M \) .

Now suppose \( M \) and \( N \) are smooth manifolds with or without boundary, and \( F : M \rightarrow  N \) is a smooth map. We obtain a smooth map \( {dF} : {TM} \rightarrow  {TN} \) , called the global differential of \( \mathbf{F} \) , whose restriction to each tangent space \( {T}_{p}M \) is the linear map \( d{F}_{p} \) defined above. In general, the global differential does not take vector fields to vector fields. In the special case that \( X \in  \mathfrak{X}\left( M\right) \) and \( Y \in  \mathfrak{X}\left( N\right) \) are vector fields such that \( {dF}\left( {X}_{p}\right)  = {Y}_{F\left( p\right) } \) for all \( p \in  M \) , we say that the vector fields \( X \) and \( Y \) are F-related.

Lemma A.36. [LeeSM, Prop. 8.19 &Cor. 8.21] Let \( F : M \rightarrow  N \) be a diffeomorphism between smooth manifolds with or without boundary. For every \( X \in  \mathfrak{X}\left( M\right) \) , there is a unique vector field \( {F}_{ * }X \in  \mathfrak{X}\left( N\right) \) , called the pushforward of \( \mathbf{X} \) , that is \( F \) -related to \( X \) . For every \( f \in  {C}^{\infty }\left( N\right) \) , it satisfies

\[
\left( {\left( {{F}_{ * }X}\right) f}\right)  \circ  F = X\left( {f \circ  F}\right) . \tag{A.7}
\]

Suppose \( X \in  \mathfrak{X}\left( M\right) \) . Given a real-valued function \( f \in  {C}^{\infty }\left( M\right) \) , applying \( X \) to \( f \) yields a new function \( {Xf} \in  {C}^{\infty }\left( M\right) \) by \( {Xf}\left( p\right)  = {X}_{p}f \) . The defining equation (A.1) for tangent vectors translates into the following product rule for vector fields:

\[
X\left( {fg}\right)  = {fXg} + {gXf}. \tag{A.8}
\]

A map \( X : {C}^{\infty }\left( M\right)  \rightarrow  {C}^{\infty }\left( M\right) \) is called a derivation of \( {C}^{\infty }\left( \mathbf{M}\right) \) (as opposed to a derivation at a point) if it is linear over \( \mathbb{R} \) and satisfies (A.8) for all \( f, g \in  {C}^{\infty }\left( M\right) \) .

Lemma A.37. [LeeSM, Prop. 8.15] Let \( M \) be a smooth manifold with or without boundary. A map \( D : {C}^{\infty }\left( M\right)  \rightarrow  {C}^{\infty }\left( M\right) \) is a derivation if and only if it is of the form \( {Df} = {Xf} \) for some \( X \in  \mathfrak{X}\left( M\right) \) .

Given smooth vector fields \( X, Y \in  \mathfrak{X}\left( M\right) \) , define a map \( \left\lbrack  {X, Y}\right\rbrack   : {C}^{\infty }\left( M\right)  \rightarrow \; {C}^{\infty }\left( M\right) \) by

\[
\left\lbrack  {X, Y}\right\rbrack  f = X\left( {Yf}\right)  - Y\left( {Xf}\right) .
\]

A straightforward computation shows that \( \left\lbrack  {X, Y}\right\rbrack \) is a derivation of \( {C}^{\infty }\left( M\right) \) , and thus by Lemma A.37 it defines a smooth vector field, called the Lie bracket of \( X \) and \( Y \) .

Proposition A.38 (Properties of Lie Brackets). [LeeSM, Prop. 8.28] Let \( M \) be a smooth manifold with or without boundary and \( X, Y, Z \in  \mathfrak{X}\left( M\right) \) .

(a) \( \left\lbrack  {X, Y}\right\rbrack \) is bilinear over \( \mathbb{R} \) as a function of \( X \) and \( Y \) .

(b) \( \left\lbrack  {X, Y}\right\rbrack   =  - \left\lbrack  {Y, X}\right\rbrack \) (antisymmetry).

(c) \( \left\lbrack  {X,\left\lbrack  {Y, Z}\right\rbrack  }\right\rbrack   + \left\lbrack  {Y,\left\lbrack  {Z, X}\right\rbrack  }\right\rbrack   + \left\lbrack  {Z,\left\lbrack  {X, Y}\right\rbrack  }\right\rbrack   = 0 \) (Jacobi identity).

(d) For \( f, g \in  {C}^{\infty }\left( M\right) ,\left\lbrack  {{fX},{gY}}\right\rbrack   = {fg}\left\lbrack  {X, Y}\right\rbrack   + \left( {fXg}\right) Y - \left( {gYf}\right) X \) .

Proposition A.39 (Naturality of Lie Brackets). [LeeSM, Prop. 8.30 & Cor. 8.31] Let \( F : M \rightarrow  N \) be a smooth map between manifolds with or without boundary, and let \( {X}_{1},{X}_{2} \in  \mathfrak{X}\left( M\right) \) and \( {Y}_{1},{Y}_{2} \in  \mathfrak{X}\left( N\right) \) be vector fields such that \( {X}_{i} \) is \( F \) -related to \( {Y}_{i} \) for \( i = 1,2 \) . Then \( \left\lbrack  {{X}_{1},{X}_{2}}\right\rbrack \) is \( F \) -related to \( \left\lbrack  {{Y}_{1},{Y}_{2}}\right\rbrack \) . In particular, if \( F \) is a diffeomorphism, then \( {F}_{ * }\left\lbrack  {{X}_{1},{X}_{2}}\right\rbrack   = \left\lbrack  {{F}_{ * }{X}_{1},{F}_{ * }{X}_{2}}\right\rbrack \) .

Now suppose \( \widetilde{M} \) is a smooth manifold with or without boundary and \( M \subseteq  \widetilde{M} \) is an immersed or embedded submanifold with or without boundary. The bundle \( T\widetilde{M}{ \mid  }_{M} \) , obtained by restricting \( T\widetilde{M} \) to \( M \) , is called the ambient tangent bundle. It is a smooth bundle over \( M \) whose rank is equal to the dimension of \( \widetilde{M} \) . The tangent bundle \( {TM} \) is naturally viewed as a smooth subbundle of \( T\widetilde{M}{\lfloor }_{M} \) , and smooth vector fields on \( M \) can also be viewed as smooth sections of \( {\left. T\widetilde{M}\right| }_{M} \) . A vector field \( X \in  \mathcal{X}\left( \widetilde{M}\right) \) always restricts to a smooth section of \( {\left. T\widetilde{M}\right| }_{M} \) , and it restricts to a smooth section of \( {TM} \) if and only if it is tangent to \( M \) , meaning that \( {X}_{p} \in  {T}_{p}M \subseteq  {T}_{p}\widetilde{M} \) for each \( p \in  M \) .

Corollary A.40 (Brackets of Vector Fields Tangent to Submanifolds). [LeeSM, Cor. 8.32] Let \( \widetilde{M} \) be a smooth manifold and let \( M \) be an immersed submanifold with or without boundary in \( \widetilde{M} \) . If \( {Y}_{1} \) and \( {Y}_{2} \) are smooth vector fields on \( \widetilde{M} \) that are tangent to \( M \) , then \( \left\lbrack  {{Y}_{1},{Y}_{2}}\right\rbrack \) is also tangent to \( M \) .

Exercise A.41. Let \( \widetilde{\mathbf{M}} \) be a smooth manifold with or without boundary and let \( M \subseteq \; \widetilde{M} \) be an embedded submanifold with or without boundary. Show that a vector field \( X \in \; \mathcal{X}\left( \widetilde{M}\right) \) is tangent to \( M \) if and only if \( {\left. \left( Xf\right) \right| }_{M} = 0 \) whenever \( f \in  {C}^{\infty }\left( \widetilde{M}\right) \) is a function that vanishes on \( M \) .

## Integral Curves and Flows

A curve in a smooth manifold \( M \) (with or without boundary) is a continuous map \( \gamma  : I \rightarrow  M \) , where \( I \subseteq  \mathbb{R} \) is some interval. If \( \gamma \) is smooth, then for each \( {t}_{0} \in  I \) we obtain a vector \( {\gamma }^{\prime }\left( {t}_{0}\right)  = d{\gamma }_{{t}_{0}}\left( {d/{\left. dt\right| }_{{t}_{0}}}\right) \) , called the velocity of \( \gamma \) at time \( {t}_{0} \) . It acts on functions by

\[
{\gamma }^{\prime }\left( {t}_{0}\right) f = {\left( f \circ  \gamma \right) }^{\prime }\left( {t}_{0}\right) .
\]

In any smooth local coordinates, the coordinate expression for \( {\gamma }^{\prime }\left( {t}_{0}\right) \) is exactly the same as it would be in \( {\mathbb{R}}^{n} \) : the components of \( {\gamma }^{\prime }\left( {t}_{0}\right) \) are the ordinary \( t \) -derivatives of the components of \( \gamma \) .

If \( X \in  \mathfrak{X}\left( M\right) \) , then a smooth curve \( \gamma  : I \rightarrow  M \) is called an integral curve of \( X \) if its velocity at each point is equal to the value of \( X \) there: \( {\gamma }^{\prime }\left( t\right)  = {X}_{\gamma \left( t\right) } \) for each \( t \in  I \) .

The fundamental fact about vector fields (at least in the case of manifolds without boundary) is that there exists a unique maximal integral curve starting at each point, varying smoothly as the point varies. These integral curves are all encoded into a global object called a flow, which we now define.

Given a smooth manifold \( M \) (without boundary), a flow domain for \( M \) is an open subset \( \mathcal{D} \subseteq  \mathbb{R} \times  M \) with the property that for each \( p \in  M \) , the set \( {\mathcal{D}}^{\left( p\right) } = \; \{ t \in  \mathbb{R} : \left( {t, p}\right)  \in  \mathcal{D}\} \) is an open interval containing 0 . Given a flow domain \( \mathcal{D} \) and a map \( \theta  : \mathcal{D} \rightarrow  M \) , for each \( t \in  \mathbb{R} \) we let \( {M}_{t} = \{ p \in  M : \left( {t, p}\right)  \in  \mathcal{D}\} \) , and we define maps \( {\theta }_{t} : {M}_{t} \rightarrow  M \) and \( {\theta }^{\left( p\right) } : {\mathcal{D}}^{\left( p\right) } \rightarrow  M \) by \( {\theta }_{t}\left( p\right)  = {\theta }^{\left( p\right) }\left( t\right)  = \theta \left( {t, p}\right) \) .

A flow on \( M \) is a continuous map \( \theta  : \mathcal{D} \rightarrow  M \) , where \( \mathcal{D} \subseteq  \mathbb{R} \times  M \) is a flow domain, that satisfies

\[
{\theta }_{0} = {\operatorname{Id}}_{M}
\]

\[
{\theta }_{t} \circ  {\theta }_{s}\left( p\right)  = {\theta }_{t + s}\left( p\right) \;\text{ wherever both sides are defined. }
\]

If \( \theta \) is a smooth flow, we obtain a smooth vector field \( X \in  \mathfrak{X}\left( M\right) \) defined by \( {X}_{p} = \; {\left( {\theta }^{\left( p\right) }\right) }^{\prime }\left( 0\right) \) , called the infinitesimal generator of \( \theta \) .

Theorem A.42 (Fundamental Theorem on Flows). [LeeSM, Thm. 9.12] Let \( X \) be a smooth vector field on a smooth manifold \( M \) (without boundary). There is a unique smooth maximal flow \( \theta  : \mathcal{D} \rightarrow  M \) whose infinitesimal generator is \( X \) . This flow has the following properties:

(a) For each \( p \in  M \) , the curve \( {\theta }^{\left( p\right) } : {\mathcal{D}}^{\left( p\right) } \rightarrow  M \) is the unique maximal integral curve of \( X \) starting at \( p \) .

(b) If \( s \in  {\mathcal{D}}^{\left( p\right) } \) , then \( {\mathcal{D}}^{\left( \theta \left( s, p\right) \right) } \) is the interval \( {\mathcal{D}}^{\left( p\right) } - s = \left\{  {t - s : t \in  {\mathcal{D}}^{\left( p\right) }}\right\} \) .

(c) For each \( t \in  \mathbb{R} \) , the set \( {M}_{t} \) is open in \( M \) , and \( {\theta }_{t} : {M}_{t} \rightarrow  {M}_{-t} \) is a diffeomorphism with inverse \( {\theta }_{-t} \) .

Although the fundamental theorem guarantees only that each point lies on an integral curve that exists for a short time, the next lemma can often be used to prove that a particular integral curve exists for all time.

Lemma A.43 (Escape Lemma). Suppose \( M \) is a smooth manifold and \( X \in  \mathfrak{X}\left( M\right) \) . If \( \gamma  : I \rightarrow  M \) is a maximal integral curve of \( X \) whose domain I has a finite least upper bound \( b \) , then for every \( {t}_{0} \in  I,\gamma \left( \left\lbrack  {{t}_{0}, b}\right) \right) \) is not contained in any compact subset of \( M \) .

- Exercise A.44. Prove the escape lemma.

Proposition A.45 (Canonical Form for a Vector Field). [LeeSM, Thm. 9.22] Let \( X \) be a smooth vector field on a smooth manifold \( M \) , and suppose \( p \in  M \) is a point where \( {X}_{p} \neq  0 \) . There exist smooth coordinates \( \left( {x}^{i}\right) \) on some neighborhood of \( p \) in which \( X \) has the coordinate representation \( \partial /\partial {x}^{1} \) .

The fundamental theorem on flows leads to a way of differentiating one vector field along the flow of another. Suppose \( M \) is a smooth manifold, \( X, Y \in  \mathcal{X}\left( M\right) \) , and \( \theta \) is the flow of \( X \) . The Lie derivative of \( Y \) with respect to \( X \) is the vector field \( {\mathcal{L}}_{X}Y \) defined by

\[
{\left( {\mathcal{L}}_{X}Y\right) }_{p} = {\left. \frac{d}{dt}\right| }_{t = 0}d{\left( {\theta }_{-t}\right) }_{{\theta }_{t}\left( p\right) }\left( {Y}_{{\theta }_{t}\left( p\right) }\right)  = \mathop{\lim }\limits_{{t \rightarrow  0}}\frac{d{\left( {\theta }_{-t}\right) }_{{\theta }_{t}\left( p\right) }\left( {Y}_{{\theta }_{t}\left( p\right) }\right)  - {Y}_{p}}{t}.
\]

This formula is useless for computation, however, because typically the flow of a vector field is difficult or impossible to compute explicitly. Fortunately, there is another expression for the Lie derivative that is much easier to compute.

Proposition A.46. [LeeSM, Thm. 9.38] Suppose \( M \) is a smooth manifold and \( X, Y \in  \mathfrak{X}\left( M\right) \) . The Lie derivative of \( Y \) with respect to \( X \) is equal to the Lie bracket \( \left\lbrack  {X, Y}\right\rbrack \) .

One of the most important applications of the Lie derivative is as an obstruction to invariance under a flow. If \( \theta \) is a smooth flow, we say that a vector field \( Y \) is invariant under \( \theta \) if \( {\left( {\theta }_{t}\right) }_{ * }Y = Y \) wherever the left-hand side is defined.

Proposition A.47. [LeeSM, Thm. 9.42] Let \( M \) be a smooth manifold and \( X \in \; \mathcal{X}\left( M\right) \) . A smooth vector field is invariant under the flow of \( X \) if and only if its Lie derivative with respect to \( X \) is identically zero.

A \( k \) -tuple of vector fields \( {X}_{1},\ldots ,{X}_{k} \) is said to commute if \( \left\lbrack  {{X}_{i},{X}_{j}}\right\rbrack   = 0 \) for each \( i \) and \( j \) .

Proposition A.48 (Canonical Form for Commuting Vector Fields). [LeeSM, Thm. 9.46] Let \( M \) be a smooth n-manifold, and let \( \left( {{X}_{1},\ldots ,{X}_{k}}\right) \) be a linearly independent \( k \) -tuple of smooth commuting vector fields on an open subset \( W \subseteq  M \) . For each \( p \in  W \) , there exists a smooth coordinate chart \( \left( {U,\left( {x}^{i}\right) }\right) \) centered at \( p \) such that \( {X}_{i} = \partial /\partial {x}^{i} \) for \( i = 1,\ldots , k \) .

## Smooth Covering Maps

A covering map is a surjective continuous map \( \pi  : \widetilde{M} \rightarrow  M \) between connected and locally path-connected topological spaces, for which each point of \( M \) has connected neighborhood \( U \) that is evenly covered, meaning that each connected component of \( {\pi }^{-1}\left( U\right) \) is mapped homeomorphically onto \( U \) by \( \pi \) . It is called a smooth covering map if \( \widetilde{M} \) and \( M \) are smooth manifolds with or without boundary and each component of \( {\pi }^{-1}\left( U\right) \) is mapped diffeomorphically onto \( U \) . For every evenly covered open set \( U \subseteq  M \) , the components of \( {\pi }^{-1}\left( U\right) \) are called the sheets of the covering over \( \mathbf{U} \) .

Here are the main properties of covering maps that we need.

Proposition A.49 (Elementary Properties of Smooth Covering Maps). [LeeSM, Prop. 4.33]

(a) Every smooth covering map is a local diffeomorphism, a smooth submersion, an open map, and a quotient map.

(b) An injective smooth covering map is a diffeomorphism.

(c) A topological covering map is a smooth covering map if and only if it is a local diffeomorphism.

Proposition A.50 A covering map is a proper map if and only if it is finite-sheeted.

- Exercise A.51. Prove the preceding proposition.

Example A.52 (A Covering of the \( n \) -Torus). The \( n \) -torus is the manifold \( {\mathbb{T}}^{n} = \; {\mathbb{S}}^{1} \times  \cdots  \times  {\mathbb{S}}^{1} \) , regarded as the subset of \( {\mathbb{R}}^{2n} \) defined by \( {\left( {x}^{1}\right) }^{2} + {\left( {x}^{2}\right) }^{2} = \cdots  = \; {\left( {x}^{{2n} - 1}\right) }^{2} + {\left( {x}^{2n}\right) }^{2} = 1 \) . The smooth map \( X : {\mathbb{R}}^{n} \rightarrow  {\mathbb{T}}^{n} \) given by \( X\left( {{u}^{1},\ldots ,{u}^{n}}\right)  = \; \left( {\cos {u}^{1},\sin {u}^{1},\ldots ,\cos {u}^{n},\sin {u}^{n}}\right) \) is a smooth covering map.

If \( \pi  : \widetilde{M} \rightarrow  M \) is a covering map and \( F : B \rightarrow  M \) is a continuous map from a topological space \( B \) into \( M \) , then a lift of \( \mathbf{F} \) is a continuous map \( \widetilde{F} : B \rightarrow  \widetilde{M} \) such that \( \pi  \circ  \widetilde{F} = F \) .

Proposition A.53 (Lifts of Smooth Maps are Smooth). If \( \pi  : \widetilde{M} \rightarrow  M \) is a smooth covering map, \( B \) is a smooth manifold with or without boundary, and \( F : B \rightarrow  M \) is a smooth map, then every lift of \( F \) is smooth.

Proof. Since \( \pi \) is a smooth submersion, every lift \( \widetilde{F} : B \rightarrow  \widetilde{M} \) can be written locally as \( \widetilde{F} = \sigma  \circ  F \) , where \( \sigma \) is a smooth local section of \( \pi \) (see Thm. A.17).

Proposition A.54 (Lifting Properties of Covering Maps). Suppose \( \pi  : \widetilde{M} \rightarrow  M \) is a covering map.

(a) UNIQUE LIFTING PROPERTY [LeeTM, Thm. 11.12] If \( B \) is a connected topological space and \( F : B \rightarrow  M \) is a continuous map, then any two lifts of \( F \) that agree at one point are identical.

(b) PATH LIFTING PROPERTY [LeeTM, Cor. 11.14] Suppose \( f : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) is a continuous path. For every \( \widetilde{p} \in  {\pi }^{-1}\left( {f\left( 0\right) }\right) \) , there exists a unique lift \( \widetilde{f} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \widetilde{M} \) of \( f \) such that \( \widetilde{f}\left( 0\right)  = \widetilde{p} \) .

(c) MONODROMY THEOREM [LeeTM, Thm. 11.15] Suppose \( f, g : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) are path-homotopic paths and \( \widetilde{f},\widetilde{g} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \widetilde{M} \) are their lifts starting at the same point. Then \( \widetilde{f} \) and \( \widetilde{g} \) are path-homotopic and \( \widetilde{f}\left( 1\right)  = \widetilde{g}\left( 1\right) \) .

Theorem A.55 (Injectivity Theorem). [LeeTM, Thm. 11.16] If \( \pi  : \widetilde{M} \rightarrow  M \) is a covering map, then for each point \( \widetilde{x} \in  \widetilde{M} \) , the induced fundamental group homomorphism \( {\pi }_{ * } : {\pi }_{1}\left( {\widetilde{M},\widetilde{x}}\right)  \rightarrow  {\pi }_{1}\left( {M,\pi \left( \widetilde{x}\right) }\right) \) is injective.

Theorem A.56 (Lifting Criterion). [LeeTM, Thm. 11.18] Suppose \( \pi  : \widetilde{M} \rightarrow  M \) is a covering map, \( B \) is a connected and locally path-connected topological space, and \( F : B \rightarrow  M \) is a continuous map. Given \( b \in  B \) and \( \widetilde{x} \in  \widetilde{M} \) such that \( \pi \left( \widetilde{x}\right)  = F\left( b\right) \) , the map \( F \) has a lift to \( \widetilde{M} \) if and only if \( {F}_{ * }\left( {{\pi }_{1}\left( {B, b}\right) }\right)  \subseteq  {\pi }_{ * }\left( {{\pi }_{1}\left( {\widetilde{M},\widetilde{x}}\right) }\right) \) .

Corollary A. 57 (Lifting Maps from Simply Connected Spaces). [LeeTM, Cor. 11.19] Suppose \( \pi  : \widetilde{M} \rightarrow  M \) and \( F : B \rightarrow  M \) satisfy the hypotheses of Theorem A.56, and in addition \( B \) is simply connected. Then every continuous map \( F : B \rightarrow \; M \) has a lift to \( \widetilde{M} \) . Given any \( b \in  B \) , the lift can be chosen to take \( b \) to any point in the fiber over \( F\left( b\right) \) .

Corollary A.58 (Covering Map Homeomorphism Criterion). A covering map \( \pi  : \widetilde{M} \rightarrow  M \) is a homeomorphism if and only if the induced homomorphism \( {\pi }_{ * } : {\pi }_{1}\left( {\widetilde{M},\widetilde{x}}\right)  \rightarrow  {\pi }_{1}\left( {M,\pi \left( \widetilde{x}\right) }\right) \) is surjective for some (hence every) \( \widetilde{x} \in  \widetilde{M}.A \) smooth covering map is a diffeomorphism if and only if the induced homomorphism is surjective.

Proof. By Theorem A.56, the hypothesis implies that the identity map Id: \( M \rightarrow  M \) has a lift Id: \( M \rightarrow  \widetilde{M} \) , which in this case is a continuous inverse for \( \pi \) . If \( \pi \) is a smooth covering map, then the lift is also smooth.

Corollary A.59 (Coverings of Simply Connected Spaces). [LeeTM, Cor. 11.33] If \( M \) is a simply connected manifold with or without boundary, then every covering of \( M \) is a homeomorphism, and if \( M \) is smooth, every smooth covering is a diffeomorphism.

Proposition A.60 (Existence of a Universal Covering Manifold). [LeeSM, Cor. 4.43] If \( M \) is a connected smooth manifold, then there exist a simply connected smooth manifold \( \widetilde{M} \) , called the universal covering manifold of \( M \) , and a smooth covering map \( \pi  : \widetilde{M} \rightarrow  M \) . It is unique in the sense that if \( {\widetilde{M}}^{\prime } \) is any other simply connected smooth manifold that admits a smooth covering map \( {\pi }^{\prime } : {\widetilde{M}}^{\prime } \rightarrow  M \) , then there exists a diffeomorphism \( \Phi  : \widetilde{M} \rightarrow  {\widetilde{M}}^{\prime } \) such that \( {\pi }^{\prime } \circ  \Phi  = \pi \) .

Proposition A.61. [LeeTM, Cor. 11.31] With \( \pi  : \widetilde{M} \rightarrow  M \) as in the previous proposition, each fiber of \( \pi \) has the same cardinality as the fundamental group of \( M \) .

Exercise A.62. Suppose \( \pi  : \widetilde{M} \rightarrow  M \) is a covering map. Show that \( \widetilde{M} \) is compact if and only if \( M \) is compact and \( \pi \) is a finite-sheeted covering.

We will revisit smooth covering maps at the end of Appendix C.
