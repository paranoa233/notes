## §17 Review of Homotopy Theory

To pave the way for later applications of the spectral sequence, we give in this section a brief account of homotopy theory. Following the definitions and basic properties of the homotopy groups, we compute some low-dimensional homotopy groups of the spheres. The geometrical ideas in this computation lead to the homotopy properties of attaching cells. A space built up from a collection of points by attaching cells is called a \( {CW} \) complex. To show that every manifold has the homotopy type of a \( {CW} \) complex, we make a digression into Morse theory. Returning to the main topic, we next discuss the relation between homotopy and homology, and indicate a proof of the Hurewicz isomorphism theorem using the homology spectral sequence. The homotopy groups of the sphere, \( {\pi }_{q}\left( {S}^{n}\right) , q \leq  n \) , are immediate corollaries. Finally, venturing into the next nontrivial homotopy group, \( {\pi }_{3}\left( {S}^{2}\right) \) , we discuss the Hopf invariant in terms of differential forms. Some of the general references for homotopy theory are Hu[1], Steenrod [1], and Whitehead [1].

## Homotopy Groups

Let \( X \) be a topological space with a base point *. For \( q \geq  1 \) the \( q \) th homotopy group \( {\pi }_{a}\left( X\right) \) of \( X \) is defined to be the homotopy classes of maps from the \( q \) -cube \( {I}^{q} \) to \( X \) which send the faces \( {I}^{q} \) of \( {I}^{q} \) to the base point of \( X \) . Equivalently \( {\pi }_{a}\left( X\right) \) may be regarded as the homotopy classes of base-point preserving maps from the \( q \) -sphere \( {S}^{q} \) to \( X \) . The group operation on \( {\pi }_{q}\left( X\right) \) is defined as follows (see Figure 17.1). If \( \alpha \) and \( \beta \) are maps from \( {I}^{q} \) to \( X \) , representing \( \left\lbrack  \alpha \right\rbrack \) and \( \left\lbrack  \beta \right\rbrack \) in \( {\pi }_{q}\left( X\right) \) , then the product \( \left\lbrack  \alpha \right\rbrack  \left\lbrack  \beta \right\rbrack \) is the homotopy class of the map

\[
\gamma \left( {{t}_{1},\ldots ,{t}_{q}}\right)  = \left\{  \begin{array}{lll} \alpha \left( {2{t}_{1},{t}_{2},\ldots ,{t}_{q}}\right) & \text{ for } & 0 \leq  {t}_{1} \leq  \frac{1}{2} \\  \beta \left( {2{t}_{1} - 1,{t}_{2},\ldots ,{t}_{q}}\right) & \text{ for } & \frac{1}{2} \leq  {t}_{1} \leq  1. \end{array}\right.
\]

We recall here some basic properties of the homotopy groups.

![bo_d7b6f8alb0pc73dd9avg_217_255_291_1122_868_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_217_255_291_1122_868_0.jpg)

Figure 17.1

Proposition 17.1. (a) \( {\pi }_{q}\left( {X \times  Y}\right)  = {\pi }_{q}\left( X\right)  \times  {\pi }_{q}\left( Y\right) \) .

(b) \( {\pi }_{q}\left( X\right) \) is Abelian for \( q > 1 \) .

Proof. (a) is clear since every map from \( {I}^{q} \) into \( X \times  Y \) is of the form \( \left( {{f}_{1},{f}_{2}}\right) \) where \( {f}_{1} \) is a map into \( X \) and \( {f}_{2} \) is a map into \( Y \) . Furthermore, since \( \left( {{f}_{1},{f}_{2}}\right) \left( {{g}_{1},{g}_{2}}\right)  = \left( {{f}_{1}{g}_{1},{f}_{2}{g}_{2}}\right) \) , the bijection in (a) is actually a group isomorphism. To prove (b), let \( \left\lbrack  \alpha \right\rbrack \) and \( \left\lbrack  \beta \right\rbrack \) be two elements of \( {\pi }_{q}\left( X\right) \) . We represent \( {\alpha \beta } \) by

\[
\alpha \;\beta \;\gamma \left( {{t}_{1},\ldots ,{t}_{q}}\right)  = \left\{  \begin{array}{ll} \alpha \left( {2{t}_{1},{t}_{2},\ldots ,{t}_{q}}\right) & \text{ for }0 \leq  {t}_{1} \leq  \frac{1}{2} \\  \beta \left( {2{t}_{1} - 1,{t}_{2},\ldots ,{t}_{q}}\right) & \text{ for }\frac{1}{2} \leq  {t}_{1} \leq  1. \end{array}\right.
\]

\( {\alpha \beta } \) is homotopic to the map \( \delta \) from \( {I}^{q} \) to \( X \) given by

\[
\left( \begin{matrix} \alpha &  * \\   * & \beta  \end{matrix}\right) \;\delta \left( {{t}_{1},\ldots ,{t}_{q}}\right)  = \left\{  \begin{matrix} \alpha \left( {2{t}_{1},2{t}_{2} - 1,{t}_{3},\ldots ,{t}_{q}}\right) , \\  0 \leq  {t}_{1} \leq  \frac{1}{2},\;\frac{1}{2} \leq  {t}_{2} \leq  1, \\  \beta \left( {2{t}_{1} - 1,2{t}_{2},\ldots ,{t}_{q}}\right) , \\  \frac{1}{2} \leq  {t}_{1} \leq  1,\;0 \leq  {t}_{2} \leq  \frac{1}{2}, \\   * \;\text{ otherwise. } \end{matrix}\right.
\]

\( \delta \) is in turn homotopic to

![bo_d7b6f8alb0pc73dd9avg_218_731_397_221_181_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_218_731_397_221_181_0.jpg)

![bo_d7b6f8alb0pc73dd9avg_218_735_631_222_180_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_218_735_631_222_180_0.jpg)

and finally to

![bo_d7b6f8alb0pc73dd9avg_218_733_937_191_185_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_218_733_937_191_185_0.jpg)

Proposition 17.2. \( {\pi }_{q - 1}\left( {\Omega X}\right)  = {\pi }_{q}\left( X\right) , q \geq  2 \) .

Sketch of Proof. Elements of \( {\pi }_{2}\left( X\right) \) are given by maps of the square \( {I}^{2} \) into \( X \) which send the boundary \( {I}^{2} \) to the base point \( * \) . Such a map may be viewed as a pencil of loops in \( X \) , i.e., a map from the unit interval into \( {\Omega X} \) . Therefore, \( {\pi }_{2}\left( X\right)  = {\pi }_{1}\left( {\Omega X}\right) \) . The general case is similar; we view a map from \( {I}^{q} \) to \( X \) as a map from \( {I}^{q - 1} \) to \( {\Omega X} \) .

It is often useful to introduce \( {\pi }_{0}\left( X\right) \) , which is defined to be the set of all path components of \( X \) . It has a distinguished element, namely the path component containing the base point of \( X \) . This component is the base point of \( {\pi }_{0}\left( X\right) \) . For a manifold the path components are the same as the connected components (Dugundji [1, Theorem IV.5.5, p. 116]).

Recall that a Lie group is a manifold endowed with a group structure such that the group operations, multiplication and the inverse operation, are smooth functions. Although \( {\pi }_{0}\left( X\right) \) is in general not a group, if \( G \) is a Lie group, then \( {\pi }_{0}\left( G\right) \) is a group. This follows from the following proposition.

Proposition 17.3. The identity component \( H \) of a Lie group \( G \) is a normal subgroup of \( G \) . Therefore, \( {\pi }_{0}\left( G\right)  = G/H \) is a group.

Proof. Let \( a, b \) be in \( H \) . Since the continuous image of a connected set is connected, \( {bH} \) is a connected set having a nonempty intersection with \( H \) .

Hence \( {bH} \subset  H \) . It follows that \( {abH} \subset  {aH} \subset  H \) , so \( {ab} \) is in \( H \) . Similarly \( {a}^{-1}H \) is a connected set having a nonempty intersection with \( H \) , since 1 is in \( {a}^{-1}H \) ; so \( {a}^{-1}H \subset  H \) and \( {a}^{-1} \) is also in \( H \) . This shows that \( H \) is a subgroup of \( G \) .

Let \( g \) be an element of \( G \) . Since \( {gH}{g}^{-1} \) is a connected set containing 1, by the same reasoning as above, \( {gH}{g}^{-1} \subset  H \) . Thus \( H \) is normal.

Because multiplication by \( g \) is a homeomorphism, the coset \( {gH} \) is connected. Since distinct cosets are disjoint, \( G/H \) consists of precisely the connected components of \( G \) . Therefore, \( {\pi }_{0}\left( G\right)  = G/H \) .

Let \( \pi  : E \rightarrow  B \) be a (base-point preserving) fibering with fiber \( F \) . Then there is an exact sequence of homotopy groups, called the homotopy sequence of the fibering (Steenrod [1, p. 91]):

(17.4)

\[
\cdots  \rightarrow  {\pi }_{q}\left( F\right) \overset{{i}_{ * }}{ \rightarrow  }{\pi }_{q}\left( E\right) \overset{{\pi }_{ * }}{ \rightarrow  }{\pi }_{q}\left( B\right) \overset{\partial }{ \rightarrow  }{\pi }_{q - 1}\left( F\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {\pi }_{0}\left( E\right)  \rightarrow  {\pi }_{0}\left( B\right)  \rightarrow  0
\]

In this exact sequence the last three maps are not group homomorphisms, but only set maps. The kernel of a set map between pointed sets is by definition the inverse image of the base point. Exactness in this context is given by the same condition as before: "the image equals the kernel." The maps \( {i}_{ * } \) and \( {\pi }_{ * } \) are the maps induced by the inclusion \( i : F \rightarrow  E \) and the projection \( \pi  : E \rightarrow  B \) respectively. Here we regard \( F \) as the fiber over the base point of \( B \) . To describe \( \partial \) we use the covering homotopy property of a fibering. For simplicity consider first \( q = 1 \) . A loop \( \alpha  : {I}^{1} \rightarrow  B \) from the unit interval to \( B \) , representing an element of \( {\pi }_{1}\left( B\right) \) , may be lifted to a path \( \overline{\alpha } \) in \( E \) with \( \overline{\alpha }\left( 0\right) \) being the base point of \( F \) . Then \( \partial \left\lbrack  \alpha \right\rbrack \) is given by \( \overline{\alpha }\left( 1\right) \) in \( {\pi }_{0}\left( F\right) \) . More generally let \( {I}^{q - 1} \subset  {I}^{q} \) be the inclusion

\[
\left( {{t}_{1},\ldots ,{t}_{q - 1}}\right)  \mapsto  \left( {{t}_{1},\ldots ,{t}_{q - 1},0}\right) .
\]

A map \( \alpha  : {I}^{q} \rightarrow  B \) representing an element of \( {\pi }_{q}\left( B\right) \) may be regarded as a homotopy of \( {\left. \alpha \right| }_{{I}^{q - 1}} \) in \( B \) . Let the constant map \( *  : {I}^{q - 1} \rightarrow  E \) from \( {I}^{q - 1} \) to the base point of \( F \) be the map that covers \( {\alpha }_{{I}^{q - 1} : }\left( {{t}_{1},\ldots ,{t}_{q - 1},0}\right)  \rightarrow  B \) . By the covering homotopy property, there is a homotopy upstairs \( \overrightarrow{\alpha } : {I}^{q} \rightarrow  E \) which covers \( \alpha \) and such that \( {\left. \overline{\alpha }\right| }_{{I}^{q - 1}} =  * \) . Then \( \partial \left\lbrack  \alpha \right\rbrack \) is the homotopy class of the map \( \overline{\alpha } : \left( {{t}_{1},\ldots ,{t}_{q - 1},1}\right)  \rightarrow  F \) . By Remark 16.4, \( \partial \left\lbrack  \alpha \right\rbrack \) is well-defined.

Example 17.5. A covering space \( \pi  : E \rightarrow  B \) is a fibering with discrete fibers. By the homotopy sequence of the fibering,

\[
{\pi }_{q}\left( E\right)  = {\pi }_{q}\left( B\right) \;\text{ for }\;q \geq  2
\]

and

\[
{\pi }_{1}\left( E\right)  \hookrightarrow  {\pi }_{1}\left( B\right)
\]

WARNING 17.6 (Dependence on base points). Consider the homotopy groups \( {\pi }_{a}\left( {X, x}\right) \) and \( {\pi }_{q}\left( {X, y}\right) \) of a path-connected space \( X \) , computed relative to two different points \( x \) and \( y \) . A path \( \gamma \) from \( x \) to \( y \) induces by conjugation a map from the loop space \( {\Omega }_{x}X \) to the loop space \( {\Omega }_{y}X \) :

\[
\lambda  \mapsto  {\gamma \lambda }{\gamma }^{-1}\;\text{ for any }\lambda \text{ in }{\Omega }_{x}X.
\]

This in turn induces a map of homotopy groups

\[
{\gamma }_{ * } : {\pi }_{q - 1}\left( {{\Omega }_{x}X,\overrightarrow{x}}\right)  \rightarrow  {\pi }_{q - 1}\left( {{\Omega }_{y}X,\overrightarrow{y}}\right)
\]

\[
\parallel
\]

\[
{\pi }_{q}\left( {X, x}\right) \;{\pi }_{q}\left( {X, y}\right)
\]

where \( \bar{x} \) and \( \bar{y} \) are the constant maps to \( x \) and \( y \) . The map \( {\gamma }_{ * } \) is clearly an isomorphism, with inverse given by \( {\left( {\gamma }^{-1}\right) }_{ * } \) .

We can describe \( {\gamma }_{ * } \) explicitly as follows. Let \( \left\lbrack  \alpha \right\rbrack \) be an element of \( {\pi }_{a}\left( {X, x}\right) \) . Define a map \( F \) to be \( \alpha \) on the bottom face of the cube \( {I}^{q + 1} \) and \( \gamma \) on the vertical faces (Figure 17.2 (a)); more precisely, if \( \left( {u, t}\right)  \in  {I}^{q} \times  I = \; {I}^{q + 1} \) , then

\[
F\left( {u,0}\right)  = \alpha \left( u\right) \text{ for all }u\text{ in }{I}^{q}
\]

and

\[
F\left( {u, t}\right)  = \gamma \left( t\right) \text{ for all }u\text{ in }\partial {I}^{q}\text{ . }
\]

![bo_d7b6f8alb0pc73dd9avg_220_561_1243_544_553_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_220_561_1243_544_553_0.jpg)

Figure 17.2(a)

By the box principle from obstruction theory (which states that a map from the union of all but one face of a cube into any space can be extended to the whole cube), the map \( F \) can be extended to the entire \( {I}^{q + 1} \) . Its restriction to the top face represents \( {\gamma }_{ * }\left\lbrack  \alpha \right\rbrack \) .

One checks easily that \( {\gamma }_{ * } \) depends only on the homotopy class of \( \gamma \) amongst the paths from \( x \) to \( y \) , so that when we take \( x = y \) , the assignment \( \gamma  \mapsto  {\gamma }_{ * } \) may be thought of as an action of \( {\pi }_{1}\left( {X, x}\right) \) on \( {\pi }_{q}\left( {X, x}\right) \) . Only if this action is trivial, can one speak unambiguously of \( {\pi }_{q}\left( X\right) \) without reference to a base point. In that case one can also identify the free homotopy classes of maps \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) with \( {\pi }_{q}\left( X\right) \) ; here by a free homotopy we mean a homotopy that does not necessarily preserve the base points. In general, however, \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) is not a group and its relation to \( {\pi }_{q}\left( X\right) \) is given by the following.

Proposition 17.6.1. Let \( X \) be a path-connected space. The inclusion of basepoint preserving maps into the set of all maps induces a bijection

\[
{\pi }_{q}\left( {X, x}\right) /{\pi }_{1}\left( {X, x}\right) \overset{ \sim  }{ \rightarrow  }\left\lbrack  {{S}^{q}, X}\right\rbrack
\]

where the notation on the left indicates the equivalence relation \( \left\lbrack  \alpha \right\rbrack   \sim  {\gamma }_{ * }\left\lbrack  \alpha \right\rbrack \) for \( \left\lbrack  \gamma \right\rbrack \) in \( {\pi }_{1}\left( {X, x}\right) \) .

Proof. Let \( h : {\pi }_{q}\left( {X, x}\right)  \rightarrow  \left\lbrack  {{S}^{q}, X}\right\rbrack \) be induced by the inclusion of base point preserving maps into the set of all maps. If \( \left\lbrack  \alpha \right\rbrack   \in  {\pi }_{q}\left( {X, x}\right) \) and \( \left\lbrack  \gamma \right\rbrack   \in  {\pi }_{1}\left( {X, x}\right) \) , it is laborious but not difficult to write down an explicit free homotopy between \( \alpha \) and \( {\gamma }_{ * }\alpha \) (see Figure 17.2 (b) for the cases \( q = 1 \) and \( q = 2 \) ). Hence \( h \) factors through the action of \( {\pi }_{1}\left( {X, x}\right) \) on \( {\pi }_{q}\left( {X, x}\right) \) and defines a map

\[
H : {\pi }_{q}\left( {X, x}\right) /{\pi }_{1}\left( {X, x}\right)  \rightarrow  \left\lbrack  {{S}^{q}, X}\right\rbrack  .
\]

![bo_d7b6f8alb0pc73dd9avg_221_549_1079_558_1062_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_221_549_1079_558_1062_0.jpg)

Figure 17.2(b)

![bo_d7b6f8alb0pc73dd9avg_222_553_429_542_544_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_222_553_429_542_544_0.jpg)

Since \( X \) is path connected, any map in \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) can be deformed to a base-point preserving map. So \( H \) is surjective. To show injectivity, suppose \( \left\lbrack  \alpha \right\rbrack \) in \( {\pi }_{q}\left( {X, x}\right) \) is null-homotopic in \( \left\lbrack  {{S}^{q}, X}\right\rbrack \) . This means there is a map \( F : {I}^{q + 1} \rightarrow  X \) such that

\[
{\left. F\right| }_{\text{ top face }} = \alpha
\]

\[
{\left. F\right| }_{\text{ bottom face }} = \bar{x},
\]

and \( F \) is constant on the boundary of each horizontal slice (Figure 17.2 (c)). Let \( \gamma \) be the restriction of \( F \) to a vertical segment. Then \( \alpha  = {\gamma }_{ * }\left( \bar{x}\right) \) . Therefore, \( H \) is injective.

## The Relative Homotopy Sequence

Let \( X \) be a path-connected space with base point \( * \) , and \( A \) a subset of \( X \) (See Figure 17.3). Denote by \( {\Omega }_{ * }^{A} \) the space of all paths from \( * \) to \( A \) . The endpoint map \( e : {\Omega }_{ * }^{A} \rightarrow  A \) gives a fibering

![bo_d7b6f8alb0pc73dd9avg_222_749_1765_167_140_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_222_749_1765_167_140_0.jpg)

The homotopy sequence of this fibering is

\[
\cdots  \rightarrow  {\pi }_{q}\left( A\right)  \rightarrow  {\pi }_{q - 1}\left( {\Omega X}\right)  \rightarrow  {\pi }_{q - 1}\left( {\Omega }_{ * }^{A}\right)  \rightarrow  {\pi }_{q - 1}\left( A\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {\pi }_{0}\left( {\Omega }_{ * }^{A}\right)  \rightarrow  {\pi }_{0}\left( A\right)  \rightarrow  0
\]

![bo_d7b6f8alb0pc73dd9avg_223_541_309_531_338_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_223_541_309_531_338_0.jpg)

We define the relative homotopy group \( {\pi }_{q}\left( {X, A}\right) \) to be \( {\pi }_{q - 1}\left( {\Omega }_{ * }^{A}\right) \) . Then the sequence above becomes the relative homotopy sequence of \( A \) in \( X \) :

(17.7)

\[
\cdots  \rightarrow  {\pi }_{q}\left( A\right)  \rightarrow  {\pi }_{q}\left( X\right)  \rightarrow  {\pi }_{q}\left( {X, A}\right)  \rightarrow  {\pi }_{q - 1}\left( A\right)  \rightarrow  \cdots
\]

\[
\cdots  \rightarrow  {\pi }_{1}\left( {X, A}\right)  \rightarrow  {\pi }_{0}\left( A\right)  \rightarrow  0.
\]

Observe that \( {\pi }_{q}\left( {X, A}\right) \) is an Abelian group for \( q \geq  3,{\pi }_{2}\left( {X, A}\right) \) is a group but in general not Abelian, while \( {\pi }_{1}\left( {X, A}\right) \) is only a set.

## Some Homotopy Groups of the Spheres

In this section we will compute \( {\pi }_{q}\left( {S}^{n}\right) \) for \( q \leq  n \) . Although these homotopy groups are immediate from the Hurewicz isomorphism theorem (17.21), the geometric proof presented here is important in being the pattern for later discussions of the homotopy properties of attaching cells (17.11).

Proposition 17.8 Every continuous map \( f : M \rightarrow  N \) between two manifolds is continuously homotopic to a differentiable map.

Proof. We first note that if \( f : M \rightarrow  \mathbb{R} \) is a continuous function and \( \varepsilon \) a positive number, then there is a differentiable real-valued function \( h \) on \( M \) with \( \left| {f - h}\right|  < \varepsilon \) . This is more or less clear from the fact that via its graph, \( f \) may be regarded as a continuous section of the trivial bundle \( M \times  \mathbb{R} \) over \( M \) ; in any \( \varepsilon \) -neighborhood of \( f \) there is a differentiable section \( h \) and because the \( \varepsilon \) -neighborhood of \( f \) may be continuously deformed onto \( f, h \) is continuously homotopic to \( f \) (see Figure 17.4). Indeed, to be more explicit, this differentiable section \( h \) can be given by successively averaging the values of \( f \) over small disks.

Next consider a continuous map \( f : M \rightarrow  N \) of manifolds. By the Whitney embedding theorem (see, for instance, de Rham [1, p. 12]), there is a differentiable embedding \( g : N \rightarrow  {\mathbb{R}}^{n} \) . If

\[
g \circ  f : M \rightarrow  g\left( N\right)  \subset  {\mathbb{R}}^{n}
\]

is homotopic to a differentiable map, then so is

\[
f = {g}^{-1} \circ  \left( {g \circ  f}\right)  : M \rightarrow  N.
\]

![bo_d7b6f8alb0pc73dd9avg_224_332_302_985_663_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_224_332_302_985_663_0.jpg)

Figure 17.4

So we may assume at the outset that \( N \) is a submanifold of an Euclidean space \( {\mathbb{R}}^{n} \) . Then the map \( f \) is given by continuous real-valued functions \( \left( {f}_{1}\right. \) , \( \left. {\ldots ,{f}_{n}}\right) \) . As noted above, each coordinate function \( {f}_{i} \) can be approximated by a differentiable function \( {h}_{i} \) to within \( \varepsilon \) , and \( {f}_{i} \) is continuously homotopic to \( {h}_{i} \) . Thus we get a differentiable map \( h : M \rightarrow  {\mathbb{R}}^{n} \) whose image is in some tubular neighborhood \( T \) of \( N \) . But every tubular neighborhood of \( N \) can be deformed to \( N \) via a differentiable map \( k : T \rightarrow  N \) (Figure 17.5). This gives a differentiable map \( k \circ  h : M \rightarrow  N \) which is homotopic to \( f \) .

![bo_d7b6f8alb0pc73dd9avg_224_406_1375_847_432_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_224_406_1375_847_432_0.jpg)

Figure 17.5

Corollary 17.8.1. Let \( M \) be a manifold. Then the homotopy groups of \( M \) in the \( {C}^{\infty } \) sense are the same as the homotopy groups of \( M \) in the continuous sense.

Proposition 17.9. \( {\pi }_{q}\left( {S}^{n}\right)  = 0 \) , for \( q < n \) .

Proof. Let \( f \) be a continuous map from \( {I}^{q} \) to \( {S}^{n} \) , representing an element of \( {\pi }_{q}\left( {S}^{n}\right) \) . By the lemma above, we may assume \( f \) differentiable. Hence Sard’s theorem applies. Because \( q \) is strictly less than \( n \) , the images of \( f \) are all critical values. By Sard’s theorem \( f \) cannot be surjective. Choose a point \( P \) not in the image of \( f \) and let \( c \) be a contraction of \( {S}^{n} - \{ P\} \) to the antipodal point \( Q \) of \( P \) (Figure 17.6):

\[
{c}_{t} : {S}^{n} - \{ P\}  \rightarrow  {S}^{n} - \{ P\} , t \in  \left\lbrack  {0,1}\right\rbrack
\]

\[
{c}_{0} = \text{ identity }
\]

\[
{c}_{1} = \text{ constant map }Q\text{ . }
\]

Then \( {c}_{t} \circ  f \) is a homotopy between \( f \) and the constant map \( Q \) . Therefore, \( {\pi }_{q}\left( {S}^{n}\right)  = 0 \) for \( q < n \) .

![bo_d7b6f8alb0pc73dd9avg_225_616_766_390_395_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_225_616_766_390_395_0.jpg)

Figure 17.6

Proposition 17.10. \( {\pi }_{n}\left( {S}^{n}\right)  = \mathbb{Z} \) .

We will indicate here the main ideas in the geometrical proof of this statement, omitting some technical details.

Recall that to every map from \( {S}^{n} \) to \( {S}^{n} \) one can associate an integer called its degree. Since the degree is a homotopy invariant, it gives a map \( \deg  : {\pi }_{n}\left( {S}^{n}\right)  \rightarrow  \mathbb{Z} \) . There are two key lemmas.

Lemma 17.10.1. The map \( \deg  : {\pi }_{n}\left( {S}^{n}\right)  \rightarrow  \mathbb{Z} \) is a group homomorphism; that is,

\[
\deg \left( {\left\lbrack  f\right\rbrack  \left\lbrack  g\right\rbrack  }\right)  = \deg \left\lbrack  f\right\rbrack   + \deg \left\lbrack  g\right\rbrack  .
\]

Lemma 17.10.2 Two maps from \( {S}^{n} \) to \( {S}^{n} \) of the same degree can be deformed into each other.

The surjectivity of deg follows immediately from Lemma 17.10.1, since if \( f \) is the identity map, then \( \deg \left( {\left\lbrack  f\right\rbrack  }^{k}\right)  = k \) for any integer \( k \) ; the injectivity follows from (17.10.2).

To prove these lemmas we will deform any map \( f : {S}^{n} \rightarrow  {S}^{n} \) into a normal form as follows. By the inverse function theorem \( f \) is a local diffeomorphism around a regular point. By Sard's theorem regular values exist. Let \( U \) be an open set around a regular value so that \( {f}^{-1}\left( U\right) \) consists of finitely many disjoint open sets, \( {U}_{1},\ldots ,{U}_{r} \) , each of which \( f \) maps diffeomorphically onto \( U \) (Figure 17.7). Choose the base point \( * \) of \( {S}^{n} \) to be not in \( U \) . We deform the map \( f \) by deforming \( U \) in such a way that the complement of \( U \) goes into \( * \) . The deformed \( f \) then maps the complement of \( \mathop{\bigcup }\limits_{{i = 1}}^{k}{U}_{i} \) to \( * \) . Each \( {U}_{i} \) comes with a multiplicity of \( \pm  1 \) depending on whether \( f \) is orientation preserving or reversing on \( {U}_{i} \) . The degree of \( f \) is the sum of these multiplicities. Given two maps \( f \) and \( g \) from \( {S}^{n} \) to \( {S}^{n} \) , we deform each as above, choosing \( U \) to be a neighborhood of a regular value of both \( f \) and \( g \) . By summing the multiplicities of the inverse images of \( U \) , we see that \( \deg \left( {\left\lbrack  f\right\rbrack  \left\lbrack  g\right\rbrack  }\right)  = \deg \left\lbrack  f\right\rbrack   + \deg \left\lbrack  g\right\rbrack \) (Figure 17.8). This proves Lemma 17.10.1.

![bo_d7b6f8alb0pc73dd9avg_226_322_296_1019_691_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_226_322_296_1019_691_0.jpg)

Figure 17.7

To bring a map \( f : {S}^{n} \rightarrow  {S}^{n} \) into what we consider its normal form requires one more step. If \( {U}_{i} \) and \( {U}_{j} \) have multiplicities +1 and -1 respectively, we join \( {U}_{i} \) to \( {U}_{j} \) with a path. It is plausible that \( f \) can be deformed further so that it maps \( {U}_{i} \cup  {U}_{j} \) to the base point \( * \) , since \( f \) wraps \( {U}_{i} \) around the sphere one way and \( {U}_{j} \) the reverse way. For \( {S}^{1} \) this is clear.

![bo_d7b6f8alb0pc73dd9avg_226_292_1703_1121_382_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_226_292_1703_1121_382_0.jpg)

Figure 17.8

The general case is where we wave our hands. The details are quite involved and can be found in Whitney [1]. In this way pairs of open sets with opposite multiplicities are cancelled out. In the normal form, if \( f \) has degree \( \pm  k \) , then there are exactly \( k \) open sets, \( {U}_{1},\ldots ,{U}_{k} \) , with all \( + 1 \) multiplicities or all -1 multiplicities. Hence two maps from \( {S}^{n} \) to \( {S}^{n} \) of the same degree can be deformed into each other.

## Attaching Cells

Let \( {e}^{n} \) be the closed \( n \) -disk and \( {S}^{n - 1} \) its boundary. Given a space \( X \) and a map \( f : {S}^{n - 1} \rightarrow  X \) , the space \( Y \) obtained from \( X \) by attaching the n-cell \( {e}^{n} \) via \( f \) is by definition (see Figure 17.9)

\[
Y = X{ \cup  }_{f}{e}^{n} = X \coprod  {e}^{n}/f\left( u\right)  \sim  u\text{ , for }u \in  {S}^{n - 1}\text{ . }
\]

![bo_d7b6f8alb0pc73dd9avg_227_255_903_1113_336_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_227_255_903_1113_336_0.jpg)

For example, the 2-sphere is obtained from a point by attaching a 2-cell (Figure 17.10):

\[
{S}^{2} = p \cup  {e}^{2}.
\]

![bo_d7b6f8alb0pc73dd9avg_227_670_1450_294_298_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_227_670_1450_294_298_0.jpg)

Figure 17.10

It is easy to show that if \( f \) and \( g \) are homotopic maps from \( {S}^{n - 1} \) to \( X \) , then \( X{ \cup  }_{f}{e}^{n} \) and \( X{ \cup  }_{g}{e}^{n} \) have the same homotopy type (see Bott and Mather [1, Prop. 1, p. 466] for an explicit homotopy). The most fundamental homotopy property of attaching an \( n \) -cell is the following.

Proposition 17.11. Attaching an n-cell to a space \( X \) does not alter the homotopy in dimensions strictly less than \( n - 1 \) , but may kill elements in \( {\pi }_{n - 1}\left( X\right) \) ; more precisely, the inclusion \( X \hookrightarrow  X \cup  {e}^{n} \) induces isomorphisms

\[
{\pi }_{q}\left( X\right)  \simeq  {\pi }_{q}\left( {X \cup  {e}^{n}}\right) \;\text{ for }q < n - 1
\]

and a surjection

\[
{\pi }_{n - 1}\left( X\right)  \rightarrow  {\pi }_{n - 1}\left( {X \cup  {e}^{n}}\right) .
\]

Proof. Assume \( q \leq  n - 1 \) and let \( f : {S}^{q} \rightarrow  X \cup  {e}^{n} \) be a continuous basepoint preserving map. We would like first of all to show that \( f \) is homotopic to some map whose image does not contain all of \( {e}^{n} \) . If \( f \) is differentiable and \( X{ \cup  }_{f}{e}^{n} \) is a manifold, this follows immediately from Sard’s theorem. In fact, as long as \( f \) is differentiable on some submanifold of \( {S}^{q} \) that maps into \( {e}^{n} \) , the same conclusion holds. As in the proof of Proposition 17.8 this can always be arranged by moving the given \( f \) in its homotopy class. So we may assume that \( f \) does not surject onto \( {e}^{n} \) . Choose a point \( p \) not in the image and fix a retraction \( {c}_{t} \) of \( \left( {{e}^{n}-\{ p\} }\right) \) to the boundary of \( {e}^{n} \) . This gives a retraction \( {c}_{t} \) of \( X \cup  \left( {{e}^{n}-\{ p\} }\right) \) to \( X \) . Via \( {c}_{t} \circ  f \) , the map \( f \) is homotopic in \( X \cup  {e}^{n} \) to a map from \( {S}^{q} \) to \( X \) (Figure 17.11). Hence \( {\pi }_{q}\left( X\right)  \rightarrow  {\pi }_{q}\left( {X \cup  {e}^{n}}\right) \) is surjective for \( q \leq  n - 1 \) .

![bo_d7b6f8alb0pc73dd9avg_228_404_1083_853_381_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_228_404_1083_853_381_0.jpg)

Figure 17.11

Now assume \( q \leq  n - 2 \) . To show injectivity let \( f \) and \( g \) be two maps representing elements of \( {\pi }_{q}\left( X\right) \) which have the same image in \( {\pi }_{q}\left( {X \cup  {e}^{n}}\right) \) . Let \( F : {S}^{q} \times  I \rightarrow  X \cup  {e}^{n} \) be a homotopy in \( X \cup  {e}^{n} \) between \( f \) and \( g \) . Since the dimension of \( {S}^{q} \times  I \) is less than \( n \) , again we can deform \( F \) so that its image does not contain all of \( {e}^{n} \) . Reasoning as before, we find maps

\[
{c}_{t} \circ  F : {S}^{q} \times  I \rightarrow  X \cup  {e}^{n}
\]

![bo_d7b6f8alb0pc73dd9avg_228_263_1723_1148_320_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_228_263_1723_1148_320_0.jpg)

Figure 17.12

such that \( {c}_{1} \circ  F : {S}^{q} \times  \{ 1\}  \rightarrow  X \) is a homotopy between \( f \) and \( g \) which lies in \( X \) (Figure 17.12). Therefore \( \left\lbrack  f\right\rbrack   = \left\lbrack  g\right\rbrack \) as elements of \( {\pi }_{q}\left( X\right) \) .

As for homology we have the following:

Proposition 17.12. Attaching an n-cell to a space \( X \) via a map \( f \) does not alter the homology except possibly in dimensions \( n - 1 \) and \( n \) . Writing \( {X}_{f} \) for \( X{ \cup  }_{f}{e}^{n} \) , there is an exact sequence

\[
0 \rightarrow  {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( {X}_{f}\right)  \rightarrow  \mathbb{Z}\xrightarrow[]{{f}_{ * }}{H}_{n - 1}\left( X\right)  \rightarrow  {H}_{n - 1}\left( {X}_{f}\right)  \rightarrow  0
\]

where \( {f}_{ * } : {H}_{n - 1}\left( {S}^{n - 1}\right)  \rightarrow  {H}_{n - 1}\left( X\right) \) is the induced map. So the inclusion \( X \hookrightarrow \; {X}_{f} \) induces a surjection in dimension \( n - 1 \) and an injection in dimension \( n \) .

Proof. Let \( U \) be \( {X}_{f} - \{ p\} \) where \( p \) is the origin of \( {e}^{n} \) , and let \( V \) be \( \left\{  {x \in  {e}^{n} \mid  }\right. \; \parallel x\parallel  < \frac{1}{2}\} \) . Then \( U \) is homotopic to \( X, V \) is contractible, and \( \{ U, V\} \) is an open cover of \( {X}_{f} \) . By the Mayer-Vietoris sequence (15.6), the following is exact

\[
\cdots  \rightarrow  {H}_{q}\left( {S}^{n - 1}\right)  \rightarrow  {H}_{q}\left( X\right)  \oplus  {H}_{q}\left( V\right)  \rightarrow  {H}_{q}\left( {X}_{f}\right)  \rightarrow  {H}_{q - 1}\left( {S}^{n - 1}\right)  \rightarrow  \cdots .
\]

So for \( q \neq  n - 1 \) or \( n,{H}_{q}\left( {X}_{f}\right)  = {H}_{q}\left( X\right) \) . For \( q = n \) , we have

\[
0 \rightarrow  {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( {X}_{f}\right)  \rightarrow  {H}_{n - 1}\left( {S}^{n - 1}\right) \xrightarrow[]{{f}_{ * }}{H}_{n - 1}\left( X\right)  \rightarrow  {H}_{n - 1}\left( {X}_{f}\right)  \rightarrow  0.
\]

A \( {CW} \) complex is a space \( Y \) built up from a collection of points by the successive attaching of cells, where the cells are attached in the order of increasing dimensions; the topology of \( Y \) is required to be the so-called weak topology: a set in \( Y \) is closed if and only if its intersection with every cell is closed. (By a cell we mean a closed cell.) The cells of dimension at most \( n \) in a \( {CW} \) complex \( Y \) together comprise the \( n \) -skeleton of \( Y \) . Clearly every triangularizable space is a \( {CW} \) complex. Every manifold is also a \( {CW} \) complex; this is most readily seen in the framework of Morse theory, as we will show in the next subsection.

For us the importance of the \( {CW} \) complexes comes from the following proposition.

Proposition 17.13. Every CW complex is homotopy equivalent to a space with a good cover.

Hence the entire machinery of the spectral sequence that we have developed applies to \( {CW} \) complexes. This proposition follows from the nontrivial fact that every CW complex has the homotopy type of a simplicial complex (Gray [1, Cor. 16.44, p. 149 and Cor. 21.15, p. 206] or Lundell and Weingram [1, Cor. 4.7, p. 131]), for the open stars of the vertices of the simplicial complex form a good cover.

## Digression on Morse Theory

Using Morse theory, it can be shown that every differentiable manifold has the homotopy type of a \( {CW} \) complex (see Milnor [2, p. 36]). The goal of this section is to prove this for the simpler case of a compact differentiable manifold.

Let \( f \) be a smooth real-valued function on a manifold \( M \) . A critical point of \( f \) is a point \( p \) where \( {df} = 0 \) ; in terms of local coordinates \( {x}_{1},\ldots ,{x}_{n} \) centered at \( p \) , the condition \( {df}\left( p\right)  = \sum \left( {\partial f/\partial {x}_{i}}\right) \left( p\right) d{x}_{i} = 0 \) is equivalent to the vanishing of all the partial derivatives \( \left( {\partial f/\partial {x}_{i}}\right) \left( p\right) \) . The image \( f\left( p\right) \) of a critical point is called a critical value. Note that the definition of a critical point given here is a special case of the more general definition preceding Theorem 4.11 for a map between manifolds. A critical point is nondegenerate if for some coordinate system \( {x}_{1},\ldots ,{x}_{n} \) centered at \( p \) , the matrix of second partials, \( \left( {\left( {{\partial }^{2}f/\partial {x}_{i}\partial {x}_{j}}\right) \left( p\right) }\right) \) , is nonsingular; this matrix is called the Hessian of \( f \) relative to the coordinate system \( {x}_{1},\ldots ,{x}_{n} \) at \( p \) . The notion of a nondegenerate critical point is independent of the choice of coordinate systems, for if \( {y}_{1},\ldots ,{y}_{n} \) is another coordinate system centered at \( p \) , then

\[
\frac{\partial f}{\partial {y}_{\ell }} = \mathop{\sum }\limits_{j}\frac{\partial f}{d{x}_{j}}\frac{\partial {x}_{j}}{\partial {y}_{\ell }}
\]

and

\[
\frac{{\partial }^{2}f}{\partial {y}_{k}\partial {y}_{\ell }} = \mathop{\sum }\limits_{{i, j}}\frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\frac{\partial {x}_{i}}{\partial {y}_{k}}\frac{\partial {x}_{j}}{\partial {y}_{\ell }} + \mathop{\sum }\limits_{j}\frac{\partial f}{\partial {x}_{j}}\frac{{\partial }^{2}{x}_{j}}{\partial {y}_{k}\partial {y}_{\ell }}.
\]

At \( p,\partial f/\partial {x}_{j} = 0 \) , so that

\[
\frac{{\partial }^{2}f}{\partial {y}_{k}\partial {y}_{\ell }} = \mathop{\sum }\limits_{{i, j}}\frac{{\partial }^{2}f}{\partial {x}_{i}\partial {x}_{j}}\frac{\partial {x}_{i}}{\partial {y}_{k}}\frac{\partial {x}_{j}}{\partial {y}_{\ell }}.
\]

In matrix notation

\[
H\left( y\right)  = {J}^{t}H\left( x\right) J
\]

where \( H\left( x\right) \) is the Hessian of \( f \) relative to the coordinate system \( {x}_{1},\ldots ,{x}_{n} \) , and \( J \) is the Jacobian \( \left( {\partial {x}_{i}/\partial {y}_{k}}\right) \) . Since the Jacobian is nonsingular, \( \det \left( {{\partial }^{2}f/\partial {y}_{k}\partial {y}_{\ell }}\right)  \neq  0 \) if and only if \( \det \left( {{\partial }^{2}f/\partial {x}_{i}\partial {x}_{j}}\right)  \neq  0 \) . The index of a nondegenerate critical point is the number of negative eigenvalues in the Hessian of \( f \) . By Sylvester’s theorem from linear algebra, the index is independent of the coordinate systems. It may be interpreted as the number of independent directions along which \( f \) is decreasing.

EXAMPLE 17.14. Consider a torus in 3-space sitting on a plane as shown in Figure 17.13. Let \( f\left( p\right) \) be the height of the point \( p \) above the plane. Then as a function on the torus \( f \) has four critical points \( A, B, C \) , and \( D \) , of indices 0, 1, 1, and 2 respectively.

![bo_d7b6f8alb0pc73dd9avg_231_504_490_608_499_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_231_504_490_608_499_0.jpg)

Figure 17.13

We outline below the proofs of the two main theorems of Morse theory. For details the reader is referred to Milnor [2, §3] or Bott and Mather [1, pp. 468-472].

Theorem 17.15. Let \( f \) be a differentiable function on the manifold \( M \) , and \( {M}_{a} \) the set \( {f}^{-1}\left( \left\lbrack  {-\infty , a}\right\rbrack  \right) \) . If \( {f}^{-1}\left( \left\lbrack  {a, b}\right\rbrack  \right) \) is compact and contains no critical points, then \( {M}_{a} \) has the same homotopy type as \( {M}_{b} \) .

Outline of Proof. Choose a Riemannian structure \( \langle \) , \( \rangle {onM} \) . Then away from the critical points of \( f \) , the gradient \( \nabla f \) of a differentiable function \( f \) is defined: it is the unique vector field on \( M \) such that for all vector fields \( Y \) on \( M \) ,

\[
\left\langle  {\nabla {f}_{p},{Y}_{p}}\right\rangle   = d{f}_{p}\left( {Y}_{p}\right) .
\]

Let \( X \) be the unit vector field \( - \nabla f/\parallel \nabla f\parallel \) . Because \( f \) has no critical points on \( {f}^{-1}\left( \left\lbrack  {a, b}\right\rbrack  \right) , X \) is defined on \( {f}^{-1}\left( \left\lbrack  {a, b}\right\rbrack  \right) \) . As in vector calculus on \( {\mathbb{R}}^{n} \) the gradient of a function points in the direction of the fastest increase, so \( X \) points in the direction of the fastest decrease. Extend \( X \) to a vector field on \( M \) . The flow lines of \( X \) give a deformation retraction of \( {M}_{b} \) onto \( {M}_{a} \) (Figure 17.14).

![bo_d7b6f8alb0pc73dd9avg_231_578_1674_471_376_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_231_578_1674_471_376_0.jpg)

Figure 17.14

Theorem 17.16. Suppose \( {f}^{-1}\left( \left\lbrack  {a, b}\right\rbrack  \right) \) is compact and contains precisely one critical point in its interior, which is nondegenerate and of index \( k \) . Then \( {M}_{b} \) has the homotopy type of \( {M}_{a} \cup  {e}^{k} \) .

To prove this theorem we need the following.

Morse lemma. If \( p \) is a nondegenerate critical point of \( f \) of index \( k \) , then there is a coordinate system \( {x}_{1},\ldots ,{x}_{n} \) near \( p \) such that

\[
f = f\left( p\right)  - {x}_{1}^{2} - \cdots  - {x}_{k}^{2} + {x}_{k + 1}^{2} + \cdots  + {x}_{n}^{2}.
\]

The Morse lemma may be proved by the method used to diagonalize quadratic forms (see Milnor [2, p. 6]).

Outline of a PROOF OF THEOREM 17.16. Let \( c = f\left( p\right) \) be the critical value and \( \varepsilon \) a small positive number. By Theorem 17.15, \( {M}_{b} \) has the homotopy type of \( {M}_{c + \varepsilon } \) , and \( {M}_{a} \) that of \( {M}_{c - \varepsilon } \) , so it suffices to show that \( {M}_{c + \varepsilon } \) has the homotopy type of \( {M}_{c - \varepsilon } \cup  {e}^{k} \) .

![bo_d7b6f8alb0pc73dd9avg_232_511_1413_648_658_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_232_511_1413_648_658_0.jpg)

Figure 17.15

On a neighborhood \( U \) of \( p \) where the Morse lemma holds,

\[
{M}_{c + \varepsilon } \cap  U = \left\{  {-{x}_{1}^{2} - \cdots  - {x}_{k}^{2} + {x}_{k + 1}^{2} + \cdots  + {x}_{n}^{2} \leq  \varepsilon }\right\}
\]

\[
{M}_{c - \varepsilon } \cap  U = \left\{  {-{x}_{1}^{2} - \cdots  - {x}_{k}^{2} + {x}_{k + 1} + \cdots  + {x}_{n}^{2} \leq   - \varepsilon }\right\}
\]

These regions are illustrated in Figure 17.15 for \( k = 1 \) and \( n = 2 \) . The set \( {M}_{c + \varepsilon } \) is the shaded portion. (We choose \( \varepsilon \) small enough so that \( U \) meets the level sets \( {f}^{-1}\left( {c + \varepsilon }\right) \) and \( {f}^{-1}\left( {c - \varepsilon }\right) \) .)

Let \( C \) be the subset of \( U \) defined by

\[
C = \left\{  {f \leq  c + \varepsilon ,{x}_{1}^{2} + \cdots  + {x}_{k}^{2} \leq  \delta }\right\}  ,
\]

where \( \delta \) is a small positive number, say smaller than \( {\varepsilon }^{2} \) . Note that \( C \) is homotopically equivalent to the cell \( {e}^{k} \) . Set \( B = {\bar{M}}_{c + \varepsilon } - \bar{C}.B \) is the shaded region in the picture in Figure 17.16. From the picture it is plausible that \( B \) can be contracted onto \( {M}_{c - \varepsilon } \) by moving along the vector field \( - \nabla f \) . Since \( {M}_{c + \varepsilon } \) is obtained from \( B \) by attaching \( C \) , up to homotopy

\[
{M}_{c + \varepsilon } \simeq  {M}_{c - \varepsilon } \cup  {e}^{k}.
\]

![bo_d7b6f8alb0pc73dd9avg_233_538_1084_508_434_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_233_538_1084_508_434_0.jpg)

Figure 17.16

A smooth real-valued function on a manifold all of whose critical points are nondegenerate is called a Morse function. It follows from the two preceding theorems that there is a very close relation between the topology of a manifold and the critical points of a Morse function. We next show that there are many Morse functions on any manifold. Our proof is taken from Guillemin and Pollack [1, pp. 43-45].

Lemma 17.17. Let \( U \) be an open subset of \( {\mathbb{R}}^{n} \) and \( f \) any smooth real-valued function on \( U \) . Then for almost all \( a = \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) in \( {\mathbb{R}}^{n} \) , the function \( {f}_{a}\left( x\right)  = \; f\left( x\right)  + {a}_{1}{x}_{1} + \cdots  + {a}_{n}{x}_{n} \) is a Morse function.

Proof. Recall that we denote the Jacobian matrix of a function \( h \) by \( D\left( h\right) \) . Define \( g\left( x\right)  = \left( {\partial f/\partial {x}_{1},\ldots ,\partial f/\partial {x}_{n}}\right) \) . Note that the Hessian of \( f \) is precisely the

Jacobian of \( g \) , and \( x \) is a nondegenerate critical point of \( f \) if and only if \( g\left( x\right)  = 0 \) and \( D\left( g\right) \left( x\right) \) is nonsingular. Let \( {g}_{a}\left( x\right)  = \left( {\partial {f}_{a}/\partial {x}_{1},\ldots ,\partial {f}_{a}/\partial {x}_{n}}\right) \) . Then \( {g}_{a}\left( x\right)  = g\left( x\right)  + a \) and \( D\left( {g}_{a}\right)  = D\left( g\right) \) . In this setup \( x \) is a critical point of \( {f}_{a} \) if and only if \( g\left( x\right)  =  - a \) ; it is nondegenerate if and only if in addition \( D\left( g\right) \left( x\right) \) is nonsingular, i.e., \( a \) is a regular value of \( g \) . By Sard’s theorem almost all \( a \) in \( {\mathbb{R}}^{n} \) are regular values of \( g \) . For any such \( a \) , the function \( {f}_{a} \) will be a Morse function on \( U \) .

Proposition 17.18. Let \( M \) be a manifold of dimension \( n \) in \( {\mathbb{R}}^{r} \) . For almost all \( a = \left( {{a}_{1},\ldots ,{a}_{r}}\right) \) in \( {\mathbb{R}}^{r} \) , the function \( f\left( x\right)  = {a}_{1}{x}_{1} + \cdots  + {a}_{r}{x}_{r} \) is a Morse function on \( M \) .

Proof. Let \( {x}_{1},\ldots ,{x}_{r} \) be the coordinate functions on \( {\mathbb{R}}^{r} \) . Every point \( x \) in \( M \) has a neighborhood \( U \) in \( M \) on which some \( n \) of \( {x}_{1},\ldots ,{x}_{r} \) form a coordinate system. (Proof: Since \( {T}_{x}M \rightarrow  {T}_{x}{\mathbb{R}}^{r} \) is injective, \( {T}_{x}^{ * }{\mathbb{R}}^{r} \rightarrow  {T}_{x}^{ * }M \) is surjective, so \( d{x}_{1},\ldots , d{x}_{r} \) restrict to a spanning set in the cotangent space \( {T}_{x}^{ * }M \) . If \( d{x}_{{i}_{1}},\ldots , d{x}_{{i}_{n}} \) is a basis for \( {T}_{x}^{ * }M \) , then \( {x}_{{i}_{1}},\ldots ,{x}_{{i}_{n}} \) is a set of local coordinates around \( x \) .) Because a manifold is by definition second countable, \( M \) can be covered by a countable number of such open sets, \( M = \mathop{\bigcup }\limits_{{i = 1}}^{\infty }{U}_{i} \) . Suppose \( {x}_{1},\ldots ,{x}_{n} \) form a local coordinate system on \( {U}_{i} \) . Fix \( \left( {{a}_{n + 1},\ldots {a}_{r}}\right) \) and define \( f\left( x\right)  = {a}_{n + 1}{x}_{n + 1} + \cdots  + {a}_{r}{x}_{r} \) on \( {U}_{i} \) . By Lemma 17.17, for almost all \( \left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , the function \( f\left( x\right)  + {a}_{1}{x}_{1} + \cdots  + {a}_{n}{x}_{n} \) is a Morse function on \( {U}_{i} \) . It follows that for almost all \( a = \left( {{a}_{1},\ldots ,{a}_{r}}\right) \) in \( {\mathbb{R}}^{r} \) , the function \( {f}_{a}\left( x\right)  = {a}_{1}{x}_{1} + \cdots  + {a}_{r}{x}_{r} \) is a Morse function on \( {U}_{i} \) . Let

\[
{A}_{i} = \left\{  {a \in  {\mathbb{R}}^{r} \mid  {f}_{a}\left( x\right) \text{ is not a Morse function on }{U}_{i}}\right\}  .
\]

If \( a \in  {\mathbb{R}}^{r} - \mathop{\bigcup }\limits_{{i = 1}}^{\infty }{A}_{i} \) , then \( {f}_{a}\left( x\right) \) is a Morse function on \( M \) . Since \( \mathop{\bigcup }\limits_{{i = 1}}^{\infty }{A}_{i} \) has measure zero, the proposition is proved.

Theorem 17.19. Every compact manifold \( M \) has the homotopy type of a finite CW complex.

Proof. By Whitney's embedding theorem (see de Rham [1, p. 12]), we may assume that \( M \) is a submanifold of some Euclidean space. Let \( f \) be a Morse function on \( M \) (the existence of \( f \) is guaranteed by Proposition 17.18). By the Morse lemma, the critical points of \( f \) are isolated. Since \( M \) is compact, \( f \) can have only finitely many critical points on \( M \) . Furthermore, for any real number \( a \) , the set \( {M}_{a} = {f}^{-1}\left( \left\lbrack  {-\infty , a}\right\rbrack  \right) \) is compact, as it is a closed subset of a compact set. Let \( {p}_{1},\ldots ,{p}_{r} \) be the critical points of index 0 . By the two main theorems of Morse theory (Theorems 17.15 and 17.16), up to homotopy \( M \) is constructed from \( {p}_{1},\ldots ,{p}_{r} \) by attaching cells, a cell of dimension \( k \) for each critical point of index \( k > 0 \) . The only question that remains is: are the cells attached in the order of increasing dimensions? Suppose not. Then at some point there is a cell \( {e}^{k} \) which is attached to a finite \( {CW} \) complex \( X \) via an attaching map \( f : {S}^{k - 1} \rightarrow  X \) whose image does not lie entirely in the \( \left( {k - 1}\right) \) -skeleton of \( X \) . If \( n > k - 1 \) , then \( f \) cannot surject onto an \( n \) -cell of \( X \) , so for each such \( n \) -cell \( {e}^{n} \) we can choose a point \( P \) in \( {e}^{n} - f\left( {S}^{k - 1}\right) \) and deform \( f \) to the boundary of \( {e}^{n} \) . In this way \( f \) can be deformed so that its image lies in the \( \left( {k - 1}\right) \) -skeleton of \( X \) . Thus up to homotopy the cells of \( M \) can be attached in the proper order and \( M \) has the homotopy type of a finite \( {CW} \) complex.

The Relation between Homotopy and Homology

The relation between the homotopy and the homology functors is a very subtle one. There is of course a natural homomorphism

\[
i : {\pi }_{q}\left( X\right)  \rightarrow  {H}_{q}\left( X\right)
\]

defined as follows: fix a generator \( u \) for \( {H}_{q}\left( {S}^{q}\right) \) and send \( \left\lbrack  f\right\rbrack \) in \( {\pi }_{q}\left( X\right) \) to \( {f}_{ * }\left( u\right) \) . In general \( i \) is neither injective nor surjective. We have seen that \( {H}_{q} \) is relatively computable. On the other hand, \( {\pi }_{q} \) is not; there is no analogue of the Mayer-Vietoris principle for \( {\pi }_{q} \) . For this reason, the following theorems are a cornerstone of homotopy theory.

Theorem 17.20. Let \( X \) be a path-connected space. Then \( {H}_{1}\left( X\right) \) is the Abelianization of \( {\pi }_{1}\left( X\right) \) , i.e., if \( \left\lbrack  {{\pi }_{1}\left( X\right) ,{\pi }_{1}\left( X\right) }\right\rbrack \) is the commutator subgroup of \( {\pi }_{1}\left( X\right) \) , then \( {H}_{1}\left( X\right)  = {\pi }_{1}\left( X\right) /\left\lbrack  {{\pi }_{1}\left( X\right) ,{\pi }_{1}\left( X\right) }\right\rbrack \) .

We will assume this theorem as known. Its proof may be found in, for instance, Greenberg [1, p. 48]. The higher-dimensional analogue is

Theorem 17.21 (Hurewicz Isomorphism Theorem). Let \( X \) be a simply connected path-connected CW complex. Then the first nontrivial homotopy and homology occur in the same dimension and are equal, i.e., given a positive integer \( n \geq  2 \) , if \( {\pi }_{q}\left( X\right)  = 0 \) for \( 1 \leq  q < n \) , then \( {H}_{q}\left( X\right)  = 0 \) for \( 1 \leq  q < n \) and \( {H}_{n}\left( X\right)  = {\pi }_{n}\left( X\right) . \)

Proof. To start the induction, consider the case \( n = 2 \) . The \( {E}^{2} \) term of the homology spectral sequence of the path fibration

![bo_d7b6f8alb0pc73dd9avg_235_721_1740_177_129_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_235_721_1740_177_129_0.jpg)

\( q \)

1 \( {H}_{1}\left( {\Omega X}\right) \)

0 \( \mathbb{Z} \) 0 \( {H}_{2}\left( X\right) \)

0 1 2

is

Thus

\[
{H}_{2}\left( X\right)  = {H}_{1}\left( {\Omega X}\right) \;\text{ because }{PX}\text{ has no homology }
\]

\[
= {\pi }_{1}\left( {\Omega X}\right) \;\text{ because }{\pi }_{1}\left( {\Omega X}\right)  = {\pi }_{2}\left( X\right) \text{ is Abelian }
\]

\[
= {\pi }_{2}\left( X\right) \text{ . }
\]

Now let \( n \) be any positive integer greater than 2. By the induction hypothesis applied to \( {\Omega X} \) ,

\[
{H}_{q}\left( {\Omega X}\right)  = 0\;\text{ for }q < n - 1
\]

and

\[
{H}_{n - 1}\left( {\Omega X}\right)  = {\pi }_{n - 1}\left( {\Omega X}\right)  = {\pi }_{n}\left( X\right) .
\]

The \( {E}_{2} \) term of the homology spectral sequence of the path fibration is

![bo_d7b6f8alb0pc73dd9avg_236_278_834_1078_373_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_236_278_834_1078_373_0.jpg)

Since \( {PX} \) has trivial homology,

\[
{H}_{q}\left( X\right)  = {H}_{q - 1}\left( {\Omega X}\right)  = 0\;\text{ for }1 \leq  q < n
\]

and

\[
{H}_{n}\left( X\right)  = {H}_{n - 1}\left( {\Omega X}\right)  = {\pi }_{n}\left( X\right) .
\]

REMARK 17.21.1. A careful reader should have noticed that there is a sleight of hand in this deceptively simple proof: because we developed the Leray spectral sequence for spaces with a good cover (Theorem 15.11 and its homology analogue), to be strictly correct, we must show that both \( X \) and \( {\Omega X} \) have good covers. By (17.13), the \( {CW} \) complex \( X \) is homotopy equivalent to a space with a good cover. Next we quote the theorem of Milnor that the loop space of a \( {CW} \) complex is again a \( {CW} \) complex (Milnor [1, Cor. 3, p. 276]). So, at least up to homotopy, \( {\Omega X} \) also has a good cover.

Actually the Hurewicz theorem is true for any path-connected topological space. This is a consequence of the \( {CW} \) -approximation theorem which, in the form that we need, states that given any topological space \( X \) there is a CW complex \( K \) and a map \( f : K \rightarrow  X \) which induces isomorphisms \( {f}_{ * } : {\pi }_{q}\left( K\right) \overset{ \sim  }{ \rightarrow  }{\pi }_{q}\left( X\right) \) and \( {f}_{ * } : {H}_{q}\left( K\right) \overset{ \sim  }{ \rightarrow  }{H}_{q}\left( X\right) \) in all homotopy and homology (Whitehead [1, Ch. V, Section 3, p. 219]). Thus, in the Hurewicz isomorphism theorem, we may drop the requirement that \( X \) be a \( {CW} \) complex.

The spectral sequence proof of the Hurewicz isomorphism theorem is due to Serre [2, pp. 271-274]. Actually, Serre's approach is slightly different; by developing a spectral sequence which is valid in much greater generality than ours, Serre could bypass the question of the existence of a good cover on a topological space. Of course, a price has to be paid for this greater generality; one has to work much harder to establish Serre's spectral sequence.

As a first and very important example, consider \( {S}^{n} \) again. It follows from the Hurewicz theorem and the homology of \( {S}^{n} \) that the homotopy groups of \( {S}^{n} \) in low dimensions are

\[
{\pi }_{q}\left( {S}^{n}\right)  = 0\;\text{ for }q < n
\]

and

\[
{\pi }_{n}\left( {S}^{n}\right)  = \mathbb{Z}
\]

## \( {\pi }_{3}\left( {S}^{2}\right) \) and the Hopf Invariant

Now that we have computed \( {\pi }_{q}\left( {S}^{n}\right) \) for \( q \leq  n \) , the first nontrivial computation of the homotopy of a sphere is \( {\pi }_{3}\left( {S}^{2}\right) \) . This can be done using the homotopy exact sequence of the Hopf fibration, as follows.

Let \( {S}^{3} \) be the unit sphere \( \left\{  {\left( {{z}_{0},{z}_{1}}\right) \left| \right| {z}_{0}\left| {{}^{2} + }\right| {z}_{1}{\left. \right| }^{2} = 1}\right\} \) in \( {\mathbb{C}}^{2} \) . Define an equivalence relation on \( {S}^{3} \) by

\[
\left( {{z}_{0},{z}_{1}}\right)  \sim  \left( {{w}_{0},{w}_{1}}\right) \;\text{ if and only if }\left( {{z}_{0},{z}_{1}}\right)  = \left( {\lambda {w}_{0},\lambda {w}_{1}}\right)
\]

for some complex number \( \lambda \) of absolute value 1 . The quotient \( {S}^{3}/ \sim \) is the complex projective space \( \mathbb{C}{P}^{1} \) and the fibering

\( {S}^{1} \rightarrow  {S}^{3} \)

\( {S}^{2} = \mathbb{C}{P}^{1} \)

is the Hopf fibration. From the exact homotopy sequence

\[
\cdots  \rightarrow  {\pi }_{q}\left( {S}^{1}\right)  \rightarrow  {\pi }_{q}\left( {S}^{3}\right)  \rightarrow  {\pi }_{q}\left( {S}^{2}\right)  \rightarrow  {\pi }_{q - 1}\left( {S}^{1}\right)  \rightarrow  \cdots
\]

and the fact that \( {\pi }_{q}\left( {S}^{1}\right)  = 0 \) for \( q \geq  2 \) (see Example 18.1(a)), we get \( {\pi }_{q}\left( {S}^{3}\right)  = \; {\pi }_{q}\left( {S}^{2}\right) \) for \( q \geq  3 \) . In particular \( {\pi }_{3}\left( {S}^{2}\right)  = \mathbb{Z} \) .

This homotopy group \( {\pi }_{3}\left( {S}^{2}\right) \) was first computed by H. Hopf in 1931 using a linking number argument which associates to each homotopy class of maps from \( {S}^{3} \) to \( {S}^{2} \) an integer now called the Hopf invariant. We give here an account of the Hopf invariant first in the dual language of differential forms and then in terms of the linking number. Thus the setting for this section is the differentiable category.

Let \( f : {S}^{3} \rightarrow  {S}^{2} \) be a differentiable map and let \( \alpha \) be a generator of \( {H}_{DR}^{2}\left( {S}^{2}\right) \) . Since \( {H}_{DR}^{2}\left( {S}^{3}\right)  = 0 \) , there exists a 1-form \( \omega \) on \( {S}^{3} \) such that \( {f}^{ * }\alpha  = {d\omega } \) . As will be shown below, the expression

\[
H\left( f\right)  = {\int }_{{S}^{3}}\omega  \land  {d\omega }
\]

is independent of the choice of \( \omega \) . We define \( H\left( f\right) \) to be the Hopf invariant of \( f \) .

More generally the same procedure defines the Hopf invariant for any differentiable map \( f : {S}^{{2n} - 1} \rightarrow  {S}^{n} \) . If \( \alpha \) is a generator of \( {H}_{DR}^{n}\left( {S}^{n}\right) \) , then \( {f}^{ * }\alpha  = {d\omega } \) for some \( \left( {n - 1}\right) \) -form \( \omega \) on \( {S}^{{2n} - 1} \) and the Hopf invariant of \( f \) is

\[
H\left( f\right)  = {\int }_{{S}^{{2n} - 1}}\omega  \land  {d\omega }.
\]

Proposition 17.22. (a) The definition of the Hopf invariant is independent of the choice of \( \omega \) .

(b) For odd \( n \) the Hopf invariant is 0 .

(c) Homotopic maps have the same Hopf invariant.

Proof. (a) Let \( {\omega }^{\prime } \) be another \( \left( {n - 1}\right) \) -form on \( {S}^{{2n} - 1} \) such that \( {f}^{ * }\alpha  = d{\omega }^{\prime } \) . Then \( 0 = d\left( {\omega  - {\omega }^{\prime }}\right) \) . Hence

\[
{\int }_{{S}^{{2n} - 1}}\omega  \land  {d\omega } - {\int }_{{S}^{{2n} - 1}}{\omega }^{\prime } \land  d{\omega }^{\prime } = {\int }_{{S}^{{2n} - 1}}\left( {\omega  - {\omega }^{\prime }}\right)  \land  {d\omega }
\]

\[
=  \pm  {\int }_{{S}^{{2n} - 1}}d\left( {\left( {\omega  - {\omega }^{\prime }}\right)  \land  \omega }\right)
\]

\[
= 0\text{ by Stokes’ theorem. }
\]

(b) Since \( \omega \) is even-dimensional,

\[
\omega  \land  {d\omega } = \frac{1}{2}d\left( {\omega  \land  \omega }\right) .
\]

By Stokes’ theorem, \( {\int }_{{S}^{{2n} - 1}}\omega  \land  {d\omega } = 0 \) .

(c) By (b) we may assume \( n \) even. Let \( F : {S}^{{2n} - 1} \times  I \rightarrow  {S}^{n} \) be a homotopy between the two maps \( {f}_{0} \) and \( {f}_{1} \) from \( {S}^{{2n} - 1} \) to \( {S}^{n} \) , where \( I = \left\lbrack  {0,1}\right\rbrack \) . If \( {i}_{0} \) is the inclusion

\[
{i}_{0} : {S}^{{2n} - 1} \rightarrow  {S}_{0} = {S}^{{2n} - 1} \times  \{ 0\}  \subset  {S}^{{2n} - 1} \times  I
\]

and similarly for \( {i}_{1} \) , then

\[
F \circ  {i}_{0} = {f}_{0}
\]

\[
F \circ  {i}_{1} = {f}_{1}
\]

Let \( \alpha \) be a generator of \( {H}_{DR}^{n}\left( {S}^{n}\right) \) . Then \( {F}^{ * }\alpha  = {d\omega } \) for some \( \left( {n - 1}\right) \) -form \( \omega \) on \( {S}^{{2n} - 1} \times  I \) . Define \( {i}_{0}^{ * }\omega  = {\omega }_{0} \) and \( {i}_{1}^{ * }\omega  = {\omega }_{1} \) . Then

\[
{f}_{0}^{ * }\alpha  = d{\omega }_{0}\;\text{ and }\;{f}_{1}^{ * }\alpha  = d{\omega }_{1}.
\]

Note that

\[
{\omega }_{0} \land  d{\omega }_{0} = {i}_{0}^{ * }\left( {\omega  \land  {d\omega }}\right)
\]

Hence,

\[
H\left( {f}_{1}\right)  - H\left( {f}_{0}\right)  = {\int }_{{S}^{{2n} - 1}}{\omega }_{1} \land  d{\omega }_{1} - {\int }_{{S}^{{2n} - 1}}{\omega }_{0} \land  d{\omega }_{0}
\]

\[
= {\int }_{{S}^{{2n} - 1}}{i}_{1}^{ * }\left( {\omega  \land  {d\omega }}\right)  - {\int }_{{S}^{{2n} - 1}}{i}_{0}^{ * }\left( {\omega  \land  {d\omega }}\right)
\]

\[
= {\int }_{{S}_{1}}\omega  \land  {d\omega } - {\int }_{{S}_{0}}\omega  \land  {d\omega }
\]

\[
= {\int }_{\partial \left( {{S}^{{2n} - 1} \times  I}\right) }\omega  \land  {d\omega }
\]

\[
= {\int }_{{S}^{{2n} - 1} \times  I}{d\omega } \land  {d\omega }\text{ by Stokes’ theorem }
\]

\[
= {\int }_{{S}^{{2n} - 1} \times  I}{F}^{ * }\left( {\alpha  \land  \alpha }\right)
\]

\[
= 0\text{ because }\alpha  \land  \alpha  \in  {\Omega }^{2n}\left( {\mathrm{\;S}}^{n}\right) \text{ . }
\]

Since homotopy groups can be computed using only smooth maps (Proposition 17.8.1), it follows from Proposition 17.22(c) that the Hopf invariant gives a map

\[
H : {\pi }_{{2n} - 1}\left( {S}^{n}\right)  \rightarrow  \mathbb{R}\text{ . }
\]

We leave it as an exercise to the reader to prove that \( H \) is in fact a homomorphism.

Actually the Hopf invariant is always an integer and is geometrically given by the linking number of the pre-images \( A = {f}^{-1}\left( p\right) \) and \( B = {f}^{-1}\left( q\right) \) of any two distinct regular values of \( f \) . In the classical case where \( n = 2 \) , these two submanifolds are two "circles" embedded in \( {S}^{3} \) . To fix the ideas we will first explain the linking concept for this case.

The linking number of two disjoint oriented circles \( A \) and \( B \) in \( {S}^{3} \) can be defined in several quite different but equivalent ways.

The Intersection-Theory Definition.

Choose a smooth surface \( D \) in \( {S}^{3} \) with boundary \( A \) such that \( D \) intersects \( B \) transversally (Figure 17.17). Set the linking number to be

\[
\operatorname{link}\left( {A, B}\right)  = \mathop{\sum }\limits_{{D \cap  B}} \pm  1
\]

Here the sum is extended over the points in the intersection of \( D \) with \( B \) and the sign is given by the usual convention: at a point \( x \) in \( D \cap  B \) , the sign is +1 or -1 according to whether the tangent space \( {T}_{x}{S}^{3} \) has or does not have the direct sum orientation of \( {T}_{x}D \oplus  {T}_{x}B \) (Guillemin and Pollack [1, p. 108]).

![bo_d7b6f8alb0pc73dd9avg_240_363_302_918_303_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_240_363_302_918_303_0.jpg)

Figure 17.17

It of course has to be shown that the linking number as defined is independent of the choice of \( D \) . This is a consequence of the discussion to follow.

## The Differential-Form Definition.

Choose disjoint open neighborhoods \( {W}_{A} \) and \( {W}_{B} \) of \( A \) and \( B \) and choose representatives \( {\eta }_{A} \) and \( {\eta }_{B} \) of the compact Poincaré duals of \( A \) and \( B \) in \( {H}_{c}^{2}\left( {W}_{A}\right) \) and \( {H}_{c}^{2}\left( {W}_{B}\right) \) . Because \( {H}_{DR}^{2}\left( {S}^{3}\right)  = 0 \) , the extensions of \( {\eta }_{A} \) and \( {\eta }_{B} \) by zero to all of \( {S}^{3} \) , also denoted \( {\eta }_{A} \) and \( {\eta }_{B} \) , are exact. Thus there are 1-forms \( {\omega }_{A} \) and \( {\omega }_{B} \) on \( {S}^{3} \) such that

\[
d{\omega }_{A} = {\eta }_{A}\;\text{ and }\;d{\omega }_{B} = {\eta }_{B}.
\]

In terms of these forms one would expect, naively, that the dual to the intersection-theory definition is the expression

\[
{\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{B}
\]

for if \( A = \partial D \) and \( {\eta }_{A} = d{\omega }_{A} \) , then in some sense \( D \) should correspond to \( {\omega }_{A} \) . So let this integral be the differential-form definition of the linking number of \( A \) and \( B \) . We have to check that it is independent of all the choices involved. Let \( {\omega }_{A}^{\prime } \) be some other form with \( d{\omega }_{A}^{\prime } = {\eta }_{A} \) . Then \( {\omega }_{A}^{\prime } - {\omega }_{A} \) is closed. So

\[
\begin{aligned} {\int }_{{S}^{3}}\left( {{\omega }_{A}^{\prime } - {\omega }_{A}}\right)  \land  {\eta }_{B} &  =  \pm  {\int }_{{S}^{3}}d\left\lbrack  {\left( {{\omega }_{A}^{\prime } - {\omega }_{A}}\right)  \land  {\omega }_{B}}\right\rbrack  \\   &  = 0. \end{aligned}
\]

On the other hand, if \( {\eta }_{B}^{\prime } \) is another representative of \( \left\lbrack  {\eta }_{B}\right\rbrack \) , then

\[
{\eta }_{B} - {\eta }_{B}^{\prime } = {d\mu }
\]

for some \( \mu \) in \( {\Omega }_{c}^{1}\left( {W}_{B}\right) \) . Hence,

\[
{\int }_{{S}^{3}}{\omega }_{A} \land  \left( {{\eta }_{B} - {\eta }_{B}^{\prime }}\right)  =  - {\int }_{{S}^{3}}d\left( {{\omega }_{A} \land  \mu }\right)  + {\int }_{{S}^{3}}{\eta }_{A} \land  \mu .
\]

Both terms on the right vanish: the first by Stokes' theorem, and the second because the supports of \( {\eta }_{A} \) and \( \mu \) are disjoint!

The differential-form definition is quite close to the Hopf invariant. To bring one into the other, we first choose disjoint neighborhoods \( {U}_{p} \) and \( {U}_{q} \) of the regular values \( p \) and \( q \) of \( f \) and set \( {W}_{A} = {f}^{-1}\left( {U}_{p}\right) \) and \( {W}_{B} = {f}^{-1}\left( {U}_{q}\right) \) . We next choose forms \( {\alpha }_{p} \) and \( {\alpha }_{q} \) in \( {\Omega }_{c}^{2}\left( {U}_{p}\right) \) and \( {\Omega }_{c}^{2}\left( {U}_{q}\right) \) representing the Poincaré duals of \( p \) and \( q \) and set \( {\eta }_{A} = {f}^{ * }{\alpha }_{p} \) and \( {\eta }_{B} = {f}^{ * }{\alpha }_{q} \) . According to the differential-form definition the linking number of \( {f}^{-1}\left( p\right)  = A \) and \( {f}^{-1}\left( q\right)  = B \) is then given by

\[
{\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{B}
\]

where \( {\omega }_{A} \) is a form on \( {S}^{3} \) with \( d{\omega }_{A} = {\eta }_{A} \) . On the other hand, as \( {\alpha }_{p} \) generates \( {H}_{DR}^{2}\left( {S}^{2}\right) \) , the Hopf invariant is given by

\[
H\left( f\right)  = {\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{A}.
\]

Because \( {\alpha }_{p} \) and \( {\alpha }_{q} \) are both representatives for the generator of \( {H}_{DR}^{2}\left( {S}^{2}\right) \) , there is a form \( \beta \) in \( {\Omega }^{1}\left( {S}^{2}\right) \) such that

\[
{\alpha }_{p} - {\alpha }_{q} = {d\beta }
\]

Hence,

\[
{\omega }_{A} \land  \left( {{\eta }_{A} - {\eta }_{B}}\right)  = {\omega }_{A} \land  {f}^{ * }{d\beta }
\]

\[
=  - d\left( {{\omega }_{A} \land  {f}^{ * }\beta }\right)  + \left( {d{\omega }_{A}}\right)  \land  {f}^{ * }\beta .
\]

The last term on the right equals

\[
{\eta }_{A} \land  {f}^{ * }\beta  = {f}^{ * }\left( {{\alpha }_{p} \land  \beta }\right) .
\]

But \( {\alpha }_{p} \land  \beta  \in  {\Omega }^{3}\left( {S}^{2}\right) \) and hence vanishes! By Stokes’ theorem it follows that

\[
{\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{B} = {\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{A} = H\left( f\right) ,
\]

as was to be shown.

Finally we prove the compatibility of the two definitions of the linking number. This will then also explain why the Hopf invariant is always an integer.

To start off one needs certain plausible constructions of differential topology. The first of these is that a surface such as \( D \) , which has boundary \( A \) , can always be extended by a small ribbon diffeomorphic to \( A \times  \left\lbrack  {0,1}\right\rbrack \) . More precisely, there exists an embedding

\[
\phi  : A \times  \left\lbrack  {-1,1}\right\rbrack   \hookrightarrow  {S}^{3}
\]

such that \( \phi \) maps \( A \times  \left\lbrack  {-1,0}\right\rbrack \) diffeomorphically onto a closed neighborhood of \( A = {\delta D} \) in \( D \) , with \( A \times  \{ 0\} \) going to \( A \) , and such that

\[
{D}_{1} = D \cup  \phi \left( {A \times  \left\lbrack  {0,1}\right\rbrack  }\right)
\]

is still a smoothly embedded manifold with boundary. If we set

\[
{D}_{-1} = D - \phi \left( {A \times  ( - 1,0\rbrack }\right) ,
\]

this construction exhibits \( D \) in a nested sequence of submanifolds with boundary

\[
{D}_{1} \supset  D \supset  {D}_{-1}
\]

with the interior of \( {D}_{1} - {D}_{-1} \) being diffeomorphic to \( A \times  \left( {-1,1}\right) \) . A map \( \phi \) of this type is often called a collar about \( \partial D \) , and the restriction of \( \phi \) to \( A \times  \left( {-1,1}\right) \) an open collar about \( \partial D \) .

Using this parametrization we can clearly construct a smooth function \( {\chi }_{A} \) on \( {D}_{1} \) such that

(1) \( {\chi }_{A} \equiv  0 \) near \( \partial {D}_{1} \) , and

(2) \( {\chi }_{A} \equiv  1 \) on a neighborhood of \( {D}_{-1} \) in \( {D}_{1} \) .

It follows that \( d{\chi }_{A} \) is a 1-form with compact support on the open collar \( {D}_{1}^{ \circ  } - {D}_{-1} \) , where \( {D}_{1}^{ \circ  } \) is the interior of \( {D}_{1} \) . Furthermore, \( d{\chi }_{A} \) represents the compact Poincaré dual of \( A \) in \( {\Omega }_{c}^{1}\left( {{D}_{1}^{ \circ  } - {D}_{-1}}\right) \) .

Next we choose a neighborhood of \( {D}_{1} \) in \( {S}^{3} \) , say \( W \) , small enough to admit a retraction

\[
r : W \rightarrow  {D}_{1}\text{ . }
\]

(For \( \varepsilon \) small enough an \( \varepsilon \) -neighborhood of \( {D}_{1} \) relative to some Riemannian structure on \( {S}^{3} \) will do.) Let \( T \) be a tubular neighborhood of \( {D}_{1} - \partial {D}_{1} \) in \( W - \partial {D}_{1} \) diffeomorphic to the unit disk bundle in the normal bundle of \( {D}_{1} - \partial {D}_{1} \) in \( W - \partial {D}_{1} \) and let \( {\omega }_{A}^{ \circ  } \) represent the Thom class of \( T \) in \( {\Omega }_{cv}^{1}\left( T\right) \) . See Figure 17.18.

![bo_d7b6f8alb0pc73dd9avg_242_424_1392_811_696_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_242_424_1392_811_696_0.jpg)

Figure 17.18

Now consider the 1-form

\[
{\omega }_{A} = \left( {{r}^{ * }{\chi }_{A}}\right) {\omega }_{A}^{ \circ  }.
\]

It has many virtues. First of all it has compact support in \( W \) and so can be extended by zero to all of \( {S}^{3} \) . This comes about because \( {\omega }_{A}^{ \circ  } \) has compact support normal to \( {D}_{1}^{ \circ  } \) and \( {r}^{ * }{\chi }_{A} \) vanishes identically near \( \partial {D}_{1} \) . Secondly, we see that if we set

\[
{W}_{A} = {r}^{-1}\left( {{D}_{1}^{ \circ  } - {D}_{-1}}\right) ,
\]

then \( d{\omega }_{A} \in  {\Omega }_{c}^{2}\left( {W}_{A}\right) \) and represents the compact Poincaré dual of \( A \) there.

We will use this \( {\omega }_{A} \) in the integral \( {\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{B} \) to complete the argument that

\[
{\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{B} = \mathop{\sum }\limits_{{D \cap  B}} \pm  1
\]

First choose a small enough neighborhood \( {W}_{B} \) of \( B \) , a small enough collar for \( D \) , and a small enough tubular neighborhood \( T \) for \( {D}_{1}^{ \circ  } \) so that (see Figure 17.19)

\[
{W}_{B} \cap  T \subset  {r}^{-1}\left( {D}_{-1}\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_243_470_1109_704_689_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_243_470_1109_704_689_0.jpg)

Figure 17.19

Once this is done \( {\omega }_{A} \) will equal \( {\omega }_{A}^{ \circ  } \) in the support of \( {\eta }_{B} \) since on \( {r}^{-1}\left( {D}_{-1}\right) \) the function \( {r}^{ * }{\chi }_{A} \) is identically 1 . Therefore, our integral can be rewritten in the form

(*)

\[
{\int }_{{S}^{3} - \partial {D}_{1}}{\omega }_{A}^{ \circ  } \land  {\eta }_{B}.
\]

But now \( {\omega }_{A}^{ \circ  } \) represents the Poincaré dual of \( {D}_{1}^{ \circ  } \) in \( {\Omega }^{1}\left( {{S}^{3} - \partial {D}_{1}}\right) \) and \( {\eta }_{B} \) the compact Poincaré dual of \( B \) in \( {\Omega }_{c}^{1}\left( {{S}^{3} - \partial {D}_{1}}\right) \) . In Section 6 we discussed the relation between the Thom isomorphism, Poincaré duality, and the transversal intersections of closed oriented submanifolds. Although (6.24) and (6.31) were stated for the closed Poincaré duals, the same discussion applies to the compact Poincaré duals, provided the relevant submanifolds are compact. Hence the integral (*) just counts the transversal intersection number of \( {D}_{1} \) with \( B \) . Thus

\[
{\int }_{{S}^{3}}{\omega }_{A} \land  {\eta }_{B} = \mathop{\sum }\limits_{{{D}_{1} \cap  B}} \pm  1 = \mathop{\sum }\limits_{{D \cap  B}} \pm  1
\]

the last being valid because the extension \( {D}_{1} \) intersects \( B \) no more often than \( D \) did.

REMARK. The arguments of this section of course extend to the higher-dimensional examples. In particular the two definitions of the linking number make sense and are equivalent whenever \( A \) and \( B \) are compact oriented submanifolds of an oriented manifold \( M \) satisfying the following conditions:

(1) \( A \) and \( B \) are disjoint;

(2) \( \dim A + \dim B = \dim M - 1 \) ;

(3) both \( A \) and \( B \) are bounding in the sense that their fundamental classes are homologous to zero in \( {H}_{ * }\left( M\right) \) .

Linking is therefore not a purely homological concept.

We cannot resist mentioning at this point that there is yet a third definition of the linking number of two disjoint oriented circles \( A \) and \( B \) in \( {S}^{3} \) .

The Degree Definition.

Remove a point \( p \) from \( {S}^{3} \) not on \( A \) or \( B \) and identify \( {S}^{3} - \{ p\} \) with \( {\mathbb{R}}^{3} \) . Let

\[
L : A \times  B \rightarrow  {S}^{2}
\]

be the map to the unit sphere in \( {\mathbb{R}}^{3} \) given by

\[
L\left( {x, y}\right)  = \frac{x - y}{\parallel x - y\parallel },
\]

where \( \parallel \;\parallel \) denotes the Euclidean length in \( {\mathbb{R}}^{3} \) . Give \( A \times  B \) the product orientation and \( {S}^{2} \) the standard orientation. Then

\[
\operatorname{link}\left( {A, B}\right)  = \deg L\text{ . }
\]

We close this section with two explicit computations of the Hopf invariant in the classical case, one using the differential-geometric and the other the intersection point of view. Just to be sure, if you will.

EXAMPLE 17.23 (The Hopf invariant of the Hopf fibration). Let \( {S}^{3} \) be the unit sphere in \( {\mathbb{C}}^{2} \) and \( f : {S}^{3} \rightarrow  \mathbb{C}{P}^{1} \) the natural map

\[
f : \left( {{z}_{0},{z}_{1}}\right)  \rightarrow  \left\lbrack  {{z}_{0},{z}_{1}}\right\rbrack
\]

where we write \( \left\lbrack  {{z}_{0},{z}_{1}}\right\rbrack \) for the homogeneous coordinates on \( \mathbb{C}{P}^{1} \) . If \( \mathbb{C}{P}^{1} \) is identified with the unit sphere \( {S}^{2} \) in \( {\mathbb{R}}^{3} \) , say via the stereographic projection, then the map \( f : {S}^{3} \rightarrow  {S}^{2} \) is the Hopf fibration. To compute its Hopf invariant, we proceed in five steps:

(a) Find a volume form \( \sigma \) on the 2-sphere.

(b) Write down a diffeomorphism \( g : \mathbb{C}{P}^{1} \simeq  {S}^{2} \) .

(c) Pull the generator \( \sigma \) of \( {H}^{2}\left( {S}^{2}\right) \) via \( g \) back to a generator \( \alpha \) of \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right) \) .

(d) Pull \( \alpha \) back to \( {S}^{3} \) via \( f \) and find a 1-form \( \omega \) such that \( {f}^{ * }\alpha  = {d\omega } \) on \( {S}^{3} \) .

(e) Compute \( {\int }_{{S}^{3}}\omega  \land  {d\omega } \) .

(a) A Volume Form on the 2-Sphere.

Let \( {u}_{1},{u}_{2} \) , and \( {u}_{3} \) be the standard coordinates of \( {\mathbb{R}}^{3} \) . By Exercise 4.3.1 a generator of \( {H}^{2}\left( {S}^{2}\right) \) is

\[
\sigma  = \frac{1}{4\pi }\left( {{u}_{1}d{u}_{2}d{u}_{3} - {u}_{2}d{u}_{1}d{u}_{2} + {u}_{3}d{u}_{1}d{u}_{2}}\right) .
\]

Since \( \left( {dr}\right)  \cdot  \sigma  = \left( {r/{4\pi }}\right) d{u}_{1}d{u}_{2}d{u}_{3} \) , which is the standard orientation on \( {\mathbb{R}}^{3} \) , the form \( \sigma \) represents the positive generator on \( {S}^{2} \) (see the discussion preceding Exercise 6.32).

Over the open set in \( {S}^{2} \) where \( {u}_{3} \neq  0 \) , the form \( \sigma \) has a simpler expression. For if

\[
{u}_{1}^{2} + {u}_{2}^{2} + {u}_{3}^{2} = 1
\]

then

\[
{u}_{1}d{u}_{1} + {u}_{2}d{u}_{2} + {u}_{3}d{u}_{3} = 0,
\]

so that we can eliminate \( d{u}_{3} \) from \( \sigma \) to get

(17.23.1)

\[
\sigma  = \frac{1}{4\pi }\frac{d{u}_{1}d{u}_{2}}{{u}_{3}}.
\]

(b) Stereographic Projection of \( {S}^{2} \) onto \( \mathbb{C}{P}^{1} \) .

In the homogeneous coordinates \( \left\lbrack  {{z}_{0},{z}_{1}}\right\rbrack \) on \( \mathbb{C}{P}^{1} \) , the single point \( \left\lbrack  {{z}_{0},0}\right\rbrack \) is called the point at infinity. On the open set \( {z}_{1} \neq  0 \) , we may use \( z = {z}_{0}/{z}_{1} \) as the coordinate and identify the point \( z = x + {iy} \) in \( \mathbb{C}{P}^{1} - \{ \left\lbrack  {1,0}\right\rbrack  \} \) with the point \( \left( {x, y,0}\right) \) of the \( \left( {{u}_{1},{u}_{2}}\right) \) -plane in \( {\mathbb{R}}^{3} \) . Then the stereographic projection from the north pole \( \left( {0,0,1}\right) \) maps \( {S}^{2} \) onto \( \mathbb{C}{P}^{1} \) , sending the north pole to the point at infinity (Figure 17.20). To find the inverse map \( g : \mathbb{C}{P}^{1} \rightarrow  {S}^{2} \) , note that the line through \( \left( {0,0,1}\right) \) and \( \left( {x, y,0}\right) \) has parametric equation \( \left( {0,0,1}\right)  + t\left( {x, y, - 1}\right) \) , which intersects the unit sphere when

\[
{t}^{2}{x}^{2} + {t}^{2}{y}^{2} + {\left( 1 - t\right) }^{2} = 1,
\]

that is,

\[
t = 0\;\text{ or }\;\frac{2}{1 + {x}^{2} + {y}^{2}}.
\]

Hence the inverse map \( g : \mathbb{C}{P}^{1} \rightarrow  {S}^{2} \subset  {\mathbb{R}}^{3} \) is given by

(17.23.2) \( z = x + {iy} \mapsto  \left( {\frac{2x}{1 + {x}^{2} + {y}^{2}},\frac{2y}{1 + {x}^{2} + {y}^{2}},\frac{-1 + {x}^{2} + {y}^{2}}{1 + {x}^{2} + {y}^{2}}}\right) \) .

![bo_d7b6f8alb0pc73dd9avg_246_290_891_1080_456_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_246_290_891_1080_456_0.jpg)

Figure 17.20

(c) The Generator of \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right) \) .

By pulling the generator \( \sigma \) in \( {H}^{2}\left( {S}^{2}\right) \) back to \( \mathbb{C}{P}^{1} \) we obtain a generator \( {g}^{ * }\sigma \) in \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right) \) . It follows from (17.23.1) and (17.23.2) that in the appropriate coordinate patch,

\[
{g}^{ * }\sigma  = \frac{1}{4\pi }\frac{d{u}_{1}d{u}_{2}}{{u}_{3}},
\]

where

\[
{u}_{1} = \frac{2x}{1 + {x}^{2} + {y}^{2}},\;{u}_{2} = \frac{2y}{1 + {x}^{2} + {y}^{2}},\;\text{ and }{u}_{3} = \frac{-1 + {x}^{2} + {y}^{2}}{1 + {x}^{2} + {y}^{2}}.
\]

In terms of \( z = x + {iy} \) , the form \( {g}^{ * }\sigma \) can be written as

\[
{g}^{ * }\sigma  =  - \frac{1}{\pi }\frac{dxdy}{{\left( 1 + {x}^{2} + {y}^{2}\right) }^{2}} =  - \frac{i}{2\pi }\frac{{dzd}\bar{z}}{{\left( 1 + {\left| z\right| }^{2}\right) }^{2}}.
\]

By convention the standard orientation on \( \mathbb{C}{P}^{1} \) is given locally by \( {dxdy} \) . Therefore the positive generator in \( {H}^{2}\left( {\mathbb{C}{P}^{1}}\right) \) is

\[
\alpha  =  - {g}^{ * }\sigma  = \frac{i}{2\pi }\frac{{dzd}\bar{z}}{{\left( 1 + {\left| z\right| }^{2}\right) }^{2}}.
\]

Since \( z = {z}_{0}/{z}_{1} \) , in terms of the homogeneous coordinates,

(17.23.3)

\[
\alpha  = \frac{i}{2\pi }\frac{\left( {{z}_{1}d{z}_{0} - {z}_{0}d{z}_{1}}\right) \left( {{\bar{z}}_{1}d{\bar{z}}_{0} - {\bar{z}}_{0}d{\bar{z}}_{1}}\right) }{{\left( {\left| {z}_{0}\right| }^{2} + {\left| {z}_{1}\right| }^{2}\right) }^{2}}.
\]

REMARK. If \( {S}^{2} \) and \( \mathbb{C}{P}^{1} \) are given their respective standard orientations, then the stereographic projection from \( {S}^{2} \) to \( \mathbb{C}{P}^{1} \) is orientation-reversing.

(d) Finding an \( \omega \) such that \( {f}^{ * }\alpha  = {d\omega } \) on \( {S}^{3} \) .

Let \( {z}_{0} = {x}_{1} + i{x}_{2} \) and \( {z}_{1} = {x}_{3} + i{x}_{4} \) be the coordinates on \( {\mathbb{C}}^{2} \) . Then the unit 3-sphere \( {S}^{3} \) is defined by

\[
{\left| {z}_{0}\right| }^{2} + {\left| {z}_{1}\right| }^{2} = {x}_{1}^{2} + {x}_{2}^{2} + {x}_{3}^{2} + {x}_{4}^{2} = 1.
\]

Hence \( \mathop{\sum }\limits_{{i = 1}}^{4}{x}_{i}d{x}_{i} = 0 \) on \( {S}^{3} \) . By a straightforward computation, replacing \( {z}_{0} \) and \( {z}_{1} \) in (17.23.3) by the \( {x}_{i} \) ’s, we find

\[
{f}^{ * }\alpha  = \frac{1}{\pi }\left( {d{x}_{1}d{x}_{2} + d{x}_{3}d{x}_{4}}\right)  = \frac{1}{\pi }d\left( {{x}_{1}d{x}_{2} + {x}_{3}d{x}_{4}}\right) .
\]

Therefore, we may take \( \omega \) to be

\[
\omega  = \frac{1}{\pi }\left( {{x}_{1}d{x}_{2} + {x}_{3}d{x}_{4}}\right) .
\]

(e) Computing the Integral.

The Hopf invariant of the Hopf fibration is

\[
H\left( f\right)  = {\int }_{{S}^{3}}\omega  \land  {d\omega }
\]

\[
= \frac{1}{{\pi }^{2}}{\int }_{{S}^{3}}{x}_{1}d{x}_{2}d{x}_{3}d{x}_{4} + {x}_{3}d{x}_{1}d{x}_{2}d{x}_{4}
\]

\[
= \frac{2}{{\pi }^{2}}{\int }_{{S}^{3}}{x}_{1}d{x}_{2}d{x}_{3}d{x}_{4}\text{ by symmetry. }
\]

Using spherical coordinates,

\[
{x}_{1} = \sin \xi \sin \phi \cos \theta
\]

\[
{x}_{2} = \sin \xi \sin \phi \sin \theta
\]

\[
{x}_{3} = \sin \xi \cos \phi
\]

\[
{x}_{4} = \cos \xi
\]

where \( 0 \leq  \xi  \leq  \pi ,0 \leq  \phi  \leq  \pi \) , and \( 0 \leq  \theta  \leq  {2\pi } \) , the integral becomes

\[
{\int }_{{S}^{3}}{x}_{1}d{x}_{2}d{x}_{3}d{x}_{4} = {\int }_{0}^{\pi }{\int }_{0}^{\pi }{\int }_{0}^{2\pi }{\sin }^{4}\xi {\sin }^{3}\phi {\cos }^{2}{\theta d\theta d\phi d\xi }
\]

\[
= {\pi }^{2}/2\text{ . }
\]

Therefore, the Hopf invariant of \( f \) is 1 .

This Hopf invariant may also be found geometrically, for by identifying \( {S}^{3} - \{ \) north pole \( \} \) with \( {\mathbb{R}}^{3} \) via the stereographic projection, it is possible to visualize the fibers of the Hopf fibration

\( {S}^{1} \rightarrow  {S}^{3} \)

\( {S}^{2} = \mathbb{C}{P}^{1} \)

and to compute the linking number of two fibers. We let \( {z}_{0} = {x}_{1} + i{x}_{2} \) , \( {z}_{1} = {x}_{3} + i{x}_{4} \) . Then the stereographic projection

\[
p : {S}^{3} - \{ \left( {0,0,0,1}\right) \}  \rightarrow  {\mathbb{R}}^{3} = \left\{  {{x}_{4} = 0}\right\}
\]

is given by

\[
\left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right)  \mapsto  \left( {\frac{{x}_{1}}{1 - {x}_{4}},\frac{{x}_{2}}{1 - {x}_{4}},\frac{{x}_{3}}{1 - {x}_{4}}}\right)
\]

This we see as follows. The line through the north pole \( \left( {0,0,0,1}\right) \) and the point \( \left( {{x}_{1},{x}_{2},{x}_{3},{x}_{4}}\right) \) has parametric equation \( \left( {0,0,0,1}\right)  + t\left( {{x}_{1},{x}_{2},{x}_{3}}\right. \) , \( {x}_{4} - 1) \) . It intersects \( {\mathbb{R}}^{3} = \left\{  {{x}_{4} = 0}\right\} \) at \( t = 1/\left( {1 - {x}_{4}}\right) \) , so the intersection point is

\[
\left( {\frac{{x}_{1}}{1 - {x}_{4}},\frac{{x}_{2}}{1 - {x}_{4}},\frac{{x}_{3}}{1 - {x}_{4}},0}\right) \text{ . }
\]

See Figure 17.21.

Note that the fiber \( {S}_{\infty } \) of the Hopf fibration over \( \left\lbrack  {1,0}\right\rbrack   \in  \mathbb{C}{P}^{1} \) is \( \left\{  \left( {{z}_{0},}\right. \right. \; 0) \in  {\mathbb{C}}^{2}\left\{  {\left| {z}_{0}\right|  = 1}\right\} \) and the fiber \( {S}_{0} \) over \( \left\lbrack  {0,1}\right\rbrack \) is \( \left\{  \left( {0,0,\cos \theta ,\sin \theta ) \in  {\mathbb{R}}^{4}}\right. \right. \) , \( \left. {0 \leq  \theta  \leq  {2\pi }}\right\} \) , both oriented counterclockwise in their planes. So via the stereographic projection \( {S}_{\infty } \) corresponds to the unit circle in the \( \left( {x}_{1}\right. \) , \( {x}_{2} \) )-plane while \( {S}_{0} \) corresponds to \( \left\{  {(0,0,\cos \theta /\left( {1 - \sin \theta }\right) ,0 \leq  \theta  \leq  {2\pi }\} }\right. \) , which is the \( {x}_{3} \) -axis with its usual orientation. Therefore the linking number

![bo_d7b6f8alb0pc73dd9avg_249_274_309_1067_488_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_249_274_309_1067_488_0.jpg)

Figure 17.21 of \( {S}_{\infty } \) and \( {S}_{0} \) is 1 . By the geometric interpretation of the Hopf invariant as a linking number, the Hopf invariant of the Hopf fibration is 1.

Exercise 17.24. (a) Given an integer \( q \) , show that for \( n \geq  q + 2 \) , the natural inclusion \( O\left( n\right)  \hookrightarrow  O\left( {n + 1}\right) \) induces an isomorphism \( {\pi }_{q}\left( {O\left( n\right) }\right)  \simeq  {\pi }_{q}\left( {O\left( {n + 1}\right) }\right) \) . For \( n \) sufficiently large, the homotopy group \( {\pi }_{q}\left( {O\left( n\right) }\right) \) is therefore independent of \( n \) and we can write \( {\pi }_{q}\left( O\right) \) . This is the \( q \) -th stable homotopy group of the orthogonal group.

(b) Given integers \( k \) and \( q \) , show that for \( n \geq  k + q + 2 \) ,

\[
{\pi }_{q}\left( {O\left( n\right) /O\left( {n - k}\right) }\right)  = 0.
\]

(c) Similarly, use the fiber bundle of \( {S}^{{2n} + 1} = U\left( {n + 1}\right) /U\left( n\right) \) to show that for \( {2n} \geq  q + 1 \) , the inclusion \( U\left( n\right)  \hookrightarrow  U\left( {n + 1}\right) \) induces an isomorphism

\[
{\pi }_{q}\left( {U\left( n\right) }\right)  \simeq  {\pi }_{q}\left( {U\left( {n + 1}\right) }\right) .
\]

Deduce that for \( n \geq  \left( {{2k} + q + 1}\right) /2 \) ,

\[
{\pi }_{q}\left( {U\left( n\right) /U\left( {n - k}\right) }\right)  = 0.
\]
