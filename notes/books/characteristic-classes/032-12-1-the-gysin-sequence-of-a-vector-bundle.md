# 12.1 The Gysin Sequence of a Vector Bundle

Let \( \xi \) be an \( n \) -plane bundle with projection map \( \pi  : E \rightarrow  B \) . Restricting \( \pi \) to the space \( {E}_{0} \) of non-zero vectors in \( E \) , we obtain an associated projection map \( {\pi }_{0} : {E}_{0} \rightarrow  B \) .

Theorem 12.2. To any oriented \( n \) -plane bundle \( \xi \) there is associated an exact sequence of the form

\[
\cdots  \rightarrow  {\mathrm{H}}^{i}\left( B\right) \overset{ \smile  \mathrm{e}}{ \rightarrow  }{\mathrm{H}}^{i + n}\left( B\right) \overset{{\pi }_{0}^{ * }}{ \rightarrow  }{\mathrm{H}}^{i + n}\left( {E}_{0}\right)  \rightarrow  {\mathrm{H}}^{i + 1}\left( B\right) \overset{ \smile  \mathrm{e}}{ \rightarrow  }\cdots ,
\]

using integer coefficients.

Here the symbol \( \smile \) e stands for the homomorphism \( a \mapsto  a \smile  \mathrm{e}\left( \xi \right) \) .

Proof. Starting with the cohomology exact sequence

\[
\ldots  \rightarrow  {\mathrm{H}}^{j}\left( {E,{E}_{0}}\right)  \rightarrow  {\mathrm{H}}^{j}\left( E\right)  \rightarrow  {\mathrm{H}}^{j}\left( {E}_{0}\right) \overset{\delta }{ \rightarrow  }{\mathrm{H}}^{j + 1}\left( {E,{E}_{0}}\right)  \rightarrow  \ldots
\]

of the pair \( \left( {E,{E}_{0}}\right) \) , use the isomorphism

\[
\smile  u : {\mathrm{H}}^{j - n}\left( E\right)  \rightarrow  {\mathrm{H}}^{j}\left( {E,{E}_{0}}\right)
\]

of \( \text{ § }{10} \) , to substitute the isomorphic group \( {\mathrm{H}}^{j - n}\left( E\right) \) in place of \( {\mathrm{H}}^{j}\left( {E,{E}_{0}}\right) \) . Thus we obtain an exact sequence of the form

\[
\ldots  \rightarrow  {\mathrm{H}}^{j - n}\left( E\right) \overset{g}{ \rightarrow  }{\mathrm{H}}^{j}\left( E\right)  \rightarrow  {\mathrm{H}}^{j}\left( {E}_{0}\right)  \rightarrow  {\mathrm{H}}^{j - n + 1}\left( E\right)  \rightarrow  \ldots ,
\]

where

\[
g\left( x\right)  = {\left. \left( x \smile  u\right) \right| }_{E} = x \smile  \left( {\left. u\right| }_{E}\right) .
\]

Now substitute the isomorphic cohomology ring \( {\mathrm{H}}^{ * }\left( B\right) \) in place of \( {\mathrm{H}}^{ * }\left( E\right) \) . Since the cohomology class \( {\left. u\right| }_{E} \) in \( {\mathrm{H}}^{n}\left( E\right) \) corresponds to the Euler class in \( {\mathrm{H}}^{n}\left( B\right) \) , this yields the required exact sequence

\[
\cdots  \rightarrow  {\mathrm{H}}^{j - n}\left( B\right) \overset{ \smile  \mathrm{e}}{ \rightarrow  }{\mathrm{H}}^{j}\left( B\right)  \rightarrow  {\mathrm{H}}^{j}\left( {E}_{0}\right)  \rightarrow  {\mathrm{H}}^{j - n + 1}\left( B\right)  \rightarrow  \ldots
\]

Similarly, for an unoriented bundle, there is a corresponding exact sequence with mod 2 coefficients, using the Stiefel-Whitney class \( {\mathrm{w}}_{n}\left( \xi \right) \) in place of the Euler class. (Compare the proof of 11.3) As an example, consider the twisted line bundle \( {\gamma }_{n}^{1} \) over the projective space \( {\mathbb{P}}^{n} \) . Since the space \( {E}_{0}\left( {\gamma }_{n}^{1}\right) \) can be identified with \( {\mathbb{R}}^{n + 1} - 0 \) , it contains the unit sphere \( {S}^{n} \) as deformation retract. Thus we obtain an exact sequence

\[
\cdots  \rightarrow  {\mathrm{H}}^{j - 1}\left( {\mathbb{P}}^{n}\right) \xrightarrow[]{ \smile  {\mathrm{w}}_{1}}{\mathrm{H}}^{j}\left( {\mathbb{P}}^{n}\right)  \rightarrow  {\mathrm{H}}^{j}\left( {S}^{n}\right)  \rightarrow  {\mathrm{H}}^{j}\left( {\mathbb{P}}^{n}\right)  \rightarrow  \cdots
\]

with mod 2 coefficients, where \( {\mathrm{w}}_{1} = {\mathrm{w}}_{1}\left( {\gamma }_{n}^{1}\right) \) .

More generally, consider any 2-fold covering \( \widetilde{B} \rightarrow  B \) . That is assume that each point of \( B \) has an open neighborhood \( U \) whose inverse image consists of two disjoint open copies of \( U \) . Then we can construct a line bundle \( \xi \) over \( B \) whose total space \( E \) is obtained from \( \widetilde{E} \times  \mathbb{R} \) by identifying each pair \( \left( {x, t}\right) \) with \( \left( {{x}^{\prime }, - t}\right) \) , where \( x \) and \( {x}^{\prime } \) are the two distinct points of \( \widetilde{B} \) lying over one point of \( B \) . Evidently the open subset \( {E}_{0} \) contains \( \widetilde{B} \) as deformation retract. Thus we have proved the following.

Corollary 12.3. To any 2-fold \( \widetilde{B} \rightarrow  B \) there is associated an exact sequence of the form

\[
\ldots  \rightarrow  {\mathrm{H}}^{j - 1}\left( B\right) \xrightarrow[]{ \smile  {\mathrm{w}}_{1}}{\mathrm{H}}^{j}\left( B\right)  \rightarrow  {\mathrm{H}}^{j}\left( \widetilde{B}\right)  \rightarrow  {\mathrm{H}}^{j}\left( B\right)  \rightarrow  \ldots
\]

with mod 2 coefficients, where \( {\mathrm{w}}_{1} = {\mathrm{w}}_{1}\left( \xi \right) \) .
