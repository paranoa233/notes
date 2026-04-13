# 11.4 Poincaré Duality and the Diagonal Class

Let \( M \) be a compact smooth manifold. We will study the cohomology of \( M \) with coefficients in a field \( \Lambda \) , continuing to assume either that \( M \) is oriented or that \( \Lambda  = \mathbb{Z}/2 \) .

Theorem 11.10 (Duality Theorem). To each basis \( {b}_{1},\ldots ,{b}_{r} \) for \( {\mathrm{H}}^{ * }\left( M\right) \) there corresponds a dual basis \( {b}_{1}^{\# },\ldots ,{b}_{r}^{\# } \) for \( {\mathrm{H}}^{ * }\left( M\right) \) , satisfying the identity

\[
\left\langle  {{b}_{i} \smile  {b}_{j}^{\# },\mu }\right\rangle   = \left\{  \begin{array}{ll} 1 & i = j, \\  0 & i \neq  j \end{array}\right.
\]

It follows as a corollary that the rank of the vector space \( {\mathrm{H}}^{k}\left( M\right) \) is equal to the rank of \( {\mathrm{H}}^{n - k}\left( M\right) \) . For if a basis element \( {b}_{i} \) has dimension \( k \) then the dual basis element \( {b}_{i}^{\# } \) must have dimension \( n - k \) . In fact, it follows that the vector space \( {\mathrm{H}}^{k}\left( M\right) \) is isomorphic to the dual vector space \( {\operatorname{Hom}}_{\Lambda }\left( {{\mathrm{H}}^{k}\left( M\right) ,\Lambda }\right) \) , using the correspondence \( a \mapsto  {h}_{a} \) where \( {h}_{a}\left( b\right)  = \langle a \smile  b,\mu \rangle \) . (For other formulations of Poincaré duality, see 11-B and Appendix A, as well as [Spa81], [Dol95].)

While proving 11.10, we will simultaneuously give a precise description of the cohomology class \( {u}^{\prime \prime } \in  {\mathrm{H}}^{n}\left( {M \times  M}\right) \) .

Theorem 11.11. With \( \left\{  {b}_{i}\right\} \) and \( \left\{  {b}_{i}^{\# }\right\} \) as above, the diagonal cohomology class \( {u}^{\prime \prime } \) is equal to

\[
\mathop{\sum }\limits_{{i = 1}}^{r}{\left( -1\right) }^{\dim {b}_{i}}{b}_{i} \times  {b}_{i}^{\# }
\]

Proof of 11.10 and 11.11. Using the Künneth formula,

\[
{\mathrm{H}}^{ * }\left( {M \times  M}\right)  \cong  {\mathrm{H}}^{ * }\left( M\right)  \otimes  {\mathrm{H}}^{ * }\left( M\right) ,
\]

it follows easily that the diagonal class can be represented by a \( r \) -fold sum

\[
{u}^{\prime \prime } = {b}_{1} \times  {c}_{1} + \cdots  + {b}_{r} \times  {c}_{r},
\]

where \( {c}_{1},\ldots ,{c}_{r} \) are certain well-defined cohomology classes in \( {\mathrm{H}}^{ * }\left( M\right) \) with

\[
\dim {b}_{i} + \dim {c}_{i} = n
\]

Let us apply the homomorphism \( /\mu \) to both sides of the identity

\[
\left( {a \times  1}\right)  \smile  {u}^{\prime \prime } = \left( {1 \times  a}\right)  \smile  {u}^{\prime \prime }.
\]

On the left side, using the left linearity of the slant product, we obtain

\[
\left( {\left( {a \times  1}\right)  \smile  {u}^{\prime \prime }}\right) /\mu  = a \smile  \left( {{u}^{\prime \prime }/\mu }\right)  = a.
\]

On the right side, substituting \( \sum {b}_{j} \times  {c}_{j} \) for \( {u}^{\prime \prime } \) , we obtain

\[
\sum {\left( -1\right) }^{\dim a\dim {b}_{j}}\left( {{b}_{j} \times  \left( {a \smile  {c}_{j}}\right) }\right) /\mu  = \sum {\left( -1\right) }^{\dim a\dim {b}_{j}}{b}_{j}\left\langle  {a \smile  {c}_{j},\mu }\right\rangle  .
\]

Hence this last expression must be equal to \( a \) . Substituting \( {b}_{i} \) for \( a \) , it follows that the coefficient

\[
{\left( -1\right) }^{\dim a\dim {b}_{j}}\left\langle  {{b}_{i} \smile  {c}_{j},\mu }\right\rangle
\]

of \( {b}_{j} \) must be +1 for \( i = j \) , and 0 for \( i \neq  j \) . Setting \( {b}_{i}^{\# } = {\left( -1\right) }^{\dim {b}_{i}}{c}_{i} \) , the conclusions follow easily.
