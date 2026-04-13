# §7 Framed Cobordism; the Pontryagin Construction

THE degree of a mapping \( M \rightarrow  {M}^{\prime } \) is defined only when the manifolds \( M \) and \( {M}^{\prime } \) are oriented and have the same dimension. We will study a generalization, due to Pontryagin, which is defined for a smooth map

\[
f : M \rightarrow  {S}^{p}
\]

from an arbitrary compact, boundaryless manifold to a sphere. First some definitions.

Let \( N \) and \( {N}^{\prime } \) be compact \( n \) -dimensional submanifolds of \( M \) with \( \partial N = \partial {N}^{\prime } = \partial M = \varnothing \) . The difference of dimensions \( m - n \) is called the codimension of the submanifolds.

Definition. \( N \) is cobordant to \( {N}^{\prime } \) within \( M \) if the subset

\[
N \times  \left\lbrack  {0,\epsilon ) \cup  {N}^{\prime } \times  (1 - \epsilon ,1}\right\rbrack
\]

of \( M \times  \left\lbrack  {0,1}\right\rbrack \) can be extended to a compact manifold

\[
X \subset  M \times  \left\lbrack  {0,1}\right\rbrack
\]

so that

\[
\partial X = N \times  0 \cup  {N}^{\prime } \times  1
\]

and so that \( X \) does not intersect \( M \times  0 \cup  M \times  1 \) except at the points of \( \partial X \) .

Clearly cobordism is an equivalence relation. (See Figure 15.)

Definition. A framing of the submanifold \( N \subset  M \) is a smooth function \( \mathfrak{v} \) which assigns to each \( x \) ε \( N \) a basis

\[
\mathfrak{v}\left( x\right)  = \left( {{v}^{1}\left( x\right) ,\cdots ,{v}^{m - n}\left( x\right) }\right)
\]

for the space \( T{N}_{x}^{ \bot  } \subset  T{M}_{x} \) of normal vectors to \( N \) in \( M \) at \( x \) . (See

![bo_d7du9valb0pc73deirc0_53_354_281_789_219_0.jpg](images/bo_d7du9valb0pc73deirc0_53_354_281_789_219_0.jpg)

Figure 15. Pasting together two cobordisms within \( M \)

Figure 16.) The pair \( \left( {N,\mathfrak{v}}\right) \) is called a framed submanifold of \( M \) . Two framed submanifolds \( \left( {N,\mathfrak{v}}\right) \) and \( \left( {{N}^{\prime },\mathfrak{w}}\right) \) are framed cobordant if there exists a cobordism \( X \subset  M \times  \left\lbrack  {0,1}\right\rbrack \) between \( N \) and \( {N}^{\prime } \) and a framing \( u \) of \( X \) , so that

\[
{u}^{i}\left( {x, t}\right)  = \left( {{v}^{i}\left( x\right) ,0}\right) \;\text{ for }\;\left( {x, t}\right) \;{\varepsilon N} \times  \lbrack 0,\epsilon )
\]

\[
{u}^{i}\left( {x, t}\right)  = \left( {{w}^{i}\left( x\right) ,0}\right) \;\text{ for }\;\left( {x, t}\right) \varepsilon {N}^{\prime } \times  (1 - \epsilon ,1\rbrack .
\]

Again this is an equivalence relation.

Now consider a smooth map \( f : M \rightarrow  {S}^{p} \) and a regular value \( {y\varepsilon }{S}^{p} \) . The map \( f \) induces a framing of the manifold \( {f}^{-1}\left( y\right) \) as follows: Choose a positively oriented basis \( \mathfrak{v} = \left( {{v}^{1},\cdots ,{v}^{p}}\right) \) for the tangent space \( T{\left( {S}^{p}\right) }_{y} \) . For each \( {x\varepsilon }{f}^{-1}\left( y\right) \) recall from page 12 that

\[
d{f}_{x} : T{M}_{x} \rightarrow  T{\left( {S}^{p}\right) }_{y}
\]

maps the subspace \( T{f}^{-1}{\left( y\right) }_{x} \) to zero and maps its orthogonal complement \( T{f}^{-1}{\left( y\right) }_{x}^{ \bot  } \) isomorphically onto \( T{\left( {S}^{p}\right) }_{y} \) . Hence there is a unique vector

\[
{w}^{i}\left( x\right) {\varepsilon T}{f}^{-1}{\left( y\right) }_{x}^{ \bot  } \subset  T{M}_{x}
\]

that maps into \( {v}^{i} \) under \( d{f}_{x} \) . It will be convenient to use the notation \( \mathfrak{w} = {f}^{ * }\mathfrak{v} \) for the resulting framing \( {w}^{1}\left( x\right) ,\cdots ,{w}^{p}\left( x\right) \) of \( {f}^{-1}\left( y\right) \) .

Definition. This framed manifold \( \left( {{f}^{-1}\left( y\right) ,{f}^{ * }\mathfrak{v}}\right) \) will be called the Pontryagin manifold associated with \( f \) .

Of course \( f \) has many Pontryagin manifolds, corresponding to different choices of \( y \) and \( \mathfrak{v} \) , but they all belong to a single framed cobordism class:

Theorem A. If \( {y}^{\prime } \) is another regular value of \( f \) and \( {\mathfrak{v}}^{\prime } \) is a positively oriented basis for \( T{\left( {S}^{p}\right) }_{{y}^{\prime }} \) , then the framed manifold \( \left( {{f}^{-1}\left( {y}^{\prime }\right) ,{f}^{ * }{\mathfrak{v}}^{\prime }}\right) \) is framed cobordant to \( \left( {{f}^{-1}\left( y\right) ,{f}^{ * }\mathfrak{v}}\right) \) .

Theorem B. Two mappings from \( M \) to \( {S}^{p} \) are smoothly homotopic if and only if the associated Pontryagin manifolds are framed cobordant.

![bo_d7du9valb0pc73deirc0_54_183_279_956_1161_0.jpg](images/bo_d7du9valb0pc73deirc0_54_183_279_956_1161_0.jpg)

Figure 16. Framed submanifolds and a framed cobordism

Theorem C. Any compact framed submanifold \( \left( {N,\mathfrak{w}}\right) \) of codimension \( p \) in \( M \) occurs as Pontryagin manifold for some smooth mapping \( f : M \rightarrow  {S}^{p} \) .

Thus the homotopy classes of maps are in one-one correspondence with the framed cobordism classes of submanifolds.

The proof of Theorem A will be very similar to the arguments in §§4 and 5. It will be based on three lemmas.

Lemma 1. If \( \mathfrak{v} \) and \( {\mathfrak{v}}^{\prime } \) are two different positively oriented bases at \( y \) , then the Pontryagin manifold \( \left( {{f}^{-1}\left( y\right) ,{f}^{ * }\mathfrak{v}}\right) \) is framed cobordant to \( \left( {{f}^{-1}\left( y\right) }\right. \) , \( \left. {{f}^{ * }{\mathfrak{v}}^{\prime }}\right) \) .

Proof. Choose a smooth path from \( \mathfrak{v} \) to \( {\mathfrak{v}}^{\prime } \) in the space of all positively oriented bases for \( T{\left( {S}^{p}\right) }_{y} \) . This is possible since this space of bases can be identified with the space \( G{L}^{ + }\left( {p, R}\right) \) of matrices with positive determinant, and hence is connected. Such a path gives rise to the required framing of the cobordism \( {f}^{-1}\left( y\right)  \times  \left\lbrack  {0,1}\right\rbrack \) .

By abuse of notation we will often delete reference to \( {f}^{ * }\mathfrak{v} \) and speak simply of "the framed manifold \( {f}^{-1}\left( y\right) \) ."

Lemma 2. If \( y \) is a regular value of \( f \) , and \( z \) is sufficiently close to \( y \) , then \( {f}^{-1}\left( z\right) \) is framed cobordant to \( {f}^{-1}\left( y\right) \) .

Proof. Since the set \( f\left( C\right) \) of critical values is compact, we can choose \( \epsilon  > 0 \) so that the \( \epsilon \) -neighborhood of \( y \) contains only regular values. Given \( z \) with \( \parallel z - y\parallel  < \epsilon \) , choose a smooth one-parameter family of rotations (i.e. an isotopy) \( {r}_{t} : {S}^{p} \rightarrow  {S}^{p} \) so that \( {r}_{1}\left( y\right)  = z \) , and so that

1) \( {r}_{t} \) is the identity for \( 0 \leq  t < {\epsilon }^{\prime } \) ,

2) \( {r}_{t} \) equals \( {r}_{1} \) for \( 1 - {\epsilon }^{\prime } < t \leq  1 \) , and

3) each \( {r}_{t}^{-1}\left( z\right) \) lies on the great circle from \( y \) to \( z \) , and hence is a regular value of \( f \) .

Define the homotopy

\[
F : M \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  {S}^{p}
\]

by \( F\left( {x, t}\right)  = {r}_{t}f\left( x\right) \) . For each \( t \) note that \( z \) is a regular value of the composition

\[
{r}_{\iota } \circ  f : M \rightarrow  {S}^{p}.
\]

It follows a fortiori that \( z \) is a regular value for the mapping \( F \) . Hence

\[
{F}^{-1}\left( z\right)  \subset  M \times  \left\lbrack  {0,1}\right\rbrack
\]

is a framed manifold and provides a framed cobordism between the framed manifolds \( {f}^{-1}\left( z\right) \) and \( {\left( {r}_{1} \circ  f\right) }^{-1}\left( z\right)  = {f}^{-1}{r}_{1}^{-1}\left( z\right)  = {f}^{-1}\left( y\right) \) . This proves Lemma 2.

Lemma 3. If \( f \) and \( g \) are smoothly homotopic and \( y \) is a regular value for both, then \( {f}^{-1}\left( y\right) \) is framed cobordant to \( {g}^{-1}\left( y\right) \) .

Proof. Choose a homotopy \( F \) with

\[
F\left( {x, t}\right)  = f\left( x\right) \;0 \leq  t < \epsilon ,
\]

\[
F\left( {x, t}\right)  = g\left( x\right) \;1 - \epsilon  < t \leq  1.
\]

Choose a regular value \( z \) for \( F \) which is close enough to \( y \) so that \( {f}^{-1}\left( z\right) \) is framed cobordant to \( {f}^{-1}\left( y\right) \) and so that \( {g}^{-1}\left( z\right) \) is framed cobordant to \( {g}^{-1}\left( y\right) \) . Then \( {F}^{-1}\left( z\right) \) is a framed manifold and provides a framed cobordism between \( {f}^{-1}\left( z\right) \) and \( {g}^{-1}\left( z\right) \) . This proves Lemma 3.

Proof of Theorem A. Given any two regular values \( y \) and \( z \) for \( f \) , we can choose rotations

\[
{r}_{t} : {S}^{p} \rightarrow  {S}^{p}
\]

so that \( {r}_{0} \) is the identity and \( {r}_{1}\left( y\right)  = z \) . Thus \( f \) is homotopic to \( {r}_{1} \circ  f \) ; hence \( {f}^{-1}\left( z\right) \) is framed cobordant to

\[
{\left( {r}_{1} \circ  f\right) }^{-1}\left( z\right)  = {f}^{-1}{r}_{1}^{-1}\left( z\right)  = {f}^{-1}\left( y\right) .
\]

This completes the proof of Theorem A.

The proof of Theorem C will be based on the following: Let \( N \subset  M \) be a framed submanifold of codimension \( p \) with framing \( \mathfrak{v} \) . Assume that \( N \) is compact and that \( \partial N = \partial M = \varnothing \) .

Product Neighborhood Theorem. Some neighborhood of \( N \) in \( M \) is diffeomorphic to the product \( N \times  {R}^{p} \) . Furthermore the diffeomorphism can be chosen so that each \( {x\varepsilon N} \) corresponds to \( \left( {x,0}\right) {\varepsilon N} \times  {R}^{p} \) and so that each normal frame \( \mathfrak{v}\left( x\right) \) corresponds to the standard basis for \( {R}^{p} \) .

REMARK. Product neighborhoods do not exist for arbitrary submani-folds. (Compare Figure 17.)

![bo_d7du9valb0pc73deirc0_56_356_1221_623_261_0.jpg](images/bo_d7du9valb0pc73deirc0_56_356_1221_623_261_0.jpg)

Figure 17. An unframable submanifold

Proof. First suppose that \( M \) is the euclidean space \( {R}^{n + p} \) . Consider the mapping \( g : N \times  {R}^{p} \rightarrow  M \) , defined by

\[
g\left( {x;{t}_{1},\cdots ,{t}_{p}}\right)  = x + {t}_{1}{v}^{1}\left( x\right)  + \cdots  + {t}_{p}{v}^{p}\left( x\right) .
\]

Clearly \( d{g}_{\left( x;0,\cdots ,0\right) } \) is nonsingular; hence \( g \) maps some neighborhood of \( \left( {x,0}\right) \) ε \( N \times  {R}^{p} \) diffeomorphically onto an open set.

We will prove that \( g \) is one-one on the entire neighborhood \( N \times  {U}_{\epsilon } \) of \( N \times  0 \) , providing that \( \epsilon  > 0 \) is sufficiently small; where \( {U}_{\epsilon } \) denotes the \( \epsilon \) -neighborhood of 0 in \( {R}^{p} \) . For otherwise there would exist pairs \( \left( {x, u}\right)  \neq  \left( {{x}^{\prime },{u}^{\prime }}\right) \) in \( N \times  {R}^{p} \) with \( \parallel u\parallel \) and \( \begin{Vmatrix}{u}^{\prime }\end{Vmatrix} \) arbitrarily small and with

\[
g\left( {x, u}\right)  = g\left( {{x}^{\prime },{u}^{\prime }}\right) .
\]

Since \( N \) is compact, we could choose a sequence of such pairs with \( x \) converging, say to \( {x}_{0} \) , with \( {x}^{\prime } \) converging to \( {x}_{0}^{\prime } \) , and with \( u \rightarrow  0 \) and \( {u}^{\prime } \rightarrow  0 \) . Then clearly \( {x}_{0} = {x}_{0}^{\prime } \) , and we have contradicted the statement that \( g \) is one-one in a neighborhood of \( \left( {{x}_{0},0}\right) \) .

Thus \( g \) maps \( N \times  {U}_{\epsilon } \) diffeomorphically onto an open set. But \( {U}_{\epsilon } \) is diffeomorphic to the full euclidean space \( {R}^{p} \) under the correspondence

\[
u \rightarrow  u/\left( {1 - \parallel u{\parallel }^{2}/{\epsilon }^{2}}\right) .
\]

Since \( g\left( {x,0}\right)  = x \) , and since \( d{g}_{\left( x,0\right) } \) does what is expected of it, this proves the Product Neighborhood Theorem for the special case \( M = {R}^{n + p} \) .

For the general case it is necessary to replace straight lines in \( {R}^{n + p} \) by geodesics in \( M \) . More precisely let \( g\left( {x;{t}_{1},\cdots ,{t}_{p}}\right) \) be the endpoint of the geodesic segment of length \( \begin{Vmatrix}{{t}_{1}{v}^{1}\left( x\right)  + \cdots  + {t}_{p}{v}^{p}\left( x\right) }\end{Vmatrix} \) in \( M \) which starts at \( x \) with the initial velocity vector

\[
{t}_{1}{v}^{1}\left( x\right)  + \cdots  + {t}_{p}{v}^{p}\left( x\right) /\left| \right| {t}_{1}{v}^{1}\left( x\right)  + \cdots  + {t}_{p}{v}^{p}\left( x\right) \left| \right| .
\]

The reader who is familiar with geodesics will have no difficulty in checking that

\[
g : N \times  {U}_{\epsilon } \rightarrow  M
\]

is well defined and smooth, for \( \epsilon \) sufficiently small. The remainder of the proof proceeds exactly as before.

Proof of Theorem C. Let \( N \subset  M \) be a compact, boundaryless, framed submanifold. Choose a product representation

\[
g : N \times  {R}^{p} \rightarrow  V \subset  M
\]

for a neighborhood \( V \) of \( N \) , as above, and define the projection

\[
\pi  : V \rightarrow  {R}^{p}
\]

by \( \pi \left( {g\left( {x, y}\right) }\right)  = y \) . (See Figure 18.) Clearly 0 is a regular value, and \( {\pi }^{-1}\left( 0\right) \) is precisely \( N \) with its given framing.

![bo_d7du9valb0pc73deirc0_57_378_1743_697_334_0.jpg](images/bo_d7du9valb0pc73deirc0_57_378_1743_697_334_0.jpg)

Figure 18. Constructing a map with given Pontryagin manifold

Now choose a smooth map \( \varphi  : {R}^{p} \rightarrow  {S}^{p} \) which maps every \( x \) with \( \parallel x\parallel  \geq  1 \) into a base point \( {s}_{0} \) , and maps the open unit ball in \( {R}^{p} \) diffeomor-phically* onto \( {S}^{p} - {s}_{0} \) . Define

\[
f : M \rightarrow  {S}^{p}
\]

by

\[
f\left( x\right)  = \varphi \left( {\pi \left( x\right) }\right) \text{ for }{x\varepsilon V}
\]

\[
f\left( x\right)  = {s}_{0}\;\text{ for }\;x \notin  V.
\]

Clearly \( f \) is smooth, and the point \( \varphi \left( 0\right) \) is a regular value of \( f \) . Since the corresponding Pontryagin manifold

\[
{f}^{-1}\left( {\varphi \left( 0\right) }\right)  = {\pi }^{-1}\left( 0\right)
\]

is precisely equal to the framed manifold \( N \) , this completes the proof of Theorem C.

In order to prove Theorem B we must first show that the Pontryagin manifold of a map determines its homotopy class. Let \( f, g : M \rightarrow  {S}^{p} \) be smooth maps with a common regular value \( y \) .

Lemma 4. If the framed manifold \( \left( {{f}^{-1}\left( y\right) ,{f}^{ * }\mathfrak{v}}\right) \) is equal to \( \left( {{g}^{-1}\left( y\right) ,{g}^{ * }\mathfrak{v}}\right) \) , then \( f \) is smoothly homotopic to \( g \) .

Proof. It will be convenient to set \( N = {f}^{-1}\left( y\right) \) . The hypothesis that \( {f}^{ * }\mathfrak{v} = {g}^{ * }\mathfrak{v} \) means that \( d{f}_{x} = d{g}_{x} \) for all \( {x\varepsilon N} \) .

First suppose that \( f \) actually coincides with \( g \) throughout an entire neighborhood \( V \) of \( N \) . Let \( h : {S}^{p} - y \rightarrow  {R}^{p} \) be stereographic projection. Then the homotopy

\[
F\left( {x, t}\right)  = f\left( x\right) \;\text{ for }x \in  V
\]

\[
F\left( {x, t}\right)  = {h}^{-1}\left\lbrack  {t \cdot  h\left( {f\left( x\right) }\right)  + \left( {1 - t}\right)  \cdot  h\left( {g\left( x\right) }\right) }\right\rbrack  \;\text{ for }\;{x\varepsilon M} - N
\]

proves that \( f \) is smoothly homotopic to \( g \) .

Thus is suffices to deform \( f \) so that it coincides with \( g \) in some small neighborhood of \( N \) , being careful not to map any new points into \( y \) during the deformation. Choose a product representation

\[
N \times  {R}^{p} \rightarrow  V \subset  M
\]

for a neighborhood \( V \) of \( N \) , where \( V \) is small enough so that \( f\left( V\right) \) and \( g\left( V\right) \) do not contain the antipode \( \bar{y} \) of \( y \) . Identifying \( V \) with \( N \times  {R}^{p} \) and identifying \( {S}^{p} - \bar{y} \) with \( {R}^{p} \) , we obtain corresponding mappings

\[
F, G : N \times  {R}^{p} \rightarrow  {R}^{p},
\]

---

* For example, \( \varphi \left( x\right)  = {h}^{-1}\left( {x/\lambda \left( {\parallel x{\parallel }^{2}}\right) }\right) \) , where \( h \) is the stereographic projection from \( {s}_{0} \) and where \( \lambda \) is a smooth monotone decreasing function with \( \lambda \left( t\right)  > 0 \) for \( t < 1 \) and \( \lambda \left( t\right)  = 0 \) for \( t \geq  1 \) .

---

with

\[
{F}^{-1}\left( 0\right)  = {G}^{-1}\left( 0\right)  = N \times  0,
\]

and with

\[
d{F}_{\left( x,0\right) } = d{G}_{\left( x,0\right) } = \left( {\text{ projection to }{R}^{p}}\right)
\]

for all \( x \) : \( N \) .

We will first find a constant \( c \) so that

\[
F\left( {x, u}\right)  \cdot  u > 0,\;G\left( {x, u}\right)  \cdot  u > 0
\]

for \( {x\varepsilon N} \) and \( 0 < \parallel u\parallel  < c \) . That is, the points \( F\left( {x, u}\right) \) and \( G\left( {x, u}\right) \) belong to the same open half-space in \( {R}^{p} \) . So the homotopy

\[
\left( {1 - t}\right) F\left( {x, u}\right)  + {tG}\left( {x, u}\right)
\]

between \( F \) and \( G \) will not map any new points into 0, at least for \( \parallel u\parallel  < c \) .

By Taylor's theorem

\[
\left| \right| F\left( {x, u}\right)  - u\left| \right|  \leq  {c}_{1}\left| \right| u{\left| \right| }^{2},\;\text{ for }\;\left| \right| u\left| \right|  \leq  1.
\]

Hence

\[
\left| {\left( {F\left( {x, u}\right)  - u}\right)  \cdot  u}\right|  \leq  {c}_{1}\parallel u{\parallel }^{3}
\]

and

\[
F\left( {x, u}\right)  \cdot  u \geq  \parallel u{\parallel }^{2} - {c}_{1}\parallel u{\parallel }^{3} > 0
\]

for \( 0 < \parallel u\parallel  < \operatorname{Min}\left( {{c}_{1}^{-1},1}\right) \) , with a similar inequality for \( G \) .

To avoid moving distant points we select a smooth map \( \lambda  : {R}^{p} \rightarrow  R \) with

\[
\lambda \left( u\right)  = 1\text{ for }\parallel \left| u\right| \parallel  \leq  c/2
\]

\[
\lambda \left( u\right)  = 0\text{ for }\parallel \left| u\right| \parallel  \geq  c.
\]

Now the homotopy

\[
{F}_{t}\left( {x, u}\right)  = \left\lbrack  {1 - \lambda \left( u\right) t}\right\rbrack  F\left( {x, u}\right)  + \lambda \left( u\right) {tG}\left( {x, u}\right)
\]

deforms \( F = {F}_{0} \) into a mapping \( {F}_{1} \) that (1) coincides with \( G \) in the region \( \parallel u\parallel  < c/2 \) ,(2) coincides with \( F \) for \( \parallel u\parallel  \geq  c \) , and (3) has no new zeros. Making a corresponding deformation of the original mapping \( f \) , this clearly completes the proof of Lemma 4.

Proof of Theorem B. If \( f \) and \( g \) are smoothly homotopic, then Lemma 3 asserts that the Pontryagin manifolds \( {f}^{-1}\left( y\right) \) and \( {g}^{-1}\left( y\right) \) are framed cobordant. Conversely, given a framed cobordism \( \left( {X,\mathfrak{w}}\right) \) between \( {f}^{-1}\left( y\right) \) and \( {g}^{-1}\left( y\right) \) , an argument completely analogous to the proof of Theorem C constructs a homotopy

\[
F : M \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  {S}^{p}
\]

whose Pontryagin manifold \( \left( {{F}^{-1}\left( y\right) ,{F}^{ * }\mathfrak{v}}\right) \) is precisely equal to \( \left( {X,\mathfrak{w}}\right) \) . Setting \( {F}_{t}\left( x\right)  = F\left( {x, t}\right) \) , note that the maps \( {F}_{0} \) and \( f \) have exactly the same Pontryagin manifold. Hence \( {F}_{0} \sim  f \) by Lemma 4; and similarly \( {F}_{1} \sim  g \) . Therefore \( f \sim  g \) , which completes the proof of Theorem B.

REMARKS. Theorems A, B, and C can easily be generalized so as to apply to a manifold \( M \) with boundary. The essential idea is to consider only mappings which carry the boundary into a base point \( {s}_{0} \) . The homotopy classes of such mappings

\[
\left( {M,\partial M}\right)  \rightarrow  \left( {{S}^{p},{s}_{0}}\right)
\]

are in one-one correspondence with the cobordism classes of framed submanifolds

\[
N \subset  \operatorname{Interior}\left( M\right)
\]

of codimension \( p \) . If \( p \geq  \frac{1}{2}m + 1 \) , then this set of homotopy classes can be given the structure of an abelian group, called the \( p \) -th cohomotopy group \( {\pi }^{p}\left( {M,\partial M}\right) \) . The composition operation in \( {\pi }^{p}\left( {M,\partial M}\right) \) corresponds to the union operation for disjoint framed submanifolds of Interior \( \left( M\right) \) . (Compare §8, Problem 17.)

## THE HOPF THEOREM

As an example, let \( M \) be a connected and oriented manifold of dimension \( m = p \) . A framed submanifold of codimension \( p \) is just a finite set of points with a preferred basis at each. Let sgn \( \left( x\right) \) equal +1 or -1 according as the preferred basis determines the right or wrong orientation. Then \( \sum \operatorname{sgn}\left( x\right) \) is clearly equal to the degree of the associated map \( M \rightarrow  {S}^{m} \) . But it is not difficult to see that the framed cobordism class of the 0-manifold is uniquely determined by this integer \( \sum \operatorname{sgn}\left( x\right) \) . Thus we have proved the following.

Theorem of Hopf. If \( M \) is connected, oriented, and boundaryless, then two maps \( M \rightarrow  {S}^{m} \) are smoothly homotopic if and only if they have the same degree.

On the other hand, suppose that \( M \) is not orientable. Then given a basis for \( T{M}_{x} \) we can slide \( x \) around \( M \) in a closed loop so as to transform the given basis into one of opposite orientation. An easy argument then proves the following:

Theorem. If \( M \) is connected but nonorientable, then two maps \( M \rightarrow  {S}^{m} \) are homotopic if and only if they have the same mod 2 degree.

The theory of framed cobordism was introduced by Pontryagin in order to study homotopy classes of mappings

\[
{S}^{m} \rightarrow  {S}^{p}
\]

with \( m > p \) . For example if \( m = p + 1 \geq  4 \) , there are precisely two homotopy classes of mappings \( {S}^{m} \rightarrow  {S}^{p} \) . Pontryagin proved this result by classifying framed 1-manifolds in \( {S}^{m} \) . With considerably more difficulty he was able to show that there are just two homotopy classes also in the case \( m = p + 2 \geq  4 \) , using framed 2-manifolds. However, for \( m - p > 2 \) this approach to the problem runs into manifold diff-culties.

It has since turned out to be easier to enumerate homotopy classes of mappings by quite different, more algebraic methods.* Pontryagin's construction is, however, a double-edged tool. It not only allows us to translate information about manifolds into homotopy theory; it conversely enables us to translate any information about homotopy into manifold theory. Some of the deepest work in modern topology has come from the interplay of these two theories. René Thom's work on cobordism is an important example of this. (References [36], [21].)

---

* See for example S.-T. Hu, Homotopy Theory.

---
