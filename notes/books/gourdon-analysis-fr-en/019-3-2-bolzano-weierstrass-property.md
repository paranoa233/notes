#### 3.2. Bolzano-Weierstrass Property

*Français : 3.2. Propriété de Bolzano-Weierstrass*

La compacité d'un espace métrique peut être caractérisée par la propriété dite de Bolzano-Weierstrass, a priori totalement différente, mais parfois beaucoup plus souple d'utilisation.

> The compactness of a metric space can be characterized by the so-called Bolzano-Weierstrass property, which is a priori completely different, but sometimes much more flexible to use.

THÉORÉME 1 (DE BOLZANO-WEIERSTRASS). Un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est compact si et seulement si de toute suite de points de \( E \) , on peut en extraire une sous-suite convergente dans \( E \) .

> THEOREM 1 (BOLZANO-WEIERSTRASS). A metric space \( \left( {E,\mathrm{\;d}}\right) \) is compact if and only if from any sequence of points in \( E \) , one can extract a subsequence converging in \( E \) .

Démonstration. La condition nécessaire se montre facilement, la condition suffisante est plus délicate.

> Proof. The necessary condition is shown easily; the sufficient condition is more delicate.

Condition nécessaire. (Borel-Lebesgue : Bolzano-Weierstrass). Nous allons en donner deux preuves.

> Necessary condition. (Borel-Lebesgue : Bolzano-Weierstrass). We will provide two proofs.

Première preuve. Soit \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) une suite de \( E \) . Pour tout \( p \in \mathbb{N} \) , on note \( {A}_{p} = \left\{ {{x}_{n}, n \geq p}\right\} \) . La suite \( {\left( \overline{{A}_{p}}\right) }_{p \in \mathbb{N}} \) est une suite décroissante de fermés non vides, donc (voir la proposition 3) \( { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \neq \varnothing \) . Choisissons \( x \in { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \) . On construit une sous-suite \( \left( {x}_{\varphi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) comme suit.

> First proof. Let \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of \( E \) . For every \( p \in \mathbb{N} \) , we denote \( {A}_{p} = \left\{ {{x}_{n}, n \geq p}\right\} \) . The sequence \( {\left( \overline{{A}_{p}}\right) }_{p \in \mathbb{N}} \) is a decreasing sequence of non-empty closed sets, therefore (see proposition 3) \( { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \neq \varnothing \) . Let us choose \( x \in { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \) . We construct a subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) as follows.

- On choisit \( {x}_{\varphi \left( 0\right) } \in  {A}_{0} \) .

> - We choose \( {x}_{\varphi \left( 0\right) } \in  {A}_{0} \) .

- L’élément \( {x}_{\varphi \left( n\right) } \) étant construit, on prend \( {x}_{\varphi \left( {n + 1}\right) } \in  {A}_{n + 1} \) tel que \( \varphi \left( {n + 1}\right)  > \varphi \left( n\right) \) et \( \mathrm{d}\left( {{x}_{\varphi \left( {n + 1}\right) }, x}\right)  < 1/{2}^{n + 1} \) (c’est possible car \( x \in  \overline{{A}_{n + 1}} \) ).

> - The element \( {x}_{\varphi \left( n\right) } \) being constructed, we take \( {x}_{\varphi \left( {n + 1}\right) } \in  {A}_{n + 1} \) such that \( \varphi \left( {n + 1}\right)  > \varphi \left( n\right) \) and \( \mathrm{d}\left( {{x}_{\varphi \left( {n + 1}\right) }, x}\right)  < 1/{2}^{n + 1} \) (this is possible because \( x \in  \overline{{A}_{n + 1}} \) ).

Ainsi construite, \( \left( {x}_{\varphi \left( n\right) }\right) \) est une sous-suite de \( \left( {x}_{n}\right) \) qui converge vers \( x \) .

> Thus constructed, \( \left( {x}_{\varphi \left( n\right) }\right) \) is a subsequence of \( \left( {x}_{n}\right) \) that converges to \( x \) .

Seconde preuve. Soit \( \left( {x}_{n}\right) \) une suite de \( E \) . Si cette suite ne prend qu’un nombre de valeurs fini, on peut en extraire une sous-suite constante donc convergente. Sinon, \( A = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \) est infini. Nous allons prouver que \( A \) a au moins un point d’accumulation. Supposons le contraire, de sorte que pour tout \( x \in E \) , il existe \( {r}_{x} > 0 \) tel que \( \mathrm{B}\left( {x,{r}_{x}}\right) \cap A \) est fini. Du recouvrement \( { \cup }_{x \in E}\mathrm{\;B}\left( {x,{r}_{x}}\right) \) de \( E \) , on peut en extraire un sous-recouvrement fini. En termes mathématiques, ceci s'écrit

> Second proof. Let \( \left( {x}_{n}\right) \) be a sequence of \( E \) . If this sequence takes only a finite number of values, we can extract a constant, and therefore convergent, subsequence. Otherwise, \( A = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \) is infinite. We will prove that \( A \) has at least one accumulation point. Assume the contrary, such that for every \( x \in E \) , there exists \( {r}_{x} > 0 \) such that \( \mathrm{B}\left( {x,{r}_{x}}\right) \cap A \) is finite. From the covering \( { \cup }_{x \in E}\mathrm{\;B}\left( {x,{r}_{x}}\right) \) of \( E \) , we can extract a finite subcovering. In mathematical terms, this is written

\[
\exists J \subset  E, J\text{ fini, }\;\text{ avec }\;E = { \cup  }_{x \in  J}\mathrm{\;B}\left( {x,{r}_{x}}\right) .
\]

Ainsi, \( A = { \cup }_{x \in J}\left( {\mathrm{\;B}\left( {x,{r}_{x}}\right) \cap A}\right) \) , réunion finie d’ensembles finis, est fini, ce qui est contradictoire.

> Thus, \( A = { \cup }_{x \in J}\left( {\mathrm{\;B}\left( {x,{r}_{x}}\right) \cap A}\right) \) , a finite union of finite sets, is finite, which is a contradiction.

L’ensemble \( A \) admet donc au moins un point d’accumulation \( x \in E \) . Ainsi, \( x \) est valeur d’adhérence de la suite \( \left( {x}_{n}\right) \) , donc il existe une sous-suite de \( \left( {x}_{n}\right) \) qui converge vers \( x \) .

> The set \( A \) therefore admits at least one accumulation point \( x \in E \) . Thus, \( x \) is a cluster point of the sequence \( \left( {x}_{n}\right) \) , so there exists a subsequence of \( \left( {x}_{n}\right) \) that converges to \( x \) .

Condition suffisante. (Bolzano-Weierstrass \( \Rightarrow \) Borel-Lebesgue). Nous montrons deux lemmes. PRÉCOMPACITÉ (OU \( \varepsilon \) -RECOUVREMENT). Un espace métrique \( E \) est dit précompact si pour tout \( \varepsilon > 0 \) , il existe un recouvrement fini de \( E \) par des boules (ouvertes) de rayon \( \varepsilon \) .

> Sufficient condition. (Bolzano-Weierstrass \( \Rightarrow \) Borel-Lebesgue). We show two lemmas. PRECOMPACTNESS (OR \( \varepsilon \) -COVERING). A metric space \( E \) is said to be precompact if for every \( \varepsilon > 0 \) , there exists a finite covering of \( E \) by (open) balls of radius \( \varepsilon \) .

LEMME 1. Tout espace métrique \( \left( {E,\mathrm{\;d}}\right) \) vérifiant la propriété de Bolzano-Weierstrass est pré- compact.

> LEMMA 1. Every metric space \( \left( {E,\mathrm{\;d}}\right) \) satisfying the Bolzano-Weierstrass property is precompact.

En effet. Raisonnons par l'absurde en supposant l'existence de \( \varepsilon > 0 \) tel que l’on ne puisse pas trouver un sous-recouvrement fini de \( E \) par des boules de rayon \( \varepsilon \) .

> Indeed. Let us reason by contradiction by assuming the existence of \( \varepsilon > 0 \) such that one cannot find a finite subcovering of \( E \) by balls of radius \( \varepsilon \) .

- Soit \( {x}_{0} \in  E \) . Alors \( \mathrm{B}\left( {{x}_{0},\varepsilon }\right)  \neq  E \) .

> - Let \( {x}_{0} \in  E \) . Then \( \mathrm{B}\left( {{x}_{0},\varepsilon }\right)  \neq  E \) .

- Donc il existe \( {x}_{1} \in  E \) tel que \( \mathrm{d}\left( {{x}_{0},{x}_{1}}\right)  \geq  \varepsilon \) .

> - Thus there exists \( {x}_{1} \in  E \) such that \( \mathrm{d}\left( {{x}_{0},{x}_{1}}\right)  \geq  \varepsilon \) .

- De même, comme \( \mathrm{B}\left( {{x}_{0},\varepsilon }\right)  \cup  \mathrm{B}\left( {{x}_{1},\varepsilon }\right)  \neq  E \) , il existe \( {x}_{2} \in  E \) tel que \( \mathrm{d}\left( {{x}_{0},{x}_{1}}\right)  \geq  \varepsilon \) et \( \mathrm{d}\left( {{x}_{0},{x}_{2}}\right)  \geq  \varepsilon \) .

> - Similarly, since \( \mathrm{B}\left( {{x}_{0},\varepsilon }\right)  \cup  \mathrm{B}\left( {{x}_{1},\varepsilon }\right)  \neq  E \) , there exists \( {x}_{2} \in  E \) such that \( \mathrm{d}\left( {{x}_{0},{x}_{1}}\right)  \geq  \varepsilon \) and \( \mathrm{d}\left( {{x}_{0},{x}_{2}}\right)  \geq  \varepsilon \) .

- On recommence \( \ldots {x}_{0},{x}_{1},\ldots ,{x}_{n} \) étant construits tels que \( \forall i < j \leq  n,\mathrm{\;d}\left( {{x}_{i},{x}_{j}}\right)  \geq  \varepsilon \) , on sait que \( { \cup  }_{0 \leq  i \leq  n}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right)  \neq  E \) , donc il existe \( {x}_{n + 1} \in  E \) tel que pour tout \( i,0 \leq  i \leq  n \) , \( \mathrm{d}\left( {{x}_{i},{x}_{n + 1}}\right)  \geq  \varepsilon . \)

> - We repeat this; \( \ldots {x}_{0},{x}_{1},\ldots ,{x}_{n} \) being constructed such that \( \forall i < j \leq  n,\mathrm{\;d}\left( {{x}_{i},{x}_{j}}\right)  \geq  \varepsilon \) , we know that \( { \cup  }_{0 \leq  i \leq  n}\mathrm{\;B}\left( {{x}_{i},\varepsilon }\right)  \neq  E \) , therefore there exists \( {x}_{n + 1} \in  E \) such that for all \( i,0 \leq  i \leq  n \) , \( \mathrm{d}\left( {{x}_{i},{x}_{n + 1}}\right)  \geq  \varepsilon . \)

On construit ainsi une suite \( \left( {x}_{n}\right) \) de \( E \) telle que \( \mathrm{d}\left( {{x}_{i},{x}_{j}}\right) \geq \varepsilon \) dès que \( i \neq j \) . La suite \( \left( {x}_{n}\right) \) n’admet donc aucune sous-suite convergente car aucune sous-suite n'est de Cauchy, d'où la contradiction voulue, d'où notre premier lemme.

> We thus construct a sequence \( \left( {x}_{n}\right) \) of \( E \) such that \( \mathrm{d}\left( {{x}_{i},{x}_{j}}\right) \geq \varepsilon \) whenever \( i \neq j \) . The sequence \( \left( {x}_{n}\right) \) therefore admits no convergent subsequence because no subsequence is Cauchy, hence the desired contradiction, which proves our first lemma.

LEMME 2. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique vérifiant la propriété de Bolzano-Weierstrass, et soit \( {\left( {O}_{i}\right) }_{i \in I} \) un recouvrement de \( E \) par des ouverts de \( E \) . Alors :

> LEMMA 2. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space satisfying the Bolzano-Weierstrass property, and let \( {\left( {O}_{i}\right) }_{i \in I} \) be a covering of \( E \) by open sets of \( E \) . Then:

\[
\left( {\exists \alpha  > 0,\forall x \in  E,\exists i \in  I}\right) ,\;\mathrm{\;B}\left( {x,\alpha }\right)  \subset  {O}_{i}.
\]

En effet. Raisonnons par l'absurde, en supposant que

> Indeed. Let us reason by contradiction, assuming that

\[
\left( {\forall \alpha  > 0,\exists x \in  E,\forall i \in  I}\right) ,\;\mathrm{B}\left( {x,\alpha }\right)  \text{ ⊄ } {O}_{i}.
\]

En particulier,

> In particular,

\[
\left( {\forall n \in  {\mathbb{N}}^{ * },\exists {x}_{n} \in  E,\forall i \in  I}\right) ,\;\mathrm{B}\left( {{x}_{n},\frac{1}{n}}\right)  \text{ ⊄ } {O}_{i}.
\]

Soit \( \left( {x}_{\varphi \left( n\right) }\right) \) une sous-suite de \( \left( {x}_{n}\right) \) qui converge. Notons \( x \) sa limite. Il existe \( i \in I \) tel que \( x \in {O}_{i} \) . Comme \( {O}_{i} \) est ouvert, il existe \( r > 0 \) tel que \( \mathrm{B}\left( {x,{2r}}\right) \subset {O}_{i} \) . Comme \( \left( {x}_{\varphi \left( n\right) }\right) \) converge vers \( x \) ,

> Let \( \left( {x}_{\varphi \left( n\right) }\right) \) be a convergent subsequence of \( \left( {x}_{n}\right) \). Let \( x \) denote its limit. There exists \( i \in I \) such that \( x \in {O}_{i} \). Since \( {O}_{i} \) is open, there exists \( r > 0 \) such that \( \mathrm{B}\left( {x,{2r}}\right) \subset {O}_{i} \). Since \( \left( {x}_{\varphi \left( n\right) }\right) \) converges to \( x \),

\[
\exists N \in  \mathbb{N},\forall n \geq  N,\;\left( {\mathrm{\;d}\left( {{x}_{\varphi \left( n\right) }, x}\right)  < r\;\text{ et }\;\varphi \left( n\right)  > \frac{1}{r}}\right) .
\]

Alors

> Then

\[
\forall n \geq  N,\forall y \in  \mathrm{B}\left( {{x}_{\varphi \left( n\right) },\frac{1}{\varphi \left( n\right) }}\right) ,\;\mathrm{d}\left( {x, y}\right)  \leq  \mathrm{d}\left( {x,{x}_{\varphi \left( n\right) }}\right)  + \mathrm{d}\left( {{x}_{\varphi \left( n\right) }, y}\right)  < r + r = {2r},
\]

donc pour tout \( n \geq N,\mathrm{\;B}\left( {{x}_{\varphi \left( n\right) },1/\varphi \left( n\right) }\right) \subset {O}_{i} \) , ce qui est absurde. D’où le lemme 2.

> therefore for all \( n \geq N,\mathrm{\;B}\left( {{x}_{\varphi \left( n\right) },1/\varphi \left( n\right) }\right) \subset {O}_{i} \), which is absurd. Hence lemma 2.

Achevons notre raisonnement. Soit \( \left( {E,\mathrm{\;d}}\right) \) vérifiant la propriété de Bolzano-Weierstrass, soit \( {\left( {O}_{i}\right) }_{i \in I} \) un recouvrement de \( E \) par des ouverts de \( E \) . D’après le lemme 2,

> Let us complete our reasoning. Let \( \left( {E,\mathrm{\;d}}\right) \) satisfy the Bolzano-Weierstrass property, and let \( {\left( {O}_{i}\right) }_{i \in I} \) be an open cover of \( E \) by open sets of \( E \). According to lemma 2,

\[
\exists \alpha  > 0,\forall x \in  E,\exists i \in  I,\;\mathrm{\;B}\left( {x,\alpha }\right)  \subset  {O}_{i}.
\]

D’après le lemme 1, on peut recouvrir \( E \) par un nombre fini de boules de rayon \( \alpha \) , ce qui s’écrit

> According to lemma 1, one can cover \( E \) with a finite number of balls of radius \( \alpha \), which is written as

\[
\exists n \in  {\mathbb{N}}^{ * },\exists {x}_{1},\ldots ,{x}_{n} \in  E,\;E = { \cup  }_{i = 1}^{n}\mathrm{\;B}\left( {{x}_{i},\alpha }\right) .
\]

Or pour tout \( j,1 \leq j \leq n \) , il existe \( {i}_{j} \in I \) tel que \( \mathrm{B}\left( {{x}_{j},\alpha }\right) \subset {O}_{{i}_{j}} \) . On en déduit \( E = { \cup }_{j = 1}^{n}{O}_{{i}_{j}} \) , d'où le résultat.

> However, for all \( j,1 \leq j \leq n \), there exists \( {i}_{j} \in I \) such that \( \mathrm{B}\left( {{x}_{j},\alpha }\right) \subset {O}_{{i}_{j}} \). We deduce \( E = { \cup }_{j = 1}^{n}{O}_{{i}_{j}} \), hence the result.

Il existe d'autres formulations de ce théorème qui sont les suivantes.

> There are other formulations of this theorem, which are as follows.

\( \rightarrow \) COROLLAIRE 1. Un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est compact si et seulement si l’une des assertions suivantes est vérifiée

> \( \rightarrow \) COROLLARY 1. A metric space \( \left( {E,\mathrm{\;d}}\right) \) is compact if and only if one of the following assertions is satisfied

- Toute suite de \( E \) admet au moins une valeur d’adhérence dans \( E \) .

> - Every sequence in \( E \) has at least one cluster point in \( E \).

- Toute partie infinie de \( E \) admet au moins un point d’accumulation dans \( E \) .

> - Every infinite subset of \( E \) has at least one accumulation point in \( E \).
