## §11 Sphere Bundles

Let \( \pi  : E \rightarrow  M \) be a fiber bundle with fiber the sphere \( {S}^{n}, n \geq  1 \) . As the structure group we normally take the largest group possible, namely the diffeomorphism group \( \operatorname{Diff}\left( {S}^{n}\right) \) , but sometimes we also consider sphere bundles with structure group \( O\left( {n + 1}\right) \) . These two notions are not equivalent; there are examples of sphere bundles whose structure groups cannot be reduced to the orthogonal group. Thus, every vector bundle defines a sphere bundle, but not conversely. By the Leray-Hirsch theorem if there is a closed global \( n \) -form on \( E \) whose restriction to each fiber generates the cohomology of the fiber, then the cohomology of \( E \) is

\[
{H}^{ * }\left( E\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( {S}^{n}\right) .
\]

It is therefore of interest to know when such a global form exists.

In Section 6 we constructed the global angular form \( \psi \) on a rank 2 vector bundle with structure group \( {SO}\left( 2\right) \) . This form \( \psi \) was seen to have the following two properties:

(a) \( \psi \) restricts to the volume form on each fiber, i.e., a generator of \( {H}_{c}^{2} \) (fiber) (b) \( {d\psi } =  - {\pi }^{ * }e \)

where \( e \) is the Euler class. Exactly the same procedure defines the angular form and the Euler class of a circle bundle with structure group \( {SO}\left( 2\right) \) .

Consequently, for such a bundle also, if the Euler class vanishes, then \( \psi \) is closed and satisfies the condition of the Leray-Hirsch theorem.

We now consider more generally a sphere bundle with structure group Diff \( \left( {S}^{n}\right) \) or \( O\left( {n + 1}\right) \) . We will see that the existence of a global form as above entails overcoming two obstructions: orientability and the Euler class.

## Orientability

In this section the base space of the bundle is assumed to be connected. A sphere bundle with fiber \( {S}^{n}, n \geq  1 \) , is said to be orientable if for each fiber \( {F}_{x} \) it is possible to choose a generator \( \left\lbrack  {\sigma }_{x}\right\rbrack \) of \( {H}^{n}\left( {F}_{x}\right) \) satisfying the local compatibility condition: around any point there is a neighborhood \( U \) and a generator \( \left\lbrack  {\sigma }_{U}\right\rbrack \) of \( {H}^{n}\left( {\left. E\right| }_{U}\right) \) such that for any \( x \) in \( U,\left\lceil  {\sigma }_{U}\right\rceil \) restricted to the fiber \( {F}_{x} \) is the chosen generator \( \left\lbrack  {\sigma }_{x}\right\rbrack \) ; equivalently, there is an open cover \( \left\{  {U}_{\alpha }\right\} \) of \( M \) and generators \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) of \( {H}^{n}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) so that \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   = \left\lbrack  {\sigma }_{\beta }\right\rbrack \) in \( {H}^{n}\left( {E{ \mid  }_{{U}_{\alpha } \cap  {U}_{\beta }}}\right) \) .

Since a generator of the top cohomology of a fiber is an \( n \) -form with total integral 1, there are two possible generators, depending on the orientation of the fiber. A priori all that one could say is that \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   =  \pm  \left\lbrack  {\sigma }_{\beta }\right\rbrack \) on \( {U}_{\alpha } \cap  {U}_{\beta } \) . For an orientable sphere bundle either choice of a consistent system of generators is called an orientation of the sphere bundle. A bundle with a given orientation is said to be oriented. An \( {S}^{0} \) -bundle over a manifold \( M \) is a double cover of \( M \) ; such a bundle over a connected base space is said to be orientable if and only if the total space has two connected components.

CAVEAT. The fact that the cohomology classes \( \left\{  \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right\} \) agree on overlaps does not mean that they piece together to form a global cohomology class. A global cohomology class must be represented by a global form; the equality of cohomology classes \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   = \left\lbrack  {\sigma }_{\beta }\right\rbrack \) implies only that the forms \( {\sigma }_{\alpha } \) and \( {\sigma }_{\beta } \) differ by an exact form.

Recall that in Section 7 we called a vector bundle of rank \( n + 1 \) orient-able if and only if it can be given by transition functions with values in \( {SO}\left( {n + 1}\right) \) . We now study the relation between the orientability of a sphere bundle and the orientability of a vector bundle.

Let \( E \) be a vector bundle of rank \( n + 1 \) endowed with a Riemannian metric so that its structure group is reduced to \( O\left( {n + 1}\right) \) . Its unit sphere bundle \( S\left( E\right) \) is the fiber bundle whose fiber at \( x \) consists of all the unit vectors in \( {E}_{x} \) and whose transition functions are the same as those of \( E \) . \( S\left( E\right) \) is an \( {S}^{n} \) -bundle with structure group \( O\left( {n + 1}\right) \) .

REMARK 11.1. Fix an orientation on the sphere \( {S}^{n} \) . If the linear transformation \( g \) is in the special orthogonal group \( {SO}\left( {n + 1}\right) \) and \( \left\lbrack  \sigma \right\rbrack \) is a generator of \( {H}^{n}\left( {S}^{n}\right) \) with \( {\int }_{{S}^{n}}\sigma  = 1 \) , then the image \( g\left( {S}^{n}\right) \) is the sphere \( {S}^{n} \) with the same orientation, so that

\[
{\int }_{{S}^{n}}{g}^{ * }\sigma  = {\int }_{g\left( {S}^{n}\right) }\sigma  = {\int }_{{S}^{n}}\sigma  = 1
\]

Thus for an orthogonal transformation \( g,{g}^{ * }\sigma \) and \( \sigma \) represent the same cohomology class if and only if \( g \) has positive determinant.

Proposition 11.2. A vector bundle \( E \) is orientable if and only if its sphere bündle \( S\left( E\right) \) is orientable.

Proof. \( \left(  \Rightarrow  \right) \) Fix a generator \( \sigma \) on \( {S}^{n} \) and fix a trivialization \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) for \( E \) so that the transition functions \( {g}_{\alpha \beta } \) assume values in \( {SO}\left( {n + 1}\right) \) . Let

\[
{\rho }_{\alpha } : {U}_{\alpha } \times  {S}^{n} \rightarrow  {S}^{n}
\]

be the projection and let \( {\pi }^{-1}\left( x\right) \) be the fiber of the sphere bundle \( \pi  : S\left( E\right)  \rightarrow  M \) at \( x \) . Define \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) in \( {H}^{n}\left( {\left. S\left( E\right) \right| }_{{U}_{\alpha }}\right) \) by

\[
\left\lbrack  {\sigma }_{\alpha }\right\rbrack   = {\phi }_{\alpha }^{ * }{\rho }_{\alpha }^{ * }\left\lbrack  \sigma \right\rbrack  .
\]

To avoid cumbersome notations we will write \( {\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{x} \) and \( {\left. {\phi }_{\alpha }\right| }_{x} \) for the restrictions \( {\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{{\pi }^{-1}\left( x\right) } \) and \( {\left. {\phi }_{\alpha }\right| }_{{\pi }^{-1}\left( x\right) } \) respectively. Then for every \( x \) in \( {U}_{\alpha } \) ,

\[
{\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{x} = {\left( {\phi }_{\alpha }{|}_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack  .
\]

For \( x \in  {U}_{\alpha } \cap  {U}_{\beta } \) ,

\[
{\left. \left\lbrack  {\sigma }_{\beta }\right\rbrack  \right| }_{x} = {\left. \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right| }_{x}
\]

\[
\text{ iff }{\left( {\left. {\phi }_{\beta }\right| }_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack   = {\left( {\left. {\phi }_{\alpha }\right| }_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack
\]

\[
\text{ iff }\left\lbrack  \sigma \right\rbrack   = {\left( {\left( {\left. {\phi }_{\beta }\right| }_{x}\right) }^{ * }\right) }^{-1}{\left( {\left. {\phi }_{\alpha }\right| }_{x}\right) }^{ * }\left\lbrack  \sigma \right\rbrack
\]

iff \( \left\lbrack  \sigma \right\rbrack   = {g}_{\alpha \beta }{\left( x\right) }^{ * }\left\lbrack  \sigma \right\rbrack \) .

Since \( {g}_{\alpha \beta }\left( x\right) \) has positive determinant, \( \left\lbrack  \sigma \right\rbrack   = {g}_{\alpha \beta }{\left( x\right) }^{ * }\left\lbrack  \sigma \right\rbrack \) by (11.1). Therefore, \( \left\lbrack  {\sigma }_{\beta }\right\rbrack   = \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) on \( {U}_{\alpha } \cap  {U}_{\beta } \) and the sphere bundle \( S\left( E\right) \) is orientable.

\( \left(  \Leftarrow  \right) \) Conversely, let \( \left\{  {{U}_{\alpha },\left\lbrack  {\sigma }_{\alpha }\right\rbrack  }\right\} \) be an orientation on the sphere bundle \( S\left( E\right) \) and let \( \left( {{S}^{n},\sigma }\right) \) be an oriented sphere in \( {\mathbb{R}}^{n + 1} \) , where \( \sigma \) is a nontrivial top form on \( {S}^{n} \) . Choose the trivializations for \( S\left( E\right) \)

\[
{\phi }_{\alpha } : {\left. S\left( E\right) \right| }_{{U}_{\alpha }} \rightarrow  {U}_{\alpha } \times  {S}^{n}
\]

in such a way that \( {\phi }_{a} \) preserves the metric and \( {\phi }_{\alpha }^{ * }{\rho }_{\alpha }^{ * }\left\lbrack  \sigma \right\rbrack   = \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) . Then at any point \( x \) in \( {U}_{\alpha } \cap  {U}_{\beta } \) , the transition function \( {g}_{\alpha \beta }\left( x\right) \) pulls \( \left\lbrack  \sigma \right\rbrack \) to itself and so \( {g}_{\alpha \beta }\left( x\right) \) must be in \( {SO}\left( {n + 1}\right) \) .

REMARK 11.3. Since \( {SO}\left( 1\right)  = \{ 1\} \) , a line bundle \( L \) over a connected base space is orientable if and only if it is trivial. In this case the sphere bundle \( S\left( L\right) \) consists of two connected components.

Proposition 11.4. A vector bundle \( E \) is orientable if and only if its determinant bundle det \( E \) is orientable.

Proof. Let \( \left\{  {g}_{\alpha \beta }\right\} \) be the transition functions of \( E \) . Then the transition functions of det \( E \) are \( \left\{  {\det {g}_{\alpha \beta }}\right\} \) . An orthogonal matrix \( {g}_{\alpha \beta } \) assumes values in \( {SO}\left( {n + 1}\right) \) if and only if det \( {g}_{\alpha \beta } \) is positive, so the proposition follows.

Whether \( E \) is orientable or not, the 0-sphere bundle \( S\left( {\text{ det }E}\right) \) is always a 2-sheeted covering of \( M \) . Combining Corollary 11.3 and Proposition 11.4, we see that over a connected base space a vector bundle \( E \) is orientable if and only if \( S\left( {\text{ det }E}\right) \) is disconnected. Since a simply connected base space cannot have any connected covering space of more than one sheet, we have proven the following.

Proposition 11.5. Every vector bundle over a simply connected base space is orientable.

In particular, the tangent bundle of a simply connected manifold is orientable. Since a manifold is orientable if and only if its tangent bundle is (Example 6.3), this gives

Corollary 11.6. Every simply connected manifold is orientable.

## The Euler Class of an Oriented Sphere Bundle

We first consider the case of a circle bundle \( \pi  : E \rightarrow  M \) with structure group Diff \( \left( {S}^{1}\right) \) . As stated in the introduction to this section, our problem is to find a closed global 1-form on \( E \) which restricts to a generator of the cohomology on each fiber. As a first approximation, in each \( {U}_{\alpha } \) of a good cover \( \left\{  {U}_{\alpha }\right\} \) of \( M \) we choose a generator \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack \) of \( {H}^{1}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) . The collection \( \left\{  {\sigma }_{\alpha }\right\} \) is an element \( {\sigma }^{0,1} \) in the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) :

![bo_d7b6f8alb0pc73dd9avg_126_690_1624_317_208_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_126_690_1624_317_208_0.jpg)

From the isomorphism between the cohomology of \( E \) and the cohomology of this double complex,

\[
{H}_{DR}^{ * }\left( E\right)  \simeq  {H}_{D}\left\{  {{C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) }\right\}  ,
\]

we see that to find a global form which restricts to the \( d \) -cohomology class of \( {\sigma }^{0,1} \) it suffices to extend \( {\sigma }^{0,1} \) to a \( D \) -cocycle. The first step of the extension requires that \( {\left( \delta {\sigma }^{0,1}\right) }_{\alpha \beta } = {\sigma }_{\beta } - {\sigma }_{\alpha } \) be exact, i.e., \( \left\lbrack  {\sigma }_{\alpha }\right\rbrack   = \left\lbrack  {\sigma }_{\beta }\right\rbrack \) for all \( \alpha ,\beta \) .

This is precisely the orientability condition. Assume the bundle \( E \) to be oriented with orientation \( {\sigma }^{0,1} \) , so that \( \delta {\sigma }^{0,1} = d{\sigma }^{1,0} \) for some \( {\sigma }^{1,0} \) in \( {C}^{1}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{0}}\right) \) . Then \( {\sigma }^{0,1} + {\sigma }^{1,0} \) is a \( D \) -cocycle if and only if \( \delta {\sigma }^{1,0} = 0 \) . Since

\[
d\left( {\delta {\sigma }^{1,0}}\right)  = \delta \left( {d{\sigma }^{1,0}}\right)  = \delta \left( {\delta {\sigma }^{0,1}}\right)  = 0,
\]

\( \delta {\sigma }^{1,0} \) actually comes from an element \( - \varepsilon \) of the cochain group \( {C}^{2}\left( {{\pi }^{-1}\mathfrak{U}}\right. \) , \( \mathbb{R} \) ). Now since the open covers \( \mathfrak{U} \) and \( {\pi }^{-1}\mathfrak{U} \) have the same combinatorics, i.e., \( {\pi }^{-1}{U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) is nonempty if and only if \( {U}_{{\alpha }_{0}\ldots {\alpha }_{p}} \) is, \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},\mathbb{R}}\right)  = {C}^{ * }\left( {\mathfrak{U},\mathbb{R}}\right) \) and we may regard \( \varepsilon \) as an element of \( {C}^{2}\left( {\mathfrak{U},\mathbb{R}}\right) \) . In fact, because \( {\delta \varepsilon } = 0,\varepsilon \) defines a Čech cohomology class in \( {H}^{2}\left( {\mathfrak{U},\mathbb{R}}\right) \) . By the isomorphism between the Čech cohomology of a good cover and de Rham cohomology, \( \varepsilon \) corresponds to a cohomology class \( e\left( E\right) \) in \( {H}^{2}\left( M\right) \) . For a circle bundle with structure group \( {SO}\left( 2\right) \) , this class turns out to be the Euler class of Section 6, as will be shown later. So for an oriented circle bundle \( E \) with structure group \( \operatorname{Diff}\left( {S}^{1}\right) \) we also call \( e\left( E\right) \) the Euler class.

The discussion above generalizes immediately to any sphere bundle with fiber \( {S}^{n}, n \geq  1 \) . Such a sphere bundle is orientable if and only if it is possible to find an element \( {\sigma }^{0, n} \) in \( {C}^{0}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{n}}\right) \) which extends one step down toward being a \( D \) -cocycle:

\[
\delta {\sigma }^{0, n} = d{\sigma }^{1, n - 1} =  - {D}^{\prime \prime }{\sigma }^{1, n - 1}.
\]

![bo_d7b6f8alb0pc73dd9avg_127_433_1174_786_316_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_127_433_1174_786_316_0.jpg)

There is no obstruction to extending \( {\sigma }^{1, n - 1} \) one step further, since every closed \( \left( {n - 1}\right) \) -form on \( {\left. E\right| }_{{U}_{{a0},{a1},{a2}}} \) is exact. In general, extension is possible until we hit a nontrivial cohomology of the fiber. Thus for an oriented sphere bundle \( E \) we can extend all the way down to \( {\sigma }^{n,0} \) in such a manner that if

\[
\sigma  = {\sigma }^{0, n} + {\sigma }^{1, n - 1} + \cdots  + {\sigma }^{n,0},
\]

then

\[
{D\sigma } = \delta {\sigma }^{n,0}.
\]

Since \( d\left( {\delta {\sigma }^{n,0}}\right)  = \delta \left( {d{\sigma }^{n,0}}\right)  =  \pm  \delta \left( {\delta {\sigma }^{n - 1,1}}\right)  = 0 \) ,

\[
{D\sigma } = \delta {\sigma }^{n,0} = i\left( {-\varepsilon }\right)
\]

for some \( \varepsilon \) in \( {C}^{n + 1}\left( {{\pi }^{-1}\mathfrak{U},\mathbb{R}}\right)  \simeq  {C}^{n + 1}\left( {\mathfrak{U},\mathbb{R}}\right) \) , where \( i \) is the inclusion \( {C}^{n + 1}\left( {{\pi }^{-1}\mathfrak{U},\mathbb{R}}\right)  \rightarrow  {C}^{n + 1}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{0}}\right) \) . Clearly \( {\delta \varepsilon } = 0 \) , so \( \varepsilon \) defines a cohomology class \( e\left( E\right) \) in \( {H}^{n + 1}\left( {\mathfrak{U},\mathbb{R}}\right)  \simeq  {H}^{n + 1}\left( M\right) \) , the Euler class of the oriented \( {S}^{n} \) -bundle \( E \) with orientation \( {\sigma }^{0, n} \) . The Euler class of an oriented \( {S}^{0} \) -bundle is defined to be 0 . Note that the Euler class depends on the orientation \( \left\{  \left\lbrack  {\sigma }_{a}\right\rbrack  \right\} \) of \( E \) ; the opposite orientation would give \( - e\left( E\right) \) instead.

If \( E \) is an oriented vector bundle, the complement \( {E}^{0} \) of its zero section has the homotopy type of an oriented sphere bundle. The Euler class of \( E \) is defined to be that of \( {E}^{0} \) . Equivalently, if \( E \) is endowed with a Riemannian metric, then the unit sphere bundle \( S\left( E\right) \) of \( E \) makes sense and we may define the Euler class of \( E \) to be that of its unit sphere bundle. This latter definition is independent of the metric and in fact agrees with the definition in terms of \( {E}^{0} \) , since for any metric on \( E \) , the unit sphere bundle \( S\left( E\right) \) has the homotopy type of \( {E}^{0} \) .

In the next two propositions we show that the Euler class is well defined.

Proposition 11.7. For a given orientation \( \left\{  \left\lbrack  {\sigma }_{a}\right\rbrack  \right\} \) the Euler class is independent of the choice of \( {\sigma }^{j, n - j}, j = 0,\ldots , n \) .

Proof.

![bo_d7b6f8alb0pc73dd9avg_128_573_976_494_366_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_128_573_976_494_366_0.jpg)

Let \( {\overline{\sigma }}^{0, n} \) be another cochain in \( {C}^{0}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{n}}\right) \) which represents the orientation \( \left\{  \left\lbrack  {\sigma }_{\alpha }\right\rbrack  \right\} \) . Then \( {\overline{\sigma }}^{0, n} - {\sigma }^{0, n} = d{\tau }^{n - 1} \) for some \( {\tau }^{n - 1} \) in \( {C}^{0}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{n - 1}}\right) \) . Since \( d\left( {\delta {\tau }^{n - 1}}\right) \) and \( d\left( {{\overline{\sigma }}^{1, n - 1} - {\sigma }^{1, n - 1}}\right) \) are equal, \( \delta {\tau }^{n - 1} \) and \( {\overline{\sigma }}^{1, n - 1} - {\sigma }^{1, n - 1} \) differ by \( d{\tau }^{n - 2} \) for some \( {\tau }^{n - 2} \) in \( {C}^{1}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{n - 2}}\right) \) . Again,

\[
d\left( {\delta {\tau }^{n - 2}}\right)  =  - d\left( {{\overline{\sigma }}^{2, n - 2} - {\sigma }^{2, n - 2}}\right) ,
\]

so

\[
\left( {\delta {\tau }^{n - 2}}\right)  - \left( {{\overline{\sigma }}^{2, n - 2} - {\sigma }^{2, n - 2}}\right)  = d{\tau }^{n - 3}
\]

for some \( {\tau }^{n - 3} \) in \( {C}^{2}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{n - 3}}\right) \) . Eventually we get

\[
\delta {\tau }^{0} - \left( {{\overline{\sigma }}^{n,0} - {\sigma }^{n,0}}\right)  = {i\tau },\tau  \in  {C}^{n}\left( {{\pi }^{-1}\mathfrak{U},\mathbb{R}}\right) .
\]

Taking \( \delta \) of both sides, we have

\[
\overline{\varepsilon } - \varepsilon  = {\delta \tau }.
\]

So \( \overline{\varepsilon } \) and \( \varepsilon \) define the same Čech cohomology class.

Proposition 11.8. The Euler class \( e\left( E\right) \) is independent of the choice of the good cover.

Proof. Write \( {\varepsilon }_{\mathfrak{U}} \) for the cocycle in \( {H}^{n + 1}\left( {\mathfrak{U},\mathbb{R}}\right) \) which defines the Euler class in terms of the good cover \( \mathfrak{U} \) . If a good cover \( \mathfrak{V} \) is a refinement of \( \mathfrak{U} \) , then there is a commutative diagram

![bo_d7b6f8alb0pc73dd9avg_129_558_438_509_221_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_129_558_438_509_221_0.jpg)

\( {\varepsilon }_{\mathfrak{U}} \) and \( {\varepsilon }_{\mathfrak{D}} \) give the same element in \( {H}_{DR}^{n + 1}\left( M\right) \) , because if we choose the \( {\sigma }^{0, n} \) on \( {\pi }^{-1}\mathfrak{B} \) to be the restriction of the \( {\sigma }^{0, n} \) on \( {\pi }^{-1}\mathfrak{U} \) , the cocycle \( {\varepsilon }_{\mathfrak{B}} \) in \( {C}^{n + 1}(\mathfrak{B} \) , \( \mathbb{R}) \) will be the restriction of the cocycle \( {\varepsilon }_{\mathfrak{U}} \) in \( {C}^{n + 1}\left( {\mathfrak{U},\mathbb{R}}\right) \) , so that as elements of the Čech cohomology \( {H}^{n + 1}\left( {M,\mathbb{R}}\right) \) they are equal. Given two arbitrary good covers \( \mathfrak{U} \) and \( \mathfrak{B} \) , we can take a common refinement \( \mathfrak{W} \) ; then \( {\varepsilon }_{\mathfrak{U}} = \; {\varepsilon }_{\mathfrak{B}} = {\varepsilon }_{\mathfrak{W}} \) in \( {H}^{n + 1}\left( {M,\mathbb{R}}\right) \) . So the Euler class is independent of the cover.

If the Euler class \( e\left( E\right)  \in  {H}^{n + 1}\left( M\right) \) vanishes, its representative \( \varepsilon  \in  {C}^{n + 1}\left( {\mathfrak{U},\mathbb{R}}\right) \) is a \( \delta \) -coboundary; this permits one to alter \( {\sigma }^{n,0} \) so that \( {D\sigma } = 0 \) . The \( D \) -cocycle \( \sigma \) then corresponds to a global form which restricts to the \( d \) - cohomology class of \( {\sigma }^{0, n} \) . In sum, then, there is a global form that restricts to a generator on each fiber if and only if

(a) \( E \) is orientable, and

(b) the Euler class \( e\left( E\right) \) vanishes.

For \( E \) a product bundle, the extension stops at the \( {\sigma }^{0, n} \) stage so that \( \varepsilon  = 0 \) . In this sense the Euler class is a measure of the twisting of an oriented sphere bundle. However, as we will see in the proposition below, \( E \) need not be a product bundle for its Euler class to vanish.

Proposition 11.9. If the oriented sphere bundle \( E \) has a section, then its Euler class vanishes.

Proof. Let \( s \) be a section of \( E \) . It follows from \( \pi  \circ  s = 1 \) that \( {s}^{ * }{\pi }^{ * } = 1 \) . We saw in the construction of the Euler class that

\[
- {\pi }^{ * }\varepsilon  = {D\sigma }
\]

for some \( D \) -cochain \( \sigma \) . Applying \( {s}^{ * } \) to both sides gives

\[
- \varepsilon  = D{s}^{ * }\sigma ,
\]

so \( e \) is a coboundary in \( {H}^{ * }\left( M\right) \) .

The converse of this proposition is not true. In general a cohomology class is too "coarse" an invariant to yield information on the existence of geometrical constructs. In (23.16) we will show the existence of a sphere bundle whose Euler class vanishes, but which does not admit any section.

We now show that for a circle bundle \( \pi  : E \rightarrow  M \) with structure group \( {SO}\left( 2\right) \) the definitions of the Euler class in Section 6 and in this section agree. We briefly recall here the earlier construction. If \( {\theta }_{\alpha } \) is the angular coordinate over \( {U}_{\alpha } \) , then \( \left\lbrack  {d{\theta }_{\alpha }/{2\pi }}\right\rbrack \) is a generator of \( {H}^{1}\left( {\left. E\right| }_{{U}_{\alpha }}\right) \) . Furthermore,

\[
\frac{d{\theta }_{\beta }}{2\pi } - \frac{d{\theta }_{\alpha }}{2\pi } = {\pi }^{ * }\frac{d{\phi }_{\alpha \beta }}{2\pi } = {\pi }^{ * }{\xi }_{\beta } - {\pi }^{ * }{\xi }_{\alpha }\text{ for some 1-form }{\xi }_{\alpha }\text{ over }{U}_{\alpha }.
\]

The Euler class of the circle bundle \( E \) was defined to be the cohomology class of the global form \( \left\{  {d{\xi }_{\alpha }}\right\} \) .

In the present context these cochains fit into the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) of \( E \) as shown in the diagram below.

![bo_d7b6f8alb0pc73dd9avg_130_449_773_745_373_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_130_449_773_745_373_0.jpg)

\[
{C}^{ * }\left( {{\pi }^{-1}\mathcal{U},\mathbb{R}}\right)
\]

By the explicit isomorphism between de Rham and Čech (Proposition 9.8), the differential form on \( M \) corresponding to the Čech cocycle \( \varepsilon \) is \( {\left( -{D}^{\prime \prime }K\right) }^{2}\varepsilon \) . Since \( {\xi }_{\beta } - {\xi }_{\alpha } = \left( {1/{2\pi }}\right) d{\phi }_{\alpha \beta },{\delta \xi } = \left( {1/{2\pi }}\right) {d\phi } \) , so by (8.7), we may take \( \xi \) to be \( \left( {1/{2\pi }}\right) {Kd\phi } \) . Also note that since \( \delta \left( {\phi /{2\pi }}\right)  =  - \varepsilon \) ,

\[
- {K\varepsilon } = \phi /{2\pi }\text{ (modulo a }\delta \text{ -coboundary). }
\]

Hence

\[
{\left( -{D}^{\prime \prime }K\right) }^{2}\varepsilon  =  - {dKdK\varepsilon }
\]

\[
= {dKd}\left( {\left( {\phi /{2\pi }}\right)  + {\delta \tau }}\right) \text{ for some }\tau
\]

\[
= {dKd}\left( {\phi /{2\pi }}\right)  + {dKd}{\delta \tau }
\]

\[
= {d\xi } + {dKd}{\delta \tau }.
\]

Here

\[
{dKd\delta \tau } = {dK\delta d\tau }\;\text{ because }d\text{ commutes with }\delta
\]

\[
= d\left( {1 - {\delta K}}\right) {d\tau }\text{ by }\left( {8.7}\right)
\]

\[
=  - {\delta dKd\tau }\text{ . }
\]

Since \( {Kd\tau } \in  {\Omega }^{1}\left( M\right) ,{dKd\tau } \) is a global exact form, so \( {\delta dKd\tau } = 0 \) . Hence \( {\left( -{D}^{\prime \prime }K\right) }^{2}\varepsilon  = {d\xi } \) , showing that the two definitions of the Euler class could be made to agree on the level of forms.

## The Global Angular Form

In Section 6 we exhibited on an oriented circle bundle the global angular form \( \psi \) which has the following properties:

(a) its restriction to each fiber is a generator of the cohomology of the fiber;

(b) \( {d\psi } =  - {\pi }^{ * }e \) , where \( e \) represents the Euler class of the circle bundle.

Using the collating formula (9.5) we will now construct such a form on any oriented \( {S}^{n} \) -bundle.

Let \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) be an open cover of \( M \) . Recall that the Euler class of \( E \) is defined by the following diagram:

![bo_d7b6f8alb0pc73dd9avg_131_505_866_609_247_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_131_505_866_609_247_0.jpg)

where \( {\alpha }_{0} \in  {C}^{0}\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{n}}\right) \) is the orientation of \( E \) ,

\[
\delta {\alpha }_{i} =  - {D}^{\prime \prime }{\alpha }_{i + 1},\;i = 0,\ldots , n - 1,
\]

and

\[
\delta {\alpha }_{n} =  - {\pi }^{ * }\varepsilon
\]

Hence

\[
D\left( {{\alpha }_{0} + \cdots  + {\alpha }_{n}}\right)  =  - {\pi }^{ * }\varepsilon .
\]

Here \( {\alpha }_{i} \) is what we formerly wrote as \( {\sigma }^{i, n - i} \) .

If \( \left\{  {\rho }_{\alpha }\right\} \) is a partition of unity subordinate to the open cover \( \mathfrak{U} = \left\{  {U}_{\alpha }\right\} \) , then \( \left\{  {{\pi }^{ * }{\rho }_{\alpha }}\right\} \) is a partition of unity subordinate to the inverse cover \( {\pi }^{-1}\mathfrak{U} = \; \left\{  {{\pi }^{-1}{U}_{\alpha }}\right\} \) . Using these data we can define a homotopy operator \( K \) on the double complex \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) and also one on \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) as in (8.6). We denote both operators by \( K \) . Both \( K \) satisfy

\[
{\delta K} + {K\delta } = 1.
\]

Since

\[
{\left( K{\pi }^{ * }\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} = \sum \left( {{\pi }^{ * }{\rho }_{\alpha }}\right) {\left( {\pi }^{ * }\omega \right) }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}
\]

\[
= {\pi }^{ * }\sum {\rho }_{\alpha }{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}}
\]

\[
= {\left( {\pi }^{ * }K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}},
\]

\( K \) commutes with \( {\pi }^{ * } \) .

Exercise 11.10. If \( s : M \rightarrow  E \) is a section, show that \( K{s}^{ * } = {s}^{ * }K \) .

By the collating formula (9.5),

(11.11)

\[
\psi  = \mathop{\sum }\limits_{{i = 0}}^{n}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} + {\left( -1\right) }^{n + 1}K{\left( {D}^{\prime \prime }K\right) }^{n}\left( {-{\pi }^{ * }\varepsilon }\right)
\]

is a global form on \( E \) . Furthermore,

\[
{d\psi } = {\left( -1\right) }^{n + 1}{dK}{\left( {D}^{\prime \prime }K\right) }^{n}\left( {-{\pi }^{ * }\varepsilon }\right)
\]

\[
=  - {\pi }^{ * }{\left( -1\right) }^{n + 1}{\left( {D}^{\prime \prime }K\right) }^{n + 1}\varepsilon \;\text{ since }{\pi }^{ * }\text{ commutes with }{D}^{\prime \prime }K
\]

(11.12)

\[
=  - {\pi }^{ * }e\text{ by Proposition 9.8. }
\]

In formula (11.11) since the restriction of \( {\pi }^{ * }\left( {{\left( -1\right) }^{n + 1}K{\left( {D}^{\prime \prime }K\right) }^{n}\varepsilon }\right) \) to a fiber is 0, the restriction of the global form \( \psi \) to each fiber is \( d \) -cohomologous to \( {\left. {\alpha }_{0}\right| }_{\text{ fiber }} \) , hence is a generator of the cohomology of the fiber. The global \( n \) -form \( \psi \) on the sphere bundle \( E \) satisfies the properties \( \left( a\right) \) and \( \left( b\right) \) stated earlier. We call it the global angular form on the sphere bundle.

REMARK 11.12.1. Let \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) be an open cover of \( M \) which trivializes the \( n \) -sphere bundle \( E \) and let \( \psi \) and \( e \) be defined by (11.11) and (11.12). Then Supp \( {d\psi } \subset   \cup  {\pi }^{-1}\left( {U}_{{\alpha }_{0}\ldots {\alpha }_{n}}\right) \) and Supp \( e \) is contained in the union \( \cup  {U}_{{\alpha }_{0}\ldots {\alpha }_{n}} \) of the \( \left( {n + 1}\right) \) -fold intersections.

Proof. By (8.6), \( \operatorname{Supp}{\left( K\omega \right) }_{{\alpha }_{0}\ldots {\alpha }_{p - 1}} \subset  { \cup  }_{\alpha }\operatorname{Supp}{\omega }_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \subset  { \cup  }_{\alpha }{U}_{\alpha {\alpha }_{0}\ldots {\alpha }_{p - 1}} \) . Since Supp \( \varepsilon  \subset   \cup  {U}_{{\alpha }_{0}\ldots {\alpha }_{n}} \) , the remark follows from (11.11) and (11.12).

Exercise 11.13. Use the existence of the global angular form \( \psi \) to prove Proposition 11.9.

## Euler Number and the Isolated Singularities of a Section

Let \( \pi  : E \rightarrow  M \) be an oriented \( \left( {k - 1}\right) \) -sphere bundle over a compact oriented manifold of dimension \( k \) . Since \( {H}^{k}\left( M\right)  \simeq  \mathbb{R} \) , the Euler class of \( E \) may be identified with the number \( {\int }_{M}e\left( E\right) \) , which is by definition the Euler number of \( E \) . The Euler number of the manifold \( M \) is defined to be that of its unit tangent bundle \( S\left( {T}_{M}\right) \) relative to some Riemannian structure on \( M \) . While the Euler number of an orientable sphere bundle is defined only up to sign, depending on the orientations of both \( E \) and \( M \) , the Euler number of the orientable manifold \( M \) is unambiguous, since reversing the orientation of \( M \) also reverses that of the tangent bundle.

In general the sphere bundle \( E \) will not have a global section; however, there may be a section \( s \) over the complement of a finite number of points \( {x}_{1},\ldots ,{x}_{q} \) in \( M \) . In fact, as we will show in Proposition 11.14, if the sphere bundle has structure group \( O\left( k\right) \) , then such a "partial" section \( s \) always exists. In this section we will explain how one may compute the Euler class of \( E \) in terms of the behavior of the section \( s \) near the singularities \( {x}_{1},\ldots ,{x}_{q} \) .

Proposition 11.14. Let \( \pi  : E \rightarrow  M \) be a \( \left( {k - 1}\right) \) -sphere bundle over a compact manifold of dimension \( k \) . Suppose the structure group of \( E \) can be reduced to \( O\left( k\right) \) . Then \( E \) has a section over \( M - \left\{  {{x}_{1},\ldots ,{x}_{q}}\right\} \) for some finite number of points in \( M \) .

Proof. Since the structure group of \( E \) is \( O\left( k\right) \) , we can form a Riemannian vector bundle \( {E}^{\prime } \) of rank \( k \) whose unit sphere bundle is \( E \) . A section \( {s}^{\prime } \) of \( {E}^{\prime } \) over \( M \) gives rise to a partial section \( s \) of \( E : s\left( x\right)  = {s}^{\prime }\left( x\right) /\begin{Vmatrix}{{s}^{\prime }\left( x\right) }\end{Vmatrix} \) , where \( \parallel \) denotes the length of a vector in \( {E}^{\prime } \) . Let \( Z \) be the zero locus of \( {s}^{\prime };s \) is only a partial section in the sense that it is not defined over \( Z \) . Thus to prove the proposition, we only have to show that the vector bundle \( {E}^{\prime } \) has a section that vanishes over a finite number of points.

This is an easy consequence of the transversality theorem which states that given a submanifold \( Z \) in a manifold \( Y \) , every map \( f : X \rightarrow  Y \) becomes transversal to \( Z \) under a slight perturbation (Guillemin and Pollack [1, p. 68]). Furthermore, we may assume that a small perturbation of a section \( t \) of \( {E}^{\prime } \) is again a section, as follows. Suppose \( f \) is a perturbation of \( t \) and \( f \) is transversal to the zero section. Then \( g = \pi  \circ  f \) is a perturbation of \( \pi  \circ  t \) , which is the identity. Thus, for a sufficiently small perturbation, \( g \) will be close to the identity and so must be a diffeomorphism. For such an \( f \) , define \( {s}^{\prime }\left( x\right)  = \; f\left( {{g}^{-1}\left( x\right) }\right) \) . Then \( \pi  \circ  {s}^{\prime } = 1 \) and \( {s}^{\prime } \) is transversal to \( {s}_{0}\left( M\right) \) , i.e., \( S = {s}^{\prime }\left( M\right) \) intersects \( {S}_{0} = {s}_{0}\left( M\right) \) transversally. Applying this procedure to the zero section of \( {E}^{\prime } \) , i.e., choosing \( t = {s}_{0} \) , will yield the desired transversal section \( {s}^{\prime } \) for \( {E}^{\prime } \) . Since

\[
\dim S + \dim {S}_{0} = \dim {E}^{\prime },
\]

\( S \cap  {S}_{0} \) consists of a discrete set of points. By the compactness of \( S \) , it must be a finite set of points.

REMARK 11.15. It follows from the rudiments of obstruction theory that this proposition is true even if the structure group of the sphere bundle cannot be reduced to an orthogonal group. For a beautiful account of obstruction theory, see Steenrod [1, Part III].

Suppose \( s \) is a section over a punctured neighborhood of a point \( x \) in \( M \) . Choose this neighborhood sufficiently small so that it is diffeomorphic to a punctured disc in \( {\mathbb{R}}^{k} \) and \( E \) is trivial over it. Let \( {D}_{r} \) be the open neighborhood of \( x \) corresponding to the ball of radius \( r \) in \( {\mathbb{R}}^{k} \) under the diffeomorphism above. As an open subset of the oriented manifold \( M,{D}_{r} \) is also oriented. Choose the orientation on the sphere \( {S}^{k - 1} \) in such a way that the isomorphism \( E{ \mid  }_{{D}_{r}} \simeq  {D}_{r} \times  {S}^{k - 1} \) is orientation-preserving, where \( {D}_{r} \times  {S}^{k - 1} \) is given the product orientation. (If \( A \) and \( B \) are two oriented manifolds with orientation forms \( {\omega }_{A} \) and \( {\omega }_{B} \) , then the product orientation on \( A \times  B \) is given by \( \left( {{p}_{1}^{ * }{\omega }_{A}}\right)  \land  \left( {{p}_{2}^{ * }{\omega }_{B}}\right) \) , where \( {p}_{1} \) and \( {p}_{2} \) are the projections of \( A \times  B \) onto \( A \) and \( B \) respectively.) The local degree of the section \( s \) at \( x \) is defined to be the degree of the composite map

\[
\partial {\bar{D}}_{r}\overset{s}{ \rightarrow  }{\left. E\right| }_{{\bar{D}}_{r}} = {\bar{D}}_{r} \times  {S}^{k - 1}\overset{\rho }{ \rightarrow  }{S}^{k - 1}
\]

where \( \rho \) is the projection and \( {\bar{D}}_{r} \) is the closure of \( {D}_{r} \) .

Theorem 11.16. Let \( \pi  : E \rightarrow  M \) be an oriented \( \left( {k - 1}\right) \) -sphere bundle over a compact oriented manifold of dimension \( k \) . If \( E \) has a section over \( M - \left\{  {x}_{1}\right. \) , \( \left. {\ldots ,{x}_{q}}\right\} \) , then the Euler number of \( E \) is the sum of the local degrees of \( s \) at \( {x}_{1},\ldots ,{x}_{q} \) .

Proof. We first show that it is possible to move the support of the Euler class away from finitely many points.

Lemma. Let \( M \) be a manifold and \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) an open cover of \( M \) . Given finitely many points \( {x}_{1},\ldots ,{x}_{q} \) on \( M \) , there is a refinement \( {\left\{  {V}_{\alpha }\right\}  }_{\alpha  \in  I} \) of \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) such that \( {V}_{\alpha } \subset  {U}_{\alpha } \) and each \( {x}_{i} \) has a neighborhood \( {W}_{i} \) which is disjoint from all but one of the \( {V}_{\alpha } \) ’s.

Proof of LEMMA. Suppose \( {x}_{1} \in  {U}_{1} \) . Let \( {W}_{1} \) be an open neighborhood of \( {x}_{1} \) such that \( {x}_{1} \in  {W}_{1} \subset  {\bar{W}}_{1} \subset  {U}_{1} \) . We define a new open cover \( {\left\{  {U}_{\alpha }^{\prime }\right\}  }_{\alpha  \in  I} \) by setting \( {U}_{1}^{\prime } = {U}_{1} \) and \( {U}_{\alpha }^{\prime } = {U}_{\alpha } - {\bar{W}}_{1} \) for \( \alpha  \neq  1 \) . (Check that this is indeed an open cover of \( M \) .) The neighborhood \( {W}_{1} \) of \( {x}_{1} \) is contained in \( {U}_{1}^{\prime } \) but disjoint from all \( {U}_{\alpha }^{\prime },\alpha  \neq  1 \) .

Next suppose \( {x}_{2} \in  {U}_{2}^{\prime } \) . Let \( {W}_{2} \) be an open neighborhood of \( {x}_{2} \) such that \( {x}_{2} \in  {W}_{2} \subset  {\bar{W}}_{2} \subset  {U}_{2}^{\prime } \) . As before define a new open cover \( {\left\{  {U}_{\alpha }^{\prime \prime }\right\}  }_{\alpha  \in  I} \) by setting \( {U}_{2}^{\prime \prime } = {U}_{2}^{\prime } \) and \( {U}_{\alpha }^{\prime \prime } = {U}_{\alpha }^{\prime } - {\bar{W}}_{2} \) for \( \alpha  \neq  2 \) . Since \( {U}_{\alpha }^{\prime \prime } \subset  {U}_{\alpha }^{\prime } \) , the open neighborhood \( {W}_{1} \) of \( {x}_{1} \) is disjoint from all \( {U}_{\alpha }^{\prime \prime },\alpha  \neq  1 \) . By definition, the open neighborhood \( {W}_{2} \) of \( {x}_{2} \) is disjoint from all \( {U}_{\alpha }^{\prime \prime },\alpha  \neq  2 \) . Repeating this process to \( {x}_{3},\ldots ,{x}_{q} \) in succession yields the open cover \( \left\{  {V}_{\alpha }\right\} \) of the lemma.

Now let \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) be an open cover of \( M \) which trivializes \( E \) . By the lemma we may assume that each \( {x}_{i} \) has a neighborhood \( {W}_{i} \) which is contained in exactly one \( {U}_{\alpha } \) . Construct the global angular form \( \psi \) and the form \( e \) relative to \( {\left\{  {U}_{\alpha }\right\}  }_{\alpha  \in  I} \) . By Remark 11.12.1, since Supp \( e \subset   \cup  {U}_{{\alpha }_{0}\ldots {\alpha }_{k - 1}} \) , the form \( e \) must vanish on \( {W}_{i} \) for all \( i = 1,\ldots , q \) . So \( e \) is supported away from the points \( {x}_{1},\ldots ,{x}_{q} \) .

For each \( i \) choose an open ball \( {D}_{i} \) around the point \( {x}_{i} \) so that \( {D}_{i} \subset  {W}_{i} \) . Then(11.16.1)

\[
{\int }_{M}e = {\int }_{M -  \cup  {D}_{i}}e = {\int }_{M -  \cup  {D}_{i}}{s}^{ * }{\pi }^{ * }e
\]

since \( s \) is a global section over \( M -  \cup  {D}_{i} \)

\[
=  - {\int }_{M -  \cup  {D}_{i}}{s}^{ * }{d\psi }
\]

because \( {\pi }^{ * }e =  - {d\psi } \)

\[
= \mathop{\sum }\limits_{i}{\int }_{\partial {\bar{D}}_{i}}{s}^{ * }\psi
\]

by Stokes' theorem and the fact that \( \partial {\bar{D}}_{i} \) has the opposite orientation as

\( \partial \left( {M -  \cup  {D}_{i}}\right) \) .

Although the global angular form is not closed, by our construction \( {d\psi } = 0 \) on \( {\left. E\right| }_{{W}_{i}} \) , so \( \psi \) defines a cohomology class in \( {H}^{k - 1}\left( {\left. E\right| }_{{W}_{i}}\right) \) , which is in fact the generator. Let \( \sigma \) be the generator of \( {S}^{k - 1} \) . Then \( {\rho }^{ * }\sigma \) restricts to the generator on each fiber of \( {\left. E\right| }_{W} \) . So \( {\rho }^{ * }\sigma \) and the angular form \( \psi \) define the same cohomology class in \( {H}^{k - 1}\left( {\left. E\right| }_{{W}_{i}}\right) \) , i.e.,

\[
\psi  - {\rho }^{ * }\sigma  = {d\tau }
\]

for some \( \left( {k - 2}\right) \) -form \( {\left. \tau \text{ on }E\right| }_{{W}_{i}} \) . Thus on \( {\bar{D}}_{i} \) ,

\[
{s}^{ * }\psi  - {s}^{ * }{\rho }^{ * }\sigma  = {s}^{ * }{d\tau }
\]

and

\[
{\int }_{\partial \overline{{D}_{r}}}{s}^{ * }\psi  - {\int }_{\partial \overline{{D}_{r}}}{s}^{ * }{\rho }^{ * }\sigma  = {\int }_{\partial \overline{{D}_{r}}}d{s}^{ * }\tau  = 0\;\text{ by Stokes’ theorem. }
\]

Therefore,

\[
{\int }_{\partial {\bar{D}}_{r}}{s}^{ * }\psi  = \text{ local degree of the section }s\text{ at }{x}_{i}.
\]

Together with (11.16.1), this gives

\[
{\int }_{M}e = \mathop{\sum }\limits_{i}\left( {\text{ local degree of }s\text{ at }{x}_{i}}\right) .
\]

This theorem can also be phrased in terms of vector bundles. Let \( \pi  : E \rightarrow  M \) be an oriented rank \( k \) vector bundle over a manifold of dimension \( k \) and \( s \) a section of \( E \) with a finite number of zeros. The multiplicity of a zero \( x \) of \( s \) is defined to be the local degree of \( x \) as a singularity of the section \( s/\parallel s\parallel \) of the unit sphere bundle of \( E \) relative to some Riemannian structure on \( E \) . (This definition of the index is independent of the Riemannian structure because the local degree is a homotopy invariant.) Since the Euler class \( e\left( E\right) \) of \( E \) is a \( k \) -form on \( M \) , it is Poincaré dual to \( {nP} \) , where \( n = {\int }_{M}e\left( E\right) \) and \( P \) is a point on \( M \) . Thus we have the following.

Theorem 11.17. Let \( \pi  : E \rightarrow  M \) be an oriented rank \( k \) vector bundle over a compact oriented manifold of dimension \( k \) . Let \( s \) be a section of \( E \) with a finite number of zeros. The Euler class of \( E \) is Poincaré dual to the zeros of \( s \) , counted with the appropriate multiplicities.

EXAMPLE 11.18 (The Euler class of the unit tangent bundle to \( {S}^{2} \) ). Let \( S\left( {T}_{{S}^{2}}\right) \) be the unit tangent bundle to \( {S}^{2} \) . It is a circle bundle over \( {S}^{2} \) :

![bo_d7b6f8alb0pc73dd9avg_135_720_1678_198_177_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_135_720_1678_198_177_0.jpg)

Fix a unit tangent vector \( v \) at the north pole. We can define a smooth vector field on \( {S}^{2} \) -\{south pole\} by parallel translating \( v \) along the great circles from the north pole to the south pole (see Figure 11.1). (Parallel translation along a great circle on \( {S}^{2} \) is prescribed by the following two conditions:

(a) the tangent field to the great circle is parallel;

(b) the angles are preserved under parallel translation.)

![bo_d7b6f8alb0pc73dd9avg_136_392_301_310_317_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_136_392_301_310_317_0.jpg)

Figure 11.1

![bo_d7b6f8alb0pc73dd9avg_136_944_385_313_242_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_136_944_385_313_242_0.jpg)

Figure 11.2

This gives a section \( s \) of \( S\left( {T}_{{S}^{2}}\right) \) over \( {S}^{2} \) -\{south pole\}. On a small circle around the south pole, the vector field looks like Figure 11.2, i.e., as we go around the circle \( {90}^{ \circ  } \) , the vectors rotate through \( {180}^{ \circ  } \) ; therefore, the local degree of \( s \) at the south pole is 2 . By Theorem 11.16, the Euler number of the unit tangent bundle to \( {S}^{2} \) is 2 .

Exercise 11.19. Show that the Euler class of an oriented sphere bundle with even-dimensional fibers is zero, at least when the sphere bundle comes from a vector bundle.

Since the Euler class is the obstruction to finding a closed global angular form on an oriented sphere bundle, by the Leray-Hirsch theorem we have the following corollary of Exercise 11.19.

Proposition 11.20. If \( \pi  : E \rightarrow  M \) is an orientable \( {S}^{2n} \) -bundle, then

\[
{H}^{ * }\left( E\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( {S}^{2n}\right) .
\]

Exercise 11.21. Compute the Euler class of the unit tangent bundle of the sphere \( {S}^{k} \) by finding a vector field on \( {S}^{k} \) and computing its local degrees.

Euler Characteristic and the Hopf Index Theorem

In this section we show that the Euler number \( {\int }_{M}e\left( {T}_{M}\right) \) is the same as the Euler characteristic \( \chi \left( M\right)  = \sum {\left( -1\right) }^{q}\dim {H}^{q}\left( M\right) \) and deduce as a corollary the Hopf index theorem. The manifold \( M \) is assumed to be compact and oriented.

Let \( \left\{  {\omega }_{i}\right\} \) be a basis of the vector space \( {H}^{ * }\left( M\right) ,\left\{  {\tau }_{j}\right\} \) be the dual basis under Poincaré duality, i.e., \( {\int }_{M}{\omega }_{i} \land  {\tau }_{j} = {\delta }_{ij} \) , and let \( \pi \) and \( \rho \) be the two projections of \( M \times  M \) to \( M \) :

![bo_d7b6f8alb0pc73dd9avg_136_694_1944_289_191_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_136_694_1944_289_191_0.jpg)

By the Künneth formula, \( {H}^{ * }\left( {M \times  M}\right)  = {H}^{ * }\left( M\right)  \otimes  {H}^{ * }\left( M\right) \) with \( \left\{  {{\pi }^{ * }{\omega }_{i} \land  }\right. \; \left. {{\rho }^{ * }{\tau }_{j}}\right\} \) as an additive basis. So the Poincaré dual \( {\eta }_{\Delta } \) of the diagonal \( \Delta \) in \( M \times  M \) is some linear combination \( {\eta }_{\Delta } = \sum {c}_{ij}{\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{j} \) .

Lemma 11.22. \( {\eta }_{\Delta } = \sum {\left( -1\right) }^{\deg {\omega }_{i}}{\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{i} \) .

Proof. We compute \( {\int }_{\Delta }{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} \) in two ways. On the one hand, we can pull this integral back to \( M \) via the diagonal map \( \iota  : M \rightarrow  \Delta  \subset  M \times  M \) :

\[
{\int }_{\Delta }{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} = {\int }_{M}{\iota }^{ * }{\pi }^{ * }{\tau }_{k} \land  {\iota }^{ * }{\rho }^{ * }{\omega }_{l} = {\int }_{M}{\tau }_{k} \land  {\omega }_{l} = {\left( -1\right) }^{\left( {\deg {\tau }_{k}}\right) \left( {\deg {\omega }_{l}}\right) }{\delta }_{kl}.
\]

On the other hand, by the definition of the Poincaré dual of a closed oriented submanifold (5.13),

\[
{\int }_{\Delta }{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} = {\int }_{M \times  M}{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} \land  {\eta }_{\Delta }
\]

\[
= \mathop{\sum }\limits_{{i, j}}{c}_{ij}{\int }_{M \times  M}{\pi }^{ * }{\tau }_{k} \land  {\rho }^{ * }{\omega }_{l} \land  {\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{j}
\]

\[
= \mathop{\sum }\limits_{{i, j}}{c}_{ij}{\left( -1\right) }^{\left( {\deg {\tau }_{k} + \deg {\omega }_{l}}\right) \left( {\deg {\omega }_{i}}\right) }{\int }_{M \times  M}{\pi }^{ * }\left( {{\omega }_{i} \land  {\tau }_{k}}\right) {\rho }^{ * }\left( {{\omega }_{l} \land  {\tau }_{j}}\right)
\]

\[
= {\left( -1\right) }^{\left( {\deg {\tau }_{k} + \deg {\omega }_{l}}\right) \deg {\omega }_{k}}{c}_{kl}.
\]

Therefore

\[
{c}_{kl} = \left\{  \begin{array}{ll} 0 & \text{ if }k \neq  l \\  {\left( -1\right) }^{\deg {\omega }_{k}} & \text{ if }k = l. \end{array}\right.
\]

Lemma 11.23. The normal bundle \( {N}_{\Delta } \) of the diagonal \( \Delta \) in \( M \times  M \) is isomorphic to the tangent bundle \( {T}_{\Delta } \) .

Proof. Since the diagonal map \( \iota  : M \rightarrow  M \times  M \) sends \( M \) diffeomorphically onto \( \Delta ,{\iota }^{ * }{T}_{\Delta } = {T}_{M} \) . It follows from the commutative diagram

\[
\left( {v, v}\right)  \mapsto  \left( {v, v}\right)
\]

\[
{\left. 0 \rightarrow  {T}_{\Delta } \rightarrow  {T}_{M \times  M}\right| }_{\Delta } \rightarrow  {N}_{\Delta } \rightarrow  0
\]

\[
\text{ 12 }
\]

\[
0 \rightarrow  {T}_{M} \rightarrow  {T}_{M} \oplus  {T}_{M} \rightarrow  {T}_{M} \rightarrow  0
\]

\[
v \mapsto  \left( {v, v}\right)
\]

that \( {N}_{\Delta } \simeq  {T}_{M} \simeq  {T}_{\Delta } \) .

Recall that the Poincaré dual of a closed oriented submanifold \( S \) is represented by the same form as the Thom class of a tubular neighborhood of \( S \) (see (6.23)). Thus

\[
{\int }_{\Delta }{\eta }_{\Delta } = {\int }_{\Delta }\Phi \left( {N}_{\Delta }\right)
\]

bundle \( {N}_{\Delta } \) regarded as a tubular neighborhood of \( \Delta \) in \( M \times  M \) section of the bundle is the Euler class (proved for rank 2 bundles in Prop. 6.41 on p. 74; the general

\[
= {\int }_{\Delta }e\left( {T}_{\Delta }\right)
\]

\[
= {\int }_{M}e\left( {T}_{M}\right) \text{ . }
\]

So the self-intersection number of the diagonal \( \Delta \) in \( M \times  M \) is the Euler number of \( M \) . (By Poincaré duality, \( {\int }_{\Delta }{\eta }_{\Delta } = {\int }_{M \times  M}{\eta }_{\Delta } \land  {\eta }_{\Delta } \) is the self-intersection number of \( \Delta \) in \( M \times  M \) .)

Now the right-hand side of Lemma 11.22 evaluated on the diagonal \( \Delta \) is

\[
{\int }_{\Delta }{\eta }_{\Delta } = \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}{\int }_{\Delta }{\pi }^{ * }{\omega }_{i} \land  {\rho }^{ * }{\tau }_{i}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}{\int }_{M}{\iota }^{ * }{\pi }^{ * }{\omega }_{i} \land  {\iota }^{ * }{\rho }^{ * }{\tau }_{i}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}{\int }_{M}{\omega }_{i} \land  {\tau }_{i}
\]

\[
= \mathop{\sum }\limits_{i}{\left( -1\right) }^{\deg {\omega }_{i}}
\]

\[
= \mathop{\sum }\limits_{q}{\left( -1\right) }^{q}\dim {H}^{q}\left( M\right)
\]

\[
= \chi \left( M\right) \text{ . }
\]

Therefore,

Proposition 11.24. The Euler number of a compact oriented manifold \( {\int }_{M}e\left( {T}_{M}\right) \) is equal to its Euler characteristic \( \chi \left( M\right)  = \sum {\left( -1\right) }^{q}\dim {H}^{q} \) .

It is now a simple matter to derive the Hopf index theorem. Let \( V \) be a vector field with isolated zeros on \( M \) . The index of \( V \) at a zero \( u \) is defined to be the local degree at \( u \) of \( V/\parallel V\parallel \) as a section of the unit tangent bundle of \( M \) relative to some Riemannian metric on \( M \) . By Theorem 11.16 the sum of the indices of \( V \) is the Euler number of \( M \) . The equality of the Euler number and the Euler characteristic then yields the following.

Theorem 11.25 (Hopf Index Theorem). The sum of the indices of a vector field on a compact oriented manifold \( M \) is the Euler characteristic of \( M \) .

Exercise 11.26 (Lefschetz fixed-point formula). Let \( f : M \rightarrow  M \) be a smooth map of a compact oriented manifold into itself. Denote by \( {H}^{q}\left( f\right) \) the induced map on the cohomology \( {H}^{q}\left( M\right) \) . The Lefschetz number of \( f \) is defined to be

\[
L\left( f\right)  = \mathop{\sum }\limits_{q}{\left( -1\right) }^{q}\operatorname{trace}{H}^{q}\left( f\right) .
\]

Let \( \Gamma \) be the graph of \( f \) in \( M \times  M \) .

(a) Show that

\[
{\int }_{\Delta }{\eta }_{\Gamma } = L\left( f\right)
\]

(b) Show that if \( f \) has no fixed points, then \( L\left( f\right) \) is zero.

(c) At a fixed point \( P \) of \( f \) the derivative \( {\left( Df\right) }_{P} \) is an endomorphism of the tangent space \( {T}_{P}M \) . We define the multiplicity of the fixed point \( P \) to be

\[
{\sigma }_{P} = \operatorname{sgn}\det \left( {{\left( Df\right) }_{P} - I}\right) .
\]

Show that if the graph \( \Gamma \) is transversal to the diagonal \( \Delta \) in \( M \times  M \) , then

\[
L\left( f\right)  = \mathop{\sum }\limits_{P}{\sigma }_{P}
\]

where \( P \) ranges over the fixed points of \( f \) . (For an explanation of the meaning of the multiplicity \( {\sigma }_{P} \) , see Guillemin and Pollack [1, p. 121].)
