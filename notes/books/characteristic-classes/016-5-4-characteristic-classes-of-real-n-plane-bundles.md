# 5.4 Characteristic Classes of Real \( n \) -Plane Bundles

Using Theorems 5.6 and 5.7, it is possible to give a precise definition of the concept of characteristic class. First observe the following.

Corollary 5.10. Any \( {\mathbb{R}}^{n} \) -bundle \( \xi \) over a paracompact space \( B \) determines a unique homotopy class of maps

\[
{\bar{f}}_{\xi } : B \rightarrow  {\mathrm{{Gr}}}_{n}
\]

Proof. Let \( {f}_{\xi } : \xi  \rightarrow  {\gamma }^{n} \) be any bundle map, and let \( {\bar{f}}_{\xi } \) be the induced map of base spaces.

Now let \( \Lambda \) be a coefficient group or ring and let

\[
c \in  {\mathrm{H}}^{i}\left( {{\mathrm{{Gr}}}_{n};\Lambda }\right)
\]

be any cohomology class. Then \( \xi \) and \( c \) together determine a cohomology class

\[
{\bar{f}}_{\xi }^{ * }c \in  {\mathrm{H}}^{i}\left( {B;\Lambda }\right) .
\]

This class will be denoted briefly by \( c\left( \xi \right) \) .

Definition. \( c\left( \xi \right) \) is called the characteristic cohomology class of \( \xi \) determined by \( c \) .

Note that the correspondence \( \xi  \mapsto  c\left( \xi \right) \) is natural with respect to bundle maps. (Compare Axiom 2 in §4.) Conversely, given any correspondence

\[
\xi  \mapsto  c\left( \xi \right)  \in  {\mathrm{H}}^{i}\left( {B\left( \xi \right) ;\Lambda }\right)
\]

which is natural with respect to bundle maps, we have

\[
c\left( \xi \right)  = {\bar{f}}_{\xi }^{ * }c\left( {\gamma }^{n}\right) .
\]

Thus the above construction is the most general one. Briefly speaking: The ring consisting of all characteristic cohomology classes for \( {\mathbb{R}}^{n} \) -bundles over paracompact base spaces with coefficient ring \( \Lambda \) is canonically isomorphic to the cohomology ring \( {\mathrm{H}}^{ \bullet  }\left( {{\mathrm{{Gr}}}_{n};\Lambda }\right) \) .

These constructions emphasize the importance of computing the cohomology of the space \( {\mathrm{{Gr}}}_{n} \) . The next two sections will give one procedure for computing this cohomology, at least modulo 2.

Remark 6. Using the "covering homotopy theorem" (compare [Dol95], [Hus94]), Corollary 5.10 can be sharpened as follows: Two \( {\mathbb{R}}^{n} \) -bundles \( \xi \) and \( \eta \) over the paracompact space \( B \) are isomorphic if and only if the mapping \( {\bar{f}}_{\xi } \) of 5.10 is homotopic to \( {\bar{f}}_{\eta } \) .

Here are five problems for the reader.

Problem 5-A. Show that the Grassmann manifold \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) can be made into a smooth manifold as follows: a function \( f : {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right)  \rightarrow  \mathbb{R} \) belongs to the collection \( F \) of smooth real valued functions if and only if \( f \circ  q : {V}_{n}\left( {\mathbb{R}}^{n + k}\right)  \rightarrow  \mathbb{R} \) is smooth.

Problem 5-B. Show that the tangent bundle of \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is isomorphic to \( \operatorname{Hom}\left( {{\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) ,{\gamma }^{ \bot  }}\right) \) ; where \( {\gamma }^{ \bot  } \) denotes the orthogonal complement of \( {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right) \) in \( {\varepsilon }^{n + k} \) . Now consider a smooth manifold \( M \subset  {\mathbb{R}}^{n + k} \) . If \( \bar{g} : M \rightarrow  {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) denotes the generalized Gauss map, show that

\[
\mathrm{d}\bar{g} : \mathbf{T}M \rightarrow  \mathbf{T}\left( {{\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) }\right)
\]

gives rise to a cross-section of the bundle

\[
\operatorname{Hom}\left( {{\tau }_{M},\operatorname{Hom}\left( {{\tau }_{M},\nu }\right) }\right)  \cong  \operatorname{Hom}\left( {{\tau }_{M} \otimes  {\tau }_{M},\nu }\right) .
\]

(The cross-section is called the second fundamental form of \( M \) .)

Problem 5-C. Show that \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) is diffeomorphic to the smooth manifold consisting of all \( m \times  m \) symmetric, idempotent matrices of trace \( n \) . Alternatively show that the map

\[
\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mapsto  {x}_{1} \land  \ldots  \land  {x}_{n}
\]

from \( {\mathrm{V}}_{n}\left( {\mathbb{R}}^{m}\right) \) to the exterior power \( {\Lambda }^{n}\left( {\mathbb{R}}^{m}\right) \) gives rise to a smooth embedding of \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{m}\right) \) in the projective space \( {\operatorname{Gr}}_{1}\left( {{\Lambda }^{n}\left( {\mathbb{R}}^{m}\right) }\right)  \cong  {\mathbb{P}}^{\left( \begin{matrix} m \\  n \end{matrix}\right)  - 1} \) . (Compare [Ped39,§7])

Problem 5-D. Show that \( {\mathrm{{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) has the following symmetry property. Given any two \( n \) -planes \( X, Y \subset  {\mathbb{R}}^{n + k} \) there exists an orthogonal automorphism of \( {\mathbb{R}}^{n + k} \) which interchanges \( X \) and \( Y \) . [Whi61] defines the angle \( \alpha \left( {X, Y}\right) \) between \( n \) -planes as the maximum over all unit vectors \( x \in  X \) of the angle between \( x \) and \( Y \) . Show that \( \alpha \) is a metric for the topological space \( {\operatorname{Gr}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) and show that

\[
\alpha \left( {X, Y}\right)  = \alpha \left( {{Y}^{ \bot  },{X}^{ \bot  }}\right) .
\]

Problem 5-E. Let \( \xi \) be an \( {\mathbb{R}}^{n} \) -bundle over \( B \) .

1) Show that there exists a vector bundle \( \eta \) over \( B \) with \( \xi  \oplus  \eta \) trivial if and only if there exists a bundle map

\[
\xi  \rightarrow  {\gamma }^{n}\left( {\mathbb{R}}^{n + k}\right)
\]

for large \( k \) . If such a map exists, \( \xi \) will be called a bundle of finite type.

2) Now assume that \( B \) is normal. Show that \( \xi \) has finite type if and only if \( B \) is covered by finitely many open sets \( {U}_{1},\ldots ,{U}_{r} \) with \( {\left. \xi \right| }_{{U}_{i}} \) trivial.

3) If \( B \) is paracompact and has finite covering dimension, show (using the argument of 5.3) that every \( \xi \) over \( B \) has finite type.

4) Using Stiefel-Whitney classes, show that the vector bundle \( {\gamma }^{1} \) over \( {\mathbb{P}}^{\infty } \) does not have finite type.
