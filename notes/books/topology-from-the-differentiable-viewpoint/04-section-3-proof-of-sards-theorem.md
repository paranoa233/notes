# §3 Proof of Sard's Theorem

First let us recall the statement:

Theorem of Sard. Let \( f : U \rightarrow  {R}^{p} \) be a smooth map, with \( U \) open in \( {R}^{n} \) , and let \( C \) be the set of critical points; that is the set of all \( {x\varepsilon U} \) with

\[
\operatorname{rank}d{f}_{x} < p
\]

Then \( f\left( C\right)  \subset  {R}^{p} \) has measure zero.

REMARK. The cases where \( n \leq  p \) are comparatively easy. (Compare de Rham [29, p. 10].) We will, however, give a unified proof which makes these cases look just as bad as the others.

The proof will be by induction on \( n \) . Note that the statement makes sense for \( n \geq  0, p \geq  1 \) . (By definition \( {R}^{0} \) consists of a single point.) To start the induction, the theorem is certainly true for \( n = 0 \) .

Let \( {C}_{1} \subset  C \) denote the set of all \( {x\varepsilon U} \) such that the first derivative \( d{f}_{x} \) is zero. More generally let \( {C}_{i} \) denote the set of \( x \) such that all partial derivatives of \( f \) of order \( \leq  i \) vanish at \( x \) . Thus we have a descending sequence of closed sets

\[
C \supset  {C}_{1} \supset  {C}_{2} \supset  {C}_{3} \supset  \cdots .
\]

The proof will be divided into three steps as follows:

Step 1. The image \( f\left( {C - {C}_{1}}\right) \) has measure zero.

Step 2. The image \( f\left( {{C}_{i} - {C}_{i + 1}}\right) \) has measure zero, for \( i \geq  1 \) .

STEP 3. The image \( f\left( {C}_{k}\right) \) has measure zero for \( k \) sufficiently large.

(REMARK. If \( f \) happens to be real analytic, then the intersection of the \( {C}_{i} \) is vacuous unless \( f \) is constant on an entire component of \( U \) . Hence in this case it is sufficient to carry out Steps 1 and 2.)

---

* Our proof is based on that given by Pontryagin [28]. The details are somewhat easier since we assume that \( f \) is infinitely differentiable.

---

Proof of Step 1. This first step is perhaps the hardest. We may assume that \( p \geq  2 \) , since \( C = {C}_{1} \) when \( p = 1 \) . We will need the well known theorem of Fubini* which asserts that a measurable set

\[
A \subset  {R}^{p} = {R}^{1} \times  {R}^{p - 1}
\]

must have measure zero if it intersects each hyperplane (constant) \( \times  {R}^{p - 1} \) in a set of \( \left( {p - 1}\right) \) -dimensional measure zero.

For each \( \bar{x}{\varepsilon C} - {C}_{1} \) we will find an open neighborhood \( V \subset  {R}^{n} \) so that \( f\left( {V \cap  C}\right) \) has measure zero. Since \( C - {C}_{1} \) is covered by countably many of these neighborhoods, this will prove that \( f\left( {C - {C}_{1}}\right) \) has measure zero.

Since \( \bar{x} \notin  {C}_{1} \) , there is some partial derivative, say \( \partial {f}_{1}/\partial {x}_{1} \) , which is not zero at \( \bar{x} \) . Consider the map \( h : U \rightarrow  {R}^{n} \) defined by

\[
h\left( x\right)  = \left( {{f}_{1}\left( x\right) ,{x}_{2},\cdots ,{x}_{n}}\right) .
\]

Since \( d{h}_{\widehat{x}} \) is nonsingular, \( h \) maps some neighborhood \( V \) of \( \bar{x} \) diffeomor-phically onto an open set \( {V}^{\prime } \) . The composition \( g = f \circ  {h}^{-1} \) will then map \( {V}^{\prime } \) into \( {R}^{p} \) . Note that the set \( {C}^{\prime } \) of critical points of \( g \) is precisely \( h\left( {V \cap  C}\right) \) ; hence the set \( g\left( {C}^{\prime }\right) \) of critical values of \( g \) is equal to \( f\left( {V \cap  C}\right) \) .

![bo_d7du9valb0pc73deirc0_27_407_1363_638_557_0.jpg](images/bo_d7du9valb0pc73deirc0_27_407_1363_638_557_0.jpg)

Figure 5. Construction of the map \( g \)

---

* For an easy proof (as well as an alternative proof of Sard's theorem) see Sternberg [35, pp. 51-52]. Sternberg assumes that \( A \) is compact, but the general case follows easily from this special case.

---

For each \( \left( {t,{x}_{2},\cdots ,{x}_{n}}\right) \varepsilon {V}^{\prime } \) note that \( g\left( {t,{x}_{2},\cdots ,{x}_{n}}\right) \) belongs to the hyperplane \( t \times  {R}^{p - 1} \subset  {R}^{p} \) : thus \( g \) carries hyperplanes into hyper-planes. Let

\[
{g}^{t} : \left( {t \times  {R}^{n - 1}}\right)  \cap  {V}^{\prime } \rightarrow  t \times  {R}^{p - 1}
\]

denote the restriction of \( g \) . Note that a point of \( t \times  {R}^{n - 1} \) is critical for \( {g}^{t} \) if and only if it is critical for \( g \) ; for the matrix of first derivatives of \( g \) has the form

\[
\left( {\partial {g}_{i}/\partial {x}_{j}}\right)  = \left( \begin{matrix} 1 & 0 \\   * & \left( {\partial {g}_{i}^{t}/\partial {x}_{j}}\right)  \end{matrix}\right) .
\]

According to the induction hypothesis, the set of critical values of \( {g}^{t} \) has measure zero in \( t \times  {R}^{p - 1} \) . Therefore the set of critical values of \( g \) intersects each hyperplane \( t \times  {R}^{p - 1} \) in a set of measure zero. This set \( g\left( {C}^{\prime }\right) \) is measurable, since it can be expressed as a countable union of compact subsets. Hence, by Fubini's theorem, the set

\[
g\left( {C}^{\prime }\right)  = f\left( {V \cap  C}\right)
\]

has measure zero, and Step 1 is complete.

Proof of STEP 2. For each \( \bar{x}\varepsilon {C}_{k} - {C}_{k + 1} \) there is some \( {\left( k + 1\right) }^{-{st}} \) derivative \( {\partial }^{k + 1}{f}_{r}/\partial {x}_{{s}_{1}}\ldots \partial {x}_{{s}_{k + 1}} \) which is not zero. Thus the function

\[
w\left( x\right)  = {\partial }^{k}{f}_{r}/\partial {x}_{{s}_{2}}\cdots \partial {x}_{{s}_{k + 1}}
\]

vanishes at \( \bar{x} \) but \( \partial w/\partial {x}_{{s}_{1}} \) does not. Suppose for definiteness that \( {s}_{1} = 1 \) . Then the map \( h : U \rightarrow  {R}^{n} \) defined by

\[
h\left( x\right)  = \left( {w\left( x\right) ,{x}_{2},\cdots ,{x}_{n}}\right)
\]

carries some neighborhood \( V \) of \( \bar{x} \) diffeomorphically onto an open set \( {V}^{\prime } \) . Note that \( h \) carries \( {C}_{k} \cap  V \) into the hyperplane \( 0 \times  {R}^{n - 1} \) . Again we consider

\[
g = f \circ  {h}^{-1} : {V}^{\prime } \rightarrow  {R}^{p}.
\]

Let

\[
\bar{g} : \left( {0 \times  {R}^{n - 1}}\right)  \cap  {V}^{\prime } \rightarrow  {R}^{p}
\]

denote the restriction of \( g \) . By induction, the set of critical values of \( \bar{g} \) has measure zero in \( {R}^{p} \) . But each point in \( h\left( {{C}_{k} \cap  V}\right) \) is certainly a critical point of \( \bar{g} \) (since all derivatives of order \( \leq  k \) vanish). Therefore

\[
\bar{g}h\left( {{C}_{k} \cap  V}\right)  = f\left( {{C}_{k} \cap  V}\right) \text{ has measure zero. }
\]

Since \( {C}_{k} - {C}_{k + 1} \) is covered by countably many such sets \( V \) , it follows that \( f\left( {{C}_{k} - {C}_{k + 1}}\right) \) has measure zero.

Proof of STEP 3. Let \( {I}^{n} \subset  U \) be a cube with edge \( \delta \) . If \( k \) is sufficiently large \( \left( {k > n/p - 1}\right. \) to be precise) we will prove that \( f\left( {{C}_{k} \cap  {I}^{n}}\right. \) ) has measure zero. Since \( {C}_{k} \) can be covered by countably many such cubes, this will prove that \( f\left( {C}_{k}\right) \) has measure zero.

From Taylor’s theorem, the compactness of \( {I}^{n} \) , and the definition of \( {C}_{k} \) , we see that

\[
f\left( {x + h}\right)  = f\left( x\right)  + R\left( {x, h}\right)
\]

where

1)

\[
\left| \right| R\left( {x, h}\right) \left| \right|  \leq  c\left| \right| h{\left| \right| }^{k + 1}
\]

for \( {x\varepsilon }{C}_{k} \cap  {I}^{n}, x + {h\varepsilon }{I}^{n} \) . Here \( c \) is a constant which depends only on \( f \) and \( {I}^{n} \) . Now subdivide \( {I}^{n} \) into \( {r}^{n} \) cubes of edge \( \delta /r \) . Let \( {I}_{1} \) be a cube of the subdivision which contains a point \( x \) of \( {C}_{k} \) . Then any point of \( {I}_{1} \) can be written as \( x + h \) , with

2)

\[
\parallel h\parallel  \leq  \sqrt{n}\left( {\delta /r}\right) .
\]

From 1) it follows that \( f\left( {I}_{1}\right) \) lies in a cube of edge \( a/{r}^{k + 1} \) centered about \( f\left( x\right) \) , where \( a = {2c}{\left( \sqrt{n}\delta \right) }^{k + 1} \) is constant. Hence \( f\left( {{C}_{k} \cap  {I}^{n}}\right) \) is contained in a union of at most \( {r}^{n} \) cubes having total volume

\[
V \leq  {r}^{n}{\left( a/{r}^{k + 1}\right) }^{p} = {a}^{p}{r}^{n - \left( {k + 1}\right) p}.
\]

If \( k + 1 > n/p \) , then evidently \( V \) tends to 0 as \( r \rightarrow  \infty \) ; so \( f\left( {{C}_{k} \cap  {I}^{n}}\right) \) must have measure zero. This completes the proof of Sard's theorem.
