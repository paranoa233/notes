#### 5.1. Reminders

*Français : 5.1. Rappels*

On rappelle qu’un \( \mathbb{K} \) -espace vectoriel \( E \) (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ) est normé s’il est muni d’une norme \( \parallel .\parallel \) . En notant \( \mathrm{d}\left( {x, y}\right) = \parallel x - y\parallel \) , on fait de \( E \) un espace métrique. Sauf mention contraire, c'est toujours cette distance qui est utilisée dans un e.v.n. On dit qu'un e.v.n est un espace de Banach s'il est complet.

> Recall that a \( \mathbb{K} \)-vector space \( E \) (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \)) is normed if it is equipped with a norm \( \parallel .\parallel \). By noting \( \mathrm{d}\left( {x, y}\right) = \parallel x - y\parallel \), we make \( E \) a metric space. Unless otherwise stated, this is the distance always used in an n.v.s. An n.v.s is said to be a Banach space if it is complete.

Deux normes \( \parallel .{\parallel }_{1} \) et \( \parallel .{\parallel }_{2} \) sur \( E \) sont dite équivalentes si

> Two norms \( \parallel .{\parallel }_{1} \) and \( \parallel .{\parallel }_{2} \) on \( E \) are said to be equivalent if

\[
\exists a > 0,\exists b > 0,\forall x \in  E,\;a\parallel x{\parallel }_{1} \leq  \parallel x{\parallel }_{2} \leq  b\parallel x{\parallel }_{1}.
\]

Deux normes équivalentes définissent des distances équivalentes. Sur un plan topologique, et lorsque l'on travaille avec des suites de Cauchy, il est indifférent de prendre l'une ou l'autre de ces normes.

> Two equivalent norms define equivalent distances. Topologically, and when working with Cauchy sequences, it is indifferent to use one or the other of these norms.

L’application \( x \mapsto \left| x\right| \) est une norme sur \( \mathbb{R} \) , et \( z \mapsto \left| z\right| \) une norme sur \( \mathbb{C} \) . Plus généralement, pour tout \( \alpha \geq 1 \) , si \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{K}}^{n} \) (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ),

> The map \( x \mapsto \left| x\right| \) is a norm on \( \mathbb{R} \), and \( z \mapsto \left| z\right| \) a norm on \( \mathbb{C} \). More generally, for any \( \alpha \geq 1 \), if \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in {\mathbb{K}}^{n} \) (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \)),

\[
\parallel x{\parallel }_{\alpha } = {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{\alpha }\right) }^{1/\alpha }
\]

définit une norme sur \( {\mathbb{K}}^{n} \) (voir la conséquence de l’inégalité de Minkowsky, page 98), de même que \( \parallel x{\parallel }_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) .

> defines a norm on \( {\mathbb{K}}^{n} \) (see the consequence of Minkowski's inequality, page 98), as does \( \parallel x{\parallel }_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \).

Dans un e.v.n, les opérations \( \left( {x, y}\right) \mapsto x + y \) et \( \left( {\lambda , x}\right) \mapsto {\lambda x} \) sont continues. La norme est également une fonction continue.

> In an n.v.s, the operations \( \left( {x, y}\right) \mapsto x + y \) and \( \left( {\lambda , x}\right) \mapsto {\lambda x} \) are continuous. The norm is also a continuous function.

Si \( V \) est un s.e.v. de l’e.v.n \( E \) , alors son adhérence \( \bar{V} \) est un s.e.v de \( E \) . En particulier, un hyperplan de \( E \) est soit fermé, soit dense dans \( E \) .

> If \( V \) is a subspace of the n.v.s \( E \), then its closure \( \bar{V} \) is a subspace of \( E \). In particular, a hyperplane of \( E \) is either closed or dense in \( E \).
