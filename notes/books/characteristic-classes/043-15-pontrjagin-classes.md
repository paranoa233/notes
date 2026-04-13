# 15 Pontrjagin Classes

To obtain further information about real vector bundles we will need the following construction. Let \( V \) be a real vector space. Then the tensor product \( V \otimes  \mathbb{C} = V{ \otimes  }_{\mathbb{R}}\mathbb{C} \) of \( V \) with the complex numbers is a complex vector space called the complexification of \( V \) . Applying this construction to each fiber \( F \) of the real \( n \) -plane bundle \( \xi \) we obtain a complex \( n \) -plane bundle with typical fiber \( F \otimes  \mathbb{C} \) over the same base space. We denote this new bundle by \( \xi  \otimes  \mathbb{C} \) and call it the complexification of the real vector bundle \( \xi \) .

Note that every element in the complex vector space \( F \otimes  \mathbb{C} \) can be written uniquely as a sum \( x + {iy} \) with \( x, y \in  F \) . Using this real direct sum decomposition

\[
F \otimes  \mathbb{C} = F \oplus  {iF}
\]

it follows that the underlying real vector bundle \( {\left( \xi  \otimes  \mathbb{C}\right) }_{\mathbb{R}} \) is canonically isomorphic to the Whitney sum \( \xi  \oplus  \xi \) . Evidently the given complex structure on \( \xi  \otimes  \mathbb{C} \) corresponds to the complex structure

\[
\mathbf{J}\left( {x, y}\right)  = \left( {-y, x}\right)
\]

on this Whitney sum \( \xi  \oplus  \xi \) .

Lemma 15.1. The complexification \( \xi  \otimes  \mathbb{C} \) of a real vector bundle is always isomorphic to its own conjugate bundle \( \overline{\xi  \otimes  \mathbb{C}} \) .

For the correspondence \( f : x + {iy} \mapsto  x - {iy} \) , maps the total space \( E\left( {\xi  \otimes  \mathbb{C}}\right) \) homeomorphically onto itself, and is \( \mathbb{R} \) -linear in each fiber with

\[
f\left( {i\left( {x + {iy}}\right) }\right)  =  - {if}\left( {x + {iy}}\right) .
\]

Now consider the total Chern class

\[
\mathrm{c}\left( {\xi  \otimes  \mathbb{C}}\right)  = 1 + {\mathrm{c}}_{1}\left( {\xi  \otimes  \mathbb{C}}\right)  + {\mathrm{c}}_{2}\left( {\xi  \otimes  \mathbb{C}}\right)  + \cdots  + {\mathrm{c}}_{n}\left( {\xi  \otimes  \mathbb{C}}\right)
\]

of this compleixfied \( n \) -plane bundle. Setting this equal to

\[
\mathrm{c}\left( \overline{\xi  \otimes  \mathbb{C}}\right)  = 1 - {\mathrm{c}}_{1}\left( {\xi  \otimes  \mathbb{C}}\right)  + {\mathrm{c}}_{2}\left( {\xi  \otimes  \mathbb{C}}\right)  - \cdots  \pm  {\mathrm{c}}_{n}\left( {\xi  \otimes  \mathbb{C}}\right)
\]

by 14.9, we see that the odd Chern classes

\[
{\mathrm{c}}_{1}\left( {\xi  \otimes  \mathbb{C}}\right) ,{\mathrm{c}}_{3}\left( {\xi  \otimes  \mathbb{C}}\right) ,\cdots
\]

are all elements of order 2. (Compare Problem 15-D.)

Definition. Ignoring these elements of order 2, the \( i \) -th Pontrjagin class

\[
{\mathrm{p}}_{i}\left( \xi \right)  \in  {\mathrm{H}}^{4i}\left( {B;\mathbb{Z}}\right)
\]

is defined to be the integral cohomology class \( {\left( -1\right) }^{i}{\mathrm{c}}_{2i}\left( {\xi  \otimes  \mathbb{C}}\right) \) . The sign \( {\left( -1\right) }^{i} \) is introduced here so as to avoid a sign in later formulas (Corollary 15.8, Example 15.6). Evidently \( {\mathrm{p}}_{i}\left( \xi \right) \) is zero for \( i > n/2 \) . The total Pontrjagin class is defined to be the unit

\[
\mathrm{p}\left( {xi}\right)  = 1 + {\mathrm{p}}_{1}\left( \xi \right)  + \cdots  + {\mathrm{p}}_{\lfloor n/2\rfloor }\left( \xi \right)
\]

in the ring \( {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Z}}\right) \) . Here \( \lfloor n/2\rfloor \) denotes the largest integer less than or equal to \( n/2 \) .

Lemma 15.2. Pontrjagin classes are natural with respect to bundle maps. Furthermore, if \( {\varepsilon }^{k} \) is a trivial \( k \) -plane bundle, then \( \mathrm{p}\left( {\xi  \oplus  {\varepsilon }^{k}}\right)  = \mathrm{p}\left( \varepsilon \right) \) .

Proof. This follows immediately from 14.2 and 14.3.

In analogy with the other characteristic classes we have studied, we would like the Pontrjagin classes to satisfy a product formula. There is some difficulty however, since the odd Chern classes of \( \xi  \otimes  \mathbb{C} \) have been thrown away, so the best we can do is the following.

Theorem 15.3. The total Pontrjagin class \( \mathrm{p}\left( {\xi  \oplus  \eta }\right) \) of a Whitney sum is congruent to \( \mathrm{p}\left( \xi \right) \mathrm{p}\left( \eta \right) \) modulo elements of order 2 . In otherwords

\[
2\left( {\mathrm{p}\left( {\xi  \oplus  \eta }\right)  - \mathrm{p}\left( \xi \right) \mathrm{p}\left( \eta \right) }\right)  = 0.
\]

Proof. Since \( \left( {\xi  \oplus  \eta }\right)  \otimes  \mathbb{C} \) is clearly isomorphic to \( \left( {\xi  \otimes  \mathbb{C}}\right)  \oplus  \left( {\eta  \otimes  \mathbb{C}}\right) \) we have

\[
{\mathrm{c}}_{k}\left( {\left( {\xi  \oplus  \eta }\right)  \otimes  \mathbb{C}}\right)  = \mathop{\sum }\limits_{{i + j = k}}{\mathrm{c}}_{i}\left( {\xi  \otimes  \mathbb{C}}\right) {\mathrm{c}}_{j}\left( {\eta  \otimes  \mathbb{C}}\right) .
\]

Ignoring the odd Chern classes, which are all elements of order 2, it follows that

\[
{\mathrm{c}}_{2k}\left( {\left( {\xi  \oplus  \eta }\right)  \otimes  \mathbb{C}}\right)  = \mathop{\sum }\limits_{{i + j = k}}{\mathrm{c}}_{2i}\left( {\xi  \otimes  \mathbb{C}}\right) {\mathrm{c}}_{2j}\left( {\eta  \otimes  \mathbb{C}}\right)
\]

modulo elements of order 2. Multiplying both sides of this congruence by \( {\left( -1\right) }^{k} = {\left( -1\right) }^{i}{\left( -1\right) }^{j} \) , it follows that

\[
{\mathrm{p}}_{k}\left( {\xi  \oplus  \eta }\right)  = \mathop{\sum }\limits_{{i + j = k}}{\mathrm{p}}_{i}\left( \xi \right) {\mathrm{p}}_{j}\left( \eta \right) ,
\]

as required.

Example 3. For the tangent bundle \( {\tau }^{n} \) of the \( n \) -sphere, since the Whitney sum \( {\tau }^{n} \oplus  {\nu }^{1} \cong  {\tau }^{n} \oplus  {\varepsilon }^{1} \) is trivial, it follows by 15.2 that the total Pontrjagin class \( \mathrm{p}\left( {\tau }^{n}\right) \) is equal to 1 .

Thus the Pontrjagin classes of the tangent bundle of a sphere are uninteresting. To obtain some interesting examples we will look at the complex projective spaces. But first we must develop a further relationship betwen Pontrjagin classes and Chern classes.

At this point, we have a situation which can be represented schematically by Figure 11.

Starting with the real \( n \) -plane bundle \( \xi \) , we can first form the induced complex \( n \) -plane bundle \( \xi  \otimes  \mathbb{C} \) . Then, forgetting the complex structure, we obtain the underlying real \( {2n} \) -plane bundle \( {\left( \xi  \otimes  \mathbb{C}\right) }_{\mathbb{R}} \) with a canonical preferred orientation. Finally, forgetting the orientation, this resulting real \( {2n} \) -plane bundle can be identified simply with the Whitney sum \( \xi  \oplus  \xi \) .

![bo_d7du9galb0pc73deir9g_181_599_386_512_500_0.jpg](images/bo_d7du9galb0pc73deir9g_181_599_386_512_500_0.jpg)

Figure 11

However, instead of starting at the top of the circle (i.e., with a real vector bundle), we can equally well start somewhere else on the circle. After circumnavigating the circle we will then obtain a new bundle of the same type (complex or oriented) as the bundle we started with, but with twice the dimension of the original bundle. Suppose for example that we start with a complex vector bundle.

Lemma 15.4. For any complex vector bundle \( \omega \) , the complexification \( {\omega }_{\mathbb{R}} \otimes  \mathbb{C} \) of the underlying real vector bundle is canonically isomorphic to the Whitney sum \( \omega  \oplus  \overline{\omega } \) .

Proof. For any real vector space \( V \) , recall that \( V \otimes  \mathbb{C} \) can be identified with the direct sum \( V \oplus  V \) , made into a complex vector space by means of the complex structure \( \mathbf{J}\left( {x, y}\right)  = \left( {-y, x}\right) \) .

Now suppose that \( V = {F}_{\mathbb{R}} \) where \( F \) is the typical fiber of a complex vector bundle. Then it is easy to verify that the correspondence

\[
g : x \mapsto  \left( {x, - {ix}}\right)
\]

from \( F \) to \( V \oplus  V \) is complex lienar, that is \( g\left( {ix}\right)  = \mathbf{J}\left( {g\left( x\right) }\right) \) . Similarly the correspondence from \( F \) to \( V \oplus  V \) is conjugate linear. Since every point \( \left( {x, y}\right) \) of \( V \oplus  V \cong  {F}_{\mathbb{R}} \otimes  \mathbb{C} \) can be written uniquely as the sum

\[
g\left( \frac{x + {iy}}{2}\right)  + h\left( \frac{x - {iy}}{2}\right)
\]

of an elemnt in \( g\left( F\right) \) and an element in \( h\left( F\right) \) , it follows that \( {F}_{\mathbb{R}} \otimes  \mathbb{C} \) is canonically isomorphic, as complex vector space to \( F \oplus  \bar{F} \) . This is true for each fiber \( F \) of \( \omega \) , so combining all of these isomorphisms it follows that \( {\omega }_{\mathbb{R}} \otimes  \mathbb{C} \cong  \omega  \oplus  \overline{\omega } \) as asserted.

Corollary 15.5. For any complex \( n \) -plane bundle \( \omega \) , the Chern classes \( {\mathrm{c}}_{i}\left( \omega \right) \) determine the Pontrjagin classes \( {\mathrm{p}}_{k}\left( {\omega }_{\mathbb{R}}\right) \) by the formula

\[
1 - {\mathrm{p}}_{1} + {\mathrm{p}}_{2} - \cdots  \pm  {\mathrm{p}}_{n} = \left( {1 - {\mathrm{c}}_{1} + {\mathrm{c}}_{2} - \cdots  \pm  {\mathrm{c}}_{n}}\right) \left( {1 + {\mathrm{c}}_{1} + {\mathrm{c}}_{2} + \cdots  + {\mathrm{c}}_{n}}\right)
\]

Thus \( {\mathrm{p}}_{k}\left( {\omega }_{\mathbb{R}}\right) \) is equal to

\[
{\mathrm{c}}_{k}{\left( \omega \right) }^{2} - 2{\mathrm{c}}_{k - 1}\left( \omega \right) {\mathrm{c}}_{k + 1}\left( \omega \right)  + \cdots  \pm  2{\mathrm{c}}_{1}\left( \omega \right) {\mathrm{c}}_{{2k} - 1}\left( \omega \right)  \mp  2{\mathrm{c}}_{2k}\left( \omega \right)
\]

Proof. This follows immediately, making use of 14.7 and Lemma 14.9.

Examples 15.6. Let \( \tau \) be the tangent bundle of the complex projective space \( {\mathbb{P}}^{n}\left( \mathbb{C}\right) \) . Since the total Chern class \( \mathrm{c}\left( \tau \right) \) equals \( {\left( 1 + a\right) }^{n + 1} \) by Theorem 14.10, it follows that the Pontrjagin classes \( {\mathrm{p}}_{k}\left( {\tau }_{\mathbb{R}}\right) \) are given by

\[
\left( {1 - {\mathrm{p}}_{1} + \cdots  \pm  {\mathrm{p}}_{n}}\right)  = \left( {1 - {\mathrm{c}}_{1} + \cdots  \pm  {\mathrm{c}}_{n}}\right) \left( {1 + {\mathrm{c}}_{1} + \cdots  + {\mathrm{c}}_{n}}\right)
\]

\[
= {\left( 1 - a\right) }^{n + 1}{\left( 1 + a\right) }^{n + 1} = {\left( 1 - {a}^{2}\right) }^{n + 1}.
\]

Therefore the total Pontrjagin class \( 1 + {\mathrm{p}}_{1} + \cdots  + {\mathrm{p}}_{n} \) is equal to \( {\left( 1 + {a}^{2}\right) }^{n + 1} \) . In other words

\[
{\mathrm{p}}_{k}\left( {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right)  = \left( \begin{matrix} n + 1 \\  k \end{matrix}\right) {a}^{2k}
\]

for \( 1 \leq  k \leq  n/2 \) , where the higher Pontrjagin classes are zero since \( {\mathrm{H}}^{4k}\left( {{\mathbb{P}}^{n}\left( \mathbb{C}\right) }\right) \) for \( k > n/2 \) . Here we are using the abbreviation \( {\mathrm{p}}_{k}\left( M\right) \) for the tangential Pontrjagin class \( {\mathrm{p}}_{k}\left( {\tau {\left( M\right) }_{\mathbb{R}}}\right) \) of a complex manifold \( M \) . Thus

\[
\mathrm{p}\left( {{\mathbb{P}}^{1}\left( \mathbb{C}\right) }\right)  = 1
\]

\[
\mathrm{p}\left( {{\mathbb{P}}^{2}\left( \mathbb{C}\right) }\right)  = 1 + 3{a}^{2}
\]

\[
\mathrm{p}\left( {{\mathbb{P}}^{3}\left( \mathbb{C}\right) }\right)  = 1 + 4{a}^{2}
\]

\[
\mathrm{p}\left( {{\mathbb{P}}^{4}\left( \mathbb{C}\right) }\right)  = 1 + 5{a}^{2} + {10}{a}^{4}
\]

\[
\mathrm{p}\left( {{\mathbb{P}}^{5}\left( \mathbb{C}\right) }\right)  = 1 + 6{a}^{2} + {15}{a}^{4}
\]

\[
\mathrm{p}\left( {{\mathbb{P}}^{6}\left( \mathbb{C}\right) }\right)  = 1 + 7{a}^{2} + {21}{a}^{4} + {35}{a}^{6},
\]

and so on. From these examples we see that Pontrjagin classes can well be nonzero.

Now suppose we start with an oriented \( n \) -plane bundle \( \xi \) . Complexifying and then passing to the underlying real vector bundle, we obtain a \( {2n} \) -plane bundle \( {\left( \xi  \otimes  \mathbb{C}\right) }_{\mathbb{R}} \) with a preferred orientation by 14.1.

Lemma 15.7. The real \( {2n} \) -plane bundle \( {\left( \xi  \otimes  \mathbb{C}\right) }_{\mathbb{R}} \) is isomorphic to \( \xi  \oplus  \xi \) under an isomorphism which either preserves or reverses orientation according as \( n\left( {n - 1}\right) /2 \) is even or odd.

Proof. Let \( {v}_{1},\cdots ,{v}_{n} \) be an ordered basis for a typical fiber \( F \) of \( \xi \) . Then the vectors \( {v}_{1}, i{v}_{1},\cdots ,{v}_{n}, i{v}_{n} \) form an ordered basis determining the preferred orientation for \( {\left( F \otimes  \mathbb{C}\right) }_{\mathbb{R}} \) . Identifying this with the real direct sum \( F \oplus  {iF} \cong  F \oplus  F \) , the basis \( {v}_{1},\cdots ,{v}_{n} \) for \( F \) followed by the basis \( i{v}_{1},\cdots , i{v}_{n} \) for \( {iF} \) gives a different ordered basis. Evidently the permutation which transforms one ordered basis to the other has sign \( {\left( -1\right) }^{\left( {n - 1}\right)  + \left( {n - 2}\right)  + \cdots  + 1} = {\left( -1\right) }^{n\left( {n - 1}\right) /2} \) .

Corollary 15.8. If \( \xi \) is an oriented \( {2k} \) -plane bundle, then the Pontrjagin class \( {\mathrm{p}}_{k}\left( \xi \right) \) is equal to the square of the Euler class \( \mathrm{e}\left( \xi \right) \) .

For by definition \( {\mathrm{p}}_{k}\left( \xi \right) \) is equal to the \( {\left( -1\right) }^{k}{\mathrm{c}}_{2k}\left( {\xi  \otimes  \mathbb{C}}\right)  = {\left(  = 1\right) }^{k}\mathrm{e}\left( {\left( \xi  \otimes  \mathbb{C}\right) }_{\mathbb{R}}\right) \) . But, according to Lemma 15.7 and Property 9.6, the Euler class \( \mathrm{e}\left( {\left( \xi  \otimes  \mathbb{C}\right) }_{\mathbb{R}}\right) \) is equal to \( \mathrm{e}\left( {\xi  \oplus  \xi }\right)  = \mathrm{e}{\left( \xi \right) }^{2} \) multiplied by the sign \( {\left( -1\right) }^{{2k}\left( {{2k} - 1}\right) /2} = {\left( -1\right) }^{k} \) .
