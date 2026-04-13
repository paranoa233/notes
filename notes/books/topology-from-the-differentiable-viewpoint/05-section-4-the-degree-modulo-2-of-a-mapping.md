# §4 The Degree Modulo 2 of a Mapping

Consider a smooth map \( f : {S}^{n} \rightarrow  {S}^{n} \) . If \( y \) is a regular value, recall that #f \( {}^{-1}\left( y\right) \) denotes the number of solutions \( x \) to the equation \( f\left( x\right)  = y \) . We will prove that the residue class modulo 2 of \( \# {f}^{-1}\left( y\right) \) does not depend on the choice of the regular value \( y \) . This residue class is called the mod 2 degree of \( f \) . More generally this same definition works for any smooth map

\[
f : M \rightarrow  N
\]

where \( M \) is compact without boundary, \( N \) is connected, and both manifolds have the same dimension. (We may as well assume also that \( N \) is compact without boundary, since otherwise the mod 2 degree would necessarily be zero.) For the proof we introduce two new concepts.

## SMOOTH HOMOTOPY AND SMOOTH ISOTOPY

Given \( X \subset  {R}^{k} \) , let \( X \times  \left\lbrack  {0,1}\right\rbrack \) denote the subset* of \( {R}^{k + 1} \) consisting of all \( \left( {x, t}\right) \) with \( {x\varepsilon X} \) and \( 0 \leq  t \leq  1 \) . Two mappings

\[
f, g : X \rightarrow  Y
\]

are called smoothly homotopic (abbreviated \( f \sim  g \) ) if there exists a smooth map \( F : X \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  Y \) with

\[
F\left( {x,0}\right)  = f\left( x\right) ,\;F\left( {x,1}\right)  = g\left( x\right)
\]

---

* If \( M \) is a smooth manifold without boundary, then \( M \times  \left\lbrack  {0,1}\right\rbrack \) is a smooth manifold bounded by two "copies" of \( M \) . Boundary points of \( M \) will give rise to "corner" points of \( M \times  \left\lbrack  {0,1}\right\rbrack \) .

---

for all \( {x\varepsilon X} \) . This map \( F \) is called a smooth homotopy between \( f \) and \( g \) .

Note that the relation of smooth homotopy is an equivalence relation. To see that it is transitive we use the existence of a smooth function \( \varphi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \left\lbrack  {0,1}\right\rbrack \) with

\[
\varphi \left( t\right)  = 0\text{ for }0 \leq  t \leq  \frac{1}{3}
\]

\[
\varphi \left( t\right)  = 1\text{ for }\frac{2}{3} \leq  t \leq  1.
\]

(For example, let \( \varphi \left( t\right)  = \lambda \left( {t - \frac{1}{3}}\right) /\left( {\lambda \left( {t - \frac{1}{3}}\right)  + \lambda \left( {\frac{2}{3} - t}\right) }\right) \) , where \( \lambda \left( \tau \right)  = 0 \) for \( \tau  \leq  0 \) and \( \lambda \left( \tau \right)  = \exp \left( {-{\tau }^{-1}}\right) \) for \( \tau  > 0 \) .) Given a smooth homotopy \( F \) between \( f \) and \( g \) , the formula \( G\left( {x, t}\right)  = F\left( {x,\varphi \left( t\right) }\right) \) defines a smooth homotopy \( G \) with

\[
G\left( {x, t}\right)  = f\left( x\right) \text{ for }0 \leq  t \leq  \frac{1}{3}
\]

\[
G\left( {x, t}\right)  = g\left( x\right) \text{ for }\frac{2}{3} \leq  t \leq  1.
\]

Now if \( f \sim  g \) and \( g \sim  h \) , then, with the aid of this construction, it is easy to prove that \( f \sim  h \) .

If \( f \) and \( g \) happen to be diffeomorphisms from \( X \) to \( Y \) , we can also define the concept of a "smooth isotopy" between \( f \) and \( g \) . This also will be an equivalence relation.

Definition. The diffeomorphism \( f \) is smoothly isotopic to \( g \) if there exists a smooth homotopy \( F : X \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  Y \) from \( f \) to \( g \) so that, for each \( {t\varepsilon }\left\lbrack  {0,1}\right\rbrack \) , the correspondence

\[
x \rightarrow  F\left( {x, t}\right)
\]

maps \( X \) diffeomorphically onto \( Y \) .

It will turn out that the mod 2 degree of a map depends only on its smooth homotopy class:

Homotopy Lemma. Let \( f, g : M \rightarrow  N \) be smoothly homotopic maps between manifolds of the same dimension, where \( M \) is compact and without boundary. If \( {y\varepsilon N} \) is a regular value for both \( f \) and \( g \) , then

\[
\# {f}^{-1}\left( y\right)  \equiv  \# {g}^{-1}\left( y\right) \;\left( {\;\operatorname{mod}\;2}\right) .
\]

Proof. Let \( F : M \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  N \) be a smooth homotopy between \( f \) and \( g \) . First suppose that \( y \) is also a regular value for \( F \) . Then \( {F}^{-1}\left( y\right) \) is a compact 1-manifold, with boundary equal to

\[
{F}^{-1}\left( y\right)  \cap  \left( {M \times  0 \cup  M \times  1}\right)  = {f}^{-1}\left( y\right)  \times  0 \cup  {g}^{-1}\left( y\right)  \times  1.
\]

Thus the total number of boundary points of \( {F}^{-1}\left( y\right) \) is equal to

\[
\# {f}^{-1}\left( y\right)  + \# {g}^{-1}\left( y\right) \text{ . }
\]

But we recall from \( \text{ § }2 \) that a compact 1-manifold always has an even number of boundary points. Thus \( \# {f}^{-1}\left( y\right)  + \# {g}^{-1}\left( y\right) \) is even, and therefore

\[
\# {f}^{-1}\left( y\right)  \equiv  \# {g}^{-1}\left( y\right) \;\left( {\;\operatorname{mod}\;2}\right) .
\]

![bo_d7du9valb0pc73deirc0_32_441_839_482_289_0.jpg](images/bo_d7du9valb0pc73deirc0_32_441_839_482_289_0.jpg)

Figure 6. The number of boundary points on the left is congruent to the number on the right modulo 2

Now suppose that \( y \) is not a regular value of \( F \) . Recall (from §1) that \( \# {f}^{-1}\left( {y}^{\prime }\right) \) and \( \# {g}^{-1}\left( {y}^{\prime }\right) \) are locally constant functions of \( {y}^{\prime } \) (as long as we stay away from critical values). Thus there is a neighborhood \( {V}_{1} \subset  N \) of \( y \) , consisting of regular values of \( f \) , so that

\[
\# {f}^{-1}\left( {y}^{\prime }\right)  = \# {f}^{-1}\left( y\right)
\]

for all \( {y}^{\prime }\varepsilon {V}_{1} \) ; and there is an analogous neighborhood \( {V}_{2} \subset  N \) so that

\[
\# {g}^{-1}\left( {y}^{\prime }\right)  = \# {g}^{-1}\left( y\right)
\]

for all \( {y}^{\prime }\varepsilon {V}_{2} \) . Choose a regular value \( z \) of \( F \) within \( {V}_{1} \cap  {V}_{2} \) . Then

\[
\# {f}^{-1}\left( y\right)  = \# {f}^{-1}\left( z\right)  \equiv  \# {g}^{-1}\left( z\right)  = \# {g}^{-1}\left( y\right) ),
\]

which completes the proof.

We will also need the following:

Homogeneity Lemma. Let \( y \) and \( z \) be arbitrary interior points of the smooth, connected manifold \( N \) . Then there exists a diffeomorphism \( h : N \rightarrow  N \) that is smoothly isotopic to the identity and carries \( y \) into \( z \) .

(For the special case \( N = {S}^{n} \) the proof is easy: simply choose \( h \) to be the rotation which carries \( y \) into \( z \) and leaves fixed all vectors orthogonal to the plane through \( y \) and \( z \) .)

The proof in general proceeds as follows: We will first construct a smooth isotopy from \( {R}^{n} \) to itself which

1) leaves all points outside of the unit ball fixed, and

2) slides the origin to any desired point of the open unit ball.

![bo_d7du9valb0pc73deirc0_33_295_708_828_273_0.jpg](images/bo_d7du9valb0pc73deirc0_33_295_708_828_273_0.jpg)

Figure 7. Deforming the unit ball

Let \( \varphi  : {R}^{n} \rightarrow  R \) be a smooth function which satisfies

\[
\varphi \left( x\right)  > 0\text{ for }\parallel \left| x\right| \parallel  < 1
\]

\[
\varphi \left( x\right)  = 0\text{ for }\parallel \left| x\right| \parallel  \geq  1.
\]

(For example let \( \varphi \left( x\right)  = \lambda \left( {1 - \parallel x{\parallel }^{2}}\right) \) where \( \lambda \left( t\right)  = 0 \) for \( t \leq  0 \) and \( \lambda \left( t\right)  = \exp \left( {-{t}^{-1}}\right) \) for \( t > 0 \) .) Given any fixed unit vector \( {c\varepsilon }{S}^{n - 1} \) , consider the differential equations

\[
\frac{\mathrm{d}{x}_{i}}{\mathrm{\;d}t} = {c}_{i}\varphi \left( {{x}_{1},\cdots ,{x}_{n}}\right) ;\;i = 1,\cdots , n.
\]

For any \( \bar{x}\varepsilon {R}^{n} \) these equations have a unique solution \( x = x\left( t\right) \) , defined for all* real numbers which satisfies the initial condition

\[
x\left( 0\right)  = \bar{x}.
\]

We will use the notation \( x\left( t\right)  = {F}_{t}\left( \bar{x}\right) \) for this solution. Then clearly

1) \( {F}_{t}\left( \bar{x}\right) \) is defined for all \( t \) and \( \bar{x} \) and depends smoothly on \( t \) and \( \bar{x} \) ,

2) \( {F}_{0}\left( \bar{x}\right)  = \bar{x} \) ,

3) \( {F}_{s + t}\left( \bar{x}\right)  = {F}_{s} \circ  {F}_{t}\left( \bar{x}\right) \) .

---

* Compare [22, §2.4].

---

Therefore each \( {F}_{t} \) is a diffeomorphism from \( {R}^{n} \) onto itself. Letting \( t \) vary, we see that each \( {F}_{t} \) is smoothly isotopic to the identity under an isotopy which leaves all points outside of the unit ball fixed. But clearly, with suitable choice of \( c \) and \( t \) , the diffeomorphism \( {F}_{t} \) will carry the origin to any desired point in the open unit ball.

Now consider a connected manifold \( N \) . Call two points of \( N \) "isotopic" if there exists a smooth isotopy carrying one to the other. This is clearly an equivalence relation. If \( y \) is an interior point, then it has a neighborhood diffeomorphic to \( {R}^{n} \) ; hence the above argument shows that every point sufficiently close to \( y \) is "isotopic" to \( y \) . In other words, each "isotopy class" of points in the interior of \( N \) is an open set, and the interior of \( N \) is partitioned into disjoint open isotopy classes. But the interior of \( N \) is connected; hence there can be only one such isotopy class. This completes the proof.

We can now prove the main result of this section. Assume that \( M \) is compact and boundaryless, that \( N \) is connected, and that \( f : M \rightarrow  N \) is smooth.

Theorem. If \( y \) and \( z \) are regular values of \( f \) then

\[
\# {f}^{-1}\left( y\right)  \equiv  \# {f}^{-1}\left( z\right) \;\left( {\;\operatorname{modulo}2}\right) .
\]

This common residue class, which is called the mod 2 degree of f, depends only on the smooth homotopy class of \( f \) .

Proof. Given regular values \( y \) and \( z \) , let \( h \) be a diffeomorphism from \( N \) to \( N \) which is isotopic to the identity and which carries \( y \) to \( z \) . Then \( z \) is a regular value of the composition \( h \circ  f \) . Since \( h \circ  f \) is homotopic to \( f \) , the Homotopy Lemma asserts that

\[
\# {\left( h \circ  f\right) }^{-1}\left( z\right)  \equiv  \# {f}^{-1}\left( z\right) \;\left( {\;\operatorname{mod}\;2}\right) .
\]

But

\[
{\left( h \circ  f\right) }^{-1}\left( z\right)  = {f}^{-1}{h}^{-1}\left( z\right)  = {f}^{-1}\left( y\right) ,
\]

so that

\[
\# {\left( h \circ  f\right) }^{-1}\left( z\right)  = \# {f}^{-1}\left( y\right) .
\]

Therefore

\[
\# {f}^{-1}\left( y\right)  \equiv  \# {f}^{-1}\left( z\right) \;\left( {\;\operatorname{mod}\;2}\right) ,
\]

as required.

Call this common residue class \( {\deg }_{2}\left( f\right) \) . Now suppose that \( f \) is smoothly homotopic to \( g \) . By Sard’s theorem, there exists an element \( y \) : \( N \) which is a regular value for both \( f \) and \( g \) . The congruence

\[
{\deg }_{2}f \equiv  \# {f}^{-1}\left( y\right)  \equiv  \# {g}^{-1}\left( y\right)  \equiv  {\deg }_{2}g \tag{mod 2}
\]

now shows that \( {\deg }_{2}f \) is a smooth homotopy invariant, and completes the proof.

EXAMPLES. A constant map \( c : M \rightarrow  M \) has even mod 2 degree. The identity map \( I \) of \( M \) has odd degree. Hence the identity map of a compact boundaryless manifold is not homotopic to a constant.

In the case \( M = {S}^{n} \) , this result implies the assertion that no smooth map \( f : {D}^{n + 1} \rightarrow  {S}^{n} \) leaves the sphere pointwise fixed. (I.e., the sphere is not a smooth "retract" of the disk. Compare §2, Lemma 5.) For such a map \( f \) would give rise to a smooth homotopy

\[
F : {S}^{n} \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  {S}^{n},\;F\left( {x, t}\right)  = f\left( {tx}\right) ,
\]

between a constant map and the identity.
