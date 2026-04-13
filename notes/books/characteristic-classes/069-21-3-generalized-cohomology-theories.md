# 21.3 Generalized Cohomology Theories

So far we have discussed characteristic classes using ordinary cohomology theory, but using various exotic types of bundles. A quite different generalization arises if we use ordinary vector bundles, but generalize the cohomology. By definition, a generalized cohomology theory is a functor

\( \left( {X, A}\right)  \mapsto  {\mathcal{H}}^{ * }\left( {X, A}\right) \) from pairs of spaces to graded additive groups which satisfies the first six Eilenberg-Steenrod axioms, but fails to satisfy the dimension axiom (the axiom that \( {\mathcal{H}}^{k} \) (point) \( = 0 \) for \( k \neq  0 \) ). Compare [Dye69]. The first and most important example of such a generalized cohomology theory is provided by K-theory.

Definition. For any compact space \( X \) the additive group \( {\mathrm{K}}^{0}\left( X\right) \) is defined by means of a presentation by generators and relations as follows. There is to be one generator \( \left\lbrack  \xi \right\rbrack \) for each isomorphism class of complex vector bundles \( \xi \) over \( X \) and one relation

\[
\left\lbrack  {\xi  \oplus  \eta }\right\rbrack   = \left\lbrack  \xi \right\rbrack   + \left\lbrack  \eta \right\rbrack
\]

for each pair of complex vector bundles. For \( m > 0 \) the group \( {\mathrm{K}}^{-m}\left( X\right) \) can be defined as the kernel of the natural surjection

\[
{\mathrm{K}}^{0}\left( {{S}^{m} \times  X}\right)  \rightarrow  {\mathrm{K}}^{0}\left( {\left( \text{ base point }\right)  \times  X}\right) .
\]

The tensor product operation for complex vector bundles gives rise to a product operation

\[
{\mathrm{K}}^{-m}\left( X\right)  \otimes  {\mathrm{K}}^{-n}\left( Y\right)  \rightarrow  {\mathrm{K}}^{-m - n}\left( {X \times  Y}\right) .
\]

The Bott periodicity theorem now asserts that the product with a standard generator in the group \( {\mathrm{K}}^{-2} \) (point) \( \cong  \mathbb{Z} \) yields an isomorphism

\[
{\mathrm{K}}^{-m}\left( X\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{K}}^{-m - 2}\left( X\right)
\]

(This is closely related to the statement that the classifying space BU has the homotopy type of its own \( {2}^{\text{ nd }} \) loop space.)

The ring \( {\mathrm{{KO}}}^{ * }\left( X\right) \) is defined similarly, using real vector bundles in place of complex vector bundles. In this case there is a periodicity theorem

\[
{\mathrm{{KO}}}^{-m}\left( X\right) \overset{ \cong  }{ \rightarrow  }{\mathrm{{KO}}}^{-m - 8}\left( X\right)
\]

An illustrations of the powers of these methods, we refer the reader to [Ati18],[Ada60],[Ada62], [Ada65],[Ada66] and [ASH72].

Similarly one can define the concept of a generalized homology theory. One important example is provided by the stable homotopy groups

\[
{\pi }_{n}^{s}\left( X\right)  = \mathop{\lim }\limits_{ \rightarrow  }{\pi }_{n + k}\left( {{\sum }^{k}X}\right)
\]

where \( {\sum }^{k}X \) denotes the \( k \) -fold suspension of \( X \) . Another is provided by the oriented bordism groups \( {\Omega }_{n}\left( X\right) \) . (Compare [CF66].) By definition two maps

\[
{f}_{1} : {M}_{1} \rightarrow  X,\;{f}_{2} : {M}_{2} \rightarrow  X
\]

from smooth, compact, oriented \( n \) -manifolds to \( X \) are called bordant if there exists a smooth, compact, oriented manifold-with-boundary \( N \) with \( \partial N = {M}_{1} + \left( {-{M}_{2}}\right) \) , and map \( N \rightarrow  X \) extending \( {f}_{1} \) and \( {f}_{2} \) . The bordism classes of such maps form a group \( {\Omega }_{n}\left( X\right) \) . Note that \( {\Omega }_{n} \) (point) is just the cobordism group \( {\Omega }_{n} \) of Section 17. Each such generalized homology theory is associated with a corresponding generalized cohomology theory. See [Whi62].

In order to study characteristic classes with values in a generalized cohomology theory such as \( {\mathrm{K}}^{ * }\left( B\right) \) , one must first compute \( {\mathrm{K}}^{ * } \) of the appropriate classifying space. In the case of complex K-theory, [AH72] establish an isomorphism between \( {\mathrm{K}}^{ * }\left( {\mathrm{\;B}G}\right) \) for a compact lie group \( G \) and the completion of the representation ring of \( G \) . (See [And64] for the corresponding KO-theory results.)

Just as the orientation of a manifold using the classical homology theory \( {\mathrm{H}}_{ * }\left( {-;\mathbb{Z}}\right) \) plays an important role in studying homology of manifolds, so the analogous K-theory orientations play a basic role in studying the K-theory of manifolds. (Compare [Tho65].) For example [Sul06] has proved the amazing result that a PL-bundle is more or less the same thing as a spherical fibration together with a KO-orientation.

For any K-oriented bundle one can use the approach of Section 8 and Section 19 to define K-theory characteristic classes, using appropriate K-theory operations in place of the Steenrod operations. This idea was initially suggested by [Bot62], and was developed more extensively by [Ada65].

As a typical illustration of the usefulness of these classes, consider the work of [ABP67] on spin cobordism. Suppose that one is given an oriented simply connected manifold \( M \) with \( {\mathrm{w}}_{2}\left( M\right)  = 0 \) . In order to test whether \( M \) bounds an oriented manifold-with-boundary with \( {\mathrm{w}}_{2} = 0 \) one must check, not only that the Stiefel-Whitney numbers (and Pontrjagin numbers) are zero, but also that all KO-characteristic numbers are zero.

If the cohomology theory is the one corresponding to complex bordism, [CF66] have introduced Chern-type classes. The algebra in this situation turns out to be particularly manageable so that rapid progress has been made by several people, notably [Nov67] (cf. [Ada67]).

Appendices
