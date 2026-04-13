# Appendix: The Homotopy Type of a Monotone Union

Based on lecture notes by

M. Spivak and R. Wells

The object of this appendix will be to give an alternative version for the final step in the proof of Theorem 17.3 (the fundamental theorem of Morse theory). Given the subsets \( {\Omega }^{{a}_{0}} \subseteq  {\Omega }^{{a}_{1}} \subseteq  {\Omega }^{{a}_{2}} \subseteq  \ldots \) of the path space \( \Omega  = \Omega \left( {M;p, q}\right) \) , and given the information that each \( {\Omega }^{{a}_{i}} \) has the homotopy type of a certain CW-complex, we wish to prove that the union \( \Omega \) also has the homotopy type of a certain CW-complex.

More generally consider a topological space \( X \) and a sequence \( {X}_{0} \subseteq  {X}_{1} \subseteq  {X}_{2} \subseteq \) ... of subspaces. To what extent is the homotopy type of \( X \) determined by the homotopy types of the \( {X}_{i} \) ?

It is convenient to consider the infinite union

\[
{X}_{\sum } = {X}_{0} \times  \left\lbrack  {0,1}\right\rbrack   \cup  {X}_{1} \times  \left\lbrack  {1,2}\right\rbrack   \cup  {X}_{2} \times  \left\lbrack  {2,3}\right\rbrack   \cup  \ldots .
\]

This is to be topologized as a subset of \( X \times  \mathbf{R} \) .

Definition A.1. We will say that \( X \) is the homotopy direct limit of the sequence \( \left( {X}_{i}\right) \) if the projection map \( p : {X}_{\sum } \rightarrow  X \) , defined by \( p\left( {x,\tau }\right)  = x \) , is a homotopy equivalence.

Example A.2. Suppose that each point of \( X \) lies in the interior of some \( {X}_{i} \) , and that \( X \) is paracompact. Then using a partition of unity one can construct a map

\[
f : X \rightarrow  \mathbf{R}
\]

so that \( f\left( x\right)  \geq  i + 1 \) for \( x \neq  {X}_{i} \) , and \( f\left( x\right)  \geq  0 \) for all \( x \) . Now the correspondence \( x \mapsto  \left( {x, f\left( x\right) }\right) \) maps \( X \) homeomorphically onto a subset of \( X \) . which is clearly a deformation retract. Therefore \( p \) is a homotopy equivalence; and \( X \) is a homotopy direct limit.

Example A.3. Let \( X \) be a CW-complex, and let the \( {X}_{i} \) be subcomplexes with union \( X \) . Since \( p : {X}_{\sum } \rightarrow  X \) induces isomorphisms of homotopy groups in all dimensions, it follows from Whitehead's theorem that \( \mathrm{X} \) is a homotopy direct limit.

Example A.4. The unit interval \( \left\lbrack  {0,1}\right\rbrack \) is not the homotopy direct limit of the sequence of closed subsets \( \left\lbrack  0\right\rbrack   \cup  \left\lbrack  {1/i,1}\right\rbrack \) .

The main result of this appendix is the following.

Theorem A.5. Suppose that \( X \) is the homotopy direct limit of \( \left( {X}_{i}\right) \) and \( Y \) is the homotopy direct limit of \( \left( {Y}_{i}\right) \) . Let \( f : X \rightarrow  Y \) be a map which carries each \( {X}_{i} \) into \( {Y}_{i} \) by a homotopy equivalence. Then \( f \) itself is a homotopy equivalence.

Assuming Theorem A.5, the alternative proof of Theorem 17.3 can be given as follows. Recall that we bad constructed a commutative diagram

![bo_d7du90alb0pc73deir8g_136_632_461_393_167_0.jpg](images/bo_d7du90alb0pc73deir8g_136_632_461_393_167_0.jpg)

of homotopy equivalences. Since \( \Omega  =  \cup  {\Omega }^{{a}_{i}} \) and \( K =  \cup  {K}_{i} \) are homotopy direct limits (compare Examples A. 2 and A. 3 above), it follows that the limit mapping \( \Omega  \rightarrow  K \) is also a homotopy equivalence.

Proof of Theorem A.5. Define \( {f}_{\sum } : {X}_{\sum } \rightarrow  {Y}_{\sum } \) by \( {f}_{\sum }\left( {x, t}\right)  = \left( {f\left( x\right) , t}\right) \) . It is clearly sufficient to prove that \( {f}_{\sum } \) is a homotopy equivalence.

Case 1. Suppose that \( {X}_{i} = {Y}_{i} \) and that each map \( {f}_{i} : {X}_{i} \rightarrow  {Y}_{i} \) (obtained by restricting \( f \) ) is homotopic to the identity. We must prove that \( {f}_{\sum } \) is a homotopy equivalence.

Remark. Under these conditions it would be natural to conjecture that \( {f}_{\sum } \) . must actually be homotopic to the identity. However counterexamples can be given.

For each \( n \) let

\[
{h}_{u}^{n} : {X}_{n} \rightarrow  {X}_{n}
\]

be a one-parameter family of mappings, with \( {h}_{0}^{n} = {f}_{n},{h}_{1}^{n} = \) identity. Define the homotopy

\[
{h}_{u} : {X}_{\sum } \rightarrow  {X}_{\sum }
\]

as follows (where it is always to be understood that \( 0 \leq  t \leq  1 \) , and \( n = 0,1,2,\ldots \) ).

\[
{h}_{u}\left( {x, n + t}\right)  = \left\{  \begin{array}{lll} \left( {{h}_{u}^{n}\left( x\right) , n + {2t}}\right) & \text{ for } & 0 \leq  t \leq  \frac{1}{2} \\  \left( {{h}_{\left( {3 - {4t}}\right) u}^{n}\left( x\right) , n + 1}\right) & \text{ for } & \frac{1}{2} \leq  t \leq  \frac{3}{4} \\  \left( {{h}_{\left( {4 - {3t}}\right) u}^{n}\left( x\right) , n + 1}\right) & \text{ for } & \frac{3}{4} \leq  t \leq  1. \end{array}\right.
\]

Taking \( u = 0 \) this defines a map \( {h}_{0} : {X}_{\sum } \rightarrow  {X}_{\sum } \) which is clearly homotopic to \( {f}_{\sum } \) . The mapping \( {h}_{1} : {X}_{\sum } \rightarrow  {X}_{\sum } \) on the other hand has the following properties:

\[
{h}_{1}\left( {x, n + t}\right)  = \left( {x, n + {2t}}\right) \;\text{ for }\;0 \leq  t \leq  \frac{1}{2}
\]

\[
{h}_{1}\left( {x, n + t}\right)  \in  {X}_{n + 1} \times  \left\lbrack  {n + 1}\right\rbrack  \;\text{ for }\;\frac{1}{2} \leq  t \leq  1.
\]

We will show that any such map \( {h}_{1} \) is a homotopy equivalence. In fact a homotopy inverse \( g : {X}_{\sum } \rightarrow  {X}_{\sum } \) can be defined by the formula

\[
g\left( {x, n + t}\right)  = \left\{  \begin{array}{lll} \left( {x, n + {2t}}\right) & \text{ for } & 0 \leq  t \leq  \frac{1}{2} \\  {h}_{1}\left( {x, n + \frac{3}{2} - t}\right) & \text{ for } & \frac{1}{2} \leq  t \leq  1. \end{array}\right.
\]

This is well defined since

\[
{h}_{1}\left( {x, n + \frac{1}{2}}\right)  = {h}_{1}\left( {x, n + 1}\right)  = \left( {x, n + 1}\right) .
\]

Proof that the composition \( {h}_{1} \circ  g \) is homotopic to the identity map of \( {X}_{\sum } \) . Note that

\[
g\left( {x, n + t}\right)  = \left\{  \begin{array}{lll} \left( {x, n + {2t}}\right) & \text{ for } & 0 \leq  t \leq  \frac{1}{4} \\  {h}_{1}\left( {x, n + {2t}}\right) & \text{ for } & \frac{1}{4} \leq  t \leq  \frac{1}{2} \\  {h}_{1}\left( {x, n + \frac{3}{2} - t}\right) & \text{ for } & \frac{1}{2} \leq  t \leq  1 \end{array}\right.
\]

Define a homotopy \( {H}_{u} : {X}_{\sum } \rightarrow  {X}_{\sum } \) as follows. For \( 0 \leq  u \leq  \frac{1}{2} \) let

\[
{H}_{u}\left( {x, n + t}\right)  = \left\{  \begin{array}{ll} {h}_{1} \circ  g\left( {x, n + t}\right) & \text{ for }\;t \in  \left\lbrack  {0,\frac{\left( 1 - u\right) }{4}}\right\rbrack   \cup  \left\lbrack  {\frac{1}{2} + t}\right. \\  {h}_{1}\left( {x, n + 1 - u}\right) & \text{ for }\;\frac{\left( 1 - u\right) }{4} \leq  t \leq  \frac{1}{2} + u. \end{array}\right.
\]

This is well defined since

\[
{h}_{1}g\left( {x, n + \frac{\left( 1 - u\right) }{2}}\right)  = {h}_{1}g\left( {x, n + \frac{1}{2} + u}\right)  = {h}_{1}\left( {x, n + 1 - u}\right) .
\]

Now \( {H}_{0} \) is equal to \( {h}_{1}g \) and \( {H}_{\frac{1}{2}} \) is given by

\[
{H}_{\frac{1}{2}}\left( {x, n + t}\right)  = \left\{  \begin{array}{ll} \left( {x, n + {4t}}\right) & 0 \leq  t \leq  \frac{1}{4} \\  \left( {x, n + 1}\right) & \frac{1}{4} \leq  t \leq  1. \end{array}\right.
\]

Clearly this is homotopic to the identity.

Thus \( {h}_{1}g \) is homotopic to the identity; and a completely analogous argument shows that \( g{h}_{1} \) is homotopic to the identity. This completes the proof in Case 1. Case 2. Now let \( X \) and \( Y \) be arbitrary. For each \( n \) let \( {g}_{n} : {Y}_{n} \rightarrow  {X}_{n} \) be a homotopy inverse to \( {f}_{n} \) . Note that the diagram

![bo_d7du90alb0pc73deir8g_137_654_1410_272_173_0.jpg](images/bo_d7du90alb0pc73deir8g_137_654_1410_272_173_0.jpg)

(where \( {\iota }_{n} \) and \( {\jmath }_{n} \) denote inclusion maps) is homotopy commutative. In fact

\[
{i}_{n} \circ  {g}_{n} \sim  {g}_{n + 1} \circ  {f}_{n + 1} \circ  {i}_{n} \circ  {g}_{n} = {g}_{n + 1} \circ  {j}_{n} \circ  {f}_{n} \circ  {g}_{n} \sim  {g}_{n + 1} \circ  {j}_{n}.
\]

Choose a specific homotopy \( {h}_{u}^{n} : {Y}_{n} \rightarrow  {X}_{n + 1} \) with \( {h}_{0}^{n} = {i}_{n}{g}_{n},{h}_{1}^{n} = {g}_{n + 1}{j}_{n} \) ; and define \( G : {Y}_{\sum } \rightarrow  {X}_{\sum } \) by the formula

\[
G\left( {y, n + t}\right)  = \left\{  \begin{array}{ll} \left( {{g}_{n}\left( y\right) , n + {2t}}\right) & 0 \leq  t \leq  \frac{1}{2} \\  \left( {{h}_{{2t} - 1}^{n}, n + 1}\right) & \frac{1}{2} \leq  t \leq  1. \end{array}\right.
\]

We will show that the composition \( G \circ  {f}_{\sum } : {X}_{\sum } \rightarrow  {X}_{\sum } \) . is a homotopy equivalence. Let \( {X}_{\sum }^{n} \) denote the subset of \( {X}_{\sum } \) consisting of all pairs \( \left( {x,\tau }\right) \) with \( \tau  \leq  n \) . (Thus \( {X}_{\sum }^{n} = {X}_{0} \times  \left\lbrack  {0,1}\right\rbrack   \cup  \cdots  \cup  {X}_{n - 1} \times  \left\lbrack  {n - 1, n}\right\rbrack   \cup  {X}_{n} \times  \left\lbrack  n\right\rbrack \) .) The composition \( G \circ  {f}_{\sum } \) carries

\( {X}_{\sum }^{n} \) into itself by a mapping which is homotopic to the identity. In fact \( {X}_{\sum }^{n} \) contains \( {X}_{n} \times  \left\lbrack  n\right\rbrack \) as deformation retract; and the mapping \( G \circ  {f}_{\sum } \) restricted to \( {X}_{n} \times  \left\lbrack  n\right\rbrack \) can be identified with \( {g}_{n} \circ  {f}_{n} \) , and hence is homotopic to the identity. Thus we can apply Case 1 to the sequence \( \left\{  {X}_{\sum }^{n}\right\} \) and conclude that \( G \circ  {f}_{\sum } \) is a homotopy equivalence.

This proves that \( {f}_{\sum } \) has a left homotopy inverse. A similar argument shows that \( {f}_{\sum } \circ  G : {Y}_{\sum } \rightarrow  {Y}_{\sum } \) . is a homotopy equivalence, so that \( {f}_{\sum } \) has a right homotopy inverse. This proves that \( {f}_{\sum } \) is a homotopy equivalence (compare page 20) and completes the proof of Theorem A.5.

Corollary A.6. Suppose that \( X \) is the homotopy direct limit of \( \left( {X}_{i}\right) \) . If each \( {X}_{i} \) has the homotopy type of a CW-complex, then X itself has the homotopy type of a CW-complex.

The proof is not difficult.
