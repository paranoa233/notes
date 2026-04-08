## §18 Applications to Homotopy Theory

The Leray spectral sequence is basically a tool for computing the homology or cohomology of a fibration. However, since by the Hurewicz isomorphism theorem, the first nontrivial homology of the Eilenberg-MacLane space \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \) is \( {\pi }_{q}\left( X\right) \) , if one can fit the Eilenberg-MacLane spaces \( K\left( {{\pi }_{q}\left( X\right) , n}\right) \) into a fibering, it may be possible to apply the spectral sequence to compute the homotopy groups. Such fiberings are provided by the Postnikov approximation and the Whitehead tower, two twisted products of Eilenberg-

MacLane spaces which in some way approximate a given space in homotopy. As examples of how this works, we compute in this section \( {\pi }_{4}\left( {S}^{3}\right) \) and \( {\pi }_{5}\left( {S}^{3}\right) \) .

## Eilenberg-MacLane Spaces

Let \( A \) be a group. A path-connected space \( Y \) is an Eilenberg-MacLane space \( K\left( {A, n}\right) \) if

\[
{\pi }_{q}\left( Y\right)  = \left\{  \begin{array}{ll} A & \text{ in dimension }n \\  0 & \text{ otherwise. } \end{array}\right.
\]

(We do not consider \( {\pi }_{0} \) unless otherwise indicated.) For any group \( A \) and any integer \( n \geq  1 \) (with the obvious restriction that \( A \) be Abelian if \( n > 1 \) ), it can be shown that in the category of \( {CW} \) complexes such a space exists and is unique up to homotopy equivalence (Spanier [1, Chap. 8, Sec. 1, Cor. 5, p. 426] and Mosher and Tangora [1, Cor. 2, p. 3]). So provided we consider only \( {CW} \) complexes, the symbol \( K\left( {A, n}\right) \) is unambiguous.

Example 18.1. (a) Since \( \pi  : {\mathbb{R}}^{1} \rightarrow  {S}^{1} \) given by

\[
\pi \left( x\right)  = {e}^{2\pi ix}
\]

is a covering space, \( {\pi }_{q}\left( {S}^{1}\right)  = {\pi }_{q}\left( {\mathbb{R}}^{1}\right)  = 0 \) for \( q \geq  2 \) by (17.5). Therefore the circle is a \( K\left( {\mathbb{Z},1}\right) \) .

(b) If \( F \) is a free group, then \( K\left( {F,1}\right) \) is a bouquet of circles, one for each generator (Figure 18.1).

![bo_d7b6f8alb0pc73dd9avg_250_660_1388_328_360_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_250_660_1388_328_360_0.jpg)

Figure 18.1

(c) The fundamental group of a Riemann surface \( S \) of genus \( g \geq  1 \) (Figure 18.2) is a group \( \pi \) with generators \( {a}_{1},{b}_{1},\ldots ,{a}_{g},{b}_{g} \) and a single relation

\[
{a}_{1}{b}_{1}{a}_{1}^{-1}{b}_{1}^{-1}\cdots {a}_{g}{b}_{g}{a}_{g}^{-1}{b}_{g}^{-1} = 1.
\]

By the uniformization theorem of complex function theory the universal cover of a Riemann surface of genus \( g \geq  1 \) is contractible. Hence the Riemann surface \( S \) is the Eilenberg-MacLane space \( K\left( {\pi ,1}\right) \) .

![bo_d7b6f8alb0pc73dd9avg_251_307_299_1012_321_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_251_307_299_1012_321_0.jpg)

Figure 18.2

(d) By Proposition 17.2, we see that \( {\Omega K}\left( {A, n}\right)  = K\left( {A, n - 1}\right) \) .

(e) The Eilenberg-MacLane space \( K\left( {\mathbb{Z}, n}\right) \) may be constructed from the sphere \( {S}^{n} \) by killing all \( {\pi }_{q}\left( {S}^{n}\right) \) for \( q > n \) . The procedure for killing homotopy groups is discussed in the section on Postnikov approximation.

(f) By (17.1.a) if \( A \) and \( B \) are two groups, then

\[
K\left( {A, n}\right)  \times  K\left( {B, n}\right)  = K\left( {A \times  B, n}\right) .
\]

## The Telescoping Construction

In this section we give a technique for constructing certain Eilenberg-MacLane spaces, called the telescoping construction. It is best illustrated with examples.

EXAMPLE 18.2 (The infinite real projective space). The real projective space \( \mathbb{R}{P}^{n} \) is defined as the quotient of the sphere \( {S}^{n} \) under the equivalence relation which identifies the antipodal points of \( {S}^{n} \) . There is a natural sequence of inclusions

\[
\{ \text{ point }\}  \hookrightarrow  \cdots  \hookrightarrow  \overset{i}{ \hookrightarrow  }\mathbb{R}{P}^{n}\overset{i}{ \hookrightarrow  }\mathbb{R}{P}^{n + 1} \hookrightarrow  \cdots
\]

We define the infinite real projective space \( \mathbb{R}{P}^{\infty } \) by gluing together via the natural inclusions all the finite real projective spaces

\[
\mathbb{R}{P}^{\infty } = \mathop{\coprod }\limits_{n}\mathbb{R}{P}^{n} \times  I/\left( {x,1}\right)  \sim  \left( {i\left( x\right) ,0}\right) .
\]

Pictorially \( \mathbb{R}{P}^{\infty } \) looks like an infinite telescope (Figure 18.3).

Since \( {S}^{n} \rightarrow  \mathbb{R}{P}^{n} \) is a double cover, by (17.5) \( {\pi }_{q}\left( {\mathbb{R}{P}^{n}}\right)  = {\pi }_{q}\left( {S}^{n}\right)  = 0 \) for \( 1 < q < n \) . We now show that \( \mathbb{R}{P}^{\infty } \) has no higher homotopy, i.e., \( {\pi }_{q}\left( {\mathbb{R}{P}^{\infty }}\right)  = 0 \) for \( q > 1 \) . Take \( {\pi }_{15}\left( {\mathbb{R}{P}^{\infty }}\right) \) for example. Suppose \( f : {S}^{15} \rightarrow  \mathbb{R}{P}^{\infty } \) represents an element of \( {\pi }_{15}\left( {\mathbb{R}{P}^{\infty }}\right) \) . Since the image \( f\left( {S}^{15}\right) \) is compact, it must lie in a finite union of the \( \mathbb{R}{P}^{n} \times  I \) ’s above. We can slide \( f\left( {S}^{15}\right) \) into a high \( \mathbb{R}{P}^{n} \times  I \) . If \( n > {15} \) , then \( f\left( {S}^{15}\right) \) will be contractible. Therefore \( {\pi }_{15}\left( {\mathbb{R}{P}^{\infty }}\right)  = 0 \) . Thus by sliding the image of a sphere into a high enough projective space, we see that this telescope kills all higher homotopy groups.

![bo_d7b6f8alb0pc73dd9avg_252_498_307_645_397_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_252_498_307_645_397_0.jpg)

Figure 18.3

Applying the telescoping construction to the sequence of spheres

\[
\text{ \{point\} } \hookrightarrow  \cdots  \hookrightarrow  {S}^{n}\overset{i}{ \hookrightarrow  }{S}^{n + 1} \hookrightarrow  \cdots
\]

we obtain the infinite sphere

\[
{S}^{\infty } = \mathop{\coprod }\limits_{n}{S}^{n} \times  I/\left( {x,1}\right)  \sim  \left( {i\left( x\right) ,0}\right) .
\]

It is a double cover of \( \mathbb{R}{P}^{\infty } \) . By the same reasoning as above, \( {S}^{\infty } \) has no homotopy in any dimension. Therefore \( {\pi }_{1}\left( {\mathbb{R}{P}^{\infty }}\right)  = {\mathbb{Z}}_{2} \) . This proves that \( \mathbb{R}{P}^{\infty } \) is a \( K\left( {{\mathbb{Z}}_{2},1}\right) \) .

EXAMPLE 18.3. (The infinite complex projective space). Applying the telescoping construction to the sequences

\[
\cdots  \subset  {S}^{{2n} + 1} \subset  {S}^{{2n} + 3} \subset  \cdots
\]

\[
{S}^{1} \downarrow  \; \downarrow
\]

\[
\cdots  \subset  \mathbb{C}{P}^{n} \subset  \mathbb{C}{P}^{n + 1} \subset  \cdots ,
\]

we obtain the fibering

\[
{S}^{1} \rightarrow  {S}^{\infty }
\]

(18.3.1)

↓

\( \mathbb{C}{P}^{\infty } \)

where \( \mathbb{C}{P}^{\infty } \) is gotten by gluing together the \( \mathbb{C}{P}^{n} \) ’s as in the previous example. Since \( {S}^{\infty } \) has no homotopy in any dimension, it follows from the homotopy sequence of the fibering that

\[
{\pi }_{k}\left( {\mathbb{C}{P}^{\infty }}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ when }k = 2 \\  0 & \text{ otherwise. } \end{array}\right.
\]

Therefore \( \mathbb{C}{P}^{\infty } \) is a \( K\left( {\mathbb{Z},2}\right) \) .

Exercise 18.4. By the Hurewicz isomorphism theorem \( {H}_{k}\left( {S}^{\infty }\right)  = 0 \) except in dimension 0 . Apply the spectral sequence of the fibering (18.3.1) to show that the cohomology ring of \( \mathbb{C}{P}^{\infty } \) is a polynomial algebra with a generator in dimension 2:

\[
{H}^{ * }\left( {\mathbb{C}{P}^{\infty }}\right)  = \mathbb{Z}\left\lbrack  x\right\rbrack  ,\;\dim x = 2.
\]

EXAMPLE 18.5 (Lens spaces). Let \( {S}^{{2n} + 1} \) be the unit sphere in \( {\mathbb{C}}^{n + 1} \) . Since \( {S}^{1} \) acts freely on \( {S}^{{2n} + 1} \) , so does any subgroup of \( {S}^{1} \) . For example, \( {\mathbb{Z}}_{5} \) acts on \( {S}^{{2n} + 1} \) by

\[
{e}^{{2\pi i}/5} : \left( {{z}_{0},\ldots ,{z}_{n}}\right)  \mapsto  \left( {{e}^{{2\pi i}/5}{z}_{0},\ldots ,{e}^{{2\pi i}/5}{z}_{n}}\right) .
\]

The quotient space of \( {S}^{{2n} + 1} \) by the action of \( {\mathbb{Z}}_{5} \) is the lens space \( L\left( {n,5}\right) \) . Applying the telescoping construction

\[
{S}^{1} \subset  \cdots  \subset  {S}^{{2n} + 1} \subset  {S}^{{2n} + 3}\; \subset  \cdots
\]

\[
{\mathbb{Z}}_{5} \downarrow  \; \downarrow  \; \downarrow
\]

\[
L\left( {0,5}\right)  \subset  \cdots  \subset  L\left( {n,5}\right)  \subset  L\left( {n + 1,5}\right)  \subset  \cdots ,
\]

we obtain a five-sheeted covering

\[
{\mathbb{Z}}_{5} \rightarrow  {S}^{\infty }
\]

\[
\text{ ↓ }
\]

\[
L\left( {\infty ,5}\right) \text{ . }
\]

Hence

\[
{\pi }_{k}\left( {L\left( {\infty ,5}\right) }\right)  = \left\{  \begin{array}{ll} {\mathbb{Z}}_{5} & \text{ if }k = 1 \\  0 & \text{ if }k > 1. \end{array}\right.
\]

So the infinite lens space \( L\left( {\infty ,5}\right) \) is a \( K\left( {{\mathbb{Z}}_{5},1}\right) \) . In exactly the same manner we can construct \( L\left( {\infty , q}\right)  = K\left( {{\mathbb{Z}}_{q},1}\right) \) for any positive integer \( q \) .

Remark 18.5.1. The lens space \( L\left( {n,2}\right) \) is the real projective space \( \mathbb{R}{P}^{{2n} + 1} \) , and the infinite lens space \( L\left( {\infty ,2}\right) \) is \( \mathbb{R}{P}^{\infty } \) .

Next we shall compute the cohomology of a lens space, say \( L\left( {n,5}\right) \) . Since the lens space \( L\left( {n,5}\right) \) is not simply connected, the defining fibration \( {\mathbb{Z}}_{5} \rightarrow  {S}^{{2n} + 1} \rightarrow  L\left( {n,5}\right) \) is of little use in the computation of the cohomology. Instead, note that the free action of \( {S}^{1} \) on \( {S}^{{2n} + 1} \) descends to an action on \( L\left( {n,5}\right) \) :

\[
\left( {{z}_{0},\ldots ,{z}_{n}}\right)  \mapsto  \left( {\lambda {z}_{0},\ldots ,\lambda {z}_{n}}\right) ,\;\lambda  \in  {S}^{1} \subset  {\mathbb{C}}^{ * },
\]

with quotient \( \mathbb{C}{P}^{n} \) , so that there is a fiber bundle

\[
{S}^{1} \rightarrow  L\left( {n,5}\right)
\]

\[
\mathbb{C}{P}^{n}\text{ . }
\]

The \( {E}_{2} \) term of this fiber bundle is(18.5.2)

![bo_d7b6f8alb0pc73dd9avg_254_525_364_540_312_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_254_525_364_540_312_0.jpg)

To decide what the differential \( {d}_{2} \) is, we compare with the spectral sequence of the fiber bundle \( {S}^{1} \rightarrow  {S}^{{2n} + 1}\overset{{\pi }_{s}}{ \rightarrow  }\mathbb{C}{P}^{n} \) . The bundle map \( \rho \) : \( {S}^{{2n} + 1} \rightarrow  L\left( {n,5}\right) \) over \( \mathbb{C}{P}^{n} \) induces a chain map on the double complexes

\[
{\rho }^{ * } : {C}^{ * }\left( {{\pi }_{L}^{-1}\mathfrak{U},{\Omega }^{ * }}\right)  \rightarrow  {C}^{ * }\left( {{\pi }_{S}^{-1}\mathfrak{U},{\Omega }^{ * }}\right) ,
\]

where \( \mathfrak{U} \) is a good cover of \( \mathbb{C}{P}^{n} \) . Let \( {a}_{L} \) and \( {a}_{S} \) be the generators of \( {E}_{2}^{0,1} \) for these two complexes, and \( x \) a generator of \( {H}^{ * }\left( {\mathbb{C}{P}^{n}}\right) \) . Because \( \rho \) is a map of degree \( 5,{\rho }^{ * }{a}_{L} = 5{a}_{S} \) . Hence,

\[
{\rho }^{ * }\left( {{d}_{2}{a}_{L}}\right)  = {d}_{2}{\rho }^{ * }{a}_{L} = {d}_{2}5{a}_{S} = {5x}.
\]

So \( {d}_{2}{a}_{L} = {5x} \) in (18.5.2). The cohomology of the lens space \( L\left( {n,5}\right) \) is therefore

\[
{H}^{ * }\left( {L\left( {n,5}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ in dimension }0 \\  {\mathbb{Z}}_{5} & \text{ in dimensions }2,4,\ldots ,{2n} \\  \mathbb{Z} & \text{ in dimension }{2n} + 1 \\  0 & \text{ otherwise. } \end{array}\right.
\]

REMARK 18.5.3. Another way of determining the differential in (18.5.2) is to compute \( {H}^{2}\left( {L\left( {n,5}\right) }\right) \) first by the universal coefficient theorem (15.14). Since \( {\pi }_{1}\left( {L\left( {n,5}\right) }\right)  = {\mathbb{Z}}_{5},{H}_{1}\left( {L\left( {n,5}\right) }\right)  = {\mathbb{Z}}_{5} \) and \( {H}^{2} = {\mathbb{Z}}_{5} \oplus \) free part. Therefore \( {d}_{2}a \) must be \( {5x} \) and \( {H}^{2} = {\mathbb{Z}}_{5} \) .

In exactly the same way we see that the cohomology of the lens space \( L\left( {n, q}\right) \) is

(18.6)

\[
{H}^{ * }\left( {L\left( {n, q}\right) }\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ in dimension }0 \\  {\mathbb{Z}}_{q} & \text{ in dimensions }2,4,\ldots ,{2n} \\  \mathbb{Z} & \text{ in dimension }{2n} + 1 \\  0 & \text{ otherwise. } \end{array}\right.
\]

Exercise 18.7. Prove that the lens space \( L\left( {n, q}\right) \) is an orientable manifold.

Exercise 18.8. Let \( q \) be a positive integer greater than one.

(a) Show that the integer cohomology of \( K\left( {{\mathbb{Z}}_{q},1}\right) \) is

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;\mathbb{Z}}\right)  = \left\{  \begin{array}{ll} \mathbb{Z} & \text{ in dimension }0 \\  {\mathbb{Z}}_{q} & \text{ in every positive even dimension } \\  0 & \text{ otherwise. } \end{array}\right.
\]

(b) Using the fibering \( {S}^{1} \rightarrow  K\left( {{\mathbb{Z}}_{q},1}\right)  \rightarrow  \mathbb{C}{P}^{\infty } \) , compute \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;{\mathbb{Z}}_{p}}\right) \) where \( p \) is a prime.

Exercise 18.9. Let \( n \) and \( q \) be positive integers. Show that

\[
{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q}, n}\right) ;\mathbb{Q}}\right)  = \left\{  \begin{array}{ll} \mathbb{Q} & \text{ in dimension }0 \\  0 & \text{ otherwise. } \end{array}\right.
\]

Therefore, by the structure theorem for finitely generated Abelian groups, the rational cohomology of \( K\left( {A, n}\right) \) is trivial for a finitely generated torsion Abelian group.

Exercise 18.10. Determine the product structures of \( {H}^{ * }\left( {L\left( {n, q}\right) }\right) ,{H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},}\right) }\right. \) 1)), and \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{q},1}\right) ;{\mathbb{Z}}_{p}}\right) \) . In particular, show that

\[
{H}^{ * }\left( {\mathbb{R}{P}^{\infty }}\right)  = \mathbb{Z}\left\lbrack  a\right\rbrack  /\left( {2a}\right) ,\;\dim a = 2,
\]

and

\[
{H}^{ * }\left( {\mathbb{R}{P}^{\infty };{\mathbb{Z}}_{2}}\right)  = {\mathbb{Z}}_{2}\left\lbrack  x\right\rbrack  ,\;\dim x = 1.
\]

The Cohomology of \( K\left( {\mathbb{Z},3}\right) \)

Since \( {\pi }_{q}\left( {S}^{3}\right)  = 0 \) for \( q < 3 \) and \( {\pi }_{3}\left( {S}^{3}\right)  = \mathbb{Z} \) , one may wonder if the sphere \( {S}^{3} \) is a \( K\left( {\mathbb{Z},3}\right) \) . One way of deciding this is to compute the cohomology of \( K\left( {\mathbb{Z},3}\right) \) . We first observe that

\[
{\Omega K}\left( {\mathbb{Z},3}\right)  = K\left( {\mathbb{Z},2}\right)  = \mathbb{C}{P}^{\infty },
\]

whose cohomology we know to be \( \mathbb{Z}\left\lbrack  x\right\rbrack \) from Exercise 18.4. Since by Remark 17.13, every \( {CW} \) complex has a good cover, we can apply the spectral sequence of the path fibration

\[
K\left( {\mathbb{Z},2}\right)  \rightarrow  {PK}\left( {\mathbb{Z},3}\right)
\]

\[
\text{ ↓ }
\]

\[
K\left( {\mathbb{Z},3}\right)
\]

to compute the cohomology of \( K\left( {\mathbb{Z},3}\right) \) .

By Leray’s theorem with integer coefficients (15.11), the \( {E}_{2} \) term of the spectral sequence is

\[
{E}_{2}^{p, q} = {H}^{p}\left( {K\left( {\mathbb{Z},3}\right) }\right)  \otimes  {H}^{q}\left( {\mathbb{C}{P}^{\infty }}\right)
\]

and its product structure is that of the tensor product of \( {H}^{ * }\left( {K\left( {\mathbb{Z},3}\right) }\right) \) and \( {H}^{ * }\left( {\mathbb{C}{P}^{\infty }}\right) \) .

![bo_d7b6f8alb0pc73dd9avg_256_289_381_938_500_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_256_289_381_938_500_0.jpg)

Since the total space \( {PK}\left( {\mathbb{Z},3}\right) \) is contractible, the \( {E}_{\infty } \) term is 0 except for \( {E}_{\infty }^{0,0} \) . The plan now is to "create" elements in the bottom row of the \( {E}_{2} \) picture which would sooner or later "kill off" all the nonzero elements of the spectral sequence. There can be no nonzero elements in the bottom row of columns 1 and 2, for any such element would survive to \( {E}_{\infty } \) . However there must be an element \( s \) in column 3 to kill off \( a \) . Thus

\[
{d}_{3}a = s
\]

and

\[
{d}_{3}\left( {a}^{2}\right)  = {2a}{d}_{3}a = {2as}.
\]

There must be an element \( y \) in column 6 to kill off as for otherwise as would survive to \( {E}_{\infty } \) . Therefore \( {H}^{6}\left( {K\left( {\mathbb{Z},3}\right) }\right)  \neq  0 \) . This proves that \( {S}^{3} \) is not a \( K\left( {\mathbb{Z},3}\right) \) . Equivalently, it shows the existence of nontrivial higher homotopy groups for \( {S}^{3} \) . Later in this section we will compute \( {\pi }_{4} \) and \( {\pi }_{5} \) of \( {S}^{3} \) .

As for the cohomology ring of \( K\left( {\mathbb{Z},3}\right) \) , we can be more precise. First, note that \( y = {d}_{3}\left( {as}\right)  = \left( {{d}_{3}a}\right)  \cdot  s = {s}^{2} \) . From the picture of \( {E}_{2} \) , it is clear that \( {H}^{6}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = {\mathbb{Z}}_{2} \) . Therefore, \( 2{s}^{2} = 0 \) . Now a nonzero element in \( {E}_{2}^{7,0} = \; {H}^{7}\left( {K\left( {\mathbb{Z},3}\right) }\right) \) can be killed only by \( {a}^{3} \) under \( {d}_{7} \) . Since \( {d}_{3}\left( {a}^{3}\right)  = 3{a}^{2}s \neq  0,{a}^{3} \) does not even live to \( {E}_{4} \) . So \( {H}^{7}\left( {K\left( {\mathbb{Z},3}\right) }\right)  = 0 \) . Since \( {d}_{3}\left( {{a}^{2}s}\right)  = {2a}{s}^{2} = 0,{a}^{2}s \) would live to \( {E}_{\infty } \) unless \( {d}_{5}\left( {{a}^{2}s}\right)  = t \neq  0 \) . In \( {E}_{4} = {E}_{5},{a}^{2}s \) generates the cyclic group \( {\mathbb{Z}}_{3} \) . Since \( t \) is the element that kills \( {a}^{2}s \) in \( {E}_{5}, t \) is of order 3 . In summary the first few cohomology groups of \( K\left( {\mathbb{Z},3}\right) \) are(18.11)

<table><tr><td>\( q \)</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>\( {H}^{q} \)</td><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td><td>\( {\mathbb{Z}}_{2} \)</td><td>0</td><td>\( {\mathbb{Z}}_{3} \)</td></tr><tr><td>generators</td><td>1</td><td></td><td></td><td>\( S \)</td><td></td><td></td><td>\( {s}^{2} \)</td><td></td><td>\( t \)</td></tr></table>

EXERCISE 18.12. Show that \( {H}^{ * }\left( {K\left( {\mathbb{Z}, n}\right) ;\mathbb{Q}}\right) \) is an exterior algebra on one generator of dimension \( n \) if \( n \) is odd and a polynomial algebra on one generator of dimension \( n \) if \( n \) is even. In either case we say that the cohomology of \( K\left( {\mathbb{Z}, n}\right) \) is free on one generator (see Section 19 for the definition of a free algebra).

## The Transgression

Let \( \pi  : E \rightarrow  X \) be a fibration with connected fiber \( F \) over a simply connected space with a good cover \( \mathfrak{U} \) . In computing the differentials of the spectral sequence of \( E \) using what we have developed so far, one often encounters ambiguities which cannot be resolved without further clues. One such clue is knowledge of the transgressive elements. An element \( \omega \) in

\[
{H}^{q}\left( F\right)  \hookrightarrow  {E}_{2}^{0, q} = {H}^{0}\left( {\mathfrak{U},{\mathcal{H}}^{q}\left( F\right) }\right)
\]

is called transgressive if it lives to \( {E}_{q + 1} \) ; that is,

\[
{d}_{2}\omega  = {d}_{3}\omega  = \cdots  = {d}_{q}\omega  = 0.
\]

An alternative characterization of a transgressive element is given in the following proposition, which we phrase in the language of differential forms. Of course by replacing forms with singular cochains, the proposition is equally true in the singular setting with arbitrary coefficients.

Proposition 18.13. Let \( \pi  : E \rightarrow  M \) be a fibration with fiber \( F \) in the differentiable category. An element \( \omega \) in \( {H}^{q}\left( F\right) \) is transgressive if and only if it is the restriction of a global form \( \psi \) on \( E \) such that \( {d\psi } = {\pi }^{ * }\tau \) for some form \( \tau \) on the base M.

REMARK 18.13.1. Because \( {\pi }^{ * } \) is injective and

\[
{\pi }^{ * }{d\tau } = {dd\psi } = 0,
\]

we actually have

\[
{d\tau } = 0,
\]

so the form \( \tau \) defines a cohomology class on \( M \) .

Proof of PROPOSITION 18.13. Let \( \mathfrak{U} \) be a good cover of \( M \) . If \( \omega \) is transgressive, then by (14.12) it can be extended to a cochain \( \alpha  = {\alpha }_{0} + \cdots  + {\alpha }_{q} \) in the double complex \( {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) \) such that \( {D\alpha } = {\pi }^{ * }\beta \) for some Čech cocycle \( \beta \) on \( M \) . By the collating formula (9.5),

(*)

\[
\psi  = \mathop{\sum }\limits_{{i = 0}}^{q}{\left( -1\right) }^{i}{\left( {D}^{\prime \prime }K\right) }^{i}{\alpha }_{i} + {\left( -1\right) }^{q + 1}K{\left( {D}^{\prime \prime }K\right) }^{q}{\pi }^{ * }\beta
\]

![bo_d7b6f8alb0pc73dd9avg_257_627_1897_390_247_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_257_627_1897_390_247_0.jpg)

is a global form on \( E \) corresponding to \( \alpha \) . From (*) we see that

\[
{d\psi } = {\left( -1\right) }^{q + 1}{\left( {D}^{\prime \prime }K\right) }^{q + 1}{\pi }^{ * }\beta  = {\pi }^{ * }\tau ,
\]

where \( \tau  = {\left( -{D}^{\prime \prime }K\right) }^{q + 1}\beta \) is by (9.8) a closed global form on \( M \) .

Conversely, suppose \( \psi \) is a global \( q \) -form on \( E \) with \( {d\psi } = {\pi }^{ * }\tau \) for some \( \left( {q + 1}\right) \) -form on \( M \) . We will identify global forms on \( M \) with 0 -cochains in \( {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) \) that vanish under \( \delta \) . By Remark 18.13.1, \( \tau \) defines a cohomology class on \( M \) . Let \( \beta  \in  {C}^{q + 1}\left( {\mathfrak{U},\mathbb{R}}\right) \) be the Čech cocycle corresponding to \( \tau \) under the Čech-de Rham isomorphism. Then

\[
\tau  = \beta  + D\left( {{\gamma }_{0} + {\gamma }_{1} + \cdots  + {\gamma }_{q}}\right)  \in  {C}^{ * }\left( {\mathfrak{U},{\Omega }^{ * }}\right) ,
\]

where \( {\gamma }_{i} \in  {C}^{i}\left( {\mathfrak{U},{\Omega }^{q - i}}\right) \) . Hence,

\[
{D\psi } = {\pi }^{ * }\tau  = {\pi }^{ * }\beta  + D\left( {{\pi }^{ * }{\gamma }_{0} + {\pi }^{ * }{\gamma }_{1} + \cdots  + {\pi }^{ * }{\gamma }_{q}}\right)  \in  {C}^{ * }\left( {{\pi }^{-1}\mathfrak{U},{\Omega }^{ * }}\right) .
\]

Let \( {\alpha }_{i} =  - {\pi }^{ * }{\gamma }_{i} \) . Then

(**)

\[
D\left( {\psi  + {\alpha }_{0} + {\alpha }_{1} + \cdots  + {\alpha }_{q}}\right)  = {\pi }^{ * }\beta .
\]

Since \( {\left. \left( \psi  + {\alpha }_{0}\right) \right| }_{F} = {\left. \left( \psi  - {\pi }^{ * }{\gamma }_{0}\right) \right| }_{F} = {\left. \psi \right| }_{F} \) , the cohomology class of \( {\left. \psi \right| }_{F} \) in \( {H}^{q}\left( F\right) \) can be represented by the cochain \( \psi  + {\alpha }_{0} \in  {E}_{2}^{0, q} \) . The existence of \( {\alpha }_{1},\ldots ,{\alpha }_{q} \) in \( \left( {* * }\right) \) shows that the cochain \( \psi  + {\alpha }_{0} \) lives to \( {E}_{q + 1} \) .

We will now apply the singular analogue of Proposition 18.13 to obtain one of the most useful vanishing criteria for the differentials of a spectral sequence.

Proposition 18.14. In mod 2 cohomology, if \( \alpha \) is a transgressive, so is \( {\alpha }^{2} \) .

Proof. Let \( \psi \) be the singular cochain on \( E \) given by Prop. 18.13. Since \( \psi \) restricts to \( \alpha \) on a fiber, \( {\psi }^{2} \) restricts to \( {\alpha }^{2} \) . With \( {\mathbb{Z}}_{2} \) coefficients,

\[
d\left( {\psi }^{2}\right)  = \left( {d\psi }\right) \psi  \pm  {\psi d\psi } = {2\psi d\psi } = 0,
\]

because \( - 1 =  + 1\left( {\;\operatorname{mod}\;2}\right) \) . Therefore, by Prop. 18.13 again, \( {\alpha }^{2} \) is transgressive.

Exercise 18.15. Compute \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},2}\right) ;{\mathbb{Z}}_{2}}\right) \) and \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},2}\right) ;\mathbb{Z}}\right) \) up to dimension 6.

Exercise 18.16. Compute \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},3}\right) ;{\mathbb{Z}}_{2}}\right) \) and \( {H}^{ * }\left( {K\left( {{\mathbb{Z}}_{2},3}\right) ;\mathbb{Z}}\right) \) up to dimension 6.

Exercise 18.16.1. Compute the homology \( {H}_{ * }\left( {K\left( {{\mathbb{Z}}_{2},4}\right) ;\mathbb{Z}}\right) \) up to dimension 6.

## Basic Tricks of the Trade

In homotopy theory every map \( f : A \rightarrow  B \) from a space \( A \) to a path-connected space \( B \) may be viewed as either an inclusion or a fibering. We can see this as follows.

## (18.17) Inclusion

Applying the telescoping idea just once, we construct the mapping cylinder of \( f \) (see Figure 18.4):

\[
{M}_{f} = \left( {A \times  I}\right)  \cup  B/\left( {a,1}\right)  \sim  f\left( a\right) .
\]

![bo_d7b6f8alb0pc73dd9avg_259_485_758_676_390_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_259_485_758_676_390_0.jpg)

Figure 18.4

It is clear that the mapping cylinder \( {M}_{f} \) has the same homotopy type as \( B \) and that \( A \) is included in \( {M}_{f} \) . Indeed the following diagram is commutative:

![bo_d7b6f8alb0pc73dd9avg_259_571_1351_501_250_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_259_571_1351_501_250_0.jpg)

(18.18) Fibering

Let \( f : A \rightarrow  B \) be any map, with \( B \) path connected. By (18.17) we may assume that \( f \) is an inclusion, i.e., \( A \) is a subspace of \( B \) (Figure 18.5). Define \( L \) to be the space of all paths in \( B \) with initial point in \( A \) . By shrinking every path to its initial point, we get a homotopy equivalence

\[
L \simeq  A\text{ . }
\]

![bo_d7b6f8alb0pc73dd9avg_259_613_1815_438_292_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_259_613_1815_438_292_0.jpg)

Figure 18.5

On the other hand by projecting every path to its endpoint, we get a fibering

\[
{\Omega }_{ * }^{A} \rightarrow  L \simeq  A
\]

\[
\text{ ↓ }
\]

\[
B
\]

whose fiber is \( {\Omega }_{ * }^{A} \) , the space of all paths from a point \( * \) in \( B \) to \( A \) . So up to homotopy equivalence, \( f : A \rightarrow  B \) is a fibering.

## Postnikov Approximation

Let \( X \) be a \( {CW} \) complex with homotopy groups \( {\pi }_{q}\left( X\right)  = {\pi }_{q} \) . Although \( X \) has the same homotopy groups as the product space \( \prod K\left( {{\pi }_{q}, q}\right) \) , in general it will not have the same homotopy type as \( \prod K\left( {{\pi }_{q}, q}\right) \) . However, up to homotopy every \( {CW} \) complex can be thought of as a "twisted product" of Eilenberg-MacLane spaces in the following sense.

Proposition 18.19 (Postnikov Approximation). Every connected CW complex can be approximated by a twisted product of Eilenberg-MacLane spaces; more precisely, for each \( n \) , there is a sequence of fibrations \( {Y}_{q} \rightarrow  {Y}_{q - 1} \) with the \( K\left( {{\pi }_{q}, q}\right) \) ’s as fibers and commuting maps \( X \rightarrow  {Y}_{q} \)

![bo_d7b6f8alb0pc73dd9avg_260_383_1439_584_242_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_260_383_1439_584_242_0.jpg)

such that the map \( X \rightarrow  {Y}_{q} \) induces an isomorphism of homotopy groups in dimensions \( \leq  q \) .

Such a sequence of fibrations is called a Postnikov tower of \( X \) . In view of (18.18) that every map in homotopy theory is a fibration, this proposition is perhaps not so surprising.

We first explain a procedure for killing the homotopy groups of \( X \) above a given dimension. For example, to construct \( K\left( {{\pi }_{1},1}\right) \) we kill off the homotopy groups of \( X \) in dimensions \( \geq  2 \) as follows. If \( \alpha  : {S}^{2} \rightarrow  X \) represents a nontrivial element in \( {\pi }_{2}\left( X\right) \) , we attach a 3-cell to \( X \) via \( \alpha \) :

\[
X \cup  {e}^{3} = X\coprod {e}^{3}/x \sim  \alpha \left( x\right) ,\;x \in  {S}^{2}.
\]

This procedure does not change the fundamental group of the space. By Proposition 17.11 attaching an \( n \) -cell to \( X \) could kill an element of \( {\pi }_{n - 1}\left( X\right) \) but does not affect the homotopy of \( X \) in dimensions \( \leq  n - 2 \) . For each generator of \( {\pi }_{2}\left( X\right) \) we attach a 3-cell to \( X \) as above. In this way we create a new space \( {X}_{1} \) with the same fundamental group as \( X \) but with no \( {\pi }_{2} \) . Iterating this procedure we can kill all higher homotopy groups. This gives \( {Y}_{1} \) .

Proof of proposition 18.19. To construct \( {Y}_{n} \) we kill off all homotopy of \( X \) in dimensions \( \geq  n + 1 \) by attaching cells of dimensions \( \geq  n + 2 \) . Then

\[
{\pi }_{k}\left( {Y}_{n}\right)  = \left\{  \begin{array}{ll} 0, & k \geq  n + 1 \\  {\pi }_{k}, & k = 1,2,\ldots , n. \end{array}\right.
\]

Having constructed \( {Y}_{n} \) , the space \( {Y}_{n - 1} \) is obtained from \( {Y}_{n} \) by killing the homotopy of \( {Y}_{n} \) in dimension \( n \) and above. By (18.18), the inclusions

\[
X \subset  {Y}_{n} \subset  {Y}_{n - 1} \subset  \cdots  \subset  {Y}_{1}
\]

may be converted to fiberings. From the exact homotopy sequence of a fibering we see that the fiber of \( {Y}_{q} \rightarrow  {Y}_{q - 1} \) is the Eilenberg-MacLane space \( K\left( {{\pi }_{q}, q}\right) \) .

Computation of \( {\pi }_{4}\left( {S}^{3}\right) \)

This computation of \( {\pi }_{4} = {\pi }_{4}\left( {S}^{3}\right) \) is based on the fact that the homotopy group \( {\pi }_{4} \) appears as the first nontrivial homology group of the Eilenberg-MacLane space \( K\left( {{\pi }_{4},4}\right) \) . If this Eilenberg-MacLane space can be fitted into some fibering, its homology may be found from the spectral sequence. Such a fibering is provided by the Postnikov approximation.

Let \( {Y}_{4} \) be a space whose homotopy agrees with \( {S}^{3} \) up to and including dimension 4 and vanishes in higher dimensions. To get such a space we kill off all homotopy groups of \( {S}^{3} \) in dimensions \( \geq  5 \) by attaching cells of dimensions \( \geq  6 \) . So

\[
{Y}_{4} = {S}^{3} \cup  {e}^{6} \cup  \ldots
\]

By Proposition 17.12, \( {H}_{4}\left( {Y}_{4}\right)  = {H}_{5}\left( {Y}_{4}\right)  = 0 \) . The Postnikov approximation theorem gives us a fibering

\[
K\left( {{\pi }_{4},4}\right)  \rightarrow  {Y}_{4}
\]

The \( {E}^{2} \) term of the homology spectral sequence of this fibering is

![bo_d7b6f8alb0pc73dd9avg_262_510_360_643_418_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_262_510_360_643_418_0.jpg)

where the homology of \( K\left( {\mathbb{Z},3}\right) \) is obtained from (18.11) and the universal coefficient theorem (15.14). Since \( {H}_{4}\left( {Y}_{4}\right)  = {H}_{5}\left( {Y}_{4}\right)  = 0 \) , the arrow shown must be an isomorphism. Hence \( {\pi }_{4}\left( {S}^{3}\right)  = {\mathbb{Z}}_{2} \) .

More generally since \( {Y}_{q} = {S}^{3} \cup  {e}^{q + 2} \cup  \ldots \) , by (17.12),

\[
{H}_{q}\left( {Y}_{q}\right)  = {H}_{q + 1}\left( {Y}_{q}\right)  = 0.
\]

Hence from the homology \( {E}^{2} \) term of the fibration

![bo_d7b6f8alb0pc73dd9avg_262_274_1100_1056_355_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_262_274_1100_1056_355_0.jpg)

we get

(18.20)

\[
{\pi }_{q}\left( {S}^{3}\right)  = {H}_{q + 1}\left( {Y}_{q - 1}\right) .
\]

## The Whitehead Tower

The Whitehead tower is a sequence of fibrations, dual to the Postnikov approximation in a certain sense, which generalizes the universal covering of a space. It is due independently to Cartan and Serre [1] and to George Whitehead [2]. Unlike the Postnikov construction, where we kill successively the homotopy groups above a given dimension, here the idea is to kill at each stage all the homotopy groups below a given dimension.

Up to homotopy the universal covering of a space \( X \) may be constructed as follows. Write \( {\pi }_{a} = {\pi }_{a}\left( X\right) \) . By attaching cells to \( X \) we can kill all \( {\pi }_{a} \) for \( q \geq  2 \) as in (18.19). Let \( Y = X \cup  {e}^{3} \cup  \cdots \) be the space so obtained; \( Y \) is a \( K\left( {{\pi }_{1},1}\right) \) containing \( X \) as a subspace. Consider the space \( {\Omega }_{ * }^{X} \) of all paths in \( Y \) from a base point \( * \) to \( X \) (Figure 18.6). The endpoint map: \( {\Omega }_{ * }^{X} \rightarrow  X \) is a fibration with fiber \( {\Omega Y} = {\Omega K}\left( {{\pi }_{1},1}\right)  = K\left( {{\pi }_{1},0}\right) \) . From the homotopy exact

![bo_d7b6f8alb0pc73dd9avg_263_600_311_427_339_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_263_600_311_427_339_0.jpg)

Figure 18.6

sequence of the fibering

\[
K\left( {{\pi }_{1},0}\right)  \rightarrow  {\Omega }_{ * }^{X}
\]

\[
\text{ ↓ }
\]

\[
X
\]

we see that \( {\pi }_{1}\left( {\Omega }_{ * }^{X}\right)  = 0 \) . Hence \( {X}_{1} = {\Omega }_{ * }^{X} \) is the universal covering of \( X \) up to homotopy.

We will now generalize this procedure to obtain a sequence of fibrations

\[
K\left( {{\pi }_{n}, n - 1}\right)  \rightarrow  {X}_{n}
\]

\[
\text{ ↓ }
\]

\[
{X}_{n - 1}
\]

\[
\text{ ↓ }
\]

\[
\vdots
\]

\[
\text{ ↓ }
\]

\[
K\left( {{\pi }_{1},0}\right)  \rightarrow  {X}_{1}
\]

\[
\text{ ↓ }
\]

\[
X
\]

such that

(a) \( {X}_{n} \) is \( n \) -connected, i.e., \( {\pi }_{q}\left( {X}_{n}\right)  = 0 \) for all \( q \leq  n \) ;

(b) above dimension \( n \) the homotopy groups of \( {X}_{n} \) and \( X \) agree;

(c) the fiber of \( {X}_{n} \rightarrow  {X}_{n - 1} \) is \( K\left( {{\pi }_{n}, n - 1}\right) \) .

This is the Whitehead tower of \( X \) . To construct \( {X}_{n} \) from \( {X}_{n - 1} \) , we first kill all \( {\pi }_{q}\left( {X}_{n - 1}\right) , q \geq  n + 1 \) , by attaching cells to \( {X}_{n - 1} \) . This gives a

\[
K\left( {{\pi }_{n}, n}\right)  = {X}_{n - 1} \cup  {e}^{n + 2} \cup  \ldots
\]

Next let \( {X}_{n} = {\Omega }_{ * }^{{X}_{n - 1}} \) be the space of all paths in \( K\left( {{\pi }_{n}, n}\right) \) from a base point * to \( {X}_{n - 1} \) . The endpoint map: \( {X}_{n} \rightarrow  {X}_{n - 1} \) has fiber \( {\Omega K}\left( {{\pi }_{n}, n}\right)  = K\left( {{\pi }_{n}, n - 1}\right) \) .

From the homotopy exact sequence of the fibering

\[
K\left( {{\pi }_{n}, n - 1}\right)  \rightarrow  {X}_{n}
\]

\[
{X}_{n - 1}
\]

it is readily checked that \( {\pi }_{q}\left( {X}_{n}\right)  = {\pi }_{q}\left( {X}_{n - 1}\right) \) for \( q \geq  n + 1 \) ; and \( {\pi }_{q}\left( {X}_{n}\right)  = 0 \) for \( q \leq  n - 2 \) ; furthermore,

(18.21)

\[
0 \rightarrow  {\pi }_{n}\left( {X}_{n}\right)  \rightarrow  {\pi }_{n}\left( {X}_{n - 1}\right) \overset{\partial }{ \rightarrow  }{\pi }_{n - 1}\left( {{\Omega K}\left( {{\pi }_{n}, n}\right) }\right)  \rightarrow  {\pi }_{n - 1}\left( {X}_{n}\right)  \rightarrow  0
\]

is exact. Here \( {\pi }_{n}\left( {X}_{n - 1}\right)  = {\pi }_{n} \) by the induction hypothesis, and the problem is to show that \( \partial  : {\pi }_{n}\left( {X}_{n - 1}\right)  \rightarrow  {\pi }_{n - 1}\left( {{\Omega K}\left( {{\pi }_{n}, n}\right) }\right) \) is an isomorphism. Now the inclusion \( {X}_{n - 1} \subset  K\left( {{\pi }_{n}, n}\right)  = {X}_{n - 1} \cup  {e}^{n + 2} \cup  \cdots \) induces by (17.11) an isomorphism

\[
{\pi }_{n}\left( {X}_{n - 1}\right)  \simeq  {\pi }_{n}\left( {K\left( {{\pi }_{n}, n}\right) }\right) .
\]

Moreover, the definition of the boundary map

\[
\partial  : {\pi }_{n}\left( {X}_{n - 1}\right)  \rightarrow  {\pi }_{n - 1}\left( {{\Omega K}\left( {{\pi }_{n}, n}\right) }\right)
\]

(see (17.4)) is precisely how \( {\pi }_{n}\left( {K\left( {{\pi }_{n}, n}\right) }\right) \) was identified with \( {\pi }_{n - 1}\left( {{\Omega K}\left( {{\pi }_{n}, n}\right) }\right) \) in Proposition 17.2. Therefore \( \partial \) is an isomorphism and \( {\pi }_{n}\left( {X}_{n}\right)  = {\pi }_{n - 1}\left( {X}_{n}\right)  = \) 0 in (18.21). This completes the construction of the Whitehead tower.

As a first application of the Whitehead tower we will prove Serre's theorem on the homotopy groups of the spheres. We call a sphere \( {S}^{n} \) odd or even according to whether \( n \) is odd or even.

Theorem 18.22 (Serre). The homotopy groups of an odd sphere \( {S}^{n} \) are torsion except in dimension \( n \) ; those of an even sphere \( {S}^{n} \) are torsion except in dimensions \( n \) and \( {2n} - 1 \) .

Proof. We will need to know that all homotopy groups of \( {S}^{n} \) are finitely generated. This is a consequence of Serre’s mod \( \mathcal{C} \) theory, with \( \mathcal{C} \) the class of finitely generated Abelian groups (see Serre [2] or Mosher and Tangora [1, Prop. 1, p. 95]). Assuming this, the essential facts to be used in the proof are the following:

(a) in the Whitehead tower of any space \( X,{\pi }_{q + 1}\left( X\right)  = {H}_{q + 1}\left( {X}_{q}\right) \) ; hence,

\[
{\pi }_{q + 1}\left( X\right)  \otimes  \mathbb{Q} = {H}_{q + 1}\left( {{X}_{q};\mathbb{Q}}\right) ;
\]

(b) the rational cohomology ring of \( K\left( {\pi , n}\right) \) is trivial for a torsion finitely generated Abelian group \( \pi \) and is free on one generator of dimension \( n \) for \( \pi  = \mathbb{Z} \) (Exercises 18.9 and 18.12).

Since \( {S}^{n} \) is \( \left( {n - 1}\right) \) -connected and \( {\pi }_{n}\left( {S}^{n}\right)  = \mathbb{Z} \) , the Whitehead tower begins with

\[
K\left( {\mathbb{Z}, n - 1}\right)  \rightarrow  {X}_{n}
\]

(18.22.1)

\[
\text{ ↓ }
\]

For the rest of this proof we write \( {\pi }_{q} \) for \( {\pi }_{q}\left( {S}^{n}\right) \) . First consider the case where \( n \) is odd. We will assume \( n \geq  3 \) . Then the rational cohomology of \( K\left( {\mathbb{Z}, n - 1}\right) \) is a polynomial algebra on one generator of dimension \( n - 1 \) and the cohomology spectral sequence of the fibration (18.22.1) has \( {E}_{2} \) term

![bo_d7b6f8alb0pc73dd9avg_265_546_515_579_292_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_265_546_515_579_292_0.jpg)

(Here we are using the cohomology spectral sequence to take advantage of the product structure.) The bottom arrow is an isomorphism because \( {H}_{n - 1}\left( {{X}_{n};\mathbb{Q}}\right)  = 0 \) ; the other arrows are isomorphisms by the product structure. From the spectral sequence we see that \( {X}_{n} \) has trivial rational cohomology, hence trivial rational homology. By Remark (a) above, \( {\pi }_{n + 1} \) is torsion. Now consider the next step of the Whitehead tower:

\[
K\left( {{\pi }_{n + 1}, n}\right)  \rightarrow  {X}_{n + 1}
\]

\[
{X}_{n}\text{ . }
\]

Since both \( {X}_{n} \) and \( K\left( {{\pi }_{n + 1}, n}\right) \) have trivial rational homology, so does \( {X}_{n + 1} \) . By Remark (a) again, \( {\pi }_{n + 2} = {H}_{n + 2}\left( {X}_{n + 1}\right) \) is torsion. By induction for all \( q \geq  n + 1,{X}_{q} \) has trivial rational homology and \( {\pi }_{q} \) is torsion.

Now suppose \( n \) is even. Then the rational cohomology of \( K\left( {\mathbb{Z}, n - 1}\right) \) is an exterior algebra and the \( {E}_{2} \) term of the rational homology sequence of the fibration (18.22.1) has only four nonzero boxes:

![bo_d7b6f8alb0pc73dd9avg_265_573_1585_555_329_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_265_573_1585_555_329_0.jpg)

The arrow shown is an isomorphism because \( {X}_{n} \) is \( n \) -connected. So

\[
{H}_{ * }\left( {{X}_{n};\mathbb{Q}}\right)  = \left\{  \begin{array}{ll} \mathbb{Q} & \text{ in dimensions }0,{2n} - 1 \\  0 & \text{ otherwise. } \end{array}\right.
\]

Suppose \( n > 2 \) . Then \( n + 1 < {2n} - 1 \) . By Remark (a), \( {\pi }_{n + 1} = {H}_{n + 1}\left( {X}_{n}\right) \) is torsion. Since \( {H}_{ * }\left( {K\left( {{\pi }_{n + 1}, n}\right) ;\mathbb{Q}}\right) \) is trivial, from the fibration

\[
K\left( {{\pi }_{n + 1}, n}\right)  \rightarrow  {X}_{n + 1}
\]

\[
{X}_{n}
\]

we conclude that \( {X}_{n + 1} \) has the same rational homology as \( {X}_{n} \) . This sets the induction going again, showing that \( {\pi }_{q} \) is torsion, until we hit \( {\pi }_{{2n} - 1} = \; {H}_{{2n} - 1}\left( {X}_{{2n} - 2}\right) \) , which is not torsion. In fact, \( {\pi }_{{2n} - 1} \) has one infinite cyclic generator and possibly some torsion generators. At this point we may assume \( n \geq  2 \) . By Remark (b), the rational cohomology ring

\[
{H}^{ * }\left( {K\left( {{\pi }_{{2n} - 1},{2n} - 2}\right) ;\mathbb{Q}}\right)
\]

is a polynomial algebra on one generator, so the cohomology \( {E}_{2} \) term of the fibration

\[
K\left( {{\pi }_{{2n} - 1},{2n} - 2}\right)  \rightarrow  {X}_{{2n} - 1}
\]

\[
{X}_{{2n} - 2}
\]

↓

is

![bo_d7b6f8alb0pc73dd9avg_266_553_1201_563_342_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_266_553_1201_563_342_0.jpg)

Since \( {H}_{{2n} - 1}\left( {X}_{{2n} - 1}\right)  = 0 \) , the arrows shown must all be isomorphisms. It follows that the rational cohomology groups of \( {X}_{q} \) are trivial for all \( q > {2n} - 1 \) and the homotopy groups \( {\pi }_{q}\left( {S}^{n}\right) \) are torsion for all \( q > {2n} - 1 \) .

Exercise 18.23. Give a proof of Theorem 18.22 based on the Postnikov approximation.

Computation of \( {\pi }_{5}\left( {S}^{3}\right) \)

If we try to compute \( {\pi }_{5}\left( {S}^{3}\right) \) using the Postnikov approximation, we very quickly run up against an ambiguity in the spectral sequence. For by (18.20), \( {\pi }_{5}\left( {S}^{3}\right)  = {H}_{6}\left( {Y}_{4}\right) \) , but to compute \( {H}_{6}\left( {Y}_{4}\right) \) from the homology spectral sequence of the fibering

![bo_d7b6f8alb0pc73dd9avg_267_263_371_797_510_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_267_263_371_797_510_0.jpg)

we will have to decide whether the arrow shown is the zero map or an isomorphism. With the tools at our disposal, this cannot be done. (For the homology of \( K\left( {{\mathbb{Z}}_{2},4}\right) \) and \( K\left( {\mathbb{Z},3}\right) \) see (18.16.1) and (18.11).)

In this case the Whitehead tower is more useful. Since \( {S}^{3} \) is 2-connected, the Whitehead tower up to \( {X}_{4} \) is

\[
K\left( {{\pi }_{4},3}\right)  \rightarrow  {X}_{4}
\]

\[
\text{ ↓ }
\]

\[
K\left( {\mathbb{Z},2}\right)  \rightarrow  {X}_{3}
\]

\[
\text{ ↓ }
\]

\[
{S}^{3}\text{ . }
\]

From the construction of the Whitehead tower and the Hurewicz isomorphism, \( {\pi }_{5}\left( {S}^{3}\right)  = {\pi }_{5}\left( {X}_{4}\right)  = {H}_{5}\left( {X}_{4}\right) \) . So we can get \( {\pi }_{5} \) by computing the homology of \( {X}_{4} \) . This method also gives \( {\pi }_{4}\left( {S}^{3}\right) \) , which is \( {H}_{4}\left( {X}_{3}\right) \) .

The cohomology of \( {X}_{3} \) may be computed from the spectral sequence of the fibration \( K\left( {\mathbb{Z},2}\right)  \rightarrow  {X}_{3} \rightarrow  {S}^{3} \) , whose \( {E}_{2} \) term is

![bo_d7b6f8alb0pc73dd9avg_267_555_1676_528_396_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_267_555_1676_528_396_0.jpg)

Since \( {d}_{2} \) is clearly zero, \( {E}_{2} = {E}_{3} \) . Next \( {d}_{3} : {E}_{3}^{0,2} \rightarrow  {E}_{3}^{3,0} \) is an isomorphism because \( {X}_{3} \) is 3-connected. By the antiderivation property of the differential \( {d}_{3} \) , which we will write as \( d \) here,

\[
d\left( {x}^{n}\right)  = n{x}^{n - 1}{dx} = n{x}^{n - 1}u.
\]

Hence the integral cohomology and homology of \( {X}_{3} \) are

<table><tr><td>\( q \)</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td></td></tr><tr><td>\( {H}^{q}\left( {X}_{3}\right) \)</td><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td><td>0</td><td>0</td><td>\( \mathbb{{Z}_{2}} \)</td><td>0</td><td>\( {\mathbb{Z}}_{3} \)</td><td>0</td><td>\( \mathbb{{Z}_{4}} \)</td><td>0</td><td>\( {\mathbb{Z}}_{5} \)</td><td></td></tr><tr><td>\( {H}_{q}\left( {X}_{3}\right) \)</td><td>\( \mathbb{Z} \)</td><td>0</td><td>0</td><td>0</td><td>\( {\mathbb{Z}}_{2} \)</td><td>0</td><td>\( {\mathbb{Z}}_{3} \)</td><td>0</td><td>\( \mathbb{{Z}_{4}} \)</td><td>0</td><td>\( \mathbb{{Z}_{5}} \)</td><td>0</td><td>日</td></tr></table>

where the homology is obtained from the cohomology by the universal coefficient theorem (15.14.1).

The homology spectral sequence of the fibration \( K\left( {{\pi }_{4},3}\right)  \rightarrow  {X}_{4} \rightarrow  {X}_{3} \) has \( {E}_{2} \) term

![bo_d7b6f8alb0pc73dd9avg_268_590_966_454_458_0.jpg](images/bo_d7b6f8alb0pc73dd9avg_268_590_966_454_458_0.jpg)

which shows that \( {\pi }_{4} = {\mathbb{Z}}_{2} \) , since \( {X}_{4} \) is 4-connected.

By Exercise 18.16, \( {H}_{4}\left( {K\left( {{\mathbb{Z}}_{2},3}\right) }\right)  = 0 \) and \( {H}_{5}\left( {K\left( {{\mathbb{Z}}_{2},3}\right) }\right)  = {\mathbb{Z}}_{2} \) . Since the only homomorphism from \( {\mathbb{Z}}_{3} \) to \( {\mathbb{Z}}_{2} \) is the zero map, \( {d}_{6} \) in the diagram above is zero. Hence \( {H}_{5}\left( {X}_{4}\right)  = {\mathbb{Z}}_{2} \) and \( {\pi }_{5}\left( {S}^{3}\right)  = {\pi }_{5}\left( {X}_{4}\right)  = {H}_{5}\left( {X}_{4}\right)  = {\mathbb{Z}}_{2} \) .

Exercise 18.24. Given a prime \( p \) , find the least \( q \) such that the homotopy group \( {\pi }_{q}\left( {S}^{3}\right) \) has \( p \) -torsion.
