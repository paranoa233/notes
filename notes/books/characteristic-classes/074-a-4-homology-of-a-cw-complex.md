# A.4 Homology of a CW-Complex

Let \( K \) be the underlying space of a CW-complex (compare Definition 6.1), and let \( {K}^{n} \subset  K \) denote the \( \mathbf{n} \) -skeleton, the union of all cells of dimension \( < n \) .

Lemma A.2. The relative homology group \( {\mathrm{H}}_{i}\left( {{K}^{n},{K}^{n - 1}}\right) \) with coefficients in \( \Lambda \) is zero for \( i \neq  n \) and is a free module for \( i = n \) with one generator for each \( n \) -cell of \( K \) .

It follows by Theorem A. 1 that the cohomology group \( {\mathrm{H}}^{i}\left( {{K}^{n},{K}^{n - 1}}\right) \) is also zero for \( i \neq  n \) .

Proof. We assume that the reader is familiar with the basic fact that the homology group \( {\mathrm{H}}_{i}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - 0}\right) \) is zero for \( i \neq  n \) , and is isomorphic to \( \Lambda \) when \( i = n \) . (See for example [Dol95, p. 56] and compare Theorem A. 5 below.)

Since the unit disk \( {D}^{n} \) is a deformation retract of \( {\mathbb{R}}^{n} \) and the unit sphere \( {S}^{n - 1} \) is a deformation retract of \( {\mathbb{R}}^{n} - 0 \) , the group \( {\mathrm{H}}_{i}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - 0}\right) \) is isomorphic to \( {\mathrm{H}}_{i}\left( {{D}^{n},{S}^{n - 1}}\right) \) , which is computed in [ES52, p. 45] or [Spa81, p. 45].

Let \( S \) denote a discrete set which consists of one point \( {s}_{E} \) from each open \( n \) -cell \( E \) of \( K \) . Then it is not difficult to see that \( {K}^{n - 1} \) is a deformation retract of \( {K}^{n} - S \) . Using the exact sequence of the triple \( \left( {{K}^{n},{K}^{n} - S,{K}^{n - 1}}\right) \) , it follows that

\[
{\mathrm{H}}_{i}\left( {{K}^{n},{K}^{n - 1}}\right)  \cong  {\mathrm{H}}_{i}\left( {{K}^{n},{K}^{n} - S}\right) .
\]

By excision this last group is isomorphic to \( {\mathrm{H}}_{i}\left( {\bigsqcup E,\bigsqcup \left( {E - {s}_{E}}\right) }\right) \) , where \( \bigsqcup E \) denotes the disjoint union of all \( n \) -cells of \( K \) . But the homology of such a disjoint union of open subsets of \( {K}^{n} \) is clearly the direct sum of the homology groups \( {\mathrm{H}}_{i}\left( {E, E - {s}_{E}}\right)  \cong  {\mathrm{H}}_{i}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - 0}\right) \) , and this last group is free on one generator for \( i = n \) and is zero otherwise.

Corollary A.3. The group \( {\mathrm{H}}_{i}{K}^{n} \) is zero for \( i > n \) and is isomorphic to \( {\mathrm{H}}_{i}K \) for \( i < n \) . Similar statements hold for cohomology.

Proof for homology. Certainly \( {\mathrm{H}}_{i}{K}^{0} = 0 \) for \( i > 0 \) . Using the exact sequence

\[
{\mathrm{H}}_{i}{K}^{n - 1} \rightarrow  {\mathrm{H}}_{i}{K}^{n} \rightarrow  {\mathrm{H}}_{i}\left( {{K}^{n},{K}^{n - 1}}\right)
\]

it follows by induction on \( n \) that \( {\mathrm{H}}_{i}{K}^{n} = 0 \) for \( i > n \) . If \( i < n \) , a similar sequence shows that \( {\mathrm{H}}_{i}{K}^{n} \cong  {\mathrm{H}}_{i}{K}^{n + 1} \) , and hence inductively that

\[
{\mathrm{H}}_{i}{K}^{n} \cong  {\mathrm{H}}_{i}{K}^{n + 1} \cong  {\mathrm{H}}_{i}{K}^{n + 2} \cong  \cdots
\]

If \( K \) is of finite dimension, this completes the proof. For the general case, it is necessary to appeal to the theorem that \( {\mathrm{H}}_{i}K \) is isomorphic to the direct limit as \( r \rightarrow  \infty \) of \( {\mathrm{H}}_{i}{K}^{r} \) . This is true since every singular simplex of \( K \) is contained in a compact subset, and hence is contained in some \( {K}^{r} \) . (Compare

[Whi61, Section 5(D)].)

Proof for cohomology. It follows similarly that the relative group \( {\mathrm{H}}_{i}\left( {K,{K}^{n}}\right) \) , being isomorphic to \( {\mathrm{H}}_{i}\left( {{K}^{n + 1},{K}^{n}}\right) \) , is zero for \( i \leq  n \) . Therefore \( {\mathrm{H}}^{i}\left( {K,{K}^{n}}\right)  = 0 \) for \( i \leq  n \) by Theorem A. 1 and using the cohomology exact sequence of this pair we see that \( {\mathrm{H}}^{i}\left( K\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{H}}^{i}\left( {K}^{n}\right) \) for \( i < n \) . The proof that \( {\mathrm{H}}^{i}\left( {K}^{n}\right)  = 0 \) for \( i > n \) is completely analogous to the corresponding proof for homology.

Definition. The free module \( {\mathrm{H}}_{n}\left( {{K}^{n},{K}^{n - 1}}\right) \) will be called the \( n \) -th chain group of the CW-complex \( K \) and will be denoted by \( {C}_{n}^{\mathrm{{CW}}}K = {C}_{n}^{\mathrm{{CW}}}\left( {K;\Lambda }\right) \) . Similarly the module

\[
{\mathrm{H}}^{n}\left( {{K}^{n},{K}^{n - 1}}\right)  \cong  {\operatorname{Hom}}_{\Lambda }\left( {{C}_{n}^{\mathrm{{CW}}}K,\Lambda }\right)
\]

will be called the \( n \) -th cochain group, and will be denoted by \( {C}_{\mathrm{{CW}}}^{n}K \) .

A "boundary" homomorphism \( {\partial }_{n} : {C}_{n + 1}^{\mathrm{{CW}}}K \rightarrow  {C}_{n}^{\mathrm{{CW}}}K \) is obtained by using the homology exact sequence of the triple \( \left( {{K}^{n + 1},{K}^{n},{K}^{n - 1}}\right) \) . Similarly \( {\delta }^{n} : {C}_{\mathrm{{CW}}}^{n}K \rightarrow  {C}_{\mathrm{{CW}}}^{n + 1}K \) is defined.

Theorem A.4. The homology group \( {Z}_{n}^{\mathrm{{CW}}}K/{B}_{n}^{\mathrm{{CW}}}K \) of the chain complex \( {C}_{ \bullet  }^{\mathrm{{CW}}}K \) is canonically isomorphic to \( {\mathrm{H}}_{n}K \) . Similarly the group \( {Z}_{\mathrm{{CW}}}^{n}K/{B}_{\mathrm{{CW}}}^{n}K \) obtained from the cochain complex \( {C}_{\mathrm{{CW}}}^{ \bullet  }K \) is canonically isomorphic to \( {\mathrm{H}}^{n}K \) .

Proof. Consider the following commutative diagram

![bo_d7du9galb0pc73deir9g_267_407_960_924_408_0.jpg](images/bo_d7du9galb0pc73deir9g_267_407_960_924_408_0.jpg)

The horizontal line is a portion of the homology exact sequence of the triple \( \left( {{K}^{n + 1},{K}^{n},{K}^{n - 2}}\right) \) , and the vertical line is a portion of the exact sequence of \( \left( {{K}^{n},{K}^{n - 1},{K}^{n - 2}}\right) \) . Evidently it follows from this diagram that

\[
{Z}_{n}^{\mathrm{{CW}}} \cong  {\mathrm{H}}_{n}\left( {{K}^{n},{K}^{n - 2}}\right)
\]

and

\[
{Z}_{n}^{\mathrm{{CW}}}/{B}_{n}^{\mathrm{{CW}}} \cong  {\mathrm{H}}_{n}\left( {{K}^{n + 1},{K}^{n - 2}}\right) .
\]

But using Corollary A. 3 one sees that

\[
{\mathrm{H}}_{n}\left( {{K}^{n + 1},{K}^{n - 2}}\right)  \cong  {\mathrm{H}}_{n}{K}^{n + 1} \cong  {\mathrm{H}}_{n}K.
\]

The proof for cohomology is completely analogous.
