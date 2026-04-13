# B Bernoulli Numbers

Since the appearance of Hirzebruch's signature theorem and his generalized Riemann-Roch theorem, it has become useful for topologists to know something about Bernoulli numbers and their number theoretic properties. This appendix will describe some of these properties.

The Bernoulli numbers \( {B}_{1},{B}_{2},\ldots \) can be defined as the coefficients that appear in the power series

\[
\frac{x}{\tanh x} = \frac{x\cosh x}{\sinh x} = 1 + \frac{{B}_{1}}{2!}{\left( 2x\right) }^{2} - \frac{{B}_{2}}{4!}{\left( 2x\right) }^{4} + \frac{{B}_{3}}{6!}{\left( 2x\right) }^{6} -  + \ldots
\]

(convergent for \( \left| x\right|  < \pi \) ), or equivalently in the expansion

\[
\frac{z}{{e}^{z} - 1} = 1 - \frac{z}{2} + \frac{{B}_{1}}{2!}{z}^{2} - \frac{{B}_{2}}{4!}{z}^{4} + \frac{{B}_{3}}{6!}{z}^{6} -  + \ldots .
\]

These two series are related by the easily verified identity

\[
\frac{x}{\tanh x} = \frac{2x}{{e}^{2x} - 1} + x.
\]

With this notation one has

\[
{B}_{1} = \frac{1}{6},{B}_{2} = \frac{1}{30},{B}_{3} = \frac{1}{42},{B}_{4} = \frac{1}{30},{B}_{5} = \frac{5}{66},{B}_{6} = \frac{691}{2730},{B}_{7} = \frac{7}{6},{B}_{8} = \frac{3617}{510}\text{ , }
\]

and so on. (The reader should beware since other conflicting notations are also in common usage.) These numbers were first introduced by Jakob Bernoulli, the oldest of that famous family of mathematicians, in a work published posthumously in 1713. They can be computed for example by actually dividing the appropriate power series, or by a procedure based on the proof of Lemma B.1 below.

Many related classical power series expansions can be derived from these. For example the identity

\[
\frac{1}{\sinh {2x}} = \frac{1}{\tanh x} - \frac{1}{\tanh {2x}}
\]

leads to the series

\[
\frac{u}{\sinh u} = 1 - \left( {{2}^{2} - 2}\right) \frac{{B}_{1}}{2!}{u}^{2} + \left( {{2}^{4} - 2}\right) \frac{{B}_{2}}{4!}{u}^{4} -  + \ldots
\]

(compare Problem 19-C), and the identity

\[
\tanh x = \frac{2}{\tanh {2x}} - \frac{1}{\tanh x}
\]

leads to the series

\[
\tanh x = {2}^{2}\left( {{2}^{2} - 1}\right) \frac{{B}_{1}}{2!}x - {2}^{4}\left( {{2}^{4} - 1}\right) \frac{{B}_{2}}{4!}{x}^{3} +  - \ldots .
\]

Closely related, by means of the equation \( \tanh {iy} = i\tan y \) , is the series

\[
\tan y = {2}^{2}\left( {{2}^{2} - 1}\right) \frac{{B}_{1}}{2!}y + {2}^{4}\left( {{2}^{4} - 1}\right) \frac{{B}_{2}}{4!}{y}^{3} + \ldots .
\]

This last can be used to prove an interesting number theoretic property.

Lemma B.1. For each \( n \) the number \( {2}^{2n}\left( {{2}^{2n} - 1}\right) {B}_{n}/{2n} \) is a positive integer.

Proof. For the above Taylor expansion shows that \( {2}^{2n}\left( {{2}^{2n} - 1}\right) {B}_{n}/{2n} \) is equal to the \( \left( {{2n} - 1}\right) \) -st derivative of \( \tan y \) at the origin. But the identity

\[
\frac{\mathrm{d}{\tan }^{m}y}{\mathrm{\;d}y} = m\left( {{\tan }^{m - 1}y + {\tan }^{m + 1}y}\right)
\]

together with a straightforward induction shows that the \( \left( {{2n} - 1}\right) \) -st derivative of \( \tan y \) equals

\[
{a}_{n0} + {a}_{n1}{\tan }^{2}y + \ldots  + {a}_{nn}{\tan }^{2n}y
\]

where the coefficients \( {a}_{n0},{a}_{n1},\ldots ,{a}_{nn} \) are positive integers. In particular the value \( {a}_{n0} \) at the origin is a positive integer.

Lemma B. 2 (Lipschitz-Sylvester). For any integer \( k \) , the expression \( {k}^{2n}\left( {{k}^{2n} - }\right. \) 1) \( {B}_{n}/{2n} \) is an integer.

Proof. Consider the function \( f\left( x\right)  = 1 + {e}^{x} + {e}^{2x} + \ldots  + {e}^{\left( {k - 1}\right) x} = \left( {{e}^{kx} - 1}\right) /\left( {{e}^{x} - 1}\right) \) . Note that \( f\left( 0\right)  = k \) , and that the derivatives of \( f \) at zero are all integers. Now consider the logarithmic derivative

\[
{f}^{\prime }\left( x\right) /f\left( x\right)  = \frac{\mathrm{d}}{\mathrm{d}x}\left( {\log \left( {{e}^{kx} - 1}\right)  - \log \left( {{e}^{x} - 1}\right) }\right)  = \frac{k{e}^{kx}}{{e}^{kx} - 1} - \frac{{e}^{x}}{{e}^{x} - 1}.
\]

Using the Taylor expansion

\[
\frac{{e}^{x}}{{e}^{x} - 1} = \frac{1}{x}\frac{-x}{{e}^{-x} - 1} = \frac{1}{x}\left( {1 + \frac{x}{2} + \frac{{B}_{1}}{2!}{x}^{2} - \frac{{B}_{2}}{4!}{x}^{4} +  - \ldots }\right) ,
\]

we obtain

\[
\frac{{f}^{\prime }\left( x\right) }{f\left( x\right) } = \frac{k - 1}{2} + \left( {{k}^{2} - 1}\right) \frac{{B}_{1}}{2!}x - \left( {{k}^{4} - 1}\right) \frac{{B}_{2}}{4!}{x}^{3} +  - \ldots .
\]

Therefore the \( \left( {{2n} - 1}\right) \) -st derivative of \( {f}^{\prime }\left( x\right) /f\left( x\right) \) at the origin is equal to \( \pm  \left( {{k}^{2n} - 1}\right) {B}_{n}/{2n} \) . A straightforward induction shows that this derivative can be expressed as a polynomial in \( f\left( x\right) ,{f}^{\prime }\left( x\right) ,\ldots ,{f}^{\left( 2n\right) }\left( x\right) \) with integer coefficients, divided by \( {\left( f\left( x\right) \right) }^{2n} \) . Setting \( x = 0 \) , this yields

\[
\frac{\left( {{k}^{2n} - 1}\right) {B}_{n}}{2n} = \frac{\text{ integer }}{{k}^{2n}},
\]

as required.

The following two theorems give more precise number theoretic information. The first was proved independently by T. Clausen and K. G. C von Staudt in 1840.

Theorem B.3. The rational number \( {\left( -1\right) }^{n}{B}_{n} \) is congruent mod \( \mathbb{Z} \) to \( \sum \left( {1/p}\right) \) , to be summed over all primes \( p \) such that \( p - 1 \) divides \( {2n} \) . Hence the denominator of \( {B}_{n} \) , expressed as a fraction in lowest terms, is equal to the product of all primes \( p \) with \( \left( {p - 1}\right)  \mid  {2n} \) .

Proof. Thus the denominator of \( {B}_{n} \) is always square free and divisible by 6 . It is divisible by a prime \( p > 3 \) if and only if \( n \) is a multiple of \( \left( {p - 1}\right) /2 \) . For a proof the reader is referred to [Har+08, Section 7.10] or [BS66, p. 384]

The next result was proved by von Staudt in 1845.

Theorem B.4. A prime divides the denominator of \( {B}_{n}/n \) (expressed as a fraction in lowest terms) if and only if it divides the denominator of \( {B}_{n} \) .

It is now easy to compute the denominator of \( {B}_{n}/n \) explicitly. For any prime \( p \) with \( \left( {p - 1}\right)  \mid  {2n} \) , let \( {p}^{\mu } \) be the highest power of \( p \) dividing \( n \) . Then clearly \( {p}^{\mu  + 1} \) is the highest power of \( p \) dividing the denominator of \( {B}_{n}/n \) . As an example, for \( n = {14} \) since the primes2,3,5,29are the only ones satisfying \( \left( {p - 1}\right)  \mid  {2n} \) , it follows that the denominator of \( {B}_{14}/{14} \) is equal to \( {2}^{2} \cdot  3 \cdot  5 \cdot  {29} \) .

Remark. This computation is of interest to homotopy theorists, in view of the theorem that the image of the stable \( J \) -homomorphism

\[
J : {\pi }_{{4n} - 1}{\mathrm{{SO}}}_{N} \rightarrow  {\pi }_{{4n} - 1 + N}\left( {S}^{N}\right)
\]

is a cyclic group of order equal to the denominator of \( {B}_{n}/{4n} \) . (Compare [KM63], [Ada65] and [Mah70].)

Proof of B.4. Let \( p \) be an arbitrary prime. If \( p \) divides the denominator of \( {B}_{n} \) , then it certainly divides the denominator of \( {B}_{n}/n \) . If \( p \) does not divide the denominator of \( {B}_{n} \) , then \( {2n} \text{ ≢ } 0\left( {{\;\operatorname{mod}\;p} - 1}\right) \) by B.3. Choose a primitive root \( k \) modulo \( p \) , that is, choose \( k \) so that \( {k}^{r} \equiv  1\left( {\;\operatorname{mod}\;p}\right) \) if and only if \( r \) is a multiple of \( p - 1 \) . Then

\[
{k}^{2n} \text{ ≢ } 1\;\left( {\;\operatorname{mod}\;p}\right)
\]

hence the integer \( {k}^{2n}\left( {{k}^{2n} - 1}\right) /2 \) is relatively prime to \( p \) . Therefore \( {B}_{n}/n \) , being equal to the integer \( {k}^{2n}\left( {{k}^{2n} - 1}\right) {B}_{n}/{2n} \) divided by \( {k}^{2n}\left( {{k}^{2n} - 1}\right) /2 \) , has denominator prime to \( p \) .

The numerator of the fraction \( {B}_{n}/n \) is much more difficult to compute. For small values of \( n \) it can be tabulated as follows.

<table><tr><td>\( n \)</td><td>≤ 5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>numerator \( \left( \frac{{B}_{n}}{n}\right) \)</td><td>1</td><td>691</td><td>1</td><td>3617</td><td>43867</td><td>174611</td><td>77683</td><td>236364091</td></tr></table>

Remark. This numerator is of interest to differential topologists in view of the theorem that the group consisting of all diffeomorphism classes of exotic \( \left( {{4n} - 1}\right)  - \) spheres which bound parallelizable manifolds is a cyclic group of order

\[
{2}^{{2n} - 2}\left( {{2}^{{2n} - 1} - 1}\right)  \times  \text{ numerator }\left( \frac{4{B}_{n}}{n}\right)
\]

for \( n \geq  2 \) . (See [KM63].) It of interest in number theory since Kummer, in 1850, proved Fermat’s last theorem for any prime exponent \( p \) which does not divide the numerator of any \( {B}_{n}/n \) . (See [BS66].) Such primes are called "regular". The smallest irregular prime is 37, which divides the numerator 7709321041217 of \( {B}_{16} \) . If two integers \( m \) and \( n \) satisfy \( m \equiv  n \text{ ≢ } 0\left( {{\;\operatorname{mod}\;\left( {p - 1}\right) }/2}\right) \) for some prime \( p \) , then Kummer showed that \( p \) divides the numerator of

\[
\frac{{\left( -1\right) }^{m}{B}_{m}}{m} - \frac{{\left( -1\right) }^{n}{B}_{n}}{n}.
\]

Therefore, in order to test a given prime \( p \) for regularity, it suffices to examine the numerators of those \( {B}_{n} \) with \( 1 \leq  n < \left( {p - 1}\right) /2 \) .

The numerator of \( {B}_{n}/n \) is non-trivial for \( n \geq  8 \) , and grows very rapidly with \( n \) . To see this, recall the famous formula

\[
1 + \frac{1}{{2}^{2n}} + \frac{1}{{3}^{2n}} + \frac{1}{{4}^{2n}} + \ldots  = \frac{{B}_{n}{\left( 2\pi \right) }^{2n}}{2\left( {2n}\right) !}
\]

of Euler. (See Problem B-4 below.) Using Stirling's formula

\[
1 < \frac{m!}{{m}^{m}{e}^{-m\sqrt{2\pi m}}} < {e}^{1/{12m}}
\]

(see [AB15]), this implies that

\[
{B}_{n} > \frac{2\left( {2n}\right) !}{{\left( 2\pi \right) }^{2n}} > 4{\left( \frac{n}{\pi e}\right) }^{2n}\sqrt{\pi n}
\]

(where all three expressions are asymptotically equal as \( n \rightarrow  \infty \) ). Therefore

\[
\text{ numerator }\left( \frac{{B}_{n}}{n}\right)  > \frac{{B}_{n}}{n} > \frac{4}{\sqrt{e}}{\left( \frac{n}{\pi e}\right) }^{{2n} - \frac{1}{2}} > 1
\]

for all \( n > {\pi e} = {8.539}\ldots \)

For further information concerning Bernoulli numbers, the reader is referred to [Nie23] or [BS66].

We conclude with some exercises.

Problem B-1 (J. F. Adams). If all prime factors of \( n \) have the form \( {6k} + 1 \) , show that the denominator of \( {B}_{n}/n \) is equal to 6 .

Problem B-2 (J. F. Adams). Given constants \( N > {\log }_{2}\left( {4n}\right) \) show that the greatest common divisor of the integers

\[
{2}^{N}\left( {{2}^{2n} - 1}\right) ,{3}^{N}\left( {{3}^{2n} - 1}\right) ,{4}^{N}\left( {{4}^{2n} - 1}\right) ,\ldots
\]

is equal to the denominator of \( {B}_{n}/{4n} \) .

Problem B-3. Let \( D = \frac{\mathrm{d}}{\mathrm{d}t} \) denote the differentiation operator \( f\left( t\right)  \mapsto  {f}^{\prime }\left( t\right) \) applied to any polynomial \( f\left( t\right) \) . Show that the operator

\[
{e}^{D} = 1 + D + \frac{1}{2!}{D}^{2} + \ldots
\]

maps \( f\left( t\right) \) to \( f\left( {t + 1}\right) \) , and show that the operator

\[
\frac{D}{{e}^{D} - 1} = 1 - \frac{1}{2}D + \frac{{B}_{1}}{2!}{D}^{2} -  + \ldots
\]

maps \( f\left( t\right) \) to a polynomial

\[
g\left( t\right)  = f\left( t\right)  - \frac{1}{2}{f}^{\prime }\left( t\right)  + \frac{{B}_{1}}{2!}{f}^{\prime \prime }\left( t\right)  - \frac{{B}_{2}}{4!}{f}^{\prime \prime \prime }\left( t\right)  +  - \ldots
\]

which satisfies the difference equation

\[
g\left( {t + 1}\right)  - g\left( t\right)  = {f}^{\prime }\left( t\right) .
\]

In this way prove the Euler-Maclaurin summation formula

\[
{f}^{\prime }\left( 0\right)  + {f}^{\prime }\left( 1\right)  + \ldots  + {f}^{\prime }\left( {k - 1}\right)  = g\left( k\right)  - g\left( 0\right) .
\]

Problem B-4. Taking \( f\left( t\right)  = {t}^{m}/m! \) , the corresponding polynomial

\[
g\left( t\right)  = \frac{{t}^{m}}{m!} - \frac{1}{2}\frac{{t}^{m - 1}}{\left( {m - 1}\right) !} + \frac{{B}_{1}}{2!}\frac{{t}^{m - 2}}{\left( {m - 2}\right) !} +  - \ldots
\]

may be called the \( m \) -th "Bernoulli polynomial" \( {p}_{m}\left( t\right) \) . Show that these Bernoulli polynomials can be characterized inductively, starting with \( {p}_{0}\left( t\right)  = 1 \) , by the property that each \( {p}_{m}\left( t\right) , m \geq  1 \) , is an indefinite integral of \( {p}_{m - 1}\left( t\right) \) and satisfies \( {\int }_{0}^{1}{p}_{m}\left( t\right) \mathrm{d}t = 0 \) . Compute the integral

\[
{\int }_{0}^{1}{p}_{m}\left( t\right) {e}^{-{2\pi ikt}}\mathrm{\;d}t =  - \frac{1}{{\left( 2\pi ik\right) }^{m}}
\]

inductively, for \( k \neq  0, m \geq  1 \) , using integration by parts, and hence establish the uniformly convergent Fourier series expansion

\[
{p}_{m}\left( t\right)  =  - \mathop{\sum }\limits_{{k \neq  0}}\frac{{e}^{2\pi ikt}}{{\left( 2\pi ik\right) }^{m}}
\]

for \( m \geq  2,0 \leq  t \leq  1 \) . Evaluating at \( t = 0 \) , prove Euler’s formula

\[
\frac{{B}_{n}}{\left( {2n}\right) !} = 2\mathop{\sum }\limits_{{k = 1}}^{\infty }\frac{1}{{\left( 2\pi k\right) }^{2n}}.
\]
