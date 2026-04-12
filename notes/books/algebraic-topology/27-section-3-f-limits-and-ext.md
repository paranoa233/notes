# 3.F Limits and Ext

It often happens that one has a CW complex \( X \) expressed as a union of an increasing sequence of subcomplexes \( {X}_{0} \subset  {X}_{1} \subset  {X}_{2} \subset  \cdots \) . For example, \( {X}_{i} \) could be the \( i \) -skeleton of \( X \) , or the \( {X}_{i} \) ’s could be finite complexes whose union is \( X \) . In situations of this sort, Proposition 3.33 says that \( {H}_{n}\left( {X;G}\right) \) is the direct limit \( \underline{\lim }{H}_{n}\left( {{X}_{i};G}\right) \) . Our goal in this section is to show this holds more generally for any homology theory, and to derive the corresponding formula for cohomology theories, which is a bit more complicated even for ordinary cohomology with \( \mathbb{Z} \) coefficients. For ordinary homology and cohomology the results apply somewhat more generally than just to CW complexes, since if a space \( X \) is the union of an increasing sequence of subspaces \( {X}_{i} \) with the property that each compact set in \( X \) is contained in some \( {X}_{i} \) , then the singular complex of \( X \) is the union of the singular complexes of the \( {X}_{i} \) ’s, and so this gives a reduction to the CW case.

Passing to limits can often result in nonfinitely generated homology and cohomology groups. At the end of this section we describe some of the rather subtle behavior of Ext for nonfinitely generated groups.

## Direct and Inverse Limits

As a special case of the general definition in \( \text{ § }{3.3} \) , the direct limit \( \underline{\lim }{G}_{i} \) of a sequence of homomorphisms of abelian groups \( {G}_{1}\overset{{\alpha }_{1}}{ \rightarrow  }{G}_{2}\overset{{\alpha }_{2}}{ \rightarrow  }{G}_{3} \rightarrow  \cdots \) is defined to be the quotient of the direct sum \( { \oplus  }_{i}{G}_{i} \) by the subgroup consisting of elements of the form \( \left( {{g}_{1},{g}_{2} - {\alpha }_{1}\left( {g}_{1}\right) ,{g}_{3} - {\alpha }_{2}\left( {g}_{2}\right) ,\cdots }\right) \) . It is easy to see from this definition that every element of \( \underline{\lim }{G}_{i} \) is represented by an element \( {g}_{i} \in  {G}_{i} \) for some \( i \) , and two such representatives \( {g}_{i} \in  {G}_{i} \) and \( {g}_{j} \in  {G}_{j} \) define the same element of \( \underline{\lim }{G}_{i} \) iff they have the same image in some \( {G}_{k} \) under the appropriate composition of \( {\alpha }_{\ell } \) ’s. If all the \( {\alpha }_{i} \) ’s are injective and are viewed as inclusions of subgroups, \( \underline{\lim }{G}_{i} \) is just \( \mathop{\bigcup }\limits_{i}{G}_{i} \) .

Example 3F.1. For a prime \( p \) , consider the sequence \( \mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z} \rightarrow  \cdots \) with all maps multiplication by \( p \) . Then \( \underline{\lim }{G}_{i} \) can be identified with the subgroup \( \mathbb{Z}\left\lbrack  {1/p}\right\rbrack \) of \( \mathbb{Q} \) consisting of rational numbers with denominator a power of \( p \) . More generally, we can realize any subgroup of \( \mathbb{Q} \) as the direct limit of a sequence \( \mathbb{Z} \rightarrow  \mathbb{Z} \rightarrow  \mathbb{Z} \rightarrow  \cdots \) with an appropriate choice of maps. For example, if the \( {n}^{th} \) map is multiplication by \( n \) , then the direct limit is \( \mathbb{Q} \) itself.

Example 3F.2. The sequence of injections \( {\mathbb{Z}}_{p}\overset{p}{ \rightarrow  }{\mathbb{Z}}_{{p}^{2}}\overset{p}{ \rightarrow  }{\mathbb{Z}}_{{p}^{3}} \rightarrow  \cdots \) , with \( p \) prime, has direct limit a group we denote \( {\mathbb{Z}}_{{p}^{\infty }} \) . This is isomorphic to \( \mathbb{Z}\left\lbrack  {1/p}\right\rbrack  /\mathbb{Z} \) , the subgroup of \( \mathbb{Q}/\mathbb{Z} \) represented by fractions with denominator a power of \( p \) . In fact \( \mathbb{Q}/\mathbb{Z} \) is isomorphic to the direct sum of the subgroups \( \mathbb{Z}\left\lbrack  {1/p}\right\rbrack  /\mathbb{Z} \approx  {\mathbb{Z}}_{{p}^{\infty }} \) for all primes \( p \) . It is not hard to determine all the subgroups of \( \mathbb{Q}/\mathbb{Z} \) and see that each one can be realized as a direct limit of finite cyclic groups with injective maps between them. Conversely, every such direct limit is isomorphic to a subgroup of \( \mathbb{Q}/\mathbb{Z} \) .

We can realize these algebraic examples topologically by the following construction. The mapping telescope of a sequence of maps \( {X}_{0}\overset{{f}_{0}}{ \rightarrow  }{X}_{1}\overset{{f}_{1}}{ \rightarrow  }{X}_{2} \rightarrow  \cdots \) is the union of the mapping cylinders \( {M}_{{f}_{i}} \) with the copies of \( {X}_{i} \) in \( {M}_{{f}_{i}} \) and \( {M}_{{f}_{i - 1}} \) identified for all \( i \) . Thus the mapping telescope is the quotient space of the disjoint union \( \mathop{\coprod }\limits_{i}\left( {{X}_{i} \times  \left\lbrack  {i, i + 1}\right\rbrack  }\right) \) in which each point \( \left( {{x}_{i}, i + 1}\right)  \in  {X}_{i} \times  \left\lbrack  {i, i + 1}\right\rbrack \) is identified with \( \left( {{f}_{i}\left( {x}_{i}\right) , i + 1}\right)  \in  {X}_{i + 1} \times  \left\lbrack  {i + 1, i + 2}\right\rbrack \) . In the mapping telescope \( T \) , let \( {T}_{i} \) be the union of the first \( i \) mapping cylinders. This deformation retracts onto \( {X}_{i} \) by deformation retracting each mapping cylinder onto its right end in turn. If the maps \( {f}_{i} \) are cellular, each mapping cylinder is a CW complex and the telescope \( T \) is the increasing union of the subcomplexes \( {T}_{i} \simeq  {X}_{i} \) . Then Proposition 3.33, or Theorem 3F. 8 below, implies that \( {H}_{n}\left( {T;G}\right)  \approx  \underline{\lim }{H}_{n}\left( {{X}_{i};G}\right) \) .

![bo_d7dtv0s91nqc73eq8nv0_320_978_313_608_296_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_320_978_313_608_296_0.jpg)

Example 3F.3. Suppose each \( {f}_{i} \) is a map \( {S}^{n} \rightarrow  {S}^{n} \) of degree \( p \) for a fixed prime \( p \) . Then \( {H}_{n}\left( T\right) \) is the direct limit of the sequence \( \mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z} \rightarrow  \cdots \) considered in Example 3F. 1 above, and \( {\widetilde{H}}_{k}\left( T\right)  = 0 \) for \( k \neq  n \) , so \( T \) is a Moore space \( M\left( {\mathbb{Z}\left\lbrack  {1/p}\right\rbrack  , n}\right) \) .

Example 3F.4. In the preceding example, if we attach a cell \( {e}^{n + 1} \) to the first \( {S}^{n} \) in \( T \) via the identity map of \( {S}^{n} \) , we obtain a space \( X \) which is a Moore space \( M\left( {{\mathbb{Z}}_{{p}^{\infty }}, n}\right) \) since \( X \) is the union of its subspaces \( {X}_{i} = {T}_{i} \cup  {e}^{n + 1} \) , which are \( M\left( {{\mathbb{Z}}_{{p}^{i}}, n}\right) \) ’s, and the inclusion \( {X}_{i} \subset  {X}_{i + 1} \) induces the inclusion \( {\mathbb{Z}}_{{p}^{i}} \subset  {\mathbb{Z}}_{{p}^{i + 1}} \) on \( {H}_{n} \) .

Generalizing these two examples, we can obtain Moore spaces \( M\left( {G, n}\right) \) for arbitrary subgroups \( G \) of \( \mathbb{Q} \) or \( \mathbb{Q}/\mathbb{Z} \) by choosing maps \( {f}_{i} : {S}^{n} \rightarrow  {S}^{n} \) of suitable degrees.

The behavior of cohomology groups is more complicated. If \( X \) is the increasing union of subcomplexes \( {X}_{i} \) , then the cohomology groups \( {H}^{n}\left( {{X}_{i};G}\right) \) , for fixed \( n \) and \( G \) , form a sequence of homomorphisms

\[
\cdots  \rightarrow  {G}_{2}\overset{{\alpha }_{2}}{ \rightarrow  }{G}_{1}\overset{{\alpha }_{1}}{ \rightarrow  }{G}_{0}
\]

Given such a sequence of group homomorphisms, the inverse limit \( \underline{\lim }{G}_{i} \) is defined to be the subgroup of \( \mathop{\prod }\limits_{i}{G}_{i} \) consisting of sequences \( \left( {g}_{i}\right) \) with \( {\alpha }_{i}\left( {g}_{i}\right)  = {g}_{i - 1} \) for all \( i \) . There is a natural map \( \lambda  : {H}^{n}\left( {X;G}\right)  \rightarrow  \underline{\lim }{H}^{n}\left( {{X}_{i};G}\right) \) sending an element of \( {H}^{n}\left( {X;G}\right) \) to its sequence of images in \( {H}^{n}\left( {{X}_{i};G}\right) \) under the maps \( {H}^{n}\left( {X;G}\right)  \rightarrow  {H}^{n}\left( {{X}_{i};G}\right) \) induced by inclusion. One might hope that \( \lambda \) is an isomorphism, but this is not true in general, as we shall see. However, for some choices of \( G \) it is:

Proposition 3F.5. If the CW complex \( X \) is the union of an increasing sequence of sub-complexes \( {X}_{i} \) and if \( G \) is one of the fields \( \mathbb{Q} \) or \( {\mathbb{Z}}_{p} \) , then \( \lambda  : {H}^{n}\left( {X;G}\right)  \rightarrow  \mathop{\lim }\limits_{ \rightarrow  }{H}^{n}\left( {{X}_{i};G}\right) \) is an isomorphism for all \( n \) .

Proof: First we have an easy algebraic fact: Given a sequence of homomorphisms of abelian groups \( {G}_{1}\overset{{\alpha }_{1}}{ \rightarrow  }{G}_{2}\overset{{\alpha }_{2}}{ \rightarrow  }{G}_{3} \rightarrow  \cdots \) , then \( \operatorname{Hom}\left( {\mathop{\lim }\limits^{\underleftarrow{} }{G}_{i}, G}\right)  = \mathop{\lim }\limits^{\underleftarrow{} }\operatorname{Hom}\left( {{G}_{i}, G}\right) \) for any \( G \) . Namely, it follows from the definition of \( \underline{\lim }{G}_{i} \) that a homomorphism \( \varphi  : \underline{\lim }{G}_{i} \rightarrow  G \) is the same thing as a sequence of homomorphisms \( {\varphi }_{i} : {G}_{i} \rightarrow  G \) with \( {\varphi }_{i} = {\varphi }_{i + 1}{\alpha }_{i} \) for all \( i \) . Such a sequence \( \left( {\varphi }_{i}\right) \) is exactly an element of \( \underline{\lim }\operatorname{Hom}\left( {{G}_{i}, G}\right) \) .

Now if \( G \) is a field \( \mathbb{Q} \) or \( {\mathbb{Z}}_{p} \) we have

\[
{H}^{n}\left( {X;G}\right)  = \operatorname{Hom}\left( {{H}_{n}\left( {X;G}\right) , G}\right)
\]

\[
= \operatorname{Hom}\left( {\mathop{\lim }\limits_{ \rightarrow  }{H}_{n}\left( {{X}_{i};G}\right) , G}\right)
\]

\[
= \mathop{\lim }\limits_{ \leftarrow  }\operatorname{Hom}\left( {{H}_{n}\left( {{X}_{i};G}\right) , G}\right)
\]

\[
= \mathop{\lim }\limits_{ \leftarrow  }{H}^{n}\left( {{X}_{i};G}\right)
\]

Let us analyze what happens for cohomology with an arbitrary coefficient group, or more generally for any cohomology theory. Given a sequence of homomorphisms of abelian groups

\[
\cdots  \rightarrow  {G}_{2}\overset{{\alpha }_{2}}{ \rightarrow  }{G}_{1}\overset{{\alpha }_{1}}{ \rightarrow  }{G}_{0}
\]

define a map \( \delta  : \mathop{\prod }\limits_{i}{G}_{i} \rightarrow  \mathop{\prod }\limits_{i}{G}_{i} \) by \( \delta \left( {\cdots ,{g}_{i},\cdots }\right)  = \left( {\cdots ,{g}_{i} - {\alpha }_{i + 1}\left( {g}_{i + 1}\right) ,\cdots }\right) \) , so that \( \underline{\lim }{G}_{i} \) is the kernel of \( \delta \) . Denoting the cokernel of \( \delta \) by \( {\underline{\lim }}^{1}{G}_{i} \) , we have then an exact sequence

\[
0 \rightarrow  \mathop{\lim }\limits_{ \leftarrow  }{G}_{i} \rightarrow  \mathop{\prod }\limits_{i}{G}_{i}\overset{\delta }{ \rightarrow  }\mathop{\prod }\limits_{i}{G}_{i} \rightarrow  {\mathop{\lim }\limits_{ \leftarrow  }}^{1}{G}_{i} \rightarrow  0
\]

This may be compared with the corresponding situation for the direct limit of a sequence \( {G}_{1}\overset{{\alpha }_{1}}{ \rightarrow  }{G}_{2}\overset{{\alpha }_{2}}{ \rightarrow  }{G}_{3} \rightarrow  \cdots \) . In this case one has a short exact sequence

\[
0 \rightarrow  {\bigoplus }_{i}{G}_{i}\overset{\delta }{ \rightarrow  }{\bigoplus }_{i}{G}_{i} \rightarrow  \mathop{\lim }\limits_{ \rightarrow  }{G}_{i} \rightarrow  0
\]

where \( \delta \left( {\cdots ,{g}_{i},\cdots }\right)  = \left( {\cdots ,{g}_{i} - {\alpha }_{i - 1}\left( {g}_{i - 1}\right) ,\cdots }\right) \) , so \( \delta \) is injective and there is no term \( {\underline{\lim }}^{1}{G}_{i} \) analogous to \( {\underline{\lim }}^{1}{G}_{i} \) .

Here are a few simple observations about \( \underline{\lim } \) and \( {\underline{\lim }}^{1} \) :

- If all the \( {\alpha }_{i} \) ’s are isomorphisms then \( \underline{\lim }{G}_{i} \approx  {G}_{0} \) and \( {\underline{\lim }}^{1}{G}_{i} = 0 \) . In fact, \( {\underline{\lim }}^{1}{G}_{i} = 0 \) if each \( {\alpha }_{i} \) is surjective, for to realize a given element \( \left( {h}_{i}\right)  \in  \mathop{\prod }\limits_{i}{G}_{i} \) as \( \delta \left( {g}_{i}\right) \) we can take \( {g}_{0} = 0 \) and then solve \( {\alpha }_{1}\left( {g}_{1}\right)  =  - {h}_{0},{\alpha }_{2}\left( {g}_{2}\right)  = {g}_{1} - {h}_{1},\cdots \) .

- If all the \( {\alpha }_{i} \) ’s are zero then \( \underline{\lim }{G}_{i} = {\underline{\lim }}^{1}{G}_{i} = 0 \) .

- Deleting a finite number of terms from the end of the sequence \( \cdots  \rightarrow  {G}_{1} \rightarrow  {G}_{0} \) does not affect \( \underline{\lim }{G}_{i} \) or \( {\underline{\lim }}^{1}{G}_{i} \) . More generally, \( \underline{\lim }{G}_{i} \) and \( {\underline{\lim }}^{1}{G}_{i} \) are unchanged if we replace the sequence \( \cdots  \rightarrow  {G}_{1} \rightarrow  {G}_{0} \) by a subsequence, with the appropriate compositions of \( {\alpha }_{j} \) ’s as the maps.

Example 3F.6. Consider the sequence of natural surjections \( \cdots  \rightarrow  {\mathbb{Z}}_{{p}^{3}} \rightarrow  {\mathbb{Z}}_{{p}^{2}} \rightarrow  {\mathbb{Z}}_{p} \) with \( p \) a prime. The inverse limit of this sequence is a famous object in number theory, called the \( \mathbf{p} \) -adic integers. Our notation for it will be \( {\widehat{\mathbb{Z}}}_{p} \) . It is actually a commutative ring, not just a group, since the projections \( {\mathbb{Z}}_{{p}^{i + 1}} \rightarrow  {\mathbb{Z}}_{{p}^{i}} \) are ring homomorphisms, but we will be interested only in the additive group structure. Elements of \( {\widehat{\mathbb{Z}}}_{p} \) are infinite sequences \( \left( {\cdots ,{a}_{2},{a}_{1}}\right) \) with \( {a}_{i} \in  {\mathbb{Z}}_{{p}^{i}} \) such that \( {a}_{i} \) is the mod \( {p}^{i} \) reduction of \( {a}_{i + 1} \) . For each choice of \( {a}_{i} \) there are exactly \( p \) choices for \( {a}_{i + 1} \) , so \( {\widehat{\mathbb{Z}}}_{p} \) is uncountable. There is a natural inclusion \( \mathbb{Z} \subset  {\widehat{\mathbb{Z}}}_{p} \) as the constant sequences \( {a}_{i} = n \in  \mathbb{Z} \) . It is easy to see that \( {\widehat{\mathbb{Z}}}_{p} \) is torsionfree by checking that it has no elements of prime order.

There is another way of looking at \( {\widehat{\mathbb{Z}}}_{p} \) . An element of \( {\widehat{\mathbb{Z}}}_{p} \) has a unique representation as a sequence \( \left( {\cdots ,{a}_{2},{a}_{1}}\right) \) of integers \( {a}_{i} \) with \( 0 \leq  {a}_{i} < {p}^{i} \) for each \( i \) . We can write each \( {a}_{i} \) uniquely in the form \( {b}_{i - 1}{p}^{i - 1} + \cdots  + {b}_{1}p + {b}_{0} \) with \( 0 \leq  {b}_{j} < p \) . The fact that \( {a}_{i + 1} \) reduces \( {\;\operatorname{mod}\;{p}^{i}} \) to \( {a}_{i} \) means that the numbers \( {b}_{j} \) depend only on the element \( \left( {\cdots ,{a}_{2},{a}_{1}}\right)  \in  {\widehat{\mathbb{Z}}}_{p} \) , so we can view the elements of \( {\widehat{\mathbb{Z}}}_{p} \) as the ’base \( p \) infinite numbers’ \( \cdots {b}_{1}{b}_{0} \) with \( 0 \leq  {b}_{i} < p \) for all \( i \) , with the familiar rule for addition in base \( p \) notation. The finite expressions \( {b}_{n}\cdots {b}_{1}{b}_{0} \) represent the nonnegative integers, but negative integers have infinite expansions. For example,-1has \( {b}_{i} = p - 1 \) for all \( i \) , as one can see by adding 1 to this number.

Since the maps \( {\mathbb{Z}}_{{p}^{i + 1}} \rightarrow  {\mathbb{Z}}_{{p}^{i}} \) are surjective, \( {\underline{\lim }}^{1}{\mathbb{Z}}_{{p}^{i}} = 0 \) . The next example shows how \( p \) -adic integers can also give rise to a nonvanishing \( {\underline{\lim }}^{1} \) term.

Example 3F.7. Consider the sequence \( \cdots  \rightarrow  \mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z} \) for \( p \) prime. In this case the inverse limit is zero since a nonzero integer can only be divided by \( p \) finitely often. The \( {\underline{\lim }}^{1} \) term is the cokernel of the map \( \delta  : \mathop{\prod }\limits_{\infty }\mathbb{Z} \rightarrow  \mathop{\prod }\limits_{\infty }\mathbb{Z} \) given by \( \delta \left( {{y}_{1},{y}_{2},\cdots }\right)  = \; \left( {{y}_{1} - p{y}_{2},{y}_{2} - p{y}_{3},\cdots }\right) \) . We claim that the map \( {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \rightarrow \) Coker \( \delta \) sending a \( p \) -adic number \( \cdots {b}_{1}{b}_{0} \) as in the preceding example to \( \left( {{b}_{0},{b}_{1},\cdots }\right) \) is an isomorphism. To see this, note that the image of \( \delta \) consists of the sums \( {y}_{1}\left( {1,0,\cdots }\right)  + {y}_{2}\left( {-p,1,0,\cdots }\right)  + \; {y}_{3}\left( {0, - p,1,0,\cdots }\right)  + \cdots \) . The terms after \( {y}_{1}\left( {1,0,\cdots }\right) \) give exactly the relations that hold among the \( p \) -adic numbers \( \cdots {b}_{1}{b}_{0} \) , and in particular allow one to reduce an arbitrary sequence \( \left( {{b}_{0},{b}_{1},\cdots }\right) \) to a unique sequence with \( 0 \leq  {b}_{i} < p \) for all \( i \) . The term \( {y}_{1}\left( {1,0,\cdots }\right) \) corresponds to the subgroup \( \mathbb{Z} \subset  {\widehat{\mathbb{Z}}}_{p} \) .

We come now to the main result of this section:

Theorem 3F.8. For a CW complex \( X \) which is the union of an increasing sequence of subcomplexes \( {X}_{0} \subset  {X}_{1} \subset  \cdots \) there is an exact sequence

\[
0 \rightarrow  {\lim }^{1}{h}^{n - 1}\left( {X}_{i}\right)  \rightarrow  {h}^{n}\left( X\right) \overset{\lambda }{ \rightarrow  }{\lim }^{n}{h}^{n}\left( {X}_{i}\right)  \rightarrow  0
\]

where \( {h}^{ * } \) is any reduced or unreduced cohomology theory. For any homology theory \( {h}_{ * } \) , reduced or unreduced, the natural maps \( \underline{\lim }{h}_{n}\left( {X}_{i}\right)  \rightarrow  {h}_{n}\left( X\right) \) are isomorphisms.

Proof: Let \( T \) be the mapping telescope of the inclusion sequence \( {X}_{0} \hookrightarrow  {X}_{1} \hookrightarrow  \cdots \) . This is a subcomplex of \( X \times  \lbrack 0,\infty ) \) when \( \lbrack 0,\infty ) \) is given the CW structure with the integer points as 0-cells. We have \( T \simeq  X \) since \( T \) is a deformation retract of \( X \times  \lbrack 0,\infty ) \) , as we showed in the proof of Lemma 2.34 in the special case that \( {X}_{i} \) is the \( i \) -skeleton of \( X \) , but the argument works just as well for arbitrary subcomplexes \( {X}_{i} \) .

Let \( {T}_{1} \subset  T \) be the union of the products \( {X}_{i} \times  \left\lbrack  {i, i + 1}\right\rbrack \) for \( i \) odd, and let \( {T}_{2} \) be the corresponding union for \( i \) even. Thus \( {T}_{1} \cap  {T}_{2} = \mathop{\coprod }\limits_{i}{X}_{i} \) and \( {T}_{1} \cup  {T}_{2} = T \) . For an unreduced cohomology theory \( {h}^{ * } \) we have then a Mayer-Vietoris sequence

\[
\begin{matrix} {h}^{n - 1}\left( {T}_{1}\right)  \oplus  {h}^{n - 1}\left( {T}_{2}\right)  \rightarrow  {h}^{n - 1}\left( {{T}_{1} \cap  {T}_{2}}\right)  \rightarrow  {h}^{n}\left( T\right)  \rightarrow  {h}^{n}\left( {T}_{1}\right)  \oplus  {h}^{n}\left( {T}_{2}\right)  \rightarrow  {h}^{n}\left( {{T}_{1} \cap  {T}_{2}}\right) \\  l \end{matrix}
\]

\[
{\Pi }_{i}{h}^{n - 1}\left( {X}_{i}\right) \overset{\varphi }{ \rightarrow  }{\Pi }_{i}{h}^{n - 1}\left( {X}_{i}\right)  \rightarrow  {h}^{n}\left( X\right)  \rightarrow  {\Pi }_{i}{h}^{n}\left( {X}_{i}\right) \overset{\varphi }{ \rightarrow  }{\Pi }_{i}{h}^{n}\left( {X}_{i}\right)
\]

The maps \( \varphi \) making the diagram commute are given by the formula \( \varphi \left( {\cdots ,{g}_{i},\cdots }\right)  = \; \left( {\cdots ,{\left( -1\right) }^{i - 1}\left( {{g}_{i} - \rho \left( {g}_{i + 1}\right) }\right) ,\cdots }\right) \) , the \( \rho \) ’s being the appropriate restriction maps. This differs from \( \delta \) only in the sign of its even coordinates, so if we change the isomorphism \( {h}^{k}\left( {{T}_{1} \cap  {T}_{2}}\right)  \approx  \mathop{\prod }\limits_{i}{h}^{k}\left( {X}_{i}\right) \) by inserting a minus sign in the even coordinates, we can replace \( \varphi \) by \( \delta \) in the second row of the diagram. This row then yields a short exact sequence \( 0 \rightarrow \) Coker \( \delta  \rightarrow  {h}^{n}\left( {X;G}\right)  \rightarrow  \operatorname{Ker}\delta  \rightarrow  0 \) , finishing the proof for unreduced cohomology.

The same argument works for reduced cohomology if we use the reduced telescope obtained from \( T \) by collapsing \( \left\{  {x}_{0}\right\}   \times  \lbrack 0,\infty ) \) to a point, for \( {x}_{0} \) a basepoint 0-cell of \( {X}_{0} \) . Then \( {T}_{1} \cap  {T}_{2} = \mathop{\bigvee }\limits_{i}{X}_{i} \) rather than \( \mathop{\coprod }\limits_{i}{X}_{i} \) , and the rest of the argument goes through unchanged. The proof also applies for homology theories, with direct products replaced by direct sums in the second row of the diagram. As we noted earlier, Ker \( \delta  = 0 \) in the direct limit case, and Coker \( \delta  = \underline{\lim } \) .

Example 3F.9. As in Example 3F.3, consider the mapping telescope \( T \) for the sequence of degree \( p \) maps \( {S}^{n} \rightarrow  {S}^{n} \rightarrow  \cdots \) . Letting \( {T}_{i} \) be the union of the first \( i \) mapping cylinders in the telescope, the inclusions \( {T}_{1} \hookrightarrow  {T}_{2} \hookrightarrow  \cdots \) induce on \( {H}^{n}\left( {-;\mathbb{Z}}\right) \) the sequence \( \cdots  \rightarrow  \mathbb{Z}\overset{p}{ \rightarrow  }\mathbb{Z} \) in Example 3F.7. From the theorem we deduce that \( {H}^{n + 1}\left( {T;\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \) and \( {\widetilde{H}}^{k}\left( {T;\mathbb{Z}}\right)  = 0 \) for \( k \neq  n + 1 \) . Thus we have the rather strange situation that the CW complex \( T \) is the union of subcomplexes \( {T}_{i} \) each having cohomology consisting only of a \( \mathbb{Z} \) in dimension \( n \) , but \( T \) itself has no cohomology in dimension \( n \) and instead has a huge uncountable group \( {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \) in dimension \( n + 1 \) . This contrasts sharply with what happens for homology, where the groups \( {H}_{n}\left( {T}_{i}\right)  \approx  \mathbb{Z} \) fit together nicely to give \( {H}_{n}\left( T\right)  \approx  \mathbb{Z}\left\lbrack  {1/p}\right\rbrack  . \)

Example 3F.10. A more reasonable behavior is exhibited if we consider the space \( X = M\left( {{\mathbb{Z}}_{{p}^{\infty }}, n}\right) \) in Example 3F.4 expressed as the union of its subspaces \( {X}_{i} \) . By the universal coefficient theorem, the reduced cohomology of \( {X}_{i} \) with \( \mathbb{Z} \) coefficients consists of a \( {\mathbb{Z}}_{{p}^{i}} = \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{i}},\mathbb{Z}}\right) \) in dimension \( n + 1 \) . The inclusion \( {X}_{i} \hookrightarrow  {X}_{i + 1} \) induces the inclusion \( {\mathbb{Z}}_{{p}^{i}} \hookrightarrow  {\mathbb{Z}}_{{p}^{i + 1}} \) on \( {H}_{n} \) , and on Ext this induced map is a surjection \( {\mathbb{Z}}_{{p}^{i + 1}} \rightarrow  {\mathbb{Z}}_{{p}^{i}} \) as one can see by looking at the diagram of free resolutions on the left:

![bo_d7dtv0s91nqc73eq8nv0_323_255_1925_1331_191_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_323_255_1925_1331_191_0.jpg)

Applying \( \operatorname{Hom}\left( {-,\mathbb{Z}}\right) \) to this diagram, we get the diagram on the right, with exact rows, and the left-hand vertical map is a surjection since the vertical map to the right of it is surjective. Thus the sequence \( \cdots  \rightarrow  {H}^{n + 1}\left( {{X}_{2};\mathbb{Z}}\right)  \rightarrow  {H}^{n + 1}\left( {{X}_{1};\mathbb{Z}}\right) \) is the sequence in Example 3F.6, and we deduce that \( {H}^{n + 1}\left( {X;\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) , the \( p \) -adic integers, and \( {\widetilde{H}}^{k}\left( {X;\mathbb{Z}}\right)  = 0 \) for \( k \neq  n + 1 \) .

This example can be related to the preceding one. If we view \( X \) as the mapping cone of the inclusion \( {S}^{n} \hookrightarrow  T \) of one end of the telescope, then the long exact sequences of homology and cohomology groups for the pair \( \left( {T,{S}^{n}}\right) \) reduce to the short exact sequences at the right.

\[
\begin{matrix} 0 \rightarrow  {H}_{n}\left( {S}^{n}\right)  \rightarrow  {H}_{n}\left( T\right)  \rightarrow  {H}_{n}\left( X\right)  \rightarrow  0 \\  \parallel \;\parallel \;\parallel \;\parallel \\  \mathbb{Z}\left\lbrack  {1/p}\right\rbrack  \;{\mathbb{Z}}_{{p}^{\infty }} \end{matrix}
\]

\[
\begin{matrix} 0 \rightarrow  {H}^{n}\left( {S}^{n}\right)  \rightarrow  {H}^{n + 1}\left( X\right)  \rightarrow  {H}^{n + 1}\left( T\right)  \rightarrow  0 \\  {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \end{matrix}
\]

From these examples and the universal coefficient theorem we obtain isomorphisms \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) and \( \operatorname{Ext}\left( {\mathbb{Z}\left\lbrack  {1/p}\right\rbrack  ,\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \) . These can also be derived directly from the definition of Ext. A free resolution of \( {\mathbb{Z}}_{{p}^{\infty }} \) is

\[
0 \rightarrow  {\mathbb{Z}}^{\infty }\overset{\varphi }{ \rightarrow  }{\mathbb{Z}}^{\infty } \rightarrow  {\mathbb{Z}}_{{p}^{\infty }} \rightarrow  0
\]

where \( {\mathbb{Z}}^{\infty } \) is the direct sum of an infinite number of \( \mathbb{Z} \) ’s, the sequences \( \left( {{x}_{1},{x}_{2},\cdots }\right) \) of integers all but finitely many of which are zero, and \( \varphi \) sends \( \left( {{x}_{1},{x}_{2},\cdots }\right) \) to \( \left( {p{x}_{1} - {x}_{2}, p{x}_{2} - {x}_{3},\cdots }\right) \) . We can view \( \varphi \) as the linear map corresponding to the infinite matrix with \( p \) ’s on the diagonal,-1’s just above the diagonal, and 0 ’s everywhere else. Clearly \( \operatorname{Ker}\varphi  = 0 \) since integers cannot be divided by \( p \) infinitely often. The image of \( \varphi \) is generated by the vectors \( \left( {p,0,\cdots }\right) ,\left( {-1, p,0,\cdots }\right) ,\left( {0, - 1, p,0,\cdots }\right) ,\cdots \) so Coker \( \varphi  \approx  {\mathbb{Z}}_{{p}^{\infty }} \) . Dualizing by taking \( \operatorname{Hom}\left( {-,\mathbb{Z}}\right) \) , we have \( \operatorname{Hom}\left( {{\mathbb{Z}}^{\infty },\mathbb{Z}}\right) \) the infinite direct product of \( \mathbb{Z} \) ’s, and \( {\varphi }^{ * }\left( {{y}_{1},{y}_{2},\cdots }\right)  = \left( {p{y}_{1}, p{y}_{2} - {y}_{1}, p{y}_{3} - {y}_{2},\cdots }\right) \) , corresponding to the transpose of the matrix of \( \varphi \) . By definition, \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  = \) Coker \( {\varphi }^{ * } \) . The image of \( {\varphi }^{ * } \) consists of the infinite sums \( {y}_{1}\left( {p, - 1,0\cdots }\right)  + {y}_{2}\left( {0, p, - 1,0,\cdots }\right)  + \cdots \) , so Coker \( {\varphi }^{ * } \) can be identified with \( {\widehat{\mathbb{Z}}}_{p} \) by rewriting a sequence \( \left( {{z}_{1},{z}_{2},\cdots }\right) \) as the \( p \) -adic number \( \cdots {z}_{2}{z}_{1} \) .

The calculation \( \operatorname{Ext}\left( {\mathbb{Z}\left\lbrack  {1/p}\right\rbrack  ,\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \) is quite similar. A free resolution of \( \mathbb{Z}\left\lbrack  {1/p}\right\rbrack \) can be obtained from the free resolution of \( {\mathbb{Z}}_{{p}^{\infty }} \) by omitting the first column of the matrix of \( \varphi \) and, for convenience, changing sign. This gives the formula \( \varphi \left( {{x}_{1},{x}_{2},\cdots }\right)  = \left( {{x}_{1},{x}_{2} - p{x}_{1},{x}_{3} - p{x}_{2},\cdots }\right) \) , with the image of \( \varphi \) generated by the elements \( \left( {1, - p,0,\cdots }\right) ,\left( {0,1, - p,0,\cdots }\right) ,\cdots \) . The dual map \( {\varphi }^{ * } \) is given by \( {\varphi }^{ * }\left( {{y}_{1},{y}_{2},\cdots }\right)  = \left( {{y}_{1} - p{y}_{2},{y}_{2} - p{y}_{3},\cdots }\right) \) , and this has image consisting of the sums \( {y}_{1}\left( {1,0\cdots }\right)  + {y}_{2}\left( {-p,1,0,\cdots }\right)  + {y}_{3}\left( {0, - p,1,0,\cdots }\right)  + \cdots \) , so we get \( \operatorname{Ext}\left( {\mathbb{Z}\left\lbrack  {1/p}\right\rbrack  ,\mathbb{Z}}\right)  = \) Coker \( {\varphi }^{ * } \approx  {\widehat{\mathbb{Z}}}_{p}/\mathbb{Z} \) . Note that \( {\varphi }^{ * } \) is exactly the map \( \delta \) in Example 3F.7.

It is interesting to note also that the map \( \varphi  : {\mathbb{Z}}^{\infty } \rightarrow  {\mathbb{Z}}^{\infty } \) in the two cases \( {\mathbb{Z}}_{{p}^{\infty }} \) and \( \mathbb{Z}\left\lbrack  {1/p}\right\rbrack \) is precisely the cellular boundary map \( {H}_{n + 1}\left( {{X}^{n + 1},{X}^{n}}\right)  \rightarrow  {H}_{n}\left( {{X}^{n},{X}^{n - 1}}\right) \) for the Moore space \( M\left( {{\mathbb{Z}}_{{p}^{\infty }}, n}\right) \) or \( M\left( {\mathbb{Z}\left\lbrack  {1/p}\right\rbrack  , n}\right) \) constructed as the mapping telescope of the sequence of degree \( p \) maps \( {S}^{n} \rightarrow  {S}^{n} \rightarrow  \cdots \) , with a cell \( {e}^{n + 1} \) attached to the first \( {S}^{n} \) in the case of \( {\mathbb{Z}}_{{p}^{\infty }} \) .

## More About Ext

The functors Hom and Ext behave fairly simply for finitely generated groups, when cohomology and homology are essentially the same except for a dimension shift in the torsion. But matters are more complicated in the nonfinitely generated case. A useful tool for getting a handle on this complication is the following:

Proposition 3F.11. Given an abelian group \( G \) and a short exact sequence of abelian groups \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) , there are exact sequences

\[
0 \rightarrow  \operatorname{Hom}\left( {G, A}\right)  \rightarrow  \operatorname{Hom}\left( {G, B}\right)  \rightarrow  \operatorname{Hom}\left( {G, C}\right)  \rightarrow  \operatorname{Ext}\left( {G, A}\right)  \rightarrow  \operatorname{Ext}\left( {G, B}\right)  \rightarrow  \operatorname{Ext}\left( {G, C}\right)  \rightarrow  0
\]

\[
0 \rightarrow  \operatorname{Hom}\left( {C, G}\right)  \rightarrow  \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  \operatorname{Ext}\left( {C, G}\right)  \rightarrow  \operatorname{Ext}\left( {B, G}\right)  \rightarrow  \operatorname{Ext}\left( {A, G}\right)  \rightarrow  0
\]

Proof: A free resolution \( 0 \rightarrow  {F}_{1} \rightarrow  {F}_{0} \rightarrow  G \rightarrow  0 \) gives rise to a commutative diagram

\[
0 \rightarrow  \operatorname{Hom}\left( {{F}_{0}, A}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{0}, B}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{0}, C}\right)  \rightarrow  0
\]

\[
0 \rightarrow  \operatorname{Hom}\left( {{F}_{1}, A}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{1}, B}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{1}, C}\right)  \rightarrow  0
\]

Since \( {F}_{0} \) and \( {F}_{1} \) are free, the two rows are exact, as they are simply direct products of copies of the exact sequence \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) , in view of the general fact that \( \operatorname{Hom}\left( {{\bigoplus }_{i}{G}_{i}, H}\right)  = \mathop{\prod }\limits_{i}\operatorname{Hom}\left( {{G}_{i}, H}\right) \) . Enlarging the diagram by zeros above and below, it becomes a short exact sequence of chain complexes, and the associated long exact sequence of homology groups is the first of the two six-term exact sequences in the proposition.

![bo_d7dtv0s91nqc73eq8nv0_325_1049_1182_530_405_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_325_1049_1182_530_405_0.jpg)

To obtain the other exact sequence we will construct the commutative diagram at the right, where the columns are free resolutions and the rows are exact. To start, let \( {F}_{0} \rightarrow  A \) and \( {F}_{0}^{\prime \prime } \rightarrow  C \) be surjections from free abelian groups onto \( A \) and \( C \) . Then let \( {F}_{0}^{\prime } = {F}_{0} \oplus  {F}_{0}^{\prime \prime } \) , with the obvious maps in the second row, inclusion and projection. The map \( {F}_{0}^{\prime } \rightarrow  B \) is defined on the summand \( {F}_{0} \) to make the lower left square commute, and on the summand \( {F}_{0}^{\prime \prime } \) it is defined by sending basis elements of \( {F}_{0}^{\prime \prime } \) to elements of \( B \) mapping to the images of these basis elements in \( C \) , so the lower right square also commutes. Now we have the bottom two rows of the diagram, and we can regard these two rows as a short exact sequence of two-term chain complexes. The associated long exact sequence of homology groups has six terms, the first three being the kernels of the three vertical maps to \( A, B \) , and \( C \) , and the last three being the cokernels of these maps. Since the vertical maps to \( A \) and \( C \) are surjective, the fourth and sixth of the six homology groups vanish, hence also the fifth, which says the vertical map to \( B \) is surjective. The first three of the original six homology groups form a short exact sequence, and we let this be the top row of the diagram, formed by the kernels of the vertical maps to \( A, B \) , and \( C \) . These kernels are subgroups of free abelian groups, hence are also free.

Thus the three columns are free resolutions. The upper two squares automatically commute, so the construction of the diagram is complete.

The first two rows of the diagram split by freeness, so applying \( \operatorname{Hom}\left( {-, G}\right) \) yields a diagram

\( \downarrow  \; \downarrow  \; \downarrow \)

\[
0 \rightarrow  \operatorname{Hom}\left( {{F}_{0}^{\prime \prime }, G}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{0}^{\prime }, G}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{0}, G}\right)  \rightarrow  0
\]

\[
0 \rightarrow  \operatorname{Hom}\left( {{F}_{1}^{\prime \prime }, G}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{1}^{\prime }, G}\right)  \rightarrow  \operatorname{Hom}\left( {{F}_{1}, G}\right)  \rightarrow  0
\]

with exact rows. Again viewing this as a short exact sequence of chain complexes, the associated long exact sequence of homology groups is the second six-term exact sequence in the statement of the proposition.

The second sequence in the proposition says in particular that an injection \( A \rightarrow  B \) induces a surjection \( \operatorname{Ext}\left( {B, C}\right)  \rightarrow  \operatorname{Ext}\left( {A, C}\right) \) for any \( C \) . For example, if \( A \) has torsion, this says \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is nonzero since it maps onto \( \operatorname{Ext}\left( {{\mathbb{Z}}_{n},\mathbb{Z}}\right)  \approx  {\mathbb{Z}}_{n} \) for some \( n > 1 \) . The calculation \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) earlier in this section shows that torsion in \( A \) does not necessarily yield torsion in \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) , however.

Two other useful formulas whose proofs we leave as exercises are:

\[
\operatorname{Ext}\left( {{\bigoplus }_{i}{A}_{i}, B}\right)  \approx  \mathop{\prod }\limits_{i}\operatorname{Ext}\left( {{A}_{i}, B}\right) \;\operatorname{Ext}\left( {A,{\bigoplus }_{i}{B}_{i}}\right)  \approx  {\bigoplus }_{i}\operatorname{Ext}\left( {A,{B}_{i}}\right)
\]

For example, since \( \mathbb{Q}/\mathbb{Z} = {\bigoplus }_{p}{\mathbb{Z}}_{{p}^{\infty }} \) we obtain \( \operatorname{Ext}\left( {\mathbb{Q}/\mathbb{Z},\mathbb{Z}}\right)  \approx  \mathop{\prod }\limits_{p}{\widehat{\mathbb{Z}}}_{p} \) from the calculation \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) . Then from the exact sequence \( 0 \rightarrow  \mathbb{Z} \rightarrow  \mathbb{Q} \rightarrow  \mathbb{Q}/\mathbb{Z} \rightarrow  0 \) we get \( \operatorname{Ext}\left( {\mathbb{Q},\mathbb{Z}}\right)  \approx  \left( {\mathop{\prod }\limits_{p}{\widehat{\mathbb{Z}}}_{p}}\right) /\mathbb{Z} \) using the second exact sequence in the proposition.

In these examples the groups \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) are rather large, and the next result says this is part of a general pattern:

Proposition 3F.12. If \( A \) is not finitely generated then either \( \operatorname{Hom}\left( {A,\mathbb{Z}}\right) \) or \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable. Hence if \( {H}_{n}\left( {X;\mathbb{Z}}\right) \) is not finitely generated then either \( {H}^{n}\left( {X;\mathbb{Z}}\right) \) or \( {H}^{n + 1}\left( {X;\mathbb{Z}}\right) \) is uncountable.

Both possibilities can occur, as we see from the examples \( \operatorname{Hom}\left( {{\bigoplus }_{\infty }\mathbb{Z},\mathbb{Z}}\right)  \approx  \mathop{\prod }\limits_{\infty }\mathbb{Z} \) and \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) .

This proposition has some interesting topological consequences. First, it implies that if a space \( X \) has \( {\widetilde{H}}^{ * }\left( {X;\mathbb{Z}}\right)  = 0 \) , then \( {\widetilde{H}}_{ * }\left( {X;\mathbb{Z}}\right)  = 0 \) , since the case of finitely generated homology groups follows from our earlier results. And second, it says that one cannot always construct a space \( X \) with prescribed cohomology groups \( {H}^{n}\left( {X;\mathbb{Z}}\right) \) , as one can for homology. For example there is no space whose only nonvanishing \( {\widetilde{H}}^{n}\left( {X;\mathbb{Z}}\right) \) is a countable nonfinitely generated group such as \( \mathbb{Q} \) or \( \mathbb{Q}/\mathbb{Z} \) . Even in the finitely generated case the dimension \( n = 1 \) is somewhat special since the group \( {H}^{1}\left( {X;\mathbb{Z}}\right)  \approx  \operatorname{Hom}\left( {{H}_{1}\left( X\right) ,\mathbb{Z}}\right) \) is always torsionfree.

Proof: We begin with two consequences of Proposition 3F.11:

(a) An inclusion \( B \hookrightarrow  A \) induces a surjection \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right)  \rightarrow  \operatorname{Ext}\left( {B,\mathbb{Z}}\right) \) . Hence \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable if \( \operatorname{Ext}\left( {B,\mathbb{Z}}\right) \) is.

(b) If \( A \rightarrow  A/B \) is a quotient map with \( B \) finitely generated, then the first term in the exact sequence \( \operatorname{Hom}\left( {B,\mathbb{Z}}\right)  \rightarrow  \operatorname{Ext}\left( {A/B,\mathbb{Z}}\right)  \rightarrow  \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is countable, so \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable if \( \operatorname{Ext}\left( {A/B,\mathbb{Z}}\right) \) is.

There are two explicit calculations that will be used in the proof:

(c) If \( A \) is a direct sum of infinitely many nontrivial finite cyclic groups, then \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable, the product of infinitely many nontrivial groups \( \operatorname{Ext}\left( {{\mathbb{Z}}_{n},\mathbb{Z}}\right)  \approx  {\mathbb{Z}}_{n} \) .

(d) For \( p \) prime, Example 3F.10 gives \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) which is uncountable.

Consider now the map \( A \rightarrow  A \) given by \( a \mapsto  {pa} \) for a fixed prime \( p \) . Denote the kernel, image, and cokernel of this map by \( {}_{p}A,{pA} \) , and \( {A}_{p} \) , respectively. The functor \( A \mapsto  {A}_{p} \) is the same as \( A \mapsto  A \otimes  {\mathbb{Z}}_{p} \) . We call the dimension of \( {A}_{p} \) as a vector space over \( {\mathbb{Z}}_{p} \) the \( p \) -rank of \( A \) .

Suppose the \( p \) -rank of \( A \) is infinite. Then \( \operatorname{Ext}\left( {{A}_{p},\mathbb{Z}}\right) \) is uncountable by (c). There is an exact sequence \( 0 \rightarrow  {pA} \rightarrow  A \rightarrow  {A}_{p} \rightarrow  0 \) , so \( \operatorname{Hom}\left( {{pA},\mathbb{Z}}\right)  \rightarrow  \operatorname{Ext}\left( {{A}_{p},\mathbb{Z}}\right)  \rightarrow  \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is exact, hence either \( \operatorname{Hom}\left( {{pA},\mathbb{Z}}\right) \) or \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable. Also, we have an isomorphism \( \operatorname{Hom}\left( {{pA},\mathbb{Z}}\right)  \approx  \operatorname{Hom}\left( {A,\mathbb{Z}}\right) \) since the exact sequence \( 0{ \rightarrow  }_{p}A \rightarrow  A \rightarrow  {pA} \rightarrow  0 \) gives an exact sequence \( 0 \rightarrow  \operatorname{Hom}\left( {{pA},\mathbb{Z}}\right)  \rightarrow  \operatorname{Hom}\left( {A,\mathbb{Z}}\right)  \rightarrow  \operatorname{Hom}\left( {{}_{p}A,\mathbb{Z}}\right) \) whose last term is 0 since \( {}_{p}A \) is a torsion group. Thus we have shown that either \( \operatorname{Hom}\left( {A,\mathbb{Z}}\right) \) or \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable if \( A \) has infinite \( p \) -rank for some \( p \) .

In the remainder of the proof we will show that \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable if \( A \) has finite \( p \) -rank for all \( p \) and \( A \) is not finitely generated.

Let \( C \) be a nontrivial cyclic subgroup of \( A \) , either finite or infinite. If there is no maximal cyclic subgroup of \( A \) containing \( C \) then there is an infinite ascending chain of cyclic subgroups \( C = {C}_{1} \subset  {C}_{2} \subset  \cdots \) . If the indices \( \left\lbrack  {{C}_{i} : {C}_{i - 1}}\right\rbrack \) involve infinitely many distinct prime factors \( p \) then \( A/C \) contains an infinite sum \( {\bigoplus }_{\infty }{\mathbb{Z}}_{p} \) for these \( p \) so \( \operatorname{Ext}\left( {A/C,\mathbb{Z}}\right) \) is uncountable by (a) and (c) and hence also \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) by (b). If only finitely many primes are factors of the indices \( \left\lbrack  {{C}_{i} : {C}_{i - 1}}\right\rbrack \) then \( A/C \) contains a subgroup \( {Z}_{{p}^{\infty }} \) so \( \operatorname{Ext}\left( {A/C,\mathbb{Z}}\right) \) and hence \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is uncountable in this case as well by (a),(b), and (d). Thus we may assume that each nonzero element of \( A \) lies in a maximal cyclic subgroup.

If \( A \) has positive finite \( p \) -rank we can choose a cyclic subgroup mapping nontriv-ially to \( {A}_{p} \) and then a maximal cyclic subgroup \( C \) containing this one will also map nontrivially to \( {A}_{p} \) . The quotient \( A/C \) has smaller \( p \) -rank since \( C \rightarrow  A \rightarrow  A/C \rightarrow  0 \) exact implies \( {C}_{p} \rightarrow  {A}_{p} \rightarrow  {\left( A/C\right) }_{p} \rightarrow  0 \) exact, as tensoring with \( {\mathbb{Z}}_{p} \) preserves exactness to this extent. By (b) and induction on \( p \) -rank this gives a reduction to the case \( {A}_{p} = 0 \) , so \( A = {pA} \) .

If \( A \) is torsionfree, the maximality of the cyclic subgroup \( C \) in the preceding paragraph implies that \( A/C \) is also torsionfree, so by induction on \( p \) -rank we reduce to the case that \( A \) is torsionfree and \( A = {pA} \) . But in this case \( A \) has no maximal cyclic subgroups so this case has already been covered.

If \( A \) has torsion, its torsion subgroup \( T \) is the direct sum of the \( p \) -torsion subgroups \( T\left( p\right) \) for all primes \( p \) . Only finitely many of these \( T\left( p\right) \) ’s can be nonzero, otherwise \( A \) contains finite cyclic subgroups not contained in maximal cyclic subgroups. If some \( T\left( p\right) \) is not finitely generated then by (a) we can assume \( A = T\left( p\right) \) . In this case the reduction from finite \( p \) -rank to \( p \) -rank 0 given above stays within the realm of \( p \) -torsion groups. But if \( A = {pA} \) we again have no maximal cyclic subgroups, so we are done in the case that \( T \) is not finitely generated. Finally, when \( T \) is finitely generated then we can use (b) to reduce to the torsionfree case by passing from \( A \) to \( A/T \) .

## Exercises

1. Given maps \( {f}_{i} : {X}_{i} \rightarrow  {X}_{i + 1} \) for integers \( i < 0 \) , show that the ’reverse mapping telescope’ obtained by glueing together the mapping cylinders of the \( {f}_{i} \) ’s in the obvious way deformation retracts onto \( {X}_{0} \) . Similarly, if maps \( {f}_{i} : {X}_{i} \rightarrow  {X}_{i + 1} \) are given for all \( i \in  \mathbb{Z} \) , show that the resulting ’double mapping telescope’ deformation retracts onto any of the ordinary mapping telescopes contained in it, the union of the mapping cylinders of the \( {f}_{i} \) ’s for \( i \) greater than a given number \( n \) .

2. Show that \( {\underline{\lim }}^{1}{G}_{i} = 0 \) if the sequence \( \cdots  \rightarrow  {G}_{2}\overset{{\alpha }_{2}}{ \rightarrow  }{G}_{1}\overset{{\alpha }_{1}}{ \rightarrow  }{G}_{0} \) satisfies the Mittag-Leffler condition that for each \( i \) the images of the maps \( {G}_{i + n} \rightarrow  {G}_{i} \) are independent of \( n \) for sufficiently large \( n \) .

3. Show that \( \operatorname{Ext}\left( {A,\mathbb{Q}}\right)  = 0 \) for all \( A \) . [Consider the homology with \( \mathbb{Q} \) coefficients of a Moore space \( M\left( {A, n}\right) \) .]

4. An abelian group \( G \) is defined to be divisible if the map \( G\overset{n}{ \rightarrow  }G, g \mapsto  {ng} \) , is surjective for all \( n > 1 \) . Show that a group is divisible iff it is a quotient of a direct sum of \( \mathbb{Q} \) ’s. Deduce from the previous problem that if \( G \) is divisible then \( \operatorname{Ext}\left( {A, G}\right)  = 0 \) for all \( A \) .

5. Show that \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is isomorphic to the cokernel of \( \operatorname{Hom}\left( {A,\mathbb{Q}}\right)  \rightarrow  \operatorname{Hom}\left( {A,\mathbb{Q}/\mathbb{Z}}\right) \) , the map induced by the quotient map \( \mathbb{Q} \rightarrow  \mathbb{Q}/\mathbb{Z} \) . Use this to get another proof that \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},\mathbb{Z}}\right)  \approx  {\widehat{\mathbb{Z}}}_{p} \) for \( p \) prime.

6. Show that \( \operatorname{Ext}\left( {{\mathbb{Z}}_{{p}^{\infty }},{\mathbb{Z}}_{p}}\right)  \approx  {\mathbb{Z}}_{p} \) .

7. Show that for a short exact sequence of abelian groups \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) , a Moore space \( M\left( {C, n}\right) \) can be realized as a quotient \( M\left( {B, n}\right) /M\left( {A, n}\right) \) . Applying the long exact sequence of cohomology for the pair \( \left( {M\left( {B, n}\right) , M\left( {A, n}\right) }\right) \) with any coefficient group \( G \) , deduce an exact sequence

\[
0 \rightarrow  \operatorname{Hom}\left( {C, G}\right)  \rightarrow  \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  \operatorname{Ext}\left( {C, G}\right)  \rightarrow  \operatorname{Ext}\left( {B, G}\right)  \rightarrow  \operatorname{Ext}\left( {A, G}\right)  \rightarrow  0
\]

8. Show that for a Moore space \( M\left( {G, n}\right) \) the Bockstein long exact sequence in cohomology associated to the short exact sequence of coefficient groups \( 0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0 \) reduces to an exact sequence

\[
0 \rightarrow  \operatorname{Hom}\left( {G, A}\right)  \rightarrow  \operatorname{Hom}\left( {G, B}\right)  \rightarrow  \operatorname{Hom}\left( {G, C}\right)  \rightarrow  \operatorname{Ext}\left( {G, A}\right)  \rightarrow  \operatorname{Ext}\left( {G, B}\right)  \rightarrow  \operatorname{Ext}\left( {G, C}\right)  \rightarrow  0
\]

9. For an abelian group \( A \) let \( p : A \rightarrow  A \) be multiplication by \( p \) , and let \( {}_{p}A = \operatorname{Ker}p \) , \( {pA} = \operatorname{Im}p \) , and \( {A}_{p} = \) Coker \( p \) as in the proof of Proposition 3F.12. Show that the six-term exact sequences involving \( \operatorname{Hom}\left( {-,\mathbb{Z}}\right) \) and \( \operatorname{Ext}\left( {-,\mathbb{Z}}\right) \) associated to the short exact sequences \( 0{ \rightarrow  }_{p}A \rightarrow  A \rightarrow  {pA} \rightarrow  0 \) and \( 0 \rightarrow  {pA} \rightarrow  A \rightarrow  {A}_{p} \rightarrow  0 \) can be spliced together to yield the exact sequence across the top of the following diagram

![bo_d7dtv0s91nqc73eq8nv0_329_210_149_1376_230_0.jpg](images/bo_d7dtv0s91nqc73eq8nv0_329_210_149_1376_230_0.jpg)

where the map labeled ’ \( p \) ’ is multiplication by \( p \) . Use this to show:

(a) \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is divisible iff \( A \) is torsionfree.

(b) \( \operatorname{Ext}\left( {A,\mathbb{Z}}\right) \) is torsionfree if \( A \) is divisible, and the converse holds if \( \operatorname{Hom}\left( {A,\mathbb{Z}}\right)  = 0 \) .
