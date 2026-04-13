# 16.2 Chern Numbers

Let \( {K}^{n} \) be a compact complex manifold of complex dimension \( n \) . Then for each partition \( I = {i}_{1},\ldots ,{i}_{r} \) of \( n \) , the \( I \) -th Chern number

\[
{\mathrm{c}}_{i}\left\lbrack  {K}^{n}\right\rbrack   = {\mathrm{c}}_{{i}_{1}}\cdots {\mathrm{c}}_{{i}_{r}}\left\lbrack  {K}^{n}\right\rbrack
\]

is defined to be the integer

\[
\left\langle  {{\mathrm{c}}_{{i}_{1}}\left( {\tau }^{n}\right) \ldots {\mathrm{c}}_{{i}_{r}}\left( {\tau }^{n}\right) ,{\mu }_{2n}}\right\rangle  \text{ . }
\]

Here \( {\tau }^{n} \) denotes the tangent bundle of \( {K}^{2n} \) , and \( {\mu }_{2n} \) denotes the fundamental homology class determined by the preferred orientation. We adopt the convention that \( {\mathrm{c}}_{I}\left\lbrack  {K}^{n}\right\rbrack \) is zero if \( I \) is a partition of some integer other than \( n \) .

As an example, for the complex projective space \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) , since \( {\mathrm{c}}_{i}\left( {\tau }^{n}\right)  = \left( \begin{matrix} n + 1 \\  i \end{matrix}\right) {a}^{i} \) and \( \left\langle  {{a}^{n},{\mu }_{2n}}\right\rangle   =  + 1 \) by Theorem 14.10, we have the formula

\[
{\mathrm{c}}_{{i}_{1}}\cdots {\mathrm{c}}_{{i}_{r}}\left\lbrack  {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right\rbrack   = \left( \begin{matrix} n + 1 \\  {i}_{1} \end{matrix}\right) \cdots \left( \begin{matrix} n + 1 \\  {i}_{r} \end{matrix}\right)
\]

for any partition \( {i}_{1},\ldots ,{i}_{r} \) of \( n \) .

A complex 1-dimensional manifold \( {K}^{1} \) has just one Chern number, namely the Euler characteristic \( {\mathrm{c}}_{1}\left\lbrack  {K}^{1}\right\rbrack \) . For a complex 2-manifold there are two Chern numbers, namely \( {\mathrm{c}}_{1}{\mathrm{c}}_{1}\left\lbrack  {K}^{2}\right\rbrack \) and the Euler characteristic \( {\mathrm{c}}_{2}\left\lbrack  {K}^{2}\right\rbrack \) . In general, a complex \( n \) -manifold has \( p\left( n\right) \) Chern numbers, where \( p\left( n\right) \) is the number of distinct partitions of \( n \) . (Compare p. 88.) We will see in 16.7 that these \( p\left( n\right) \) Chern numbers are linearly independent; that is there is no linear relation between them which is satisfied for all complex \( n \) -manifolds.

There is another way of thinking about Chern classes which is important for many purposes. Note that the cohomology group \( {\mathrm{H}}^{2n}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right) \) is free abelian of rank \( p\left( n\right) \) . The products \( {\mathrm{c}}_{{i}_{1}}\left( {\gamma }^{n}\right) \ldots {\mathrm{c}}_{{i}_{r}}\left( {\gamma }^{n}\right) \) , where \( {i}_{1},\ldots ,{i}_{r} \) ranges over all partitions of \( n \) , form a basis for this group. For any complex manifold \( {K}^{n} \) the tangent bundle \( {\tau }^{n} \) is "classified" by a map

\[
f : {K}^{n} \rightarrow  {\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right)
\]

with \( {f}^{ * }\left( {\gamma }^{n}\right)  \cong  {\tau }^{n} \) . Using this classifying map \( f \) , the fundamental homology class \( {\mu }_{2n} \) of \( {K}^{n} \) gives rise to a homology class \( {f}_{ * }\left( {\mu }_{2n}\right) \) in the free abelian group \( {\mathrm{H}}_{2n}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right) \) of rank \( p\left( n\right) \) . To identify this homology class \( {f}_{ * }\left( {\mu }_{2n}\right) \) , we only need to compute the \( p\left( n\right) \) Kronecker indices

\[
\left\langle  {{\mathrm{c}}_{{i}_{1}}\left( {\gamma }^{n}\right) \ldots {\mathrm{c}}_{{i}_{r}}\left( {\gamma }^{n}\right) ,{f}_{ * }\left( {\mu }_{2n}\right) }\right\rangle  ,
\]

since the products \( {\mathrm{c}}_{{i}_{1}}\left( {\gamma }^{n}\right) \ldots {\mathrm{c}}_{{i}_{r}}\left( {\gamma }^{n}\right) \) range over a basis for the corresponding cohomology group. But each such Kronecker index is equal to the Chern number

\[
\left\langle  {{f}^{ * }\left( {{\mathrm{c}}_{{i}_{1}}\left( {\gamma }^{n}\right) \ldots {\mathrm{c}}_{{i}_{r}}\left( {\gamma }^{n}\right) }\right) ,{\mu }_{2n}}\right\rangle   = {\mathrm{c}}_{{i}_{1}}\cdots {\mathrm{c}}_{{i}_{r}}\left\lbrack  {K}^{n}\right\rbrack  .
\]

We see from this approach that it is not necessary to use the basis \( \left\{  {{\mathrm{c}}_{{i}_{1}}\left( {\gamma }^{n}\right) \ldots {\mathrm{c}}_{{i}_{r}}\left( {\gamma }^{n}\right) }\right\} \) for \( {\mathrm{H}}^{2n}\left( {{\mathrm{{Gr}}}_{n}\left( {\mathbb{C}}^{\infty }\right) ;\mathbb{Z}}\right) \) . Any other basis would serve equally well. Later we will make use of a quite different basis for this group.
