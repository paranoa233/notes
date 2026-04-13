# 11.3 The Diagonal Cohomology Class in H^n(M x M)

We continue to assume either that \( M \) is oriented or that the coefficient ring \( \Lambda \) is \( \mathbb{Z}/2 \) , so that the fundamental class

\[
{u}^{\prime } \in  {\mathrm{H}}^{n}\left( {M \times  M, M \times  M - \Delta \left( M\right) }\right)
\]

is defined. Note that the restriction homomorphism

\[
{\mathrm{H}}^{n}\left( {M \times  M, M \times  M - \Delta \left( M\right) }\right)  \rightarrow  {\mathrm{H}}^{n}\left( {M \times  M}\right)
\]

maps \( {u}^{\prime } \) to a cohomology class \( {\left. {u}^{\prime }\right| }_{M \times  M} \) which, by definition, is "dual" to the diagonal submanifold of \( M \times  M \) .

Definition. This cohomology class \( {\left. {u}^{\prime }\right| }_{M \times  M} \) will be denoted briefly by \( {u}^{\prime \prime } \) , and called the diagonal cohomology class in \( {\mathrm{H}}^{n}\left( {M \times  M}\right) \) .

We would like to characterize this diagonal cohomology class more explicitly. First, a preliminary lemma which expresses algebraically the fact that \( {u}^{\prime \prime } \) is "concentrated" along the diagonal in \( M \times  M \) .

Lemma 11.8. For any cohomology class \( a \in  {\mathrm{H}}^{ * }\left( M\right) \) , the product \( \left( {a \times  1}\right)  \smile  {u}^{\prime \prime } \) is equal to \( \left( {1 \times  a}\right)  \smile  {u}^{\prime \prime } \) .

Proof. Let \( {N}_{\varepsilon } \) be a tubular neighborhood of the diagonal submanifold \( \Delta \left( M\right) \) in \( M \times  M \) . Evidently \( \Delta \left( M\right) \) is a deformation retract of \( {N}_{\varepsilon } \) . Define the two projection maps

\[
{p}_{1},{p}_{2} : M \times  M \rightarrow  M
\]

by \( {p}_{1}\left( {x, y}\right)  = x,{p}_{2}\left( {x, y}\right)  = y \) . Since \( {p}_{1} \) and \( {p}_{2} \) coincide on \( \Delta \left( M\right) \) , it follows that the restriction \( {\left. {p}_{1}\right| }_{{N}_{\varepsilon }} \) is homotopic to \( {\left. {p}_{2}\right| }_{{N}_{\varepsilon }} \) . Therefore the two cohomology classes \( {p}_{1}^{ * }\left( a\right)  = a \times  1 \) and \( {p}_{2}^{ * }\left( a\right)  = 1 \times  a \) have the same image under the restriction homomorphism \( {\mathrm{H}}^{i}\left( {M \times  M}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {N}_{\varepsilon }\right) \) . Now, using the commutative diagram

\[
{\mathrm{H}}^{i}\left( {M \times  M}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {N}_{\varepsilon }\right)
\]

\[
\downarrow   \sim  {u}^{\prime }\; \downarrow   \sim  {\left. {u}^{\prime }\right| }_{\left( {N}_{\varepsilon },{N}_{\varepsilon } - \Delta \left( M\right) \right) }
\]

\[
{\mathrm{H}}^{i + n}\left( {M \times  M, M \times  M - \Delta \left( M\right) }\right) \overset{ \cong  }{ \rightarrow  }{H}^{i + n}\left( {{N}_{\varepsilon },{N}_{\varepsilon } - \Delta \left( M\right) }\right)
\]

it follows that \( \left( {a \times  1}\right)  \smile  {u}^{\prime } = \left( {1 \times  a}\right)  \smile  {u}^{\prime } \) . Restricting to \( {\mathrm{H}}^{i + n}\left( {M \times  M}\right) \) , the conclusion follows.

We will make use of the slant product operation

\[
{\mathrm{H}}^{p + q}\left( {X \times  Y}\right)  \otimes  {\mathrm{H}}_{q}\left( Y\right)  \rightarrow  {\mathrm{H}}^{p}\left( X\right)
\]

with coefficients in \( \Lambda \) . In the special case where \( X \) and \( Y \) are finite complexes and \( \Lambda \) is a field, so that

\[
{\mathrm{H}}^{ * }\left( {X \times  Y}\right)  \cong  {\mathrm{H}}^{ * }\left( X\right)  \otimes  {\mathrm{H}}^{ * }\left( Y\right)
\]

this slant product can be defined quite easily as follows. Define a homomorphism

\[
{\mathrm{H}}^{ * }\left( X\right)  \otimes  {\mathrm{H}}^{ * }\left( Y\right)  \otimes  {\mathrm{H}}_{ * }\left( Y\right)  \rightarrow  {\mathrm{H}}^{ * }\left( X\right)
\]

by the formula \( a \otimes  b \otimes  \beta  \mapsto  a\langle b,\beta \rangle \) . Now, substituting \( {\mathrm{H}}^{ * }\left( {X \times  Y}\right) \) for \( {\mathrm{H}}^{ * }\left( X\right)  \otimes  {\mathrm{H}}^{ * }\left( Y\right) \) , we have the required operation

\[
{\mathrm{H}}^{ * }\left( {X \times  Y}\right)  \otimes  {\mathrm{H}}_{ * }\left( Y\right)  \rightarrow  {\mathrm{H}}^{ * }\left( X\right)
\]

which is denoted by \( p \otimes  \beta  \mapsto  p/\beta \) . This operation satisfies and is characterized by the identity

\[
\left( {a \times  b}\right) /\beta  = a\langle b,\beta \rangle .
\]

For each fixed \( \beta  \in  {\mathrm{H}}_{ * }\left( Y\right) \) , note that the homomorphism \( p \mapsto  p/\beta \) is left \( {\mathrm{H}}^{ * }\left( X\right) \) - linear in the sense that \( \left( {\left( {a \times  1}\right)  \smile  p}\right) /\beta  = a \smile  \left( {p/\beta }\right) \) for every \( \mathrm{a} \in  {\mathrm{H}}^{ * }\left( X\right) \) and every \( p \in  {\mathrm{H}}^{ * }\left( {X \times  Y}\right) \) .

For the definition of slant product in general, the reader is referred to [Spa81] or [Dol95].

Lemma 11.9. Suppose that \( M \) is compact, so that the fundamental homology class \( \mu  \in  {\mathrm{H}}_{n}\left( M\right) \) is defined. Then the diagonal cohomology class \( {u}^{\prime \prime } \in  {\mathrm{H}}^{n}\left( {M \times  M}\right) \) and the fundamental homology class \( \mu \) are related by the identity \( {u}^{\prime \prime }/\mu  = 1 \in  {\mathrm{H}}^{0}\left( M\right) . \)

We are assuming field coefficients, although the proof would actually go through with any coefficient ring, in the oriented case.

Proof. For any \( x \in  M \) we will compute the image of \( {u}^{\prime \prime }/\mu \) under the restriction homomorphism \( {\mathrm{H}}^{0}\left( M\right)  \rightarrow  {\mathrm{H}}^{0}\left( x\right)  \cong  \Lambda \) . We will make use of the commutative diagram

![bo_d7du9galb0pc73deir9g_133_662_548_407_192_0.jpg](images/bo_d7du9galb0pc73deir9g_133_662_548_407_192_0.jpg)

Note that the left hand vertical arrow maps the cohomology class \( {u}^{\prime \prime } \) to \( 1 \times  {i}_{x}^{ * }\left( {u}^{\prime \prime }\right) \) , where

\[
{i}_{X} : M \rightarrow  M \times  M
\]

denotes the embedding \( y \mapsto  \left( {x, y}\right) \) . Using the identity \( \left( {a \times  b}\right) /\mu  = a\langle b,\mu \rangle \) , it follows that \( {\left. \left( {u}^{\prime \prime }/\mu \right) \right| }_{x} \) is equal to the Kronecker index \( \left\langle  {{i}_{x}\left( {u}^{\prime \prime }\right) ,\mu }\right\rangle \) multiplied by \( 1 \in  {\mathrm{H}}^{0}\left( x\right) \) .

As constructed in Appendix A, the fundamental homology class \( \mu \) is uniquely characterized by the property that for each \( x \in  M \) the natural homomorphism

\[
{\mathrm{H}}_{n}\left( M\right)  \rightarrow  {\mathrm{H}}_{n}\left( {M, M - x}\right)
\]

maps \( \mu \) to the preferred generator \( {\mu }_{x} \) . Making use of the mappings

![bo_d7du9galb0pc73deir9g_133_551_1388_630_176_0.jpg](images/bo_d7du9galb0pc73deir9g_133_551_1388_630_176_0.jpg)

where \( {j}_{x} \) also sends \( y \) to \( \left( {x, y}\right) \) , it follows from this defining property of \( \mu \) that the Kronecker index \( \left\langle  {{i}_{x}^{ * }\left( {u}^{\prime \prime }\right) ,\mu }\right\rangle   = {\left\langle  {j}_{x}^{ * }\left( {u}^{\prime }\right) { \mid  }_{M},\mu \right\rangle  }^{\text{ is }} \) equal to \( \left\langle  {{j}_{x}^{ * }\left( {u}^{\prime }\right) ,{\mu }_{x}}\right\rangle \) . Since this equals 1 by lemma 11.7, we have proved that

\[
{\left. \left( {u}^{\prime \prime }/\mu \right) \right| }_{x} = 1 \in  {\mathrm{H}}^{0}\left( x\right)
\]

This is true for every \( x \) , so it clearly follows that \( {u}^{\prime \prime }/\mu \) is equal to the identity element of \( {\mathrm{H}}^{0}\left( M\right) \) .
