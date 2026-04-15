#### 4.1. Definition of the Riemann multiple integral

*Français : 4.1. Définition de l'intégrale multiple de Riemann*

DÉFINITION 1. On appelle pavé de \( {\mathbb{R}}^{n} \) tout ensemble du type \( P = {I}_{1} \times \cdots \times {I}_{n} \) où pour tout \( k,{I}_{k} \) est un intervalle borné de \( \mathbb{R} \) . On appelle mesure \( n \) -dimensionnelle de \( P \) le réel \( \operatorname{mes}\left( P\right) = {\lambda }_{1}\cdots {\lambda }_{n} \) où pour tout \( k,{\lambda }_{k} \) est la longueur de \( {I}_{k} \) (si \( {\bar{I}}_{k} = \left\lbrack {a, b}\right\rbrack ,{\lambda }_{k} = b - a \) ).

> DEFINITION 1. A block of \( {\mathbb{R}}^{n} \) is any set of the type \( P = {I}_{1} \times \cdots \times {I}_{n} \) where for all \( k,{I}_{k} \) is a bounded interval of \( \mathbb{R} \). The \( n \)-dimensional measure of \( P \) is the real number \( \operatorname{mes}\left( P\right) = {\lambda }_{1}\cdots {\lambda }_{n} \) where for all \( k,{\lambda }_{k} \) is the length of \( {I}_{k} \) (if \( {\bar{I}}_{k} = \left\lbrack {a, b}\right\rbrack ,{\lambda }_{k} = b - a \)).

Pour tout sous-ensemble \( A \) de \( {\mathbb{R}}^{n} \) , on notera \( {\chi }_{A} : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) la fonction caractéristique de \( A \) , définie par \( {\chi }_{A}\left( x\right) = 1 \) si \( x \in A, = 0 \) sinon.

> For any subset \( A \) of \( {\mathbb{R}}^{n} \), we denote by \( {\chi }_{A} : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) the characteristic function of \( A \), defined by \( {\chi }_{A}\left( x\right) = 1 \) if \( x \in A, = 0 \) otherwise.

DÉFINITION 2. Une fonction \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) est dite en escalier si on peut l’écrire comme combinaison linéaire de fonctions caractéristiques de pavés de \( {\mathbb{R}}^{n} \) . Une telle famille de pavés est dite bien adaptée à \( f \) . Si \( f = \mathop{\sum }\limits_{i}{\lambda }_{i}{\chi }_{{P}_{i}} \) où \( {P}_{i} \) est un pavé pour tout \( i \) , le réel \( I\left( f\right) = \mathop{\sum }\limits_{i}{\lambda }_{i}\operatorname{mes}\left( {P}_{i}\right) \) ne dépend pas de la famille de pavés \( \left( {P}_{i}\right) \) bien adaptée à \( \varphi \) et on l’appelle intégrale de \( f \) .

> DEFINITION 2. A function \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) is called a step function if it can be written as a linear combination of characteristic functions of blocks of \( {\mathbb{R}}^{n} \). Such a family of blocks is said to be well-adapted to \( f \). If \( f = \mathop{\sum }\limits_{i}{\lambda }_{i}{\chi }_{{P}_{i}} \) where \( {P}_{i} \) is a block for all \( i \), the real number \( I\left( f\right) = \mathop{\sum }\limits_{i}{\lambda }_{i}\operatorname{mes}\left( {P}_{i}\right) \) does not depend on the family of blocks \( \left( {P}_{i}\right) \) well-adapted to \( \varphi \) and it is called the integral of \( f \).

DÉFINITION 3. Soit \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) une fonction bornée,à support compact (i. e. \( f \) est nulle en dehors d'un compact). Soient les deux ensembles

> DEFINITION 3. Let \( f : {\mathbb{R}}^{n} \rightarrow \mathbb{R} \) be a bounded function with compact support (i.e., \( f \) is zero outside a compact set). Let the two sets be

\( {E}^{ + } = \{ I\left( v\right) , f \leq v \) et \( v \) est en escalier \( \} \) et \( {E}^{ - } = \{ I\left( u\right) , u \leq f \) et \( u \) est en escalier \( \} . \)

> \( {E}^{ + } = \{ I\left( v\right) , f \leq v \) and \( v \) is a step function \( \} \) and \( {E}^{ - } = \{ I\left( u\right) , u \leq f \) and \( u \) is a step function \( \} . \)

Les ensembles \( {E}^{ + } \) et \( {E}^{ - } \) sont non vides car \( f \) est bornée, donc \( {I}^{ + } = \inf {E}^{ + } \) et \( {I}^{ - } = \sup {E}^{ - } \) existent. On a toujours \( {I}^{ - } \leq {I}^{ + } \) . Si \( {I}^{ - } = {I}^{ + }, f \) est dite Riemann-intégrable, et le réel \( {\int }_{{\mathbb{R}}^{n}}f\left( x\right) {dx} = {I}^{ - } = {I}^{ + } \) est appelé intégrale de \( f \) sur \( {\mathbb{R}}^{n} \) .

> The sets \( {E}^{ + } \) and \( {E}^{ - } \) are non-empty because \( f \) is bounded, so \( {I}^{ + } = \inf {E}^{ + } \) and \( {I}^{ - } = \sup {E}^{ - } \) exist. We always have \( {I}^{ - } \leq {I}^{ + } \). If \( {I}^{ - } = {I}^{ + }, f \) is said to be Riemann-integrable, and the real number \( {\int }_{{\mathbb{R}}^{n}}f\left( x\right) {dx} = {I}^{ - } = {I}^{ + } \) is called the integral of \( f \) over \( {\mathbb{R}}^{n} \).

Remarque 1. Lorsque \( n = 1 \) et que \( f \) est continue par morceaux, cette dernière définition de l’intégrale est cohérente avec celle d’une fonction à variable réelle. Pour tout \( n \in {\mathbb{N}}^{ * } \) , elle est également cohérente avec l'intégrale d'une fonction en escalier définie plus haut.

> Remark 1. When \( n = 1 \) and \( f \) is piecewise continuous, this latest definition of the integral is consistent with that of a function of a real variable. For all \( n \in {\mathbb{N}}^{ * } \), it is also consistent with the integral of a step function defined above.

L’intégrale de \( f \) est parfois notée \( \int \cdots {\int }_{{\mathbb{R}}^{n}}f\left( {{x}_{1},\ldots ,{x}_{n}}\right) d{x}_{1}\cdots d{x}_{n} \) (avec \( n \) signes d’inté- gration).

> The integral of \( f \) is sometimes denoted \( \int \cdots {\int }_{{\mathbb{R}}^{n}}f\left( {{x}_{1},\ldots ,{x}_{n}}\right) d{x}_{1}\cdots d{x}_{n} \) (with \( n \) integration signs).

##### Measurable sets, integral over a measurable set.

*Français : Ensembles mesurables, intégrale sur un ensemble mesurable.*

DéFINITION 4. Une partie bornée \( A \) de \( {\mathbb{R}}^{n} \) est dite mesurable si \( {\chi }_{A} \) est Riemann-intégrable. On appelle alors mesure de \( A \) le réel mes \( \left( A\right) = {\int }_{{\mathbb{R}}^{n}}{\chi }_{A}\left( x\right) {dx} \) .

> DEFINITION 4. A bounded subset \( A \) of \( {\mathbb{R}}^{n} \) is said to be measurable if \( {\chi }_{A} \) is Riemann-integrable. The real number mes \( \left( A\right) = {\int }_{{\mathbb{R}}^{n}}{\chi }_{A}\left( x\right) {dx} \) is then called the measure of \( A \).

Remarque 2. Si \( n = 2, A \) est dite quarrable, et mes \( \left( A\right) \) est appelé l’aire de \( A \) . Si \( n = 3, A \) est dite cubable, et mes \( \left( A\right) \) est appelé le volume de \( A \) .

> Remark 2. If \( n = 2, A \) is said to be squarable, and mes \( \left( A\right) \) is called the area of \( A \). If \( n = 3, A \) is said to be cubable, and mes \( \left( A\right) \) is called the volume of \( A \).

Exemple 1. - Tout pavé de \( {\mathbb{R}}^{n} \) est mesurable.

> Example 1. - Every block in \( {\mathbb{R}}^{n} \) is measurable.

- Une partie bornée \( A \) de \( {\mathbb{R}}^{2} \) est dite élémentaire si elle admet les deux définitions suivantes

> - A bounded subset \( A \) of \( {\mathbb{R}}^{2} \) is said to be elementary if it satisfies the following two definitions

\[
A = \left\{  {\left( {x, y}\right)  \in  {\mathbb{R}}^{2} : a \leq  x \leq  b,{\varphi }_{1}\left( x\right)  \leq  y \leq  {\varphi }_{2}\left( x\right) }\right\}
\]

\[
A = \left\{  {\left( {x, y}\right)  \in  {\mathbb{R}}^{2} : c \leq  y \leq  d,{\psi }_{1}\left( x\right)  \leq  x \leq  {\psi }_{2}\left( x\right) }\right\}
\]

où \( \left\lbrack {a, b}\right\rbrack \) et \( \left\lbrack {c, d}\right\rbrack \) sont deux segments de \( \mathbb{R} \) et \( {\varphi }_{1},{\varphi }_{2},{\psi }_{1} \) et \( {\psi }_{2} \) sont des fonctions continues, vérifiant \( {\varphi }_{1} < {\varphi }_{2} \) sur \( \rbrack a, b\left\lbrack {\text{ et }{\psi }_{1} < {\psi }_{2}\text{ sur }}\right\rbrack c, d\lbrack \) . Une partie de \( {\mathbb{R}}^{2} \) est dite simple si elle est la réunion finie de parties élémentaires dont les intérieurs sont deux à deux disjoints. Toute partie élémentaire, toute partie simple de \( {\mathbb{R}}^{2} \) , est mesurable.

> where \( \left\lbrack {a, b}\right\rbrack \) and \( \left\lbrack {c, d}\right\rbrack \) are two segments of \( \mathbb{R} \) and \( {\varphi }_{1},{\varphi }_{2},{\psi }_{1} \) and \( {\psi }_{2} \) are continuous functions, satisfying \( {\varphi }_{1} < {\varphi }_{2} \) on \( \rbrack a, b\left\lbrack {\text{ et }{\psi }_{1} < {\psi }_{2}\text{ sur }}\right\rbrack c, d\lbrack \) . A subset of \( {\mathbb{R}}^{2} \) is said to be simple if it is the finite union of elementary subsets whose interiors are pairwise disjoint. Every elementary subset, every simple subset of \( {\mathbb{R}}^{2} \) , is measurable.

- Une partie \( A \) de \( {\mathbb{R}}^{n} \) est dite négligeable (au sens de Riemann) si \( A \) est mesurable et si mes \( \left( A\right)  = 0 \) . On peut montrer qu’une partie bornée \( A \) de \( {\mathbb{R}}^{n} \) est mesurable si et seulement si sa frontière \( \operatorname{Fr}\left( A\right) \) est négligeable. On peut en déduire le résultat suivant :

> - A subset \( A \) of \( {\mathbb{R}}^{n} \) is said to be negligible (in the Riemann sense) if \( A \) is measurable and if mes \( \left( A\right)  = 0 \) . It can be shown that a bounded subset \( A \) of \( {\mathbb{R}}^{n} \) is measurable if and only if its boundary \( \operatorname{Fr}\left( A\right) \) is negligible. From this, we can deduce the following result:

Si \( \varphi \) est un \( {\mathcal{C}}^{1} \) -difféomorphisme de \( U \subset {\mathbb{R}}^{n} \) sur \( \varphi \left( U\right) \) (où \( U \) est un ouvert de \( \left. {\mathbb{R}}^{n}\right) \) , si \( A \) est mesurable et si \( \bar{A} \subset U \) , alors \( \varphi \left( A\right) \) est mesurable.

> If \( \varphi \) is a \( {\mathcal{C}}^{1} \) -diffeomorphism from \( U \subset {\mathbb{R}}^{n} \) onto \( \varphi \left( U\right) \) (where \( U \) is an open set of \( \left. {\mathbb{R}}^{n}\right) \) , if \( A \) is measurable and if \( \bar{A} \subset U \) , then \( \varphi \left( A\right) \) is measurable.

Par exemple, tout disque du plan, toute sphère de \( {\mathbb{R}}^{n} \) est mesurable.

> For example, every disk in the plane, every sphere in \( {\mathbb{R}}^{n} \) is measurable.

Nous nous limiterons désormais aux cas des fonctions continues sur les ensembles mesurables compacts.

> We will henceforth limit ourselves to the case of continuous functions on compact measurable sets.

DéFINITION 5. Soit \( A \subset {\mathbb{R}}^{n} \) un ensemble mesurable compact et \( f : A \rightarrow \mathbb{R} \) une application continue. Le prolongement \( \widetilde{f} \) de \( f \) à \( {\mathbb{R}}^{n} \) (obtenu en posant \( \widetilde{f}\left( x\right) = f\left( x\right) \) si \( x \in A, = 0 \) sinon) est Riemann-intégrable, et on appelle intégrale de \( f \) le réel \( {\int }_{A}f\left( x\right) {dx} = {\int }_{{\mathbb{R}}^{n}}\widetilde{f}\left( x\right) {dx} \) .

> DEFINITION 5. Let \( A \subset {\mathbb{R}}^{n} \) be a compact measurable set and \( f : A \rightarrow \mathbb{R} \) a continuous mapping. The extension \( \widetilde{f} \) of \( f \) to \( {\mathbb{R}}^{n} \) (obtained by setting \( \widetilde{f}\left( x\right) = f\left( x\right) \) if \( x \in A, = 0 \) otherwise) is Riemann-integrable, and the real number \( {\int }_{A}f\left( x\right) {dx} = {\int }_{{\mathbb{R}}^{n}}\widetilde{f}\left( x\right) {dx} \) is called the integral of \( f \).

Propriétés élémentaires. Les intégrales multiples possèdent les mêmes propriétés que les intégrales simples. Nous désignons par \( A \) un ensemble mesurable compact de \( {\mathbb{R}}^{n} \) .

> Elementary properties. Multiple integrals possess the same properties as simple integrals. We denote by \( A \) a compact measurable set of \( {\mathbb{R}}^{n} \).

(i) Linéarité. L’ensemble \( \mathcal{C}\left( {A,\mathbb{R}}\right) \) des fonctions continues de \( A \) dans \( \mathbb{R} \) est un \( \mathbb{R} \) -e.v et l’application \( \mathcal{C}\left( {A,\mathbb{R}}\right) \rightarrow \mathbb{R}\;f \mapsto {\int }_{A}f\left( x\right) {dx} \) est linéaire.

> (i) Linearity. The set \( \mathcal{C}\left( {A,\mathbb{R}}\right) \) of continuous functions from \( A \) to \( \mathbb{R} \) is a \( \mathbb{R} \) -v.s. and the mapping \( \mathcal{C}\left( {A,\mathbb{R}}\right) \rightarrow \mathbb{R}\;f \mapsto {\int }_{A}f\left( x\right) {dx} \) is linear.

(ii) Positivité. Si \( f \geq 0 \) , alors \( {\int }_{A}f\left( x\right) {dx} \geq 0 \) ; si \( f \leq g,{\int }_{A}f\left( x\right) {dx} \leq {\int }_{A}g\left( x\right) {dx} \) .

> (ii) Positivity. If \( f \geq 0 \) , then \( {\int }_{A}f\left( x\right) {dx} \geq 0 \) ; if \( f \leq g,{\int }_{A}f\left( x\right) {dx} \leq {\int }_{A}g\left( x\right) {dx} \) .

(iii) On a \( \left| {{\int }_{A}f\left( x\right) {dx}}\right| \leq {\int }_{A}\left| {f\left( x\right) }\right| {dx} \) .

> (iii) We have \( \left| {{\int }_{A}f\left( x\right) {dx}}\right| \leq {\int }_{A}\left| {f\left( x\right) }\right| {dx} \) .

(iv) Relation de Chasles. Si A et \( B \) sont des compacts mesurables, \( A \cup B \) et \( A \cap B \) sont des compacts mesurables. Si de plus mes \( \left( {A \cap B}\right) = 0 \) , toute fonction \( f \) continue sur \( A \cup B \) vérifie \( {\int }_{A \cup B}f\left( x\right) {dx} = {\int }_{A}f\left( x\right) {dx} + {\int }_{B}f\left( x\right) {dx}. \)

> (iv) Chasles' relation. If A and \( B \) are compact measurable sets, \( A \cup B \) and \( A \cap B \) are compact measurable sets. If, furthermore, mes \( \left( {A \cap B}\right) = 0 \) , any function \( f \) continuous on \( A \cup B \) satisfies \( {\int }_{A \cup B}f\left( x\right) {dx} = {\int }_{A}f\left( x\right) {dx} + {\int }_{B}f\left( x\right) {dx}. \)

Remarque 3. On peut également définir l’intégrale multiple d’une fonction continue \( f \) à valeurs dans un e.v \( E \) de dimension finie. Si \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) est une base de \( E \) , on écrit \( f = \; \sum {f}_{i}{e}_{i} \) où les \( {f}_{i} \) sont à valeurs réelles, et l’intégrale multiple de \( f \) est \( {\int }_{A}f = \mathop{\sum }\limits_{i}\left( {{\int }_{A}{f}_{i}}\right) {e}_{i} \) . Cette définition est indépendante de la base de \( E \) choisie. En particulier, si \( f = {f}_{1} + i{f}_{2} \) est à valeurs complexes, alors \( {\int }_{A}f = {\int }_{A}{f}_{1} + i\left( {{\int }_{A}{f}_{2}}\right) \) .

> Remark 3. One can also define the multiple integral of a continuous function \( f \) with values in a finite-dimensional v.s. \( E \) . If \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) is a basis of \( E \) , we write \( f = \; \sum {f}_{i}{e}_{i} \) where the \( {f}_{i} \) are real-valued, and the multiple integral of \( f \) is \( {\int }_{A}f = \mathop{\sum }\limits_{i}\left( {{\int }_{A}{f}_{i}}\right) {e}_{i} \) . This definition is independent of the chosen basis of \( E \) . In particular, if \( f = {f}_{1} + i{f}_{2} \) is complex-valued, then \( {\int }_{A}f = {\int }_{A}{f}_{1} + i\left( {{\int }_{A}{f}_{2}}\right) \) .
