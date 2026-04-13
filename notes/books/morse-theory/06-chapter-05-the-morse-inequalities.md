# Chapter 5 The Morse Inequalities

Based on lecture notes by

M. Spivak and R. Wells

In Morse's original treatment of this subject, Theorem 3.3 was not available. The relationship between the topology of \( M \) and the critical points of a real valued function on \( M \) were described instead in terms of a collection of inequalities. This section will describe this original point of view.

Definition 5.1. Let \( S \) be a function from certain pairs of spaces to the integers. \( S \) is subadditive if whenever \( X \supset  Y \supset  Z \) we have \( S\left( {X, Z}\right)  \leq  S\left( {X, Y}\right)  + S\left( {Y, Z}\right) \) . If equality holds, \( S \) is called additive.

As an example, given any field \( \mathbb{F} \) as coefficient group, let

\[
{R}_{\lambda }\left( {X, Y}\right)  = \lambda \text{ th Betti number of }\left( {X, Y}\right)
\]

\[
= \text{ rank over }\mathbb{F}\text{ of }{\mathrm{H}}_{\lambda }\left( {X, Y;\mathbb{F}}\right) \text{ , }
\]

for any pair \( \left( {X, Y}\right) \) such that this rank is finite. \( {R}_{\lambda } \) is subadditive, as is easily seen by examining the following portion of the exact sequence for \( \left( {X, Y, Z}\right) \) :

\[
\cdots  \rightarrow  {\mathrm{H}}_{\lambda }\left( {Y, Z}\right)  \rightarrow  {\mathrm{H}}_{\lambda }\left( {X, Z}\right)  \rightarrow  {\mathrm{H}}_{\lambda }\left( {X, Y}\right)  \rightarrow  \cdots
\]

The Euler characteristic \( \chi \left( {X, Y}\right) \) is additive, where \( \chi \left( {X, Y}\right)  = \sum {\left( -1\right) }^{\lambda }{R}_{\lambda }\left( {X, Y}\right) \) .

Lemma 5.2. Let \( S \) be subadditive and let \( {X}_{0} \subset  \cdots  \subset  {X}_{n} \) . Then \( S\left( {{X}_{n},{X}_{0}}\right)  \leq \; \mathop{\sum }\limits_{{i = 1}}^{n}S\left( {{X}_{i},{X}_{i - 1}}\right) \) . If \( S \) is additive then equality holds.

Proof. Induction on \( n \) . For \( n = 1 \) , equality holds trivially and the case \( n = 2 \) is the definition of (sub) additivity.

If the result is true for \( n - 1 \) , then \( S\left( {{X}_{n - 1},{X}_{0}}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}S\left( {{X}_{i},{X}_{i - 1}}\right) \) . Therefore \( S\left( {{X}_{n},{X}_{0}}\right)  \leq  S\left( {{X}_{n - 1},{X}_{0}}\right)  + S\left( {{X}_{n},{X}_{n - 1}}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}S\left( {{X}_{i},{X}_{i - 1}}\right) \) and the result is true for \( n \) .

Let \( S\left( {X,\varnothing }\right)  = S\left( X\right) \) . Taking \( {X}_{0} = \varnothing \) in Lemma 5.2, we have

\[
S\left( {X}_{n}\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}S\left( {{X}_{i},{X}_{i - 1}}\right) \tag{5.1}
\]

with equality if \( S \) is additive.

Let \( M \) be a compact manifold and \( f \) a differentiable function on \( M \) with isolated, non-degenerate, critical points. Let \( {a}_{1} < \cdots  < {a}_{k} \) be such that \( {M}^{{a}_{i}} \) contains exactly \( i \) critical points, and \( {M}^{{a}_{k}} = M \) . Then

\[
{\mathrm{H}}_{ * }\left( {{M}^{{a}_{i}},{M}^{{a}_{i - 1}}}\right)  = {\mathrm{H}}_{ * }\left( {{M}^{{a}_{i - 1}} \cup  {\mathrm{e}}^{{\lambda }_{i}},{M}^{{a}_{i - 1}}}\right)
\]

\[
= {\mathrm{H}}_{ * }\left( {{\mathrm{e}}^{{\lambda }_{i}},{\dot{\mathrm{e}}}^{{\lambda }_{i}}}\right) \;\text{ by excision, }
\]

\[
= \left\{  \begin{array}{ll} \text{ coefficient group in dimension } & {\lambda }_{i} \\  0 & \text{ otherwise. } \end{array}\right.
\]

where \( {\lambda }_{i} \) is the index of the critical point.

Applying Equation (5.1) to \( \varnothing  = {M}^{{a}_{0}} \subset  \cdots  \subset  {M}^{{a}_{k}} = M \) with \( S = {R}_{\lambda } \) we have

\[
{R}_{\lambda }\left( M\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{n}{R}_{\lambda }\left( {{M}^{{a}_{i}},{M}^{{a}_{i - 1}}}\right)  = {C}_{\lambda }
\]

where \( {C}_{\lambda } \) denotes the number of critical points of index \( \lambda \) . Applying this formula to the case \( S = \chi \) we have

\[
\chi \left( M\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\chi \left( {{M}^{{a}_{i}},{M}^{{a}_{i - 1}}}\right)  = {C}_{0} - {C}_{1} + {C}_{2} -  + \cdots  \pm  {C}_{n}.
\]

Thus we have proven:

Theorem 5.3 (Weak Morse Inequalities). If \( {C}_{\lambda } \) denotes the number of critical points of index \( \lambda \) on the compact manifold \( M \) then

\[
{R}_{\lambda }\left( M\right)  \leq  {C}_{\lambda },\;\text{ and } \tag{5.2}
\]

\[
\sum {\left( -1\right) }^{\lambda }{R}_{\lambda }\left( M\right)  = \sum {\left( -1\right) }^{\lambda }{C}_{\lambda } \tag{5.3}
\]

Slightly sharper inequalities can be proven by the following argument.

Lemma 5.4. The function \( {S}_{\lambda } \) is subadditive, where

\[
{S}_{\lambda }\left( {X, Y}\right)  = {R}_{\lambda }\left( {X, Y}\right)  - {R}_{\lambda  - 1}\left( {X, Y}\right)  + {R}_{\lambda  - 2}\left( {X, Y}\right)  -  + \cdots  \pm  {R}_{0}\left( {X, Y}\right) .
\]

Proof. Given an exact sequence

\[
\overset{h}{ \rightarrow  }A\overset{i}{ \rightarrow  }B\overset{j}{ \rightarrow  }C\overset{k}{ \rightarrow  }\cdots \ldots  \rightarrow  D \rightarrow  0
\]

of vector spaces note that the rank of the homomorphism \( h \) plus the rank of \( i \) is equal to the rank of \( A \) . Therefore,

\[
\text{ Rank }h = \operatorname{Rank}A - \operatorname{Rank}i
\]

\[
= \operatorname{Rank}A - \operatorname{Rank}B + \operatorname{Rank}j
\]

\[
= \operatorname{Rank}A - \operatorname{Rank}B + \operatorname{Rank}C - \operatorname{Rank}K
\]

\[
\vdots
\]

\[
= \operatorname{Rank}A - \operatorname{Rank}B + \operatorname{Rank}C -  + \cdots  \pm  \operatorname{Rank}D.
\]

Hence the last expression is \( \geq  0 \) . Now consider the homology exact sequence of a triple \( X \supset  Y \supset  Z \) . Applying this computation to the homomorphism

\[
{\mathrm{H}}_{\lambda  + 1}\left( {X, Y}\right) \overset{\partial }{ \rightarrow  }{\mathrm{H}}_{\lambda }\left( {Y, Z}\right)
\]

we see that

\[
\operatorname{Rank}\partial  = {R}_{\lambda }\left( {Y, Z}\right)  - {R}_{\lambda }\left( {X, Z}\right)  + {R}_{\lambda }\left( {X, Y}\right)  - {R}_{\lambda  - 1}\left( {Y, Z}\right)  + \cdots  \geq  0
\]

Collecting terms, this means that

\[
{S}_{\lambda }\left( {Y, Z}\right)  - {S}_{\lambda }\left( {X, Z}\right)  + {S}_{\lambda }\left( {X, Y}\right)  \geq  0,
\]

which completes the proof.

Applying this subadditive function \( {S}_{\lambda } \) , to the spaces

\[
\varnothing  \subset  {M}^{{a}_{1}} \subset  {M}^{{a}_{2}} \subset  \cdots  \subset  {M}^{{a}_{k}}
\]

we obtain the Morse inequalities:

\[
{S}_{\lambda }\left( M\right)  \leq  \mathop{\sum }\limits_{{i = 1}}^{k}{S}_{\lambda }\left( {{M}^{{a}_{i}},{M}^{{a}_{i - 1}}}\right)  = {C}_{\lambda } - {C}_{\lambda  - 1} +  - \cdots  \pm  {C}_{0}
\]

or

\[
{R}_{\lambda }\left( M\right)  - {R}_{\lambda  - 1}\left( M\right)  +  - \cdots  \pm  {R}_{0}\left( M\right)  \leq  {C}_{\lambda } - {C}_{\lambda  - 1} +  - \cdots  \pm  {C}_{0}.
\]

\( \left( {4}_{\lambda }\right) \)

These inequalities are definitely sharper than the previous ones. In fact, adding \( \left( {4}_{\lambda }\right) \) and \( \left( {4}_{\lambda  - 1}\right) \) , one obtains \( \left( {2}_{\lambda }\right) \) ; and comparing \( \left( {4}_{\lambda }\right) \) with \( \left( {4}_{\lambda  - 1}\right) \) for \( \lambda  > n \) one obtains the equality (5.3).

As an illustration of the use of the Morse inequalities, suppose that \( {C}_{\lambda  + 1} = 0 \) . Then \( {R}_{\lambda  + 1} \) must also be zero. Comparing the inequalities \( \left( {4}_{\lambda }\right) \) and \( \left( {4}_{\lambda  + 1}\right) \) , we see that

\[
{R}_{\lambda } - {R}_{\lambda  - 1} +  - \cdots  \pm  {R}_{0} = {C}_{\lambda } - {C}_{\lambda  - 1} +  - \cdots  \pm  {C}_{0}.
\]

Now suppose that \( {C}_{\lambda  - 1} \) is also zero. Then \( {R}_{\lambda  - 1} = 0 \) , and a similar argument shows that

\[
{R}_{\lambda  - 2} - {R}_{\lambda  - 3} +  - \cdots  \pm  {R}_{0} = {C}_{\lambda  - 2} - {C}_{\lambda  - 3} +  - \cdots  \pm  {C}_{0}.
\]

Subtracting this from the equality above we obtain the following:

Corollary 5.5. If \( {C}_{\lambda  + 1} = {C}_{\lambda  - 1} = 0 \) then \( {R}_{\lambda } = {C}_{\lambda } \) and \( {R}_{\lambda  + 1} = {R}_{\lambda  - 1} = 0 \) .

(Of course this would also follow from Theorem 3.3.) Note that this corollary enables us to find the homology groups of complex projective space (see chapter 4) without making use of Theorem 3.3.
