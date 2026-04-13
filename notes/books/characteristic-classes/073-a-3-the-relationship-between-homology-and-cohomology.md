# A.3 The Relationship between Homology and Cohomology

Henceforth we will assume that \( \Lambda \) is a principal ideal domain (for example the integers or a field). In order to simplify notation we will omit reference to \( \Lambda \) whenever possible, writing \( {\mathrm{H}}_{n}X \) in place of \( {\mathrm{H}}_{n}\left( {X;\Lambda }\right) \) for example. The abbreviated notation \( {\mathrm{H}}_{ * }X \) will often be used to denote the entire sequence of groups \( \left( {{\mathrm{H}}_{0}X,{\mathrm{H}}_{1}X,{\mathrm{H}}_{2}X,\ldots }\right) \) .

Theorem A.1. Suppose that \( {\mathrm{H}}_{n - 1}X \) is zero or is a free \( \Lambda \) -module. Then \( {\mathrm{H}}^{n}X \) is canonically isomorphic to the module \( {\operatorname{Hom}}_{\Lambda }\left( {{\mathrm{H}}_{n}X,\Lambda }\right) \) consisting of all \( \Lambda \) -linear maps from \( {\mathrm{H}}_{n}X \) to \( \Lambda \) . There is a corresponding assertion for pairs \( \left( {X, A}\right) \) .

(Compare [Mac75, p. 77] or [Spa81, p. 243].) Note that the hypothesis is always satisfied if \( \Lambda \) happens to be a field.

Proof. Given elements \( x \in  {\mathrm{H}}^{n}X \) and \( \xi  \in  {\mathrm{H}}_{n}X \) define the Kronecker index \( \langle x,\xi \rangle  \in  \Lambda \) as follows. Choose a representative cocycle \( z \in  {Z}^{n}X \) for \( x \) and a representative cycle \( \zeta  \in  {Z}_{n}X \) for \( \xi \) ; and set \( \langle x,\xi \rangle \) equal to \( \langle z,\xi \rangle  \in  \Lambda \) . The reader should verify that this does not depend on the choice of \( z \) and \( \zeta \) . Now define a homomorphism

\[
k : {\mathrm{H}}^{n}X \rightarrow  {\operatorname{Hom}}_{\Lambda }\left( {{\mathrm{H}}_{n}X,\Lambda }\right)
\]

by the identity \( k\left( x\right) \left( \xi \right)  = \langle x,\xi \rangle \) .

Proof that the homomorphism \( k \) is onto. First note that the submodule \( {Z}_{n}X \subset  {C}_{n}X \) is a direct summand. This follows from the fact that the quotient module

\[
{C}_{n}X/{Z}_{n}X \cong  {B}_{n - 1}X \subset  {C}_{n - 1}X
\]

is a submodule of a free module, and hence is free. (See for example [Kap18].) Therefore any homomorphism \( {Z}_{n}X \rightarrow  \Lambda \) can be extended over \( {C}_{n}X \) .

Let \( f \) be an arbitrary element of \( {\operatorname{Hom}}_{\Lambda }\left( {{\mathrm{H}}_{n}X,\Lambda }\right) \) . The composition

\[
{Z}_{n}X \rightarrow  {\mathrm{H}}_{n}X\overset{f}{ \rightarrow  }\Lambda
\]

extends to a homomorphism \( F : {C}_{n}X \rightarrow  \Lambda \) . Since \( F \) vanishes on boundaries, it follows that \( {\delta F} = 0 \) . Let \( x \in  {\mathrm{H}}^{n}X \) denote the cohomology class of the cocycle \( F \) . Then for any \( \xi  \in  {\mathrm{H}}_{n}X \) with representative \( \zeta  \in  {Z}_{n}X \) , we have

\[
\langle x,\xi \rangle  = F\left( \zeta \right)  = f\left( \xi \right) .
\]

Thus \( k\left( x\right)  = f \) , which proves that \( k \) is onto.

Proof that \( k \) has kernel zero: Let \( {z}_{0} \in  {Z}^{n}X \) be such that \( \left\langle  {{z}_{0},\zeta }\right\rangle   = 0 \) for all cycles \( \zeta  \in  {Z}_{n}X \) . We must prove that \( {z}_{0} \) is a coboundary.

Since \( {z}_{0} \) annihilates cycles, it follows that the composition \( {z}_{0}{\partial }^{-1} : {B}_{n - 1}X \rightarrow  \Lambda \) is well-defined. The quotient

\[
{Z}_{n - 1}X/{B}_{n - 1}X = {\mathrm{H}}_{n - 1}X
\]

is assumed to be free, so it follows that \( {B}_{n - 1}X \) is a direct summand of \( {Z}_{n - 1}X \) , and hence of \( {C}_{n - 1}X \) . Therefore the homomorphism \( {z}_{0}{\partial }^{-1} \) can be extended over \( {C}_{n - 1}X \) . Let

\[
f : {C}_{n - 1}X \rightarrow  \Lambda
\]

be such an extension; then

\[
\langle {\delta f},\left\lbrack  \sigma \right\rbrack  \rangle  =  \pm  \langle f,\partial \left\lbrack  \sigma \right\rbrack  \rangle  =  \pm  {z}_{0}{\partial }^{-1}\left( {\partial \left\lbrack  \sigma \right\rbrack  }\right)  =  \pm  \left\langle  {{z}_{0},\left\lbrack  \sigma \right\rbrack  }\right\rangle  .
\]

Thus \( \pm  {z}_{0} \) is equal to the coboundary of \( f \) , as required.
