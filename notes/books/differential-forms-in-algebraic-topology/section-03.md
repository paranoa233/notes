## §3 Orientation and Integration

## Orientation and the Integral of a Differential Form

Let \( {x}_{1},\ldots ,{x}_{n} \) be the standard coordinates on \( {\mathbb{R}}^{n} \) . Recall that the Riemann integral of a differentiable function \( f \) with compact support is

\[
{\int }_{{\mathbb{R}}^{n}}f\left| {d{x}_{1}\ldots d{x}_{n}}\right|  = \mathop{\lim }\limits_{{\Delta {x}_{i} \rightarrow  0}}\sum {f\Delta }{x}_{1}\ldots \Delta {x}_{n}.
\]

We define the integral of an \( n \) -form with compact support \( \omega  = {fd}{x}_{1}\ldots d{x}_{n} \) to be the Riemann integral \( {\int }_{{\mathbb{R}}^{n}}f\left| {d{x}_{1}\ldots d{x}_{n}}\right| \) . Note that contrary to the usual calculus notation we put an absolute value sign in the Riemann integral; this is to emphasize the distinction between the Riemann integral of a function and the integral of a differential form. While the order of \( {x}_{1},\ldots ,{x}_{n} \) matters in a differential form, it does not in a Riemann integral; if \( \pi \) is a permutation of \( \{ 1,\ldots , n\} \) , then

\[
\int {fd}{x}_{\pi \left( 1\right) }\ldots d{x}_{\pi \left( n\right) } = \left( {\operatorname{sgn}\pi }\right) \int f\left| {d{x}_{1}\ldots d{x}_{n}}\right| ,
\]

but

\[
\int f\left| {d{x}_{\pi \left( 1\right) }\ldots d{x}_{\pi \left( n\right) }}\right|  = \int f\left| {d{x}_{1}\ldots d{x}_{n}}\right| .
\]

In a situation where there is no possibility of confusion, we may revert to the usual calculus notation.

So defined, the integral of an \( n \) -form on \( {\mathbb{R}}^{n} \) depends on the coordinates \( {x}_{1},\ldots ,{x}_{n} \) . From our point of view a change of coordinates is given by a diffeomorphism \( T : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) with coordinates \( {y}_{1},\ldots ,{y}_{n} \) and \( {x}_{1},\ldots ,{x}_{n} \) respectively:

\[
{x}_{i} = {x}_{i} \circ  T\left( {{y}_{1},\ldots ,{y}_{n}}\right)  = {T}_{i}\left( {{y}_{1},\ldots ,{y}_{n}}\right) .
\]

We now study how the integral \( \int \omega \) transforms under such diffeomorphisms.

Exercise 3.1. Show that \( d{T}_{1}\ldots d{T}_{n} = J\left( T\right) d{y}_{1}\ldots d{y}_{n} \) , where \( J\left( T\right)  = \; \det \left( {\partial {x}_{i}/\partial {y}_{j}}\right) \) is the Jacobian determinant of \( T \) .

Hence,

\[
{\int }_{{\mathbb{R}}^{n}}{T}^{ * }\omega  = {\int }_{{\mathbb{R}}^{n}}\left( {f \circ  T}\right) d{T}_{1}\ldots d{T}_{n} = {\int }_{{\mathbb{R}}^{n}}\left( {f \circ  T}\right) J\left( T\right) \left| {d{y}_{1}\ldots d{y}_{n}}\right|
\]

relative to the coordinate system \( {y}_{1},\ldots ,{y}_{n} \) . On the other hand, by the change of variables formula,

\[
{\int }_{{\mathbb{R}}^{n}}\omega  = {\int }_{{\mathbb{R}}^{n}}f\left( {{x}_{1},\ldots ,{x}_{n}}\right) \left| {d{x}_{1}\ldots d{x}_{n}}\right|  = {\int }_{{\mathbb{R}}^{n}}\left( {f \circ  T}\right) \left| {J\left( T\right) }\right| \left| {d{y}_{1}\ldots d{y}_{n}}\right|
\]

Thus

\[
{\int }_{{\mathbb{R}}^{n}}{T}^{ * }\omega  =  \pm  {\int }_{{\mathbb{R}}^{n}}\omega
\]

depending on whether the Jacobian determinant is positive or negative. In general if \( T \) is a diffeomorphism of open subsets of \( {\mathbb{R}}^{n} \) and if the Jacobian determinant \( J\left( T\right) \) is everywhere positive, then \( T \) is said to be orientation-preserving. The integral on \( {\mathbb{R}}^{n} \) is not invariant under the whole group of diffeomorphisms of \( {\mathbb{R}}^{n} \) , but only under the subgroup of orientation-preserving diffeomorphisms.

Let \( M \) be a differentiable manifold with atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) . We say that the atlas is oriented if all the transition functions \( {g}_{\alpha \beta } = {\phi }_{\alpha } \circ  {\phi }_{\beta }^{-1} \) are orientation-preserving, and that the manifold is orientable if it has an oriented atlas.

Proposition 3.2. A manifold \( M \) of dimension \( n \) is orientable if and only if it has a global nowhere vanishing n-form.

Proof. Observe that \( T : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) is orientation-preserving if and only if \( {T}^{ * }d{x}_{1}\ldots d{x}_{n} \) is a positive multiple of \( d{x}_{1}\ldots d{x}_{n} \) at every point.

\( \left(  \Leftarrow  \right) \; \) Suppose \( M \) has a global nowhere-vanishing \( n \) -form \( \omega \) . Let \( {\phi }_{\alpha } : {U}_{\alpha } \simeq \; {\mathbb{R}}^{n} \) be a coordinate map. Then \( {\phi }_{\alpha }^{ * }d{x}_{1}\ldots d{x}_{n} = {f}_{\alpha }\omega \) where \( {f}_{\alpha } \) is a nowhere-vanishing real-valued function on \( {U}_{\alpha } \) . Thus \( {f}_{\alpha } \) is either everywhere positive or everywhere negative. In the latter case replace \( {\phi }_{\alpha } \) by \( {\psi }_{\alpha } = T \circ  {\phi }_{\alpha } \) , where \( T : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) is the orientation-reversing diffeomorphism \( T\left( {{x}_{1},{x}_{2},\ldots ,{x}_{n}}\right) \; = \left( {-{x}_{1},{x}_{2},\ldots ,{x}_{n}}\right) \) . Since \( {\psi }_{\alpha }^{ * }d{x}_{1}\ldots d{x}_{n} = {\phi }_{\alpha }^{ * }{T}^{ * }d{x}_{1}\ldots d{x}_{n} = \; - {\phi }_{\alpha }^{ * }d{x}_{1}\ldots d{x}_{n} = \left( {-{f}_{\alpha }}\right) \omega \) , we may assume \( {f}_{\alpha } \) to be positive for all \( \alpha \) . Hence, any transition function \( {\phi }_{\beta }{\phi }_{\alpha }^{-1} : {\phi }_{\alpha }\left( {{U}_{\alpha } \cap  {U}_{\beta }}\right)  \rightarrow  {\phi }_{\beta }\left( {{U}_{\alpha } \cap  {U}_{\beta }}\right) \) will pull \( d{x}_{1}\ldots d{x}_{n} \) to a positive multiple of itself. So \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) is an oriented atlas.

\( \left(  \Rightarrow  \right) \) Conversely, suppose \( M \) has an oriented atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) . Then

\[
{\left( {\phi }_{\beta }{\phi }_{\alpha }^{-1}\right) }^{ * }\left( {d{x}_{1}\ldots d{x}_{n}}\right)  = {\lambda d}{x}_{1}\ldots d{x}_{n}
\]

for some positive function \( \lambda \) . Thus

\[
{\phi }_{\beta }^{ * }d{x}_{1}\ldots d{x}_{n} = \left( {{\phi }_{\alpha }^{ * }\lambda }\right) \left( {{\phi }_{\alpha }^{ * }d{x}_{1}\ldots d{x}_{n}}\right) .
\]

Denoting \( {\phi }_{\alpha }^{ * }d{x}_{1}\ldots d{x}_{n} \) by \( {\omega }_{\alpha } \) , we see that \( {\omega }_{\beta } = f{\omega }_{\alpha } \) where \( f = {\phi }_{\alpha }^{ * }\lambda  = \lambda \) 。 \( {\phi }_{\alpha } \) is a positive function on \( {U}_{\alpha } \cap  {U}_{\beta } \) .

Let \( \omega  = \sum {\rho }_{\alpha }{\omega }_{\alpha } \) where \( {\rho }_{\alpha } \) is a partition of unity subordinate to the open cover \( \left\{  {U}_{\alpha }\right\} \) . At each point \( p \) in \( M \) , all the forms \( {\omega }_{\alpha } \) , if defined, are positive multiples of one another. Since \( {\rho }_{\alpha } \geq  0 \) and not all \( {\rho }_{\alpha } \) can vanish at a point, \( \omega \) is nowhere vanishing.

Any two global nowhere vanishing \( n \) -forms \( \omega \) and \( {\omega }^{\prime } \) on an orientable manifold \( M \) of dimension \( n \) differ by a nowhere vanishing function: \( \omega  = f{\omega }^{\prime } \) . If \( M \) is connected, then \( f \) is either everywhere positive or everywhere negative. We say that \( \omega \) and \( {\omega }^{\prime } \) are equivalent if \( f \) is positive. Thus on a connected orientable manifold \( M \) the nowhere vanishing \( n \) -forms fall into two equivalence classes. Either class is called an orientation on \( M \) , written \( \left\lbrack  M\right\rbrack \) . For example, the standard orientation on \( {\mathbb{R}}^{n} \) is given by \( d{x}_{1}\ldots d{x}_{n} \) .

Now choose an orientation \( \left\lbrack  M\right\rbrack \) on \( M \) . Given a top form \( \tau \) in \( {\Omega }_{c}^{n}\left( M\right) \) , we define its integral by

\[
{\int }_{\left\lbrack  M\right\rbrack  }\tau  = \mathop{\sum }\limits_{\alpha }{\int }_{{U}_{\alpha }}{\rho }_{\alpha }\tau
\]

where \( {\int }_{{U}_{\alpha }}{\rho }_{\alpha }\tau \) means \( {\int }_{{\mathbb{R}}^{n}}{\left( {\phi }_{\alpha }^{-1}\right) }^{ * }\left( {{\rho }_{\alpha }\tau }\right) \) for some orientation-preserving trivialization \( {\phi }_{\alpha } : {U}_{\alpha } \simeq  {\mathbb{R}}^{n} \) ; as in Proposition 2.7, \( {\rho }_{\alpha }\tau \) has compact support. By the orientability assumption, the integral over a coordinate patch \( {\int }_{{U}_{a}}\omega \) is well defined. With a fixed orientation on \( M \) understood, we will often write \( {\int }_{M}\tau \) instead of \( {\int }_{\left\lbrack  M\right\rbrack  }\tau \) . Reversing the orientation results in the negative of the integral.

Proposition 3.3. The definition of the integral \( {\int }_{M}\tau \) is independent of the oriented atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) and the partition of unity \( \left\{  {\rho }_{\alpha }\right\} \) .

Proof. Let \( \left\{  {V}_{\beta }\right\} \) be another oriented atlas of \( M \) , and \( \left\{  {\chi }_{\beta }\right\} \) a partition of unity subordinate to \( \left\{  {V}_{\beta }\right\} \) . Since \( \mathop{\sum }\limits_{\beta }{\chi }_{\beta } = 1 \) ,

\[
\mathop{\sum }\limits_{\alpha }{\int }_{{U}_{\alpha }}{\rho }_{\alpha }\tau  = \mathop{\sum }\limits_{{\alpha ,\beta }}{\int }_{{U}_{\alpha }}{\rho }_{\alpha }{\chi }_{\beta }\tau .
\]

Now \( {\rho }_{\alpha }{\chi }_{\beta }\tau \) has support in \( {U}_{\alpha } \cap  {V}_{\beta } \) , so

Therefore

\[
{\int }_{{U}_{\alpha }}{\rho }_{\alpha }{\chi }_{\beta }\tau  = {\int }_{{V}_{\beta }}{\rho }_{\alpha }{\chi }_{\beta }\tau .
\]

\[
\mathop{\sum }\limits_{\alpha }{\int }_{{U}_{\alpha }}{\rho }_{\alpha }\tau  = \mathop{\sum }\limits_{{\alpha ,\beta }}{\int }_{{V}_{\beta }}{\rho }_{\alpha }{\chi }_{\beta }\tau  = \mathop{\sum }\limits_{\beta }{\int }_{{V}_{\beta }}{\chi }_{\beta }\tau .
\]

A manifold \( M \) of dimension \( n \) with boundary is given by an atlas \( \left\{  \left( {{U}_{\alpha },{\phi }_{\alpha }}\right) \right\} \) where \( {U}_{\alpha } \) is homeomorphic to either \( {\mathbb{R}}^{n} \) or the upper half space \( {\mathbb{H}}^{n} = \left\{  {\left( {{x}_{1},\ldots ,{x}_{n}}\right)  \mid  {x}_{n} \geq  0}\right\} \) . The boundary \( \partial M \) of \( M \) is an \( \left( {n - 1}\right) \) - dimensional manifold. An oriented atlas for \( M \) induces in a natural way an oriented atlas for \( \partial M \) . This is a consequence of the following lemma.

Lemma 3.4. Let \( T : {\mathbb{H}}^{n} \rightarrow  {\mathbb{H}}^{n} \) be a diffeomorphism of the upper half space with everywhere positive Jacobian determinant. \( T \) induces a map \( \bar{T} \) of the boundary of \( {\mathbb{H}}^{n} \) to itself. The induced map \( \bar{T} \) , as a diffeomorphism of \( {\mathbb{R}}^{n - 1} \) , also has positive Jacobian determinant everywhere.

Proof. By the inverse function theorem an interior point of \( {\mathbb{H}}^{n} \) must be the image of an interior point. Hence \( T \) maps the boundary to the boundary. We will check that \( \bar{T} \) has positive Jacobian determinant for \( n = 2 \) ; the general case is similar.

Let \( T \) be given by

\[
{x}_{1} = {T}_{1}\left( {{y}_{1},{y}_{2}}\right)
\]

\[
{x}_{2} = {T}_{2}\left( {{y}_{1},{y}_{2}}\right) .
\]

Then \( \bar{T} \) is given by

\[
{x}_{1} = {T}_{1}\left( {{y}_{1},0}\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_41_254_294_1122_433_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_41_254_294_1122_433_0.jpg)

Figure 3.1

By assumption

\[
\left| \begin{array}{ll} \frac{\partial {T}_{1}}{\partial {y}_{1}}\left( {{y}_{1},0}\right) & \frac{\partial {T}_{1}}{\partial {y}_{2}}\left( {{y}_{1},0}\right) \\  \frac{\partial {T}_{2}}{\partial {y}_{1}}\left( {{y}_{1},0}\right) & \frac{\partial {T}_{2}}{\partial {y}_{2}}\left( {{y}_{1},0}\right)  \end{array}\right|  > 0.
\]

Since \( 0 = {T}_{2}\left( {{y}_{1},0}\right) \) for all \( {y}_{1},\partial {T}_{2}/\partial {y}_{1}\left( {{y}_{1},0}\right)  = 0 \) ; since \( T \) maps the upper half plane to itself,

\[
\frac{\partial {T}_{2}}{\partial {y}_{2}}\left( {{y}_{1},0}\right)  > 0
\]

Therefore

\[
\frac{\partial {T}_{1}}{\partial {y}_{1}}\left( {{y}_{1},0}\right)  > 0
\]

Let the upper half space \( {\mathbb{H}}^{n} = \left\{  {{x}_{n} \geq  0}\right\} \) in \( {\mathbb{R}}^{n} \) be given the standard orientation \( d{x}_{1}\ldots d{x}_{n} \) . Then the induced orientation on its boundary \( \partial {\mathbb{H}}^{n} = \; \left\{  {{x}_{n} = 0}\right\} \) is by definition the equivalence class of \( {\left( -1\right) }^{n}d{x}_{1}\ldots d{x}_{n - 1} \) for \( n \geq  2 \) and -1 for \( n = 1 \) ; the sign \( {\left( -1\right) }^{n} \) is needed to make Stokes’ theorem sign-free. In general for \( M \) an oriented manifold with boundary, we define the induced orientation \( \left\lbrack  {\partial M}\right\rbrack \) on \( \partial M \) by the following requirement: if \( \phi \) is an orientation-preserving diffeomorphism of some open set \( U \) in \( M \) into the upper half space \( {\mathbb{H}}^{n} \) , then

\[
{\phi }^{ * }\left\lbrack  {\partial {\mathbb{H}}^{n}}\right\rbrack   = \left\lbrack  {\partial M}\right\rbrack  {|}_{\partial U},
\]

where \( \partial U = \left( {\partial M}\right)  \cap  U \) (see Figure 3.1).

## Stokes' Theorem

A basic result in the theory of integration is

Theorem 3.5 (Stokes’ Theorem). If \( \omega \) is an \( \left( {n - 1}\right) \) -form with compact support on an oriented manifold \( M \) of dimension \( n \) and if \( \partial M \) is given the induced orientation, then

\[
{\int }_{M}{d\omega } = {\int }_{\partial M}\omega
\]

We first examine two special cases.

Special CASE 1 \( \left( {\mathbb{R}}^{n}\right) \) . By the linearity of the integrand we may take \( \omega \) to be \( {fd}{x}_{1}\ldots d{x}_{n - 1} \) . Then \( {d\omega } =  \pm  \partial f/\partial {x}_{n}d{x}_{1}\ldots d{x}_{n} \) . By Fubini’s theorem,

\[
{\int }_{{\mathbb{R}}^{n}}{d\omega } =  \pm  \int \left( {{\int }_{-\infty }^{\infty }\frac{\partial f}{\partial {x}_{n}}d{x}_{n}}\right) d{x}_{1}\ldots d{x}_{n - 1}.
\]

But \( {\int }_{-\infty }^{\infty }\partial f/\partial {x}_{n}d{x}_{n} = f\left( {{x}_{1},\ldots ,{x}_{n - 1},\infty }\right)  - f\left( {{x}_{1},\ldots ,{x}_{n - 1}, - \infty }\right)  = 0 \) because \( f \) has compact support. Since \( {\mathbb{R}}^{n} \) has no boundary, this proves Stokes’ theorem for \( {\mathbb{R}}^{n} \) .

SPECIAL CASE 2 (The upper half plane). In this case (see Figure 3.2)

\[
\omega  = f\left( {x, y}\right) {dx} + g\left( {x, y}\right) {dy}
\]

and

\[
{d\omega } = \left( {-\frac{\partial f}{\partial y} + \frac{\partial g}{\partial x}}\right) {dxdy}.
\]

Note that

\[
{\int }_{{\mathrm{H}}^{2}}\frac{\partial g}{\partial x}{dxdy} = {\int }_{0}^{\infty }\left( {{\int }_{-\infty }^{\infty }\frac{\partial g}{\partial x}{dx}}\right) {dy} = \int g\left( {\infty , y}\right)  - g\left( {-\infty , y}\right) {dy} = 0,
\]

since \( g \) has compact support. Therefore,

\[
{\int }_{{\mathbb{H}}^{2}}{d\omega } =  - {\int }_{{\mathbb{H}}^{2}}\frac{\partial f}{\partial y}{dxdy} =  - {\int }_{-\infty }^{\infty }\left( {{\int }_{0}^{\infty }\frac{\partial f}{\partial y}{dy}}\right) {dx}
\]

\[
=  - {\int }_{-\infty }^{\infty }\left( {f\left( {x,\infty }\right)  - f\left( {x,0}\right) }\right) {dx}
\]

\[
= {\int }_{-\infty }^{\infty }f\left( {x,0}\right) {dx} = {\int }_{\partial {H}^{2}}\omega
\]

where the last equality holds because the restriction of \( g\left( {x, y}\right) {dy} \) to \( \partial {\mathbb{H}}^{2} \) is 0 . So Stokes' theorem holds for the upper half plane.

![bo_d7b6f8alb0pc73dd9avg_42_467_1827_727_263_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_42_467_1827_727_263_0.jpg)

Figure 3.2

The case of the upper half space in \( {\mathbb{R}}^{n} \) is entirely analogous.

Exercise 3.6. Prove Stokes' theorem for the upper half space.

We now consider the general case of a manifold of dimension \( n \) . Let \( \left\{  {U}_{\alpha }\right\} \) be an oriented atlas for \( M \) and \( \left\{  {\rho }_{\alpha }\right\} \) a partition of unity subordinate to \( \left\{  {U}_{\alpha }\right\} \) . Write \( \omega  = \sum {\rho }_{\alpha }\omega \) . Since Stokes’ theorem \( {\int }_{M}{d\omega } = {\int }_{\partial M}\omega \) is linear in \( \omega \) , we need to prove it only for \( {\rho }_{\alpha }\omega \) , which has the virtue that its support is contained entirely in \( {U}_{\alpha } \) . Furthermore, \( {\rho }_{\alpha }\omega \) has compact support because

\[
\operatorname{Supp}{\rho }_{\alpha }\omega  \subset  \operatorname{Supp}{\rho }_{\alpha } \cap  \operatorname{Supp}\omega
\]

is a closed subset of a compact set. Since \( {U}_{\alpha } \) is diffeomorphic to either \( {\mathbb{R}}^{n} \) or the upper half space \( {\mathbb{H}}^{n} \) , by the computations above Stokes’ theorem holds for \( {U}_{\alpha } \) . Consequently

\[
{\int }_{M}d{\rho }_{\alpha }\omega  = {\int }_{{U}_{\alpha }}d{\rho }_{\alpha }\omega  = {\int }_{\partial {U}_{\alpha }}{\rho }_{\alpha }\omega  = {\int }_{\partial M}{\rho }_{\alpha }\omega .
\]

This concludes the proof of Stokes' theorem in general.
