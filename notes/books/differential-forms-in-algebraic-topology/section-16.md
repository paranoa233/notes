## §16 The Path Fibration

Recall again that through §18 we work in the category of topological spaces and continuous maps. Unless otherwise noted all cohomology groups will be assumed to have integer coefficients. Let \( \pi  : E \rightarrow  X \) be a fiber bundle with fiber \( F \) over a topological space \( X \) that has a good cover \( \mathfrak{U} \) . We have shown that there is a spectral sequence converging to the cohomology \( {H}^{ * }\left( E\right) \) of the total space, with \( {E}_{2} \) term

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}\left( F\right) }\right) ,
\]

where \( {\mathcal{H}}^{q}\left( F\right) \) is the presheaf that associates to every open set \( U \) in \( \mathfrak{U} \) the group \( {H}^{q}\left( {{\pi }^{-1}U}\right)  \simeq  {H}^{q}\left( F\right) \) . Now suppose \( \pi  : E \rightarrow  X \) is simply a map, not necessarily locally trivial. One can still obtain a spectral sequence by considering the double complex of singular cochains \( K = {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{S}^{ * }}\right) \) on \( E \) . As long as the map \( \pi  : E \rightarrow  X \) has the property that(16.1)\( {H}^{q}\left( {{\pi }^{-1}U}\right)  \simeq  {H}^{q}\left( F\right) \) for some fixed space \( F \) and for any contractible open set \( U \) ,

then \( {E}_{2} = {H}_{\delta }{H}_{d}\left( K\right) \) will be the same as for a fiber bundle. Since the spectral sequence is a purely algebraic way of going from \( {H}_{\delta }{H}_{d} \) to \( {H}_{D} \) , which is isomorphic to \( {H}^{ * }\left( E\right) \) , the spectral sequence of this double complex will again converge to \( {H}^{ * }\left( E\right) \) . An example of such a map is the path fibration. As will be seen in the next few sections, Serre's application of the spectral sequence in this unexpected setting has far-reaching consequences in homotopy theory.

## The Path Fibration

Let \( X \) be a topological space with a base point \( * \) and \( \left\lbrack  {0,1}\right\rbrack \) the unit interval with base point 0 . The path space of \( X \) is defined to be the space \( P\left( X\right) \) consisting of all the paths in \( X \) with initial point \( * \) :

\[
P\left( X\right)  = \{ \text{ maps }\mu  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  X \mid  \mu \left( 0\right)  =  * \} .
\]

We give this space the compact open topology; i.e., a sub-basic open set in \( P\left( X\right) \) consists of all base-point preserving maps \( \mu  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  X \) such that \( \mu \left( K\right)  \subset  U \) for a fixed compact set \( K \) in \( \left\lbrack  {0,1}\right\rbrack \) and a fixed open set \( U \) in \( X \) . There is a natural projection \( \pi  : P\left( X\right)  \rightarrow  X \) given by the endpoint of a path: \( \pi \left( \mu \right)  = \mu \left( 1\right) \) . The fiber at \( p \) of this projection consists of all the paths from * to \( p \) (see Figure 16.1).

![bo_d7b6f8alb0pc73dd9avg_208_603_1543_463_365_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_208_603_1543_463_365_0.jpg)

Figure 16.1

We now show that the map \( \pi  : P\left( X\right)  \rightarrow  X \) has the property (16.1). Let \( U \) be a contractible open set containing \( p \) . There is a natural inclusion

\[
i : {\pi }^{-1}\left( p\right)  \rightarrow  {\pi }^{-1}\left( U\right)
\]

![bo_d7b6f8alb0pc73dd9avg_209_622_303_385_275_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_209_622_303_385_275_0.jpg)

Figure 16.2

(See Figure 16.2.) Using a contraction of \( U \) to \( p \) , we can get a map

\[
\phi  : {\pi }^{-1}\left( U\right)  \rightarrow  {\pi }^{-1}\left( p\right) .
\]

It is readily checked that \( \phi \) and \( i \) are homotopy inverses. Furthermore, if \( p \) and \( q \) are two points in the same path component of \( X \) , then a fixed path from \( p \) to \( q \) induces a homotopy equivalence \( {\pi }^{-1}\left( p\right)  \simeq  {\pi }^{-1}\left( q\right) \) . Thus all fibers have the homotopy type of \( {\pi }^{-1}\left( *\right) \) , which is the loop space \( {\Omega X} \) of \( X \) :

\[
{\Omega X} = \{ \mu  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  X \mid  \mu \left( 0\right)  = \mu \left( 1\right)  =  * \} .
\]

So the map \( \pi  : P\left( X\right)  \rightarrow  X \) has the property \( {H}^{ * }\left( {{\pi }^{-1}U}\right)  \simeq  {H}^{ * }\left( {\Omega X}\right) \) for any contractible \( U \) in \( X \) .

A more general class of maps satisfying (16.1) are the fiberings or fibrations. A map \( \pi  : E \rightarrow  X \) is called a fibering or a fibration if it satisfies the covering homotopy property:

(16.2) given a map \( f : Y \rightarrow  E \) from any topological space \( Y \) into \( E \) and a homotopy \( {\bar{f}}_{t} \) of \( \bar{f} = \pi  \circ  f \) in \( X \) , there is a homotopy \( {f}_{t} \) of \( f \) in \( E \) which covers \( {\bar{f}}_{t} \) ; that is, \( \pi  \circ  {f}_{t} = {\bar{f}}_{t} \) .

The covering homotopy property may be expressed in terms of the diagram

![bo_d7b6f8alb0pc73dd9avg_209_616_1445_429_224_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_209_616_1445_429_224_0.jpg)

Such a fibering is sometimes called a fibering in the sense of Hurewicz, as opposed to a fibering in the sense of Serre which requires only that the covering homotopy property be satisfied for finite polyhedra \( Y \) . If \( X \) is a pointed space with base point \( * \) , we call \( {\pi }^{-1}\left( *\right) \) the fiber of the fibering, and for any \( x \) in \( X \) , we call \( {F}_{x} = {\pi }^{-1}\left( x\right) \) the fiber over \( x \) . As a convention we will assume the base space \( X \) of a fibering to be path-connected. It is clear that the map \( \pi  : {PX} \rightarrow  X \) is a fibering with fiber \( {\Omega X} \) , for a homotopy in \( X \) naturally induces a covering homotopy in \( {PX} \) . This fibering, called the path fibration of \( X \) , is fundamental in the computation of the cohomology of the loop spaces. Its total space \( {PX} \) can be contracted to the constant path: \( \left\lbrack  {0,1}\right\rbrack   \rightarrow   * \) .

We prove below two basic properties of a fibering, from which it will follow that (16.1) holds for a fibering.

Proposition 16.3.(a) Any two fibers of a fibering over an arcwise-connected space have the same homotopy type.

(b) For every contractible open set \( U \) , the inverse image \( {\pi }^{-1}U \) has the homotopy type of the fiber \( {F}_{a} \) , where \( a \) is any point in \( U \) .

Proof. (a) A path \( \gamma \left( t\right) \) from \( a \) to \( b \) in \( X \) may be regarded as a homotopy of the point \( a \) . Let \( \bar{g} : {F}_{a} \times  I \rightarrow  X \) be given by \( \left( {y, t}\right)  \mapsto  \gamma \left( t\right) \) , where \( I \) is the unit interval \( \left\lbrack  {0,1}\right\rbrack \) . So we have the situation depicted in Figure 16.3. By the

![bo_d7b6f8alb0pc73dd9avg_210_273_835_1090_387_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_210_273_835_1090_387_0.jpg)

Figure 16.3

covering homotopy property, there is a map \( g \) which covers \( \bar{g} \) . The restriction \( {g}_{1} = {\left. g\right| }_{{F}_{a}\times \{ 1\} } \) is then a map from \( {F}_{a} \) to \( {F}_{b} \) . Thus a path from a to \( b \) induces a map from the fiber \( {F}_{a} \) to the fiber \( {F}_{b} \) .

We will show that homotopic paths from \( a \) to \( b \) in \( X \) induce homotopic maps from \( {F}_{a} \) to \( {F}_{b} \) . Let \( \mu \) be a path from \( a \) to \( b \) which is homotopic to \( \gamma \) , \( h \) a covering homotopy of \( \mu \) , and \( {h}_{1} \) the induced map from \( {F}_{a} \) to \( {F}_{b} \) . Define \( Z \) by (see Figure 16.4)

\[
Z = {F}_{a} \times  I \times  \{ 0\}  \cup  {F}_{a} \times  \dot{I} \times  I,
\]

where \( i = \{ 0\}  \cup  \{ 1\} \) , and \( f : Z \rightarrow  E \) by

\[
{\left. f\right| }_{{F}_{a} \times  I\times \{ 0\} }\left( {y, s,0}\right)  = y
\]

\[
{\left. f\right| }_{{F}_{a}\times \{ 0\}  \times  I}\left( {y,0, t}\right)  = g\left( {y, t}\right)
\]

\[
{\left. f\right| }_{{F}_{a}\times \{ 1\}  \times  I}\left( {y,1, t}\right)  = h\left( {y, t}\right) .
\]

We regard the homotopy between \( \gamma \) and \( \mu \) in \( X \) as a homotopy \( \bar{G} \) of \( \pi  \circ  f \) . By the covering homotopy property there is a covering map \( G \) from \( {F}_{a} \times  I \times  I \) , which is homotopic to \( Z \times  I \) , into \( E \) . The restriction of \( G \) to \( {F}_{a} \times  I \times  \{ 1\} \) has image in \( {F}_{b} \) . Since \( {\left. G\right| }_{{F}_{a}\times \{ 0\} \times \{ 1\} } = {g}_{1} \) and \( {\left. G\right| }_{{F}_{a}\times \{ 1\} \times \{ 1\} } = \; {h}_{1},{\left. G\right| }_{{F}_{a} \times  I\times \{ 1\} } \) is a homotopy in \( {F}_{b} \) between \( {g}_{1} \) and \( {h}_{1} \) .

![bo_d7b6f8alb0pc73dd9avg_211_256_290_1098_699_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_211_256_290_1098_699_0.jpg)

Figure 16.4

Given two points \( a \) and \( b \) in \( X \) and a path \( \gamma \) from \( a \) to \( b \) , let \( u : {F}_{a} \rightarrow  {F}_{b} \) be a map induced by \( \gamma \) and \( v : {F}_{b} \rightarrow  {F}_{a} \) a map induced by \( {\gamma }^{-1} \) . Then \( v \circ  u \) : \( {F}_{a} \rightarrow  {F}_{a} \) is a map induced by \( {\gamma }^{-1}\gamma \) . Since \( {\gamma }^{-1}\gamma \) is homotopic to the constant map to \( a \) , the composition \( v \circ  u \) is homotopic to the identity on \( {F}_{a} \) . Therefore, \( {F}_{a} \) and \( {F}_{b} \) have the same homotopy type.

(b) Let \( \gamma  : U \times  I \rightarrow  U \) be a deformation retraction of \( U \) to the point \( a \) . By the covering homotopy property, there is a map \( g : {\pi }^{-1}U \times  I \rightarrow  {\pi }^{-1}U \) such that the following diagram is commutative. ing with \( t \) in the unit interval \( I \) . At \( t = 0 \) ,

\[
{g}_{0} : {\pi }^{-1}U \times  \{ 0\}  \rightarrow  {\pi }^{-1}U
\]

![bo_d7b6f8alb0pc73dd9avg_211_433_1650_733_252_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_211_433_1650_733_252_0.jpg)

We will show that \( g \) gives a deformation retraction of \( {\pi }^{-1}U \) onto the fiber \( {F}_{a} \) . Let \( {g}_{t} \) be the restriction of \( g \) to \( {\pi }^{-1}U \times  \{ t\} \) . By identifying \( {\pi }^{-1}U \) with \( {\pi }^{-1}U \times  \{ t\} \) , we may regard \( g \) as a family of maps \( {g}_{t} : {\pi }^{-1}U \rightarrow  {\pi }^{-1}U \) vary-

is the identity and at \( t = 1 \) ,

\[
{g}_{1} : {\pi }^{-1}U \times  \{ 1\}  \rightarrow  {\pi }^{-1}U
\]

has image in the fiber \( {F}_{a} \) . Hence, \( {g}_{1} \) may be factored as \( {g}_{1} = i \circ  \phi \) :

\[
{\pi }^{-1}U \times  \{ 1\} \overset{\phi }{ \rightarrow  }{F}_{a}\overset{i}{ \hookrightarrow  }{\pi }^{-1}U
\]

So via \( g \) the composition \( i \circ  \phi \) is homotopic to the identity. To show that \( \phi  \circ  i : {F}_{a} \rightarrow  {F}_{a} \) is homotopic to the identity, consider the following diagram

![bo_d7b6f8alb0pc73dd9avg_212_471_926_717_263_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_212_471_926_717_263_0.jpg)

Note that \( \phi  \circ  i = {\left. g \circ  j\right| }_{{F}_{a}\times \{ 1\} } \) is induced from the constant path \( I \rightarrow  \{ a\}  \in  X \) , since \( \gamma  \circ  \pi  \circ  j\left( {y, t}\right)  = a \) for all \( t \) . (The deformation retraction \( \gamma \) fixes \( a \) at all times.) By the proof of (a), \( \phi  \circ  i \) is homotopic to the identity.

REMARK 16.4. If we replace \( {F}_{a} \) with any space \( Y \) , the argument in (a) proves that in the covering homotopy property (16.2), homotopic maps in \( X \) induce homotopic covering maps in \( E \) .

Generalizing the fact that a simply connected space cannot have a connected covering space of more than one sheet, we have the following.

Proposition 16.5. Let \( \pi  : E \rightarrow  X \) be a fibering. If \( X \) is simply connected and \( E \) is path connected, then the fibers are path connected.

Proof. Trivially the \( {E}_{2}^{0,0} \) term of the fibering survives to \( {E}_{\infty } \) . Hence

\[
{E}_{2}^{0,0} = {E}_{\infty }^{0,0} = {H}^{0}\left( E\right)  = \mathbb{Z},
\]

since \( E \) is path connected. On the other hand,

\[
{E}_{2}^{0,0} = {H}^{0}\left( {X,{H}^{0}\left( F\right) }\right)  = {H}^{0}\left( F\right) .
\]

Therefore \( {H}^{0}\left( F\right)  = \mathbb{Z} \) .

The Cohomology of the Loop Space of a Sphere

As an application of the spectral sequence of the path fibration, we compute here the integer cohomology groups of the loop space \( \Omega {S}^{n}, n \geq  2 \) .

EXAMPLE 16.6 (The 2-sphere). Since \( {S}^{2} \) is simply connected, the spectral sequence of the path fibration

\[
\Omega {S}^{2} \rightarrow  P{S}^{2}
\]

\[
{S}^{2}
\]

↓

has \( {E}_{2} \) term

\[
{E}_{2}^{p, q} = {H}^{p}\left( {{S}^{2},{H}^{q}\left( {\Omega {S}^{2}}\right) }\right) .
\]

So the zeroth column \( {E}_{2}^{0, q} = {H}^{0}\left( {{S}^{2},{H}^{q}\left( {\Omega {S}^{2}}\right) }\right)  = {H}^{q}\left( {\Omega {S}^{2}}\right) \) is the cohomology of the fiber. By Proposition 16.5, \( {H}^{0}\left( {\Omega {S}^{2}}\right)  = \mathbb{Z} \) , so the bottom row \( {H}_{2}^{p,0} = \; {H}^{p}\left( {{S}^{2},{H}^{0}\left( {\Omega {S}^{2}}\right) }\right)  = {H}^{p}\left( {{S}^{2},\mathbb{Z}}\right) \) is the cohomology of the base.

![bo_d7b6f8alb0pc73dd9avg_213_569_1145_459_331_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_213_569_1145_459_331_0.jpg)

By the universal coefficient theorem (15.14), all columns in \( {E}_{2} \) except \( p = 0 \) and \( p = 2 \) are zero. Hence all the differentials \( {d}_{3},{d}_{4},\ldots \) are zero and \( {E}_{3}^{p, q} = {E}_{\infty }^{p, q} \) . Because the path space \( P{S}^{2} \) is contractible,

\[
{E}_{\infty }^{p, q} = \left\{  \begin{array}{ll} \mathbb{Z} & \left( {p, q}\right)  = \left( {0,0}\right) \\  0 & \text{ otherwise. } \end{array}\right.
\]

Thus \( {d}_{2} : {E}_{2}^{0,1} \rightarrow  {E}_{2}^{2,0} \) must be an isomorphism. It follows that \( {H}^{1}\left( {\Omega {S}^{2}}\right)  = \mathbb{Z} \) . But then

\[
{E}_{2}^{2,1} = {H}^{2}\left( {{S}^{2},{H}^{1}\left( {\Omega {S}^{2}}\right) }\right)  = {H}^{2}\left( {{S}^{2},\mathbb{Z}}\right)  = \mathbb{Z}.
\]

Since \( {d}_{2} : {E}_{2}^{0,2} \rightarrow  {E}_{2}^{2,1} \) is an isomorphism, \( {H}^{2}\left( {\Omega {S}^{2}}\right)  = \mathbb{Z} \) . Working our way up, we find \( {H}^{q}\left( {\Omega {S}^{2}}\right)  = \mathbb{Z} \) in every dimension \( q \) .

EXAMPLE 16.7 (The 3-sphere). In the \( {E}_{2} \) term of the fibering

![bo_d7b6f8alb0pc73dd9avg_214_368_376_870_511_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_214_368_376_870_511_0.jpg)

the nonzero columns are \( p = 0 \) and \( p = 3 \) . For dimension reasons \( {d}_{2} = 0 \) and \( {d}_{4} = {d}_{5} = \cdots  = 0 \) . Because the total space is contractible, \( {d}_{3} \) is an isomorphism except at \( {E}_{3}^{0,0} \) . Therefore,

\[
{H}^{ * }\left( {\Omega {S}^{3}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ in even dimensions } \\  0 & \text{ otherwise. } \end{array}\right.
\]

Similarly we find that in general

\[
{H}^{ * }\left( {\Omega {S}^{n}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ in dimensions }0, n - 1,2\left( {n - 1}\right) ,\ldots \\  0 & \text{ otherwise. } \end{array}\right.
\]

Next we examine the ring structure of \( {H}^{ * }\left( {\Omega {S}^{n}}\right) \) . We start with \( \Omega {S}^{2} \) . Let \( u \) be a generator of \( {E}_{2}^{2,0} = {H}^{2}\left( {S}^{2}\right) \) and let \( x \) be the generator of \( {H}^{1}\left( {\Omega {S}^{1}}\right) \) which is mapped to \( u \) by \( {d}_{2} \) . For simplicity we occasionally write \( d \) for \( {d}_{2} \) . By Example 16.6, the differential \( {d}_{2} \) is an isomorphism. Note that \( x \) commutes with \( u \) because \( {E}_{2} \) is the tensor product \( {H}^{ * }\left( {\Omega {S}^{2}}\right)  \otimes  {H}^{ * }\left( {S}^{2}\right) \) . ( \( x \) is actually \( x \otimes  1 \) and \( u \) is \( 1 \otimes  u \) .)

![bo_d7b6f8alb0pc73dd9avg_214_607_1718_449_455_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_214_607_1718_449_455_0.jpg)

Since \( {d}_{2}\left( {x}^{2}\right)  = \left( {{d}_{2}x}\right)  \cdot  x - x \cdot  {d}_{2}x = {ux} - {xu} = 0 \) , we have \( {x}^{2} = 0 \) . Thus the generator \( e \) in \( {H}^{2}\left( {\Omega {S}^{2}}\right) \) which maps to \( {xu} \) is algebraically independent of \( x \) . Since \( d\left( {ex}\right)  = {eu} \) , the product \( {ex} \) is a generator in dimension 3 . Similarly, \( d\left( {e}^{2}\right)  = {2exu} \) so that \( {e}^{2}/2 \) is a generator in dimension \( 4;d\left( {\left( {{e}^{2}/2}\right) x}\right)  = \left( {{e}^{2}/2}\right) u \) so that \( \left( {{e}^{2}/2}\right)  \cdot  x \) is a generator in dimension 5 . By induction we shall prove

\[
\frac{{e}^{k}}{k!}\text{ is a generator in dimension }{2k}
\]

and

\[
\frac{{e}^{k}}{k!}x\text{ is a generator in dimension }{2k} + 1\text{ . }
\]

Proof. Suppose the claim is true for \( k - 1 \) . Since

\[
d\frac{{e}^{k}}{k!} = \frac{{e}^{k - 1}}{\left( {k - 1}\right) !}{de} = \frac{{e}^{k - 1}}{\left( {k - 1}\right) !}{xu},
\]

which is a generator of \( {E}_{2}^{2,{2k} - 1} \) , the element \( {e}^{k}/k \) ! is a generator of \( {H}^{2k}\left( {\Omega {S}^{2}}\right) \) . Similarly, since

\[
d\left( {\frac{{e}^{k}}{k!}x}\right)  = \frac{{e}^{k - 1}}{\left( {k - 1}\right) !}{xu} \cdot  x + \frac{{e}^{k}}{k!}u = \frac{{e}^{k}}{k!}u,
\]

which is a generator of \( {E}_{2}^{2,{2k}} \) , the element \( \left( {{e}^{k}/k!}\right) x \) is a generator of \( {H}^{{2k} + 1}\left( {\Omega {S}^{2}}\right) \) .

By definition the exterior algebra \( E\left( x\right) \) is the ring \( \mathbb{Z}\left\lbrack  x\right\rbrack  /\left( {x}^{2}\right) \) and the divided polynomial algebra \( {Z}_{v}\left( e\right) \) with generator \( e \) is the \( \mathbb{Z} \) -algebra with additive basis \( \left\{  {1, e,{e}^{2}/2!,{e}^{3}/3!,\ldots }\right\} \) . Hence

\[
{H}^{ * }\left( {\Omega {S}^{2}}\right)  = E\left( x\right)  \otimes  {Z}_{\gamma }\left( e\right)
\]

where \( \dim x = 1 \) and \( \dim e = 2 \) .

Now consider \( {H}^{ * }\left( {\Omega {S}^{n}}\right) \) for \( n \) odd. Let \( u \) be a generator of \( {H}^{n}\left( {S}^{n}\right) \) and \( e \) the generator of \( {H}^{n - 1}\left( {\Omega {S}^{n}}\right) \) which maps to \( u \) under the isomorphism \( {d}_{n} \) . Since \( {d}_{n}\left( {e}^{2}\right)  = {2eu},{e}^{2}/2 \) is a generator in dimension \( 2\left( {n - 1}\right) \) . In general if \( {e}^{k}/k! \) is a generator in dimension \( k\left( {n - 1}\right) \) , then \( {d}_{n}\left( {{e}^{k + 1}/\left( {k + 1}\right) !}\right)  = \left( {{e}^{k}/k!}\right) u \) so that \( {e}^{k + 1}/\left( {k + 1}\right) \) ! is a generator in dimension \( \left( {k + 1}\right) \left( {n - 1}\right) \) .

![bo_d7b6f8alb0pc73dd9avg_215_617_1748_424_432_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_215_617_1748_424_432_0.jpg)

This shows that for \( n \) odd,

\[
{H}^{ * }\left( {\Omega {S}^{n}}\right)  = {Z}_{\gamma }\left( e\right) ,\;\dim e = n - 1.
\]

By a computation similar to that of \( {H}^{ * }\left( {\Omega {S}^{2}}\right) \) , we see that for \( n \) even,

\[
{H}^{ * }\left( {\Omega {S}^{n}}\right)  = E\left( x\right)  \otimes  {Z}_{\gamma }\left( e\right) ,\;\dim x = n - 1,\;\dim e = 2\left( {n - 1}\right) .
\]
