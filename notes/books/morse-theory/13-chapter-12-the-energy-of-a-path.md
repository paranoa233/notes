# Chapter 12 The Energy of a Path

Based on lecture notes by

M. Spivak and R. Wells

Suppose now that \( M \) is a Riemannian manifold. The length of a vector \( v \in  T{M}_{p} \) will be denoted by \( \parallel v\parallel  = \langle v, v{\rangle }^{\frac{1}{2}} \) . For \( \omega  \in  \Omega \) define the energy of \( \omega \) from \( a \) to \( b \) (where \( 0 \leq  a < b \leq  1 \) ) as

\[
{E}_{a}^{b}\left( \omega \right)  = {\int }_{a}^{b}{\begin{Vmatrix}\frac{\mathrm{d}\omega }{\mathrm{d}t}\end{Vmatrix}}^{2}\mathrm{\;d}t.
\]

We will write \( E \) for \( {E}_{0}^{1} \) .

This can be compared with the arc-length from \( a \) to \( b \) given by

\[
{L}_{a}^{b}\left( \omega \right)  = {\int }_{a}^{b}\parallel \frac{\mathrm{d}\omega }{\mathrm{d}t}\parallel \mathrm{d}t
\]

as follows. Applying Schwarz's inequality

\[
{\left( {\int }_{a}^{b}fg\mathrm{\;d}t\right) }^{2} \leq  \left( {{\int }_{a}^{b}{f}^{2}\mathrm{\;d}t}\right) \left( {{\int }_{a}^{b}{g}^{2}\mathrm{\;d}t}\right)
\]

with \( f\left( t\right)  = 1 \) and \( g\left( t\right)  = \begin{Vmatrix}\frac{\mathrm{d}\omega }{\mathrm{d}t}\end{Vmatrix} \) we see that

\[
{\left( {L}_{a}^{b}\right) }^{2} \leq  \left( {b - a}\right) {E}_{a}^{b},
\]

where equality holds if and only if \( g \) is constant; that is if and only if the parameter \( t \) is proportional to arc-length.

Now suppose that there exists a minimal geodesic \( \gamma \) from \( p = \omega \left( 0\right) \) to \( q = \omega \left( 1\right) \) . Then

\[
E\left( \gamma \right)  = L{\left( \gamma \right) }^{2} \leq  L{\left( \omega \right) }^{2} \leq  E\left( \omega \right) .
\]

Here the equality \( L{\left( \gamma \right) }^{2} = L{\left( \omega \right) }^{2} \) can hold only if \( \omega \) is also a minimal geodesic, possibly reparametrized. (Compare Corollary 10.9.) On the other hand the equality \( L{\left( \omega \right) }^{2} = E\left( \omega \right) \) can hold only if the parameter is proportional to arc-length along \( \omega \) . This proves that \( E\left( \gamma \right)  < E\left( \omega \right) \) unless \( \omega \) is also a minimal geodesic. In other words:

Lemma 12.1. Let \( M \) be a complete Riemannian manifold and let \( p, q \in  M \) have distance d. Then the energy function

\[
E : \Omega \left( {M;p, q}\right)  \rightarrow  \mathbf{R}
\]

takes on its minimum \( {d}^{2} \) precisely on the set of minimal geodesics from \( p \) to \( q \) .

We will now see which paths \( \omega  \in  \Omega \) are critical paths for the energy function \( E \) .

Let \( \overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega \) be a variation of \( \omega \) , and let \( {W}_{t} = \frac{\partial \alpha }{\partial u}\left( {0, t}\right) \) be the associated variation vector field. Furthermore, let:

\[
{V}_{t} = \frac{\mathrm{d}\omega }{\mathrm{d}t} = \text{ velocity vector of }\omega ,
\]

\[
{A}_{t} = \frac{\mathrm{D}}{\mathrm{d}t}\frac{\mathrm{d}\omega }{\mathrm{d}t} = \text{ acceleration vector of }\omega ,
\]

\( {\Delta }_{t}V = {V}_{t + } - {V}_{t - } = \) discontinuity in the velocity vector at \( t \) , where \( 0 < t < 1 \) .

Of course \( {\Delta }_{t}V = 0 \) for all but a finite number of values of \( t \) .

Theorem 12.2 (First Variation Formula). The derivative \( {\left. \frac{1}{2}\mathrm{\;d}E\left( \overline{\alpha }\left( u\right) \right) /\mathrm{d}u\right| }_{u = 0} \) is equal to

\[
- \mathop{\sum }\limits_{t}\left\langle  {{W}_{t},{\Delta }_{t}V}\right\rangle   - {\int }_{0}^{1}\left\langle  {{W}_{t},{A}_{t}}\right\rangle  \mathrm{d}t
\]

Proof. According to Lemma 8.5, we have

\[
\frac{\partial }{\partial u}\left\langle  {\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial t}}\right\rangle   = 2\left\langle  {\frac{\mathrm{D}}{\mathrm{d}u}\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial t}}\right\rangle  .
\]

Therefore

\[
\frac{\mathrm{d}E\left( {\overline{\alpha }\left( u\right) }\right) }{\mathrm{d}u} = \frac{\mathrm{d}}{\mathrm{d}u}{\int }_{0}^{1}\left\langle  {\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t = 2{\int }_{0}^{1}\left\langle  {\frac{\mathrm{D}}{\mathrm{d}u}\frac{\partial \alpha }{\partial t},\frac{\partial \alpha }{\partial t}}\right\rangle  .
\]

By Lemma 8.9 we can substitute \( \frac{\mathrm{D}}{\mathrm{d}u}\frac{\partial \alpha }{\partial t} \) for \( \frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial u} \) in this last formula.

Choose \( 0 = {t}_{0} < {t}_{1} < \cdots  < {t}_{k} = 1 \) so that \( \alpha \) is differentiable on each strip \( \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {{t}_{i - 1},{t}_{i}}\right\rbrack \) . Then we can "integrate by parts" on \( \left\lbrack  {{t}_{i - 1},{ti}}\right\rbrack \) , as follows. The identity

\[
\frac{\partial }{\partial t}\left\langle  {\frac{\partial \alpha }{\partial u},\frac{\partial \alpha }{\partial t}}\right\rangle   = \left\langle  {\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial u},\frac{\partial \alpha }{\partial t}}\right\rangle   + \left\langle  {\frac{\partial \alpha }{\partial u},\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t}}\right\rangle
\]

implies that

\[
{\int }_{{t}_{i - 1}}^{{t}_{i}}\left\langle  {\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial u},\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t = {\left. \left\langle  \frac{\partial \alpha }{\partial u},\frac{\partial \alpha }{\partial t}\right\rangle  \right| }_{t = {t}_{i - 1} + }^{t = {t}_{i} - } - {\int }_{{t}_{i - 1}}^{{t}_{i}}\left\langle  {\frac{\partial \alpha }{\partial u},\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t.
\]

Adding up the corresponding formulas for \( i = 1,\ldots , k \) ; and using the fact that \( \frac{\partial \alpha }{\partial u} = 0 \) for \( t = 0 \) or 1, this gives

\[
\frac{1}{2}\frac{\mathrm{d}E\left( {\overline{\alpha }\left( u\right) }\right) }{\mathrm{d}u} =  - \mathop{\sum }\limits_{{i = 1}}^{{k - 1}}\left\langle  {{W}_{t},{\Delta }_{{t}_{i}}V}\right\rangle   - {\int }_{0}^{1}\left\langle  {\frac{\partial \alpha }{\partial u},\frac{\mathrm{D}}{\mathrm{d}t}\frac{\partial \alpha }{\partial t}}\right\rangle  \mathrm{d}t.
\]

Setting \( u = 0 \) , we now obtain the required formula

\[
\frac{1}{2}\frac{\mathrm{d}E \circ  \overline{\alpha }}{\mathrm{d}u}\left( 0\right)  =  - \mathop{\sum }\limits_{t}\left\langle  {{W}_{t},{\Delta }_{t}V}\right\rangle   - {\int }_{0}^{1}\langle W, A\rangle \mathrm{d}t.
\]

This completes the proof.

Intuitively, the first term in the expression for \( \mathrm{d}E \circ  \overline{\alpha }/\mathrm{d}u\left( 0\right) \) shows that varying the path \( \omega \) in the direction of decreasing "kink," tends to decrease \( E \) ; see Figure 12.1.

![bo_d7du90alb0pc73deir8g_72_443_614_923_500_0.jpg](images/bo_d7du90alb0pc73deir8g_72_443_614_923_500_0.jpg)

Figure 12.1

The second term shows that varying the curve in the direction of its acceleration vector \( \frac{\mathrm{D}}{\mathrm{d}t}\left( \frac{\mathrm{d}\omega }{\mathrm{d}t}\right) \) tends to reduce \( E \) .

Recall that the path \( {\omega \alpha \Omega } \) is called a geodesic if and only if \( \omega \) is \( {C}^{\infty } \) on the whole interval \( \left\lbrack  {0,1}\right\rbrack \) , and the acceleration vector \( \frac{\mathrm{D}}{\mathrm{d}t}\left( \frac{\mathrm{d}\omega }{\mathrm{d}t}\right) \) of \( \omega \) is identically zero along \( \omega \) .

Corollary 12.3. The path \( \omega \) is a critical point for the function \( E \) if and only if \( \omega \) is a geodesic.

Proof. Clearly a geodesic is a critical point. Let \( \omega \) be a critical point. There is a variation of \( \omega \) with \( W\left( t\right)  = f\left( t\right) A\left( t\right) \) where \( f\left( t\right) \) is positive except that it vanishes at the \( {t}_{i} \) . Then

\[
\frac{1}{2}\frac{\mathrm{d}E}{\mathrm{\;d}u}\left( 0\right)  =  - {\int }_{0}^{1}f\left( t\right) \langle A\left( t\right) , A\left( t\right) \rangle \mathrm{d}t.
\]

This is zero if and only if \( A\left( t\right)  = 0 \) for all \( t \) . Hence each \( {\left. \omega \right| }_{\left\lbrack  {t}_{i},{t}_{i + 1}\right\rbrack  } \) is a geodesic.

Now pick a variation such that \( W\left( {t}_{i}\right)  = {\Delta }_{{t}_{i}}V \) . Then \( \frac{1}{2}\mathrm{\;d}E/\mathrm{d}u\left( 0\right)  =  - \sum \left\langle  {{\Delta }_{{t}_{i}}V,{\Delta }_{{t}_{i}}V}\right\rangle \) . If this is zero then all \( {\Delta }_{t}V \) are 0, and \( \omega \) is differentiable of class \( {C}^{1} \) , even at the points \( {t}_{i} \) . Now it follows from the uniqueness theorem for differential equations that \( \omega \) is \( {C}^{\infty } \) everywhere: thus \( \omega \) is an unbroken geodesic.
