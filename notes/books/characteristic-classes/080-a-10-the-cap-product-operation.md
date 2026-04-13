# A.10 The Cap Product Operation

For any space \( X \) and any coefficient domain, there is a bilinear pairing operation

\[
\cap   : {C}^{i}X \otimes  {C}_{n}X \rightarrow  {C}_{n - i}X
\]

which can be characterized as follows. For each cochain \( b \in  {C}^{i}X \) and each chain \( \xi  \in  {C}_{n}X \) the cap product \( b \cap  \xi \) is the unique element of \( {C}_{n - i}X \) such that

\[
\langle a, b \cap  \xi \rangle  = \langle {ab},\xi \rangle \tag{1}
\]

for all \( a \in  {C}^{n - i}X \) . More explicitly, for each generator \( \left\lbrack  \sigma \right\rbrack \) of \( {C}_{n}X \) , the cap product \( b \cap  \left\lbrack  \sigma \right\rbrack \) can be defined as the product of the ring element

\( {\left( -1\right) }^{i\left( {n - i}\right) }\langle b,\left\lbrack  {\text{ back }i\text{ -face of }\sigma }\right\rbrack  \rangle \) with the singular simplex [front \( \left( {n - i}\right) \) -face of \( \sigma \) ].

Combining the identity (1) with the standard properties of cup products, one can derive the following rules:

\[
\left( {bc}\right)  \cap  \xi  = b \cap  \left( {c \cap  \xi }\right) \tag{2}
\]

\[
1 \cap  \xi  = \xi \tag{3}
\]

\[
\partial \left( {b \cap  \xi }\right)  = \left( {\delta b}\right)  \cap  \xi  + {\left( -1\right) }^{\dim b}b \cap  \partial \xi . \tag{4}
\]

From (4) it follows that there is a corresponding operation

\[
{\mathrm{H}}^{i}X \otimes  {\mathrm{H}}_{n}X \rightarrow  {\mathrm{H}}_{n - i}X
\]

which will also be denoted by \( \cap \) .

In terms of this operation we can now state the duality theorem for compact manifolds, using any coefficient domain.

Theorem (Poincaré Duality). If \( M \) is compact and oriented, then \( {\mathrm{H}}^{i}M \) is isomorphic to \( {\mathrm{H}}_{n - i}M \) under the correspondence \( a \mapsto  a \cap  {\mu }_{M} \) .

For a non-orientable manifold the duality theorem is still true, but only if one uses the coefficient domain \( \mathbb{Z}/2 \) .

Proof. The proof will involve a more general situation. First observe that for any pair \( \left( {X, A}\right) \) , the cap product gives rise to a pairing

\[
{C}^{i}\left( {X, A}\right)  \otimes  {C}_{n}\left( {X, A}\right)  \rightarrow  {C}_{n - i}X
\]

and hence to a pairing

\[
\cap   : {\mathrm{H}}^{i}\left( {X, A}\right)  \otimes  {\mathrm{H}}_{n}\left( {X, A}\right)  \rightarrow  {\mathrm{H}}_{n - i}X.
\]

(In even greater generality one can define

\[
\cap   : {\mathrm{H}}^{i}\left( {X, A}\right)  \otimes  {\mathrm{H}}_{n}\left( {X, A \cup  B}\right)  \rightarrow  {\mathrm{H}}_{n - i}\left( {X, B}\right)
\]

if \( A \) and \( B \) are open in \( A \cup  B \) .) Now let \( M \) be oriented but not necessarily compact. Define the duality map

\[
D : {\mathrm{H}}_{c}^{i}M \rightarrow  {\mathrm{H}}_{n - i}M
\]

as follows. For any \( a \in  {\mathrm{H}}_{c}^{i}M = \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}^{i}\left( {M, M - K}\right) \) choose a representative \( {a}^{\prime } \in  {\mathrm{H}}^{i}\left( {M, M - K}\right) \) and set

\[
D\left( a\right)  = {a}^{\prime } \cap  {\mu }_{K}.
\]

This is well defined since, for \( K \subset  L \) , the diagram

![bo_d7du9galb0pc73deir9g_281_478_362_774_173_0.jpg](images/bo_d7du9galb0pc73deir9g_281_478_362_774_173_0.jpg)

is clearly commutative. In the special case where \( M \) is compact, note that \( D\left( a\right)  = a \cap  {\mu }_{M} \) . Assuming the Theorem below, this proves Poincaré duality.

Theorem A.9 (Duality theorem). The homomorphism D maps \( {\mathrm{H}}_{c}^{i}M \) isomorphically onto \( {\mathrm{H}}_{n - i}M \) .

If \( M \) is compact, then this implies that \( \cap  {\mu }_{M} \) maps \( {\mathrm{H}}^{i}M \) isomorphically onto \( {\mathrm{H}}_{n - i}M \) , as previously asserted.

Proof. The proof will be divided into five cases.

Case 1. Suppose that \( M = {\mathbb{R}}^{n} \) .

Given any ball \( B \) we clearly have \( {\mathrm{H}}_{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - B}\right)  \cong  \Lambda \) with generator \( {\mu }_{B} \) . (Compare Theorem A.8, Case 1.) Hence \( {\mathrm{H}}^{n}\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - B}\right)  \cong  \Lambda \) by Theorem A.1, with a generator \( a \) such that \( \left\langle  {a,{\mu }_{B}}\right\rangle   = 1 \) . Now the identity

\[
\left\langle  {{1a},{\mu }_{B}}\right\rangle   = \left\langle  {1, a \cap  {\mu }_{B}}\right\rangle
\]

shows that \( a \cap  {\mu }_{B} \) is a generator of \( {\mathrm{H}}_{0}{\mathbb{R}}^{n} \cong  \Lambda \) . Thus \( \cap  {\mu }_{B} \) maps \( {\mathrm{H}}^{ \bullet  }\left( {{\mathbb{R}}^{n},{\mathbb{R}}^{n} - B}\right) \) isomorphically to \( {\mathrm{H}}_{ \bullet  }\left( {\mathbb{R}}^{n}\right) \) , and passing to the direct limit as \( B \) becomes larger it follows that the homomorphism \( D \) maps \( {\mathrm{H}}_{c}^{ \bullet  }\left( {\mathbb{R}}^{n}\right) \) isomorphically onto \( {\mathrm{H}}_{ \bullet  }\left( {\mathbb{R}}^{n}\right) \) .

Case 2. Suppose that \( M = U \cup  V \) where the theorem is true for the open subsets \( U, V \) and \( U \cap  V \) .

We will construct a commutative diagram where the bottom line is a Mayer-Vietoris sequence [ES52, p. 37]. The construction of the bottom sequence is similar to that in the proof of Lemma A.7. To construct the top exact sequence, note that for each compact \( K \subset  U \) and \( L \subset  V \) there is a relative Mayer-Vietoris sequence

\[
\ldots \overset{\delta }{ \rightarrow  }{\mathrm{H}}^{i}\left( {M, M - K \cap  L}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {M, M - K}\right)  \oplus  {\mathrm{H}}^{i}\left( {M, M - L}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {M, M - K \cup  L}\right)  \rightarrow  \ldots ,
\]

![bo_d7du9galb0pc73deir9g_281_364_1744_1091_190_0.jpg](images/bo_d7du9galb0pc73deir9g_281_364_1744_1091_190_0.jpg)

as in the proof of Lemma A.7. By excision this can be rewritten as

\[
\ldots \overset{\delta }{ \rightarrow  }{\mathrm{H}}^{i}\left( {U \cap  V, U \cap  V - K \cap  L}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {U, U - K}\right)  \oplus  {\mathrm{H}}^{i}\left( {V, V - L}\right)  \rightarrow  {\mathrm{H}}^{i}\left( {M, M - K \cup  L}\right)  \rightarrow  \ldots ,
\]

Now passing to the direct limit as \( K \) and \( L \) become larger we obtain the required sequence.

Applying the Five Lemma to the resulting diagram, this completes the proof in Case 2.

Case 3. \( M \) is the union of a nested family of open sets \( {U}_{\alpha } \) , where the duality theorem is true for each \( {U}_{a} \) .

Then \( {\mathrm{H}}_{c}^{i}M = \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}_{c}^{i}{U}_{\alpha } \) and \( {\mathrm{H}}_{n - i}M = \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}_{n - i}{U}_{\alpha } \) . (Both assertions follow easily from the fact that every compact subset of \( M \) is contained in some \( {U}_{a} \) .) Since the direct limit of isomorphisms is an isomorphism, this completes the proof in Case 3.

Case 4. \( M \) is an open subset of \( {\mathbb{R}}^{n} \) .

If \( M \) is convex, then it is homeomorphic to \( {\mathbb{R}}^{n} \) , so the statement follows from Case 1. More generally choose convex open sets \( {V}_{1},{V}_{2},{V}_{3},\ldots \) with union \( M \) . Using Case 2 inductively, the theorem is true for each \( {V}_{1} \cup  {V}_{2} \cup  \ldots  \cup  {V}_{k} \) . Passing to the direct limit as \( k \rightarrow  \infty \) , it is true for \( M \) .

Case 5. \( M \) is arbitrary.

Cover \( M \) by open sets \( {V}_{a} \) , each diffeomorphic to an open subset of \( {\mathbb{R}}^{n} \) , and choose a well ordering of the index set. (If \( M \) has a countable basis, then we can use the positive integers as index set.) Now a straightforward transfinite induction, using Cases 2,3, and 4, shows that the theorem is true for each partial union \( \mathop{\bigcup }\limits_{{\alpha  < \beta }}{V}_{\alpha } \) . Hence, by Case 3, it is true for \( M \) .

Here are two concluding problems for the reader.

Problem A-1. For an oriented manifold-with-boundary construct the duality isomorphism

\[
{\mathrm{H}}_{c}^{i}M \rightarrow  {\mathrm{H}}_{n - i}\left( {M,\partial M}\right)
\]

Alternatively, defining \( {\mathrm{H}}_{c}^{i}\left( {M,\partial M}\right)  = \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}^{i}\left( {M,\left( {M - K}\right)  \cup  \partial M}\right) \) , construct the isomorphism

\[
{\mathrm{H}}_{c}^{i}\left( {M,\partial M}\right)  \rightarrow  {\mathrm{H}}_{n - i}M
\]

Problem A-2 (Alexander duality). Let \( K \) be a compact subset of the sphere \( {S}^{n} \) which is a retract of some neighborhood. (This hypothesis is needed since we are using singular, rather than Čech, cohomology.) Show that \( {\mathrm{H}}^{i}K \) is isomorphic to the direct limit \( \mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}^{i}U \) as \( U \) ranges over all neighborhoods of \( K \) . Show that \( {\mathrm{H}}^{i}\left( {{S}^{n}, K}\right) \) is isomorphic to

\[
\mathop{\lim }\limits_{ \rightarrow  }{\mathrm{H}}^{i}\left( {{S}^{n}, U}\right)  \cong  {\mathrm{H}}_{\mathrm{c}}^{i}\left( {{S}^{n} - K}\right)  \cong  {\mathrm{H}}_{n - i}\left( {{S}^{n} - K}\right) .
\]

Finally, given \( x \in  K \) and \( y \in  {S}^{n} - K \) , show that

\[
{\mathrm{H}}^{i - 1}\left( {K, x}\right)  \cong  {\mathrm{H}}_{n - i}\left( {{S}^{n} - K, y}\right) .
\]
