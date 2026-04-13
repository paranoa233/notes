# 6 a Cell Structure for Grassmann Manifolds

This section will describe a canonical cell subdivision, due to Ehresmann [Ehr34], which makes the infinite Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) into a CW-complex. Each finite Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) appears as a finite sub-complex. This cell structure has been used by Pontrjagin [Pon47] and by Chern [Che48] as a basis for the theory of characteristic classes. The reader should consult these sources, as well as [Wu48] for further information. For a thorough treatment of cell complexes in general, consult [LW69]. Grassmann manifolds appear there on p. 17.

First recall some definitions. Let \( {\mathbb{D}}^{p} \) denote the unit disk in \( {\mathbb{R}}^{p} \) , consisting of all vectors \( v \) with \( \left| v\right|  \leq  1 \) . The interior of \( {\mathbb{D}}^{p} \) is defined to be the subset consisting of all \( v \) with \( \left| v\right|  < 1 \) . For the special case \( p = 0 \) , both \( {\mathbb{D}}^{p} \) and its interior consist of a single point.

Any space homeomorphic to \( {\mathbb{D}}^{p} \) is called a closed \( p \) -cell; and any space homeomorphic to the interior of \( {\mathbb{D}}^{p} \) is called an open \( p \) -cell. For example \( {\mathbb{R}}^{p} \) is an open \( p \) -cell.

Definition 6.1 (J. H. C. Whitehead, 1949). A CW-complex consists of a Hausdorff space \( K \) , called the underlying space, together with a partition of \( K \) into a collection \( \left\{  {e}_{\alpha }\right\} \) of disjoint subsets, such that four conditions are satisfied:

1) Each \( {e}_{\alpha } \) is topologically an open cell of dimension \( n\left( \alpha \right)  \geq  0 \) . Furthermore for each cell \( {e}_{\alpha } \) there exists a continuous map

\[
f : {\mathbb{D}}^{n\left( \alpha \right) } \rightarrow  K
\]

which carries the interior of the disk \( {\mathbb{D}}^{n\left( \alpha \right) } \) homeomorphically onto \( {e}_{a} \) . (This \( f \) is called a characteristic map for the cell \( {e}_{\alpha } \) .)

2) Each point \( x \) which belongs to the closure \( {\bar{e}}_{\alpha } \) , but not to \( {e}_{\alpha } \) itself, must lie in a cell \( {e}_{\beta } \) of lower dimension.

If the complex is finite (i.e., if there are only finitely many \( {e}_{a} \) ) then these two conditions suffice. However in general two further conditions are needed. A subset of \( K \) is called a [finite] subcomplex if it is a closed set and is a union of [finitely many] \( {e}_{a} \) ’s.

3) Closure finiteness. Each point of \( K \) is contained in a finite subcomplex.

4) Whitehead topology. \( K \) is topologized as the direct limit of its finite subcomplexes. I.e., a subset of \( K \) is closed if and only if its intersection with each finite subcomplex is closed.

Note that the closure \( {\bar{e}}_{\alpha } \) of a cell of \( K \) need not be a cell. For example the sphere \( {S}^{n} \) can be considered as a CW-complex with one 0-cell and one \( n \) -cell. In this case the closure of the \( n \) -cell is equal to the entire sphere.

A theorem of Miyazaki [Miy52] asserts that every CW-complex is paracom-pact. (Compare [Dug66, p. 419].)

The cell structure for the Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) is obtained as follows. Recall that \( {\mathbb{R}}^{m} \) contains subspaces

\[
{\mathbb{R}}^{0} \subset  {\mathbb{R}}^{1} \subset  {\mathbb{R}}^{2} \subset  \cdots  \subset  {\mathbb{R}}^{m}
\]

where \( {\mathbb{R}}^{k} \) consists of all vectors of the form \( v = \left( {{v}_{1},\ldots ,{v}_{k},0,\ldots ,0}\right) \) . Any \( n \) -plane \( X \subset  {\mathbb{R}}^{m} \) gives rise to a sequence of integers

\[
0 \leq  \dim \left( {X \cap  {\mathbb{R}}^{1}}\right)  \leq  \dim \left( {X \cap  {\mathbb{R}}^{2}}\right)  \leq  \cdots  \leq  \dim \left( {X \cap  {\mathbb{R}}^{m}}\right)  = n.
\]

Two consecutive integers in this sequence differ by at most 1 . This fact is proved by inspecting the exact sequence

\[
0 \rightarrow  X \cap  {\mathbb{R}}^{k - 1} \rightarrow  X \cap  {\mathbb{R}}^{k}\xrightarrow[]{k\text{ -th coordinate }}\mathbb{R}\text{ . }
\]

Thus the above sequence of integers contains precisely \( n \) "jumps". By a Schubert symbol \( \sigma  = \left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right) \) is meant a sequence of \( n \) integers satisfying

\[
1 \leq  {\sigma }_{1} < {\sigma }_{2} < \cdots  < {\sigma }_{n} \leq  m
\]

For each Schubert symbol \( \sigma \) , let \( e\left( \sigma \right)  \subset  {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) denote the set of all \( n \) -planes \( X \) such that

\[
\dim \left( {X \cap  {\mathbb{R}}^{{\sigma }_{i}}}\right)  = i,\dim \left( {X \cap  {\mathbb{R}}^{{\sigma }_{i} - 1}}\right)  = i - 1
\]

for \( i = 1,\ldots , n \) . Evidently each \( X \in  {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) belongs to precisely one of the sets \( e\left( \sigma \right) \) . We will see presently that \( e\left( \sigma \right) \) is an open cell \( {}^{1} \) of dimension

\[
d\left( \sigma \right)  = \left( {{\sigma }_{1} - 1}\right)  + \left( {{\sigma }_{2} - 2}\right)  + \cdots  + \left( {{\sigma }_{n} - n}\right) .
\]

Let \( {\mathbb{H}}^{k} \subset  {\mathbb{R}}^{k} \) denote the open half-space consisting of all \( x = \left( {{\xi }_{1},\ldots ,{\xi }_{k},0,\ldots ,0}\right) \) with \( {\xi }_{k} > 0 \) . Note that an \( n \) -plane \( X \) belongs to \( e\left( \sigma \right) \) if and only if it possesses a basis \( {x}_{1},\ldots ,{x}_{n} \) so that

\[
{x}_{1} \in  {\mathbb{H}}^{{\sigma }_{1}},\ldots ,{x}_{n} \in  {\mathbb{H}}^{{\sigma }_{n}}
\]

for if \( X \) possesses such a basis, then the exact sequence above shows that

\[
\dim \left( {X \cap  {\mathbb{R}}^{{\sigma }_{i}}}\right)  > \dim \left( {X \cap  {\mathbb{R}}^{{\sigma }_{i} - 1}}\right)
\]

for \( i = 1,\ldots , n \) , hence \( X \in  e\left( \sigma \right) \) . The converse is proved similarly. In terms of matrices, the \( n \) -plane \( X \) belongs to \( e\left( \sigma \right) \) if and only if it can be described as the row space of an \( n \times  m \) matrix \( \left\lbrack  {x}_{ij}\right\rbrack \) of the form

\[
\left\lbrack  \begin{matrix}  * & \ldots &  * {10} & \ldots & {000} & \ldots & {000} & \ldots & 0 \\   * & \ldots &  *  *  * & \ldots &  * {10} & \ldots & {000} & \ldots & 0 \\  \vdots & & \vdots & & \vdots & & \vdots & & \vdots \\   * & \ldots &  *  *  * & \ldots &  *  *  * & \ldots &  * {10} & \ldots & 0 \end{matrix}\right\rbrack
\]

where the \( i \) -th row has \( {\sigma }_{i} \) -th entry positive (say equal to 1), and all subsequent entries zero.

---

\( {}^{1} \) The closure \( \bar{e}\left( \sigma \right) \) is called a Schubert variety. (Compare [Sch].) In the notation of Chern and Wu, the cell \( e\left( \sigma \right) \) is indexed not by the sequence \( \sigma  = \left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right) \) but rather by the modified sequence \( \left( {{\sigma }_{1} - 1,{\sigma }_{2} - 2,\ldots ,{\sigma }_{n} - n}\right) \) , which is more convenient to use for many purposes.

---

Lemma 6.2. Each \( n \) -plane \( X \in  e\left( \sigma \right) \) possesses a unique orthonormal basis \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) which belongs to \( {\mathbb{H}}^{{\sigma }_{1}} \times  \cdots  \times  {\mathbb{H}}^{{\sigma }_{n}} \) .

Proof. The vector \( {x}_{1} \) is required to lie in the 1-dimensional vector space \( X \cap  {\mathbb{R}}^{{\sigma }_{1}} \) , and to be a unit vector. This leaves only two possibilities for \( {x}_{1} \) , and the condition that the \( {\sigma }_{1} \) -th coordinate be positive specifies one of these two. Now \( {x}_{2} \) is required to be a unit vector in the 2 dimensional space \( X \cap  {\mathbb{R}}^{{\sigma }_{2}} \) , and to be orthogonal to \( {x}_{1} \) . Again this leaves two possibilities, and the condition that the \( {\sigma }_{2} \) -th coordinate be positive specifies one of these two. Continuing by induction, it follows that \( {x}_{3},{x}_{4},\ldots ,{x}_{n} \) are also uniquely determined.

Definition. Let \( {e}^{\prime }\left( \sigma \right)  = {\mathrm{V}}_{n}^{0}\left( {\mathbb{R}}^{m}\right)  \cap  \left( {{\mathbb{H}}^{{\sigma }_{1}} \times  \cdots  \times  {\mathbb{H}}^{{\sigma }_{n}}}\right) \) denote the set of all orthonormal \( n \) -frames \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) such that each \( {x}_{i} \) belongs to the open half-space \( {\mathbb{H}}^{{\sigma }_{i}} \) . Let \( {\bar{e}}^{\prime }\left( \sigma \right) \) denote the set of orthonormal frames \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) such that each \( {x}_{i} \) belongs to the closure \( {\overline{\mathbb{H}}}^{{\sigma }_{i}} \) .

Lemma 6.3. The set \( {\bar{e}}^{\prime }\left( \sigma \right) \) is topologically a closed cell of dimension \( d\left( \sigma \right)  = \left( {{\sigma }_{1} - 1}\right)  + \left( {{\sigma }_{2} - 2}\right)  + \cdots  + \left( {{\sigma }_{n} - n}\right) \) , with interior \( {e}^{\prime }\left( \sigma \right) \) . Furthermore \( q \) maps the interior \( {e}^{\prime }\left( \sigma \right) \) homeomorphically onto \( e\left( \sigma \right) \) .

Thus \( e\left( \sigma \right) \) is actually an open cell of dimension \( d\left( \sigma \right) \) . Furthermore the map

\[
{\left. q\right| }_{{\bar{e}}^{\prime }\left( \sigma \right) } : {\bar{e}}^{\prime }\left( \sigma \right)  \rightarrow  {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{m}\right)
\]

will serve as a characteristic map for this cell.

Proof. The proof of 6.3 will be by induction on \( n \) . For \( n = 1 \) the set \( {\bar{e}}^{\prime }\left( {\sigma }_{1}\right) \) consists of all vectors

\[
{x}_{1} = \left( {{x}_{11},{x}_{12},\ldots ,{x}_{1{\sigma }_{1}},0,\ldots ,0}\right)
\]

with \( \sum {x}_{1i}^{2} = 1,{x}_{1{\sigma }_{1}} \geq  0 \) . Evidently \( {\bar{e}}^{\prime }\left( {\sigma }_{1}\right) \) is a closed hemisphere of dimension \( {\sigma }_{1} - 1 \) , and therefore is homeomorphic to the disk \( {\mathbb{D}}^{{\sigma }_{1} - 1} \) .

Given unit vectors \( u, v \in  {\mathbb{R}}^{m} \) with \( u \neq   - v \) , let \( T\left( {u, v}\right) \) denote the unique rotation of \( {\mathbb{R}}^{m} \) which carries \( u \) to \( v \) , and leaves everything orthogonal to \( u \) and \( v \) fixed. Thus \( T\left( {u, u}\right) \) is the identity map and \( T\left( {v, u}\right)  = T{\left( u, v\right) }^{-1} \) . Alternatively \( T\left( {u, v}\right) \) can be defined by the formula

\[
T\left( {u, v}\right) x = x - \frac{\left( {u + v}\right)  \cdot  x}{1 + u \cdot  v}\left( {u + v}\right)  + 2\left( {u \cdot  x}\right) v
\]

In fact the function \( T\left( {u, v}\right) \) defined in this way is linear in \( x \) , and has the correct effect on the vectors \( u, v \) , and on all vectors orthogonal to \( u \) and \( v \) . It follows from this formula that:

1) \( T\left( {u, v}\right) x \) is continuous as a function of three variables; and

2) if \( u, v \in  {\mathbb{R}}^{k} \) then \( T\left( {u, v}\right) x \equiv  x \) (modulo \( {\mathbb{R}}^{k} \) ).

Let \( {b}_{i} \in  {\mathbb{H}}^{{\sigma }_{i}} \) denote the vector with \( {\sigma }_{i} \) -th coordinate equal to 1, and all other coordinates zero. Thus \( \left( {{b}_{1},\ldots ,{b}_{n}}\right)  \in  {e}^{\prime }\left( \sigma \right) \) . For any \( n \) -frame \( \left( {{x}_{1},\ldots ,{x}_{n}}\right)  \in  {\bar{e}}^{\prime }\left( \sigma \right) \) consider the rotation

\[
T = T\left( {{b}_{n},{x}_{n}}\right)  \circ  T\left( {{b}_{n - 1},{x}_{n - 1}}\right)  \circ  \cdots  \circ  T\left( {{b}_{1},{x}_{1}}\right)
\]

of \( {\mathbb{R}}^{m} \) . This rotation carries the \( n \) vectors \( {b}_{1},\ldots ,{b}_{n} \) to the vectors \( {x}_{1},\ldots ,{x}_{n} \) respectively. In fact the rotations \( T\left( {{b}_{1},{x}_{1}}\right) ,\ldots , T\left( {{b}_{i - 1},{x}_{i - 1}}\right) \) leave \( {b}_{i} \) fixed (since \( {b}_{i} \cdot  {b}_{j} = {b}_{i} \cdot  {x}_{j} = 0 \) for \( i > \mathrm{j} \) ); the rotation \( T\left( {{b}_{i},{x}_{i}}\right) \) carries \( {b}_{i} \) to \( {x}_{i} \) ; and the rotations \( T\left( {{b}_{i + 1},{x}_{i + 1}}\right) ,\ldots , T\left( {{b}_{n},{x}_{n}}\right) \) leave \( {x}_{i} \) fixed.

Given an integer \( {\sigma }_{n + 1} > {\sigma }_{n} \) let \( D \) denote the set of all unit vectors \( u \in  {\overline{\mathbb{H}}}^{{\sigma }_{n + 1}} \) with

\[
{b}_{1} \cdot  u = \cdots  = {b}_{n} \cdot  u = 0.
\]

Evidently \( D \) is a closed hemisphere of dimension \( {\sigma }_{n + 1} - n - 1 \) , and hence is topologically a closed cell. We will construct a homeomorphism

\[
f : {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right)  \times  D \rightarrow  {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n + 1}}\right) .
\]

In fact \( f \) is defined by the formula

\[
f\left( {\left( {{x}_{1},\ldots ,{x}_{n}}\right) , u}\right)  = \left( {{x}_{1},\ldots ,{x}_{n},{Tu}}\right)
\]

where the rotation \( T \) depends on \( {x}_{1},\ldots ,{x}_{n} \) , as above. To prove that \( \left( {{x}_{1},\ldots ,{x}_{n},{Tu}}\right) \) actually belongs to \( {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n + 1}}\right) \) we note that

\[
{x}_{i} \cdot  {Tu} = T{b}_{i} \cdot  {Tu} = {b}_{i} \cdot  u = 0
\]

for \( i \leq  n \) , and that

\[
{Tu} \cdot  {Tu} = u \cdot  u = 1
\]

where \( {Tu} \in  {\overline{\mathbb{H}}}^{{\sigma }_{n + 1}} \) since \( {Tu} \equiv  u\left( {\;\operatorname{mod}\;{\mathbb{R}}^{{\sigma }_{n}}}\right) \) . Evidently \( f \) maps \( {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right)  \times  D \) continuously to \( {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n + 1}}\right) \) . Similarly the formula

\[
u = {T}^{-1}{x}_{n + 1} = T\left( {{x}_{1},{b}_{1}}\right)  \circ  \cdots  \circ  T\left( {{x}_{n},{b}_{n}}\right) {x}_{n + 1} \in  D
\]

shows that \( {f}^{-1} \) is well defined and continuous.

Thus \( {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n + 1}}\right) \) is homeomorphic to the product \( {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right)  \times  D \) It follows by induction on \( n \) that each \( {\bar{e}}^{\prime }\left( \sigma \right) \) is a closed cell of dimension \( d\left( \sigma \right) \) . A similar induction shows that each \( {e}^{\prime }\left( \sigma \right) \) is the interior of the cell \( {\bar{e}}^{\prime }\left( \sigma \right) \) . In fact the homeomorphism

\[
f : {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right)  \times  D \rightarrow  {\bar{e}}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n + 1}}\right)
\]

carries the product \( {e}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right)  \times \) Interior \( D \) onto \( {e}^{\prime }\left( {{\sigma }_{1},\ldots ,{\sigma }_{n + 1}}\right) \) .

Proof that the map

\[
{\left. q\right| }_{{e}^{\prime }\left( \sigma \right) } : {e}^{\prime }\left( \sigma \right)  \rightarrow  e\left( \sigma \right)
\]

is a homeomorphism. According to 6.2, \( q \) carries \( {e}^{\prime }\left( \sigma \right) \) in one-one fashion onto \( e\left( \sigma \right) \) . On the other hand, if \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) belongs to the boundary \( {\bar{e}}^{\prime }\left( \sigma \right)  \smallsetminus  {e}^{\prime }\left( \sigma \right) \) , then the \( n \) -plane \( X = q\left( {{x}_{1},\ldots ,{x}_{n}}\right) \) does not belong to \( e\left( \sigma \right) \) , for one of the vectors \( {x}_{i} \) must lie in the boundary \( {\mathbb{R}}^{{\sigma }_{i} - 1} \) of the half-space \( {\overline{\mathbb{H}}}^{{\sigma }_{i}} \) . This implies that

\[
\dim \left( {X \cap  {\mathbb{R}}^{{\sigma }_{i} - 1}}\right)  \geq  i
\]

and hence that \( X \notin  e\left( \sigma \right) \) .

Now let \( A \subset  {e}^{\prime }\left( \sigma \right) \) be a relatively closed subset. Then \( \bar{A} \cap  {e}^{\prime }\left( \sigma \right)  = A \) , where the closure \( \bar{A} \subset  {\bar{e}}^{\prime }\left( \sigma \right) \) is compact, hence \( q\left( \bar{A}\right) \) is closed. The preceding paragraph implies that \( q\left( \bar{A}\right)  \cap  e\left( \sigma \right)  = q\left( A\right) \) , and it follows that \( q\left( A\right)  \subset  e\left( \sigma \right) \) is a relatively closed set. Thus \( q \) maps the cell \( {e}^{\prime }\left( \sigma \right) \) homeomorphically onto \( e\left( \sigma \right) \) .

Theorem 6.4. The \( \left( \begin{matrix} m \\  n \end{matrix}\right) \) sets \( e\left( \sigma \right) \) form the cells of a CW-complex with underlying space \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{m}\right) \) . Similarly taking the direct limit as \( m \rightarrow  \infty \) , one obtains an infinite CW-complex with underlying space \( {\mathrm{{Gr}}}_{n} = {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) .

Proof. We must first show that each point in the boundary of a cell \( e\left( \sigma \right) \) belongs to a cell \( e\left( \tau \right) \) of lower dimension. Since \( {\bar{e}}^{\prime }\left( \sigma \right) \) is compact, the image \( q{\bar{e}}^{\prime }\left( \sigma \right) \) is equal to \( \bar{e}\left( \sigma \right) \) . Hence every \( n \) -plane \( X \) in the boundary \( \bar{e}\left( \sigma \right)  - e\left( \sigma \right) \) has a basis \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) belonging to \( {\bar{e}}^{\prime }\left( \sigma \right)  - {e}^{\prime }\left( \sigma \right) \) Evidently the vectors \( {x}_{1},\ldots ,{x}_{n} \) are orthonormal, with \( {x}_{i} \in  {\mathbb{R}}^{{\sigma }_{i}} \) . It follows that \( \dim \left( {X \cap  {\mathbb{R}}^{{\sigma }_{i}}}\right)  \geq  i \) for each \( i \) , thus the Schubert symbol \( \left( {{\tau }_{1},\ldots ,{\tau }_{n}}\right) \) associated with \( X \) must satisfy

\[
{\tau }_{1} \leq  {\sigma }_{1},\ldots ,{\tau }_{n} \leq  {\sigma }_{n}
\]

As above, one of the vectors \( {x}_{i} \) must actually belong to \( {\mathbb{R}}^{{\sigma }_{i} - 1} \) ; hence the corresponding integer \( {\tau }_{i} \) must be strictly less than \( {\sigma }_{i} \) . Therefore \( d\left( \tau \right)  < d\left( \sigma \right) \) . Together with 6.3, this completes the proof that \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) is a finite CW-complex.

Similarly \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) is a CW-complex. The closure finiteness condition is satisfied since each \( X \in  {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) belongs to a finite subcomplex \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{m}\right) \) . The space \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) has the direct limit topology by definition.

It is instructive to look at the special case \( n = 1 \) .

Corollary 6.5. The infinite projective space \( {\mathbb{P}}^{\infty } = {\mathrm{{Gr}}}_{1}\left( {\mathbb{R}}^{\infty }\right) \) is a CW-complex having one \( r \) -cell \( e\left( {r + 1}\right) \) for each integer \( r \geq  0 \) . The closure \( \bar{e}\left( {r + 1}\right)  \subset  {\mathbb{P}}^{\infty } \) is equal to the finite projective space \( {\mathbb{P}}^{r} \) .

The proof is straightforward.

Now let us count the number of \( r \) -cells in \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) for arbitrary \( n \) . It is convenient to introduce the language of partitions.

Definition 6.6. A partition of an integer \( r \geq  0 \) is an unordered sequence \( {i}_{1}{i}_{2}\ldots {i}_{s} \) of positive integers with sum \( \mathbb{R} \) . The number of partitions of \( r \) is customarily denoted by \( p\left( r\right) \) . Thus for \( r \leq  {10} \) one has the following table.

<table><tr><td>\( r \)</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td></tr><tr><td>\( p\left( r\right) \)</td><td>1</td><td>1</td><td>2</td><td>3</td><td>5</td><td>7</td><td>11</td><td>15</td><td>22</td><td>30</td><td>42</td></tr></table>

Table 6.1: Partitions of \( r \) for \( r \leq  {10} \)

For example the integer 4 has five partitions, namely: 111 1 1 1 1 2 , 22 , 13, and 4. The integer 0 has just one (vacuous) partition. (According to Hardy and Ramanujan the function \( p\left( r\right) \) is asymptotic to \( \exp \left( {\pi \sqrt{{2r}/3}}\right) /{4r}\sqrt{3} \) as \( r \rightarrow  \infty \) . For further information see [Ost56].)

To every Schubert symbol \( \left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right) \) with \( d\left( \sigma \right)  = r \) and \( {\sigma }_{n} \leq  m \) there corresponds a partition \( {i}_{1}\ldots {i}_{s} \) of \( r \) , where \( {i}_{1},\ldots ,{i}_{s} \) denotes the sequence obtained from \( {\sigma }_{1} - 1,\ldots ,{\sigma }_{n} - n \) by cancelling any zeros which may appear at the beginning of this sequence. Clearly

\[
1 \leq  {i}_{1} \leq  {i}_{2} \leq  \cdots  \leq  {i}_{s} \leq  m - n
\]

and \( s \leq  n \) . Thus

Corollary 6.7. The number of \( r \) -cells in \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{m}\right) \) is equal to the number of partitions of \( r \) into at most \( n \) integers each of which is \( \leq  m - n \) .

In particular, if both \( n \) and \( m - n \) are \( \geq  r \) , then the number of \( r \) -cells in \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) is equal to \( p\left( r\right) \) .

Note that this corollary remains true if \( m \) is allowed to take the value \( + \infty \) .

Here are five problems for the reader.

Problem 6-A. Show that a CW-complex is finite if and only if its underlying space is compact.

Problem 6-B. Show that the restriction homomorphism

\[
{i}^{ * } : {\mathrm{H}}^{p}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{\infty }\right) }\right)  \rightarrow  {\mathrm{H}}^{p}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) }\right)
\]

is an isomorphism for \( p < k \) . Any coefficient group may be used. (Compare the description of cohomology for CW-complexes in Appendix A.)

Problem 6-C. Show that the correspondence \( X\overset{f}{ \rightarrow  }{\mathbb{R}}^{1} \oplus  X \) defines an embedding of the Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) into \( {\operatorname{Gr}}_{n + 1}\left( {{\mathbb{R}}^{1} \oplus  {\mathbb{R}}^{m}}\right)  = {\operatorname{Gr}}_{n + 1}\left( {\mathbb{R}}^{m + 1}\right) \) , and that \( f \) is covered by a bundle map

\[
{\varepsilon }^{1} \oplus  {\gamma }^{n}\left( {\mathbb{R}}^{m}\right)  \rightarrow  {\gamma }^{n + 1}\left( {\mathbb{R}}^{m + 1}\right) .
\]

Show that \( f \) carries the \( r \) -cell of \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) which corresponds to a given partition \( {i}_{1}\ldots {i}_{s} \) of \( r \) onto the \( r \) -cell of \( {\operatorname{Gr}}_{n + 1}\left( {\mathbb{R}}^{m + 1}\right) \) which corresponds to the same partition \( {i}_{1}\ldots {i}_{s} \) .

Problem 6-D. Show that the number of distinct Stiefel-Whitney numbers \( {\mathrm{w}}_{1}^{{r}_{1}}\ldots {\mathrm{w}}_{n}^{{r}_{n}}\left\lbrack  M\right\rbrack \) for an \( n \) -dimensional manifold is equal to \( p\left( n\right) \) .

Problem 6-E. Show that the number of \( r \) -cells in \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is equal to the number of \( r \) -cells in \( {\operatorname{Gr}}_{k}\left( {\mathbb{R}}^{n + k}\right) \) (or show that these two CW-complexes are actually isomorphic).
