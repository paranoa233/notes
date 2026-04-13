# 4.1 Consequences of the Four Axioms

As immediate consequences of Axiom 2 one has the following.

Proposition 1. If \( \xi \) is isomorphic to \( \eta \) then \( {\mathrm{w}}_{i}\left( \xi \right)  = {\mathrm{w}}_{i}\left( \eta \right) \) .

Proposition 2. If \( \varepsilon \) is a trivial vector bundle then \( {\mathrm{w}}_{i}\left( \varepsilon \right)  = 0 \) for \( i > 0 \) .

For if \( \varepsilon \) is trivial then there exists a bundle map from \( \varepsilon \) to a vector bundle over a point.

Combining this information with the Whitney product theorem, one obtains:

Proposition 3. If \( \varepsilon \) is trivial, then \( {\mathrm{w}}_{i}\left( {\varepsilon  \oplus  \eta }\right)  = {\mathrm{w}}_{i}\left( \eta \right) \) .

Proposition 4. If \( \xi \) is an \( {\mathbb{R}}^{n} \) -bundle with a Euclidean metric which possesses a nowhere zero cross-section, then \( {\mathrm{w}}_{n}\left( \xi \right)  = 0 \) . If \( \xi \) possesses \( k \) cross-sections which are nowhere linearly dependent, then

\[
{\mathrm{w}}_{n - k + 1}\left( \xi \right)  = {\mathrm{w}}_{n - k + 2}\left( \xi \right)  = \cdots  = {\mathrm{w}}_{n}\left( \xi \right)  = 0.
\]

For it follows from Theorem 3.3 that \( \xi \) splits as a Whitney sum \( \varepsilon  \oplus  {\varepsilon }^{ \bot  } \) where \( \varepsilon \) is trivial and \( {\varepsilon }^{ \bot  } \) has dimension \( n - k \) .

A particularly interesting case of the Whitney product theorem occurs when the Whitney sum \( \xi  \oplus  \eta \) is trivial. Then the relations

\[
{\mathrm{w}}_{1}\left( \xi \right)  + {\mathrm{w}}_{1}\left( \eta \right)  = 0
\]

\[
{\mathrm{w}}_{2}\left( \xi \right)  + {\mathrm{w}}_{1}\left( \xi \right) {\mathrm{w}}_{1}\left( \eta \right)  + {\mathrm{w}}_{2}\left( \eta \right)  = 0
\]

\[
{\mathrm{w}}_{3}\left( \xi \right)  + {\mathrm{w}}_{2}\left( \xi \right) {\mathrm{w}}_{1}\left( \eta \right)  + {\mathrm{w}}_{1}\left( \xi \right) {\mathrm{w}}_{2}\left( \eta \right)  + {\mathrm{w}}_{3}\left( \eta \right)  = 0,\text{ etc., }
\]

can be solved inductively, so that \( {\mathrm{w}}_{i}\left( \eta \right) \) is expressed as a polynomial in the Stiefel-Whitney classes of \( \xi \) . It is convenient to introduce the following formalism.

Definition. \( {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Z}/2}\right) \) will denote the ring consisting of all formal infinite series

\[
a = {a}_{0} + {a}_{1} + {a}_{2} + \cdots
\]

with \( {a}_{i} \in  {\mathrm{H}}^{i}\left( {B;\mathbb{Z}/2}\right) \) . The product operation in this ring is to be given by the formula

\[
\left( {{a}_{0} + {a}_{1} + {a}_{2} + \cdots }\right) \left( {{b}_{0} + {b}_{1} + {b}_{2} + \cdots }\right)
\]

\[
= \left( {{a}_{0}{b}_{0}}\right)  + \left( {{a}_{1}{b}_{0} + {a}_{0}{b}_{1}}\right)  + \left( {{a}_{2}{b}_{0} + {a}_{1}{b}_{1} + {a}_{0}{b}_{2}}\right)  + \cdots .
\]

This product is commutative (since we are working modulo 2) and associative. Additively, \( {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Z}/2}\right) \) is to be simply the Cartesian product of the groups \( {\mathrm{H}}^{i}\left( {B;\mathbb{Z}/2}\right) \) .

The total Stiefel-Whitney class of an \( n \) -plane bundle \( \xi \) over \( B \) is defined to be the element

\[
\mathrm{w}\left( \xi \right)  = 1 + {\mathrm{w}}_{1}\left( \xi \right)  + {\mathrm{w}}_{2}\left( \xi \right)  + \cdots  + {\mathrm{w}}_{n}\left( \xi \right)  + 0 + \cdots
\]

of this ring. Note that the Whitney product theorem can now be expressed by the simple formula

\[
\mathrm{w}\left( {\xi  \oplus  \eta }\right)  = \mathrm{w}\left( \xi \right) \mathrm{w}\left( \eta \right) .
\]

Lemma 4.1. The collection of all infinite series

\[
\mathrm{w} = 1 + {\mathrm{w}}_{1} + {\mathrm{w}}_{2} + \cdots \; \in  {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Z}/2}\right)
\]

with leading term 1 forms a commutative group under multiplication.

(This is precisely the group of units of the ring \( {\mathrm{H}}^{\Pi }\left( {B;\mathbb{Z}/2}\right) \) .)

Proof. The inverse

\[
\overline{\mathrm{w}} = 1 + {\overline{\mathrm{w}}}_{1} + {\overline{\mathrm{w}}}_{2} + {\overline{\mathrm{w}}}_{3} + \cdots
\]

of a given element \( w \) can be constructed inductively by the algorithm

\[
{\overline{\mathrm{w}}}_{n} = {\mathrm{w}}_{1}{\overline{\mathrm{w}}}_{n - 1} + {\mathrm{w}}_{2}{\overline{\mathrm{w}}}_{n - 2} + \cdots  + {\mathrm{w}}_{n - 1}{\overline{\mathrm{w}}}_{1} + {\mathrm{w}}_{n}.
\]

Thus one obtains:

\[
{\overline{\mathrm{w}}}_{1} = {\mathrm{w}}_{1}
\]

\[
{\overline{\mathrm{w}}}_{2} = {\mathrm{w}}_{1}^{2} + {\mathrm{w}}_{2}
\]

\[
{\overline{\mathrm{w}}}_{3} = {\mathrm{w}}_{1}^{3} + {\mathrm{w}}_{3}
\]

\[
{\overline{\mathrm{w}}}_{4} = {\mathrm{w}}_{1}^{4} + {\mathrm{w}}_{1}^{2}{\mathrm{w}}_{2} + {\mathrm{w}}_{2}^{2} + {\mathrm{w}}_{4},
\]

and so on. This completes the proof.

Alternatively \( \overline{\mathrm{w}} \) can be computed by the power series expansion:

\[
\overline{\mathrm{w}} = {\left\lbrack  1 + \left( {\mathrm{w}}_{1} + {\mathrm{w}}_{2} + {\mathrm{w}}_{3} + \cdots \right) \right\rbrack  }^{-1}
\]

\[
= 1 - \left( {{\mathrm{w}}_{1} + {\mathrm{w}}_{2} + {\mathrm{w}}_{3} + \cdots }\right)  + {\left( {\mathrm{w}}_{1} + {\mathrm{w}}_{2} + \cdots \right) }^{2} - {\left( {\mathrm{w}}_{1} + {\mathrm{w}}_{2} + \cdots \right) }^{3} + \cdots
\]

\[
= 1 - {\mathrm{w}}_{1} + \left( {{\mathrm{w}}_{1}^{2} - {\mathrm{w}}_{2}}\right)  + \left( {-{\mathrm{w}}_{1}^{3} + 2{\mathrm{w}}_{1}{\mathrm{w}}_{2} - {\mathrm{w}}_{3}}\right)  + \cdots
\]

(where the signs are of course irrelevant). This leads to the precise expression \( \left( {{i}_{1} + \cdots  + {i}_{k}}\right) !/{i}_{1}!\cdots {i}_{k}! \) for the coefficient of \( {\mathrm{w}}_{1}^{{i}_{1}}{\mathrm{w}}_{2}^{{i}_{2}}\cdots {\mathrm{w}}_{k}^{{i}_{k}} \) in \( \overline{\mathrm{w}} \) .

Now consider two vector bundles \( \xi \) and \( \eta \) over the same base space. It follows from Proposition 1 that the equation

\[
\mathrm{w}\left( {\xi  \oplus  \eta }\right)  = \mathrm{w}\left( \xi \right) \mathrm{w}\left( \eta \right)
\]

can be uniquely solved as

\[
\mathrm{w}\left( \eta \right)  = \overline{\mathrm{w}}\left( \xi \right) \mathrm{w}\left( {\xi  \oplus  \eta }\right) .
\]

In particular, if \( \xi  \oplus  \eta \) is trivial, then

\[
\mathrm{w}\left( \eta \right)  = \overline{\mathrm{w}}\left( \xi \right) .
\]

One important special case is the following.

Lemma 4.2 (Whitney duality theorem). If \( {\tau }_{M} \) is the tangent bundle of a manifold in Euclidean space and \( \nu \) is the normal bundle then

\[
{\mathrm{w}}_{i}\left( \nu \right)  = {\overline{\mathrm{w}}}_{i}\left( {\tau }_{M}\right) .
\]

Now let us compute the Stiefel-Whitney classes in some special cases. It will frequently be convenient to use the abbreviation \( \mathrm{w}\left( M\right) \) for the total Stiefel-Whitney class of a tangent bundle \( {\tau }_{M} \) .

Example 6. For the tangent bundle \( \tau \) of the unit sphere \( {S}^{n} \) , the class \( \mathrm{w}\left( \tau \right)  = \mathrm{w}\left( {S}^{n}\right) \) is equal to 1 . In other words, \( \tau \) cannot be distinguished from the trivial bundle over \( {S}^{n} \) by means of Stiefel-Whitney classes.

Proof. For the standard imbedding \( {S}^{n} \subset  {\mathbb{R}}^{n + 1} \) , the normal bundle \( \nu \) is trivial. Since \( \mathrm{w}\left( \tau \right) \mathrm{w}\left( \nu \right)  = 1 \) and \( \mathrm{w}\left( \nu \right)  = 1 \) it follows that \( \mathrm{w}\left( \tau \right)  = 1 \) .

Alternative proof (without using the Whitney product theorem): The canonical map

\[
f : {S}^{n} \rightarrow  {\mathbb{P}}^{n}
\]

to projective space is locally a diffeomorphism. Hence the induced map

\[
\mathrm{d}f : \mathbf{T}{S}^{n} \rightarrow  \mathbf{T}{\mathbb{P}}^{n}
\]

of tangent bundles is a bundle map. Applying Axiom 2, one obtains the identity

\[
{f}^{ * }{\mathrm{\;w}}_{n}\left( {\mathbb{P}}^{n}\right)  = {\mathrm{w}}_{n}\left( {S}^{n}\right)
\]

where the homomorphism

\[
{f}^{ * } : {\mathrm{H}}^{n}\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right)  \rightarrow  {\mathrm{H}}^{n}\left( {{S}^{n};\mathbb{Z}/2}\right)
\]

is well known to be zero. (Compare the remark below.) Therefore \( {\mathrm{w}}_{n}\left( {S}^{n}\right)  = 0 \) , which completes the alternative proof.

The rest of \( \text{ § }4 \) will be concerned with bundles over the projective space \( {\mathbb{P}}^{n} \) . It is first necessary to describe the mod 2 cohomology of \( {\mathbb{P}}^{n} \) .

Lemma 4.3. The group \( {\mathrm{H}}^{i}\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right) \) is cyclic of order 2 for \( 0 \leq  i \leq  n \) and is zero for higher values of \( i \) . Furthermore, if \( a \) denotes the non-zero element of \( {\mathrm{H}}^{1}\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right) \) then each \( {\mathrm{H}}^{i}\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right) \) is generated by the \( i \) -fold cup product \( {a}^{i} \) .

Thus \( {\mathrm{H}}^{ \bullet  }\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right) \) can be described as the algebra with unit over \( \mathbb{Z}/2 \) having one generator \( a \) and one relation \( {a}^{n + 1} = 0 \) .

For a proof the reader may refer to [Pal, § 4.3.3] or [Spa81, p. 264]. See Problems 11-A and 12-C. (Compare Theorem 14.4.)

Remark 5. This lemma can be used to compute the homomorphism

\[
{f}^{ * } : {\mathrm{H}}^{n}\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right)  \rightarrow  {\mathrm{H}}^{n}\left( {{S}^{n};\mathbb{Z}/2}\right)
\]

providing that \( n > 1 \) . In fact

\[
{f}^{ * }\left( {a}^{n}\right)  = {\left( {f}^{ * }a\right) }^{n}
\]

is zero since \( {f}^{ * }a \in  {\mathrm{H}}^{1}\left( {{S}^{n};\mathbb{Z}/2}\right)  = 0 \) .

Example 7. The total Stiefel-Whitney class of the canonical line bundle \( {\gamma }_{n}^{1} \) over \( {\mathbb{P}}^{n} \) is given by

\[
\mathrm{w}\left( {\gamma }_{n}^{1}\right)  = 1 + a.
\]

Proof. The standard inclusion \( j : {\mathbb{P}}^{1} \rightarrow  {\mathbb{P}}^{n} \) is clearly covered by a bundle map from \( {\gamma }_{1}^{1} \) to \( {\gamma }_{n}^{1} \) . Therefore

\[
{j}^{ * }{\mathrm{\;w}}_{1}\left( {\gamma }_{n}^{1}\right)  = {\mathrm{w}}_{1}\left( {\gamma }_{1}^{1}\right)  \neq  0.
\]

This shows that \( {\mathrm{w}}_{1}\left( {\gamma }_{n}^{1}\right) \) cannot be zero, hence must be equal to a. Since the remaining Stiefel-Whitney classes of \( {\gamma }_{n}^{1} \) are determined by Axiom 1, this completes the proof.

Example 8. By its definition, the line bundle \( {\gamma }_{n}^{1} \) over \( {\mathbb{P}}^{n} \) is contained as a sub-bundle in the trivial bundle \( {\varepsilon }^{n + 1} \) . Let \( {\gamma }^{ \bot  } \) denote the orthogonal complement of \( {\gamma }_{n}^{1} \) in \( {\varepsilon }^{n + 1} \) . (Thus the total space \( E\left( {\gamma }^{ \bot  }\right) \) consists of all pairs

\[
\left( {\{  \pm  x\} , v}\right)  \in  {\mathbb{P}}^{n} \times  {\mathbb{R}}^{n + 1}
\]

with \( v \) perpendicular to \( x \) .) Then

\[
\mathrm{w}\left( {\gamma }^{ \bot  }\right)  = 1 + a + {a}^{2} + \cdots  + {a}^{n}.
\]

Proof. Since \( {\gamma }_{n}^{1} \oplus  {\gamma }^{ \bot  } \) is trivial we have

\[
\mathrm{w}\left( {\gamma }^{ \bot  }\right)  = \overline{\mathrm{w}}\left( {\gamma }_{n}^{1}\right)  = {\left( 1 + a\right) }^{-1} = 1 + a + {a}^{2} + \cdots  + {a}^{n}.
\]

This example shows that all of the \( n \) Stiefel-Whitney classes of an \( {\mathbb{R}}^{n} \) -bundle may be non-zero.

Example 9. Let \( \tau \) be the tangent bundle of the projective space \( {\mathbb{P}}^{n} \) .

Lemma 4.4. The tangent bundle \( \tau \) of \( {\mathbb{P}}^{n} \) is isomorphic to \( \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }^{ \bot  }}\right) \) .

Proof. Let \( L \) be a line through the origin in \( {\mathbb{R}}^{n + 1} \) , intersecting \( {S}^{n} \) in the points \( \pm  x \) , and let \( {L}^{ \bot  } \subset  {\mathbb{R}}^{n + 1} \) be the complementary \( n \) -plane. Let \( f : {S}^{n} \rightarrow  {\mathbb{P}}^{n} \) denote the canonical map, \( f\left( x\right)  = \{  \pm  x\} \) . Note that the two tangent vectors \( \left( {x, v}\right) \) and \( \left( {-x, - v}\right) \) in \( \mathbf{T}{S}^{n} \) both have the same image under the map

\[
\mathrm{d}f : \mathbf{T}{S}^{n} \rightarrow  \mathbf{T}{\mathbb{P}}^{n}
\]

![bo_d7du9galb0pc73deir9g_51_514_276_697_699_0.jpg](images/bo_d7du9galb0pc73deir9g_51_514_276_697_699_0.jpg)

Figure 5

which is induced by \( f \) . (Compare Figure 5.) Thus the tangent manifold \( {\mathbf{{TP}}}^{n} \) can be identified with the set of all pairs \( \{ \left( {x, v}\right) ,\left( {-x, - v}\right) \} \) satisfying

\[
x \cdot  x = 1,\;x \cdot  v = 0
\]

But each such pair determines, and is determined by, a linear mapping

\[
\ell  : \mathrm{L} \rightarrow  {\mathrm{L}}^{ \bot  },
\]

where

\[
\ell \left( x\right)  = v.
\]

Thus the tangent space of \( {\mathbb{P}}^{n} \) at \( \{  \pm  x\} \) is canonically isomorphic to the vector space \( \operatorname{Hom}\left( {L,{L}^{ \bot  }}\right) \) . It follows that the tangent vector bundle \( \tau \) is canonically isomorphic to the bundle \( \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }^{ \bot  }}\right) \) . This completes the proof of Lemma 4.4.

We cannot compute \( \mathrm{w}\left( {\mathbb{P}}^{n}\right) \) directly from this lemma since we do not yet have

any procedure for relating the Stiefel-Whitney classes of \( \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }^{ \bot  }}\right) \) to those of \( {\gamma }_{n}^{1} \) and \( {\gamma }^{ \bot  } \) . However the computation can be carried through as follows. Let \( {\varepsilon }^{1} \) be a trivial line bundle over \( {\mathbb{P}}^{n} \) .

Theorem 4.5. The Whitney sum \( \tau  \oplus  {\varepsilon }^{1} \) is isomorphic to the \( \left( {n + 1}\right) \) -fold Whitney sum \( {\gamma }_{n}^{1} \oplus  {\gamma }_{n}^{1} \oplus  \cdots  \oplus  {\gamma }_{n}^{1} \) . Hence the total Stiefel-Whitney class of \( {\mathbb{P}}^{n} \) is given by

\[
\mathrm{w}\left( {\mathbb{P}}^{n}\right)  = {\left( 1 + a\right) }^{n + 1} = 1 + \left( \begin{matrix} n + 1 \\  1 \end{matrix}\right) a + \left( \begin{matrix} n + 1 \\  2 \end{matrix}\right) {a}^{2} + \cdots  + \left( \begin{matrix} n + 1 \\  n \end{matrix}\right) {a}^{n}.
\]

Proof. The bundle \( \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }_{n}^{1}}\right) \) is trivial since it is a line bundle with a canonical nowhere zero cross-section. Therefore

\[
\tau  \oplus  {\varepsilon }^{1} \cong  \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }^{ \bot  }}\right)  \oplus  \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }_{n}^{1}}\right) .
\]

This is clearly isomorphic to

\[
\operatorname{Hom}\left( {{\gamma }_{n}^{1},{\gamma }^{ \bot  } \oplus  {\gamma }_{n}^{1}}\right)  \cong  \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\varepsilon }^{n + 1}}\right) ,
\]

and therefore is isomorphic to the \( \left( {n + 1}\right) \) -fold sum

\[
\operatorname{Hom}\left( {{\gamma }_{n}^{1},{\varepsilon }^{1} \oplus  \cdots  \oplus  {\varepsilon }^{1}}\right)  \cong  \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\varepsilon }^{1}}\right)  \oplus  \cdots  \oplus  \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\varepsilon }^{1}}\right)
\]

But the bundle \( \operatorname{Hom}\left( {{\gamma }_{n}^{1},{\varepsilon }^{1}}\right) \) is isomorphic to \( {\gamma }_{n}^{1} \) , since \( {\gamma }_{n}^{1} \) has a Euclidean metric. (Compare Problem 3-D.) This proves that

\[
\tau  \oplus  {\varepsilon }^{1} \cong  {\gamma }_{n}^{1} \oplus  \cdots  \oplus  {\gamma }_{n}^{1}
\]

Now the Whitney product theorem (Axiom 3) implies that \( \mathrm{w}\left( \tau \right)  = \mathrm{w}\left( {\tau  \oplus  {\varepsilon }^{1}}\right) \) is equal to

\[
\mathrm{w}\left( {\gamma }_{n}^{1}\right) \cdots \mathrm{w}\left( {\gamma }_{n}^{1}\right)  = {\left( 1 + a\right) }^{n + 1}
\]

Expanding by the binomial theorem, this completes the proof of 4.5.

Here is a table of the binomial coefficients \( \left( \begin{matrix} n + 1 \\  i \end{matrix}\right) \) modulo 2, for \( n \leq  {14} \) .

<table><tr><td>\( {P}^{1} \) : <br> \( {P}^{2} \) : <br> \( {P}^{3} \) : <br> \( {P}^{4} \) : <br> \( {P}^{5} \) : <br> \( {P}^{6} \) : <br> \( {P}^{7} : \) <br> \( {P}^{8} : \) <br> \( {P}^{9} \) : <br> \( {P}^{10} \) : <br> \( {P}^{11} \) :</td><td>1 <br> 11 <br> 101 <br> 1111 <br> 10001 <br> 110011 <br> 1010101 <br> \( \left\lbrack  \begin{matrix} 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \end{matrix}\right\rbrack \) <br> \( \begin{array}{lllllllll} 1 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{array} \) <br> \( \begin{array}{llllllllll} 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 \end{array} \) <br> \( \begin{array}{lllllllllll} 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \end{array} \) <br> \( \left\lbrack  \begin{matrix} 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 \end{matrix}\right\rbrack \) <br> \( \begin{array}{lllllllllllll} 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 1 \end{array} \) <br> \( \begin{array}{llllllllllllll} 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 & 1 & 1 \end{array} \) <br> 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 <br> D14 . 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1</td></tr></table>

The right hand edge of this triangle can be ignored for our purposes since \( {\mathrm{H}}^{n + 1}\left( {{\mathbb{P}}^{n};\mathbb{Z}/2}\right)  = 0 \) . As examples one has:

\[
\mathrm{w}\left( {\mathbb{P}}^{2}\right)  = 1 + a + {a}^{2}
\]

\[
\mathrm{w}\left( {\mathbb{P}}^{3}\right)  = 1
\]

and

\[
\mathrm{w}\left( {\mathbb{P}}^{4}\right)  = 1 + a + {a}^{4}.
\]

Corollary 4.6. (Stiefel). The class \( \mathrm{w}\left( {\mathbb{P}}^{n}\right) \) is equal to 1 if and only if \( n + 1 \) is a power of 2. Thus the only projective spaces which can be parallelizable are \( {\mathbb{P}}^{1},{\mathbb{P}}^{3},{\mathbb{P}}^{7},{\mathbb{P}}^{15},\ldots \)

(We will see in a moment that \( {\mathbb{P}}^{1},{\mathbb{P}}^{3} \) , and \( {\mathbb{P}}^{7} \) actually are parallelizable. On the other hand it is known that the higher projective spaces \( {\mathbb{P}}^{15},{\mathbb{P}}^{31},\ldots \) are not parallelizable. See [BM58],[Ker58],[Ada60].)

Proof. The identity \( {\left( a + b\right) }^{2} \equiv  {a}^{2} + {b}^{2} \) modulo 2 implies that

\[
{\left( 1 + a\right) }^{{2}^{r}} = 1 + {a}^{{2}^{r}}
\]

Therefore if \( n + 1 = {2}^{r} \) then

\[
\mathrm{w}\left( {\mathbb{P}}^{n}\right)  = {\left( 1 + a\right) }^{n + 1} = 1 + {a}^{n + 1} = 1.
\]

Conversely if \( n + 1 = {2}^{r}m \) with \( m \) odd, \( m > 1 \) , then

\[
\mathrm{w}\left( {P}^{n}\right)  = {\left( 1 + a\right) }^{n + 1} = {\left( 1 + {a}^{{2}^{r}}\right) }^{m} = 1 + m{a}^{{2}^{r}} + \frac{m\left( {m - 1}\right) }{2}{a}^{2 \cdot  {2}^{r}} + \cdots  \neq  1
\]

since \( {2}^{r} < n + 1 \) . This completes the proof.
