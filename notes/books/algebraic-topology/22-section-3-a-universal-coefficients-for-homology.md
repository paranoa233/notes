# 3.A Universal Coefficients for Homology

The main goal in this section is an algebraic formula for computing homology with arbitrary coefficients in terms of homology with \( \mathbb{Z} \) coefficients. The theory parallels rather closely the universal coefficient theorem for cohomology in §3.1.

The first step is to formulate the definition of homology with coefficients in terms of tensor products. The chain group \( {C}_{n}\left( {X;G}\right) \) as defined in \( \text{ § }{2.2} \) consists of the finite formal sums \( \mathop{\sum }\limits_{i}{g}_{i}{\sigma }_{i} \) with \( {g}_{i} \in  G \) and \( {\sigma }_{i} : {\Delta }^{n} \rightarrow  X \) . This means that \( {C}_{n}\left( {X;G}\right) \) is a direct sum of copies of \( G \) , with one copy for each singular \( n \) -simplex in \( X \) . More generally, the relative chain group \( {C}_{n}\left( {X, A;G}\right)  = {C}_{n}\left( {X;G}\right) /{C}_{n}\left( {A;G}\right) \) is also a direct sum of copies of \( G \) , one for each singular \( n \) -simplex in \( X \) not contained in \( A \) . From the basic properties of tensor products listed in the discussion of the Künneth formula in \( \text{ § }{3.2} \) it follows that \( {C}_{n}\left( {X, A;G}\right) \) is naturally isomorphic to \( {C}_{n}\left( {X, A}\right)  \otimes  G \) , via the correspondence \( \mathop{\sum }\limits_{i}{g}_{i}{\sigma }_{i} \mapsto  \mathop{\sum }\limits_{i}{\sigma }_{i} \otimes  {g}_{i} \) . Under this isomorphism the boundary map \( {C}_{n}\left( {X, A;G}\right)  \rightarrow  {C}_{n - 1}\left( {X, A;G}\right) \) becomes the map \( \partial  \otimes  \mathbb{1} : {C}_{n}\left( {X, A}\right)  \otimes  G \rightarrow  {C}_{n - 1}\left( {X, A}\right)  \otimes  G \) where \( \partial  : {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n - 1}\left( {X, A}\right) \) is the usual boundary map for \( \mathbb{Z} \) coefficients. Thus we have the following algebraic problem:

Given a chain complex \( \cdots  \rightarrow  {C}_{n}\xrightarrow[]{{\partial }_{n}}{C}_{n - 1} \rightarrow  \cdots \) of free abelian groups \( {C}_{n} \) , is it possible to compute the homology groups \( {H}_{n}\left( {C;G}\right) \) of the associated chain complex \( \cdots  \rightarrow  {C}_{n} \otimes  G\xrightarrow[]{{\partial }_{n} \otimes  \mathbb{1}}{C}_{n - 1} \otimes  G \rightarrow  \cdots \) just in terms of \( G \) and the homology groups \( {H}_{n}\left( C\right) \) of the original complex?

To approach this problem, the idea will be to compare the chain complex \( C \) with two simpler subcomplexes, the subcomplexes consisting of the cycles and the boundaries in \( C \) , and see what happens upon tensoring all three complexes with \( G \) .

Let \( {Z}_{n} = \operatorname{Ker}{\partial }_{n} \subset  {C}_{n} \) and \( {B}_{n} = \operatorname{Im}{\partial }_{n + 1} \subset  {C}_{n} \) . The restrictions of \( {\partial }_{n} \) to these two subgroups are zero, so they can be regarded as subcomplexes \( Z \) and \( B \) of \( C \) with trivial boundary maps. Thus we have a short exact sequence of chain complexes consisting of the commutative diagrams(i)

![bo_d7dtv0s91nqc73eq8nv0_269_521_1868_730_193_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_269_521_1868_730_193_0.jpg)

The rows in this diagram split since each \( {B}_{n} \) is free, being a subgroup of the free group \( {C}_{n} \) . Thus \( {C}_{n} \approx  {Z}_{n} \oplus  {B}_{n - 1} \) , but the chain complex \( C \) is not the direct sum of the chain complexes \( Z \) and \( B \) since the latter have trivial boundary maps but the boundary maps in \( C \) may be nontrivial. Now tensor with \( G \) to get a commutative diagram

(ii)

\[
\begin{array}{l} 0 \rightarrow  {Z}_{n} \otimes  G \rightarrow  {C}_{n} \otimes  G\overset{{\partial }_{n} \otimes  \mathbb{1}}{ \rightarrow  }{B}_{n - 1} \otimes  G \rightarrow  0 \\  0 \rightarrow  {Z}_{n - 1} \otimes  G \rightarrow  {C}_{n - 1} \otimes  G\overset{{\partial }_{n} \otimes  \mathbb{1}}{ \rightarrow  }{B}_{n - 2} \otimes  G \rightarrow  0 \\  \end{array}
\]

The rows are exact since the rows in (i) split and tensor products satisfy \( \left( {A \oplus  B}\right)  \otimes  G \approx \; A \otimes  G \oplus  B \otimes  G \) , so the rows in (ii) are split exact sequences too. Thus we have a short exact sequence of chain complexes \( 0 \rightarrow  Z \otimes  G \rightarrow  C \otimes  G \rightarrow  B \otimes  G \rightarrow  0 \) . Since the boundary maps are trivial in \( Z \otimes  G \) and \( B \otimes  G \) , the associated long exact sequence of homology groups has the form

(iii)

\[
\cdots  \rightarrow  {B}_{n} \otimes  G \rightarrow  {Z}_{n} \otimes  G \rightarrow  {H}_{n}\left( {C;G}\right)  \rightarrow  {B}_{n - 1} \otimes  G \rightarrow  {Z}_{n - 1} \otimes  G \rightarrow  \cdots
\]

The ’boundary’ maps \( {B}_{n} \otimes  G \rightarrow  {Z}_{n} \otimes  G \) in this sequence are simply the maps \( {i}_{n} \otimes  \mathbb{1} \) where \( {i}_{n} : {B}_{n} \rightarrow  {Z}_{n} \) is the inclusion. This is evident from the definition of the boundary map in a long exact sequence of homology groups: In diagram (ii) one takes an element of \( {B}_{n - 1} \otimes  G \) , pulls it back via \( {\left( {\partial }_{n} \otimes  \mathbb{1}\right) }^{-1} \) to \( {C}_{n} \otimes  G \) , then applies \( {\partial }_{n} \otimes  \mathbb{1} \) to get into \( {C}_{n - 1} \otimes  G \) , then pulls back to \( {Z}_{n - 1} \otimes  G \) .

The long exact sequence (iii) can be broken up into short exact sequences

(iv)

\[
0 \rightarrow  \operatorname{Coker}\left( {{i}_{n} \otimes  \mathbb{1}}\right)  \rightarrow  {H}_{n}\left( {C;G}\right)  \rightarrow  \operatorname{Ker}\left( {{i}_{n - 1} \otimes  \mathbb{1}}\right)  \rightarrow  0
\]

where \( \operatorname{Coker}\left( {{i}_{n} \otimes  \mathbb{1}}\right)  = \left( {{Z}_{n} \otimes  G}\right) /\operatorname{Im}\left( {{i}_{n} \otimes  \mathbb{1}}\right) \) . The next lemma shows this cokernel is just \( {H}_{n}\left( C\right)  \otimes  G \) .

Lemma 3A.1. If the sequence of abelian groups \( A\overset{i}{ \rightarrow  }B\overset{j}{ \rightarrow  }C \rightarrow  0 \) is exact, then so is \( A \otimes  G\xrightarrow[]{i \otimes  \mathbb{1}}B \otimes  G\xrightarrow[]{j \otimes  \mathbb{1}}C \otimes  G \rightarrow  0 \) .

Proof: Certainly the compositions of two successive maps in the latter sequence are zero. Also, \( j \otimes  \mathbb{1} \) is clearly surjective since \( j \) is. To check exactness at \( B \otimes  G \) it suffices to show that the map \( B \otimes  G/\operatorname{Im}\left( {i \otimes  \mathbb{1}}\right)  \rightarrow  C \otimes  G \) induced by \( j \otimes  \mathbb{1} \) is an isomorphism, which we do by constructing its inverse. Define a map \( \varphi  : C \times  G \rightarrow  B \otimes  G/\operatorname{Im}\left( {i \otimes  \mathbb{1}}\right) \) by \( \varphi \left( {c, g}\right)  = b \otimes  g \) where \( j\left( b\right)  = c \) . This \( \varphi \) is well-defined since if \( j\left( b\right)  = j\left( {b}^{\prime }\right)  = c \) then \( b - {b}^{\prime } = i\left( a\right) \) for some \( a \in  A \) by exactness, so \( b \otimes  g - {b}^{\prime } \otimes  g = \left( {b - {b}^{\prime }}\right)  \otimes  g = \; i\left( a\right)  \otimes  g \in  \operatorname{Im}\left( {i \otimes  \mathbb{1}}\right) \) . Since \( \varphi \) is a homomorphism in each variable separately, it induces a homomorphism \( C \otimes  G \rightarrow  B \otimes  G/\operatorname{Im}\left( {i \otimes  \mathbb{1}}\right) \) . This is clearly an inverse to the map \( B \otimes  G/\operatorname{Im}\left( {i \otimes  \mathbb{1}}\right)  \rightarrow  C \otimes  G \) .

It remains to understand \( \operatorname{Ker}\left( {{i}_{n - 1} \otimes  \mathbb{1}}\right) \) , or equivalently \( \operatorname{Ker}\left( {{i}_{n} \otimes  \mathbb{1}}\right) \) . The situation is that tensoring the short exact sequence

(v)

\[
0 \rightarrow  {B}_{n}\overset{{i}_{n}}{ \rightarrow  }{Z}_{n} \rightarrow  {H}_{n}\left( C\right)  \rightarrow  0
\]

with \( G \) produces a sequence which becomes exact only by insertion of the extra term \( \operatorname{Ker}\left( {{i}_{n} \otimes  \mathbb{1}}\right) \) :

(vi)

\[
0 \rightarrow  \operatorname{Ker}\left( {{i}_{n} \otimes  \mathbb{1}}\right)  \rightarrow  {B}_{n} \otimes  G\xrightarrow[]{{i}_{n} \otimes  \mathbb{1}}{Z}_{n} \otimes  G \rightarrow  {H}_{n}\left( C\right)  \otimes  G \rightarrow  0
\]

What we will show is that \( \operatorname{Ker}\left( {{i}_{n} \otimes  \mathbb{1}}\right) \) does not really depend on \( {B}_{n} \) and \( {Z}_{n} \) but only on their quotient \( {H}_{n}\left( C\right) \) , and of course \( G \) .

The sequence (v) is a free resolution of \( {H}_{n}\left( C\right) \) , where as in \( \text{ § }{3.1} \) a free resolution of an abelian group \( H \) is an exact sequence

\[
\cdots  \rightarrow  {F}_{2}\overset{{f}_{2}}{ \rightarrow  }{F}_{1}\overset{{f}_{1}}{ \rightarrow  }{F}_{0}\overset{{f}_{0}}{ \rightarrow  }H \rightarrow  0
\]

with each \( {F}_{n} \) free. Tensoring a free resolution of this form with a fixed group \( G \) produces a chain complex

\[
\cdots  \rightarrow  {F}_{1} \otimes  G\xrightarrow[]{{f}_{1} \otimes  \mathbb{1}}{F}_{0} \otimes  G\xrightarrow[]{{f}_{0} \otimes  \mathbb{1}}H \otimes  G \rightarrow  0
\]

By the preceding lemma this is exact at \( {F}_{0} \otimes  G \) and \( H \otimes  G \) , but to the left of these two terms it may not be exact. For the moment let us write \( {H}_{n}\left( {F \otimes  G}\right) \) for the homology group \( \operatorname{Ker}\left( {{f}_{n} \otimes  \mathbb{1}}\right) /\operatorname{Im}\left( {{f}_{n + 1} \otimes  \mathbb{1}}\right) \) .

Lemma 3A.2. For any two free resolutions \( F \) and \( {F}^{\prime } \) of \( H \) there are canonical isomorphisms \( {H}_{n}\left( {F \otimes  G}\right)  \approx  {H}_{n}\left( {{F}^{\prime } \otimes  G}\right) \) for all \( n \) .

Proof: We will use Lemma 3.1(a). In the situation described there we have two free resolutions \( F \) and \( {F}^{\prime } \) with a chain map between them. If we tensor the two free resolutions with \( G \) we obtain chain complexes \( F \otimes  G \) and \( {F}^{\prime } \otimes  G \) with the maps \( {\alpha }_{n} \otimes  \mathbb{1} \) forming a chain map between them. Passing to homology, this chain map induces homomorphisms \( {\alpha }_{ * } : {H}_{n}\left( {F \otimes  G}\right)  \rightarrow  {H}_{n}\left( {{F}^{\prime } \otimes  G}\right) \) which are independent of the choice of \( {\alpha }_{n} \) ’s since if \( {\alpha }_{n} \) and \( {\alpha }_{n}^{\prime } \) are chain homotopic via a chain homotopy \( {\lambda }_{n} \) then \( {\alpha }_{n} \otimes  \mathbb{1} \) and \( {\alpha }_{n}^{\prime } \otimes  \mathbb{1} \) are chain homotopic via \( {\lambda }_{n} \otimes  \mathbb{1} \) .

For a composition \( H\overset{\alpha }{ \rightarrow  }{H}^{\prime }\overset{\beta }{ \rightarrow  }{H}^{\prime \prime } \) with free resolutions \( F,{F}^{\prime } \) , and \( {F}^{\prime \prime } \) of these three groups also given, the induced homomorphisms satisfy \( {\left( \beta \alpha \right) }_{ * } = {\beta }_{ * }{\alpha }_{ * } \) since we can choose for the chain map \( F \rightarrow  {F}^{\prime \prime } \) the composition of chain maps \( F \rightarrow  {F}^{\prime } \rightarrow  {F}^{\prime \prime } \) . In particular, if we take \( \alpha \) to be an isomorphism, with \( \beta \) its inverse and \( {F}^{\prime \prime } = F \) , then \( {\beta }_{ * }{\alpha }_{ * } = {\left( \beta \alpha \right) }_{ * } = {\mathbb{1}}_{ * } = \mathbb{1} \) , and similarly with \( \beta \) and \( \alpha \) reversed. So \( {\alpha }_{ * } \) is an isomorphism if \( \alpha \) is an isomorphism. Specializing further, taking \( \alpha \) to be the identity but with two different free resolutions \( F \) and \( {F}^{\prime } \) , we get a canonical isomorphism \( {\mathbb{1}}_{ * } : {H}_{n}\left( {F \otimes  G}\right)  \rightarrow  {H}_{n}\left( {{F}^{\prime } \otimes  G}\right) . \)

The group \( {H}_{n}\left( {F \otimes  G}\right) \) , which depends only on \( H \) and \( G \) , is denoted \( {\operatorname{Tor}}_{n}\left( {H, G}\right) \) . Since a free resolution \( 0 \rightarrow  {F}_{1} \rightarrow  {F}_{0} \rightarrow  H \rightarrow  0 \) always exists, as noted in §3.1, it follows that \( {\operatorname{Tor}}_{n}\left( {H, G}\right)  = 0 \) for \( n > 1 \) . Usually \( {\operatorname{Tor}}_{1}\left( {H, G}\right) \) is written simply as \( \operatorname{Tor}\left( {H, G}\right) \) . As we shall see later, \( \operatorname{Tor}\left( {H, G}\right) \) provides a measure of the common torsion of \( H \) and \( G \) , hence the name 'Tor'.

Is there a group \( {\operatorname{Tor}}_{0}\left( {H, G}\right) \) ? With the definition given above it would be zero since Lemma 3A.1 implies that \( {F}_{1} \otimes  G \rightarrow  {F}_{0} \otimes  G \rightarrow  H \otimes  G \rightarrow  0 \) is exact. It is probably better to modify the definition of \( {H}_{n}\left( {F \otimes  G}\right) \) to be the homology groups of the sequence \( \cdots  \rightarrow  {F}_{1} \otimes  G \rightarrow  {F}_{0} \otimes  G \rightarrow  0 \) , omitting the term \( H \otimes  G \) which can be regarded as a kind of augmentation. With this revised definition, Lemma 3A.1 then gives an isomorphism \( {\operatorname{Tor}}_{0}\left( {H, G}\right)  \approx  H \otimes  G. \)

We should remark that \( \operatorname{Tor}\left( {H, G}\right) \) is a functor of both \( G \) and \( H \) : Homomorphisms \( \alpha  : H \rightarrow  {H}^{\prime } \) and \( \beta  : G \rightarrow  {G}^{\prime } \) induce homomorphisms \( {\alpha }_{ * } : \operatorname{Tor}\left( {H, G}\right)  \rightarrow  \operatorname{Tor}\left( {{H}^{\prime }, G}\right) \) and \( {\beta }_{ * } : \operatorname{Tor}\left( {H, G}\right)  \rightarrow  \operatorname{Tor}\left( {H,{G}^{\prime }}\right) \) , satisfying \( {\left( \alpha {\alpha }^{\prime }\right) }_{ * } = {\alpha }_{ * }{\alpha }_{ * }^{\prime },{\left( \beta {\beta }^{\prime }\right) }_{ * } = {\beta }_{ * }{\beta }_{ * }^{\prime } \) , and \( {\mathbb{1}}_{ * } = \mathbb{1} \) . The induced map \( {\alpha }_{ * } \) was constructed in the proof of Lemma 3A.2, while for \( \beta \) the construction of \( {\beta }_{ * } \) is obvious.

Before going into calculations of \( \operatorname{Tor}\left( {H, G}\right) \) let us finish analyzing the earlier exact sequence (iv). Recall that we have a chain complex \( C \) of free abelian groups, with homology groups denoted \( {H}_{n}\left( C\right) \) , and tensoring \( C \) with \( G \) gives another complex \( C \otimes  G \) whose homology groups are denoted \( {H}_{n}\left( {C;G}\right) \) . The following result is known as the universal coefficient theorem for homology since it describes homology with arbitrary coefficients in terms of homology with the ’universal’ coefficient group \( \mathbb{Z} \) .

Theorem 3A.3. If \( C \) is a chain complex of free abelian groups, then there are natural short exact sequences

\[
0 \rightarrow  {H}_{n}\left( C\right)  \otimes  G \rightarrow  {H}_{n}\left( {C;G}\right)  \rightarrow  \operatorname{Tor}\left( {{H}_{n - 1}\left( C\right) , G}\right)  \rightarrow  0
\]

for all \( n \) and all \( G \) , and these sequences split, though not naturally.

Naturality means that a chain map \( C \rightarrow  {C}^{\prime } \) induces a map between the corresponding short exact sequences, with commuting squares.

Proof: This exact sequence is (iv) since we can identify Coker \( \left( {{i}_{n} \otimes  \mathbb{1}}\right) \) with \( {H}_{n}\left( C\right)  \otimes  G \) and \( \operatorname{Ker}\left( {{i}_{n - 1} \otimes  \mathbb{1}}\right) \) with \( \operatorname{Tor}\left( {{H}_{n - 1}\left( C\right) , G}\right) \) . Verifying naturality is a mental exercise in definition-checking, left to the reader.

The splitting is obtained as follows. We observed earlier that the short exact sequence \( 0 \rightarrow  {Z}_{n} \rightarrow  {C}_{n} \rightarrow  {B}_{n - 1} \rightarrow  0 \) splits, so there is a projection \( p : {C}_{n} \rightarrow  {Z}_{n} \) restricting to the identity on \( {Z}_{n} \) . The map \( p \) gives an extension of the quotient map \( {Z}_{n} \rightarrow  {H}_{n}\left( C\right) \) to a homomorphism \( {C}_{n} \rightarrow  {H}_{n}\left( C\right) \) . Letting \( n \) vary, we then have a chain map \( C \rightarrow  H\left( C\right) \) where the groups \( {H}_{n}\left( C\right) \) are regarded as a chain complex with trivial boundary maps, so the chain map condition is automatic. Now tensor with \( G \) to get a chain map \( C \otimes  G \rightarrow  H\left( C\right)  \otimes  G \) . Taking homology groups, we then have induced homomorphisms \( {H}_{n}\left( {C;G}\right)  \rightarrow  {H}_{n}\left( C\right)  \otimes  G \) since the boundary maps in the chain complex \( H\left( C\right)  \otimes  G \) are trivial. The homomorphisms \( {H}_{n}\left( {C;G}\right)  \rightarrow  {H}_{n}\left( C\right)  \otimes  G \) give the desired splitting since at the level of chains they are the identity on cycles in \( C \) , by the definition of \( p \) .

Corollary 3A.4. For each pair of spaces \( \left( {X, A}\right) \) there are split exact sequences

\[
0 \rightarrow  {H}_{n}\left( {X, A}\right)  \otimes  G \rightarrow  {H}_{n}\left( {X, A;G}\right)  \rightarrow  \operatorname{Tor}\left( {{H}_{n - 1}\left( {X, A}\right) , G}\right)  \rightarrow  0
\]

for all \( n \) , and these sequences are natural with respect to maps \( \left( {X, A}\right)  \rightarrow  \left( {Y, B}\right) \) .

The splitting is not natural, for if it were, a map \( X \rightarrow  Y \) that induced trivial maps \( {H}_{n}\left( X\right)  \rightarrow  {H}_{n}\left( Y\right) \) and \( {H}_{n - 1}\left( X\right)  \rightarrow  {H}_{n - 1}\left( Y\right) \) would have to induce the trivial map \( {H}_{n}\left( {X;G}\right)  \rightarrow  {H}_{n}\left( {Y;G}\right) \) for all \( G \) , but in Example 2.51 we saw an instance where this fails, namely the quotient map \( M\left( {{\mathbb{Z}}_{m}, n}\right)  \rightarrow  {S}^{n + 1} \) with \( G = {\mathbb{Z}}_{m} \) .

The basic tools for computing Tor are given by:

Proposition 3A.5.

(1) \( \operatorname{Tor}\left( {A, B}\right)  \approx  \operatorname{Tor}\left( {B, A}\right) \) .

(2) \( \operatorname{Tor}\left( {{\bigoplus }_{i}{A}_{i}, B}\right)  \approx  {\bigoplus }_{i}\operatorname{Tor}\left( {{A}_{i}, B}\right) \) .

(3) \( \operatorname{Tor}\left( {A, B}\right)  = 0 \) if \( A \) or \( B \) is free, or more generally torsionfree.

(4) \( \operatorname{Tor}\left( {A, B}\right)  \approx  \operatorname{Tor}\left( {T\left( A\right) , B}\right) \) where \( T\left( A\right) \) is the torsion subgroup of \( A \) .

(5) \( \operatorname{Tor}\left( {{\mathbb{Z}}_{n}, A}\right)  \approx  \operatorname{Ker}\left( {A\overset{n}{ \rightarrow  }A}\right) \) .

(6) For each short exact sequence \( 0 \rightarrow  B \rightarrow  C \rightarrow  D \rightarrow  0 \) there is a naturally associated exact sequence

\[
0 \rightarrow  \operatorname{Tor}\left( {A, B}\right)  \rightarrow  \operatorname{Tor}\left( {A, C}\right)  \rightarrow  \operatorname{Tor}\left( {A, D}\right)  \rightarrow  A \otimes  B \rightarrow  A \otimes  C \rightarrow  A \otimes  D \rightarrow  0
\]

Proof: Statement (2) is easy since one can choose as a free resolution of \( { \oplus  }_{i}{A}_{i} \) the direct sum of free resolutions of the \( {A}_{i} \) ’s. Also easy is (5), which comes from tensoring the free resolution \( 0 \rightarrow  \mathbb{Z}\overset{n}{ \rightarrow  }\mathbb{Z} \rightarrow  {\mathbb{Z}}_{n} \rightarrow  0 \) with \( A \) .

For (3), if \( A \) is free, it has a free resolution with \( {F}_{n} = 0 \) for \( n \geq  1 \) , so \( \operatorname{Tor}\left( {A, B}\right)  = 0 \) for all \( B \) . On the other hand, if \( B \) is free, then tensoring a free resolution of \( A \) with \( B \) preserves exactness, since tensoring a sequence with a direct sum of \( \mathbb{Z} \) ’s produces just a direct sum of copies of the given sequence. So Tor \( \left( {A, B}\right)  = 0 \) in this case too. The generalization to torsionfree \( A \) or \( B \) will be given below.

For (6), choose a free resolution \( 0 \rightarrow  {F}_{1} \rightarrow  {F}_{0} \rightarrow  A \rightarrow  0 \) and tensor with the given short exact sequence to get a commutative diagram

![bo_d7dtv0s91nqc73eq8nv0_273_484_1381_838_154_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_273_484_1381_838_154_0.jpg)

The rows are exact since tensoring with a free group preserves exactness. Extending the three columns by zeros above and below, we then have a short exact sequence of chain complexes whose associated long exact sequence of homology groups is the desired six-term exact sequence.

To prove (1) we apply (6) to a free resolution \( 0 \rightarrow  {F}_{1} \rightarrow  {F}_{0} \rightarrow  B \rightarrow  0 \) . Since \( \operatorname{Tor}\left( {A,{F}_{1}}\right) \) and \( \operatorname{Tor}\left( {A,{F}_{0}}\right) \) vanish by the part of (3) which we have proved, the six-term sequence in (6) reduces to the first row of the following diagram:

\[
0 \rightarrow  \operatorname{Tor}\left( {A, B}\right)  \rightarrow  A \otimes  {F}_{1} \rightarrow  A \otimes  {F}_{0} \rightarrow  A \otimes  B \rightarrow  0
\]

\[
\downarrow   \approx  \; \downarrow   \approx  \; \downarrow   \approx
\]

\[
0 \rightarrow  \operatorname{Tor}\left( {B, A}\right)  \rightarrow  {F}_{1} \otimes  A \rightarrow  {F}_{0} \otimes  A \rightarrow  B \otimes  A \rightarrow  0
\]

The second row comes from the definition of \( \operatorname{Tor}\left( {B, A}\right) \) . The vertical isomorphisms come from the natural commutativity of tensor product. Since the squares commute, there is induced a map \( \operatorname{Tor}\left( {A, B}\right)  \rightarrow  \operatorname{Tor}\left( {B, A}\right) \) , which is an isomorphism by the five-lemma.

Now we can prove the statement (3) in the torsionfree case. For a free resolution \( 0 \rightarrow  {F}_{1}\overset{\varphi }{ \rightarrow  }{F}_{0} \rightarrow  A \rightarrow  0 \) we wish to show that \( \varphi  \otimes  \mathbb{1} : {F}_{1} \otimes  B \rightarrow  {F}_{0} \otimes  B \) is injective if \( B \) is torsionfree. Suppose \( \mathop{\sum }\limits_{i}{x}_{i} \otimes  {b}_{i} \) lies in the kernel of \( \varphi  \otimes  \mathbb{1} \) . This means that \( \mathop{\sum }\limits_{i}\varphi \left( {x}_{i}\right)  \otimes  {b}_{i} \) can be reduced to 0 by a finite number of applications of the defining relations for tensor products. Only a finite number of elements of \( B \) are involved in this process. These lie in a finitely generated subgroup \( {B}_{0} \subset  B \) , so \( \mathop{\sum }\limits_{i}{x}_{i} \otimes  {b}_{i} \) lies in the kernel of \( \varphi  \otimes  \mathbb{1} : {F}_{1} \otimes  {B}_{0} \rightarrow  {F}_{0} \otimes  {B}_{0} \) . This kernel is zero since \( \operatorname{Tor}\left( {A,{B}_{0}}\right)  = 0 \) , as \( {B}_{0} \) is finitely generated and torsionfree, hence free.

Finally, we can obtain statement (4) by applying (6) to the short exact sequence \( 0 \rightarrow  T\left( A\right)  \rightarrow  A \rightarrow  A/T\left( A\right)  \rightarrow  0 \) since \( A/T\left( A\right) \) is torsionfree.

In particular,(5) gives \( \operatorname{Tor}\left( {{\mathbb{Z}}_{m},{\mathbb{Z}}_{n}}\right)  \approx  {\mathbb{Z}}_{q} \) where \( q \) is the greatest common divisor of \( m \) and \( n \) . Thus \( \operatorname{Tor}\left( {{\mathbb{Z}}_{m},{\mathbb{Z}}_{n}}\right) \) is isomorphic to \( {\mathbb{Z}}_{m} \otimes  {\mathbb{Z}}_{n} \) , though somewhat by accident. Combining this isomorphism with (2) and (3) we see that for finitely generated \( A \) and \( B \) , \( \operatorname{Tor}\left( {A, B}\right) \) is isomorphic to the tensor product of the torsion subgroups of \( A \) and \( B \) , or roughly speaking, the common torsion of \( A \) and \( B \) . This is one reason for the 'Tor' designation, further justification being (3) and (4).

Homology calculations are often simplified by taking coefficients in a field, usually \( \mathbb{Q} \) or \( {\mathbb{Z}}_{p} \) for \( p \) prime. In general this gives less information than taking \( \mathbb{Z} \) coefficients, but still some of the essential features are retained, as the following result indicates:

Corollary 3A.6. (a) \( {H}_{n}\left( {X;\mathbb{Q}}\right)  \approx  {H}_{n}\left( {X;\mathbb{Z}}\right)  \otimes  \mathbb{Q} \) , so when \( {H}_{n}\left( {X;\mathbb{Z}}\right) \) is finitely generated, the dimension of \( {H}_{n}\left( {X;\mathbb{Q}}\right) \) as a vector space over \( \mathbb{Q} \) equals the rank of \( {H}_{n}\left( {X;\mathbb{Z}}\right) \) .

(b) If \( {H}_{n}\left( {X;\mathbb{Z}}\right) \) and \( {H}_{n - 1}\left( {X;\mathbb{Z}}\right) \) are finitely generated, then for \( p \) prime, \( {H}_{n}\left( {X;{\mathbb{Z}}_{p}}\right) \) consists of

(i) a \( {\mathbb{Z}}_{p} \) summand for each \( \mathbb{Z} \) summand of \( {H}_{n}\left( {X;\mathbb{Z}}\right) \) ,

(ii) a \( {\mathbb{Z}}_{p} \) summand for each \( {\mathbb{Z}}_{{p}^{k}} \) summand in \( {H}_{n}\left( {X;\mathbb{Z}}\right) , k \geq  1 \) ,

(iii) a \( {\mathbb{Z}}_{p} \) summand for each \( {\mathbb{Z}}_{{p}^{k}} \) summand in \( {H}_{n - 1}\left( {X;\mathbb{Z}}\right) , k \geq  1 \) .

Even in the case of nonfinitely generated homology groups, field coefficients still give good qualitative information:

Corollary 3A.7. (a) \( {\widetilde{H}}_{n}\left( {X;\mathbb{Z}}\right)  = 0 \) for all \( n \) iff \( {\widetilde{H}}_{n}\left( {X;\mathbb{Q}}\right)  = 0 \) and \( {\widetilde{H}}_{n}\left( {X;{\mathbb{Z}}_{p}}\right)  = 0 \) for all \( n \) and all primes \( p \) .

(b) A map \( f : X \rightarrow  Y \) induces isomorphisms on homology with \( \mathbb{Z} \) coefficients iff it induces isomorphisms on homology with \( \mathbb{Q} \) and \( {\mathbb{Z}}_{p} \) coefficients for all primes \( p \) .

Proof: Statement (b) follows from (a) by passing to the mapping cone of \( f \) . The universal coefficient theorem gives the 'only if' half of (a). For the 'if' implication it suffices to show that if an abelian group \( A \) is such that \( A \otimes  \mathbb{Q} = 0 \) and \( \operatorname{Tor}\left( {A,{\mathbb{Z}}_{p}}\right)  = 0 \)

for all primes \( p \) , then \( A = 0 \) . For the short exact sequences \( 0 \rightarrow  \mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z} \rightarrow  {\mathbb{Z}}_{p} \rightarrow  0 \) and \( 0 \rightarrow  \mathbb{Z} \rightarrow  \mathbb{Q} \rightarrow  \mathbb{Q}/\mathbb{Z} \rightarrow  0 \) , the six-term exact sequences in (6) of the proposition become

\[
0 \rightarrow  \operatorname{Tor}\left( {A,{\mathbb{Z}}_{p}}\right)  \rightarrow  A\overset{p}{ \rightarrow  }A \rightarrow  A \otimes  {\mathbb{Z}}_{p} \rightarrow  0
\]

\[
0 \rightarrow  \operatorname{Tor}\left( {A,\mathbb{Q}/\mathbb{Z}}\right)  \rightarrow  A \rightarrow  A \otimes  \mathbb{Q} \rightarrow  A \otimes  \mathbb{Q}/\mathbb{Z} \rightarrow  0
\]

If \( \operatorname{Tor}\left( {A,{\mathbb{Z}}_{p}}\right)  = 0 \) for all \( p \) , then exactness of the first sequence implies that \( A\overset{p}{ \rightarrow  }A \) is injective for all \( p \) , so \( A \) is torsionfree. Then \( \operatorname{Tor}\left( {A,\mathbb{Q}/\mathbb{Z}}\right)  = 0 \) by (3) or (4) of the proposition, so the second sequence implies that \( A \rightarrow  A \otimes  \mathbb{Q} \) is injective, hence \( A = 0 \) if \( A \otimes  \mathbb{Q} = 0 \) .

The algebra by means of which the Tor functor is derived from tensor products has a very natural generalization in which abelian groups are replaced by modules over a fixed ring \( R \) with identity, using the definition of tensor product of \( R \) -modules given in §3.2. Free resolutions of \( R \) -modules are defined in the same way as for abelian groups, using free \( R \) -modules, which are direct sums of copies of \( R \) . Lemmas 3A.1 and 3A.2 carry over to this context without change, and so one has functors \( {\operatorname{Tor}}_{n}^{R}\left( {A, B}\right) \) . However, it need not be true that \( {\operatorname{Tor}}_{n}^{R}\left( {A, B}\right)  = 0 \) for \( n > 1 \) . The reason this was true when \( R = \mathbb{Z} \) was that subgroups of free groups are free, but submodules of free \( R \) -modules need not be free in general. If \( R \) is a principal ideal domain, submodules of free \( R \) -modules are free, so in this case the rest of the algebra, in particular the universal coefficient theorem, goes through without change. When \( R \) is a field \( F \) , every module is free and \( {\operatorname{Tor}}_{n}^{F}\left( {A, B}\right)  = 0 \) for \( n > 0 \) via the free resolution \( 0 \rightarrow  A \rightarrow  A \rightarrow  0 \) . Thus \( {H}_{n}\left( {C{ \otimes  }_{F}G}\right)  \approx  {H}_{n}\left( C\right) { \otimes  }_{F}G \) if \( F \) is a field.

## Exercises

1. Use the universal coefficient theorem to show that if \( {H}_{ * }\left( {X;\mathbb{Z}}\right) \) is finitely generated, so the Euler characteristic \( \chi \left( X\right)  = \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}\operatorname{rank}{H}_{n}\left( {X;\mathbb{Z}}\right) \) is defined, then for any coefficient field \( F \) we have \( \chi \left( X\right)  = \mathop{\sum }\limits_{n}{\left( -1\right) }^{n}\dim {H}_{n}\left( {X;F}\right) \) .

2. Show that \( \operatorname{Tor}\left( {A,\mathbb{Q}/\mathbb{Z}}\right) \) is isomorphic to the torsion subgroup of \( A \) . Deduce that \( A \) is torsionfree iff \( \operatorname{Tor}\left( {A, B}\right)  = 0 \) for all \( B \) .

3. Show that if \( {\widetilde{H}}^{n}\left( {X;\mathbb{Q}}\right) \) and \( {\widetilde{H}}^{n}\left( {X;{\mathbb{Z}}_{p}}\right) \) are zero for all \( n \) and all primes \( p \) , then \( {\widetilde{H}}_{n}\left( {X;\mathbb{Z}}\right)  = 0 \) for all \( n \) , and hence \( {\widetilde{H}}^{n}\left( {X;G}\right)  = 0 \) for all \( G \) and \( n \) .

4. Show that \( \otimes \) and Tor commute with direct limits: \( \left( {\underline{\lim }{A}_{\alpha }}\right)  \otimes  B = \underline{\lim }\left( {{A}_{\alpha } \otimes  B}\right) \) and \( \operatorname{Tor}\left( {\mathop{\lim }\limits_{ \rightarrow  }{A}_{\alpha }, B}\right)  = \mathop{\lim }\limits_{ \rightarrow  }\operatorname{Tor}\left( {{A}_{\alpha }, B}\right) . \)

5. From the fact that \( \operatorname{Tor}\left( {A, B}\right)  = 0 \) if \( A \) is free, deduce that \( \operatorname{Tor}\left( {A, B}\right)  = 0 \) if \( A \) is torsionfree by applying the previous problem to the directed system of finitely generated subgroups \( {A}_{\alpha } \) of \( A \) .

6. Show that \( \operatorname{Tor}\left( {A, B}\right) \) is always a torsion group, and that \( \operatorname{Tor}\left( {A, B}\right) \) contains an element of order \( n \) iff both \( A \) and \( B \) contain elements of order \( n \) .
