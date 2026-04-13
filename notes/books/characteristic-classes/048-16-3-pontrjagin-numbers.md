# 16.3 Pontrjagin Numbers

Now consider a smooth, compact, oriented manifold \( {M}^{4n} \) . For each partition \( I = {i}_{1},\ldots ,{i}_{r} \) of \( n \) , the \( I \) -th Pontrjagin number \( {\mathrm{p}}_{I}\left\lbrack  {M}^{4n}\right\rbrack   = {\mathrm{p}}_{{i}_{1}}\cdots {\mathrm{p}}_{{i}_{r}}\left\lbrack  {M}^{4n}\right\rbrack \) is defined to be the integer

\[
\left\langle  {{\mathrm{p}}_{{i}_{1}}\left( {\tau }^{4n}\right) \cdots {\mathrm{p}}_{{i}_{r}}\left( {\tau }^{4n}\right) ,{\mu }_{4n}}\right\rangle  \text{ . }
\]

Here \( {\tau }^{4n} \) denotes the tangent bundle and \( {\mu }_{4n} \) the fundamental homology class.

As an example, the complex projective space \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) , with its complex structure forgotten, is a compact oriented manifold of real dimension \( {4n} \) . The Pontr-jagin numbers of this manifold are given by the formula

\[
{\mathrm{p}}_{{i}_{1}}\cdots {\mathrm{p}}_{{i}_{r}}\left\lbrack  {{\mathbb{P}}^{2n}\left( \mathbb{C}\right) }\right\rbrack   = \left( \begin{matrix} {2n} + 1 \\  {i}_{1} \end{matrix}\right) \cdots \left( \begin{matrix} {2n} + 1 \\  {i}_{r} \end{matrix}\right) ,
\]

as one easily verifies using 15.6.

If we reverse the orientation of a manifold \( {M}^{4n} \) , note that its Pontrjagin classes remain unchanged, but its fundamental homology class \( {\mu }_{4n} \) changes sign. Hence each Pontrjagin number

\[
{\mathrm{p}}_{{i}_{1}}\cdots {\mathrm{p}}_{{i}_{r}}\left\lbrack  {M}^{4n}\right\rbrack   = \left\langle  {{p}_{1}\cdots {\mathrm{p}}_{{i}_{r}},{\mu }_{4n}}\right\rangle
\]

also changes sign. Thus if some Pontrjagin number \( {\mathrm{p}}_{{i}_{1}}\cdots {\mathrm{p}}_{{i}_{r}}\left\lbrack  {M}^{4n}\right\rbrack \) is nonzero, then it follows that \( {M}^{4n} \) cannot possess any orientation reversing diffeomorphism.

As an example, the complex projective space \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) does not possess any orientation reversing diffeomorphism. (On the other hand, \( {\mathbb{P}}^{{2n} + 1}\left( \mathbb{C}\right) \) does have an orientation reversing diffeomorphism, arising from complex conjugation.)

This behavior of Pontrjagin numbers is in contrast to the behaviour of the Euler number \( \mathrm{e}\left\lbrack  {M}^{2n}\right\rbrack \) which is invariant under change of orientation. In fact the manifold \( {S}^{2n} \) , with \( \mathrm{e}\left\lbrack  {S}^{2n}\right\rbrack   \neq  0 \) , certainly does admit an orientation reserving diffeomorphism.

Furthermore, if some Pontrjagin number \( {\mathrm{p}}_{{i}_{1}}\cdots {\mathrm{p}}_{{i}_{r}}\left\lbrack  {M}^{4n}\right\rbrack \) is non-zero then, proceeding as in Lemma 14.9, we see that \( {M}^{4n} \) cannot be the boundary of any smooth, compact, oriented \( \left( {{4n} + 1}\right) \) -dimensional manifold with boundary. (Compare §17.) For example, the projective space \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) cannot be an oriented boundary. In fact the disjoint union \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right)  + \cdots  + {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) of any number of copies of \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) cannot be an oriented boundary, since the \( I \) -th Pontrjagin number of such a \( k \) -fold union is clearly just \( k \) times the \( I \) -th Pontrjagin number of \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) itself. Again this argument does not work for \( {\mathbb{P}}^{2n}\left( \mathbb{C}\right) \) . (In fact \( {\mathbb{P}}^{{2n} + 1}\left( \mathbb{C}\right) \) is the total space of a circle-bundle over a quaternion projective space, and hence is the boundary of an associated disk-bundle.)

Again the corresponding statement for Euler numbers is also false. Thus \( \mathrm{e}\left\lbrack  {S}^{2n}\right\rbrack   \neq  0 \) even though \( {S}^{2n} \) clearly bounds an oriented manifold. All of these remarks are due to Pontrjagin.
