## Chapter 12 Curvature and Topology

In this final chapter, we bring together most of the tools we have developed so far to prove some significant local-to-global theorems relating curvature and topology of Riemannian manifolds.

We focus first on constant-curvature manifolds. The main result here is the Killing-Hopf theorem, which shows that every complete, simply connected manifold with constant sectional curvature is isometric to one of our frame-homogeneous model spaces. A corollary of the theorem then shows that the ones that are not simply connected are just quotients of the models by discrete groups of isometries. The technique used to prove this result also leads to a global characterization of symmetric spaces in terms of parallel curvature tensors.

Next we turn to nonpositively curved manifolds. The primary result is the Cartan-Hadamard theorem, which topologically characterizes complete, simply connected manifolds with nonpositive sectional curvature: they are all diffeomorphic to \( {\mathbb{R}}^{n} \) . After proving the main result, we prove two other theorems, due to Cartan and Preissman, that place severe restrictions on the fundamental groups of complete manifolds with nonpositive or negative curvature.

Finally, we address the case of positive curvature. The main theorem is Myers's theorem, which says that a complete manifold with Ricci curvature bounded below by a positive constant must be compact and have a finite fundamental group and diameter no larger than that of the sphere with the same Ricci curvature. The borderline case is addressed by Cheng's maximal diameter theorem, which says that the diameter bound is achieved only by a round sphere. These results are supplemented by theorems of Milnor and Synge, which further restrict the topology of manifolds with nonnegative Ricci and positive sectional curvature, respectively.

## Manifolds of Constant Curvature

Our first major local-to-global theorem is a global characterization of complete manifolds of constant curvature. If \( \left( {M, g}\right) \) has constant sectional curvature, Corollary

![bo_d7dtff491nqc73eq8m7g_355_239_188_1051_492_0.jpg](images/bo_d7dtff491nqc73eq8m7g_355_239_188_1051_492_0.jpg)

Fig. 12.1: Analytic continuation of a local isometry

10.15 shows that each point of \( M \) has a neighborhood that is isometric to an open subset of one of the constant-curvature model spaces of Chapter 3. In order to turn that into a global result, we use a technique modeled on the theory of analytic continuation in complex analysis.

Suppose \( \left( {M, g}\right) \) and \( \left( {\widehat{M},\widehat{g}}\right) \) are Riemannian manifolds of the same dimension and \( \varphi  : U \rightarrow  \widehat{M} \) is a local isometry defined on some connected open subset \( U \subseteq  M \) . If \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) is a continuous path such that \( \gamma \left( 0\right)  \in  U \) , then an analytic continuation of \( \varphi \) along \( \gamma \) is a family of pairs \( \left\{  {\left( {{U}_{t},{\varphi }_{t}}\right)  : t \in  \left\lbrack  {0,1}\right\rbrack  }\right\} \) , where \( {U}_{t} \) is a connected neighborhood of \( \gamma \left( t\right) \) and \( {\varphi }_{t} : {U}_{t} \rightarrow  \widehat{M} \) is a local isometry, such that \( {\varphi }_{0} = \varphi \) on \( {U}_{0} \cap  U \) , and for each \( t \in  \left\lbrack  {0,1}\right\rbrack \) there exists \( \delta  > 0 \) such that \( \left| {t - {t}_{1}}\right|  < \delta \) implies that \( \gamma \left( {t}_{1}\right)  \in  {U}_{t} \) and that \( {\varphi }_{t} \) agrees with \( {\varphi }_{{t}_{1}} \) on \( {U}_{t} \cap  {U}_{{t}_{1}} \) (see Fig. 12.1). Note that we require \( {\varphi }_{t} \) and \( {\varphi }_{{t}_{1}} \) to agree where they overlap only if \( t \) and \( {t}_{1} \) are sufficiently close; in particular, if \( \gamma \) is not injective, the values of the analytic continuation may differ at different times at which \( \gamma \) returns to the same point. However, as the next lemma shows, all analytic continuations along the same path will end up with the same value.

Lemma 12.1 (Uniqueness of Analytic Continuation). With \( \left( {M, g}\right) ,\left( {\widehat{M},\widehat{g}}\right) \) , and \( \varphi \) as above, if \( \left\{  \left( {{U}_{t},{\varphi }_{t}}\right) \right\} \) and \( \left\{  \left( {{U}_{t}^{\prime },{\varphi }_{t}^{\prime }}\right) \right\} \) are two analytic continuations of \( \varphi \) along the same path \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) , then \( {\varphi }_{1} = {\varphi }_{1}^{\prime } \) on a neighborhood of \( \gamma \left( 1\right) \) .

Proof. Let \( \mathcal{T} \) be the set of all \( t \in  \left\lbrack  {0,1}\right\rbrack \) such that \( {\varphi }_{t} = {\varphi }_{t}^{\prime } \) on a neighborhood of \( \gamma \left( t\right) \) . Then \( 0 \in  \mathcal{T} \) , because both \( {\varphi }_{0} \) and \( {\varphi }_{0}^{\prime } \) agree with \( \varphi \) on a neighborhood of \( \gamma \left( 0\right) \) . We will show that \( \mathcal{T} \) is open and closed in \( \left\lbrack  {0,1}\right\rbrack \) , from which it follows that \( 1 \in  \mathcal{T} \) , which proves the lemma.

To see that it is open, suppose \( t \in  \mathcal{T} \) . By the definition of analytic continuation, there is some \( \delta  > 0 \) such that if \( {t}_{1} \in  \left\lbrack  {0,1}\right\rbrack \) and \( \left| {{t}_{1} - t}\right|  < \delta \) , then \( {\varphi }_{{t}_{1}} \) and \( {\varphi }_{{t}_{1}}^{\prime } \) both agree with \( {\varphi }_{t} \) on a neighborhood of \( \gamma \left( t\right) \) , so \( \left\lbrack  {0,1}\right\rbrack   \cap  \left( {t - \delta , t + \delta }\right)  \subseteq  \mathcal{T} \) . Thus \( \mathcal{T} \) is open.

To see that it is closed, suppose \( t \) is a limit point of \( \mathcal{T} \) . There is a sequence \( {t}_{i} \rightarrow  t \) such that \( {t}_{i} \in  \mathcal{T} \) , which means that \( {\varphi }_{{t}_{i}} = {\varphi }_{{t}_{i}}^{\prime } \) on a neighborhood of \( {t}_{i} \) for each \( i \) . By definition of analytic continuation, for \( i \) large enough, we have \( \gamma \left( {t}_{i}\right)  \in  {U}_{t} \cap  {U}_{t}^{\prime } \) and \( {\varphi }_{t} = {\varphi }_{{t}_{i}} = {\varphi }_{{t}_{i}}^{\prime } = {\varphi }_{t}^{\prime } \) on a neighborhood of \( \gamma \left( {t}_{i}\right) \) . In particular, this means that \( {\varphi }_{t}\left( {\gamma \left( {t}_{i}\right) }\right)  = {\varphi }_{t}^{\prime }\left( {\gamma \left( {t}_{i}\right) }\right) \) and \( d{\left( {\varphi }_{t}\right) }_{\gamma \left( {t}_{i}\right) } = d{\left( {\varphi }_{t}^{\prime }\right) }_{\gamma \left( {t}_{i}\right) } \) for each such \( i \) . By continuity, therefore, \( {\varphi }_{t}\left( {\gamma \left( t\right) }\right)  = {\varphi }_{t}^{\prime }\left( {\gamma \left( t\right) }\right) \) and \( d{\left( {\varphi }_{t}\right) }_{\gamma \left( t\right) } = d{\left( {\varphi }_{t}^{\prime }\right) }_{\gamma \left( t\right) } \) . Proposition 5.22 shows that \( {\varphi }_{t} = {\varphi }_{t}^{\prime } \) on a neighborhood of \( \gamma \left( t\right) \) , so \( t \in  \mathcal{T} \) .

The previous lemma shows that all analytic continuations along the same path end up with the same value. But when we consider analytic continuations along different paths, this may not be the case. The next theorem gives a sufficient condition for analytic continuations along two different paths to result in the same value.

Theorem 12.2 (Monodromy Theorem for Local Isometries). Let \( \left( {M, g}\right) \) and \( \left( {\widehat{M},\widehat{g}}\right) \) be connected Riemannian manifolds. Suppose \( U \) is a neighborhood of a point \( p \in  M \) and \( \varphi  : U \rightarrow  \widehat{M} \) is a local isometry that can be analytically continued along every path starting at \( p \) . If \( {\gamma }_{0},{\gamma }_{1} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) are path-homotopic paths from \( p \) to a point \( q \in  M \) , then the analytic continuations along \( {\gamma }_{0} \) and \( {\gamma }_{1} \) agree in a neighborhood of \( q \) .

Proof. Suppose \( {\gamma }_{0} \) and \( {\gamma }_{1} \) are path-homotopic, and let \( H : \left\lbrack  {0,1}\right\rbrack   \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be a path homotopy from \( {\gamma }_{0} \) to \( {\gamma }_{1} \) . Write \( {H}_{s}\left( t\right)  = H\left( {t, s}\right) \) , so that \( {H}_{0} = {\gamma }_{0},{H}_{1} = {\gamma }_{1} \) , and \( {H}_{s}\left( 0\right)  = p \) and \( {H}_{s}\left( 1\right)  = q \) for all \( s \in  \left\lbrack  {0,1}\right\rbrack \) . The hypothesis implies that for each \( s \in  \left\lbrack  {0,1}\right\rbrack \) , there is an analytic continuation of \( \varphi \) along \( {H}_{s} \) , which we denote by \( \left\{  {\left( {{U}_{t}^{\left( s\right) },{\varphi }_{t}^{\left( s\right) }}\right)  : t \in  \left\lbrack  {0,1}\right\rbrack  }\right\} \) .

Consider the function \( P : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \widehat{M} \) given by \( P\left( s\right)  = {\varphi }_{1}^{\left( s\right) }\left( q\right) \) . Given \( s \in  \left\lbrack  {0,1}\right\rbrack \) , if \( {s}^{\prime } \) is sufficiently close to \( s \) , it follows from compactness of \( {H}_{s}\left( \left\lbrack  {0,1}\right\rbrack  \right) \) that the same family \( \left\{  {\left( {{U}_{t}^{\left( s\right) },{\varphi }_{t}^{\left( s\right) }}\right)  : t \in  \left\lbrack  {0,1}\right\rbrack  }\right\} \) serves as an analytic continuation along \( {H}_{{s}^{\prime }} \) . This means that \( P\left( s\right) \) is locally constant as a function of \( s \) , so \( {\varphi }_{1}^{\left( 1\right) }\left( q\right)  = {\varphi }_{1}^{\left( 0\right) }\left( q\right) \) . Since a path from \( p \) to \( q \) can easily be modified near \( q \) to yield a path from \( p \) to any point \( {q}^{\prime } \) sufficiently nearby, and the same analytic continuation works for the modified path, it follows from the same argument that \( {\varphi }_{1}^{\left( 1\right) }\left( {q}^{\prime }\right)  = {\varphi }_{1}^{\left( 0\right) }\left( {q}^{\prime }\right) \) for all \( {q}^{\prime } \) in a neighborhood of \( q \) .

Corollary 12.3. Let \( \left( {M, g}\right) \) and \( \left( {\widehat{M},\widehat{g}}\right) \) be simply connected, complete Riemannian manifolds. Suppose \( U \) is a connected neighborhood of a point \( p \in  M \) and \( \varphi  : U \rightarrow \; \widehat{M} \) is a local isometry that can be analytically continued along every path starting at \( p \) . Then there is a global isometry \( \Phi  : M \rightarrow  \widehat{M} \) whose restriction to \( U \) agrees with \( \varphi \) .

Proof. Let \( q \in  M \) be arbitrary. We wish to define \( \Phi \left( q\right) \) to be the value of an analytic continuation of \( \varphi \) along a path from \( p \) to \( q \) . The fact that \( M \) is simply connected means that all paths from \( p \) to \( q \) are path-homotopic, so the monodromy theorem implies that all such analytic continuations agree in a neighborhood of \( q \) ; thus \( \Phi \) is well defined. Because it is a globally defined local isometry and \( M \) is complete, it follows from Theorem 6.23 that \( \Phi \) is a Riemannian covering map. Since \( \widehat{M} \) is simply connected, every covering of \( \widehat{M} \) is bijective by Corollary A.59, so \( \Phi \) is a bijective local isometry and thus a global isometry.

![bo_d7dtff491nqc73eq8m7g_357_193_183_1152_546_0.jpg](images/bo_d7dtff491nqc73eq8m7g_357_193_183_1152_546_0.jpg)

Fig. 12.2: Proof of the Killing-Hopf theorem

The next theorem, due to Wilhelm Killing and Heinz Hopf, is the main result of this section.

Theorem 12.4 (Killing-Hopf). Let \( \left( {M, g}\right) \) be a complete, simply connected Riemannian \( n \) -manifold with constant sectional curvature, \( n \geq  2 \) . Then \( M \) is isometric to one of the model spaces \( {\mathbb{R}}^{n},{\mathbb{S}}^{n}\left( R\right) \) , and \( {\mathbb{H}}^{n}\left( R\right) \) .

Proof. Given \( \left( {M, g}\right) \) satisfying the hypotheses, let \( \left( {\widehat{M},\widehat{g}}\right) \) be the Euclidean space, sphere, or hyperbolic space with the same constant sectional curvature as \( M \) . Note that \( \widehat{M} \) is simply connected in each case. Let \( p \in  M \) be arbitrary. Corollary 10.15 shows that there exist an open subset \( V \subseteq  M \) containing \( p \) , an open subset \( \widehat{V} \subseteq  \widehat{M} \) , and an isometry \( \varphi  : V \rightarrow  \widehat{V} \) . If we can show that \( \varphi \) can be analytically continued along every path starting at \( p \) , then we can conclude from Corollary 12.3 that there exists a global isometry \( \Phi  : M \rightarrow  \widehat{M} \) , thus proving the theorem.

To that end, let \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be a path starting at \( p \) . Corollary 10.15 shows that for each \( t \in  \left\lbrack  {0,1}\right\rbrack \) , there is a neighborhood of \( \gamma \left( t\right) \) that is isometric to an open subset of \( \widehat{M} \) . After shrinking the neighborhoods if necessary, we may assume by Theorem 6.17 that each such neighborhood is a convex geodesic ball. By compactness, we can choose a partition \( \left( {{t}_{0},\ldots ,{t}_{k + 1}}\right) \) of \( \left\lbrack  {0,1}\right\rbrack \) and a finite sequence of such balls \( {B}_{0},\ldots ,{B}_{k} \) such that \( \gamma \left( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  \right)  \subseteq  {B}_{i} \) for each \( i = 0,\ldots , k \) . After shrinking \( {B}_{0} \) and adding more points to the partition if necessary, we can also assume \( {B}_{0} \subseteq  V \) .

We wish to construct local isometries \( {\psi }_{i} : {B}_{i} \rightarrow  \widehat{M} \) such that successive ones agree on overlaps. Begin with \( {\psi }_{0} = {\left. \varphi \right| }_{{B}_{0}} \) . By our choice of \( {B}_{1} \) , there is some isometry \( {\beta }_{1} \) from \( {B}_{1} \) to an open subset of \( \widehat{M} \) . Note that \( {B}_{0} \cap  {B}_{1} \) is an intersection of geodesically convex sets and thus is connected, and it is nonempty because it contains \( \gamma \left( {t}_{1}\right) \) . The composition \( {\psi }_{0} \circ  {\beta }_{1}^{-1} \) is an isometry from \( {\beta }_{1}\left( {{B}_{0} \cap  {B}_{1}}\right) \) to \( {\psi }_{0}\left( {{B}_{0} \cap  {B}_{1}}\right) \) , both of which are connected open subsets of \( \widehat{M} \) , so by Problem 5-11(c), it is the restriction of a global isometry \( \Psi  : \widehat{M} \rightarrow  \widehat{M} \) (Fig. 12.2). Let \( {\psi }_{1} = \Psi  \circ  {\beta }_{1} : {B}_{1} \rightarrow  \widehat{M} \) . Our choice of \( \Psi \) guarantees that \( {\left. {\psi }_{1}\right| }_{{B}_{0} \cap  {B}_{1}} = {\left. {\psi }_{0}\right| }_{{B}_{0} \cap  {B}_{1}} \) .

Proceeding similarly by induction, we can define \( {\psi }_{i} : {B}_{i} \rightarrow  \widehat{M} \) for \( i = 2,\ldots , k \) , such that \( {\psi }_{i} \) agrees with \( {\psi }_{i - 1} \) on \( {B}_{i} \cap  {B}_{i - 1} \) .

Now we define the analytic continuation of \( \varphi \) as follows: start with \( \left( {{U}_{t},{\varphi }_{t}}\right)  = \; \left( {{B}_{0},{\psi }_{0}}\right) \) for \( 0 \leq  t \leq  {t}_{1} \) , and thereafter let \( \left( {{U}_{t},{\varphi }_{t}}\right)  = \left( {{B}_{i},{\psi }_{i}}\right) \) for \( {t}_{i} < t \leq  {t}_{i + 1} \) . It is easy to verify that this family of maps does the job.

Corollary 12.5 (Characterization of Constant-Curvature Manifolds). The complete, connected, n-dimensional Riemannian manifolds of constant sectional curvature are, up to isometry, exactly the Riemannian quotients of the form \( \widetilde{M}/\Gamma \) , where \( \widetilde{M} \) is one of the constant-curvature model spaces \( {\mathbb{R}}^{n},{\mathbb{S}}^{n}\left( R\right) \) , or \( {\mathbb{H}}^{n}\left( R\right) \) , and \( \Gamma \) is a discrete subgroup of \( \operatorname{Iso}\left( \widetilde{M}\right) \) that acts freely on \( \widetilde{M} \) .

Proof. First suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian \( n \) -manifold with constant sectional curvature, and let \( \pi  : \widetilde{M} \rightarrow  M \) be its universal covering manifold with the pullback metric \( \widetilde{g} = {\pi }^{ * }g \) . The preceding theorem shows that \( \left( {\widetilde{M},\widetilde{g}}\right) \) is isometric to one of the model spaces, so we might as well take it to be one of the models. Proposition C. 20 shows that the group \( \Gamma \) of covering automorphisms acts freely and properly on \( \widetilde{M} \) , and Corollary 2.33 shows that \( M \) is isometric to \( \widetilde{M}/\Gamma \) . Moreover, if \( \varphi \) is any covering automorphism, then \( \pi  \circ  \varphi  = \pi \) , and so \( {\varphi }^{ * }\widetilde{g} = \; {\varphi }^{ * }{\pi }^{ * }g = {\pi }^{ * }g = \widetilde{g} \) ; thus \( \Gamma \) acts isometrically, so it is a subgroup of \( \operatorname{Iso}\left( \widetilde{M}\right) \) .

To show that \( \Gamma \) is discrete, suppose \( \left\{  {\varphi }_{i}\right\}   \subseteq  \Gamma \) is an infinite set with an accumulation point in \( \operatorname{Iso}\left( \widetilde{M}\right) \) . (Note that Problem 5-11 shows that \( \operatorname{Iso}\left( {\widetilde{M},\widetilde{g}}\right) \) is a Lie group acting smoothly on \( \widetilde{M} \) in each case, so it makes sense to talk about the topology of the isometry group.) Since the action of \( \Gamma \) is free, for every point \( \widetilde{p} \in  \widetilde{M} \) the set \( \left\{  {{\varphi }_{i}\left( \widetilde{p}\right) }\right\} \) is infinite, and by continuity of the action it has an accumulation point in \( \bar{M} \) . But this is impossible, since the points \( \left\{  {{\varphi }_{i}\left( \widetilde{p}\right) }\right\} \) all project to the same point in \( M \) under the covering map \( \pi \) , and so form a closed discrete set. Thus \( \Gamma \) is discrete in \( \operatorname{Iso}\left( \widetilde{M}\right) \) .

Conversely, suppose \( \widetilde{M} \) is one of the model spaces and \( \Gamma \) is a discrete subgroup of Iso \( \left( \widetilde{M}\right) \) that acts freely on \( \widetilde{M} \) . Then \( \Gamma \) is a closed Lie subgroup of Iso \( \left( \widetilde{M}\right) \) by Proposition C.9, so the result of Problem 6-28 shows that it acts properly on \( M \) . It then follows from Proposition 2.32 that \( \widetilde{M}/\Gamma \) is a smooth manifold and has a unique Riemannian metric such that the quotient map \( \pi  : \widetilde{M} \rightarrow  \widetilde{M}/\Gamma \) is a Riemannian covering, and \( \widetilde{M}/\Gamma \) is complete by Corollary 6.24. Since a Riemannian covering is in particular a local isometry, \( \widetilde{M}/\Gamma \) has constant sectional curvature.

A complete, connected Riemannian manifold with constant sectional curvature is called a space form. A space form is called spherical, Euclidean, or hyperbolic, depending on whether its sectional curvature is positive, zero, or negative, respectively. The preceding corollary, combined with the characterization of the isometry groups of the simply connected model spaces given in Problem 5-11, essentially reduces the classification of space forms to the group-theoretic problem of classifying the discrete subgroups of \( \mathrm{E}\left( n\right) ,\mathrm{O}\left( {n + 1}\right) \) , and \( {\mathrm{O}}^{ + }\left( {n,1}\right) \) that act without fixed points. Nevertheless, the group-theoretic problem is still far from easy.

The spherical space forms were classified in 1972 by Joseph Wolf [Wol11]; the proof is intimately connected with the representation theory of finite groups. Although in even dimensions there are only spheres and projective spaces (see Problem 12-2), the situation in odd dimensions is far more complicated. Already in dimension 3 there are many interesting examples: some notable ones are the lens spaces obtained as quotients of \( {\mathbb{S}}^{3} \subseteq  {\mathbb{C}}^{2} \) by cyclic groups rotating the two complex coordinates through different angles, and the quotients of SO(3) (which is diffeomorphic to \( {\mathbb{{RP}}}^{3} \) and is therefore already a quotient of \( {\mathbb{S}}^{3} \) ) by the dihedral groups, the symmetry groups of regular 3-dimensional polyhedra.

The complete classification of Euclidean space forms is known only in low dimensions. Problem 12-3 shows that every compact 2-dimensional Euclidean space form is diffeomorphic to the torus or the Klein bottle. It turns out that there are 10 classes of nondiffeomorphic compact Euclidean space forms of dimension 3, and 75 classes in dimension 4. The fundamental groups of compact Euclidean space forms are examples of crystallographic groups—discrete groups of Euclidean isometries with compact quotients, which have been studied extensively by physicists as well as geometers. (A quotient of \( {\mathbb{R}}^{n} \) by a crystallographic group is a space form, provided it is a manifold, which is true whenever the group is torsion-free.) In higher dimensions, the classification is still elusive. The main things that are known are two results proved by Ludwig Bieberbach in the early twentieth century: (1) every Euclidean space form is a quotient of a flat torus by a finite group of isometries, and (2) in each dimension, there are only finitely many diffeomorphism classes of Euclidean space forms. See [Wol11] for proofs of the Bieberbach theorems and a complete survey of the state of the art.

In addition to the question of classifying Euclidean space forms up to diffeomorphism, there is also the question of classifying the different flat Riemannian metrics on a given manifold up to isometry. Problem 12-5 shows, for example, that there is a three-parameter family of nonisometric flat Riemannian metrics on the 2-torus.

Finally, the study of hyperbolic space forms is a vast and rich subject in its own right. A good introduction is the book [Rat06].

## Symmetric Spaces Revisited

The technique of analytic continuation of local isometries can also be used to derive a fundamental global result about symmetric spaces. Theorem 10.19 showed that locally symmetric spaces are characterized by having parallel curvature. The next theorem is a global version of that result.

Theorem 12.6. Suppose \( \left( {M, g}\right) \) is a complete, simply connected Riemannian manifold with parallel Riemann curvature tensor. Then \( M \) is a symmetric space.

Proof. Let \( p \) be an arbitrary point of \( M \) . Theorem 10.19 shows that \( M \) is locally symmetric, so there is a point reflection \( \varphi  : U \rightarrow  U \) defined on some connected neighborhood \( U \) of \( p \) . If we can show that \( \varphi \) can be analytically continued along every path starting at \( p \) , then Corollary 12.3 shows that \( \varphi \) extends to a global isometry \( \Phi  : M \rightarrow  M \) ; because it agrees with \( \varphi \) on \( U \) , it satisfies \( d{\Phi }_{p} = d{\varphi }_{p} =  - \mathrm{{Id}} \) , so it is a point reflection.

Let \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be a path starting at \( p \) . By compactness, we can find a partition \( \left( {{t}_{0},\ldots ,{t}_{k + 1}}\right) \) of \( \left\lbrack  {0,1}\right\rbrack \) and convex geodesic balls \( {B}_{0},\ldots ,{B}_{k} \) such that \( \gamma \left( \left\lbrack  {{t}_{i},{t}_{i + 1}}\right\rbrack  \right)  \subseteq \; {B}_{i} \) for each \( i = 0,\ldots , k \) , with \( {B}_{0} \) chosen small enough that \( {B}_{0} \subseteq  U \) . As in the proof of Theorem 12.4, we will construct local isometries \( {\psi }_{i} : {B}_{i} \rightarrow  M \) such that successive ones agree on overlaps.

Begin with \( {\psi }_{0} = {\left. \varphi \right| }_{{B}_{0}} \) , and let \( {p}_{1} = \gamma \left( {t}_{1}\right) \) and \( {q}_{1} = {\psi }_{0}\left( {p}_{1}\right) \) . Because \( {\psi }_{0} \) is a local isometry, the linear map \( {\left. d{\psi }_{0}\right| }_{{p}_{1}} : {T}_{{p}_{1}}M \rightarrow  {T}_{{q}_{1}}M \) satisfies \( {\left( {\left. d{\psi }_{0}\right| }_{{p}_{1}}\right) }^{ * }{g}_{{q}_{1}} = \; {g}_{{p}_{1}} \) and \( {\left( {\left. d{\psi }_{0}\right| }_{{p}_{1}}\right) }^{ * }R{m}_{{q}_{1}} = R{m}_{{p}_{1}} \) . Lemma 10.18 then shows that there is a local isometry \( {\psi }_{1} : {B}_{1} \rightarrow  M \) that satisfies \( {\psi }_{1}\left( {p}_{1}\right)  = {\psi }_{0}\left( {p}_{1}\right) \) and \( {\left. d{\psi }_{1}\right| }_{{p}_{1}} = {\left. d{\psi }_{0}\right| }_{{p}_{1}} \) , and it follows from Proposition 5.22 that \( {\psi }_{1} \) and \( {\psi }_{0} \) agree on the connected open set \( {B}_{0} \cap \; {B}_{1} \) . Proceeding by induction, we obtain local isometries \( {\psi }_{i} : {B}_{i} \rightarrow  M \) satisfying \( {\left. {\psi }_{i}\right| }_{{B}_{i - 1} \cap  {B}_{i}} = {\left. {\psi }_{i - 1}\right| }_{{B}_{i - 1} \cap  {B}_{i}} \) . Then the analytic continuation of \( \varphi \) is defined just as in the last paragraph of the proof of Theorem 12.4, thus completing the proof.

Corollary 12.7. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold. The following are equivalent:

(a) \( M \) has parallel curvature tensor.

(b) \( M \) is a locally symmetric space.

(c) \( M \) is isometric to a Riemannian quotient \( \widetilde{M}/\Gamma \) , where \( \widetilde{M} \) is a (globally) symmetric space and \( \Gamma \) is a discrete Lie group that acts freely, properly, and isometrically on \( \widetilde{M} \) .

Proof. Theorem 10.19 shows that (a) \( \Leftrightarrow \) (b). To show that (a) \( \Rightarrow \) (c), assume that \( M \) has parallel curvature tensor, and let \( \left( {\widetilde{M},\widetilde{g}}\right) \) be its universal covering manifold with the pullback metric. Since the covering map \( \pi  : \widetilde{M} \rightarrow  M \) is a local isometry, \( \widetilde{M} \) also has parallel curvature tensor, and Corollary 6.24 shows that it is complete. Then Theorem 12.6 shows that \( \widetilde{M} \) is a symmetric space. If we let \( \Gamma \) denote the covering automorphism group with the discrete topology, then Proposition C. 20 shows that \( \Gamma \) is a discrete Lie group acting smoothly, freely, and properly on \( \widetilde{M} \) , and it acts isometrically because the pullback metric is invariant under all covering automor-phisms. Finally, Corollary 2.33 shows that \( M \) is isometric to \( \widetilde{M}/\Gamma \) .

Finally, we show that (c) \( \Rightarrow \) (a). If \( M \) is isometric to a Riemannian quotient of the form \( \widetilde{M}/\Gamma \) as in (c), then the quotient map \( \widetilde{M} \rightarrow  \widetilde{M}/\Gamma \) is a Riemannian covering by Proposition 2.32. Since \( \widetilde{M} \) has parallel curvature tensor by the result of Problem 7-3, so does \( M \) .

An extensive treatment of the structure and classification of symmetric spaces can be found in [Hel01].

The analytic continuation technique used in this section was introduced in 1926 by Élie Cartan, in the same paper [Car26] in which he first defined symmetric spaces and proved many of their properties. The technique was generalized in 1956 by Warren Ambrose [Amb56] to allow for isometries between more general Riemannian manifolds with varying curvature; and then in 1959 it was generalized further by Noel Hicks [Hic59] to manifolds with connections in their tangent bundles, not necessarily Riemannian ones. The resulting theorem is known as the Cartan-Ambrose-Hicks theorem. We do not pursue it further, but a statement and proof can be found in [CE08].

## Manifolds of Nonpositive Curvature

Our next major local-to-global theorem provides a complete topological characterization of complete, simply connected manifolds of nonpositive sectional curvature. This was proved in 1928 by Élie Cartan, generalizing earlier proofs for surfaces by Hans Carl Friedrich von Mangoldt and Jacques Hadamard. As with many other such theorems, tradition has given it a title that is not entirely historically accurate, but is generally recognized by mathematicians.

Theorem 12.8 (Cartan-Hadamard). If \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold with nonpositive sectional curvature, then for every point \( p \in  M \) , the map \( {\exp }_{p} : {T}_{p}M \rightarrow  M \) is a smooth covering map. Thus the universal covering space of \( M \) is diffeomorphic to \( {\mathbb{R}}^{n} \) , and if \( M \) is simply connected, then \( M \) itself is diffeomorphic to \( {\mathbb{R}}^{n} \) .

Proof. By Theorem 11.12, the assumption of nonpositive curvature guarantees that \( p \) has no conjugate points along any geodesic. Therefore, by Proposition 10.20, \( {\exp }_{p} \) is a local diffeomorphism on all of \( {T}_{p}M \) .

Let \( \widetilde{g} \) be the (variable-coefficient) 2-tensor field \( {\exp }_{p}^{ * }g \) defined on \( {T}_{p}M \) . Because \( {\exp }_{p} \) is a local diffeomorphism, \( \widetilde{g} \) is a Riemannian metric, and \( {\exp }_{p} \) is a local isometry from \( \left( {{T}_{p}M,\widetilde{g}}\right) \) to \( \left( {M, g}\right) \) . Note that each line \( t \mapsto  {tv} \) in \( {T}_{p}M \) is a \( \widetilde{g} \) - geodesic, so \( \left( {{T}_{p}M,\widetilde{g}}\right) \) is complete by Corollary 6.20. It then follows from Theorem 6.23 that \( {\exp }_{p} \) is a smooth covering map. The remaining statements of the theorem follow immediately from uniqueness of the universal covering space.

Because of this theorem, a complete, simply connected Riemannian manifold with nonpositive sectional curvature is called a Cartan-Hadamard manifold. The basic examples are Euclidean and hyperbolic spaces. The next two propositions show that Cartan-Hadamard manifolds share many basic geometric properties with these model spaces. A line in a Riemannian manifold is the image of a nonconstant geodesic that is defined on all of \( \mathbb{R} \) and restricts to a minimizing segment between any two of its points.

Proposition 12.9 (Basic Properties of Cartan-Hadamard Manifolds). Suppose \( \left( {M, g}\right) \) is a Cartan-Hadamard manifold.

(a) The injectivity radius of \( M \) is infinite.

(b) The image of every nonconstant maximal geodesic in \( M \) is a line.

(c) Any two distinct points in \( M \) are contained in a unique line.

(d) Every open or closed metric ball in \( M \) is a geodesic ball.

(e) For every point \( q \in  M \) , the function \( r\left( x\right)  = {d}_{g}\left( {q, x}\right) \) is smooth on \( M \smallsetminus  \{ q\} \) and \( r{\left( x\right) }^{2} \) is smooth on all of \( M \) .

Proof. These properties follow from Lemma 6.8, Proposition 6.11, and Corollaries 6.12 and 6.13, together with the fact that \( M \) is a normal neighborhood of each of its points.

Suppose \( A, B, C \) are three points in a Cartan-Hadamard manifold that are noncollinear (meaning that they are not all contained in a single line). The geodesic triangle \( \bigtriangleup {ABC} \) determined by the points is the union of the images of the (unique) geodesic segments connecting the three points. (In the present context, we do not require that a geodesic triangle bound a two-dimensional region, as we did in Chapter 9.) If \( \bigtriangleup {ABC} \) is a geodesic triangle, we denote the angle in \( {T}_{A}M \) formed by the initial velocities of the geodesic segments from \( A \) to \( B \) and \( A \) to \( C \) by \( \angle A \) (or \( \angle {CAB} \) if necessary to avoid ambiguity), and similarly for the other angles.

Proposition 12.10. Suppose \( \bigtriangleup {ABC} \) is a geodesic triangle in a Cartan-Hadamard manifold \( \left( {M, g}\right) \) , and let \( a, b, c \) denote the lengths of the segments opposite the vertices \( A, B \) , and \( C \) , respectively. The following inequalities hold:

(a) \( {c}^{2} \geq  {a}^{2} + {b}^{2} - {2ab}\cos \angle C \) .

(b) \( \angle A + \angle B + \angle C \leq  \pi \) .

If the sectional curvatures of \( g \) are all strictly negative, then strict inequality holds in both cases.

Proof. Problem 12-7.

Another consequence of the Cartan-Hadamard theorem is that there are stringent topological restrictions on which manifolds can carry metrics of nonpositive sectional curvature. The next corollary is immediate.

Corollary 12.11. No simply connected compact manifold admits a metric of nonpositive sectional curvature.

With a little more work, we can obtain a much more powerful result.

Corollary 12.12. Suppose \( M \) and \( N \) are positive-dimensional compact, connected smooth manifolds, at least one of which is simply connected. Then \( M \times  N \) does not admit any Riemannian metric of nonpositive sectional curvature.

Proof. Suppose for the sake of contradiction that \( M \) is simply connected and \( g \) is a metric on \( M \times  N \) with nonpositive sectional curvature. If \( \widetilde{N} \) is the universal covering manifold of \( N \) , then there is a universal covering map \( \pi  : M \times  \widetilde{N} \rightarrow  M \times  N \) , and \( {\pi }^{ * }g \) is a complete metric of nonpositive sectional curvature on \( M \times  \widetilde{N} \) . The Cartan-Hadamard theorem shows that \( M \times  \widetilde{N} \) is diffeomorphic to a Euclidean space.

Since \( M \) is simply connected, it is orientable (Cor. B.19). Let \( \mu \) be a smooth orientation \( m \) -form for \( M \) , where \( m = \dim M \) . Then \( \mu \) is closed because there are no nontrivial \( \left( {m + 1}\right) \) -forms on \( M \) , but Stokes’s theorem shows that \( \mu \) is not exact, because \( {\int }_{M}\mu  > 0 \) . On the other hand, if we let \( p : M \times  \widetilde{N} \rightarrow  M \) denote the projection on the first factor, then the form \( {p}^{ * }\mu \) is exact on \( M \times  N \) , because every closed \( m \) -form on a Euclidean space is exact.

Choose an arbitrary point \( {y}_{0} \in  \widetilde{N} \) and define \( \sigma  : M \rightarrow  M \times  \widetilde{N} \) by \( \sigma \left( x\right)  = \left( {x,{y}_{0}}\right) \) ; it is a diffeomorphism onto its image \( \sigma \left( M\right)  = M \times  \left\{  {y}_{0}\right\} \) , which is a compact embedded submanifold of \( M \times  \widetilde{N} \) . By diffeomorphism invariance of the integral,

\[
{\int }_{\sigma \left( M\right) }{p}^{ * }\mu  = {\int }_{M}{\sigma }^{ * }\left( {{p}^{ * }\mu }\right)  = {\int }_{M}{\left( p \circ  \sigma \right) }^{ * }\mu  = {\int }_{M}\mu  > 0,
\]

because \( p \circ  \sigma  = \) Id. But \( {p}^{ * }\mu \) is exact on \( M \times  \widetilde{N} \) , which implies \( {\int }_{\sigma \left( M\right) }{p}^{ * }\mu  = 0 \) , a contradiction.

Example 12.13. By the preceding corollary, every metric on \( {\mathbb{S}}^{m} \times  {\mathbb{S}}^{n} \) must have positive sectional curvature somewhere, provided \( m \geq  2 \) and \( n \geq  1 \) , because both spheres are compact and \( {\mathbb{S}}^{m} \) is simply connected.

With a little more algebraic topology, one can obtain more information. A topological space whose higher homotopy groups \( {\pi }_{k}\left( M\right) \) all vanish for \( k > 1 \) is called aspherical.

Corollary 12.14. If \( M \) is a smooth manifold that admits a metric of nonpositive sectional curvature, then \( M \) is aspherical.

Proof. Suppose \( M \) admits a nonpositively curved metric, so its universal covering space is diffeomorphic to \( {\mathbb{R}}^{n} \) by Cartan-Hadamard. Since \( {\mathbb{R}}^{n} \) is contractible, it is aspherical. Since covering maps induce isomorphisms on \( {\pi }_{k} \) for \( k > 1 \) (see [Hat02, Prop. 4.1]), it follows that \( M \) is aspherical as well.

## Cartan's Torsion Theorem

In addition to the topological restrictions on nonpositively curved manifolds imposed directly by the Cartan-Hadamard theorem, it turns out that there is a stringent restriction on the fundamental groups of such manifolds (Corollary 12.18 below). In preparation for the proof, we need the following two lemmas, both of which are interesting in their own right.

Lemma 12.15. Suppose \( \left( {M, g}\right) \) is a Cartan-Hadamard manifold. Given \( q \in  M \) , let \( f : M \rightarrow  \lbrack 0,\infty ) \) be the function \( f\left( x\right)  = \frac{1}{2}{d}_{g}{\left( x, q\right) }^{2} \) . Then \( f \) is strictly geodesically convex, in the sense that for every geodesic segment \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) , the following inequality holds for all \( t \in  \left( {0,1}\right) \) :

\[
f\left( {\gamma \left( t\right) }\right)  < \left( {1 - t}\right) f\left( {\gamma \left( 0\right) }\right)  + {tf}\left( {\gamma \left( 1\right) }\right) . \tag{12.1}
\]

Proof. We can write \( f\left( x\right)  = \frac{1}{2}r{\left( x\right) }^{2} \) , where \( r \) is the radial distance function from \( q \) with respect to any normal coordinates, and Proposition 12.9 shows that \( f \) is smooth on all of \( M \) . The Hessian comparison theorem implies that \( {\mathcal{H}}_{r} \geq  \left( {1/r}\right) {\pi }_{r} \) on \( M \smallsetminus  \{ q\} \) , and therefore

\[
{\mathcal{H}}_{f} = \nabla \left( {\operatorname{grad}f}\right)  = \nabla \left( {r\operatorname{grad}r}\right)  = \operatorname{grad}r \otimes  {dr} + r{\mathcal{H}}_{r} \geq  \operatorname{grad}r \otimes  {dr} + {\pi }_{r}.
\]

The expression on the right-hand side above is actually equal to the identity operator, as can be checked by applying it separately to \( {\partial }_{r} = \operatorname{grad}r \) and an arbitrary vector perpendicular to \( {\partial }_{r} \) . Therefore \( \left\langle  {{\mathcal{H}}_{f}\left( v\right) , v}\right\rangle   \geq  {\left| v\right| }^{2} \) for all tangent vectors to \( M \smallsetminus  \{ q\} \) , and by continuity, the same holds at \( q \) as well.

Now suppose \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) is a geodesic segment. By the chain rule,

\[
\frac{d}{dt}f\left( {\gamma \left( t\right) }\right)  = d{f}_{\gamma \left( t\right) }\left( {{\gamma }^{\prime }\left( t\right) }\right)  = \left\langle  {{\left. \operatorname{grad}f\right| }_{\gamma \left( t\right) },{\gamma }^{\prime }\left( t\right) }\right\rangle  ,
\]

and thus (using the fact that \( {\gamma }^{\prime } \) is parallel along \( \gamma \) )

\[
\frac{{d}^{2}}{d{t}^{2}}f\left( {\gamma \left( t\right) }\right)  = \left\langle  {{\nabla }_{{\gamma }^{\prime }\left( t\right) }\operatorname{grad}{\left. f\right| }_{\gamma \left( t\right) },{\gamma }^{\prime }\left( t\right) }\right\rangle   = \left\langle  {{\mathcal{H}}_{f}\left( {{\gamma }^{\prime }\left( t\right) }\right) ,{\gamma }^{\prime }\left( t\right) }\right\rangle   > 0.
\]

Therefore, the function \( f \circ  \gamma \) is strictly convex on \( \left\lbrack  {0,1}\right\rbrack \) , and (12.1) follows.

Lemma 12.16. Suppose \( \left( {M, g}\right) \) is a Cartan-Hadamard manifold and \( S \) is a compact subset of \( M \) containing more than one point. Then there is a unique closed ball of minimum radius containing \( S \) .

Proof. Because \( S \) is compact, it is bounded. Let \( \delta  = \operatorname{diam}\left( S\right) \) , and let \( {q}_{0} \) be any point of \( S \) , so that \( S \subseteq  {\bar{B}}_{\delta }\left( {q}_{0}\right) \) . Let \( {c}_{0} \) be the infimum of the radii of closed metric balls containing \( S \) , and let \( \left( {{\bar{B}}_{{c}_{i}}\left( {p}_{i}\right) }\right) \) be a sequence of closed balls containing \( S \) such that \( {c}_{i} \searrow  {c}_{0} \) as \( i \rightarrow  \infty \) . For \( i \) large enough that \( {c}_{i} < {2\delta } \) , the fact that \( {q}_{0} \in  S \subseteq \; {\bar{B}}_{{c}_{i}}\left( {p}_{i}\right) \) implies \( {d}_{g}\left( {{p}_{i},{q}_{0}}\right)  \leq  {c}_{i} < {2\delta } \) , so each of the points \( {p}_{i} \) lies in the compact ball \( {\bar{B}}_{2\delta }\left( {q}_{0}\right) \) . After passing to a subsequence, we may assume that \( {p}_{i} \) converges to some point \( {p}_{0} \in  M \) .

To show that \( S \subseteq  {\bar{B}}_{{c}_{0}}\left( {p}_{0}\right) \) , suppose \( q \in  S \) , and let \( \varepsilon  > 0 \) be arbitrary. If \( i \) is large enough that \( {d}_{g}\left( {{p}_{i},{p}_{0}}\right)  \leq  \varepsilon /2 \) and \( {c}_{i} \leq  {c}_{0} + \varepsilon /2 \) , then

\[
{d}_{g}\left( {q,{p}_{0}}\right)  \leq  {d}_{g}\left( {q,{p}_{i}}\right)  + {d}_{g}\left( {{p}_{i},{p}_{0}}\right)  \leq  {c}_{i} + \varepsilon /2 \leq  {c}_{0} + \varepsilon .
\]

Since \( \varepsilon \) was arbitrary, this shows that \( {d}_{g}\left( {q,{p}_{0}}\right)  \leq  {c}_{0} \) , and thus \( S \subseteq  {\bar{B}}_{{c}_{0}}\left( {p}_{0}\right) \) .

Now we need to show that \( {\bar{B}}_{{c}_{0}}\left( {p}_{0}\right) \) is the unique closed ball of radius \( {c}_{0} \) containing \( S \) . Suppose to the contrary that \( {\bar{B}}_{{c}_{0}}\left( {p}_{0}^{\prime }\right) \) is another such ball. Let \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be the geodesic segment from \( {p}_{0} \) to \( {p}_{0}^{\prime } \) , and let \( m = \gamma \left( \frac{1}{2}\right) \) be its midpoint. Let \( q \in  S \) be arbitrary, and let \( f : M \rightarrow  \lbrack 0,\infty ) \) be the function \( f\left( x\right)  = \frac{1}{2}{d}_{g}{\left( q, x\right) }^{2} \) . Lemma 12.15 implies that

\[
\frac{1}{2}{d}_{g}{\left( q, m\right) }^{2} = f\left( m\right)  < \frac{1}{2}f\left( {p}_{0}\right)  + \frac{1}{2}f\left( {p}_{0}^{\prime }\right)  \leq  \frac{1}{2}\left( {\frac{1}{2}{c}_{0}^{2}}\right)  + \frac{1}{2}\left( {\frac{1}{2}{c}_{0}^{2}}\right)  = \frac{1}{2}{c}_{0}^{2}.
\]

Thus for every \( q \in  S \) , we have \( {d}_{g}\left( {q, m}\right)  < {c}_{0} \) . Since \( S \) is compact, the continuous function \( {d}_{g}\left( {\cdot , m}\right) \) takes on a maximum value \( {b}_{0} < {c}_{0} \) on \( S \) , showing that \( S \subseteq  {\bar{B}}_{{b}_{0}}\left( m\right) \) . This contradicts the fact that \( {c}_{0} \) is the minimum radius of a ball containing \( S \) .

Let us call the center of the smallest enclosing ball the 1-center of the set \( S \) . (The term is borrowed from optimization theory, where the "1-center problem" is the problem of finding a location for a single production facility that minimizes the maximum distance to any client. Some Riemannian geometry texts refer to the 1-center of a set \( S \subseteq  M \) as its "circumcenter" or "center of gravity," but these terms seem inappropriate, because the 1-center does not coincide with the classical meaning of either term for finite subsets of the Euclidean plane.)

Theorem 12.17 (Cartan’s Fixed-Point Theorem). Suppose \( \left( {M, g}\right) \) is a Cartan-Hadamard manifold and \( G \) is a compact Lie group acting smoothly and isometrically on \( M \) . Then \( G \) has a fixed point in \( M \) , that is, a point \( {p}_{0} \in  M \) such that \( \varphi  \cdot  {p}_{0} = {p}_{0} \) for all \( \varphi  \in  G \) .

Proof. Let \( {q}_{0} \in  M \) be arbitrary, and let \( S = G \cdot  {q}_{0} \) be the orbit of \( {q}_{0} \) . If \( S \) contains only the point \( {q}_{0} \) , then \( {q}_{0} \) is a fixed point, so we may assume that the orbit contains at least two points. Because \( S \) is the image of the continuous map from \( G \) to \( M \) given by \( \varphi  \mapsto  \varphi  \cdot  {q}_{0} \) , it is compact, so by Lemma 12.16, there is a unique smallest closed geodesic ball containing \( S \) . Let \( {p}_{0} \) be the center of this ball (the 1-center of \( S) \) , and let \( {c}_{0} \) be its radius.

Now let \( {\varphi }_{0} \in  G \) be arbitrary, and note that \( {\varphi }_{0} \cdot  S \) is the set of all points of the form \( {\varphi }_{0} \cdot  \varphi  \cdot  {q}_{0} \) for \( \varphi  \in  G \) . As \( \varphi \) ranges over all of \( G \) , so does \( {\varphi }_{0}\varphi \) , so this image set is exactly the orbit of \( {q}_{0} \) . In other words, \( {\varphi }_{0} \cdot  S = S \) .

Because \( G \) acts by isometries, \( {\varphi }_{0} \cdot  {\bar{B}}_{{c}_{0}}\left( {p}_{0}\right)  = {\bar{B}}_{{c}_{0}}\left( {{\varphi }_{0} \cdot  {p}_{0}}\right) \) . Thus \( {\bar{B}}_{{c}_{0}}\left( {{\varphi }_{0} \cdot  {p}_{0}}\right) \) is a closed ball of the same radius \( {c}_{0} \) containing \( {\varphi }_{0} \cdot  S = S \) , so by uniqueness of the 1-center we must have \( {\varphi }_{0} \cdot  {p}_{0} = {p}_{0} \) . Since \( {\varphi }_{0} \) was arbitrary, this shows that \( {p}_{0} \) is a fixed point of \( G \) .

Cartan's fixed-point theorem has important applications to Lie theory (where it is used to prove that all maximal compact subgroups of a Lie group are conjugate to each other). But our interest in the theorem is that it leads to the next corollary, also due to Cartan. If \( G \) is a group, an element \( \varphi  \in  G \) is called a torsion element if \( {\varphi }^{k} = 1 \) for some integer \( k > 1 \) . A group is said to be torsion-free if the only torsion element is the identity.

Corollary 12.18 (Cartan's Torsion Theorem). Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold with nonpositive sectional curvature. Then \( {\pi }_{1}\left( M\right) \) is torsion-free.

Proof. Let \( \left( {\widetilde{M},\widetilde{g}}\right) \) be the universal covering manifold of \( M \) with the pullback metric. Then \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Cartan-Hadamard manifold, and \( M \) is isometric to a Riemannian quotient \( \widetilde{M}/\Gamma \) , where \( \Gamma \) is subgroup of \( \operatorname{Iso}\left( {\widetilde{M},\widetilde{g}}\right) \) , isomorphic to \( {\pi }_{1}\left( M\right) \) and acting freely on \( \widetilde{M} \) .

Suppose \( \varphi \) is a torsion element of \( \Gamma \) . Then the cyclic group generated by \( \varphi \) is finite, and thus is a compact 0-dimensional Lie group with the discrete topology, acting smoothly on \( \widetilde{M} \) because isometries are smooth. Cartan’s fixed-point theorem shows that it has a fixed point. Because \( \Gamma \) acts freely, this implies that \( \varphi \) is the identity. Thus \( \Gamma \) is torsion-free, and the same is true of \( {\pi }_{1}\left( M\right) \) .

## Preissman's Theorem

Taken together, the Cartan-Hadamard theorem and Cartan's torsion theorem put severe restrictions on the possible topologies of manifolds that can carry nonposi-tively curved metrics. If we make the stronger assumption of strictly negative sectional curvature, we can restrict the topology even further. The following theorem was first proved in 1943 by Alexandre Preissman [Pre43].

Theorem 12.19 (Preissman). If \( \left( {M, g}\right) \) is a compact, connected Riemannian manifold with strictly negative sectional curvature, then every nontrivial abelian subgroup of \( {\pi }_{1}\left( M\right) \) is isomorphic to \( \mathbb{Z} \) .

Before proving Preissman's theorem, we need two more lemmas. Suppose \( \left( {M, g}\right) \) is a complete Riemannian manifold and \( \varphi  : M \rightarrow  M \) is an isometry. A geodesic \( \gamma  : \mathbb{R} \rightarrow  M \) is called an axis for \( \varphi \) if \( \varphi \) restricts to a nontrivial translation along \( \gamma \) , that is, if there is a nonzero constant \( c \) such that \( \varphi \left( {\gamma \left( t\right) }\right)  = \gamma \left( {t + c}\right) \) for all \( t \in  \mathbb{R} \) . An isometry with no fixed points that has an axis is said to be axial.

Example 12.20 (Axial Isometries). In \( {\mathbb{R}}^{2} \) with its Euclidean metric, every nontrivial translation \( \left( {x, y}\right)  \mapsto  \left( {x + a, y + b}\right) \) is axial, and every line parallel to the vector \( a{\partial }_{x} + b{\partial }_{y} \) is an axis. In the upper half-plane model of the hyperbolic plane, every dilation \( \left( {x, y}\right)  \mapsto  \left( {{cx},{cy}}\right) \) for \( c \neq  1 \) is axial, and the geodesic \( \gamma \left( t\right)  = \left( {0,{e}^{t}}\right) \) is an axis. On the other hand, the horizontal translations \( \left( {x, y}\right)  \mapsto  \left( {x + a, y}\right) \) are not axial for the hyperbolic plane, because no geodesic is invariant under such an isometry. //

As the next lemma shows, there is a close relation between axes and closed geodesics. This lemma will also prove useful in the proof of Synge's theorem later in the chapter.

Lemma 12.21. Suppose \( \left( {M, g}\right) \) is a compact, connected Riemannian manifold, and \( \pi  : \widetilde{M} \rightarrow  M \) is its universal covering manifold endowed with the metric \( \widetilde{g} = {\pi }^{ * }g \) . Then every covering automorphism of \( \pi \) has an axis, which restricts to a lift of a closed geodesic in \( M \) that is the shortest admissible path in its free homotopy class.

Proof. Let \( \varphi \) be any nontrivial covering automorphism of \( \pi \) , so it is also an isometry of \( \left( {\widetilde{M},\widetilde{g}}\right) \) . Every continuous path \( \widetilde{\sigma } : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \widetilde{M} \) from a point \( \widetilde{x} \in  \widetilde{M} \) to its image \( \varphi \left( \widetilde{x}\right) \) projects to a loop \( \sigma  = \pi  \circ  \widetilde{\sigma } \) in \( M \) . We begin by showing that the set of all loops obtained from \( \varphi \) in this way is exactly one free homotopy class. Suppose \( {\sigma }_{0},{\sigma }_{1} : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) are two such loops, so that \( {\sigma }_{i} = \pi  \circ  {\widetilde{\sigma }}_{i} \) for each \( i \) , where \( {\widetilde{\sigma }}_{i} \) is a path in \( \widetilde{M} \) from \( {\widetilde{x}}_{i} \) to \( \varphi \left( {\widetilde{x}}_{i}\right) \) (Fig. 12.3). For \( i = 0,1 \) , let \( {x}_{i} = \pi \left( {\widetilde{x}}_{i}\right) \) , so \( {\sigma }_{i} \) is a loop based at \( {x}_{i} \) . Choose a path \( \widetilde{\alpha } \) from \( {\widetilde{x}}_{0} \) to \( {\widetilde{x}}_{1} \) , and let \( \widetilde{\beta } = \varphi  \circ  \widetilde{\alpha } \) , which is a path from \( \varphi \left( {\widetilde{x}}_{0}\right) \) to \( \varphi \left( {\widetilde{x}}_{1}\right) \) , and \( \alpha  = \pi  \circ  \widetilde{\alpha } = \pi  \circ  \widetilde{\beta } \) , a path from \( {x}_{0} \) to \( {x}_{1} \) in \( M \) . Because \( \widetilde{M} \) is simply connected, the two paths \( {\widetilde{\alpha }}^{-1} \cdot  {\widetilde{\sigma }}_{0} \cdot  \widetilde{\beta } \) and \( {\widetilde{\sigma }}_{1} \) from \( {\widetilde{x}}_{1} \) to \( \varphi \left( {\widetilde{x}}_{1}\right) \) are path-homotopic, and therefore so are their images \( {\alpha }^{-1} \cdot  {\sigma }_{0} \cdot  \alpha \) and \( {\sigma }_{1} \) . An easy argument shows that the loops \( {\alpha }^{-1} \cdot  {\sigma }_{0} \cdot  \alpha \) and \( {\sigma }_{0} \) are freely homotopic, by a homotopy that gradually shrinks the "tail" \( \alpha \) to a point, so it follows that \( {\sigma }_{0} \) and \( {\sigma }_{1} \) are freely homotopic.

![bo_d7dtff491nqc73eq8m7g_367_502_185_509_697_0.jpg](images/bo_d7dtff491nqc73eq8m7g_367_502_185_509_697_0.jpg)

Fig. 12.3: Defining a free homotopy class

Conversely, let \( {\sigma }_{0} \) and \( {\sigma }_{1} \) be freely homotopic loops based at \( {x}_{0} \) and \( {x}_{1} \) in \( M \) , respectively, and suppose one of them, say \( {\sigma }_{0} \) , is of the form \( {\sigma }_{0} = \pi  \circ  {\widetilde{\sigma }}_{0} \) for some path \( {\widetilde{\sigma }}_{0} \) from a point \( {\widetilde{x}}_{0} \) to \( \varphi \left( {\widetilde{x}}_{0}\right) \) in \( \widetilde{M} \) . We need to show that \( {\sigma }_{1} \) is also of this form. The fact that the loops are freely homotopic means that there is a homotopy \( H : \left\lbrack  {0,1}\right\rbrack   \times \; \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) satisfying \( H\left( {s,0}\right)  = {\sigma }_{0}\left( s\right) , H\left( {s,1}\right)  = {\sigma }_{1}\left( s\right) \) , and \( H\left( {0, t}\right)  = H\left( {1, t}\right) \) for all \( t \) . Let \( \alpha  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) be the path \( \alpha \left( t\right)  = H\left( {0, t}\right)  = H\left( {1, t}\right) \) from \( {x}_{0} \) to \( {x}_{1} \) . The existence of such a homotopy implies that the two loops \( {\alpha }^{-1} \cdot  {\sigma }_{0} \cdot  \alpha \) and \( {\sigma }_{1} \) based at \( {x}_{1} \) are path-homotopic (see [LeeTM, Lemma 7.17]). By the monodromy theorem (Prop. A.54(c)), their lifts starting at \( {\widetilde{x}}_{1} \) both end at the same point. Let \( {\widetilde{\sigma }}_{1} \) be the lift of \( {\sigma }_{1} \) starting at the point \( {\widetilde{x}}_{1} = \widetilde{\alpha }\left( 1\right) \) , let \( \widetilde{\alpha } \) be the lift of \( \alpha \) starting at \( {\widetilde{x}}_{0} \) , and let \( \widetilde{\beta } = \varphi  \circ  \widetilde{\alpha } \) . Then \( {\widetilde{\alpha }}^{-1} \cdot  {\widetilde{\sigma }}_{0} \cdot  \widetilde{\beta } \) is a lift of \( {\alpha }^{-1} \cdot  {\sigma }_{0} \cdot  \alpha \) starting at \( {\widetilde{x}}_{1} \) , and it ends at \( \widetilde{\beta }\left( 1\right)  = \varphi \left( {\widetilde{x}}_{1}\right) \) . The monodromy theorem therefore implies that \( {\widetilde{\sigma }}_{1} \) is a path from \( {\widetilde{x}}_{1} \) to \( \varphi \left( {\widetilde{x}}_{1}\right) \) , as claimed.

We have shown that the covering automorphism \( \varphi \) determines a unique free homotopy class in \( M \) . It is not the trivial class, because that class contains the constant loop, which cannot be the image of a path from a point \( \widetilde{x} \) to \( \varphi \left( \widetilde{x}\right) \) because \( \varphi \) has no fixed points. Since \( M \) is compact, Proposition 6.28 shows that there is a closed geodesic \( \gamma  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) that is the shortest admissible path in this free homotopy class. This means, in particular, that there is a lift \( \widetilde{\gamma } \) of \( \gamma \) that satisfies \( \widetilde{\gamma }\left( 1\right)  = \varphi \left( {\widetilde{\gamma }\left( 0\right) }\right) \) . Because \( \widetilde{M} \) is complete, \( \widetilde{\gamma } \) extends to a geodesic in \( \widetilde{M} \) defined on all of \( \mathbb{R} \) . Let \( {\widetilde{\gamma }}_{0},{\widetilde{\gamma }}_{1} : \mathbb{R} \rightarrow  \widetilde{M} \) be the geodesics defined by \( {\widetilde{\gamma }}_{0}\left( t\right)  = \varphi  \circ  \widetilde{\gamma }\left( t\right) \) and \( {\widetilde{\gamma }}_{1}\left( t\right)  = \widetilde{\gamma }\left( {t + 1}\right) \) . Then \( {\widetilde{\gamma }}_{0}\left( 0\right)  = \widetilde{\gamma }\left( 1\right)  = {\widetilde{\gamma }}_{1}\left( 0\right) \) , and

\[
d{\pi }_{\widetilde{\gamma }\left( 1\right) }\left( {{\widetilde{\gamma }}_{0}^{\prime }\left( 0\right) }\right)  = d{\pi }_{\widetilde{\gamma }\left( 1\right) } \circ  d{\varphi }_{\widetilde{\gamma }\left( 0\right) }\left( {{\widetilde{\gamma }}^{\prime }\left( 0\right) }\right)
\]

(definition of \( {\widetilde{\gamma }}_{0} \) )

\[
= d{\pi }_{\widetilde{\gamma }\left( 0\right) }\left( {{\widetilde{\gamma }}^{\prime }\left( 0\right) }\right)
\]

\[
\text{ (because }\pi  \circ  \varphi  = \pi \text{ ) }
\]

\[
= {\gamma }^{\prime }\left( 0\right)
\]

(because \( \pi  \circ  \widetilde{\gamma } = \gamma \) )

\[
= {\gamma }^{\prime }\left( 1\right)
\]

( \( \gamma \) is a closed geodesic)

\[
= d{\pi }_{\widetilde{\gamma }\left( 1\right) }\left( {{\widetilde{\gamma }}^{\prime }\left( 1\right) }\right)
\]

\( \left( {\pi  \circ  \widetilde{\gamma } = \gamma \text{ again }}\right) \)

\[
= d{\pi }_{\widetilde{\gamma }\left( 1\right) }\left( {{\widetilde{\gamma }}_{1}^{\prime }\left( 0\right) }\right)
\]

(definition of \( {\widetilde{\gamma }}_{1} \) ).

![bo_d7dtff491nqc73eq8m7g_368_372_208_769_323_0.jpg](images/bo_d7dtff491nqc73eq8m7g_368_372_208_769_323_0.jpg)

Fig. 12.4: Uniqueness of the axis in the negative curvature case

The fact that \( d{\pi }_{\widetilde{\gamma }\left( 1\right) } \) is injective then implies \( {\widetilde{\gamma }}_{0}^{\prime }\left( 0\right)  = {\widetilde{\gamma }}_{1}^{\prime }\left( 0\right) \) , so by uniqueness of geodesics we have \( {\widetilde{\gamma }}_{0} \equiv  {\widetilde{\gamma }}_{1} \) , or in other words \( \varphi \left( {\widetilde{\gamma }\left( t\right) }\right)  = \widetilde{\gamma }\left( {t + 1}\right) \) for all \( t \in  \mathbb{R} \) . Thus \( \widetilde{\gamma } \) is an axis for \( \varphi \) .

In general, an axis of an isometry need not be unique, as we saw in the case of translations of \( {\mathbb{R}}^{2} \) in Example 12.20. However, as the next lemma shows, the situation is different in the case of negatively curved Cartan-Hadamard manifolds.

Lemma 12.22. Suppose \( \left( {M, g}\right) \) is a Cartan-Hadamard manifold with strictly negative sectional curvature. If \( \varphi  : M \rightarrow  M \) is an axial isometry, then its axis is unique up to reparametrization.

Proof. Let \( \varphi  : M \rightarrow  M \) be an axial isometry, and suppose \( {\gamma }_{1},{\gamma }_{2} : \mathbb{R} \rightarrow  M \) are both axes for \( \varphi \) . After reparametrizing the geodesics if necessary, we can assume that \( \varphi \) translates both geodesics by time 1.

Suppose first that the two axes do not intersect. Then the points \( A = {\gamma }_{1}\left( 0\right) , B = \; {\gamma }_{1}\left( 1\right)  = \varphi \left( A\right) , C = {\gamma }_{2}\left( 0\right) \) , and \( D = {\gamma }_{2}\left( 1\right)  = \varphi \left( C\right) \) are all distinct (Fig. 12.4). Let \( \sigma \) be the geodesic segment from \( A \) to \( C \) , so that \( \varphi  \circ  \sigma \) is the geodesic segment from \( B \) to \( D \) , forming a "geodesic quadrilateral" \( {ABDC} \) . Because \( \varphi \) preserves angles, the angles \( \angle {CAB} \) and \( \angle {ABD} \) are supplementary, as are \( \angle {ACD} \) and \( \angle {CDB} \) . Thus the angle sum of \( {ABDC} \) is exactly \( {2\pi } \) .

On the other hand, Proposition 12.10 shows that the geodesic triangles \( \bigtriangleup {ABC} \) and \( \bigtriangleup {BCD} \) have angle sums strictly less than \( \pi \) . The angle \( \angle {ACD} \) is no larger than the sum \( \angle {ACB} + \angle {BCD} \) : one way to see this is to note that Problem 6-2 shows that the angle between two unit vectors \( v, w \in  {T}_{C}M \) , namely arccos \( \langle v, w\rangle \) , is exactly equal to the Riemannian distance between \( v \) and \( w \) regarded as points on the unit sphere in \( {T}_{C}M \) with its round metric, so we can apply the triangle inequality for distances on the sphere. Similarly, \( \angle {ABD} \leq  \angle {ABC} + \angle {CBD} \) . Thus the sum of the four angles of \( {ABDC} \) is strictly less than \( {2\pi } \) , which is a contradiction.

It follows that \( {\gamma }_{1} \) and \( {\gamma }_{2} \) must intersect at some point, say \( x = {\gamma }_{1}\left( {t}_{1}\right)  = {\gamma }_{2}\left( {t}_{2}\right) \) . But then \( \varphi \left( x\right)  = {\gamma }_{1}\left( {{t}_{1} + 1}\right)  = {\gamma }_{2}\left( {{t}_{2} + 1}\right) \) is another intersection point, so Proposition 12.9(c) shows that \( {\gamma }_{2} \) must be a reparametrization of \( {\gamma }_{1} \) .

Proof of Preissman’s Theorem. Suppose \( \left( {M, g}\right) \) satisfies the hypotheses of the theorem, and let \( \pi  : \widetilde{M} \rightarrow  M \) be its universal covering, with the metric \( \widetilde{g} = {\pi }^{ * }g \) . Then \( \left( {\widetilde{M},\widetilde{g}}\right) \) is a Cartan-Hadamard manifold with strictly negative curvature. Because the fundamental group of \( M \) based at any point is isomorphic to the group of covering automorphisms of \( \pi \) (see Prop. C.22), it suffices to show that every nontrivial abelian group of covering automorphisms is isomorphic to \( \mathbb{Z} \) . Let \( H \) be such a group.

Let \( \varphi \) be any non-identity element of \( H \) , and let \( \gamma  : \mathbb{R} \rightarrow  \widetilde{M} \) be the axis for \( \varphi \) , which we may give a unit-speed parametrization. Thus there is a nonzero constant \( c \) such that \( \varphi \left( {\gamma \left( t\right) }\right)  = \gamma \left( {t + c}\right) \) for all \( t \in  \mathbb{R} \) . If \( \psi \) is any other element of \( H \) , then for all \( t \in  \mathbb{R} \) we have

\[
\varphi \left( {\psi \left( {\gamma \left( t\right) }\right) }\right)  = \psi \left( {\varphi \left( {\gamma \left( t\right) }\right) }\right)  = \psi \left( {\gamma \left( {t + c}\right) }\right) ,
\]

which shows that \( \psi  \circ  \gamma \) is also an axis for \( \varphi \) . Since axes are unique by Lemma 12.22, this means that \( \psi  \circ  \gamma \) is a (unit-speed) reparametrization of \( \gamma \) . It cannot be a backward reparametrization (one satisfying \( \varphi  \circ  \gamma \left( t\right)  = \gamma \left( {-t + a}\right) \) ), because then \( \psi \) would be a nontrivial covering automorphism having \( \gamma \left( {a/2}\right) \) as a fixed point, while the only covering automorphism with a fixed point is the identity. Thus there must be some \( a \in  \mathbb{R} \) such that \( \psi \left( {\gamma \left( t\right) }\right)  = \gamma \left( {t + a}\right) \) for all \( t \in  \mathbb{R} \) .

Define a map \( F : H \rightarrow  \mathbb{R} \) as follows: for each \( \psi  \in  H \) , let \( F\left( \psi \right) \) be the unique constant \( a \) such that \( \psi \left( {\gamma \left( t\right) }\right)  = \gamma \left( {t + a}\right) \) for all \( t \in  \mathbb{R} \) . A simple computation shows that \( F\left( {{\psi }_{1} \circ  {\psi }_{2}}\right)  = F\left( {\psi }_{1}\right)  + F\left( {\psi }_{2}\right) \) , so \( F \) is a group homomorphism. It is injective because \( F\left( \psi \right)  = 0 \) implies that \( \psi \) fixes every point in the image of \( \gamma \) , so it must be the identity. Thus \( F\left( H\right) \) is an additive subgroup of \( \mathbb{R} \) isomorphic to \( H \) .

Now let \( b \) be the infimum of the set of positive elements of \( F\left( H\right) \) . If \( b = 0 \) , then there exists \( \psi  \in  H \) such that \( 0 < F\left( \psi \right)  < \operatorname{inj}\left( M\right) \) , and then \( \pi  \circ  \gamma \) is a unit-speed geodesic in \( M \) satisfying \( \pi  \circ  \gamma \left( a\right)  = \pi  \circ  \gamma \left( 0\right) \) , where \( a = F\left( \psi \right) \) , which contradicts the fact that \( 0 < a < \operatorname{inj}\left( M\right) \) . Thus \( b > 0 \) . If \( b \notin  F\left( H\right) \) , there is a sequence of elements \( {\psi }_{i} \in  H \) such that \( F\left( {\psi }_{i}\right)  \searrow  b \) , and then for sufficiently large \( i < j \) we have \( 0 < F\left( {{\psi }_{i} \circ  {\psi }_{j}^{-1}}\right)  < \operatorname{inj}\left( M\right) \) , which leads to a contradiction as before. Thus \( b \) is the smallest positive element of \( F\left( H\right) \) , and then it is easy to verify that \( F\left( H\right) \) consists exactly of all integral multiples of \( b \) , so it is isomorphic to \( \mathbb{Z} \) .

The most important consequence of Preissman's theorem is the following corollary.

Corollary 12.23. No product of positive-dimensional connected compact manifolds admits a metric of strictly negative sectional curvature.

## Manifolds of Positive Curvature

Finally, we consider manifolds with positive curvature. The most important fact about such manifolds is the following theorem, which was first proved in 1941 by Sumner B. Myers [Mye41], building on earlier work of Ossian Bonnet, Heinz Hopf, and John L. Synge.

Theorem 12.24 (Myers). Let \( \left( {M, g}\right) \) be a complete, connected Riemannian \( n \) - manifold, and suppose there is a positive constant R such that the Ricci curvature of \( M \) satisfies \( \operatorname{Rc}\left( {v, v}\right)  \geq  \left( {n - 1}\right) /{R}^{2} \) for all unit vectors \( v \) . Then \( M \) is compact, with diameter less than or equal to \( {\pi R} \) , and its fundamental group is finite.

Proof. The diameter comparison theorem (Cor. 11.18) shows that the diameter of \( M \) is no greater than \( {\pi R} \) . To show that \( M \) is compact, we just choose a base point \( p \) and note that every point in \( M \) can be connected to \( p \) by a geodesic segment of length at most \( {\pi R} \) . Therefore, \( {\exp }_{p} : {\bar{B}}_{\pi R}\left( 0\right)  \rightarrow  M \) is surjective, so \( M \) is the continuous image of a compact set.

To prove the statement about the fundamental group, let \( \pi  : \widetilde{M} \rightarrow  M \) denote the universal covering space of \( M \) , with the metric \( \widetilde{g} = {\pi }^{ * }g \) . Then \( \left( {\widetilde{M},\widetilde{g}}\right) \) is complete by Corollary 6.24, and \( \widetilde{g} \) also has Ricci curvature satisfying the same lower bound, so \( \widetilde{M} \) is compact by the argument above. By Proposition A.61, for every \( p \in  M \) there is a one-to-one correspondence between \( {\pi }_{1}\left( {M, p}\right) \) and the fiber \( {\pi }^{-1}\left( p\right) \) . If \( {\pi }_{1}\left( {M, p}\right) \) were infinite, therefore, \( {\pi }^{-1}\left( p\right) \) would be an infinite discrete closed subset of \( \widetilde{M} \) , contradicting the compactness of \( \widetilde{M} \) . Thus \( {\pi }_{1}\left( {M, p}\right) \) is finite.

In case the manifold is already known to be compact, the hypothesis can be relaxed.

Corollary 12.25. Suppose \( \left( {M, g}\right) \) is a compact, connected Riemannian n-manifold whose Ricci tensor is positive definite everywhere. Then \( M \) has finite fundamental group.

Proof. Because the unit tangent bundle of \( M \) is compact by Proposition 2.9, the hypothesis implies that there is a positive constant \( c \) such that \( \operatorname{Rc}\left( {v, v}\right)  \geq  c \) for all unit tangent vectors \( v \) . Thus the hypotheses of Myers’s theorem are satisfied with \( \left( {n - 1}\right) /{R}^{2} = c \) .

On the other hand, it is possible for complete, noncompact manifolds to have strictly positive Ricci or even sectional curvature, as long as the curvature gets arbitrarily close to zero, as the following example shows.

Exercise 12.26. Let \( n \geq  2 \) , and let \( M \subseteq  {\mathbb{R}}^{n + 1} \) be the paraboloid \( \left\{  {\left( {{x}^{1},\ldots ,{x}^{n}, y}\right)  : }\right. \; y = {\left| x\right| }^{2}\} \) with the induced metric (see Problem 8-1). Show that \( M \) has strictly positive sectional and Ricci curvatures everywhere, but is not compact.

One of the most useful applications of Myers's theorem is to Einstein metrics.

Corollary 12.27. If \( \left( {M, g}\right) \) is a complete Einstein manifold with positive scalar curvature, then \( M \) is compact.

Proof. If \( g \) is Einstein with positive scalar curvature, then \( {Rc} = \frac{1}{n}{Sg} \) satisfies the hypotheses of Myers’s theorem with \( \left( {n - 1}\right) /{R}^{2} = \frac{1}{n}S \) .

In 1975, Shiu-Yuen Cheng proved the following theorem [Che75], showing that the diameter inequality in Myers's theorem is an equality only for a round sphere.

Theorem 12.28 (Cheng's Maximal Diameter Theorem). Suppose \( \left( {M, g}\right) \) satisfies the hypotheses of Myers’s theorem and \( \operatorname{diam}\left( M\right)  = {\pi R} \) . Then \( \left( {M, g}\right) \) is isometric to \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) .

Proof. By Myers’s theorem, \( M \) is compact, and thus by continuity of the distance function there are points \( {p}_{1},{p}_{2} \in  M \) such that \( {d}_{g}\left( {{p}_{1},{p}_{2}}\right)  = \operatorname{diam}\left( M\right)  = {\pi R} \) . For \( i = 1,2 \) and \( 0 < \delta  \leq  {\pi R} \) , let \( {B}_{\delta }\left( {p}_{i}\right) \) denote the open metric ball in \( M \) of radius \( \delta \) about \( {p}_{i} \) , and let \( {B}_{\delta } \) denote a metric ball in \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) of the same radius. The Bishop-Gromov theorem shows that the ratio \( \operatorname{Vol}\left( {{B}_{\delta }\left( {p}_{i}\right) }\right) /\operatorname{Vol}\left( {B}_{\delta }\right) \) is a nonincreasing function of \( \delta \) for each \( i \) , which implies the following inequality for \( 0 < \delta  < {\pi R} \)

\[
\frac{\operatorname{Vol}\left( {{B}_{\delta }\left( {p}_{i}\right) }\right) }{\operatorname{Vol}\left( M\right) } = \frac{\operatorname{Vol}\left( {{B}_{\delta }\left( {p}_{i}\right) }\right) }{\operatorname{Vol}\left( {{B}_{\pi R}\left( {p}_{i}\right) }\right) } \geq  \frac{\operatorname{Vol}\left( {\overset{ \circ  }{B}}_{\delta }\right) }{\operatorname{Vol}\left( {\overset{ \circ  }{B}}_{\pi R}\right) } = \frac{\operatorname{Vol}\left( {\overset{ \circ  }{B}}_{\delta }\right) }{\operatorname{Vol}\left( {{\mathbb{S}}^{n}\left( R\right) }\right) }. \tag{12.2}
\]

Now suppose \( {\delta }_{1},{\delta }_{2} \) are positive numbers such that \( {\delta }_{1} + {\delta }_{2} = {\pi R} \) . The fact that \( {d}_{g}\left( {{p}_{1},{p}_{2}}\right)  = {\pi R} \) together with the triangle inequality implies that \( {B}_{{\delta }_{1}}\left( {p}_{1}\right) \) and \( {B}_{{\delta }_{2}}\left( {p}_{2}\right) \) are disjoint, so

\[
\operatorname{Vol}\left( {{B}_{{\delta }_{1}}\left( {p}_{1}\right) }\right)  + \operatorname{Vol}\left( {{B}_{{\delta }_{2}}\left( {p}_{2}\right) }\right)  \leq  \operatorname{Vol}\left( M\right) . \tag{12.3}
\]

On the other hand, \( \operatorname{Vol}\left( {\overset{ \circ  }{B}}_{{\delta }_{1}}\right)  + \operatorname{Vol}\left( {\overset{ \circ  }{B}}_{{\delta }_{2}}\right)  = \operatorname{Vol}\left( {{\mathbb{S}}^{n}\left( R\right) }\right) \) (think of balls centered at the north and south poles), so (12.2) and (12.3) imply

\[
1 \geq  \frac{\operatorname{Vol}\left( {{B}_{{\delta }_{1}}\left( {p}_{1}\right) }\right)  + \operatorname{Vol}\left( {{B}_{{\delta }_{2}}\left( {p}_{2}\right) }\right) }{\operatorname{Vol}\left( M\right) } \geq  \frac{\operatorname{Vol}\left( {\overset{ \circ  }{B}}_{{\delta }_{1}}\right)  + \operatorname{Vol}\left( {\overset{ \circ  }{B}}_{{\delta }_{2}}\right) }{\operatorname{Vol}\left( {{\mathbb{S}}^{n}\left( R\right) }\right) } = 1.
\]

Thus the inequalities above are equalities, so in particular equality holds in (12.3). Moreover, the boundary of a metric ball has measure zero because it is contained in the image of a sphere under the exponential map, so we also have

\[
\operatorname{Vol}\left( {{\bar{B}}_{{\delta }_{1}}\left( {p}_{1}\right) }\right)  + \operatorname{Vol}\left( {{\bar{B}}_{{\delta }_{2}}\left( {p}_{2}\right) }\right)  = \operatorname{Vol}\left( M\right) . \tag{12.4}
\]

Next we will show that \( {d}_{g}\left( {{p}_{1}, q}\right)  + {d}_{g}\left( {{p}_{2}, q}\right)  = {d}_{g}\left( {{p}_{1},{p}_{2}}\right)  = {\pi R} \) for all \( q \in  M \) . Suppose not: by the triangle inequality, the only way this can fail is if there is a point \( q \) such that \( {d}_{g}\left( {{p}_{1}, q}\right)  + {d}_{g}\left( {{p}_{2}, q}\right)  > {\pi R} \) . Choosing \( {\delta }_{1} < {d}_{g}\left( {{p}_{1}, q}\right) \) and \( {\delta }_{2} < \; {d}_{g}\left( {{p}_{2}, q}\right) \) such that \( {\delta }_{1} + {\delta }_{2} = {\pi R} \) , we see that \( q \) is not in the closed set \( {\bar{B}}_{{\delta }_{1}}\left( {p}_{1}\right)  \cup \; {\bar{B}}_{{\delta }_{2}}\left( {p}_{2}\right) \) , so there is a neighborhood of \( q \) disjoint from that set (Fig. 12.5). But any such neighborhood would have positive volume, contradicting (12.4).

Suppose \( \gamma  : \lbrack 0,\infty ) \rightarrow  M \) is a unit-speed geodesic starting at \( {p}_{1} \) , and choose \( \varepsilon  > 0 \) small enough that \( {\left. \gamma \right| }_{\left\lbrack  0,\varepsilon \right\rbrack  } \) is minimizing. Then \( {d}_{g}\left( {{p}_{1},\gamma \left( \varepsilon \right) }\right)  = \varepsilon \) , and there is also a minimizing unit-speed geodesic \( {\gamma }_{2} \) from \( \gamma \left( \varepsilon \right) \) to \( {p}_{2} \) , whose length is \( {d}_{g}\left( {{p}_{2},\gamma \left( \varepsilon \right) }\right)  = \; {\pi R} - \varepsilon \) . The piecewise regular curve consisting of \( {\left. \gamma \right| }_{\left\lbrack  0,\varepsilon \right\rbrack  } \) followed by a unit-speed reparametrization of \( {\gamma }_{2} \) is an admissible curve from \( {p}_{1} \) to \( {p}_{2} \) of length \( {\pi R} \) , and is therefore minimizing; thus it is a (smooth) geodesic, and in fact coincides with \( \gamma \) , which is therefore minimizing on \( \left\lbrack  {0,{\pi R}}\right\rbrack \) . This shows that the cut time of every unit-speed geodesic starting at \( {p}_{1} \) is at least \( {\pi R} \) , so the injectivity radius \( \operatorname{inj}\left( {p}_{1}\right) \) is at least \( {\pi R} \) ; and then the injectivity radius comparison theorem (Cor. 11.17) shows that it is exactly \( {\pi R} \) . Thus \( M \smallsetminus  \left\{  {p}_{2}\right\}   = {B}_{\pi R}\left( {p}_{1}\right) \) is a geodesic ball around \( {p}_{1} \) . An analogous argument shows that \( M \smallsetminus  \left\{  {p}_{1}\right\} \) is a geodesic ball around \( {p}_{2} \) .

![bo_d7dtff491nqc73eq8m7g_372_628_210_275_471_0.jpg](images/bo_d7dtff491nqc73eq8m7g_372_628_210_275_471_0.jpg)

Fig. 12.5: A step in the proof of the maximal diameter theorem

The upshot of these observations is that the distance functions \( {r}_{1}\left( q\right)  = {d}_{g}\left( {{p}_{1}, q}\right) \) and \( {r}_{2}\left( q\right)  = {d}_{g}\left( {{p}_{2}, q}\right) \) are both smooth on \( M \smallsetminus  \left\{  {{p}_{1},{p}_{2}}\right\} \) , and because their sum is constant, they satisfy \( \Delta {r}_{1} =  - \Delta {r}_{2} \) . Elementary trigonometric identities show that the function \( {s}_{c} \) defined by (10.8) with \( c = 1/R \) satisfies \( {s}_{c}\left( {{\pi R} - t}\right)  = {s}_{c}\left( t\right) \) and \( {s}_{c}^{\prime }\left( {{\pi R} - t}\right)  =  - {s}_{c}^{\prime }\left( t\right) \) , so the Laplacian comparison theorem (Thm. 11.15) applied to \( {r}_{1} \) and \( {r}_{2} = {\pi R} - {r}_{1} \) yields

\[
\Delta {r}_{1} \leq  \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( {r}_{1}\right) }{{s}_{c}\left( {r}_{1}\right) } =  - \left( {n - 1}\right) \frac{{s}_{c}^{\prime }\left( {r}_{2}\right) }{{s}_{c}\left( {r}_{2}\right) } \leq   - \Delta {r}_{2} = \Delta {r}_{1}.
\]

Thus both inequalities are equalities. Arguing exactly as in the last part of the proof of the Bishop-Gromov theorem, we conclude that \( \left( {M, g}\right) \) has constant sectional curvature \( 1/{R}^{2} \) , and thus by Corollary 12.5 it admits a (finite-sheeted) Riemannian covering by \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) . Since the injectivity domain of \( {p}_{1} \) is the entire ball of radius \( {\pi R} \) , on which the metric has the form (10.17) in normal coordinates, it follows from Theorem 10.34 that the volume of \( M \) is equal to that of \( \left( {{\mathbb{S}}^{n}\left( R\right) ,{\overset{ \circ  }{g}}_{R}}\right) \) . Problem 2-14 then shows that the covering is one-sheeted, so it is a global isometry.

If we weaken the hypothesis to require merely that the Ricci curvature be nonnegative instead of positive definite, there are still nontrivial topological consequences. Let \( \Gamma \) be a finitely generated group. We say that \( \Gamma \) has polynomial growth if there exist a finite generating set \( S \subseteq  \Gamma \) and positive real numbers \( C, k \) such that for every positive integer \( m \) , the number of distinct elements of \( \Gamma \) that can be expressed as products of at most \( m \) elements of \( S \) and their inverses is no larger than \( C{m}^{k} \) . The order of polynomial growth of such a group is the infimum of such values of \( k \) . It is easy to check that \( {\mathbb{Z}}^{n} \) has polynomial growth of order \( n \) ; in fact, using the fundamental theorem on finitely generated abelian groups [DF04, p. 158], one can show that every finitely generated abelian group has polynomial growth of order equal to its free rank.

The following theorem, proved in 1968 by John Milnor [Mil68], shows in effect that fundamental groups of complete manifolds with nonnegative Ricci curvature are not too far from being abelian, at least when they are finitely generated. (Milnor conjectured in the same paper that the fundamental group of such a manifold is always finitely generated. This is true in the compact case, because compact manifolds are homotopy equivalent to finite CW complexes [Hat02, Cor. A.12], and these have finitely generated fundamental groups, as shown, for example, in [LeeTM, Thm. 10.15]. But the conjecture has not been proved in the noncompact case.) By contrast, Milnor proved in the same paper that the fundamental group of a negatively curved compact manifold never has polynomial growth, and that was extended in 1970 by André Avez [Ave70] to the case of a nonpositively curved compact manifold as long as it is not flat.

Theorem 12.29 (Milnor). Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian n-manifold with nonnegative Ricci curvature. Every finitely generated subgroup of \( {\pi }_{1}\left( M\right) \) has polynomial growth of order at most \( n \) .

Proof. Problem 12-11.

Corollary 12.30. If \( M \) is a connected smooth manifold whose fundamental group is free on more than one generator, then M admits no complete Riemannian metric with nonnegative Ricci curvature.

Exercise 12.31. Prove this corollary.

The corollary implies, for example, that a plane with two or more punctures does not admit a complete metric with nonnegative Gaussian curvature.

On the other hand, if we strengthen the hypothesis and assume positive sectional curvature, then we can reach a stronger conclusion. The following theorem was proved in 1936 by John L. Synge [Syn36].

Theorem 12.32 (Synge). Suppose \( \left( {M, g}\right) \) is a compact, connected Riemannian n-manifold with strictly positive sectional curvature.

(a) If \( n \) is even and \( M \) is orientable, then \( M \) is simply connected.

(b) If \( n \) is odd, then \( M \) is orientable.

Proof. Suppose for the sake of contradiction that the appropriate hypothesis holds but the conclusion is false. Let \( \pi  : \widetilde{M} \rightarrow  M \) be the universal covering manifold of \( M \) with the pullback metric \( \widetilde{g} = {\pi }^{ * }g \) . We can give \( \widetilde{M} \) the pullback orientation in the even-dimensional case; in the odd-dimensional case, just choose an orientation on \( \widetilde{M} \) . In either case, there is a nontrivial covering automorphism \( \varphi  : \widetilde{M} \rightarrow  \widetilde{M} \) ; in the even-dimensional case, it is orientation-preserving, and in the odd-dimensional case we can choose it to be orientation-reversing. By Lemma 12.21, there is a geodesic \( \widetilde{\gamma } : \mathbb{R} \rightarrow  \widetilde{M} \) that is an axis for \( \varphi \) , and \( \gamma  = \pi  \circ  \widetilde{\gamma } \) restricts to a closed geodesic in \( M \) that minimizes length in its free homotopy class. After reparametrizing if necessary, we may assume that \( \varphi \left( {\widetilde{\gamma }\left( t\right) }\right)  = \widetilde{\gamma }\left( {t + 1}\right) \) for all \( t \in  \mathbb{R} \) . Let \( {\widetilde{x}}_{0} = \widetilde{\gamma }\left( 0\right) ,{\widetilde{x}}_{1} = \widetilde{\gamma }\left( 1\right)  = \; \varphi \left( {\widetilde{x}}_{0}\right) \) , and \( x = \pi \left( {\widetilde{x}}_{0}\right)  = \pi \left( {\widetilde{x}}_{1}\right) \) .

Let \( \widetilde{P} : {T}_{{\widetilde{x}}_{0}}\widetilde{M} \rightarrow  {T}_{{\widetilde{x}}_{1}}\widetilde{M} \) be parallel transport along \( \widetilde{\gamma }{ \mid  }_{\left\lbrack  0,1\right\rbrack  } \) , and let \( P : {T}_{x}M \rightarrow \; {T}_{x}M \) be parallel transport along \( {\left. \gamma \right| }_{\left\lbrack  0,1\right\rbrack  } \) . Because local isometries preserve parallelism, the following diagram commutes, and all four maps are linear isometries:

![bo_d7dtff491nqc73eq8m7g_374_565_690_394_239_0.jpg](images/bo_d7dtff491nqc73eq8m7g_374_565_690_394_239_0.jpg)

Because \( d{V}_{\widetilde{g}} \) applied to a parallel frame is constant, \( \widetilde{P} \) is orientation-preserving. In the even-dimensional case, the vertical maps are both orientation-preserving, so \( P \) is too. In the odd-dimensional case, the fact that \( d{\pi }_{{\widetilde{x}}_{0}} = d{\pi }_{{\widetilde{x}}_{1}} \circ  d{\varphi }_{{\widetilde{x}}_{0}} \) implies that the two vertical maps induce opposite orientations on \( {T}_{x}M \) , so \( P \) is orientation-reversing.

The upshot is that in each case, \( P \) is a linear isometry of \( {T}_{x}M \) whose determinant is \( {\left( -1\right) }^{n} \) . Note that the determinant is the product of the eigenvalues of \( P \) , counted with multiplicities. Since the real eigenvalues of a linear isometry are \( \pm  1 \) , and the others come in conjugate pairs whose product is 1, the equation \( \det P = {\left( -1\right) }^{n} \) implies that the multiplicity of -1 has the same parity as \( n \) , and therefore the multiplicity of +1 must be even. We know that \( {\gamma }^{\prime }\left( 0\right) \) is a +1-eigenvector, so there must be another independent +1-eigenvector \( v \in  {T}_{x}M \) , which we can take to be orthogonal to \( {\gamma }^{\prime }\left( 0\right) \) . Extending \( v \) by parallel transport yields a nontrivial parallel normal vector field \( V \in  \mathfrak{X}\left( \gamma \right) \) satisfying \( V\left( 0\right)  = V\left( 1\right) \) .

Consider the variation of \( \gamma \) defined by \( \Gamma \left( {s, t}\right)  = {\exp }_{\gamma \left( t\right) }\left( {{sV}\left( t\right) }\right) \) . Because \( V\left( 0\right)  = \; V\left( 1\right) \) , this is a variation through admissible loops. The first variation formula (6.1) shows that the first derivative of \( {L}_{g}\left( {\Gamma }_{s}\right) \) at \( s = 0 \) is zero, because \( \gamma \) is a geodesic and the boundary terms cancel. We can then apply the general version of the second variation formula given in Problem 10-9, with the image of the geodesic \( s \mapsto  {\exp }_{x}\left( {sv}\right) \) playing the role of \( {M}_{1} \) and \( {M}_{2} \) . Because this is a totally geodesic submanifold, its second fundamental form vanishes, and we obtain

\[
{\left. \frac{{d}^{2}}{d{s}^{2}}\right| }_{s = 0}{L}_{g}\left( {\Gamma }_{s}\right)  = {\int }_{a}^{b}\left( {{\left| {D}_{t}V\right| }^{2} - {Rm}\left( {V,{\gamma }^{\prime },{\gamma }^{\prime }, V}\right) }\right) {dt}.
\]

Because \( V \) is parallel along \( \gamma \) and \( \sec \left( {V,{\gamma }^{\prime }}\right)  > 0 \) for all \( t \) , this second derivative is strictly negative, which implies that \( {L}_{g}\left( {\Gamma }_{s}\right)  < {L}_{g}\left( \gamma \right) \) for sufficiently small \( s \) . But this contradicts the fact that \( \gamma \) minimizes length in its free homotopy class.

The next corollary shows that there are only two possibilities for fundamental groups of positively curved compact manifolds in the even-dimensional case. (Compare this to Problem 12-2, which shows that the only even-dimensional manifolds that admit complete metrics of constant positive curvature are spheres and real projective spaces.)

Corollary 12.33. Suppose \( \left( {M, g}\right) \) is a compact, connected, even-dimensional Riemannian manifold with strictly positive sectional curvature. If \( M \) is orientable, then \( {\pi }_{1}\left( M\right) \) is trivial, and if not, then \( {\pi }_{1}\left( M\right)  \cong  \mathbb{Z}/2 \) .

Proof. The orientable case is part of Synge’s theorem. If \( M \) is nonorientable, it has a two-sheeted orientable covering manifold \( \widetilde{M} \) ; Synge’s theorem shows that \( \widetilde{M} \) is simply connected, so it is the universal covering space of \( M \) . Because each fiber of the universal covering has the same cardinality as \( {\pi }_{1}\left( M\right) \) , it follows that \( {\pi }_{1}\left( M\right) \) is isomorphic to the two-element group \( \mathbb{Z}/2 \) .

The preceding corollary implies, for example, that \( {\mathbb{{RP}}}^{n} \times  {\mathbb{{RP}}}^{n} \) has no metric of positive sectional curvature for any \( n \geq  2 \) , because its fundamental group is isomorphic to \( \mathbb{Z}/2 \times  \mathbb{Z}/2 \) .

For odd-dimensional compact manifolds, not many topological obstructions to the existence of positively curved metrics are known, apart from orientability and finiteness of \( {\pi }_{1} \) . And in the simply connected case, almost nothing is known. There are many examples of simply connected compact manifolds that admit metrics of nonnegative sectional curvature (for example, products of nonnegatively curved, simply connected compact manifolds, by the result of Problem 8-10); but there is not a single known example of a simply connected compact manifold that admits a metric of nonnegative sectional curvature but not one of positive sectional curvature. It was conjectured by Heinz Hopf in the early 1930s that \( {\mathbb{S}}^{2} \times  {\mathbb{S}}^{2} \) admits no positively curved metric, and it is reasonable to extend the conjecture to every product of positive-dimensional simply connected compact manifolds that both admit nonnegatively curved metrics; but nobody has come up with an example of such a product for which the conjecture can be proved or disproved.

## Further Results

We end the book with a brief look at some other local-to-global theorems about manifolds with positive or nonnegative curvature, whose proofs are beyond our scope.

Some of the most powerful applications of comparison theory have been to prove "pinching theorems." Given a positive real number \( \delta \) , a Riemannian manifold is said to be \( \delta \) -pinched if there exists a positive constant \( c \) such that all sectional curvatures satisfy

\[
{\delta c} \leq  \sec \left( \Pi \right)  \leq  c
\]

It is said to be strictly \( \delta \) -pinched if at least one of the inequalities is strict. The following celebrated theorem was originally proved by Marcel Berger and Wilhelm Klingenberg in the early 1960s [Ber60, Kli61].

Theorem 12.34 (The Sphere Theorem). A complete, simply connected, Riemannian n-manifold that is strictly \( \frac{1}{4} \) -pinched is homeomorphic to \( {\mathbb{S}}^{n} \) .

This result is sharp, at least in even dimensions, because the Fubini-Study metrics on complex projective spaces are \( \frac{1}{4} \) -pinched (Problem 8-13).

For noncompact manifolds, there is the following remarkable theorem of Jeff Cheeger and Detlef Gromoll [CG72].

Theorem 12.35 (The Soul Theorem). If \( \left( {M, g}\right) \) is a complete, connected, noncom-pact Riemannian manifold with nonnegative sectional curvature, then there exists a compact totally geodesic submanifold \( S \subseteq  M \) (called a soul of \( M \) ) such that \( M \) is diffeomorphic to the normal bundle of \( S \) in \( M \) . If \( M \) has strictly positive sectional curvature, then \( S \) is a point and \( M \) is diffeomorphic to a Euclidean space.

Even if we assume only nonnegative Ricci curvature, something nontrivial can be said in the noncompact case. The next theorem is also due to Cheeger and Gromoll [CG71]. Recall that a line in a Riemannian manifold is the image of a nonconstant geodesic defined on \( \mathbb{R} \) whose restriction to each compact subinterval is minimizing.

Theorem 12.36 (The Splitting Theorem). If \( \left( {M, g}\right) \) is a complete, connected, non-compact Riemannian manifold with nonnegative Ricci curvature, and M contains a line, then there is a Riemannian manifold \( \left( {N, h}\right) \) with nonnegative Ricci curvature such that \( M \) is isometric to the Riemannian product \( N \times  \mathbb{R} \) .

The proofs of all three of the above theorems, which can be found, for example, in [Pet16], are elaborate applications of comparison theory.

All of our comparison theorems, and indeed most of the things we have proved about Riemannian manifolds, are based on the analysis of ordinary differential equations-the geodesic equation, the parallel transport equation, the Jacobi equation, and the Riccati equation. Using techniques of partial differential equations can lead to much stronger conclusions in some cases. For instance, in 1982, Richard Hamilton [Ham82] proved the following striking result about 3-manifolds.

Theorem 12.37 (Hamilton's 3-Manifold Theorem). Suppose \( M \) is a simply connected compact Riemannian 3-manifold with positive definite Ricci curvature. Then \( M \) is diffeomorphic to \( {\mathbb{S}}^{3} \) .

He followed it up four years later [Ham86] with an analogous result about 4- manifolds, with Ricci curvature replaced by the curvature operator described in Problem 8-33.

Theorem 12.38 (Hamilton's 4-Manifold Theorem). Suppose \( M \) is a simply connected compact Riemannian 4-manifold with positive curvature operator. Then \( M \) is diffeomorphic to \( {\mathbb{S}}^{4} \) .

Much more recently, Christoph Böhm and Burkhard Wilking [BW08] extended this result to all dimensions.

Theorem 12.39 (Böhm-Wilking). Every simply connected compact Riemannian manifold with positive curvature operator is diffeomorphic to a sphere.

The method of proof of these three sphere theorems was to start with an initial metric \( {g}_{0} \) , and then define a one-parameter family of metrics \( \left\{  {{g}_{t} : t \geq  0}\right\} \) evolving according to the following partial differential equation, called the Ricci flow:

\[
\frac{\partial }{\partial t}{g}_{t} =  - {2R}{c}_{t}
\]

where \( R{c}_{t} \) is the Ricci curvature of \( {g}_{t} \) . Under the appropriate curvature assumption on \( {g}_{0} \) , the metric \( {g}_{t} \) can be rescaled to converge to a metric with constant positive sectional curvature as \( t \rightarrow  \infty \) , and then it follows from the Killing-Hopf theorem that the original manifold must be diffeomorphic to a sphere. Since Hamilton first introduced it, this technique has been vastly generalized by Hamilton and others, culminating in 2003 in a proof by Grigory Perelman of the Thurston geometrization conjecture described in Chapter 3.

The Ricci flow has also been used to improve the original \( \frac{1}{4} \) -pinched sphere theorem significantly. The techniques used to prove the original theorem were not strong enough to prove that \( M \) is diffeomorphic to \( {\mathbb{S}}^{n} \) , leaving open the possibility that there might exist strictly \( \frac{1}{4} \) -pinched metrics on exotic spheres (topological spheres with nonstandard smooth structures). In 2009, Simon Brendle and Richard Schoen [BS09] were able to use Ricci-flow techniques to close this gap. They also were able to prove the theorem under a weaker hypothesis: a Riemannian metric \( g \) is said to be pointwise \( \delta \) -pinched if for every \( p \in  M \) , there exists a positive number \( c\left( p\right) \) such that

\[
{\delta c}\left( p\right)  \leq  \sec \left( \Pi \right)  \leq  c\left( p\right)
\]

for every 2-plane \( \Pi  \subseteq  {T}_{p}M \) , and strictly pointwise \( \delta \) -pinched if at least one of the inequalities is strict at each point.

Theorem 12.40 (Differentiable Sphere Theorem). Let \( \left( {M, g}\right) \) be a compact, simply connected Riemannian manifold of dimension \( n \geq  4 \) . If \( M \) is strictly pointwise \( \frac{1}{4} \) -pinched, then it is diffeomorphic to \( {\mathbb{S}}^{n} \) with its standard smooth structure.

For a nice exposition of the proof, see the recent book [Bre10].

## Problems

12-1. Suppose \( \left( {M, g}\right) \) is a simply connected (but not necessarily complete) Riemannian \( n \) -manifold with constant sectional curvature. Prove that there exists an isometric immersion from \( M \) into one of the model spaces \( {\mathbb{R}}^{n} \) , \( {\mathbb{S}}^{n}\left( R\right) ,{\mathbb{H}}^{n}\left( R\right) \) .

12-2. Prove that if \( n \) is even, then every orientation-preserving orthogonal linear map from \( {\mathbb{R}}^{n + 1} \) to itself fixes at least one point of the unit sphere, and use this to prove that every even-dimensional spherical space form is isometric to either a round sphere or a real projective space with a constant multiple of the metric defined in Example 2.34. (Used on p. 349.)

12-3. Show that every compact 2-dimensional Euclidean space form is diffeomorphic to the torus or the Klein bottle, and every noncompact one is diffeomorphic to \( {\mathbb{R}}^{2},{\mathbb{S}}^{1} \times  {\mathbb{R}}^{2} \) , or the open Möbius band (see Example 2.35).

12-4. A lattice in \( {\mathbb{R}}^{n} \) is an additive subgroup \( \Lambda  \subseteq  {\mathbb{R}}^{n} \) of the form

\[
\Lambda  = \left\{  {{m}_{1}{v}_{1} + \cdots  + {m}_{n}{v}_{n} : {m}_{1},\ldots ,{m}_{n} \in  \mathbb{Z}}\right\}  ,
\]

for some basis \( \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) of \( {\mathbb{R}}^{n} \) . Let \( {\mathbb{T}}^{n} \) denote the \( n \) -torus.

(a) Show that if \( g \) is a flat Riemannian metric on \( {\mathbb{T}}^{n} \) , then \( \left( {{\mathbb{T}}^{n}, g}\right) \) is isometric to a Riemannian quotient of the form \( {\mathbb{R}}^{n}/\Lambda \) for some lattice \( \Lambda \) , acting on \( {\mathbb{R}}^{n} \) by vector addition.

(b) Show that two such quotients \( {\mathbb{R}}^{n}/{\Lambda }_{1} \) and \( {\mathbb{R}}^{n}/{\Lambda }_{2} \) are isometric if and only if \( {\Lambda }_{2} = A\left( {\Lambda }_{1}\right) \) for some \( A \in  \mathrm{O}\left( n\right) \) .

12-5. CLASSIFICATION OF FLAT TORI: Let \( {\mathbb{T}}^{2} = {\mathbb{S}}^{1} \times  {\mathbb{S}}^{1} \) denote the 2-torus. Show that if \( g \) is a flat Riemannian metric on \( {\mathbb{T}}^{2} \) , then \( \left( {{\mathbb{T}}^{2}, g}\right) \) is isometric to one and only one Riemannian quotient \( {\mathbb{R}}^{2}/\Lambda \) , where \( \Lambda \) is a lattice generated by a basis of the form \( \left( {\left( {a,0}\right) ,\left( {b, c}\right) }\right) \) , with \( a > 0,0 \leq  b \leq  a/2, c > 0 \) , and \( {b}^{2} + {c}^{2} \geq  {a}^{2} \) . [Hint: Given a lattice \( \Lambda  \subseteq  {\mathbb{R}}^{2} \) , let \( {v}_{1} \) be an element of \( \Lambda  \smallsetminus  \{ \left( {0,0}\right) \} \) of minimal norm; let \( {v}_{2} \) be an element of \( \Lambda  \smallsetminus  \left\langle  {v}_{1}\right\rangle \) of minimal norm (where \( \left\langle  {v}_{1}\right\rangle \) is the cyclic subgroup generated by \( {v}_{1} \) ), chosen so that the angle between \( {v}_{1} \) and \( {v}_{2} \) is less than or equal to \( \pi /2 \) ; and then apply a suitable orthogonal transformation.]

12-6. Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold, and \( p, q \in \; M \) . Proposition 6.25 showed that every path-homotopy class of paths from \( p \) to \( q \) contains a geodesic segment \( \gamma \) . Show that if \( M \) has nonpositive sectional curvature, then \( \gamma \) is the unique geodesic segment in the given path homotopy class.

12-7. Prove Proposition 12.10 (inequalities for triangles in Cartan-Hadamard manifolds). [Hint: Compare with appropriate triangles in Euclidean space.]

12-8. Prove Corollary 12.23 (nonexistence of negatively curved metrics on compact product manifolds).

12-9. Prove the following generalization of the Cartan-Hadamard theorem, due to Robert Hermann [Her63]: Suppose \( \left( {M, g}\right) \) is a complete, connected Riemannian manifold with nonpositive sectional curvature, and \( P \subseteq  M \) is a connected, properly embedded, totally geodesic submanifold. If for some \( x \in  P \) , the homomorphism \( {\pi }_{1}\left( {P, x}\right)  \rightarrow  {\pi }_{1}\left( {M, x}\right) \) induced by the inclusion \( P \hookrightarrow  M \) is surjective, then the normal exponential map \( E : {NP} \rightarrow  M \) is a diffeomorphism. [Hint: Mimic the proof of the Cartan-Hadamard theorem, using the result of Problem 10-20.]

12-10. Give a counterexample to show that Myers's theorem is false in dimensions greater than 2 if we replace the lower bound on Ricci curvature by a positive lower bound on scalar curvature.

12-11. ProveTheorem 12.29 (Milnor's theorem on the fundamental group of a manifold with nonnegative Ricci curvature) as follows: Let \( \pi  : \widetilde{M} \rightarrow  M \) be the universal covering space of \( M \) , and give \( \widetilde{M} \) the pullback metric \( \widetilde{g} = {\pi }^{ * }g \) . Because the covering automorphism group is isomorphic to \( {\pi }_{1}\left( M\right) \) (Prop. C. 22), it suffices to prove the result for every finitely generated subgroup of the automorphism group. Let \( \Gamma \) be such a subgroup, and let \( S = \left\{  {{\varphi }_{1},\ldots ,{\varphi }_{N}}\right\} \) be a finite generating set. Choose a base point \( p \in  \widetilde{M} \) . For each \( i = 1,\ldots , N \) , let \( {d}_{i} \) be the Riemannian distance from \( p \) to \( {\varphi }_{i}\left( p\right) \) , and let \( D = \max \left( {{d}_{1},\ldots ,{d}_{n}}\right) \) . For each nonidentity element \( \psi  \in  \Gamma \) , define the length of \( \psi \) to be the smallest integer \( m \) such \( \psi \) can be expressed as a product of \( m \) elements of \( S \) and their inverses.

(a) Show that there exists \( \varepsilon  > 0 \) such that for any two distinct elements \( {\psi }_{1},{\psi }_{2} \in  \Gamma \) , the metric balls \( {B}_{\varepsilon }\left( {{\psi }_{1}\left( p\right) }\right) \) and \( {B}_{\varepsilon }\left( {{\psi }_{2}\left( p\right) }\right) \) are disjoint.

(b) Show that if \( \psi  \in  \Gamma \) has length \( m \) , then \( {B}_{\varepsilon }\left( {\psi \left( p\right) }\right)  \subseteq  {B}_{{mD} + \varepsilon }\left( p\right) \) .

(c) Use the Bishop-Gromov theorem to prove that the number of distinct elements of \( \Gamma \) of length at most \( m \) is bounded by a constant times \( {m}^{n} \) .

12-12. Prove that there is no compact manifold that admits both a metric of positive definite Ricci curvature and a metric of nonpositive sectional curvature.

12-13. Suppose \( \left( {M, g}\right) \) is a complete Riemannian manifold. Recall that a line in \( M \) is the image of a nonconstant geodesic defined on all of \( \mathbb{R} \) that is minimizing between every pair of its points.

(a) Show that if \( \left( {M, g}\right) \) has strictly positive sectional curvature, then \( M \) contains no lines. [Hint: Given a geodesic \( \gamma  : \mathbb{R} \rightarrow  M \) , let \( \alpha  : \mathbb{R} \rightarrow  \mathbb{R} \) be a smooth positive function such that \( \alpha \left( t\right) \) is smaller than the minimum sectional curvature at \( \gamma \left( t\right) \) for each \( t \) , and let \( u : \mathbb{R} \rightarrow  \mathbb{R} \) be the solution to the initial value problem \( {u}^{\prime \prime } + {\alpha u} = 0 \) with \( u\left( 0\right)  = 1 \) and \( {u}^{\prime }\left( 0\right)  = 0 \) . Prove that there are numbers \( a < 0 < b \) such that \( u\left( a\right)  = u\left( b\right)  = 0 \) , and evaluate \( I\left( {V, V}\right) \) for a vector field of the form \( V\left( t\right)  = u\left( t\right) E\left( t\right) \) along \( {\left. \gamma \right| }_{\left\lbrack  a, b\right\rbrack  } \) , where \( E \) is a parallel unit normal vector field.]

(b) Give an example of a complete nonflat Riemannian manifold with nonnegative sectional curvature that contains a line.
