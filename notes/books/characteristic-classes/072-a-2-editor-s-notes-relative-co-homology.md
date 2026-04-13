# A.2 Editor's notes: Relative (co)homology

Definition (Relative Homology). Let \( \left( {X, A}\right) \) be a pair of topological spaces. This means there is an inclusion \( A\overset{\iota }{ \rightarrow  }X \) . Then there is an induced map by post composition \( {\iota }_{ * } : {C}_{n}\left( {A;\Lambda }\right)  \rightarrow  {C}_{n}\left( {X;\Lambda }\right) \) . Identifying \( {C}_{n}\left( {A;\Lambda }\right) \) as a submodule of \( {C}_{n}\left( {X,\Lambda }\right) \) , we define

\[
{C}_{n}\left( {X, A;\Lambda }\right)  = {C}_{n}\left( {X,\Lambda }\right) /{C}_{n}\left( {A;\Lambda }\right)
\]

as the relative relative chain group of \( \left( {X, A}\right) \) . We have an induced map

\[
\overline{\partial } : {C}_{n + 1}\left( {X, A;\Lambda }\right)  \rightarrow  {C}_{n}\left( {X, A;\Lambda }\right) .
\]

We define the relative homology

\[
{\mathrm{H}}_{n}\left( {X, A;\Lambda }\right)  = {Z}_{n}\left( {X, A;\Lambda }\right) /{B}_{n}\left( {X, A;\Lambda }\right)
\]

where \( {Z}_{n}\left( {X, A;\Lambda }\right)  = \ker \left( {\overline{\partial } : {C}_{n}\left( {X, A;\Lambda }\right)  \rightarrow  {C}_{n - 1}\left( {X, A;\Lambda }\right) }\right) \) are the relative cycles and \( {B}_{n}\left( {X, A;\Lambda }\right)  = \overline{\partial }\left( {{C}_{n + 1}\left( {X, A;\Lambda }\right) }\right) \) are the relative boundaries.

We can define relative cohomology similarly, see [Hat02, p. 199] for details.

Theorem (Long exact homology of (co)homology). For a triple of CW-complexes \( \left( {X, A, B}\right) \) , i.e. \( B \subset  A \subset  X \) , there exists a long exact sequence

\[
\cdots  \rightarrow  {\mathrm{H}}_{n}\left( {A, B;\Lambda }\right)  \rightarrow  {\mathrm{H}}_{n}\left( {X, B;\Lambda }\right)  \rightarrow  {\mathrm{H}}_{n}\left( {X, A;\Lambda }\right) \overset{\partial }{ \rightarrow  }{\mathrm{H}}_{n - 1}\left( {A, B;\Lambda }\right)  \rightarrow  \cdots
\]

and one of cohomology

\[
\cdots  \rightarrow  {\mathrm{H}}^{n}\left( {X, A;\Lambda }\right)  \rightarrow  {\mathrm{H}}^{n}\left( {X, B;\Lambda }\right)  \rightarrow  {\mathrm{H}}^{n}\left( {A, B;\Lambda }\right) \overset{\delta }{ \rightarrow  }{\mathrm{H}}^{n + 1}\left( {X, A;\Lambda }\right)  \rightarrow  \cdots .
\]

Specializing to \( B = \varnothing \) , we get what is known as the long exact sequence of a pair \( \left( {X, A}\right) \) .

Explicitly, let \( \left\lbrack  \alpha \right\rbrack   \in  {\mathrm{H}}_{n}\left( {X, A;\Lambda }\right) \) be the class of a relative cycle. Then

\[
\partial \left\lbrack  \alpha \right\rbrack   = \left\lbrack  {\partial \alpha }\right\rbrack   \in  {\mathrm{H}}_{n - 1}\left( {A, B}\right) .
\]

Similarly for \( \left\lbrack  \alpha \right\rbrack   \in  {\mathrm{H}}^{n}\left( {A, B;\Lambda }\right) \) ,

\[
\delta \left\lbrack  \alpha \right\rbrack   = \left\lbrack  {\delta \alpha }\right\rbrack   \in  {\mathrm{H}}^{n + 1}\left( {X, A;\Lambda }\right) .
\]

For proof and more details, see [Hat02, p. 113, 199].

Theorem (Excision). For a pair of CW-complexes \( \left( {X, A}\right) \) , we have a natural isomorphism

\[
{\mathrm{H}}_{n}\left( {X, A;\Lambda }\right)  \cong  {\mathrm{H}}_{n}\left( {X/A, A/A;\Lambda }\right)
\]

This is called the excision isomorphism. The same statement with cohomology also holds.

For proof, see [Hat02, p. 119].

This is equivalent to saying this: if \( A, B \subset  X \) are CW-complexes and \( A \cup  B = X \) , then

\[
{\mathrm{H}}_{n}\left( {X, A}\right)  \cong  {\mathrm{H}}_{n}\left( {B, A \cap  B}\right) \text{ . }
\]

This is also called the excision isomorphism.
