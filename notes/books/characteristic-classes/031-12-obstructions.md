# 12 Obstructions

In the original work of Stiefel and Whitney, characteristic classes were defined as obstructions to the existence of certain fields of linearly independent vectors. A careful exposition from this point of view is given in [Ste51, §25.6, 35 and 38]. The construction can be outlined roughly as follows.

Let \( \xi \) be an \( n \) -plane bundle with base space \( B \) . For each fiber \( F \) of \( \xi \) consider the Stiefel manifold \( {\mathrm{V}}_{k}\left( F\right) \) consisting of all \( k \) -frames in \( F \) . Here by a \( k \) -frame we mean simply a \( k \) -tuple \( \left( {{v}_{1},\ldots ,{v}_{k}}\right) \) of linearly independent vectors of \( F \) ; where \( 1 \leq \; k \leq  n \) . (Compare \( \text{ § }5 \) . Steenrod uses orthonormal \( k \) -frames, but this modification does not affect the argument). These manifolds \( {\mathrm{V}}_{k}\left( F\right) \) can be considered as the fibers of a new fiber bundle which we will denote by \( {\mathrm{V}}_{k}\left( \xi \right) \) and call the associated Stiefel manifold bundle over \( B \) . By definition, the total space of \( {\mathrm{V}}_{k}\left( \xi \right) \) consists of all pairs \( \left( {x,\left( {{v}_{1},\ldots ,{v}_{k}}\right) }\right) \) where \( x \) is a point of \( B \) and \( \left( {{v}_{1},\ldots ,{v}_{k}}\right) \) is a \( k \) -frame in the fiber \( {F}_{x} \) over \( x \) . Note that a cross-section of this Stiefel manifold bundle is nothing but a \( k \) -tuple of linearly independent cross-sections of the vector bundle \( \xi \) .

Now suppose that the base space \( B \) is a CW-complex. \( {}^{1} \) As an example, if the base space is a smooth paracompact manifold then according to J. H. C. Whitehead it possesses a smooth triangulation, and hence can certainly be given the structure of a CW-complex. (Compare [Mun00].)

Steenrod shows that the fiber \( {\mathrm{V}}_{k}\left( F\right) \) is \( \left( {n - k - 1}\right) \) -connected, so it is easy to construct a cross-section of \( {\mathrm{V}}_{k}\left( \xi \right) \) over the \( \left( {n - k}\right) \) -skeleton of \( B \) . There exists a cross-section over the \( \left( {n - k + 1}\right) \) -skeleton of \( B \) if and only if a certain well defined primary obstruction class in

\[
{\mathrm{H}}^{n - k + 1}\left( {B;\left\{  {{\pi }_{n - k}{\mathrm{\;V}}_{k}\left( F\right) }\right\}  }\right)
\]

---

\( {}^{1} \) Steenrod considers only the case of a finite cell complex but it is useful, and not much more difficult, to allow arbitrary CW-complexes.

---

is zero. Here we are using cohomology with local coefficients. The notation \( \left\{  {{\pi }_{n - k}{\mathrm{\;V}}_{k}\left( F\right) }\right\} \) is used to denote the system of local coefficients (= bundle of abelian groups) which associates to each point \( x \) of \( B \) the coefficient group \( {\pi }_{n - k}{\mathrm{\;V}}_{k}\left( {F}_{x}\right) \) . (In the special case \( n - k = 0,{\pi }_{0}X \) is defined to be the reduced singular group \( {\widetilde{\mathrm{H}}}_{0}\left( {X;\mathbb{Z}}\right) \) .)

Setting \( j = n - k + 1 \) , we will use the notation

\[
{\mathfrak{o}}_{j}\left( \xi \right)  \in  {\mathrm{H}}^{j}\left( {B;\left\{  {{\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) }\right\}  }\right)
\]

for this primary obstruction class. If \( j \) is even, and less than \( n \) , then Steenrod shows that the coefficient group \( {\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) \) is cyclic of order 2 . Hence it is canonically isomorphic to \( \mathbb{Z}/2 \) . If \( j \) is odd, or \( j = n \) , the group \( {\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) \) is infinite cyclic. However it is not canonically isomorphic to \( \mathbb{Z} \) . The system of local coefficients \( \left\{  {{\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) }\right\} \) is twisted in general.

In any case, there is certainly a unique non-trivial homomorphism \( h \) from \( {\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) \) to \( \mathbb{Z}/2 \) . Hence we can reduce the coefficients modulo 2, obtaining an induced cohomology class \( {h}_{ * }{\mathfrak{o}}_{j}\left( \xi \right)  \in  {\mathrm{H}}^{j}\left( {B;\mathbb{Z}/2}\right) \) .

Theorem 12.1. This reduction modulo 2 of the obstruction class \( {\mathfrak{o}}_{j}\left( \xi \right) \) is equal to the Stiefel-Whitney class \( {\mathrm{w}}_{j}\left( \xi \right) \) .

Proof. First consider the universal bundle \( {\gamma }^{n} \) over \( {\mathrm{{Gr}}}_{n} = {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{\infty }\right) \) . Since \( {\mathrm{H}}^{ * }\left( {{\mathrm{{Gr}}}_{n};\mathbb{Z}/2}\right) \) is a polynomial algebra on generators \( {\mathrm{w}}_{1}\left( {\gamma }^{n}\right) ,\ldots ,{\mathrm{w}}_{n}\left( {\gamma }^{n}\right) \) , it follows that

\[
{h}_{ * }{\mathfrak{o}}_{j}\left( {\gamma }^{n}\right)  = {f}_{j}\left( {{\mathrm{\;w}}_{1}\left( {\gamma }^{n}\right) ,\ldots ,{\mathrm{w}}_{n}\left( {\gamma }^{n}\right) }\right)
\]

for some polynomial \( {f}_{j} \) in \( n \) variables. Since both the obstruction class and the Stiefel-Whitney classes are natural with respect to bundle mappings (see [Ste51, §35.7]), it follows that

\[
{h}_{ * }{\mathfrak{o}}_{j}\left( \xi \right)  = {f}_{j}\left( {{\mathrm{\;w}}_{1}\left( \xi \right) ,\ldots ,{\mathrm{w}}_{n}\left( \xi \right) }\right)
\]

for any \( n \) -plane bundle \( \xi \) over a CW-complex.

Since \( {f}_{j}\left( {{\mathrm{w}}_{1},\ldots ,{\mathrm{w}}_{n}}\right) \) is a cohomology class of dimension \( j \leq  n \) , the polynomial \( {f}_{j} \) can certainly be written uniquely as a sum

\[
{f}_{j}\left( {{\mathrm{w}}_{1},\ldots ,{\mathrm{w}}_{n}}\right)  = {f}^{\prime }\left( {{\mathrm{w}}_{1},\ldots ,{\mathrm{w}}_{j - 1}}\right)  + \lambda {\mathrm{w}}_{j}
\]

where \( {f}^{\prime } = {f}_{j, n}^{\prime } \) is a polynomial and \( \lambda  = {\lambda }_{j, n} \) equals 0 or 1 .

To compute \( {f}^{\prime } \) , consider the \( n \) -plane bundle \( \eta  = {\gamma }^{j - 1} \oplus  {\varepsilon }^{n - j + 1} \) over \( {\operatorname{Gr}}_{j - 1} \) , where \( {\varepsilon }^{n - j + 1} \) is a trivial bundle. This bundle \( \eta \) admits \( n - j + 1 \) linearly independent cross-sections, so the obstruction class

\[
{\mathfrak{o}}_{j}\left( \eta \right)  \in  {\mathrm{H}}^{j}\left( {B;\left\{  {{\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) }\right\}  }\right)
\]

must be zero. Therefore the mod 2 class

\[
{h}_{ * }{\mathfrak{o}}_{j}\left( \eta \right)  = {f}^{\prime }\left( {{\mathrm{w}}_{1}\left( \eta \right) ,\ldots ,{\mathrm{w}}_{j - 1}\left( \eta \right) }\right)  + \lambda {\mathrm{w}}_{j}\left( \eta \right)
\]

\[
= {f}^{\prime }\left( {{\mathrm{w}}_{1}\left( {\gamma }^{j - 1}\right) ,\ldots ,{\mathrm{w}}_{j - 1}\left( {\gamma }^{j - 1}\right) }\right)  + 0
\]

is equal to zero. Since the classes \( {\mathrm{w}}_{1}\left( {\gamma }^{j - 1}\right) ,\ldots ,{\mathrm{w}}_{j - 1}\left( {\gamma }^{j - 1}\right) \) are algebraically independent, this proves that \( {f}^{\prime } = 0 \) . Thus

\[
{h}_{ * }{\mathfrak{o}}_{j}\left( \xi \right)  = \lambda {\mathrm{w}}_{j}\left( \xi \right)
\]

for any \( n \) -plane bundle \( \xi \) .

To prove that \( \lambda  = {\lambda }_{j, n} \) is equal to 1, first consider the case \( j = n \) . Let \( \xi  = {\gamma }_{1}^{n} \) be the restriction of the universal bundle \( {\gamma }^{n} \) to the Grassmann manifold \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + 1}\right) \) of \( n \) -planes in \( \left( {n + 1}\right) \) -space. Identifying \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + 1}\right) \) with the real projective space \( {\mathbb{P}}^{n} \) as in 5.1, this bundle \( {\gamma }_{1}^{n} \) can be described as follows. Corresponding to each pair of antipodal points \( \{ u, - u\} \) on the unit sphere \( {S}^{n} \) one associates the fiber consisting of all vectors \( v \) in \( {\mathbb{R}}^{n + 1} \) with \( u \cdot  v = 0 \)

A cross-section of \( {\gamma }_{1}^{n} \) which is non-zero except at a single point \( \left\{  {{u}_{0}, - {u}_{0}}\right\} \) of \( {\mathbb{P}}^{n} \) is given by the formula \( \{ u, - u\}  \mapsto  {u}_{0} - \left( {{u}_{0} \cdot  u}\right) u \) .

Now choosing the point \( {u}_{0} \) in the middle of the \( n \) -dimensional cell of \( {\mathbb{P}}^{n} \) (compare \( \text{ § }{6.5} \) ), we have a cross-section of \( {\mathrm{V}}_{1}\left( {\gamma }_{1}^{n}\right) \) over the \( \left( {n - 1}\right) \) -skeleton, and the obstruction cocycle clearly assigns to the \( n \) -cell a generator of the cyclic group

\[
{\pi }_{n - 1}{\mathrm{\;V}}_{1}F = {\pi }_{n - 1}\left( {F - 0}\right)  \cong  \mathbb{Z}.
\]

![bo_d7du9galb0pc73deir9g_147_654_265_380_405_0.jpg](images/bo_d7du9galb0pc73deir9g_147_654_265_380_405_0.jpg)

Figure 9

Thus \( {h}_{ * }{\mathfrak{o}}_{n}\left( {\gamma }_{1}^{n}\right)  \neq  0 \) , so the coefficient \( {\lambda }_{n, n} \) must be equal to 1 .

The proof for \( j < n \) is completely analogous. One uses the vector bundle \( {\gamma }_{1}^{j} \oplus  {\varepsilon }^{n - j} \) over \( {\operatorname{Gr}}_{j}\left( {\mathbb{R}}^{j + 1}\right)  \cong  {\mathbb{P}}^{j} \) , together with the description of the generator of the group \( {\pi }_{j - 1}{v}_{n - j + 1}\left( {\mathbb{R}}^{n}\right) \) which is given [Ste51,§25.6].

Remark. Closely related to the obstruction point of view is a curious description of the Stiefel-Whitney classes of a manifold \( M \) which was conjectured by Stiefel and first proved by Whitney. Choosing any smooth triangulation of \( M \) , the sum of all simplices in the first barycentric subdivision is a mod 2 cycle, representing the homology class \( \mathrm{w} \cap  \mu \) which is Poincaré dual to the total Stiefel-Whitney class of \( {\tau }_{M} \) . A proof of this result has recently been published by [HT72].

If we are given the Stiefel-Whitney classes \( {\mathrm{w}}_{j}\left( \xi \right) \) of an \( n \) -plane bundle, to what extent is it possible to reconstruct the obstruction classes \( {\mathfrak{o}}_{j}\left( \xi \right) \) ? If \( j = {2i} \) is even and less than \( n \) , then the coefficient group \( {\pi }_{j - 1}{\mathrm{\;V}}_{n - j + 1}\left( F\right) \) has order 2, so we can write

\[
{\mathfrak{o}}_{2i}\left( \xi \right)  = {\mathrm{w}}_{2i}\left( \xi \right) \;\text{ for }\;{2i} < n,
\]

without any danger of ambiguity. Furthermore, according to [Ste51, §38.8], the class \( {\mathfrak{o}}_{{2i} + 1}\left( \xi \right) \) can be expressed as the image \( {\delta }^{ * }{\mathfrak{o}}_{2i}\left( \xi \right) \) where \( {\delta }^{ * } \) is a suitably defined cohomology operation. Thus the obstruction classes \( {\mathfrak{o}}_{j}\left( \xi \right) \) with \( j \) odd or \( j < n \) are completely determined by the Stiefel-Whitney classes of \( \xi \) .

![bo_d7du9galb0pc73deir9g_148_582_374_403_401_0.jpg](images/bo_d7du9galb0pc73deir9g_148_582_374_403_401_0.jpg)

Figure 10

We will show that the highest obstruction class \( {\mathfrak{o}}_{n}\left( \xi \right) \) can be identified with the Euler class \( \mathrm{e}\left( \xi \right) \) , provided that \( \xi \) is oriented. We will make use of two important constructions in the proof.
