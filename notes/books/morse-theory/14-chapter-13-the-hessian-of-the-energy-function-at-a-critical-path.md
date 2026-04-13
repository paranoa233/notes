# Chapter 13 The Hessian of the Energy Function at a Critical Path

Based on lecture notes by

M. Spivak and R. Wells

Continuing with the analogy developed in the preceding section, we now wish to define a bilinear functional

\[
{E}_{* * } : T{\Omega }_{\gamma } \times  T{\Omega }_{\gamma } \rightarrow  \mathbf{R}
\]

when \( \gamma \) is a critical point of the function \( E \) , i.e., a geodesic. This bilinear functional will be called the Hessian of \( E \) at \( \gamma \) .

If \( f \) is a real valued function on a manifold \( M \) with critical point \( p \) , then the Hessian

\[
{f}_{* * } : T{M}_{p} \times  T{M}_{p} \rightarrow  \mathbf{R}
\]

can be defined as follows. Given \( {X}_{1},{X}_{2} \in  T{M}_{p} \) choose a smooth map \( \left( {{u}_{1},{u}_{2}}\right)  \mapsto \; \alpha \left( {{u}_{1},{u}_{2}}\right) \) defined on a neighborhood of \( \left( {0,0}\right) \) in \( {\mathbf{R}}^{2} \) , with values in \( M \) , so that

\[
\alpha \left( {0,0}\right)  = p,\;\frac{\partial \alpha }{\partial {u}_{1}}\left( {0,0}\right)  = {X}_{1},\;\frac{\partial \alpha }{\partial {u}_{2}}\left( {0,0}\right)  = {X}_{2}
\]

Then

\[
{f}_{* * }\left( {{X}_{1},{X}_{2}}\right)  = {\left. \frac{{\partial }^{2}f\left( {\alpha \left( {{u}_{1},{u}_{2}}\right) }\right) }{\partial {u}_{1}\partial {u}_{2}}\right| }_{\left( 0,0\right) }.
\]

This suggests defining \( {E}_{* * } \) as follows. Given vector fields \( {W}_{1},{W}_{2} \in  T{\Omega }_{\gamma } \) choose a 2-parameter variation

\[
\alpha  : U \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

where \( U \) is a neighborhood of \( \left( {0,0}\right) \) in \( {\mathbf{R}}^{2} \) , so that

\[
\alpha \left( {0,0, t}\right)  = \gamma \left( t\right) ,\;\frac{\partial \alpha }{\partial {u}_{1}}\left( {0,0, t}\right)  = {W}_{1}\left( t\right) ,\;\frac{\partial \alpha }{\partial {u}_{2}}\left( {0,0, t}\right)  = {W}_{2}\left( t\right) .
\]

(Compare chapter 11.) Then the Hessian \( {E}_{* * }\left( {{W}_{1},{W}_{2}}\right) \) will be defined to be the second partial derivative

\[
{\left. \frac{{\partial }^{2}E\left( {\overline{\alpha }\left( {{u}_{1},{u}_{2}}\right) }\right) }{\partial {u}_{1}\partial {u}_{2}}\right| }_{\left( 0,0\right) };
\]

where \( \overline{\alpha }\left( {{u}_{1},{u}_{2}}\right)  \in  \Omega \) denotes the path \( \overline{\alpha }\left( {{u}_{1},{u}_{2}}\right) \left( t\right)  = \alpha \left( {{u}_{1},{u}_{2}, t}\right) \) . This second derivative will be written briefly as \( \frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}}\left( {0,0}\right) \) .

The following theorem is needed to prove that \( {E}_{* * } \) is well defined.

Theorem 13.1 (Second variation formula). Let \( \overline{\alpha } : U \rightarrow  \Omega \) be a 2-parameter variation of the geodesic \( \gamma \) with variation vector fields

\[
{W}_{i} = \frac{\partial \overline{\alpha }}{\partial {u}_{i}}\left( {0,0}\right)  \in  T{\Omega }_{\gamma },\;i = 1,2.
\]

Then the second derivative \( \frac{1}{2}\frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}}\left( {0,0}\right) \) of the energy function is equal to

\[
- \mathop{\sum }\limits_{t}\left\langle  {{W}_{2}\left( t\right) ,{\Delta }_{t}\frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t}}\right\rangle   - {\int }_{0}^{1}\left\langle  {{W}_{2},\frac{{\mathrm{D}}^{2}{W}_{1}}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( {V,{W}_{1}}\right) V}\right\rangle  \mathrm{d}t;
\]

where \( V = \frac{\mathrm{d}\gamma }{\mathrm{d}t} \) denotes the velocity vector field and where

\[
{\Delta }_{t}\frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t} = \frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t}\left( {t}^{ + }\right)  - \frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t}\left( {t}^{ - }\right)
\]

denotes the jump in \( \frac{\mathrm{D}{W}_{1}}{\mathrm{\;d}t} \) at one of its finitely many points of discontinuity in the open unit interval.

Proof. According to Theorem 12.2 we have

\[
\frac{1}{2}\frac{\partial E}{\partial {u}_{2}} - \mathop{\sum }\limits_{t}\left\langle  {\frac{\partial \alpha }{\partial {u}_{2}},{\Delta }_{t}\frac{\partial \alpha }{\partial t}}\right\rangle   - {\int }_{0}^{1}\left\langle  {\frac{\partial \alpha }{\partial {u}_{2}},\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t.
\]

Therefore

\[
\frac{1}{2}\frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}} =  - \mathop{\sum }\limits_{t}\left\langle  {\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}\frac{\partial \alpha }{\partial {u}_{2}},{\Delta }_{t}\frac{\partial \alpha }{\partial t}}\right\rangle   - \mathop{\sum }\limits_{t}\left\langle  {\frac{\partial \alpha }{\partial {u}_{2}},\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}{\Delta }_{t}\frac{\partial \alpha }{\partial t}}\right\rangle
\]

\[
- {\int }_{0}^{1}\left\langle  {\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}\frac{\partial \alpha }{\partial {u}_{2}},\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t - {\int }_{0}^{1}\left\langle  {\frac{\partial \alpha }{\partial {u}_{2}},\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t.
\]

Let us evaluate this expression for \( \left( {{u}_{1},{u}_{2}}\right)  = \left( {0,0}\right) \) . Since \( \gamma  = \overline{\alpha }\left( {0,0}\right) \) is an unbroken geodesic, we have

\[
{\Delta }_{t}\frac{\partial \alpha }{\partial t} = 0,\;\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t} = 0,
\]

so that the first and third terms are zero.

Rearranging the second term, we obtain

\[
\frac{1}{2}\frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}}\left( {0,0}\right)  =  - \mathop{\sum }\limits_{t}\left\langle  {{W}_{2},{\Delta }_{t}\frac{\mathrm{D}}{\mathrm{d}t}{W}_{1}}\right\rangle   - {\int }_{0}^{1}\left\langle  {{W}_{2},\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}\frac{\mathrm{D}}{\mathrm{d}t}V}\right\rangle  \mathrm{d}t. \tag{13.1}
\]

In order to interchange the two operators \( \frac{\mathrm{D}}{\mathrm{d}{u}_{1}} \) and \( \frac{\mathrm{D}}{\mathrm{d}t} \) , we need to bring in the curvature formula,

\[
\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}\frac{\mathrm{D}}{\mathrm{d}t}V - \frac{\mathrm{D}}{\mathrm{d}t}\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}V = \mathcal{R}\left( {\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial {u}_{1}}}\right) V = \mathcal{R}\left( {V,{W}_{1}}\right) V.
\]

Together with the identity \( \frac{\mathrm{D}}{\mathrm{d}{u}_{1}}V = \frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial {u}_{1}} = \frac{\mathrm{D}}{\mathrm{d}t}{W}_{1} \) this yields

\[
\frac{\mathrm{D}}{\mathrm{d}{u}_{1}}\frac{\partial }{\partial t}V = \frac{{\mathrm{D}}^{2}{W}_{1}}{\mathrm{\;d}{t}^{2}} + \mathcal{R}\left( {V,{W}_{1}}\right) V. \tag{13.2}
\]

Substituting this expression into (13.1) this completes the proof of Theorem 13.1.

Corollary 13.2. The expression \( {E}_{* * }\left( {{W}_{1},{W}_{2}}\right)  = \frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}}\left( {0,0}\right) \) is a well defined symmetric and bilinear function of \( W \) and \( {W}_{2} \) .

Proof. The second variation formula shows that \( \frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}}\left( {0,0}\right) \) depends only on the variation vector fields \( {W}_{1} \) and \( {W}_{2} \) , so that \( {E}_{* * }\left( {{W}_{1},{W}_{2}}\right) \) is well defined. This formula also shows that \( {E}_{* * } \) is bilinear. The symmetry property

\[
{E}_{* * }\left( {{W}_{1},{W}_{2}}\right)  = {E}_{* * }\left( {{W}_{2},{W}_{1}}\right)
\]

is not at all obvious from the second variation formula; but does follow immediately from the symmetry property \( \frac{{\partial }^{2}E}{\partial {u}_{1}\partial {u}_{2}} = \frac{{\partial }^{2}E}{\partial {u}_{2}\partial {u}_{1}} \) .

Remark. The diagonal terms \( {E}_{* * }\left( {W, W}\right) \) of the bilinear pairing \( {E}_{* * } \) can be described in terms of a 1-parameter variation of \( \gamma \) . In fact

\[
{E}_{* * }\left( {W, W}\right)  = \frac{{\mathrm{d}}^{2}E \circ  \overline{\alpha }}{\mathrm{d}{u}^{2}}\left( 0\right) ,
\]

where \( \overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega \) denotes any variation of \( \gamma \) with variation vector field \( \frac{\mathrm{d}\overline{\alpha }}{\mathrm{d}u}\left( 0\right) \) equal to \( W \) . To prove this identity it is only necessary to introduce the two parameter variation

\[
\overline{\beta }\left( {{u}_{1},{u}_{2}}\right)  = \overline{\alpha }\left( {{u}_{1} + {u}_{2}}\right)
\]

and to note that

\[
\frac{\partial \overline{\beta }}{\partial {u}_{i}} = \frac{\mathrm{d}\overline{\alpha }}{\mathrm{d}u},\;\frac{{\partial }^{2}E \circ  \overline{\beta }}{\partial {u}_{1}\partial {u}_{2}} = \frac{{\mathrm{d}}^{2}E \circ  \overline{\alpha }}{\mathrm{d}{u}^{2}}.
\]

As an application of this remark, we have the following.

Lemma 13.3. If \( \gamma \) is a minimal geodesic from \( p \) to \( q \) then the bilinear pairing \( {E}_{* * } \) is positive semi-definite. Hence the index \( \lambda \) of \( {E}_{* * } \) is zero.

Proof. The inequality \( E\left( {\overline{\alpha }\left( u\right) }\right)  \geq  E\left( \gamma \right)  = E\left( {\overline{\alpha }\left( 0\right) }\right) \) implies that \( \frac{{\mathrm{d}}^{2}E\left( {\overline{\alpha }\left( u\right) }\right) }{\mathrm{d}{u}^{2}} \) , evaluated at \( u = 0 \) , is \( \geq  0 \) . Hence \( {E}_{* * }\left( {W, W}\right)  \geq  0 \) for all \( W \) .
