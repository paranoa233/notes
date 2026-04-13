# 10 The Thom Isomorphism Theorem

This section will first give a complete proof of the Thom isomorphism theorem in the unoriented case (compare Theorem 8.1), and then describe the changes needed for the oriented case (Theorem 9.1). For the first half of this section, the coefficient field \( \mathbb{Z}/2 \) is to be understood.

We begin by outlining some constructions which are described in more detail in Appendix A. (See in particular A.6.) Let \( {\mathbb{R}}_{0}^{n} \) denote the set of non-zero vectors in \( {\mathbb{R}}^{n} \) . For \( n = 1 \) the cohomology group \( {\mathrm{H}}^{1}\left( {\mathbb{R},{\mathbb{R}}_{0}}\right) \) with mod 2 coefficients is cyclic of order 2. Let \( {e}^{1} \) denote the non-zero element. Then for any topological space \( B \) a cohomology isomorphism

\[
{\mathrm{H}}^{j}\left( B\right)  \rightarrow  {\mathrm{H}}^{j + 1}\left( {B \times  \mathbb{R}, B \times  {\mathbb{R}}_{0}}\right)
\]

is defined by the correspondence

\[
y \mapsto  y \times  {e}^{1},
\]

using the cohomology cross product operation. This is proved by studying the cohomology exact sequence of the triple \( \left( {B \times  \mathbb{R}, B \times  {\mathbb{R}}_{0}, B \times  {\mathbb{R}}_{ - }}\right) \) , where \( {\mathbb{R}}_{ - } \) denotes the set of negative real numbers.

Now let \( {B}^{\prime } \) be an open subset of \( B \) . Then for each cohomology class \( y \in  {\mathrm{H}}^{j}\left( {B,{B}^{\prime }}\right) \) the cross product \( y \times  {e}^{1} \) is defined with

\[
y \times  {e}^{1} \in  {\mathrm{H}}^{j + 1}\left( {B \times  \mathbb{R},{B}^{\prime } \times  \mathbb{R} \cup  B \times  {\mathbb{R}}_{0}}\right) .
\]

Using the Five Lemma \( {}^{1} \) it follows that the correspondence \( y \mapsto  y \times  {e}^{1} \) defines an isomorphism

\[
{\mathrm{H}}^{j}\left( {B,{B}^{\prime }}\right)  \rightarrow  {\mathrm{H}}^{j + 1}\left( {B \times  \mathbb{R},{B}^{\prime } \times  \mathbb{R} \cup  B \times  {\mathbb{R}}_{0}}\right) .
\]

Therefore it follows inductively that the \( n \) -fold composition

\[
y\mapsto y \times  {e}^{1}\mapsto y \times  {e}^{1} \times  {e}^{1}\mapsto \ldots \mapsto y \times  {e}^{1} \times  \ldots  \times  {e}^{1}
\]

is also an isomorphism. (See Appendix A for further details.) Setting

\[
{e}^{n} = {e}^{1} \times  \ldots  \times  {e}^{1} \in  {\mathrm{H}}^{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}_{0}^{n}}\right) ,
\]

this proves the following.

Lemma 10.1. For any topological space \( B \) and any \( n \geq  1 \) , a cohomology isomorphism

\[
{\mathrm{H}}^{j}\left( B\right)  \rightarrow  {\mathrm{H}}^{j + n}\left( {B \times  {\mathbb{R}}^{n}, B \times  {\mathbb{R}}_{0}^{n}}\right)
\]

is defined by the correspondence \( y \mapsto  y \times  {e}^{n} \) .

Now recall the statement of Thom’s theorem. Let \( \xi \) be an \( n \) -plane bundle with projection \( \pi  : E \rightarrow  B \) .

Theorem 10.2 (Thom isomorphism). There is one and only one cohomology class \( u \in  {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) with mod 2 coefficients whose restriction to \( {\mathrm{H}}^{n}\left( {F,{F}_{0}}\right) \) is non-zero for every fiber \( F \) . Furthermore, the correspondence \( y \mapsto  y \smile  u \) maps the cohomology group \( {\mathrm{H}}^{j}\left( E\right) \) isomorphically onto \( {\mathrm{H}}^{j + n}\left( {E,{E}_{0}}\right) \) for every integer \( j \) .

In particular, taking \( j < 0 \) , it follows that the cohomology of the pair \( \left( {E,{E}_{0}}\right) \) is trivial in dimensions less than \( n \) .

Proof. The proof will be divided into four cases.

Case 1. Suppose that \( \xi \) is a trivial vector bundle. Then we will identify \( E \) with the product \( B \times  {\mathbb{R}}^{n} \) . Thus the cohomology \( {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right)  = {\mathrm{H}}^{n}\left( {B \times  {\mathbb{R}}^{n}, B \times  {\mathbb{R}}_{0}^{n}}\right) \) is canonically isomorphic to \( {\mathrm{H}}^{0}\left( B\right) \) by 10.1. To prove the existence and uniqueness of \( u \) , it suffices to show that there is one and only one cohomology class \( s \in  {\mathrm{H}}^{0}\left( B\right) \) whose restriction to each point of \( B \) is non-zero. Evidently the identity element \( 1 \in  {\mathrm{H}}^{0}\left( B\right) \) is the only class satisfying this condition. Therefore \( u \) exists and is equal to \( 1 \times  {e}^{n} \) .

---

\( {}^{1} \) See for example [Spa81, pp. 185]

---

Finally, since every cohomology class in \( {\mathrm{H}}^{j}\left( {B \times  {\mathbb{R}}^{n}}\right) \) can be written uniquely as a product \( y \times  1 \) with \( y \in  {\mathrm{H}}^{j}\left( B\right) \) , it follows from 10.1 that the correspondence

\[
y \times  1 \mapsto  \left( {y \times  1}\right)  \smile  u = \left( {y \times  1}\right)  \smile  \left( {1 \times  {e}^{n}}\right)  = y \times  {e}^{n}
\]

is an isomorphism. This completes the proof in Case 1.

Case 2. Suppose that \( B \) is the union of two open sets \( {B}^{\prime } \) and \( {B}^{\prime \prime } \) , where the assertion 10.2 is known to be true for the restrictions \( {\left. \xi \right| }_{{B}^{\prime }} \) and \( {\left. \xi \right| }_{{B}^{\prime \prime }} \) and also for \( {\left. \xi \right| }_{{B}^{\prime } \cap  {B}^{\prime \prime }} \) . We introduce the abbreviation \( {B}^{ \cap  } \) for \( {B}^{\prime } \cap  {B}^{\prime \prime } \) , and the abbreviations \( {E}^{\prime },{E}^{\prime \prime } \) and \( {E}^{ \cap  } \) for the inverse images of \( {B}^{\prime },{B}^{\prime \prime } \) and \( {B}^{\prime } \cap  {B}^{\prime \prime } \) for the total space. The following Mayer-Vietoris sequence will be used:

\[
\ldots  \rightarrow  {\mathrm{H}}^{i - 1}\left( {{E}^{ \cap  },{E}_{0}^{ \cap  }}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {E,{E}_{0}}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {{E}^{\prime },{E}_{0}^{\prime }}\right)  \oplus  {\mathrm{H}}^{i}\left( {{E}^{\prime \prime },{E}_{0}^{\prime \prime }}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {{E}^{ \cap  },{E}_{0}^{ \cap  }}\right)  \rightarrow  \ldots .
\]

For the construction of this sequence, the reader is referred, for example, to [Spa81, pp. 190, 239].

By hypothesis, there exist unique cohomology classes \( {u}^{\prime } \in  {\mathrm{H}}^{n}\left( {{E}^{\prime },{E}_{0}^{\prime }}\right) \) and \( {u}^{\prime \prime } \in  {\mathrm{H}}^{n}\left( {{E}^{\prime \prime },{E}_{0}^{\prime \prime }}\right) \) whose restrictions to each fiber are non-zero. Applying the uniqueness statement for \( {\left. \xi \right| }_{{B}^{\prime } \cap  {B}^{\prime \prime }} \) , we see that the classes \( {u}^{\prime } \) and \( {u}^{\prime \prime } \) have the same image in \( {\mathrm{H}}^{n}\left( {{E}^{ \cap  },{E}_{0}^{ \cap  }}\right) \) . Therefore they come from a common cohomology class \( u \) in \( {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) . This class \( u \) is uniquely defined, since \( {\mathrm{H}}^{n - 1}\left( {{E}^{ \cap  },{E}_{0}^{ \cap  }}\right)  = 0 \) .

Now consider the Mayer-Vietoris sequence

\[
\ldots  \rightarrow  {\mathrm{H}}^{j - 1}\left( {E}^{ \cap  }\right)  \rightarrow  {\mathrm{H}}^{j}\left( E\right)  \rightarrow  {\mathrm{H}}^{j}\left( {E}^{\prime }\right)  \oplus  {\mathrm{H}}^{j}\left( {E}^{\prime \prime }\right)  \rightarrow  {\mathrm{H}}^{j}\left( {E}^{ \cap  }\right)  \rightarrow  \ldots
\]

where \( j + n = i \) . Mapping this sequence to the previous Mayer-Vietoris sequence by the correspondence \( y \mapsto  y \smile  u \) and applying the Five Lemma, it follows that

\[
{\mathrm{H}}^{j}\left( E\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{H}}^{j + n}\left( {E,{E}_{0}}\right) .
\]

This completes the proof in Case 2.

Case 3. Suppose that \( B \) is covered by finitely many open sets \( {B}_{1},\ldots ,{B}_{k} \) such that the bundle \( {\left. \xi \right| }_{{B}_{i}} \) is trivial for each \( {B}_{i} \) . We will prove by induction on \( k \) that the assertion of 10.2 is true for the bundle \( \xi \) .

To start the induction, the assertion is certainly true when \( k = 1 \) . If \( k > 1 \) , then we can assume by induction that the assertion is true for \( {\left. \xi \right| }_{{B}_{1} \cup  \ldots  \cup  {B}_{k - 1}} \) and for \( {\left. \xi \right| }_{\left( {{B}_{1} \cup  \ldots  \cup  {B}_{k - 1}}\right)  \cap  {B}_{k}} \) . Hence, by Case 2, it is true for \( \xi \) .

General Case. Let \( C \) be an arbitrary compact subset of the base space \( B \) . Then evidently the bundle \( {\left. \xi \right| }_{C} \) satisfies the hypothesis of Case 3. Since the union of any two compact sets is compact \( {}^{2} \) we can form the direct limit

\( \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}_{j}\left( C\right) \)

of homology groups as \( C \) varies over all compact subsets of \( B \) , and the corresponding inverse limit \( \underline{\lim }{\mathrm{H}}^{j}\left( C\right) \) of cohomology groups. We recall the following.

Lemma 10.3. The natural homomorphism

\[
{\mathrm{H}}^{j}\left( B\right)  \rightarrow  \mathop{\lim }\limits_{ \leftarrow  }{\mathrm{H}}^{j}\left( C\right)
\]

is an isomorphism, and similarly \( {\mathrm{H}}^{j}\left( {E,{E}_{0}}\right) \) maps isomorphically to \( \mathop{\lim }\limits_{ \leftarrow  }{\mathrm{H}}^{j}\left( {{\pi }^{-1}\left( C\right) ,{\pi }^{-1}{\left( C\right) }_{0}}\right) . \)

Caution. These statements are only true since we are working with field coefficients. The corresponding statements with integer coefficients would definitely be false.

Proof of 10.3. The corresponding homology statement, that \( \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}_{j}\left( C\right) \) maps isomorphically to \( {\mathrm{H}}_{j}\left( B\right) \) , is clearly true for arbitrary coefficients, since every singular chain on \( B \) is contained in some compact subset of \( B \) . Similarly, the group \( \mathop{\lim }\limits_{{i \rightarrow  \infty }}{\mathrm{H}}_{j}\left( {{\pi }^{-1}\left( C\right) ,{\pi }^{-1}{\left( C\right) }_{0}}\right) \) maps isomorphically to \( {\mathrm{H}}_{j}\left( {E,{E}_{0}}\right) \) . But according to A. 1 in the Appendix, the cohomology \( {\mathrm{H}}^{j}\left( B\right) \) with coefficients in the field \( \mathbb{Z}/2 \)

---

\( {}^{2} \) Here we are implicitly assuming that the base space \( B \) is Hausdorff. This is not actually necessary. The proof goes through perfectly well for non-Hausdorff spaces provided that one substitutes "quasi-compact" (i.e., every open covering contains a finite covering) for "compact" throughout.

---

is canonically isomorphic to \( \operatorname{Hom}\left( {{\mathrm{H}}_{j}\left( B\right) ,\mathbb{Z}/2}\right) \) . Together with the easily verified isomorphism

\[
\operatorname{Hom}\left( {\mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}_{j}\left( C\right) ,\mathbb{Z}/2}\right) \overset{ \cong  }{ \rightarrow  }\mathop{\lim }\limits_{ \leftarrow  }\operatorname{Hom}\left( {{\mathrm{H}}_{j}\left( C\right) ,\mathbb{Z}/2}\right)
\]

this proves 10.3.

In particular, the cohomology group \( {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) maps isomorphically to the inverse limit of the groups \( {\mathrm{H}}^{n}\left( {{\pi }^{-1}\left( C\right) ,{\pi }^{-1}{\left( C\right) }_{0}}\right) \) . But each of the latter groups contains one and only one class \( {u}_{C} \) whose restriction to each fiber is non-zero. It follows immediately that \( {\mathrm{H}}^{n}\left( {E,{E}_{0}}\right) \) contains one and only one class \( u \) whose restriction to each fiber is non-zero.

Now consider the homomorphism \( \smile  u : {\mathrm{H}}^{j}\left( E\right)  \rightarrow  {\mathrm{H}}^{j + n}\left( {E,{E}_{0}}\right) \) . Evidently, for each compact subset \( C \) of \( B \) there is a commutative diagram

![bo_d7du9galb0pc73deir9g_116_406_961_721_244_0.jpg](images/bo_d7du9galb0pc73deir9g_116_406_961_721_244_0.jpg)

Passing to the inverse limit, as \( C \) varies over all compact subsets, it follows that \( \smile  u \) is itself an isomorphism. This completes the proof of 10.2. Hence we have finally completed the proof of existence (and uniqueness) for Stiefel-Whitney classes.

Now let us try to carry out analogous arguments with coefficients in an arbitrary ring \( \Lambda \) . (It is of course assumed that \( \Lambda \) is associative with 1.) Just as in the argument above, the cohomology \( {\mathrm{H}}^{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}_{0}^{n};\Lambda }\right) \) is a free \( \Lambda \) -module, with a single generator \( {e}^{n} = {e}^{1} \times  \ldots  \times  {e}^{1} \) . (See A. 6 in the Appendix.)

Let \( \xi \) be an oriented \( n \) -plane bundle. Then for each fiber \( F \) of \( \xi \) we are given a preferred generator

\[
{u}_{F} \in  {\mathrm{H}}^{n}\left( {F,{F}_{0};\mathbb{Z}}\right) \text{ . }
\]

(Compare §9.) Using the unique ring homomorphism \( \mathbb{Z} \rightarrow  \Lambda \) , this gives rise to a corresponding generator for \( {\mathrm{H}}^{n}\left( {F,{F}_{0};\Lambda }\right) \) which will also be denoted by the symbol \( {u}_{F} \) .

Theorem 10.4 (Thom Isomorphism). There is one and only one cohomology class \( u \in  {\mathrm{H}}^{n}\left( {E,{E}_{0};\Lambda }\right) \) whose restriction to \( \left( {F,{F}_{0}}\right) \) is equal to \( {u}_{F} \) for every fiber \( F \) . Furthermore the correspondence \( y \mapsto  y \smile  u \) maps \( {\mathrm{H}}^{j}\left( {E;\Lambda }\right) \) isomorphically onto \( {\mathrm{H}}^{j + n}\left( {E,{E}_{0};\Lambda }\right) \) for every integer \( j \) .

If the coefficient ring \( \Lambda \) is a field, then the proof is completely analogous to the proof of 10.2. Details will be left to the reader. Similarly, if the base space \( B \) is compact, then the proof is completely analogous to the proof of 10.2. (A similar argument works for any bundle \( \xi \) of finite type. Compare Problem 5-E.)

The difficulty in extending to the general case is that Lemma 10.3 is not available for cohomology with non-field coefficients. In fact the inverse limits of 10.3 can be very badly behaved in general. However, the construction of the fundamental class \( u \) does go through without too much difficulty. We will need the following.

Lemma 10.5. The homology group \( {\mathrm{H}}_{n - 1}\left( {E,{E}_{0};\mathbb{Z}}\right) \) is zero.

Assuming this for the present, it follows from A. 1 in the Appendix that the cohomology group \( {\mathrm{H}}^{n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) is canonically isomorphic to \( \operatorname{Hom}\left( {{\mathrm{H}}_{n}\left( {E,{E}_{0};\mathbb{Z}}\right) ,\mathbb{Z}}\right) \) . Therefore, just as in the proof of 10.3, we see that \( {\mathrm{H}}^{n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) is canonically isomorphic to the inverse limit of the groups

\[
{\mathrm{H}}^{n}\left( {{\pi }^{-1}\left( C\right) ,{\pi }^{-1}{\left( C\right) }_{0};\mathbb{Z}}\right)
\]

as \( C \) varies over all compact subsets of the base space \( B \) . Since 10.4 has already been proved for any vector bundle over a compact base space \( C \) , it follows that there is a unique fundamental cohomology class \( u \in  {\mathrm{H}}^{n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) .

Remark. It is important to note that the fundamental class in \( {\mathrm{H}}^{n}\left( {E,{E}_{0};\mathbb{Z}}\right) \) corresponds to a fundamental class in \( {\mathrm{H}}^{n}\left( {E,{E}_{0};\Lambda }\right) \) for any ring \( \Lambda \) , under the unique ring homomorphism \( \mathbb{Z} \rightarrow  \Lambda \) .

To prove that the cup product with \( u \) induces cohomology isomorphisms, we will make use of the following constructions.

Definition. A free chain complex over \( \mathbb{Z} \) is a sequence of free \( \mathbb{Z} \) -modules \( {K}_{n} \) and homomorphisms

\[
\ldots  \rightarrow  {K}_{n}\overset{\partial }{ \rightarrow  }{K}_{n - 1}\overset{\partial }{ \rightarrow  }{K}_{n - 2} \rightarrow  \ldots
\]

with \( \partial  \circ  \partial  = 0 \) . A chain mapping \( f : K \rightarrow  {K}^{\prime } \) of degree \( d \) is a sequence of homomorphisms \( {K}_{i} \rightarrow  {K}_{i + d}^{\prime } \) satisfying \( {\partial }^{\prime } \circ  f = {\left( -1\right) }^{d}\left( {f \circ  \partial }\right) \) .

Lemma 10.6. Let \( f : K \rightarrow  {K}^{\prime } \) be a chain mapping, where \( K \) and \( {K}^{\prime } \) are free chain complexes over \( \mathbb{Z} \) . If \( f \) induces a cohomology isomorphism

\[
{f}^{ * } : {\mathrm{H}}^{ * }\left( {{K}^{\prime };\Lambda }\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {K;\Lambda }\right)
\]

for every coefficient field \( \Lambda \) , then \( f \) induces isomorphisms of homology and cohomology with arbitrary coefficients.

Proof. The mapping cone \( {K}^{f} \) is a free chain complex constructed as follows. Let \( {K}_{i}^{f} = {K}_{i - d - 1} \oplus  {K}_{i}^{\prime } \) with boundary homomorphism \( {\partial }^{f} : {K}_{i}^{f} \rightarrow  {K}_{i - 1}^{f} \) defined by

\[
{\partial }^{f}\left( {\kappa ,{\kappa }^{\prime }}\right)  = \left( {{\left( -1\right) }^{d + 1}\partial \kappa , f\left( \kappa \right)  + {\partial }^{\prime }{\kappa }^{\prime }}\right)
\]

(Compare [Spa81, pp. 166].) Evidently \( {K}^{f} \) fits into a short exact sequence

\[
0 \rightarrow  {K}^{\prime } \rightarrow  {K}^{f} \rightarrow  K \rightarrow  0
\]

of chain mappings. Furthermore the boundary homomorphism

\[
{\partial }^{f} : {\mathrm{H}}_{i - d - 1}\left( K\right)  \rightarrow  {\mathrm{H}}_{i - 1}\left( {K}^{\prime }\right)
\]

in the associated homology exact sequence is precisely equal to \( {f}_{ * } \) . Thus the homology \( {\mathrm{H}}_{ * }\left( {K}^{f}\right) \) is zero if and only if \( f \) induces an isomorphism \( {\mathrm{H}}_{ * }\left( K\right)  \rightarrow  {\mathrm{H}}_{ * }\left( {K}^{\prime }\right) \) of integral homology.

In our case, \( f \) is known to induce a cohomology isomorphism

\( {\mathrm{H}}^{ * }\left( {{K}^{\prime };\Lambda }\right)  \rightarrow  {\mathrm{H}}^{ * }\left( {K;\Lambda }\right) \) for every coefficient field \( \Lambda \) . Using the cohomology exact sequence, it follows that \( {\mathrm{H}}^{ * }\left( {{K}^{f};\Lambda }\right)  = 0 \) . But the cohomology \( {\mathrm{H}}^{n}\left( {{K}^{f};\Lambda }\right) \) is canonically isomorphic to \( {\operatorname{Hom}}_{\Lambda }\left( {{\mathrm{H}}_{n}\left( {{K}^{f} \otimes  \Lambda }\right) ,\Lambda }\right) \) by A. 1 in the Appendix.

Therefore, the homology vector space \( {\mathrm{H}}_{n}\left( {{K}^{f} \otimes  \Lambda }\right) \) is zero. For otherwise there would exist a non-trivial \( \Lambda \) -linear mapping from this space to the coefficient field \( \Lambda \) .

In particular the rational homology \( {\mathrm{H}}_{n}\left( {{K}^{f} \otimes  \mathbb{Q}}\right) \) is zero. Therefore, for every cycle \( \zeta  \in  {Z}_{n}\left( {K}^{f}\right) \) it follows that some integral multiple of \( \zeta \) is a boundary. Hence the integral homology \( {\mathrm{H}}_{n}\left( {K}^{f}\right) \) is a torsion group.

To prove that this torsion group \( {\mathrm{H}}_{n}\left( {K}^{f}\right) \) is zero, it suffices to prove that every element of prime order is zero. Let \( \zeta  \in  {Z}_{n}\left( {K}^{f}\right) \) be a cycle representing a homology class of prime order \( p \) . Then

\[
{p\zeta } = \partial \kappa
\]

for some \( \kappa  \in  {K}_{n + 1}^{f} \) . Thus \( \kappa \) is a cycle modulo \( p \) . Since the homology \( {\mathrm{H}}_{n + 1}\left( {{K}^{f} \otimes  \mathbb{Z}/p}\right) \) is known to be zero, it follows that \( \kappa \) is a boundary mod \( p \) , say

\[
\kappa  = \partial {\kappa }^{\prime } + p{\kappa }^{\prime \prime }.
\]

Therefore \( {p\zeta } = \partial \kappa \) is equal to \( p\partial {\kappa }^{\prime \prime } \) , and hence \( \zeta  = \partial {\kappa }^{\prime \prime } \) . Thus \( \zeta \) represents the trivial homology class, and we have proved that \( {\mathrm{H}}_{ * }\left( {K}^{f}\right)  = 0 \) .

It now follows easily that \( {K}^{f} \) has trivial homology and cohomology with arbitrary coefficients. (Compare [Spa81, pp. 167].) For example since \( {Z}_{n - 1}\left( {K}^{f}\right) \) is free, the exact sequence

\[
0 \rightarrow  {Z}_{n}\left( {K}^{f}\right)  \rightarrow  {K}_{n}^{f} \rightarrow  {Z}_{n - 1}\left( {K}^{f}\right)  \rightarrow  0
\]

is split exact, and therefore remains exact when we tensor it with an arbitrary additive group \( \Lambda \) . It follows easily that the sequence

\[
\ldots  \rightarrow  {K}_{n + 1}^{f} \otimes  \Lambda  \rightarrow  {K}_{n}^{f} \otimes  \Lambda  \rightarrow  {K}_{n - 1}^{f} \otimes  \Lambda  \rightarrow  \ldots
\]

is also exact, which proves that \( {\mathrm{H}}_{ * }\left( {{K}^{f} \otimes  \Lambda }\right)  = 0 \) . This completes the proof of 10.6.

The proof of 10.4 now proceeds as follows. We will make use of the cap product operation. (For the definition and basic properties, see A.10.) While proving 10.4, we will simultaneously prove the following. The coefficient ring \( \mathbb{Z} \) is to be understood.

Corollary 10.7. The correspondence \( \eta  \mapsto  u \cap  \eta \) defines an isomorphism from the integral homology group \( {\mathrm{H}}_{n + i}\left( {E,{E}_{0}}\right) \) to \( {\mathrm{H}}_{i}\left( E\right) \) .

Proof. Choose a singular cocycle \( z \in  {Z}^{n}\left( {E,{E}_{0}}\right) \) representing the fundamental cohomology class \( u \) . Then the correspondence \( \gamma  \mapsto  z \cap  \gamma \) from \( {C}_{n + i}\left( {E,{E}_{0}}\right) \) to \( {C}_{i}\left( E\right) \) satisfies the identity

\[
\partial \left( {z \cap  \gamma }\right)  = {\left( -1\right) }^{n}z \cap  \left( {\partial \gamma }\right)
\]

Therefore

\[
z \cap   : {C}_{ * }\left( {E,{E}_{0}}\right)  \rightarrow  {C}_{ * }\left( E\right)
\]

is a chain mapping of degree \( - n \) . Using the identity

\[
\langle c, z \cap  \gamma \rangle  = \langle c \smile  z,\gamma \rangle
\]

we see that the induced cochain mapping

\[
{\left( z \cap  \right) }^{\# } : {C}^{ * }\left( {E;\Lambda }\right)  \rightarrow  {C}^{ * }\left( {E,{E}_{0};\Lambda }\right)
\]

is given by \( c \mapsto  c \smile  z \) . Here \( \Lambda \) can be any ring. If the coefficient ring \( \Lambda \) is a field, then this cochain mapping induces a cohomology isomorphism by the portion of 10.4 that has already been proved. Thus we can apply 10.6, and concludes that the homomorphisms

\[
u \cap   : {\mathrm{H}}_{i + n}\left( {E,{E}_{0};\Lambda }\right)  \rightarrow  {\mathrm{H}}_{i}\left( {E;\Lambda }\right)
\]

and

\[
\smile  u : {\mathrm{H}}^{i}\left( {E;\Lambda }\right)  \rightarrow  {\mathrm{H}}^{i + n}\left( {E,{E}_{0};\Lambda }\right)
\]

are actually isomorphisms for arbitrary \( \Lambda \) . In particular, using the isomorphism \( \smile  u : {\mathrm{H}}^{0}\left( {E;\Lambda }\right)  \rightarrow  {\mathrm{H}}^{n}\left( {E,{E}_{0};\Lambda }\right) \) , the uniqueness of the fundamental cohomology class \( u \) with coefficients in \( \Lambda \) can now be verified.

This completes the proof of 10.4 and 10.7 except for one step that has been skipped over. Namely, we must still prove that \( {\mathrm{H}}_{n - 1}\left( {E,{E}_{0};\mathbb{Z}}\right)  = 0 \) (Lemma 10.5).

First suppose that the base space \( B \) is compact. Then we have already observed that Theorem 10.4 is true independently of 10.5. Similarly the proof of 10.7, in this special case, goes through without making use of 10.5. Thus we are free to make use of 10.7 to conclude that

\[
{\mathrm{H}}_{n - 1}\left( {E,{E}_{0};\mathbb{Z}}\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{H}}_{-1}\left( {E;\mathbb{Z}}\right)  = 0.
\]

The proof of 10.5 in the general case now follows immediately, using the homology isomorphism

\[
\mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}_{i}\left( {{\pi }^{-1}\left( C\right) ,{\pi }^{-1}{\left( C\right) }_{0};\mathbb{Z}}\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{H}}_{i}\left( {E,{E}_{0};\mathbb{Z}}\right) ,
\]

where \( C \) varies over all compact subsets of \( B \) . (Compare 10.3.) This completes the proof.
