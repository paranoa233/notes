## §4 Poincaré Lemmas

## The Poincaré Lemma for de Rham Cohomology

In this section we compute the ordinary cohomology and the compactly supported cohomology of \( {\mathbb{R}}^{n} \) . Let \( \pi  : {\mathbb{R}}^{n} \times  {\mathbb{R}}^{1} \rightarrow  {\mathbb{R}}^{n} \) be the projection on the first factor and \( s : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \times  {\mathbb{R}}^{1} \) the zero section.

![bo_d7b6f8alb0pc73dd9avg_43_509_1516_643_217_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_43_509_1516_643_217_0.jpg)

We will show that these maps induce inverse isomorphisms in cohomology and therefore \( {H}^{ * }\left( {\mathbb{R}}^{n + 1}\right)  \simeq  {H}^{ * }\left( {\mathbb{R}}^{n}\right) \) . As a matter of convention all maps are assumed to be \( {C}^{\infty } \) unless otherwise specified.

Since \( \pi  \circ  s = 1 \) , we have trivially \( {s}^{ * } \circ  {\pi }^{ * } = 1 \) . However \( s \circ  \pi  \neq  1 \) and correspondingly \( {\pi }^{ * } \circ  {s}^{ * } \neq  1 \) on the level of forms. For example, \( {\pi }^{ * } \circ  {s}^{ * } \) sends the function \( f\left( {x, t}\right) \) to \( f\left( {x,0}\right) \) , a function which is constant along every fiber. To show that \( {\pi }^{ * } \circ  {s}^{ * } \) is the identity in cohomology, it is enough to find a map \( K \) on \( {\Omega }^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) \) such that

\[
1 - {\pi }^{ * } \circ  {s}^{ * } =  \pm  \left( {{dK} \pm  {Kd}}\right)
\]

for \( {dK} \pm  {Kd} \) maps closed forms to exact forms and therefore induces zero in cohomology. Such a \( K \) is called a homotopy operator; if it exists, we say that \( {\pi }^{ * } \circ  {s}^{ * } \) is chain homotopic to the identity. Note that the homotopy operator \( K \) decreases the degree by 1 .

Every form on \( {\mathbb{R}}^{n} \times  \mathbb{R} \) is uniquely a linear combination of the following two types of forms:

\[
\text{ (I) }\left( {{\pi }^{ * }\phi }\right) f\left( {x, t}\right) \text{ , }
\]

\[
\text{ (II) }\left( {{\pi }^{ * }\phi }\right) f\left( {x, t}\right) {dt}\text{ , }
\]

where \( \phi \) is a form on the base \( {\mathbb{R}}^{n} \) . We define \( K : {\Omega }^{q}\left( {{\mathbb{R}}^{n} \times  \mathbb{R}}\right)  \rightarrow \; {\Omega }^{q - 1}\left( {{\mathbb{R}}^{n} \times  \mathbb{R}}\right) \) by

\[
\text{ (I) }\left( {{\pi }^{ * }\phi }\right) f\left( {x, t}\right)  \mapsto  0\text{ , }
\]

\[
\text{ (II) }\left( {{\pi }^{ * }\phi }\right) f\left( {x, t}\right) {dt} \mapsto  \left( {{\pi }^{ * }\phi }\right) {\int }_{0}^{t}f\text{ . }
\]

Let’s check that \( K \) is indeed a homotopy operator. We will use the simplified notation \( \partial f/\partial {xd} \) for \( \sum \partial f/\partial {x}_{i}d{x}_{i} \) , and \( \int g \) for \( \int g\left( {x, t}\right) {dt} \) . On forms of type (I),

\[
\omega  = \left( {{\pi }^{ * }\phi }\right)  \cdot  f\left( {x, t}\right) ,\;\deg \omega  = q,
\]

\[
\left( {1 - {\pi }^{ * }{s}^{ * }}\right) \omega  = \left( {{\pi }^{ * }\phi }\right)  \cdot  f\left( {x, t}\right)  - {\pi }^{ * }\phi  \cdot  f\left( {x,0}\right) ,
\]

\[
\left( {{dK} - {Kd}}\right) \omega  =  - {Kd\omega } =  - K\left( {\left( {d{\pi }^{ * }\phi }\right) f + {\left( -1\right) }^{q}{\pi }^{ * }\phi \left( {\frac{\partial f}{\partial x}{dx} + \frac{\partial f}{\partial t}{dt}}\right) }\right)
\]

\[
= {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi {\int }_{0}^{t}\frac{\partial f}{\partial t} = {\left( -1\right) }^{q - 1}{\pi }^{ * }\phi \left\lbrack  {f\left( {x, t}\right)  - f\left( {x,0}\right) }\right\rbrack  .
\]

Thus,

\[
\left( {1 - {\pi }^{ * }{s}^{ * }}\right) \omega  = {\left( -1\right) }^{q - 1}\left( {{dK} - {Kd}}\right) \omega .
\]

On forms of type (II),

\[
\omega  = \left( {{\pi }^{ * }\phi }\right) {fdt},\;\deg \omega  = q
\]

\[
{d\omega } = \left( {{\pi }^{ * }{d\phi }}\right) {fdt} + {\left( -1\right) }^{q - 1}\left( {{\pi }^{ * }\phi }\right) \frac{\partial f}{\partial x}{dxdt}
\]

\[
\left( {1 - {\pi }^{ * }{s}^{ * }}\right) \omega  = \omega \text{ because }{s}^{ * }\left( {dt}\right)  = d\left( {{s}^{ * }t}\right)  = d\left( 0\right)  = 0\text{ . }
\]

\[
{Kd\omega } = \left( {{\pi }^{ * }{d\phi }}\right) {\int }_{0}^{t}f + {\left( -1\right) }^{q - 1}\left( {{\pi }^{ * }\phi }\right) {dx}{\int }_{0}^{t}\frac{\partial f}{\partial x},
\]

\[
{dK\omega } = \left( {{\pi }^{ * }{d\phi }}\right) {\int }_{0}^{t}f + {\left( -1\right) }^{q - 1}\left( {{\pi }^{ * }\phi }\right) \left\lbrack  {{dx}\left( {{\int }_{0}^{t}\frac{\partial f}{\partial x}}\right)  + {fdt}}\right\rbrack  .
\]

Thus

\[
\left( {{dK} - {Kd}}\right) \omega  = {\left( -1\right) }^{q - 1}\omega .
\]

In either case,

\[
1 - {\pi }^{ * } \circ  {s}^{ * } = {\left( -1\right) }^{q - 1}\left( {{dK} - {Kd}}\right) \;\text{ on }\;{\Omega }^{q}\left( {{\mathbb{R}}^{n} \times  \mathbb{R}}\right) .
\]

This proves

Proposition 4.1. The maps \( {H}^{ * }\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right) \overset{{\pi }^{ * }}{\underset{{s}^{ * }}{ \leftrightarrows  }}{H}^{ * }\left( {\mathbb{R}}^{n}\right) \) are isomorphisms.

By induction, we obtain the cohomology of \( {\mathbb{R}}^{n} \) .

Corollary 4.1.1 (Poincaré Lemma).

\[
{H}^{ * }\left( {\mathbb{R}}^{n}\right)  = {H}^{ * }\left( \text{ point }\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimension }0 \\  0 & \text{ elsewhere. } \end{array}\right.
\]

Consider more generally

![bo_d7b6f8alb0pc73dd9avg_45_744_944_142_135_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_45_744_944_142_135_0.jpg)

If \( \left\{  {U}_{\alpha }\right\} \) is an atlas for \( M \) , then \( \left\{  {{U}_{\alpha } \times  {\mathbb{R}}^{1}}\right\} \) is an atlas for \( M \times  {\mathbb{R}}^{1} \) . Again every form on \( M \times  {\mathbb{R}}^{1} \) is a linear combination of the two types of forms (I) and (II). We can define the homotopy operator \( K \) as before and the proof carries over word for word to show that \( {H}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \simeq  {H}^{ * }\left( M\right) \) is an isomorphism via \( {\pi }^{ * } \) and \( {s}^{ * } \) .

Corollary 4.1.2 (Homotopy Axiom for de Rham Cohomology). Homotopic maps induce the same map in cohomology.

Proof. Recall that a homotopy between two maps \( f \) and \( g \) from \( M \) to \( N \) is a map \( F : M \times  {\mathbb{R}}^{1} \rightarrow  N \) such that

\[
\left\{  \begin{array}{lll} F\left( {x, t}\right)  = f\left( x\right) & \text{ for } & t \geq  1 \\  F\left( {x, t}\right)  = g\left( x\right) & \text{ for } & t \leq  0. \end{array}\right.
\]

Equivalently if \( {s}_{0} \) and \( {s}_{1} : M \rightarrow  M \times  {\mathbb{R}}^{1} \) are the 0-section and 1-section respectively, i.e., \( {s}_{1}\left( x\right)  = \left( {x,1}\right) \) , then

\[
f = F \circ  {s}_{1}
\]

\[
g = F \circ  {s}_{0}.
\]

Thus

\[
{f}^{ * } = {\left( F \circ  {s}_{1}\right) }^{ * } = {s}_{1}^{ * } \circ  {F}^{ * }
\]

\[
{g}^{ * } = {\left( F \circ  {s}_{0}\right) }^{ * } = {s}_{0}^{ * } \circ  {F}^{ * }
\]

Since \( {s}_{1}^{ * } \) and \( {s}_{0}^{ * } \) both invert \( {\pi }^{ * } \) , they are equal. Hence,

\[
{f}^{ * } = {g}^{ * }\text{ . }
\]

Two manifolds \( M \) and \( N \) are said to have the same homotopy type in the \( {C}^{\infty } \) sense if there are \( {C}^{\infty } \) maps \( f : M \rightarrow  N \) and \( g : N \rightarrow  M \) such that \( g \circ  f \) and \( f \circ  g \) are \( {C}^{\infty } \) homotopic to the identity on \( M \) and \( N \) respectively.* A manifold having the homotopy type of a point is said to be contractible.

Corollary 4.1.2.1. Two manifolds with the same homotopy type have the same de Rham cohomology.

If \( i : A \subset  M \) is the inclusion and \( r : M \rightarrow  A \) is a map which restricts to the identity on \( A \) , then \( r \) is called a retraction of \( M \) onto \( A \) . Equivalently, \( r \circ  i : A \rightarrow  A \) is the identity. If in addition \( i \circ  r : M \rightarrow  M \) is homotopic to the identity on \( M \) , then \( r \) is said to be a deformation retraction of \( M \) onto \( A \) . In this case \( A \) and \( M \) have the same homotopy type.

Corollary 4.1.2.2. If \( A \) is a deformation retract of \( M \) , then \( A \) and \( M \) have the same de Rham cohomology.

Exercise 4.2. Show that \( r : {\mathbb{R}}^{2} - \{ 0\}  \rightarrow  {S}^{1} \) given by \( r\left( x\right)  = x/\parallel x\parallel \) is a deformation retraction.

Exercise 4.3. The cohomology of the n-sphere \( {S}^{n} \) . Cover \( {S}^{n} \) by two open sets \( U \) and \( V \) where \( U \) is slightly larger than the northern hemisphere and \( V \) slightly larger than the southern hemisphere (Figure 4.1). Then \( U \cap  V \) is diffeomorphic to \( {S}^{n - 1} \times  {\mathbb{R}}^{1} \) where \( {S}^{n - 1} \) is the equator. Using the Mayer-Vietoris sequence, show that

\[
{H}^{ * }\left( {S}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimensions }0, n \\  0 & \text{ otherwise. } \end{array}\right.
\]

We saw previously that a generator of \( {H}^{1}\left( {S}^{1}\right) \) is a bump 1-form on \( {S}^{1} \) which gives the isomorphism \( {H}^{1}\left( {S}^{1}\right)  \simeq  {\mathbb{R}}^{1} \) under integration (see Figure

![bo_d7b6f8alb0pc73dd9avg_46_638_1571_387_359_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_46_638_1571_387_359_0.jpg)

Figure 4.1

* In fact two manifolds have the same homotopy type in the \( {C}^{\infty } \) sense if and only if they have the same homotopy type in the usual (continuous) sense. This is because every continuous map between two manifolds is continuously homotopic to a \( {C}^{\infty } \) map (see Proposition 17.8).

![bo_d7b6f8alb0pc73dd9avg_47_674_298_254_284_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_47_674_298_254_284_0.jpg)

Figure 4.2

4.2). This bump 1-form propagates by the boundary map of the Mayer-Vietoris sequence to a bump 2-form on \( {S}^{2} \) , which represents a generator of \( {H}^{2}\left( {S}^{2}\right) \) . In general a generator of \( {H}^{n}\left( {S}^{n}\right) \) can be taken to be a bump \( n \) -form on \( {S}^{n} \) .

Exercise 4.3.1 Volume form on a sphere. Let \( {S}^{n}\left( r\right) \) be the sphere of radius \( r \)

\[
{x}_{1}^{2} + \cdots  + {x}_{n + 1}^{2} = {r}^{2}
\]

in \( {\mathbb{R}}^{n + 1} \) , and let

\[
\omega  = \frac{1}{r}\mathop{\sum }\limits_{{i = 1}}^{{n + 1}}{\left( -1\right) }^{i - 1}{x}_{i}d{x}_{1}\cdots \widehat{d{x}_{i}}\cdots d{x}_{n + 1}.
\]

(a) Write \( {S}^{n} \) for the unit sphere \( {S}^{n}\left( 1\right) \) . Compute the integral \( {\int }_{{S}^{n}}\omega \) and conclude that \( \omega \) is not exact.

(b) Regarding \( r \) as a function on \( {\mathbb{R}}^{n + 1} - 0 \) , show that \( \left( {dr}\right)  \cdot  \omega  = d{x}_{1}\cdots \; d{x}_{n + 1} \) . Thus \( \omega \) is the Euclidean volume form on the sphere \( {S}^{n}\left( r\right) \) .

From (a) we obtain an explicit formula for the generator of the top cohomology of \( {S}^{n} \) (although not as a bump form). For example, the generator of \( {H}^{2}\left( {S}^{2}\right) \) is represented by

\[
\sigma  = \frac{1}{4\pi }\left( {{x}_{1}d{x}_{2}d{x}_{3} - {x}_{2}d{x}_{1}d{x}_{3} + {x}_{3}d{x}_{1}d{x}_{2}}\right) .
\]

## The Poincaré Lemma for Compactly Supported Cohomology

The computation of the compactly supported cohomology \( {H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right) \) is again by induction; we will show that there is an isomorphism

\[
{H}_{c}^{* + 1}\left( {{\mathbb{R}}^{n} \times  {\mathbb{R}}^{1}}\right)  \simeq  {H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right) .
\]

Note that here, unlike the previous case, the dimension is shifted by one.

More generally consider the projection \( \pi  : M \times  {\mathbb{R}}^{1} \rightarrow  M \) . Since the pullback of a form on \( M \) to a form on \( M \times  {\mathbb{R}}^{1} \) necessarily has noncompact support, the pullback map \( {\pi }^{ * } \) does not send \( {\Omega }_{c}^{ * }\left( M\right) \) to \( {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right) \) . However, there is a push-forward map \( {\pi }_{ * } : {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }_{c}^{* - 1}\left( M\right) \) , called integration along the fiber, defined as follows. First note that a compactly supported form on \( M \times  {\mathbb{R}}^{1} \) is a linear combination of two types of forms:

(I) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) \) , (II) \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) {dt} \) ,

where \( \phi \) is a form on the base (not necessarily with compact support), and \( f\left( {x, t}\right) \) is a function with compact support. We define \( {\pi }_{ * } \) by

\[
\text{ (I) }{\pi }^{ * }\phi  \cdot  f\left( {x, t}\right)  \mapsto  0\text{ , }
\]

(4.4)

\[
\text{ (II) }{\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) {dt} \mapsto  \phi {\int }_{-\infty }^{\infty }f\left( {x, t}\right) {dt}\text{ . }
\]

Exercise 4.5. Show that \( d{\pi }_{ * } = {\pi }_{ * }d \) ; in other words, \( {\pi }_{ * } : {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow \; {\Omega }_{c}^{* - 1}\left( M\right) \) is a chain map.

By this exercise \( {\pi }_{ * } \) induces a map in cohomology \( {\pi }_{ * } : {H}_{c}^{ * } \rightarrow  {H}_{c}^{* - 1} \) . To produce a map in the reverse direction, let \( e = e\left( t\right) {dt} \) be a compactly supported 1-form on \( {\mathbb{R}}^{1} \) with total integral 1 and define

\[
{e}_{ * } : {\Omega }_{c}^{ * }\left( M\right)  \rightarrow  {\Omega }_{c}^{* + 1}\left( {M \times  {\mathbb{R}}^{1}}\right)
\]

by

\[
\phi  \mapsto  \left( {{\pi }^{ * }\phi }\right)  \land  e
\]

The map \( {e}_{ * } \) clearly commutes with \( d \) , so it also induces a map in cohomology. It follows directly from the definition that \( {\pi }_{ * } \circ  {e}_{ * } = 1 \) on \( {\Omega }_{c}^{ * }\left( {\mathbb{R}}^{n}\right) \) . Although \( {e}_{ * } \circ  {\pi }_{ * } \neq  1 \) on the level of forms, we shall produce a homotopy operator \( K \) between 1 and \( {e}_{ * } \circ  {\pi }_{ * } \) ; it will then follow that \( {e}_{ * } \circ  {\pi }_{ * } = 1 \) in cohomology.

To streamline the notation, write \( \phi  \cdot  f \) for \( {\pi }^{ * }\phi  \cdot  f\left( {x, t}\right) \) and \( \int f \) for \( \int f\left( {x, t}\right) {dt} \) . The homotopy operator \( K : {\Omega }_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right)  \rightarrow  {\Omega }_{c}^{* - 1}\left( {M \times  {\mathbb{R}}^{1}}\right) \) is defined by

(I) \( \phi  \cdot  f \mapsto  0 \) ,

(II) \( \phi  \cdot  {fdt} \mapsto  \phi {\int }_{-\infty }^{t}f - {\phi A}\left( t\right) {\int }_{-\infty }^{\infty }f\; \) where \( A\left( t\right)  = {\int }_{-\infty }^{t}e \) .

Proposition 4.6. \( 1 - {e}_{ * }{\pi }_{ * } = {\left( -1\right) }^{q - 1}\left( {{dK} - {Kd}}\right) \) on \( {\Omega }_{c}^{q}\left( {M \times  {\mathbb{R}}^{1}}\right) \) .

Proof. On forms of type (I), assuming \( \deg \phi  = q \) , we have

\[
\left( {1 - {e}_{ * }{\pi }_{ * }}\right) \phi  \cdot  f = \phi  \cdot  f,
\]

\[
\left( {{dK} - {Kd}}\right) \phi  \cdot  f =  + K\left( {{d\phi } \cdot  f + {\left( -1\right) }^{q}\phi \frac{\partial f}{\partial x}{dx} + {\left( -1\right) }^{q}\phi \frac{\partial f}{\partial t}{dt}}\right)
\]

\[
= {\left( -1\right) }^{q - 1}\left( {\phi {\int }_{-\infty }^{t}\frac{\partial f}{\partial t} - {\phi A}\left( t\right) {\int }_{-\infty }^{\infty }\frac{\partial f}{\partial t}}\right)
\]

\[
= {\left( -1\right) }^{q - 1}{\phi f}.\;\left\lbrack  {\text{ Here }{\int }_{-\infty }^{\infty }\frac{\partial f}{\partial t} = f\left( {x,\infty }\right)  - f\left( {x, - \infty }\right)  = 0.}\right\rbrack
\]

So

\[
1 - {e}_{ * }{\pi }_{ * } = {\left( -1\right) }^{q - 1}\left( {{dK} - {Kd}}\right) .
\]

On forms of type (II), now assuming \( \deg \phi  = q - 1 \) , we have

\[
\left( {1 - {e}_{ * }{\pi }_{ * }}\right) {\phi fdt} = {\phi fdt} - \phi \left( {{\int }_{-\infty }^{\infty }f}\right)  \land  e
\]

\[
\left( {dK}\right) \left( {{\phi f} \curlywedge  {dt}}\right)  = \left( {d\phi }\right) {\int }_{-\infty }^{t}f + {\left( -1\right) }^{q - 1}\phi \left( {{\int }_{-\infty }^{t}\frac{\partial f}{\partial x}}\right) {dx} + {\left( -1\right) }^{q - 1}{\phi fdt}
\]

\[
- \left( {d\phi }\right) A\left( t\right) {\int }_{-\infty }^{\infty }f - {\left( -1\right) }^{q - 1}\phi \left\lbrack  {e{\int }_{-\infty }^{\infty }f + A\left( t\right) \left( {{\int }_{-\infty }^{\infty }\frac{\partial f}{\partial x}}\right) {dx}}\right\rbrack
\]

\[
\left( {Kd}\right) \left( {\phi fdt}\right)  = K\left( {\left( {d\phi }\right)  \cdot  {fdt} + {\left( -1\right) }^{q - 1}\phi \frac{\partial f}{\partial x}{dxdt}}\right)
\]

\[
= \left( {d\phi }\right) {\int }_{-\infty }^{t}f - \left( {d\phi }\right) A\left( t\right) {\int }_{-\infty }^{\infty }f
\]

\[
+ {\left( -1\right) }^{q - 1}\left\lbrack  {\phi \left( {{\int }_{-\infty }^{t}\frac{\partial f}{\partial x}}\right) {dx} - {\phi A}\left( t\right) \left( {{\int }_{-\infty }^{\infty }\frac{\partial f}{\partial x}}\right) {dx}}\right\rbrack  .
\]

So

\[
\left( {{dK} - {Kd}}\right) {\phi fdt} = {\left( -1\right) }^{q - 1}\left\lbrack  {{\phi fdt} - \phi \left( {{\int }_{-\infty }^{\infty }f}\right) e}\right\rbrack
\]

and the formula again holds.

This concludes the proof of the following

Proposition 4.7. The maps

\[
{H}_{c}^{ * }\left( {M \times  {\mathbb{R}}^{1}}\right) \underset{{e}_{ * }}{\overset{{\pi }_{ * }}{ \rightleftarrows  }}{H}_{c}^{* - 1}\left( M\right)
\]

are isomorphisms.

Corollary 4.7.1 (Poincaré Lemma for Compact Supports).

\[
{H}_{c}^{ * }\left( {\mathbb{R}}^{n}\right)  = \left\{  \begin{array}{ll} \mathbb{R} & \text{ in dimension }n \\  0 & \text{ otherwise. } \end{array}\right.
\]

Here the isomorphism \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right)  \simeq  \mathbb{R} \) is given by iterated \( {\pi }_{ * } \) , i.e., by integration over \( {\mathbb{R}}^{n} \) .

To determine a generator for \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) , we start with the constant function 1 on a point and iterate with \( {e}_{ * } \) . This gives \( e\left( {x}_{1}\right) d{x}_{1}e\left( {x}_{2}\right) d{x}_{2}\ldots e\left( {x}_{n}\right) d{x}_{n} \) . So a generator for \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) is a bump \( n \) -form \( \alpha \left( x\right) d{x}_{1}\ldots d{x}_{n} \) with

\[
{\int }_{{\mathbb{R}}^{n}}\alpha \left( x\right) d{x}_{1}\ldots d{x}_{n} = 1
\]

The support of \( \alpha \) can be made as small as we like.

REMARK. This Poincaré lemma shows that the compactly supported cohomology is not invariant under homotopy equivalence, although it is of course invariant under diffeomorphisms.

Exercise 4.8. Compute the cohomology groups \( {H}^{ * }\left( M\right) \) and \( {H}_{c}^{ * }\left( M\right) \) of the open Möbius strip \( M \) , i.e., the Möbius strip without the bounding edge (Figure 4.3). [Hint: Apply the Mayer-Vietoris sequences.]

## The Degree of a Proper Map

As an application of the Poincaré lemma for compact supports we introduce here a \( {C}^{\infty } \) invariant of a proper map between two Euclidean spaces of the same dimension. Later, after Poincaré duality, this will be generalized to a proper map between any two oriented manifolds; for compact manifolds the properness assumption is of course redundant.

Let \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) be a proper map. Then the pullback \( {f}^{ * } : {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right)  \rightarrow \; {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) is defined. It carries a generator of \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) , i.e., a compactly supported closed form with total integral one, to some multiple of the generator. This multiple is defined to be the degree of \( f \) . If \( \alpha \) is a generator of \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) , then

\[
\deg f = {\int }_{{\mathbb{R}}^{n}}{f}^{ * }\alpha .
\]

A priori the degree of a proper map is a real number; surprisingly, it turns out to be an integer. To see this, we need Sard's theorem. Recall that a critical point of a smooth map \( f : {\mathbb{R}}^{m} \rightarrow  {\mathbb{R}}^{m} \) is a point \( p \) where the differential \( {\left( {f}_{ * }\right) }_{p} : {T}_{p}{\mathbb{R}}^{n} \rightarrow  {T}_{f\left( p\right) }{\mathbb{R}}^{n} \) is not surjective, and a critical value is the image of a critical point. A point of \( {\mathbb{R}}^{n} \) which is not a critical value is called a regular value. According to this definition any point of \( {\mathbb{R}}^{n} \) which is not in the image of \( f \) is a regular value so that the inverse image of a regular value may be empty.

![bo_d7b6f8alb0pc73dd9avg_50_280_1843_1114_247_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_50_280_1843_1114_247_0.jpg)

Figure 4.3

Theorem 4.9 (Sard’s Theorem for \( {\mathbb{R}}^{n} \) ). The set of critical values of a smooth map \( f : {\mathbb{R}}^{m} \rightarrow  {\mathbb{R}}^{n} \) has measure zero in \( {\mathbb{R}}^{n} \) for any integers \( m \) and \( n \) .

This means that given any \( \varepsilon  > 0 \) , the set of critical values can be covered by cubes with total volume less than \( \varepsilon \) . Important special cases of this theorem were first published by A. P. Morse [1]. Sard's proof of the general case may be found in Sard [1].

Proposition 4.10 Let \( f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n} \) be a proper map. If \( f \) is not surjective, then it has degree 0 .

Proof. Since the image of a proper map is closed (why?), if \( f \) misses a point \( q \) , it must miss some neighborhood \( U \) of \( q \) . Choose a bump \( n \) -form \( \alpha \) whose support lies in \( U \) . Then \( {f}^{ * }\alpha  \equiv  0 \) so that \( \deg f = 0 \) .

Exercise 4.10.1. Prove that the image of a proper map is closed.

So to show that the degree is an integer we only need to look at surjective proper maps from \( {\mathbb{R}}^{n} \) to \( {\mathbb{R}}^{n} \) . By Sard’s theorem, almost all points in the image of such a map are regular values. Pick one regular value, say \( q \) . By hypothesis the inverse image of \( q \) is nonempty. Since in our case the two Euclidean spaces have the same dimension, the differential \( {f}_{ * } \) is surjective if and only if it is an isomorphism. So by the inverse function theorem, around any point in the pre-image of \( q, f \) is a local diffeomorphism. It follows that \( {f}^{-1}\left( q\right) \) is a discrete set of points. Since \( f \) is proper, \( {f}^{-1}\left( q\right) \) is in fact a finite set of points. Choose a generator \( \alpha \) of \( {H}_{c}^{n}\left( {\mathbb{R}}^{n}\right) \) whose support is localized near \( q \) . Then \( {f}^{ * }\alpha \) is an \( n \) -form whose support is localized near the points of \( {f}^{-1}\left( q\right) \) (see Figure 4.4). As noted earlier, a diffeomorphism preserves an integral only up to sign, so the integral of \( {f}^{ * }\alpha \) near each point of \( {f}^{-1}\left( q\right) \) is \( \pm  1 \) . Thus

\[
{\int }_{{\mathbb{R}}^{n}}{f}^{ * }\alpha  = \mathop{\sum }\limits_{{f - 1\left( q\right) }} \pm  1
\]

This proves that the degree of a proper map between two Euclidean spaces of the same dimension is an integer. More precisely, it shows that the number of points, counted with multiplicity \( \pm  1 \) , in the inverse image of any regular value is the same for all regular values and that this number is equal to the degree of the map.

![bo_d7b6f8alb0pc73dd9avg_51_343_1752_935_343_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_51_343_1752_935_343_0.jpg)

Figure 4.4

Sard's theorem for \( {\mathbb{R}}^{n} \) , a key ingredient of this discussion, has a natural extension to manifolds. We take this opportunity to state Sard's theorem in general. A subset \( S \) of a manifold \( M \) is said to have measure zero if it can be covered by countably many coordinate open sets \( {U}_{i} \) such that \( {\phi }_{i}\left( {S \cap  {U}_{i}}\right) \) has measure zero in \( {\mathbb{R}}^{n} \) ; here \( {\phi }_{i} \) is the trivialization on \( {U}_{i} \) . A critical point of a smooth map \( f : M \rightarrow  N \) between two manifolds is a point \( p \) in \( M \) where the differential \( {\left( {f}_{ * }\right) }_{p} : {T}_{p}M \rightarrow  {T}_{f\left( p\right) }N \) is not surjective, and a critical value is the image of a critical point.

Theorem 4.11 (Sard's Theorem). The set of critical values of a smooth map \( f : M \rightarrow  N \) has measure zero.

Exercise 4.11.1. Prove Theorem 4.11 from Sard’s theorem for \( {\mathbb{R}}^{n} \) .
