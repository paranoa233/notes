#### 1.1. Norms and Distances

*Français : 1.1. Normes et Distances*

##### Norms.

*Français : Normes.*

DéFINITION 1. Soit \( E \) un \( \mathbb{K} \) -espace vectoriel (où \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ). Une norme sur \( E \) est une application \( E \rightarrow {\mathbb{R}}^{ + }\;x \mapsto \parallel x\parallel \) telle que

> DEFINITION 1. Let \( E \) be a \( \mathbb{K} \) -vector space (where \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \) ). A norm on \( E \) is a mapping \( E \rightarrow {\mathbb{R}}^{ + }\;x \mapsto \parallel x\parallel \) such that

(i) On a \( \parallel x\parallel = 0 \) si et seulement si \( x = 0 \) .

> (i) We have \( \parallel x\parallel = 0 \) if and only if \( x = 0 \) .

(ii) Pour tout \( \lambda \in \mathbb{K} \) , pour tout \( x \in E,\parallel {\lambda x}\parallel = \left| \lambda \right| \cdot \parallel x\parallel \) .

> (ii) For all \( \lambda \in \mathbb{K} \) , for all \( x \in E,\parallel {\lambda x}\parallel = \left| \lambda \right| \cdot \parallel x\parallel \) .

(iii) Pour tout \( \left( {x, y}\right) \in {E}^{2},\parallel x + y\parallel \leq \parallel x\parallel + \parallel y\parallel \) (inégalité triangulaire).

> (iii) For all \( \left( {x, y}\right) \in {E}^{2},\parallel x + y\parallel \leq \parallel x\parallel + \parallel y\parallel \) (triangle inequality).

Muni d’une norme, \( E \) est appelé un \( \mathbb{K} \) -espace vectoriel normé (en abrégé e.v.n).

> Equipped with a norm, \( E \) is called a \( \mathbb{K} \) -normed vector space (abbreviated as n.v.s.).

Exemple 1. - \( x \mapsto \left| x\right| \) est une norme sur \( \mathbb{R}, z \mapsto \left| z\right| \) est une norme sur \( \mathbb{C} \) .

> Example 1. - \( x \mapsto \left| x\right| \) is a norm on \( \mathbb{R}, z \mapsto \left| z\right| \) is a norm on \( \mathbb{C} \) .

- Dans \( {\mathbb{R}}^{n} \) , en notant \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) , on a les normes classiques suivantes

> - In \( {\mathbb{R}}^{n} \) , by denoting \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) , we have the following classical norms

\[
\parallel x{\parallel }_{1} = \mathop{\sum }\limits_{i}\left| {x}_{i}\right| ,\;\parallel x{\parallel }_{2} = \sqrt{\mathop{\sum }\limits_{i}{x}_{i}^{2}},\;\parallel x{\parallel }_{\infty } = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| .
\]

Plus généralement, pour tout \( \alpha \geq 1,\parallel x{\parallel }_{\alpha } = {\left( \mathop{\sum }\limits_{i}{\left| {x}_{i}\right| }^{\alpha }\right) }^{1/\alpha } \) est une norme sur \( {\mathbb{R}}^{n} \) (voir la conséquence de l'inégalité de Minkowsky, page 98).

> More generally, for all \( \alpha \geq 1,\parallel x{\parallel }_{\alpha } = {\left( \mathop{\sum }\limits_{i}{\left| {x}_{i}\right| }^{\alpha }\right) }^{1/\alpha } \) is a norm on \( {\mathbb{R}}^{n} \) (see the consequence of Minkowski's inequality, page 98).

- L’ensemble \( \mathcal{B}\left( {X, E}\right) \) des applications bornées d’un ensemble \( X \) dans un e.v.n \( E \) est un espace vectoriel normé muni de la norme \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in  X}}\left| {f\left( x\right) }\right| \) (cette norme s'appelle norme de la convergence uniforme.)

> - The set \( \mathcal{B}\left( {X, E}\right) \) of bounded mappings from a set \( X \) into an n.v.s. \( E \) is a normed vector space equipped with the norm \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in  X}}\left| {f\left( x\right) }\right| \) (this norm is called the uniform convergence norm.)

Remarque 1. Lorsque seules les propriétés (ii) et (iii) de la définition sont vérifiées, on dit que \( \parallel \cdot \parallel \) est une semi-norme.

> Remark 1. When only properties (ii) and (iii) of the definition are satisfied, \( \parallel \cdot \parallel \) is called a semi-norm.

Distances.

> Distances.

DéFINITION 2. Soit \( E \) un ensemble. On appelle distance sur \( E \) toute application d : \( E \times \; E \rightarrow {\mathbb{R}}^{ + } \) telle que :

> DEFINITION 2. Let \( E \) be a set. A distance on \( E \) is any mapping d : \( E \times \; E \rightarrow {\mathbb{R}}^{ + } \) such that:

(i) \( \mathrm{d}\left( {x, y}\right) = 0 \) si et seulement si \( x = y \) .

> (i) \( \mathrm{d}\left( {x, y}\right) = 0 \) if and only if \( x = y \) .

(ii) Pour tout \( x, y \in E,\mathrm{\;d}\left( {x, y}\right) = \mathrm{d}\left( {y, x}\right) \) (symétrie).

> (ii) For all \( x, y \in E,\mathrm{\;d}\left( {x, y}\right) = \mathrm{d}\left( {y, x}\right) \) (symmetry).

(iii) Pour tout \( x, y, z \in E,\mathrm{\;d}\left( {x, z}\right) \leq \mathrm{d}\left( {x, y}\right) + \mathrm{d}\left( {y, z}\right) \) (inégalité triangulaire).

> (iii) For all \( x, y, z \in E,\mathrm{\;d}\left( {x, z}\right) \leq \mathrm{d}\left( {x, y}\right) + \mathrm{d}\left( {y, z}\right) \) (triangle inequality).

Muni d'une distance, \( E \) est appelé espace métrique.

> Equipped with a distance, \( E \) is called a metric space.

Exemple 2. - Si \( E \) est un e.v.n, \( \mathrm{d}\left( {x, y}\right) = \parallel x - y\parallel \) définit une distance sur \( E \) , qui fait de l'e.v.n \( E \) un espace métrique. Sauf mention contraire, c'est cette distance que l'on choisit toujours dans un e.v.n.

> Example 2. - If \( E \) is a n.v.s., \( \mathrm{d}\left( {x, y}\right) = \parallel x - y\parallel \) defines a distance on \( E \) , which makes the n.v.s. \( E \) a metric space. Unless otherwise stated, this is the distance always chosen in a n.v.s.

- Sur tout ensemble \( E \) , la distance d définie par

> - On any set \( E \) , the distance d defined by

\[
\mathrm{d}\left( {x, y}\right)  = 0\text{ si }x = y,\;\mathrm{\;d}\left( {x, y}\right)  = 1\text{ si }x \neq  y
\]

est appelée distance discrète sur \( E \) . L’espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est alors appelé espace discret.

> is called the discrete distance on \( E \) . The metric space \( \left( {E,\mathrm{\;d}}\right) \) is then called a discrete space.

##### Diameter of a subset, distance between two subsets.

*Français : Diamètre d'une partie, distance entre deux parties.*

DéFINITION 3. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. Si \( A \subset E, A \neq \varnothing \) , on appelle diamètre de A l’élément de \( \left\lbrack {0, + \infty }\right\rbrack \) défini par

> DEFINITION 3. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. If \( A \subset E, A \neq \varnothing \) , the diameter of A is the element of \( \left\lbrack {0, + \infty }\right\rbrack \) defined by

\[
\delta \left( A\right)  = \mathop{\sup }\limits_{{\left( {x, y}\right)  \in  {A}^{2}}}\mathrm{\;d}\left( {x, y}\right) .
\]

On dit que \( A \) est bornée si \( A = \varnothing \) ou si \( \delta \left( A\right) < + \infty \) .

> \( A \) is said to be bounded if \( A = \varnothing \) or if \( \delta \left( A\right) < + \infty \) .

DéFINITION 4. Soient \( A \) et \( B \) deux parties non vides d’un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) . On appelle distance de \( A \) à \( B \) le réel

> DEFINITION 4. Let \( A \) and \( B \) be two non-empty subsets of a metric space \( \left( {E,\mathrm{\;d}}\right) \) . The distance from \( A \) to \( B \) is the real number

\[
\mathrm{d}\left( {A, B}\right)  = \mathop{\inf }\limits_{\substack{{x \in  A} \\  {y \in  B} }}\mathrm{\;d}\left( {x, y}\right) .
\]

Lorsque \( x \) est un élément de \( E \) , on appelle distance de \( x \) à \( A \) le réel

> When \( x \) is an element of \( E \) , the distance from \( x \) to \( A \) is the real number

\[
\mathrm{d}\left( {x, A}\right)  = \mathrm{d}\left( {\{ x\} , A}\right)  = \mathop{\inf }\limits_{{y \in  A}}\mathrm{\;d}\left( {x, y}\right) .
\]

Remarque 2. Attention ! Avec cette définition, l’application d : \( {\left( \mathcal{P}\left( E\right) \smallsetminus \{ \varnothing \} \right) }^{2}\;\left( {A, B}\right) \rightarrow \; \mathrm{d}\left( {A, B}\right) \) n’est pas une distance sur \( \mathcal{P}\left( E\right) \smallsetminus \{ \varnothing \} \) (on peut avoir \( \mathrm{d}\left( {A, B}\right) = 0 \) avec \( A \neq B \) ).

> Remark 2. Caution! With this definition, the mapping d : \( {\left( \mathcal{P}\left( E\right) \smallsetminus \{ \varnothing \} \right) }^{2}\;\left( {A, B}\right) \rightarrow \; \mathrm{d}\left( {A, B}\right) \) is not a distance on \( \mathcal{P}\left( E\right) \smallsetminus \{ \varnothing \} \) (we can have \( \mathrm{d}\left( {A, B}\right) = 0 \) with \( A \neq B \) ).

##### Balls and spheres.

*Français : Boules et sphères.*

DéFINITION 5. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique. Pour tout \( x \in E \) et pour tout \( \rho > 0 \) , on appelle

> DEFINITION 5. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space. For any \( x \in E \) and for any \( \rho > 0 \), we call

- boule ouverte de centre \( x \) de rayon \( \rho \) l’ensemble \( \mathrm{B}\left( {x,\rho }\right)  = \{ y \in  E \mid  \mathrm{d}\left( {x, y}\right)  < \rho \} \) ,

> - open ball with center \( x \) and radius \( \rho \) the set \( \mathrm{B}\left( {x,\rho }\right)  = \{ y \in  E \mid  \mathrm{d}\left( {x, y}\right)  < \rho \} \),

- boule fermée de centre \( x \) de rayon \( \rho \) l’ensemble \( {\mathrm{B}}_{\mathrm{f}}\left( {x,\rho }\right)  = \{ y \in  E \mid  \mathrm{d}\left( {x, y}\right)  \leq  \rho \} \) ,

> - closed ball with center \( x \) and radius \( \rho \) the set \( {\mathrm{B}}_{\mathrm{f}}\left( {x,\rho }\right)  = \{ y \in  E \mid  \mathrm{d}\left( {x, y}\right)  \leq  \rho \} \),

- sphère de centre \( x \) de rayon \( \rho \) l’ensemble \( \mathrm{S}\left( {x,\rho }\right)  = \{ y \in  E \mid  \mathrm{d}\left( {x, y}\right)  = \rho \} \) .

> - sphere with center \( x \) and radius \( \rho \) the set \( \mathrm{S}\left( {x,\rho }\right)  = \{ y \in  E \mid  \mathrm{d}\left( {x, y}\right)  = \rho \} \).

Lorsque \( E \) est un espace vectoriel normé (muni de la distance issue de la norme) et que \( x = 0,\rho = 1 \) , on parle de boule unité ouverte, boule unité fermée et de sphère unité.

> When \( E \) is a normed vector space (equipped with the distance derived from the norm) and \( x = 0,\rho = 1 \), we speak of the open unit ball, closed unit ball, and unit sphere.

Proposition 1. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique, \( A \) une partie de \( E \) , et \( x \in E \) . L’ensemble A est borné si et seulement s’il existe \( r > 0 \) tel que \( A \subset \mathrm{B}\left( {x, r}\right) \) .

> Proposition 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space, \( A \) a subset of \( E \), and \( x \in E \). The set A is bounded if and only if there exists \( r > 0 \) such that \( A \subset \mathrm{B}\left( {x, r}\right) \).
