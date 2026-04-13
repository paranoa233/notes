# §1 Smooth Manifolds and Smooth Maps

First let us explain some of our terms. \( {R}^{k} \) denotes the \( k \) -dimensional euclidean space; thus a point \( {x\varepsilon }{R}^{k} \) is an \( k \) -tuple \( x = \left( {{x}_{1},\cdots ,{x}_{k}}\right) \) of real numbers.

Let \( U \subset  {R}^{k} \) and \( V \subset  {R}^{l} \) be open sets. A mapping \( f \) from \( U \) to \( V \) (written \( f : U \rightarrow  V \) ) is called smooth if all of the partial derivatives \( {\partial }^{n}f/\partial {x}_{{i}_{1}}\cdots \partial {x}_{{i}_{n}} \) exist and are continuous.

More generally let \( X \subset  {R}^{k} \) and \( Y \subset  {R}^{l} \) be arbitrary subsets of euclidean spaces. A map \( f : X \rightarrow  Y \) is called smooth if for each \( {x\varepsilon X} \) there exist an open set \( U \subset  {R}^{k} \) containing \( x \) and a smooth mapping \( F : U \rightarrow  {R}^{l} \) that coincides with \( f \) throughout \( U \cap  X \) .

If \( f : X \rightarrow  Y \) and \( g : Y \rightarrow  Z \) are smooth, note that the composition \( g \circ  f : X \rightarrow  Z \) is also smooth. The identity map of any set \( X \) is automatically smooth.

Definition. A map \( f : X \rightarrow  Y \) is called a diffeomorphism if \( f \) carries \( X \) homeomorphically onto \( Y \) and if both \( f \) and \( {f}^{-1} \) are smooth.

We can now indicate roughly what differential topology is about by saying that it studies those properties of a set \( X \subset  {R}^{k} \) which are invariant under diffeomorphism.

We do not, however, want to look at completely arbitrary sets \( X \) . The following definition singles out a particularly attractive and useful class.

DEFINITION. A subset \( M \subset  {R}^{k} \) is called a smooth manifold of dimension \( m \) if each \( {x\varepsilon M} \) has a neighborhood \( W \cap  M \) that is diffeomorphic to an open subset \( U \) of the euclidean space \( {R}^{m} \) .

Any particular diffeomorphism \( g : U \rightarrow  W \cap  M \) is called a parametrization of the region \( W \cap  M \) . (The inverse diffeomorphism \( W \cap  M \rightarrow  U \) is called a system of coordinates on \( W \cap  M \) .)

![bo_d7du9valb0pc73deirc0_12_238_271_858_403_0.jpg](images/bo_d7du9valb0pc73deirc0_12_238_271_858_403_0.jpg)

Figure 1. Parametrization of a region in \( M \)

Sometimes we will need to look at manifolds of dimension zero. By definition, \( M \) is a manifold of dimension zero if each \( {x\varepsilon M} \) has a neighborhood \( W \cap  M \) consisting of \( x \) alone.

Examples. The unit sphere \( {S}^{2} \) , consisting of all \( \left( {x, y, z}\right) \) ε \( {R}^{3} \) with \( {x}^{2} + {y}^{2} + {z}^{2} = 1 \) is a smooth manifold of dimension 2 . In fact the diffeomorphism

\[
\left( {x, y}\right)  \rightarrow  \left( {x, y,\sqrt{1 - {x}^{2} - {y}^{2}}}\right) ,
\]

for \( {x}^{2} + {y}^{2} < 1 \) , parametrizes the region \( z > 0 \) of \( {S}^{2} \) . By interchanging the roles of \( x, y, z \) , and changing the signs of the variables, we obtain similar parametrizations of the regions \( x > 0, y > 0, x < 0, y < 0 \) , and \( z < 0 \) . Since these cover \( {S}^{2} \) , it follows that \( {S}^{2} \) is a smooth manifold.

More generally the sphere \( {S}^{n - 1} \subset  {R}^{n} \) consisting of all \( \left( {{x}_{1},\cdots ,{x}_{n}}\right) \) with \( \sum {x}_{i}^{2} = 1 \) is a smooth manifold of dimension \( n - 1 \) . For example \( {S}^{0} \subset  {R}^{1} \) is a manifold consisting of just two points.

A somewhat wilder example of a smooth manifold is given by the set of all \( \left( {x, y}\right) \) ε \( {R}^{2} \) with \( x \neq  0 \) and \( y = \sin \left( {1/x}\right) \) .

## TANGENT SPACES AND DERIVATIVES

To define the notion of derivative \( d{f}_{x} \) for a smooth map \( f : M \rightarrow  N \) of smooth manifolds, we first associate with each \( {x\varepsilon M} \subset  {R}^{k} \) a linear subspace \( T{M}_{x} \subset  {R}^{k} \) of dimension \( m \) called the tangent space of \( M \) at \( x \) . Then \( d{f}_{x} \) will be a linear mapping from \( T{M}_{x} \) to \( T{N}_{y} \) , where \( y = f\left( x\right) \) . Elements of the vector space \( T{M}_{x} \) are called tangent vectors to \( M \) at \( x \) .

Intuitively one thinks of the \( m \) -dimensional hyperplane in \( {R}^{k} \) which best approximates \( M \) near \( x \) ; then \( T{M}_{x} \) is the hyperplane through the origin that is parallel to this. (Compare Figures 1 and 2.) Similarly one thinks of the nonhomogeneous linear mapping from the tangent hyperplane at \( x \) to the tangent hyperplane at \( y \) which best approximates \( f \) . Translating both hyperplanes to the origin, one obtains \( d{f}_{x} \) .

Before giving the actual definition, we must study the special case of mappings between open sets. For any open set \( U \subset  {R}^{k} \) the tangent space \( T{U}_{x} \) is defined to be the entire vector space \( {R}^{k} \) . For any smooth map \( f : U \rightarrow  V \) the derivative

\[
d{f}_{x} : {R}^{k} \rightarrow  {R}^{l}
\]

is defined by the formula

\[
d{f}_{x}\left( h\right)  = \mathop{\lim }\limits_{{t \rightarrow  0}}\left( {f\left( {x + {th}}\right)  - f\left( x\right) }\right) /t
\]

for \( {x\varepsilon U},{h\varepsilon }{R}^{k} \) . Clearly \( d{f}_{x}\left( h\right) \) is a linear function of \( h \) . (In fact \( d{f}_{x} \) is just that linear mapping which corresponds to the \( l \times  k \) matrix \( {\left( \partial {f}_{i}/\partial {x}_{j}\right) }_{x} \) of first partial derivatives, evaluated at \( x \) .)

Here are two fundamental properties of the derivative operation:

1 (Chain rule). If \( f : U \rightarrow  V \) and \( g : V \rightarrow  W \) are smooth maps, with \( f\left( x\right)  = y \) , then

\[
d{\left( g \circ  f\right) }_{x} = d{g}_{y} \circ  d{f}_{x}.
\]

In other words, to every commutative triangle

![bo_d7du9valb0pc73deirc0_13_574_1341_267_224_0.jpg](images/bo_d7du9valb0pc73deirc0_13_574_1341_267_224_0.jpg)

of smooth maps between open subsets of \( {R}^{k},{R}^{l},{R}^{m} \) there corresponds a commutative triangle of linear maps

![bo_d7du9valb0pc73deirc0_13_558_1700_301_234_0.jpg](images/bo_d7du9valb0pc73deirc0_13_558_1700_301_234_0.jpg)

2. If \( I \) is the identity map of \( U \) , then \( d{I}_{x} \) is the identity map of \( {R}^{k} \) . More generally, if \( U \subset  {U}^{\prime } \) are open sets and

\[
i : U \rightarrow  {U}^{\prime }
\]

is the inclusion map, then again \( d{i}_{x} \) is the identity map of \( {R}^{k} \) .

Note also:

3. If \( L : {R}^{k} \rightarrow  {R}^{l} \) is a linear mapping, then \( d{L}_{x} = L \) .

As a simple application of the two properties one has the following:

Assertion. If \( f \) is a diffeomorphism between open sets \( U \subset  {R}^{k} \) and \( V \subset  {R}^{l} \) , then \( k \) must equal \( l \) , and the linear mapping

\[
d{f}_{x} : {R}^{k} \rightarrow  {R}^{l}
\]

must be nonsingular.

Proof. The composition \( {f}^{-1} \circ  f \) is the identity map of \( U \) ; hence \( d{\left( {f}^{-1}\right) }_{y} \circ  d{f}_{x} \) is the identity map of \( {R}^{k} \) . Similarly \( d{f}_{x} \circ  d{\left( {f}^{-1}\right) }_{y} \) is the identity map of \( {R}^{l} \) . Thus \( d{f}_{x} \) has a two-sided inverse, and it follows that \( k = l \) .

A partial converse to this assertion is valid. Let \( f : U \rightarrow  {R}^{k} \) be a smooth map, with \( U \) open in \( {R}^{k} \) .

Inverse Function Theorem. If the derivative \( d{f}_{x} : {R}^{k} \rightarrow  {R}^{k} \) is nonsingular, then \( f \) maps any sufficiently small open set \( {U}^{\prime } \) about \( x \) diffeomor-phically onto an open set \( f\left( {U}^{\prime }\right) \) .

(See Apostol [2, p. 144] or Dieudonné [7, p. 268].)

Note that \( f \) may not be one-one in the large, even if every \( d{f}_{x} \) is nonsingular. (An instructive example is provided by the exponential mapping of the complex plane into itself.)

Now let us define the tangent space \( T{M}_{x} \) for an arbitrary smooth manifold \( M \subset  {R}^{k} \) . Choose a parametrization

\[
g : U \rightarrow  M \subset  {R}^{k}
\]

of a neighborhood \( g\left( U\right) \) of \( x \) in \( M \) , with \( g\left( u\right)  = x \) . Here \( U \) is an open subset of \( {R}^{m} \) . Think of \( g \) as a mapping from \( U \) to \( {R}^{k} \) , so that the derivative

\[
d{g}_{u} : {R}^{m} \rightarrow  {R}^{k}
\]

is defined. Set \( T{M}_{x} \) equal to the image \( d{g}_{u}\left( {R}^{m}\right) \) of \( d{g}_{u} \) . (Compare Figure 1.)

We must prove that this construction does not depend on the particular choice of parametrization \( g \) . Let \( h : V \rightarrow  M \subset  {R}^{k} \) be another parametrization of a neighborhood \( h\left( V\right) \) of \( x \) in \( M \) , and let \( v = {h}^{-1}\left( x\right) \) . Then \( {h}^{-1} \circ  g \) maps some neighborhood \( {U}_{1} \) of \( u \) diffeomorphically onto a neighborhood \( {V}_{1} \) of \( v \) . The commutative diagram of smooth maps ween open sets

![bo_d7du9valb0pc73deirc0_15_423_362_293_237_0.jpg](images/bo_d7du9valb0pc73deirc0_15_423_362_293_237_0.jpg)

es rise to a commutative diagram of linear maps

![bo_d7du9valb0pc73deirc0_15_420_702_306_246_0.jpg](images/bo_d7du9valb0pc73deirc0_15_420_702_306_246_0.jpg)

1 it follows immediately that

\[
\text{ Image }\left( {d{g}_{u}}\right)  = \text{ Image }\left( {d{h}_{v}}\right) \text{ . }
\]

1s \( T{M}_{x} \) is well defined.

Proof that \( T{M}_{x} \) is AN \( m \) -DIMENSIONAL VECTOR SPACE. Since

\[
{g}^{-1} : g\left( U\right)  \rightarrow  U
\]

smooth mapping, we can choose an open set \( W \) containing \( x \) and mooth map \( F : W \rightarrow  {R}^{m} \) that coincides with \( {g}^{-1} \) on \( W \cap  g\left( U\right) \) . ting \( {U}_{0} = {g}^{-1}\left( {W \cap  g\left( U\right) }\right) \) , we have the commutative diagram

![bo_d7du9valb0pc73deirc0_15_371_1504_397_194_0.jpg](images/bo_d7du9valb0pc73deirc0_15_371_1504_397_194_0.jpg)

therefore

![bo_d7du9valb0pc73deirc0_15_371_1779_397_197_0.jpg](images/bo_d7du9valb0pc73deirc0_15_371_1779_397_197_0.jpg)

s diagram clearly implies that \( d{g}_{u} \) has rank \( m \) , and hence that its ge \( T{M}_{x} \) has dimension \( m \) .

Tow consider two smooth manifolds, \( M \subset  {R}^{k} \) and \( N \subset  {R}^{l} \) , and a smooth map

\[
f : M \rightarrow  N
\]

with \( f\left( x\right)  = y \) . The derivative

\[
d{f}_{x} : T{M}_{x} \rightarrow  T{N}_{y}
\]

is defined as follows. Since \( f \) is smooth there exist an open set \( W \) containing \( x \) and a smooth map

\[
F : W \rightarrow  {R}^{l}
\]

that coincides with \( f \) on \( W \cap  M \) . Define \( d{f}_{x}\left( v\right) \) to be equal to \( d{F}_{x}\left( v\right) \) for all \( {v\varepsilon T}{M}_{x} \) .

To justify this definition we must prove that \( d{F}_{x}\left( v\right) \) belongs to \( T{N}_{y} \) and that it does not depend on the particular choice of \( F \) .

Choose parametrizations

\[
g : U \rightarrow  M \subset  {R}^{k}\text{ and }h : V \rightarrow  N \subset  {R}^{l}
\]

for neighborhoods \( g\left( U\right) \) of \( x \) and \( h\left( V\right) \) of \( y \) . Replacing \( U \) by a smaller set if necessary, we may assume that \( g\left( U\right)  \subset  W \) and that \( f \) maps \( g\left( U\right) \) into \( h\left( V\right) \) . It follows that

\[
{h}^{-1} \circ  f \circ  g : U \rightarrow  V
\]

is a well-defined smooth mapping.

Consider the commutative diagram

![bo_d7du9valb0pc73deirc0_16_502_1346_323_236_0.jpg](images/bo_d7du9valb0pc73deirc0_16_502_1346_323_236_0.jpg)

of smooth mappings between open sets. Taking derivatives, we obtain a commutative diagram of linear mappings

![bo_d7du9valb0pc73deirc0_16_426_1698_471_236_0.jpg](images/bo_d7du9valb0pc73deirc0_16_426_1698_471_236_0.jpg)

where \( u = {g}^{-1}\left( x\right) , v = {h}^{-1}\left( y\right) \) .

It follows immediately that \( d{F}_{x} \) carries \( T{M}_{x} = \) Image \( \left( {d{g}_{u}}\right) \) into \( T{N}_{y} = \) Image \( \left( {d{h}_{v}}\right) \) . Furthermore the resulting map \( d{f}_{x} \) does not depend on the particular choice of \( F \) , for we can obtain the same linear transformation by going around the bottom of the diagram. That is:

\[
d{f}_{x} = d{h}_{v} \circ  d{\left( {h}^{-1} \circ  f \circ  g\right) }_{u} \circ  {\left( d{g}_{u}\right) }^{-1}.
\]

This completes the proof that

\[
d{f}_{x} : T{M}_{x} \rightarrow  T{N}_{y}
\]

is a well-defined linear mapping.

As before, the derivative operation has two fundamental properties:

1. (Chain rule). If \( f : M \rightarrow  N \) and \( g : N \rightarrow  P \) are smooth, with \( f\left( x\right)  = y \) , then

\[
d{\left( g \circ  f\right) }_{x} = d{g}_{y} \circ  d{f}_{x}.
\]

2. If \( I \) is the identity map of \( M \) , then \( d{I}_{x} \) is the identity map of \( T{M}_{x} \) . More generally, if \( M \subset  N \) with inclusion map \( i \) , then \( T{M}_{x} \subset  T{N}_{x} \) with inclusion map \( d{i}_{x} \) . (Compare Figure 2.)

![bo_d7du9valb0pc73deirc0_17_281_1040_882_320_0.jpg](images/bo_d7du9valb0pc73deirc0_17_281_1040_882_320_0.jpg)

Figure 2. The tangent space of a submanifold

The proofs are straightforward.

As before, these two properties lead to the following:

Assertion. If \( f : M \rightarrow  N \) is a diffeomorphism, then \( d{f}_{x} : T{M}_{x} \rightarrow  T{N}_{y} \) is an isomorphism of vector spaces. In particular the dimension of \( M \) must be equal to the dimension of \( N \) .

## REGULAR VALUES

Let \( f : M \rightarrow  N \) be a smooth map between manifolds of the same dimension.* We say that \( {x\varepsilon M} \) is a regular point of \( f \) if the derivative \( d{f}_{x} \) is nonsingular. In this case it follows from the inverse function theorem that \( f \) maps a neighborhood of \( x \) in \( M \) diffeomorphically onto an open set in \( N \) . The point \( {y\varepsilon N} \) is called a regular value if \( {f}^{-1}\left( y\right) \) contains only regular points.

---

* This restriction will be removed in \( \text{ § }2 \) .

---

If \( d{f}_{x} \) is singular, then \( x \) is called a critical point of \( f \) , and the image \( f\left( x\right) \) is called a critical value. Thus each \( {y\varepsilon N} \) is either a critical value or a regular value according as \( {f}^{-1}\left( y\right) \) does or does not contain a critical point.

Observe that if \( M \) is compact and \( {y\varepsilon N} \) is a regular value, then \( {f}^{-1}\left( y\right) \) is a finite set (possibly empty). For \( {f}^{-1}\left( y\right) \) is in any case compact, being a closed subset of the compact space \( M \) ; and \( {f}^{-1}\left( y\right) \) is discrete, since \( f \) is one-one in a neighborhood of each \( {x\varepsilon }{f}^{-1}\left( y\right) \) .

For a smooth \( f : M \rightarrow  N \) , with \( M \) compact, and a regular value \( {y\varepsilon N} \) , we define \( \# {f}^{-1}\left( y\right) \) to be the number of points in \( {f}^{-1}\left( y\right) \) . The first observation to be made about \( \# {f}^{-1}\left( y\right) \) is that it is locally constant as a function of \( y \) (where \( y \) ranges only through regular values!). I.e., there is a neighborhood \( V \subset  N \) of \( y \) such that \( \# {f}^{-1}\left( {y}^{\prime }\right)  = \# {f}^{-1}\left( y\right) \) for any \( {y}^{\prime }{\varepsilon V} \) . [Let \( {x}_{1},\cdots ,{x}_{k} \) be the points of \( {f}^{-1}\left( y\right) \) , and choose pairwise disjoint neighborhoods \( {U}_{1},\cdots ,{U}_{k} \) of these which are mapped diffeomorphically onto neighborhoods \( {V}_{1},\cdots ,{V}_{k} \) in \( N \) . We may then take

\[
V = {V}_{1} \cap  {V}_{2} \cap  \cdots  \cap  {V}_{k} - f\left( {M - {U}_{1} - \cdots  - {U}_{k}}\right) .\rbrack
\]

## THE FUNDAMENTAL THEOREM OF ALGEBRA

As an application of these notions, we prove the fundamental theorem of algebra: every nonconstant complex polynomial \( P\left( z\right) \) must have a zero.

For the proof it is first necessary to pass from the plane of complex numbers to a compact manifold. Consider the unit sphere \( {S}^{2} \subset  {R}^{3} \) and the stereographic projection

\[
{h}_{ + } : {S}^{2} - \{ \left( {0,0,1}\right) \}  \rightarrow  {R}^{2} \times  0 \subset  {R}^{3}
\]

from the "north pole" \( \left( {0,0,1}\right) \) of \( {S}^{2} \) . (See Figure 3.) We will identify \( {R}^{2} \times  0 \) with the plane of complex numbers. The polynomial map \( P \) from \( {R}^{2} \times  0 \) itself corresponds to a map \( f \) from \( {S}^{2} \) to itself; where

\[
f\left( x\right)  = {h}_{ + }^{-1}P{h}_{ + }\left( x\right) \text{ for }x \neq  \left( {0,0,1}\right)
\]

\[
f\left( {0,0,1}\right)  = \left( {0,0,1}\right) .
\]

It is well known that this resulting map \( f \) is smooth, even in a neighborhood of the north pole. To see this we introduce the stereographic projection \( {h}_{ - } \) from the south pole \( \left( {0,0, - 1}\right) \) and set

\[
Q\left( z\right)  = {h}_{ - }f{h}_{ - }^{-1}\left( z\right) .
\]

![bo_d7du9valb0pc73deirc0_19_380_287_667_320_0.jpg](images/bo_d7du9valb0pc73deirc0_19_380_287_667_320_0.jpg)

Figure 3. Stereographic projection

Note, by elementary geometry, that

\[
{h}_{ + }{h}_{ - }^{-1}\left( z\right)  = z/{\left| z\right| }^{2} = 1/\bar{z}.
\]

Now if \( P\left( z\right)  = {a}_{0}{z}^{n} + {a}_{1}{z}^{n - 1} + \cdots  + {a}_{n} \) , with \( {a}_{0} \neq  0 \) , then a short computation shows that

\[
Q\left( z\right)  = {z}^{n}/\left( {{\bar{a}}_{0} + {\bar{a}}_{1}z + \cdots  + {\bar{a}}_{n}{z}^{n}}\right) .
\]

Thus \( Q \) is smooth in a neighborhood of 0, and it follows that \( f = {h}_{ - }^{-1}Q{h}_{ - } \) is smooth in a neighborhood of \( \left( {0,0,1}\right) \) .

Next observe that \( f \) has only a finite number of critical points; for \( P \) fails to be a local diffeomorphism only at the zeros of the derivative polynomial \( {P}^{\prime }\left( z\right)  = \sum {a}_{n - j}j{z}^{i - 1} \) , and there are only finitely many zeros since \( {P}^{\prime } \) is not identically zero. The set of regular values of \( f \) , being a sphere with finitely many points removed, is therefore connected. Hence the locally constant function \( \# {f}^{-1}\left( y\right) \) must actually be constant on this set. Since \( {f}^{-1}\left( y\right) \) can’t be zero everywhere, we conclude that it is zero nowhere. Thus \( f \) is an onto mapping, and the polynomial \( P \) must have a zero.
