# 16.5 A Product Formula

Let \( \omega \) be a complex \( n \) -plane bundle with base space \( B \) and with total Chern class \( \mathrm{c} = 1 + {\mathrm{c}}_{1} + \ldots  + {\mathrm{c}}_{n} \) . For any \( k \geq  0 \) and any partition \( I \) of \( k \) the cohomology class

\[
{s}_{I}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{k}}\right)  \in  {\mathrm{H}}^{2k}\left( {B;\mathbb{Z}}\right)
\]

will be denoted briefly by the symbol \( {s}_{I}\left( \mathrm{c}\right) \) or \( {s}_{I}\left( {\mathrm{c}\left( \omega \right) }\right) \) .

Lemma 16.2 (Thom). The characteristic class \( {s}_{I}\left( {\mathrm{c}\left( {\omega  \oplus  {\omega }^{\prime }}\right) }\right) \) of a Whitney sum is equal to

\[
\mathop{\sum }\limits_{{{JK} = I}}{s}_{J}\left( {\mathrm{c}\left( \omega \right) }\right) {s}_{K}\left( {\mathrm{c}\left( {\omega }^{\prime }\right) }\right) ,
\]

to be summed over all partitions \( J \) and \( K \) with juxtaposition \( {JK} \) equal to \( I \) .

As an example, since the single element partition of \( k \) can be expressed as a juxtaposition only in two trivial ways, we obtain the following.

Corollary 16.3. The characteristic class \( {s}_{k}\left( {\mathrm{c}\left( {\omega  \oplus  {\omega }^{\prime }}\right) }\right) \) of a Whitney sum is equal to \( {s}_{k}\left( {\mathrm{c}\left( \omega \right) }\right)  + {s}_{k}\left( {\mathrm{c}\left( {\omega }^{\prime }\right) }\right) \) .

Proof of 16.2. Consider a polynomial ring \( \mathbb{Z}\left\lbrack  {{t}_{1},\ldots ,{t}_{2n}}\right\rbrack \) in \( {2n} \) indeterminates, and let \( {\omega }_{k} \) [respectively \( {\sigma }_{k}^{\prime } \) ] be the \( k \) -th elementary symmetric function of the indeterminates \( {t}_{1},\ldots ,{t}_{n} \) [respecitvely \( {t}_{n + 1},\ldots ,{t}_{2n} \) ]. Then defining

\[
{\sigma }_{k}^{\prime \prime } = \mathop{\sum }\limits_{{i = 0}}^{k}{\sigma }_{i}{\sigma }_{k - i}^{\prime }
\]

it is clear that \( {\sigma }_{k}^{\prime \prime } \) is equal to the \( k \) -th elementary symmetric function of \( {t}_{1},\ldots ,{t}_{2n} \) . We will verify the identity

\[
{s}_{I}\left( {{\sigma }_{1}^{\prime \prime },\ldots ,{\sigma }_{k}^{\prime \prime }}\right)  = \mathop{\sum }\limits_{{{JK} = I}}{s}_{J}\left( {{\sigma }_{1},{\sigma }_{2},\ldots }\right) {s}_{K}\left( {{\sigma }_{1}^{\prime },{\sigma }_{2}^{\prime },\ldots }\right)
\]

for any partition \( I = {i}_{1},\ldots ,{i}_{r} \) of \( k \) . Since the classes \( {\omega }_{1},\ldots ,{\omega }_{k},{\omega }_{1}^{\prime },\ldots ,{\omega }_{k}^{\prime } \) are algebraically independent (assuming as we may that \( k \leq  n \) ), this identity together with the product theorem for Chern classes will clearly complete the proof.

By definition, the element

\[
{s}_{I}\left( {{\omega }_{1}^{\prime \prime },\ldots ,{\omega }_{k}^{\prime \prime }}\right)  \in  \mathbb{Z}\left\lbrack  {{t}_{1},\ldots ,{t}_{2m}}\right\rbrack
\]

is equal to the sum of all monomials which can be written in the form \( {t}_{{\alpha }_{1}}^{{i}_{1}}\ldots {t}_{{\alpha }_{r}}^{{i}_{r}} \) , with \( {\alpha }_{1},\ldots ,{\alpha }_{r} \) distinct numbers between 1 and \( {2n} \) . For each such monomial let \( J \) [respectively \( K \) ] be the partition formed by those exponents \( {i}_{q} \) such that

\( 1 \leq  {\alpha }_{q} \leq  n \) [respectively \( n + 1 \leq  {\alpha }_{q} \leq  {2n} \) ]. The sum of all terms corresponding to a given decomposition \( {JK} = I \) is clearly equal to

\[
{s}_{J}\left( {{\sigma }_{1},{\sigma }_{2},\ldots }\right) {s}_{K}\left( {{\sigma }_{1}^{\prime },{\sigma }_{2}^{\prime },\ldots }\right) .
\]

Since every such decomposition occurs, this completes the proof.

Now consider a compact complex manifold \( {K}^{n} \) of complex dimension \( n \) . For each partition \( I \) of \( n \) the notation \( {s}_{I}\left( \mathrm{c}\right) \left\lbrack  {K}^{n}\right\rbrack \) , or briefly \( {s}_{I}\left\lbrack  {K}^{n}\right\rbrack \) , will stand for the characteristic number

\[
\left\langle  {{s}_{I}\left( {\mathrm{c}\left( {\tau }^{n}\right) }\right) ,{\mu }_{2n}}\right\rangle   \in  \mathbb{Z}.
\]

This characteristic number is of course equal to a suitable linear combination of Chern numbers.

Corollary 16.4. The characteristic number \( {s}_{I}\left\lbrack  {{K}^{m} \times  {L}^{n}}\right\rbrack \) of a product of complex manifolds is equal to

\[
\mathop{\sum }\limits_{{{I}_{1}{I}_{2} = I}}{s}_{{I}_{1}}\left\lbrack  {K}^{m}\right\rbrack  {s}_{{I}_{2}}\left\lbrack  {L}^{n}\right\rbrack
\]

to be summed over all partitions \( {I}_{1} \) of \( m \) and \( {I}_{2} \) of \( n \) with juxtaposition \( {I}_{1}{I}_{2} \) equal to \( I \) .

Proof. For the tangent bundle of \( {K}^{m} \times  {L}^{n} \) splits as a Whitney sum

\[
\tau  \times  {\tau }^{\prime } \cong  \left( {{\pi }_{1}^{ * }\tau }\right)  \oplus  \left( {{\pi }_{2}^{ * }{\tau }^{\prime }}\right)
\]

where \( {\pi }_{1} \) and \( {\pi }_{2} \) are the projection maps onto the two factors. Hence the characteristic number

\[
\left\langle  {{s}_{I}\left( {\tau  \times  {\tau }^{\prime }}\right) ,{\mu }_{2n} \times  {\mu }_{2n}^{\prime }}\right\rangle
\]

is equal to

\[
\mathop{\sum }\limits_{{{I}_{1}{I}_{2} = I}}\left\langle  {{s}_{{I}_{1}}\left( \tau \right) ,{\mu }_{2m}}\right\rangle  \left\langle  {{s}_{{I}_{2}}\left( {\tau }^{\prime }\right) ,{\mu }_{2n}^{\prime }}\right\rangle  .
\]

There are no signs in this formula, since these classes are all even dimensional.

As a special case, we clearly have the following.

Corollary 16.5. For any product \( {K}^{m} \times  {L}^{n} \) of complex manifolds of dimensions \( m, n \neq  0 \) , the characteristic number \( {s}_{m + n}\left\lbrack  {{K}^{m} \times  {L}^{n}}\right\rbrack \) is zero.

This corollary suggests the importance of the characteristic number \( {s}_{m}\left\lbrack  {K}^{m}\right\rbrack \) . Here is an example to show that this characteristic number is not always zero.

Examples 16.6. For the complex projective space \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) , since \( \mathrm{c}\left( \tau \right)  = {\left( 1 + a\right) }^{n + 1} \) it follows that \( {\mathrm{c}}_{k}\left( \tau \right) \) is equal to the \( k \) -th elementary symmetric function of \( n + 1 \) copies of \( a \) . Therefore \( {s}_{k}\left( {{\mathrm{c}}_{1},\ldots ,{\mathrm{c}}_{k}}\right) \) is equal to the sum of \( n + 1 \) copies of \( {a}^{k} \) , that is

\[
{s}_{k} = \left( {n + 1}\right) {a}^{k}.
\]

Taking \( k = n \) , it follows that

\[
{s}_{n}\left\lbrack  {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right\rbrack   = n + 1 \neq  0.
\]

Thus \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) cannot be expressed non-trivially as a product of complex manifolds.

Completely analogous formulas are true for Pontrjagin classes and Pontrjagin numbers. If \( \xi \) is a real vector bundle over \( B \) , then for any partition \( I \) of \( n \) the characteristic classes

\[
{s}_{I}\left( {{\mathrm{p}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{p}}_{n}\left( \xi \right) }\right)  \in  {\mathrm{H}}^{4n}\left( {B;\mathbb{Z}}\right)
\]

is denoted briefly by \( {s}_{I}\left( {\mathrm{p}\left( \xi \right) }\right) \) . The congruence

\[
{s}_{I}\left( {\mathrm{p}\left( {\xi  \oplus  {\xi }^{\prime }}\right) }\right)  = \mathop{\sum }\limits_{{{JK} = I}}{s}_{J}\left( {\mathrm{p}\left( \xi \right) }\right) {s}_{K}\left( {\mathrm{p}\left( {\xi }^{\prime }\right) }\right)
\]

modulo elements of order 2 clearly follows from the proof of 16.2. Hence there is a corresponding equality

\[
{s}_{I}\left( \mathrm{p}\right) \left\lbrack  {M \times  N}\right\rbrack   = \mathop{\sum }\limits_{{{JK} = I}}{s}_{J}\left( \mathrm{p}\right) \left\lbrack  M\right\rbrack  {s}_{K}\left( \mathrm{p}\right) \left\lbrack  N\right\rbrack
\]

for characterisitc numbers. In particular, these characteristic numbers of \( M \times  N \) are zero unless the dimensions of \( M \) and \( N \) are divisible by 4 .
