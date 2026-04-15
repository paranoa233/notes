#### 4.1. Definitions

DÉFINITION 1. On appelle série entière toute série de fonctions de la forme \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{a}_{n}{z}^{n} \) où \( z \) est une variable complexe et où \( \left( {a}_{n}\right) \) est une suite complexe.

> DEFINITION 1. A power series is any series of functions of the form \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}{a}_{n}{z}^{n} \) where \( z \) is a complex variable and \( \left( {a}_{n}\right) \) is a complex sequence.

Rayon de convergence. Il est naturel de s'interroger sur le domaine des nombres complexes \( z \) pour lesquels une série entière converge.

> Radius of convergence. It is natural to inquire about the domain of complex numbers \( z \) for which a power series converges.

\( \rightarrow \) PROPOSITION 1 (LEMME D’ABEL). Soit \( \sum {a}_{n}{z}^{n} \) une série entière et \( {z}_{0} \in \mathbb{C} \) tel que la suite \( {\left( {a}_{n}{z}_{0}^{n}\right) }_{n \in \mathbb{N}} \) soit bornée. Alors

> \( \rightarrow \) PROPOSITION 1 (ABEL'S LEMMA). Let \( \sum {a}_{n}{z}^{n} \) be a power series and \( {z}_{0} \in \mathbb{C} \) such that the sequence \( {\left( {a}_{n}{z}_{0}^{n}\right) }_{n \in \mathbb{N}} \) is bounded. Then

(i) \( \forall z \in \mathbb{C},\left| z\right| < \left| {z}_{0}\right| \) , la série \( \sum {a}_{n}{z}^{n} \) est absolument convergente ;

> (i) \( \forall z \in \mathbb{C},\left| z\right| < \left| {z}_{0}\right| \) , the series \( \sum {a}_{n}{z}^{n} \) is absolutely convergent;

(ii) pour tout \( r,0 < r < \left| {z}_{0}\right| \) , la série de fonctions \( \sum {a}_{n}{z}^{n} \) est normalement conver-gente dans \( \{ z \in \mathbb{C}\left| \right| z \mid \leq r\} \) .

> (ii) for any \( r,0 < r < \left| {z}_{0}\right| \) , the series of functions \( \sum {a}_{n}{z}^{n} \) is normally convergent in \( \{ z \in \mathbb{C}\left| \right| z \mid \leq r\} \) .

Démonstration. Si \( M \) est un majorant de \( \left( {\left| {a}_{n}\right| {\left| {z}_{0}\right| }^{n}}\right) \) , la preuve est simple à partir de la majoration

> Proof. If \( M \) is an upper bound for \( \left( {\left| {a}_{n}\right| {\left| {z}_{0}\right| }^{n}}\right) \) , the proof is simple based on the inequality

\[
\left| {{a}_{n}{z}^{n}}\right|  = {\left| \frac{z}{{z}_{0}}\right| }^{n}\left| {a}_{n}\right| {\left| {z}_{0}\right| }^{n} \leq  M{\left| \frac{z}{{z}_{0}}\right| }^{n}.
\]

Le lemme d'Abel justifie la définition suivante.

> Abel's lemma justifies the following definition.

DéFINITION 2 (Rayon de convergence). Soit \( \sum {a}_{n}{z}^{n} \) une série entière. Le nombre

> DEFINITION 2 (Radius of convergence). Let \( \sum {a}_{n}{z}^{n} \) be a power series. The number

\[
R = \sup \left\{  {r \geq  0 \mid  }\right. \text{ la suite }\left( {\left| {a}_{n}\right| {r}^{n}}\right) \text{ est bornée }\}
\]

s’appelle rayon de convergence de \( \sum {a}_{n}{z}^{n} \) . D’après le lemme d’Abel,

> is called the radius of convergence of \( \sum {a}_{n}{z}^{n} \) . According to Abel's lemma,

- pour tout \( z \in  \mathbb{C} \) tel que \( \left| z\right|  < R,\sum {a}_{n}{z}^{n} \) converge absolument ;

> - for any \( z \in  \mathbb{C} \) such that \( \left| z\right|  < R,\sum {a}_{n}{z}^{n} \) converges absolutely;

- pour tout \( z \in  \mathbb{C} \) tel que \( \left| z\right|  > R,\overline{\sum }{a}_{n}{z}^{n} \) diverge;

> - for any \( z \in  \mathbb{C} \) such that \( \left| z\right|  > R,\overline{\sum }{a}_{n}{z}^{n} \) diverges;

- pour tout \( r \) tel que \( 0 \leq  r < R \) , la série entière \( \sum {a}_{n}{z}^{n} \) converge normalement sur \( \{ z \in  \mathbb{C}\left| \right| z \mid   \leq  r\} . \)

> - for any \( r \) such that \( 0 \leq  r < R \) , the power series \( \sum {a}_{n}{z}^{n} \) converges normally on \( \{ z \in  \mathbb{C}\left| \right| z \mid   \leq  r\} . \)

Le disque ouvert \( \{ z \in \mathbb{C}\left| \right| z \mid < R\} \) est appelé disque de convergence de la série entière.

> The open disk \( \{ z \in \mathbb{C}\left| \right| z \mid < R\} \) is called the disk of convergence of the power series.

Remarque 1. - On peut avoir \( R = 0 \) ou \( R = + \infty \) . Si \( R = + \infty ,\sum {a}_{n}{z}^{n} \) converge pour tout \( z \in \mathbb{C} \) et la somme de cette série entière définit une fonction de \( \mathbb{C} \) dans \( \mathbb{C} \) appelée fonction entière.

> Remark 1. - We may have \( R = 0 \) or \( R = + \infty \) . If \( R = + \infty ,\sum {a}_{n}{z}^{n} \) converges for all \( z \in \mathbb{C} \) and the sum of this power series defines a function from \( \mathbb{C} \) to \( \mathbb{C} \) called an entire function.

- Sur le cercle \( \left| z\right|  = R \) , la série entière peut ou non converger.

> - On the circle \( \left| z\right|  = R \) , the power series may or may not converge.

- Les séries entières \( \sum {a}_{n}{z}^{n} \) et \( \sum \left| {a}_{n}\right| {z}^{n} \) ont même rayon de convergence.

> - The power series \( \sum {a}_{n}{z}^{n} \) and \( \sum \left| {a}_{n}\right| {z}^{n} \) have the same radius of convergence.

Calcul pratique du rayon de convergence. Il existe quelques recettes qui permettent parfois de calculer explicitement le rayon de convergence d'une série entière. Celles ci sont des conséquences directes des règles de d'Alembert et de Cauchy que l'on a vu pour les séries numériques.

> Practical calculation of the radius of convergence. There are some recipes that sometimes allow for the explicit calculation of the radius of convergence of a power series. These are direct consequences of the d'Alembert and Cauchy rules seen for numerical series.

Proposition 2 (Règle de d’Alembert). Si \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left| {{a}_{n + 1}/{a}_{n}}\right| = \lambda \) avec \( \lambda \in \left\lbrack {0, + \infty }\right\rbrack \) , alors le rayon de convergence de la série entière \( \sum {a}_{n}{z}^{n} \) est \( R = 1/\lambda \) (en convenant \( 1/0 = + \infty \) et \( 1/ + \infty = 0 \) ).

> Proposition 2 (d'Alembert's rule). If \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\left| {{a}_{n + 1}/{a}_{n}}\right| = \lambda \) with \( \lambda \in \left\lbrack {0, + \infty }\right\rbrack \) , then the radius of convergence of the power series \( \sum {a}_{n}{z}^{n} \) is \( R = 1/\lambda \) (with the convention \( 1/0 = + \infty \) and \( 1/ + \infty = 0 \) ).

Proposition 3 (Règle de Cauchy). Si \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\left| {a}_{n}\right| }^{1/n} = \lambda \) avec \( \lambda \in \left\lbrack {0, + \infty }\right\rbrack \) , alors le rayon de convergence de la série entière \( \sum {a}_{n}{z}^{n} \) est \( R = 1/\lambda \) (en convenant \( 1/0 = + \infty \) et \( 1/ + \infty = 0) \) .

> Proposition 3 (Cauchy's rule). If \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\left| {a}_{n}\right| }^{1/n} = \lambda \) with \( \lambda \in \left\lbrack {0, + \infty }\right\rbrack \) , then the radius of convergence of the power series \( \sum {a}_{n}{z}^{n} \) is \( R = 1/\lambda \) (with the convention \( 1/0 = + \infty \) and \( 1/ + \infty = 0) \) .

Exemple 1. Grâce à la règle de d'Alembert, on montre facilement que

> Example 1. Using d'Alembert's rule, it is easy to show that

- la série entière \( \sum {z}^{n}/n \) ! a un rayon de convergence infini ;

> - the power series \( \sum {z}^{n}/n \) ! has an infinite radius of convergence;

- pour tout \( \alpha  \in  \mathbb{R} \) , la série entière \( \sum {n}^{\alpha }{z}^{n} \) a un rayon de convergence égal à 1 ;

> - for any \( \alpha  \in  \mathbb{R} \) , the power series \( \sum {n}^{\alpha }{z}^{n} \) has a radius of convergence equal to 1;

- la série entière \( \sum n!{z}^{n} \) a un rayon de convergence nul.

> - the power series \( \sum n!{z}^{n} \) has a radius of convergence of zero.

Remarque 2. - Attention, les règles de d'Alembert ou de Cauchy ne s'appliquent pas toujours (essayez de les appliquer, par exemple,à \( \sum {z}^{2n} \) ).

> Remark 2. - Be careful, d'Alembert's or Cauchy's rules do not always apply (try applying them, for example, to \( \sum {z}^{2n} \) ).

- On peut montrer, pour une série entière donnée, que si la règle de d'Alembert s'applique alors la règle de Cauchy s'applique (la réciproque est fausse).

> - It can be shown, for a given power series, that if d'Alembert's rule applies then Cauchy's rule applies (the converse is false).

- Dans tous les cas, on montre que le rayon de convergence de \( \sum {a}_{n}{z}^{n} \) est \( 1/\rho \) avec \( \rho  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left( {\mathop{\sup }\limits_{{p \geq  n}}{\left| {a}_{p}\right| }^{1/p}}\right) . \)

> - In all cases, it is shown that the radius of convergence of \( \sum {a}_{n}{z}^{n} \) is \( 1/\rho \) with \( \rho  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}\left( {\mathop{\sup }\limits_{{p \geq  n}}{\left| {a}_{p}\right| }^{1/p}}\right) . \)

Somme et produit de séries entières. Soient \( \sum {a}_{n}{z}^{n} \) et \( \sum {b}_{n}{z}^{n} \) deux séries entières de rayon de convergence respectivement égal à \( R > 0 \) et \( {R}^{\prime } > 0 \) . Notons \( f \) et \( g \) les sommes de ces séries entières sur leur disque de convergence \( D \) et \( {D}^{\prime } \) .

> Sum and product of power series. Let \( \sum {a}_{n}{z}^{n} \) and \( \sum {b}_{n}{z}^{n} \) be two power series with radii of convergence equal to \( R > 0 \) and \( {R}^{\prime } > 0 \) respectively. Let \( f \) and \( g \) denote the sums of these power series on their disks of convergence \( D \) and \( {D}^{\prime } \) .

Somme. La série entière \( \sum {c}_{n}{z}^{n} \) définie par \( {c}_{n} = {a}_{n} + {b}_{n} \) est appelée somme des séries entières \( \sum {a}_{n}{z}^{n} \) et \( \sum {b}_{n}{z}^{n} \) . Son rayon de convergence \( {R}^{\prime \prime } \) de vérifie \( {R}^{\prime \prime } \geq \inf \left\{ {R,{R}^{\prime }}\right\} \) et sur \( D \cap {D}^{\prime }, f + g \) est la somme de la série entière \( \sum {c}_{n}{z}^{n} \) .

> Sum. The power series \( \sum {c}_{n}{z}^{n} \) defined by \( {c}_{n} = {a}_{n} + {b}_{n} \) is called the sum of the power series \( \sum {a}_{n}{z}^{n} \) and \( \sum {b}_{n}{z}^{n} \) . Its radius of convergence \( {R}^{\prime \prime } \) satisfies \( {R}^{\prime \prime } \geq \inf \left\{ {R,{R}^{\prime }}\right\} \) and on \( D \cap {D}^{\prime }, f + g \) is the sum of the power series \( \sum {c}_{n}{z}^{n} \) .

Produit. La série entière \( \sum {c}_{n}{z}^{n} \) définie par

> Product. The power series \( \sum {c}_{n}{z}^{n} \) defined by

\[
\forall n \in  \mathbb{N},\;{c}_{n} = {a}_{0}{b}_{n} + {a}_{1}{b}_{n - 1} + \cdots  + {a}_{n - 1}{b}_{1} + {a}_{n}{b}_{0}
\]

est appelée produit de Cauchy des séries entières \( \sum {a}_{n}{z}^{n} \) et \( \sum {b}_{n}{z}^{n} \) . Son rayon de convergence \( {R}^{\prime \prime } \) vérifie \( {R}^{\prime \prime } \geq \inf \left\{ {R,{R}^{\prime }}\right\} \) et sur \( D \cap {D}^{\prime } \) , le produit \( {fg} \) est la somme de la série entière \( \sum {c}_{n}{z}^{n} \) (conséquence du théorème 9 page 216 sur le produit de Cauchy de deux séries absolument convergentes).

> is called the Cauchy product of the power series \( \sum {a}_{n}{z}^{n} \) and \( \sum {b}_{n}{z}^{n} \) . Its radius of convergence \( {R}^{\prime \prime } \) satisfies \( {R}^{\prime \prime } \geq \inf \left\{ {R,{R}^{\prime }}\right\} \) and on \( D \cap {D}^{\prime } \) , the product \( {fg} \) is the sum of the power series \( \sum {c}_{n}{z}^{n} \) (a consequence of theorem 9 on page 216 regarding the Cauchy product of two absolutely convergent series).

Remarque 3. On ne peut rien dire de plus en général sur les rayons de convergence de la somme ou du produit de Cauchy de deux séries entières. Par exemple, les séries entières \( \sum {z}^{n} \) et \( \sum - {z}^{n} \) ont leur rayon de convergence égal à1mais la somme a un rayon de convergence infini.

> Remark 3. In general, nothing more can be said about the radii of convergence of the sum or the Cauchy product of two power series. For example, the power series \( \sum {z}^{n} \) and \( \sum - {z}^{n} \) have a radius of convergence equal to 1, but their sum has an infinite radius of convergence.
