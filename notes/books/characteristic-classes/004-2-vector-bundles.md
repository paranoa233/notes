# 2 Vector Bundles

Let \( B \) denote a fixed topological space, which will be called the base space.

Definition. A real vector bundle \( \xi \) over \( B \) consists of the following:

1) A topological space \( E = E\left( \xi \right) \) called the total space.

2) A (continuous) map \( \pi  : E \rightarrow  B \) called the projection map.

3) For each \( b \in  B \) , the structure of a vector space \( {}^{1} \) over the real numbers in the set \( {\pi }^{-1}\left( b\right) \) .

These must satisfy the following restriction:

Condition of local triviality. For each point \( p \in  B \) , there should exist a neighborhood \( U \subset  B \) , and integer \( n \geq  0 \) , and a homeomorphism

\( h : U \times  {\mathbb{R}}^{n} \rightarrow  {\pi }^{-1}\left( U\right) \) so that, for each \( b \in  U \) , the correspondence \( x \mapsto  h\left( {b, x}\right) \) defines an isomorphism between the vector space \( {\mathbb{R}}^{n} \) and the vector space \( {\pi }^{-1}\left( b\right) \) .

Such a pair \( \left( {U, h}\right) \) will be called a local coordinate system for \( \xi \) about \( b \) . If it is possible to choose \( U \) equal to the entire base space, then \( \xi \) will be called a trivial bundle.

The vector space \( {\pi }^{-1}\left( b\right) \) is called the fiber over \( b \) . It may be denoted by \( {F}_{b} \) or \( {F}_{b}\left( \xi \right) \) . Note that \( {F}_{b} \) is never vacuous, although it may consist of a single point. The dimension \( n \) of \( {F}_{b} \) is allowed to be a (locally constant) function of \( b \) ; but in most cases of interest this function is constant. One then speaks of an \( n \) -plane bundle, or briefly an \( {\mathbb{R}}^{n} \) -bundle.

---

\( {}^{1} \) To be more precise, this vector space structure could be specified by giving the subset of \( \mathbb{R} \times  \mathbb{R} \times  E \times  E \times  E \) consisting of all 5-tuples \( \left( {{t}_{1},{t}_{2},{e}_{1},{e}_{2},{e}_{3}}\right) \) with

\[
\pi \left( {e}_{1}\right)  = \pi \left( {e}_{2}\right)  = \pi \left( {e}_{3}\right) \text{ and }{e}_{3} = {t}_{1}{e}_{1} + {t}_{2}{e}_{2}
\]

---

The concept of a smooth vector bundle can be defined similarly. One requires that \( B \) and \( E \) be smooth manifolds, that \( \pi \) be a smooth map, and that, for each \( b \in  B \) there exist a local coordinate system \( \left( {U, h}\right) \) with \( b \in  U \) such that \( h \) is a diffeomorphism.

Remark. An \( {\mathbb{R}}^{n} \) -bundle is a very special example of a fibre bundle. (See [WS51].) In Steenrod’s terminology an \( {\mathbb{R}}^{n} \) -bundle is a fiber bundle with fiber \( {\mathbb{R}}^{n} \) and with the full linear group \( {\mathrm{{GL}}}_{n}\left( \mathbb{R}\right) \) in \( n \) variables as structural group.

Now consider two vector bundles \( \xi \) and \( \eta \) over the same base space \( B \) .

Definition. \( \xi \) is isomorphic to \( \eta \) , written \( \xi  \cong  \eta \) , if there exists a homeomorphism

\[
f : E\left( \xi \right)  \rightarrow  E\left( \eta \right)
\]

between the total spaces which maps each vector space \( {F}_{b}\left( \xi \right) \) isomorphically onto the corresponding vector space \( {F}_{b}\left( \eta \right) \) .

Example 1. The trivial bundle with total space \( B \times  {\mathbb{R}}^{n} \) , with projection map \( \pi \left( {b, x}\right)  = b \) , and with the vector space structures in the fibers defined by

\[
{t}_{1}\left( {b,{x}_{1}}\right)  + {t}_{2}\left( {b,{x}_{2}}\right)  = \left( {b,{t}_{1}{x}_{1} + {t}_{2}{x}_{2}}\right)
\]

will be denoted by \( {\varepsilon }_{B}^{n} \) . Note that a \( {\mathbb{R}}^{n} \) -bundle over \( B \) is trivial if and only if it is isomorphic to \( {\varepsilon }_{B}^{n} \) .

Example 2. The tangent bundle \( {\tau }_{M} \) of a smooth manifold \( M \) . The total space of \( {\tau }_{M} \) is the manifold \( \mathbf{T}M \) consisting of all pairs \( \left( {x, v}\right) \) with \( x \in  M \) and \( v \) tangent to \( M \) at \( x \) . The projection map \( \pi  : \mathbf{T}M \rightarrow  M \) is defined by \( \pi \left( {x, v}\right)  = x \) ; and the vector space structure in \( {\pi }^{-1}\left( x\right) \) is defined by

\[
{t}_{1}\left( {x,{v}_{1}}\right)  + {t}_{2}\left( {x,{v}_{2}}\right)  = \left( {x,{t}_{1}{v}_{1} + {t}_{2}{v}_{2}}\right) .
\]

The local triviality condition is not difficult to verify. Note that \( {\tau }_{M} \) is an example of a smooth vector bundle.

If \( {\tau }_{M} \) is a trivial bundle, then the manifold \( M \) is called parallelizable. For example, suppose that \( M \) is an open subset of \( {\mathbb{R}}^{n} \) . Then \( \mathbf{T}M \) is equal to \( M \times  {\mathbb{R}}^{n} \) , and \( M \) is clearly parallelizable.

The unit 2-sphere \( {S}^{2} \subset  {\mathbb{R}}^{3} \) provides an example of a manifold which is not parallelizable. (Compare 2-B.) In fact we will see in \( \text{ § }9 \) that a parallelizable manifold must have Euler characteristic zero, whereas the 2-sphere has Euler characteristic +2. (See Proposition 9.3 and Lemma 11.6.)

Example 3. The normal bundle \( {\nu }_{M} \) of a smooth manifold \( M \subset  {\mathbb{R}}^{n} \) is obtained as follows. The total space \( E \subset  M \times  {\mathbb{R}}^{n} \) is the set of all pairs \( \left( {x, v}\right) \) such that \( v \) is orthogonal to the tangent space \( {\mathbf{T}}_{x}M \) . The projection map \( \pi  : E \rightarrow  M \) and the vector space structure in \( {\pi }^{-1}\left( x\right) \) are defined, as in Examples 1,2, by the formulas

\[
\pi \left( {x, v}\right)  = x,\;{t}_{1}\left( {x,{v}_{1}}\right)  + {t}_{2}\left( {x,{v}_{2}}\right)  = \left( {x,{t}_{1}{v}_{1} + {t}_{2}{v}_{2}}\right) .
\]

The proof that \( {\nu }_{M} \) satisfies the local triviality condition will be deferred until 3.4.

Example 4. The real projective space \( {\mathbb{P}}^{n} \) can be defined \( {}^{2} \) as the set of all unordered pairs \( \{ x, - x\} \) where \( x \) ranges over the unit sphere \( {S}^{n} \subset  {\mathbb{R}}^{n + 1} \) ; and is topologized as a quotient space of \( {S}^{n} \) .

Let \( E\left( {\gamma }_{n}^{1}\right) \) be the subset of \( {\mathbb{P}}^{n} \times  {\mathbb{R}}^{n + 1} \) consisting of all pairs \( \left( {\{  \pm  x\} , v}\right) \) such that the vector \( v \) is a multiple of \( x \) . Define \( \pi  : E\left( {\gamma }_{n}^{1}\right)  \rightarrow  {\mathbb{P}}^{n} \) by \( \pi \left( {\{  \pm  x\} , v}\right)  = \{  \pm  x\} \) . Thus each fiber \( {\pi }^{-1}\left( {\{  \pm  x\} }\right) \) can be identified with the line through \( x \) and \( - x \) in \( {\mathbb{R}}^{n + 1} \) . Each such line is to be given its usual vector space structure. The resulting vector bundle \( {\gamma }_{n}^{1} \) will be called the canonical line bundle over \( {\mathbb{P}}^{n} \) .

Proof THAT \( {\gamma }_{n}^{1} \) IS LOCALLY TRIVIAL. Let \( U \subset  {S}^{n} \) be any open set which is small enough so as to contain no pair of antipodal points, and let \( {U}_{1} \) denote the image of \( U \) in \( {\mathbb{P}}^{n} \) . Then a homeomorphism \( h : {U}_{1} \times  {\mathbb{R}}^{n} \rightarrow  {\pi }^{-1}\left( {U}_{1}\right) \) is defined by the requirement that \( h\left( {\{  \pm  x\} , t}\right)  = \left( {\{  \pm  x\} ,{tx}}\right) \) for each \( \left( {x, t}\right)  \in  U \times  \mathbb{R} \) . Evidently \( \left( {{U}_{1}, h}\right) \) is a local coordinate system; hence \( {\gamma }_{n}^{1} \) is locally trivial.

Theorem 2.1. The bundle \( {\gamma }_{n}^{1} \) over \( {\mathbb{P}}^{n} \) is not trivial, for \( n \geq  1 \) . Proof. This will be proved by studying cross-sections of \( {\gamma }_{n}^{1} \)

---

\( {}^{2} \) Alternatively, \( {\mathbb{P}}^{n} \) can be defined as the set of lines through the origin in \( {\mathbb{R}}^{n + 1} \) . (Compare 1-B.) This amounts to the same thing since every such line cuts \( {S}^{n} \) in two antipodal points.

---

Definition. A cross-section of a vector bundle \( \xi \) with base space \( B \) is a continuous function \( s : B \rightarrow  E\left( \xi \right) \) which takes each \( b \in  B \) into the corresponding fiber \( {F}_{b}\left( \xi \right) \) . Such a cross-section is nowhere zero if \( s\left( b\right) \) is a non-zero vector of \( {F}_{b}\left( \xi \right) \) for each \( b \) .

(A cross-section of the tangent bundle of a smooth manifold \( M \) is usually called a vector field on \( M \) .)

Evidently a trivial \( {\mathbb{R}}^{1} \) -bundle possesses a cross-section which is nowhere zero. We will see that the bundle \( {\gamma }_{n}^{1} \) has no such cross-section.

Let \( s : {\mathbb{P}}^{n} \rightarrow  E\left( {\gamma }_{n}^{1}\right) \) be any cross-section, and consider the composition

\[
{S}^{n} \rightarrow  {\mathbb{P}}^{n}\overset{s}{ \rightarrow  }E\left( {\gamma }_{n}^{1}\right)
\]

which carries each \( x \in  {S}^{n} \) to some pair

\[
\left( {\{  \pm  x\} , t\left( x\right) x}\right)  \in  E\left( {\gamma }_{n}^{1}\right)
\]

Evidently \( t\left( x\right) \) is a continuous real valued function of \( x \) , and \( t\left( {-x}\right)  =  - t\left( x\right) \) . Since \( {S}^{n} \) is connected, it follows from the intermediate value theorem that \( t\left( {x}_{0}\right)  = 0 \) for some \( {x}_{0} \) . Hence \( s\left( \left\{  {\pm {x}_{0}}\right\}  \right)  = \left( {\left\{  {\pm {x}_{0}}\right\}  ,0}\right) \) . This completes the proof.

It is interesting to take a closer look at the space \( E\left( {\gamma }_{n}^{1}\right) \) for the special case \( n = 1 \) . In this case each point \( e = \left( {\{  \pm  x\} , v}\right) \) of \( E\left( {\gamma }_{n}^{1}\right) \) can be written as

\[
e = \left( {\{  \pm  \left( {\cos \theta ,\sin \theta }\right) \} , t\left( {\cos \theta ,\sin \theta }\right) }\right)
\]

with \( 0 \leq  \theta  \leq  \pi , t \in  \mathbb{R} \) . This representation is unique except that the point \( \left( {\{  \pm  \left( {\cos 0,\sin 0}\right) \} , t\left( {\cos 0,\sin 0}\right) }\right) \) is equal to \( \left( {\{  \pm  \left( {\cos \pi ,\sin \pi }\right) \} , - t\left( {\cos \pi ,\sin \pi }\right) }\right) \) for each \( t \) . In other words, \( E\left( {\gamma }_{1}^{1}\right) \) can be obtained from the strip \( \left\lbrack  {0,\pi }\right\rbrack   \times  \mathbb{R} \) in the \( \left( {\theta , t}\right) \) -plane by identifying the left hand boundary \( \left\lbrack  0\right\rbrack   \times  \mathbb{R} \) with the right hand boundary \( \left\lbrack  \pi \right\rbrack   \times  \mathbb{R} \) under the correspondence \( \left( {0, t}\right)  \mapsto  \left( {\pi , - t}\right) \) . Thus \( E\left( {\gamma }_{1}^{1}\right) \) is an open Möbius band. (Compare Figure 2.)

This description gives an alternative proof that \( {\gamma }_{1}^{1} \) is non-trivial, for the Möbius band is certainly not homeomorphic to the cylinder \( {\mathbb{P}}^{1} \times  \mathbb{R} \) .

![bo_d7du9galb0pc73deir9g_26_256_295_1019_483_0.jpg](images/bo_d7du9galb0pc73deir9g_26_256_295_1019_483_0.jpg)

Figure 2

Now consider a collection \( \left\{  {{s}_{1},\ldots ,{s}_{n}}\right\} \) of cross-sections of a vector bundle \( \xi \) .

Definition. The cross-sections \( {s}_{1},\ldots ,{s}_{n} \) are nowhere dependent if, for each \( b \in  B \) , the vectors \( {s}_{1}\left( b\right) ,\ldots ,{s}_{n}\left( b\right) \) are linearly independent.

Theorem 2.2. An \( {\mathbb{R}}^{n} \) -bundle \( \xi \) is trivial if and only if \( \xi \) admits \( n \) cross-sections \( {s}_{1}\left( b\right) ,\ldots ,{s}_{n}\left( b\right) \) which are nowhere dependent.

The proof will depend on the following basic result.

Lemma 2.3. Let \( \xi \) and \( \eta \) be vector bundles over \( B \) and let \( f : E\left( \xi \right)  \rightarrow  E\left( \eta \right) \) be a continuous function which maps each vector space \( {F}_{b}\left( \xi \right) \) isomorphically onto the corresponding vector space \( {F}_{b}\left( \eta \right) \) . Then \( f \) is necessarily a homeomorphism. Hence \( \xi \) is isomorphic to \( \eta \) .

Proof. Given any point \( {b}_{0} \in  B \) , choose local coordinate systems \( \left( {U, g}\right) \) for \( \xi \) and \( \left( {V, h}\right) \) for \( \eta \) , with \( {b}_{0} \in  U \cap  V \) . Then we must show that the composition

\[
\left( {U \cap  V}\right)  \times  {\mathbb{R}}^{n}\xrightarrow[]{{h}^{-1} \circ  f \circ  g}\left( {U \cap  V}\right)  \times  {\mathbb{R}}^{n}
\]

is a homeomorphism. Setting

\[
{h}^{-1}\left( {f\left( {g\left( {b, x}\right) }\right) }\right)  = \left( {b, y}\right)
\]

it is evident that \( y = \left\{  {{y}_{1},\ldots ,{y}_{n}}\right\} \) can be expressed in the form

\[
{y}_{i} = \mathop{\sum }\limits_{j}{f}_{ij}\left( b\right) {x}_{j}
\]

where \( \left\lbrack  {{f}_{ij}\left( b\right) }\right\rbrack \) denotes a non-singular matrix of real numbers. Furthermore, the entries \( {f}_{ij}\left( b\right) \) depend continuously on \( b \) . Let \( \left\lbrack  {{F}_{ji}\left( b\right) }\right\rbrack \) denote the inverse matrix. Evidently

\[
\left( {{g}^{-1} \circ  {f}^{-1} \circ  h}\right) \left( {b, y}\right)  = \left( {b, x}\right) ,
\]

where

\[
{x}_{j} = \mathop{\sum }\limits_{i}{F}_{ji}\left( b\right) {y}_{i}
\]

Since the numbers \( {F}_{ji}\left( b\right) \) depend continuously on the matrix \( \left\lbrack  {{f}_{ij}\left( b\right) }\right\rbrack \) , they depend continuously on \( b \) . Thus \( {g}^{-1} \circ  {f}^{-1} \circ  h \) is continuous, which completes the proof of 2.3.

Proof of 2.2. Let \( {s}_{1},\ldots ,{s}_{n} \) be cross-sections of \( \xi \) which are nowhere linearly dependent. Define \( f : B \times  {\mathbb{R}}^{n} \rightarrow  E \) by

\[
f\left( {b, x}\right)  = {x}_{1}{s}_{1}\left( b\right)  + \cdots  + {x}_{n}{s}_{n}\left( b\right)
\]

Evidently \( f \) is continuous and maps each fiber of the trivial bundle \( {\varepsilon }_{B}^{n} \) isomorphically onto the corresponding fiber of \( \xi \) . Hence \( f \) is a bundle isomorphism, and \( \xi \) is trivial.

Conversely suppose that \( \xi \) is trivial, with coordinate system \( \left( {B, h}\right) \) . Defining

\[
{s}_{i}\left( b\right)  = h\left( {b,\left( {0,\ldots ,0,1,0,\ldots ,0}\right) }\right)  \in  {F}_{b}\left( \xi \right)
\]

(with the 1 in the \( i \) -th place), it is evident that \( {s}_{1},\ldots ,{s}_{n} \) are nowhere dependent cross-sections. This completes the proof.

As an illustration, the tangent bundle of the circle \( {S}^{1} \subset  {\mathbb{R}}^{2} \) admits one nowhere zero cross-section, as illustrated in Figure 3. (The indicated arrows lead from \( x \in  {S}^{1} \) to \( x + v \) , where \( s\left( x\right)  = \left( {x, v}\right)  = \left( {\left( {{x}_{1},{x}_{2}}\right) ,\left( {-{x}_{2},{x}_{1}}\right) }\right) \) .) Hence \( {S}^{1} \) is parallelizable. Similarly the 3-sphere \( {S}^{3} \subset  {\mathbb{R}}^{4} \) admits three nowhere dependent vector fields \( {s}_{i}\left( x\right)  = \left( {x,{\bar{s}}_{i}\left( x\right) }\right) \) where

\[
{\bar{s}}_{1}\left( x\right)  = \left( {-{x}_{2},{x}_{1}, - {x}_{4},{x}_{3}}\right) ,
\]

\[
{\bar{s}}_{2}\left( x\right)  = \left( {-{x}_{3},{x}_{4},{x}_{1}, - {x}_{2}}\right) ,
\]

\[
{\bar{s}}_{3}\left( x\right)  = \left( {-{x}_{4}, - {x}_{3},{x}_{2},{x}_{1}}\right) .
\]

Hence \( {S}^{3} \) is parallelizable. (These formulas come from the quaternion multiplication in \( {\mathbb{R}}^{4} \) . Compare [WS51].)

![bo_d7du9galb0pc73deir9g_28_513_761_514_454_0.jpg](images/bo_d7du9galb0pc73deir9g_28_513_761_514_454_0.jpg)

Figure 3
