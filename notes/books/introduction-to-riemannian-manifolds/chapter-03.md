## Chapter 3 Model Riemannian Manifolds

Before we delve into the general theory of Riemannian manifolds, we pause to give it some substance by introducing a variety of "model Riemannian manifolds" that should help to motivate the general theory. These manifolds are distinguished by having a high degree of symmetry.

We begin by describing the most symmetric model spaces of all-Euclidean spaces, spheres, and hyperbolic spaces. We analyze these in detail, and prove that each one has a very large isometry group: not only is there an isometry taking any point to any other point, but in fact one can find an isometry taking any orthonormal basis at one point to any orthonormal basis at any other point. As we will see in Chapter 8, this has strong consequences for the curvatures of these manifolds.

After introducing these very special models, we explore some more general classes of Riemannian manifolds with symmetry-the invariant metrics on Lie groups, homogeneous spaces, and symmetric spaces.

At the end of the chapter, we give a brief introduction to some analogous models in the pseudo-Riemannian case. For the particular case of Lorentz manifolds, these are the Minkowski spaces, de Sitter spaces, and anti-de Sitter spaces, which are important model spaces in general relativity.

## Symmetries of Riemannian Manifolds

The main feature of the Riemannian manifolds we are going to introduce in this chapter is that they are all highly symmetric, meaning that they have large groups of isometries.

Let \( \left( {M, g}\right) \) be a Riemannian manifold. Recall that Iso \( \left( {M, g}\right) \) denotes the set of all isometries from \( M \) to itself, which is a group under composition. We say that \( \left( {M, g}\right) \) is a homogeneous Riemannian manifold if \( \operatorname{Iso}\left( {M, g}\right) \) acts transitively on \( M \) , which is to say that for each pair of points \( p, q \in  M \) , there is an isometry \( \varphi  : M \rightarrow  M \) such that \( \varphi \left( p\right)  = q \) .

The isometry group does more than just act on \( M \) itself. For every \( \varphi  \in  \operatorname{Iso}\left( {M, g}\right) \) , the global differential \( {d\varphi } \) maps \( {TM} \) to itself and restricts to a linear isometry \( d{\varphi }_{p} : {T}_{p}M \rightarrow  {T}_{\varphi \left( p\right) }M \) for each \( p \in  M \) .

Given a point \( p \in  M \) , let \( {\operatorname{Iso}}_{p}\left( {M, g}\right) \) denote the isotropy subgroup at \( p \) , that is, the subgroup of \( \operatorname{Iso}\left( {M, g}\right) \) consisting of isometries that fix \( p \) . For each \( \varphi  \in \; {\operatorname{Iso}}_{p}\left( {M, g}\right) \) , the linear map \( d{\varphi }_{p} \) takes \( {T}_{p}M \) to itself, and the map \( {I}_{p} : {\operatorname{Iso}}_{p}\left( {M, g}\right)  \rightarrow \; \mathrm{{GL}}\left( {{T}_{p}M}\right) \) given by \( {I}_{p}\left( \varphi \right)  = d{\varphi }_{p} \) is a representation of \( {\operatorname{Iso}}_{p}\left( {M, g}\right) \) , called the isotropy representation. We say that \( M \) is isotropic at \( p \) if the isotropy representation of \( {\operatorname{Iso}}_{p}\left( {M, g}\right) \) acts transitively on the set of unit vectors in \( {T}_{p}M \) . If \( M \) is isotropic at every point, we say simply that \( M \) is isotropic.

There is an even stronger kind of symmetry than isotropy. Let \( \mathrm{O}\left( M\right) \) denote the set of all orthonormal bases for all tangent spaces of \( M \) :

\[
\mathrm{O}\left( M\right)  = \mathop{\coprod }\limits_{{p \in  M}}\{ \text{ orthonormal bases for }{T}_{p}M\} .
\]

There is an induced action of \( \operatorname{Iso}\left( {M, g}\right) \) on \( \mathrm{O}\left( M\right) \) , defined by using the differential of an isometry \( \varphi \) to push an orthonormal basis at \( p \) forward to an orthonormal basis at \( \varphi \left( p\right) \) :

\[
\varphi  \cdot  \left( {{b}_{1},\ldots ,{b}_{n}}\right)  = \left( {d{\varphi }_{p}\left( {b}_{1}\right) ,\ldots , d{\varphi }_{p}\left( {b}_{n}\right) }\right) . \tag{3.1}
\]

We say that \( \left( {M, g}\right) \) is frame-homogeneous if this induced action is transitive on \( \mathrm{O}\left( M\right) \) , or in other words, if for all \( p, q \in  M \) and choices of orthonormal bases at \( p \) and \( q \) , there is an isometry taking \( p \) to \( q \) and the chosen basis at \( p \) to the one at \( q \) . (Warning: Some authors, such as [Boo86, dC92, Spi79], use the term isotropic to refer to the property we have called frame-homogeneous.)

Proposition 3.1. Let \( \left( {M, g}\right) \) be a Riemannian manifold.

(a) If \( M \) is isotropic at one point and it is homogeneous, then it is isotropic.

(b) If M is frame-homogeneous, then it is homogeneous and isotropic.

Proof. Problem 3-3.

A homogeneous Riemannian manifold looks geometrically the same at every point, while an isotropic one looks the same in every direction. It turns out that an isotropic Riemannian manifold is automatically homogeneous; however, a Riemannian manifold can be isotropic at one point without being isotropic (for example, the paraboloid \( z = {x}^{2} + {y}^{2} \) in \( {\mathbb{R}}^{3} \) with the induced metric); homogeneous without being isotropic anywhere (for example, the Berger metrics on \( {\mathbb{S}}^{3} \) discussed in Problem 3-10 below); or homogeneous and isotropic without being frame-homogeneous (for example, the Fubini-Study metrics on complex projective spaces discussed in Example 2.30). The proofs of these claims will have to wait until we have developed the theories of geodesics and curvature (see Problems 6-18, 8-5, 8-16, and 8-13).

As mentioned in Chapter 1, the Myers-Steenrod theorem shows that \( \operatorname{Iso}\left( {M, g}\right) \) is always a Lie group acting smoothly on \( M \) . Although we will not use that result, in many cases we can identify a smooth Lie group action that accounts for at least some of the isometry group, and in certain cases we will be able to prove that it is the entire isometry group.

## Euclidean Spaces

The simplest and most important model Riemannian manifold is of course n-dimensional Euclidean space, which is just \( {\mathbb{R}}^{n} \) with the Euclidean metric \( \bar{g} \) given by (2.8).

Somewhat more generally, if \( V \) is any \( n \) -dimensional real vector space endowed with an inner product, we can set \( g\left( {v, w}\right)  = \langle v, w\rangle \) for any \( p \in  V \) and any \( v, w \in  {T}_{p}V \cong  V \) . Choosing an orthonormal basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( V \) defines a basis isomorphism from \( {\mathbb{R}}^{n} \) to \( V \) that sends \( \left( {{x}^{1},\ldots ,{x}^{n}}\right) \) to \( {x}^{i}{b}_{i} \) ; this is easily seen to be an isometry of \( \left( {V, g}\right) \) with \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) , so all \( n \) -dimensional inner product spaces are isometric to each other as Riemannian manifolds.

It is easy to construct isometries of the Riemannian manifold \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) : for example, every orthogonal linear transformation \( A : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) preserves the Euclidean metric, as does every translation \( x \mapsto  b + x \) . It follows that every map of the form \( x \mapsto  b + {Ax} \) , formed by first applying the orthogonal map \( A \) and then translating by \( b \) , is an isometry.

It turns out that the set of all such isometries can be realized as a Lie group acting smoothly on \( {\mathbb{R}}^{n} \) . Regard \( {\mathbb{R}}^{n} \) as a Lie group under addition, and let \( \theta  : \mathrm{O}\left( n\right)  \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) be the natural action of \( \mathrm{O}\left( n\right) \) on \( {\mathbb{R}}^{n} \) . Define the Euclidean group \( \mathrm{E}\left( n\right) \) to be the semidirect product \( {\mathbb{R}}^{n}{ \rtimes  }_{\theta }\mathrm{O}\left( n\right) \) determined by this action: this is the Lie group whose underlying manifold is the product space \( {\mathbb{R}}^{n} \times  \mathrm{O}\left( n\right) \) , with multiplication given by \( \left( {b, A}\right) \left( {{b}^{\prime },{A}^{\prime }}\right)  = \left( {b + A{b}^{\prime }, A{A}^{\prime }}\right) \) (see Example C.12). It has a faithful representation given by the map \( \rho  : \mathrm{E}\left( n\right)  \rightarrow  \mathrm{{GL}}\left( {n + 1,\mathbb{R}}\right) \) defined in block form by

\[
\rho \left( {b, A}\right)  = \left( \begin{array}{ll} A & b \\  0 & 1 \end{array}\right)
\]

where \( b \) is considered an \( n \times  1 \) column matrix.

The Euclidean group acts on \( {\mathbb{R}}^{n} \) via

\[
\left( {b, A}\right)  \cdot  x = b + {Ax}. \tag{3.2}
\]

Problem 3-1 shows that when \( {\mathbb{R}}^{n} \) is endowed with the Euclidean metric, this action is isometric and the induced action on \( \mathrm{O}\left( {\mathbb{R}}^{n}\right) \) is transitive. (Later, we will see that this is in fact the full isometry group of \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) -see Problem 5-11-but we do not need that fact now.) Thus each Euclidean space is frame-homogeneous.

![bo_d7dtff491nqc73eq8m7g_71_410_187_706_772_0.jpg](images/bo_d7dtff491nqc73eq8m7g_71_410_187_706_772_0.jpg)

Fig. 3.1: Transitivity of \( \mathrm{O}\left( {n + 1}\right) \) on \( \mathrm{O}\left( {{\mathbb{S}}^{n}\left( R\right) }\right) \)

## Spheres

Our second class of model Riemannian manifolds comes in a family, with one for each positive real number. Given \( R > 0 \) , let \( {\mathbb{S}}^{n}\left( R\right) \) denote the sphere of radius \( R \) centered at the origin in \( {\mathbb{R}}^{n + 1} \) , endowed with the metric \( {\overset{ \circ  }{g}}_{R} \) (called the round metric of radius \( \mathbf{R} \) ) induced from the Euclidean metric on \( {\mathbb{R}}^{n + 1} \) . When \( R = 1 \) , it is the round metric on \( {\mathbb{S}}^{n} \) introduced in Example 2.13, and we use the notation \( \overset{ \circ  }{g} = {\overset{ \circ  }{g}}_{1} \) .

One of the first things one notices about the spheres is that like Euclidean spaces, they are highly symmetric. We can immediately write down a large group of isometries of \( {\mathbb{S}}^{n}\left( R\right) \) by observing that the linear action of the orthogonal group \( \mathrm{O}\left( {n + 1}\right) \) on \( {\mathbb{R}}^{n + 1} \) preserves \( {\mathbb{S}}^{n}\left( R\right) \) and the Euclidean metric, so its restriction to \( {\mathbb{S}}^{n}\left( R\right) \) acts isometrically on the sphere. (Problem 5-11 will show that this is the full isometry group.)

Proposition 3.2. The group \( \mathrm{O}\left( {n + 1}\right) \) acts transitively on \( \mathrm{O}\left( {{\mathbb{S}}^{n}\left( R\right) }\right) \) , and thus each round sphere is frame-homogeneous.

Proof. It suffices to show that given any \( p \in  {\mathbb{S}}^{n}\left( R\right) \) and any orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}{\mathbb{S}}^{n}\left( R\right) \) , there is an orthogonal map that takes the "north pole" \( N = \left( {0,\ldots ,0, R}\right) \) to \( p \) and the basis \( \left( {{\partial }_{1},\ldots ,{\partial }_{n}}\right) \) for \( {T}_{N}{\mathbb{S}}^{n}\left( R\right) \) to \( \left( {b}_{i}\right) \) .

To do so, think of \( p \) as a vector of length \( R \) in \( {\mathbb{R}}^{n + 1} \) , and let \( \widehat{p} = p/R \) denote the unit vector in the same direction (Fig. 3.1). Since the basis vectors \( \left( {b}_{i}\right) \) are tangent to the sphere, they are orthogonal to \( \widehat{p} \) , so \( \left( {{b}_{1},\ldots ,{b}_{n},\widehat{p}}\right) \) is an orthonormal basis for \( {\mathbb{R}}^{n + 1} \) . Let \( \alpha \) be the matrix whose columns are these basis vectors. Then \( \alpha  \in  \mathrm{O}\left( {n + 1}\right) \) , and by elementary linear algebra, \( \alpha \) takes the standard basis vectors \( \left( {{\partial }_{1},\ldots ,{\partial }_{n + 1}}\right) \) to \( \left( {{b}_{1},\ldots ,{b}_{n},\widehat{p}}\right) \) . It follows that \( \alpha \left( N\right)  = p \) . Moreover, since \( \alpha \) acts linearly on \( {\mathbb{R}}^{n + 1} \) , its differential \( d{\alpha }_{N} : {T}_{N}{\mathbb{R}}^{n + 1} \rightarrow  {T}_{p}{\mathbb{R}}^{n + 1} \) is represented in standard coordinates by the same matrix as \( \alpha \) itself, so \( d{\alpha }_{N}\left( {\partial }_{i}\right)  = {b}_{i} \) for \( i = 1,\ldots , n \) , and \( \alpha \) is the desired orthogonal map.

Another important feature of the round metrics—one that is much less evident than their symmetry—is that they bear a certain close relationship to the Euclidean metrics, which we now describe. Two metrics \( {g}_{1} \) and \( {g}_{2} \) on a manifold \( M \) are said to be conformally related (or pointwise conformal or just conformal) to each other if there is a positive function \( f \in  {C}^{\infty }\left( M\right) \) such that \( {g}_{2} = f{g}_{1} \) . Given two Riemannian manifolds \( \left( {M, g}\right) \) and \( \left( {\widetilde{M},\widetilde{g}}\right) \) , a diffeomorphism \( \varphi  : M \rightarrow  \widetilde{M} \) is called a conformal diffeomorphism (or a conformal transformation) if it pulls \( \widetilde{g} \) back to a metric that is conformal to \( g \) :

\[
{\varphi }^{ * }\widetilde{g} = {fg}\text{ for some positive }f \in  {C}^{\infty }\left( M\right) \text{ . }
\]

Problem 3-6 shows that conformal diffeomorphisms are the same as angle-preserving diffeomorphisms. Two Riemannian manifolds are said to be conformally equivalent if there is a conformal diffeomorphism between them.

A Riemannian manifold \( \left( {M, g}\right) \) is said to be locally conformally flat if every point of \( M \) has a neighborhood that is conformally equivalent to an open set in \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) .

Exercise 3.3. (a) Show that for every smooth manifold \( M \) , conformality is an equivalence relation on the set of all Riemannian metrics on \( M \) .

(b) Show that conformal equivalence is an equivalence relation on the class of all Riemannian manifolds.

Exercise 3.4. Suppose \( {g}_{1} \) and \( {g}_{2} = f{g}_{1} \) are conformally related metrics on an oriented \( n \) -manifold. Show that their volume forms are related by \( d{V}_{{g}_{2}} = {f}^{n/2}d{V}_{{g}_{1}} \) .

A conformal equivalence between \( {\mathbb{R}}^{n} \) and \( {\mathbb{S}}^{n}\left( R\right) \) minus a point is provided by stereographic projection from the north pole. This is the map \( \sigma  : {\mathbb{S}}^{n}\left( R\right)  \smallsetminus  \{ N\}  \rightarrow \; {\mathbb{R}}^{n} \) that sends a point \( P \in  {\mathbb{S}}^{n}\left( R\right)  \smallsetminus  \{ N\} \) , written \( P = \left( {{\xi }^{1},\ldots ,{\xi }^{n},\tau }\right) \) , to \( u = \; \left( {{u}^{1},\ldots ,{u}^{n}}\right)  \in  {\mathbb{R}}^{n} \) , where \( U = \left( {{u}^{1},\ldots ,{u}^{n},0}\right) \) is the point where the line through \( N \) and \( P \) intersects the hyperplane \( \{ \left( {\xi ,\tau }\right)  : \tau  = 0\} \) in \( {\mathbb{R}}^{n + 1} \) (Fig. 3.2). Thus \( U \) is characterized by the fact that \( \left( {U - N}\right)  = \lambda \left( {P - N}\right) \) for some nonzero scalar \( \lambda \) . Writing \( N = \left( {0, R}\right) , U = \left( {u,0}\right) \) , and \( P = \left( {\xi ,\tau }\right)  \in  {\mathbb{R}}^{n + 1} = {\mathbb{R}}^{n} \times  \mathbb{R} \) , we obtain the system of equations

\[
{u}^{i} = \lambda {\xi }^{i}, \tag{3.3}
\]

\[
- R = \lambda \left( {\tau  - R}\right) .
\]

Solving the second equation for \( \lambda \) and plugging it into the first equation, we get the following formula for stereographic projection from the north pole of the sphere of radius \( R \) :

\[
\sigma \left( {\xi ,\tau }\right)  = u = \frac{R\xi }{R - \tau }. \tag{3.4}
\]

![bo_d7dtff491nqc73eq8m7g_73_414_195_704_713_0.jpg](images/bo_d7dtff491nqc73eq8m7g_73_414_195_704_713_0.jpg)

Fig. 3.2: Stereographic projection

It follows from this formula that \( \sigma \) is defined and smooth on all of \( {\mathbb{S}}^{n}\left( R\right)  \smallsetminus  \{ N\} \) . The easiest way to see that it is a diffeomorphism is to compute its inverse. Solving the two equations of (3.3) for \( \tau \) and \( {\xi }^{i} \) gives

\[
{\xi }^{i} = \frac{{u}^{i}}{\lambda },\;\tau  = R\frac{\lambda  - 1}{\lambda }. \tag{3.5}
\]

The point \( P = {\sigma }^{-1}\left( u\right) \) is characterized by these equations and the fact that \( P \) is on the sphere. Thus, substituting (3.5) into \( {\left| \xi \right| }^{2} + {\tau }^{2} = {R}^{2} \) gives

\[
\frac{{\left| u\right| }^{2}}{{\lambda }^{2}} + {R}^{2}\frac{{\left( \lambda  - 1\right) }^{2}}{{\lambda }^{2}} = {R}^{2},
\]

from which we conclude

\[
\lambda  = \frac{{\left| u\right| }^{2} + {R}^{2}}{2{R}^{2}}.
\]

Inserting this back into (3.5) gives the formula

\[
{\sigma }^{-1}\left( u\right)  = \left( {\xi ,\tau }\right)  = \left( {\frac{2{R}^{2}u}{{\left| u\right| }^{2} + {R}^{2}}, R\frac{{\left| u\right| }^{2} - {R}^{2}}{{\left| u\right| }^{2} + {R}^{2}}}\right) , \tag{3.6}
\]

which by construction maps \( {\mathbb{R}}^{n} \) back to \( {\mathbb{S}}^{n}\left( R\right)  \smallsetminus  \{ N\} \) and shows that \( \sigma \) is a diffeomorphism.

Proposition 3.5. Stereographic projection is a conformal diffeomorphism between \( {\mathbb{S}}^{n}\left( R\right)  \smallsetminus  \{ N\} \) and \( {\mathbb{R}}^{n} \) .

Proof. The inverse map \( {\sigma }^{-1} \) is a smooth parametrization of \( {\mathbb{S}}^{n}\left( R\right)  \smallsetminus  \{ N\} \) , so we can use it to compute the pullback metric. Using the usual technique of substitution to compute pullbacks, we obtain the following coordinate representation of \( {\overset{ \circ  }{g}}_{R} \) in stereographic coordinates:

\[
{\left( {\sigma }^{-1}\right) }^{ * }{\overset{ \circ  }{g}}_{R} = {\left( {\sigma }^{-1}\right) }^{ * }\overset{ - }{g} = \mathop{\sum }\limits_{j}{\left( d\left( \frac{2{R}^{2}{u}^{j}}{{\left| u\right| }^{2} + {R}^{2}}\right) \right) }^{2} + {\left( d\left( R\frac{{\left| u\right| }^{2} - {R}^{2}}{{\left| u\right| }^{2} + {R}^{2}}\right) \right) }^{2}.
\]

If we expand each of these terms individually, we get

\[
d\left( \frac{2{R}^{2}{u}^{j}}{{\left| u\right| }^{2} + {R}^{2}}\right)  = \frac{2{R}^{2}d{u}^{j}}{{\left| u\right| }^{2} + {R}^{2}} - \frac{4{R}^{2}{u}^{j}\mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{2}}
\]

\[
d\left( {R\frac{{\left| u\right| }^{2} - {R}^{2}}{{\left| u\right| }^{2} + {R}^{2}}}\right)  = \frac{{2R}\mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}}{{\left| u\right| }^{2} + {R}^{2}} - \frac{{2R}\left( {{\left| u\right| }^{2} - {R}^{2}}\right) \mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{2}}
\]

\[
= \frac{4{R}^{3}\mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{2}}.
\]

Therefore,

\[
{\left( {\sigma }^{-1}\right) }^{ * }{\overset{ \circ  }{g}}_{R} = \frac{4{R}^{4}\mathop{\sum }\limits_{j}{\left( d{u}^{j}\right) }^{2}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{2}} - \frac{{16}{R}^{4}{\left( \mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}\right) }^{2}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{3}} + \frac{{16}{R}^{4}{\left| u\right| }^{2}{\left( \mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}\right) }^{2}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{4}}
\]

\[
+ \frac{{16}{R}^{6}{\left( \mathop{\sum }\limits_{i}{u}^{i}d{u}^{i}\right) }^{2}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{4}}
\]

\[
= \frac{4{R}^{4}\mathop{\sum }\limits_{j}{\left( d{u}^{j}\right) }^{2}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{2}}.
\]

In other words,

\[
{\left( {\sigma }^{-1}\right) }^{ * }{\overset{ \circ  }{g}}_{R} = \frac{4{R}^{4}}{{\left( {\left| u\right| }^{2} + {R}^{2}\right) }^{2}}\bar{g}, \tag{3.7}
\]

where \( \bar{g} \) now represents the Euclidean metric on \( {\mathbb{R}}^{n} \) , and so \( \sigma \) is a conformal diffeomorphism.

Corollary 3.6. Each sphere with a round metric is locally conformally flat.

Proof. Stereographic projection gives a conformal equivalence between a neighborhood of any point except the north pole and Euclidean space; applying a suitable rotation and then stereographic projection (or stereographic projection from the south pole), we get such an equivalence for a neighborhood of the north pole as well.

## Hyperbolic Spaces

Our third class of model Riemannian manifolds is perhaps less familiar than the other two. For each \( n \geq  1 \) and each \( R > 0 \) we will define a frame-homogeneous Riemannian manifold \( {\mathbb{H}}^{n}\left( R\right) \) , called hyperbolic space of radius \( R \) . There are four equivalent models of the hyperbolic spaces, each of which is useful in certain contexts. In the next theorem, we introduce all of them and show that they are isometric.

Theorem 3.7. Let \( n \) be an integer greater than 1. For each fixed \( R > 0 \) , the following Riemannian manifolds are all mutually isometric.

(a) (HYPERBOLOID MODEL) \( {\mathbb{H}}^{n}\left( R\right) \) is the submanifold of Minkowski space \( {\mathbb{R}}^{n,1} \) defined in standard coordinates \( \left( {{\xi }^{1},\ldots ,{\xi }^{n},\tau }\right) \) as the "upper sheet" \( \{ \tau  > 0\} \) of the two-sheeted hyperboloid \( {\left( {\xi }^{1}\right) }^{2} + \cdots  + {\left( {\xi }^{n}\right) }^{2} - {\tau }^{2} =  - {R}^{2} \) , with the induced metric

\[
{\breve{g}}_{R}^{1} = {\iota }^{ * }\bar{q}
\]

where \( \iota  : {\mathbb{H}}^{n}\left( R\right)  \rightarrow  {\mathbb{R}}^{n,1} \) is inclusion, and \( \bar{q} = {\bar{q}}^{\left( n,1\right) } \) is the Minkowski metric:

\[
\bar{q} = {\left( d{\xi }^{1}\right) }^{2} + \cdots  + {\left( d{\xi }^{n}\right) }^{2} - {\left( d\tau \right) }^{2}. \tag{3.8}
\]

(b) (BELTRAMI-KLEIN MODEL) \( {\mathbb{K}}^{n}\left( R\right) \) is the ball of radius \( R \) centered at the origin in \( {\mathbb{R}}^{n} \) , with the metric given in coordinates \( \left( {{w}^{1},\ldots ,{w}^{n}}\right) \) by

\[
{\check{g}}_{R}^{2} = {R}^{2}\frac{{\left( d{w}^{1}\right) }^{2} + \cdots  + {\left( d{w}^{n}\right) }^{2}}{{R}^{2} - {\left| w\right| }^{2}} + {R}^{2}\frac{{\left( {w}^{1}d{w}^{1} + \cdots  + {w}^{n}d{w}^{n}\right) }^{2}}{{\left( {R}^{2} - {\left| w\right| }^{2}\right) }^{2}}. \tag{3.9}
\]

(c) (POINCARÉ BALL MODEL) \( {\mathbb{B}}^{n}\left( R\right) \) is the ball of radius \( R \) centered at the origin in \( {\mathbb{R}}^{n} \) , with the metric given in coordinates \( \left( {{u}^{1},\ldots ,{u}^{n}}\right) \) by

\[
{\breve{g}}_{R}^{3} = 4{R}^{4}\frac{{\left( d{u}^{1}\right) }^{2} + \cdots  + {\left( d{u}^{n}\right) }^{2}}{{\left( {R}^{2} - {\left| u\right| }^{2}\right) }^{2}}.
\]

(d) (POINCARÉ HALF-SPACE MODEL) \( {\mathbb{U}}^{n}\left( R\right) \) is the upper half-space in \( {\mathbb{R}}^{n} \) defined in coordinates \( \left( {{x}^{1},\ldots ,{x}^{n - 1}, y}\right) \) by \( {\mathbb{U}}^{n}\left( R\right)  = \{ \left( {x, y}\right)  : y > 0\} \) , endowed with the metric

\[
{\breve{g}}_{R}^{4} = {R}^{2}\frac{{\left( d{x}^{1}\right) }^{2} + \cdots  + {\left( d{x}^{n - 1}\right) }^{2} + d{y}^{2}}{{y}^{2}}.
\]

Proof. Let \( R > 0 \) be given. We need to verify that \( {\mathbb{H}}^{n}\left( R\right) \) is actually a Riemannian submanifold of \( {\mathbb{R}}^{n,1} \) , or in other words that \( {\breve{g}}_{R}^{1} \) is positive definite. One way to do this is to show, as we will below, that it is the pullback of \( {\breve{g}}_{R}^{2} \) or \( {\breve{g}}_{R}^{3} \) (both of which are manifestly positive definite) by a diffeomorphism. Alternatively, here is a direct proof using some of the theory of submanifolds of pseudo-Riemannian manifolds developed in Chapter 1.

![bo_d7dtff491nqc73eq8m7g_76_188_250_1157_393_0.jpg](images/bo_d7dtff491nqc73eq8m7g_76_188_250_1157_393_0.jpg)

Fig. 3.3: Isometries among the hyperbolic models

Note that \( {\mathbb{H}}^{n}\left( R\right) \) is an open subset of a level set of the smooth function \( f : {\mathbb{R}}^{n,1} \rightarrow  \mathbb{R} \) given by \( f\left( {\xi ,\tau }\right)  = {\left( {\xi }^{1}\right) }^{2} + \cdots  + {\left( {\xi }^{n}\right) }^{2} - {\tau }^{2} \) . We have

\[
{df} = 2{\xi }^{1}d{\xi }^{1} + \cdots  + 2{\xi }^{n}d{\xi }^{n} - {2\tau d\tau }
\]

and therefore the gradient of \( f \) with respect to \( \bar{q} \) is given by

\[
\operatorname{grad}f = 2{\xi }^{1}\frac{\partial }{\partial {\xi }^{1}} + \cdots  + 2{\xi }^{n}\frac{\partial }{\partial {\xi }^{n}} + {2\tau }\frac{\partial }{\partial \tau }. \tag{3.10}
\]

Direct computation shows that

\[
\bar{q}\left( {\operatorname{grad}f,\operatorname{grad}f}\right)  = 4\left( {\mathop{\sum }\limits_{i}{\left( {\xi }^{i}\right) }^{2} - {\tau }^{2}}\right) ,
\]

which is equal to \( - 4{R}^{2} \) at points of \( {\mathbb{H}}^{n}\left( R\right) \) . Thus it follows from Corollary 2.71 that \( {\mathbb{H}}^{n}\left( R\right) \) is a pseudo-Riemannian submanifold of signature \( \left( {n,0}\right) \) , which is to say it is Riemannian.

We will show that all four Riemannian manifolds are mutually isometric by defining isometries \( c : {\mathbb{H}}^{n}\left( R\right)  \rightarrow  {\mathbb{K}}^{n}\left( R\right) ,\pi  : {\mathbb{H}}^{n}\left( R\right)  \rightarrow  {\mathbb{B}}^{n}\left( R\right) \) , and \( \kappa  : {\mathbb{B}}^{n}\left( R\right)  \rightarrow  {\mathbb{U}}^{n}\left( R\right) \) (shown schematically in Fig. 3.3).

We begin with a geometric construction of a diffeomorphism called central projection from the hyperboloid to the ball,

\[
c : {\mathbb{H}}^{n}\left( R\right)  \rightarrow  {\mathbb{K}}^{n}\left( R\right)
\]

which turns out to be an isometry between the two metrics given in (a) and (b). For any \( P = \left( {{\xi }^{1},\ldots ,{\xi }^{n},\tau }\right)  \in  {\mathbb{H}}^{n}\left( R\right)  \subseteq  {\mathbb{R}}^{n,1} \) , set \( c\left( P\right)  = w \in  {\mathbb{K}}^{n}\left( R\right) \) , where \( W = \left( {w, R}\right)  \in  {\mathbb{R}}^{n,1} \) is the point where the line from the origin to \( P \) intersects the hyperplane \( \{ \left( {\xi ,\tau }\right)  : \tau  = R\} \) (Fig. 3.4). Because \( W \) is characterized as the unique scalar multiple of \( P \) whose last coordinate is \( R \) , we have \( W = {RP}/\tau \) , and therefore \( c \) is given by the formula

\[
c\left( {\xi ,\tau }\right)  = \frac{R\xi }{\tau }. \tag{3.11}
\]

![bo_d7dtff491nqc73eq8m7g_77_359_204_764_547_0.jpg](images/bo_d7dtff491nqc73eq8m7g_77_359_204_764_547_0.jpg)

Fig. 3.4: Central projection from the hyperboloid to the Beltrami-Klein model

The relation \( {\left| \xi \right| }^{2} - {\tau }^{2} =  - {R}^{2} \) guarantees that \( {\left| c\left( \xi ,\tau \right) \right| }^{2} = {R}^{2}\left( {1 - {R}^{2}/{\tau }^{2}}\right)  < {R}^{2} \) , so \( c \) maps \( {\mathbb{H}}^{n}\left( R\right) \) into \( {\mathbb{K}}^{n}\left( R\right) \) . To show that \( c \) is a diffeomorphism, we determine its inverse map. Let \( w \in  {\mathbb{K}}^{n}\left( R\right) \) be arbitrary. The unique positive scalar \( \lambda \) such that the point \( \left( {\xi ,\tau }\right)  = \lambda \left( {w, R}\right) \) lies on \( {\mathbb{H}}^{n}\left( R\right) \) is characterized by \( {\lambda }^{2}{\left| w\right| }^{2} - {\lambda }^{2}{R}^{2} =  - {R}^{2} \) , and therefore

\[
\lambda  = \frac{R}{\sqrt{{R}^{2} - {\left| w\right| }^{2}}}.
\]

It follows that the following smooth map is an inverse for \( c \) :

\[
{c}^{-1}\left( w\right)  = \left( {\xi ,\tau }\right)  = \left( {\frac{Rw}{\sqrt{{R}^{2} - {\left| w\right| }^{2}}},\frac{{R}^{2}}{\sqrt{{R}^{2} - {\left| w\right| }^{2}}}}\right) . \tag{3.12}
\]

Thus \( c \) is a diffeomorphism. To show that it is an isometry between \( {\breve{g}}_{R}^{1} \) and \( {\breve{g}}_{R}^{2} \) , we use the fact that \( {\breve{g}}_{R}^{1} \) is the metric induced from \( \bar{q} \) , analogously to the computation we did for stereographic projection above. With \( \left( {\xi ,\tau }\right) \) defined by (3.12), we have

\[
d{\xi }^{i} = \frac{{Rd}{w}^{i}}{\sqrt{{R}^{2} - {\left| w\right| }^{2}}} + \frac{R{w}^{i}\mathop{\sum }\limits_{j}{w}^{j}d{w}^{j}}{{\left( {R}^{2} - {\left| w\right| }^{2}\right) }^{3/2}},
\]

\[
{d\tau } = \frac{{R}^{2}\mathop{\sum }\limits_{j}{w}^{j}d{w}^{j}}{{\left( {R}^{2} - {\left| w\right| }^{2}\right) }^{3/2}}.
\]

It is then straightforward to compute that \( {\left( {c}^{-1}\right) }^{ * }{\breve{g}}_{R}^{1} = \mathop{\sum }\limits_{i}{\left( d{\xi }^{i}\right) }^{2} - {\left( d\tau \right) }^{2} = {\breve{g}}_{R}^{2} \) .

![bo_d7dtff491nqc73eq8m7g_78_374_195_730_754_0.jpg](images/bo_d7dtff491nqc73eq8m7g_78_374_195_730_754_0.jpg)

Fig. 3.5: Hyperbolic stereographic projection

Next we describe a diffeomorphism

\[
\pi  : {\mathbb{H}}^{n}\left( R\right)  \rightarrow  {\mathbb{B}}^{n}\left( R\right)
\]

from the hyperboloid to the ball, called hyperbolic stereographic projection, which is an isometry between the metrics of (a) and (c). Let \( S \in  {\mathbb{R}}^{n,1} \) denote the point \( S = \left( {0,\ldots ,0, - R}\right) \) . For any \( P = \left( {{\xi }^{1},\ldots ,{\xi }^{n},\tau }\right)  \in  {\mathbb{H}}^{n}\left( R\right)  \subseteq  {\mathbb{R}}^{n,1} \) , set \( \pi \left( P\right)  = u \in \; {\mathbb{B}}^{n}\left( R\right) \) , where \( U = \left( {u,0}\right)  \in  {\mathbb{R}}^{n,1} \) is the point where the line through \( S \) and \( P \) intersects the hyperplane \( \{ \left( {\xi ,\tau }\right)  : \tau  = 0\} \) (Fig. 3.5). The point \( U \) is characterized by \( \left( {U - S}\right)  = \lambda \left( {P - S}\right) \) for some nonzero scalar \( \lambda \) , or

\[
{u}^{i} = \lambda {\xi }^{i}, \tag{3.13}
\]

\[
R = \lambda \left( {\tau  + R}\right) .
\]

These equations can be solved in the same manner as in the spherical case to yield

\[
\pi \left( {\xi ,\tau }\right)  = u = \frac{R\xi }{R + \tau },
\]

which takes its values in \( {\mathbb{B}}^{n}\left( R\right) \) because \( {\left| \pi \left( \xi ,\tau \right) \right| }^{2} = {R}^{2}\left( {{\tau }^{2} - {R}^{2}}\right) \left( {{\tau }^{2} + {R}^{2}}\right)  < {R}^{2} \) . A computation similar to the ones before shows that the inverse map is

\[
{\pi }^{-1}\left( u\right)  = \left( {\xi ,\tau }\right)  = \left( {\frac{2{R}^{2}u}{{R}^{2} - {\left| u\right| }^{2}}, R\frac{{R}^{2} + {\left| u\right| }^{2}}{{R}^{2} - {\left| u\right| }^{2}}}\right) .
\]

We will show that \( {\left( {\pi }^{-1}\right) }^{ * }{\breve{g}}_{R}^{1} = {\breve{g}}_{R}^{3} \) . The computation proceeds just as in the spherical case, so we skip over most of the details:

\[
{\left( {\pi }^{-1}\right) }^{ * }{\breve{g}}_{R}^{1} = \mathop{\sum }\limits_{j}{\left( d\left( \frac{2{R}^{2}{u}^{j}}{{R}^{2} - {\left| u\right| }^{2}}\right) \right) }^{2} - {\left( d\left( R\frac{{R}^{2} + {\left| u\right| }^{2}}{{R}^{2} - {\left| u\right| }^{2}}\right) \right) }^{2}
\]

\[
= \frac{4{R}^{4}\mathop{\sum }\limits_{j}{\left( d{u}^{j}\right) }^{2}}{{\left( {R}^{2} - {\left| u\right| }^{2}\right) }^{2}}
\]

\[
= {\breve{g}}_{R}^{3}\text{ . }
\]

Next we consider the Poincaré half-space model, by constructing an explicit diffeomorphism

\[
\kappa  : {\mathbb{U}}^{n}\left( R\right)  \rightarrow  {\mathbb{B}}^{n}\left( R\right) .
\]

In this case it is more convenient to write the coordinates on the ball as \( \left( {u, v}\right)  = \; \left( {{u}^{1},\ldots ,{u}^{n - 1}, v}\right) \) . In the 2-dimensional case, \( \kappa \) is easy to write down in complex notation \( w = u + {iv} \) and \( z = x + {iy} \) . It is a variant of the classical Cayley transform:

\[
\kappa \left( z\right)  = w = {iR}\frac{z - {iR}}{z + {iR}}. \tag{3.14}
\]

Elementary complex analysis shows that this is a complex-analytic diffeomorphism taking \( {\mathbb{U}}^{2}\left( R\right) \) onto \( {\mathbb{B}}^{2}\left( R\right) \) . Separating \( z \) into real and imaginary parts, we can also write this in real terms as

\[
\kappa \left( {x, y}\right)  = \left( {u, v}\right)  = \left( {\frac{2{R}^{2}x}{{\left| x\right| }^{2} + {\left( y + R\right) }^{2}}, R\frac{{\left| x\right| }^{2} + {\left| y\right| }^{2} - {R}^{2}}{{\left| x\right| }^{2} + {\left( y + R\right) }^{2}}}\right) . \tag{3.15}
\]

This same formula makes sense in any dimension \( n \) if we interpret \( x \) to mean \( \left( {{x}^{1},\ldots ,{x}^{n - 1}}\right) \) , and it is easy to check that it maps the upper half-space \( \{ y > 0\} \) into the ball of radius \( R \) . A direct computation shows that its inverse is

\[
{\kappa }^{-1}\left( {u, v}\right)  = \left( {x, y}\right)  = \left( {\frac{2{R}^{2}u}{{\left| u\right| }^{2} + {\left( v - R\right) }^{2}}, R\frac{{R}^{2} - {\left| u\right| }^{2} - {v}^{2}}{{\left| u\right| }^{2} + {\left( v - R\right) }^{2}}}\right) ,
\]

so \( \kappa \) is a diffeomorphism, called the generalized Cayley transform. The verification that \( {\kappa }^{ * }{\breve{g}}_{R}^{3} = {\breve{g}}_{R}^{4} \) is basically a long calculation, and is left to Problem 3-4.

We often use the generic notation \( {\mathbb{H}}^{n}\left( R\right) \) to refer to any one of the Riemannian manifolds of Theorem 3.7, and \( {\breve{g}}_{R} \) to refer to the corresponding metric; the special case \( R = 1 \) is denoted by \( \left( {{\mathbb{H}}^{n},\breve{g}}\right) \) and is called simply hyperbolic space, or in the 2-dimensional case, the hyperbolic plane.

Because all of the models for a given value of \( R \) are isometric to each other, when analyzing them geometrically we can use whichever model is most convenient for the application we have in mind. The next corollary is an example in which the Poincaré ball and half-space models serve best.

Corollary 3.8. Each hyperbolic space is locally conformally flat.

Proof. In either the Poincaré ball model or the half-space model, the identity map gives a global conformal equivalence with an open subset of Euclidean space.

The examples presented so far might give the impression that most Riemannian manifolds are locally conformally flat. This is far from the truth, but we do not yet have the tools to prove it. See Problem 8-25 for some explicit examples of Riemannian manifolds that are not locally conformally flat.

The symmetries of \( {\mathbb{H}}^{n}\left( R\right) \) are most easily seen in the hyperboloid model. Let \( \mathrm{O}\left( {n,1}\right) \) denote the group of linear maps from \( {\mathbb{R}}^{n,1} \) to itself that preserve the Minkowski metric, called the \( \left( {n + 1}\right) \) -dimensional Lorentz group. Note that each element of \( \mathrm{O}\left( {n,1}\right) \) preserves the hyperboloid \( \left\{  {{\tau }^{2} - {\left| \xi \right| }^{2} = {R}^{2}}\right\} \) , which has two components determined by \( \tau  > 0 \) and \( \tau  < 0 \) . We let \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) denote the subgroup of \( \mathrm{O}\left( {n,1}\right) \) consisting of maps that take the \( \tau  > 0 \) component of the hyperboloid to itself. (This is called the orthochronous Lorentz group, because physically it represents coordinate changes that preserve the forward time direction.) Then \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) preserves \( {\mathbb{H}}^{n}\left( R\right) \) , and because it preserves \( \bar{q} \) it acts isometrically on \( {\mathbb{H}}^{n}\left( R\right) \) . (Problem 5-11 will show that this is the full isometry group.) Recall that \( \mathrm{O}\left( {{\mathbb{H}}^{n}\left( R\right) }\right) \) denotes the set of all orthonormal bases for all tangent spaces of \( {\mathbb{H}}^{n}\left( R\right) \) .

Proposition 3.9. The group \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) acts transitively on \( \mathrm{O}\left( {{\mathbb{H}}^{n}\left( R\right) }\right) \) , and therefore \( {\mathbb{H}}^{n}\left( R\right) \) is frame-homogeneous.

Proof. The argument is entirely analogous to the proof of Proposition 3.2, so we give only a sketch. Suppose \( p \in  {\mathbb{H}}^{n}\left( R\right) \) and \( \left( {b}_{i}\right) \) is an orthonormal basis for \( {T}_{p}{\mathbb{H}}^{n}\left( R\right) \) . Identifying \( p \in  {\mathbb{R}}^{n,1} \) with an element of \( {T}_{p}{\mathbb{R}}^{n,1} \) in the usual way, we can regard \( \widehat{p} = p/R \) as a \( \bar{q} \) -unit vector in \( {T}_{p}{\mathbb{R}}^{n,1} \) , and (3.10) shows that it is a scalar multiple of the \( \bar{q} \) -gradient of the defining function \( f \) and thus is orthogonal to \( {T}_{p}{\mathbb{H}}^{n}\left( R\right) \) with respect to \( \bar{q} \) . Thus \( \left( {{b}_{1},\ldots ,{b}_{n},{b}_{n + 1} = \widehat{p}}\right) \) is a \( \bar{q} \) -orthonormal basis for \( {\mathbb{R}}^{n,1} \) , and \( \bar{q} \) has the following expression in terms of the dual basis \( \left( {\beta }^{j}\right) \) :

\[
\bar{q} = {\left( {\beta }^{1}\right) }^{2} + \cdots  + {\left( {\beta }^{n}\right) }^{2} - {\left( {\beta }^{n + 1}\right) }^{2}.
\]

Thus the matrix whose columns are \( \left( {{b}_{1},\ldots ,{b}_{n + 1}}\right) \) is an element of \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) sending \( N = \left( {0,\ldots ,0, R}\right) \) to \( p \) and \( {\partial }_{i} \) to \( {b}_{i} \) (Fig. 3.6).

## Invariant Metrics on Lie Groups

Lie groups provide us with another large class of homogeneous Riemannian manifolds. (See Appendix C for a review of the basic facts about Lie groups that we will use.)

Let \( G \) be a Lie group. A Riemannian metric \( g \) on \( G \) is said to be left-invariant if it is invariant under all left translations: \( {L}_{\varphi }^{ * }g = g \) for all \( \varphi  \in  G \) . Similarly, \( g \) is right-invariant if it is invariant under all right translations, and bi-invariant if it is both left- and right-invariant. The next lemma shows that left-invariant metrics are easy to come by.

![bo_d7dtff491nqc73eq8m7g_81_404_203_720_557_0.jpg](images/bo_d7dtff491nqc73eq8m7g_81_404_203_720_557_0.jpg)

Fig. 3.6: Frame homogeneity of \( {\mathbb{H}}^{n}\left( R\right) \)

Lemma 3.10. Let \( G \) be a Lie group and let \( \mathfrak{g} \) be its Lie algebra of left-invariant vector fields.

(a) A Riemannian metric \( g \) on \( G \) is left-invariant if and only if for all \( X, Y \in  \mathfrak{g} \) , the function \( g\left( {X, Y}\right) \) is constant on \( G \) .

(b) The restriction map \( g \mapsto  {g}_{e} \in  {\sum }^{2}\left( {{T}_{e}^{ * }G}\right) \) together with the natural identification \( {T}_{e}G \cong  \mathfrak{g} \) gives a bijection between left-invariant Riemannian metrics on \( G \) and inner products on \( \mathfrak{g} \) .

- Exercise 3.11. Prove the preceding lemma.

Thus all we need to do to construct a left-invariant metric is choose any inner product on \( \mathfrak{g} \) , and define a metric on \( G \) by applying that inner product to left-invariant vector fields. Right-invariant metrics can be constructed in a similar way using right-invariant vector fields. Since a Lie group acts transitively on itself by either left or right translation, every left-invariant or right-invariant metric is homogeneous.

Much more interesting are the bi-invariant metrics, because, as you will be able to prove later (Problems 7-13 and 8-17), their curvatures are intimately related to the structure of the Lie algebra of the group. But bi-invariant metrics are generally much rarer than left-invariant or right-invariant ones; in fact, some Lie groups have no bi-invariant metrics at all (see Problems 3-12 and 3-13). Fortunately, there is a complete answer to the question of which Lie groups admit bi-invariant metrics, which we present in this section.

We begin with a proposition that shows how to determine whether a given left-invariant metric is bi-invariant, based on properties of the adjoint representation of the group. Recall that this is the representation Ad: \( G \rightarrow  \mathrm{{GL}}\left( \mathfrak{g}\right) \) given by \( \operatorname{Ad}\left( \varphi \right)  = \; {\left( {C}_{\varphi }\right) }_{ * } : \mathfrak{g} \rightarrow  \mathfrak{g} \) , where \( {C}_{\varphi } : G \rightarrow  G \) is the automorphism defined by conjugation: \( {C}_{\varphi }\left( \psi \right)  = {\varphi \psi }{\varphi }^{-1} \) . See Appendix C for more details.

Proposition 3.12. Let \( G \) be a Lie group and \( \mathfrak{g} \) its Lie algebra. Suppose \( g \) is a left-invariant Riemannian metric on \( G \) , and let \( \langle  \cdot  , \cdot  \rangle \) denote the corresponding inner product on \( \mathfrak{g} \) as in Lemma 3.10. Then \( g \) is bi-invariant if and only if \( \langle  \cdot  , \cdot  \rangle \) is invariant under the action of \( \operatorname{Ad}\left( G\right)  \subseteq  \operatorname{GL}\left( \mathfrak{g}\right) \) , in the sense that \( \langle \operatorname{Ad}\left( \varphi \right) X,\operatorname{Ad}\left( \varphi \right) Y\rangle  = \langle X, Y\rangle \) for all \( X, Y \in  \mathfrak{g} \) and \( \varphi  \in  G \) .

Proof. We begin the proof with some preliminary computations. Suppose \( g \) is left-invariant and \( \langle  \cdot  , \cdot  \rangle \) is the associated inner product on \( \mathfrak{g} \) . Let \( \varphi  \in  G \) be arbitrary, and note that \( {C}_{\varphi } \) is the composition of left multiplication by \( \varphi \) followed by right multiplication by \( {\varphi }^{-1} \) . Thus for every \( X \in  \mathfrak{g} \) , left-invariance implies \( {\left( {R}_{{\varphi }^{-1}}\right) }_{ * }X = \; {\left( {R}_{{\varphi }^{-1}}\right) }_{ * }{\left( {L}_{\varphi }\right) }_{ * }X = {\left( {C}_{\varphi }\right) }_{ * }X = \operatorname{Ad}\left( \varphi \right) X \) . Therefore, for all \( \psi  \in  G \) and \( X, Y \in  \mathfrak{g} \) , we have

\[
{\left( {\left( {R}_{{\varphi }^{-1}}\right) }^{ * }g\right) }_{\psi }\left( {{X}_{\psi },{Y}_{\psi }}\right)  = {g}_{\psi {\varphi }^{-1}}\left( {{\left( {\left( {R}_{{\varphi }^{-1}}\right) }_{ * }X\right) }_{\psi {\varphi }^{-1}},{\left( {\left( {R}_{{\varphi }^{-1}}\right) }_{ * }Y\right) }_{\psi {\varphi }^{-1}}}\right)
\]

\[
= {g}_{\psi {\varphi }^{-1}}\left( {{\left( \operatorname{Ad}\left( \varphi \right) X\right) }_{\psi {\varphi }^{-1}},{\left( \operatorname{Ad}\left( \varphi \right) Y\right) }_{\psi {\varphi }^{-1}}}\right)
\]

\[
= \langle \operatorname{Ad}\left( \varphi \right) X,\operatorname{Ad}\left( \varphi \right) Y\rangle .
\]

Now assume that \( \langle  \cdot  , \cdot  \rangle \) is invariant under \( \operatorname{Ad}\left( G\right) \) . Then the expression on the last line above is equal to \( \langle X, Y\rangle  = {g}_{\psi }\left( {{X}_{\psi },{Y}_{\psi }}\right) \) , which shows that \( {\left( {R}_{{\varphi }^{-1}}\right) }^{ * }g = g \) . Since this is true for all \( \varphi  \in  G \) , it follows that \( g \) is bi-invariant.

Conversely, assuming that \( g \) is bi-invariant, we have \( {\left( {R}_{{\varphi }^{-1}}\right) }^{ * }g = g \) for each \( \varphi  \in  G \) , so the above computation yields

\[
\langle X, Y\rangle  = {g}_{\psi }\left( {{X}_{\psi },{Y}_{\psi }}\right)  = {\left( {\left( {R}_{{\varphi }^{-1}}\right) }^{ * }g\right) }_{\psi }\left( {{X}_{\psi },{Y}_{\psi }}\right)  = \langle \operatorname{Ad}\left( \varphi \right) X,\operatorname{Ad}\left( \varphi \right) Y\rangle ,
\]

which shows that \( \langle  \cdot  , \cdot  \rangle \) is \( \operatorname{Ad}\left( G\right) \) -invariant.

In order to apply the preceding proposition, we need a lemma about finding invariant inner products on vector spaces. Recall from Appendix C that for every finite-dimensional real vector space \( V,\mathrm{{GL}}\left( V\right) \) denotes the Lie group of all invertible linear maps from \( V \) to itself. If \( H \) is a subgroup of \( \mathrm{{GL}}\left( V\right) \) , an inner product \( \langle  \cdot  , \cdot  \rangle \) on \( V \) is said to be \( H \) -invariant if \( \langle {hx},{hy}\rangle  = \langle x, y\rangle \) for all \( x, y \in  V \) and \( h \in  H \) .

Lemma 3.13. Suppose \( V \) is a finite-dimensional real vector space and \( H \) is a subgroup of \( \mathrm{{GL}}\left( V\right) \) . There exists an \( H \) -invariant inner product on \( V \) if and only if \( H \) has compact closure in \( \mathrm{{GL}}\left( V\right) \) .

Proof. Assume first that there exists an \( H \) -invariant inner product \( \langle  \cdot  , \cdot  \rangle \) on \( V \) . This implies that \( H \) is contained in the subgroup \( \mathrm{O}\left( V\right)  \subseteq  \mathrm{{GL}}\left( V\right) \) consisting of linear isomorphisms of \( V \) that are orthogonal with respect to this inner product. Choosing an orthonormal basis of \( V \) yields a Lie group isomorphism between \( \mathrm{O}\left( V\right) \) and \( \mathrm{O}\left( n\right)  \subseteq  \mathrm{{GL}}\left( {n,\mathbb{R}}\right) \) (where \( n = \dim V \) ), so \( \mathrm{O}\left( V\right) \) is compact; and the closure of \( H \) is a closed subset of this compact group, and thus is itself compact.

Conversely, suppose \( H \) has compact closure in \( \mathrm{{GL}}\left( V\right) \) , and let \( K \) denote the closure. A simple limiting argument shows that \( K \) is itself a subgroup, and thus it is a Lie group by the closed subgroup theorem (Thm. C.8). Let \( \langle  \cdot  , \cdot  {\rangle }_{0} \) be an arbitrary inner product on \( V \) , and let \( \mu \) be a right-invariant volume form on \( K \) (for example, the volume form of some right-invariant metric on \( K \) ). For fixed \( x, y \in  V \) , define a smooth function \( {f}_{x, y} : K \rightarrow  \mathbb{R} \) by \( {f}_{x, y}\left( k\right)  = \langle {kx},{ky}{\rangle }_{0} \) . Then define a new inner product \( \langle  \cdot  , \cdot  \rangle \) on \( V \) by

\[
\langle x, y\rangle  = {\int }_{K}{f}_{x, y}\mu .
\]

It follows directly from the definition that \( \langle  \cdot  , \cdot  \rangle \) is symmetric and bilinear over \( \mathbb{R} \) . For each nonzero \( x \in  V \) , we have \( {f}_{x, x} > 0 \) everywhere on \( K \) , so \( \langle x, x\rangle  > 0 \) , showing that \( \langle  \cdot  , \cdot  \rangle \) is indeed an inner product.

To see that it is invariant under \( K \) , let \( {k}_{0} \in  K \) be arbitrary. Then for all \( x, y \in  V \) and \( k \in  K \) , we have

\[
{f}_{{k}_{0}x,{k}_{0}y}\left( k\right)  = {\left\langle  k{k}_{0}x, k{k}_{0}y\right\rangle  }_{0}
\]

\[
= {f}_{x, y} \circ  {R}_{{k}_{0}}\left( k\right) ,
\]

where \( {R}_{{k}_{0}} : K \rightarrow  K \) is right translation by \( {k}_{0} \) . Because \( \mu \) is right-invariant, it follows from diffeomorphism invariance of the integral that

\[
\left\langle  {{k}_{0}x,{k}_{0}y}\right\rangle   = {\int }_{K}{f}_{{k}_{0}x,{k}_{0}y}\mu
\]

\[
= {\int }_{K}\left( {{f}_{x, y} \circ  {R}_{{k}_{0}}}\right) \mu
\]

\[
= {\int }_{K}{R}_{{k}_{0}}^{ * }\left( {{f}_{x, y}\mu }\right)
\]

\[
= {\int }_{K}{f}_{x, y}\mu  = \langle x, y\rangle .
\]

Thus \( \langle  \cdot  , \cdot  \rangle \) is \( K \) -invariant, and it is also \( H \) -invariant because \( H \subseteq  K \) .

Theorem 3.14 (Existence of Bi-invariant Metrics). Let \( G \) be a Lie group and \( \mathfrak{g} \) its Lie algebra. Then \( G \) admits a bi-invariant metric if and only if \( \operatorname{Ad}\left( G\right) \) has compact closure in \( \mathrm{{GL}}\left( \mathrm{g}\right) \) .

Proof. Proposition 3.12 shows that there is a bi-invariant metric on \( G \) if and only if there is an \( \operatorname{Ad}\left( G\right) \) -invariant inner product on \( \mathfrak{g} \) , and Lemma 3.13 in turn shows that the latter is true if and only if \( \operatorname{Ad}\left( G\right) \) has compact closure in \( \operatorname{GL}\left( g\right) \) .

The most important application of the preceding theorem is to compact groups.

Corollary 3.15. Every compact Lie group admits a bi-invariant Riemannian metric.

Proof. If \( G \) is compact, then \( \operatorname{Ad}\left( G\right) \) is a compact subgroup of \( \mathrm{{GL}}\left( \mathfrak{g}\right) \) because Ad: \( G \rightarrow  \mathrm{{GL}}\left( \mathfrak{g}\right) \) is continuous.

Another important application is to prove that certain Lie groups do not admit bi-invariant metrics. One way to do this is to note that if \( \operatorname{Ad}\left( G\right) \) has compact closure in \( \mathrm{{GL}}\left( g\right) \) , then every orbit of \( \mathrm{{Ad}}\left( G\right) \) must be a bounded subset of \( g \) with respect to any choice of norm, because it is contained in the image of the compact set \( \overline{\operatorname{Ad}\left( G\right) } \) under a continuous map of the form \( \varphi  \mapsto  \varphi \left( {X}_{0}\right) \) from \( \mathrm{{GL}}\left( \mathfrak{g}\right) \) to \( \mathfrak{g} \) . Thus if one can find an element \( {X}_{0} \in  \mathfrak{g} \) and a subset \( S \subseteq  G \) such that the elements of the form \( \operatorname{Ad}\left( \varphi \right) X \) are unbounded in \( \mathfrak{g} \) for \( \varphi  \in  S \) , then there is no bi-invariant metric.

Here are some examples.

## Example 3.16 (Invariant Metrics on Lie Groups).

(a) Every left-invariant metric on an abelian Lie group is bi-invariant, because the adjoint representation is trivial. Thus the Euclidean metric on \( {\mathbb{R}}^{n} \) and the flat metric on \( {\mathbb{T}}^{n} \) of Example 2.21 are both bi-invariant.

(b) If a metric \( g \) on a Lie group \( G \) is left-invariant, then the induced metric on every Lie subgroup \( H \subseteq  G \) is easily seen to be left-invariant. Similarly, if \( g \) is bi-invariant, then the induced metric on \( H \) is bi-invariant.

(c) The Lie group \( \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) (the group of \( 2 \times  2 \) real matrices of determinant 1) admits many left-invariant metrics (as does every positive-dimensional Lie group), but no bi-invariant ones. To see this, recall that the Lie algebra of \( \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) is isomorphic to the algebra \( \mathfrak{{sl}}\left( {2,\mathbb{R}}\right) \) of trace-free \( 2 \times  2 \) matrices, and the adjoint representation is given by \( \operatorname{Ad}\left( A\right) X = {AX}{A}^{-1} \) (see Example C.10). If we let \( {X}_{0} = \left( \begin{array}{ll} 0 & 1 \\  0 & 0 \end{array}\right)  \in  \mathfrak{{sl}}\left( {2,\mathbb{R}}\right) \) and \( {A}_{c} = \left( \begin{matrix} c & 0 \\  0 & 1/c \end{matrix}\right)  \in  \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) for \( c > 0 \) , then \( \operatorname{Ad}\left( {A}_{c}\right) {X}_{0} = \left( \begin{matrix} 0 & {c}^{2} \\  0 & 0 \end{matrix}\right) \) , which is unbounded as \( c \rightarrow  \infty \) . Thus the orbit of \( {X}_{0} \) is not contained in any compact subset, which implies that there is no bi-invariant metric on \( \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) . A similar argument shows that \( \mathrm{{SL}}\left( {n,\mathbb{R}}\right) \) admits no bi-invariant metric for any \( n \geq  2 \) . In view of (b) above, this shows also that \( \operatorname{GL}\left( {n,\mathbb{R}}\right) \) admits no bi-invariant metric for \( n \geq  2 \) . (Of course, \( \operatorname{GL}\left( {1,\mathbb{R}}\right) \) does admit bi-invariant metrics because it is abelian.)

(d) With \( {\mathbb{S}}^{3} \) regarded as a submanifold of \( {\mathbb{C}}^{2} \) , the map

\[
\left( {w, z}\right)  \mapsto  \left( \begin{array}{rr} w & z \\   - \bar{z} & \bar{w} \end{array}\right) \tag{3.16}
\]

gives a diffeomorphism from \( {\mathbb{S}}^{3} \) to \( \mathrm{{SU}}\left( 2\right) \) . Under the inverse of this map, the round metric on \( {\mathbb{S}}^{3} \) pulls back to a bi-invariant metric on \( \mathrm{{SU}}\left( 2\right) \) , as Problem 3-10 shows.

(e) Let \( \mathfrak{o}\left( n\right) \) denote the Lie algebra of \( \mathrm{O}\left( n\right) \) , identified with the algebra of skew-symmetric \( n \times  n \) matrices, and define a bilinear form on \( \mathfrak{o}\left( n\right) \) by

\[
\langle A, B\rangle  = \operatorname{tr}\left( {{A}^{T}B}\right) .
\]

This is an Ad-invariant inner product, and thus determines a bi-invariant Riemannian metric on \( \mathrm{O}\left( n\right) \) (see Problem 3-11).

(f) Let \( {\mathbb{U}}^{n} \) be the upper half-space as defined in Theorem 3.7. We can regard \( {\mathbb{U}}^{n} \) as a Lie group by identifying each point \( \left( {x, y}\right)  = \left( {{x}^{1},\ldots ,{x}^{n - 1}, y}\right)  \in  {\mathbb{U}}^{n} \) with an invertible \( n \times  n \) matrix as follows:

\[
\left( {x, y}\right)  \leftrightarrow  \left( \begin{matrix} {I}_{n - 1} & 0 \\  {x}^{T} & y \end{matrix}\right)
\]

where \( {I}_{n - 1} \) is the \( \left( {n - 1}\right)  \times  \left( {n - 1}\right) \) identity matrix. Then the hyperbolic metric \( {\breve{g}}_{R}^{4} \) is left-invariant on \( {\mathbb{U}}^{n} \) but not right-invariant (see Problem 3-12).

(g) For \( n \geq  1 \) , the \( \left( {{2n} + 1}\right) \) -dimensional Heisenberg group is the Lie subgroup \( {H}_{n} \subseteq  \mathrm{{GL}}\left( {n + 2,\mathbb{R}}\right) \) defined by

\[
{H}_{n} = \left\{  {\left( \begin{matrix} 1 & {x}^{T} & z \\  0 & 1 & y \\  0 & 0 & 1 \end{matrix}\right)  : x, y \in  {\mathbb{R}}^{n}, z \in  \mathbb{R}}\right\}  ,
\]

where \( x \) and \( y \) are treated as column matrices. These are the simplest examples of nilpotent Lie groups, meaning that the series of subgroups \( G \supseteq  \left\lbrack  {G, G}\right\rbrack   \supseteq \; \left\lbrack  {G,\left\lbrack  {G, G}\right\rbrack  }\right\rbrack   \supseteq  \cdots \) eventually reaches the trivial subgroup (where for any subgroups \( {G}_{1},{G}_{2} \subseteq  G \) , the notation \( \left\lbrack  {{G}_{1},{G}_{2}}\right\rbrack \) means the subgroup of \( G \) generated by all elements of the form \( {x}_{1}{x}_{2}{x}_{1}^{-1}{x}_{2}^{-1} \) for \( {x}_{i} \in  {G}_{i} \) ). There are many left-invariant metrics on \( {H}_{n} \) , but no bi-invariant ones, as Problem 3-13 shows.

(h) Our last example is a group that plays an important role in the classification of 3-manifolds. Let Sol denote the following 3-dimensional Lie subgroup of \( \mathrm{{GL}}\left( {3,\mathbb{R}}\right) \) :

\[
\text{ Sol } = \left\{  {\left( \begin{matrix} {e}^{z} & 0 & x \\  0 & {e}^{-z} & y \\  0 & 0 & 1 \end{matrix}\right)  : x, y, z \in  \mathbb{R}}\right\}  \text{ . }
\]

This group is the simplest nonnilpotent example of a solvable Lie group, meaning that the series of subgroups \( G \supseteq  \left\lbrack  {G, G}\right\rbrack   \supseteq  \left\lbrack  {\left\lbrack  {G, G}\right\rbrack  ,\left\lbrack  {G, G}\right\rbrack  }\right\rbrack   \supseteq  \cdots \) eventually reaches the trivial subgroup. Like the Heisenberg groups, Sol admits left-invariant metrics but not bi-invariant ones (Problem 3-14).

In fact, John Milnor showed in 1976 [Mil76] that the only Lie groups that admit bi-invariant metrics are those that are isomorphic to direct products of compact groups and abelian groups.

## Other Homogeneous Riemannian Manifolds

There are many homogeneous Riemannian manifolds besides the frame-homogeneous ones and the Lie groups with invariant metrics. To identify other examples, it is natural to ask the following question: If \( M \) is a smooth manifold endowed with a smooth, transitive action by a Lie group \( G \) (called a homogeneous \( G \) -space or just a homogeneous space), is there a Riemannian metric on \( M \) that is invariant under the group action?

The next theorem gives a necessary and sufficient condition for existence of an invariant Riemannian metric that is usually easy to check.

Theorem 3.17 (Existence of Invariant Metrics on Homogeneous Spaces). Suppose \( G \) is a Lie group and \( M \) is a homogeneous \( G \) -space. Let \( {p}_{0} \) be a point in \( M \) , and let \( {I}_{{p}_{0}} : {G}_{{p}_{0}} \rightarrow  \mathrm{{GL}}\left( {{T}_{{p}_{0}}M}\right) \) denote the isotropy representation at \( {p}_{0} \) . There exists a \( G \) -invariant Riemannian metric on \( M \) if and only if \( {I}_{{p}_{0}}\left( {G}_{{p}_{0}}\right) \) has compact closure in \( \mathrm{{GL}}\left( {{T}_{{p}_{0}}M}\right) \) .

Proof. Assume first that \( g \) is a \( G \) -invariant metric on \( M \) . Then the inner product \( {g}_{{p}_{0}} \) on \( {T}_{{p}_{0}}M \) is invariant under the isotropy representation, so it follows from Lemma 3.13 that \( {I}_{{p}_{0}}\left( {G}_{{p}_{0}}\right) \) has compact closure in \( \mathrm{{GL}}\left( {{T}_{{p}_{0}}M}\right) \) .

Conversely, assume that \( {I}_{{p}_{0}}\left( {G}_{{p}_{0}}\right) \) has compact closure in \( \mathrm{{GL}}\left( {{T}_{{p}_{0}}M}\right) \) . Lemma 3.13 shows that there is an inner product \( {g}_{{p}_{0}} \) on \( {T}_{{p}_{0}}\left( M\right) \) that is invariant under the isotropy representation. For arbitrary \( p \in  M \) , we define an inner product \( {g}_{p} \) on \( {T}_{p}M \) by choosing an element \( \varphi  \in  G \) such that \( \varphi \left( p\right)  = {p}_{0} \) and setting

\[
{g}_{p} = {\left( d{\varphi }_{p}\right) }^{ * }{g}_{{p}_{0}}.
\]

If \( {\varphi }_{1},{\varphi }_{2} \) are any two such elements of \( G \) , then \( {\varphi }_{1} = h{\varphi }_{2} \) with \( h = {\varphi }_{1}{\varphi }_{2}^{-1} \in  {G}_{{p}_{0}} \) , so

\[
{\left( {\left. d{\varphi }_{1}\right| }_{p}\right) }^{ * }{g}_{{p}_{0}} = {\left( d{\left( h{\varphi }_{2}\right) }_{p}\right) }^{ * }{g}_{{p}_{0}} = {\left( {\left. d{\varphi }_{2}\right| }_{p}\right) }^{ * }{\left( d{h}_{{p}_{0}}\right) }^{ * }{g}_{{p}_{0}} = {\left( {\left. d{\varphi }_{2}\right| }_{p}\right) }^{ * }{g}_{{p}_{0}},
\]

showing that \( g \) is well defined as a rough tensor field on \( M \) . An easy computation shows that \( g \) is \( G \) -invariant, so it remains only to show that it is smooth.

The map \( \pi  : G \rightarrow  M \) given by \( \pi \left( \psi \right)  = \psi  \cdot  {p}_{0} \) is a smooth surjection because the action is smooth and transitive. Given \( \varphi  \in  G \) , if we let \( {\theta }_{\varphi } : M \rightarrow  M \) denote the map \( p \mapsto  \varphi  \cdot  p \) and \( {L}_{\varphi } : G \rightarrow  G \) the left translation by \( \varphi \) , then the map \( \pi \) satisfies

\[
\pi  \circ  {L}_{\varphi }\left( \psi \right)  = \left( {\varphi \psi }\right)  \cdot  {p}_{0} = \varphi  \cdot  \left( {\psi  \cdot  {p}_{0}}\right)  = {\theta }_{\varphi } \circ  \pi \left( \psi \right) , \tag{3.17}
\]

so it is equivariant with respect to these two actions. Thus it is a submersion by the equivariant rank theorem (Thm. C.14).

Define a rough 2-tensor field \( \tau \) on \( G \) by \( \tau  = {\pi }^{ * }g \) . (It will typically not be positive definite, because \( {\tau }_{e}\left( {v, w}\right)  = 0 \) if either \( v \) or \( w \) is tangent to the isotropy group \( {G}_{{p}_{0}} \) and thus in the kernel of \( d{\pi }_{e} \) .) For all \( \varphi  \in  G \) ,(3.17) implies

\[
{L}_{\varphi }^{ * }\tau  = {L}_{\varphi }^{ * }{\pi }^{ * }g = {\left( \pi  \circ  {L}_{\varphi }\right) }^{ * }g = {\left( {\theta }_{\varphi } \circ  \pi \right) }^{ * }g = {\pi }^{ * }{\theta }_{\varphi }^{ * }g = {\pi }^{ * }g = \tau ,
\]

where the next-to-last equality follows from the \( G \) -invariance of \( g \) . Thus \( \tau \) is a left-invariant tensor field on \( G \) . Every basis \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) for the Lie algebra of \( G \) forms a smooth global left-invariant frame for \( G \) , and with respect to such a frame the components \( \tau \left( {{X}_{i},{X}_{j}}\right) \) are constant; thus \( \tau \) is a smooth tensor field on \( G \) .

For each \( p \in  M \) , the fact that \( \pi \) is a surjective smooth submersion implies that there exist a neighborhood \( U \) of \( p \) and a smooth local section \( \sigma  : U \rightarrow  G \) (Thm. A.17). Then

\[
{\left. g\right| }_{U} = {\left( \pi  \circ  \sigma \right) }^{ * }g = {\sigma }^{ * }{\pi }^{ * }g = {\sigma }^{ * }\tau ,
\]

showing that \( g \) is smooth on \( U \) . Since this holds in a neighborhood of each point, \( g \) is smooth.

The next corollary, which follows immediately from Theorem 3.17, addresses the most commonly encountered case. (Other necessary and sufficient conditions for the existence of invariant metrics are given in [Poo81, 6.58-6.59].)

Corollary 3.18. If a Lie group \( G \) acts smoothly and transitively on a smooth manifold \( M \) with compact isotropy groups, then there exists a \( G \) -invariant Riemannian metric on \( M \) .

Exercise 3.19. Suppose \( G \) is a Lie group and \( M \) is a homogeneous \( G \) -space that admits at least one \( g \) -invariant metric. Show that for each \( p \in  M \) , the map \( g \mapsto  {g}_{p} \) gives a bijection between \( G \) -invariant metrics on \( M \) and \( {I}_{p}\left( {G}_{p}\right) \) -invariant inner products on \( {T}_{p}M \) .

## Locally Homogeneous Riemannian Manifolds

A Riemannian manifold \( \left( {M, g}\right) \) is said to be locally homogeneous if for every pair of points \( p, q \in  M \) there is a Riemannian isometry from a neighborhood of \( p \) to a neighborhood of \( q \) that takes \( p \) to \( q \) . Similarly, we say that \( \left( {M, g}\right) \) is locally frame-homogeneous if for every \( p, q \in  M \) and every pair of orthonormal bases \( \left( {v}_{i}\right) \) for \( {T}_{p}M \) and \( \left( {w}_{i}\right) \) for \( {T}_{q}M \) , there is an isometry from a neighborhood of \( p \) to a neighborhood of \( q \) that takes \( p \) to \( q \) , and whose differential takes \( {v}_{i} \) to \( {w}_{i} \) for each \( i \) .

Every homogeneous Riemannian manifold is locally homogeneous, and every frame-homogeneous one is locally frame-homogeneous. Every proper open subset of a homogeneous or frame-homogeneous Riemannian manifold is locally homogeneous or locally frame-homogeneous, respectively. More interesting examples arise in the following way.

Proposition 3.20. Suppose \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a homogeneous Riemannian manifold, \( \left( {M, g}\right) \) is a Riemannian manifold, and \( \pi  : \widetilde{M} \rightarrow  M \) is a Riemannian covering. Then \( \left( {M, g}\right) \) is locally homogeneous. If \( \left( {\widetilde{M},\widetilde{g}}\right) \) is frame-homogeneous, then \( \left( {M, g}\right) \) is locally frame-homogeneous.

Exercise 3.21. Prove this proposition.

Locally homogeneous Riemannian metrics play an important role in classification theorems for manifolds, especially in low dimensions. The most fundamental case is that of compact 2-manifolds, for which we have the following important theorem.

Theorem 3.22 (Uniformization of Compact Surfaces). Every compact, connected, smooth 2-manifold admits a locally frame-homogeneous Riemannian metric, and a Riemannian covering by the Euclidean plane, hyperbolic plane, or round unit sphere.

Sketch of proof. The proof relies on the topological classification of compact surfaces (see, for example, [LeeTM, Thms. 6.15 and 10.22]), which says that every connected compact surface is homeomorphic to a sphere, a connected sum of one or more tori, or a connected sum of one or more projective planes. The crux of the proof is showing that each of the model surfaces on this list has a metric that admits a Riemannian covering by one of the model frame-homogeneous manifolds, and therefore is locally frame-homogeneous by Proposition 3.20. We consider each model surface in turn.

![bo_d7dtff491nqc73eq8m7g_88_266_237_408_371_0.jpg](images/bo_d7dtff491nqc73eq8m7g_88_266_237_408_371_0.jpg)

Fig. 3.7: A connected sum of tori

![bo_d7dtff491nqc73eq8m7g_88_855_226_383_378_0.jpg](images/bo_d7dtff491nqc73eq8m7g_88_855_226_383_378_0.jpg)

Fig. 3.8: Constructing a Riemannian covering

The 2-sphere: \( {\mathbb{S}}^{2} \) , of course, has its round metric, and the identity map is a Riemannian covering.

The 2-torus: Exercise 2.36 shows that the flat metric on \( {\mathbb{T}}^{2} \) described in Example 2.21 admits a Riemannian covering by \( \left( {{\mathbb{R}}^{2},\bar{g}}\right) \) .

A connected sum of \( n \geq  2 \) copies of \( {\mathbb{T}}^{2} \) : It is shown in [LeeTM, Example 6.13] that such a surface is homeomorphic to a quotient of a regular \( {4n} \) -sided polygonal region by side identifications indicated schematically by the sequence of labels \( {a}_{1}{b}_{1}{a}_{1}^{-1}{b}_{1}^{-1}\ldots {a}_{n}{b}_{n}{a}_{n}^{-1}{b}_{n}^{-1} \) (Fig. 3.7 illustrates the case \( n = 2 \) ). Let \( G \subseteq  \mathrm{{GL}}\left( {2,\mathbb{C}}\right) \) be the following subgroup:

\[
G = \left\{  {\left( {\frac{\alpha }{\beta }\frac{\beta }{\alpha }}\right)  : \alpha ,\beta  \in  \mathbb{C},{\left| \alpha \right| }^{2} - {\left| \beta \right| }^{2} > 0}\right\}  . \tag{3.18}
\]

Problem 3-8 shows that \( G \) acts transitively and isometrically on the Poincaré disk with its hyperbolic metric. It is shown in [LeeTM] that for each \( n \geq  2 \) , there is a discrete subgroup \( {\Gamma }_{n} \subseteq  G \) such that the quotient map \( {\mathbb{B}}^{2} \rightarrow  {\mathbb{B}}^{2}/{\Gamma }_{n} \) is a covering map, and \( {\mathbb{B}}^{2}/{\Gamma }_{n} \) is homeomorphic to a connected sum of \( n \) tori. The group is found by first identifying a compact region \( P \subseteq  {\mathbb{B}}^{2} \) bounded by a "regular geodesic polygon," which is a union of \( {4n} \) congruent circular arcs making interior angles that all measure exactly \( \pi /{2n} \) , so that \( {4n} \) of them fit together locally to fill out a neighborhood of a point (see Fig. 3.8). (The name "geodesic polygon" reflects the fact that these circular arcs are segments of geodesics with respect to the hyperbolic metric, as we will see in Chapter 5.) Then \( {\Gamma }_{n} \) is the group generated by certain elements of \( G \) that take an edge with a label \( {a}_{n} \) or \( {b}_{n} \) to the other edge with the same label. Because \( {\Gamma }_{n} \) acts isometrically, it follows that such a connected sum admits a locally frame-homogeneous metric and a Riemannian covering by the Poincaré disk. For details, see the proofs of Theorems 12.29 and 12.30 of [LeeTM].

![bo_d7dtff491nqc73eq8m7g_89_252_284_319_282_0.jpg](images/bo_d7dtff491nqc73eq8m7g_89_252_284_319_282_0.jpg)

Fig. 3.9: The Klein bottle

![bo_d7dtff491nqc73eq8m7g_89_810_185_379_381_0.jpg](images/bo_d7dtff491nqc73eq8m7g_89_810_185_379_381_0.jpg)

Fig. 3.10: Connected sum of three projective planes

The projective plane: Example 2.34 shows that \( {\mathbb{{RP}}}^{2} \) has a metric that admits a 2-sheeted Riemannian covering by \( \left( {{\mathbb{S}}^{2},\overset{ \circ  }{g}}\right) \) .

A connected sum of two copies of \( {\mathbb{{RP}}}^{2} \) : It is shown in [LeeTM, Lemma 6.16] that \( {\mathbb{{RP}}}^{2}\# {\mathbb{{RP}}}^{2} \) is homeomorphic to the Klein bottle, which is the quotient space of the unit square \( \left\lbrack  {0,1}\right\rbrack   \times  \left\lbrack  {0,1}\right\rbrack \) by the equivalence relation generated by the following relations (see Fig. 3.9):

(3.19)

\[
\left( {x,0}\right)  \sim  \left( {x,1}\right) \;\text{ for }0 \leq  x \leq  1,
\]

\[
\left( {0, y}\right)  \sim  \left( {1,1 - y}\right) \;\text{ for }0 \leq  y \leq  1.
\]

Let E(2) be the Euclidean group in two dimensions as defined earlier in this chapter, and let \( \Gamma  \subseteq  \mathrm{E}\left( 2\right) \) be the subgroup defined by

\[
\Gamma  = \left\{  {\left( {b, A}\right)  \in  \mathrm{E}\left( 2\right)  : b = \left( {k, l}\right) \text{ with }k, l \in  \mathbb{Z},\text{ and }A = \left( \begin{matrix} 1 & 0 \\  0 & {\left( -1\right) }^{k} \end{matrix}\right) }\right\}  . \tag{3.20}
\]

It turns out that \( \Gamma \) acts freely and properly on \( {\mathbb{R}}^{2} \) , and every \( \Gamma \) -orbit has a representative in the unit square such that two points in the square are in the same orbit if and only if they satisfy the equivalence relation generated by the relations in (3.19). Thus the orbit space \( {\mathbb{R}}^{2}/\Gamma \) is homeomorphic to the Klein bottle, and since the group action is isometric, it follows that the Klein bottle inherits a flat, locally frame-homogeneous metric and the quotient map is a Riemannian covering. Problem 3-18 asks you to work out the details.

A connected sum of \( n \geq  3 \) copies of \( {\mathbb{{RP}}}^{2} \) : Such a surface is homeomorphic to a quotient of a regular \( {2n} \) -sided polygonal region by side identifications according to \( {a}_{1}{a}_{1}{a}_{2}{a}_{2}\ldots {a}_{n}{a}_{n} \) [LeeTM, Example 6.13]. As in the case of a connected sum of tori, there is a compact region \( P \subseteq  {\mathbb{B}}^{2} \) bounded by a \( {2n} \) -sided regular geodesic polygon whose interior angles are all \( \pi /n \) (see Fig. 3.10), and there is a discrete group of isometries that realizes the appropriate side identifications and yields a quotient homeomorphic to the connected sum. The new ingredient here is that because such a connected sum is not orientable, we must work with the full group of isometries of \( {\mathbb{B}}^{2} \) , not just the (orientation-preserving) ones determined by elements of \( G \) ; but otherwise the argument is essentially the same as the one for connected sums of tori. The details can be found in [Ive92, Section VII.1].

There is one remaining step. The arguments above show that each compact topological 2-manifold possesses a smooth structure and a locally frame-homogeneous Riemannian metric, which admits a Riemannian covering by one of the three frame-homogeneous model spaces. However, we started with a smooth compact 2-manifold, and we are looking for a Riemannian metric that is smooth with respect to the given smooth structure. To complete the proof, we appeal to a result by James Munkres [Mun56], which shows that any two smooth structures on a 2-manifold are related by a diffeomorphism; thus after pulling back the metric by this diffeomorphism, we obtain a locally frame-homogeneous metric on \( M \) with its originally given smooth structure.

Locally homogeneous metrics also play a key role in the classification of compact 3-manifolds. In 1982, William Thurston made a conjecture about the classification of such manifolds, now known as the Thurston geometrization conjecture. The conjecture says that every compact, orientable 3-manifold can be expressed as a connected sum of compact manifolds, each of which either admits a Riemannian covering by a homogeneous Riemannian manifold or can be cut along embedded tori so that each piece admits a finite-volume locally homogeneous Riemannian metric. An important ingredient in the analysis leading up to the conjecture was his classification of all simply connected homogeneous Riemannian 3-manifolds that admit finite-volume Riemannian quotients. Thurston showed that there are exactly eight such manifolds (see [Thu97] or [Sco83] for a proof):

- \( {\mathbb{R}}^{3} \) with the Euclidean metric

- \( {\mathbb{S}}^{3} \) with a round metric

- \( {\mathbb{H}}^{3} \) with a hyperbolic metric

- \( {\mathbb{S}}^{2} \times  \mathbb{R} \) with a product of a round metric and the Euclidean metric

- \( {\mathbb{H}}^{2} \times  \mathbb{R} \) with a product of a hyperbolic metric and the Euclidean metric

- The Heisenberg group \( {H}_{1} \) of Example 3.16(g) with a left-invariant metric

- The group Sol of Example 3.16(h) with a left-invariant metric

- The universal covering group of \( \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) with a left-invariant metric

The Thurston geometrization conjecture was proved in 2003 by Grigori Perelman. The proof is described in several books [BBBMP, KL08, MF10, MT14].

## Symmetric Spaces

We end this section with a brief introduction to another class of Riemannian manifolds with abundant symmetry, called symmetric spaces. They turn out to be intermediate between frame-homogeneous and homogeneous Riemannian manifolds.

Here is the definition. If \( \left( {M, g}\right) \) is a Riemannian manifold and \( p \in  M \) , a point reflection at \( p \) is an isometry \( \varphi  : M \rightarrow  M \) that fixes \( p \) and satisfies \( d{\varphi }_{p} = \) -Id: \( {T}_{p}M \rightarrow  {T}_{p}M \) . A Riemannian manifold \( \left( {M, g}\right) \) is called a (Riemannian) symmetric space if it is connected and for each \( p \in  M \) there exists a point reflection at p. (The modifier "Riemannian" is included to distinguish such spaces from other kinds of symmetric spaces that can be defined, such as pseudo-Riemannian symmetric spaces and affine symmetric spaces; since we will be concerned only with Riemannian symmetric spaces, we will sometimes refer to them simply as "symmetric spaces" for brevity.)

Although we do not yet have the tools to prove it, we will see later that every Riemannian symmetric space is homogeneous (see Problem 6-19). More generally, \( \left( {M, g}\right) \) is called a (Riemannian) locally symmetric space if each \( p \in  M \) has a neighborhood \( U \) on which there exists an isometry \( \varphi  : U \rightarrow  U \) that is a point reflection at p. Clearly every Riemannian symmetric space is locally symmetric.

The next lemma can be used to facilitate the verification that a given Riemannian manifold is symmetric.

Lemma 3.23. If \( \left( {M, g}\right) \) is a connected homogeneous Riemannian manifold that possesses a point reflection at one point, then it is symmetric.

Proof. Suppose \( \left( {M, g}\right) \) satisfies the hypothesis, and let \( \varphi  : M \rightarrow  M \) be a point reflection at \( p \in  M \) . Given any other point \( q \in  M \) , by homogeneity there is an isometry \( \psi  : M \rightarrow  M \) satisfying \( \psi \left( p\right)  = q \) . Then \( \widetilde{\varphi } = \psi  \circ  \varphi  \circ  {\psi }^{-1} \) is an isometry that fixes \( q \) . Because \( d{\psi }_{p} \) is linear, it commutes with multiplication by -1, so

\[
d{\widetilde{\varphi }}_{q} = d{\psi }_{p} \circ  \left( {-{\operatorname{Id}}_{{T}_{pM}}}\right)  \circ  d{\left( {\psi }^{-1}\right) }_{q} = \left( {-{\operatorname{Id}}_{{T}_{qM}}}\right)  \circ  d{\psi }_{p} \circ  d{\left( {\psi }^{-1}\right) }_{q}
\]

\[
=  - {\operatorname{Id}}_{{T}_{qM}}\text{ . }
\]

Thus \( \widetilde{\varphi } \) is a point reflection at \( q \) .

Example 3.24 (Riemannian Symmetric Spaces).

(a) Suppose \( \left( {M, g}\right) \) is any connected frame-homogeneous Riemannian manifold. Then for each \( p \in  M \) , we can choose an orthonormal basis \( \left( {b}_{i}\right) \) for \( {T}_{p}M \) , and frame homogeneity guarantees that there is an isometry \( \varphi  : M \rightarrow  M \) that fixes \( p \) and sends \( \left( {b}_{i}\right) \) to \( \left( {-{b}_{i}}\right) \) , which implies that \( d{\varphi }_{p} =  - \mathrm{{Id}} \) . Thus every frame-homogeneous Riemannian manifold is a symmetric space. In particular, all Euclidean spaces, spheres, and hyperbolic spaces are symmetric.

(b) Suppose \( G \) is a connected Lie group with a bi-invariant Riemannian metric \( g \) . If we define \( \Phi  : G \rightarrow  G \) by \( \Phi \left( x\right)  = {x}^{-1} \) , then it is straightforward to check that \( d{\Phi }_{e}\left( v\right)  =  - v \) for every \( v \in  {T}_{e}G \) , from which it follows that \( d{\Phi }_{e}^{ * }\left( {g}_{e}\right)  = \; {g}_{e} \) . To see that \( \Phi \) is an isometry, let \( p \in  G \) be arbitrary. The identity \( {q}^{-1} = \; {\left( {p}^{-1}q\right) }^{-1}{p}^{-1} \) for all \( q \in  G \) implies that \( \Phi  = {R}_{{p}^{-1}} \circ  \Phi  \circ  {L}_{{p}^{-1}} \) , and therefore it follows from bi-invariance of \( g \) that

\[
{\left( {\Phi }^{ * }g\right) }_{p} = d{\Phi }_{p}^{ * }{g}_{{p}^{-1}} = d{\left( {L}_{{p}^{-1}}\right) }_{p}^{ * } \circ  d{\Phi }_{e}^{ * } \circ  d{\left( {R}_{{p}^{-1}}\right) }_{e}^{ * }{g}_{{p}^{-1}} = {g}_{p}.
\]

Therefore \( \Phi \) is an isometry of \( g \) and hence a point reflection at \( e \) . Lemma 3.23 then implies that \( \left( {G, g}\right) \) is a symmetric space.

(c) The complex projective spaces introduced in Example 2.30 and the Grassmann manifolds introduced in Problem 2-7 are all Riemannian symmetric spaces (see Problems 3-19 and 3-20).

(d) Every product of Riemannian symmetric spaces is easily seen to be a symmetric space when endowed with the product metric. A symmetric space is said to be irreducible if it is not isometric to a product of positive-dimensional symmetric spaces.

## Model Pseudo-Riemannian Manifolds

The definitions of the Euclidean, spherical, and hyperbolic metrics can easily be adapted to give analogous classes of frame-homogeneous pseudo-Riemannian manifolds.

The first example is one we have already seen: the pseudo-Euclidean space of signature \( \left( {r, s}\right) \) is the pseudo-Riemannian manifold \( \left( {{\mathbb{R}}^{r, s},{\bar{q}}^{\left( r, s\right) }}\right) \) , where \( {\bar{q}}^{\left( r, s\right) } \) is the pseudo-Riemannian metric defined by (2.24).

There are also pseudo-Riemannian analogues of the spherical and hyperbolic metrics. For nonnegative integers \( r \) and \( s \) and a positive real number \( R \) , we define the pseudosphere \( \left( {{\mathbb{S}}^{r, s}\left( R\right) ,{\overset{ \circ  }{q}}_{R}^{\left( r, s\right) }}\right) \) and the pseudohyperbolic space \( \left( {{\mathbb{H}}^{r, s}\left( R\right) ,{\overset{ \circ  }{q}}_{R}^{\left( r, s\right) }}\right) \) as follows. As manifolds, \( {\mathbb{S}}^{r, s}\left( R\right)  \subseteq  {\mathbb{R}}^{r + 1, s} \) and \( {\mathbb{H}}^{r, s}\left( R\right)  \subseteq  {\mathbb{R}}^{r, s + 1} \) are defined by

\[
{\mathbb{S}}^{r, s}\left( R\right)  = \left\{  {\left( {\xi ,\tau }\right)  : {\left( {\xi }^{1}\right) }^{2} + \cdots  + {\left( {\xi }^{r + 1}\right) }^{2} - {\left( {\tau }^{1}\right) }^{2} - \cdots  - {\left( {\tau }^{s}\right) }^{2} = {R}^{2}}\right\}  ,
\]

\[
{\mathbb{H}}^{r, s}\left( R\right)  = \left\{  {\left( {\xi ,\tau }\right)  : {\left( {\xi }^{1}\right) }^{2} + \cdots  + {\left( {\xi }^{r}\right) }^{2} - {\left( {\tau }^{1}\right) }^{2} - \cdots  - {\left( {\tau }^{s + 1}\right) }^{2} =  - {R}^{2}}\right\}  .
\]

The metrics are the ones induced from the respective pseudo-Euclidean metrics: \( {\overset{ \circ  }{q}}_{R}^{\left( r, s\right) } = {\iota }^{ * }{\bar{q}}^{\left( r + 1, s\right) } \) on \( {\mathbb{S}}^{r, s}\left( R\right) \) , and \( {\breve{q}}_{R}^{\left( r, s\right) } = {\iota }^{ * }{\bar{q}}^{\left( r, s + 1\right) } \) on \( {\mathbb{H}}^{r, s}\left( R\right) \) .

Theorem 3.25. For all \( r, s \) , and \( R \) as above, \( {\mathbb{S}}^{r, s}\left( R\right) \) and \( {\mathbb{H}}^{r, s}\left( R\right) \) are pseudo-Riemannian manifolds of signature \( \left( {r, s}\right) \) .

Proof. Problem 3-22.

It turns out that these pseudo-Riemannian manifolds all have the same degree of symmetry as the three classes of model Riemannian manifolds introduced earlier. For pseudo-Riemannian manifolds, though, it is necessary to modify the definition of frame homogeneity slightly. If \( \left( {M, g}\right) \) is a pseudo-Riemannian manifold of signature \( \left( {r, s}\right) \) , let us say that an orthonormal basis for some tangent space \( {T}_{p}M \) is in standard order if the expression for \( {g}_{p} \) in terms of the dual basis \( \left( {\varepsilon }^{i}\right) \) is \( {\left( {\varepsilon }^{1}\right) }^{2} + \cdots  + {\left( {\varepsilon }^{r}\right) }^{2} - {\left( {\varepsilon }^{r + 1}\right) }^{2} - \cdots  - {\left( {\varepsilon }^{r + s}\right) }^{2} \) , with all positive terms coming before the negative terms. With this understanding, we define \( \mathrm{O}\left( M\right) \) to be the set of all standard-ordered orthonormal bases for all tangent spaces to \( M \) , and we say that \( \left( {M, g}\right) \) is frame-homogeneous if the isometry group acts transitively on \( \mathrm{O}\left( M\right) \) .

Theorem 3.26. All pseudo-Euclidean spaces, pseudospheres, and pseudohyperbolic spaces are frame-homogeneous.

In the particular case of signature \( \left( {n,1}\right) \) , the Lorentz manifolds \( \left( {{\mathbb{S}}^{n,1}\left( R\right) ,{\overset{ \circ  }{q}}_{R}^{\left( n,1\right) }}\right) \) and \( \left( {{\mathbb{H}}^{n,1}\left( R\right) ,{\breve{q}}_{R}^{\left( n,1\right) }}\right) \) are called de Sitter space of radius \( R \) and anti-de Sitter space of radius \( R \) , respectively.

## Problems

3-1. Show that (3.2) defines a smooth isometric action of \( \mathrm{E}\left( n\right) \) on \( \left( {{\mathbb{R}}^{n},\bar{g}}\right) \) , and the induced action on \( \mathrm{O}\left( {\mathbb{R}}^{n}\right) \) is transitive. (Used on p. 57.)

3-2. Prove that the metric on \( {\mathbb{{RP}}}^{n} \) described in Example 2.34 is frame-homogeneous. (Used on p. 145)

3-3. Prove Proposition 3.1 (about homogeneous and isotropic Riemannian manifolds).

3-4. Complete the proof of Theorem 3.7 by showing that \( {\kappa }^{ * }{\breve{g}}_{R}^{3} = {\breve{g}}_{R}^{4} \) .

3-5. (a) Prove that \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) is isometric to \( \left( {{\mathbb{S}}^{n},{R}^{2}\overset{ \circ  }{g}}\right) \) for each \( R > 0 \) .

(b) Prove that \( \left( {{\mathbb{H}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) is isometric to \( \left( {{\mathbb{H}}^{n},{R}^{2}\breve{g}}\right) \) for each \( R > 0 \) .

(c) We could also have defined a family of metrics on \( {\mathbb{R}}^{n} \) by \( {\bar{g}}_{R} = {R}^{2}\bar{g} \) . Why did we not bother?

(Used on p. 185.)

3-6. Show that two Riemannian metrics \( {g}_{1} \) and \( {g}_{2} \) are conformal if and only if they define the same angles but not necessarily the same lengths, and that a diffeomorphism is a conformal equivalence if and only if it preserves angles. [Hint: Let \( \left( {E}_{i}\right) \) be a local orthonormal frame for \( {g}_{1} \) , and consider the \( {g}_{2} \) -angle between \( {E}_{i} \) and \( \left. {\left. {\left( {\cos \theta }\right) {E}_{i} + \left( {\sin \theta }\right) {E}_{j}\text{ . }}\right) \text{ (Used on p. 59. }}\right\rbrack \)

3-7. Let \( {\mathbb{U}}^{2} \) denote the upper half-plane model of the hyperbolic plane (of radius 1), with the metric \( \breve{g} = \left( {d{x}^{2} + d{y}^{2}}\right) /{y}^{2} \) . Let \( \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) denote the group of \( 2 \times  2 \) real matrices of determinant 1 . Regard \( {\mathbb{U}}^{2} \) as a subset of the complex plane with coordinate \( z = x + {iy} \) , and let

\[
A \cdot  z = \frac{{az} + b}{{cz} + d},\;A = \left( \begin{array}{ll} a & b \\  c & d \end{array}\right)  \in  \mathrm{{SL}}\left( {2,\mathbb{R}}\right) .
\]

Show that this defines a smooth, transitive, orientation-preserving, and isometric action of \( \mathrm{{SL}}\left( {2,\mathbb{R}}\right) \) on \( \left( {{\mathbb{U}}^{2},\breve{g}}\right) \) . Is the induced action transitive on \( \mathrm{O}\left( {\mathbb{U}}^{2}\right) ? \)

3-8. Let \( {\mathbb{B}}^{2} \) denote the Poincaré disk model of the hyperbolic plane (of radius 1), with the metric \( \breve{g} = \left( {d{u}^{2} + d{v}^{2}}\right) /{\left( 1 - {u}^{2} - {v}^{2}\right) }^{2} \) , and let \( G \subseteq  \mathrm{{GL}}\left( {2,\mathbb{C}}\right) \) be the subgroup defined by (3.18). Regarding \( {\mathbb{B}}^{2} \) as a subset of the complex plane with coordinate \( w = u + {iv} \) , let \( G \) act on \( {\mathbb{B}}^{2} \) by

\[
\left( {\frac{\alpha }{\beta }\frac{\beta }{\overline{\alpha }}}\right)  \cdot  w = \frac{{\alpha z} + \beta }{\overline{\beta }z + \overline{\alpha }}.
\]

Show that this defines a smooth, transitive, orientation-preserving, and isometric action of \( G \) on \( \left( {{\mathbb{B}}^{2},\breve{g}}\right) \) . [Hint: One way to proceed is to define an action of \( G \) on the upper half-plane by \( A \cdot  z = {\kappa }^{-1} \circ  A \circ  \kappa \left( z\right) \) , where \( \kappa \) is the Cayley transform defined by (3.14) in the case \( R = 1 \) , and use the result of Problem 3-7.] (Used on pp. 73, 185.)

3-9. Suppose \( G \) is a compact Lie group with a left-invariant metric \( g \) and a left-invariant orientation. Show that the Riemannian volume form \( d{V}_{g} \) is bi-invariant. [Hint: Show that \( d{V}_{g} \) is equal to the Riemannian volume form for a bi-invariant metric.]

3-10. Consider the basis

\[
X = \left( \begin{array}{rr} 0 & 1 \\   - 1 & 0 \end{array}\right) ,\;Y = \left( \begin{array}{ll} 0 & i \\  i & 0 \end{array}\right) ,\;Z = \left( \begin{array}{rr} i & 0 \\  0 &  - i \end{array}\right)
\]

for the Lie algebra \( \mathfrak{{su}}\left( 2\right) \) . For each positive real number \( a \) , define a left-invariant metric \( {g}_{a} \) on the group \( \mathrm{{SU}}\left( 2\right) \) by declaring \( X, Y,{aZ} \) to be an orthonormal frame.

(a) Show that \( {g}_{a} \) is bi-invariant if and only if \( a = 1 \) .

(b) Show that the map defined by (3.16) is an isometry between \( \left( {{\mathbb{S}}^{3},\overset{ \circ  }{g}}\right) \) and \( \left( {\mathrm{{SU}}\left( 2\right) ,{g}_{1}}\right) \) . [Remark: \( \mathrm{{SU}}\left( 2\right) \) with any of these metrics is called a Berger sphere, named after Marcel Berger.]

(Used on pp. 56, 71, 259.)

3-11. Prove that the formula \( \langle A, B\rangle  = \operatorname{tr}\left( {{A}^{T}B}\right) \) defines a bi-invariant Riemannian metric on \( \mathrm{O}\left( n\right) \) . (See Example 3.16(e).)

3-12. Regard the upper half-space \( {\mathbb{U}}^{n} \) as a Lie group as described in Example 3.16(f).

(a) Show that for each \( R > 0 \) , the hyperbolic metric \( {\breve{g}}_{R}^{4} \) on \( {\mathbb{U}}^{n} \) is left-invariant.

(b) Show that \( {\mathbb{U}}^{n} \) does not admit any bi-invariant metrics.

(Used on pp. 68, 72.)

3-13. Write down an explicit formula for an arbitrary left-invariant metric on the Heisenberg group \( {H}_{n} \) of Example 3.16(g) in terms of global coordinates \( \left( {{x}^{1},\ldots ,{x}^{n},{y}^{1},\ldots ,{y}^{n}, z}\right) \) , and show that the group has no bi-invariant metrics. (Used on pp. 68, 72.)

3-14. Repeat Problem 3-13 for the group Sol of Example 3.16(h). (Used on p. 72.)

3-15. Let \( {\mathbb{R}}^{n,1} \) be the \( \left( {n + 1}\right) \) -dimensional Minkowski space with coordinates \( \left( {\xi ,\tau }\right)  = \left( {{\xi }^{1},\ldots ,{\xi }^{n},\tau }\right) \) and with the Minkowski metric \( {\bar{q}}^{\left( n,1\right) } = \mathop{\sum }\limits_{i}d{\left( {\xi }^{i}\right) }^{2} - \; d{\tau }^{2} \) . Let \( S \subseteq  {\mathbb{R}}^{n,1} \) be the set

\[
S = \left\{  {\left( {\xi ,\tau }\right)  : {\left( {\xi }^{1}\right) }^{2} + \cdots  + {\left( {\xi }^{n}\right) }^{2} = \tau  = 1}\right\}  .
\]

(a) Prove that \( S \) is a smooth submanifold diffeomorphic to \( {\mathbb{S}}^{n - 1} \) , and with the induced metric \( g = {\iota }_{S}^{ * }{\bar{q}}^{\left( n,1\right) } \) it is isometric to the round unit \( \left( {n - 1}\right) \) - sphere.

(b) Define an action of the orthochronous Lorentz group \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) on \( S \) as follows: For every \( p \in  S \) , let \( \langle p\rangle \) denote the 1-dimensional subspace of \( {\mathbb{R}}^{n,1} \) spanned by \( p \) . Given \( A \in  {\mathrm{O}}^{ + }\left( {n,1}\right) \) , show that the image set \( A\left( {\langle p\rangle }\right) \) is a 1-dimensional subspace that intersects \( S \) in exactly one point, so we can define \( A \cdot  p \) to be the unique point in \( S \cap  A\left( {\langle p\rangle }\right) \) . Prove that this is a smooth transitive action on \( S \) .

(c) Prove that \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) acts by conformal diffeomorphisms of \( \left( {S, g}\right) \) .

3-16. Prove that there is no Riemannian metric on the sphere that is invariant under the group action described in Problem 3-15.

3-17. Given a Lie group \( G \) , define an action of the product group \( G \times  G \) on \( G \) by \( \left( {{\varphi }_{1},{\varphi }_{2}}\right)  \cdot  \psi  = {\varphi }_{1}\psi {\varphi }_{2}^{-1} \) . Show that this action is transitive, and that the isotropy group of the identity is the diagonal subgroup \( \Delta  = \{ \left( {\varphi ,\varphi }\right)  : \varphi  \in  G\} \) . Then show that the following diagram commutes:

![bo_d7dtff491nqc73eq8m7g_95_620_923_347_213_0.jpg](images/bo_d7dtff491nqc73eq8m7g_95_620_923_347_213_0.jpg)

where \( {I}_{e} \) is the isotropy representation of \( \Delta \) and \( \mathfrak{g} \) is the Lie algebra of \( G \) , and use this to give an alternative proof of Theorem 3.14.

3-18. Let \( \Gamma  \subseteq  \mathrm{E}\left( 2\right) \) be the subgroup defined by (3.20). Prove that \( \Gamma \) acts freely and properly on \( {\mathbb{R}}^{2} \) and the orbit space is homeomorphic to the Klein bottle, and conclude that the Klein bottle has a flat metric and a Riemannian covering by the Euclidean plane.

3-19. Show that the Fubini-Study metric on \( {\mathbb{{CP}}}^{n} \) (Example 2.30) is homogeneous, isotropic, and symmetric. (Used on p. 78.)

3-20. Show that the metric on the Grassmannian \( {\mathrm{G}}_{k}\left( {\mathbb{R}}^{n}\right) \) defined in Problem 2-7 is homogeneous, isotropic, and symmetric. (Used on p. 78.)

3-21. Let \( \left( {\widetilde{M},\widetilde{g}}\right) \) be a simply connected Riemannian manifold, and suppose \( {\Gamma }_{1} \) and \( {\Gamma }_{2} \) are countable subgroups of \( \operatorname{Iso}\left( {\widetilde{M},\widetilde{g}}\right) \) acting smoothly, freely, and properly on \( M \) (when endowed with the discrete topology). For \( i = 1,2 \) , let \( {M}_{i} = \widetilde{M}/{\Gamma }_{i} \) , and let \( {g}_{i} \) be the Riemannian metric on \( {M}_{i} \) that makes the quotient map \( {\pi }_{i} : \widetilde{M} \rightarrow  {M}_{i} \) a Riemannian covering (see Prop. 2.32). Prove that the Riemannian manifolds \( \left( {{M}_{1},{g}_{1}}\right) \) and \( \left( {{M}_{2},{g}_{2}}\right) \) are isometric if and only if \( {\Gamma }_{1} \) and \( {\Gamma }_{2} \) are conjugate subgroups of \( \operatorname{Iso}\left( {\widetilde{M},\widetilde{g}}\right) \) .

3-22. Prove Theorem 3.25 (showing that pseudospheres and pseudohyperbolic spaces are pseudo-Riemannian manifolds). [Hint: Mimic the argument in the proof of Theorem 3.7 that \( {\mathbb{H}}^{n}\left( R\right) \) is Riemannian.]

3-23. Prove Theorem 3.26 (pseudo-Euclidean spaces, pseudospheres, and pseudo-hyperbolic spaces are frame-homogeneous).

3-24. Prove that for all positive integers \( r \) and \( s \) and every real number \( R > 0 \) , both the pseudohyperbolic space \( {\mathbb{H}}^{r, s}\left( R\right) \) and the pseudosphere \( {\mathbb{S}}^{s, r}\left( R\right) \) are diffeomorphic to \( {\mathbb{R}}^{r} \times  {\mathbb{S}}^{s} \) . [Hint: Consider the maps \( \varphi ,\psi  : {\mathbb{R}}^{r} \times  {\mathbb{S}}^{s} \rightarrow  {\mathbb{R}}^{r + s + 1} \) given by

\[
\varphi \left( {x, y}\right)  = \left( {{Rx},\left( \sqrt{1 + {\left| x\right| }^{2}}\right) {Ry}}\right) ,\;\psi \left( {x, y}\right)  = \left( {\left( \sqrt{1 + {\left| x\right| }^{2}}\right) {Ry},{Rx}}\right) .\rbrack
\]

3-25. Let \( \left( {{\mathbb{K}}^{r}\left( R\right) ,{\breve{g}}_{R}^{2}}\right) \) be the \( r \) -dimensional ball of radius \( R \) with the Beltrami-Klein metric (3.9), and let \( {\widetilde{\mathbb{H}}}^{r,1}\left( R\right) \) be the product manifold \( {\mathbb{K}}^{r}\left( R\right)  \times  \mathbb{R} \) with the pseudo-Riemannian warped product metric \( q = {\breve{g}}_{R}^{2} \oplus  \left( {-{f}^{2}d{t}^{2}}\right) \) , where \( f : {\mathbb{K}}^{r}\left( R\right)  \rightarrow  {\mathbb{R}}^{ + } \) is given by

\[
f\left( w\right)  = \frac{{R}^{2}}{\sqrt{{R}^{2} - {\left| w\right| }^{2}}}.
\]

Define \( F : {\widetilde{\mathbb{H}}}^{r,1}\left( R\right)  \rightarrow  {\mathbb{R}}^{r,2} \) by

\[
F\left( {w, t}\right)  = \frac{\left( Rw,{R}^{2}\cos t,{R}^{2}\sin t\right) }{\sqrt{{R}^{2} - {\left| w\right| }^{2}}}.
\]

Prove that the image of \( F \) is the anti-de Sitter space \( {\mathbb{H}}^{r,1}\left( R\right) \) , and \( F \) defines a pseudo-Riemannian covering of \( \left( {{\mathbb{H}}^{r,1}\left( R\right) ,{q}_{R}^{\left( r,1\right) }}\right) \) by \( \left( {{\widetilde{\mathbb{H}}}^{r,1}\left( R\right) , q}\right) \) . [Remark: We are tacitly extending the notions of warped product metric and Riemannian coverings to the pseudo-Riemannian case in the obvious ways. It follows from the result of Problem 3-24 that \( {\mathbb{H}}^{r, s}\left( R\right) \) is simply connected when \( s \geq  2 \) but \( {\mathbb{H}}^{r,1}\left( R\right) \) is not. This shows that \( \left( {{\widetilde{\mathbb{H}}}^{r,1}\left( R\right) , q}\right) \) , called universal anti-de Sitter space of radius \( \mathbf{R} \) , is the universal pseudo-Riemannian covering manifold of \( \left( {{\mathbb{H}}^{r,1}\left( R\right) ,{q}_{R}^{\left( r,1\right) }}\right) \) .]
