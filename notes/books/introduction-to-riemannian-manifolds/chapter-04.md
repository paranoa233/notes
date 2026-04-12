## Chapter 4 Connections

Our ultimate goal is to define a notion of curvature that makes sense on arbitrary Riemannian manifolds, and to relate it to other geometric and topological properties. Before we can do so, however, we need to study geodesics, the generalizations to Riemannian manifolds of straight lines in Euclidean space. There are two key properties satisfied by straight lines in \( {\mathbb{R}}^{n} \) , either of which serves to characterize them uniquely: first, every segment of a straight line is the unique shortest path between its endpoints; and second, straight lines are the only curves that have parametrizations with zero acceleration.

The first of these characterizations—as shortest paths—is probably the most "geometric," so it is tempting to try to use it as a definition of geodesics in Riemannian manifolds. However, this property turns out to be technically difficult to work with as a definition, so instead we will use "zero acceleration" as the defining property and generalize that.

To make sense of acceleration on a manifold, we have to introduce a new object called a connection-essentially a coordinate-independent set of rules for taking directional derivatives of vector fields.

We begin this chapter by examining more closely the problem of finding an invariant interpretation for the acceleration of a curve, as a way to motivate the definitions that follow. We then give a rather general definition of a connection, in terms of directional derivatives of sections of vector bundles. After deriving some basic properties of connections, we show how to use them to differentiate vector fields along curves, to define geodesics, and to define "parallel transport" of vectors along curves.

## The Problem of Differentiating Vector Fields

To see why we need a new kind of differentiation operator, let us begin by thinking informally about curves in \( {\mathbb{R}}^{n} \) . Let \( I \subseteq  \mathbb{R} \) be an interval and \( \gamma  : I \rightarrow  {\mathbb{R}}^{n} \) a smooth curve, written in standard coordinates as \( \gamma \left( t\right)  = \left( {{\gamma }^{1}\left( t\right) ,\ldots ,{\gamma }^{n}\left( t\right) }\right) \) . Such a curve has a well-defined velocity \( {\gamma }^{\prime }\left( t\right) \) and acceleration \( {\gamma }^{\prime \prime }\left( t\right) \) at each \( t \in  I \) , computed by differentiating the components:

\[
{\gamma }^{\prime }\left( t\right)  = {\left. {\dot{\gamma }}^{1}\left( t\right) \frac{\partial }{\partial {x}^{1}}\right| }_{\gamma \left( t\right) } + \cdots  + {\left. {\dot{\gamma }}^{n}\left( t\right) \frac{\partial }{\partial {x}^{n}}\right| }_{\gamma \left( t\right) }, \tag{4.1}
\]

\[
{\gamma }^{\prime \prime }\left( t\right)  = {\left. {\ddot{\gamma }}^{1}\left( t\right) \frac{\partial }{\partial {x}^{1}}\right| }_{\gamma \left( t\right) } + \cdots  + {\left. {\ddot{\gamma }}^{n}\left( t\right) \frac{\partial }{\partial {x}^{n}}\right| }_{\gamma \left( t\right) }. \tag{4.2}
\]

(Here and throughout the book, we use dots to denote ordinary derivatives with respect to \( t \) when there are superscripts that would make primes hard to read.) A curve \( \gamma \) in \( {\mathbb{R}}^{n} \) is a straight line if and only if it has a parametrization for which \( {\gamma }^{\prime \prime }\left( t\right)  \equiv  0 \) .

We can also make sense of directional derivatives of vector fields on \( {\mathbb{R}}^{n} \) , just by computing ordinary directional derivatives of the component functions in standard coordinates: given a vector field \( Y \in  \mathfrak{X}\left( {\mathbb{R}}^{n}\right) \) and a vector \( v \in  {T}_{p}{\mathbb{R}}^{n} \) , we define the Euclidean directional derivative of \( Y \) in the direction \( v \) by the formula

\[
{\overline{\nabla }}_{v}Y = {\left. v\left( {Y}^{1}\right) \frac{\partial }{\partial {x}^{1}}\right| }_{p} + \cdots  + {\left. v\left( {Y}^{n}\right) \frac{\partial }{\partial {x}^{n}}\right| }_{p},
\]

where for each \( i, v\left( {Y}^{i}\right) \) is the result of applying the vector \( v \) to the function \( {Y}^{i} \) :

\[
v\left( {Y}^{i}\right)  = {v}^{1}\frac{\partial {Y}^{i}\left( p\right) }{\partial {x}^{1}} + \cdots  + {v}^{n}\frac{\partial {Y}^{i}\left( p\right) }{\partial {x}^{n}}.
\]

If \( X \) is another vector field on \( {\mathbb{R}}^{n} \) , we obtain a new vector field \( {\overline{\nabla }}_{X}Y \) by evaluating \( {\overline{\nabla }}_{{X}_{p}}Y \) at each point:

\[
{\overline{\nabla }}_{X}Y = X\left( {Y}^{1}\right) \frac{\partial }{\partial {x}^{1}} + \cdots  + X\left( {Y}^{n}\right) \frac{\partial }{\partial {x}^{n}}. \tag{4.3}
\]

More generally, we can play the same game with curves and vector fields on a submanifold of \( {\mathbb{R}}^{n} \) . Suppose \( M \subseteq  {\mathbb{R}}^{n} \) is an embedded submanifold, and consider a smooth curve \( \gamma  : I \rightarrow  M \) . We want to think of a geodesic in \( M \) as a curve in \( M \) that is "as straight as possible." Of course, if \( M \) itself is curved, then \( {\gamma }^{\prime }\left( t\right) \) (thought of as a vector in \( {\mathbb{R}}^{n} \) ) will probably have to vary, or else the curve will leave \( M \) . But we can try to insist that the velocity not change any more than necessary for the curve to stay in \( M \) . One way to do this is to compute the Euclidean acceleration \( {\gamma }^{\prime \prime }\left( t\right) \) as above, and then apply the tangential projection \( {\pi }^{\top } : {T}_{\gamma \left( t\right) }{\mathbb{R}}^{n} \rightarrow  {T}_{\gamma \left( t\right) }M \) (see Prop. 2.16). This yields a vector \( {\gamma }^{\prime \prime }{\left( t\right) }^{\top } = {\pi }^{\top }\left( {{\gamma }^{\prime \prime }\left( t\right) }\right) \) tangent to \( M \) , which we call the tangential acceleration of \( \gamma \) . It is reasonable to say that \( \gamma \) is as straight as it is possible for a curve in \( M \) to be if its tangential acceleration is zero.

Similarly, suppose \( Y \) is a smooth vector field on (an open subset of) \( M \) , and we wish to ask how much \( Y \) is varying in \( M \) in the direction of a vector \( v \in  {T}_{p}M \) . Just as in the case of velocity vectors, if we look at it from the point of view of \( {\mathbb{R}}^{n} \) , the vector field \( Y \) might be forced to vary just so that it can remain tangent to \( M \) . But one plausible way to answer the question is to extend \( Y \) to a smooth vector field \( \widetilde{Y} \) on an open subset of \( {\mathbb{R}}^{n} \) , compute the Euclidean directional derivative of \( \widetilde{Y} \) in the direction \( v \) , and then project orthogonally onto \( {T}_{p}M \) . Let us define the tangential directional derivative of \( Y \) in the direction \( v \) to be

\[
{\nabla }_{v}^{\top }Y = {\pi }^{\top }\left( {{\overline{\nabla }}_{v}\widetilde{Y}}\right) . \tag{4.4}
\]

![bo_d7dtff491nqc73eq8m7g_99_214_197_483_481_0.jpg](images/bo_d7dtff491nqc73eq8m7g_99_214_197_483_481_0.jpg)

Fig. 4.1: Cartesian coordinates

![bo_d7dtff491nqc73eq8m7g_99_841_241_402_437_0.jpg](images/bo_d7dtff491nqc73eq8m7g_99_841_241_402_437_0.jpg)

Fig. 4.2: Polar coordinates

Problem 4-1 shows that the tangential directional derivative is well defined and preserved by rigid motions of \( {\mathbb{R}}^{n} \) . However, at this point there is little reason to believe that the tangential directional derivative is an intrinsic invariant of \( M \) (one that depends only on the Riemannian geometry of \( M \) with its induced metric).

On an abstract Riemannian manifold, for which there is no "ambient Euclidean space" in which to differentiate, this technique is not available. Thus we have to find some way to make sense of the acceleration of a smooth curve in an abstract manifold. Let \( \gamma  : I \rightarrow  M \) be such a curve. As you know from your study of smooth manifold theory, at each time \( t \in  I \) , the velocity of \( \gamma \) is a well-defined vector \( {\gamma }^{\prime }\left( t\right)  \in \; {T}_{\gamma \left( t\right) }M \) (see Appendix A), whose representation in any coordinates is given by (4.1), just as in Euclidean space.

However, unlike velocity, acceleration has no such coordinate-independent interpretation. For example, consider the parametrized circle in the plane given in Cartesian coordinates by \( \gamma \left( t\right)  = \left( {x\left( t\right) , y\left( t\right) }\right)  = \left( {\cos t,\sin t}\right) \) (Fig. 4.1). As a smooth curve in \( {\mathbb{R}}^{2} \) , it has an acceleration vector at time \( t \) given by

\[
{\gamma }^{\prime \prime }\left( t\right)  = {x}^{\prime \prime }\left( t\right) {\left. \frac{\partial }{\partial x}\right| }_{\gamma \left( t\right) } + {y}^{\prime \prime }\left( t\right) {\left. \frac{\partial }{\partial x}\right| }_{\gamma \left( t\right) }
\]

\[
=  - {\left. \cos t\frac{\partial }{\partial x}\right| }_{\gamma \left( t\right) } - {\left. \sin t\frac{\partial }{\partial x}\right| }_{\gamma \left( t\right) }.
\]

![bo_d7dtff491nqc73eq8m7g_100_511_182_509_365_0.jpg](images/bo_d7dtff491nqc73eq8m7g_100_511_182_509_365_0.jpg)

Fig. 4.3: \( {\gamma }^{\prime }\left( t\right) \) and \( {\gamma }^{\prime }\left( {t + h}\right) \) lie in different vector spaces

But in polar coordinates, the same curve is described by \( \left( {r\left( t\right) ,\theta \left( t\right) }\right)  = \left( {1, t}\right) \) (Fig. 4.2). In these coordinates, if we try to compute the acceleration vector by the analogous formula, we get

\[
{\gamma }^{\prime \prime }\left( t\right)  = {r}^{\prime \prime }\left( t\right) {\left. \frac{\partial }{\partial r}\right| }_{\gamma \left( t\right) } + {\theta }^{\prime \prime }\left( t\right) {\left. \frac{\partial }{\partial \theta }\right| }_{\gamma \left( t\right) } = 0.
\]

The problem is this: to define \( {\gamma }^{\prime \prime }\left( t\right) \) by differentiating \( {\gamma }^{\prime }\left( t\right) \) with respect to \( t \) , we have to take a limit of a difference quotient involving the vectors \( {\gamma }^{\prime }\left( {t + h}\right) \) and \( {\gamma }^{\prime }\left( t\right) \) ; but these live in different vector spaces \( \left( {{T}_{\gamma \left( {t + h}\right) }M}\right. \) and \( {T}_{\gamma \left( t\right) }M \) respectively), so it does not make sense to subtract them (Fig. 4.3). The definition of acceleration works in the special case of smooth curves in \( {\mathbb{R}}^{n} \) expressed in standard coordinates (or more generally, curves in any finite-dimensional vector space expressed in linear coordinates) because each tangent space can be naturally identified with the vector space itself. On a general smooth manifold, there is no such natural identification.

The velocity vector \( {\gamma }^{\prime }\left( t\right) \) is an example of a vector field along a curve, a concept for which we will give a rigorous definition presently. To interpret the acceleration of a curve in a manifold, what we need is some coordinate-independent way to differentiate vector fields along curves. To do so, we need a way to compare values of the vector field at different points, or intuitively, to "connect" nearby tangent spaces. This is where a connection comes in: it will be an additional piece of data on a manifold, a rule for computing directional derivatives of vector fields.

## Connections

It turns out to be easiest to define a connection first as a way of differentiating sections of vector bundles. The definition is meant to capture the essential properties of the Euclidean and tangential directional derivative operators \( \left( {\overline{\nabla }\text{ and }\left. {\nabla }^{\top }\right) }\right. \) that we defined above. (We will verify later that those operators actually are connections; see Examples 4.8 and 4.9.) After defining connections in this general setting, we will adapt the definition to the case of vector fields along curves.

Let \( \pi  : E \rightarrow  M \) be a smooth vector bundle over a smooth manifold \( M \) with or without boundary, and let \( \Gamma \left( E\right) \) denote the space of smooth sections of \( E \) . A connection in \( E \) is a map

\[
\nabla  : \mathcal{X}\left( M\right)  \times  \Gamma \left( E\right)  \rightarrow  \Gamma \left( E\right) ,
\]

written \( \left( {X, Y}\right)  \mapsto  {\nabla }_{X}Y \) , satisfying the following properties:

(i) \( {\nabla }_{X}Y \) is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) : for \( {f}_{1},{f}_{2} \in  {C}^{\infty }\left( M\right) \) and \( {X}_{1},{X}_{2} \in  \mathfrak{X}\left( M\right) \) ,

\[
{\nabla }_{{f}_{1}{X}_{1} + {f}_{2}{X}_{2}}Y = {f}_{1}{\nabla }_{{X}_{1}}Y + {f}_{2}{\nabla }_{{X}_{2}}Y.
\]

(ii) \( {\nabla }_{X}Y \) is linear over \( \mathbb{R} \) in \( Y \) : for \( {a}_{1},{a}_{2} \in  \mathbb{R} \) and \( {Y}_{1},{Y}_{2} \in  \Gamma \left( E\right) \) ,

\[
{\nabla }_{X}\left( {{a}_{1}{Y}_{1} + {a}_{2}{Y}_{2}}\right)  = {a}_{1}{\nabla }_{X}{Y}_{1} + {a}_{2}{\nabla }_{X}{Y}_{2}.
\]

(iii) \( \nabla \) satisfies the following product rule: for \( f \in  {C}^{\infty }\left( M\right) \) ,

\[
{\nabla }_{X}\left( {fY}\right)  = f{\nabla }_{X}Y + \left( {Xf}\right) Y.
\]

The symbol \( \nabla \) is read "del" or "nabla," and \( {\nabla }_{X}Y \) is called the covariant derivative of \( Y \) in the direction \( X \) . (This use of the word "covariant" has nothing to do with covariant functors in category theory. It is related, albeit indirectly, to the use of the word in the context of covariant and contravariant tensors, in that it reflects the fact that the components of the covariant derivative have a transformation law that "varies correctly" to give a well-defined meaning independent of coordinates. From the modern coordinate-free point of view, "invariant derivative" would probably be a better term.)

There is a variety of types of connections that are useful in different circumstances. The type of connection we have defined here is sometimes called a Koszul connection to distinguish it from other types. Since we have no need to consider other types of connections in this book, we refer to Koszul connections simply as connections.

Although a connection is defined by its action on global sections, it follows from the definitions that it is actually a local operator, as the next lemma shows.

Lemma 4.1 (Locality). Suppose \( \nabla \) is a connection in a smooth vector bundle \( E \rightarrow \; M \) . For every \( X \in  \mathfrak{X}\left( M\right) , Y \in  \Gamma \left( E\right) \) , and \( p \in  M \) , the covariant derivative \( {\left. {\nabla }_{X}Y\right| }_{p} \) depends only on the values of \( X \) and \( Y \) in an arbitrarily small neighborhood of p. More precisely, if \( X = \widetilde{X} \) and \( Y = \widetilde{Y} \) on a neighborhood of \( p \) , then \( {\left. {\nabla }_{X}Y\right| }_{p} = \; {\left. {\nabla }_{\widetilde{X}}\widetilde{Y}\right| }_{p} \)

Proof. First consider \( Y \) . Replacing \( Y \) by \( Y - \widetilde{Y} \) shows that it suffices to prove \( {\left. {\nabla }_{X}Y\right| }_{p} = 0 \) if \( Y \) vanishes on a neighborhood of \( p \) .

Thus suppose \( Y \) is a smooth section of \( E \) that is identically zero on a neighborhood \( U \) of \( p \) . Choose a bump function \( \varphi  \in  {C}^{\infty }\left( M\right) \) with support in \( U \) such that \( \varphi \left( p\right)  = 1 \) . The hypothesis that \( Y \) vanishes on \( U \) implies that \( {\varphi Y} \equiv  0 \) on all of \( M \) , so for every \( X \in  \mathfrak{X}\left( M\right) \) , we have \( {\nabla }_{X}\left( {\varphi Y}\right)  = {\nabla }_{X}\left( {0 \cdot  {\varphi Y}}\right)  = 0{\nabla }_{X}\left( {\varphi Y}\right)  = 0 \) . Thus the product rule gives

\[
0 = {\nabla }_{X}\left( {\varphi Y}\right)  = \left( {X\varphi }\right) Y + \varphi \left( {{\nabla }_{X}Y}\right) . \tag{4.5}
\]

Now \( Y \equiv  0 \) on the support of \( \varphi \) , so the first term on the right is identically zero. Evaluating (4.5) at \( p \) shows that \( {\left. {\nabla }_{X}Y\right| }_{p} = 0 \) . The argument for \( X \) is similar but easier.

Exercise 4.2. Complete the proof of Lemma 4.1 by showing that \( {\nabla }_{X}Y \) and \( {\nabla }_{\widetilde{X}}Y \) agree at \( p \) if \( X = \widetilde{X} \) on a neighborhood of \( p \) .

Proposition 4.3 (Restriction of a Connection). Suppose \( \nabla \) is a connection in a smooth vector bundle \( E \rightarrow  M \) . For every open subset \( U \subseteq  M \) , there is a unique connection \( {\nabla }^{U} \) on the restricted bundle \( {\left. E\right| }_{U} \) that satisfies the following relation for every \( X \in  \mathfrak{X}\left( M\right) \) and \( Y \in  \Gamma \left( E\right) \) :

\[
{\nabla }_{\left( {\left. X\right| }_{U}\right) }^{U}\left( {\left. Y\right| }_{U}\right)  = {\left. \left( {\nabla }_{X}Y\right) \right| }_{U}. \tag{4.6}
\]

Proof. First we prove uniqueness. Suppose \( {\nabla }^{U} \) is any such connection and \( X \in \; \mathcal{X}\left( U\right) \) and \( Y \in  \Gamma \left( {\left. E\right| }_{U}\right) \) are arbitrary. Given \( p \in  U \) , we can use a bump function to construct a smooth vector field \( \widetilde{X} \in  \mathfrak{X}\left( M\right) \) and a smooth section \( \widetilde{Y} \in  \Gamma \left( E\right) \) such that \( {\left. \widetilde{X}\right| }_{U} \) agrees with \( X \) and \( {\left. \widetilde{Y}\right| }_{U} \) with \( Y \) on some neighborhood of \( p \) , and then Lemma 4.1 together with (4.6) implies

\[
{\left. {\nabla }_{X}^{U}Y\right| }_{p} = {\nabla }_{\left( {\left. \widetilde{X}\right| }_{U}\right) }^{U}{\left. \left( {\left. \widetilde{Y}\right| }_{U}\right) \right| }_{p} = {\left. \left( {\nabla }_{\widetilde{X}}\widetilde{Y}\right) \right| }_{p}. \tag{4.7}
\]

Since the right-hand side is completely determined by \( \nabla \) , this shows that \( {\nabla }^{U} \) is uniquely defined if it exists.

To prove existence, given \( X \in  \mathcal{X}\left( U\right) \) and \( Y \in  \Gamma \left( {\left. E\right| }_{U}\right) \) , for every \( p \in  U \) we just construct \( \widetilde{X} \) and \( \widetilde{Y} \) as above, and define \( {\nabla }_{X}^{U}Y\left| {}_{p}\text{ by (4.7). This is independent of the }\right| \) choices of \( \widetilde{X} \) and \( \widetilde{Y} \) by Lemma 4.1, and it is smooth because the same formula holds on some neighborhood of \( p \) . The fact that it satisfies the properties of a connection is an easy exercise.

- Exercise 4.4. Complete the proof of the preceding proposition by showing that \( {\nabla }^{U} \) is a connection.

In the situation of this proposition, we typically just refer to the restricted connection as \( \nabla \) instead of \( {\nabla }^{U} \) ; the proposition guarantees that there is no ambiguity in doing so.

Lemma 4.1 tells us that we can compute the value of \( {\nabla }_{X}Y \) at \( p \) knowing only the values of \( X \) and \( Y \) in a neighborhood of \( p \) . In fact, as the next proposition shows, we need only know the value of \( X \) at \( p \) itself.

Proposition 4.5. Under the hypotheses of Lemma 4.1, \( {\left. {\nabla }_{X}Y\right| }_{p} \) depends only on the values of \( Y \) in a neighborhood of \( p \) and the value of \( X \) at \( p \) .

Proof. The claim about \( Y \) was proved in Lemma 4.1. To prove the claim about \( X \) , it suffices by linearity to assume that \( {X}_{p} = 0 \) and show that \( {\left. {\nabla }_{X}Y\right| }_{p} = 0 \) . Choose a coordinate neighborhood \( U \) of \( p \) , and write \( X = {X}^{i}{\partial }_{i} \) in coordinates on \( U \) , with \( {X}^{i}\left( p\right)  = 0 \) . Thanks to Proposition 4.3, it suffices to work with the restricted connection on \( U \) , which we also denote by \( \nabla \) . For every \( Y \in  \Gamma \left( {\left. E\right| }_{U}\right) \) , we have

\[
{\left. {\nabla }_{X}Y\right| }_{p} = {\nabla }_{{X}^{i}{\partial }_{i}}{\left. Y\right| }_{p} = {X}^{i}\left( p\right) {\nabla }_{{\partial }_{i}}{\left. Y\right| }_{p} = 0.
\]

Thanks to Propositions 4.3 and 4.5, we can make sense of the expression \( {\nabla }_{v}Y \) when \( v \) is some element of \( {T}_{p}M \) and \( Y \) is a smooth local section of \( E \) defined only on some neighborhood of \( p \) . To evaluate it, let \( X \) be a vector field on a neighborhood of \( p \) whose value at \( p \) is \( v \) , and set \( {\nabla }_{v}Y = {\left. {\nabla }_{X}Y\right| }_{p} \) . Proposition 4.5 shows that the result does not depend on the extension chosen. Henceforth, we will interpret covariant derivatives of local sections of bundles in this way without further comment.

## Connections in the Tangent Bundle

For Riemannian or pseudo-Riemannian geometry, our primary concern is with connections in the tangent bundle, so for the rest of the chapter we focus primarily on that case. A connection in the tangent bundle is often called simply a connection on \( M \) . (The terms affine connection and linear connection are also sometimes used in this context, but there is little agreement on the precise definitions of these terms, so we avoid them.)

Suppose \( M \) is a smooth manifold with or without boundary. By the definition we just gave, a connection in \( {TM} \) is a map

\[
\nabla  : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right)
\]

satisfying properties (i)-(iii) above. Although the definition of a connection resembles the characterization of \( \left( {1,2}\right) \) -tensor fields given by the tensor characterization lemma (Lemma B.6), a connection in \( {TM} \) is not a tensor field because it is not linear over \( {C}^{\infty }\left( M\right) \) in its second argument, but instead satisfies the product rule.

For computations, we need to examine how a connection appears in terms of a local frame. Let \( \left( {E}_{i}\right) \) be a smooth local frame for \( {TM} \) on an open subset \( U \subseteq  M \) . For every choice of the indices \( i \) and \( j \) , we can expand the vector field \( {\nabla }_{{E}_{i}}{E}_{j} \) in terms of this same frame:

\[
{\nabla }_{{E}_{i}}{E}_{j} = {\Gamma }_{ij}^{k}{E}_{k} \tag{4.8}
\]

As \( i, j \) , and \( k \) range from 1 to \( n = \dim M \) , this defines \( {n}^{3} \) smooth functions \( {\Gamma }_{ij}^{k} : U \rightarrow  \mathbb{R} \) , called the connection coefficients of \( \nabla \) with respect to the given frame. The following proposition shows that the connection is completely determined in \( U \) by its connection coefficients.

Proposition 4.6. Let \( M \) be a smooth manifold with or without boundary, and let \( \nabla \) be a connection in TM. Suppose \( \left( {E}_{i}\right) \) is a smooth local frame over an open subset \( U \subseteq  M \) , and let \( \left\{  {\Gamma }_{ij}^{k}\right\} \) be the connection coefficients of \( \nabla \) with respect to this frame. For smooth vector fields \( X, Y \in  \mathfrak{X}\left( U\right) \) , written in terms of the frame as \( X = {X}^{i}{E}_{i}, Y = {Y}^{j}{E}_{j} \) , one has

\[
{\nabla }_{X}Y = \left( {X\left( {Y}^{k}\right)  + {X}^{i}{Y}^{j}{\Gamma }_{ij}^{k}}\right) {E}_{k}. \tag{4.9}
\]

Proof. Just use the defining properties of a connection and compute:

\[
{\nabla }_{X}Y = {\nabla }_{X}\left( {{Y}^{j}{E}_{j}}\right)
\]

\[
= X\left( {Y}^{j}\right) {E}_{j} + {Y}^{j}{\nabla }_{{X}^{i}{E}_{i}}{E}_{j}
\]

\[
= X\left( {Y}^{j}\right) {E}_{j} + {X}^{i}{Y}^{j}{\nabla }_{{E}_{i}}{E}_{j}
\]

\[
= X\left( {Y}^{j}\right) {E}_{j} + {X}^{i}{Y}^{j}{\Gamma }_{ij}^{k}{E}_{k}.
\]

Renaming the dummy index in the first term yields (4.9).

Once the connection coefficients (and thus the connection) have been determined in some local frame, they can be determined in any other local frame on the same open set by the result of the following proposition.

Proposition 4.7 (Transformation Law for Connection Coefficients). Let \( M \) be a smooth manifold with or without boundary, and let \( \nabla \) be a connection in \( {TM} \) . Suppose we are given two smooth local frames \( \left( {E}_{i}\right) \) and \( \left( {\widetilde{E}}_{j}\right) \) for TM on an open subset \( U \subseteq  M \) , related by \( {\widetilde{E}}_{i} = {A}_{i}^{j}{E}_{j} \) for some matrix of functions \( \left( {A}_{i}^{j}\right) \) . Let \( {\Gamma }_{ij}^{k} \) and \( {\widetilde{\Gamma }}_{ij}^{k} \) denote the connection coefficients of \( \nabla \) with respect to these two frames. Then

\[
{\widetilde{\Gamma }}_{ij}^{k} = {\left( {A}^{-1}\right) }_{p}^{k}{A}_{i}^{q}{A}_{j}^{r}{\Gamma }_{qr}^{p} + {\left( {A}^{-1}\right) }_{p}^{k}{A}_{i}^{q}{E}_{q}\left( {A}_{j}^{p}\right) . \tag{4.10}
\]

Proof. Problem 4-3.

Observe that the first term above is exactly what the transformation law would be if \( {\Gamma }_{ij}^{k} \) were the components of a \( \left( {1,2}\right) \) -tensor field; but the second term is of a different character, because it involves derivatives of the transition matrix \( \left( {A}_{j}^{p}\right) \) .

## Existence of Connections

So far, we have studied properties of connections but have not produced any, so you might be wondering whether they are plentiful or rare. In fact, they are quite plentiful, as we will show shortly. Let us begin with the simplest example.

Example 4.8 (The Euclidean Connection). In \( T{\mathbb{R}}^{n} \) , define the Euclidean connection \( \overline{\nabla } \) by formula (4.3). It is easy to check that this satisfies the required properties for a connection, and that its connection coefficients in the standard coordinate frame are all zero. ‖

Here is a way to construct a large class of examples.

Example 4.9 (The Tangential Connection on a Submanifold of \( {\mathbb{R}}^{n} \) ). Let \( M \subseteq  {\mathbb{R}}^{n} \) be an embedded submanifold. Define a connection \( {\nabla }^{\top } \) on \( {TM} \) , called the tangential connection, by setting

\[
{\nabla }_{X}^{\top }Y = {\pi }^{\top }\left( {{\overline{\nabla }}_{\widetilde{X}}{\left. \widetilde{Y}\right| }_{M}}\right) ,
\]

where \( {\pi }^{\top } \) is the orthogonal projection onto \( {TM} \) (Prop. 2.16), \( \overline{\nabla } \) is the Euclidean connection on \( {\mathbb{R}}^{n} \) (Example 4.8), and \( \widetilde{X} \) and \( \widetilde{Y} \) are smooth extensions of \( X \) and \( Y \) to an open set in \( {\mathbb{R}}^{n} \) . (Such extensions exist by the result of Exercise A.23.) Since the value of \( {\overline{\nabla }}_{\widetilde{X}}\widetilde{Y} \) at a point \( p \in  M \) depends only on \( {\widetilde{X}}_{p} = {X}_{p} \) , this just boils down to defining \( {\left( {\nabla }_{X}^{\top }Y\right) }_{p} \) to be equal to the tangential directional derivative \( {\nabla }_{{X}_{p}}^{\top }Y \) that we defined in (4.4) above. Problem 4-1 shows that this value is independent of the choice of extension \( \widetilde{Y} \) , so \( {\nabla }^{\top } \) is well defined. Smoothness is easily verified by expressing \( {\overline{\nabla }}_{\widetilde{X}}\widetilde{Y} \) in terms of an adapted orthonormal frame (see Prop. 2.14).

It is immediate from the definition that \( {\nabla }_{X}^{\top }Y \) is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) and over \( \mathbb{R} \) in \( Y \) , so to show that \( {\nabla }^{\top } \) is a connection, only the product rule needs to be checked. Let \( f \in  {C}^{\infty }\left( M\right) \) , and let \( \widetilde{f} \) be an extension of \( f \) to a neighborhood of \( M \) in \( {\mathbb{R}}^{n} \) . Then \( \widetilde{f}\widetilde{Y} \) is a smooth extension of \( {fY} \) to a neighborhood of \( M \) , so

\[
{\nabla }_{X}^{\top }\left( {fY}\right)  = {\pi }^{\top }\left( {{\overline{\nabla }}_{\widetilde{X}}\left( {\widetilde{f}\widetilde{Y}}\right) {\left. \right| }_{M}}\right)
\]

\[
= {\pi }^{\top }\left( {\left. \left( \widetilde{X}\widetilde{f}\right) \widetilde{Y}\right| }_{M}\right)  + {\pi }^{\top }\left( {\left. \widetilde{f}{\overline{\nabla }}_{\widetilde{X}}\widetilde{Y}\right| }_{M}\right)
\]

\[
= \left( {Xf}\right) Y + f{\nabla }_{X}^{\top }Y\text{ . }
\]

Thus \( {\nabla }^{\top } \) is a connection.

In fact, there are many connections on \( {\mathbb{R}}^{n} \) , or indeed on every smooth manifold that admits a global frame (for example, every manifold covered by a single smooth coordinate chart). The following lemma shows how to construct all of them explicitly.

Lemma 4.10. Suppose \( M \) is a smooth n-manifold with or without boundary, and M admits a global frame \( \left( {E}_{i}\right) \) . Formula (4.9) gives a one-to-one correspondence between connections in TM and choices of \( {n}^{3} \) smooth real-valued functions \( \left\{  {\Gamma }_{ij}^{k}\right\} \) on M.

Proof. Every connection determines functions \( \left\{  {\Gamma }_{ij}^{k}\right\} \) by (4.8), and Proposition 4.6 shows that those functions satisfy (4.9). On the other hand, given \( \left\{  {\Gamma }_{ij}^{k}\right\} \) , we can define \( {\nabla }_{X}Y \) by (4.9); it is easy to see that the resulting expression is smooth if \( X \) and \( Y \) are smooth, linear over \( \mathbb{R} \) in \( Y \) , and linear over \( {C}^{\infty }\left( M\right) \) in \( X \) . To prove that it is a connection, only the product rule requires checking; this is a straightforward computation left as an exercise.

- Exercise 4.11. Complete the proof of Lemma 4.10.

Proposition 4.12. The tangent bundle of every smooth manifold with or without boundary admits a connection.

Proof. Let \( M \) be a smooth manifold with or without boundary, and cover \( M \) with coordinate charts \( \left\{  {U}_{\alpha }\right\} \) ; the preceding lemma guarantees the existence of a connection \( {\nabla }^{\alpha } \) on each \( {U}_{\alpha } \) . Choose a partition of unity \( \left\{  {\varphi }_{\alpha }\right\} \) subordinate to \( \left\{  {U}_{\alpha }\right\} \) . We would like to patch the various \( {\nabla }^{\alpha } \) ’s together by the formula

\[
{\nabla }_{X}Y = \mathop{\sum }\limits_{\alpha }{\varphi }_{\alpha }{\nabla }_{X}^{\alpha }Y \tag{4.11}
\]

Because the set of supports of the \( {\varphi }_{\alpha } \) ’s is locally finite, the sum on the right-hand side has only finitely many nonzero terms in a neighborhood of each point, so it defines a smooth vector field on \( M \) . It is immediate from this definition that \( {\nabla }_{X}Y \) is linear over \( \mathbb{R} \) in \( Y \) and linear over \( {C}^{\infty }\left( M\right) \) in \( X \) . We have to be a bit careful with the product rule, though, since a linear combination of connections is not necessarily a connection. (You can check, for example, that if \( {\nabla }^{0} \) and \( {\nabla }^{1} \) are connections, then neither \( 2{\nabla }^{0} \) nor \( {\nabla }^{0} + {\nabla }^{1} \) satisfies the product rule.) By direct computation,

\[
{\nabla }_{X}\left( {fY}\right)  = \mathop{\sum }\limits_{\alpha }{\varphi }_{\alpha }{\nabla }_{X}^{\alpha }\left( {fY}\right)
\]

\[
= \mathop{\sum }\limits_{\alpha }{\varphi }_{\alpha }\left( {\left( {Xf}\right) Y + f{\nabla }_{X}^{\alpha }Y}\right)
\]

\[
= \left( {Xf}\right) Y\mathop{\sum }\limits_{\alpha }{\varphi }_{\alpha } + f\mathop{\sum }\limits_{\alpha }{\varphi }_{\alpha }{\nabla }_{X}^{\alpha }Y
\]

\[
= \left( {Xf}\right) Y + f{\nabla }_{X}Y
\]

Although a connection is not a tensor field, the next proposition shows that the difference between two connections is.

Proposition 4.13 (The Difference Tensor). Let \( M \) be a smooth manifold with or without boundary. For any two connections \( {\nabla }^{0} \) and \( {\nabla }^{1} \) in \( {TM} \) , define a map \( D : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) by

\[
D\left( {X, Y}\right)  = {\nabla }_{X}^{1}Y - {\nabla }_{X}^{0}Y.
\]

Then \( D \) is bilinear over \( {C}^{\infty }\left( M\right) \) , and thus defines a \( \left( {1,2}\right) \) -tensor field called the difference tensor between \( {\nabla }^{0} \) and \( {\nabla }^{1} \) .

Proof. It is immediate from the definition that \( D \) is linear over \( {C}^{\infty }\left( M\right) \) in its first argument, because both \( {\nabla }^{0} \) and \( {\nabla }^{1} \) are. To show that it is linear over \( {C}^{\infty }\left( M\right) \) in the second argument, expand \( D\left( {X,{fY}}\right) \) using the product rule, and note that the two terms in which \( f \) is differentiated cancel each other.

Now that we know there is always one connection in \( {TM} \) , we can use the result of the preceding proposition to say exactly how many there are.

Theorem 4.14. Let \( M \) be a smooth manifold with or without boundary, and let \( {\nabla }^{0} \) be any connection in \( {TM} \) . Then the set \( \mathcal{A}\left( {TM}\right) \) of all connections in \( {TM} \) is equal to the following affine space:

\[
\mathcal{A}\left( {TM}\right)  = \left\{  {{\nabla }^{0} + D : D \in  \Gamma \left( {{T}^{\left( 1,2\right) }{TM}}\right) }\right\}  ,
\]

where \( D \in  \Gamma \left( {{T}^{\left( 1,2\right) }{TM}}\right) \) is interpreted as a map from \( \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right) \) to \( \mathfrak{X}\left( M\right) \) as in Proposition B.1, and \( {\nabla }^{0} + D : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) is defined by

\[
{\left( {\nabla }^{0} + D\right) }_{X}Y = {\nabla }_{X}^{0}Y + D\left( {X, Y}\right) .
\]

Proof. Problem 4-4.

## Covariant Derivatives of Tensor Fields

By definition, a connection in \( {TM} \) is a rule for computing covariant derivatives of vector fields. We show in this section that every connection in \( {TM} \) automatically induces connections in all tensor bundles over \( M \) , and thus gives us a way to compute covariant derivatives of tensor fields of any type.

Proposition 4.15. Let \( M \) be a smooth manifold with or without boundary, and let \( \nabla \) be a connection in \( {TM} \) . Then \( \nabla \) uniquely determines a connection in each tensor bundle \( {T}^{\left( k, l\right) }{TM} \) , also denoted by \( \nabla \) , such that the following four conditions are satisfied.

(i) In \( {T}^{\left( 1,0\right) }{TM} = {TM},\nabla \) agrees with the given connection.

(ii) In \( {T}^{\left( 0,0\right) }{TM} = M \times  \mathbb{R},\nabla \) is given by ordinary differentiation of functions:

\[
{\nabla }_{X}f = {Xf}
\]

(iii) \( \nabla \) obeys the following product rule with respect to tensor products:

\[
{\nabla }_{X}\left( {F \otimes  G}\right)  = \left( {{\nabla }_{X}F}\right)  \otimes  G + F \otimes  \left( {{\nabla }_{X}G}\right) .
\]

(iv) \( \nabla \) commutes with all contractions: if "tr" denotes a trace on any pair of indices, one covariant and one contravariant, then

\[
{\nabla }_{X}\left( {\operatorname{tr}F}\right)  = \operatorname{tr}\left( {{\nabla }_{X}F}\right) .
\]

This connection also satisfies the following additional properties:

(a) \( \nabla \) obeys the following product rule with respect to the natural pairing between a covector field \( \omega \) and a vector field \( Y \) :

\[
{\nabla }_{X}\langle \omega , Y\rangle  = \left\langle  {{\nabla }_{X}\omega , Y}\right\rangle   + \left\langle  {\omega ,{\nabla }_{X}Y}\right\rangle  .
\]

(b) For all \( F \in  \Gamma \left( {{T}^{\left( k, l\right) }{TM}}\right) \) , smooth 1-forms \( {\omega }^{1},\ldots ,{\omega }^{k} \) , and smooth vector fields \( {Y}_{1},\ldots ,{Y}_{l} \) ,

\[
\left( {{\nabla }_{X}F}\right) \left( {{\omega }^{1},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{Y}_{l}}\right)  = X\left( {F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{Y}_{l}}\right) }\right)
\]

\[
- \mathop{\sum }\limits_{{i = 1}}^{k}F\left( {{\omega }^{1},\ldots ,{\nabla }_{X}{\omega }^{i},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{Y}_{l}}\right) \tag{4.12}
\]

\[
- \mathop{\sum }\limits_{{j = 1}}^{l}F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{\nabla }_{X}{Y}_{j},\ldots ,{Y}_{l}}\right) .
\]

Proof. First we show that every family of connections on all tensor bundles satisfying (i)-(iv) also satisfies (a) and (b). Suppose we are given such a family of connections, all denoted by \( \nabla \) . To prove (a), note that \( \langle \omega , Y\rangle  = \operatorname{tr}\left( {\omega  \otimes  Y}\right) \) , as can be seen by evaluating both sides in coordinates, where they both reduce to \( {\omega }_{i}{Y}^{i} \) . Therefore, (i)-(iv) imply

\[
{\nabla }_{X}\langle \omega , Y\rangle  = {\nabla }_{X}\left( {\operatorname{tr}\left( {\omega  \otimes  Y}\right) }\right)
\]

\[
= \operatorname{tr}\left( {{\nabla }_{X}\left( {\omega  \otimes  Y}\right) }\right)
\]

\[
= \operatorname{tr}\left( {{\nabla }_{X}\omega  \otimes  Y + \omega  \otimes  {\nabla }_{X}Y}\right)
\]

\[
= \left\langle  {{\nabla }_{X}\omega , Y}\right\rangle   + \left\langle  {\omega ,{\nabla }_{X}Y}\right\rangle  .
\]

Then (b) is proved by induction using a similar computation applied to

\[
F\left( {{\omega }^{1},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{Y}_{l}}\right)  = \underset{k + l}{\underbrace{\operatorname{tr} \circ  \cdots  \circ  \operatorname{tr}}}\left( {F \otimes  {\omega }^{1} \otimes  \cdots  \otimes  {\omega }^{k} \otimes  {Y}_{1} \otimes  \cdots  \otimes  {Y}_{l}}\right) ,
\]

where each trace operator acts on an upper index of \( F \) and the lower index of the corresponding 1-form, or a lower index of \( F \) and the upper index of the corresponding vector field.

Next we address uniqueness. Assume again that \( \nabla \) represents a family of connections satisfying (i)-(iv), and hence also (a) and (b). Observe that (ii) and (a) imply that the covariant derivative of every 1-form \( \omega \) can be computed by

\[
\left( {{\nabla }_{X}\omega }\right) \left( Y\right)  = X\left( {\omega \left( Y\right) }\right)  - \omega \left( {{\nabla }_{X}Y}\right) . \tag{4.13}
\]

It follows that the connection on 1-forms is uniquely determined by the original connection in \( {TM} \) . Similarly,(b) gives a formula that determines the covariant derivative of every tensor field \( F \) in terms of covariant derivatives of vector fields and 1-forms, so the connection in every tensor bundle is uniquely determined.

Now to prove existence, we first define covariant derivatives of 1-forms by (4.13), and then we use (4.12) to define \( \nabla \) on all other tensor bundles. The first thing that needs to be checked is that the resulting expression is multilinear over \( {C}^{\infty }\left( M\right) \) in each \( {\omega }^{i} \) and \( {Y}_{j} \) , and therefore defines a smooth tensor field. This is done by inserting \( f{\omega }^{i} \) in place of \( {\omega }^{i} \) , or \( f{Y}_{j} \) in place of \( {Y}_{j} \) , and expanding the right-hand side, noting that the two terms in which \( f \) is differentiated cancel each other out. Once we know that \( {\nabla }_{X}F \) is a smooth tensor field, we need to check that it satisfies the defining properties of a connection. Linearity over \( {C}^{\infty }\left( M\right) \) in \( X \) and linearity over \( \mathbb{R} \) in \( F \) are both evident from (4.12) and (4.13), and the product rule in \( F \) follows easily from the fact that differentiation of functions by \( X \) satisfies the product rule.

While (4.12) and (4.13) are useful for proving the existence and uniqueness of the connections in tensor bundles, they are not very practical for computation, because computing the value of \( {\nabla }_{X}F \) at a point requires extending all of its arguments to vector fields and covector fields in an open set, and computing a great number of derivatives. For computing the components of a covariant derivative in terms of a local frame, the formulas in the following proposition are far more useful.

Proposition 4.16. Let \( M \) be a smooth manifold with or without boundary, and let \( \nabla \) be a connection in \( {TM} \) . Suppose \( \left( {E}_{i}\right) \) is a local frame for \( M,\left( {\varepsilon }^{j}\right) \) is its dual coframe, and \( \left\{  {\Gamma }_{ij}^{k}\right\} \) are the connection coefficients of \( \nabla \) with respect to this frame. Let \( X \) be a smooth vector field, and let \( {X}^{i}{E}_{i} \) be its local expression in terms of this frame.

(a) The covariant derivative of a 1-form \( \omega  = {\omega }_{i}{\varepsilon }^{i} \) is given locally by

\[
{\nabla }_{X}\left( \omega \right)  = \left( {X\left( {\omega }_{k}\right)  - {X}^{j}{\omega }_{i}{\Gamma }_{jk}^{i}}\right) {\varepsilon }^{k}.
\]

(b) If \( F \in  \Gamma \left( {{T}^{\left( k, l\right) }{TM}}\right) \) is a smooth mixed tensor field of any rank, expressed locally as

\[
F = {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{E}_{{i}_{1}} \otimes  \cdots  \otimes  {E}_{{i}_{k}} \otimes  {\varepsilon }^{{j}_{1}} \otimes  \cdots  \otimes  {\varepsilon }^{{j}_{l}},
\]

then the covariant derivative of \( F \) is given locally by

\[
{\nabla }_{X}F = \left( {X\left( {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}\right)  + \mathop{\sum }\limits_{{s = 1}}^{k}{X}^{m}{F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots p\ldots {i}_{k}}{\Gamma }_{mp}^{{i}_{s}} - \mathop{\sum }\limits_{{s = 1}}^{l}{X}^{m}{F}_{{j}_{1}\ldots p\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{\Gamma }_{m{j}_{s}}^{p}}\right)  \times
\]

\[
{E}_{{i}_{1}} \otimes  \cdots  \otimes  {E}_{{i}_{k}} \otimes  {\varepsilon }^{{j}_{1}} \otimes  \cdots  \otimes  {\varepsilon }^{{j}_{l}}.
\]

Proof. Problem 4-5.

Because the covariant derivative \( {\nabla }_{X}F \) of a tensor field (or, as a special case, a vector field) is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) , the covariant derivatives of \( F \) in all directions can be handily encoded in a single tensor field whose rank is one more than the rank of \( F \) , as follows.

Proposition 4.17 (The Total Covariant Derivative). Let \( M \) be a smooth manifold with or without boundary and let \( \nabla \) be a connection in \( {TM} \) . For every \( F \in \; \Gamma \left( {{T}^{\left( k, l\right) }{TM}}\right) \) , the map

\[
\nabla F : \underset{k\text{ copies }}{\underbrace{{\Omega }^{1}\left( M\right)  \times  \cdots  \times  {\Omega }^{1}\left( M\right) }} \times  \underset{l + 1\text{ copies }}{\underbrace{\mathfrak{X}\left( M\right)  \times  \cdots  \times  \mathfrak{X}\left( M\right) }} \rightarrow  {C}^{\infty }\left( M\right)
\]

given by

\[
\left( {\nabla F}\right) \left( {{\omega }^{1},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{Y}_{l}, X}\right)  = \left( {{\nabla }_{X}F}\right) \left( {{\omega }^{1},\ldots ,{\omega }^{k},{Y}_{1},\ldots ,{Y}_{l}}\right) \tag{4.14}
\]

defines a smooth \( \left( {k, l + 1}\right) \) -tensor field on \( M \) called the total covariant derivative of \( \mathbf{F} \) .

Proof. This follows immediately from the tensor characterization lemma (Lemma B.6): \( {\nabla }_{X}F \) is a tensor field, so it is multilinear over \( {C}^{\infty }\left( M\right) \) in its \( k + l \) arguments; and it is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) by definition of a connection.

When we write the components of a total covariant derivative in terms of a local frame, it is standard practice to use a semicolon to separate indices resulting from differentiation from the preceding indices. Thus, for example, if \( Y \) is a vector field written in coordinates as \( Y = {Y}^{i}{E}_{i} \) , the components of the \( \left( {1,1}\right) \) -tensor field \( \nabla Y \) are written \( {Y}^{i}{}_{;j} \) , so that

\[
\nabla Y = {Y}^{i};{}_{j}{E}_{i} \otimes  {\varepsilon }^{j},
\]

with

\[
{Y}^{i}{}_{;j} = {E}_{j}{Y}^{i} + {Y}^{k}{\Gamma }_{jk}^{i}.
\]

For a 1-form \( \omega \) , the formulas read

\[
\nabla \omega  = {\omega }_{i;j}{\varepsilon }^{i} \otimes  {\varepsilon }^{j},\;\text{ with }{\omega }_{i;j} = {E}_{j}{\omega }_{i} - {\omega }_{k}{\Gamma }_{ji}^{k}.
\]

More generally, the next lemma gives a formula for the components of total covariant derivatives of arbitrary tensor fields.

Proposition 4.18. Let \( M \) be a smooth manifold with or without boundary and let \( \nabla \) be a connection in \( {TM} \) ; and let \( \left( {E}_{i}\right) \) be a smooth local frame for \( {TM} \) and \( \left\{  {\Gamma }_{ij}^{k}\right\} \) the corresponding connection coefficients. The components of the total covariant derivative of a \( \left( {k, l}\right) \) -tensor field \( F \) with respect to this frame are given by

\[
{F}_{{j}_{1}\ldots {j}_{l};m}^{{i}_{1}\ldots {i}_{k}} = {E}_{m}\left( {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}\right)  + \mathop{\sum }\limits_{{s = 1}}^{k}{F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots p\ldots {i}_{k}}{\Gamma }_{mp}^{{i}_{s}} - \mathop{\sum }\limits_{{s = 1}}^{l}{F}_{{j}_{1}\ldots p\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{\Gamma }_{m{j}_{s}}^{p}.
\]

Exercise 4.19. Prove Proposition 4.18.

Exercise 4.20. Suppose \( F \) is a smooth \( \left( {k, l}\right) \) -tensor field and \( G \) is a smooth \( \left( {r, s}\right) \) - tensor field. Show that the components of the total covariant derivative of \( F \otimes  G \) are given by

\[
{\left( \nabla \left( F \otimes  G\right) \right) }_{{j}_{1}\ldots {j}_{l}{q}_{1}\ldots {q}_{s};m}^{{i}_{1}\ldots {i}_{k}{p}_{1}\ldots {p}_{r}} = {F}_{{j}_{1}\ldots {j}_{l};m}^{{i}_{1}\ldots {i}_{k}}{G}_{{q}_{1}\ldots {q}_{s}}^{{p}_{1}\ldots {p}_{r}} + {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{G}_{{q}_{1}\ldots {q}_{s};m}^{{p}_{1}\ldots {p}_{r}}.
\]

[Remark: This formula is often written in the following way, more suggestive of the product rule for ordinary derivatives:

\[
{\left( {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{G}_{{q}_{1}\ldots {q}_{s}}^{{p}_{1}\ldots {p}_{r}}\right) }_{;m} = {F}_{{j}_{1}\ldots {j}_{l};m}^{{i}_{1}\ldots {i}_{k}}{G}_{{q}_{1}\ldots {q}_{s}}^{{p}_{1}\ldots {p}_{r}} + {F}_{{j}_{1}\ldots {j}_{l}}^{{i}_{1}\ldots {i}_{k}}{G}_{{q}_{1}\ldots {q}_{s};m}^{{p}_{1}\ldots {p}_{r}}.
\]

Notice that this does not say that \( \nabla \left( {F \otimes  G}\right)  = \left( {\nabla F}\right)  \otimes  G + F \otimes  \left( {\nabla G}\right) \) , because in the first term on the right-hand side of this latter formula, the index resulting from differentiation is not the last lower index.]

## Second Covariant Derivatives

Having defined the tensor field \( \nabla F \) for a \( \left( {k, l}\right) \) -tensor field \( F \) , we can in turn take its total covariant derivative and obtain a \( \left( {k, l + 2}\right) \) -tensor field \( {\nabla }^{2}F = \nabla \left( {\nabla F}\right) \) . Given vector fields \( X, Y \in  \mathcal{X}\left( M\right) \) , let us introduce the notation \( {\nabla }_{X, Y}^{2}F \) for the \( \left( {k, l}\right) \) -tensor field obtained by inserting \( X, Y \) in the last two slots of \( {\nabla }^{2}F \) :

\[
{\nabla }_{X, Y}^{2}F\left( \ldots \right)  = {\nabla }^{2}F\left( {\ldots , Y, X}\right) .
\]

Note the reversal of order of \( X \) and \( Y \) : this is necessitated by our convention that the last index position in \( \nabla F \) is the one resulting from differentiation, while it is conventional to let \( {\nabla }_{X, Y}^{2} \) stand for differentiating first in the \( Y \) direction, then in the \( X \) direction. (For this reason, some authors adopt the convention that the new index position introduced by differentiation is the first instead of the last. As usual, be sure to check each author's conventions when you read.)

It is important to be aware that \( {\nabla }_{X, Y}^{2}F \) is not the same as \( {\nabla }_{X}\left( {{\nabla }_{Y}F}\right) \) . The main reason is that the former is linear over \( {C}^{\infty }\left( M\right) \) in \( Y \) , while the latter is not. The relationship between the two expressions is given in the following proposition.

Proposition 4.21. Let \( M \) be a smooth manifold with or without boundary and let \( \nabla \) be a connection in TM. For every smooth vector field or tensor field \( F \) ,

\[
{\nabla }_{X, Y}^{2}F = {\nabla }_{X}\left( {{\nabla }_{Y}F}\right)  - {\nabla }_{\left( {\nabla }_{X}Y\right) }F.
\]

Proof. A covariant derivative \( {\nabla }_{Y}F \) can be expressed as the trace of \( \nabla F \otimes  Y \) on its last two indices:

\[
{\nabla }_{Y}F = \operatorname{tr}\left( {\nabla F \otimes  Y}\right)
\]

as you can verify by noting that both expressions have the same component formula, \( {F}_{{j}_{1}\ldots {j}_{l};m}^{{i}_{1}\ldots {i}_{k}}{Y}^{m} \) . Similarly, \( {\nabla }_{X, Y}^{2}F \) can be expressed as an iterated trace:

\[
{\nabla }_{X, Y}^{2}F = \operatorname{tr}\left( {\operatorname{tr}\left( {{\nabla }^{2}F \otimes  X}\right)  \otimes  Y}\right) .
\]

(First trace the last index of \( {\nabla }^{2}F \) with that of \( X \) , and then trace the last remaining free index-originally the second-to-last in \( {\nabla }^{2}F \) -with that of \( Y \) .)

Therefore, since \( {\nabla }_{X} \) commutes with contraction and satisfies the product rule with respect to tensor products (Prop. 4.15), we have

\[
{\nabla }_{X}\left( {{\nabla }_{Y}F}\right)  = {\nabla }_{X}\left( {\operatorname{tr}\left( {\nabla F \otimes  Y}\right) }\right)
\]

\[
= \operatorname{tr}\left( {{\nabla }_{X}\left( {\nabla F \otimes  Y}\right) }\right)
\]

\[
= \operatorname{tr}\left( {{\nabla }_{X}\left( {\nabla F}\right)  \otimes  Y + \nabla F \otimes  {\nabla }_{X}Y}\right)
\]

\[
= \operatorname{tr}\left( {\operatorname{tr}\left( {{\nabla }^{2}F \otimes  X}\right)  \otimes  Y}\right)  + \operatorname{tr}\left( {\nabla F \otimes  {\nabla }_{X}Y}\right)
\]

\[
= {\nabla }_{X, Y}^{2}F + {\nabla }_{\left( {\nabla }_{X}Y\right) }F.
\]

Example 4.22 (The Covariant Hessian). Let \( u \) be a smooth function on \( M \) . Then \( \nabla u \in  \Gamma \left( {{T}^{\left( 0,1\right) }{TM}}\right)  = {\Omega }^{1}\left( M\right) \) is just the 1-form \( {du} \) , because both tensors have the same action on vectors: \( \nabla u\left( X\right)  = {\nabla }_{X}u = {Xu} = {du}\left( X\right) \) . The 2-tensor \( {\nabla }^{2}u = \; \nabla \left( {du}\right) \) is called the covariant Hessian of \( \mathbf{u} \) . Proposition 4.21 shows that its action on smooth vector fields \( X, Y \) can be computed by the following formula:

\[
{\nabla }^{2}u\left( {Y, X}\right)  = {\nabla }_{X, Y}^{2}u = {\nabla }_{X}\left( {{\nabla }_{Y}u}\right)  - {\nabla }_{\left( {\nabla }_{X}Y\right) }u = Y\left( {Xu}\right)  - \left( {{\nabla }_{Y}X}\right) u.
\]

In any local coordinates, it is

\[
{\nabla }^{2}u = {u}_{;{ij}}d{x}^{i} \otimes  d{x}^{j},\;\text{ with }{u}_{;{ij}} = {\partial }_{j}{\partial }_{i}u - {\Gamma }_{ji}^{k}{\partial }_{k}u.
\]

## Vector and Tensor Fields Along Curves

Now we can address the question that originally motivated the definition of connections: How can we make sense of the derivative of a vector field along a curve?

Let \( M \) be a smooth manifold with or without boundary. Given a smooth curve \( \gamma  : I \rightarrow  M \) , a vector field along \( \gamma \) is a continuous map \( V : I \rightarrow  {TM} \) such that \( V\left( t\right)  \in  {T}_{\gamma \left( t\right) }M \) for every \( t \in  I \) ; it is a smooth vector field along \( \gamma \) if it is smooth as a map from \( I \) to \( {TM} \) . We let \( \mathcal{X}\left( \gamma \right) \) denote the set of all smooth vector fields along \( \gamma \) . It is a real vector space under pointwise vector addition and multiplication by constants, and it is a module over \( {C}^{\infty }\left( I\right) \) with multiplication defined pointwise:

\[
\left( {fX}\right) \left( t\right)  = f\left( t\right) X\left( t\right) .
\]

The most obvious example of a vector field along a smooth curve \( \gamma \) is the curve’s velocity: \( {\gamma }^{\prime }\left( t\right)  \in  {T}_{\gamma \left( t\right) }M \) for each \( t \) , and its coordinate expression (4.1) shows that it is smooth. Here is another example: if \( \gamma \) is a curve in \( {\mathbb{R}}^{2} \) , let \( N\left( t\right)  = R{\gamma }^{\prime }\left( t\right) \) , where \( R \) is counterclockwise rotation by \( \pi /2 \) , so \( N\left( t\right) \) is normal to \( {\gamma }^{\prime }\left( t\right) \) . In standard coordinates, \( N\left( t\right)  = \left( {-{\dot{\gamma }}^{2}\left( t\right) ,{\dot{\gamma }}^{1}\left( t\right) }\right) \) , so \( N \) is a smooth vector field along \( \gamma \) .

A large supply of examples is provided by the following construction: suppose \( \gamma  : I \rightarrow  M \) is a smooth curve and \( \widetilde{V} \) is a smooth vector field on an open subset of \( M \) containing the image of \( \gamma \) . Define \( V : I \rightarrow  {TM} \) by setting \( V\left( t\right)  = {\widetilde{V}}_{\gamma \left( t\right) } \) for each \( t \in  I \) . Since \( V \) is equal to the composition \( \widetilde{V} \circ  \gamma \) , it is smooth. A smooth vector field along \( \gamma \) is said to be extendible if there exists a smooth vector field \( \widetilde{V} \) on a neighborhood of the image of \( \gamma \) that is related to \( V \) in this way (Fig. 4.4). Not every vector field along a curve need be extendible; for example, if \( \gamma \left( {t}_{1}\right)  = \gamma \left( {t}_{2}\right) \) but \( {\gamma }^{\prime }\left( {t}_{1}\right)  \neq  {\gamma }^{\prime }\left( {t}_{2}\right) \) (Fig. 4.5), then \( {\gamma }^{\prime } \) is not extendible. Even if \( \gamma \) is injective, its velocity need not be extendible, as the next example shows.

Example 4.23. Consider the figure eight curve \( \gamma  : \left( {-\pi ,\pi }\right)  \rightarrow  {\mathbb{R}}^{2} \) defined by

\[
\gamma \left( t\right)  = \left( {\sin {2t},\sin t}\right) .
\]

![bo_d7dtff491nqc73eq8m7g_113_225_188_490_371_0.jpg](images/bo_d7dtff491nqc73eq8m7g_113_225_188_490_371_0.jpg)

![bo_d7dtff491nqc73eq8m7g_113_804_317_488_242_0.jpg](images/bo_d7dtff491nqc73eq8m7g_113_804_317_488_242_0.jpg)

Fig. 4.4: Extendible vector field Fig. 4.5: Nonextendible vector field

![bo_d7dtff491nqc73eq8m7g_113_615_649_302_336_0.jpg](images/bo_d7dtff491nqc73eq8m7g_113_615_649_302_336_0.jpg)

Fig. 4.6: The image of the figure eight curve of Example 4.23

Its image is a set that looks like a figure eight in the plane (Fig. 4.6). Problem 4-7 asks you to show that \( \gamma \) is an injective smooth immersion, but its velocity vector field is not extendible. //

More generally, a tensor field along \( \gamma \) is a continuous map \( \sigma \) from \( I \) to some tensor bundle \( {T}^{\left( k, l\right) }{TM} \) such that \( \sigma \left( t\right)  \in  {T}^{\left( k, l\right) }\left( {{T}_{\gamma \left( t\right) }M}\right) \) for each \( t \in  I \) . It is a smooth tensor field along \( \gamma \) if it is smooth as a map from \( I \) to \( {T}^{\left( k, l\right) }{TM} \) , and it is extendible if there is a smooth tensor field \( \widetilde{\sigma } \) on a neighborhood of \( \gamma \left( I\right) \) such that \( \sigma  = \widetilde{\sigma } \circ  \gamma \)

## Covariant Derivatives Along Curves

Here is the promised interpretation of a connection as a way to take derivatives of vector fields along curves.

Theorem 4.24 (Covariant Derivative Along a Curve). Let \( M \) be a smooth manifold with or without boundary and let \( \nabla \) be a connection in \( {TM} \) . For each smooth curve \( \gamma  : I \rightarrow  M \) , the connection determines a unique operator

\[
{D}_{t} : \mathfrak{X}\left( \gamma \right)  \rightarrow  \mathfrak{X}\left( \gamma \right)
\]

called the covariant derivative along \( \gamma \) , satisfying the following properties:

(i) LINEARITY OVER R:

\[
{D}_{t}\left( {{aV} + {bW}}\right)  = a{D}_{t}V + b{D}_{t}W\;\text{ for }a, b \in  \mathbb{R}.
\]

(ii) PRODUCT RULE:

\[
{D}_{t}\left( {fV}\right)  = {f}^{\prime }V + f{D}_{t}V\;\text{ for }f \in  {C}^{\infty }\left( I\right) .
\]

(iii) If \( V \in  \mathfrak{X}\left( \gamma \right) \) is extendible, then for every extension \( \widetilde{V} \) of \( V \) ,

\[
{D}_{t}V\left( t\right)  = {\nabla }_{{\gamma }^{\prime }\left( t\right) }\widetilde{V}.
\]

There is an analogous operator on the space of smooth tensor fields of any type along \( \gamma \) .

Proof. For simplicity, we prove the theorem for the case of vector fields along \( \gamma \) ; the proof for arbitrary tensor fields is essentially identical except for notation.

First we show uniqueness. Suppose \( {D}_{t} \) is such an operator, and let \( {t}_{0} \in  I \) be arbitrary. An argument similar to that of Lemma 4.1 shows that the value of \( {D}_{t}V \) at \( {t}_{0} \) depends only on the values of \( V \) in any interval \( \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right) \) containing \( {t}_{0} \) . (If \( {t}_{0} \) is an endpoint of \( I \) , extend a coordinate representation of \( \gamma \) to a slightly bigger open interval, prove the lemma there, and then restrict back to \( I \) .)

Choose smooth coordinates \( \left( {x}^{i}\right) \) for \( M \) in a neighborhood of \( \gamma \left( {t}_{0}\right) \) , and write

\[
V\left( t\right)  = {\left. {V}^{j}\left( t\right) {\partial }_{j}\right| }_{\gamma \left( t\right) }
\]

for \( t \) near \( {t}_{0} \) , where \( {V}^{1},\ldots ,{V}^{n} \) are smooth real-valued functions defined on some neighborhood of \( {t}_{0} \) in \( I \) . By the properties of \( {D}_{t} \) , since each \( {\partial }_{j} \) is extendible,

\[
{D}_{t}V\left( t\right)  = {\left. {\dot{V}}^{j}\left( t\right) {\partial }_{j}\right| }_{\gamma \left( t\right) } + {\left. {V}^{j}\left( t\right) {\nabla }_{{\gamma }^{\prime }\left( t\right) }{\partial }_{j}\right| }_{\gamma \left( t\right) }
\]

\[
= {\left. \left( {\dot{V}}^{k}\left( t\right)  + {\dot{\gamma }}^{i}\left( t\right) {V}^{j}\left( t\right) {\Gamma }_{ij}^{k}\left( \gamma \left( t\right) \right) \right) {\partial }_{k}\right| }_{\gamma \left( t\right) }. \tag{4.15}
\]

This shows that such an operator is unique if it exists.

For existence, if \( \gamma \left( I\right) \) is contained in a single chart, we can define \( {D}_{t}V \) by (4.15); the easy verification that it satisfies the requisite properties is left as an exercise. In the general case, we can cover \( \gamma \left( I\right) \) with coordinate charts and define \( {D}_{t}V \) by this formula in each chart, and uniqueness implies that the various definitions agree whenever two or more charts overlap.

(It is worth noting that in the physics literature, the covariant derivative along a curve is sometimes called the absolute derivative.)

---

Exercise 4.25. Complete the proof of Theorem 4.24 by showing that the operator \( {D}_{t} \) defined in coordinates by (4.15) satisfies properties (i)-(iii).

---

Apart from its use in proving existence of the covariant derivative along a curve, (4.15) also gives a practical formula for computing such covariant derivatives in coordinates.

Now we can improve Proposition 4.5 by showing that \( {\nabla }_{v}Y \) actually depends only on the values of \( Y \) along any curve through \( p \) whose velocity is \( v \) .

Proposition 4.26. Let \( M \) be a smooth manifold with or without boundary, let \( \nabla \) be a connection in \( {TM} \) , and let \( p \in  M \) and \( v \in  {T}_{p}M \) . Suppose \( Y \) and \( \widetilde{Y} \) are two smooth vector fields that agree at points in the image of some smooth curve \( \gamma  : I \rightarrow  M \) such that \( \gamma \left( {t}_{0}\right)  = p \) and \( {\gamma }^{\prime }\left( {t}_{0}\right)  = v \) . Then \( {\nabla }_{v}Y = {\nabla }_{v}\widetilde{Y} \) .

Proof. We can define a smooth vector field \( Z \) along \( \gamma \) by \( Z\left( t\right)  = {Y}_{\gamma \left( t\right) } = {\widetilde{Y}}_{\gamma \left( t\right) } \) . Since both \( Y \) and \( \widetilde{Y} \) are extensions of \( Z \) , it follows from condition (iii) in Theorem 4.24 that both \( {\nabla }_{v}Y \) and \( {\nabla }_{v}\widetilde{Y} \) are equal to \( {D}_{t}Z\left( {t}_{0}\right) \) .

## Geodesics

Armed with the notion of covariant differentiation along curves, we can now define acceleration and geodesics.

Let \( M \) be a smooth manifold with or without boundary and let \( \nabla \) be a connection in \( {TM} \) . For every smooth curve \( \gamma  : I \rightarrow  M \) , we define the acceleration of \( \gamma \) to be the vector field \( {D}_{t}{\gamma }^{\prime } \) along \( \gamma \) . A smooth curve \( \gamma \) is called a geodesic (with respect to \( \nabla ) \) if its acceleration is zero: \( {D}_{t}{\gamma }^{\prime } \equiv  0 \) . In terms of smooth coordinates \( \left( {x}^{i}\right) \) , if we write the component functions of \( \gamma \) as \( \gamma \left( t\right)  = \left( {{x}^{1}\left( t\right) ,\ldots ,{x}^{n}\left( t\right) }\right) \) , then it follows from (4.15) that \( \gamma \) is a geodesic if and only if its component functions satisfy the following geodesic equation:

\[
{\ddot{x}}^{k}\left( t\right)  + {\dot{x}}^{i}\left( t\right) {\dot{x}}^{j}\left( t\right) {\Gamma }_{ij}^{k}\left( {x\left( t\right) }\right)  = 0, \tag{4.16}
\]

where we use \( x\left( t\right) \) as an abbreviation for the \( n \) -tuple of component functions \( \left( {{x}^{1}\left( t\right) ,\ldots ,{x}^{n}\left( t\right) }\right) \) . This is a system of second-order ordinary differential equations (ODEs) for the real-valued functions \( {x}^{1},\ldots ,{x}^{n} \) . The next theorem uses ODE theory to prove existence and uniqueness of geodesics with suitable initial conditions. (Because difficulties can arise when a geodesic starts on the boundary or later hits the boundary, we state and prove this theorem only for manifolds without boundary.)

Theorem 4.27 (Existence and Uniqueness of Geodesics). Let \( M \) be a smooth manifold and \( \nabla \) a connection in \( {TM} \) . For every \( p \in  M, w \in  {T}_{p}M \) , and \( {t}_{0} \in  \mathbb{R} \) , there exist an open interval \( I \subseteq  \mathbb{R} \) containing \( {t}_{0} \) and a geodesic \( \gamma  : I \rightarrow  M \) satisfying \( \gamma \left( {t}_{0}\right)  = p \) and \( {\gamma }^{\prime }\left( {t}_{0}\right)  = w \) . Any two such geodesics agree on their common domain.

Proof. Let \( \left( {x}^{i}\right) \) be smooth coordinates on some neighborhood \( U \) of \( p \) . A smooth curve in \( U \) , written as \( \gamma \left( t\right)  = \left( {{x}^{1}\left( t\right) ,\ldots ,{x}^{n}\left( t\right) }\right) \) , is a geodesic if and only if its component functions satisfy (4.16). The standard trick for proving existence and uniqueness for such a second-order system is to introduce auxiliary variables \( {v}^{i} = \; {\dot{x}}^{i} \) to convert it to the following equivalent first-order system in twice the number of variables:

(4.17)

\[
{\dot{x}}^{k}\left( t\right)  = {v}^{k}\left( t\right) ,
\]

\[
{\dot{v}}^{k}\left( t\right)  =  - {v}^{i}\left( t\right) {v}^{j}\left( t\right) {\Gamma }_{ij}^{k}\left( {x\left( t\right) }\right) .
\]

![bo_d7dtff491nqc73eq8m7g_116_461_188_603_193_0.jpg](images/bo_d7dtff491nqc73eq8m7g_116_461_188_603_193_0.jpg)

Fig. 4.7: Uniqueness of geodesics

Treating \( \left( {{x}^{1},\ldots ,{x}^{n},{v}^{1},\ldots ,{v}^{n}}\right) \) as coordinates on \( U \times  {\mathbb{R}}^{n} \) , we can recognize (4.17) as the equations for the flow of the vector field \( G \in  \mathfrak{X}\left( {U \times  {\mathbb{R}}^{n}}\right) \) given by

\[
{G}_{\left( x, v\right) } = {\left. {v}^{k}\frac{\partial }{\partial {x}^{k}}\right| }_{\left( x, v\right) } - {\left. {v}^{i}{v}^{j}{\Gamma }_{ij}^{k}\left( x\right) \frac{\partial }{\partial {v}^{k}}\right| }_{\left( x, v\right) }. \tag{4.18}
\]

By the fundamental theorem on flows (Thm. A.42), for each \( \left( {p, w}\right)  \in  U \times  {\mathbb{R}}^{n} \) and \( {t}_{0} \in  \mathbb{R} \) , there exist an open interval \( {I}_{0} \) containing \( {t}_{0} \) and a unique smooth solution \( \zeta  : {I}_{0} \rightarrow  U \times  {\mathbb{R}}^{n} \) to this system satisfying the initial condition \( \zeta \left( {t}_{0}\right)  = \left( {p, w}\right) \) . If we write the component functions of \( \zeta \) as \( \zeta \left( t\right)  = \left( {{x}^{i}\left( t\right) ,{v}^{i}\left( t\right) }\right) \) , then we can easily check that the curve \( \gamma \left( t\right)  = \left( {{x}^{1}\left( t\right) ,\ldots ,{x}^{n}\left( t\right) }\right) \) in \( U \) satisfies the existence claim of the theorem.

To prove the uniqueness claim, suppose \( \gamma ,\widetilde{\gamma } : I \rightarrow  M \) are both geodesics defined on some open interval with \( \gamma \left( {t}_{0}\right)  = \widetilde{\gamma }\left( {t}_{0}\right) \) and \( {\gamma }^{\prime }\left( {t}_{0}\right)  = {\widetilde{\gamma }}^{\prime }\left( {t}_{0}\right) \) . In any local coordinates around \( \gamma \left( {t}_{0}\right) \) , we can define smooth curves \( \zeta ,\widetilde{\zeta } : \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right)  \rightarrow  U \times  {\mathbb{R}}^{n} \) as above. These curves both satisfy the same initial value problem for the system (4.17), so by the uniqueness of ODE solutions, they agree on \( \left( {{t}_{0} - \varepsilon ,{t}_{0} + \varepsilon }\right) \) for some \( \varepsilon  > 0 \) . Suppose for the sake of contradiction that \( \gamma \left( b\right)  \neq  \widetilde{\gamma }\left( b\right) \) for some \( b \in  I \) . First suppose \( b > {t}_{0} \) , and let \( \beta \) be the infimum of numbers \( b \in  I \) such that \( b > {t}_{0} \) and \( \gamma \left( b\right)  \neq  \widetilde{\gamma }\left( b\right) \) (Fig. 4.7). Then \( \beta  \in  I \) , and by continuity, \( \gamma \left( \beta \right)  = \widetilde{\gamma }\left( \beta \right) \) and \( {\gamma }^{\prime }\left( \beta \right)  = {\widetilde{\gamma }}^{\prime }\left( \beta \right) \) . Applying local uniqueness in a neighborhood of \( \beta \) , we conclude that \( \gamma \) and \( \widetilde{\gamma } \) agree on a neighborhood of \( \beta \) , which contradicts our choice of \( \beta \) . Arguing similarly to the left of \( {t}_{0} \) , we conclude that \( \gamma  \equiv  \widetilde{\gamma } \) on all of \( I \) .

A geodesic \( \gamma  : I \rightarrow  M \) is said to be maximal if it cannot be extended to a geodesic on a larger interval, that is, if there does not exist a geodesic \( \widetilde{\gamma } : \widetilde{I} \rightarrow  M \) defined on an interval \( \widetilde{I} \) properly containing \( I \) and satisfying \( \widetilde{\gamma }{\left. \right| }_{I} = \gamma \) . A geodesic segment is a geodesic whose domain is a compact interval.

![bo_d7dtff491nqc73eq8m7g_117_319_190_890_452_0.jpg](images/bo_d7dtff491nqc73eq8m7g_117_319_190_890_452_0.jpg)

Fig. 4.8: A parallel vector field along a curve

Corollary 4.28. Let \( M \) be a smooth manifold and let \( \nabla \) be a connection in \( {TM} \) . For each \( p \in  M \) and \( v \in  {T}_{p}M \) , there is a unique maximal geodesic \( \gamma  : I \rightarrow  M \) with \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) , defined on some open interval \( I \) containing 0 .

Proof. Given \( p \in  M \) and \( v \in  {T}_{p}M \) , let \( I \) be the union of all open intervals containing 0 on which there is a geodesic with the given initial conditions. By Theorem 4.27, all such geodesics agree where they overlap, so they define a geodesic \( \gamma  : I \rightarrow  M \) , which is obviously the unique maximal geodesic with the given initial conditions.

Exercise 4.29. Show that the maximal geodesics on \( {\mathbb{R}}^{n} \) with respect to the Euclidean connection (4.3) are exactly the constant curves and the straight lines with constant-speed parametrizations.

The unique maximal geodesic \( \gamma \) with \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = v \) is often called simply the geodesic with initial point \( p \) and initial velocity \( v \) , and is denoted by \( {\gamma }_{v} \) . (For simplicity, we do not specify the initial point \( p \) in the notation; it can implicitly be recovered from \( v \) by \( p = \pi \left( v\right) \) , where \( \pi  : {TM} \rightarrow  M \) is the natural projection.)

## Parallel Transport

Another construction involving covariant differentiation along curves that will be useful later is called parallel transport. As we did with geodesics, we restrict attention here to manifolds without boundary.

Let \( M \) be a smooth manifold and let \( \nabla \) be a connection in \( {TM} \) . A smooth vector or tensor field \( V \) along a smooth curve \( \gamma \) is said to be parallel along \( \gamma \) (with respect to \( \nabla \) ) if \( {D}_{t}V \equiv  0 \) (Fig. 4.8). Thus a geodesic can be characterized as a curve whose velocity vector field is parallel along the curve.

Exercise 4.30. Let \( \gamma  : I \rightarrow  {\mathbb{R}}^{n} \) be a smooth curve, and let \( V \) be a smooth vector field along \( \gamma \) . Show that \( V \) is parallel along \( \gamma \) with respect to the Euclidean connection if and only if its component functions (with respect to the standard basis) are constants.

The fundamental fact about parallel vector and tensor fields along curves is that every tangent vector or tensor at any point on a curve can be uniquely extended to a parallel field along the entire curve. Before we prove this claim, let us examine what the equation of parallelism looks like in coordinates. Given a smooth curve \( \gamma \) with a local coordinate representation \( \gamma \left( t\right)  = \left( {{\gamma }^{1}\left( t\right) ,\ldots ,{\gamma }^{n}\left( t\right) }\right) \) , formula (4.15) shows that a vector field \( V \) is parallel along \( \gamma \) if and only if

\[
{\dot{V}}^{k}\left( t\right)  =  - {V}^{j}\left( t\right) {\dot{\gamma }}^{i}\left( t\right) {\Gamma }_{ij}^{k}\left( {\gamma \left( t\right) }\right) ,\;k = 1,\ldots , n, \tag{4.19}
\]

with analogous expressions based on Proposition 4.18 for tensor fields of other types. In each case, this is a system of first-order linear ordinary differential equations for the unknown coefficients of the vector or tensor field—in the vector case, the functions \( \left( {{V}^{1}\left( t\right) ,\ldots ,{V}^{n}\left( t\right) }\right) \) . The usual ODE theorem guarantees the existence and uniqueness of a solution for a short time, given any initial values at \( t = {t}_{0} \) ; but since the equation is linear, we can actually show much more: there exists a unique solution on the entire parameter interval.

Theorem 4.31 (Existence, Uniqueness, and Smoothness for Linear ODEs). Let \( I \subseteq  \mathbb{R} \) be an open interval, and for \( 1 \leq  j, k \leq  n \) , let \( {A}_{j}^{k} : I \rightarrow  \mathbb{R} \) be smooth functions. For all \( {t}_{0} \in  I \) and every initial vector \( \left( {{c}^{1},\ldots ,{c}^{n}}\right)  \in  {\mathbb{R}}^{n} \) , the linear initial value problem

(4.20)

\[
{\dot{V}}^{k}\left( t\right)  = {A}_{j}^{k}\left( t\right) {V}^{j}\left( t\right)
\]

\[
{V}^{k}\left( {t}_{0}\right)  = {c}^{k},
\]

has a unique smooth solution on all of \( I \) , and the solution depends smoothly on \( \left( {t, c}\right)  \in  I \times  {\mathbb{R}}^{n} \) .

Proof. First assume \( {t}_{0} = 0 \) . Let \( \left( {{x}^{0},{x}^{1},\ldots ,{x}^{n}}\right) \) denote standard coordinates on the manifold \( I \times  {\mathbb{R}}^{n} \subseteq  {\mathbb{R}}^{n + 1} \) , and consider the vector field \( Y \in  \mathfrak{X}\left( {I \times  {\mathbb{R}}^{n}}\right) \) defined by

\[
Y = \frac{\partial }{\partial {x}^{0}} + {A}_{j}^{1}\left( {x}^{0}\right) {x}^{j}\frac{\partial }{\partial {x}^{1}} + \cdots  + {A}_{j}^{n}\left( {x}^{0}\right) {x}^{j}\frac{\partial }{\partial {x}^{n}}.
\]

If \( V\left( t\right)  = \left( {{V}^{1}\left( t\right) ,\ldots ,{V}^{n}\left( t\right) }\right) \) is a solution to (4.20) with \( {t}_{0} = 0 \) defined on some interval \( {I}_{0} \subseteq  I \) , then the curve \( \eta \left( t\right)  = \left( {t,{V}^{1}\left( t\right) ,\ldots ,{V}^{n}\left( t\right) }\right) \) is an integral curve of \( Y \) defined on \( {I}_{0} \) satisfying the initial condition

\[
\eta \left( 0\right)  = \left( {0,{c}^{1},\ldots ,{c}^{n}}\right) . \tag{4.21}
\]

Conversely, for each \( \left( {{c}^{1},\ldots ,{c}^{n}}\right)  \in  {\mathbb{R}}^{n} \) , there is an integral curve \( \eta \) of \( Y \) defined on some open interval \( {I}_{0} \subseteq  I \) containing 0 and satisfying (4.21). If we write the component functions of \( \eta \) as \( \eta \left( t\right)  = \left( {{\eta }^{0}\left( t\right) ,{\eta }^{1}\left( t\right) ,\ldots ,{\eta }^{n}\left( t\right) }\right) \) , then \( {\dot{\eta }}^{0}\left( t\right)  \equiv  1 \) and \( {\eta }^{0}\left( 0\right)  = 0 \) , so \( \eta \left( t\right)  = t \) for all \( t \) . It then follows that \( V\left( t\right)  = \left( {{\eta }^{1}\left( t\right) ,\ldots ,{\eta }^{n}\left( t\right) }\right) \) solves (4.20) with \( {t}_{0} = 0 \) . Thus there is a one-to-one correspondence between solutions to (4.20) and integral curves of \( Y \) satisfying (4.21).

The fundamental theorem on flows of vector fields (Thm. A.42) guarantees that for each \( \left( {{c}^{1},\ldots ,{c}^{n}}\right)  \in  {\mathbb{R}}^{n} \) , there exists a maximal integral curve \( \eta \) of \( Y \) defined on some open interval containing 0 and satisfying the initial condition (4.21), and the solutions depend smoothly on \( \left( {t, c}\right) \) . Therefore, there is a solution to (4.20) for \( t \) in some maximal interval \( {I}_{0} \subseteq  I \) , and we need only show that \( {I}_{0} = I \) . Write \( I = \left( {a, b}\right) \) and \( {I}_{0} = \left( {{a}_{0},{b}_{0}}\right) \) (where \( a, b,{a}_{0},{b}_{0} \) can be finite or infinite), and assume for the sake of contradiction that \( {b}_{0} < b \) .

Let us use the differential equation to estimate the derivative of \( {\left| V\left( t\right) \right| }^{2} \) :

\[
\frac{d}{dt}{\left| V\left( t\right) \right| }^{2} = 2\mathop{\sum }\limits_{k}{\dot{V}}^{k}\left( t\right) {V}^{k}\left( t\right)
\]

\[
= 2\mathop{\sum }\limits_{{j, k}}{A}_{j}^{k}\left( t\right) {V}^{j}\left( t\right) {V}^{k}\left( t\right)
\]

\[
= {2V}{\left( t\right) }^{T}A\left( t\right) V\left( t\right)  \leq  2\left| {A\left( t\right) }\right| {\left| V\left( t\right) \right| }^{2}.
\]

Here \( \left| \cdot \right| \) denotes the Frobenius norm of a vector or matrix, obtained by summing the squares of all the components and taking the square root. (It is just the Euclidean norm of the components.) On the compact interval \( \left\lbrack  {0,{b}_{0}}\right\rbrack   \subseteq  I \) , the functions \( {A}_{j}^{k} \) are all bounded, so there is a constant \( M \) such that \( \left| {A\left( t\right) }\right|  \leq  M \) there. It then follows that

\[
\frac{d}{dt}\left( {{e}^{-{2Mt}}{\left| V\left( t\right) \right| }^{2}}\right)  = {e}^{-{2Mt}}\left( {\frac{d}{dt}{\left| V\left( t\right) \right| }^{2} - {2M}{\left| V\left( t\right) \right| }^{2}}\right)  \leq  0,
\]

so the expression \( {e}^{-{2Mt}}{\left| V\left( t\right) \right| }^{2} \) is a nonincreasing function of \( t \) , and thus is bounded for all \( t \in  \left\lbrack  {0,{b}_{0}}\right) \) by its initial value \( {\left| V\left( 0\right) \right| }^{2} \) . This implies \( {\left| V\left( t\right) \right| }^{2} \leq  {e}^{2Mt}{\left| V\left( 0\right) \right| }^{2} \) for \( t \in  \left\lbrack  {0,{b}_{0}}\right) \) , which in turn implies that the corresponding integral curve of \( Y \) stays in the compact set \( \left\lbrack  {0,{b}_{0}}\right\rbrack   \times  {\bar{B}}_{R}\left( 0\right)  \subseteq  I \times  {\mathbb{R}}^{n} \) , where \( R = {e}^{M{b}_{0}}\left| {V\left( 0\right) }\right| \) . This contradicts the escape lemma (Lemma A.43), and shows that \( {b}_{0} = b \) . The possibility that \( a < {a}_{0} \) can be ruled out by applying the same reasoning to the vector field \( - Y \) .

Finally, the case of general \( {t}_{0} \in  I \) can be reduced to the previous case by making the substitutions \( {V}^{k}\left( t\right)  = {\widetilde{V}}^{k}\left( {t - {t}_{0}}\right) \) and \( {A}_{j}^{k}\left( t\right)  = {\widetilde{A}}_{j}^{k}\left( {t - {t}_{0}}\right) \) .

Theorem 4.32 (Existence and Uniqueness of Parallel Transport). Suppose \( M \) is a smooth manifold with or without boundary, and \( \nabla \) is a connection in \( {TM} \) . Given a smooth curve \( \gamma  : I \rightarrow  M,{t}_{0} \in  I \) , and a vector \( v \in  {T}_{\gamma \left( {t}_{0}\right) }M \) or tensor \( v \in \; {T}^{\left( k, l\right) }\left( {{T}_{\gamma \left( t\right) }M}\right) \) , there exists a unique parallel vector or tensor field \( V \) along \( \gamma \) such that \( V\left( {t}_{0}\right)  = v \) .

Proof. As in the proof of Theorem 4.24, we carry out the proof for vector fields. The case of tensor fields differs only in notation.

First suppose \( \gamma \left( I\right) \) is contained in a single coordinate chart. Then \( V \) is parallel along \( \gamma \) if and only if its components satisfy the linear system of ODEs (4.19). Theorem 4.31 guarantees the existence and uniqueness of a solution on all of \( I \) with any initial condition \( V\left( {t}_{0}\right)  = v \) .

![bo_d7dtff491nqc73eq8m7g_120_412_194_706_556_0.jpg](images/bo_d7dtff491nqc73eq8m7g_120_412_194_706_556_0.jpg)

Fig. 4.9: Existence and uniqueness of parallel transports

Now suppose \( \gamma \left( I\right) \) is not covered by a single chart. Let \( \beta \) denote the supremum of all \( b > {t}_{0} \) for which a unique parallel transport exists on \( \left\lbrack  {{t}_{0}, b}\right\rbrack \) . (The argument for \( t < {t}_{0} \) is similar.) We know that \( \beta  > {t}_{0} \) , since for \( b \) close enough to \( {t}_{0},\gamma \left( \left\lbrack  {{t}_{0}, b}\right\rbrack  \right) \) is contained in a single chart and the above argument applies. Then a unique parallel transport \( V \) exists on \( \left\lbrack  {{t}_{0},\beta }\right) \) (Fig. 4.9). If \( \beta \) is equal to sup \( I \) , we are done. If not, choose smooth coordinates on an open set containing \( \gamma \left( {\beta  - \delta ,\beta  + \delta }\right) \) for some positive \( \delta \) . Then there exists a unique parallel vector field \( \widetilde{V} \) on \( \left( {\beta  - \delta ,\beta  + \delta }\right) \) satisfying the initial condition \( \widetilde{V}\left( {\beta  - \delta /2}\right)  = V\left( {\beta  - \delta /2}\right) \) . By uniqueness, \( V = \widetilde{V} \) on their common domain, and therefore \( \widetilde{V} \) is a parallel extension of \( V \) past \( \beta \) , which is a contradiction.

The vector or tensor field whose existence and uniqueness are proved in Theorem 4.32 is called the parallel transport of \( v \) along \( \gamma \) . For each \( {t}_{0},{t}_{1} \in  I \) , we define a map

\[
{P}_{{t}_{0}{t}_{1}}^{\gamma } : {T}_{\gamma \left( {t}_{0}\right) }M \rightarrow  {T}_{\gamma \left( {t}_{1}\right) }M \tag{4.22}
\]

called the parallel transport map, by setting \( {P}_{{t}_{0}{t}_{1}}^{\gamma }\left( v\right)  = V\left( {t}_{1}\right) \) for each \( v \in  {T}_{\gamma \left( {t}_{0}\right) }M \) , where \( V \) is the parallel transport of \( v \) along \( \gamma \) . This map is linear, because the equation of parallelism is linear. It is in fact an isomorphism, because \( {P}_{{t}_{1}{t}_{0}}^{\gamma } \) is an inverse for it.

It is also useful to extend the parallel transport operation to curves that are merely piecewise smooth. Given an admissible curve \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) , a map \( V : \left\lbrack  {a, b}\right\rbrack   \rightarrow \; {TM} \) such that \( V\left( t\right)  \in  {T}_{\gamma \left( t\right) }M \) for each \( t \) is called a piecewise smooth vector field along \( \gamma \) if \( V \) is continuous and there is an admissible partition \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) for \( \gamma \) such that \( V \) is smooth on each subinterval \( \left\lbrack  {{a}_{i - 1},{a}_{i}}\right\rbrack \) . We will call any such partition an admissible partition for \( V \) . A piecewise smooth vector field \( V \) along \( \gamma \) is said to be parallel along \( \gamma \) if \( {D}_{t}V = 0 \) wherever \( V \) is smooth.

Corollary 4.33 (Parallel Transport Along Piecewise Smooth Curves). Suppose \( M \) is a smooth manifold with or without boundary, and \( \nabla \) is a connection in \( {TM} \) . Given an admissible curve \( \gamma  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  M \) and a vector \( v \in  {T}_{\gamma \left( {t}_{0}\right) }M \) or tensor \( v \in \; {T}^{\left( k, l\right) }\left( {{T}_{\gamma \left( t\right) }M}\right) \) , there exists a unique piecewise smooth parallel vector or tensor field \( V \) along \( \gamma \) such that \( V\left( a\right)  = v \) , and \( V \) is smooth wherever \( \gamma \) is.

Proof. Let \( \left( {{a}_{0},\ldots ,{a}_{k}}\right) \) be an admissible partition for \( \gamma \) . First define \( {\left. V\right| }_{\left\lbrack  {a}_{0},{a}_{1}\right\rbrack  } \) to be the parallel transport of \( v \) along the first smooth segment \( {\left. \gamma \right| }_{\left\lbrack  {a}_{0},{a}_{1}\right\rbrack  } \) ; then define \( {\left. V\right| }_{\left\lbrack  {a}_{1},{a}_{2}\right\rbrack  } \) to be the parallel transport of \( V\left( {a}_{1}\right) \) along the next smooth segment \( {\left. \gamma \right| }_{\left\lbrack  {a}_{1},{a}_{2}\right\rbrack  } \) ; and continue by induction.

Here is an extremely useful tool for working with parallel transport. Given any basis \( \left( {{b}_{1},\ldots ,{b}_{n}}\right) \) for \( {T}_{\gamma \left( {t}_{0}\right) }M \) , we can parallel transport the vectors \( {b}_{i} \) along \( \gamma \) , thus obtaining an \( n \) -tuple of parallel vector fields \( \left( {{E}_{1},\ldots ,{E}_{n}}\right) \) along \( \gamma \) . Because each parallel transport map is an isomorphism, the vectors \( \left( {{E}_{i}\left( t\right) }\right) \) form a basis for \( {T}_{\gamma \left( t\right) }M \) at each point \( \gamma \left( t\right) \) . Such an \( n \) -tuple of vector fields along \( \gamma \) is called a parallel frame along \( \gamma \) . Every smooth (or piecewise smooth) vector field along \( \gamma \) can be expressed in terms of such a frame as \( V\left( t\right)  = {V}^{i}\left( t\right) {E}_{i}\left( t\right) \) , and then the properties of covariant derivatives along curves, together with the fact that the \( {E}_{i} \) ’s are parallel, imply

\[
{D}_{t}V\left( t\right)  = {\dot{V}}^{i}\left( t\right) {E}_{i}\left( t\right) \tag{4.23}
\]

wherever \( V \) and \( \gamma \) are smooth. This means that a vector field is parallel along \( \gamma \) if and only if its component functions with respect to the frame \( \left( {E}_{i}\right) \) are constants.

The parallel transport map is the means by which a connection "connects" nearby tangent spaces. The next theorem and its corollary show that parallel transport determines covariant differentiation along curves, and thereby the connection itself.

Theorem 4.34 (Parallel Transport Determines Covariant Differentiation). Let \( M \) be a smooth manifold with or without boundary, and let \( \nabla \) be a connection in TM. Suppose \( \gamma  : I \rightarrow  M \) is a smooth curve and \( V \) is a smooth vector field along \( \gamma \) . For each \( {t}_{0} \in  I \) ,

\[
{D}_{t}V\left( {t}_{0}\right)  = \mathop{\lim }\limits_{{{t}_{1} \rightarrow  {t}_{0}}}\frac{{P}_{{t}_{1}{t}_{0}}^{\gamma }V\left( {t}_{1}\right)  - V\left( {t}_{0}\right) }{{t}_{1} - {t}_{0}}. \tag{4.24}
\]

Proof. Let \( \left( {E}_{i}\right) \) be a parallel frame along \( \gamma \) , and write \( V\left( t\right)  = {V}^{i}\left( t\right) {E}_{i}\left( t\right) \) for \( t \in  I \) . On the one hand,(4.23) shows that \( {D}_{t}V\left( {t}_{0}\right)  = {\dot{V}}^{i}\left( {t}_{0}\right) {E}_{i}\left( {t}_{0}\right) \) .

On the other hand, for every fixed \( {t}_{1} \in  I \) , the parallel transport of the vector \( V\left( {t}_{1}\right) \) along \( \gamma \) is the constant-coefficient vector field \( W\left( t\right)  = {V}^{i}\left( {t}_{1}\right) {E}_{i}\left( t\right) \) along \( \gamma \) , so \( {P}_{{t}_{1}{t}_{0}}^{\gamma }V\left( {t}_{1}\right)  = {V}^{i}\left( {t}_{1}\right) {E}_{i}\left( {t}_{0}\right) \) . Inserting these formulas into (4.24) and taking the limit as \( {t}_{1} \rightarrow  {t}_{0} \) , we conclude that the right-hand side is also equal to \( {\dot{V}}^{i}\left( {t}_{0}\right) {E}_{i}\left( {t}_{0}\right) \) .

Corollary 4.35 (Parallel Transport Determines the Connection). Let \( M \) be a smooth manifold with or without boundary, and let \( \nabla \) be a connection in TM. Suppose \( X \) and \( Y \) are smooth vector fields on \( M \) . For every \( p \in  M \) ,

\[
{\left. {\nabla }_{X}Y\right| }_{p} = \mathop{\lim }\limits_{{h \rightarrow  0}}\frac{{P}_{h0}^{\gamma }{Y}_{\gamma \left( h\right) } - {Y}_{p}}{h}, \tag{4.25}
\]

where \( \gamma  : I \rightarrow  M \) is any smooth curve such that \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = {X}_{p} \) .

Proof. Given \( p \in  M \) and a smooth curve \( \gamma \) such that \( \gamma \left( 0\right)  = p \) and \( {\gamma }^{\prime }\left( 0\right)  = {X}_{p} \) , let \( V\left( t\right) \) denote the vector field along \( \gamma \) determined by \( Y \) , so \( V\left( t\right)  = {Y}_{\gamma \left( t\right) } \) . By property (iii) of Theorem 4.24, \( {\left. {\nabla }_{X}Y\right| }_{p} \) is equal to \( {D}_{t}V\left( 0\right) \) , so the result follows from Theorem 4.34.

A smooth vector or tensor field on \( M \) is said to be parallel (with respect to \( \nabla \) ) if it is parallel along every smooth curve in \( M \) . For example, Exercise 4.30 shows that every constant-coefficient vector field on \( {\mathbb{R}}^{n} \) is parallel.

Proposition 4.36. Suppose \( M \) is a smooth manifold with or without boundary, \( \nabla \) is a connection in \( {TM} \) , and \( A \) is a smooth vector or tensor field on \( M \) . Then \( A \) is parallel on \( M \) if and only if \( \nabla A \equiv  0 \) .

Proof. Problem 4-12.

Although Theorem 4.32 showed that it is always possible to extend a vector at a point to a parallel vector field along any given curve, it may not be possible in general to extend it to a parallel vector field on an open subset of the manifold. The impossibility of finding such extensions is intimately connected with the phenomenon of curvature, which will occupy a major portion of our attention in the second half of the book.

## Pullback Connections

Like vector fields, connections in the tangent bundle cannot be either pushed forward or pulled back by arbitrary smooth maps. However, there is a natural way to pull back such connections by means of a diffeomorphism. In this section we define this operation and enumerate some of its most important properties.

Suppose \( M \) and \( \widetilde{M} \) are smooth manifolds and \( \varphi  : M \rightarrow  \widetilde{M} \) is a diffeomorphism. For a smooth vector field \( X \in  \mathcal{X}\left( M\right) \) , recall that the pushforward of \( X \) is the unique vector field \( {\varphi }_{ * }X \in  \mathfrak{X}\left( \widetilde{M}\right) \) that satisfies \( d{\varphi }_{p}\left( {X}_{p}\right)  = {\left( {\varphi }_{ * }X\right) }_{\varphi \left( p\right) } \) for all \( p \in  M \) . (See Lemma A.36.)

Lemma 4.37 (Pullback Connections). Suppose \( M \) and \( \widetilde{M} \) are smooth manifolds with or without boundary. If \( \widetilde{\nabla } \) is a connection in \( T\widetilde{M} \) and \( \varphi  : M \rightarrow  \widetilde{M} \) is a diffeomorphism, then the map \( {\varphi }^{ * }\widetilde{\nabla } : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) defined by

\[
{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Y = {\left( {\varphi }^{-1}\right) }_{ * }\left( {{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right) }\right) \tag{4.26}
\]

is a connection in \( {TM} \) , called the pullback of \( \widetilde{\nabla } \) by \( \varphi \) .

Proof. It is immediate from the definition that \( {\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Y \) is linear over \( \mathbb{R} \) in \( Y \) . To see that it is linear over \( {C}^{\infty }\left( M\right) \) in \( X \) , let \( f \in  {C}^{\infty }\left( M\right) \) , and let \( \widetilde{f} = f \circ  {\varphi }^{-1} \) , so \( {\varphi }_{ * }\left( {fX}\right)  = \widetilde{f}{\varphi }_{ * }X \) . Then

\[
{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{fX}Y = {\left( {\varphi }^{-1}\right) }_{ * }\left( {{\widetilde{\nabla }}_{\widetilde{f}{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right) }\right)
\]

\[
= {\left( {\varphi }^{-1}\right) }_{ * }\left( {\widetilde{f}{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right) }\right)
\]

\[
= f{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Y
\]

Finally, to prove the product rule in \( Y \) , let \( f \) and \( \widetilde{f} \) be as above, and note that (A.7) implies \( \left( {{\varphi }_{ * }X}\right) \left( \widetilde{f}\right)  = \left( {Xf}\right)  \circ  {\varphi }^{-1} \) . Thus

\[
{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}\left( {fY}\right)  = {\left( {\varphi }^{-1}\right) }_{ * }\left( {{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {\widetilde{f}{\varphi }_{ * }Y}\right) }\right)
\]

\[
= {\left( {\varphi }^{-1}\right) }_{ * }\left( {\widetilde{f}{\widetilde{\nabla }}_{{\varphi }_{ * }X}\left( {{\varphi }_{ * }Y}\right)  + \left( {{\varphi }_{ * }X}\right) \left( \widetilde{f}\right) {\varphi }_{ * }Y}\right)
\]

\[
= f{\left( {\varphi }^{ * }\widetilde{\nabla }\right) }_{X}Y + \left( {Xf}\right) Y.
\]

The next proposition shows that various important concepts defined in terms of connections—covariant derivatives along curves, parallel transport, and geodesics— all behave as expected with respect to pullback connections.

Proposition 4.38 (Properties of Pullback Connections). Suppose \( M \) and \( \widetilde{M} \) are smooth manifolds with or without boundary, and \( \varphi  : M \rightarrow  \widetilde{M} \) is a diffeomorphism. Let \( \widetilde{\nabla } \) be a connection in \( T\widetilde{M} \) and let \( \nabla  = {\varphi }^{ * }\widetilde{\nabla } \) be the pullback connection in \( {TM} \) . Suppose \( \gamma  : I \rightarrow  M \) is a smooth curve.

(a) \( \varphi \) takes covariant derivatives along curves to covariant derivatives along curves: if \( V \) is a smooth vector field along \( \gamma \) , then

\[
{d\varphi } \circ  {D}_{t}V = {\widetilde{D}}_{t}\left( {{d\varphi } \circ  V}\right) ,
\]

where \( {D}_{t} \) is covariant differentiation along \( \gamma \) with respect to \( \nabla \) , and \( {\widetilde{D}}_{t} \) is covariant differentiation along \( \varphi  \circ  \gamma \) with respect to \( \widetilde{\nabla } \) .

(b) \( \varphi \) takes geodesics to geodesics: if \( \gamma \) is a \( \nabla \) -geodesic in \( M \) , then \( \varphi  \circ  \gamma \) is a \( \widetilde{\nabla } \) -geodesic in \( \widetilde{M} \) .

(c) \( \varphi \) takes parallel transport to parallel transport: for every \( {t}_{0},{t}_{1} \in  I \) ,

\[
d{\varphi }_{\gamma \left( {t}_{1}\right) } \circ  {P}_{{t}_{0}{t}_{1}}^{\gamma } = {P}_{{t}_{0}{t}_{1}}^{\varphi  \circ  \gamma } \circ  d{\varphi }_{\gamma \left( {t}_{0}\right) }.
\]

Proof. Problem 4-13.

## Problems

4-1. Let \( M \subseteq  {\mathbb{R}}^{n} \) be an embedded submanifold and \( Y \in  \mathfrak{X}\left( M\right) \) . For every point \( p \in  M \) and vector \( v \in  {T}_{p}M \) , define \( {\nabla }_{v}^{\top }Y \) by (4.4).

(a) Show that \( {\nabla }_{v}^{\top }Y \) does not depend on the choice of extension \( \widetilde{Y} \) of \( Y \) . [Hint: Use Prop. A.28.]

(b) Show that \( {\nabla }_{v}^{\top }Y \) is invariant under rigid motions of \( {\mathbb{R}}^{n} \) , in the following sense: if \( F \in  \mathrm{E}\left( n\right) \) and \( \widetilde{M} = F\left( M\right) \) , then \( d{F}_{p}\left( {{\nabla }_{v}^{\top }Y}\right)  = {\nabla }_{d{F}_{p}\left( v\right) }^{\top }\left( {{F}_{ * }Y}\right) \) .

(Used on pp. 87, 93.)

4-2. In your study of smooth manifolds, you have already seen another way of taking "directional derivatives of vector fields," the Lie derivative \( {\mathcal{L}}_{X}Y \) (which is equal to the Lie bracket \( \left\lbrack  {X, Y}\right\rbrack \) ; see Prop. A.46). Suppose \( M \) is a smooth manifold of positive dimension.

(a) Show that the map \( \mathcal{L} : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) is not a connection.

(b) Show that there are smooth vector fields \( X \) and \( Y \) on \( {\mathbb{R}}^{2} \) such that \( X = Y = {\partial }_{1} \) along the \( {x}^{1} \) -axis, but the Lie derivatives \( {\mathcal{L}}_{X}\left( {\partial }_{2}\right) \) and \( {\mathcal{L}}_{Y}\left( {\partial }_{2}\right) \) are not equal on the \( {x}^{1} \) -axis.

4-3. Prove Proposition 4.7 (the transformation law for the connection coefficients).

4-4. Prove Theorem 4.14 (characterizing the space of connections).

4-5. Prove Proposition 4.16 (local formulas for covariant derivatives of tensor fields).

4-6. Let \( M \) be a smooth manifold and let \( \nabla \) be a connection in \( {TM} \) . Define a map \( \tau  : \mathfrak{X}\left( M\right)  \times  \mathfrak{X}\left( M\right)  \rightarrow  \mathfrak{X}\left( M\right) \) by

\[
\tau \left( {X, Y}\right)  = {\nabla }_{X}Y - {\nabla }_{Y}X - \left\lbrack  {X, Y}\right\rbrack  .
\]

(a) Show that \( \tau \) is a \( \left( {1,2}\right) \) -tensor field, called the torsion tensor of \( \nabla \) .

(b) We say that \( \nabla \) is symmetric if its torsion vanishes identically. Show that \( \nabla \) is symmetric if and only if its connection coefficients with respect to every coordinate frame are symmetric: \( {\Gamma }_{ij}^{k} = {\Gamma }_{ji}^{k} \) . [Warning: They might not be symmetric with respect to other frames.]

(c) Show that \( \nabla \) is symmetric if and only if the covariant Hessian \( {\nabla }^{2}u \) of every smooth function \( u \in  {C}^{\infty }\left( M\right) \) is a symmetric 2-tensor field. (See Example 4.22.)

(d) Show that the Euclidean connection \( \overline{\nabla } \) on \( {\mathbb{R}}^{n} \) is symmetric.

(Used on pp. 113, 121, 123.)

4-7. Let \( \gamma  : \left( {-\pi ,\pi }\right)  \rightarrow  {\mathbb{R}}^{2} \) be the figure eight curve defined in Example 4.23. Prove that \( \gamma \) is an injective smooth immersion, but its velocity vector field is not extendible.

4-8. Suppose \( M \) is a smooth manifold (without boundary), \( I \subseteq  \mathbb{R} \) is an interval (bounded or not, with or without endpoints), and \( \gamma  : I \rightarrow  M \) is a smooth curve.

(a) Show that for every \( {t}_{0} \in  I \) such that \( {\gamma }^{\prime }\left( {t}_{0}\right)  \neq  0 \) , there is a connected neighborhood \( J \) of \( {t}_{0} \) in \( I \) such that every smooth vector field along \( {\left. \gamma \right| }_{J} \) is extendible.

(b) Show that if \( I \) is an open interval or a compact interval and \( \gamma \) is a smooth embedding, then every smooth vector field along \( \gamma \) is extendible.

4-9. Let \( M \) be a smooth manifold, and let \( {\nabla }^{0} \) and \( {\nabla }^{1} \) be two connections on \( {TM} \) .

(a) Show that \( {\nabla }^{0} \) and \( {\nabla }^{1} \) have the same torsion (Problem 4-6) if and only if their difference tensor is symmetric, i.e., \( D\left( {X, Y}\right)  = D\left( {Y, X}\right) \) for all \( X \) and \( Y \) .

(b) Show that \( {\nabla }^{0} \) and \( {\nabla }^{1} \) determine the same geodesics if and only if their difference tensor is antisymmetric, i.e., \( D\left( {X, Y}\right)  =  - D\left( {Y, X}\right) \) for all \( X \) and \( Y \) .

(Used on p. 145.)

4-10. Suppose \( M \) is a smooth manifold endowed with a connection, \( \gamma  : I \rightarrow  M \) is a smooth curve, and \( Y \in  \mathcal{X}\left( \gamma \right) \) . Prove that if \( Y \) is parallel along \( \gamma \) , then it is parallel along every reparametrization of \( \gamma \) .

4-11. Suppose \( G \) is a Lie group.

(a) Show that there is a unique connection \( \nabla \) in \( {TG} \) with the property that every left-invariant vector field is parallel.

(b) Show that the torsion tensor of \( \nabla \) (Problem 4-6) is zero if and only if \( G \) is abelian.

4-12. Prove Proposition 4.36 (a vector or tensor field \( A \) is parallel if and only if \( \left. {\nabla A \equiv  0}\right) \) .

4-13. Prove Proposition 4.38 (properties of pullback connections).

4-14. Let \( M \) be a smooth \( n \) -manifold and \( \nabla \) a connection in \( {TM} \) , let \( \left( {E}_{i}\right) \) be a local frame on some open subset \( U \subseteq  M \) , and let \( \left( {\varepsilon }^{i}\right) \) be the dual coframe.

(a) Show that there is a uniquely determined \( n \times  n \) matrix of smooth 1- forms \( \left( {{\omega }_{i}{}^{j}}\right) \) on \( U \) , called the connection 1-forms for this frame, such that

\[
{\nabla }_{X}{E}_{i} = {\omega }_{i}^{j}\left( X\right) {E}_{j}
\]

for all \( X \in  \mathcal{X}\left( U\right) \) .

(b) CARTAN'S FIRST STRUCTURE EQUATION: Prove that these forms satisfy the following equation, due to Élie Cartan:

\[
d{\varepsilon }^{j} = {\varepsilon }^{i} \land  {\omega }_{i}{}^{j} + {\tau }^{j},
\]

where \( {\tau }^{1},\ldots ,{\tau }^{n} \in  {\Omega }^{2}\left( M\right) \) are the torsion 2-forms, defined in terms of the torsion tensor \( \tau \) (Problem 4-6) and the frame \( \left( {E}_{i}\right) \) by

\[
\tau \left( {X, Y}\right)  = {\tau }^{j}\left( {X, Y}\right) {E}_{j}.
\]

(Used on pp. 145, 222.)
