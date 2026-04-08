## CHAPTER III Spectral Sequences and Applications

This chapter begins with the abstract properties of spectral sequences and their relation to the double complexes encountered earlier. Then in Section 15 comes the crucial transition to integer coefficients. Many, but not all, of the constructions for the de Rham theory carry over to the singular theory. We point out the similarities and the differences whenever appropriate. In particular, there is a very brief discussion of the Künneth formula and the universal coefficient theorems in this new setting. Thereafter we apply the spectral sequences to the path fibration of Serre and compute the cohomology of the loop space of a sphere. The short review of homotopy theory that follows includes a digression into Morse theory, where we sketch a proof that compact manifolds are \( {CW} \) complexes. In connection with the computation of \( {\pi }_{3}\left( {S}^{2}\right) \) , we also discuss the Hopf invariant and the linking number and explore the rather subtle aspects of Poincaré duality concerned with the boundary of a submanifold. Returning to the spectral sequences, we compute the cohomology of certain Eilenberg-MacLane spaces. The Eilenberg-MacLane spaces may be pieced together into a twisted product that approximates a given space. They are in this sense the basic building blocks of homotopy theory. As an application, we show that \( {\pi }_{5}\left( {S}^{3}\right)  = {\mathbb{Z}}_{2} \) . We conclude with a very brief introduction to the rational homotopy theory of Dennis Sullivan. A more detailed overview of this chapter may be obtained by reading the introductions to the various sections. One word about the notation: for simplicity we often omit the coefficients from the cohomology groups. This should not cause any confusion, as \( {H}^{ * }\left( X\right) \) always denotes the de Rham cohomology except in Sections 15 through 18, where in the context of the singular theory it stands for the singular cohomology.

## §14 The Spectral Sequence of a Filtered Complex

By considering the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) of differential forms on an open cover, we generalized in Chapter II the key theorems of Chapter I. This double complex is a very degenerate case of an algebraic construction called the spectral sequence, a powerful tool in the computation of homology, cohomology and even homotopy groups. In this chapter we construct the spectral sequence of a filtered complex and apply it to a variety of situations, generalizing and reproving many previous results. Among the various approaches to the construction of a spectral sequence, perhaps the simplest is through exact couples, due to Massey [1].

## Exact Couples

An exact couple is an exact sequence of Abelian groups of the form

![bo_d7b6f8alb0pc73dd9avg_165_724_995_188_184_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_165_724_995_188_184_0.jpg)

where \( i, j \) , and \( k \) are group homomorphisms. Define \( d : B \rightarrow  B \) by \( d = j \circ  k \) . Then \( {d}^{2} = j\left( {kj}\right) k = 0 \) , so the homology group \( H\left( B\right)  = \left( {\ker d}\right) /\left( {\operatorname{im}d}\right) \) is defined. Here \( A \) and \( B \) are assumed to be Abelian so that the quotient \( H\left( B\right) \) is a group.

Out of a given exact couple we can construct a new exact couple, called the derived couple,(14.1)

![bo_d7b6f8alb0pc73dd9avg_165_724_1467_202_183_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_165_724_1467_202_183_0.jpg)

by making the following definitions.

(a) \( {A}^{\prime } = i\left( A\right) ;{B}^{\prime } = H\left( B\right) \) .

(b) \( {i}^{\prime } \) is induced from \( i \) ; to be precise,

\[
{i}^{\prime }\left( {ia}\right)  = i\left( {ia}\right) \text{ . }
\]

(c) If \( {a}^{\prime } = {ia} \) is in \( {A}^{\prime } \) , with \( a \) in \( A \) , then \( {j}^{\prime }{a}^{\prime } = \left\lbrack  {ja}\right\rbrack \) , where [ ] denotes the homology class in \( H\left( B\right) \) . To show that \( {j}^{\prime } \) is well-defined we have to check two things:

(i) \( {ja} \) is a cycle. This follows from \( d\left( {ja}\right)  = j\left( {kj}\right) a = 0 \) .

(ii) The homology class \( \left\lbrack  {ja}\right\rbrack \) is independent of the choice of \( a \) .

Suppose \( {a}^{\prime } = i\bar{a} \) for some other \( \bar{a} \) in \( A \) . Then because \( 0 = i\left( {a - \bar{a}}\right) \) , we have \( a - \bar{a} = {kb} \) for some \( b \) in \( B \) . Thus

\[
{ja} - j\bar{a} = {jkb} = {db},
\]

so

\[
\left\lbrack  {ja}\right\rbrack   = \left\lbrack  {j\bar{a}}\right\rbrack  \text{ . }
\]

(d) \( {k}^{\prime } \) is induced from \( k \) . Let \( \left\lbrack  b\right\rbrack \) be a homology class in \( H\left( B\right) \) . Then \( {jkb} = 0 \) so that \( {kb} = {ia} \) for some \( a \) in \( A \) . Define

\[
{k}^{\prime }\left\lbrack  b\right\rbrack   = {kb} \in  i\left( A\right) .
\]

It is straightforward to check that with these definitions, (14.1) is an exact couple. We will check the exactness at \( {B}^{\prime } \) and leave the other steps to the reader.

(i) \( \operatorname{im}{j}^{\prime } \subset  \ker {k}^{\prime } \) :

\( {k}^{\prime }{j}^{\prime }\left( {a}^{\prime }\right)  = {k}^{\prime }{j}^{\prime }\left( {ia}\right)  = {k}^{\prime }j\left( a\right)  = {kj}\left( a\right)  = 0. \)

(ii) ker \( {k}^{\prime } \subset \) im \( {j}^{\prime } \) :

Since \( {k}^{\prime }\left( b\right)  = k\left( b\right)  = 0 \) , it follows that \( b = j\left( a\right)  = {j}^{\prime }\left( {ia}\right)  \in  \operatorname{im}{j}^{\prime } \) .

## The Spectral Sequence of a Filtered Complex

Let \( K \) be a differential complex with differential operator \( D \) ; i.e., \( K \) is an Abelian group and \( D : K \rightarrow  K \) is a group homomorphism such that \( {D}^{2} = 0 \) . Usually \( K \) comes with a grading \( K = {\bigoplus }_{k \in  Z}{C}^{k} \) and \( D : {C}^{k} \rightarrow  {C}^{k + 1} \) increases the degree by 1, but the grading is not absolutely indispensable. A subcomplex \( {K}^{\prime } \) of \( K \) is a subgroup such that \( D{K}^{\prime } \subset  {K}^{\prime } \) . A sequence of subcomplexes

\[
K = {K}_{0} \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  \cdots
\]

is called a filtration on \( K \) . This makes \( K \) into a filtered complex, with associated graded complex

\[
{GK} = {\bigoplus }_{p = 0}^{\infty }{K}_{p}/{K}_{p + 1}
\]

For notational reasons we usually extend the filtration to negative indices by defining \( {K}_{p} = K \) for \( p < 0 \) .

EXAMPLE 14.2. If \( K =  \oplus  {K}^{p, q} \) is a double complex with horizontal operator \( \delta \) and vertical operator \( d \) , we can form a single complex out of it in the usual way, by letting \( K =  \oplus  {C}^{k} \) , where \( {C}^{k} = { \oplus  }_{p + q = k}{K}^{p, q} \) , and defining the differential operator \( D : {C}^{k} \rightarrow  {C}^{k + 1} \) to be \( D = \dot{\delta } + {\left( -1\right) }^{p}d \) . Then the sequence of subcomplexes indicated below is a filtration on \( K \) :

\[
{K}_{p} = {\bigoplus }_{i \geq  p}{\bigoplus }_{q \geq  0}{K}^{i, q}
\]

![bo_d7b6f8alb0pc73dd9avg_167_484_304_661_615_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_167_484_304_661_615_0.jpg)

Returning to the general filtered complex \( K \) , let \( A \) be the group

\[
A = {\bigoplus }_{p \in  \mathbf{Z}}{K}_{p}
\]

\( A \) is again a differential complex with operator \( D \) . Define \( i : A \rightarrow  A \) to be the inclusion \( {K}_{p + 1} \hookrightarrow  {K}_{p} \) and define \( B \) to be the quotient

(14.3)

\[
0 \rightarrow  A\overset{i}{ \rightarrow  }A\overset{j}{ \rightarrow  }B \rightarrow  0
\]

Then \( B \) is the associated graded complex \( {GK} \) of \( K \) . In the short exact sequence (14.3) each group is a complex with operator induced from \( D \) . In the graded case we get from this short exact sequence a long exact sequence of cohomology groups

\[
\cdots  \rightarrow  {H}^{k}\left( A\right) \overset{{i}_{1}}{ \rightarrow  }{H}^{k}\left( A\right) \overset{{j}_{1}}{ \rightarrow  }{H}^{k}\left( B\right) \overset{{k}_{1}}{ \rightarrow  }{H}^{k + 1}\left( A\right)  \rightarrow  \cdots ,
\]

which we may write as

![bo_d7b6f8alb0pc73dd9avg_167_451_1807_656_219_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_167_451_1807_656_219_0.jpg)

where the map \( i \) need no longer be an inclusion. We suppress the subscript of

\( {i}_{1} \) to avoid cumbersome notation later. It is not difficult to see that the same diagram exists in the ungraded case. Since this diagram is an exact couple, it gives rise as in (14.1) to a sequence of exact couples:

![bo_d7b6f8alb0pc73dd9avg_168_716_459_216_212_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_168_716_459_216_212_0.jpg)

each being the derived couple of its predecessor.

For the sake of the exposition consider now the case where the filtered complex terminates after \( {K}_{3} \) :

\[
\cdots  = {K}_{-1} = {K}_{0} \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  0.
\]

Then \( {A}_{1} \) is the direct sum of all the terms in the following sequence

\[
\cdots  \rightleftarrows  H\left( K\right)  \rightleftarrows  H\left( K\right) \overset{i}{ \leftarrow  }H\left( {K}_{1}\right) \overset{i}{ \leftarrow  }H\left( {K}_{2}\right) \overset{i}{ \leftarrow  }H\left( {K}_{3}\right)  \leftarrow  0.
\]

This is of course not an exact sequence. Next, \( {A}_{2} \) by definition is the image of \( {A}_{1} \) under \( i \) in \( {A}_{1} \) and so is the direct sum of the groups in the sequence

\[
\cdots  \rightleftarrows  H\left( K\right)  \rightleftarrows  H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \leftarrow  {iH}\left( {K}_{2}\right)  \leftarrow  {iH}\left( {K}_{3}\right)  \leftarrow  0.
\]

Note that here the map \( {iH}\left( {K}_{1}\right)  \subset  H\left( K\right) \) is an inclusion. Similarly \( {A}_{3} \) is the sum of

\[
\cdots  \cong  H\left( K\right)  \cong  H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {iiH}\left( {K}_{2}\right)  \leftarrow  {iiH}\left( {K}_{3}\right)  \leftarrow  0
\]

and \( {A}_{4} \) is the sum of

\[
\simeq  H\left( K\right)  \cong  H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {iiH}\left( {K}_{2}\right)  \supset  {iiiH}\left( {K}_{3}\right)  \supset  0.
\]

Since all the maps become inclusions in \( {A}_{4} \) , all the \( A \) ’s are stationary after the fourth derived couple and we define \( {A}_{\infty } \) to be the stationary value:

\[
{A}_{4} = {A}_{5} = {A}_{6} = \cdots  = {A}_{\infty }.
\]

Furthermore, since

![bo_d7b6f8alb0pc73dd9avg_168_716_1874_219_202_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_168_716_1874_219_202_0.jpg)

is exact and \( i : {A}_{4} \rightarrow  {A}_{4} \) is the inclusion, the map \( {k}_{4} : {B}_{4} \rightarrow  {A}_{4} \) must be the zero map. Therefore, after the fourth stage all the differentials of the exact couples are zero and the \( B \) ’s also become stationary,

\[
{B}_{4} = {B}_{5} = {B}_{6} = \cdots  = {B}_{\infty }.
\]

In the exact couple

![bo_d7b6f8alb0pc73dd9avg_169_634_519_315_231_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_169_634_519_315_231_0.jpg)

\( {A}_{\infty } \) is the direct sum of the groups

(14.4)

\[
\cdots  = H\left( K\right)  = H\left( K\right)  \supset  {iH}\left( {K}_{1}\right)  \supset  {iiH}\left( {K}_{2}\right)  \supset  {iiiH}\left( {K}_{3}\right)  \supset  0
\]

and the inclusion \( {i}_{\infty } \) is as in (14.4). Since \( {B}_{\infty } \) is the quotient of \( {i}_{\infty } \) , it is the direct sum of the successive quotients in \( {i}_{\infty } \) . If we let (14.4) be the filtration on \( H\left( K\right) \) , then \( {B}_{\infty } \) is the associated graded complex of the filtered complex \( H\left( K\right) \) .

We now return to the general case. The sequence of subcomplexes

\[
\cdots  = K = K \supset  {K}_{1} \supset  {K}_{2} \supset  {K}_{3} \supset  \cdots
\]

induces a sequence in cohomology

\[
\cdots  \rightleftarrows  H\left( K\right)  \subset  H\left( K\right) \overset{i}{ \leftarrow  }H\left( {K}_{1}\right) \overset{i}{ \leftarrow  }H\left( {K}_{2}\right) \overset{i}{ \leftarrow  }H\left( {K}_{3}\right)  \leftarrow  \cdots ,
\]

where the maps \( i \) are of course no longer inclusions. Let \( {F}_{p} \) be the image of \( H\left( {K}_{p}\right) \) in \( H\left( K\right) \) . Then there is a sequence of inclusions

(14.5)

\[
H\left( K\right)  = {F}_{0} \supset  {F}_{1} \supset  {F}_{2} \supset  {F}_{3} \supset  \cdots ,
\]

making \( H\left( K\right) \) into a filtered complex; this filtration is called the induced filtration on \( H\left( K\right) \) .

A filtration \( {K}_{p} \) on the filtered complex \( K \) is said to have length \( \ell \) if \( {K}_{\ell } \neq  0 \) and \( {K}_{p} = 0 \) for \( p > \ell \) . By the same argument as the special case above, we see that whenever the filtration on \( K \) has finite length, then \( {A}_{r} \) and \( {B}_{r} \) are eventually stationary and the stationary value \( {B}_{\infty } \) is the associated graded complex \( \oplus  {F}_{p}/{F}_{p + 1} \) of the filtered complex \( H\left( K\right) \) with filtration given by (14.5).

It is customary to write \( {E}_{r} \) for \( {B}_{r} \) . Hence,

\[
{E}_{1} = H\left( B\right) \text{ with differential }{d}_{1} = {j}_{1} \circ  {k}_{1},
\]

\[
{E}_{2} = H\left( {E}_{1}\right) \text{ with differential }{d}_{2} = {j}_{2} \circ  {k}_{2},
\]

\[
{E}_{3} = H\left( {E}_{2}\right) \text{ , etc. }
\]

A sequence of differential groups \( \left\{  {{E}_{r},{d}_{r}}\right\} \) in which each \( {E}_{r} \) is the homology of its predecessor \( {E}_{r - 1} \) is called a spectral sequence. If \( {E}_{r} \) eventually becomes stationary, we denote the stationary value by \( {E}_{\infty } \) , and if \( {E}_{\infty } \) is equal to the associated graded group of some filtered group \( H \) , then we say that the spectral sequence converges to \( H \) .

Now suppose the filtered complex \( K \) comes with a grading: \( K = \; {\bigoplus }_{n \in  \mathbf{Z}}{K}^{n} \) . To distinguish the grading degree \( n \) from the filtration degree \( p \) , we will often call \( n \) the dimension. The filtration \( \left\{  {K}_{p}\right\} \) on \( K \) induces a filtration in each dimension: if \( {K}_{p}^{n} = {K}^{n} \cap  {K}_{p} \) , then \( \left\{  {K}_{p}^{n}\right\} \) is a filtration on \( {K}^{n} \) .

For the applications we have in mind, the filtration on \( K \) need not have finite length. However, we can prove the following.

Theorem 14.6. Let \( K = {\bigoplus }_{n \in  \mathbb{Z}}{K}^{n} \) be a graded filtered complex with filtration \( \left\{  {K}_{p}\right\} \) and let \( {H}_{D}^{ * }\left( K\right) \) be the cohomology of \( K \) with filtration given by (14.5). Suppose for each dimension \( n \) the filtration \( \left\{  {K}_{p}^{n}\right\} \) has finite length. Then the short exact sequence

\[
0 \rightarrow   \oplus  {K}_{p + 1} \rightarrow   \oplus  {K}_{p} \rightarrow   \oplus  {K}_{p}/{K}_{p + 1} \rightarrow  0
\]

induces a spectral sequence which converges to \( {H}_{D}^{ * }\left( K\right) \) .

Proof. By treating the convergence question one dimension at a time, this proof reduces to the ungraded situation. To be absolutely sure, we will write out the details. As before,

\[
{A}_{r} = {\bigoplus }_{p \in  \mathbb{Z}}{i}^{r - 1}H\left( {K}_{p}\right)
\]

if \( r \geq  p + 1 \) , then \( {i}^{r}H\left( {K}_{p}\right)  = {F}_{p} \) and

\[
i : {i}^{\mathrm{r}}H\left( {K}_{p + 1}\right)  \rightarrow  {i}^{r}H\left( {K}_{p}\right)
\]

is an inclusion. With a grading on each derived couple, \( i \) and \( j \) preserve the dimension, but \( k \) increases the dimension by 1 . Given \( n \) , let \( \ell \left( n\right) \) be the length of \( {\left\{  {K}_{p}^{n}\right\}  }_{p \in  Z} \) and let \( r \geq  \ell \left( {n + 1}\right)  + 1 \) . Then for any integer \( p \) ,

\[
{i}^{r}{H}^{n + 1}\left( {K}_{p + 1}\right)  = {F}_{p + 1}^{n + 1}
\]

and

\[
i : {i}^{r}{H}^{n + 1}\left( {K}_{p + 1}\right)  \rightarrow  {i}^{r}{H}^{n + 1}\left( {K}_{p}\right)
\]

is an inclusion. It follows that

\[
{i}_{r} : {A}_{r}^{n + 1} \rightarrow  {A}_{r}^{n + 1}
\]

is an inclusion and

\[
{k}_{r} : {B}_{r}^{n} \rightarrow  {A}_{r}^{n + 1}
\]

is the zero map. Therefore, as \( r \rightarrow  \infty \) , the group \( {B}_{r}^{n} \) becomes stationary and we can define \( {B}_{\infty }^{n} \) to be this stationary value. Note that

\[
{A}_{\infty }^{n} =  \oplus  {F}_{p}^{n}
\]

and that \( {i}_{\infty } \) sends \( {F}_{p + 1}^{n} \) into \( {F}_{p}^{n} \) for every \( n \) . Because \( {i}_{\infty } :  \oplus  {F}_{p + 1} \rightarrow   \oplus  {F}_{p} \) is an inclusion, \( {B}_{\infty } \) is the associated graded complex \( \oplus  {F}_{p}/{F}_{p + 1} \) of \( {H}_{D}^{ * }\left( K\right) \) .

## The Spectral Sequence of a Double Complex

Now let \( K = \bigoplus {K}^{p, q} \) be a double complex with the filtration of Example 14.2. We will obtain a refinement of Theorem 14.6 for this special case by taking into account not only the particular filtration in question but also the bigrading and the presence of the two differential operators \( \delta \) and \( d \) . The direct sum \( A =  \oplus  {K}_{p} \) is also a double complex. Here, as always, we form a single complex \( A =  \oplus  {A}^{k} \) out of this double complex by summing the bidegrees: \( {A}^{k} \) consists of all elements in \( A \) whose total degree is \( k \) . There is an inclusion \( i : {A}^{k} \rightarrow  {A}^{k} \) given by

\[
i : {A}^{k} \cap  {K}_{p + 1} \rightarrow  {A}^{k} \cap  {K}_{p}.
\]

The single complex \( A \) inherits the differential operator \( D = \delta  + {\left( -1\right) }^{p}d \) from \( K \) .

Similarly, \( B =  \oplus  {K}_{p}/{K}_{p + 1} \) can be made into a single complex with operator \( D \) . Note that the differential operator \( D \) on \( B \) is \( {\left( -1\right) }^{p}d \) ; therefore,

(14.7)

\[
{E}_{1} = {H}_{D}\left( B\right)  = {H}_{d}\left( K\right) .
\]

Recall that the coboundary operator \( {k}_{1} : H\left( B\right)  \rightarrow  H\left( A\right) \) is the coboundary operator of the short exact sequence (14.3) and hence is defined by the following diagram:

\[
\underset{0 \rightarrow  {A}^{k + 1} \cap  {K}_{p + 1}\overset{\left( 3\right) }{ \rightarrow  }{A}^{k + 1} \cap  {K}_{p} \rightarrow  {B}^{k + 1} \cap  {K}_{p}/{K}_{p + 1} \rightarrow  0}{ \rightarrow  }
\]

(14.8)

\[
\uparrow  D\;\left( 2\right)  \uparrow  \; \uparrow  D
\]

\[
0 \rightarrow  {A}^{k} \cap  {K}_{p + 1} \rightarrow  {A}^{k} \cap  {K}_{p}\underset{\left( 1\right) }{ \rightarrow  }{B}^{k} \cap  {K}_{p}/{K}_{p + 1} \rightarrow  0
\]

\[
\uparrow  \; \uparrow
\]

Let \( b \) in \( {A}^{k} \cap  {K}_{p} \) represent a cocycle \( \left\lbrack  b\right\rbrack \) in \( {B}^{k} \cap  {K}_{p}/{K}_{p + 1} \) . This corresponds to Step (1) in the diagram. To get \( {k}_{1}\left( \left\lbrack  b\right\rbrack  \right) \) , we

(2) compute \( {Db} \) and

(3) take its inverse under \( i \) .

Since \( b \) represents an element of \( {E}_{1} = {H}_{D}\left( B\right)  = {H}_{d}\left( K\right) ,{db} = 0 \) and \( {Db} = {\delta b} + {\left( -1\right) }^{p}{db} = {\delta b} \) . Thus \( {k}_{1}\left\lbrack  b\right\rbrack   = \left\lbrack  {\delta b}\right\rbrack \) ; so the differential \( {d}_{1} = {j}_{1}{k}_{1} \) on \( {E}_{1} \) is given by \( \delta \) (in fact by \( D \) , but \( D = \delta \) on \( {E}_{1} \) ). Consequently

(14.9)

\[
{E}_{2} = {H}_{\delta }{H}_{d}\left( K\right)
\]

We now compute the differential \( {d}_{2} \) on \( {E}_{2} \) . As noted in the proof of Proposition 12.1, an element of \( {E}_{2} = {H}_{\delta }{H}_{d}\left( K\right) \) is represented by an element \( b \) in \( K \) such that

\[
{db} = 0
\]

![bo_d7b6f8alb0pc73dd9avg_172_798_580_509_368_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_172_798_580_509_368_0.jpg)

\( {\delta b} =  - {D}^{\prime \prime }c \) for some \( c \) in \( K \) ,

where \( {D}^{\prime \prime } = {\left( -1\right) }^{p}d \) . We will denote the class of \( b \) in \( {E}_{r} \) , if it is defined, by \( {\left\lbrack  b\right\rbrack  }_{r} \) . From the definition of the derived couple (14.1),

\[
{d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {j}_{2}{k}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {j}_{2}{k}_{1}{\left\lbrack  b\right\rbrack  }_{1}.
\]

To compute \( {j}_{2}{k}_{1}{\left\lbrack  b\right\rbrack  }_{1} \) , we must find an \( a \) such that \( {k}_{1}{\left\lbrack  b\right\rbrack  }_{1} = i{\left\lbrack  a\right\rbrack  }_{1} \) . Then \( {j}_{2}{k}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {\left\lbrack  {j}_{1}a\right\rbrack  }_{2} \) . Since \( {k}_{1}b \) is in \( {A}^{k + 1} \cap  {K}_{p + 1}, a \) is in \( {A}^{k + 1} \cap  {K}_{p + 2} \) . To find \( a \) we use not \( b \) but \( b + c \) in \( {A}^{k} \cap  {K}_{p} \) to represent \( {\left\lbrack  b\right\rbrack  }_{2} \) in Step (1); this is possible since \( b \) and \( b + c \) have the same image under the projection \( {K}_{p} \rightarrow  {K}_{p}/{K}_{p + 1} \) . Then

\[
{k}_{1}\left( {b + c}\right)  = D\left( {b + c}\right)  = {\delta c}.
\]

So

(14.10)

\[
{d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {\left\lbrack  \delta c\right\rbrack  }_{2}.
\]

Thus the differential \( {d}_{2} \) is given by the \( \delta \) of the tail of the zig-zag which extends \( b \) . It is easy to show that \( {\delta c} \) represents an element of \( {H}_{\delta }{H}_{d}\left( K\right) \) and that the definition of \( {d}_{2}{\left\lbrack  b\right\rbrack  }_{2} \) is independent of the choice of \( c \) .

![bo_d7b6f8alb0pc73dd9avg_172_575_1699_519_440_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_172_575_1699_519_440_0.jpg)

Exercise 14.11. Show that if \( {d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = 0 \) , then there exist \( {c}_{1} \) and \( {c}_{2} \) so that \( b \) can be extended to a zig-zag as shown:

\[
{D}^{\prime \prime }b = 0
\]

\[
{\delta b} =  - {D}^{\prime \prime }{c}_{1}
\]

\[
\delta {c}_{1} =  - {D}^{\prime \prime }{c}_{2}.
\]

![bo_d7b6f8alb0pc73dd9avg_173_653_442_661_530_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_173_653_442_661_530_0.jpg)

We say that an element \( b \) in \( K \) lives to \( {E}_{r} \) if it represents a cohomology class in \( {E}_{r} \) ; equivalently, \( b \) is a cocycle in \( {E}_{1},{E}_{2},\ldots ,{E}_{r - 1} \) . From the discussion above we see that \( b \) lives to \( {E}_{2} \) if it can be extended to a zig-zag of length 2 , the length of a zig-zag being the number of terms in it,

\[
{db} = 0
\]

\[
{\delta b} =  - {D}^{\prime \prime }c
\]

![bo_d7b6f8alb0pc73dd9avg_173_785_1250_424_282_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_173_785_1250_424_282_0.jpg)

and \( {d}_{2}{\left\lbrack  b\right\rbrack  }_{2} = {\left\lbrack  \delta c\right\rbrack  }_{2} \) ; it lives to \( {E}_{3} \) if it can be extended to a zig-zag of length 3:

\[
{db} = 0
\]

\[
{\delta b} =  - {D}^{\prime \prime }{c}_{1}
\]

\[
\delta {c}_{1} =  - {D}^{\prime \prime }{c}_{2}
\]

![bo_d7b6f8alb0pc73dd9avg_173_811_1745_435_393_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_173_811_1745_435_393_0.jpg)

To compute \( {d}_{3}{\left\lbrack  b\right\rbrack  }_{3} \) , we use \( b + {c}_{1} + {c}_{2} \) in \( {A}^{k} \cap  {K}_{p} \) to represent \( \left\lbrack  b\right\rbrack   \in \; {B}^{k} \cap  \left( {{K}_{p}/{K}_{p + 1}}\right) \) in Step (1) of (14.8), so that \( {k}_{3}{\left\lbrack  b\right\rbrack  }_{3} \) is given by \( D(b + \; \left. {{c}_{1} + {c}_{2}}\right)  = \dot{\delta }{c}_{2} \) and \( {d}_{3}{\left\lbrack  b\right\rbrack  }_{3} = {\left\lbrack  \delta {c}_{2}\right\rbrack  }_{3} \) . In general, parallel to the discussion above, an element \( b \) in \( {K}^{p, q} \) lives to \( {E}_{r} \) if it can be extended to a zig-zag of length \( r \) : and the differential \( {d}_{r} \) on \( {E}_{r} \) is given by \( \delta \) of the tail of the zig-zag:

(14.12)

\[
{d}_{r}{\left\lbrack  b\right\rbrack  }_{r} = {\left\lbrack  \delta {c}_{r - 1}\right\rbrack  }_{r}.
\]

![bo_d7b6f8alb0pc73dd9avg_174_359_544_923_601_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_174_359_544_923_601_0.jpg)

Thus the bidegrees \( \left( {p, q}\right) \) of the double complex \( K =  \oplus  {K}^{p, q} \) persist in the spectral sequence

\[
{E}_{r} = {\bigoplus }_{p, q}{E}_{r}^{p, q}
\]

and \( {d}_{r} \) shifts the bidegrees by \( \left( {r, - r + 1}\right) \) :

\[
{d}_{r} : {E}_{r}^{p, q} \rightarrow  {E}_{r}^{p + r, q - r + 1}
\]

The filtration on \( H\left( K\right)  = \bigoplus {H}^{n}\left( K\right) \) :

\[
H\left( K\right)  = {F}_{0} \supset  {F}_{1} \supset  {F}_{2} \supset  \cdots
\]

induces a filtration on each component \( {H}^{n}\left( K\right) \) , the successive quotients of the filtration being \( {E}_{\infty }^{0, n},{E}_{\infty }^{1, n - 1},\ldots ,{E}_{\infty }^{n,0} \) :

(14.13)

\[
= \left( {{F}_{0} \cap  \underset{{E}_{\infty }^{0, n}}{\underbrace{{H}^{n}}}}\right)  \cap  \underset{{E}_{\infty }^{0, n - 1}}{\underbrace{{H}^{n}) \supset  \left( {{F}_{2} \cap  {H}^{n}}\right)  \supset  \ldots  \supset  \left( {{F}_{n} \cap  {H}^{n}}\right)  \supset  0}}
\]

This is best seen pictorially

![bo_d7b6f8alb0pc73dd9avg_175_328_294_974_559_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_175_328_294_974_559_0.jpg)

In summary, we have proved the following refinement of Theorem 14.6.

Theorem 14.14. Given a double complex \( K = {\bigoplus }_{p, q \geq  0}{K}^{p, q} \) there is a spectral sequence \( \left\{  {{E}_{r},{d}_{r}}\right\} \) converging to the total cohomology \( {H}_{D}\left( K\right) \) such that each \( {E}_{r} \) has a bigrading with

\[
{d}_{r} : {E}_{r}^{p, q} \rightarrow  {E}_{r}^{p + r, q - r + 1}
\]

and

\[
{E}_{1}^{p, q} = {H}_{d}^{p, q}\left( K\right) ,
\]

\[
{E}_{2}^{p, q} = {H}_{\delta }^{p, q}{H}_{d}\left( K\right)
\]

furthermore, the associated graded complex of the total cohomology is given by

\[
G{H}_{D}^{n}\left( K\right)  = {\bigoplus }_{p + q = n}{E}_{\infty }^{p, q}\left( K\right)
\]

REMARK 14.15. Of course, instead of the filtration in Example 14.2, we could just as well have given \( K \) the following filtration.

![bo_d7b6f8alb0pc73dd9avg_175_365_1559_903_614_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_175_365_1559_903_614_0.jpg)

This gives a second spectral sequence \( \left\{  {{E}_{r}^{\prime },{d}_{r}^{\prime }}\right\} \) converging to the total cohomology \( {H}_{D}\left( K\right) \) , but with

\[
{E}_{1}^{\prime } = {H}_{\delta }\left( K\right)
\]

\[
{E}_{2}^{\prime } = {H}_{d}{H}_{\delta }\left( K\right)
\]

and

\[
{d}_{r}^{\prime } : {E}_{r}^{\prime p, q} \rightarrow  {E}_{r}^{\prime p - r + 1, q + r}
\]

EXAMPLE 14.16 (The Mayer-Vietoris principle and the isomorphism between de Rham and Čech). Let \( M \) be a manifold and \( \mathfrak{U} \) a good cover on \( M \) . Consider the double complex \( K = \bigoplus {K}^{p, q} \) ,

\[
{K}^{p, q} = {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)
\]

Since the rows of \( K \) are the Mayer-Vietoris sequences, the \( {E}_{1} \) term of the second spectral sequence is

![bo_d7b6f8alb0pc73dd9avg_176_429_1004_786_432_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_176_429_1004_786_432_0.jpg)

Therefore the \( {E}_{2} \) term is

\[
{E}_{2} = {H}_{d}{H}_{\delta } = {\left\lbrack  \begin{matrix} {H}_{DR}^{3}\left( M\right) & & & \\   & {H}_{DR}^{2}\left( M\right) & 0 & \\   & 0 & & \\  {H}_{DR}^{1}\left( M\right) & & 0 & \\   & {H}_{DR}^{2}\left( M\right) & 0 &  \end{matrix}\right\rbrack  }_{D = 1}
\]

In general a spectral sequence is said to degenerate at the \( {E}_{r} \) term if \( {d}_{r} = \; {d}_{r + 1} = \cdots  = 0 \) . For such a spectral sequence \( {E}_{r} = {E}_{r + 1} = \cdots  = {E}_{\infty } \) . The degeneration of the second spectral sequence of the double complex

\( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) at the \( {E}_{2} \) term proves once again the Mayer-Vietoris principle (Proposition 8.8):

(14.16.1)

\[
{H}_{DR}^{k}\left( M\right)  = {\bigoplus }_{p + q = k}{H}_{D}^{p, q}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

Now consider the first spectral sequence of \( {C}^{ * }\left( {U,{\Omega }^{ * }}\right) \) . Its \( {E}_{1} \) term is

\[
{E}_{1}^{p, q} = \mathop{\prod }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{H}^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  = \left\{  \begin{array}{ll} 0 & \text{ if }q > 0 \\  {C}^{p}\left( {\mathfrak{U},\mathbb{R}}\right) & \text{ if }q = 0. \end{array}\right.
\]

![bo_d7b6f8alb0pc73dd9avg_177_472_690_689_321_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_177_472_690_689_321_0.jpg)

So the \( {E}_{2} \) term is

![bo_d7b6f8alb0pc73dd9avg_177_447_1129_735_303_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_177_447_1129_735_303_0.jpg)

The degeneration of this spectral sequence gives

\[
{H}^{k}\left( {\mathfrak{U},\mathbb{R}}\right)  = {\bigoplus }_{p + q = k}{E}_{2}^{p, q} = {\bigoplus }_{p + q = k}{E}_{\infty }^{p, q} = {H}_{D}^{k}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

Together with (14.16.1) we get

\[
{H}_{DR}^{k}\left( M\right)  = {H}^{k}\left( {\mathfrak{U},\mathbb{R}}\right) \;\text{ for all integers }k \geq  0.
\]

This is the spectral sequence proof of the isomorphism between de Rham and Čech (Theorem 8.9).

REMARK 14.17. The extension problem. Because the dimension is the only invariant of a vector space, the associated graded vector space \( {GV} \) of a filtered vector space \( V \) is isomorphic to \( V \) itself. In particular, if the double complex \( K \) is a vector space, then

\[
{H}_{D}^{n}\left( K\right)  \simeq  G{H}_{D}^{n}\left( K\right)  \simeq  {\bigoplus }_{p + q = n}{E}_{\infty }^{p, q}
\]

However, in the realm of Abelian groups a knowledge of the associated graded group does not determine the group itself. For example, the two groups \( {\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2} \) and \( {\mathbb{Z}}_{4} \) filtered by

\[
{\mathbb{Z}}_{2} \subset  {\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2}
\]

and

\[
{\mathbb{Z}}_{2} \subset  {\mathbb{Z}}_{4}
\]

have isomorphic associated graded groups, but \( {\mathbb{Z}}_{2} \oplus  {\mathbb{Z}}_{2} \) is not isomorphic to \( {\mathbb{Z}}_{4} \) . Put another way, in a short exact sequence of Abelian groups

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0,
\]

\( A \) and \( C \) do not determine \( B \) uniquely. The ambiguity is called the extension problem and lies at the heart of the subject known as homological algebra. For our purpose it suffices to be familiar with the following elementary facts from extension theory.

Proposition 14.17.1. In a short exact sequence of Abelian groups

\[
0 \rightarrow  A\overset{f}{ \rightarrow  }B\overset{g}{ \rightarrow  }C \rightarrow  0
\]

if \( C \) is free, then there exists a homomorphism \( s : C \rightarrow  B \) such that \( g \circ  s \) is the identity on \( C \) .

Proof. Define \( s \) appropriately on the generators of \( C \) and extend linearly. \( \lbrack \)

Corollary 14.17.2. Under the hypothesis of the proposition,

(a) the map \( \left( {f, s}\right)  : A \oplus  C \rightarrow  B \) is an isomorphism;

(b) for any Abelian group \( G \) the induced sequence

\[
0 \rightarrow  \operatorname{Hom}\left( {C, G}\right)  \rightarrow  \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right)  \rightarrow  0
\]

is exact;

(c) for any Abelian group \( G \) the sequence

\[
0 \rightarrow  A \otimes  G \rightarrow  B \otimes  G \rightarrow  C \otimes  G \rightarrow  0
\]

is exact.

The proof is left to the reader.

Exercise 14.17.3. Show that if

\[
0 \rightarrow  {A}_{1} \rightarrow  {A}_{2} \rightarrow  {A}_{3} \rightarrow  \cdots
\]

is an exact sequence of free Abelian groups and if \( G \) is any Abelian group, then the two sequences

\[
0 \leftarrow  \operatorname{Hom}\left( {{A}_{1}, G}\right)  \leftarrow  \operatorname{Hom}\left( {{A}_{2}, G}\right)  \leftarrow  \operatorname{Hom}\left( {{A}_{3}, G}\right)  \leftarrow  \cdots
\]

and

\[
0 \rightarrow  {A}_{1} \otimes  G \rightarrow  {A}_{2} \otimes  G \rightarrow  {A}_{3} \otimes  G \rightarrow  \cdots
\]

are both exact.

Exercise 14.17.4. Show that if

\[
0 \rightarrow  A \rightarrow  B \rightarrow  C \rightarrow  0
\]

is a short exact sequence of Abelian groups (which are not necessarily free) and \( G \) is any Abelian group, then the two sequences

\[
0 \rightarrow  \operatorname{Hom}\left( {C, G}\right)  \rightarrow  \operatorname{Hom}\left( {B, G}\right)  \rightarrow  \operatorname{Hom}\left( {A, G}\right)
\]

and

\[
A \otimes  G \rightarrow  B \otimes  G \rightarrow  C \otimes  G \rightarrow  0
\]

are both exact.

## The Spectral Sequence of a Fiber Bundle

Let \( \pi  : E \rightarrow  M \) be a fiber bundle with fiber \( F \) over a manifold \( M \) . Applying Theorem 14.14 here gives a general method for computing the cohomology of \( E \) from that of \( F \) and \( M \) . Indeed, given a good cover \( \mathfrak{U} \) of \( M,{\pi }^{-1}\mathfrak{U} \) is a cover on \( E \) and we can form the double complex

\[
{K}^{p, q} = {C}^{p}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{q}}\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \ldots  < {\alpha }_{p}}}{\Omega }^{q}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right) ,
\]

whose \( {E}_{1} \) term is

\[
{E}_{1}^{p, q} = {H}_{d}^{p, q} = \mathop{\prod }\limits_{{{\alpha }_{0} < \ldots  < {\alpha }_{p}}}{H}^{q}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)  = {C}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}}\right) ,
\]

where \( {\mathcal{H}}^{q} \) is the presheaf \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}U}\right) \) on \( M \) . For emphasis we sometimes write the presheaf \( {\mathcal{H}}^{q} \) as \( {\mathcal{H}}^{q}\left( F\right) \) . Since \( \mathfrak{U} \) is a good cover, \( {\mathcal{H}}^{q} \) is a locally constant presheaf on \( \mathfrak{U} \) with group \( {H}^{q}\left( F\right) \) (pp. 142-143). Since \( {d}_{1} = \delta \) on \( {E}_{1} \) , the \( {E}_{2} \) term is

\[
{E}_{2}^{p, q} = {H}_{\delta }^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}}\right) .
\]

By Theorem 14.14 the spectral sequence of \( K \) converges to \( {H}_{D}^{ * }\left( K\right) \) , which by the generalized Mayer-Vietoris principle (Proposition 8.8) is equal to \( {H}^{ * }\left( E\right) \) , because \( {\pi }^{-1}\mathfrak{U} \) is a cover on \( E \) .

In case the base \( M \) is simply connected and \( {H}^{q}\left( F\right) \) is finite-dimensional, Theorems 13.2 and 13.4 imply that \( {\mathcal{H}}^{q} \) is the constant presheaf \( \mathbb{R} \oplus  \cdots \; \oplus  \mathbb{R} \) on \( \mathfrak{U} \) , consisting of \( {h}^{q}\left( F\right) \) copies of \( \mathbb{R} \) where \( {h}^{q}\left( F\right)  = \dim {H}^{q}\left( F\right) \) . So the

\( {E}_{2}^{p, q} \) term is isomorphic as a vector space to the tensor product \( {H}^{p}\left( M\right)  \otimes \; {H}^{q}\left( F\right) \) , since

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},\mathbb{R} \oplus  \cdots  \oplus  \mathbb{R}}\right)  = {H}^{p}\left( {\mathfrak{U},\mathbb{R}}\right)  \otimes  {H}^{q}\left( F\right)
\]

\[
= {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) ,
\]

where the last equality follows from Theorem 8.9.

We have proven the following.

Theorem 14.18 (Leray's Theorem for de Rham Cohomology). Given a fiber bundle \( \pi  : E \rightarrow  M \) with fiber \( F \) over a manifold \( M \) and a good cover \( \mathfrak{U} \) of \( M \) , there is a spectral sequence \( \left\{  {E}_{r}\right\} \) converging to the cohomology of the total space \( {H}^{ * }\left( E\right) \) with \( {E}_{2} \) term

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}}\right) ,
\]

where \( {\mathcal{H}}^{q} \) is the locally constant presheaf \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}U}\right) \) on \( \mathfrak{U} \) . If \( M \) is simply connected and \( {H}^{q}\left( F\right) \) is finite-dimensional, then

\[
{E}_{2}^{p, q} = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) .
\]

## Some Applications

EXAMPLE 14.19 (The Künneth formula and the Leray-Hirsch theorem). We now give a spectral sequence proof of the Künneth formula (5.9). Let \( M \) and \( F \) be two manifolds and \( \mathfrak{U} \) a good cover of \( M \) . Suppose \( F \) has finite-dimensional cohomology. By Leray's theorem (14.18), the spectral sequence of the trivial bundle

![bo_d7b6f8alb0pc73dd9avg_180_720_1480_205_135_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_180_720_1480_205_135_0.jpg)

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}\left( F\right) }\right) .
\]

has \( {E}_{2} \) term

Because \( M \times  F \) is a trivial bundle over \( M \) , the presheaf \( {\mathcal{H}}^{q}\left( F\right) \) is constant, so that

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},\mathbb{R}}\right)  \otimes  {H}^{q}\left( F\right)  = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( F\right) .
\]

By (14.12) the differential \( {d}_{r} \) measures the extent to which an element of \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) that lives to \( {E}_{r} \) fails to be extended one step further to a \( D \) -cocycle. Since every element of the \( {E}_{2} \) term is already a global form on

\( M \times  F,{d}_{2} = {d}_{3} = \cdots  = 0 \) . So \( {E}_{2} = {E}_{\infty } \) , which by Theorem 14.18 is \( {H}^{ * }\left( {M \times  F}\right) \) . Therefore we have the Künneth formula

\[
{H}^{ * }\left( {M \times  F}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) .
\]

The proof of the Leray-Hirsch theorem is analogous.

REMARK 14.20 (Orientability and the Euler class of a sphere bundle). Let \( \pi  : E \rightarrow  M \) be an \( {S}^{n} \) -bundle over a manifold \( M \) and let \( \mathfrak{U} \) be a good cover of \( M \) . The spectral sequence of this fiber bundle has

\( {E}_{1}^{p, q} = {H}_{d}^{p, q} = {C}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}\left( {S}^{n}\right) }\right)  = \)

![bo_d7b6f8alb0pc73dd9avg_181_747_696_497_386_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_181_747_696_497_386_0.jpg)

Let \( \sigma \) be the element of \( {E}_{1}^{0, n} = {C}^{0}\left( {\mathfrak{U},{\mathcal{H}}^{n}\left( {S}^{n}\right) }\right) \) corresponding to the local angular forms on the sphere bundle \( E \) . From the description of the differential \( {d}_{r} \) as the \( \delta \) of the tail of a zig-zag, we see that \( E \) is orientable if and only if \( {d}_{1}\sigma  = 0 \) (compare with pp. 116-118). For an orientable \( {S}^{n} \) -bundle then, such a \( \sigma \) lives to \( {E}_{n} \) :

![bo_d7b6f8alb0pc73dd9avg_181_270_1354_1056_463_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_181_270_1354_1056_463_0.jpg)

Up to a sign \( {d}_{n}\sigma \) in \( {H}^{n + 1}\left( {\mathfrak{U},{\mathcal{H}}^{0}\left( {S}^{n}\right) }\right)  = {H}^{n + 1}\left( M\right) \) is the Euler class of the sphere bundle. It measures the extent to which \( \sigma \) fails to be extended to a \( D \) -cocycle, i.e., a global closed \( n \) -form on the sphere bundle.

EXAMPLE 14.21 (Orientability of a simply connected manifold). Let \( M \) be a simply connected manifold of dimension \( n \) and \( S\left( {T}_{M}\right) \) its unit tangent bundle. The spectral sequence of the fiber bundle

\[
{S}^{n - 1} \rightarrow  S\left( {T}_{M}\right)
\]

↓

\( M \)

has \( {E}_{2} \) term

![bo_d7b6f8alb0pc73dd9avg_182_553_562_545_171_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_182_553_562_545_171_0.jpg)

This shows that there is an element in \( {C}^{0}\left( {{\pi }^{-1}\mathfrak{U},{\mathcal{H}}^{n - 1}}\right) \) which can be extended one step down toward being a \( D \) -cocycle. Therefore \( S\left( {T}_{M}\right) \) and also \( M \) are orientable. This gives an alternative proof of the orientability of a simply connected manifold (Corollary 11.6).

EXAMPLE 14.22 (The cohomology of the complex projective space). Consider the sphere

\[
{S}^{{2n} + 1} = \left\{  {\left( {{z}_{0},\ldots ,{z}_{n}}\right) \left| \right| {z}_{0}\left| {{}^{2} + \cdots  + }\right| {z}_{n}{|}^{2} = 1}\right\}
\]

in \( {\mathbb{C}}^{n + 1} \) . Let \( {S}^{1} \) act on \( {S}^{{2n} + 1} \) by

\[
\left( {{z}_{0},\ldots ,{z}_{n}}\right)  \mapsto  \left( {\lambda {z}_{0},\ldots ,\lambda {z}_{n}}\right)
\]

where \( \lambda \) in \( {S}^{1} \) is a complex number of absolute value 1 . The quotient of \( {S}^{{2n} + 1} \) by this action is the complex projective space \( \mathbb{C}{P}^{n} \) . This gives \( {S}^{{2n} + 1} \) the structure of a circle bundle over \( \mathbb{C}{P}^{n} \)

\( {S}^{1} \rightarrow  {S}^{{2n} + 1} \)

↓

\( \mathbb{C}{P}^{n} \) .

As we will see from the homotopy exact sequence (17.4) to be discussed later, \( \mathbb{C}{P}^{n} \) is simply connected. Thus

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathbb{C}{P}^{n}}\right)  \otimes  {H}^{q}\left( {S}^{1}\right) .
\]

So \( {E}_{2} \) has only two nonzero rows, \( q = 0,1 \) , and the two rows are identical, both being \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) .

Let \( n = 2 \) . Then where the bottom row is the cohomology of the base, \( {H}^{ * }\left( {\mathbb{C}{P}^{2}}\right) \) , and the 0-th column is the cohomology of the fiber. \( {H}^{p}\left( {\mathbb{C}{P}^{2}}\right)  = 0 \) for \( p \geq  5 \) because \( \mathbb{C}{P}^{2} \) has dimension 4. Since \( {d}_{3} \) moves down two steps, \( {d}_{3} = 0 \) . Similarly,

\[
{d}_{4} = {d}_{5} = \cdots  = 0.
\]

![bo_d7b6f8alb0pc73dd9avg_182_580_1857_582_278_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_182_580_1857_582_278_0.jpg)

So the spectral sequence degenerates at the \( {E}_{3} \) term and \( {E}_{3} = {E}_{4} = \cdots  = \; {E}_{\infty } = {H}^{ * }\left( {S}^{5}\right) \) . Therefore

![bo_d7b6f8alb0pc73dd9avg_183_559_597_546_281_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_183_559_597_546_281_0.jpg)

This means

\[
{d}_{2} : \mathbb{R} \rightarrow  B,\;B \rightarrow  D,
\]

\[
0 \rightarrow  A,\;A \rightarrow  C,\;C \rightarrow  0
\]

must all be isomorphisms. It follows that

![bo_d7b6f8alb0pc73dd9avg_183_547_1131_562_282_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_183_547_1131_562_282_0.jpg)

Therefore,

\[
{H}^{ * }\left( {\mathbb{C}{P}^{2}}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimensions }0,2,4 \\  0 & \text{ otherwise. } \end{array}\right.
\]

Exercise 14.22.1. Show that

\[
{H}^{ * }\left( {\mathbb{C}{P}^{n}}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimensions }0,2,4,\ldots ,{2n} \\  0 & \text{ otherwise. } \end{array}\right.
\]

Exercise 14.23 (Algebraic Künneth Formula). Let \( E \) and \( F \) be graded differential algebras over \( \mathbb{R} \) with differential operators \( \delta \) and \( d \) respectively. Define a differential operator \( D \) on the tensor product \( E \otimes  F \) by

\[
D\left( {e \otimes  f}\right)  = \left( {\delta e}\right)  \otimes  f + {\left( -1\right) }^{\deg e}e \otimes  {df}.
\]

Prove by a spectral sequence argument that

\[
{H}_{D}\left( {E \otimes  F}\right)  = {H}_{\delta }\left( E\right)  \otimes  {H}_{d}\left( F\right) .
\]

## Product Structures

In this section we define product structures on the Čech-de Rham complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) , the de Rham cohomology, and the Čech cohomology, and show that the isomorphism between de Rham and Čech is an isomorphism of graded algebras. We also discuss the product structures on a spectral sequence.

Let \( Z \) be the closed forms and \( B \) the exact forms on a manifold \( M \) . From the antiderivation property of the exterior derivative

\[
d\left( {\omega  \cdot  \eta }\right)  = \left( {d\omega }\right)  \cdot  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cdot  {d\eta },
\]

it follows that \( Z \) is a subring of \( {\Omega }^{ * }\left( M\right) \) and \( B \) is an ideal in \( Z \) . Hence the wedge product makes the de Rham cohomology \( {H}_{DR}^{ * }\left( M\right)  = Z/B \) into a graded algebra.

On the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) , where \( \mathfrak{U} \) is any open cover of \( M \) , a natural product

\[
\cup   : {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right)  \otimes  {C}^{r}\left( {\mathfrak{U},{\Omega }^{s}}\right)  \rightarrow  {C}^{p + r}\left( {\mathfrak{U},{\Omega }^{q + s}}\right)
\]

can be defined as follows. If \( \omega \) is in \( {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right) \) and \( \eta \) is in \( {C}^{r}\left( {\mathfrak{U},{\Omega }^{s}}\right) \) , then

(14.24)

\[
\left( {\omega  \cup  \eta }\right) \left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + r}}\right)  = {\left( -1\right) }^{qr}\omega \left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)  \cdot  \eta \left( {U}_{{\alpha }_{p}\ldots {\alpha }_{p + r}}\right) ,
\]

where on the right-hand side both forms are understood to be restricted to \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + r}} \) , with the usual convention that \( {\alpha }_{0} < \cdots  < {\alpha }_{p + r} \) .

REMARK 14.25. The sign \( {\left( -1\right) }^{qr} \) is needed to make the differential operator \( D \) into an antiderivation relative to the product structure. It makes sense that this should be the sign, for in defining the product, \( p \) and \( r \) are brought together, and so are \( q \) and \( s \) , so the order of \( q \) and \( r \) in \( {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right)  \otimes  {C}^{r}(\mathfrak{U} \) , \( {\Omega }^{s} \) ) are interchanged. It is a useful principle that whenever two symbols of degrees \( m \) and \( n \) are interchanged in a graded algebra, there should be the sign \( {\left( -1\right) }^{mn} \) .

Exercise 14.26. Let \( \omega  \in  {K}^{p, q} \) and \( \eta  \in  {K}^{r, s} \) . Show that

1) \( \delta \left( {\omega  \cup  \eta }\right)  = \left( {\delta \omega }\right)  \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {\delta \eta } \)

2) \( {D}^{\prime \prime }\left( {\omega  \cup  \eta }\right)  = \left( {{D}^{\prime \prime }\omega }\right)  \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {D}^{\prime \prime }\eta \)

3) \( D\left( {\omega  \cup  \eta }\right)  = \left( {D\omega }\right)  \cup  \eta  + {\left( -1\right) }^{\deg \omega }\omega  \cup  {D\eta } \) ,

where \( \deg \omega  = p + q \) .

We will often write \( \omega  \cdot  \eta \) or even \( {\omega \eta } \) for \( \omega  \cup  \eta \) .

The inclusion of the Čech complex \( {C}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) in the Čech-de Rham complex induces a product structure on \( {C}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) : if \( \omega \) is a \( p \) -cochain and \( \eta \) an \( r \) -cochain, then

(14.27)

\[
{\left( \omega  \cdot  \eta \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + r}} = {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \cdot  {\eta }_{{\alpha }_{p}\ldots {\alpha }_{p + r}}.
\]

By Exercise 14.26, \( \delta \) is an antiderivation relative to this product. So just as in the case of de Rham cohomology this makes the Čech cohomology \( {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) into a graded algebra. If \( \mathfrak{B} \) is a refinement of \( \mathfrak{U} \) , then the restriction map \( {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right)  \rightarrow  {H}^{ * }\left( {\mathfrak{B},\mathbb{R}}\right) \) is a homomorphism of algebras. Hence the direct limit \( {H}^{ * }\left( {M,\mathbb{R}}\right) \) is also a graded algebra. Note that (14.27) also makes sense for the Čech complex \( {C}^{ * }\left( {U,\mathbb{R}}\right) \) on a topological space \( X \) ; this gives a product structure on the Čech cohomology \( {H}^{ * }\left( {X,\mathbb{R}}\right) \) of any topological space \( X \) .

With the product structures just defined, both inclusions

\[
r : {\Omega }^{ * }\left( M\right)  \rightarrow  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)
\]

and

\[
i : {C}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right)  \rightarrow  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)
\]

are algebra homomorphisms. Since as we saw in Proposition 8.8, for a good cover these homomorphisms induce bijective maps in cohomology

\[
{H}_{DR}^{ * }\left( M\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}
\]

\[
{H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}
\]

the isomorphism between \( {H}_{DR}^{ * }\left( M\right) \) and \( {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) is an algebra isomorphism. Because \( {H}^{ * }\left( {M,\mathbb{R}}\right)  = {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) for a good cover \( \mathfrak{U} \) , we have the following.

Theorem 14.28. The isomorphism between de Rham and Čech

\[
{H}_{DR}^{ * }\left( M\right)  \simeq  {H}^{ * }\left( {M,\mathbb{R}}\right)
\]

is an isomorphism of graded algebras.

If a double complex \( K \) has a product structure relative to which its differential \( D \) is an antiderivation, the same is true of all the groups \( {E}_{r} \) and their operators \( {d}_{r} \) , since \( {E}_{r} \) is the homology of \( {E}_{r - 1} \) and \( {d}_{r} \) is induced from D. With product structures, Theorem 14.14 becomes

Theorem 14.29 Let \( K \) be a double complex with a product structure relative to which \( D \) is an antiderivation. There exists a spectral sequence

\[
\left\{  {{E}_{r},{d}_{r} : {E}_{r}^{p, q} \rightarrow  {E}_{r}^{p + r, q - r + 1}}\right\}
\]

converging to \( {H}_{D}\left( K\right) \) with the following properties:

1) The \( {E}_{2}^{p, q} \) term is \( {H}_{\delta }^{p, q}{H}_{d}\left( K\right) \) .

2) Each \( {E}_{r} \) , being the homology of its predecessor \( {E}_{r - 1} \) , inherits a product structure from \( {E}_{r - 1} \) . Relative to this product, \( {d}_{r} \) is an antiderivation.

WARNING. Although both \( {E}_{\infty } \) and \( {H}_{D}\left( K\right) \) inherit their ring structures from \( K \) , they are generally not isomorphic as rings.

Exercise 14.30 The product structure on the tensor product \( A \otimes  B \) of two graded rings \( A \) and \( B \) is given by

\[
\left( {a \otimes  b}\right) \left( {c \otimes  d}\right)  = {\left( -1\right) }^{\left( {\deg b}\right) \left( {\deg c}\right) }\left( {{ac} \otimes  {bd}}\right) , a, c \in  A, b, d \in  B.
\]

Show that if \( \pi  : E \rightarrow  M \) is a fiber bundle with fiber \( F \) over a simply connected manifold \( M \) and \( F \) has finite-dimensional cohomology, then the isomorphism of the \( {E}_{2} \) term of the spectral sequence with \( {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) \) is an isomorphism of graded algebras.

REMARK 14.31. Thus in Leray’s theorem (Theorem 14.18) each group \( {E}_{r} \) is an algebra relative to which \( {d}_{r} \) is an antiderivation; furthermore, if \( M \) is simply connected, \( {E}_{2} \) is isomorphic to \( {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) \) as a graded algebra.

Example 14.32 (The ring structure of \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) ). Assume for now that \( n = 2 \) . In example 14.22, by applying the spectral sequence of the fiber bundle

![bo_d7b6f8alb0pc73dd9avg_186_742_987_165_139_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_186_742_987_165_139_0.jpg)

we computed the additive structure of the graded algebra \( {H}^{ * }\left( {\mathbb{C}{P}^{2}}\right) \) . We found that the \( {E}_{2} \) term is

![bo_d7b6f8alb0pc73dd9avg_186_504_1294_645_342_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_186_504_1294_645_342_0.jpg)

The two \( {d}_{2} \) ’s shown are isomorphisms. Let \( a \) be a generator of

\[
{E}_{2}^{0,1} \simeq  {H}^{0}\left( {\mathbb{C}{P}^{2}}\right)  \otimes  {H}^{1}\left( {S}^{1}\right)  \simeq  {H}^{1}\left( {S}^{1}\right) .
\]

Then \( {d}_{2}a = x \) is a generator of

\[
{E}_{2}^{2,0} \simeq  {H}^{2}\left( {\mathbb{C}{P}^{2}}\right)  \otimes  {H}^{0}\left( {S}^{1}\right)  \simeq  {H}^{2}\left( {\mathbb{C}{P}^{2}}\right)
\]

and \( x \cdot  a \) is a generator of

\[
{E}_{2}^{2,1} = {H}^{2}\left( {\mathbb{C}{P}^{2}}\right)  \otimes  {H}^{1}\left( {S}^{1}\right) .
\]

\[
{d}_{2}\left( {x \cdot  a}\right)  = x \cdot  {d}_{2}a = {x}^{2}.
\]

![bo_d7b6f8alb0pc73dd9avg_187_496_303_627_334_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_187_496_303_627_334_0.jpg)

Because \( {d}_{2} : {E}_{2}^{2,1} \rightarrow  {E}_{2}^{4,0} \) is an isomorphism, a generator of \( {E}_{2}^{4,0} = \; {H}^{4}\left( {\mathbb{C}{P}^{2}}\right) \) is

So as a ring,

\[
{H}^{ * }\left( {\mathbb{C}{P}^{2}}\right)  = \mathbb{R}\left\lbrack  x\right\rbrack  /\left( {x}^{3}\right) .
\]

In general, the same argument yields the ring structure of \( \mathbb{C}{P}^{n} \) as

\[
{H}^{ * }\left( {\mathbb{C}{P}^{n}}\right)  = \mathbb{R}\left\lbrack  x\right\rbrack  /\left( {x}^{n + 1}\right)
\]

where \( x \) is an element in dimension 2.

## The Gysin Sequence

The spectral sequence of a fiber bundle is essentially a way of describing the complicated algebraic relations among the cohomology of the base space, the fiber, and the total space of the bundle. In certain special situations the spectral sequence simplifies to a long exact sequence. One such special case is the cohomology of a sphere bundle. The resulting sequence is called the Gysin sequence, which we now derive.

Let \( \pi  : E \rightarrow  M \) be an oriented sphere bundle with fiber \( {S}^{k} \) . By the orientability assumption, for any good cover \( \mathfrak{U} \) on \( M \) , the locally constant pre-sheaf \( {\mathcal{H}}^{k} \) has no monodromy and is the constant presheaf \( \mathbb{R} \) . Therefore the \( {E}_{2} \) term of the spectral sequence is

\( {E}_{2}^{p, q} = {H}^{p}\left( M\right)  \otimes  {H}^{q}\left( {S}^{k}\right) . \)

![bo_d7b6f8alb0pc73dd9avg_187_691_1686_673_264_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_187_691_1686_673_264_0.jpg)

Let \( n \) be any nonnegative integer. Since nothing in \( {E}_{2}^{n - k, k} \) can get killed (that is, nothing there lies in the image of \( {d}_{r} \) for \( r \geq  2 \) ), \( {E}_{\infty }^{n - k, k} \) is the subgroup of \( {E}_{2}^{n - k, k} \) consisting of those elements with \( {d}_{3} = {d}_{4} = \cdots  = 0 \) . Hence there is an inclusion

\[
0 \rightarrow  {E}_{\infty }^{n - k, k} \rightarrow  {E}_{2}^{n - k, k}
\]

This can be extended to an exact sequence

(*)

\[
0 \rightarrow  {E}_{\infty }^{n - k, k} \rightarrow  {E}_{2}^{n - k, k}\overset{{d}_{k + 1}}{ \rightarrow  }{E}_{2}^{n + 1,0} \rightarrow  {E}_{\infty }^{n + 1,0} \rightarrow  0,
\]

\[
{H}^{n - k}\left( M\right) \;{H}^{n + 1}\left( M\right)
\]

where the last map, called an edge homomorphism, exists and is surjective because every element of \( {E}_{2}^{n + 1,0} \) survives to \( {E}_{\infty } \) .

Because of the shape of the \( {E}_{2} \) term, the filtration (14.13) on \( {H}^{n}\left( E\right) \) becomes

\[
{H}^{n}\left( E\right)  \supset  {E}_{\infty }^{n,0} \supset  0
\]

in other words, there is an exact sequence

(**)

\[
0 \rightarrow  {E}_{\infty }^{n,0} \rightarrow  {H}^{n}\left( E\right)  \rightarrow  {E}_{\infty }^{n - k, k} \rightarrow  0.
\]

The two sequences (*) and (**) may be combined into a single long exact sequence

\[
\cdots  \rightarrow  {H}^{n}\left( E\right) \overset{\alpha }{ \rightarrow  }{H}^{n - k}\left( M\right) \overset{{d}_{k + 1}}{ \rightarrow  }{H}^{n + 1}\left( M\right) \overset{\beta }{ \rightarrow  }{H}^{n + 1}\left( E\right)  \rightarrow  \cdots .
\]

This is the Gysin sequence of the sphere bundle.

It remains to identify the maps in the Gysin sequence. Let \( \mathfrak{U} \) be a good cover on \( M \) . The map \( \alpha \) is the composition of

\[
{H}^{n}\left( E\right) \xrightarrow[]{\text{ projection }}{E}_{\infty }^{n - k, k} \subset  {E}_{2}^{n - k, k} = {H}^{n - k}\left( {{\pi }^{-1}\mathfrak{U},{\mathcal{H}}^{k}}\right)
\]

\[
= {H}^{n - k}\left( M\right)  \otimes  {H}^{k}\left( {S}^{k}\right)  \simeq  {H}^{n - k}\left( M\right) .
\]

In this sequence of maps the first three are the identity on the level of forms and the last one sends a generator of \( {H}^{k}\left( {S}^{k}\right) \) to 1 by integration. Therefore \( \alpha \) is integration along the fiber.

Next consider \( {d}_{k + 1} \) . Representing an element of

\[
{E}_{2}^{n - k, k} = {H}^{n - k}\left( M\right)  \otimes  {H}^{k}\left( {S}^{k}\right)
\]

by \( \left( {{\pi }^{ * }\omega }\right)  \cdot  \left( {-\psi }\right) \) , where \( \omega \) is a closed form on \( M \) and \( \psi \) is the angular form on \( E \) , we see that

\[
{d}_{k + 1}\left( {\left( {{\pi }^{ * }\omega }\right) \left( {-\psi }\right) }\right)  = d\left( {\left( {{\pi }^{ * }\omega }\right) \left( {-\psi }\right) }\right)  = {\left( -1\right) }^{n - k}\left( {{\pi }^{ * }\omega }\right) d\left( {-\psi }\right)
\]

\[
= {\left( -1\right) }^{n - k}\left( {{\pi }^{ * }\omega }\right) \left( {{\pi }^{ * }e}\right) .
\]

Hence, up to a sign \( {d}_{k + 1} : {H}^{n - k}\left( M\right)  \rightarrow  {H}^{n + 1}\left( M\right) \) is multiplication by the Euler class \( e \) .

Finally the map \( \beta \) is the composition

\[
{H}^{n + 1}\left( M\right)  = {H}^{n + 1}\left( {\mathfrak{U},{\mathcal{H}}^{0}\left( F\right) }\right) \overset{{\pi }^{ * }}{ \rightarrow  }{H}^{n + 1}\left( {{\pi }^{-1}\mathfrak{U},{\mathcal{H}}^{0}\left( F\right) }\right)
\]

\[
= {E}_{2}^{n + 1,0}\xrightarrow[]{\text{ projection }}{E}_{\infty }^{n + 1,0} \subset  {H}^{n + 1}\left( E\right) .
\]

So \( \beta  : {H}^{n + 1}\left( M\right)  \rightarrow  {H}^{n + 1}\left( E\right) \) is the natural pullback map \( {\pi }^{ * } \) .

We summarize this discussion as follows.

Proposition 14.33. Let \( \pi  : E \rightarrow  M \) be an oriented sphere bundle with fiber \( {S}^{k} \) . Then there is a long exact sequence

\[
\cdots  \rightarrow  {H}^{n}\left( E\right) \overset{{\pi }_{ * }}{ \rightarrow  }{H}^{n - k}\left( M\right) \overset{\land e}{ \rightarrow  }{H}^{n + 1}\left( M\right) \overset{{\pi }^{ * }}{ \rightarrow  }{H}^{n + 1}\left( E\right)  \rightarrow  \cdots ,
\]

in which the maps \( {\pi }_{ * }, \land  e \) , and \( {\pi }^{ * } \) are integration along the fiber, multiplication by the Euler class, and the natural pullback, respectively.

Exercise 14.33.1. Show that if the sphere bundle comes from a vector bundle \( \pi  : V \rightarrow  M \) , then the long exact sequence in the proposition may be identified with the relative exact sequence of the inclusion \( i : {V}^{0} \rightarrow  V \) , where \( {V}^{0} \) is the complement of the zero section in \( V \) . (Compare with Proposition 6.49.)

## Leray's Construction

We consider now more generally not a fiber bundle but any map \( \pi  : X \rightarrow  Y \) from one manifold to another, and study how the cohomology groups of \( X \) relate to those of \( Y \) . Let \( \mathfrak{U} \) be any cover for \( Y \) , not necessarily a good cover. Then \( {\pi }^{-1}\mathfrak{U} \) is a cover for \( X \) . By the Mayer-Vietoris principle (Proposition 8.8 or 14.16)

\[
{H}^{ * }\left( X\right)  = {H}_{D}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

By Theorem 14.14, if \( K \) is the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) on \( X \) , then the spectral sequence of \( K \) has

\[
{E}_{\infty } = {H}_{D}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) }\right\}
\]

and

\[
{E}_{2}^{p, q} = {H}_{\delta }^{p, q}{H}_{d}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

\[
K = \left| \begin{matrix}  & & & \\   & & \left| {\mathop{\prod }\limits_{{{\alpha }_{0} < \ldots  < {\alpha }_{p}}}{\Omega }^{q + 1}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right) }\right| & \\   & \mathop{\prod }\limits_{{{\alpha }_{0} < \ldots  < {\alpha }_{p}}}{\Omega }^{q}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right) & &  \end{matrix}\right|
\]

![bo_d7b6f8alb0pc73dd9avg_190_307_661_1033_247_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_190_307_661_1033_247_0.jpg)

Here

\[
{H}_{d}^{p, q}\left( K\right)  = \mathop{\prod }\limits_{{{\alpha }_{0} < \ldots  < {\alpha }_{p}}}{H}^{q}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)  = {C}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}}\right)
\]

where \( {\mathcal{H}}^{q} \) is the presheaf on \( Y \) defined by \( {\mathcal{H}}^{q}\left( U\right)  = {H}^{q}\left( {{\pi }^{-1}U}\right) \) . In summary, there is a spectral sequence converging to \( {H}^{ * }\left( X\right) \) with \( {E}_{2} \) term

\[
{E}_{2}^{p, q} = {H}^{p}\left( {\mathfrak{U},{\mathcal{H}}^{q}}\right) .
\]

The main difference between this situation and that of a fiber bundle (Theorem 14.18) is that the presheaf \( {\mathcal{H}}^{q} \) is no longer locally constant on \( \mathfrak{U} \) ; indeed the groups \( {H}^{q}\left( {{\pi }^{-1}U}\right) \) will in general be different for different contractible open sets \( U \) .

EXAMPLE 14.34. Consider the vertical projection of a circle \( {S}^{1} \) onto a segment \( I \) . Cover \( I \) with three open sets \( {U}_{0},{U}_{1},{U}_{2} \) as shown in Figure 14.1.

![bo_d7b6f8alb0pc73dd9avg_190_637_1549_404_539_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_190_637_1549_404_539_0.jpg)

Figure 14.1

The presheaf \( {\mathcal{H}}^{0} \) attaches a group to each vertex and each edge of the nerve \( N\left( \mathfrak{U}\right) \) in the way indicated below

![bo_d7b6f8alb0pc73dd9avg_191_589_420_432_137_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_191_589_420_432_137_0.jpg)

\( {H}_{d} \) of the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) is

![bo_d7b6f8alb0pc73dd9avg_191_450_670_744_369_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_191_450_670_744_369_0.jpg)

with \( \delta \) given by \( \left( {b,\left( {{c}_{1},{c}_{2}}\right) , d}\right)  \rightarrow  \left( {\left( {{c}_{1} - b,{c}_{2} - b}\right) ,\left( {d - {c}_{1}, d - {c}_{2}}\right) }\right) \) . Thus ker \( \delta  = \{ \left( {b,\left( {b, b}\right) , b}\right) \} \) and \( {H}_{\delta }^{0,0}{H}_{d} = \mathbb{R} \) . Since im \( \delta \) is 3-dimensional, \( {H}_{\delta }^{1,0}{H}_{d} = \mathbb{R} \) . So \( {H}_{\delta }{H}_{d} \) is

![bo_d7b6f8alb0pc73dd9avg_191_538_1227_574_229_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_191_538_1227_574_229_0.jpg)

In this case, then, \( {E}_{2} = {E}_{\infty } \) and we get the cohomology of \( {S}^{1} \) .

Let us find a nontrivial 1-cochain in \( {C}^{1}\left( {\mathfrak{U},{\mathcal{H}}^{0}}\right) \) that represents a generator of \( {H}^{1}\left( {S}^{1}\right) \) . A 1-cochain in \( {C}^{1}\left( {\mathfrak{U},{\mathcal{H}}^{0}}\right) \) is given by a 4-tuple \( \left( {\left( {r, s}\right) ,\left( {t, u}\right) }\right) \) . Such a 4-tuple is exact if and only if \( r - s = u - t \) . Therefore as a generator of \( {H}^{1}\left( {S}^{1}\right) \) we may take \( \left( {\left( {1,0}\right) ,\left( {0,0}\right) }\right) \) , i.e., the 1-cochain \( \tau \) (see Figure 14.2) such that

\[
\tau \left( {U}_{01}\right)  = \left( {1,0}\right)
\]

\[
\tau \left( {U}_{12}\right)  = \left( {0,0}\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_191_701_1727_258_365_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_191_701_1727_258_365_0.jpg)

Figure 14.2

Exercise 14.35. Project the sphere \( {S}^{2} \) to a disc \( D \) (Figure 14.3) and compute \( {H}^{ * }\left( {S}^{2}\right) \) by Leray’s method.

![bo_d7b6f8alb0pc73dd9avg_192_698_616_255_496_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_192_698_616_255_496_0.jpg)

Figure 14.3

Exercise 14.36. Let \( Y \) be a manifold and \( \mathfrak{U} \) a finite good cover of \( Y \) . Denote by \( {\beta }_{p} \) the number of nonempty \( \left( {p + 1}\right) \) -fold intersections \( {U}_{{\alpha }_{0}\ldots {\alpha }_{n}} \) . Show that \( \chi \left( Y\right)  = \sum {\left( -1\right) }^{p}{\beta }_{p} \) .

Exercise 14.37. Let \( \pi  : X \rightarrow  Y \) be any may and \( \mathfrak{U} \) a finite good cover of \( Y \) . Show that

\[
\chi \left( X\right)  = \mathop{\sum }\limits_{{p, q}}\mathop{\sum }\limits_{{{\alpha }_{0} < \cdots  < {\alpha }_{p}}}{\left( -1\right) }^{p + q}\dim {H}^{q}\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\cdots {\alpha }_{p}}}\right) .
\]

Deduce that if \( \pi  : X \rightarrow  Y \) is a fiber bundle with fiber \( F, Y \) admits a finite good cover and \( F \) has finite-dimensional cohomology, then

\[
\chi \left( X\right)  = \chi \left( F\right) \chi \left( Y\right)
\]
