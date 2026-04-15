#### 2.1. Generalities

*Français : 2.1. Généralités*

DéFINITION 1. Soit \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) une suite à valeurs dans un espace vectoriel \( E \) . On appelle série de terme général \( {u}_{n} \) la suite \( {\left( {S}_{n}\right) }_{n \in \mathbb{N}} \) définie par

> DEFINITION 1. Let \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence with values in a vector space \( E \) . The series with general term \( {u}_{n} \) is the sequence \( {\left( {S}_{n}\right) }_{n \in \mathbb{N}} \) defined by

\[
\forall n \in  \mathbb{N},\;{S}_{n} = {u}_{0} + {u}_{1} + \cdots  + {u}_{n}.
\]

On note cette série \( \sum {u}_{n} \) . Pour tout \( n \in \mathbb{N},{u}_{n} \) s’appelle le terme d’indice \( n,{S}_{n} \) s’appelle la somme partielle d’indice \( n \) , de la série \( \sum {u}_{n} \) .

> We denote this series by \( \sum {u}_{n} \) . For any \( n \in \mathbb{N},{u}_{n} \) , \( n,{S}_{n} \) is called the term of index \( n,{S}_{n} \) and \( n \) is called the partial sum of index \( n \) of the series \( \sum {u}_{n} \) .

Lorsque \( E \) est un e.v.n, on dit que \( \sum {u}_{n} \) converges il a suite \( \left( {S}_{n}\right) \) converge. Dans ce cas, la limite s’appelle la somme de la série et on la note \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} \) . Pour tout \( n \in \mathbb{N} \) , on appelle alors reste d’indice \( n \) l’élément \( {R}_{n} \) défini par

> When \( E \) is a n.v.s., we say that \( \sum {u}_{n} \) converges if the sequence \( \left( {S}_{n}\right) \) converges. In this case, the limit is called the sum of the series and is denoted by \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{u}_{n} \) . For any \( n \in \mathbb{N} \) , the remainder of index \( n \) is the element \( {R}_{n} \) defined by

\[
{R}_{n} = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{u}_{k} - \mathop{\sum }\limits_{{k = 0}}^{n}{u}_{k} = \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{u}_{k}.
\]

Exemple 1. - Séries arithmétiques. Les séries de la forme \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{na} \) où \( a \) est une constante sont toujours divergentes dès que \( a \neq 0 \) . Les sommes partielles de cette séries peuvent s'exprimer de manière explicite grâce à la relation

> Example 1. - Arithmetic series. Series of the form \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{na} \) where \( a \) is a constant are always divergent as soon as \( a \neq 0 \) . The partial sums of these series can be expressed explicitly using the relation

\[
\forall n \in  \mathbb{N},\;\mathop{\sum }\limits_{{k = 0}}^{n}k = \frac{n\left( {n + 1}\right) }{2}.
\]

- Séries géométriques. Les séries \( \mathop{\sum }\limits_{{n \in  \mathbb{N}}}{q}^{n} \) où \( q \) est un nombre complexe, convergent si et seulement si \( \left| q\right|  < 1 \) . Lorsque \( q \neq  1 \) , les sommes partielles sont données par

> - Geometric series. The series \( \mathop{\sum }\limits_{{n \in  \mathbb{N}}}{q}^{n} \) where \( q \) is a complex number, converge if and only if \( \left| q\right|  < 1 \) . When \( q \neq  1 \) , the partial sums are given by

\[
\mathop{\sum }\limits_{{k = 0}}^{n}{q}^{k} = \frac{1 - {q}^{n + 1}}{1 - q}
\]

et si \( \left| q\right| < 1 \) , la somme et les restes de la série s’expriment explicitement :

> and if \( \left| q\right| < 1 \) , the sum and the remainders of the series are expressed explicitly:

\[
\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{q}^{k} = \frac{1}{1 - q}\;\text{ et }\;\forall n \in  \mathbb{N},\;\mathop{\sum }\limits_{{k = n}}^{\infty }{q}^{k} = \frac{{q}^{n}}{1 - q}.
\]

Critère de Cauchy pour les séries. Le critère de Cauchy pour les suites s'étend aisément pour les séries et donne le résultat suivant.

> Cauchy criterion for series. The Cauchy criterion for sequences extends easily to series and gives the following result.

Proposition 1. Une série \( \sum {u}_{n} \) à valeurs dans un espace de Banach converge si et seulement si

> Proposition 1. A series \( \sum {u}_{n} \) with values in a Banach space converges if and only if

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall n \geq  N,\forall p \in  \mathbb{N},\;\begin{Vmatrix}{{u}_{n} + \cdots  + {u}_{n + p}}\end{Vmatrix} < \varepsilon .
\]

COROLLAIRE 1. Si \( \sum {u}_{n} \) est une série convergente, alors \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{n} = 0 \) .

> COROLLARY 1. If \( \sum {u}_{n} \) is a convergent series, then \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{n} = 0 \) .

Remarque 1. La réciproque de ce corollaire est fausse ; par exemple, la série harmonique \( \sum 1/n \) diverge (voir la proposition 2).

> Remark 1. The converse of this corollary is false; for example, the harmonic series \( \sum 1/n \) diverges (see proposition 2).

Séries absolument convergentes. Voyons une autre conséquence importante du cri-tère de Cauchy pour les séries :

> Absolutely convergent series. Let us look at another important consequence of the Cauchy criterion for series:

THÉORÉME 1. Soit \( \sum {u}_{n} \) une série à valeurs dans un \( \mathbb{R} \) -espace de Banach. Si la série \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converge, on dit que \( \sum {u}_{n} \) est absolument convergente, et dans ce cas, la série \( \sum {u}_{n} \) est convergente.

> THEOREM 1. Let \( \sum {u}_{n} \) be a series with values in a Banach \( \mathbb{R} \)-space. If the series \( \sum \begin{Vmatrix}{u}_{n}\end{Vmatrix} \) converges, then \( \sum {u}_{n} \) is said to be absolutely convergent, and in this case, the series \( \sum {u}_{n} \) is convergent.

Ainsi, on est souvent ramené à prouver la convergence d'une série à termes positifs. Le but de la partie qui suit est de donner des conditions suffisantes pour assurer la convergence d'une série à termes positifs.

> Thus, we are often reduced to proving the convergence of a series with positive terms. The goal of the following section is to provide sufficient conditions to ensure the convergence of a series with positive terms.
