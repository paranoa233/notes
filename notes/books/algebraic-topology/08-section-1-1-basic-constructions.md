# 1.1 Basic Constructions

## The Fundamental Group

Algebraic topology can be roughly defined as the study of techniques for forming algebraic images of topological spaces. Most often these algebraic images are groups, but more elaborate structures such as rings, modules, and algebras also arise. The mechanisms that create these images - the 'lanterns' of algebraic topology, one might say - are known formally as functors and have the characteristic feature that they form images not only of spaces but also of maps. Thus, continuous maps between spaces are projected onto homomorphisms between their algebraic images, so topologically related spaces have algebraically related images.

With suitably constructed lanterns one might hope to be able to form images with enough detail to reconstruct accurately the shapes of all spaces, or at least of large and interesting classes of spaces. This is one of the main goals of algebraic topology, and to a surprising extent this goal is achieved. Of course, the lanterns necessary to do this are somewhat complicated pieces of machinery. But this machinery also has a certain intrinsic beauty.

This first chapter introduces one of the simplest and most important functors of algebraic topology, the fundamental group, which creates an algebraic image of a space from the loops in the space, the paths in the space starting and ending at the same point.

## The Idea of the Fundamental Group

To get a feeling for what the fundamental group is about, let us look at a few preliminary examples before giving the formal definitions.

Consider two linked circles \( A \) and \( B \) in \( {\mathbb{R}}^{3} \) , as shown in the figure. Our experience with actual links and chains tells us that since the two circles are linked, it is impossible to separate \( B \) from \( A \) by any continuous motion of \( B \) , such as pushing, pulling, or twisting. We could even take \( B \) to be made of rubber or stretchable string and allow completely general continuous deformations of \( B \) , staying in the complement of \( A \) at all times, and it would still be impossible to pull \( B \) off \( A \) . At least that is what intuition suggests, and the fundamental group will give a way of making this intuition mathematically rigorous.

![bo_d7dtv0s91nqc73eq8nv0_30_1209_151_381_247_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_30_1209_151_381_247_0.jpg)

Instead of having \( B \) link with \( A \) just once, we could make it link with \( A \) two or more times, as in the figures to the right. As a further variation, by assigning an orientation to \( B \) we can speak of \( B \) linking \( A \) a positive or a negative number of times, say positive when \( B \) comes forward through \( A \) and negative for the reverse direction. Thus for each nonzero integer \( n \) we have an oriented circle \( {B}_{n} \) linking \( {An} \) times, where by 'circle' we mean a curve homeomorphic to a circle. To complete the scheme, we could let \( {B}_{0} \) be a circle not linked to \( A \) at all.

![bo_d7dtv0s91nqc73eq8nv0_30_1212_645_378_459_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_30_1212_645_378_459_0.jpg)

Now, integers not only measure quantity, but they form a group under addition. Can the group operation be mimicked geometrically with some sort of addition operation on the oriented circles \( B \) linking \( A \) ? An oriented circle \( B \) can be thought of as a path traversed in time, starting and ending at the same point \( {x}_{0} \) , which we can choose to be any point on the circle. Such a path starting and ending at the same point is called a loop. Two different loops \( B \) and \( {B}^{\prime } \) both starting and ending at the same point \( {x}_{0} \) can be ’added’ to form a new loop \( B + {B}^{\prime } \) that travels first around \( B \) , then around \( {B}^{\prime } \) . For example, if \( {B}_{1} \) and \( {B}_{1}^{\prime } \) are loops each linking \( A \) once in the positive direction, then their sum \( {B}_{1} + {B}_{1}^{\prime } \) is deformable to \( {B}_{2} \) , linking \( A \) twice. Similarly, \( {B}_{1} + {B}_{-1} \) can be deformed to the loop \( {B}_{0} \) , unlinked from \( A \) . More generally, we see that \( {B}_{m} + {B}_{n} \) can be deformed to \( {B}_{m + n} \) for arbitrary integers \( m \) and \( n \) .

![bo_d7dtv0s91nqc73eq8nv0_30_606_1600_986_482_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_30_606_1600_986_482_0.jpg)

Note that in forming sums of loops we produce loops that pass through the basepoint more than once. This is one reason why loops are defined merely as continuous paths, which are allowed to pass through the same point many times. So if one is thinking of a loop as something made of stretchable string, one has to give the string the magical power of being able to pass through itself unharmed. However, we must be sure not to allow our loops to intersect the fixed circle \( A \) at any time, otherwise we could always unlink them from \( A \) .

Next we consider a slightly more complicated sort of linking, involving three circles forming a configuration known as the Borromean rings, shown at the left in the figure below. The interesting feature here is that if any one of the three circles is removed, the other two are not linked. In the same spirit as before, let us regard one of the circles, say \( C \) , as a loop in the complement of the other two, \( A \) and \( B \) , and we ask whether \( C \) can be continuously deformed to unlink it completely from \( A \) and \( B \) , always staying in the complement of \( A \) and \( B \) during the deformation. We can redraw the picture by pulling \( A \) and \( B \) apart, dragging \( C \) along, and then we see \( C \) winding back and forth between \( A \) and \( B \) as shown in the second figure above. In this new position, if we start at the point of \( C \) indicated by the dot and proceed in the direction given by the arrow, then we pass in sequence: (1) forward through \( A \) ,(2) forward through \( B \) ,(3) backward through \( A \) , and (4) backward through \( B \) . If we measure the linking of \( C \) with \( A \) and \( B \) by two integers, then the ’forwards’ and ’backwards’ cancel and both integers are zero. This reflects the fact that \( C \) is not linked with \( A \) or \( B \) individually.

![bo_d7dtv0s91nqc73eq8nv0_31_599_603_990_331_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_31_599_603_990_331_0.jpg)

To get a more accurate measure of how \( C \) links with \( A \) and \( B \) together, we regard the four parts (1)-(4) of \( C \) as an ordered sequence. Taking into account the directions in which these segments of \( C \) pass through \( A \) and \( B \) , we may deform \( C \) to the sum \( a + b - a - b \) of four loops as in the figure. We write the third and fourth loops as the negatives of the first two since they can be deformed to the first two, but with the opposite orientations, and as we saw in the preceding example, the sum of two oppositely oriented loops is deformable to a trivial loop, not linked with anything. We would like to view the expression \( a + b - a - b \) as lying in a nonabelian group, so that it is not automatically zero. Changing to the more usual multiplicative notation for nonabelian groups, it would be written \( {ab}{a}^{-1}{b}^{-1} \) , the commutator of \( a \) and \( b \) .

![bo_d7dtv0s91nqc73eq8nv0_31_1007_1615_583_499_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_31_1007_1615_583_499_0.jpg)

To shed further light on this example, suppose we modify it slightly so that the circles \( A \) and \( B \) are now linked, as in the next figure. The circle \( C \) can then be deformed into the position shown at the right, where it again represents the composite loop \( {ab}{a}^{-1}{b}^{-1} \) , where \( a \) and \( b \) are loops linking \( A \) and \( B \) . But from the picture on the left it is apparent that \( C \) can actually be unlinked completely from \( A \) and \( B \) . So in this case the product \( {ab}{a}^{-1}{b}^{-1} \) should be trivial.

![bo_d7dtv0s91nqc73eq8nv0_32_714_269_878_336_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_32_714_269_878_336_0.jpg)

The fundamental group of a space \( X \) will be defined so that its elements are loops in \( X \) starting and ending at a fixed basepoint \( {x}_{0} \in  X \) , but two such loops are regarded as determining the same element of the fundamental group if one loop can be continuously deformed to the other within the space \( X \) . (All loops that occur during deformations must also start and end at \( {x}_{0} \) .) In the first example above, \( X \) is the complement of the circle \( A \) , while in the other two examples \( X \) is the complement of the two circles \( A \) and \( B \) . In the second section in this chapter we will show:

- The fundamental group of the complement of the circle \( A \) in the first example is infinite cyclic with the loop \( B \) as a generator. This amounts to saying that every loop in the complement of \( A \) can be deformed to one of the loops \( {B}_{n} \) , and that \( {B}_{n} \) cannot be deformed to \( {B}_{m} \) if \( n \neq  m \) .

- The fundamental group of the complement of the two unlinked circles \( A \) and \( B \) in the second example is the nonabelian free group on two generators, represented by the loops \( a \) and \( b \) linking \( A \) and \( B \) . In particular, the commutator \( {ab}{a}^{-1}{b}^{-1} \) is a nontrivial element of this group.

- The fundamental group of the complement of the two linked circles \( A \) and \( B \) in the third example is the free abelian group on two generators, represented by the loops \( a \) and \( b \) linking \( A \) and \( B \) .

As a result of these calculations, we have two ways to tell when a pair of circles \( A \) and \( B \) is linked. The direct approach is given by the first example, where one circle is regarded as an element of the fundamental group of the complement of the other circle. An alternative and somewhat more subtle method is given by the second and third examples, where one distinguishes a pair of linked circles from a pair of unlinked circles by the fundamental group of their complement, which is abelian in one case and nonabelian in the other. This method is much more general: One can often show that two spaces are not homeomorphic by showing that their fundamental groups are not isomorphic, since it will be an easy consequence of the definition of the fundamental group that homeomorphic spaces have isomorphic fundamental groups.

This first section begins with the basic definitions and constructions, and then proceeds quickly to an important calculation, the fundamental group of the circle, using notions developed more fully in §1.3. More systematic methods of calculation are given in §1.2. These are sufficient to show for example that every group is realized as the fundamental group of some space. This idea is exploited in the Additional Topics at the end of the chapter, which give some illustrations of how algebraic facts about groups can be derived topologically, such as the fact that every subgroup of a free group is free.

## Paths and Homotopy

The fundamental group will be defined in terms of loops and deformations of loops. Sometimes it will be useful to consider more generally paths and their deformations, so we begin with this slight extra generality.

By a path in a space \( X \) we mean a continuous map \( f : I \rightarrow  X \) where \( I \) is the unit interval \( \left\lbrack  {0,1}\right\rbrack \) . The idea of continuously deforming a path, keeping its endpoints fixed, is made precise by the following definition. A homotopy of paths in \( X \) is a family \( {f}_{t} : I \rightarrow  X,0 \leq  t \leq  1 \) , such that

![bo_d7dtv0s91nqc73eq8nv0_33_999_1198_590_196_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_33_999_1198_590_196_0.jpg)

(1) The endpoints \( {f}_{t}\left( 0\right)  = {x}_{0} \) and \( {f}_{t}\left( 1\right)  = {x}_{1} \) are independent of \( t \) .

(2) The associated map \( F : I \times  I \rightarrow  X \) defined by \( F\left( {s, t}\right)  = {f}_{t}\left( s\right) \) is continuous.

When two paths \( {f}_{0} \) and \( {f}_{1} \) are connected in this way by a homotopy \( {f}_{t} \) , they are said to be homotopic. The notation for this is \( {f}_{0} \simeq  {f}_{1} \) .

Example 1.1: Linear Homotopies. Any two paths \( {f}_{0} \) and \( {f}_{1} \) in \( {\mathbb{R}}^{n} \) having the same endpoints \( {x}_{0} \) and \( {x}_{1} \) are homotopic via the homotopy \( {f}_{t}\left( s\right)  = \left( {1 - t}\right) {f}_{0}\left( s\right)  + t{f}_{1}\left( s\right) \) . During this homotopy each point \( {f}_{0}\left( s\right) \) travels along the line segment to \( {f}_{1}\left( s\right) \) at constant speed. This is because the line through \( {f}_{0}\left( s\right) \) and \( {f}_{1}\left( s\right) \) is linearly parametrized as \( {f}_{0}\left( s\right)  + t\left\lbrack  {{f}_{1}\left( s\right)  - {f}_{0}\left( s\right) }\right\rbrack   = \left( {1 - t}\right) {f}_{0}\left( s\right)  + t{f}_{1}\left( s\right) \) , with the segment from \( {f}_{0}\left( s\right) \) to \( {f}_{1}\left( s\right) \) covered by \( t \) values in the interval from 0 to 1 . If \( {f}_{1}\left( s\right) \) happens to equal \( {f}_{0}\left( s\right) \) then this segment degenerates to a point and \( {f}_{t}\left( s\right)  = {f}_{0}\left( s\right) \) for all \( t \) . This occurs in particular for \( s = 0 \) and \( s = 1 \) , so each \( {f}_{t} \) is a path from \( {x}_{0} \) to \( {x}_{1} \) . Continuity of the homotopy \( {f}_{t} \) as a map \( I \times  I \rightarrow  {\mathbb{R}}^{n} \) follows from continuity of \( {f}_{0} \) and \( {f}_{1} \) since the algebraic operations of vector addition and scalar multiplication in the formula for \( {f}_{t} \) are continuous.

This construction shows more generally that for a convex subspace \( X \subset  {\mathbb{R}}^{n} \) , all paths in \( X \) with given endpoints \( {x}_{0} \) and \( {x}_{1} \) are homotopic, since if \( {f}_{0} \) and \( {f}_{1} \) lie in \( X \) then so does the homotopy \( {f}_{t} \) .

Before proceeding further we need to verify a technical property:

Proposition 1.2. The relation of homotopy on paths with fixed endpoints in any space is an equivalence relation.

The equivalence class of a path \( f \) under the equivalence relation of homotopy will be denoted \( \left\lbrack  f\right\rbrack \) and called the homotopy class of \( f \) .

Proof: Reflexivity is evident since \( f \simeq  f \) by the constant homotopy \( {f}_{t} = f \) . Symmetry is also easy since if \( {f}_{0} \simeq  {f}_{1} \) via \( {f}_{t} \) , then \( {f}_{1} \simeq  {f}_{0} \) via the inverse homotopy \( {f}_{1 - t} \) . For transitivity, if \( {f}_{0} \simeq  {f}_{1} \) via \( {f}_{t} \) and if \( {f}_{1} = {g}_{0} \) with \( {g}_{0} \simeq  {g}_{1} \) via \( {g}_{t} \) , then \( {f}_{0} \simeq  {g}_{1} \) via the homotopy \( {h}_{t} \) that equals \( {f}_{2t} \) for \( 0 \leq  t \leq  1/2 \) and \( {\mathcal{G}}_{{2t} - 1} \) for \( 1/2 \leq  t \leq  1 \) . These two definitions agree for \( t = 1/2 \) since we assume \( {f}_{1} = {g}_{0} \) . Continuity of the associated map \( H\left( {s, t}\right)  = {h}_{t}\left( s\right) \) comes from the elementary fact, which will be used frequently without explicit mention, that a function defined on the union of two closed sets is continuous if it is continuous when restricted to each of the closed sets separately. In the case at hand we have \( H\left( {s, t}\right)  = F\left( {s,{2t}}\right) \) for \( 0 \leq  t \leq  1/2 \) and \( H\left( {s, t}\right)  = G\left( {s,{2t} - 1}\right) \) for \( 1/2 \leq  t \leq  1 \) where \( F \) and \( G \) are the maps \( I \times  I \rightarrow  X \) associated to the homotopies \( {f}_{t} \) and \( {g}_{t} \) . Since \( H \) is continuous on \( I \times  \left\lbrack  {0,1/2}\right\rbrack \) and on \( I \times  \left\lbrack  {1/2,1}\right\rbrack \) , it is continuous on \( I \times  I \) .

![bo_d7dtv0s91nqc73eq8nv0_34_1236_614_340_233_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_34_1236_614_340_233_0.jpg)

Given two paths \( f, g : I \rightarrow  X \) such that \( f\left( 1\right)  = g\left( 0\right) \) , there is a composition or product path \( f \cdot  g \) that traverses first \( f \) and then \( g \) , defined by the formula

\[
f \cdot  g\left( s\right)  = \left\{  \begin{array}{ll} f\left( {2s}\right) , & 0 \leq  s \leq  1/2 \\  g\left( {{2s} - 1}\right) , & 1/2 \leq  s \leq  1 \end{array}\right.
\]

Thus \( f \) and \( g \) are traversed twice as fast in order for \( f \cdot  g \) to be traversed in unit time. This product operation respects homotopy classes since if \( {f}_{0} \simeq  {f}_{1} \) and \( {g}_{0} \simeq  {g}_{1} \) via homotopies \( {f}_{t} \) and \( {g}_{t} \) , and if \( {f}_{0}\left( 1\right)  = {g}_{0}\left( 0\right) \) so that \( {f}_{0} \cdot  {g}_{0} \) is defined, then \( {f}_{t} \cdot  {g}_{t} \) is defined and provides a homotopy \( {f}_{0} \cdot  {g}_{0} \simeq  {f}_{1} \cdot  {g}_{1} \) .

![bo_d7dtv0s91nqc73eq8nv0_34_1164_1534_423_202_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_34_1164_1534_423_202_0.jpg)

In particular, suppose we restrict attention to paths \( f : I \rightarrow  X \) with the same starting and ending point \( f\left( 0\right)  = f\left( 1\right)  = {x}_{0} \in  X \) . Such paths are called loops, and the common starting and ending point \( {x}_{0} \) is referred to as the basepoint. The set of all homotopy classes \( \left\lbrack  f\right\rbrack \) of loops \( f : I \rightarrow  X \) at the basepoint \( {x}_{0} \) is denoted \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) .

Proposition 1.3. \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) is a group with respect to the product \( \left\lbrack  f\right\rbrack  \left\lbrack  g\right\rbrack   = \left\lbrack  {f \cdot  g}\right\rbrack \) .

This group is called the fundamental group of \( X \) at the basepoint \( {x}_{0} \) . We will see in Chapter 4 that \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) is the first in a sequence of groups \( {\pi }_{n}\left( {X,{x}_{0}}\right) \) , called homotopy groups, which are defined in an entirely analogous fashion using the \( n \) -dimensional cube \( {I}^{n} \) in place of \( I \) .

Proof: By restricting attention to loops with a fixed basepoint \( {x}_{0} \in  X \) we guarantee that the product \( f \cdot  g \) of any two such loops is defined. We have already observed that the homotopy class of \( f \cdot  g \) depends only on the homotopy classes of \( f \) and \( g \) , so the product \( \left\lbrack  f\right\rbrack  \left\lbrack  g\right\rbrack   = \left\lbrack  {f \cdot  g}\right\rbrack \) is well-defined. It remains to verify the three axioms for a group.

As a preliminary step, define a reparametrization of a path \( f \) to be a composition \( {f\varphi } \) where \( \varphi  : I \rightarrow  I \) is any continuous map such that \( \varphi \left( 0\right)  = 0 \) and \( \varphi \left( 1\right)  = 1 \) . Reparametrizing a path preserves its homotopy class since \( {f\varphi } \simeq  f \) via the homotopy \( f{\varphi }_{t} \) where \( {\varphi }_{t}\left( s\right)  = \left( {1 - t}\right) \varphi \left( s\right)  + {ts} \) so that \( {\varphi }_{0} = \varphi \) and \( {\varphi }_{1}\left( s\right)  = s \) . Note that \( \left( {1 - t}\right) \varphi \left( s\right)  + {ts} \) lies between \( \varphi \left( s\right) \) and \( s \) , hence is in \( I \) , so the composition \( f{\varphi }_{t} \) is defined.

If we are given paths \( f, g, h \) with \( f\left( 1\right)  = g\left( 0\right) \) and \( g\left( 1\right)  = h\left( 0\right) \) , then both products \( \left( {f \cdot  g}\right)  \cdot  h \) and \( f \cdot  \left( {g \cdot  h}\right) \) are defined, and \( f \cdot  \left( {g \cdot  h}\right) \) is a reparametrization of \( \left( {f \cdot  g}\right)  \cdot  h \) by the piecewise linear function \( \varphi \) whose graph is shown in the figure at the right. Hence \( \left( {f \cdot  g}\right)  \cdot  h \simeq  f \cdot  \left( {g \cdot  h}\right) \) . Restricting attention to loops at the basepoint \( {x}_{0} \) , this says the product in \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) is associative.

![bo_d7dtv0s91nqc73eq8nv0_35_1395_796_191_196_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_35_1395_796_191_196_0.jpg)

Given a path \( f : I \rightarrow  X \) , let \( c \) be the constant path at \( f\left( 1\right) \) , defined by \( c\left( s\right)  = f\left( 1\right) \) for all \( s \in  I \) . Then \( f \cdot  c \) is a reparametrization of \( f \) via the function \( \varphi \) whose graph is shown in the first figure at the right, so \( f \cdot  c \simeq  f \) . Similarly, \( c \cdot  f \simeq  f \) where \( c \) is now the constant path at \( f\left( 0\right) \) , using the reparametrization function in the second figure. Taking \( f \) to be a loop, we deduce that the homotopy class of the constant path at \( {x}_{0} \) is a two-sided identity in \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) .

![bo_d7dtv0s91nqc73eq8nv0_35_1196_1168_393_196_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_35_1196_1168_393_196_0.jpg)

For a path \( f \) from \( {x}_{0} \) to \( {x}_{1} \) , the inverse path \( \bar{f} \) from \( {x}_{1} \) back to \( {x}_{0} \) is defined by \( \bar{f}\left( s\right)  = f\left( {1 - s}\right) \) . To see that \( f \cdot  \bar{f} \) is homotopic to a constant path we use the homotopy \( {h}_{t} = {f}_{t} \cdot  {g}_{t} \) where \( {f}_{t} \) is the path that equals \( f \) on the interval \( \left\lbrack  {0,1 - t}\right\rbrack \) and that is stationary at \( f\left( {1 - t}\right) \) on the interval \( \left\lbrack  {1 - t,1}\right\rbrack \) , and \( {g}_{t} \) is the inverse path of \( {f}_{t} \) . We could also describe \( {h}_{t} \) in terms of the associated function \( H : I \times  I \rightarrow  X \) using the decomposition of \( I \times  I \) shown in the figure. On the bottom edge of the square \( H \) is given by \( f \cdot  \bar{f} \) and below the ’ \( V \) ’ we let \( H\left( {s, t}\right) \) be independent of \( t \) , while above the ’ \( V \) ’ we let \( H\left( {s, t}\right) \) be independent of \( s \) . Going back to the first description of \( {h}_{t} \) , we see that since \( {f}_{0} = f \) and \( {f}_{1} \) is the constant path \( c \) at \( {x}_{0},{h}_{t} \) is a homotopy from \( f \cdot  \bar{f} \) to \( c \cdot  \bar{c} = c \) . Replacing \( f \) by \( \bar{f} \) gives \( \bar{f} \cdot  f \simeq  c \) for \( c \) the constant path at \( {x}_{1} \) . Taking \( f \) to be a loop at the basepoint \( {x}_{0} \) , we deduce that \( \left\lbrack  \bar{f}\right\rbrack \) is a two-sided inverse for \( \left\lbrack  f\right\rbrack \) in \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) .

![bo_d7dtv0s91nqc73eq8nv0_35_1367_1650_216_191_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_35_1367_1650_216_191_0.jpg)

Example 1.4. For a convex set \( X \) in \( {\mathbb{R}}^{n} \) with basepoint \( {x}_{0} \in  X \) we have \( {\pi }_{1}\left( {X,{x}_{0}}\right)  = 0 \) , the trivial group, since any two loops \( {f}_{0} \) and \( {f}_{1} \) based at \( {x}_{0} \) are homotopic via the linear homotopy \( {f}_{t}\left( s\right)  = \left( {1 - t}\right) {f}_{0}\left( s\right)  + t{f}_{1}\left( s\right) \) , as described in Example 1.1.

It is not so easy to show that a space has a nontrivial fundamental group since one must somehow demonstrate the nonexistence of homotopies between certain loops. We will tackle the simplest example shortly, computing the fundamental group of the circle.

It is natural to ask about the dependence of \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) on the choice of the basepoint \( {x}_{0} \) . Since \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) involves only the path-component of \( X \) containing \( {x}_{0} \) , it is clear that we can hope to find a relation between \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) and \( {\pi }_{1}\left( {X,{x}_{1}}\right) \) for two basepoints \( {x}_{0} \) and \( {x}_{1} \) only if \( {x}_{0} \) and \( {x}_{1} \) lie in the same path-component of \( X \) . So let \( h : I \rightarrow  X \) be a path from \( {x}_{0} \) to \( {x}_{1} \) , with the inverse path \( \bar{h}\left( s\right)  = h\left( {1 - s}\right) \) from \( {x}_{1} \) back to \( {x}_{0} \) . We can then associate to each loop \( f \) based at \( {x}_{1} \) the loop \( h \cdot  f \cdot  \bar{h} \) based at \( {x}_{0} \) . Strictly speaking, we should choose an order of forming the product \( h \cdot  f \cdot  \bar{h} \) , either \( \left( {h \cdot  f}\right)  \cdot  \bar{h} \) or \( h \cdot  \left( {f \cdot  \bar{h}}\right) \) , but the two choices are homotopic and we are only interested in homotopy classes here. Alternatively, to avoid any ambiguity we could define a general \( n \) -fold product \( {f}_{1} \cdot  \cdots  \cdot  {f}_{n} \) in which the path \( {f}_{i} \) is traversed in the time interval \( \left\lbrack  {\frac{i - 1}{n},\frac{i}{n}}\right\rbrack \) . Either way, we define a change-of-basepoint map \( {\beta }_{h} : {\pi }_{1}\left( {X,{x}_{1}}\right)  \rightarrow  {\pi }_{1}\left( {X,{x}_{0}}\right) \) by \( {\beta }_{h}\left\lbrack  f\right\rbrack   = \left\lbrack  {h \cdot  f \cdot  \bar{h}}\right\rbrack \) . This is well-defined since if \( {f}_{t} \) is a homotopy of loops based at \( {x}_{1} \) then \( h \cdot  {f}_{t} \cdot  \bar{h} \) is a homotopy of loops based at \( {x}_{0} \) .

![bo_d7dtv0s91nqc73eq8nv0_36_1191_595_391_147_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_36_1191_595_391_147_0.jpg)

Proposition 1.5. The map \( {\beta }_{h} : {\pi }_{1}\left( {X,{x}_{1}}\right)  \rightarrow  {\pi }_{1}\left( {X,{x}_{0}}\right) \) is an isomorphism.

Proof: We see first that \( {\beta }_{h} \) is a homomorphism since \( {\beta }_{h}\left\lbrack  {f \cdot  g}\right\rbrack   = \left\lbrack  {h \cdot  f \cdot  g \cdot  \bar{h}}\right\rbrack   = \; \left\lbrack  {h \cdot  f \cdot  \bar{h} \cdot  h \cdot  g \cdot  \bar{h}}\right\rbrack   = {\beta }_{h}\left\lbrack  f\right\rbrack  {\beta }_{h}\left\lbrack  g\right\rbrack \) . Further, \( {\beta }_{h} \) is an isomorphism with inverse \( {\beta }_{\bar{h}} \) since \( {\beta }_{h}{\beta }_{\bar{h}}\left\lbrack  f\right\rbrack   = {\beta }_{h}\left\lbrack  {\bar{h} \cdot  f \cdot  h}\right\rbrack   = \left\lbrack  {h \cdot  \bar{h} \cdot  f \cdot  h \cdot  \bar{h}}\right\rbrack   = \left\lbrack  f\right\rbrack \) , and similarly \( {\beta }_{\bar{h}}{\beta }_{h}\left\lbrack  f\right\rbrack   = \left\lbrack  f\right\rbrack \) .

Thus if \( X \) is path-connected, the group \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) is, up to isomorphism, independent of the choice of basepoint \( {x}_{0} \) . In this case the notation \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) is often abbreviated to \( {\pi }_{1}\left( X\right) \) , or one could go further and write just \( {\pi }_{1}X \) .

In general, a space is called simply-connected if it is path-connected and has trivial fundamental group. The following result explains the name.

Proposition 1.6. A space \( X \) is simply-connected iff there is a unique homotopy class of paths connecting any two points in \( X \) .

Proof: Path-connectedness is the existence of paths connecting every pair of points, so we need be concerned only with the uniqueness of connecting paths. Suppose \( {\pi }_{1}\left( X\right)  = 0 \) . If \( f \) and \( g \) are two paths from \( {x}_{0} \) to \( {x}_{1} \) , then \( f \simeq  f \cdot  \bar{g} \cdot  g \simeq  g \) since the loops \( \bar{g} \cdot  g \) and \( f \cdot  \bar{g} \) are each homotopic to constant loops, using the assumption \( {\pi }_{1}\left( {X,{x}_{0}}\right)  = 0 \) in the latter case. Conversely, if there is only one homotopy class of paths connecting a basepoint \( {x}_{0} \) to itself, then all loops at \( {x}_{0} \) are homotopic to the constant loop and \( {\pi }_{1}\left( {X,{x}_{0}}\right)  = 0 \) .

## The Fundamental Group of the Circle

Our first real theorem will be the calculation \( {\pi }_{1}\left( {S}^{1}\right)  \approx  \mathbb{Z} \) . Besides its intrinsic interest, this basic result will have several immediate applications of some substance, and it will be the starting point for many more calculations in the next section. It should be no surprise then that the proof will involve some genuine work.

Theorem 1.7. \( {\pi }_{1}\left( {S}^{1}\right) \) is an infinite cyclic group generated by the homotopy class of the loop \( \omega \left( s\right)  = \left( {\cos {2\pi s},\sin {2\pi s}}\right) \) based at \( \left( {1,0}\right) \) .

Note that \( {\left\lbrack  \omega \right\rbrack  }^{n} = \left\lbrack  {\omega }_{n}\right\rbrack \) where \( {\omega }_{n}\left( s\right)  = \left( {\cos {2\pi ns},\sin {2\pi ns}}\right) \) for \( n \in  \mathbb{Z} \) . The theorem is therefore equivalent to the statement that every loop in \( {S}^{1} \) based at \( \left( {1,0}\right) \) is homotopic to \( {\omega }_{n} \) for a unique \( n \in  \mathbb{Z} \) . To prove this the idea will be to compare paths in \( {S}^{1} \) with paths in \( \mathbb{R} \) via the map \( p : \mathbb{R} \rightarrow  {S}^{1} \) given by \( p\left( s\right)  = \left( {\cos {2\pi s},\sin {2\pi s}}\right) \) . This map can be visualized geometrically by embedding \( \mathbb{R} \) in \( {\mathbb{R}}^{3} \) as the helix parametrized by \( s \mapsto  \left( {\cos {2\pi s},\sin {2\pi s}, s}\right) \) , and then \( p \) is the restriction to the helix of the projection of \( {\mathbb{R}}^{3} \) onto \( {\mathbb{R}}^{2},\left( {x, y, z}\right)  \mapsto  \left( {x, y}\right) \) . Observe that the loop \( {\omega }_{n} \) is the composition \( p{\widetilde{\omega }}_{n} \) where \( {\widetilde{\omega }}_{n} : I \rightarrow  \mathbb{R} \) is the path \( {\widetilde{\omega }}_{n}\left( s\right)  = {ns} \) , starting at 0 and ending at \( n \) , winding around the helix \( \left| n\right| \) times, upward if \( n > 0 \) and downward if \( n < 0 \) . The relation \( {\omega }_{n} = p{\widetilde{\omega }}_{n} \) is expressed by saying that \( {\widetilde{\omega }}_{n} \) is a lift of \( {\omega }_{n} \) .

![bo_d7dtv0s91nqc73eq8nv0_37_1353_734_239_460_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_37_1353_734_239_460_0.jpg)

We will prove the theorem by studying how paths in \( {S}^{1} \) lift to paths in \( \mathbb{R} \) . Most of the arguments will apply in much greater generality, and it is both more efficient and more enlightening to give them in the general context. The first step will be to define this context.

Given a space \( X \) , a covering space of \( X \) consists of a space \( \widetilde{X} \) and a map \( p : \widetilde{X} \rightarrow  X \) satisfying the following condition:

For each point \( x \in  X \) there is an open neighborhood \( U \) of \( x \) in \( X \) such that

(*) \( \;{p}^{-1}\left( U\right) \) is a union of disjoint open sets each of which is mapped homeomor-phically onto \( U \) by \( p \) .

Such a \( U \) will be called evenly covered. For example, for the previously defined map \( p : \mathbb{R} \rightarrow  {S}^{1} \) any open arc in \( {S}^{1} \) is evenly covered.

To prove the theorem we will need just the following two facts about covering spaces \( p : \widetilde{X} \rightarrow  X \) .

(a) For each path \( f : I \rightarrow  X \) starting at a point \( {x}_{0} \in  X \) and each \( {\widetilde{x}}_{0} \in  {p}^{-1}\left( {x}_{0}\right) \) there is a unique lift \( \widetilde{f} : I \rightarrow  \widetilde{X} \) starting at \( {\widetilde{x}}_{0} \) .

(b) For each homotopy \( {f}_{t} : I \rightarrow  X \) of paths starting at \( {x}_{0} \) and each \( {\widetilde{x}}_{0} \in  {p}^{-1}\left( {x}_{0}\right) \) there is a unique lifted homotopy \( {\widetilde{f}}_{t} : I \rightarrow  \widetilde{X} \) of paths starting at \( {\widetilde{x}}_{0} \) .

Before proving these facts, let us see how they imply the theorem.

Proof of Theorem 1.7: Let \( f : I \rightarrow  {S}^{1} \) be a loop at the basepoint \( {x}_{0} = \left( {1,0}\right) \) , representing a given element of \( {\pi }_{1}\left( {{S}^{1},{x}_{0}}\right) \) . By (a) there is a lift \( \widetilde{f} \) starting at 0 . This path \( \widetilde{f} \) ends at some integer \( n \) since \( p\widetilde{f}\left( 1\right)  = f\left( 1\right)  = {x}_{0} \) and \( {p}^{-1}\left( {x}_{0}\right)  = \mathbb{Z} \subset  \mathbb{R} \) . Another path in \( \mathbb{R} \) from 0 to \( n \) is \( {\widetilde{\omega }}_{n} \) , and \( \widetilde{f} \simeq  {\widetilde{\omega }}_{n} \) via the linear homotopy \( \left( {1 - t}\right) \widetilde{f} + t{\widetilde{\omega }}_{n} \) . Composing this homotopy with \( p \) gives a homotopy \( f \simeq  {\omega }_{n} \) so \( \left\lbrack  f\right\rbrack   = \left\lbrack  {\omega }_{n}\right\rbrack \) .

To show that \( n \) is uniquely determined by \( \left\lbrack  f\right\rbrack \) , suppose that \( f \simeq  {\omega }_{n} \) and \( f \simeq \; {\omega }_{m} \) , so \( {\omega }_{m} \simeq  {\omega }_{n} \) . Let \( {f}_{t} \) be a homotopy from \( {\omega }_{m} = {f}_{0} \) to \( {\omega }_{n} = {f}_{1} \) . By (b) this homotopy lifts to a homotopy \( {\widetilde{f}}_{t} \) of paths starting at 0 . The uniqueness part of (a) implies that \( {\widetilde{f}}_{0} = {\widetilde{\omega }}_{m} \) and \( {\widetilde{f}}_{1} = {\widetilde{\omega }}_{n} \) . Since \( {\widetilde{f}}_{t} \) is a homotopy of paths, the endpoint \( {\widetilde{f}}_{t}\left( 1\right) \) is independent of \( t \) . For \( t = 0 \) this endpoint is \( m \) and for \( t = 1 \) it is \( n \) , so \( m = n \) .

It remains to prove (a) and (b). Both statements can be deduced from a more general assertion about covering spaces \( p : \widetilde{X} \rightarrow  X \) :

(c) Given a map \( F : Y \times  I \rightarrow  X \) and a map \( \widetilde{F} : Y \times  \{ 0\}  \rightarrow  \widetilde{X} \) lifting \( F \mid  Y \times  \{ 0\} \) , then there is a unique map \( \widetilde{F} : Y \times  I \rightarrow  \widetilde{X} \) lifting \( F \) and restricting to the given \( \widetilde{F} \) on \( Y \times  \{ 0\} \) .

Statement (a) is the special case that \( Y \) is a point, and (b) is obtained by applying (c) with \( Y = I \) in the following way. The homotopy \( {f}_{t} \) in (b) gives a map \( F : I \times  I \rightarrow  X \) by setting \( F\left( {s, t}\right)  = {f}_{t}\left( s\right) \) as usual. A unique lift \( \widetilde{F} : I \times  \{ 0\}  \rightarrow  \widetilde{X} \) is obtained by an application of (a). Then (c) gives a unique lift \( \widetilde{F} : I \times  I \rightarrow  \widetilde{X} \) . The restrictions \( \widetilde{F} \mid  \{ 0\}  \times  I \) and \( \widetilde{F} \mid  \{ 1\}  \times  I \) are paths lifting constant paths, hence they must also be constant by the uniqueness part of (a). So \( {\widetilde{f}}_{t}\left( s\right)  = \widetilde{F}\left( {s, t}\right) \) is a homotopy of paths, and \( {\widetilde{f}}_{t} \) lifts \( {f}_{t} \) since \( p\widetilde{F} = F \) .

To prove (c) we will first construct a lift \( \widetilde{F} : N \times  I \rightarrow  \widetilde{X} \) for \( N \) some neighborhood in \( Y \) of a given point \( {y}_{0} \in  Y \) . Since \( F \) is continuous, every point \( \left( {{y}_{0}, t}\right)  \in  Y \times  I \) has a product neighborhood \( {N}_{t} \times  \left( {{a}_{t},{b}_{t}}\right) \) such that \( F\left( {{N}_{t} \times  \left( {{a}_{t},{b}_{t}}\right) }\right) \) is contained in an evenly covered neighborhood of \( F\left( {{y}_{0}, t}\right) \) . By compactness of \( \left\{  {y}_{0}\right\}   \times  I \) , finitely many such products \( {N}_{t} \times  \left( {{a}_{t},{b}_{t}}\right) \) cover \( \left\{  {y}_{0}\right\}   \times  I \) . This implies that we can choose a single neighborhood \( N \) of \( {y}_{0} \) and a partition \( 0 = {t}_{0} < {t}_{1} < \cdots  < {t}_{m} = 1 \) of \( I \) so that for each \( i, F\left( {N \times  \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  }\right) \) is contained in an evenly covered neighborhood \( {U}_{i} \) . Assume inductively that \( \widetilde{F} \) has been constructed on \( N \times  \left\lbrack  {0,{t}_{i}}\right\rbrack \) , starting with the given \( \widetilde{F} \) on \( N \times  \{ 0\} \) . We have \( F\left( {N \times  \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  }\right)  \subset  {U}_{i} \) , so since \( {U}_{i} \) is evenly covered there is an open set \( {\widetilde{U}}_{i} \subset  \widetilde{X} \) projecting homeomorphically onto \( {U}_{i} \) by \( p \) and containing the point \( \widetilde{F}\left( {{y}_{0},{t}_{i}}\right) \) . After replacing \( N \) by a smaller neighborhood of \( {y}_{0} \) we may assume that \( \widetilde{F}\left( {N \times  \left\{  {t}_{i}\right\}  }\right) \) is contained in \( {\widetilde{U}}_{i} \) , namely, replace \( N \times  \left\{  {t}_{i}\right\} \) by its intersection with \( {\left( \widetilde{F} \mid  N \times  \left\{  {t}_{i}\right\}  \right) }^{-1}\left( {\widetilde{U}}_{i}\right) \) . Now we can define \( \widetilde{F} \) on \( N \times  \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack \) to be the composition of \( F \) with the homeomorphism \( {p}^{-1} : {U}_{i} \rightarrow  {\widetilde{U}}_{i} \) . After a finite number of steps we eventually get a lift \( \widetilde{F} : N \times  I \rightarrow  \widetilde{X} \) for some neighborhood \( N \) of \( {y}_{0} \) .

Next we show the uniqueness part of (c) in the special case that \( Y \) is a point. In this case we can omit \( Y \) from the notation. So suppose \( \widetilde{F} \) and \( {\widetilde{F}}^{\prime } \) are two lifts of \( F : I \rightarrow  X \) such that \( \widetilde{F}\left( 0\right)  = {\widetilde{F}}^{\prime }\left( 0\right) \) . As before, choose a partition \( 0 = {t}_{0} < {t}_{1} < \cdots  < {t}_{m} = 1 \) of \( I \) so that for each \( i, F\left( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  \right) \) is contained in some evenly covered neighborhood \( {U}_{i} \) . Assume inductively that \( \widetilde{F} = {\widetilde{F}}^{\prime } \) on \( \left\lbrack  {0,{t}_{i}}\right\rbrack \) . Since \( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack \) is connected, so is \( \widetilde{F}\left( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  \right) \) , which must therefore lie in a single one of the disjoint open sets \( {\widetilde{U}}_{i} \) projecting homeomorphically to \( {U}_{i} \) as in \( \left( *\right) \) . By the same token, \( {\widetilde{F}}^{\prime }\left( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  \right) \) lies in a single \( {\widetilde{U}}_{i} \) , in fact in the same one that contains \( \widetilde{F}\left( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  \right) \) since \( {\widetilde{F}}^{\prime }\left( {t}_{i}\right)  = \widetilde{F}\left( {t}_{i}\right) \) . Because \( p \) is injective on \( {\widetilde{U}}_{i} \) and \( p\widetilde{F} = p{\widetilde{F}}^{\prime } \) , it follows that \( \widetilde{F} = {\widetilde{F}}^{\prime } \) on \( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack \) , and the induction step is finished.

The last step in the proof of (c) is to observe that since the \( \widetilde{F} \) ’s constructed above on sets of the form \( N \times  I \) are unique when restricted to each segment \( \{ y\}  \times  I \) , they must agree whenever two such sets \( N \times  I \) overlap. So we obtain a well-defined lift \( \widetilde{F} \) on all of \( Y \times  I \) . This \( \widetilde{F} \) is continuous since it is continuous on each \( N \times  I \) . And \( \widetilde{F} \) is unique since it is unique on each segment \( \{ y\}  \times  I \) .

Now we turn to some applications of the calculation of \( {\pi }_{1}\left( {S}^{1}\right) \) , beginning with a proof of the Fundamental Theorem of Algebra.

\( \parallel \) Theorem 1.8. Every nonconstant polynomial with coefficients in \( \mathbb{C} \) has a root in \( \mathbb{C} \) .

Proof: We may assume the polynomial is of the form \( p\left( z\right)  = {z}^{n} + {a}_{1}{z}^{n - 1} + \cdots  + {a}_{n} \) . If \( p\left( z\right) \) has no roots in \( \mathbb{C} \) , then for each real number \( r \geq  0 \) the formula

\[
{f}_{r}\left( s\right)  = \frac{p\left( {r{e}^{2\pi is}}\right) /p\left( r\right) }{\left| p\left( r{e}^{2\pi is}\right) /p\left( r\right) \right| }
\]

defines a loop in the unit circle \( {S}^{1} \subset  \mathbb{C} \) based at 1 . As \( r \) varies, \( {f}_{r} \) is a homotopy of loops based at 1 . Since \( {f}_{0} \) is the trivial loop, we deduce that the class \( \left\lbrack  {f}_{r}\right\rbrack   \in  {\pi }_{1}\left( {S}^{1}\right) \) is zero for all \( r \) . Now fix a large value of \( r \) , bigger than \( \left| {a}_{1}\right|  + \cdots  + \left| {a}_{n}\right| \) and bigger than 1 . Then for \( \left| z\right|  = r \) we have

\[
\left| {z}^{n}\right|  > \left( {\left| {a}_{1}\right|  + \cdots  + \left| {a}_{n}\right| }\right) \left| {z}^{n - 1}\right|  > \left| {{a}_{1}{z}^{n - 1}}\right|  + \cdots  + \left| {a}_{n}\right|  \geq  \left| {{a}_{1}{z}^{n - 1} + \cdots  + {a}_{n}}\right|
\]

From the inequality \( \left| {z}^{n}\right|  > \left| {{a}_{1}{z}^{n - 1} + \cdots  + {a}_{n}}\right| \) it follows that the polynomial \( {p}_{t}\left( z\right)  = \; {z}^{n} + t\left( {{a}_{1}{z}^{n - 1} + \cdots  + {a}_{n}}\right) \) has no roots on the circle \( \left| z\right|  = r \) when \( 0 \leq  t \leq  1 \) . Replacing \( p \) by \( {p}_{t} \) in the formula for \( {f}_{r} \) above and letting \( t \) go from 1 to 0, we obtain a homotopy from the loop \( {f}_{r} \) to the loop \( {\omega }_{n}\left( s\right)  = {e}^{2\pi ins} \) . By Theorem 1.7, \( {\omega }_{n} \) represents \( n \) times a generator of the infinite cyclic group \( {\pi }_{1}\left( {S}^{1}\right) \) . Since we have shown that \( \left\lbrack  {\omega }_{n}\right\rbrack   = \left\lbrack  {f}_{r}\right\rbrack   = 0 \) , we conclude that \( n = 0 \) . Thus the only polynomials without roots in \( \mathbb{C} \) are constants.

Our next application is the Brouwer fixed point theorem in dimension 2.

Theorem 1.9. Every continuous map \( h : {D}^{2} \rightarrow  {D}^{2} \) has a fixed point, that is, a point \( x \in  {D}^{2} \) with \( h\left( x\right)  = x \) .

Here we are using the standard notation \( {D}^{n} \) for the closed unit disk in \( {\mathbb{R}}^{n} \) , all vectors \( x \) of length \( \left| x\right|  \leq  1 \) . Thus the boundary of \( {D}^{n} \) is the unit sphere \( {S}^{n - 1} \) .

Proof: Suppose on the contrary that \( h\left( x\right)  \neq  x \) for all \( x \in  {D}^{2} \) . Then we can define a map \( r : {D}^{2} \rightarrow  {S}^{1} \) by letting \( r\left( x\right) \) be the point of \( {S}^{1} \) where the ray in \( {\mathbb{R}}^{2} \) starting at \( h\left( x\right) \) and passing through \( x \) leaves \( {D}^{2} \) . Continuity of \( r \) is clear since small perturbations of \( x \) produce small perturbations of \( h\left( x\right) \) , hence also small perturbations of the ray through these two points. The crucial property of \( r \) , besides continuity, is that \( r\left( x\right)  = x \) if \( x \in  {S}^{1} \) . Thus \( r \) is a retraction of \( {D}^{2} \) onto \( {S}^{1} \) . We will show that no such retraction can exist.

![bo_d7dtv0s91nqc73eq8nv0_40_1237_141_353_309_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_40_1237_141_353_309_0.jpg)

Let \( {f}_{0} \) be any loop in \( {S}^{1} \) . In \( {D}^{2} \) there is a homotopy of \( {f}_{0} \) to a constant loop, for example the linear homotopy \( {f}_{t}\left( s\right)  = \left( {1 - t}\right) {f}_{0}\left( s\right)  + t{x}_{0} \) where \( {x}_{0} \) is the basepoint of \( {f}_{0} \) . Since the retraction \( r \) is the identity on \( {S}^{1} \) , the composition \( r{f}_{t} \) is then a homotopy in \( {S}^{1} \) from \( r{f}_{0} = {f}_{0} \) to the constant loop at \( {x}_{0} \) . But this contradicts the fact that \( {\pi }_{1}\left( {S}^{1}\right) \) is nonzero.

This theorem was first proved by Brouwer around 1910, quite early in the history of topology. Brouwer in fact proved the corresponding result for \( {D}^{n} \) , and we shall obtain this generalization in Corollary 2.15 using homology groups in place of \( {\pi }_{1} \) . One could also use the higher homotopy group \( {\pi }_{n} \) . Brouwer’s original proof used neither homology nor homotopy groups, which had not been invented at the time. Instead it used the notion of degree for maps \( {S}^{n} \rightarrow  {S}^{n} \) , which we shall define in \( \text{ § }{2.2} \) using homology but which Brouwer defined directly in more geometric terms.

These proofs are all arguments by contradiction, and so they show just the existence of fixed points without giving any clue as to how to find one in explicit cases. Our proof of the Fundamental Theorem of Algebra was similar in this regard. There exist other proofs of the Brouwer fixed point theorem that are somewhat more constructive, for example the elegant and quite elementary proof by Sperner in 1928, which is explained very nicely in [Aigner-Ziegler 1999].

The techniques used to calculate \( {\pi }_{1}\left( {S}^{1}\right) \) can be applied to prove the Borsuk-Ulam theorem in dimension two:

Theorem 1.10. For every continuous map \( f : {S}^{2} \rightarrow  {\mathbb{R}}^{2} \) there exists a pair of antipodal points \( x \) and \( - x \) in \( {S}^{2} \) with \( f\left( x\right)  = f\left( {-x}\right) \) .

It may be that there is only one such pair of antipodal points \( x, - x \) , for example if \( f \) is simply orthogonal projection of the standard sphere \( {S}^{2} \subset  {\mathbb{R}}^{3} \) onto a plane.

The Borsuk-Ulam theorem holds more generally for maps \( {S}^{n} \rightarrow  {\mathbb{R}}^{n} \) , as we will show in Corollary 2B.7. The proof for \( n = 1 \) is easy since the difference \( f\left( x\right)  - f\left( {-x}\right) \) changes sign as \( x \) goes halfway around the circle, hence this difference must be zero for some \( x \) . For \( n \geq  2 \) the theorem is certainly less obvious. Is it apparent, for example, that at every instant there must be a pair of antipodal points on the surface of the earth having the same temperature and the same barometric pressure?

The theorem says in particular that there is no one-to-one continuous map from \( {S}^{2} \) to \( {\mathbb{R}}^{2} \) , so \( {S}^{2} \) is not homeomorphic to a subspace of \( {\mathbb{R}}^{2} \) , an intuitively obvious fact that is not easy to prove directly.

Proof: If the conclusion is false for \( f : {S}^{2} \rightarrow  {\mathbb{R}}^{2} \) , we can define a map \( g : {S}^{2} \rightarrow  {S}^{1} \) by \( g\left( x\right)  = \left( {f\left( x\right)  - f\left( {-x}\right) }\right) /\left| {f\left( x\right)  - f\left( {-x}\right) }\right| \) . Define a loop \( \eta \) circling the equator of \( {S}^{2} \subset  {\mathbb{R}}^{3} \) by \( \eta \left( s\right)  = \left( {\cos {2\pi s},\sin {2\pi s},0}\right) \) , and let \( h : I \rightarrow  {S}^{1} \) be the composed loop \( {g\eta } \) . Since \( g\left( {-x}\right)  =  - g\left( x\right) \) , we have the relation \( h\left( {s + 1/2}\right)  =  - h\left( s\right) \) for all \( s \) in the interval \( \left\lbrack  {0,1/2}\right\rbrack \) . As we showed in the calculation of \( {\pi }_{1}\left( {S}^{1}\right) \) , the loop \( h \) can be lifted to a path \( \widetilde{h} : I \rightarrow  \mathbb{R} \) . The equation \( h\left( {s + 1/2}\right)  =  - h\left( s\right) \) implies that \( \widetilde{h}\left( {s + 1/2}\right)  = \widetilde{h}\left( s\right)  + q/2 \) for some odd integer \( q \) that might conceivably depend on \( s \in  \left\lbrack  {0,1/2}\right\rbrack \) . But in fact \( q \) is independent of \( s \) since by solving the equation \( \widetilde{h}\left( {s + 1/2}\right)  = \widetilde{h}\left( s\right)  + q/2 \) for \( q \) we see that \( q \) depends continuously on \( s \in  \left\lbrack  {0,1/2}\right\rbrack \) , so \( q \) must be a constant since it is constrained to integer values. In particular, we have \( \widetilde{h}\left( 1\right)  = \widetilde{h}\left( {1/2}\right)  + q/2 = \widetilde{h}\left( 0\right)  + q \) . This means that \( h \) represents \( q \) times a generator of \( {\pi }_{1}\left( {S}^{1}\right) \) . Since \( q \) is odd, we conclude that \( h \) is not nullhomotopic. But \( h \) was the composition \( {g\eta } : I \rightarrow  {S}^{2} \rightarrow  {S}^{1} \) , and \( \eta \) is obviously nullhomotopic in \( {S}^{2} \) , so \( {g\eta } \) is nullhomotopic in \( {S}^{1} \) by composing a nullhomotopy of \( \eta \) with \( g \) . Thus we have arrived at a contradiction.

Corollary 1.11. Whenever \( {S}^{2} \) is expressed as the union of three closed sets \( {A}_{1},{A}_{2} \) , and \( {A}_{3} \) , then at least one of these sets must contain a pair of antipodal points \( \{ x, - x\} \) .

Proof: Let \( {d}_{i} : {S}^{2} \rightarrow  \mathbb{R} \) measure distance to \( {A}_{i} \) , that is, \( {d}_{i}\left( x\right)  = \mathop{\inf }\limits_{{y \in  {A}_{i}}}\left| {x - y}\right| \) . This is a continuous function, so we may apply the Borsuk-Ulam theorem to the map \( {S}^{2} \rightarrow  {\mathbb{R}}^{2}, x \mapsto  \left( {{d}_{1}\left( x\right) ,{d}_{2}\left( x\right) }\right) \) , obtaining a pair of antipodal points \( x \) and \( - x \) with \( {d}_{1}\left( x\right)  = {d}_{1}\left( {-x}\right) \) and \( {d}_{2}\left( x\right)  = {d}_{2}\left( {-x}\right) \) . If either of these two distances is zero, then \( x \) and \( - x \) both lie in the same set \( {A}_{1} \) or \( {A}_{2} \) since these are closed sets. On the other hand, if the distances from \( x \) and \( - x \) to \( {A}_{1} \) and \( {A}_{2} \) are both strictly positive, then \( x \) and \( - x \) lie in neither \( {A}_{1} \) nor \( {A}_{2} \) so they must lie in \( {A}_{3} \) .

To see that the number 'three' in this result is best possible, consider a sphere inscribed in a tetrahedron. Projecting the four faces of the tetrahedron radially onto the sphere, we obtain a cover of \( {S}^{2} \) by four closed sets, none of which contains a pair of antipodal points.

Assuming the higher-dimensional version of the Borsuk-Ulam theorem, the same arguments show that \( {S}^{n} \) cannot be covered by \( n + 1 \) closed sets without antipodal pairs of points, though it can be covered by \( n + 2 \) such sets, as the higher-dimensional analog of a tetrahedron shows. Even the case \( n = 1 \) is somewhat interesting: If the circle is covered by two closed sets, one of them must contain a pair of antipodal points. This is of course false for nonclosed sets since the circle is the union of two disjoint half-open semicircles.

The relation between the fundamental group of a product space and the fundamental groups of its factors is as simple as one could wish:

Proposition 1.12. \( {\pi }_{1}\left( {X \times  Y}\right) \) is isomorphic to \( {\pi }_{1}\left( X\right)  \times  {\pi }_{1}\left( Y\right) \) if \( X \) and \( Y \) are path-connected.

Proof: A basic property of the product topology is that a map \( f : Z \rightarrow  X \times  Y \) is continuous iff the maps \( g : Z \rightarrow  X \) and \( h : Z \rightarrow  Y \) defined by \( f\left( z\right)  = \left( {g\left( z\right) , h\left( z\right) }\right) \) are both continuous. Hence a loop \( f \) in \( X \times  Y \) based at \( \left( {{x}_{0},{y}_{0}}\right) \) is equivalent to a pair of loops \( g \) in \( X \) and \( h \) in \( Y \) based at \( {x}_{0} \) and \( {y}_{0} \) respectively. Similarly, a homotopy \( {f}_{t} \) of a loop in \( X \times  Y \) is equivalent to a pair of homotopies \( {g}_{t} \) and \( {h}_{t} \) of the corresponding loops in \( X \) and \( Y \) . Thus we obtain a bijection \( {\pi }_{1}\left( {X \times  Y,\left( {{x}_{0},{y}_{0}}\right) }\right)  \approx  {\pi }_{1}\left( {X,{x}_{0}}\right)  \times  {\pi }_{1}\left( {Y,{y}_{0}}\right) \) , \( \left\lbrack  f\right\rbrack   \mapsto  \left( {\left\lbrack  g\right\rbrack  ,\left\lbrack  h\right\rbrack  }\right) \) . This is obviously a group homomorphism, and hence an isomorphism.

Example 1.13: The Torus. By the proposition we have an isomorphism \( {\pi }_{1}\left( {{S}^{1} \times  {S}^{1}}\right)  \approx \; \mathbb{Z} \times  \mathbb{Z} \) . Under this isomorphism a pair \( \left( {p, q}\right)  \in  \mathbb{Z} \times  \mathbb{Z} \) corresponds to a loop that winds \( p \) times around one \( {S}^{1} \) factor of the torus and \( q \) times around the other \( {S}^{1} \) factor, for example the loop \( {\omega }_{pq}\left( s\right)  = \left( {{\omega }_{p}\left( s\right) ,{\omega }_{q}\left( s\right) }\right) \) . Interestingly, this loop can be knotted, as the figure shows for the case \( p = 3, q = 2 \) . The knots that arise in this fashion, the so-called torus knots, are studied in Example 1.24.

![bo_d7dtv0s91nqc73eq8nv0_42_1312_943_263_246_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_42_1312_943_263_246_0.jpg)

More generally, the \( n \) -dimensional torus, which is the product of \( n \) circles, has fundamental group isomorphic to the product of \( n \) copies of \( \mathbb{Z} \) . This follows by induction on \( n \) .

## Induced Homomorphisms

Suppose \( \varphi  : X \rightarrow  Y \) is a map taking the basepoint \( {x}_{0} \in  X \) to the basepoint \( {y}_{0} \in  Y \) . For brevity we write \( \varphi  : \left( {X,{x}_{0}}\right)  \rightarrow  \left( {Y,{y}_{0}}\right) \) in this situation. Then \( \varphi \) induces a homomorphism \( {\varphi }_{ * } : {\pi }_{1}\left( {X,{x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {Y,{y}_{0}}\right) \) , defined by composing loops \( f : I \rightarrow  X \) based at \( {x}_{0} \) with \( \varphi \) , that is, \( {\varphi }_{ * }\left\lbrack  f\right\rbrack   = \left\lbrack  {\varphi f}\right\rbrack \) . This induced map \( {\varphi }_{ * } \) is well-defined since a homotopy \( {f}_{t} \) of loops based at \( {x}_{0} \) yields a composed homotopy \( \varphi {f}_{t} \) of loops based at \( {y}_{0} \) , so \( {\varphi }_{ * }\left\lbrack  {f}_{0}\right\rbrack   = \left\lbrack  {\varphi {f}_{0}}\right\rbrack   = \left\lbrack  {\varphi {f}_{1}}\right\rbrack   = {\varphi }_{ * }\left\lbrack  {f}_{1}\right\rbrack \) . Furthermore, \( {\varphi }_{ * } \) is a homomorphism since \( \varphi \left( {f \cdot  g}\right)  = \left( {\varphi f}\right)  \cdot  \left( {\varphi g}\right) \) , both functions having the value \( {\varphi f}\left( {2s}\right) \) for \( 0 \leq  s \leq  1/2 \) and the value \( {\varphi g}\left( {{2s} - 1}\right) \) for \( {}^{1}/{}_{2} \leq  s \leq  1 \) .

Two basic properties of induced homomorphisms are:

- \( {\left( \varphi \psi \right) }_{ * } = {\varphi }_{ * }{\psi }_{ * } \) for a composition \( \left( {X,{x}_{0}}\right) \overset{\psi }{ \rightarrow  }\left( {Y,{y}_{0}}\right) \overset{\varphi }{ \rightarrow  }\left( {Z,{z}_{0}}\right) \) .

- \( {\mathbb{1}}_{ * } = \mathbb{1} \) , which is a concise way of saying that the identity map \( \mathbb{1} : X \rightarrow  X \) induces the identity map \( \mathbb{1} : {\pi }_{1}\left( {X,{x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {X,{x}_{0}}\right) \) .

The first of these follows from the fact that composition of maps is associative, so \( \left( {\varphi \psi }\right) f = \varphi \left( {\psi f}\right) \) , and the second is obvious. These two properties of induced homomorphisms are what makes the fundamental group a functor. The formal definition of a functor requires the introduction of certain other preliminary concepts, however, so we postpone this until it is needed in \( \text{ § }{2.3} \) .

As an application we can deduce easily that if \( \varphi \) is a homeomorphism with inverse \( \psi \) then \( {\varphi }_{ * } \) is an isomorphism with inverse \( {\psi }_{ * } \) since \( {\varphi }_{ * }{\psi }_{ * } = {\left( \varphi \psi \right) }_{ * } = {\mathbb{1}}_{ * } = \mathbb{1} \) and similarly \( {\psi }_{ * }{\varphi }_{ * } = \mathbb{1} \) . We will use this fact in the following calculation of the fundamental groups of higher-dimensional spheres:

\( \parallel \) Proposition 1.14. \( {\pi }_{1}\left( {S}^{n}\right)  = 0 \) if \( n \geq  2 \) .

The main step in the proof will be a general fact that will also play a key role in the next section:

Lemma 1.15. If a space \( X \) is the union of a collection of path-connected open sets \( {A}_{\alpha } \) each containing the basepoint \( {x}_{0} \in  X \) and if each intersection \( {A}_{\alpha } \cap  {A}_{\beta } \) is path-connected, then every loop in \( X \) at \( {x}_{0} \) is homotopic to a product of loops each of which is contained in a single \( {A}_{\alpha } \) .

Proof: Given a loop \( f : I \rightarrow  X \) at the basepoint \( {x}_{0} \) , we claim there is a partition \( 0 = \; {s}_{0} < {s}_{1} < \cdots  < {s}_{m} = 1 \) of \( I \) such that each subinterval \( \left\lbrack  {{s}_{i - 1},{s}_{i}}\right\rbrack \) is mapped by \( f \) to a single \( {A}_{\alpha } \) . Namely, since \( f \) is continuous, each \( s \in  I \) has an open neighborhood \( {V}_{s} \) in \( I \) mapped by \( f \) to some \( {A}_{\alpha } \) . We may in fact take \( {V}_{s} \) to be an interval whose closure is mapped to a single \( {A}_{\alpha } \) . Compactness of \( I \) implies that a finite number of these intervals cover \( I \) . The endpoints of this finite set of intervals then define the desired partition of \( I \) .

Denote the \( {A}_{\alpha } \) containing \( f\left( \left\lbrack  {{s}_{i - 1},{s}_{i}}\right\rbrack  \right) \) by \( {A}_{i} \) , and let \( {f}_{i} \) be the path obtained by restricting \( f \) to \( \left\lbrack  {{s}_{i - 1},{s}_{i}}\right\rbrack \) . Then \( f \) is the composition \( {f}_{1} \cdot  \cdots  \cdot  {f}_{m} \) with \( {f}_{i} \) a path in \( {A}_{i} \) . Since we assume \( {A}_{i} \cap  {A}_{i + 1} \) is path-connected, we may choose a path \( {g}_{i} \) in \( {A}_{i} \cap  {A}_{i + 1} \) from \( {x}_{0} \) to the point \( f\left( {s}_{i}\right)  \in  {A}_{i} \cap  {A}_{i + 1} \) . Consider the loop

\[
\left( {{f}_{1} \cdot  {\bar{g}}_{1}}\right)  \cdot  \left( {{g}_{1} \cdot  {f}_{2} \cdot  {\bar{g}}_{2}}\right)  \cdot  \left( {{g}_{2} \cdot  {f}_{3} \cdot  {\bar{g}}_{3}}\right)  \cdot  \cdots  \cdot  \left( {{g}_{m - 1} \cdot  {f}_{m}}\right)
\]

![bo_d7dtv0s91nqc73eq8nv0_43_1084_1423_508_354_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_43_1084_1423_508_354_0.jpg)

which is homotopic to \( f \) . This loop is a composition of loops each lying in a single \( {A}_{i} \) , the loops indicated by the parentheses.

Proof of Proposition 1.14: We can express \( {S}^{n} \) as the union of two open sets \( {A}_{1} \) and \( {A}_{2} \) each homeomorphic to \( {\mathbb{R}}^{n} \) such that \( {A}_{1} \cap  {A}_{2} \) is homeomorphic to \( {S}^{n - 1} \times  \mathbb{R} \) , for example by taking \( {A}_{1} \) and \( {A}_{2} \) to be the complements of two antipodal points in \( {S}^{n} \) . Choose a basepoint \( {x}_{0} \) in \( {A}_{1} \cap  {A}_{2} \) . If \( n \geq  2 \) then \( {A}_{1} \cap  {A}_{2} \) is path-connected. The lemma then applies to say that every loop in \( {S}^{n} \) based at \( {x}_{0} \) is homotopic to a product of loops in \( {A}_{1} \) or \( {A}_{2} \) . Both \( {\pi }_{1}\left( {A}_{1}\right) \) and \( {\pi }_{1}\left( {A}_{2}\right) \) are zero since \( {A}_{1} \) and \( {A}_{2} \) are homeomorphic to \( {\mathbb{R}}^{n} \) . Hence every loop in \( {S}^{n} \) is nullhomotopic.

Corollary 1.16. \( {\mathbb{R}}^{2} \) is not homeomorphic to \( {\mathbb{R}}^{n} \) for \( n \neq  2 \) .

Proof: Suppose \( f : {\mathbb{R}}^{2} \rightarrow  {\mathbb{R}}^{n} \) is a homeomorphism. The case \( n = 1 \) is easily disposed of since \( {\mathbb{R}}^{2} - \{ 0\} \) is path-connected but the homeomorphic space \( {\mathbb{R}}^{n} - \{ f\left( 0\right) \} \) is not path-connected when \( n = 1 \) . When \( n > 2 \) we cannot distinguish \( {\mathbb{R}}^{2} - \{ 0\} \) from \( {\mathbb{R}}^{n} - \{ f\left( 0\right) \} \) by the number of path-components, but we can distinguish them by their fundamental groups. Namely, for a point \( x \) in \( {\mathbb{R}}^{n} \) , the complement \( {\mathbb{R}}^{n} - \{ x\} \) is homeomorphic to \( {S}^{n - 1} \times  \mathbb{R} \) , so Proposition 1.12 implies that \( {\pi }_{1}\left( {{\mathbb{R}}^{n}-\{ x\} }\right) \) is isomorphic to \( {\pi }_{1}\left( {S}^{n - 1}\right)  \times  {\pi }_{1}\left( \mathbb{R}\right)  \approx  {\pi }_{1}\left( {S}^{n - 1}\right) \) . Hence \( {\pi }_{1}\left( {{\mathbb{R}}^{n}-\{ x\} }\right) \) is \( \mathbb{Z} \) for \( n = 2 \) and trivial for \( n > 2 \) , using Proposition 1.14 in the latter case.

The more general statement that \( {\mathbb{R}}^{m} \) is not homeomorphic to \( {\mathbb{R}}^{n} \) if \( m \neq  n \) can be proved in the same way using either the higher homotopy groups or homology groups. In fact, nonempty open sets in \( {\mathbb{R}}^{m} \) and \( {\mathbb{R}}^{n} \) can be homeomorphic only if \( m = n \) , as we will show in Theorem 2.26 using homology.

Induced homomorphisms allow relations between spaces to be transformed into relations between their fundamental groups. Here is an illustration of this principle:

Proposition 1.17. If a space \( X \) retracts onto a subspace \( A \) , then the homomorphism \( {i}_{ * } : {\pi }_{1}\left( {A,{x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {X,{x}_{0}}\right) \) induced by the inclusion \( i : A \hookrightarrow  X \) is injective. If \( A \) is a deformation retract of \( X \) , then \( {i}_{ * } \) is an isomorphism.

Proof: If \( r : X \rightarrow  A \) is a retraction, then \( {ri} = \mathbb{1} \) , hence \( {r}_{ * }{i}_{ * } = \mathbb{1} \) , which implies that \( {i}_{ * } \) is injective. If \( {r}_{t} : X \rightarrow  X \) is a deformation retraction of \( X \) onto \( A \) , so \( {r}_{0} = \mathbb{1},{r}_{t} \mid  A = \mathbb{1} \) , and \( {r}_{1}\left( X\right)  \subset  A \) , then for any loop \( f : I \rightarrow  X \) based at \( {x}_{0} \in  A \) the composition \( {r}_{t}f \) gives a homotopy of \( f \) to a loop in \( A \) , so \( {i}_{ * } \) is also surjective.

This gives another way of seeing that \( {S}^{1} \) is not a retract of \( {D}^{2} \) , a fact we showed earlier in the proof of the Brouwer fixed point theorem, since the inclusion-induced map \( {\pi }_{1}\left( {S}^{1}\right)  \rightarrow  {\pi }_{1}\left( {D}^{2}\right) \) is a homomorphism \( \mathbb{Z} \rightarrow  0 \) that cannot be injective.

The exact group-theoretic analog of a retraction is a homomorphism \( \rho \) of a group \( G \) onto a subgroup \( H \) such that \( \rho \) restricts to the identity on \( H \) . In the notation above, if we identify \( {\pi }_{1}\left( A\right) \) with its image under \( {i}_{ * } \) , then \( {r}_{ * } \) is such a homomorphism from \( {\pi }_{1}\left( X\right) \) onto the subgroup \( {\pi }_{1}\left( A\right) \) . The existence of a retracting homomorphism \( \rho  : G \rightarrow  H \) is quite a strong condition on \( H \) . If \( H \) is a normal subgroup, it implies that \( G \) is the direct product of \( H \) and the kernel of \( \rho \) . If \( H \) is not normal, then \( G \) is what is called in group theory the semi-direct product of \( H \) and the kernel of \( \rho \) .

Recall from Chapter 0 the general definition of a homotopy as a family \( {\varphi }_{t} : X \rightarrow  Y \) , \( t \in  I \) , such that the associated map \( \Phi  : X \times  I \rightarrow  Y,\Phi \left( {x, t}\right)  = {\varphi }_{t}\left( x\right) \) , is continuous. If \( {\varphi }_{t} \) takes a subspace \( A \subset  X \) to a subspace \( B \subset  Y \) for all \( t \) , then we speak of a homotopy of maps of pairs, \( {\varphi }_{t} : \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) . In particular, a basepoint-preserving homotopy \( {\varphi }_{t} : \left( {X,{x}_{0}}\right)  \rightarrow  \left( {Y,{y}_{0}}\right) \) is the case that \( {\varphi }_{t}\left( {x}_{0}\right)  = {y}_{0} \) for all \( t \) . Another basic property of induced homomorphisms is their invariance under such homotopies:

- If \( {\varphi }_{t} : \left( {X,{x}_{0}}\right)  \rightarrow  \left( {Y,{y}_{0}}\right) \) is a basepoint-preserving homotopy, then \( {\varphi }_{0 * } = {\varphi }_{1 * } \) .

This holds since \( {\varphi }_{0 * }\left\lbrack  f\right\rbrack   = \left\lbrack  {{\varphi }_{0}f}\right\rbrack   = \left\lbrack  {{\varphi }_{1}f}\right\rbrack   = {\varphi }_{1 * }\left\lbrack  f\right\rbrack \) , the middle equality coming from the homotopy \( {\varphi }_{t}f \) .

There is a notion of homotopy equivalence for spaces with basepoints. One says \( \left( {X,{x}_{0}}\right)  \simeq  \left( {Y,{y}_{0}}\right) \) if there are maps \( \varphi  : \left( {X,{x}_{0}}\right)  \rightarrow  \left( {Y,{y}_{0}}\right) \) and \( \psi  : \left( {Y,{y}_{0}}\right)  \rightarrow  \left( {X,{x}_{0}}\right) \) with homotopies \( {\varphi \psi } \simeq  \mathbb{1} \) and \( {\psi \varphi } \simeq  \mathbb{1} \) through maps fixing the basepoints. In this case the induced maps on \( {\pi }_{1} \) satisfy \( {\varphi }_{ * }{\psi }_{ * } = {\left( \varphi \psi \right) }_{ * } = {\mathbb{1}}_{ * } = \mathbb{1} \) and likewise \( {\psi }_{ * }{\varphi }_{ * } = \mathbb{1} \) , so \( {\varphi }_{ * } \) and \( {\psi }_{ * } \) are inverse isomorphisms \( {\pi }_{1}\left( {X,{x}_{0}}\right)  \approx  {\pi }_{1}\left( {Y,{y}_{0}}\right) \) . This somewhat formal argument gives another proof that a deformation retraction induces an isomorphism on fundamental groups, since if \( X \) deformation retracts onto \( A \) then \( \left( {X,{x}_{0}}\right)  \simeq  \left( {A,{x}_{0}}\right) \) for any choice of basepoint \( {x}_{0} \in  A \) .

Having to pay so much attention to basepoints when dealing with the fundamental group is something of a nuisance. For homotopy equivalences one does not have to be quite so careful, as the conditions on basepoints can actually be dropped:

Proposition 1.18. If \( \varphi  : X \rightarrow  Y \) is a homotopy equivalence, then the induced homomorphism \( {\varphi }_{ * } : {\pi }_{1}\left( {X,{x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {Y,\varphi \left( {x}_{0}\right) }\right) \) is an isomorphism for all \( {x}_{0} \in  X \) .

The proof will use a simple fact about homotopies that do not fix the basepoint:

Lemma 1.19. If \( {\varphi }_{t} : X \rightarrow  Y \) is a homotopy and \( h \) is the path \( {\varphi }_{t}\left( {x}_{0}\right) \) formed by the images of a basepoint \( {x}_{0} \in  X \) , then the three maps in the diagram at the right satisfy \( {\varphi }_{0 * } = {\beta }_{h}{\varphi }_{1 * } \) .

![bo_d7dtv0s91nqc73eq8nv0_45_1039_1282_544_185_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_45_1039_1282_544_185_0.jpg)

Proof: Let \( {h}_{t} \) be the restriction of \( h \) to the interval \( \left\lbrack  {0, t}\right\rbrack \) , with a reparametrization so that the domain of \( {h}_{t} \) is still \( \left\lbrack  {0,1}\right\rbrack \) . Explicitly, we can take \( {h}_{t}\left( s\right)  = h\left( {ts}\right) \) . Then if \( f \) is a loop in \( X \) at the basepoint \( {x}_{0} \) , the product \( {h}_{t} \cdot  \left( {{\varphi }_{t}f}\right)  \cdot  {\bar{h}}_{t} \) gives a homotopy of loops at \( {\varphi }_{0}\left( {x}_{0}\right) \) . Restricting this homotopy to \( t = 0 \) and \( t = 1 \) , we see that \( {\varphi }_{0 * }\left( \left\lbrack  f\right\rbrack  \right)  = \; {\beta }_{h}\left( {{\varphi }_{1 * }\left( \left\lbrack  f\right\rbrack  \right) }\right) \) .

![bo_d7dtv0s91nqc73eq8nv0_45_1147_1549_443_354_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_45_1147_1549_443_354_0.jpg)

Proof of 1.18: Let \( \psi  : Y \rightarrow  X \) be a homotopy-inverse for \( \varphi \) , so that \( {\varphi \psi } \simeq  \mathbb{1} \) and \( {\psi \varphi } \simeq  \mathbb{1} \) . Consider the maps

\[
{\pi }_{1}\left( {X,{x}_{0}}\right) \overset{{\varphi }_{ * }}{ \rightarrow  }{\pi }_{1}\left( {Y,\varphi \left( {x}_{0}\right) }\right) \overset{{\psi }_{ * }}{ \rightarrow  }{\pi }_{1}\left( {X,{\psi \varphi }\left( {x}_{0}\right) }\right) \overset{{\varphi }_{ * }}{ \rightarrow  }{\pi }_{1}\left( {Y,{\varphi \psi \varphi }\left( {x}_{0}\right) }\right)
\]

The composition of the first two maps is an isomorphism since \( {\psi \varphi } \simeq  \mathbb{1} \) implies that \( {\psi }_{ * }{\varphi }_{ * } = {\beta }_{h} \) for some \( h \) , by the lemma. In particular, since \( {\psi }_{ * }{\varphi }_{ * } \) is an isomorphism, \( {\varphi }_{ * } \) is injective. The same reasoning with the second and third maps shows that \( {\psi }_{ * } \) is injective. Thus the first two of the three maps are injections and their composition is an isomorphism, so the first map \( {\varphi }_{ * } \) must be surjective as well as injective.

## Exercises

1. Show that composition of paths satisfies the following cancellation property: If \( {f}_{0} \cdot  {g}_{0} \simeq  {f}_{1} \cdot  {g}_{1} \) and \( {g}_{0} \simeq  {g}_{1} \) then \( {f}_{0} \simeq  {f}_{1} \) .

2. Show that the change-of-basepoint homomorphism \( {\beta }_{h} \) depends only on the homotopy class of \( h \) .

3. For a path-connected space \( X \) , show that \( {\pi }_{1}\left( X\right) \) is abelian iff all basepoint-change homomorphisms \( {\beta }_{h} \) depend only on the endpoints of the path \( h \) .

4. A subspace \( X \subset  {\mathbb{R}}^{n} \) is said to be star-shaped if there is a point \( {x}_{0} \in  X \) such that, for each \( x \in  X \) , the line segment from \( {x}_{0} \) to \( x \) lies in \( X \) . Show that if a subspace \( X \subset  {\mathbb{R}}^{n} \) is locally star-shaped, in the sense that every point of \( X \) has a star-shaped neighborhood in \( X \) , then every path in \( X \) is homotopic in \( X \) to a piecewise linear path, that is, a path consisting of a finite number of straight line segments traversed at constant speed. Show this applies in particular when \( X \) is open or when \( X \) is a union of finitely many closed convex sets.

5. Show that for a space \( X \) , the following three conditions are equivalent:

(a) Every map \( {S}^{1} \rightarrow  X \) is homotopic to a constant map, with image a point.

(b) Every map \( {S}^{1} \rightarrow  X \) extends to a map \( {D}^{2} \rightarrow  X \) .

(c) \( {\pi }_{1}\left( {X,{x}_{0}}\right)  = 0 \) for all \( {x}_{0} \in  X \) .

Deduce that a space \( X \) is simply-connected iff all maps \( {S}^{1} \rightarrow  X \) are homotopic. [In this problem, 'homotopic' means 'homotopic without regard to basepoints'.]

6. We can regard \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) as the set of basepoint-preserving homotopy classes of maps \( \left( {{S}^{1},{s}_{0}}\right)  \rightarrow  \left( {X,{x}_{0}}\right) \) . Let \( \left\lbrack  {{S}^{1}, X}\right\rbrack \) be the set of homotopy classes of maps \( {S}^{1} \rightarrow  X \) , with no conditions on basepoints. Thus there is a natural map \( \Phi  : {\pi }_{1}\left( {X,{x}_{0}}\right)  \rightarrow  \left\lbrack  {{S}^{1}, X}\right\rbrack \) obtained by ignoring basepoints. Show that \( \Phi \) is onto if \( X \) is path-connected, and that \( \Phi \left( \left\lbrack  f\right\rbrack  \right)  = \Phi \left( \left\lbrack  g\right\rbrack  \right) \) iff \( \left\lbrack  f\right\rbrack \) and \( \left\lbrack  g\right\rbrack \) are conjugate in \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) . Hence \( \Phi \) induces a one-to-one correspondence between \( \left\lbrack  {{S}^{1}, X}\right\rbrack \) and the set of conjugacy classes in \( {\pi }_{1}\left( X\right) \) , when \( X \) is path-connected.

7. Define \( f : {S}^{1} \times  I \rightarrow  {S}^{1} \times  I \) by \( f\left( {\theta , s}\right)  = \left( {\theta  + {2\pi s}, s}\right) \) , so \( f \) restricts to the identity on the two boundary circles of \( {S}^{1} \times  I \) . Show that \( f \) is homotopic to the identity by a homotopy \( {f}_{t} \) that is stationary on one of the boundary circles, but not by any homotopy \( {f}_{t} \) that is stationary on both boundary circles. [Consider what \( f \) does to the path \( s \mapsto  \left( {{\theta }_{0}, s}\right) \) for fixed \( {\theta }_{0} \in  {S}^{1} \) .]

8. Does the Borsuk-Ulam theorem hold for the torus? In other words, for every map \( f : {S}^{1} \times  {S}^{1} \rightarrow  {\mathbb{R}}^{2} \) must there exist \( \left( {x, y}\right)  \in  {S}^{1} \times  {S}^{1} \) such that \( f\left( {x, y}\right)  = f\left( {-x, - y}\right) \) ?

9. Let \( {A}_{1},{A}_{2},{A}_{3} \) be compact sets in \( {\mathbb{R}}^{3} \) . Use the Borsuk-Ulam theorem to show that there is one plane \( P \subset  {\mathbb{R}}^{3} \) that simultaneously divides each \( {A}_{i} \) into two pieces of equal measure.

10. From the isomorphism \( {\pi }_{1}\left( {X \times  Y,\left( {{x}_{0},{y}_{0}}\right) }\right)  \approx  {\pi }_{1}\left( {X,{x}_{0}}\right)  \times  {\pi }_{1}\left( {Y,{y}_{0}}\right) \) it follows that loops in \( X \times  \left\{  {y}_{0}\right\} \) and \( \left\{  {x}_{0}\right\}   \times  Y \) represent commuting elements of \( {\pi }_{1}\left( {X \times  Y,\left( {{x}_{0},{y}_{0}}\right) }\right) \) . Construct an explicit homotopy demonstrating this.

11. If \( {X}_{0} \) is the path-component of a space \( X \) containing the basepoint \( {x}_{0} \) , show that the inclusion \( {X}_{0} \hookrightarrow  X \) induces an isomorphism \( {\pi }_{1}\left( {{X}_{0},{x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {X,{x}_{0}}\right) \) .

12. Show that every homomorphism \( {\pi }_{1}\left( {S}^{1}\right)  \rightarrow  {\pi }_{1}\left( {S}^{1}\right) \) can be realized as the induced homomorphism \( {\varphi }_{ * } \) of a map \( \varphi  : {S}^{1} \rightarrow  {S}^{1} \) .

13. Given a space \( X \) and a path-connected subspace \( A \) containing the basepoint \( {x}_{0} \) , show that the map \( {\pi }_{1}\left( {A,{x}_{0}}\right)  \rightarrow  {\pi }_{1}\left( {X,{x}_{0}}\right) \) induced by the inclusion \( A \hookrightarrow  X \) is surjective iff every path in \( X \) with endpoints in \( A \) is homotopic to a path in \( A \) .

14. Show that the isomorphism \( {\pi }_{1}\left( {X \times  Y}\right)  \approx  {\pi }_{1}\left( X\right)  \times  {\pi }_{1}\left( Y\right) \) in Proposition 1.12 is given by \( \left\lbrack  f\right\rbrack   \mapsto  \left( {{p}_{1 * }\left( \left\lbrack  f\right\rbrack  \right) ,{p}_{2 * }\left( \left\lbrack  f\right\rbrack  \right) }\right) \) where \( {p}_{1} \) and \( {p}_{2} \) are the projections of \( X \times  Y \) onto its two factors.

15. Given a map \( f : X \rightarrow  Y \) and a path \( h : I \rightarrow  X \) from \( {x}_{0} \) to \( {x}_{1} \) , show that \( {f}_{ * }{\beta }_{h} = {\beta }_{fh}{f}_{ * } \) in the diagram at the right.

![bo_d7dtv0s91nqc73eq8nv0_47_1031_1027_554_212_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_47_1031_1027_554_212_0.jpg)

16. Show that there are no retractions \( r : X \rightarrow  A \) in the following cases:

![bo_d7dtv0s91nqc73eq8nv0_47_1203_1304_365_202_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_47_1203_1304_365_202_0.jpg)

(a) \( X = {\mathbb{R}}^{3} \) with \( A \) any subspace homeomorphic to \( {S}^{1} \) .

(b) \( X = {S}^{1} \times  {D}^{2} \) with \( A \) its boundary torus \( {S}^{1} \times  {S}^{1} \) .

(c) \( X = {S}^{1} \times  {D}^{2} \) and \( A \) the circle shown in the figure.

(d) \( X = {D}^{2} \vee  {D}^{2} \) with \( A \) its boundary \( {S}^{1} \vee  {S}^{1} \) .

(e) \( X \) a disk with two points on its boundary identified and \( A \) its boundary \( {S}^{1} \vee  {S}^{1} \) .

(f) \( X \) the Möbius band and \( A \) its boundary circle.

17. Construct infinitely many nonhomotopic retractions \( {S}^{1} \vee  {S}^{1} \rightarrow  {S}^{1} \) .

18. Using Lemma 1.15, show that if a space \( X \) is obtained from a path-connected subspace \( A \) by attaching a cell \( {e}^{n} \) with \( n \geq  2 \) , then the inclusion \( A \hookrightarrow  X \) induces a surjection on \( {\pi }_{1} \) . Apply this to show:

(a) The wedge sum \( {S}^{1} \vee  {S}^{2} \) has fundamental group \( \mathbb{Z} \) .

(b) For a path-connected CW complex \( X \) the inclusion map \( {X}^{1} \hookrightarrow  X \) of its 1-skeleton induces a surjection \( {\pi }_{1}\left( {X}^{1}\right)  \rightarrow  {\pi }_{1}\left( X\right) \) . [For the case that \( X \) has infinitely many cells, see Proposition A.1 in the Appendix.]

19. Show that if \( X \) is a path-connected 1-dimensional CW complex with basepoint \( {x}_{0} \) a 0-cell, then every loop in \( X \) is homotopic to a loop consisting of a finite sequence of edges traversed monotonically. [See the proof of Lemma 1.15. This exercise gives an elementary proof that \( {\pi }_{1}\left( {S}^{1}\right) \) is cyclic generated by the standard loop winding once around the circle. The more difficult part of the calculation of \( {\pi }_{1}\left( {S}^{1}\right) \) is therefore the fact that no iterate of this loop is nullhomotopic.]

20. Suppose \( {f}_{t} : X \rightarrow  X \) is a homotopy such that \( {f}_{0} \) and \( {f}_{1} \) are each the identity map. Use Lemma 1.19 to show that for any \( {x}_{0} \in  X \) , the loop \( {f}_{t}\left( {x}_{0}\right) \) represents an element of the center of \( {\pi }_{1}\left( {X,{x}_{0}}\right) \) . [One can interpret the result as saying that a loop represents an element of the center of \( {\pi }_{1}\left( X\right) \) if it extends to a loop of maps \( X \rightarrow  X \) .]
