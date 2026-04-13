# Chapter 4 Examples

Based on lecture notes by

M. Spivak and R. Wells

As an application of the theorems of Chapter 3 we shall prove:

Theorem 4.1 (Reeb). If \( M \) is a compact manifold and \( f \) is a differentiable function on \( M \) with only two critical points, both of which are non-degenerate, then \( M \) is homeomorphic to a sphere.

![bo_d7du90alb0pc73deir8g_32_632_1046_408_385_0.jpg](images/bo_d7du90alb0pc73deir8g_32_632_1046_408_385_0.jpg)

Proof. This follows from Theorem 3.1 together with the Lemma of Morse (Lemma 8.3). The two critical points must be the minimum and maximum points. Say that \( f\left( p\right)  = 0 \) is the minimum and \( f\left( q\right)  = 1 \) is the maximum. If \( \varepsilon \) is small enough then the sets \( {M}^{\varepsilon } = {f}^{-1}\left\lbrack  {0,\varepsilon }\right\rbrack \) and \( {f}^{-1}\left\lbrack  {1 - \varepsilon ,1}\right\rbrack \) are closed \( n \) -cells by Lemma 8.3. But \( {M}^{\varepsilon } \) is homeomorphic to \( {M}^{1 - \varepsilon } \) by Theorem 3.1. Thus \( M \) is the union of two closed \( n \) -cells, \( {M}^{1 - \varepsilon } \) and \( {f}^{-1}\left\lbrack  {1 - \varepsilon ,1}\right\rbrack \) , matched along their common boundary. It is now easy to construct a homeomorphism between \( M \) and \( {\mathbb{S}}^{n} \) .

Remark. The theorem remains true even if the critical points are degenerate. However, the proof is more difficult. (Compare Milnor, Differential topology, in [Mil64, Theorem 1]; or [Ros60, Lemma 1].)

Remark. It is not true that \( M \) must be diffeomorphic to \( {\mathbb{S}}^{n} \) with its usual differentiable structure.(Compare [Mil56]. In this paper a 7-sphere with a non-standard differentiable structure is proved to be topologically \( {\mathbb{S}}^{7} \) by finding a function on it with two non-degenerate critical points.)

As another application of the previous theorems we note that if an \( n \) -manifold has a non-degenerate function on it with only three critical points then they have index \( 0, n \) and \( \frac{n}{2} \) (by Poincaré duality), and the manifold has the homotopy type of an \( \frac{n}{2} \) -sphere with an \( n \) -cell attached. See [EK62]. Such a function exists for example on the real or complex projective plane.

Let \( {\mathbb{{CP}}}_{n} \) be complex projective \( n \) -space. We will think of \( {\mathbb{{CP}}}_{n} \) as equivalence classes of \( \left( {n + 1}\right) \) -tuples \( \left( {{z}_{1},\ldots ,{z}_{n}}\right) \) of complex numbers, with \( \sum {\left| {z}_{j}\right| }^{2} = 1 \) . Denote the equivalence class of \( \left( {{z}_{1},\ldots ,{z}_{n}}\right) \) by \( \left( {{z}_{0} : {z}_{1} : \cdots  : {z}_{n}}\right) \) .

Define a real valued function \( f \) on \( {\mathbb{{CP}}}_{n} \) by the identity

\[
f\left( {{z}_{0} : {z}_{1} : \cdots  : {z}_{n}}\right)  = \sum {c}_{j}{\left| {z}_{j}\right| }^{2}
\]

where \( {c}_{0},{c}_{1},\ldots ,{c}_{n} \) are distinct real constants. In order to determine the critical points of \( f \) , consider the following local coordinate system. Let \( {U}_{0} \) be the set of \( \left( {{z}_{0} : {z}_{1} : \cdots  : {z}_{n}}\right) \) with \( {z}_{0} \neq  0 \) , and set

\[
\left| {z}_{0}\right| \frac{{z}_{j}}{{z}_{0}} = {x}_{j} + {iy}
\]

Then

\[
{x}_{1},{y}_{1},\ldots ,{x}_{n},{y}_{n} : {U}_{0} \rightarrow  \mathbf{R}
\]

are the required coordinate functions, mapping \( {U}_{0} \) diffeomorphically onto the open unit ball in \( {\mathbf{R}}^{2n} \) . Clearly

\[
{\left| {z}_{j}\right| }^{2} = {x}_{j}^{2} + {y}_{j}^{2},\;{\left| {z}_{0}\right| }^{2} = 1 - \sum \left( {{x}_{j}^{2} + {y}_{j}^{2}}\right) ,
\]

so that

\[
f = {c}_{0} + \mathop{\sum }\limits_{{j = 1}}^{n}\left( {{c}_{j} - {c}_{0}}\right) \left( {{x}_{j}^{2} + {y}_{j}^{2}}\right)
\]

throughout the coordinate neighborhood \( {U}_{0} \) . Thus the only critical point of \( f \) within \( {U}_{0} \) lies at the center point

\[
{p}_{0} = \left( {1 : 0 : 0 : \cdots  : 0}\right)
\]

of the coordinate system. At this point \( f \) is non-degenerate; and has index equal to twice the number of \( j \) with \( {c}_{j} < {c}_{0} \) .

Similarly one can consider other coordinate systems centered at the points

\[
{p}_{1} = \left( {0 : 1 : 0 : \cdots  : 0}\right) ,\ldots ,{p}_{n} = \left( {0 : 0 : \cdots  : 0 : 1}\right) .
\]

It follows that \( {p}_{0},{p}_{1},\ldots ,{p}_{n} \) are the only critical points of \( f \) . The index of \( f \) at \( {p}_{k} \) is equal to twice the number of \( j \) with \( {c}_{j} < {c}_{k} \) . Thus every possible even index between 0 and \( {2n} \) occurs exactly once. By Theorem 3.3:

\( {\mathbb{{CP}}}_{n} \) has the homotopy type of a CW-complex of the form

\[
{\mathrm{e}}^{0} \cup  {e}^{2} \cup  {\mathrm{e}}^{4} \cup  \cdots  \cup  {\mathrm{e}}^{2n}\text{ . }
\]

It follows that the integral homology groups of \( \mathbb{C}{\mathbf{P}}_{n} \) are given by

\[
{\mathrm{H}}_{i}\left( {{\mathbb{{CP}}}_{n};\mathbb{Z}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ for }i = 0,2,4,\ldots ,{2n} \\  0 & \text{ for other values of }i \end{array}\right.
\]
