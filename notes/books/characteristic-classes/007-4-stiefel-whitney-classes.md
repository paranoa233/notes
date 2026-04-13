# 4 Stiefel-Whitney Classes

This section will begin the study of characteristic classes by introducing four axioms which characterize the Stiefel-Whitney cohomology classes of a vector bundle. The existence and uniqueness of cohomology classes satisfying these axioms will only be established in later sections.

The expression \( {\mathrm{H}}^{i}\left( {B;G}\right) \) denotes the \( i \) -th singular cohomology group of \( B \) with coefficients in \( G \) . For an outline of basic definitions and theorems concerning singular cohomology theory, the reader is referred to appendix A. In this section the coefficient group will always be \( \mathbb{Z}/2 \) , the group of integers modulo 2 .

Axiom 1. To each vector bundle \( \xi \) there corresponds a sequence of cohomology classes

\[
{\mathrm{w}}_{i}\left( \xi \right)  \in  {\mathrm{H}}^{i}\left( {B\left( \xi \right) ;\mathbb{Z}/2}\right) ,\;i = 0,1,2,\ldots
\]

called the Stiefel-Whitney classes of \( \xi \) . The class \( {\mathrm{w}}_{0}\left( \xi \right) \) is equal to the unit element

\[
1 \in  {\mathrm{H}}^{0}\left( {B\left( \xi \right) ;\mathbb{Z}/2}\right) \text{ , }
\]

and \( {\mathrm{w}}_{i}\left( \xi \right) \) equals zero for \( i > n \) if \( \xi \) is an \( n \) -plane bundle.

Axiom 2 (Naturality). If \( f : B\left( \xi \right)  \rightarrow  B\left( \eta \right) \) is covered by a bundle map from \( \xi \) to \( \eta \) , then

\[
{\mathrm{w}}_{i}\left( \xi \right)  = {f}^{ * }{\mathrm{\;w}}_{i}\left( \eta \right) .
\]

Axiom 3 (The Whitney Product Theorem). If \( \xi \) and \( \eta \) are vector bundles over the same base space, then

\[
{\mathrm{w}}_{k}\left( {\xi  \oplus  \eta }\right)  = \mathop{\sum }\limits_{{i = 0}}^{k}{\mathrm{\;w}}_{i}\left( \xi \right)  \smile  {\mathrm{w}}_{k - i}\left( \eta \right) .
\]

For example \( {\mathrm{w}}_{1}\left( {\xi  \oplus  \eta }\right)  = {\mathrm{w}}_{1}\left( \xi \right)  + {\mathrm{w}}_{1}\left( \eta \right) \) ,

\[
{\mathrm{w}}_{2}\left( {\xi  \oplus  \eta }\right)  = {\mathrm{w}}_{2}\left( \xi \right)  + {\mathrm{w}}_{1}\left( \xi \right) {\mathrm{w}}_{1}\left( \eta \right)  + {\mathrm{w}}_{2}\left( \eta \right) ,\;\text{ etc }
\]

(We will omit the symbol \( \smile \) for cup product whenever it seems convenient.)

Axiom 4. For the line bundle \( {\gamma }_{1}^{1} \) over the circle \( {\mathbb{P}}^{1} \) , the Stiefel-Whitney class \( {\mathrm{w}}_{1}\left( {\gamma }_{1}^{1}\right) \) is non-zero.

Remark 4. Characteristic homology classes for the tangent bundle of a smooth manifold were defined by [Sti35] in 1935. In the same year [Whi36] defined the classes \( {\mathrm{w}}_{i} \) for any sphere bundle over a simplicial complex. (A "sphere bundle" is the object obtained from a Euclidean vector bundle by considering only vectors of unit length in the total space.) The Whitney product theorem is due to [Whi40]; [Whi41] and [Wu48]. This axiomatic definition of Stiefel-Whitney classes was suggested by Hirzebruch [Hir66, p. 58], where an analogous definition of Chern classes is given.

It is not at all obvious that classes \( {\mathrm{w}}_{i}\left( \xi \right) \) satisfying the four axioms can be defined. Nevertheless this will be assumed for the rest of this section. A number of applications of this assumption will be given.
