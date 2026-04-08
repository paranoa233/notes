## CHAPTER II The Čech-de Rham Complex

## §8 The Generalized Mayer-Vietoris Principle

Reformulation of the Mayer-Vietoris Sequence

Let \( U \) and \( V \) be open sets on a manifold. In Section 2, we saw that the sequence of inclusions

\[
U \cup  V \leftarrow  U \coprod  V \subseteq  U \cap  V
\]

gives rise to an exact sequence of differential complexes

\[
0 \rightarrow  {\Omega }^{ * }\left( {U \cup  V}\right)  \rightarrow  {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right)  \rightarrow  {\Omega }^{ * }\left( {U \cap  V}\right)  \rightarrow  0
\]

called the Mayer-Vietoris sequence. The associated long exact sequence

\[
\cdots  \rightarrow  {H}^{q}\left( {U \cup  V}\right) \overset{\alpha }{ \rightarrow  }{H}^{q}\left( U\right)  \oplus  {H}^{q}\left( V\right) \overset{\delta }{ \rightarrow  }{H}^{q}\left( {U \cap  V}\right) \overset{{d}^{ * }}{ \rightarrow  }{H}^{q + 1}\left( {U \cup  V}\right)  \rightarrow  \cdots
\]

allows one to compute in many cases the cohomology of the union \( U \cup  V \) from the cohomology of the open subsets \( U \) and \( V \) . In this section, the Mayer-Vietoris sequence will be generalized from two open sets to countably many open sets. The main ideas here are due to Weil [1].

To make this generalization more transparent, we first reformulate the Mayer-Vietoris sequence for two open sets as follows. Let \( \mathfrak{U} \) be the open cover \( \{ U, V\} \) . Consider the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)  =  \oplus  {K}^{p, q} = \; \oplus  {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right) \) where

\[
{K}^{0, q} = {C}^{0}\left( {\mathfrak{U},{\Omega }^{q}}\right)  = {\Omega }^{q}\left( U\right)  \oplus  {\Omega }^{q}\left( V\right)
\]

\[
{K}^{1, q} = {C}^{1}\left( {\mathfrak{U},{\Omega }^{q}}\right)  = {\Omega }^{q}\left( {U \cap  V}\right) ,
\]

\[
{K}^{p, q} = 0,\;p \geq  2.
\]

![bo_d7b6f8alb0pc73dd9avg_100_477_306_670_366_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_100_477_306_670_366_0.jpg)

This double complex is equipped with two differential operators, the exterior derivative \( d \) in the vertical direction and the difference operator \( \delta \) in the horizontal direction. Of course, \( \delta \) is 0 after the first column. Because \( d \) and \( \delta \) are independent operators, they commute.

In general given a doubly graded complex \( {K}^{*, * } \) with commuting differentials \( d \) and \( \delta \) , one can form a singly graded complex \( {K}^{ * } \) by summing along the antidiagonal lines

![bo_d7b6f8alb0pc73dd9avg_100_484_979_700_303_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_100_484_979_700_303_0.jpg)

and defining the differential operator to be

\[
D = {D}^{\prime } + {D}^{\prime \prime }\text{ with }{D}^{\prime } = \delta ,{D}^{\prime \prime } = {\left( -1\right) }^{p}d\text{ on }{K}^{p, q}\text{ . }
\]

REMARK ON THE DEFINITION OF D.

\[
{D}^{2} = {d}^{2} + {\delta d} - {d\delta } + {\delta }^{2} = 0.
\]

![bo_d7b6f8alb0pc73dd9avg_100_620_1535_431_429_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_100_620_1535_431_429_0.jpg)

If \( D \) were naively defined as \( \widetilde{D} = d + \delta \) , it would not be a differential operator since \( {\widetilde{D}}^{2} = {2d\delta } \neq  0 \) . However, if we alternate the sign of \( d \) from one column to the next, then as is apparent from the diagram above,

In the sequel we will use the same symbol \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) to denote the double complex and its associated single complex. In this setup, the Mayer-Vietoris principle assumes the following form.

Theorem 8.1. The double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) computes the de Rham cohomology of \( M \) :

\[
{H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}   \simeq  {H}_{DR}^{ * }\left( M\right) .
\]

Proof. In one direction there is the natural map

\[
r : {\Omega }^{ * }\left( M\right)  \rightarrow  {\Omega }^{ * }\left( U\right)  \oplus  {\Omega }^{ * }\left( V\right)  \subset  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)
\]

given by the restriction of forms. Our first observation is that \( r \) is a chain map, i.e., that the following diagram is commutative:

![bo_d7b6f8alb0pc73dd9avg_101_651_924_337_219_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_101_651_924_337_219_0.jpg)

This is because

\[
{Dr} = \left( {\delta  + {\left( -1\right) }^{p}d}\right) r\;\left\lbrack  {\text{ here }p = 0}\right\rbrack
\]

\[
= {dr}
\]

\[
= {rd}\text{ . }
\]

Consequently \( r \) induces a map in cohomology

\[
{r}^{ * } : {H}_{DR}^{ * }\left( M\right)  \rightarrow  {H}_{D}\left\{  {\left( {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .}\right.
\]

![bo_d7b6f8alb0pc73dd9avg_101_609_1509_432_320_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_101_609_1509_432_320_0.jpg)

A \( q \) -cochain \( \alpha \) in the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) has two components

\[
\alpha  = {\alpha }_{0} + {\alpha }_{1},\;{\alpha }_{0} \in  {K}^{0, q},\;{\alpha }_{1} \in  {K}^{1, q - 1}.
\]

By the exactness of the Mayer-Vietoris sequence there exists a \( \beta \) such that \( {\delta \beta } = {\alpha }_{1} \) . With this choice of \( \beta ,\alpha  - {D\beta } \) has only the \( \left( {0, q}\right) \) -component. Thus, every cochain in \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) is D-cohomologous to a cochain with only the top component.

We now show \( {r}^{ * } \) to be an isomorphism.

Step 1. r* is surjective.

By the remark above we may assume that a given cohomology class in \( {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\} \) is represented by a cocycle \( \phi \) with only the top component. In this case

\[
{D\phi } = 0\;\text{ if and only if }\;{d\phi } = {\delta \phi } = 0.
\]

So \( \phi \) is a global closed form.

Step 2. \( {r}^{ * } \) is injective.

Suppose \( r\left( \omega \right)  = {D\phi } \) for some cochain \( \phi \) in \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) . Again by the remark above we may write \( \phi  = {\phi }^{\prime } + D{\phi }^{\prime \prime } \) , where \( {\phi }^{\prime } \) has only the top component. Then

\[
r\left( \omega \right)  = D{\phi }^{\prime } = d{\phi }^{\prime },\;\delta {\phi }^{\prime } = 0.
\]

So \( \omega \) is the exterior derivative of a global form on \( M \) .

![bo_d7b6f8alb0pc73dd9avg_102_656_994_337_321_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_102_656_994_337_321_0.jpg)

## Generalization to Countably Many Open Sets and Applications

Instead of a cover with two open sets as in the usual Mayer-Vietoris sequence, consider the open cover \( \mathfrak{U} = {\left\{  {U}_{\alpha }\right\}  }_{\alpha \epsilon J} \) of \( M \) , where the index set \( J \) is a countable ordered set. Of course \( J \) may be finite. Denote the pairwise intersections \( {U}_{\alpha } \cap  {U}_{\beta } \) by \( {U}_{\alpha \beta } \) , triple intersections \( {U}_{\alpha } \cap  {U}_{\beta } \cap  {U}_{\gamma } \) by \( {U}_{\alpha \beta \gamma } \) , etc. There is a sequence of inclusions of open sets

\[
M \leftarrow  \coprod {U}_{{\alpha }_{0}}\overset{{\alpha }_{0}}{\overbrace{{\rho }_{1}}}\mathop{\coprod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{U}_{{\alpha }_{0}{\alpha }_{1}}\overset{{\alpha }_{0}}{\overbrace{{\rho }_{2}}}\overbrace{\mathop{\coprod }\limits_{{{\alpha }_{0} < {\alpha }_{1} < {\alpha }_{2}}}}{U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}} \subsetneqq  \cdots
\]

where \( {\partial }_{\mathrm{i}} \) is the inclusion which "ignores" the \( i \) th open set; for example,

\[
{\partial }_{0} : {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}} \hookrightarrow  {U}_{{\alpha }_{1}{\alpha }_{2}}
\]

This sequence of inclusions of open sets induces a sequence of restrictions of forms

\[
{\Omega }^{ * }\left( M\right) \overset{r}{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) \overset{{\delta }_{0}}{\overset{{\delta }_{1}}{ \rightarrow  }}\mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\overset{{\delta }_{1}}{ \rightarrow  }}{\overset{{\delta }_{1}}{ \rightarrow  }}\mathop{\prod }\limits_{{{\alpha }_{0} < {\alpha }_{1} < {\alpha }_{2}}}{\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\right) \overset{ \rightarrow  }{ \rightarrow  }\cdots
\]

where \( {\delta }_{0} \) , for instance, is induced from the inclusion

\[
{\partial }_{0} : \mathop{\coprod }\limits_{\alpha }{U}_{\alpha \beta \gamma } \rightarrow  {U}_{\beta \gamma }
\]

and therefore is the restriction

\[
{\delta }_{0} : {\Omega }^{ * }\left( {U}_{\beta \gamma }\right)  \rightarrow  \mathop{\prod }\limits_{\alpha }{\Omega }^{ * }\left( {U}_{\alpha \beta \gamma }\right) .
\]

We define the difference operator \( \delta  : \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right)  \rightarrow  \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\right) \) to be the alternating difference \( {\delta }_{0} - {\delta }_{1} + {\delta }_{2} \) . Thus

\[
{\left( \delta \xi \right) }_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}} = {\xi }_{{\alpha }_{1}{\alpha }_{2}} - {\xi }_{{\alpha }_{0}{\alpha }_{2}} + {\xi }_{{\alpha }_{0}{\alpha }_{1}}.
\]

More generally the difference operator is defined as follows.

Definition 8.2. If \( \omega  \in  \prod {\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) , then \( \omega \) has "components" \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} \in \; {\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) and

\[
{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} = \mathop{\sum }\limits_{{i = 0}}^{{p + 1}}{\left( -1\right) }^{i}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 1}},
\]

where on the right-hand side the restriction operation to \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p + 1}} \) has been suppressed and the caret denotes omission.

Proposition 8.3. \( {\delta }^{2} = 0 \) .

Proof. Basically this is true because in \( {\left( {\delta }^{2}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 2}} \) we omit two indices \( {\alpha }_{i},{\alpha }_{j} \) twice with opposite signs. To be precise,

\[
{\left( {\delta }^{2}\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p + 2}} = \sum {\left( -1\right) }^{i}{\left( \delta \omega \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 2}}
\]

\[
= \mathop{\sum }\limits_{{j < i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j}{\omega }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{j}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p + 2}}
\]

\[
+ \mathop{\sum }\limits_{{j > i}}{\left( -1\right) }^{i}{\left( -1\right) }^{j - 1}{\omega }_{{\alpha }_{0}\ldots {\alpha }_{i}\ldots {\alpha }_{j\cdots {\alpha }_{p} + 2}}
\]

\[
= 0\text{ . }
\]

Convention. Up until now the indices in \( {\omega }_{{\alpha }_{0}\ldots {\alpha }_{n}} \) are all in increasing order \( {\alpha }_{0} < \ldots  < {\alpha }_{p} \) . More generally we will allow indices in any order, even with repetitions, subject to the convention that when two indices are interchanged, the form becomes its negative:

\[
{\omega }_{\ldots \alpha \ldots \beta \ldots } =  - {\omega }_{\ldots \beta \ldots \alpha \ldots }.
\]

In particular a form with repeated indices is 0 . In the following exercise the reader is asked to check that this convention is consistent with the definition of the difference operator \( \delta \) above.

Exercise 8.4. Suppose \( \alpha  < \beta \) . Then \( {\left( \delta \omega \right) }_{\ldots \beta \ldots \alpha \ldots } \) may be defined either as \( - {\left( \delta \omega \right) }_{\ldots \alpha \ldots \beta \ldots } \) or by the difference operator formula (8.2). Show that these two definitions agree.

Proposition 8.5. (The Generalized Mayer-Vietoris Sequence). The sequence

\[
0 \rightarrow  {\Omega }^{ * }\left( M\right) \overset{r}{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) \overset{\delta }{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}}\right) \overset{\delta }{ \rightarrow  }\prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}{\alpha }_{1}{\alpha }_{2}}\right) \overset{\delta }{ \rightarrow  }\ldots
\]

is exact; in other words, the \( \delta \) -cohomology of this complex vanishes identically.

Proof. Clearly \( {\Omega }^{ * }\left( M\right) \) is the kernel of the first \( \delta \) since an element of \( \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}}\right) \) is a global form on \( M \) if and only if its components agree on the overlaps.

Now let \( \left\{  {\rho }_{\alpha }\right\} \) be a partition of unity subordinate to the open cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) . Suppose \( \omega  \in  \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) is a \( p \) -cocycle. Define a \( \left( {p - 1}\right) \) - cochain \( \tau \) by

\[
{\tau }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}.
\]

Then

\[
{\left( \delta \tau \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\tau }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= \mathop{\sum }\limits_{{i,\alpha }}{\left( -1\right) }^{i}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

Because \( \omega \) is a cocycle,

\[
{\left( \delta \omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p}} = {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \mathop{\sum }\limits_{i}{\left( -1\right) }^{i + 1}{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}} = 0.
\]

So

\[
{\left( \delta \tau \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \mathop{\sum }\limits_{\alpha }{\rho }_{\alpha }\mathop{\sum }\limits_{i}{\left( -1\right) }^{i}{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= \mathop{\sum }\limits_{\alpha }{\rho }_{\alpha }{\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}}
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}}
\]

This shows that every cocycle is a coboundary. The exactness now follows from Proposition 8.3.

In fact, the definition of \( \tau \) in this proof gives a homotopy operator on the complex. Write \( {K\omega } \) for \( \tau \) :

(8.6)

\[
{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \mathop{\sum }\limits_{\alpha }{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}.
\]

Then

\[
{\left( \delta K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \sum {\left( -1\right) }^{i}{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= \sum {\left( -1\right) }^{i}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
{\left( K\delta \omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}} = \sum {\rho }_{\alpha }{\left( \delta \omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p}}
\]

\[
= \left( {\sum {\rho }_{\alpha }}\right) {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} + \sum {\left( -1\right) }^{i + 1}{\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\widehat{\alpha }}_{i}\ldots {\alpha }_{p}}
\]

\[
= {\omega }_{{\alpha }_{0}\ldots {\alpha }_{p}} - {\left( \delta K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p}}.
\]

Therefore, \( K \) is an operator from \( \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) to \( \prod {\Omega }^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p - 1}}\right) \) such that

(8.7)

\[
{\delta K} + {K\delta } = 1.
\]

As in the proof of the Poincaré lemma, the existence of a homotopy operator on a differential complex implies that the cohomology of the complex vanishes.

For future reference we note here that if \( \phi \) is a cocycle, then by (8.7), \( {\delta K\phi } = \phi \) . So on cocycles \( K \) is a right inverse to \( \delta \) . Given such \( \phi \) , the set of all solutions \( \xi \) of \( {\delta \xi } = \phi \) consists of \( {K\phi } + \delta \) -coboundaries.

The Mayer-Vietoris sequence may be arranged as an augmented double complex

![bo_d7b6f8alb0pc73dd9avg_105_471_792_727_430_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_105_471_792_727_430_0.jpg)

where \( {K}^{p, q} = {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right)  = \prod {\Omega }^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right) \) consists of the " \( p \) -cochains of the cover \( \mathfrak{U} \) with values in the \( q \) -forms." The horizontal maps of the double complex are the difference operators \( \delta \) and the vertical ones the exterior derivatives \( d \) . As before, the double complex may be made into a single complex with the differential operator given by

\[
D = {D}^{\prime } + {D}^{\prime \prime } = \delta  + {\left( -1\right) }^{p}d.
\]

A \( D \) -cocycle is a string such as \( \phi  = a + b + c \) with

![bo_d7b6f8alb0pc73dd9avg_105_548_1675_559_337_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_105_548_1675_559_337_0.jpg)

(To be precise we should write \( {\delta a} =  - {D}^{\prime \prime }b,{\delta b} =  - {D}^{\prime \prime }c \) .) So a \( D \) -cocycle may be pictured as a "zig-zag."

A \( D \) -coboundary is a string such as \( \phi  = a + b + c \) in the figure below, where \( a = \delta {a}_{1} + {D}^{\prime \prime }{a}_{2} \) , etc.

![bo_d7b6f8alb0pc73dd9avg_106_573_422_483_409_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_106_573_422_483_409_0.jpg)

The double complex

\[
{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)  = {\bigoplus }_{p, q \geq  0}{C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right)
\]

is called the Čech-de Rham complex, and an element of the Čech-de Rham complex is called a Čech-de Rham cochain. We sometimes refer to a C̆ech-de Rham cochain more simply as a D-cochain.

The fact that all the rows of the augmented complex are exact is the key ingredient in the proof of the following.

Proposition 8.8 (Generalized Mayer-Vietoris Principle). The double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) computes the de Rham cohomology of \( M \) ; more precisely, the restriction map \( r : {\Omega }^{ * }\left( M\right)  \rightarrow  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) induces an isomorphism in cohomology:

\[
{r}^{ * } : {H}_{DR}^{ * }\left( M\right)  \rightarrow  {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

Proof. Since \( {Dr} = \left( {\delta  + d}\right) r = {dr} = {rd}, r \) is a chain map, and so it induces a map \( {r}^{ * } \) in cohomology.

Step 1. \( {r}^{ * } \) is surjective.

![bo_d7b6f8alb0pc73dd9avg_106_348_1678_972_292_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_106_348_1678_972_292_0.jpg)

Let \( \phi \) be a cocycle relative to \( D \) . By \( \delta \) -exactness the lowest component of \( \phi \) is \( \delta \) of something. By subtracting \( D \) (something) from \( \phi \) , we can remove the lowest component of \( \phi \) and still stay in the same cohomology class as \( \phi \) .

After iterating this procedure enough times we can move \( \phi \) in its cohomology class to a cocycle \( {\phi }^{\prime } \) with only the top component. \( {\phi }^{\prime } \) is a closed global form because \( d{\phi }^{\prime } = 0 \) and \( \delta {\phi }^{\prime } = 0 \) .

Step 2. \( {r}^{ * } \) is injective.

![bo_d7b6f8alb0pc73dd9avg_107_254_526_1102_339_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_107_254_526_1102_339_0.jpg)

If \( r\left( \omega \right)  = {D\phi } \) , we can shorten \( \phi \) as before by subtracting boundaries until it consists of only the top component. Then because \( {\delta \phi } \) is 0, it is actually a global form on \( M \) . So \( \omega \) is exact.

The proof of this proposition is a very general argument from which we may conclude: if all the rows of an augmented double complex are exact, then the D-cohomology of the complex is isomorphic to the cohomology of the initial column.

It is natural to augment each column by the kernel of the bottom \( d \) , denoted \( {C}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) . The vector space \( {C}^{p}\left( {\mathfrak{U},\mathbb{R}}\right) \) consists of the locally constant functions on the \( \left( {p + 1}\right) \) -fold intersections \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) .

![bo_d7b6f8alb0pc73dd9avg_107_321_1349_915_382_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_107_321_1349_915_382_0.jpg)

The bottom row

\[
{C}^{0}\left( {\mathfrak{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }{C}^{1}\left( {\mathfrak{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }{C}^{2}\left( {\mathfrak{U},\mathbb{R}}\right) \overset{\delta }{ \rightarrow  }
\]

is a differential complex, and the homology of this complex, \( {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) , is called the Čech cohomology of the cover \( \mathfrak{U} \) . This is a purely combinatorial object. Note that the argument for the exactness of the generalized Mayer-Vietoris sequence breaks down for the complex \( {C}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) , because here the cochains are locally constant functions so that partitions of unity are not applicable.

If the augmented columns of the complex \( {C}^{ * }\left( {U,{\Omega }^{ * }}\right) \) are exact, then the same argument as in (8.8) will yield an isomorphism between the Čech cohomology and the cohomology of the double complex

\[
{H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \overset{ \sim  }{ \rightarrow  }{H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}
\]

and consequently an isomorphism between de Rham cohomology and Čech cohomology

\[
{H}_{DR}^{ * }\left( M\right)  \simeq  {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) .
\]

Now the failure of the \( {p}^{\text{ th }} \) column to be exact is measured by the cohomology groups

\[
\mathop{\prod }\limits_{\substack{{q \geq  1} \\  {{\alpha }_{0} < \cdots  < {\alpha }_{p}} }}{H}^{q}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)
\]

So if the cover is such that all finite nonempty intersections are contractible, e.g., a good cover, then all augmented columns will be exact. We have proven

Theorem 8.9. If \( \mathfrak{U} \) is a good cover of the manifold \( M \) , then the de Rham cohomology of \( M \) is isomorphic to the Čech cohomology of the good cover

\[
{H}_{DR}^{ * }\left( M\right)  \simeq  {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) .
\]

Let us recapitulate here what has transpired so far. First, the basic sequence of inclusions

\[
M \leftarrow  {U}_{\alpha } \leftleftarrows  {U}_{\alpha \beta } \succapprox  {U}_{\alpha \beta \gamma } \succapprox  \cdots
\]

gives rise to the diagram

![bo_d7b6f8alb0pc73dd9avg_108_483_1476_708_325_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_108_483_1476_708_325_0.jpg)

combinatorics of the cover

Along the left-hand side is the differential geometry of forms on \( M \) , along the bottom is the combinatorics of the cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) , and in the double complex itself the two are mixed. As the complex is the generalized Mayer-Vietoris sequence, the augmented rows are exact, for any cover. It follows that the de Rham cohomology of \( M \) is always isomorphic to the cohomology of the double complex:

\[
{H}_{DR}^{ * }\left( M\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

If in addition \( \mathfrak{U} \) is a good cover, then by the Poincare lemma the augmented columns are exact. In that case the Čech cohomology of the cover is also isomorphic to the cohomology of the double complex:

\[
{H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  .
\]

Hence there is an isomorphism between de Rham and Čech. This result provides us with a way of computing the de Rham cohomology by means of combinatorics, since from Section 5 we know that every manifold has a good cover. All three complexes here can be given product structures, in which case the isomorphisms between them are actually isomorphisms of algebras, as will be shown in (14.28).

A priori there is no reason why different covers of \( M \) should have the same Čech cohomology. However, it follows from Theorem 8.9 that

Corollary 8.9.1. The Čech cohomology \( {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) is the same for all good covers \( \mathfrak{U} \) of \( M \) .

If a manifold is compact, then it has a finite good cover. For such a cover the Čech cohomology \( {H}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) is clearly finite-dimensional. Thus,

Corollary 8.9.2. The de Rham cohomology \( {H}_{DR}^{ * }\left( M\right) \) of a compact manifold is finite-dimensional.

In fact,

Corollary 8.9.3. Whenever M has a finite good cover, its de Rham cohomology \( {H}_{DR}^{ * }\left( M\right) \) is finite-dimensional.

Both the proof here and the induction argument in Section 5 of the finite dimensionality of the de Rham cohomology rest on the Mayer-Vietoris sequence, but they are otherwise independent of each other.
