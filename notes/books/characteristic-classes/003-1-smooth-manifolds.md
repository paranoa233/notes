# 1 Smooth Manifolds

This section contains a brief introduction to the theory of smooth manifolds and their tangent spaces.

Let \( {\mathbb{R}}^{n} \) denote the coordinate space consisting of all \( n \) -tuples \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) of real numbers. For the special case \( n = 0 \) it is to be understood that \( {\mathbb{R}}^{0} \) consists of a single point. The real numbers themselves will be denoted by \( \mathbb{R} \) .

The word "smooth" will be used as a synonym for "differentiable of class \( {C}^{\infty } \) ." Thus a function defined on an open set \( U \subset  {\mathbb{R}}^{n} \) with values in \( {\mathbb{R}}^{k} \) is "smooth" if its partial derivatives of all orders exist and are continuous.

For some purposes it is convenient to use a coordinate space \( {\mathbb{R}}^{A} \) which may be infinite dimensional. Let \( A \) be any index set and let \( {\mathbb{R}}^{A} \) denote the vector space consisting of all functions \( {}^{1}x \) from \( A \) to \( \mathbb{R} \) . The value of a vector \( x \in  {\mathbb{R}}^{A} \) on \( \alpha  \in  A \) will be denoted by \( {x}_{\alpha } \) and called the \( \alpha \) -th coordinate of \( x \) . Similarly, for any function \( f : Y \rightarrow  {\mathbb{R}}^{A} \) , the \( \alpha \) -th coordinate of \( f\left( y\right) \) will be denoted \( {f}_{\alpha }\left( y\right) \) .

We topologize this space \( {\mathbb{R}}^{A} \) as a Cartesian product of copies of \( \mathbb{R} \) . For any subset \( M \subset  {\mathbb{R}}^{A} \) , we give \( M \) the relative topology. Thus a function \( f : Y \rightarrow  M \subset  {\mathbb{R}}^{A} \) is continuous if and only if each of the associated functions \( {f}_{\alpha } : Y \rightarrow  \mathbb{R} \) are continuous. Here \( Y \) can be an arbitrary topological space.

Definition. For \( U \subset  {\mathbb{R}}^{n} \) , a function \( f : U \rightarrow  M \subset  {\mathbb{R}}^{A} \) is said to be smooth if each of the associated functions \( {f}_{\alpha } : U \rightarrow  \mathbb{R} \) is smooth. If \( f \) is smooth, then the partial derivative \( \partial f/\partial {u}_{i} \) can be defined as the smooth function \( U \rightarrow  {\mathbb{R}}^{A} \) whose \( \alpha \) -th coordinate is \( \partial {f}_{\alpha }/\partial {u}_{i} \) for \( i = 1,2,\ldots , n \) .

The most classical and familiar examples of smooth manifolds are curves and surfaces in the coordinate space \( {\mathbb{R}}^{3} \) . Generalizing the classical description of curves and surfaces, we will consider \( n \) -dimensional objects in a coordinate space \( {\mathbb{R}}^{A} \) .

---

\( {}^{1} \) Of course our previous coordinate space \( {\mathbb{R}}^{n} \) can be obtained as a special case of this more general concept, simply by taking \( A \) to be the set of integers between 1 and \( n \) .

---

Definition. A subset \( M \subset  {\mathbb{R}}^{A} \) is a smooth manifold of dimension \( n \geq  0 \) if, for each \( x \in  M \) there exists a smooth function

\[
h : U \rightarrow  {\mathbb{R}}^{A}
\]

defined on an open set \( U \subset  {\mathbb{R}}^{n} \) such that

1) \( h \) maps \( U \) homeomorphically onto an open neighborhood \( V \) of \( x \) in \( \mathrm{M} \) , and

2) for each \( u \in  U \) the matrix \( \left\lbrack  {\partial {h}_{\alpha }\left( u\right) /\partial {u}_{j}}\right\rbrack \) has rank \( n \) . (In other words the \( n \) vectors \( \partial h/\partial {u}_{1},\ldots ,\partial h/\partial {u}_{n} \) , evaluated at \( u \) , must be linearly independent.)

The image \( h\left( U\right)  = V \) of such a mapping will be called a coordinate neighborhood in \( M \) , and the triple \( \left( {U, V, h}\right) \) will be called a local parameterization \( {}^{2} \) of \( M \) .

Lemma 1.1. Let \( \left( {U, V, h}\right) \) and \( \left( {{U}^{\prime },{V}^{\prime },{h}^{\prime }}\right) \) be two local parameterizations of \( M \) such that \( V \cap  {V}^{\prime } \) is non-vacuous. Then the correspondence

\[
{u}^{\prime } \mapsto  {h}^{-1}\left( {{h}^{\prime }\left( {u}^{\prime }\right) }\right)
\]

defines a smooth mapping from the open set \( {\left( {h}^{\prime }\right) }^{-1}\left( {V \cap  {V}^{\prime }}\right)  \subset  {\mathbb{R}}^{n} \) to the open set \( {h}^{-1}\left( {V \cap  {V}^{\prime }}\right)  \subset  {\mathbb{R}}^{n} \) .

Proof. Let \( \bar{x} = h\left( \bar{u}\right)  = h\left( {\bar{u}}^{\prime }\right) \) be an arbitrary point of \( V \cap  {V}^{\prime } \) . Choose indices \( {\alpha }_{1},\ldots ,{\alpha }_{n} \in  A \) so that the \( n \times  n \) matrix \( \left\lbrack  {\partial {h}_{{\alpha }_{i}}/\partial {u}_{j}}\right\rbrack \) , evaluated at \( \bar{u} \) , is nonsingular. Then it follows from the inverse function theorem that one can solve for \( {u}_{1},\ldots ,{u}_{n} \) as smooth functions

\[
{u}_{j} = {f}_{j}\left( {{h}_{{\alpha }_{1}}\left( u\right) ,\ldots ,{h}_{{\alpha }_{n}}\left( u\right) }\right)
\]

---

\( {}^{2} \) The inverse \( {h}^{-1} : V \rightarrow  U \subset  \overline{{\mathbb{R}}^{n}} \) is often called a "local coordinate system" or "chart" for \( M \) .

---

for some \( u \) in some neighborhood of \( \bar{u} \) . (See for example [Whi57, p.69].) Writing these equations in vector notation as \( u = f\left( {{h}_{{\alpha }_{1}}\left( u\right) ,\ldots ,{h}_{{\alpha }_{n}}\left( u\right) }\right) \) , and setting \( h\left( u\right)  = {h}^{\prime }\left( {u}^{\prime }\right) \) , it follows that the function

\[
{u}^{\prime } \mapsto  {h}^{-1}{h}^{\prime }\left( {u}^{\prime }\right)  = f\left( {{h}_{{\alpha }_{1}}^{\prime }\left( u\right) ,\ldots ,{h}_{{\alpha }_{n}}^{\prime }\left( u\right) }\right)
\]

is smooth throughout some neighborhood of \( {u}^{\prime } \) . This completes the proof.

The concept of a tangent vector can be defined as follows. Let \( \bar{x} \) be a fixed point of \( M \) , and let \( \left( {-\epsilon ,\epsilon }\right) \) denote the set of real numbers \( t \) with \( - \epsilon  < t < \epsilon \) . A smooth path through \( \bar{x} \) in \( M \) will mean a smooth function

\[
p : \left( {-\epsilon ,\epsilon }\right)  \rightarrow  M \subset  {\mathbb{R}}^{A}
\]

defined on some interval \( \left( {-\epsilon ,\epsilon }\right) \) of real numbers, with \( p\left( 0\right)  = \bar{x} \) . The velocity vector of such a path is defined to be the vector

\[
{\left. \frac{\mathrm{d}p}{\mathrm{\;d}t}\right| }_{t = 0} \in  {\mathbb{R}}^{A}
\]

whose \( \alpha \) -th component is \( \mathrm{d}{p}_{\alpha }/\mathrm{d}t \) . (Compare Figure 1.)

Definition. A vector \( v \in  {\mathbb{R}}^{A} \) is tangent to \( M \) at \( x \) if \( v \) can be expressed as the velocity vector of some smooth path through \( x \) in \( M \) . The set of all such tangent vectors will be called the tangent space of \( M \) at \( x \) , and will be denoted \( {\mathbf{T}}_{x}M \) . (In some presentations, the vector \( v \) is identified with the collection of paths \( p \) with common velocity vector \( v \) . This allows an intrinsic definition of tangent vector independent of the embedding in \( {\mathbb{R}}^{A} \) .)

In terms of local parameterization \( \left( {U, V, h}\right) \) with \( h\left( \bar{u}\right)  = \bar{x} \) , the tangent space can be described as follows.

Lemma 1.2. A vector \( v \in  {\mathbb{R}}^{A} \) is tangent to \( M \) at \( \bar{x} \) if and only if \( v \) can be expressed as a linear combination of the vectors

\[
\frac{\partial h}{\partial {u}_{1}}\left( \bar{u}\right) ,\ldots ,\frac{\partial h}{\partial {u}_{n}}\left( \bar{u}\right) .
\]

Thus \( {\mathbf{T}}_{\bar{x}}M \) is an \( n \) -dimensional vector space over the real numbers.

The proof is straightforward.

![bo_d7du9galb0pc73deir9g_15_277_370_997_834_0.jpg](images/bo_d7du9galb0pc73deir9g_15_277_370_997_834_0.jpg)

Figure 1

The tangent manifold of \( M \) is defined to be the subspace

\[
\mathbf{{TM}} \subset  M \times  {\mathbb{R}}^{A}
\]

consisting of all pairs \( \left( {x, v}\right) \) with \( x \in  M \) and \( v \in  {\mathbf{T}}_{x}M \) . It follows easily from Lemma 1.2 that \( \mathbf{T}M \) , considered as a subset of \( {\mathbb{R}}^{A} \times  {\mathbb{R}}^{A} \) , is a smooth manifold of dimension \( {2n} \) .

Now consider two smooth manifolds \( M \subset  {\mathbb{R}}^{A} \) and \( N \subset  {\mathbb{R}}^{B} \) , and a function \( f : M \rightarrow  N \) . Let \( \bar{x} \) be a point of \( M \) and \( \left( {U, V, h}\right) \) a local parameterization of \( M \) with \( \bar{x} = h\left( \bar{u}\right) \) .

Definition. The function \( f \) is said to be smooth at \( \bar{x} \) if the composition \( {}^{3} \)

\[
f \circ  h : U \rightarrow  N \subset  {\mathbb{R}}^{B}
\]

is smooth throughout some neighborhood of \( \bar{u} \) .

It follows from Lemma 1.1 that this definition does not depend on the choice of local parameterization.

Definition. The function \( f : M \rightarrow  N \) is smooth if it is smooth at every point \( x \in  M \) . A function \( f : M \rightarrow  N \) is called a diffeomorphism if \( f \) is one-to-one onto, and if both \( f \) and the inverse function \( {f}^{-1} : N \rightarrow  M \) are smooth.

Lemma 1.3. The identity map of \( M \) is always smooth. Furthermore the composition of two smooth maps \( M\overset{g}{ \rightarrow  }{M}^{\prime }\overset{f}{ \rightarrow  }{M}^{\prime \prime } \) is smooth.

The proof is similar to that of 1.1. Details will be omitted.

Any map \( f : M \rightarrow  N \) which is smooth at \( x \) determines a linear map \( \mathrm{d}{f}_{x} \) from the tangent space \( {\mathbf{T}}_{x}M \) to \( {\mathbf{T}}_{f\left( x\right) }N \) as follows. Given \( v \in  {\mathbf{T}}_{x}M \) express \( v \) as the velocity vector

\[
v = {\left. \frac{\mathrm{d}p}{\mathrm{\;d}t}\right| }_{t = 0}
\]

of some smooth path through \( x \) in \( M \) , and define \( \mathrm{d}{f}_{x}\left( v\right) \) to be the velocity vector

\[
{\left. \frac{\mathrm{d}\left( {f \circ  p}\right) }{\mathrm{d}t}\right| }_{t = 0}
\]

of the image path \( f \circ  p : \left( {-\epsilon ,\epsilon }\right)  \rightarrow  N \) . It is easily seen that this definition does not depend on the choice of \( p \) , and that \( \mathrm{d}{f}_{x} \) is a linear mapping. In fact, in terms of a local parameterization \( \left( {U, V, h}\right) \) , one has the explicit formula

\[
\mathrm{d}{f}_{x}\left( {\sum {c}_{i}\frac{\partial h}{\partial {u}_{i}}}\right)  = \sum {c}_{i}\frac{\partial \left( {f \circ  h}\right) }{\partial {u}_{i}},
\]

for any real numbers \( {c}_{1},\ldots ,{c}_{n} \) .

Definition. The linear transformation \( \mathrm{d}{f}_{x} \) is called the derivative, or the Jacobian of \( f \) at \( x \) .

---

\( {}^{3} \) The notation \( f \circ  g \) will be used for the composition of two functions \( X\overset{g}{ \rightarrow  }Y\overset{f}{ \rightarrow  }Z \) .

---

Now suppose that \( f : M \rightarrow  N \) is smooth everywhere. Combining all of the Jacobians \( \mathrm{d}{f}_{x} \) one obtains the function

\[
\mathrm{d}f : \mathbf{T}M \rightarrow  \mathbf{T}N
\]

where \( \mathrm{d}f\left( {x, v}\right)  = \left( {f\left( x\right) ,\mathrm{d}{f}_{x}\left( v\right) }\right) \) .

Lemma 1.4. \( \mathbf{T} \) is a functor \( {}^{4} \) from the category of smooth manifolds and smooth maps into itself.

In other words:

(1) If \( M \) is a smooth manifold, then \( \mathbf{T}M \) is a smooth manifold.

(2) If \( f \) is a smooth map from \( M \) to \( N \) then \( \mathrm{d}f \) is a smooth map from \( \mathbf{T}M \) to \( \mathbf{T}N \) .

(3) If \( I \) is the identity map of \( M \) then \( \mathrm{d}I \) is the identity map of \( \mathbf{T}M \) ; and

(4) If the composition \( f \circ  g \) of two smooth maps is defined, then

\[
\mathrm{d}\left( {f \circ  g}\right)  = \left( {\mathrm{d}f}\right)  \circ  \left( {\mathrm{d}g}\right) .
\]

The proofs are straightforward.

One immediate consequence is the following: If \( f \) is a diffeomorphism from \( M \) to \( N \) then \( \mathrm{d}f \) is a diffeomorphism from \( \mathbf{T}M \) to \( \mathbf{T}N \) .

Remarks. According to our definitions, the tangent space \( {\mathbf{T}}_{x}{\mathbb{R}}^{n} \) of the coordinate space \( {\mathbb{R}}^{n} \) at \( x \) is equal to the vector space \( {\mathbb{R}}^{n} \) itself. In particular, for any real number \( u \) the tangent space \( {\mathbf{T}}_{u}\mathbb{R} \) is equal to \( \mathbb{R} \) . Thus if \( f : M \rightarrow  \mathbb{R} \) is a smooth real valued function, then the derivative \( \mathrm{d}{f}_{x} : {\mathbf{T}}_{x}M \rightarrow  {\mathbf{T}}_{f\left( x\right) }\mathbb{R} = \mathbb{R} \) can be thought of as an element of the dual vector space

\[
{\operatorname{Hom}}_{\mathbb{R}}\left( {{\mathbf{T}}_{x}M,\mathbb{R}}\right) \text{ . }
\]

This element \( \mathrm{d}{f}_{x} \) of the dual space, sometimes called the "total differential" of \( f \) at \( x \) , is commonly denoted by \( \mathrm{d}f\left( x\right) \) . Note that Leibniz’s rule is satisfied:

\[
\mathrm{d}{\left( fg\right) }_{x} = f\left( x\right) \mathrm{d}{g}_{x} + g\left( x\right) \mathrm{d}{f}_{x},
\]

where \( {fg} \) stands for the product function \( x \mapsto  f\left( x\right) g\left( x\right) \) .

---

\( {}^{4} \) For the concepts of category and functor, see for example [ES52, Chapter IV].

---

For any tangent vector \( v \in  {\mathbf{T}}_{x}M \) the real number \( \mathrm{d}{f}_{x}\left( v\right) \) is called the directional derivative of the real-valued function \( f \) at \( x \) in the direction \( v \) . If we keep \( \left( {x, v}\right) \) fixed but let \( f \) vary over the vector space \( {C}^{\infty }\left( {M,\mathbb{R}}\right) \) consisting of all smooth real valued functions on \( M \) , then a linear differential operator

\[
X : {C}^{\infty }\left( {M,\mathbb{R}}\right)  \rightarrow  \mathbb{R}
\]

can be defined by the formula \( X\left( f\right)  = \mathrm{d}{f}_{x}\left( v\right) \) . Leibniz’s rule now takes the form

\[
X\left( {fg}\right)  = f\left( x\right) X\left( g\right)  + X\left( f\right) g\left( x\right) .
\]

In many expositions on the subject, the tangent vector \( \left( {x, v}\right) \) is identified with this linear operator \( X \) .

One defect of the above presentation is that the "smoothness" of a manifold \( M \) is made to depend on some particular embedding of \( M \) in a coordinate space. It is possible however to canonically embed any smooth manifold \( M \) into one preferred coordinate space.

Given a smooth manifold \( M \subset  {\mathbb{R}}^{A} \) let \( F = {C}^{\infty }\left( {M,\mathbb{R}}\right) \) denote the set of all smooth functions from \( M \) to the real numbers \( \mathbb{R} \) . Define the embedding

\[
i : M \rightarrow  {\mathbb{R}}^{F}
\]

by \( {i}_{f}\left( x\right)  = f\left( x\right) \) . Let \( {M}_{1} \) denote the image \( i\left( M\right)  \subset  {\mathbb{R}}^{F} \) .

Lemma 1.5. This image \( {M}_{1} \) is a smooth manifold in \( {\mathbb{R}}^{F} \) , and the canonical map \( i : M \rightarrow  {M}_{1} \) is a diffeomorphism.

The proof is straightforward.

Thus any smooth manifold has a canonical embedding in an associated coordinate space. This suggests the following definition. Let \( M \) be a set and let \( F \) be a collection of real valued functions on \( M \) which separates points. (That is, given \( x \neq  y \) in \( M \) there exists \( f \in  F \) such that \( f\left( x\right)  \neq  f\left( y\right) \) .) Then \( M \) can be identified with its image under the canonical imbedding \( {}^{5}i : M \rightarrow  {\mathbb{R}}^{F} \) .

Definition. The collection \( F \) is a smoothness structure on \( M \) if the subset \( i\left( M\right)  \subset  {\mathbb{R}}^{F} \) is a smooth manifold, and if \( F \) is precisely the set of all smooth real valued functions on this smooth manifold. \( {}^{6} \)

Note. This definition of "smoothness" is similar to that given by [Nom56]. In the classical point of view the "smoothness structure" of a manifold is prescribed by the collection of local parameterizations. (See for example [Ste51, p.21].) In still another point of view, one uses collections of smooth functions on open subsets. (Compare [Rha55].) All of these definitions are equivalent.

In conclusion here are three problems for the reader. The first two of these will play an important role in later sections.

Problem 1-A. Let \( {M}_{1} \subset  {\mathbb{R}}^{A} \) and \( {M}_{2} \subset  {\mathbb{R}}^{B} \) be smooth manifolds. Show that \( {M}_{1} \times  {M}_{2} \subset  {\mathbb{R}}^{A} \times  {\mathbb{R}}^{B} \) is a smooth manifold, and that the tangent manifold \( \mathbf{T}\left( {{M}_{1} \times  {M}_{2}}\right) \) is canonically diffeomorphic to the product \( \mathbf{T}{M}_{1} \times  \mathbf{T}{M}_{2} \) . Note that a function \( x \mapsto  \left( {{f}_{1}\left( x\right) ,{f}_{2}\left( x\right) }\right) \) from \( M \) to \( {M}_{1} \times  {M}_{2} \) is smooth if and only if both \( {f}_{1} : M \rightarrow  {M}_{1} \) and \( {f}_{2} : M \rightarrow  {M}_{2} \) are smooth.

Problem 1-B. Let \( {\mathbb{P}}^{n} \) denote the set of all lines through the origin in the coordinate space \( {\mathbb{R}}^{n + 1} \) . Define a function

\[
q : {\mathbb{R}}^{n + 1} - \{ 0\}  \rightarrow  {\mathbb{P}}^{n}
\]

by \( q\left( x\right)  = \mathbb{R}x = \) line through \( x \) . Let \( F \) denote the set of all functions \( f : {\mathbb{P}}^{n} \rightarrow  \mathbb{R} \) such that \( f \circ  q \) is smooth.

a) Show that \( F \) is a smooth structure on \( {\mathbb{P}}^{n} \) . The resulting smooth manifold is called the real projective space of dimension \( n \) .

b) Show that the functions

\[
{f}_{ij}\left( {\mathbb{R}x}\right)  = \frac{{x}_{i}{x}_{j}}{\mathop{\sum }\limits_{k}{x}_{k}^{2}}
\]

define a diffeomorphism between \( {\mathbb{P}}^{n} \) and the submanifold of \( {M}_{n + 1}{\left( \mathbb{R}\right) }^{7} \) consisting of all symmetric \( \left( {n + 1}\right)  \times  \left( {n + 1}\right) \) matrices \( A \) of trace 1 satisfying \( {AA} = A \) .

---

\( {}^{5} \) Editor’s note: The book uses embedding and imbedding interchangably, this is just a different spelling.

\( {}^{6} \) If only the first condition is satisfied, then \( F \) might be called a "basis" for a smoothness structure on \( M \) .

---

c) Show that \( {\mathbb{P}}^{n} \) is compact, and that a subset \( V \subset  {\mathbb{P}}^{n} \) is open if and only if \( {q}^{-1}\left( V\right) \) is open.

Problem 1-C. For any smooth manifold \( M \) show that the collection \( F = \; {C}^{\infty }\left( {M,\mathbb{R}}\right) \) of smooth real valued functions on \( M \) can be made into a ring, and that every point \( x \in  M \) determines a ring homomorphism \( F \rightarrow  \mathbb{R} \) and hence a maximal ideal in \( F \) . If \( M \) is compact, show that every maximal ideal in \( F \) arises this way from a point in \( M \) . More generally, if there is a countable basis for the topology of \( M \) , show that every ring homomorphism \( F \rightarrow  \mathbb{R} \) is obtained in this way. (Make use of an element \( f \geq  0 \) in \( F \) such that each \( {f}^{-1}\left\lbrack  {0, c}\right\rbrack \) is compact.) Thus the smooth manifold \( M \) is completely determined by the ring \( F \) . For \( x \in  M \) , show that any \( \mathbb{R} \) -linear mapping \( X : F \rightarrow  \mathbb{R} \) satisfying \( X\left( {fg}\right)  = X\left( f\right) g\left( x\right)  + f\left( x\right) X\left( g\right) \) is given by \( X\left( f\right)  = \mathrm{d}{f}_{x}\left( v\right) \) for some uniquely determined vector \( v \in  {\mathbf{T}}_{x}M \) .

---

\( {}^{7} \) Editor’s note: This is the set of \( \left( {n + 1}\right)  \times  \left( {n + 1}\right) \) matrices given a smooth structure by identifying it with \( {\mathbb{R}}^{{\left( n + 1\right) }^{2}} \) .

---
