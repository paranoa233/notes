# Chapter 3 Homotopy Type in Terms of Critical Values

Based on lecture notes by

M. Spivak and R. Wells

Throughout this section, if \( f \) is a real valued function on a manifold \( M \) , we let

\[
{M}^{a} = {f}^{-1}( - \infty , a\rbrack  = \{ p \in  M : f\left( p\right)  \leq  a\} .
\]

Theorem 3.1. Let \( f \) be a smooth real valued function on a manifold \( M \) . Let \( a < b \) and suppose that the set \( {f}^{-1}\left\lbrack  {a, b}\right\rbrack \) , consisting of all \( p \in  M \) with \( a \leq  f\left( p\right)  \leq  b \) , is compact, and contains no critical points of \( f \) . Then \( {M}^{a} \) is diffeomorphic to \( {M}^{b} \) . Furthermore, \( {M}^{a} \) is a deformation retract of \( {M}^{b} \) , so that the inclusion map \( {M}^{a} \rightarrow  {M}^{b} \) is a homotopy equivalence.

The idea of the proof is to push \( {M}^{b} \) down to \( {M}^{a} \) along the orthogonal trajectories of the hypersurfaces \( f = \) constant. (Compare Figure 3.1.)

![bo_d7du90alb0pc73deir8g_21_384_1323_802_292_0.jpg](images/bo_d7du90alb0pc73deir8g_21_384_1323_802_292_0.jpg)

Figure 3.1

Choose a Riemannian metric on \( M \) ; and let \( \langle X, Y\rangle \) denote the inner product of two tangent vectors, as determined by this metric. The gradient of \( f \) is the vector field grad \( f \) on \( M \) which is characterized by the identity \( {}^{1} \)

\[
\langle X,\operatorname{grad}f\rangle  = X\left( f\right)
\]

(= directional derivative of \( f \) along \( X \) ) for any vector field \( X \) . This vector field grad \( f \) vanishes precisely at the critical points of \( f \) . If \( c : \mathbf{R} \rightarrow  M \) is a curve with velocity vector \( \mathrm{d}c/\mathrm{d}t \) note the identity

\[
\left\langle  {\frac{\mathrm{d}c}{\mathrm{\;d}t},\operatorname{grad}f}\right\rangle   = \frac{\mathrm{d}\left( {f \circ  c}\right) }{\mathrm{d}t}.
\]

---

\( {}^{1} \) In classical notation, in terms of local coordinates \( {u}^{1},\ldots ,{u}^{n} \) , the gradient has components \( \mathop{\sum }\limits_{j}{g}^{ij}\partial f/\partial {u}^{j}. \)

---

Let \( \rho  : M \rightarrow  \mathbf{R} \) be a smooth function which is equal to \( 1/\langle \operatorname{grad}f,\operatorname{grad}f\rangle \) throughout the compact set \( {f}^{-1}\left\lbrack  {a, b}\right\rbrack \) ; and which vanishes outside of a compact neighborhood of this set. Then the vector field \( X \) , defined by

\[
{X}_{q} = \rho \left( q\right) {\left( \operatorname{grad}f\right) }_{q}
\]

satisfies the conditions of Lemma 2.4. Hence \( X \) generates a 1-parameter group of diffeomorphisms

\[
{\varphi }_{t} : M \rightarrow  M
\]

For fixed \( q \in  M \) consider the function \( t \mapsto  f\left( {{\varphi }_{t}\left( q\right) }\right) \) . If \( {\varphi }_{t}\left( q\right) \) lies in the set \( {f}^{-1}\left\lbrack  {a, b}\right\rbrack \) , then

\[
\frac{\mathrm{d}f\left( {{\varphi }_{t}\left( q\right) }\right) }{\mathrm{d}t} = \left\langle  {\frac{\mathrm{d}{\varphi }_{t}\left( q\right) }{\mathrm{d}t},\operatorname{grad}f}\right\rangle   = \langle X,\operatorname{grad}f\rangle  =  + 1.
\]

Thus the correspondence

\[
t \mapsto  f\left( {{\varphi }_{t}\left( q\right) }\right)
\]

is linear with derivative +1 as long as \( f\left( {{\varphi }_{t}\left( q\right) }\right) \) lies between \( a \) and \( b \) .

Now consider the diffeomorphism \( {\varphi }_{b - a} : M \rightarrow  M \) . Clearly this carries \( {M}^{a} \) dif-feomorphically onto \( {M}^{b} \) . This proves the first half of Theorem 3.1.

Define a 1-parameter family of maps

\[
{r}_{t} : {M}^{b} \rightarrow  {M}^{b}
\]

by

\[
{r}_{t}\left( q\right)  = \left\{  \begin{array}{lll} q & \text{ if } & f\left( q\right)  \leq  a \\  {\varphi }_{t\left( {a - f\left( q\right) }\right) }\left( q\right) & \text{ if } & a \leq  f\left( q\right)  \leq  b \end{array}\right.
\]

Then \( {r}_{0} \) is the identity, and \( {r}_{1} \) is a retraction from \( {M}^{b} \) to \( {M}^{a} \) . Hence \( {M}^{a} \) is a deformation retract of \( {M}^{b} \) . This completes the proof.

Remark. The condition that \( {f}^{-1}\left\lbrack  {a, b}\right\rbrack \) is compact cannot be omitted. For example Figure 3.2 indicates a situation in which this set is not compact. The manifold \( M \) does not contain the point \( p \) . Clearly \( {M}^{a} \) is not a deformation retract of \( {M}^{b} \) .

Theorem 3.2. Let \( f : M \rightarrow  \mathbf{R} \) be a smooth function, and let \( p \) be a non-degenerate critical point with index \( \lambda \) . Setting \( f\left( p\right)  = c \) , suppose that \( {f}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack \) is compact, and contains no critical point of \( f \) other then \( p \) , for some \( \varepsilon  > 0 \) . Then, for all sufficiently small \( \varepsilon \) , the set \( {M}^{c + \varepsilon } \) has the homotopy type of \( {M}^{c - \varepsilon } \) with a λ-cell attached.

The idea of the proof of this theorem is indicated in Figure 3.3, for the special case of the height function on a torus. The region

\[
{M}^{c - \varepsilon } = {f}^{-1}( - \infty , c - \varepsilon \rbrack
\]

is heavily shaded. We will introduce a new function \( F : M \rightarrow  \mathbf{R} \) which coincides with the height function \( f \) except that \( F < f \) in a small neighborhood of \( p \) . Thus the region \( {F}^{-1}( - \infty , c - \varepsilon \rbrack \) will consist of \( {M}^{c - \varepsilon } \) together with a region \( H \) near \( p \) . In Figure 3.3, \( H \) is the horizontally shaded region.

![bo_d7du90alb0pc73deir8g_23_533_200_521_487_0.jpg](images/bo_d7du90alb0pc73deir8g_23_533_200_521_487_0.jpg)

Figure 3.2

![bo_d7du90alb0pc73deir8g_23_455_1051_588_517_0.jpg](images/bo_d7du90alb0pc73deir8g_23_455_1051_588_517_0.jpg)

Figure 3.3

Choosing a suitable cell \( {\mathrm{e}}^{\lambda } \subset  H \) , a direct argument (i.e., pushing in along the horizontal lines) will show that \( {M}^{c - \varepsilon } \cup  {\mathrm{e}}^{\lambda } \) is a deformation retract of \( {M}^{c - \varepsilon } \cup  H \) . Finally, by applying Theorem 3.1 to the function \( F \) and the region \( {F}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack \) we will see that \( {M}^{c - \varepsilon } \cup  H \) is a deformation retract of \( {M}^{c + \varepsilon } \) . This will complete the proof.

Choose a coordinate system \( {u}^{1},\ldots {u}^{n} \) in a neighborhood \( U \) of \( p \) so that the identity

\[
f = c - {\left( {u}^{1}\right) }^{2} - \cdots  - {\left( {u}^{\lambda }\right) }^{2} + {\left( {u}^{\lambda  + 1}\right) }^{2} + \cdots  + {\left( {u}^{n}\right) }^{2}
\]

holds throughout \( U \) . Thus the critical point \( p \) will have coordinates

\[
{u}^{1}\left( p\right)  = \cdots  = {u}^{n}\left( p\right)  = 0.
\]

Choose \( \varepsilon  > 0 \) sufficiently small so that

(1) The region \( {f}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack \) is compact and contains no critical points other than \( p \) .

(2) The image of \( U \) under the diffeomorphic imbedding

\[
\left( {{u}^{1},\ldots ,{u}^{n}}\right)  : U \rightarrow  {\mathbf{R}}^{n}
\]

contains the closed ball

\[
\left\{  {\left( {{u}^{1},\ldots ,{u}^{n}}\right)  \mid  \sum {\left( {u}^{i}\right) }^{2} \leq  {2\varepsilon }}\right\}  .
\]

Now define \( {\mathrm{e}}^{\lambda } \) to be the set of points in \( U \) with

\[
{\left( {u}^{1}\right) }^{2} + \cdots  + {\left( {u}^{\lambda }\right) }^{2} \leq  \varepsilon \text{ and }{u}^{\lambda  + 1} = \cdots  = {u}^{n} = 0.
\]

The resulting situation is illustrated schematically in Figure 3.4.

![bo_d7du90alb0pc73deir8g_24_484_873_835_611_0.jpg](images/bo_d7du90alb0pc73deir8g_24_484_873_835_611_0.jpg)

Figure 3.4

The coordinate lines represent the planes \( {u}^{\lambda  + 1} = \cdots  = {u}^{n} = 0 \) and \( {u}^{1} = \cdots  = \; {u}^{\lambda } = 0 \) respectively; the circle represents the boundary of the ball of radius \( \sqrt{2\varepsilon } \) ; and the hyperbolas represent the hypersurfaces \( {f}^{-1}\left( {c - \varepsilon }\right) \) and \( {f}^{-1}\left( {c + \varepsilon }\right) \) . The region \( {M}^{c - \varepsilon } \) is heavily shaded; the region \( {f}^{-1}\left\lbrack  {c - \varepsilon , c}\right\rbrack \) is heavily dotted; and the region \( {f}^{-1}\left\lbrack  {c, c + \varepsilon }\right\rbrack \) is lightly dotted. The horizontal dark line through \( p \) represents the cell \( {\mathrm{e}}^{\lambda } \) .

Note that \( {\mathrm{e}}^{\lambda } \cap  {M}^{c - \varepsilon } \) is precisely the boundary \( {\dot{\mathrm{e}}}^{\lambda } \) , so that \( {\mathrm{e}}^{\lambda } \) is attached to \( {M}^{c - \varepsilon } \) as required. We must prove that \( {M}^{c - \varepsilon } \cup  {\mathrm{e}}^{\lambda } \) is a deformation retract of \( {M}^{c + \varepsilon } \) .

Construct a new smooth function \( F : M \rightarrow  \mathbf{R} \) as follows. Let \( \mu  : \mathbf{R} \rightarrow  \mathbf{R} \) be a \( {C}^{\infty } \) function satisfying the conditions

\[
\mu \left( 0\right)  > \varepsilon
\]

\[
\mu \left( r\right)  = 0\;\text{ for }\;r \geq  {2\varepsilon }
\]

\[
- 1 < {\mu }^{\prime }\left( r\right)  \leq  0\;\text{ for all }\;r,
\]

where \( {\mu }^{\prime }\left( r\right)  = \mathrm{d}\mu /\mathrm{d}r \) . Now let \( F \) coincide with \( f \) outside of the coordinate neighborhood \( U \) , and let

\[
F = f - \mu \left( {{\left( {u}^{1}\right) }^{2} + \cdots  + {\left( {u}^{\lambda }\right) }^{2} + 2{\left( {u}^{\lambda  + 1}\right) }^{2} + \cdots  + 2{\left( {u}^{n}\right) }^{2}}\right)
\]

within this coordinate neighborhood. It is easily verified that \( F \) is a well defined smooth function throughout \( M \) .

It is convenient to define two functions

\[
\xi ,\eta  : U \rightarrow  \lbrack 0,\infty )
\]

by

\[
\xi  = {\left( {u}^{1}\right) }^{2} + \cdots  + {\left( {u}^{\lambda }\right) }^{2},\;\eta  = {\left( {u}^{\lambda  + 1}\right) }^{2} + \cdots  + {\left( {u}^{n}\right) }^{2}
\]

Then \( f = c - \xi  + \eta \) ; so that:

\[
F\left( q\right)  = c - \xi \left( q\right)  + \eta \left( q\right)  - \mu \left( {\xi \left( q\right)  + {2\eta }\left( q\right) }\right)
\]

for all \( q \in  U \) .

Assertion 3.1. The region \( {F}^{-1}( - \infty , c + \varepsilon \rbrack \) coincides with the region \( {M}^{c + \varepsilon } = \; {f}^{-1}( - \infty , c + \varepsilon \rbrack \) .

Proof. Outside of the ellipsoid \( \xi  + {2\eta } \leq  {2\varepsilon } \) the functions \( f \) and \( F \) coincide. Within this ellipsoid we have

\[
F \leq  f = c - \xi  + \eta  \leq  c + \frac{1}{2}\xi  + \eta  \leq  c + \varepsilon .
\]

This completes the proof.

Assertion 3.2. The critical points of \( F \) are the same as those of \( f \) .

Proof. Note that

\[
\frac{\partial F}{\partial \xi } =  - 1 - {\mu }^{\prime }\left( {\xi  + {2\eta }}\right)  < 0
\]

\[
\frac{\partial F}{\partial \eta } = 1 - 2{\mu }^{\prime }\left( {\xi  + {2\eta }}\right)  \geq  1.
\]

Since

\[
\mathrm{d}F = \frac{\partial F}{\partial \xi }\mathrm{d}\xi  + \frac{\partial F}{\partial \eta }\mathrm{d}\eta
\]

where the covectors \( \mathrm{d}\xi \) and \( \mathrm{d}\eta \) are simultaneously zero only at the origin, it follows that \( F \) has no critical points in \( U \) other than the origin. Now consider the region \( {F}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack \) . By Assertion 3.1 together with the inequality \( F \leq  f \) we see that

\[
{F}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack   \subset  {f}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack  .
\]

Therefore this region is compact. It can contain no critical points of \( F \) except possibly \( p \) . But

\[
F\left( p\right)  = c - \mu \left( 0\right)  < c - \varepsilon .
\]

Hence \( {F}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack \) contains no critical points. Together with Theorem 3.1 this proves the following.

Assertion 3.3. The region \( {F}^{-1}( - \infty , c - \varepsilon \rbrack \) deformation retract of \( {M}^{c + \varepsilon } \) .

It will be convenient to denote this region \( {F}^{-1}( - \infty , c - \varepsilon \rbrack \) by \( {M}^{c - \varepsilon } \cup  H \) ; where \( H \) denotes the closure of \( {F}^{-1}( - \infty , c - \varepsilon \rbrack  - {M}^{c - \varepsilon } \) .

Remark. In the terminology of Smale, the region \( {M}^{c - \varepsilon } \cup  H \) is described as \( {M}^{c - \varepsilon } \) with a "handle" attached. It follows from Theorem 3.1 that the manifold-with-boundary \( {M}^{c - \varepsilon } \cup  H \) is diffeomorphic to \( {M}^{c + \varepsilon } \) . This fact is important in Smale’s theory of differentiable manifolds. (Compare [Sma61].)

Now consider the cell \( {\mathrm{e}}^{\lambda } \) consisting of all points \( q \) with

\[
\xi \left( q\right)  \leq  \varepsilon ,\;\eta \left( q\right)  = 0.
\]

Note that \( {\mathrm{e}}^{\lambda } \) is contained in the "handle" \( H \) . In fact, since \( \partial F/\partial \xi  < 0 \) , we have

\[
F\left( q\right)  \leq  F\left( p\right)  < c - \varepsilon
\]

but \( f\left( q\right)  \geq  c - \varepsilon \) for \( q \in  {\mathrm{e}}^{\lambda } \) .

![bo_d7du90alb0pc73deir8g_26_519_1064_709_616_0.jpg](images/bo_d7du90alb0pc73deir8g_26_519_1064_709_616_0.jpg)

Figure 3.5

The present situation is illustrated in Figure 3.5. The region \( {M}^{c - \varepsilon } \) is heavily shaded; the handle \( H \) is shaded with vertical arrows; and the region \( {F}^{-1}\left\lbrack  {c - \varepsilon , c + \varepsilon }\right\rbrack \) is dotted.

Assertion 3.4. The region \( {M}^{c - \varepsilon } \cup  {\mathrm{e}}^{\lambda } \) is a deformation retract of \( {M}^{c - \varepsilon } \cup  H \) .

Proof. A deformation retraction \( {r}_{t} : {M}^{c - \varepsilon } \cup  H \rightarrow  {M}^{c - \varepsilon } \cup  H \) is indicated schematically by the vertical arrows in Figure 3.5. More precisely let \( {r}_{t} \) be the identity outside of \( U \) ; and define \( {r}_{t} \) within \( U \) as follows. It in necessary to distinguish three cases as indicated in Figure 3.6.

![bo_d7du90alb0pc73deir8g_27_440_197_708_372_0.jpg](images/bo_d7du90alb0pc73deir8g_27_440_197_708_372_0.jpg)

Figure 3.6

Case 1. Within the region \( \xi  \leq  \varepsilon \) let \( {r}_{t} \) correspond to the transformation

\[
\left( {{u}^{1},\ldots ,{u}^{n}}\right)  \mapsto  \left( {{u}^{1},\ldots ,{u}^{\lambda }, t{u}^{\lambda  + 1},\ldots , t{u}^{n}}\right) .
\]

Thus \( {r}_{1} \) is the identity and \( {r}_{0} \) maps the entire region into \( {\mathrm{e}}^{\lambda } \) . The fact that each \( {r}_{t} \) maps \( {F}^{-1}( - \infty , c - \varepsilon \rbrack \) into itself, follows from the inequality \( \partial F/\partial \eta  > 0 \) .

Case 2. Within the region \( \varepsilon  \leq  \xi  \leq  \eta  + \varepsilon \) let \( {r}_{t} \) correspond to the transformation

\[
\left( {{u}^{1},\ldots ,{u}^{n}}\right)  \mapsto  \left( {{u}^{1},\ldots ,{u}^{\lambda },{s}_{t}{u}^{\lambda  + 1},\ldots ,{s}_{t}{u}^{n}}\right)
\]

where the number \( {s}_{t} \in  \left\lbrack  {0,1}\right\rbrack \) is defined by

\[
{s}_{t} = t + \left( {1 - t}\right) {\left( \frac{\xi  - \varepsilon }{\eta }\right) }^{\frac{1}{2}}.
\]

Thus \( {r}_{1} \) is again the identity, and \( {r}_{0} \) maps the entire region into the hypersurface \( {f}^{-1}\left( {c - \varepsilon }\right) \) . The reader should verify that the functions \( {s}_{t}{u}^{i} \) remain continuous as \( \xi  \rightarrow  \varepsilon ,\eta  \rightarrow  0 \) . Note that this definition coincides with that of Case 1 when \( \xi  = \varepsilon \) .

Case 3. Within the region \( \eta  + \varepsilon  \leq  \xi \) (i.e., within \( {M}^{c - \varepsilon } \) ). let \( {r}_{t} \) be the identity. This coincides with the preceding definition when \( \xi  = \eta  + \varepsilon \) .

This completes the proof that \( {M}^{c - \varepsilon } \cup  {\mathrm{e}}^{\lambda } \) is a deformation retract of \( {F}^{-1}( - \infty , c + \varepsilon \rbrack \) . Together with Assertion 3.4, it completes the proof of Theorem 3.2.

Remark. More generally suppose that there are \( k \) non-degenerate critical points \( {p}^{1},\ldots ,{p}^{k} \) with indices \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) in \( {f}^{-1}\left( c\right) \) . Then a similar proof shows that \( {M}^{c + \varepsilon } \) has the homotopy type of \( {M}^{c - \varepsilon } \cup  {\mathrm{e}}^{{\lambda }_{1}} \cup  \cdots  \cup  {\mathrm{e}}^{{\lambda }_{k}} \) .

Remark. A simple modification of the proof of Theorem 3.2 shows that the set \( {M}^{c} \) is also a deformation retract of \( {M}^{c + \varepsilon } \) . In fact \( {M}^{c} \) is a deformation retract of \( {F}^{-1}( - \infty , c\rbrack \) which is a deformation retract of \( {M}^{c + \varepsilon } \) (Compare Figure 3.7.) Combining this fact with Theorem 3.2 we see easily that \( {M}^{c - \varepsilon } \cup  {\mathrm{e}}^{\lambda } \) is a deformation retract of \( {M}^{c} \) .

![bo_d7du90alb0pc73deir8g_28_494_201_665_660_0.jpg](images/bo_d7du90alb0pc73deir8g_28_494_201_665_660_0.jpg)

Figure 3.7: \( {M}^{c} \) is heavily shaded, and \( {F}^{-1}\left\lbrack  {c, c + \varepsilon }\right\rbrack \) is dotted.

Theorem 3.3. If \( f \) is a differentiable function on a manifold \( M \) with no degenerate critical points, and if each \( {M}^{a} \) is compact, then \( M \) has the homotopy type of a \( {CW} \) - complex, with one cell of dimension \( \lambda \) for each critical point of index \( \lambda \) .

(For the definition of CW-complex see [Whi49a].)

The proof will be based on two lemmas concerning a topological space \( X \) with a cell attached.

Lemma 3.4 (Whitehead). Let \( {\varphi }_{0} \) and \( {\varphi }_{1} \) be homotopic maps from the sphere \( {\dot{\mathrm{e}}}^{\lambda } \) to \( X \) . Then the identity map of \( X \) extends to a homotopy equivalence

\[
k : X\underset{{\varphi }_{0}}{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  X\underset{{\varphi }_{1}}{ \cup  }{\mathrm{e}}^{\lambda }
\]

Proof. Define \( K \) by the formulas

\[
K\left( x\right)  = x
\]

\[
\text{ for }x \in  X
\]

\[
K\left( {tu}\right)  = {2tu}
\]

\[
\text{ for }0 \leq  t \leq  \frac{1}{2},\;u \in  {\dot{\mathrm{e}}}^{\lambda }
\]

\[
K\left( {tu}\right)  = {\varphi }_{2 - {2t}}\left( u\right)
\]

\[
\text{ for }\frac{1}{2} \leq  t \leq  1,\;u \in  {\dot{\mathrm{e}}}^{\lambda }\text{ . }
\]

Here \( {\varphi }_{t} \) denotes the homotopy between \( {\varphi }_{0} \) and \( {\varphi }_{1} \) ; and tu denotes the product of the scalar \( t \) with the unit vector \( u \) . A corresponding map

\[
\ell  : X\underset{{\varphi }_{1}}{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  X\underset{{\varphi }_{0}}{ \cup  }{\mathrm{e}}^{\lambda }
\]

is defined by similar formulas. It is now not difficult to verify that the compositions \( K\ell \) and \( \ell K \) are homotopic to the respective identity maps. Thus \( K \) is a homotopy equivalence.

For further details the reader is referred to, Lemma 5 of [Whi49b].

Lemma 3.5. Let \( \varphi  : {\dot{\mathrm{e}}}^{\lambda } \rightarrow  X \) be an attaching map. Any homotopy equivalence \( f : X \rightarrow  Y \) extends to a homotopy equivalence

\[
F : X\underset{\varphi }{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  X\underset{f \circ  \varphi }{ \cup  }{\mathrm{e}}^{\lambda }
\]

Proof. (Following an unpublished paper by P. Hilton.) Define \( F \) by the conditions

\[
\left\{  \begin{array}{l} {\left. F\right| }_{X} = f \\  {\left. F\right| }_{{\mathrm{e}}^{\lambda }} = \text{ identity. } \end{array}\right.
\]

Let \( g : Y \rightarrow  X \) be a homotopy inverse to \( f \) and define

\[
G : Y\underset{f \circ  \varphi }{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  Y\underset{g \circ  f \circ  \varphi }{ \cup  }{\mathrm{e}}^{\lambda }
\]

by the corresponding conditions \( {\left. G\right| }_{Y} = g,{\left. G\right| }_{{\mathrm{e}}^{\lambda }} = \) identity.

Since \( g \circ  f \circ  \varphi \) is homotopic to \( \varphi \) , it follows from Lemma 3.4 that there is a homotopy equivalence

\[
K : X\underset{g \circ  f \circ  \varphi }{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  X\underset{\varphi }{ \cup  }{\mathrm{e}}^{\lambda }
\]

We will first prove that the composition

\[
K \circ  G \circ  F : X\underset{\varphi }{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  X\underset{\varphi }{ \cup  }{\mathrm{e}}^{\lambda }
\]

is homotopic to the identity map.

Let \( {h}_{t} \) be a homotopy between \( g \circ  f \) and the identity. Using the specific definitions of \( K, G \) , and \( F \) , note that

\[
K \circ  G \circ  F\left( x\right)  = {gf}\left( x\right) \;\text{ for }\;x \in  X
\]

\[
K \circ  G \circ  F\left( {tu}\right)  = {2tu}
\]

\[
\text{ for }\;0 \leq  t \leq  \frac{1}{2},\;u \in  {\dot{\mathrm{e}}}^{\lambda }
\]

\[
K \circ  G \circ  F\left( {tu}\right)  = {h}_{2 - {2t}}\varphi \left( u\right) \;\text{ for }\;\frac{1}{2} \leq  t \leq  1,\;u \in  {\dot{\mathrm{e}}}^{\lambda }.
\]

The required homotopy

\[
{q}_{\tau } : X\underset{\varphi }{ \cup  }{\mathrm{e}}^{\lambda } \rightarrow  X\underset{\varphi }{ \cup  }{\mathrm{e}}^{\lambda }
\]

is now defined by the formula

\[
{q}_{\tau }\left( x\right)  = {h}_{\tau }\left( x\right)
\]

\[
\text{ for }x \in  X
\]

\[
{q}_{\tau }\left( {tu}\right)  = \frac{2}{1 + \tau }{tu}
\]

\[
\text{ for }\;0 \leq  t \leq  \frac{1 + \tau }{2},\;u \in  {\dot{\mathrm{e}}}^{\lambda }
\]

\[
{q}_{\tau }\left( {tu}\right)  = {h}_{2 - {2t} + \tau }\varphi \left( u\right)
\]

\[
\text{ for }\frac{1 + \tau }{2} \leq  t \leq  1,\;u \in  {\dot{\mathrm{e}}}^{\lambda }\text{ . }
\]

Therefore \( F \) has a left homotopy inverse.

The proof that \( F \) is a homotopy equivalence will now be purely formal, based on the following.

Assertion 3.5. If a map \( F \) has a left homotopy inverse \( L \) and a right homotopy inverse \( R \) , then \( F \) is a homotopy equivalence; and \( R \) (or \( L \) ) is a 2-sided homotopy

inverse.

Proof. The relations

\[
L \circ  F \simeq  \text{ identity, }\;F \circ  R \simeq  \text{ identity, }
\]

imply that

\[
L \simeq  L\left( {F \circ  R}\right)  = \left( {L \circ  F}\right) R \simeq  R.
\]

Consequently

\[
R \circ  F \simeq  L \circ  F \simeq  \text{ identity, }
\]

which proves that \( R \) is a 2-sided inverse.

The proof of Lemma 3.5 can now be completed as follows. The relation

\[
K \circ  F \circ  G \simeq  \text{ identity, }
\]

asserts that \( F \) has a left homotopy inverse; and a similar proof shows that \( G \) has a left homotopy inverse.

Step 1. Since \( K\left( {G \circ  F}\right)  \simeq \) identity, and \( K \) is known to have a left inverse, it follows that \( \left( {G \circ  F}\right) K \simeq \) identity.

Step 2. Since \( G\left( {F \circ  K}\right)  \simeq \) identity, and \( G \) is known to have a left inverse, it follows that \( \left( {F \circ  K}\right) G \simeq \) identity.

Step 3. Since \( F\left( {K \circ  G}\right)  \simeq \) identity, and \( F \) has \( K \circ  G \) as left inverse also, it follows that \( F \) is a homotopy equivalence.

This completes the proof of Lemma 3.5.

Proof of Theorem 3.3. Let \( {c}_{1} < {c}_{2} < {c}_{3} < \cdots \) be the critical values of \( f : M \rightarrow  \mathbf{R} \) . The sequence \( \left\{  {c}_{i}\right\} \) has no cluster point since each \( {M}^{a} \) is compact. The set \( {M}^{a} \) is vacuous for \( a < {c}_{1} \) . Suppose \( a{c}_{1},{c}_{2},{c}_{3},\ldots \) and that \( {M}^{a} \) is of the homotopy type of a CW-complex. Let \( c \) be the smallest \( {c}_{i} > a \) . By Theorems 3.1 and 3.2 and Chapter 3, \( {M}^{c + \varepsilon } \) has the homotopy type of \( {M}^{c - \varepsilon }\underset{{\varphi }_{1}}{ \cup  }{\mathrm{e}}^{{\lambda }_{1}} \cup  \cdots \underset{{\varphi }_{j\left( c\right) }}{ \cup  }{\mathrm{e}}^{{\lambda }_{j\left( c\right) }} \) for certain maps \( {\varphi }_{1},\ldots ,{\varphi }_{j\left( c\right) } \) when \( \varepsilon \) is small enough, and there is a homotopy equivalence \( h : {M}^{c - \varepsilon } \rightarrow  {M}^{a} \) . We have assumed that there is a homotopy equivalence \( {h}^{\prime } : {M}^{a} \rightarrow \; K \) , where \( K \) is a CW-complex.

Then each \( {h}^{\prime } \circ  h \circ  {\varphi }_{j} \) is homotopic by cellular approximation to a map

\[
{\psi }_{j} : {\dot{\mathrm{e}}}^{{\lambda }_{j}} \rightarrow  \left( {{\lambda }_{j} - 1}\right)  - \text{ skeleton of }K.
\]

Then \( K\underset{{\psi }_{1}}{ \cup  }{\mathrm{e}}^{{\lambda }_{1}} \cup  \cdots \underset{{\psi }_{j\left( c\right) }}{ \cup  }{\mathrm{e}}^{{\lambda }_{j\left( c\right) }} \) is a CW-complex, and has the same homotopy type as \( {M}^{c + \varepsilon } \) , by Lemmas 3.4 and 3.5.

By induction it follows that each \( {M}^{a}{}^{\prime } \) has the homotopy type of a CW-complex. If \( M \) is compact this completes the proof. If \( M \) is not compact, but all critical points lie in one of the compact sets \( {M}^{a} \) , then a proof similar to that of Theorem 3.1 shows that the set \( {M}^{a} \) is a deformation retract of \( M \) , so the proof is again complete.

If there are infinitely many critical points then the above construction gives us an infinite sequence of homotopy equivalences

![bo_d7du90alb0pc73deir8g_31_578_280_429_163_0.jpg](images/bo_d7du90alb0pc73deir8g_31_578_280_429_163_0.jpg)

each extending the previous one. Let \( K \) denote the union of the \( {K}_{i} \) in the direct limit topology, i.e., the finest possible compatible topology, and let \( g : M \rightarrow  K \) be the limit map. Then \( g \) induces isomorphisms of homotopy groups in all dimensions. We need only apply Theorem 1 of [Whi49a] to conclude that \( g \) is a homotopy equivalence. [Whitehead’s theorem states that if \( M \) and \( K \) are both dominated by CW-complexes, then any map \( M \rightarrow  K \) which induces isomorphisms of homotopy groups is a homotopy equivalence. Certainly \( K \) is dominated by itself. To prove that \( M \) is dominated by a CW-complex it is only necessary to consider \( M \) as a retract of tubular neighborhood in some Euclidean space.] This completes the proof of Theorem 3.3.

Remark. We have also proved that each \( {M}^{a} \) has the homotopy type of a finite CW-complex, with one cell of dimension \( \lambda \) for each critical point of index \( \lambda \) in \( {M}^{a} \) . This is true even if \( a \) is a critical value. (Compare Chapter 3.)
