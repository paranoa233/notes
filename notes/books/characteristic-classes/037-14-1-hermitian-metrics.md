# 14.1 Hermitian Metrics

Just as Euclidean metrics play an important role in the study of real vector bundles, the analogous Hermitian metrics plays an important role for complex vector bundles. By definition, a Hermitian metric on a complex vector bundle \( \omega \) is a Euclidean metric

\[
v \mapsto  {\left| v\right| }^{2} \geq  0
\]

on the underlying real vector bundle (see \( \text{ § }{2.1} \) ), which satisfies the identity

\[
\left| {iv}\right|  = \left| v\right| \text{ . }
\]

Given such a Hermitian metric it is not difficult to show that there is one and only one complex valued inner product

\[
\langle v, w\rangle  = \frac{1}{2}\left( {{\left| v + w\right| }^{2} - {\left| v\right| }^{2} - {\left| w\right| }^{2}}\right)
\]

\[
+ \frac{1}{2}i\left( {{\left| v + iw\right| }^{2} - {\left| v\right| }^{2} - {\left| iw\right| }^{2}}\right) ,
\]

defined for \( v \) and \( w \) in the same fiber of \( \omega \) , which

(1) is complex linear as a function of \( v \) for fixed \( w \) ,

(2) is conjugate linear as a function of \( w \) for fixed \( v \) (that is \( \langle v,{\lambda w}\rangle  = \overline{\lambda }\langle v, w\rangle \) ), and

(3) satisfies \( \langle v, v\rangle  = {\left| v\right| }^{2} \) .

The two vectors \( v \) and \( w \) are said to be orthogonal if this complex inner product \( \langle v, w\rangle \) is zero. The Hermitian identity

\[
\langle w, v\rangle  = \overline{\langle v, w\rangle }
\]

is easily verified, hence \( v \) is orthogonal to \( w \) if and only if \( w \) is orthogonal to \( v \) .

If this space \( B \) is paracompact, then every complex vector bundle over \( B \) admits a Hermitian metric. (Compare Problem 2-C.)
