## Chapter 1 What Is Curvature?

If you have spent some time studying modern differential geometry, with its intricate web of manifolds, submanifolds, vector fields, Lie derivatives, tensor fields, differential forms, orientations, and foliations, you might be forgiven for wondering what it all has to do with geometry. In most people's experience, geometry is concerned with properties such as distances, lengths, angles, areas, volumes, and curvature. These concepts, however, are often barely mentioned in typical beginning graduate courses in smooth manifold theory.

The purpose of this book is to introduce the theory of Riemannian manifolds: these are smooth manifolds equipped with Riemannian metrics (smoothly varying choices of inner products on tangent spaces), which allow one to measure geometric quantities such as distances and angles. This is the branch of differential geometry in which "geometric" ideas, in the familiar sense of the word, come to the fore. It is the direct descendant of Euclid's plane and solid geometry, by way of Gauss's theory of curved surfaces in space, and it is a dynamic subject of contemporary research.

The central unifying theme in current Riemannian geometry research is the notion of curvature and its relation to topology. This book is designed to help you develop both the tools and the intuition you will need for an in-depth exploration of curvature in the Riemannian setting. Unfortunately, as you will soon discover, an adequate development of curvature in an arbitrary number of dimensions requires a great deal of technical machinery, making it easy to lose sight of the underlying geometric content. To put the subject in perspective, therefore, let us begin by asking some very basic questions: What is curvature? What are some important theorems about it? In this chapter, we explore these and related questions in an informal way, without proofs. The "official" treatment of the subject begins in Chapter 2.

## The Euclidean Plane

To get a sense of the kinds of questions Riemannian geometers address and where these questions came from, let us look back at the very roots of our subject. The treatment of geometry as a mathematical subject began with Euclidean plane geometry, which you probably studied in secondary school. Its elements are points, lines, distances, angles, and areas; and its most fundamental relationship is congruence-two plane figures are congruent if one can be transformed into the other by a rigid motion of the plane, which is a bijective transformation from the plane to itself that preserves distances. Here are a couple of typical theorems.

Theorem 1.1 (Side-Side-Side). Two Euclidean triangles are congruent if and only if the lengths of their corresponding sides are equal.

Theorem 1.2 (Angle-Sum Theorem). The sum of the interior angles of a Euclidean triangle is \( \pi \) .

As trivial as they may seem, these theorems serve to illustrate two major types of results that permeate the study of geometry; in this book, we call them "classification theorems" and "local-to-global theorems."

The side-side-side (SSS) theorem is a classification theorem. Such a theorem tells us how to determine whether two mathematical objects are equivalent (under some appropriate equivalence relation). An ideal classification theorem lists a small number of computable invariants (whatever "small" may mean in a given context), and says that two objects are equivalent if and only if all of these invariants match. In this case the equivalence relation is congruence, and the invariants are the three side lengths.

The angle-sum theorem is of a different sort. It relates a local geometric property (angle measure) to a global property (that of being a three-sided polygon or triangle). Most of the theorems we study in this book are of this type, which, for lack of a better name, we call local-to-global theorems.

After proving the basic facts about points and lines and the figures constructed directly from them, one can go on to study other figures derived from the basic elements, such as circles. Two typical results about circles are given below; the first is a classification theorem, while the second is a local-to-global theorem. (It may not be obvious at this point why we consider the second to be a local-to-global theorem, but it will become clearer soon.)

Theorem 1.3 (Circle Classification Theorem). Two circles in the Euclidean plane are congruent if and only if they have the same radius.

Theorem 1.4 (Circumference Theorem). The circumference of a Euclidean circle of radius \( R \) is \( {2\pi R} \) .

If we want to continue our study of plane geometry beyond figures constructed from lines and circles, sooner or later we have to come to terms with other curves in the plane. An arbitrary curve cannot be completely described by one or two numbers such as length or radius; instead, the basic invariant is curvature, which is defined using calculus and is a function of position on the curve.

Formally, the curvature of a plane curve \( \gamma \) is defined to be \( \kappa \left( t\right)  = \left| {{\gamma }^{\prime \prime }\left( t\right) }\right| \) , the length of the acceleration vector, when \( \gamma \) is given a unit-speed parametrization. (Here and throughout this book, the word "curve" refers to a parametrized curve, not a set of points. Typically, a curve will be defined as a smooth function of a real variable \( t \) , with a prime representing an ordinary derivative with respect to \( t \) .)

![bo_d7dtff491nqc73eq8m7g_16_517_185_500_373_0.jpg](images/bo_d7dtff491nqc73eq8m7g_16_517_185_500_373_0.jpg)

Fig. 1.1: Osculating circle

Geometrically, the curvature has the following interpretation. Given a point \( p = \gamma \left( t\right) \) , there are many circles tangent to \( \gamma \) at \( p \) —namely, those circles whose velocity vector at \( p \) is the same as that of \( \gamma \) when both are given unit-speed parametrizations; these are the circles whose centers lie on the line that passes through \( p \) and is orthogonal to \( {\gamma }^{\prime }\left( p\right) \) . Among these circles, there is exactly one unit-speed parametrized circle whose acceleration vector at \( p \) is the same as that of \( \gamma \) ; it is called the osculating circle (Fig. 1.1). (If the acceleration of \( \gamma \) is zero, replace the osculating circle by a straight line, thought of as a "circle with infinite radius.") The curvature is then \( \kappa \left( t\right)  = 1/R \) , where \( R \) is the radius of the osculating circle. The larger the curvature, the greater the acceleration and the smaller the osculating circle, and therefore the faster the curve is turning. A circle of radius \( R \) has constant curvature \( \kappa  \equiv  1/R \) , while a straight line has curvature zero.

It is often convenient for some purposes to extend the definition of the curvature of a plane curve, allowing it to take on both positive and negative values. This is done by choosing a continuous unit normal vector field \( N \) along the curve, and assigning the curvature a positive sign if the curve is turning toward the chosen normal or a negative sign if it is turning away from it. The resulting function \( {\kappa }_{N} \) along the curve is then called the signed curvature.

Here are two typical theorems about plane curves.

Theorem 1.5 (Plane Curve Classification Theorem). Suppose \( \gamma \) and \( \widetilde{\gamma } : \left\lbrack  {a, b}\right\rbrack   \rightarrow \; {\mathbb{R}}^{2} \) are smooth, unit-speed plane curves with unit normal vector fields \( N \) and \( \widetilde{N} \) , and \( {\kappa }_{N}\left( t\right) ,{\kappa }_{\widetilde{N}}\left( t\right) \) represent the signed curvatures at \( \gamma \left( t\right) \) and \( \widetilde{\gamma }\left( t\right) \) , respectively. Then \( \gamma \) and \( \widetilde{\gamma } \) are congruent by a direction-preserving congruence if and only if \( {\kappa }_{N}\left( t\right)  = {\kappa }_{\widetilde{N}}\left( t\right) \) for all \( t \in  \left\lbrack  {a, b}\right\rbrack  . \)

Theorem 1.6 (Total Curvature Theorem). If \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  {\mathbb{R}}^{2} \) is a unit-speed simple closed curve such that \( {\gamma }^{\prime }\left( a\right)  = {\gamma }^{\prime }\left( b\right) \) , and \( N \) is the inward-pointing normal, then

\[
{\int }_{a}^{b}{\kappa }_{N}\left( t\right) {dt} = {2\pi }.
\]

The first of these is a classification theorem, as its name suggests. The second is a local-to-global theorem, since it relates the local property of curvature to the global (topological) property of being a simple closed curve. We will prove both of these theorems later in the book: the second will be derived as a consequence of a more general result in Chapter 9 (see Corollary 9.6); the proof of the first is left to Problem 9-12.

It is interesting to note that when we specialize to circles, these theorems reduce to the two theorems about circles above: Theorem 1.5 says that two circles are congruent if and only if they have the same curvature, while Theorem 1.6 says that if a circle has curvature \( \kappa \) and circumference \( C \) , then \( {\kappa C} = {2\pi } \) . It is easy to see that these two results are equivalent to Theorems 1.3 and 1.4. This is why it makes sense to regard the circumference theorem as a local-to-global theorem.

## Surfaces in Space

The next step in generalizing Euclidean geometry is to start working in three dimensions. After investigating the basic elements of "solid geometry"-points, lines, planes, polyhedra, spheres, distances, angles, surface areas, volumes-one is led to study more general curved surfaces in space (2-dimensional embedded subman-ifolds of \( {\mathbb{R}}^{3} \) , in the language of differential geometry). The basic invariant in this setting is again curvature, but it is a bit more complicated than for plane curves, because a surface can curve differently in different directions.

The curvature of a surface in space is described by two numbers at each point, called the principal curvatures. We will define them formally in Chapter 8, but here is an informal recipe for computing them. Suppose \( S \) is a surface in \( {\mathbb{R}}^{3}, p \) is a point in \( S \) , and \( N \) is a unit normal vector to \( S \) at \( p \) .

1. Choose a plane \( \Pi \) passing through \( p \) and parallel to \( N \) . The intersection of \( \Pi \) with a neighborhood of \( p \) in \( S \) is a plane curve \( \gamma  \subseteq  \Pi \) containing \( p \) (Fig. 1.2).

2. Compute the signed curvature \( {\kappa }_{N} \) of \( \gamma \) at \( p \) with respect to the chosen unit normal \( N \) .

3. Repeat this for all normal planes \( \Pi \) . The principal curvatures of \( S \) at \( p \) , denoted by \( {\kappa }_{1} \) and \( {\kappa }_{2} \) , are the minimum and maximum signed curvatures so obtained.

Although the principal curvatures give us a lot of information about the geometry of \( S \) , they do not directly address a question that turns out to be of paramount importance in Riemannian geometry: Which properties of a surface are intrinsic? Roughly speaking, intrinsic properties are those that could in principle be measured or computed by a 2-dimensional being living entirely within the surface. More precisely, a property of surfaces in \( {\mathbb{R}}^{3} \) is called intrinsic if it is preserved by isometries (maps from one surface to another that preserve lengths of curves).

To see that the principal curvatures are not intrinsic, consider the following two embedded surfaces \( {S}_{1} \) and \( {S}_{2} \) in \( {\mathbb{R}}^{3} \) (Figs. 1.3 and 1.4): \( {S}_{1} \) is the square in the \( {xy} \) - plane where \( 0 < x < \pi \) and \( 0 < y < \pi \) , and \( {S}_{2} \) is the half-cylinder \( \{ \left( {x, y, z}\right)  : z = \; \sqrt{1 - {y}^{2}},0 < x < \pi ,\left| y\right|  < 1\} \) . If we follow the recipe above for computing principal curvatures (using, say, the downward-pointing unit normal), we find that, since all planes intersect \( {S}_{1} \) in straight lines, the principal curvatures of \( {S}_{1} \) are \( {\kappa }_{1} = {\kappa }_{2} = 0 \) . On the other hand, it is not hard to see that the principal curvatures of \( {S}_{2} \) are \( {\kappa }_{1} = 0 \) and \( {\kappa }_{2} = 1 \) . However, the map taking \( \left( {x, y,0}\right) \) to \( \left( {x,\cos y,\sin y}\right) \) is a diffeomorphism from \( {S}_{1} \) to \( {S}_{2} \) that preserves lengths of curves, and is thus an isometry.

![bo_d7dtff491nqc73eq8m7g_18_487_186_558_518_0.jpg](images/bo_d7dtff491nqc73eq8m7g_18_487_186_558_518_0.jpg)

Fig. 1.2: Computing principal curvatures

![bo_d7dtff491nqc73eq8m7g_18_187_846_524_373_0.jpg](images/bo_d7dtff491nqc73eq8m7g_18_187_846_524_373_0.jpg)

![bo_d7dtff491nqc73eq8m7g_18_762_845_558_375_0.jpg](images/bo_d7dtff491nqc73eq8m7g_18_762_845_558_375_0.jpg)

Fig. 1.3: \( {S}_{1} \) Fig. 1.4: \( {S}_{2} \)

Even though the principal curvatures are not intrinsic, the great German mathematician Carl Friedrich Gauss made the surprising discovery in 1827 [Gau65] that a particular combination of them is intrinsic. (See also [Spi79, Vol. 2] for an excellent discussion of the details of Gauss's paper.) He found a proof that the product \( K = {\kappa }_{1}{\kappa }_{2} \) , now called the Gaussian curvature, is intrinsic. He thought this result was so amazing that he named it Theorema Egregium. (This does not mean "totally awful theorem" as its English cognate egregious might suggest; a better translation into modern colloquial English might be "totally awesome theorem.")

![bo_d7dtff491nqc73eq8m7g_19_290_208_355_191_0.jpg](images/bo_d7dtff491nqc73eq8m7g_19_290_208_355_191_0.jpg)

Fig. 1.5: \( K > 0 \)

![bo_d7dtff491nqc73eq8m7g_19_867_193_353_205_0.jpg](images/bo_d7dtff491nqc73eq8m7g_19_867_193_353_205_0.jpg)

Fig. 1.6: \( K < 0 \)

To get a feeling for what Gaussian curvature tells us about surfaces, let us look at a few examples. Simplest of all is any surface that is an open subset of a plane: as we have seen, such a surface has both principal curvatures equal to zero and therefore has constant Gaussian curvature equal to zero. The half-cylinder described above also has \( K = {\kappa }_{1}{\kappa }_{2} = 0 \cdot  1 = 0 \) , as the Theorema Egregium tells us it must, being isometric to a square. Another simple example is a sphere of radius \( R \) . Every normal plane intersects the sphere in a great circle, which has radius \( R \) and therefore curvature \( \pm  1/R \) (with the sign depending on whether we choose the outward-pointing or inward-pointing normal). Thus the principal curvatures are both equal to \( \pm  1/R \) , and the Gaussian curvature is \( {\kappa }_{1}{\kappa }_{2} = 1/{R}^{2} \) . Note that while the signs of the principal curvatures depend on the choice of unit normal, the Gaussian curvature does not: it is always positive on the sphere.

Similarly, any surface that is "bowl-shaped" or "dome-shaped" has positive Gaussian curvature (Fig. 1.5), because the two principal curvatures always have the same sign, regardless of which normal is chosen. On the other hand, the Gaussian curvature of any surface that is "saddle-shaped" (Fig. 1.6) is negative, because the principal curvatures are of opposite signs.

The model spaces of surface theory are the surfaces with constant Gaussian curvature. We have already seen two of them: the Euclidean plane \( {\mathbb{R}}^{2}\left( {K = 0}\right) \) , and the sphere of radius \( R\left( {K = 1/{R}^{2}}\right) \) . The most important model surface with constant negative Gaussian curvature is called the hyperbolic plane, and will be defined in Chapter 3. It is not so easy to visualize because it cannot be realized globally as a smoothly embedded surface in \( {\mathbb{R}}^{3} \) (see [Spi79, Vol. 3, pp. 373-385] for a proof).

Surface theory is a highly developed branch of geometry. Of all its results, two-a classification theorem and a local-to-global theorem-are generally acknowledged as the most important.

Theorem 1.7 (Uniformization Theorem). Every connected 2-manifold is diffeomorphic to a quotient of one of the constant-curvature model surfaces described above by a discrete group of isometries without fixed points. Thus every connected 2-manifold has a complete Riemannian metric with constant Gaussian curvature.

Theorem 1.8 (Gauss-Bonnet Theorem). Suppose \( S \) is a compact Riemannian 2- manifold. Then

\[
{\int }_{S}{KdA} = {2\pi \chi }\left( S\right)
\]

where \( \chi \left( S\right) \) is the Euler characteristic of \( S \) .

The uniformization theorem is a classification theorem, because it replaces the problem of classifying surfaces with that of classifying certain discrete groups of isometries of the models. The latter problem is not easy by any means, but it sheds a great deal of new light on the topology of surfaces nonetheless. In Chapter 3, we sketch a proof of the uniformization theorem for the case of compact surfaces.

Although stated here as a geometric-topological result, the uniformization theorem is usually stated somewhat differently and proved using complex analysis. If you are familiar with complex analysis and the complex version of the uniformization theorem, it will be an enlightening exercise after you have finished this book to prove that the complex version of the theorem is equivalent to the one stated here.

The Gauss-Bonnet theorem, on the other hand, is purely a theorem of differential geometry, arguably the most fundamental and important one of all. It relates a local geometric property (the curvature) with a global topological invariant (the Euler characteristic). We give a detailed proof in Chapter 9.

Taken together, these theorems place strong restrictions on the types of metrics that can occur on a given surface. For example, one consequence of the Gauss-Bonnet theorem is that the only compact, connected, orientable surface that admits a metric of strictly positive Gaussian curvature is the sphere. On the other hand, if a compact, connected, orientable surface has nonpositive Gaussian curvature, the Gauss-Bonnet theorem rules out the sphere, and then the uniformization theorem tells us that its universal covering space is topologically equivalent to the plane.

## Curvature in Higher Dimensions

We end our survey of the basic ideas of Riemannian geometry by mentioning briefly how curvature appears in higher dimensions. Suppose \( M \) is an \( n \) -dimensional Riemannian manifold. As with surfaces, the basic geometric invariant is curvature, but curvature becomes a much more complicated quantity in higher dimensions because a manifold may curve in so many different directions.

The first problem we must contend with is that, in general, Riemannian manifolds are not presented to us as embedded submanifolds of Euclidean space. Therefore, we must abandon the idea of cutting out curves by intersecting our manifold with planes, as we did when defining the principal curvatures of a surface in \( {\mathbb{R}}^{3} \) . Instead, we need a more intrinsic way of sweeping out submanifolds. Fortunately, geodesics-curves that are the shortest paths between nearby points-are readymade tools for this and many other purposes in Riemannian geometry. Examples are straight lines in Euclidean space and great circles on a sphere.

The most fundamental fact about geodesics, which we prove in Chapter 4, is that given any point \( p \in  M \) and any vector \( v \) tangent to \( M \) at \( p \) , there is a unique geodesic starting at \( p \) with initial velocity \( v \) .

Here is a brief recipe for computing some curvatures at a point \( p \in  M \) .

1. Choose a 2-dimensional subspace \( \Pi \) of the tangent space to \( M \) at \( p \) .

2. Look at all the geodesics through \( p \) whose initial velocities lie in the selected plane \( \Pi \) . It turns out that near \( p \) these sweep out a certain 2-dimensional sub-manifold \( {S}_{\Pi } \) of \( M \) , which inherits a Riemannian metric from \( M \) .

3. Compute the Gaussian curvature of \( {S}_{\Pi } \) at \( p \) , which the Theorema Egregium tells us can be computed from the Riemannian metric that \( {S}_{\Pi } \) inherits from \( M \) . This gives a number, denoted by \( \sec \left( \Pi \right) \) , called the sectional curvature of \( M \) at \( p \) associated with the plane \( \Pi \) .

Thus the "curvature" of \( M \) at \( p \) has to be interpreted as a map

\[
\text{ sec: }\left\{  {2\text{ -planes in }{T}_{p}M}\right\}   \rightarrow  \mathbb{R}\text{ . }
\]

As we will see in Chapter 3, we again have three classes of constant (sectional) curvature model spaces: \( {\mathbb{R}}^{n} \) with its Euclidean metric (for which sec \( \equiv  0 \) ); the \( n \) - sphere of radius \( R \) , with the Riemannian metric inherited from \( {\mathbb{R}}^{n + 1} \) (sec \( \equiv  1/{R}^{2} \) ); and hyperbolic space of radius \( R \) (with sec \( \equiv   - 1/{R}^{2} \) ). Unfortunately, however, there is as yet no satisfactory uniformization theorem for Riemannian manifolds in higher dimensions. In particular, it is definitely not true that every manifold possesses a metric of constant sectional curvature. In fact, the constant-curvature metrics can all be described rather explicitly by the following classification theorem.

Theorem 1.9 (Characterization of Constant-Curvature Metrics). The complete, connected, n-dimensional Riemannian manifolds of constant sectional curvature are, up to isometry, exactly the Riemannian quotients of the form \( \widetilde{M}/\Gamma \) , where \( \widetilde{M} \) is a Euclidean space, sphere, or hyperbolic space with constant sectional curvature, and \( \Gamma \) is a discrete group of isometries of \( \widetilde{M} \) that acts freely on \( \widetilde{M} \) .

On the other hand, there are a number of powerful local-to-global theorems, which can be thought of as generalizations of the Gauss-Bonnet theorem in various directions. They are consequences of the fact that positive curvature makes geodesics converge, while negative curvature forces them to spread out. Here (in somewhat simplified form) are two of the most important such theorems.

Theorem 1.10 (Cartan-Hadamard). Suppose \( M \) is a complete, connected Riemannian n-manifold with all sectional curvatures less than or equal to zero. Then the universal covering space of \( M \) is diffeomorphic to \( {\mathbb{R}}^{n} \) .

Theorem 1.11 (Myers). Suppose \( M \) is a complete, connected Riemannian manifold with all sectional curvatures bounded below by a positive constant. Then \( M \) is compact and has a finite fundamental group.

Looking back at the remarks concluding the section on surfaces above, you can see that these last three theorems generalize some of the consequences of the uniformization and Gauss-Bonnet theorems, although not their full strength. It is the primary goal of this book to prove Theorems 1.9, 1.10, and 1.11, among others; it is a primary goal of current research in Riemannian geometry to improve upon them and further generalize the results of surface theory to higher dimensions.
