# A.8 The Fundamental Homology Class of a Manifold

We will now use the infinite cyclic group \( \mathbb{Z} \) as coefficient domain. For each \( x \in  M \) , recall that

\[
{\mathrm{H}}_{i}\left( {M, M - x;\mathbb{Z}}\right)  \cong  {\mathrm{H}}_{i}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - 0;\mathbb{Z}}\right)
\]

is infinite cyclic for \( i = n \) and is zero for \( i \neq  n \) .

Definition. A local orientation \( {\mu }_{x} \) for \( M \) at \( x \) is a choice of one of the two possible generators for \( {\mathrm{H}}_{n}\left( {M, M - x;\mathbb{Z}}\right) \) .

Note that such a \( {\mu }_{x} \) determines local orientations \( {\mu }_{y} \) for all points \( y \) in a small neighborhood of \( x \) . To be precise, if \( B \) is a ball around \( x \) (in terms of some local coordinate system), then for each \( y \in  B \) the isomorphisms

\[
{\mathrm{H}}_{ \bullet  }\left( {M, M - x}\right) \overset{{\rho }_{x}}{ \leftarrow  }{\mathrm{H}}_{ \bullet  }\left( {M, M - B}\right) \overset{{\rho }_{y}}{ \rightarrow  }{\mathrm{H}}_{ \bullet  }\left( {M, M - y}\right)
\]

determines a local orientation \( {\mu }_{y} \) .

Definition. An orientation for \( M \) is a function which assigns to each \( x \in  M \) a local orientation \( {\mu }_{x} \) which "varies continuously" with \( x \) , in the following sense: For each \( x \) there should exist a compact neighborhood \( N \) and a class \( {\mu }_{N} \in  {\mathrm{H}}_{n}\left( {M, M - N}\right) \) so that \( {\rho }_{y}\left( {\mu }_{N}\right)  = {\mu }_{y} \) for each \( y \in  N \) .

The pair consisting of manifold and orientation is called an oriented manifold.

Theorem A.8. For any oriented manifold \( M \) and any compact \( K \subset  M \) , there is one and only one class \( {\mu }_{K} \in  {\mathrm{H}}_{n}\left( {M, M - K}\right) \) which satisfies \( {\rho }_{x}\left( {\mu }_{K}\right)  = {\mu }_{x} \) for each \( x \in  K \) .

In particular, if \( M \) is itself compact, then there is one and only one \( {\mu }_{M} \in \; {\mathrm{H}}_{n}M \) with the required property. This class \( \mu  = {\mu }_{M} \) is called the fundamental homology class of \( M \) .

Proof of A.8. The uniqueness of \( {\mu }_{K} \) follows immediately from Lemma A.7. The existence proof will be divided into three steps.

Case 1. If \( K \) is contained in a sufficiently small neighborhood of some given point, then the existence of \( {\mu }_{K} \) follows from the definition of orientation.

Case 2. Suppose that \( K = {K}_{1} \cup  {K}_{2} \) where \( {\mu }_{{K}_{1}} \) and \( {\mu }_{{K}_{2}} \) exist. As in A. 7 there is an exact sequence

\[
\ldots  \rightarrow  0 \rightarrow  {\mathrm{H}}_{n}\left( {M, M - K}\right) \overset{s}{ \rightarrow  }{\mathrm{H}}_{n}\left( {M, M - {K}_{1}}\right)  \oplus  {\mathrm{H}}_{n}\left( {M, M - {K}_{2}}\right) \overset{t}{ \rightarrow  }{\mathrm{H}}_{n}\left( {M, M - {K}_{1} \cap  {K}_{2}}\right)  \rightarrow  \ldots
\]

where

\[
s\left( \alpha \right)  = {\rho }_{{K}_{1}}\left( \alpha \right)  \oplus  {\rho }_{{K}_{2}}\left( \alpha \right) ,
\]

\[
t\left( {\beta  \oplus  \gamma }\right)  = {\rho }_{{K}_{1} \cap  {K}_{2}}\left( \beta \right)  - {\rho }_{{K}_{1} \cap  {K}_{2}}\left( \gamma \right) .
\]

Now \( t\left( {{\mu }_{{K}_{1}} \oplus  {\mu }_{{K}_{2}}}\right)  = 0 \) , by the uniqueness theorem applied to \( {K}_{1} \cap  {K}_{2} \) , hence \( {\mu }_{{K}_{1}} \oplus  {\mu }_{{K}_{2}} = s\left( \alpha \right) \) for some unique \( \alpha  \in  {\mathrm{H}}_{n}\left( {M, M - K}\right) \) . This \( \alpha \) is the required \( {\mu }_{K} \) .

Case 3. \( K \) arbitrary. Then \( K = {K}_{1} \cup  \ldots  \cup  {K}_{r} \) where the \( {\mu }_{{K}_{i}} \) exist by Case 1. The class \( {\mu }_{K} \) is now constructed by induction on \( r \) .

Remark 9. For any coefficient domain \( \Lambda \) , the unique homomorphism \( \mathbb{Z} \rightarrow  \Lambda \) gives rise to a class in \( {\mathrm{H}}_{n}\left( {M, M - K;\Lambda }\right) \) which will also be denoted by \( {\mu }_{K} \) . The case \( \Lambda  = \mathbb{Z}/2 \) is particularly important, since the mod 2 homology class

\[
{\mu }_{K} \in  {\mathrm{H}}_{n}\left( {M, M - K;\mathbb{Z}/2}\right)
\]

can be constructed directly for an arbitrary manifold, without making any assumption of orientability.

Remark 10. Similar considerations apply to an oriented manifold-with-boundary \( M \) . For each compact subset \( K \subset  M \) , there exists a unique class

\( {\mu }_{K} \in  {\mathrm{H}}_{n}\left( {M,\left( {M - K}\right)  \cup  \partial M}\right) \) with the property that \( {\rho }_{x}\left( {\mu }_{K}\right)  = {\mu }_{x} \) for each \( x \in  K \cap  \left( {M - \partial M}\right) \) . In particular, if \( M \) is compact, then there is a unique fundamental homology class \( {\mu }_{M} \in  {\mathrm{H}}_{n}\left( {M,\partial M}\right) \) with the required property. It can be shown that the natural homomorphism

\[
\partial  : {\mathrm{H}}_{n}\left( {M,\partial M}\right)  \rightarrow  {\mathrm{H}}_{n - 1}\left( {\partial M}\right)
\]

maps \( {\mu }_{M} \) to the fundamental homology class of \( \partial M \) . (Compare [Spa81, p. 304].)
