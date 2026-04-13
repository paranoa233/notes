# Chapter 2 Definitions and Lemmas

Based on lecture notes by

M. Spivak and R. Wells

The words "smooth" and "differentiable" will be used interchangeably to mean differentiable of class \( {C}^{\infty } \) . The tangent space of a smooth manifold \( M \) at a point \( p \) will be denoted by \( T{M}_{p} \) . If \( g : M \rightarrow  N \) is a smooth map with \( g\left( p\right)  = q \) , then the induced linear map of tangent spaces will be denoted by \( {g}_{ * } : T{M}_{p} \rightarrow  T{N}_{q} \) .

Now let \( f \) be a smooth real valued function on a manifold \( M \) . A point \( p \in  M \) is called a critical point of \( f \) if the induced map \( {f}_{ * } : T{M}_{p} \rightarrow  T{\mathbf{R}}_{f\left( p\right) } \) is zero. If we choose a local coordinate system \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) in a neighborhood \( U \) of \( p \) this means that

\[
\frac{\partial f}{\partial {x}^{1}} = \cdots  = \frac{\partial f}{\partial {x}^{n}} = 0.
\]

The real number \( f\left( p\right) \) is called a critical value of \( f \) .

We denote by \( {M}^{a} \) the set of all points \( x \in  M \) such that \( f\left( x\right)  \leq  a \) . If \( a \) is not a critical value of \( f \) then it follows from the implicit function theorem that \( {M}^{a} \) is a smooth manifold with boundary. The boundary \( {f}^{-1}\left( a\right) \) is a smooth submanifold of \( M \) .

A critical point \( p \) is called non-degenerate if and only if the matrix

\[
\left( {\frac{{\partial }^{2}f}{\partial {x}^{i}\partial {x}^{j}}\left( p\right) }\right) \tag{2.1}
\]

is non-singular. It can be checked directly that non-degeneracy does not depend on the coordinate system. This will follow also from the following intrinsic definition.

If \( p \) is a critical point of \( f \) we define a symmetric bilinear functional \( {f}_{* * } \) on \( T{M}_{p} \) , called the Hessian of \( f \) at \( p \) . If \( v, w \in  T{M}_{p} \) then \( v \) and \( w \) have extensions \( \widetilde{v} \) and \( \widetilde{w} \) to vector fields. We let \( {}^{1}{f}_{* * }\left( {v, w}\right)  = {\widetilde{v}}_{p}\left( {\widetilde{w}\left( f\right) }\right) \) , where \( {\widetilde{v}}_{P} \) is, of course, just \( v \) . We must show that this is symmetric and well-defined. It is symmetric because

\[
{\widetilde{v}}_{p}\left( {\widetilde{w}\left( f\right) }\right)  - {\widetilde{w}}_{p}\left( {\widetilde{v}\left( f\right) }\right)  = {\left\lbrack  \widetilde{v},\widetilde{w}\right\rbrack  }_{p}\left( f\right)  = 0,
\]

where \( \left\lbrack  {\widetilde{v},\widetilde{w}}\right\rbrack \) is the Poisson bracket of \( \widetilde{v} \) and \( \widetilde{w} \) , and where \( {\left\lbrack  \widetilde{v},\widetilde{w}\right\rbrack  }_{p}\left( f\right)  = 0 \) since \( f \) has \( p \) as a critical point.

Therefore \( {f}_{* * } \) is symmetric. It is now clearly well-defined since \( {\widetilde{v}}_{p}\left( {\widetilde{w}\left( f\right) }\right)  = \; {v}_{p}\left( {\widetilde{w}\left( f\right) }\right) \) is independent of the extension \( \widetilde{v} \) of \( v \) , while \( {\widetilde{w}}_{p}\left( {\widetilde{v}\left( f\right) }\right) \) is independent of \( \widetilde{w} \) .

---

\( {}^{1} \) Here \( \widetilde{w}\left( f\right) \) denotes the directional derivative of \( f \) in the direction \( \widetilde{w} \) .

---

If \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is a local coordinate system and \( v = \sum {a}_{i}\partial /{\left. \partial {x}^{i}\right| }_{p}, w = \sum {b}_{j}\partial /{\left. \partial {x}^{j}\right| }_{p} \) we can take \( \widetilde{w} = \sum {b}_{j}\partial /{\left. \partial {x}^{j}\right| }_{p} \) where \( {b}_{j} \) now denotes a constant function. Then

\[
{f}_{* * }\left( {v, w}\right)  = v\left( {\widetilde{w}\left( f\right) }\right) \left( p\right)  = v\left( {\sum {b}_{j}\frac{\partial f}{\partial {x}^{j}}}\right)  = \mathop{\sum }\limits_{{i, j}}{a}_{i}{b}_{j}\frac{{\partial }^{2}f}{\partial {x}^{i}\partial {x}^{j}};
\]

so the matrix (2.1) represents the bilinear function \( {f}_{* * } \) with respect to the basis \( \partial /{\left. \partial {x}^{1}\right| }_{p},\ldots ,\partial /{\left. \partial {x}^{n}\right| }_{p} \) .

We can now talk about the index and the nullity of the bilinear functional \( {f}_{* * } \) on \( T{M}_{p} \) . The index of a bilinear functional \( H \) , on a vector space \( V \) , is defined to be the maximal dimension of a subspace of \( V \) on which \( H \) is negative definite; the nullity is the dimension of the null-space, i.e., the subspace consisting of all \( v \in  V \) such that \( H\left( {v, w}\right)  = 0 \) for every \( w \in  V \) . The point \( p \) is obviously a non-degenerate critical point of \( f \) if and only if \( {f}_{* * } \) on \( T{M}_{p} \) has nullity equal to 0 . The index of \( {f}_{* * } \) on \( T{M}_{p} \) will be referred to simply as the index of \( f \) at \( p \) . The Lemma of Morse shows that the behaviour of \( f \) at \( p \) can be completely described by this index. Before stating this lemma we first prove the following:

Lemma 2.1. Let \( f \) be a \( {C}^{\infty } \) function in a convex neighborhood \( V \) of 0 in \( {\mathbf{R}}^{n} \) , with \( f\left( 0\right)  = 0 \) . Then

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{g}_{i}\left( {{x}_{1},\ldots ,{x}_{n}}\right) ,
\]

for some suitable \( {C}^{\infty } \) functions \( {g}_{i} \) defined in \( V \) , with \( {g}_{i}\left( o\right)  = \frac{\partial f}{\partial {x}_{i}}\left( 0\right) \) .

Proof.

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = {\int }_{0}^{1}\frac{\mathrm{d}f\left( {t{x}_{1},\ldots , t{x}_{n}}\right) }{\mathrm{d}t}\mathrm{\;d}t = {\int }_{0}^{1}\mathop{\sum }\limits_{{i = 1}}^{n}\frac{\partial f}{\partial {x}_{i}}\left( {t{x}_{1},\ldots , t{x}_{n}}\right)  \cdot  {x}_{i}\mathrm{\;d}t.
\]

Therefore we can let \( {g}_{i}\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = {\int }_{0}^{1}\partial f/\partial {x}_{i}\left( {t{x}_{1},\ldots , t{x}_{n}}\right) \mathrm{d}t \) .

Lemma 2.2 (Lemma of Morse). Let \( p \) be a non-degenerate critical point for \( f \) . Then there is a local coordinate system \( \left( {{y}^{1},\ldots ,{y}^{n}}\right) \) in a neighborhood \( U \) of \( p \) with \( {y}^{i}\left( p\right)  = 0 \) for all \( i \) and such that the identity

\[
f = f\left( p\right)  - {\left( {y}^{1}\right) }^{2} - \cdots  - {\left( {y}^{\lambda }\right) }^{2} + {\left( {y}^{\lambda  + 1}\right) }^{2} + \cdots  + {\left( {y}^{n}\right) }^{2}
\]

holds throughout \( U \) , where \( \lambda \) is the index of \( f \) at \( p \) .

Proof. We first show that if there is any such expression for \( f \) , then \( \lambda \) must be the index of \( f \) at \( p \) . For any coordinate system \( \left( {{z}^{1},\ldots ,{z}^{n}}\right) \) , if

\[
f\left( q\right)  = f\left( p\right)  - {\left( {z}^{1}\left( q\right) \right) }^{2} - \cdots  - {\left( {z}^{\lambda }\left( q\right) \right) }^{2} + {\left( {z}^{\lambda  + 1}\left( q\right) \right) }^{2} + \cdots  + {\left( {z}^{n}\left( q\right) \right) }^{2}
\]

then we have

\[
\frac{{\partial }^{2}f}{\partial {z}^{i}\partial {z}^{j}}\left( p\right)  = \left\{  \begin{array}{lll}  - 2 & \text{ if } & i = j \leq  \lambda , \\  2 & \text{ if } & i = j > \lambda , \\  0 & \text{ otherwise, } &  \end{array}\right.
\]

which shows that the matrix representing \( {f}_{* * } \) with respect to the basis \( \partial /{\left. \partial {z}^{1}\right| }_{p},\ldots ,\partial /{\left. \partial {z}^{n}\right| }_{p} \) is

\[
\left( \begin{matrix}  - 2 & & & & & \\   &  \ddots  & & & & \\   & &  - 2 & & & \\   & & & 2 & & \\   & & & &  \ddots  & \\   & & & & & 2 \end{matrix}\right)
\]

Therefore there is a subspace of \( T{M}_{p} \) of dimension \( \lambda \) where \( {f}_{* * } \) is negative definite, and a subspace \( V \) of dimension \( n - \lambda \) where \( {f}_{* * } \) is positive definite. If there were a subspace of \( T{M}_{p} \) of dimension greater than \( \lambda \) on which \( {f}_{* * } \) were negative definite then this subspace would intersect \( V \) , which is clearly impossible. Therefore \( \lambda \) is the index of \( {f}_{* * } \) .

We now show that a suitable coordinate system \( \left( {{y}^{1},\ldots ,{y}^{n}}\right) \) exists. Obviously we can assume that \( p \) is the origin of \( {\mathbf{R}}^{n} \) and that \( f\left( p\right)  = f\left( 0\right)  = 0 \) . By Lemma 2.1 we can write

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{j = 1}}^{n}{x}_{j}{g}_{j}\left( {{x}_{1},\ldots ,{x}_{n}}\right)
\]

for \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) in some neighborhood of 0 . Since 0 is assumed to be a critical point:

\[
{g}_{j}\left( 0\right)  = \frac{\partial f}{\partial {x}^{j}}\left( 0\right)  = 0.
\]

Therefore, applying Lemma 2.1 to the \( {g}_{j} \) we have

\[
{g}_{j}\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{h}_{ij}\left( {{x}_{1},\ldots ,{x}_{n}}\right)
\]

for certain smooth functions \( {h}_{ij} \) . It follows that

\[
f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = \mathop{\sum }\limits_{{i, j = 1}}^{n}{x}_{i}{x}_{j}{h}_{ij}\left( {{x}_{1},\ldots ,{x}_{n}}\right) .
\]

We can assume that \( {h}_{ij} = {h}_{ji} \) , since we can write \( {\bar{h}}_{ij} = \frac{1}{2}\left( {{h}_{ij} + {h}_{ji}}\right) \) , and then have \( {\bar{h}}_{ij} = {\bar{h}}_{ji} \) and \( f = \sum {x}_{i}{x}_{j}{\bar{h}}_{ij} \) . Moreover the matrix \( \left( {{\bar{h}}_{ij}\left( 0\right) }\right) \) is equal to

\[
\left( {\frac{1}{2}\frac{{\partial }^{2}f}{\partial {x}^{i}\partial {x}^{j}}\left( 0\right) }\right) ,
\]

and hence is non-singular.

There is a non-singular transformation of the coordinate functions which gives us the desired expression for \( f \) , in a perhaps smaller neighborhood of 0 . To see this we just imitate the usual diagonalization proof for quadratic forms. (See for example, [BML65, p. 271].) The key step can be described as follows:

Suppose by induction that there exist coordinates \( {u}_{1},\ldots ,{u}_{n} \) in a neighborhood \( {U}_{1} \) of 0 so that

\[
f =  \pm  {\left( {u}_{1}\right) }^{2} \pm  \cdots  \pm  {\left( {u}_{r - 1}\right) }^{2} + \mathop{\sum }\limits_{{i, j \geq  r}}{u}_{i}{u}_{j}{H}_{ij}\left( {{u}_{1},\ldots ,{u}_{n}}\right)
\]

throughout \( {U}_{1} \) ; where the matrices \( \left( {{H}_{ij}\left( {{u}_{1},\ldots ,{u}_{n}}\right) }\right) \) are symmetric. After a linear change in the last \( n - r + 1 \) coordinates we may assume that \( {H}_{rr} \neq  0 \) . Let \( g\left( {{u}_{1},\ldots ,{u}_{n}}\right) \) denote the square root of \( \left| {{H}_{rr}\left( {{u}_{1},\ldots ,{u}_{n}}\right) }\right| \) . This will be a smooth, non-zero function of \( {u}_{1},\ldots ,{u}_{n} \) throughout some smaller neighborhood \( {U}_{2} \subset  {U}_{1} \) of 0 . Now introduce new coordinates \( {v}_{1},\ldots ,{v}_{n} \) by

\[
{v}_{i} = {u}_{i}\;\text{ for }\;i \neq  r
\]

\[
{v}_{r}\left( {{u}_{1},\ldots ,{u}_{n}}\right)  = g\left( {{u}_{1},\ldots ,{u}_{n}}\right) \left( {{u}_{r} + \mathop{\sum }\limits_{{i > r}}{u}_{i}\frac{{H}_{ir}\left( {{u}_{1},\ldots ,{u}_{n}}\right) }{{H}_{rr}\left( {{u}_{1},\ldots ,{u}_{n}}\right) }}\right) .
\]

It follows from the inverse function theorem that \( {v}_{1},\ldots ,{v}_{n} \) will serve as coordinate functions within some sufficiently small neighborhood \( {U}_{3} \) of 0 . It is easily verified that \( f \) can be expressed as

\[
f = \mathop{\sum }\limits_{{i \leq  r}} \pm  {\left( {v}_{i}\right) }^{2} + \mathop{\sum }\limits_{{i, j \geq  r}}{v}_{i}{v}_{j}{H}_{ij}^{\prime }\left( {{v}_{1},\ldots ,{v}_{n}}\right)
\]

throughout \( {U}_{3} \) . This completes the induction; and proves Lemma 8.3.

Corollary 2.3. Non-degenerate critical points are isolated.

Examples of degenerate critical points (for functions on \( \mathbf{R} \) and \( {\mathbf{R}}^{2} \) ) are given below, together with pictures of their graphs.

We conclude this section with a discussion of 1-parameter groups of diffeomor-phisms. The reader is referred to K. Nomizu,"Lie Groups and Differential Geometry," for more details.

A 1-parameter group of diffeomorphisms of a manifold \( M \) is a \( {C}^{\infty } \) map

\[
\varphi  : \mathbf{R} \times  M \rightarrow  M
\]

such that

(1) for each \( t \in  \mathbf{R} \) the map \( {\varphi }_{t} : \mathbf{R} \times  M \rightarrow  M \) defined by \( {\varphi }_{t}\left( q\right)  = \varphi \left( {t, q}\right) \) is a diffeomorphism of \( M \) onto itself,

(2) for all \( t, s \in  \mathbf{R} \) we have \( {\varphi }_{t + s} = {\varphi }_{t} \circ  {\varphi }_{s} \) .

Given a 1-parameter group \( \varphi \) of diffeomorphisms of \( M \) we define a vector field \( X \) on \( M \) as follows. For every smooth real valued function \( f \) let

\[
{X}_{q}\left( f\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{\varphi }_{h}\left( q\right) }\right)  - f\left( q\right) }{h}.
\]

This vector field \( X \) is said to generate the group \( \varphi \) .

Lemma 2.4. A smooth vector field on \( M \) which vanishes outside of a compact set \( K \subset  M \) generates a unique 1- parameter group of diffeomorphisms of \( M \) .

![bo_d7du90alb0pc73deir8g_18_243_432_577_349_0.jpg](images/bo_d7du90alb0pc73deir8g_18_243_432_577_349_0.jpg)

(a) \( f\left( x\right)  = {\mathrm{e}}^{-\frac{1}{{x}^{2}}}{\sin }^{2}\left( \frac{1}{x}\right) \) . The origin is a degenerate, and non-isolated, critical point.

![bo_d7du90alb0pc73deir8g_18_954_436_446_363_0.jpg](images/bo_d7du90alb0pc73deir8g_18_954_436_446_363_0.jpg)

(b) \( f\left( x\right)  = {x}^{3} \) . The origin is a degenerate critical

point

![bo_d7du90alb0pc73deir8g_18_338_906_381_347_0.jpg](images/bo_d7du90alb0pc73deir8g_18_338_906_381_347_0.jpg)

(c) \( f\left( {x, y}\right)  = {x}^{3} - {3x}{y}^{2} = \) Real part of \( {\left( x + iy\right) }^{3} \) . \( \left( {0,0}\right) \) is a degenerate critical point (a "monkey saddle").

![bo_d7du90alb0pc73deir8g_18_993_910_367_305_0.jpg](images/bo_d7du90alb0pc73deir8g_18_993_910_367_305_0.jpg)

(d) \( f\left( {x, y}\right)  = {x}^{2}{y}^{2} \) . The set of critical points, all of which are degenerate, consists of the union of the \( x \) and \( y \) axis, which is not even a sub-manifold of \( {\mathbf{R}}^{2} \) .

![bo_d7du90alb0pc73deir8g_18_576_1429_500_395_0.jpg](images/bo_d7du90alb0pc73deir8g_18_576_1429_500_395_0.jpg)

(e) \( f\left( {x, y}\right)  = {x}^{2} \) . The set of critical points, all of which are degenerate, is the \( x \) axis, which is a sub-manifold of \( {\mathbf{R}}^{2} \) .

Proof. Given any smooth curve

\[
t \mapsto  c\left( t\right)  \in  M
\]

it is convenient to define the velocity vector

\[
\frac{\mathrm{d}c}{\mathrm{\;d}t} \in  T{M}_{c\left( t\right) }
\]

by the identity

\[
\frac{\mathrm{d}c}{\mathrm{\;d}t}\left( f\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{{f}_{c}\left( {t + h}\right)  - {f}_{c}\left( t\right) }{h}.
\]

(Compare Chapter 8.) Now let \( \varphi \) be a 1-parameter group of diffeomorphisms, generated by the vector field \( X \) . Then for each fixed \( q \) the curve

\[
t \mapsto  {\varphi }_{t}\left( q\right)
\]

satisfies the differential equation

\[
\frac{\mathrm{d}{\varphi }_{t}\left( q\right) }{\mathrm{d}t} = {X}_{{\varphi }_{t}}\left( q\right)
\]

with initial condition \( {\varphi }_{0}\left( q\right)  = q \) . This is true since

\[
\frac{\mathrm{d}{\varphi }_{t}\left( q\right) }{\mathrm{d}t}\left( f\right)  = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{\varphi }_{t + h}\left( q\right) }\right)  - f\left( {{\varphi }_{t}\left( q\right) }\right) }{h} = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{f\left( {{\varphi }_{h}\left( p\right) }\right)  - f\left( p\right) }{h} = {X}_{p}\left( f\right) ,
\]

where \( p = {\varphi }_{t}\left( q\right) \) . But it is well known that such a differential equation, locally, has a unique solution which depends smoothly on the initial condition. (Compare [Gra56, p. 166]. Note that, in terms of local coordinates \( {u}^{1},\ldots ,{u}^{n} \) , the differential equation takes on the more familiar form: \( \mathrm{d}{u}^{i}/\mathrm{d}t = {x}^{i}\left( {{u}^{1},\ldots ,{u}^{n}}\right) , i = 1,\ldots , n \) .)

Thus for each point of \( M \) there exists a neighborhood \( U \) and a number \( \varepsilon  > 0 \) so that the differential equation

\[
\frac{\mathrm{d}{\varphi }_{t}\left( q\right) }{\mathrm{d}t} = {X}_{{\varphi }_{t}}\left( q\right) ,\;{\varphi }_{0}\left( q\right)  = q
\]

has a unique smooth solution for \( q \in  U,\left| t\right|  < \varepsilon \) .

The compact set \( K \) can be covered by a finite number of such neighborhoods \( U \) . Let \( {\varepsilon }_{0} > 0 \) denote the smallest of the corresponding numbers \( \varepsilon \) . Setting \( {\varphi }_{t}\left( q\right)  = q \) for \( q \notin  K \) , it follows that this differential equation has a unique solution \( {\varphi }_{t}\left( q\right) \) for \( \left| t\right|  < {\varepsilon }_{0} \) and for all \( q \in  M \) . This solution is smooth as a function of both variables. Furthermore, it is clear that \( {\varphi }_{t + s} = {\varphi }_{t} \circ  {\varphi }_{s} \) providing that \( \left| t\right| ,\left| s\right| ,\left| {t + s}\right|  < {\varepsilon }_{0} \) . Therefore each such \( {\varphi }_{t} \) is a diffeomorphism.

It only remains to define \( {\varphi }_{t} \) for \( \left| t\right|  \geq  {\varepsilon }_{0} \) . Any number \( t \) can be expressed as a multiple of \( {\varepsilon }_{0}/2 \) plus a remainder \( r \) with \( \left| r\right|  < {\varepsilon }_{0}/2 \) . If \( t = k\left( {{\varepsilon }_{0}/2}\right)  + r \) with \( k \geq  0 \) , set

\[
{\varphi }_{t} = {\varphi }_{{\varepsilon }_{0}/2} \circ  {\varphi }_{{\varepsilon }_{0}/2} \circ  \cdots  \circ  {\varphi }_{{\varepsilon }_{0}/2} \circ  {\varphi }_{r}
\]

where the transformation \( {\varphi }_{{\varepsilon }_{0}/2} \) is iterated \( k \) times. If \( k < 0 \) it is only necessary to replace \( {\varphi }_{{\varepsilon }_{0}/2} \) by \( {\varphi }_{-{\varepsilon }_{0}/2} \) iterated \( - k \) times. Thus \( {\varphi }_{t} \) is defined for all values of \( t \) . It is not difficult to verify that \( {\varphi }_{t} \) is well defined, smooth, and satisfies the condition \( {\varphi }_{t + s} = {\varphi }_{t} \circ  {\varphi }_{s} \) . This completes the proof of Lemma 2.4

Remark. The hypothesis that \( X \) vanishes outside of a compact set cannot be omitted. For example let \( M \) be the open unit interval \( \left( {0,1}\right)  \subset  \mathbf{R} \) , and let \( X \) be the standard vector field \( \mathrm{d}/\mathrm{d}t \) on \( M \) . Then \( X \) does not generate any 1-parameter group of diffeomorphisms of \( M \) .
