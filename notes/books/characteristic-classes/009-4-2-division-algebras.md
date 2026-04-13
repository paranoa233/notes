# 4.2 Division Algebras

Closely related is the question of the existence of real division algebras.

Theorem 4.7 (Stiefel). Suppose that there exists a bilinear product operation \( {}^{1} \)

\[
p : {\mathbb{R}}^{n} \times  {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n}
\]

without zero divisors. Then the projective space \( {\mathbb{P}}^{n - 1} \) is parallelizable, hence \( n \) must be a power of 2 .

In fact such division algebras are known to exist for \( n = 1,2,4,8 \) : namely the real numbers, the complex numbers, the quaternions, and the Cayley numbers. It follows that the projective spaces \( {\mathbb{P}}^{1},{\mathbb{P}}^{3} \) and \( {\mathbb{P}}^{7} \) are parallelizable. That no such division algebra exists for \( n > 8 \) follows from the references cited above on parallelizability.

Proof of 4.7. Let \( {b}_{1},\ldots ,{b}_{n} \) be the standard basis for the vector space \( {\mathbb{R}}^{n} \) . Note that the correspondence \( y \mapsto  p\left( {y,{b}_{1}}\right) \) defines an isomorphism of \( {\mathbb{R}}^{n} \) onto itself.

---

\( {}^{1} \) This product operation is not required to be associative, or to have an identity element.

---

Hence the formula

\[
{v}_{i}\left( {p\left( {y,{b}_{1}}\right) }\right)  = p\left( {y,{b}_{i}}\right)
\]

defines a linear transformation

\[
{v}_{i} : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}^{n}
\]

Note that \( {v}_{1}\left( x\right) ,\ldots ,{v}_{n}\left( x\right) \) are linearly independent for \( x \neq  0 \) , and that \( {v}_{1}\left( x\right)  = x \) .

The functions \( {v}_{2},\ldots ,{v}_{n} \) give rise to \( n - 1 \) linearly independent cross-sections of the vector bundle

\[
{\tau }_{{\mathbb{P}}^{n - 1}} \cong  \operatorname{Hom}\left( {{\gamma }_{n - 1}^{1},{\gamma }^{ \bot  }}\right) .
\]

In fact for each line \( L \) through the origin, a linear transformation

\[
{\bar{v}}_{i} : L \rightarrow  {L}^{ \bot  }
\]

is defined as follows. For \( x \in  L \) , let \( {\bar{v}}_{i}\left( x\right) \) denote the image of \( {v}_{i}\left( x\right) \) under the orthogonal projection

\[
{\mathbb{R}}^{n} \rightarrow  {L}^{ \bot  }\text{ . }
\]

Clearly \( {\bar{v}}_{1} = 0 \) , but \( {\bar{v}}_{2},\ldots ,{\bar{v}}_{n} \) are everywhere linearly independent. Thus the tangent bundle \( {\tau }_{{\mathbb{P}}^{n - 1}} \) is a trivial bundle. This completes the proof of 4.7.
