## §9 More Examples and Applications of the Mayer-Vietoris Principle

In the previous section we used the Mayer-Vietoris principle to show the isomorphism of the de Rham cohomology of a manifold and the Čech cohomology of a good cover; from this, various corollaries follow. In this section, after some examples in which the combinatorics of a good cover is used to compute the de Rham cohomology, we give an explicit isomorphism from Čech to de Rham: given a Čech cocycle, we construct the corresponding global closed differential form by means of a collating formula (9.5) based on the homotopy operator \( K \) of (8.6). To conclude the section, we give as another application of the Mayer-Vietoris principle a proof of the Künneth formula valid under the hypothesis that one of the factors has finite-dimensional cohomology.

## Examples: Computing the de Rham Cohomology from the Combinatorics of a Good Cover

Let \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) be an open cover of a manifold \( M \) . The nerve of \( \mathfrak{U} \) is a simplicial complex constructed as follows. To every open set \( {U}_{\alpha } \) , we associate a vertex \( \alpha \) . If \( {U}_{\alpha } \cap  {U}_{\beta } \) is nonempty, we connect the vertices \( \alpha \) and \( \beta \) with an edge. If \( {U}_{\alpha } \cap  {U}_{\beta } \cap  {U}_{\gamma } \) is nonempty, we fill in the face of the triangle \( {\alpha \beta \gamma } \) . Repeating this procedure for all finite intersections gives the nerve of \( \mathfrak{U} \) , denoted \( N\left( \mathfrak{U}\right) \) . For the basics of simplicial complexes, see Croom [1].

Example 9.1 (The circle). Let \( \mathfrak{U} = \left\{  {{U}_{0},{U}_{1},{U}_{2}}\right\} \) be the good cover of the circle as shown in Figure 9.1. The Čech complex has two terms:

\( {C}^{0}\left( {\mathfrak{U},\mathbb{R}}\right)  = \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} = \left\{  {\left( {{\omega }_{0},{\omega }_{1},{\omega }_{2}}\right)  \mid  {\omega }_{\alpha }\text{ is a constant on }{U}_{\alpha }}\right\}  , \)

\( {C}^{1}\left( {\mathfrak{U},\mathbb{R}}\right)  = \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} = \left\{  {\left( {{\eta }_{01},{\eta }_{02},{\eta }_{12}}\right)  \mid  {\eta }_{\alpha \beta }\text{ is a constant on }{U}_{\alpha \beta }}\right\}  . \)

![bo_d7b6f8alb0pc73dd9avg_110_635_1358_380_379_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_110_635_1358_380_379_0.jpg)

Figure 9.1

The coboundary \( \delta  : {C}^{0} \rightarrow  {C}^{1} \) is given by \( {\left( \delta \omega \right) }_{\alpha \beta } = {\omega }_{\beta } - {\omega }_{\alpha } \) . Therefore,

\[
\ker \delta  = \left\{  {\left( {{\omega }_{0},{\omega }_{1},{\omega }_{2}}\right)  \mid  {\omega }_{0} = {\omega }_{1} = {\omega }_{2}}\right\}   = \mathbb{R}
\]

and

\[
{H}^{0}\left( {S}^{1}\right)  = \mathbb{R}.
\]

Since im \( \delta  = {\mathbb{R}}^{2},{H}^{1}\left( {S}^{1}\right)  = {\mathbb{R}}^{3}/\mathrm{{im}}\delta  = \mathbb{R} \) .

EXAMPLE 9.2 (A nontrivial 1-cocycle on the circle). If a 1-cocycle \( \eta  = \left( {\eta }_{01}\right. \) , \( \left. {{\eta }_{02},{\eta }_{12}}\right) \) is a coboundary, then \( {\eta }_{01} - {\eta }_{02} + {\eta }_{12} = 0 \) . So \( \eta  = \left( {1,0,0}\right) \) is a nontrivial 1-cocycle on the circle. three terms:

EXAMPLE 9.3 (The 2-sphere). Cover the lower hemisphere of Figure 9.2 with three open sets as in Figure 9.3. Together with the upper hemisphere \( {U}_{0} \) , this gives a good cover of the entire sphere. The nerve of the cover is the surface of a tetrahedron as depicted in Figure 9.4. The Čech complex has

![bo_d7b6f8alb0pc73dd9avg_111_658_710_306_303_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_111_658_710_306_303_0.jpg)

Figure 9.2

![bo_d7b6f8alb0pc73dd9avg_111_630_1178_387_382_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_111_630_1178_387_382_0.jpg)

Figure 9.3

![bo_d7b6f8alb0pc73dd9avg_111_614_1709_421_370_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_111_614_1709_421_370_0.jpg)

Figure 9.4

\( \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R}\;\mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R}\;\mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R}\;\mathbb{R} \oplus  \mathbb{R} \oplus  \mathbb{R} \)

\( \begin{array}{llllllllllllllllllll} 0 & 1 & 2 & 3 & 0 & 1 & 0 & 2 & 0 & 3 & {12} & {13} & {23} & {01} & 2 & 0 & {13} & 0 & {23} & {123} \end{array} \)

\( \ker {\delta }_{0} = \left\{  {\left( {{\omega }_{0},{\omega }_{1},{\omega }_{2},{\omega }_{3}}\right)  \mid  {\omega }_{0} = {\omega }_{1} = {\omega }_{2} = {\omega }_{3}}\right\}   = \mathbb{R} \)

So im \( {\delta }_{0} = {\mathbb{R}}^{3} \) and \( {H}^{0}\left( {S}^{2}\right)  = \mathbb{R} \) . If \( \eta \) is in ker \( {\delta }_{1} \) , then \( \eta \) is completely determined by \( {\eta }_{01},{\eta }_{02} \) , and \( {\eta }_{03} \) . Therefore ker \( {\delta }_{1} = {\mathbb{R}}^{3} \) and

\[
{H}^{1}\left( {S}^{2}\right)  = \ker {\delta }_{1}/\operatorname{im}{\delta }_{0} = 0.
\]

Since im \( {\delta }_{1} = {C}^{1}/\ker {\delta }_{1} = {\mathbb{R}}^{3} \) ,

\[
{H}^{2}\left( {S}^{2}\right)  = {\mathbb{R}}^{4}/\mathrm{{im}}{\delta }_{1} = \mathbb{R}.
\]

Explicit Isomorphisms between the Double Complex and de Rham and Čech

We saw in Proposition 8.8 that the Čech-de Rham complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) and the de Rham complex \( {\Omega }^{ * }\left( M\right) \) have the same cohomology. Actually, what is true is that these two complexes are chain homotopic. To be more precise, there is a chain map

(9.4)

\[
f : {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)  \rightarrow  {\Omega }^{ * }\left( M\right)
\]

such that

(a) \( f \circ  r = 1 \) , and

(b) \( r \circ  f \) is chain homotopic to the identity.

We may think of \( f \) as a recipe for collating together the components of a Čech-de Rham cochain into a global form. The not very intuitive formulas below were obtained, after repeated tries, by a careful bookkeeping of the inductive steps in the proof of Proposition 8.8.

Proposition 9.5 (The Collating Formula). Let \( K \) be the homotopy operator defined in (8.6). If \( \alpha  = \mathop{\sum }\limits_{{i = 0}}^{n}{\alpha }_{i} \) is an n-cochain and \( {D\alpha } = \beta  = \mathop{\sum }\limits_{{i = 0}}^{{n + 1}}{\beta }_{i} \) , then

\[
f\left( \alpha \right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\left( -{D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} - \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}K{\left( -{D}^{\prime \prime }K\right) }^{i - 1}{\beta }_{i} \in  {C}^{0}\left( {\mathfrak{U},{\Omega }^{n}}\right)
\]

is a global form satisfying the properties above. The homotopy operator

\[
L : {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)  \rightarrow  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right)
\]

such that \( 1 - r \circ  f = {DL} + {LD} \) is given by

\[
{L\alpha } = \mathop{\sum }\limits_{{p = 0}}^{{n - 1}}{\left( L\alpha \right) }_{p}
\]

where

\[
{\left( L\alpha \right) }_{p} = \mathop{\sum }\limits_{{i = p + 1}}^{n}K{\left( -{D}^{\prime \prime }K\right) }^{i - \left( {p + 1}\right) }{\alpha }_{i} \in  {C}^{p}\left( {\mathfrak{U},{\Omega }^{n - 1 - p}}\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_113_536_493_524_494_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_113_536_493_524_494_0.jpg)

REMARK. To strip away some of the mysteries in the expression for \( f\left( \alpha \right) \) , it may be helpful to observe that the operator \( {D}^{\prime \prime }K \) sends an element of \( {C}^{p}\left( {\mathfrak{U},{\Omega }^{q}}\right) \) into \( {C}^{p - 1}\left( {\mathfrak{U},{\Omega }^{q + 1}}\right) \) , so that \( {\left( {D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} \) and \( K{\left( {D}^{\prime \prime }K\right) }^{i - 1}{\beta }_{i} \) are collections of \( n \) -forms on the open sets \( {U}_{\alpha } \) . The collating formula says that a suitable linear combination of these local \( n \) -forms, with \( \pm  1 \) as coefficients, is the restriction of a global form.

The proof of Proposition 9.5 requires the following technical lemma.

Lemma 9.6. For \( i \geq  1 \) ,

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{i} = {\left( {D}^{\prime \prime }K\right) }^{i}\delta  - {\left( {D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime }.
\]

Proof of Lemma 9.6. Since \( \delta \) anticommutes with \( {D}^{\prime \prime } \) and since \( {\delta K} + {K\delta } = 1, \)

\[
\delta \left( {{D}^{\prime \prime }K}\right) {\left( {D}^{\prime \prime }K\right) }^{i - 1} =  - {D}^{\prime \prime }{\delta K}{\left( {D}^{\prime \prime }K\right) }^{i - 1}
\]

\[
=  - {D}^{\prime \prime }\left( {1 - {K\delta }}\right) {\left( {D}^{\prime \prime }K\right) }^{i - 1}
\]

\[
= \left( {{D}^{\prime \prime }K}\right) \delta {\left( {D}^{\prime \prime }K\right) }^{i - 1}\text{ . }
\]

So we can commute \( {D}^{\prime \prime }K \) and \( \delta \) until we reach \( {\left( {D}^{\prime \prime }K\right) }^{i - 1}\delta \left( {{D}^{\prime \prime }K}\right) \) . Then,

\[
\delta {\left( {D}^{\prime \prime }K\right) }^{i} = {\left( {D}^{\prime \prime }K\right) }^{i - 1}\delta \left( {{D}^{\prime \prime }K}\right)
\]

\[
=  - {\left( {D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime }\left( {1 - {K\delta }}\right)
\]

\[
=  - {\left( {D}^{\prime \prime }K\right) }^{i - 1}{D}^{\prime \prime } + {\left( {D}^{\prime \prime }K\right) }^{i}\delta .
\]

Proof of Proposition 9.5. To show that \( f\left( \alpha \right) \) is a global form, we compute \( {\delta f}\left( \alpha \right) \) . Using the lemma above and the fact that \( \delta {\alpha }_{i} + {D}^{\prime \prime }{\alpha }_{i + 1} = {\beta }_{i + 1} \) , this is a straightforward exercise which we leave to the reader. Exercise 9.7. Show that \( {\delta f}\left( \alpha \right)  = 0 \) .

Next we check that \( f \) is a chain map.

\[
f\left( {D\alpha }\right)  = f\left( \beta \right)  = \mathop{\sum }\limits_{{i = 0}}^{{n + 1}}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\beta }_{i}.
\]

\[
{df}\left( \alpha \right)  = {D}^{\prime \prime }f\left( \alpha \right)  = {\beta }_{0} + \mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\beta }_{i}.
\]

So

\[
f\left( {D\alpha }\right)  = {df}\left( \alpha \right) .
\]

The verification of Property (a) is easy, since if \( \alpha \) is a global form, then \( \alpha  = {\alpha }_{0} \) and

\[
f \circ  r\left( \alpha \right)  = f\left( \alpha \right)  = {\alpha }_{0} = \alpha .
\]

Property (b) follows from the fact that

\[
1 - r \circ  f = {DL} + {LD}.
\]

As its verification is straightforward and not very illuminating, we shall omit it. The skeptical reader may wish to carry it out for himself. Apart from the definitions, the only facts needed are Lemma 9.6 and the chain-homotopy formula (8.7).

REMARK. Actually the existence of the chain-homotopy inverse \( f \) and the homotopy operator \( L \) is guaranteed by a general principle in the theory of chain complexes (See Spanier [1, Ch. 4, Sec. 2; in particular, Cor. 11, p. 167]).

We can now give an explicit description of the various isomorphisms that follow from the generalized Mayer-Vietoris principle. For example, by applying the collating formula (9.5), we get

Proposition 9.8 (Explicit Isomorphism between de Rham and Čech). If \( \eta  \in \; {C}^{n}\left( {\mathfrak{U},\mathbb{R}}\right) \) is a Čech cocycle, then the global closed form corresponding to it is given by \( f\left( \eta \right)  = {\left( -1\right) }^{n}{\left( {D}^{\prime \prime }K\right) }^{n}\eta \) .

EXAMPLE 9.9. Let \( \mathfrak{U} \) be a good cover of the circle \( {S}^{1} \) . We shall construct from a generator of the Čech cohomology \( {H}^{1}\left( {\mathfrak{U},\mathbb{R}}\right) \) a differential form representing a generator of the de Rham cohomology \( {H}_{DR}^{1}\left( {S}^{1}\right) \) .

As we saw in Example 9.2, a nontrivial 1-cocycle on \( {S}^{1} \) is

\[
\eta  = \left( {{\eta }_{01},{\eta }_{02},{\eta }_{12}}\right)  = \left( {1,0,0}\right) .
\]

If \( \left\{  {\rho }_{\alpha }\right\} \) is a partition of unity, then

\[
{K\eta } = \left( {-{\rho }_{1},{\rho }_{0},0}\right) .
\]

So the generator \( - {D}^{\prime \prime }{K\eta } \) of \( {H}_{DR}^{1}\left( {S}^{1}\right) \) is represented by \( - d\left( {-{\rho }_{1}}\right) \) , a bump form on \( {U}_{0} \cap  {U}_{1} \) with total integral 1 .

Exercise 9.10. The real projective plane \( \mathbb{R}{P}^{2} \) is obtained by identifying the boundary of a disc as shown in Figure 9.5. Find a good cover for \( \mathbb{R}{P}^{2} \) and compute its de Rham cohomology from the combinatorics of the cover. One possible good cover has the nerve depicted in Figure 9.6.

![bo_d7b6f8alb0pc73dd9avg_115_620_543_400_402_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_115_620_543_400_402_0.jpg)

Figure 9.5

![bo_d7b6f8alb0pc73dd9avg_115_625_1192_395_455_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_115_625_1192_395_455_0.jpg)

Figure 9.6

Exercise 9.11. Let Figure 9.7 be the nerve of a good cover \( \mathfrak{U} \) on the torus, where the arrows indicate how the vertices are ordered. Write down a nontrivial 1-cocycle in \( {C}^{1}\left( {\mathfrak{U},\mathbb{R}}\right) \) .

## The Tic-Tac-Toe Proof of the Künneth Formula

We now apply the main theorems of the preceding section to give another proof of the Künneth formula. This proof, admittedly more involved in its construction than the Mayer-Vietoris argument of Section 5, is a prototype for the spectral sequence argument of Chapter III. It will also allow us to replace the requirement that \( M \) has a finite good cover by the slightly weaker hypothesis that \( F \) has finite-dimensional cohomology.

![bo_d7b6f8alb0pc73dd9avg_116_397_299_857_446_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_116_397_299_857_446_0.jpg)

Before commencing the proof we make some general remarks about a technique for studying maps. Let \( \pi  : E \rightarrow  M \) be a map of manifolds. A cover \( \mathfrak{U} \) on \( M \) induces a cover \( {\pi }^{-1}\mathfrak{U} \) on \( E \) , and we have the inclusions

\[
\pi \left\{  \begin{array}{l} E \leftarrow  \coprod {\pi }^{-1}{U}_{\alpha } \leftleftarrows  \coprod {\pi }^{-1}{U}_{\alpha \beta } \leftleftarrows  \cdots \\  M \leftarrow  \coprod {U}_{\alpha }\; \leftleftarrows  \cdots  \end{array}\right.
\]

In general \( {U}_{\alpha } \cap  {U}_{\beta } \neq  \phi \) is not equivalent to \( {\pi }^{-1}{U}_{\alpha } \cap  {\pi }^{-1}{U}_{\beta } \neq  \phi \) . However, if \( \pi \) is surjective, then the two statements are equivalent, so that in this case the combinatorics of the covers \( \mathfrak{U} \) and \( {\pi }^{-1}\mathfrak{U} \) are the same. The double complex of the inverse cover computes the cohomology of \( E \) , which can then be related to the cohomology of \( M \) , because the inverse cover comes from a cover on \( M \) . This idea will be systematically exploited throughout this chapter and the next.

A quick example of how the inverse cover \( {\pi }^{-1}\mathfrak{U} \) may be used to study maps is the following. Note that although the inverse image of a good cover is usually not a good cover, for a vector bundle \( \pi  : E \rightarrow  M \) the "goodness" of the cover is preserved. Since the de Rham cohomology is determined by the combinatorics of a good cover, this implies that

\[
{H}_{DR}^{ * }\left( E\right)  \simeq  {H}_{DR}^{ * }\left( M\right)
\]

Of course, this also follows from the homotopy axiom for the de Rham cohomology (Corollary 4.1.2.2).

Proposition 9.12 (Künneth Formula). If \( M \) and \( F \) are two manifolds and \( F \) has finite-dimensional cohomology, then the de Rham cohomology of the product \( M \times  F \) is

\[
{H}^{ * }\left( {M \times  F}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( F\right) .
\]

Proof. Let \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) be a good cover for \( M \) and \( \pi  : M \times  F \rightarrow  M \) the projection onto the first factor. Then \( {\pi }^{-1}\mathfrak{U} = \left\{  {{\pi }^{-1}{U}_{\alpha }}\right\} \) is some sort of a cover for \( E = M \times  F \) , though in general not a good cover. There is a natural map

![bo_d7b6f8alb0pc73dd9avg_117_710_439_220_213_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_117_710_439_220_213_0.jpg)

which pulls back differential forms on open sets. Choose a basis for \( {H}^{ * }\left( F\right) \) , say \( \left\{  \left\lbrack  {\omega }_{\alpha }\right\rbrack  \right\} \) , and choose differential forms \( {\omega }_{\alpha } \) representing them. These may be used to define a map of double complexes

![bo_d7b6f8alb0pc73dd9avg_117_665_792_317_216_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_117_665_792_317_216_0.jpg)

by

\[
{\pi }_{\mathfrak{u}}^{ * }\left( {\left\lbrack  {\omega }_{\alpha }\right\rbrack   \otimes  \phi }\right)  = {\rho }^{ * }{\omega }_{\alpha } \land  {\pi }^{ * }\phi
\]

where \( \rho \) is the projection on the fiber

![bo_d7b6f8alb0pc73dd9avg_117_725_1200_199_208_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_117_725_1200_199_208_0.jpg)

Since \( {H}^{ * }\left( F\right) \) is a vector space, \( {H}^{ * }\left( F\right)  \otimes  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) is a number of copies of \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) and the differential operator \( D \) on the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) induces an operator on \( {H}^{ * }\left( F\right)  \otimes  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) whose cohomology is

\[
{H}^{ * }\left( F\right)  \otimes  {H}_{D}\left\{  {{C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) }\right\}   = {H}^{ * }\left( F\right)  \otimes  {H}^{ * }\left( M\right) .
\]

Since the \( D \) -cohomology of \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) is \( {H}^{ * }\left( E\right) \) , if we can show that

![bo_d7b6f8alb0pc73dd9avg_117_676_1669_316_214_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_117_676_1669_316_214_0.jpg)

induces an isomorphism in \( D \) -cohomology, the Künneth formula will follow.

The proof now divides into two steps:

Step 1.

For a good cover \( \mathfrak{U} \) , the map \( {\pi }_{\mathfrak{U}}^{ * } \) induces an isomorphism in \( {H}_{d} \) of these complexes.

Step 2.

Whenever a homomorphism \( f : K \rightarrow  {K}^{\prime } \) of double complexes induces \( {\mathrm{H}}_{d} \) -isomorphism, it also induces \( {\mathrm{H}}_{D} \) -isomorphism. (By a homomorphism of double complexes, we mean a vector-space homomorphism which preserves bidegrees and commutes with \( d \) and \( \delta \) .)

Proof of STEP 1. The \( {p}^{\text{ th }} \) column \( {C}^{p}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) consists of forms on the \( \left( {p + 1}\right) \) -fold intersections \( \coprod  {\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) and \( {C}^{p}\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) consists of forms on \( \coprod  {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) . The \( d \) -cohomology of \( {C}^{p}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) is

(9.12.1)

\[
\prod {H}^{ * }\left( {{\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}}}\right)  \simeq  {H}^{ * }\left( F\right)  \otimes  \prod {H}^{ * }\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}}\right)
\]

the isomorphism being given by the wedge product of pullbacks. So \( {\pi }_{u}^{ * } \) induces an isomorphism of the \( d \) -cohomology of \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) and \( {H}^{ * }\left( F\right)  \otimes  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) . \)

Exercise 9.13. Give a proof of Step 2.

REMARK. This argument for the Künneth formula also proves the Leray-Hirsch theorem (5.11), but again instead of assuming that \( M \) has a finite good cover, we require the cohomology of \( F \) to be finite-dimensional. If both \( M \) and \( F \) have infinite-dimensional cohomology, the isomorphism in (9.12.1) may not be valid.

The following example shows that some sort of finiteness hypothesis is necessary for the Künneth formula or the Leray-Hirsch theorem to hold.

EXAMPLE 9.14 (Counterexample to the Künneth formula when both \( M \) and \( F \) have infinite-dimensional cohomology). Let \( M \) and \( F \) each be the set \( {\mathbb{Z}}^{ + } \) of all positive integers. Then

\[
{H}^{0}\left( {M \times  F}\right)  = \left\{  {\text{ square matrices of real numbers }\left( {a}_{ij}\right) , i, j \in  {\mathbb{Z}}^{ + }}\right\}  .
\]

But \( {H}^{0}\left( M\right)  \otimes  {H}^{0}\left( F\right) \) consists of finite sums of matrices \( \left( {a}_{ij}\right) \) of rank 1 . These two vector spaces are not equal, since a finite sum of matrices of rank 1 has finite rank, but \( {H}^{0}\left( {M \times  F}\right) \) contains matrices of infinite rank.
