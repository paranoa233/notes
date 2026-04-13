# Chapter 11 The Path Space of a Smooth Manifold

## Part III. The Calculus of Variations Applied to Geodesics

Based on lecture notes by

M. Spivak and R. Wells

Let \( M \) be a smooth manifold and let \( p \) and \( q \) be two (not necessarily distinct) points of \( M \) . By a piecewise smooth path from \( p \) to \( q \) will be meant a map \( \omega  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  M \) such that

(1) there exists a subdivision \( 0 = {t}_{0} < {t}_{1} < \cdots  < {t}_{k} = 1 \) of \( \left\lbrack  {0,1}\right\rbrack \) so that each \( {\left. \omega \right| }_{\left\lbrack  {t}_{{i}_{1}},{t}_{i}\right\rbrack  } \) is differentiable of class \( {C}^{\infty } \) ;

(2) \( \omega \left( 0\right)  = p \) and \( \omega \left( 1\right)  = q \) .

The set of all piecewise smooth paths from \( p \) to \( q \) in \( M \) will be denoted by \( \Omega \left( {M;p, q}\right) \) , or briefly by \( \Omega \left( M\right) \) or \( \Omega \) .

Later (in Chapter 16) \( \Omega \) will be given the structure of a topological space, but for the moment this will not be necessary. We will think of \( \Omega \) as being something like an "infinite dimensional manifold." To start the analogy we make the following definition.

By the tangent space of \( \Omega \) at a path \( \omega \) will be meant the vector space consisting of all piecewise smooth vector fields \( W \) along \( \omega \) for which \( W\left( 0\right)  = 0 \) and \( W\left( 1\right)  = 0 \) . The notation \( T{\Omega }_{\omega } \) will be used for this vector space.

If \( F \) is a real valued function on \( \Omega \) it is natural to ask what

\[
{F}_{ * } : T{\Omega }_{\omega } \rightarrow  T{\mathbf{R}}_{F\left( \omega \right) }
\]

the induced map on the tangent space, should mean. When \( F \) is a function which is smooth in the usual sense, on a smooth manifold \( M \) , we can define \( {F}_{ * } : T{M}_{p} \rightarrow \; T{\mathbf{R}}_{F\left( p\right) } \) as follows. Given \( X \in  T{M}_{p} \) choose a smooth path \( u \mapsto  \alpha \left( u\right) \) in \( M \) , which is defined for \( - \varepsilon  < u < \varepsilon \) , so that

\[
\alpha \left( 0\right)  = p,\;\frac{\mathrm{d}\alpha }{\mathrm{d}u}\left( 0\right)  = X.
\]

Then \( {F}_{ * }\left( X\right) \) is equal to \( \mathrm{d}\left( {F\left( {\alpha \left( u\right) }\right) /{\left. \mathrm{d}u\right| }_{u = 0} = o}\right. \) , multiplied by the basis vector \( {\left( \mathrm{d}/\mathrm{d}t\right) }_{F\left( p\right) } \in  T{\mathbf{R}}_{F\left( p\right) }. \)

In order to carry out an analogous construction for \( F : \Omega  \rightarrow  \mathbf{R} \) , the following concept is needed.

Definition 11.1. A variation of \( \omega \) (keeping endpoints fixed) is a function

\[
\overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega ,
\]

for some \( \varepsilon  > 0 \) , such that

(1) \( \overline{\alpha }\left( 0\right)  = \omega \) ;

(2) there is a subdivision \( 0 = {t}_{0} < {t}_{1} < \cdots  < {t}_{k} = 1 \) of \( \left\lbrack  {0,1}\right\rbrack \) so that the map

\[
\alpha  : \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {0,1}\right\rbrack   \rightarrow  M
\]

defined by \( \alpha \left( {u, t}\right)  = \overline{\alpha }\left( u\right) \left( t\right) \) is \( {C}^{\infty } \) on each strip \( \left( {-\varepsilon ,\varepsilon }\right)  \times  \left\lbrack  {{t}_{i - 1},{t}_{i}}\right\rbrack  , i = \; 1,\ldots , k \) .

Since each \( \overline{\alpha }\left( u\right) \) belongs to \( \Omega  = \Omega \left( {M;p, q}\right) \) , note that:

(3) \( \alpha \left( {u,0}\right)  = p,\alpha \left( {u,1}\right)  = q \) for all \( u \in  \left( {-\varepsilon ,\varepsilon }\right) \) .

We will use either \( \alpha \) or \( \overline{\alpha } \) to refer to the variation. More generally if, in the above definition, \( \left( {-\varepsilon ,\varepsilon }\right) \) is replaced by a neighborhood \( U \) of 0 in \( {\mathbf{R}}^{n} \) , then \( \alpha \) (or \( \overline{\alpha } \) ) is called an \( n \) -parameter variation of \( \omega \) .

Now \( \overline{\alpha } \) may be considered as a "smooth path" in \( \Omega \) . Its "velocity vector" \( \mathrm{d}\overline{\alpha }/\mathrm{d}u\left( 0\right)  \in  T{\Omega }_{\omega } \) is defined to be the vector field \( W \) along \( \omega \) given by

\[
{W}_{t} = \frac{\mathrm{d}\overline{\alpha }}{\mathrm{d}u}{\left( 0\right) }_{t} = \frac{\partial \alpha }{\partial u}\left( {0, t}\right) .
\]

Clearly \( W \in  T{\Omega }_{\omega } \) . This vector field \( W \) is also called the variation vector field associated with the variation \( \alpha \) .

Given any \( W \in  T{\Omega }_{\omega } \) note that there exists a variation \( \overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega \) which satisfies the conditions \( \overline{\alpha }\left( 0\right)  = \omega ,\mathrm{d}\overline{\alpha }/\mathrm{d}u\left( 0\right)  = W \) . In fact one can set

\[
\overline{\alpha }\left( t\right)  = {\exp }_{\omega \left( t\right) }\left( {u{W}_{t}}\right) .
\]

By analogy with the definition given above, if \( F \) is a real valued function on \( \Omega \) , we attempt to define

\[
{F}_{ * } : T{\Omega }_{\omega } \rightarrow  T{\mathbf{R}}_{F\left( \omega \right) }
\]

as follows. Given \( W \in  T{\Omega }_{\omega } \) choose a variation \( \overline{\alpha } : \left( {-\varepsilon ,\varepsilon }\right)  \rightarrow  \Omega \) with

\[
\overline{\alpha }\left( 0\right)  = \omega ,\;\frac{\mathrm{d}\overline{\alpha }}{\mathrm{d}u}\left( 0\right)  = W
\]

and set \( {F}_{ * }\left( W\right) \) equal to \( \mathrm{d}\left( {F\left( {\overline{\alpha }\left( u\right) }\right) }\right) /{\left. \mathrm{d}u\right| }_{u = 0} \) multiplied by the tangent vector \( {\left( \mathrm{d}/\mathrm{d}t\right) }_{F\left( \omega \right) } \) . Of course without hypothesis on \( F \) there is no guarantee that this derivative will exist, or will be independent of the choice of \( \overline{\alpha } \) . We will not investigate what conditions \( F \) must satisfy in order for \( {F}_{ * } \) to have these properties. We have indicated how \( {F}_{ * } \) might be defined only to motivate the following.

Definition 11.2. A path \( \omega \) is a critical path for a function \( F : \Omega  \rightarrow  \mathbf{R} \) if and only if \( \mathrm{d}\left( {F\left( {\overline{\alpha }\left( u\right) }\right) }\right) /{\left. \mathrm{d}u\right| }_{u = 0} \) is zero for every variation \( \overline{\alpha } \) of \( \omega \) .

Example 11.3. If \( F \) takes on its minimum at a path \( {\omega }_{0} \) , and if the derivatives \( \mathrm{d}\left( {F\left( {\overline{\alpha }\left( u\right) }\right) }\right) /\mathrm{d}u \) are all defined, then clearly \( {\omega }_{0} \) is a critical path.
