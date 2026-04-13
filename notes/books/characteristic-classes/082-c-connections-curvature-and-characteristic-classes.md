# C Connections, Curvature and Characteristic Classes

This appendix will outline the Chern-Weil description of Characteristic classes with real or complex coefficients in terms of curvature forms. (Compare [Che48] or [BC65, Section 2].) We will assume that the reader is familiar with the rudiements of exterior differential calculus and de Rham cohomology, as developed for example in [War13]. However our sign conventions, as described in Appendix A, are different from those of Warner and other authors. We will return to this point later.

We begin with the case of a complex vector bundle. Let \( \zeta \) be a smooth complex \( n \) -plane bundle with smooth base space \( M \) , and let

\[
{\tau }_{\mathbb{C}}^{ * } = {\operatorname{Hom}}_{\mathbb{R}}\left( {\tau ,\mathbb{C}}\right)
\]

be the complexified dual tangent bundle of \( M \) . Then the (complex) tensor product \( {\tau }_{\mathbb{C}}^{ * } \otimes  \zeta \) is also a complex vector bundle over \( M \) . The vector space of smooth sections of this bundle will be denoted by \( {C}^{\infty }\left( {{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right) \) .

Definition. A connection on \( \zeta \) is a \( \mathbb{C} \) -linear mapping

\[
\nabla  : {C}^{\infty }\left( \zeta \right)  \rightarrow  {C}^{\infty }\left( {{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right)
\]

which satisifies the Leibniz formula

\[
\nabla \left( {fs}\right)  = \mathrm{d}f \otimes  s + f\nabla \left( s\right)
\]

for every \( s \in  {C}^{\infty }\left( \zeta \right) \) and every \( f \in  {C}^{\infty }\left( {M,\mathbb{C}}\right) \) . The image \( \nabla \left( s\right) \) is called the covariant derivative of \( s \) .

The basic properties of connections can be outlined as follows. First note that the correspondence \( s \mapsto  \nabla \left( s\right) \) decreases supports. That is, if the section \( s \) vanishes throughout an open subset \( U \subset  M \) then \( \nabla \left( s\right) \) vanishes throughout \( U \) also. For given \( x \in  U \) we can choose a smooth function \( f \) which vanishes outside \( U \) and is identically 1 near \( x \) . The identity

\[
\mathrm{d}f \otimes  s + f\nabla \left( s\right)  = \nabla \left( {fs}\right)  = 0,
\]

evaluated at \( x \) , shows that \( \nabla \left( s\right) \) vanishes at \( x \) .

Remark. A linear mapping \( L : {C}^{\infty }\left( \zeta \right)  \rightarrow  {C}^{\infty }\left( \eta \right) \) which decreases supports is also called a local operator, since the value of \( L\left( s\right) \) at \( x \) depends only on the values of \( s \) at points in an arbitrarily small neighborhood of \( x \) . (A theorem of [Pee59] asserts that every local operator is a differential operator, that is it can be expressed locally as a finite linear combination of partial derivatives, with coefficients in \( {C}^{\infty }\left( \eta \right) \) .)

Since a connection \( \nabla \) is a local operator, it makes sense to talk about the restriction of \( \nabla \) to an open subset of \( M \) . If a collection of open sets \( {U}_{a} \) covers \( M \) , then a global connection is uniquely determined by its restrictions to the various \( {U}_{\alpha } \) .

If the open set \( U \) is small enough so that \( {\left. \zeta \right| }_{U} \) is trivial, then the collection of all possible connections on \( {\left. \zeta \right| }_{U} \) can be described as follows. Choose a basis \( {s}_{1},\ldots ,{s}_{n} \) for the sections of \( {\left. \zeta \right| }_{U} \) , so that every section can be written uniquely as a sum \( {f}_{1}{s}_{1} + \ldots  + {f}_{n}{s}_{n} \) , where the \( {f}_{i} \) are smooth complex valued functions.

Lemma C.1. A connection \( \nabla \) on the trivial bundle \( {\left. \zeta \right| }_{U} \) is uniquely determined by \( \nabla \left( {s}_{1}\right) ,\ldots ,\nabla \left( {s}_{n}\right) \) , which can be completely arbitrary smooth sections of the bundle \( {\left. {\tau }_{\mathbb{C}}^{ * } \otimes  \zeta \right| }_{U} \) . Each of the sections \( \nabla \left( {s}_{i}\right) \) can be written uniquely as a sum \( \sum {\omega }_{ij} \otimes  {s}_{j} \) where \( \left\lbrack  {\omega }_{ij}\right\rbrack \) can be an arbitrary \( n \times  n \) matrix of \( {C}^{\infty } \) complex 1-forms on \( U \) .

Proof. We adopt the convention that \( \sum \) always stands for the summation over all indices which appear twice.

In fact, given \( \nabla \left( {s}_{1}\right) ,\ldots ,\nabla \left( {s}_{n}\right) \) we can define \( \nabla \) for an arbitrary section by the formula

\[
\nabla \left( {{f}_{1}{s}_{1} + \ldots  + {f}_{n}{s}_{n}}\right)  = \sum \mathrm{d}{f}_{i} \otimes  {s}_{i} + {f}_{i}\nabla \left( {s}_{i}\right) ).
\]

Details will be left to the reader.

As an example, there is one and only one connection such that the covariant derivatives \( \nabla \left( {s}_{1}\right) ,\ldots ,\nabla \left( {s}_{n}\right) \) are all zero; or in other words so that the connection matrix \( \left\lbrack  {\omega }_{ij}\right\rbrack \) is zero. It is given by \( \nabla \left( {\sum {f}_{i}{s}_{i}}\right)  = \sum \mathrm{d}{f}_{i} \otimes  {s}_{i} \) . This particular "flat" connection depends of course on the choice of basis \( \left\{  {s}_{i}\right\} \) .

The collection of all connections on \( \zeta \) does not have any natural vector space structure. Note however that if \( {\nabla }_{1} \) and \( {\nabla }_{2} \) are two connections on \( \zeta \) , and \( g \) is a smooth complex valued function on \( M \) , then the linear combination \( g{\nabla }_{1} + \left( {1 - g}\right) {\nabla }_{2} \) is again a well defined connection on \( \zeta \) .

Lemma C.2. Every smooth complex vector bundle with paracompact base space possesses a connection.

Proof. Choose open sets \( {U}_{a} \) covering the base space with \( {\left. \zeta \right| }_{{U}_{a}} \) trivial, and choose a smooth partition of unity \( \left\{  {\lambda }_{\alpha }\right\} \) with \( \operatorname{supp}\left( {\lambda }_{\alpha }\right)  \subset  {U}_{\alpha } \) . Each restriction \( {\left. \zeta \right| }_{{U}_{a}} \) possesses a connection \( {\nabla }_{a} \) by Lemma 1. The linear combination \( \sum {\lambda }_{a}{\nabla }_{a} \) is now a well defined global connection.

Next let us consider the case of an induced vector bundle. Given a smooth map \( g : {M}^{\prime } \rightarrow  M \) we can form the induced vector bundle \( {\zeta }^{\prime } = {g}^{ * }\zeta \) . Note that there is a canonical \( {C}^{\infty }\left( {M,\mathbb{C}}\right) \) -linear mapping

\[
{g}^{ * } : {C}^{\infty }\left( \zeta \right)  \rightarrow  {C}^{\infty }\left( {\zeta }^{\prime }\right) .
\]

Also, any 1-form on \( M \) pulls back to a 1-form on \( {M}^{\prime } \) , so there is a canonical \( {C}^{\infty }\left( {M,\mathbb{C}}\right) \) -linear mapping

\[
{g}^{ * } : {C}^{\infty }\left( {{\tau }_{\mathbb{C}}^{ * }\left( M\right)  \otimes  \zeta }\right)  \rightarrow  {C}^{\infty }\left( {{\tau }_{\mathbb{C}}^{ * }\left( {M}^{\prime }\right) }\right)  \otimes  {\zeta }^{\prime })
\]

Lemma C.3. To each connection \( \nabla \) on \( \zeta \) there corresponds one and only one connection \( {\nabla }^{\prime } = {g}^{ * }\nabla \) on the induced bundle \( {\zeta }^{\prime } \) so that the following diagram is commutative

![bo_d7du9galb0pc73deir9g_295_621_270_490_189_0.jpg](images/bo_d7du9galb0pc73deir9g_295_621_270_490_189_0.jpg)

Proof. For example, given sections \( {s}_{1},\ldots ,{s}_{n} \) over an open subset \( U \) of \( M \) with \( \nabla \left( {s}_{i}\right)  = \sum {\omega }_{ij} \otimes  {s}_{j} \) we can form the lifted 1-forms \( {\omega }_{ij}^{\prime } \) and the lifted sections \( {s}_{i}^{\prime } \) over \( {g}^{-1}\left( U\right) \) . If such a connection \( {\nabla }^{\prime } \) exists, then evidently

\[
{\nabla }^{\prime }\left( {s}_{i}^{\prime }\right)  = \sum {\omega }_{ij}^{\prime } \otimes  {s}_{j}^{\prime }
\]

Further details will be left to the reader.

Given a connection \( \nabla \) on \( \zeta \) , let us try to construct something like a connection on the bundle \( {\tau }_{\mathbb{C}}^{ * } \otimes  \zeta \) . We will make use of \( \nabla \) together with the exterior differentiation operator \( d : {C}^{\infty }\left( {\tau }_{\mathbb{C}}^{ * }\right)  \rightarrow  {C}^{\infty }\left( {{\Lambda }^{2}{\tau }_{\mathbb{C}}^{ * }}\right) \) .

Lemma C.4. Given \( \nabla \) there is one and only one \( \mathbb{C} \) -linear mapping

\[
\widehat{\nabla } : {C}^{\infty }\left( {{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right)  \rightarrow  {C}^{\infty }\left( {{\Lambda }^{2}{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right)
\]

which satisfies the Leibniz formula

\[
\widehat{\nabla }\left( {\theta  \otimes  s}\right)  = \mathrm{d}\theta  \otimes  s - \theta  \land  \nabla \left( s\right)
\]

for every 1-form \( \theta \) and every section \( s \in  {C}^{\infty }\left( \zeta \right) \) . Furthermore \( \widehat{\nabla } \) satisfies the identity

\[
\widehat{\nabla }\left( {f\left( {\theta  \otimes  s}\right) }\right)  = \mathrm{d}f \land  \left( {\theta  \otimes  s}\right)  + f\widehat{\nabla }\left( {\theta  \otimes  s}\right) .
\]

Proof. In terms of a local basis \( {s}_{1},\ldots ,{s}_{n} \) for the sections, we must have

\[
\widehat{\nabla }\left( {{\theta }_{1} \otimes  {s}_{1} + \ldots  + {\theta }_{n} \otimes  {s}_{n}}\right)  = \sum \left( {\mathrm{d}{\theta }_{i} \otimes  {s}_{i} - {\theta }_{i} \land  \nabla \left( {s}_{i}\right) }\right) .
\]

Taking this formula as definition of \( \widehat{\nabla } \) , the required identities are easily verified.

Now let us consider the composition \( K = \widehat{\nabla } \circ  \nabla \) of the two \( \mathbb{C} \) -linear mappings

\[
{C}^{\infty }\left( \zeta \right) \overset{\nabla }{ \rightarrow  }{C}^{\infty }\left( {{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right) \overset{\widehat{\nabla }}{ \rightarrow  }{C}^{\infty }\left( {{\Lambda }^{2}{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right)
\]

Lemma C.5. The value of the section \( K\left( s\right)  = \widehat{\nabla }\left( {\nabla \left( s\right) }\right) \) at \( x \) depends only on \( s\left( x\right) \) , not on the values of \( s \) at other points of \( M \) . Hence the correspondence

\[
s\left( x\right)  \mapsto  K\left( s\right) \left( x\right)
\]

defines a smooth section of the complex vector bundle \( \operatorname{Hom}\left( {\zeta ,{\Lambda }^{2}{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right) \)

Definition. This section \( K = {K}_{\nabla } \) of the vector bundle

\( \operatorname{Hom}\left( {\zeta ,{\Lambda }^{2}{\tau }_{\mathbb{C}}^{ * } \otimes  \zeta }\right)  \cong  {\Lambda }^{2}{\tau }_{\mathbb{C}}^{ * } \otimes  \operatorname{Hom}\left( {\zeta ,\zeta }\right) \) is called the curvature tensor of the connection \( \nabla \) .

Proof. Clearly \( K \) is a local operator. The computation

\[
\widehat{\nabla }\left( {\nabla \left( {fs}\right) }\right)  = \widehat{\nabla }\left( {\mathrm{d}f \otimes  s + f\nabla \left( s\right) }\right)  = 0 - \mathrm{d}f \land  \nabla \left( s\right)  + \mathrm{d}f \land  \nabla \left( s\right)  + f\widehat{\nabla }\left( {\nabla \left( s\right) }\right)
\]

shows that the composition \( \widehat{\nabla } \circ  \nabla  = K \) is actually \( {C}^{\infty }\left( {M,\mathbb{C}}\right) \) -linear:

\[
K\left( {fs}\right)  = {fK}\left( s\right) .
\]

Now if \( s\left( x\right)  = {s}^{\prime }\left( x\right) \) then, in terms of a local basis \( {s}_{1},\ldots ,{s}_{n} \) for sections we have

\[
{s}^{\prime } - s = {f}_{1}{s}_{1} + \ldots  + {f}_{n}{s}_{n}
\]

near \( x \) , where \( {f}_{1}\left( x\right)  = \ldots  = {f}_{n}\left( x\right)  = 0 \) . Hence

\[
K\left( {s}^{\prime }\right)  - K\left( s\right)  = \sum {f}_{i}K\left( {s}_{i}\right)
\]

vanishes at \( x \) . This completes the proof.

In terms of a basis \( {s}_{1},\ldots ,{s}_{n} \) for the sections of \( {\left. \zeta \right| }_{U} \) , with \( \nabla \left( {s}_{i}\right)  = \sum {\omega }_{ij} \otimes  {s}_{j} \) , note the explicit formula

\[
K\left( {s}_{i}\right)  = \widehat{\nabla }\left( {\sum {\omega }_{ij} \otimes  {s}_{j}}\right)
\]

\[
= \sum {\Omega }_{ij} \otimes  {s}_{j}
\]

where we have set

\[
{\Omega }_{ij} = \mathrm{d}{\omega }_{ij} - \sum {\omega }_{i\alpha } \land  {\omega }_{\alpha j}.
\]

Thus \( K \) can be described locally by the \( n \times  n \) matrix \( \Omega  = \left\lbrack  {\Omega }_{ij}\right\rbrack \) of 2-forms in much the same way that \( \nabla \) is described locally by the matrix \( \omega  = \left\lbrack  {\omega }_{ij}\right\rbrack \) of 1-forms. In matrix notation, we have

\[
\Omega  = \mathrm{d}\omega  - \omega  \land  \omega
\]

A fundamental theorem, which we will not prove, asserts that the curvature tensor \( K \) is zero if and only if, in the neighborhood of each point of \( M \) there exists a basis \( {s}_{1},\ldots ,{s}_{n} \) for the sections of \( \zeta \) so that \( \nabla \left( {s}_{1}\right)  = \ldots  = \nabla \left( {s}_{n}\right)  = 0 \) . (Compare [BC11] or [KN63].) In fact if \( M \) is simply connected and \( K = 0 \) , then there exist global sections \( {s}_{1},\ldots ,{s}_{n} \) with \( \nabla \left( {s}_{1}\right)  = \ldots  = \nabla \left( {s}_{n}\right)  = 0 \) . It follows in that case of course that \( \zeta \) is a trivial bundle. If the tensor \( K = {K}_{\nabla } \) is zero, then the connection \( \nabla \) is called flat.

Remark. Using Steenrod's terminology, a bundle with flat connection can be described as a bundle with discrete structural group. To see this consider two different local bases, say \( {s}_{1},\ldots ,{s}_{n} \in  {C}^{\infty }\left( {\left. \zeta \right| }_{U}\right) \) and \( {s}_{1}^{\prime },\ldots ,{s}_{n}^{\prime } \in  {C}^{\infty }\left( {\left. \zeta \right| }_{V}\right) \) , both of which have covariant derivatives zero. Over the intersection \( U \cap  V \) we can set \( {s}_{i}^{\prime } = \sum {a}_{ij}{s}_{j} \) . The equation \( \nabla \left( {s}_{i}^{\prime }\right)  = \sum \mathrm{d}{a}_{ij} \otimes  {s}_{j} = 0 \) shows that the transition functions \( {a}_{ij} \) are locally constant. Hence the associated mapping

\[
\left\lbrack  {a}_{ij}\right\rbrack   : U \cap  V \rightarrow  \mathrm{{GL}}\left( {n,\mathbb{C}}\right)
\]

is continuous, even if the linear group \( \mathrm{{GL}}\left( {n,\mathbb{C}}\right) \) is provided with the discrete topology.

Starting with the curvature tensor \( K \) , we can construct characteristic classes as follows. Let \( {M}_{n}\left( \mathbb{C}\right) \) be the algebra consisting of all \( n \times  n \) complex matrices.

Definition. An invariant polynomial on \( {M}_{n}\left( \mathbb{C}\right) \) is a function

\[
P : {M}_{n}\left( \mathbb{C}\right)  \rightarrow  \mathbb{C}
\]

which can be expressed as a complex polynomial in the entries of the matrix, and satisfies

\[
P\left( {XY}\right)  = P\left( {YX}\right) ,
\]

or equivalently

\[
P\left( {{TX}{T}^{-1}}\right)  = P\left( X\right)
\]

for every non-singular matrix \( T \) .

(The first identity evidently follows from the second when \( Y \) is non-singular, and the general case follows by continuity, since every singular matrix can be approximated by non-singular matrices.)

Examples. The trace function \( \left\lbrack  {X}_{ij}\right\rbrack   \rightarrow  \sum {X}_{ii} \) , and the determinant function are well known examples of invariant polynomials on \( {M}_{n}\left( \mathbb{C}\right) \)

If \( P \) is an invariant polynomial, then an exterior form \( P\left( K\right) \) on the base space \( M \) is defined as follows. Choosing a local basis \( {s}_{1},\ldots ,{s}_{n} \) for the sections near \( x \) , we have \( K\left( {s}_{i}\right)  = \sum {\Omega }_{ij} \otimes  {s}_{j} \) . The matrix \( \Omega  = \left\lbrack  {\Omega }_{ij}\right\rbrack \) has entries in the commutative algebra over \( \mathbb{C} \) consisting of the exterior forms of even degree. It makes perfect sense therefore to evaluate the complex polynomial \( P \) at \( \Omega \) , thus obtaining an algebra element. The resulting algebra element \( P\left( \Omega \right) \) does not depend on the choice of basis \( {s}_{1},\ldots ,{s}_{n} \) , since a change of basis will replace the matrix \( \Omega \) by one of the form \( {T\Omega }{T}^{-1} \) where \( T \) is a non-singular matrix of functions. Since \( P\left( {{T\Omega }{T}^{-1}}\right)  = P\left( \Omega \right) \) , these various local differential forms \( P\left( \Omega \right) \) are uniquely defined. They piece together to yield a global differential form which we denote by \( P\left( K\right) \)

Remark 1. If \( P \) is a homogeneous polynomial of degree \( r \) , then of course \( P\left( K\right) \) is an exterior form of degree \( {2r} \) . In general, \( P \) will be a sum of homogeneous polynomials of various degrees, and correspondingly \( P\left( K\right) \) will be a sum of exterior forms of various even degrees. We will use the notation \( P\left( K\right)  \in  {C}^{\infty }\left( {{\Lambda }^{ \oplus  }{\tau }_{\mathbb{C}}^{ * }}\right)  = \bigoplus {C}^{\infty }\left( {{\Lambda }^{r}{\tau }_{\mathbb{C}}^{ * }}\right) . \)

Remark 2. 2. More generally, in place of an invariant polynomial, one can equally well use an invariant formal power series of the form

\[
P = {P}_{0} + {P}_{1} + {P}_{2} + \ldots
\]

where each \( {P}_{r} \) is an invariant homogeneous polynomial of degree \( r \) . Then \( P\left( K\right) \) is still well defined, since \( {P}_{r}\left( K\right)  = 0 \) for \( {2r} > \dim \left( M\right) \) . (A notable example of an invariant formal power series is the Chern character \( \operatorname{ch}\left( A\right)  = \operatorname{trace}\left( {\mathrm{e}}^{A/{2\pi i}}\right) \) .

Lemma (Fundamental Lemma). For any invariant polynomial (or invariant formal power series) \( P \) , the exterior form \( P\left( K\right) \) is closed, that is \( \mathrm{d}P\left( K\right)  = 0 \) .

Proof. Given any invariant polynomial or formal power series \( P\left( A\right)  = P\left( \left\lbrack  {A}_{ij}\right\rbrack  \right) \) , where \( {A}_{ij} \) stand for indeterminates, we can form the matrix

\[
\left\lbrack  \frac{\partial P}{\partial {A}_{ij}}\right\rbrack
\]

of formal first derivatives. It will be convenient to denote the transpose of this matrix by the symbol \( {P}^{\prime }\left( A\right) \) .

Now let \( \Omega  = \left\lbrack  {\Omega }_{ij}\right\rbrack \) be the curvature matrix with respect to some basis for \( {\left. \zeta \right| }_{U} \) . Evidently the exterior derivative \( \mathrm{d}P\left( \Omega \right) \) is equal to the expression

\[
\sum \frac{\partial P}{\partial {\Omega }_{ij}}\mathrm{\;d}{\Omega }_{ij}.
\]

In matrix notation, we can write this

\[
\mathrm{d}P\left( \Omega \right)  = \operatorname{trace}\left( {{P}^{\prime }\left( \Omega \right) \mathrm{d}\Omega }\right) . \tag{C.1}
\]

The matrix \( \mathrm{d}\Omega \) of 3-forms can be computed by taking the exterior derivative of the matrix equation

\[
\mathrm{d}\Omega  = \mathrm{d}\omega  - \omega  \land  \omega
\]

and then substituting this equation back into the result. This yields the Bianchi identity

\[
\mathrm{d}\Omega  = \omega  \land  \Omega  - \Omega  \land  \omega \tag{C.2}
\]

We will need the following remark. For any invariant polynomial or

power series \( P \) , the transposed matrix of first derivatives \( {P}^{\prime }\left( A\right) \) commutes with \( A \) . To prove this statement, let \( {E}_{ji} \) denote the matrix with entry 1 in the \( \left( {j, i}\right) \) -th place and zeros elsewhere. Differentiating the equation

\[
P\left( {\left( {I + t{E}_{ji}}\right) A}\right)  = P\left( {A\left( {I + t{E}_{ji}}\right) }\right)
\]

with respect to \( t \) and then setting \( t = 0 \) , we obtain

\[
\sum {A}_{i\alpha }\frac{\partial P}{\partial {A}_{j\alpha }} = \sum \frac{\partial P}{\partial {A}_{\alpha i}}{A}_{\alpha j}.
\]

Thus the matrix \( A \) commutes with the transpose of \( \left\lbrack  {\partial P/\partial {A}_{ij}}\right\rbrack \) , as asserted.

Substituting \( \Omega \) for the matrix of indeterminates \( A \) , it follows that

\[
\Omega  \land  {P}^{\prime }\left( \Omega \right)  = {P}^{\prime }\left( \Omega \right)  \land  \Omega \tag{C.3}
\]

It will be convenient to use the notation \( X \) for the product matrix \( {P}^{\prime }\left( \Omega \right)  \land  \omega \) . Now substituting the Bianchi identity (C.2) into (C.1) and using (C.3) we obtain

\[
\mathrm{d}P\left( \Omega \right)  = \operatorname{trace}\left( {X \land  \Omega  - \Omega  \land  X}\right)
\]

\[
= \sum \left( {{X}_{ij} \land  {\Omega }_{ji} - {\Omega }_{ji} \land  {X}_{ij}}\right) .
\]

Since each \( {X}_{ij} \) commutes with the 2-form \( {\Omega }_{ji} \) , this sum is zero, which proves the Fundamental Lemma.

Thus the exterior form \( P\left( K\right) \) is closed, or in other words is a de Rham cocy-cle, representing an element which we denote by \( \left( {P\left( K\right) }\right) \) in the total de Rham cohomology ring \( {\mathrm{H}}^{ \oplus  }\left( {M;\mathbb{C}}\right)  = \bigoplus {\mathrm{H}}^{i}\left( {M;\mathbb{C}}\right) \) .

Corollary C.6. The cohomology class \( \left( {P\left( K\right) }\right)  = \left( {P\left( {K}_{\nabla }\right) }\right) \) is independent of the connection \( \nabla \) .

Proof. Let \( {\nabla }_{0} \) and \( {\nabla }_{1} \) be two different connections on \( \zeta \) . Mapping \( M \times  \mathbb{R} \) to \( M \) by the projection \( \left( {x, t}\right)  \mapsto  x \) , we can form the induced bundle \( {\zeta }^{\prime } \) over \( M \times  \mathbb{R} \) , the induced connections \( {\nabla }_{0}^{\prime } \) and \( {\nabla }_{1}^{\prime } \) , and the linear combination

\[
\nabla  = t{\nabla }_{1}^{\prime } + \left( {1 - t}\right) {\nabla }_{2}^{\prime }.
\]

Thus \( P\left( {K}_{\nabla }\right) \) is a de Rham cocycle on \( M \times  \mathbb{R} \) .

Now consider the map \( {i}_{\varepsilon } : x \mapsto  \left( {x,\varepsilon }\right) \) from \( M \) to \( M \times  \mathbb{R} \) , where \( \varepsilon \) equals 0 or 1. Evidently the induced connection \( {\left( {i}_{\varepsilon }\right) }^{ * }\nabla \) on \( {\left( {i}_{\varepsilon }\right) }^{ * }{\zeta }^{\prime } \) can be identified with the connection \( {\nabla }_{\varepsilon } \) on \( \zeta \) . Therefore

\[
{\left( {i}_{\varepsilon }\right) }^{ * }\left( {P\left( {K}_{\nabla }\right) }\right)  = \left( {P\left( {K}_{{\nabla }_{\varepsilon }}\right) }\right) .
\]

But the mapping \( {i}_{0} \) is homotopic to \( {i}_{1} \) hence the cohomology class \( \left( {P\left( {K}_{{\nabla }_{0}}\right) }\right) \) is equal to \( \left( {P\left( {K}_{{\nabla }_{1}}\right) }\right) \) .

Thus \( P \) determines a characteristic cohomology class in \( {\mathrm{H}}^{ * }\left( {M;\mathbb{C}}\right) \) depending only on the isomorphism class of the vector bundle \( \zeta \) . If a map \( g \) : \( {M}^{\prime } \rightarrow  M \) induces a bundle \( {\zeta }^{\prime } = {g}^{ * }\zeta \) , with induced connection \( {\nabla }^{\prime } \) , then clearly

\[
P\left( {K}_{{\nabla }^{\prime }}\right)  = {g}^{ * }P\left( {K}_{\nabla }\right) .
\]

Thus these characteristic classes are well behaved with respect to induced bundles.

But we already know from Section 14 that any characteristic class for complex vector bundles can be expressed as a polynomial in the Chern classes. Thus we are left with the following two questions: What invariant polynomials exist; and how can their associated characteristic classes be expressed explicitly in terms of Chern classes?

The first answer can easily be answered as follows. For any square matrix \( A \) , let \( {\sigma }_{k}\left( A\right) \) denote the \( k \) -th elementary symmetric function of the eigenvalues of \( A \) , so that

\[
\det \left( {I + {tA}}\right)  = 1 + t{\sigma }_{1}\left( A\right)  + \ldots  + {t}^{n}{\sigma }_{n}\left( A\right) .
\]

Lemma C.7. Any invariant polynomial on \( {M}_{n}\left( \mathbb{C}\right) \) can be expressed as a polynomial function of \( {\sigma }_{1},\ldots ,{\sigma }_{n} \) .

Proof. Given \( A \in  {M}_{n}\left( \mathbb{C}\right) \) we can choose \( B \) so that \( {BA}{B}^{-1} \) is an upper triangular matrix; in fact, we could actually put \( A \) in Jordan canonical form. Replacing \( B \) by \( \operatorname{diag}\left( {\epsilon ,{\epsilon }^{2},\ldots ,{\epsilon }^{n}}\right) B \) , we can then make the off diagonal entries arbitrarily close to zero. By continuity it follows that \( P\left( A\right) \) depends only on the diagonal entries of \( {BA}{B}^{-1} \) , or in other words on the eigenvalues of \( A \) . Since \( P\left( A\right) \) must certainly be a symmetric function of these eigenvalues, the classical theory of symmetric functions completes the proof.

We will see later that the characteristic class \( \left( {{\sigma }_{r}\left( K\right) }\right) \) is equal to a complex multiple of the Chern class \( {\mathrm{c}}_{r}\left( \zeta \right) \) .

Leaving this for a moment, let us look at the corresponding theory for real vector bundles. The concepts of a connection

\[
\nabla  : {C}^{\infty }\left( \xi \right)  \rightarrow  {C}^{\infty }\left( {{\tau }^{ * } \otimes  \xi }\right)
\]

on a real vector bundle \( \xi \) , and of its curvature tensor

\[
K \in  {C}^{\infty }\left( {\operatorname{Hom}\left( {\xi ,{\Lambda }^{2}{\tau }^{ * } \otimes  \xi }\right) }\right)  \cong  {C}^{\infty }\left( {{\Lambda }^{2}\tau  \otimes  \operatorname{Hom}\left( {\xi ,\xi }\right) }\right) ,
\]

are defined just as above, simply substituting the real numbers for the complex numbers throughout. Any invariant polynomial \( P \) on the matrix algebra \( {M}_{n}\left( \mathbb{R}\right) \) gives rise to a characteristic cohomology class \( \left( {P\left( K\right) }\right)  \in  {\mathrm{H}}^{ * }\left( {M;\mathbb{R}}\right) \) .

The most classical and familiar example of a connection is provided by the Levi-Civita connection on the tangent or dual tangent bundle of a Riemannian manifold. We will next give an outline of this theory.

First consider a real vector bundle \( \xi \) over \( M \) which is provided with a Euclidean metric. Thus if \( s \) and \( {s}^{\prime } \) are smooth sections of \( \xi \) , then the inner product \( \left\langle  {s,{s}^{\prime }}\right\rangle \) is a smooth real valued function over \( M \) .

Definition. A connection \( \nabla \) on \( \xi \) is compatible with the metric if the identity

\[
\mathrm{d}\left\langle  {s,{s}^{\prime }}\right\rangle   = \left\langle  {\nabla s,{s}^{\prime }}\right\rangle   + \left\langle  {s,\nabla {s}^{\prime }}\right\rangle
\]

is valid for all sections \( s \) and \( {s}^{\prime } \) .

Here it is understood that the inner products on the right are defined by the requirement that

\[
\left\langle  {\theta  \otimes  s,{s}^{\prime }}\right\rangle   = \left\langle  {s,\theta  \otimes  {s}^{\prime }}\right\rangle   = \left\langle  {s,{s}^{\prime }}\right\rangle  \theta
\]

for all \( \theta  \in  {C}^{\infty }\left( {\tau }^{ * }\right) \) for all \( s,{s}^{\prime } \in  {C}^{\infty }\left( \xi \right) \) . Unfortunately this notation can be confusing in some situations. It is safer in general to make use of the following.

Lemma C.8. Let \( {s}_{1},\ldots ,{s}_{n} \) be an orthonormal basis for the sections of \( {\left. \xi \right| }_{U} \) , so that \( \left\langle  {{s}_{i},{s}_{j}}\right\rangle   = {\delta }_{ij} \) . Then a connection \( \nabla \) on \( {\left. \xi \right| }_{U} \) is compatible with the metric if and only if the associated connection matrix \( \left\lbrack  {\omega }_{ij}\right\rbrack \) (defined by \( \nabla \left( {s}_{i}\right)  = \sum {\omega }_{ij} \otimes  {s}_{j} \) ) is skew-symmetric.

Proof. For if \( \nabla \) is compatible, then

\[
0 = \mathrm{d}\left\langle  {{s}_{i},{s}_{j}}\right\rangle   = \left\langle  {\nabla {s}_{i},{s}_{j}}\right\rangle   + \left\langle  {{s}_{i},\nabla {s}_{j}}\right\rangle
\]

\[
= \left\langle  {\sum {\omega }_{ik} \otimes  {s}_{k},{s}_{j}}\right\rangle   + \left\langle  {{s}_{i},\sum {\omega }_{jk} \otimes  {s}_{k}}\right\rangle   = {\omega }_{ij} + {\omega }_{ji}.
\]

The converse will be left to the reader.

Remark. The appearance of skew-symmetric matrices at this point is of course bound up with the fact that the Lie algebra of the orthogonal group \( \mathrm{O}\left( n\right) \) is equal to the Lie subalgebra of \( {M}_{n}\left( \mathbb{R}\right) \) consisting of all skew-symmetric matrices.

Definition. A connection \( \nabla \) on \( {\tau }^{ * } \) is symmetric (or torsion free) if the composition

\[
{C}^{\infty }\left( {\tau }^{ * }\right) \overset{\nabla }{ \rightarrow  }{C}^{\infty }\left( {{\tau }^{ * } \otimes  {\tau }^{ * }}\right) \overset{ \land  }{ \rightarrow  }{C}^{\infty }\left( {{\Lambda }^{2}{\tau }^{ * }}\right)
\]

is equal to the exterior derivative d.

In terms of local coordinates \( {x}_{1},\ldots {x}^{n} \) , setting

\[
\nabla \left( {\mathrm{d}{x}^{k}}\right)  = \sum {\Gamma }_{ij}^{k}\mathrm{\;d}{x}^{i} \otimes  \mathrm{d}{x}^{j}
\]

this requires that the image \( \sum {\Gamma }_{ij}^{k}\mathrm{\;d}{x}^{i} \land  \mathrm{d}{x}^{j} \) must be equal to the exterior derivative \( \mathrm{d}\left( {\mathrm{d}{x}^{k}}\right)  = 0 \) . Hence the Christoffel symbols \( {\Gamma }_{ij}^{k} \) must be symmetric in \( i, j \) . More generally, the following is easily verified.

Assertion. A connection \( \nabla \) on \( {\tau }^{ * } \) is symmetric if and only if the second covariant derivative

\[
\nabla \left( {\mathrm{d}f}\right)  \in  {C}^{\infty }\left( {{\tau }^{ * } \otimes  {\tau }^{ * }}\right)
\]

of an arbitrary smooth function \( f \) is a symmetric tensor. That is, in terms of a local basis \( {\theta }_{1},\ldots ,{\theta }_{n} \) for the sections of \( {\tau }^{ * } \) , one must have \( \nabla \left( {\mathrm{d}f}\right)  = \sum {a}_{ij}{\theta }_{i} \otimes  {\theta }_{j} \) with \( {a}_{ij} = {a}_{ji} \) .

Lemma C.9. The dual tangent bundle \( {\tau }^{ * } \) of a Riemannian manifold possesses one and only one symmetric connection which is compatible with its metric.

This prefered connection \( \nabla \) is called the Riemannian connection or the Levi-Civita connection.

Proof. Let \( {\theta }_{1},\ldots ,{\theta }_{n} \) be an orthonormal basis for the sections of \( {\left. {\tau }^{ * }\right| }_{U} \) . We will show that there is one and only one skew-symmetric matrix \( \left\lbrack  {\omega }_{kj}\right\rbrack \) of 1 -forms such that

\[
\mathrm{d}{\theta }_{k} = \sum {\omega }_{kj} \land  {\theta }_{j}.
\]

Defining a connection \( \nabla \) on \( U \) by the requirement that

\[
\nabla \left( {\theta }_{k}\right)  = \sum {\omega }_{kj} \otimes  {\theta }_{j}
\]

it evidently follows that \( \nabla \) is the unique symmetric connection for \( {\left. {\tau }^{ * }\right| }_{U} \) which is compatible with the metric. Since these local connections are unique, they agree on intersections \( U \cap  {U}^{\prime } \) and so piece together to yield the required global connection.

We will need the following combinatorial remark. Any \( n \times  n \times  n \) array of real valued functions \( {A}_{ijk} \) can be written uniquely as the sum of an array \( {B}_{ijk} \) which is symmetric in \( i, j \) and an array \( {C}_{ijk} \) which is skew-symmetric in \( j, k \) . In fact, existence can be proved by inspecting the explicit formulas

\[
{B}_{ijk} = \frac{1}{2}\left( {{A}_{ijk} + {A}_{jik} - {A}_{kij} - {A}_{kji} + {A}_{jki} + {A}_{ikj}}\right)
\]

\[
{C}_{ijk} = \frac{1}{2}\left( {{A}_{ijk} - {A}_{jik} + {A}_{kij} + {A}_{kji} - {A}_{jki} - {A}_{ikj}}\right)
\]

and uniqueness is clear since if an array \( {D}_{ijk} \) were both symmetric in \( i, j \) and skew in \( j, k \) then the equalities

\[
{D}_{123} = {D}_{213} =  - {D}_{231} =  - {D}_{321} = {D}_{312} = {D}_{132} =  - {D}_{123}
\]

would show that the typical entry \( {D}_{123} \) is zero.

Now choosing functions \( {A}_{ijk} \) so that \( \mathrm{d}{\theta }_{k} = \sum {A}_{ijk}{\theta }_{i} \land  {\theta }_{j} \) and setting \( {A}_{ijk} = {B}_{ijk} + {C}_{ijk} \) as above, it follows that \( \mathrm{d}{\theta }_{k} = \sum {C}_{ijk}{\theta }_{i} \land  {\theta }_{j} \) . In fact, the

1-forms

\[
{\omega }_{kj} = \sum {C}_{ijk}{\theta }_{i}
\]

evidently constitute the unique skew-symmetric matrix with \( \mathrm{d}{\theta }_{k} = \sum {\omega }_{kj} \land  {\theta }_{j} \) . This proves Lemma C.9.

Let us specialize to the case of a 2-dimensional oriented Riemannian manifold. With respect to an oriented local orthonormal basis \( {\theta }_{1},{\theta }_{2} \) for 1-forms, the connection and curvature matrices take the form

\[
\left\lbrack  \begin{matrix} 0 & {\omega }_{12} \\   - {\omega }_{12} & 0 \end{matrix}\right\rbrack  \text{ and }\left\lbrack  \begin{matrix} 0 & {\Omega }_{12} \\   - {\Omega }_{12} & 0 \end{matrix}\right\rbrack  ,
\]

with \( \mathrm{d}{\omega }_{12} = {\Omega }_{12} \) . The identity

\[
\left\lbrack  \begin{matrix} \cos t & \sin t \\   - \sin t & \cos t \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} 0 & {\Omega }_{12} \\   - {\Omega }_{12} & 0 \end{matrix}\right\rbrack  \left\lbrack  \begin{matrix} \cos t &  - \sin t \\  \sin t & \cos t \end{matrix}\right\rbrack   = \left\lbrack  \begin{matrix} 0 & {\Omega }_{12} \\   - {\Omega }_{12} & 0 \end{matrix}\right\rbrack
\]

shows that the exterior 2-form \( {\Omega }_{12} \) is independent of the choice of oriented local basis. Hence it gives rise to a well defined global 2-form.

Definition. This form \( {\Omega }_{12} \) is called the Gauss-Bonnet 2-form on the oriented surface. Denoting the oriented area 2-form \( - {\theta }_{1} \land  {\theta }_{2} \) briefly by the symbol \( \mathrm{d}A \) , we can set \( {\Omega }_{12} = \mathcal{K}\mathrm{d}A \) , where \( \mathcal{K} \) is a scalar function called the Gaussian curvature.

Since both \( {\Omega }_{12} \) and \( \mathrm{d}A \) change sign if we reverse the orientation of \( M \) , it follows that \( \mathcal{K} \) is independent of orientation.

Note on signs. The above choice of sign for \( \mathrm{d}A \) may look strange to the reader. It can be justified as follows. In conformity with [Mac75], and as described in Appendix A, we introduce the sign of \( {\left( -1\right) }^{mn} \) whenever an object of dimension \( m \) is permuted with an adjacent object of dimension \( n \) . Thus if \( {I}^{n} \) denotes the unit cube with ordered coordinates \( {t}_{1},\ldots ,{t}_{n} \) and canonical orientation class \( \mu  \in  {\mathrm{H}}_{n}\left( {{I}^{n},\partial {I}^{n}}\right) \) , we set

\[
\left\langle  {\mathrm{d}{t}_{1} \land  \ldots  \land  \mathrm{d}{t}_{n},\mu }\right\rangle   = \left\langle  {\mathrm{d}{t}_{1} \land  \ldots  \land  \mathrm{d}{t}_{n},{\int }_{{t}_{1} = 0}^{1}\cdots {\int }_{{t}_{n} = 0}^{1}}\right\rangle
\]

\[
= {\left( -1\right) }^{n + \left( {n - 1}\right)  + \ldots  + 1}{\int }_{{t}_{1} = 0}^{1}\mathrm{\;d}{t}_{1}\ldots {\int }_{{t}_{n} = 0}^{1}\mathrm{\;d}{t}_{n} = {\left( -1\right) }^{n\left( {n + 1}\right) /2}.
\]

In other words the "oriented volume \( n \) -form" on \( {I}^{n} \) is, by definition, set equal to \( {\left( -1\right) }^{n\left( {n + 1}\right) /2}\mathrm{\;d}{t}_{1} \land  \ldots  \land  \mathrm{d}{t}_{n} \) . This choice of signs leads to a version of Stokes’ theorem,

\[
\langle \mathrm{d}\phi ,\mu \rangle  + {\left( -1\right) }^{\dim \phi }\langle \phi ,\partial \mu \rangle  = 0,
\]

which is compatible with Appendix A. Readers who prefer to use the classical sign conventions in [Spa81], [War13] and [BC65] can forget about these signs, but should replace \( \mathcal{K} \) by \( - \mathcal{K} \) wherever it occurs in our characteristic formulas.

To give some reality to this rather abstract definition, let us carry out a more explicit computation. In some neighborhood \( U \) of an arbitrary point on a Riemannian 2-manifold, one can introduce geodesic coordinates \( x, y \) so that the metric quadratic differential in \( {C}^{\infty }\left( {{\tau }^{ * } \otimes  {\left. {\tau }^{ * }\right| }_{U}}\right) \) takes the form

\[
\mathrm{d}x \otimes  \mathrm{d}x + g{\left( x, y\right) }^{2}\mathrm{\;d}y \otimes  \mathrm{d}y.
\]

Then setting

\[
{\theta }_{1} = \mathrm{d}x,\;{\theta }_{2} = g\mathrm{\;d}y
\]

we obtain an orthonormal basis for the 1 -forms over \( U \) . The equations

\[
\mathrm{d}{\theta }_{1} = {\omega }_{12} \land  {\theta }_{2}
\]

\[
\mathrm{d}{\theta }_{2} =  - {\omega }_{12} \land  {\theta }_{1}
\]

have unique solution \( {\omega }_{12} = {g}_{x}\mathrm{\;d}y \) , where subscript \( x \) stands for the partial derivative. It follows that

\[
{\Omega }_{12} = {g}_{xx}\mathrm{\;d}x \land  \mathrm{d}y = \left( {-{g}_{xx}/g}\right) \mathrm{d}A.
\]

Thus the Gaussian curvature is given by

\[
\mathcal{K} =  - {g}_{xx}/g.
\]

As an example, taking latitude and longitude as coordinates on the unit sphere, we have \( g\left( {x, y}\right)  = \cos \left( x\right) \) , and therefore \( \mathcal{K} = 1 \) .

Theorem (Gauss-Bonnet). For any closed oriented Riemannian 2-manifold, the integral \( \iint {\Omega }_{12} = \iint \mathcal{K}\mathrm{d}A \) is equal to \( {2\pi }\mathrm{e}\left\lbrack  M\right\rbrack \) .

Proof. More generally, consider any oriented 2-plane bundle \( \xi \) with Euclidean metric. Then \( \xi \) has a canonical complex structure \( \mathbf{J} \) which rotates each vector through an angle of \( \pi /2 \) in the "counter-clockwise" direction. In terms of an oriented local orthonormal basis \( {s}_{1},{s}_{2} \) for sections, we have \( \mathbf{J}{s}_{1}\left( x\right)  = {s}_{2}\left( x\right) \) . Choosing any compatible connection on \( \xi \) , we have

\[
\nabla {s}_{1} = {\omega }_{12} \otimes  {s}_{2}
\]

\[
\nabla {s}_{2} =  - {\omega }_{12} \otimes  {s}_{1}
\]

Evidently \( \nabla \) gives rise to a connection on the resulting complex line bundle \( \zeta \) , where

\[
\nabla {s}_{1} = {\omega }_{12} \otimes  i{s}_{1} = i{\omega }_{12} \otimes  {s}_{1}
\]

and consequently \( \nabla \left( {i{s}_{1}}\right)  = i\nabla {s}_{1} =  - {\omega }_{12} \otimes  {s}_{1} \) . Thus the connection matrix of this complex connection is the \( 1 \times  1 \) matrix \( \left\lbrack  {i{\omega }_{12}}\right\rbrack \) and the curvature matrix is \( \left\lbrack  {i{\Omega }_{12}}\right\rbrack \) . Applying the invariant polynomial \( {\sigma }_{1} = \) trace, we obtain a closed 2-form

\[
\operatorname{trace}\left\lbrack  {i{\Omega }_{12}}\right\rbrack   = i{\Omega }_{12}
\]

which represents some characteristic cohomology class in \( {\mathrm{H}}^{2}\left( {M;\mathbb{C}}\right) \) . But the only characteristic class in \( {\mathrm{H}}^{2}\left( {-;\mathbb{C}}\right) \) for complex line bundles \( \zeta \) is the Chern class \( {\mathrm{c}}_{1}\left( \zeta \right)  = \mathrm{e}\left( {\zeta }_{\mathbb{R}}\right) \) (and its multiples). Therefore

\[
\left( {i{\Omega }_{12}}\right)  = \alpha {\mathrm{c}}_{1}\left( \zeta \right)  = \alpha \mathrm{e}\left( \zeta \right)
\]

for some complex constant \( \alpha \) .

To evaluate this constant \( \alpha \) , it is only necessary to calculate both sides explicitly for one particular case. Suppose for example that \( \xi \) is the dual tangent bundle \( {\tau }^{ * } \) of a closed oriented 2-dimensional Riemannian manifold \( M \) . Since \( \left( {i{\Omega }_{12}}\right)  = \alpha \mathrm{e}\left( {\tau }^{ * }\right) \) , it follows that

\[
\iint i{\Omega }_{12} = \alpha \mathrm{e}\left\lbrack  M\right\rbrack
\]

or in other words

\[
i\iint \mathcal{K}\mathrm{d}A = \alpha \mathrm{e}\left\lbrack  M\right\rbrack
\]

Evaluating both sides for the unit 2-sphere, we see that \( \alpha  = {2\pi i} \) . This completes the proof.

Theorem. Let \( \zeta \) be a complex vector bundle with connection \( \nabla \) . Then the cohomology class \( \left( {{\sigma }_{r}\left( {K}_{\nabla }\right) }\right) \) is equal to \( {\left( 2\pi i\right) }^{r}{\mathrm{c}}_{r}\left( \zeta \right) \) .

Proof. In the case of a complex line bundle, the argument above shows that

\[
\left( {{\sigma }_{1}\left( K\right) }\right)  = \alpha {\mathrm{c}}_{1}\left( \zeta \right)  = {2\pi i}{\mathrm{c}}_{1}\left( \zeta \right) .
\]

Define the invariant polynomial \( \underline{c} \) by

\[
\underline{\mathrm{c}}\left( A\right)  = \det \left( {I + A/{2\pi i}}\right)
\]

\[
= \sum \frac{{\sigma }_{k}\left( A\right) }{{\left( 2\pi i\right) }^{k}}
\]

Thus, for a complex line bundle the coycle

\[
\underline{\mathrm{c}}\left( K\right)  = 1 + {\sigma }_{1}\left( K\right) /{2\pi i}
\]

represents the cohomology class \( \mathrm{c}\left( \zeta \right)  = 1 + {\mathrm{c}}_{1}\left( \zeta \right) \) . Now consider any bundle \( \zeta \) which splits as a Whitney sum \( {\zeta }_{1} \oplus  \ldots  \oplus  {\zeta }_{n} \) of line bundles. Choosing connections \( {\nabla }_{1},\ldots ,{\nabla }_{n} \) on the \( {\zeta }_{j} \) , there is evidently a "Whitney sum" connection on \( \zeta \) . Choosing a local section \( {s}_{j} \) for \( {\zeta }_{j} \) near \( x \) , we can consider \( {s}_{1},\ldots ,{s}_{n} \) as sections of \( \zeta \) . The corresponding local curvature matrix is diagonal:

\[
\Omega  = \operatorname{diag}\left( {{\Omega }_{1},\ldots ,{\Omega }_{n}}\right) ,
\]

and hence

\[
\underline{\mathrm{c}}\left( \Omega \right)  = \underline{\mathrm{c}}\left( {\Omega }_{1}\right) \ldots \underline{\mathrm{c}}\left( {\Omega }_{n}\right) .
\]

It follows that the corresponding global exterior forms have the same property

\[
\underline{\mathrm{c}}\left( K\right)  = \underline{\mathrm{c}}\left( {K}_{1}\right) \ldots \underline{\mathrm{c}}\left( {K}_{n}\right) .
\]

But the right side of this equation represents the total Chern classes

\[
\mathrm{c}\left( {\zeta }_{1}\right) \ldots \mathrm{c}\left( {\zeta }_{n}\right)  = \mathrm{c}\left( \zeta \right) .
\]

Thus the equality \( \mathrm{c}\left( \zeta \right)  = \left( {\underline{\mathrm{c}}\left( K\right) }\right) \) is true for any bundle \( \zeta \) which is a Whitney sum of line bundles.

The general case now follows by a standard argument. (Compare [Hir53, Section 4.2] or the uniqueness proof for Stiefel-Whitney classes in Section 7.) If \( {\gamma }^{1} \) denotes the universal line bundle over \( {\mathbb{P}}_{m}\left( \mathbb{C}\right) \) with \( m \) large, then the \( n \) -fold cross product of copies of \( {\gamma }^{1} \) satisfies

\[
\mathrm{c}\left( {{\gamma }^{1} \times  \ldots  \times  {\gamma }^{1}}\right)  = \left( {\underline{\mathrm{c}}\left( {K\left( {{\gamma }^{1} \times  \ldots  \times  {\gamma }^{1}}\right) }\right) }\right) .
\]

Since the cohomology of the base space \( {\operatorname{Gr}}_{n}\left( {\mathbb{C}}^{\infty }\right) \) of the universal bundle \( {\gamma }^{n} \) maps monomorphically into the cohomology of \( {\mathbb{P}}_{m}\left( \mathbb{C}\right)  \times  \ldots  \times  {\mathbb{P}}_{m}\left( \mathbb{C}\right) \) in dimensions \( \leq  {2m} \) , it follows that

\[
\mathrm{c}\left( {\gamma }^{n}\right)  = \left( {\underline{\mathrm{c}}\left( {K\left( {\gamma }^{n}\right) }\right) }\right) .
\]

Therefore \( \mathrm{c}\left( \zeta \right)  = \left( {\underline{\mathrm{c}}\left( {K\left( \zeta \right) }\right) }\right) \) for an arbitrary bundle \( \zeta \) .

Corollary C.10. For any real vector bundle \( \xi \) the de Rham cocycle \( {\sigma }_{2k}\left( K\right) \) represents the cohomology class \( {\left( 2\pi \right) }^{2k}{\mathrm{p}}_{k}\left( \xi \right) \) in \( {\mathrm{H}}^{4k}\left( {M;\mathbb{R}}\right) \) while \( {\sigma }_{{2k} + 1}\left( K\right) \) is a coboundary.

Proof. In other words the total Pontrjagin class \( 1 + {\mathrm{p}}_{1}\left( \xi \right)  + {\mathrm{p}}_{2}\left( \xi \right)  + \ldots \) in \( {\mathrm{H}}^{ \oplus  }\left( {M;\mathbb{R}}\right) \) corresponds to the invariant polynomial \( \mathrm{p}\left( A\right)  = \det \left( {I + A/{2\pi }}\right) \) . This follows immediately from the Theorem together with thedefinition of Pontrjagin classes.

Remark. Here is a direct proof that \( {\sigma }_{{2k} + 1}\left( K\right) \) is a coboundary. Choose a Euclidean metric on \( \xi \) , and choose a compatible connection \( \nabla \) . Then the connection matrix with respect to a local orthonormal basis for sections is skew symmetric, and it follows easily that the associated curvature matrix \( \Omega \) is skew also, \( {\Omega }^{t} =  - \Omega \) . Therefore

\[
{\sigma }_{m}\left( \Omega \right)  = {\sigma }_{m}\left( {\Omega }^{t}\right)  = {\left( -1\right) }^{m}{\sigma }_{m}\left( \Omega \right) .
\]

Thus \( {\sigma }_{m}\left( {K}_{\nabla }\right) \) is zero as a cocycle for \( m \) odd. For an arbitrary (non-metric) connection \( {\nabla }^{\prime } \) ; it follows that \( {\sigma }_{m}\left( {K}_{{\nabla }^{\prime }}\right) \) is a coboundary.

Corollary C.11. If a real [or complex] vector bundle possesses a flat connection then all of its Pontrjagin [or Chern] classes with rational coefficients are zero.

Proof. The proof is clear.

Remark. If the homology \( {\mathrm{H}}_{ * }\left( {M;\mathbb{Z}}\right) \) with integer coefficients is finitely generated, then it also follows that the Pontrjagin [or Chern] classes with integer coefficients are torsion elements. These torsion elements are not zero in general. [BH72b] have recently constructed a real [or complex] vector bundle with discrete structural group whose Pontrjagin [or Chern] classes in \( {\mathrm{H}}^{ * }\left( {B;\mathbb{Z}}\right) \) are non-torsion elements which satisfy no polynomial relations. Of course the homology \( {\mathrm{H}}_{ * }\left( {B;\mathbb{Z}}\right) \) cannot be finitely generated.

One piece of information is conspicuously absent in the above discussion. We do not have any expression for the Euler class of an oriented \( {2n} \) -plane bundle in terms of curvature (except for a very special construction in the case \( n = 1 \) ). This is not just an accident. We will see later by an example that there cannot be any formula for the Euler class in terms of the curvature of an arbitrary connection. The situation changes, however, if the connection is required to be compatible with a Euclidean metric on \( \xi \) .

The following classical construction will be needed.

Lemma C.12. There exists one and up to sign only one polynomial with integer coefficients which assigns, to each \( {2n} \times  {2n} \) skew-symmetric matrix \( A \) over a commutative ring, a ring element \( {Pf}\left( A\right) \) whose square is the determinant of \( A \) . Furthermore

\[
{Pf}\left( {{BA}{B}^{t}}\right)  = {Pf}\left( A\right) \det \left( B\right)
\]

for any \( {2n} \times  {2n} \) matrix \( B \) .

We will specify the sign by requiring that \( \operatorname{Pf}\left( {\operatorname{diag}\left( {S,\ldots , S}\right) }\right)  =  + 1 \) , where \( S \) denotes the \( 2 \times  2 \) matrix \( \left\lbrack  \begin{matrix} 0 & 1 \\   - 1 & 0 \end{matrix}\right\rbrack \) . The resulting polynomial \( {Pf} \) is called the Pfaffian. As examples,

\[
{Pf}\left\lbrack  \begin{matrix} 0 & a \\   - a & 0 \end{matrix}\right\rbrack   = a
\]

and the Pfaffin of a \( 4 \times  4 \) skew matrix \( \left\lbrack  {a}_{ij}\right\rbrack \) equals \( {a}_{12}{a}_{34} - {a}_{13}{a}_{24} + {a}_{14}{a}_{23} \) .

Proof. To prove \( {}^{1} \) Lemma C.12, we will work in the ring

\( \Lambda  = \mathbb{Z}\left\lbrack  {{A}_{12},\ldots ,{A}_{\left( {{2n} - {12}}\right) , n},{B}_{11},\ldots ,{B}_{{2n},{2n}}}\right\rbrack \) in which all of the above diagonal entries of the skew matrix \( A = \left\lbrack  {A}_{ij}\right\rbrack \) and all of the entries of \( B = \left\lbrack  {B}_{ij}\right\rbrack \) are distinct indeterminates. Over the quotient field of \( \Lambda \) , it is not difficult to find a matrix \( X \) so that \( {XA}{X}^{t} = \operatorname{diag}\left( {S,\ldots , S}\right) \) . Hence the polynomial \( \det \left( A\right)  \in  \Lambda \) is equal to a square \( \det {\left( A\right) }^{-2} \) in the quotient field of \( \Lambda \) . Since \( \Lambda \) is a unique factorization domain, this implies that \( \det \left( A\right) \) is a square already within \( \Lambda \) .

Similarly, the identity \( \det \left( {{BA}{B}^{t}}\right)  = \det \left( A\right) \det {\left( B\right) }^{2} \) implies that

\[
{Pf}\left( {{BA}{B}^{t}}\right)  =  \pm  {Pf}\left( A\right) \det \left( B\right) ,
\]

and specialising to \( B = I \) we see that the sign must be +1 .

Now let \( \xi \) be an oriented \( {2n} \) -plane bundle with Euclidean metric. Choosing an oriented orthonormal basis for the sections of \( \xi \) throughout a coordinate neighborhood \( U \) , the curvature matrix \( \Omega  = \left\lbrack  {\Omega }_{ij}\right\rbrack \) is skew-symmetric, so

\[
{Pf}\left( \Omega \right)  \in  {C}^{\infty }\left( {{\Lambda }^{2n}{\tau }^{ * }{\left. \right| }_{U}}\right)
\]

---

\( {}^{1} \) For details, see [Bou98, chapter 9, p. 82]

---

is defined. Choosing a different oriented basis for the sections over \( U \) , this exterior form will be replaced by \( {Pf}\left( {{X\Omega }{X}^{-1}}\right) \) where the matrix \( X \) is orthogonal

\( \left( {{X}^{-1} = {X}^{t}}\right) \) and orientation preserving \( \left( {\det X = 1}\right) \) . Hence the Pfaffian is unchanged. Thus we can piece these local forms together to obtain a global \( {2n} \) -form

\[
{Pf}\left( K\right)  \in  {C}^{\infty }\left( {{\Lambda }^{2n}{\tau }^{ * }}\right) .
\]

(As an example, for \( n = 2 \) we recover the statement that the Gauss-Bonnet 2- form \( {\Omega }_{12} = {Pf}\left( K\right) \) is globally well defined.) Just as in the previous case, one can verify that the matrix of formal partial derivatives \( \left\lbrack  {\partial {Pf}\left( A\right) /\partial {A}_{ij}}\right\rbrack \) commutes with \( A \) , and hence that

\[
\mathrm{d}{Pf}\left( K\right)  = 0.
\]

Thus \( {Pf}\left( K\right) \) represents a characteristic cohomology class in \( {\mathrm{H}}^{2n}\left( {M;\mathbb{R}}\right) \) . Passing to a bundle \( \widetilde{\gamma } \) which is universal in dimensions \( \leq  {4n} \) , since the square of \( {Pf}\left( {K\left( \widetilde{\gamma }\right) }\right) \) represents the cohomology class

\[
\det \left( {K\left( \widetilde{\gamma }\right) }\right)  = {\left( 2\pi \right) }^{2n}{\mathrm{p}}_{n}\left( \widetilde{\gamma }\right) ,
\]

we see that

\[
\left( {\operatorname{Pf}\left( {K\left( \widetilde{\gamma }\right) }\right) }\right)  =  \pm  {\left( 2\pi \right) }^{n}\operatorname{e}\left( \widetilde{\gamma }\right)
\]

and hence that \( \left( {{Pf}\left( {K\left( \xi \right) }\right) }\right)  =  \pm  {\left( 2\pi \right) }^{n}\mathrm{e}\left( \xi \right) \) for any oriented \( {2n} \) -plane bundle \( \xi \) . In fact, the sign is +1, as can be verified by evaluating both sides for a Whitney sum of 2-plane bundles. Thus we have proved the following.

Theorem (Generalized Gauss-Bonnet Theorem). For any oriented \( {2n} \) -plane bundle \( \xi \) with Euclidean metric and any compatible connection, the exterior \( {2n} \) -form \( {Pf}\left( {K/{2\pi }}\right) \) represents the Euler class \( \mathrm{e}\left( \xi \right) \) .

Remark. This theorem helps to illustrate the general Chern-Weil result that for any compact Lie group \( G \) with Lie algebra \( \mathfrak{g} \) , the cohomology \( {\mathrm{H}}^{ \oplus  }\left( {{B}_{G};\mathbb{R}}\right) \) of the classifying space is isomorphic to the algebra consisting of all polynomial functions \( \mathfrak{g} \rightarrow  \mathbb{R} \) which are invariant under the adjoint action of \( G \) . This general assertion fails for non-compact groups such as \( \operatorname{SL}\left( {{2n},\mathbb{R}}\right) \) .

As an example, suppose that \( {\tau }^{ * } \) is the dual tangent bundle of the unit sphere \( {S}^{2n} \) , with the Levi-Civita connection. Choosing an oriented, orthonormal basis \( {\theta }_{1},\ldots ,{\theta }_{n} \) for the sections of \( {\left. {\tau }^{ * }\right| }_{U} \) , computation shows that

\[
- {\Omega }_{ij} = {\theta }_{i} \land  {\theta }_{j}.
\]

(This equation expresses the fact that the "sectional curvature" of the unit sphere is identically equal to +1 .) Furthermore

\[
{\left( -1\right) }^{n}\operatorname{Pf}\left( \Omega \right)  = \operatorname{Pf}\left\lbrack  {{\theta }_{i} \land  {\theta }_{j}}\right\rbrack   = \left( {1 \cdot  3 \cdot  5 \cdot  7 \cdot  \ldots  \cdot  \left( {{2n} - 1}\right) }\right) {\theta }_{1} \land  \ldots  \land  {\theta }_{2n}.
\]

Integrating over \( {S}^{2n} \) , this yields

\[
\int {Pf}\left( K\right)  = \left( {1 \cdot  3 \cdot  5 \cdot  \ldots  \cdot  \left( {{2n} - 1}\right) }\right) \operatorname{volume}\left( {S}^{2n}\right) .
\]

Setting this expression equal to \( {\left( 2\pi \right) }^{n}\mathrm{e}\left\lbrack  {S}^{2n}\right\rbrack   = 2{\left( 2\pi \right) }^{n} \) , we obtain a novel proof for the identity:

\[
\operatorname{volume}\left( {S}^{2n}\right)  = \frac{2{\left( 2\pi \right) }^{n}}{1 \cdot  3 \cdot  5 \cdot  \ldots  \cdot  \left( {{2n} - 1}\right) }.
\]

To conclude this appendix, we will show that the Euler class cannot be determined by the curvature tensor of an arbitrary (non-metric) connection. In fact we will describe an example of an oriented vector bundle with flat connection such that the Euler class with real coefficients is non-zero. (Compare [Mil58] and [Woo71]) Suppose that we are given a homomorphism from the fundamental group \( \Pi  = {\pi }_{1}\left( M\right) \) to the special linear group \( \operatorname{SL}\left( {n,\mathbb{R}}\right) \) . Then \( \Pi \) acts on the universal group covering \( \widetilde{M} \) and hence acts diagonally on the product \( \widetilde{M} \times  {\mathbb{R}}^{n} \) . It is not hard to see that the natural mapping

\[
\left( {\widetilde{M} \times  {\mathbb{R}}^{n}}\right) /\Pi  \rightarrow  \widetilde{M}/\Pi  \cong  M
\]

is the projection map of an \( n \) -plane bundle \( \xi \) with flat connection (or equivalently, with discrete structural group). We will divise such an example with \( \mathrm{e}\left( \xi \right)  \neq  0 \) .

Let \( M \) be a compact Riemann surface of genus \( g > 1 \) . Then the universal covering \( \widetilde{M} \) is conformally diffeomorphic to the complex upper half plane \( H \) . (See for example [Spr01].) Every element in the group \( \Pi \) of covering transformations corresponds to a fractional linear transformation of \( H \) of the form

\[
z \mapsto  \frac{{az} + b}{{cz} + d}
\]

where the matrix

\[
\left\lbrack  \begin{array}{ll} a & b \\  \mathrm{c} & d \end{array}\right\rbrack   \in  \mathrm{{SL}}\left( {2,\mathbb{R}}\right)
\]

is well defined up to sign. Thus we have constructed a homomorphism \( h \) from \( \Pi \) to the quotient group

\[
\operatorname{PSL}\left( {2,\mathbb{R}}\right)  = \operatorname{SL}\left( {2,\mathbb{R}}\right) /\{  \pm  I\} .
\]

We will show that \( h \) lifts to a homomorphism \( \Pi  \rightarrow  \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) which induces the required 2-plane bundle over \( M \) . The group \( \operatorname{PSL}\left( {2,\mathbb{R}}\right) \) operates naturally on the real projective line \( {\mathbb{P}}^{1}\left( \mathbb{R}\right) \) which can be identified with the boundary \( \mathbb{R} \cup  \infty \) of \( H \) . Hence \( h \) induces a bundle \( \eta \) over \( M \) with fiber \( {\mathbb{P}}^{1}\left( \mathbb{R}\right) \) and projection map

\[
\left( {\widetilde{M} \times  {\mathbb{P}}^{1}\left( \mathbb{R}\right) }\right) /\Pi  \rightarrow  \widetilde{M}/\Pi  \cong  M.
\]

We will think of \( \eta \) as a bundle whose structural group is the group \( \operatorname{PSL}\left( {2,\mathbb{R}}\right) \) with the discrete topology. This induces bundle \( \eta \) can be identified with the tangent circle bundle of \( M \) . In fact, every non-zero tangent vector \( v \) at a point \( z \) of \( H \) is tangent to a unique oriented circle segment (or vertical line segment) which leads from \( z \) to a point \( f\left( {z, v}\right) \) on the boundary \( \mathbb{R} \cup  \infty \) , and which crosses this boundary orthogonally. (See Figure 12.) The mapping \( f \) is invariant under the action of \( \Pi \) (that is, \( f\left( {{\sigma z}, D{\sigma }_{z}\left( v\right) }\right)  = {\sigma f}\left( {z, v}\right) \) for \( \sigma  \in  \Pi \) ), and therefore induces the required isomorphism from the bundle of tangent directions on \( M \) to the \( \left( {\mathbb{R} \cup  \infty }\right) \) -bundle \( \eta \) . (Notation as on p. 18.) It follows that the Euler number, Euler characteristic or Euler number \( \mathrm{e}\left( \eta \right) \left\lbrack  M\right\rbrack \) is equal to \( 2 - {2g} \neq  0 \) .

Let \( {E}_{0} \) be the total space of \( \eta \) , and \( E \) be the total space of the associated topological 2-disk bundle. Since \( \mathrm{e}\left( \eta \right) \) is divisible by 2, it follows that \( {\mathrm{w}}_{2}\left( \eta \right)  = 0 \) . Hence, from the exact sequence of the pair \( \left( {E,{E}_{0}}\right) \) it follows that the fundamental class \( u \in  {\mathrm{H}}^{2}\left( {E,{E}_{0};\mathbb{Z}/2}\right) \) lifts back to a cohomology class \( a \in  {\mathrm{H}}^{1}\left( {{E}_{0};\mathbb{Z}/2}\right) \) whose restriction to each fiber is non-zero. Let \( E \rightarrow  {E}_{0} \) be the 2 -fold covering space associated with this cohomology class \( a \) . Then the composition \( {\widehat{E}}_{0} \rightarrow  {E}_{0} \rightarrow  M \) constitutes a new circle bundle \( \widehat{\eta } \) over \( M \) . Using for example the obstruction definition, we see that \( \mathrm{e}\left( \widehat{\eta }\right)  = \frac{1}{2}\mathrm{e}\left( \eta \right) \) . Thus the Euler number of \( \widehat{\eta } \) is \( 1 - g \neq  0 \) .

![bo_d7du9galb0pc73deir9g_315_364_468_1019_350_0.jpg](images/bo_d7du9galb0pc73deir9g_315_364_468_1019_350_0.jpg)

Figure 12

The structural group of this new bundle \( \widehat{\eta } \) is evidently the 2 -fold covering group \( \operatorname{SL}\left( {2,\mathbb{R}}\right) \) of \( \operatorname{PSL}\left( {2,\mathbb{R}}\right) \) , acting on the 2-fold covering of \( {\mathbb{P}}_{1}\left( \mathbb{R}\right) \) . (This is clear since PSL \( \left( {2,\mathbb{R}}\right) \) actually has the same homotopy type as the space \( {\mathbb{P}}_{1}\left( \mathbb{R}\right) \) upon which it acts.) But \( \eta \) has discrete structural group, so \( \widehat{\eta } \) does also. Hence \( \widehat{\eta } \) is induced by a suitable homomorphism \( \Pi  \rightarrow  \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) . The associated 2-plane bundle evidently has a flat connection, and has Euler number \( 1 - g \neq  0 \) .
