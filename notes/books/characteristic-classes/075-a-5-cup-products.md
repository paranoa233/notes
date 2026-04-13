# A.5 Cup Products

Given cochains \( c \in  {C}^{m}X \) and \( {c}^{\prime } \in  {C}^{n}X \) , the product \( {}^{3}c{c}^{\prime } = c \smile  {c}^{\prime } \in  {C}^{m + n}X \) is defined as follows. Let \( \sigma  : {\Delta }^{m + n} \rightarrow  X \) be a singular simplex. By the front \( m \) -face of \( \sigma \) is meant the composition \( \sigma  \circ  {\alpha }_{m} : {\Delta }^{m} \rightarrow  X \) where

\[
{a}_{m}\left( {{t}_{0},\cdots ,{t}_{m}}\right)  = \left( {{t}_{0},\cdots ,{t}_{m},0,\cdots 0}\right) .
\]

Similarly the back \( n \) -face of \( \sigma \) is the composition \( \sigma  \circ  {\beta }_{n} \) where

\[
{\beta }_{n}\left( {{t}_{m},{t}_{m + 1},\cdots {t}_{m + n}}\right)  = \left( {0,\cdots 0,{t}_{m},{t}_{m + 1},\cdots {t}_{m + n}}\right) .
\]

Now define \( c{c}^{\prime } = c \smile  {c}^{\prime } \) by the identity

\[
\left\langle  {c{c}^{\prime },\left\lbrack  \sigma \right\rbrack  }\right\rangle   = {\left( -1\right) }^{mn}\left\langle  {c,\left\lbrack  {\sigma  \circ  {a}_{m}}\right\rbrack  }\right\rangle   \cdot  \left\langle  {{c}^{\prime },\left\lbrack  {\sigma  \circ  {\beta }_{n}}\right\rbrack  }\right\rangle   \in  \Lambda .
\]

The product operation is bilinear and associative, but is not commutative. The constant cocycle \( 1 \in  {C}^{0}X \) serves as identity element. The formula

\[
\delta \left( {c{c}^{\prime }}\right)  = \left( {\delta c}\right) {c}^{\prime } + {\left( -1\right) }^{m}c\left( {\delta {c}^{\prime }}\right)
\]

is easily verified. This implies that there is a corresponding product operation \( {\mathrm{H}}^{m}X \otimes  {\mathrm{H}}^{n}X \rightarrow  {\mathrm{H}}^{m + n}X \) of cohomology classes. On the cohomology level the product operation does commute, up to sign. (See for example [Spa81, p. 252].) In fact, for \( a \in  {\mathrm{H}}^{m}X, b \in  {\mathrm{H}}^{n}X \) , one has \( {ba} = {\left( -1\right) }^{mn}{ab} \) . In dealing with graded groups, this property is called commutativity. Thus we say briefly that the cohomology \( {\mathrm{H}}^{ * }X = \left( {{\mathrm{H}}^{0}X,{\mathrm{H}}^{1}X,{\mathrm{H}}^{2}X,\cdots }\right) \) is commutative as a graded ring.

Now suppose that one is given a pair of spaces \( X \supset  A \) . If the cochain \( c \) belongs to the subset \( {C}^{m}\left( {X, A}\right)  \subset  {C}^{m}X \) (that is if \( c\left\lbrack  \sigma \right\rbrack   = 0 \) for every \( \sigma  : {\Delta }^{m} \rightarrow  A \subset  X \) ) and if \( {c}^{\prime } \in  {C}^{n}X \) , then clearly \( c{c}^{\prime } \) belongs to \( {C}^{m + n}\left( {X, A}\right) \) . This gives rise to a product operation

\[
{\mathrm{H}}^{m}\left( {X, A}\right)  \otimes  {\mathrm{H}}^{n}X \rightarrow  {\mathrm{H}}^{m + n}\left( {X, A}\right) .
\]

---

\( {}^{3} \) Editor’s note: In this text, this is what we will always mean by the cup product.

---

More generally consider two subsets \( A, B \subset  X \) which satisfy the following:

Hypothesis. Both \( A \) and \( B \) are relatively open when considered as subsets of \( A \cup  B \) .

Then one can define a product operation

\[
{\mathrm{H}}^{m}\left( {X, A}\right)  \otimes  {\mathrm{H}}^{n}\left( {X, B}\right)  \rightarrow  {\mathrm{H}}^{m + n}\left( {X, A \cup  B}\right)
\]

as follows. \( {}^{4} \) Let

\[
{\widehat{C}}^{i}\left( {X;A, B}\right)  \subset  {C}^{i}X
\]

denote the intersection of the submodules \( {C}^{i}\left( {X, A}\right) \) and \( {C}^{i}\left( {X, B}\right) \) of \( {C}^{i}X \) . Given cochains \( c \in  {C}^{m}\left( {X, A}\right) \) and \( {c}^{\prime } \in  {C}^{n}\left( {X, B}\right) \) , the product \( c{c}^{\prime } \) clearly belongs to the intersection

\[
{\widehat{C}}^{m + n}\left( {X;A, B}\right)  = {C}^{m + n}\left( {X, A}\right)  \cap  {C}^{m + n}\left( {X, B}\right) .
\]

Evidently there is a short exact sequence of cochain complexs

\[
0 \rightarrow  {C}^{ * }\left( {X, A \cup  B}\right)  \rightarrow  {\widehat{C}}^{ * }\left( {X;A, B}\right)  \rightarrow  {\widehat{C}}^{ * }\left( {A \cup  B;A, B}\right)  \rightarrow  0,
\]

But the right hand cochain complex is acyclic5, by [ES52, p. 197] or [Spa81, p. 252]. Hence the inclusion

\[
{C}^{ * }\left( {X, A \cup  B}\right)  \rightarrow  {\widehat{C}}^{ * }\left( {X;A, B}\right)
\]

induces isomorphisms of cohomology groups. Therefore one obtains a cup product operation with values in the required cohomology group \( {\mathrm{H}}^{m + n}\left( {X, A \cup  B}\right) \) .

---

\( {}^{4} \) The difficulty here is caused by the fact that

\[
{C}^{i}\left( {X, A}\right)  \cap  {C}^{i}\left( {X, B}\right)  \neq  {C}^{i}\left( {X, A \cup  B}\right)
\]

since a singular simplex in \( X \) may lie in \( A \cup  B \) without lying either in \( A \) or \( B \) .

\( {}^{5} \) Editor’s note: By acyclic we mean that the corresponding cohomology groups are 0.

---
