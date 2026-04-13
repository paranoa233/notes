# 11.5 Euler Class and Euler Characteristic

The Euler characteristic of a finite complex \( K \) is defined as the alternating sum

\[
\chi \left( K\right)  = \sum {\left( -1\right) }^{k}\operatorname{rank}{\mathrm{H}}^{k}\left( K\right) ,
\]

using field coefficients. A familiar theorem asserts that this equal to the alternating sum

\[
\sum {\left( -1\right) }^{k}\text{ (number of }k\text{ -cells), }
\]

and hence is independent of the particular coefficient field that is used. (Compare [Dol95, pp. 105, 106].)

Corollary 11.12. If \( M \) is a smooth compact oriented manifold, then the Kronecker index \( \left\langle  {\mathrm{e}\left( {\tau }_{M}\right) ,\mu }\right\rangle \) , using rational or integer coefficients, is equal to the Euler characteristic \( \chi \left( M\right) \) . Similarly, for a non-oriented manifold, the Stiefel-Whitney number \( \left\langle  {{w}_{n}\left( {\tau }_{M}\right) ,\mu }\right\rangle   = {w}_{n}\left\lbrack  M\right\rbrack \) is congruent to \( \chi \left( M\right) \) modulo 2 .

Proof. By 11.3 and 11.15 the Euler class of the tangent bundle is given by

\[
\mathrm{e}\left( {\tau }_{M}\right)  = {\Delta }^{ * }\left( {u}^{\prime \prime }\right) .
\]

Using rational coefficients, we can substitute the formula

\[
{u}^{\prime \prime } = \sum {\left( -1\right) }^{\dim {b}_{i}}{b}_{i} \times  {b}_{i}^{\# },
\]

thus obtaining

\[
\mathrm{e}\left( {\tau }_{M}\right)  = \sum {\left( -1\right) }^{\dim {b}_{i}}{b}_{i} \cup  {b}_{i}^{\# }.
\]

Now applying the homomorphism \( \langle ,\mu \rangle \) to both sides, we obtain the required formula

\[
\left\langle  {\mathrm{e}\left( {\tau }_{M}\right) ,\mu }\right\rangle   = \sum {\left( -1\right) }^{\dim {b}_{i}} = \chi \left( M\right) .
\]

The mod 2 argument is completely analogous.
