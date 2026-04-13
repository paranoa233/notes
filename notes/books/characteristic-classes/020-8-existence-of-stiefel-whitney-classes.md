# 8 Existence of Stiefel-Whitney Classes

We now proceed to prove the existence of Stiefel-Whitney classes by giving a construction in terms of known operations. For any \( n \) -plane bundle \( \xi \) with total space \( E \) , base space \( B \) and projection map \( \pi \) , we denote by \( {E}_{0} \) the set of all non-zero elements of \( E \) , and by \( {F}_{0} \) the set of all non-zero elements of a typical fiber \( F = {\pi }^{-1}\left( b\right) \) . Clearly \( {F}_{0} = F \cap  {E}_{0} \) .

Using singular theory and one of several techniques (e.g. spectral sequences or that of \( \text{ § }{10}) \) we have that

\[
{\mathrm{H}}^{i}\left( {F,{F}_{0};\mathbb{Z}/2}\right)  = \left\{  \begin{array}{ll} 0 & \text{ for }i \neq  n \\  \mathbb{Z}/2 & \text{ for }i = n \end{array}\right.
\]

and that

\[
{\mathrm{H}}^{i}\left( {E,{E}_{0};\mathbb{Z}/2}\right)  \cong  \left\{  \begin{array}{ll} 0 & \text{ for }i < n \\  {\mathrm{H}}^{i - n}\left( {B;\mathbb{Z}/2}\right) & \text{ for }i \geq  n \end{array}\right.
\]

(This can be seen intuitively, though not rigorously, as follows: The unit \( n \) -cell is a deformation retract of \( {\mathbb{R}}^{n} \) and the unit \( \left( {n - 1}\right) \) -sphere is a deformation retract of \( \left( {{\mathbb{R}}^{n}\smallsetminus \{ 0\} }\right)  = {\mathbb{R}}_{0}^{n} \) . For \( B \) paracompact, we know that we can put a Euclidean metric on \( E \) . Then the subset \( {E}^{\prime } \) consisting of all vectors \( x \in  E \) with \( x \cdot  x \leq  1 \) is evidently a deformation retract of \( E \) . Similarly the set \( {E}^{\prime \prime } \) consisting of vectors \( x \in  E \) with \( x \cdot  x = 1 \) is a deformation retract of \( {E}_{0} \) . Hence \( {\mathrm{H}}^{ * }\left( {{E}^{\prime },{E}^{\prime \prime }}\right)  \cong  {\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right) \) . Now suppose that \( B \) is a cell complex, with a fine enough cell subdivision so that the restriction of \( \xi \) to each cell \( {c}^{k} \) is a trivial bundle. Then the inverse image of the \( k \) -cell \( {c}^{k} \) in \( {E}^{\prime } \) is a product cell of dimension \( n + k \) . Thus \( {E}^{\prime } \) can be obtained from the subset \( {E}^{\prime \prime } \) by adjoining cells of dimension \( \geq  n \) , one \( \left( {n + k}\right) \) -cell corresponding to each \( k \) -cell of \( B \) . It follows that \( {\mathrm{H}}^{i}\left( {{E}^{\prime },{E}^{\prime \prime }}\right)  = 0 \) for \( i < n \) . With a little faith, it follows also that \( {\mathrm{H}}^{n + k}\left( {{E}^{\prime },{E}^{\prime \prime }}\right)  \cong  {\mathrm{H}}^{k}\left( B\right) \) .)

Rigorously and more explicitly, the following statement will be proved in \( \text{ § }{10} \) . The coefficient group \( \mathbb{Z}/2 \) is to be understood.

Theorem 8.1. The group \( {\mathrm{H}}^{i}\left( {E,{E}_{0}}\right) \) is zero for \( i < n \) , and \( {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) contains a unique class \( u \) such that for each fiber \( F = {\pi }^{-1}\left( b\right) \) the restriction

\[
{\left. u\right| }_{\left( F,{F}_{0}\right) } \in  {\mathrm{H}}^{n}\left( {F,{F}_{0}}\right)
\]

is the unique non-zero class in \( {\mathrm{H}}^{n}\left( {F,{F}_{0}}\right) \) . Furthermore the correspondence \( x \mapsto  x \smile  u \) defines an isomorphism \( {\mathrm{H}}^{k}\left( E\right)  \rightarrow  {\mathrm{H}}^{k + n}\left( {E,{E}_{0}}\right) \) for every \( k \) . (We call \( u \) the fundamental cohomology class.)

On the other hand the projection \( \pi  : E \rightarrow  B \) certainly induces an isomorphism \( {\mathrm{H}}^{k}\left( B\right)  \rightarrow  {\mathrm{H}}^{k}\left( E\right) \) , since the zero cross-section embeds \( B \) as a deformation retract of \( E \) with retraction mapping \( \pi \) .

Definition. The Thom isomorphism \( \phi  : {\mathrm{H}}^{k}\left( B\right)  \rightarrow  {\mathrm{H}}^{k + n}\left( {E,{E}_{0}}\right) \) is defined to be the composition of the two isomorphisms

\[
{\mathrm{H}}^{k}\left( B\right) \overset{{\pi }^{ * }}{ \rightarrow  }{\mathrm{H}}^{k}\left( E\right) \overset{ \smile  u}{ \rightarrow  }{\mathrm{H}}^{k + n}\left( {E,{E}_{0}}\right) .
\]

Next we will make use of the Steenrod squaring operations in \( {\mathrm{H}}^{ * }\left( {E,{E}_{0}}\right) \) . These operations can be characterized by four basic properties, as follows. (Compare [SE62].) Again mod 2 coefficients are to be understood.

(1) For each pair \( X \supset  Y \) of spaces and each pair \( n, i \) of non-negative integers there is defined an additive homomorphism

\[
{\mathrm{{Sq}}}^{i} : {\mathrm{H}}^{n}\left( {X, Y}\right)  \rightarrow  {\mathrm{H}}^{n + i}\left( {X, Y}\right) .
\]

(This homomorphism is called "square upper i.")

(2) Naturality. If \( f : \left( {X, Y}\right)  \rightarrow  \left( {{X}^{\prime },{Y}^{\prime }}\right) \) then \( {\mathrm{{Sq}}}^{i} \circ  {f}^{ * } = {f}^{ * } \circ  {\mathrm{{Sq}}}^{i} \) .

(3) If \( a \in  {\mathrm{H}}^{n}\left( {X, Y}\right) \) , then \( {\mathrm{{Sq}}}^{0}\left( a\right)  = a,{\mathrm{{Sq}}}^{n}\left( a\right)  = a \smile  a \) , and \( {\mathrm{{Sq}}}^{i}\left( a\right)  = 0 \) for \( i > n \) . (Thus the most interesting squaring operations are those for which \( 0 < i < n \) .)

(4) The Cartan formula. The identity

\[
{\mathrm{{Sq}}}^{k}\left( {a \smile  b}\right)  = \mathop{\sum }\limits_{{i + j = k}}{\mathrm{{Sq}}}^{i}\left( a\right)  \smile  {\mathrm{{Sq}}}^{j}\left( b\right)
\]

is valid whenever \( a \smile  b \) is defined.

Using these squaring operations together with the Thom isomorphism \( \phi \) , the Stiefel-Whitney class \( {\mathrm{w}}_{i}\left( \xi \right)  \in  {\mathrm{H}}^{i}\left( B\right) \) can now be defined by Thom’s identity

\[
{\mathrm{w}}_{i}\left( \xi \right)  = {\phi }^{-1}{\operatorname{Sq}}^{i}\phi \left( 1\right) .
\]

In other words \( {\mathrm{w}}_{i}\left( \xi \right) \) is the unique cohomology class in \( {\mathrm{H}}^{i}\left( B\right) \) such that \( \phi \left( {{\mathrm{w}}_{i}\left( \xi \right) }\right)  = {\pi }^{ * }{\mathrm{w}}_{i}\left( \xi \right)  \smile  u \) is equal to \( {\operatorname{Sq}}^{i}\phi \left( 1\right)  = {\operatorname{Sq}}^{i}\left( u\right) \) .

For many purposes it is convenient to introduce the total squaring operation

\[
\mathrm{{Sq}}\left( a\right)  = a + {\mathrm{{Sq}}}^{1}\left( a\right)  + {\mathrm{{Sq}}}^{2}\left( a\right)  + \cdots  + {\mathrm{{Sq}}}^{n}\left( a\right)
\]

for \( a \in  {\mathrm{H}}^{n}\left( {X, Y}\right) \) . Note that the Cartan formula can now be expressed by the equation

\[
\operatorname{Sq}\left( {a \smile  b}\right)  = \operatorname{Sq}\left( a\right)  \smile  \operatorname{Sq}\left( b\right) .
\]

Similarly the corresponding equation for the Steenrod squares of a cross product becomes simply

\[
\operatorname{Sq}\left( {a \times  b}\right)  = \left( {\operatorname{Sq}\left( a\right) }\right)  \times  \left( {\operatorname{Sq}\left( b\right) }\right) .
\]

In terms of this total squaring operation, the total Stiefel-Whitney class of a vector bundle is clearly determined by the formula

\[
w\left( \xi \right)  = {\phi }^{-1}\operatorname{Sq}\phi \left( 1\right)  = {\phi }^{-1}\operatorname{Sq}\left( u\right)
\]
