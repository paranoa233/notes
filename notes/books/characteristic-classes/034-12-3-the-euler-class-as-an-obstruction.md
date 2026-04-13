# 12.3 The Euler Class as an Obstruction

We have now assembled the preliminary constructions which we will need in order to study the top obstruction class

\[
{\mathfrak{o}}_{n}\left( \xi \right)  \in  {\mathrm{H}}^{n}\left( {B;\left\{  {{\pi }_{n - 1}{\mathrm{\;V}}_{1}\left( F\right) }\right\}  }\right)
\]

for an oriented \( n \) -plane bundle \( \xi \) . Using the orientations of the fibers \( F \) , it is clear that each coefficient group

\[
{\pi }_{n - 1}{\mathrm{\;V}}_{1}\left( F\right)  \cong  {\pi }_{n - 1}\left( {F - 0}\right)  \cong  {\mathrm{H}}_{n - 1}\left( {F - 0;\mathbb{Z}}\right)  \cong  {\mathrm{H}}_{n}\left( {F, F - 0;\mathbb{Z}}\right)
\]

is canonically isomorphic to \( \mathbb{Z} \) . Hence the following statement makes sense.

Theorem 12.5. If \( \xi \) is an oriented \( n \) -plane bundle over a CW-complex, then \( {\mathfrak{o}}_{n}\left( \xi \right) \) is equal to the Euler class \( \mathrm{e}\left( \xi \right) \) .

Proof. Using the projection map \( {\pi }_{0} : {E}_{0} \rightarrow  B \) , let us form the induced bundle \( {\pi }_{0}^{ * }\xi \) over \( {E}_{0} \) . Clearly this induced bundle has a nowhere zero cross-section, hence

\[
{\pi }_{0}^{ * }{\mathfrak{o}}_{n}\left( \xi \right)  = {\mathfrak{o}}_{n}\left( {{\pi }_{0}^{ * }\xi }\right)  = 0.
\]

Using the Gysin exact sequence

\[
{\mathrm{H}}^{0}\left( B\right) \overset{ \smile  \mathrm{e}}{ \rightarrow  }{\mathrm{H}}^{n}\left( B\right) \overset{{\pi }_{0}^{ * }}{ \rightarrow  }{\mathrm{H}}^{n}\left( {E}_{0}\right)
\]

with integer coefficients, it follows that

\[
{\mathfrak{o}}_{n}\left( \xi \right)  = \lambda  \smile  \mathrm{e}\left( \xi \right)
\]

for some \( \lambda  \in  {\mathrm{H}}^{0}\left( B\right) \) . In particular this argument applies to the universal bundle \( {\widetilde{\gamma }}^{n} \) over \( {\widetilde{\mathrm{{Gr}}}}_{n} \) . Using the Gysin sequence

\[
{\mathrm{H}}^{0}\left( {\widetilde{\mathrm{{Gr}}}}_{n}\right) \overset{ \smile  \mathrm{e}}{ \rightarrow  }{\mathrm{H}}^{n}\left( {\widetilde{\mathrm{{Gr}}}}_{n}\right) \overset{{\pi }_{0}^{ * }}{ \rightarrow  }{\mathrm{H}}^{n}\left( {{E}_{0}\left( {\widetilde{\gamma }}^{n}\right) }\right) ,
\]

it follows that

\[
{\mathfrak{o}}_{n}\left( {\widetilde{\gamma }}^{n}\right)  = {\lambda }_{n}\mathrm{e}\left( {\widetilde{\gamma }}^{n}\right)
\]

for some integer \( {\lambda }_{n} \) . Therefore, by naturality,

\[
{\mathfrak{o}}_{n}\left( \xi \right)  = {\lambda }_{n}\mathrm{e}\left( \xi \right)
\]

for every oriented \( n \) -plane bundle \( \xi \) over a CW-complex.

Now reduce both sides of this equation modulo 2, obtaining

\[
{\mathrm{w}}_{n}\left( {\widetilde{\gamma }}^{n}\right)  = {\lambda }_{n}{\mathrm{\;w}}_{n}\left( {\widetilde{\gamma }}^{n}\right)
\]

by 12.1 and 9.5. Since \( {\mathrm{w}}_{n}\left( {\widetilde{\gamma }}^{n}\right)  \neq  0 \) by 12.4, this proves that the integer \( {\lambda }_{n} \) is odd.

If the dimension \( n \) is odd, then the Euler class itself has order 2 by Property 9.4, so we have proved that \( {\mathfrak{o}}_{n}\left( \xi \right)  = \mathrm{e}\left( \xi \right) \) .

If the dimension \( n \) is even, we must prove that \( {\lambda }_{n} =  + 1 \) . Let \( \tau \) be the tangent bundle of the \( n \) -sphere with \( n \) even. Then the Kronecker index \( \langle \mathrm{e}\left( \tau \right) ,\mu \rangle \) is equal to the Euler characteristic \( \chi \left( {S}^{n}\right)  =  + 2 \) by 11.12. The analogous formula

\[
\left\langle  {{\mathfrak{o}}_{n}\left( \xi \right) ,\mu }\right\rangle   =  + 2
\]

is true by [Ste51,§39.6] or can be verified directly by inspecting the vector field on \( {S}^{n} \) which is portrayed on Figure 10. Thus the coefficient \( {\lambda }_{n} \) must be equal to +1 .

Problem 12-A. Prove that a vector bundle \( \xi \) over a CW-complex is orientable if and only if \( {\mathrm{w}}_{1}\left( \xi \right)  = 0 \) .

Problem 12-B. Using the Wu formula 11.14 and the fact that \( {\pi }_{2}{\mathrm{\;V}}_{2}\left( {\mathbb{R}}^{3}\right)  \cong  {\pi }_{2}\mathrm{{SO}}\left( 3\right)  = 0 \) [Ste51, p. 116], prove Stiefel’s theorem that every compact orientable 3-manifold is parallelizable.

Problem 12-C. Use Corollary 12.3 to give another proof that \( {\mathrm{H}}^{ * }\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right) \) is as described in Lemma 4.3.

Problem 12-D. Show that \( {\widetilde{\mathrm{{Gr}}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) is a smooth, compact, orientable manifold of dimension \( {nk} \) . Show that the correspondence which maps the plane with oriented basis \( {b}_{1},\ldots ,{b}_{n} \) to \( {b}_{1} \land  \ldots  \land  {b}_{n}/\left| {{b}_{1} \land  \ldots  \land  {b}_{n}}\right| \) embeds \( {\widetilde{\operatorname{Gr}}}_{n}\left( {\mathbb{R}}^{n + k}\right) \) smoothly in the exterior power \( {\Lambda }^{n}{\mathbb{R}}^{n + k} \) .
