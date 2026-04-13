# A.1 Basic Definitions

The standard \( n \) -simplex is the convex set \( {\Delta }^{n} \subset  {\mathbb{R}}^{n + 1} \) consisting of all \( \left( {n + 1}\right) \) -tuples \( \left( {{t}_{0},\ldots ,{t}_{n}}\right) \) of real numbers with

\[
{t}_{i} \geq  0,\;{t}_{0} + {t}_{1} + \ldots  + {t}_{n} = 1.
\]

Any continuous map from \( {\Delta }^{n} \) to a topological space \( X \) is called a singular \( n - \) simplex in \( X \) . The \( i \) -th face of a singular \( n \) -simplex \( \sigma  : {\Delta }^{n} \rightarrow  X \) is the singular \( \left( {n - 1}\right) \) -simplex

\[
\sigma  \circ  {\phi }_{i} : {\Delta }^{n - 1} \rightarrow  X
\]

where the linear imbedding \( {\phi }_{i} : {\Delta }^{n - 1} \rightarrow  {\Delta }^{n} \) is defined by

\[
{\phi }_{i}\left( {{t}_{0},\ldots ,{t}_{i - 1},{t}_{i + 1},\ldots ,{t}_{n}}\right)  = \left( {{t}_{0},\ldots ,{t}_{i - 1},0,{t}_{i + 1},\ldots ,{t}_{n}}\right) .
\]

For each \( n \geq  0 \) the singular chain group \( {C}_{n}\left( {X;\Lambda }\right) \) with coefficients in a commutative ring \( \Lambda \) is the free \( \Lambda \) -module having one generator \( \left\lbrack  \sigma \right\rbrack \) for each singular \( n \) -simplex \( \sigma \) in \( X \) . For \( n < 0 \) , the group \( {C}_{n}\left( {X;\Lambda }\right) \) is defined to be zero. The boundary homomorphism

\[
\partial  : {C}_{n}\left( {X;\Lambda }\right)  \rightarrow  {C}_{n - 1}\left( {X;\Lambda }\right)
\]

is defined by

\[
\partial \left\lbrack  \sigma \right\rbrack   = \left\lbrack  {\sigma  \circ  {\phi }_{0}}\right\rbrack   - \left\lbrack  {\sigma  \circ  {\phi }_{1}}\right\rbrack   + \ldots  + {\left( -1\right) }^{n}\left\lbrack  {\sigma  \circ  {\phi }_{n}}\right\rbrack  .
\]

The identity \( \partial  \circ  \partial  = 0 \) is easily verified. Hence we can define the \( n \) -th singular homology group \( {\mathrm{H}}_{n}\left( {X;\Lambda }\right) \) to be the quotient module \( {Z}_{n}\left( {X;\Lambda }\right) /{B}_{n}{\left( X;\Lambda \right) }^{1} \) , where \( {Z}_{n}\left( {X;\Lambda }\right) \) is the kernel of \( \partial  : {C}_{n}\left( {X;\Lambda }\right)  \rightarrow  {C}_{n - 1}\left( {X;\Lambda }\right) \) and \( {B}_{n}\left( {X;\Lambda }\right) \) is the image of \( \partial  : {C}_{n + 1}\left( {X;\Lambda }\right)  \rightarrow  {C}_{n}\left( {X;\Lambda }\right) \) . Here and elsewhere the word "group" is used, although "left \( \Lambda \) -module" is really meant.

The cochain group \( {C}^{n}\left( {X;\Lambda }\right) \) is defined to be the dual module

\( {\operatorname{Hom}}_{\Lambda }\left( {{C}_{n}\left( {X;\Lambda }\right) ,\Lambda }\right) \) consisting of all \( \Lambda \) -linear maps from \( {C}_{n}\left( {X;\Lambda }\right) \) to \( \Lambda \) . The value of a cochain \( c \) on a chain \( \gamma \) will be denoted by \( \langle c,\gamma \rangle  \in  \Lambda \) . The coboundary of a cochain \( c \in  {C}^{n}\left( {X;\Lambda }\right) \) is defined to be the cochain \( {\delta c} \in  {C}^{n + 1}\left( {X;\Lambda }\right) \) whose value on each \( \left( {n + 1}\right) \) -chain \( \alpha \) is determined by the identity

\[
\langle {\delta c},\alpha \rangle  + {\left( -1\right) }^{n}\langle c,\partial \alpha \rangle  = 0.
\]

Thus we obtain corresponding modules

\[
{\mathrm{H}}^{n}\left( {X;\Lambda }\right)  = {Z}^{n}\left( {X;\Lambda }\right) /{B}^{n}\left( {X;\Lambda }\right)  = \left( {\ker \delta }\right) /\delta {C}^{n - 1}\left( {X;\Lambda }\right)
\]

which are called the singular cohomology groups of \( {X}^{2} \) .

Remark. The choice of sign in this formula is based upon the following convention. Whenever two symbols of dimension \( m \) and \( n \) are permuted, the sign \( {\left( -1\right) }^{mn} \) will be introduced. Here the operators \( \partial \) and \( \delta \) are considered to have dimension \( \pm  1 \) . Thus our sign conventions are the same as those of [Mac75] and [Dol95], but different from those of [ES52] and [Spa81].

---

\( {}^{1} \) Editor’s note: The elements of \( {Z}_{n}\left( {X;\Lambda }\right) \) are called cycles and the elements of \( {B}_{n}\left( {X;\Lambda }\right) \) are called boundaries. In this language we say homology is cycles modded out by boundaries.

\( {}^{2} \) Editor’s note: The elements of \( {Z}^{n}\left( {X;\Lambda }\right) \) are called cocycles and the elements of \( {B}^{n}\left( {X;\Lambda }\right) \) are called coboundaries. In this language cohomology is cocycles modded out by coboundaries.

---

In some contexts, notably in obstruction theory, it is important to consider cohomology with coefficients in an arbitrary \( \Lambda \) -module. However in this appendix we consider only cohomology with coefficients in the ring \( \Lambda \) itself.
