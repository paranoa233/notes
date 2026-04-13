# Chapter 1 Introduction

## Part I. Non-degenerate Smooth Functions on a Manifold

Based on lecture notes by

M. Spivak and R. Wells

In this section we will illustrate by a specific example the situation that we will investigate later for arbitrary manifolds. Let us consider a torus \( M \) , tangent to the plane \( V \) , as indicated in Figure 1.1.

![bo_d7du90alb0pc73deir8g_11_482_957_618_465_0.jpg](images/bo_d7du90alb0pc73deir8g_11_482_957_618_465_0.jpg)

Figure 1.1

Let \( f : M \rightarrow  \mathbf{R} \) ( \( \mathbf{R} \) always denotes the real numbers) be the height above the \( V \) plane, and let \( {M}^{a} \) be the set of all points \( x \in  M \) such that \( f\left( x\right)  < a \) . Then the following things are true:

(1) If \( a < 0 = f\left( p\right) \) , then \( {M}^{a} \) is vacuous.

(2) If \( f\left( p\right)  < a < f\left( q\right) \) , then \( {M}^{a} \) is homeomorphic to a 2-cell.

(3) If \( f\left( q\right)  < a < f\left( r\right) \) , then \( {M}^{a} \) is homeomorphic to a cylinder:

![bo_d7du90alb0pc73deir8g_11_633_1839_316_185_0.jpg](images/bo_d7du90alb0pc73deir8g_11_633_1839_316_185_0.jpg)

(4) If \( f\left( r\right)  < a < f\left( s\right) \) , then \( {M}^{a} \) is homeomorphic to a compact manifold of genus one having a circle as boundary:

![bo_d7du90alb0pc73deir8g_12_667_202_310_290_0.jpg](images/bo_d7du90alb0pc73deir8g_12_667_202_310_290_0.jpg)

(5) If \( f\left( s\right)  < a \) , then \( {M}^{a} \) is the full torus.

In order to describe the change in \( {M}^{a} \) as a passes through one of the points \( f\left( p\right) , f\left( q\right) , f\left( r\right) , f\left( s\right) \) it is convenient to consider homotopy type rather than homeomorphism type. In terms of homotopy types:

\( 1 \rightarrow  2 \) is the operation of attaching a 0-cell. For as far as homotopy type is concerned, the space \( {M}^{a}, f\left( p\right)  < a < f\left( q\right) \) , cannot be distinguished from a 0-cell:

Here "≈" means "is of the same homotopy type as."

\( 2 \rightarrow  3 \) is the operation of attaching a 1-cell:

![bo_d7du90alb0pc73deir8g_12_527_1054_682_103_0.jpg](images/bo_d7du90alb0pc73deir8g_12_527_1054_682_103_0.jpg)

\( 3 \rightarrow  4 \) is again the operation of attaching a 1-cell:

![bo_d7du90alb0pc73deir8g_12_419_1281_818_215_0.jpg](images/bo_d7du90alb0pc73deir8g_12_419_1281_818_215_0.jpg)

\( 4 \rightarrow  1 \) is the operation of attaching a 2-cell.

![bo_d7du90alb0pc73deir8g_12_418_1627_803_291_0.jpg](images/bo_d7du90alb0pc73deir8g_12_418_1627_803_291_0.jpg)

The precise definition of "attaching a \( k \) -cell" can be given as follows. Let \( Y \) be any topological space, and let

\[
{\mathrm{e}}^{k} = \left\{  {x \in  {\mathbf{R}}^{k} : \parallel x\parallel  \leq  1}\right\}
\]

be the \( k \) -cell consisting of all vectors in Euclidean \( k \) -space with length \( \leq  1 \) .

The boundary

\[
{\dot{\mathrm{e}}}^{k} = \left\{  {x \in  {\mathbf{R}}^{k} : \parallel x\parallel  = 1}\right\}  ,
\]

will be denoted by \( {\mathbb{S}}^{k - 1} \) . If \( g : {\mathbb{S}}^{k - 1} \rightarrow  Y \) is a continuous map then

\[
Y{ \cup  }_{g}{\mathrm{e}}^{k},
\]

( \( Y \) with a \( k \) -cell attached by \( g \) ) is obtained by first taking the topological sum (= disjoint union) of \( Y \) and \( {\mathrm{e}}^{k} \) , and then identifying each \( x \in  {\mathbb{S}}^{k - 1} \) with \( g\left( x\right)  \in  Y \) . To tale care of the case \( k = 0 \) let \( {\mathrm{e}}^{0} \) be a point and let \( {\dot{\mathrm{e}}}^{0} = {\mathbb{S}}^{-1} \) be vacuous, so that \( Y \) with a 0-cell attached is just the union of \( Y \) and a disjoint point.

As one might expect, the points \( p, q, r \) and \( s \) at which the homotopy type of \( {M}^{a} \) changes, have a simple characterization in terms of \( f \) . They are the critical points of the function. If we choose any coordinate system \( \left( {x, y}\right) \) near these points, then the derivatives \( \partial f/\partial x \) and \( \partial f/\partial y \) are both zero. At \( p \) we can choose \( \left( {x, y}\right) \) so that \( f = {x}^{2} + {y}^{2} \) , at \( s \) so that \( f = \) constant \( - {x}^{2} - {y}^{2} \) , and at \( q \) and \( r \) so that \( f = \) constant \( + {x}^{2} - {y}^{2} \) . Note that the number of minus signs in the expression for \( f \) at each point is the dimension of the cell we must attach to go from \( {M}^{a} \) to \( {M}^{b} \) , where \( a < f\left( \text{ point }\right)  < b \) . Our first theorems will generalize these facts for any differentiable function on a manifold.

For further information on Morse Theory, the following sources are extremely useful: [Mor96, ST51, Bot59, Bot60]
