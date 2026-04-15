#### 4.2. Integral asymptotics

*Français : 4.2. Équivalents d'intégrales*

Intégration des relations de comparaison. Le théorème qui suit complète le résultat de la proposition 5 de la page 149.

> Integration of comparison relations. The following theorem completes the result of proposition 5 on page 149.

\( \rightarrow \) THÉORÉME 3. Soient [a, b[ un intervalle semi-ouvert de \( \mathbb{R} \) (avec \( - \infty < a < b \leq + \infty \) ), E un \( \mathbb{R} \) -espace de Banach, \( f : \left\lbrack {a, b\left\lbrack { \rightarrow E}\right. }\right. \) et \( g : \left\lbrack {a, b\left\lbrack { \rightarrow {\mathbb{R}}^{+ * }}\right. }\right. \) deux applications continues par morceaux sur \( \lbrack a, b\lbrack \) .

> \( \rightarrow \) THEOREM 3. Let [a, b[ be a semi-open interval of \( \mathbb{R} \) (with \( - \infty < a < b \leq + \infty \) ), E a Banach \( \mathbb{R} \) -space, \( f : \left\lbrack {a, b\left\lbrack { \rightarrow E}\right. }\right. \) and \( g : \left\lbrack {a, b\left\lbrack { \rightarrow {\mathbb{R}}^{+ * }}\right. }\right. \) two piecewise continuous mappings on \( \lbrack a, b\lbrack \) .

(i) Si l’intégrale \( {\int }_{a}^{b}g\left( t\right) \) diverge, alors lorsque \( x \rightarrow {b}^{ - } \) ,

> (i) If the integral \( {\int }_{a}^{b}g\left( t\right) \) diverges, then as \( x \rightarrow {b}^{ - } \) ,

\[
\text{ - la relation }f = O\left( g\right) \text{ entraîne }{\int }_{a}^{x}f\left( t\right) {dt} = O\left( {{\int }_{a}^{x}g\left( t\right) {dt}}\right) \text{ , }
\]

\[
\text{ - la relation }f = o\left( g\right) \text{ entraîne }{\int }_{a}^{x}f\left( t\right) {dt} = o\left( {{\int }_{a}^{x}g\left( t\right) {dt}}\right) \text{ , }
\]

\[
\text{ - la relation }f \sim  g\text{ entraîne }{\int }_{a}^{x}f\left( t\right) {dt} \sim  {\int }_{a}^{x}g\left( t\right) {dt}\text{ . }
\]

(ii) Si l’intégrale \( {\int }_{a}^{b}g\left( t\right) {dt} \) converge, alors lorsque \( x \rightarrow {b}^{ - } \) ,

> (ii) If the integral \( {\int }_{a}^{b}g\left( t\right) {dt} \) converges, then as \( x \rightarrow {b}^{ - } \) ,

\[
\text{ - la relation }f = O\left( g\right) \text{ entraîne }{\int }_{x}^{b}f\left( t\right) {dt} = O\left( {{\int }_{x}^{b}g\left( t\right) {dt}}\right) \text{ , }
\]

\[
\text{ - la relation }f = o\left( g\right) \text{ entraîne }{\int }_{x}^{b}f\left( t\right) {dt} = o\left( {{\int }_{x}^{b}g\left( t\right) {dt}}\right) \text{ , }
\]

\[
\text{ - la relation }f \sim  g\text{ entraîne }{\int }_{x}^{b}f\left( t\right) {dt} \sim  {\int }_{x}^{b}g\left( t\right) {dt}\text{ . }
\]

Démonstration. Montrons la première assertion de (i). Si \( f = O\left( g\right) \) , alors

> Proof. Let us show the first assertion of (i). If \( f = O\left( g\right) \) , then

\[
\exists c \in  \rbrack a, b\lbrack ,\exists M > 0,\forall t \in  \lbrack c, b\lbrack ,\;\parallel f\left( t\right) \parallel  \leq  {Mg}\left( t\right) .
\]

Ainsi,

> Thus,

\[
\forall x \in  \lbrack c, b\lbrack ,\;\begin{Vmatrix}{{\int }_{c}^{x}f\left( t\right) {dt}}\end{Vmatrix} \leq  M{\int }_{c}^{x}g\left( t\right) {dt}.
\]

Or \( {\int }_{a}^{b}g\left( t\right) {dt} \) diverge, donc il existe \( d \in \lbrack c, b\lbrack \) tel que \( \parallel {\int }_{a}^{c}f\left( t\right) {dt}\parallel \leq {\int }_{a}^{d}g\left( t\right) {dt} \) . On a donc

> However, \( {\int }_{a}^{b}g\left( t\right) {dt} \) diverges, so there exists \( d \in \lbrack c, b\lbrack \) such that \( \parallel {\int }_{a}^{c}f\left( t\right) {dt}\parallel \leq {\int }_{a}^{d}g\left( t\right) {dt} \) . We therefore have

\[
\forall x \in  \lbrack d, b\lbrack ,\;\begin{Vmatrix}{{\int }_{a}^{x}f\left( t\right) {dt}}\end{Vmatrix} \leq  {\int }_{a}^{d}g\left( t\right) {dt} + M{\int }_{c}^{x}g\left( t\right) {dt} \leq  \left( {M + 1}\right) {\int }_{a}^{x}g\left( t\right) {dt},
\]

d'où le premier résultat.

> whence the first result.

Prouvons maintenant la seconde assertion de (i). Donnons nous \( \varepsilon > 0 \) . D'après les hypothèses,

> Let us now prove the second assertion of (i). Let \( \varepsilon > 0 \) be given. According to the hypotheses,

\[
\exists c \in  \rbrack a, b\lbrack ,\forall t \in  \lbrack c, b\lbrack ,\;\parallel f\left( t\right) \parallel  \leq  {\varepsilon g}\left( t\right) .
\]

Ainsi,

> Thus,

\[
\forall x \in  \lbrack c, b\lbrack ,\;\begin{Vmatrix}{{\int }_{c}^{x}f\left( t\right) {dt}}\end{Vmatrix} \leq  \varepsilon {\int }_{c}^{x}g\left( t\right) {dt}.
\]

Or \( {\int }_{a}^{b}g\left( t\right) {dt} \) diverge, donc il existe \( d \in \lbrack c, b\lbrack \) tel que \( \begin{Vmatrix}{{\int }_{a}^{c}f\left( t\right) {dt}}\end{Vmatrix} \leq \varepsilon {\int }_{a}^{d}g\left( t\right) {dt} \) . On a donc

> However, \( {\int }_{a}^{b}g\left( t\right) {dt} \) diverges, so there exists \( d \in \lbrack c, b\lbrack \) such that \( \begin{Vmatrix}{{\int }_{a}^{c}f\left( t\right) {dt}}\end{Vmatrix} \leq \varepsilon {\int }_{a}^{d}g\left( t\right) {dt} \) . We therefore have

\[
\forall x \in  \lbrack d, b\lbrack ,\;\begin{Vmatrix}{{\int }_{a}^{x}f\left( t\right) {dt}}\end{Vmatrix} \leq  \varepsilon {\int }_{a}^{d}g\left( t\right) {dt} + \varepsilon {\int }_{c}^{x}g\left( t\right) {dt} \leq  {2\varepsilon }{\int }_{a}^{x}g\left( t\right) {dt},
\]

d'où le second résultat.

> whence the second result.

Si \( f \sim g \) et toujours sous les hypothèses de (i), la troisième assertion se montre en écrivant \( f - g = o\left( g\right) \) et en utilisant le résultat précédent.

> If \( f \sim g \) and still under the hypotheses of (i), the third assertion is shown by writing \( f - g = o\left( g\right) \) and using the previous result.

Les assertions de (ii) se montrent de manière analogue (et c'est plus facile).

> The assertions of (ii) are shown in an analogous manner (and it is easier).

Exemple 1. Au voisinage de \( + \infty \) , on a pour tout \( \alpha > 0 \)

> Example 1. In the neighborhood of \( + \infty \) , we have for all \( \alpha > 0 \)

\[
\frac{1}{x} = o\left( \frac{1}{{x}^{1 - \alpha }}\right) \;\text{ donc }\;\log x = {\int }_{1}^{x}\frac{dt}{t} = o\left( {{\int }_{1}^{x}{t}^{\alpha  - 1}{dt}}\right)  = o\left( {x}^{\alpha }\right) .
\]

Méthode de Laplace. Nous allons donner un résultat général sur les équivalents d'inté- grales dont l'intégrande dépend d'un paramètre, qui s'applique aux intégrales de la forme

> Laplace's method. We will provide a general result on the equivalents of integrals whose integrand depends on a parameter, which applies to integrals of the form

\[
I\left( t\right)  = {\int }_{0}^{+\infty }g\left( x\right) {e}^{{th}\left( x\right) }{dx}\;\text{ lorsque }\;t \rightarrow   + \infty .
\]

La démarche utilisée s'appelle la méthode de Laplace. Elle ne figure pas au programme des classes préparatoires, mais les techniques utilisées sont instructives et permettent de résoudre les nombreux exercices derrière lesquels se cache cette méthode.

> The approach used is called Laplace's method. It is not in the preparatory classes curriculum, but the techniques used are instructive and allow for solving the many exercises behind which this method is hidden.

Commençons par l'examen d'un cas particulier.

> Let us begin by examining a special case.

LEMME 1. Soient \( \alpha > - 1,\beta > 0, c > 0 \) et b vérifiant \( 0 < b \leq + \infty \) . Alors lorsque \( t \rightarrow + \infty \) ,

> LEMMA 1. Let \( \alpha > - 1,\beta > 0, c > 0 \) and b satisfy \( 0 < b \leq + \infty \) . Then as \( t \rightarrow + \infty \) ,

\[
J\left( t\right)  = {\int }_{0}^{b}{x}^{\alpha }{e}^{-{tc}{x}^{\beta }}{dx} \sim  \frac{1}{\beta }\Gamma \left( \frac{\alpha  + 1}{\beta }\right) {\left( ct\right) }^{-\left( {\alpha  + 1}\right) /\beta },
\]

où la fonction \( \Gamma \) est définie page 162.

> where the function \( \Gamma \) is defined on page 162.

Démonstration. Il suffit d’effectuer le changement de variable \( u = {tc}{x}^{\beta } \) , ce qui donne

> Proof. It suffices to perform the change of variable \( u = {tc}{x}^{\beta } \), which gives

\[
J\left( t\right)  = \frac{1}{\beta }{\left( ct\right) }^{-\left( {\alpha  + 1}\right) /\beta }{\int }_{0}^{c{b}^{\beta }t}{u}^{\left( {\alpha  + 1}\right) /\beta  - 1}{e}^{-u}{du},
\]

d’où le résultat lorsque \( t \rightarrow + \infty \) .

> whence the result when \( t \rightarrow + \infty \).

Nous pouvons maintenant énoncer le résultat principal de cette sous-partie.

> We can now state the main result of this subsection.

THÉORÉME 4. Soient \( g \) et \( h : \rbrack 0, + \infty \lbrack \rightarrow \mathbb{R} \) deux applications continues par morceaux vérifiant

> THEOREM 4. Let \( g \) and \( h : \rbrack 0, + \infty \lbrack \rightarrow \mathbb{R} \) be two piecewise continuous mappings satisfying

(i) la fonction \( x \mapsto g\left( x\right) {e}^{h\left( x\right) } \) est intégrable sur \( {\mathbb{R}}^{ + } \) ,

> (i) the function \( x \mapsto g\left( x\right) {e}^{h\left( x\right) } \) is integrable on \( {\mathbb{R}}^{ + } \),

(ii) \( \exists {\delta }_{0} > 0,\forall \delta \in \rbrack 0,{\delta }_{0}\left\lbrack {,\forall x \geq \delta ,\;h\left( x\right) \leq h\left( \delta \right) ,}\right. \)

> (ii) \( \exists {\delta }_{0} > 0,\forall \delta \in \rbrack 0,{\delta }_{0}\left\lbrack {,\forall x \geq \delta ,\;h\left( x\right) \leq h\left( \delta \right) ,}\right. \)

(iii) Lorsque \( x \rightarrow {0}^{ + } \) , on a

> (iii) As \( x \rightarrow {0}^{ + } \), we have

\[
g\left( x\right)  \sim  A{x}^{\alpha }\;\left( {\alpha  >  - 1}\right) \;\text{ et }\;h\left( x\right)  = a - c{x}^{\beta } + o\left( {x}^{\beta }\right) \;\left( {c > 0,\beta  > 0}\right) .
\]

Alors lorsque \( t \rightarrow + \infty \) , on a

> Then as \( t \rightarrow + \infty \), we have

\[
I\left( t\right)  = {\int }_{0}^{+\infty }g\left( x\right) {e}^{{th}\left( x\right) }{dx} \sim  \frac{A}{\beta }\Gamma \left( \frac{\alpha  + 1}{\beta }\right) {e}^{at}{\left( ct\right) }^{-\left( {\alpha  + 1}\right) /\beta }.
\]

Démonstration. Multipliant par \( {e}^{-{at}}/A \) , on peut déjà supposer \( a = 0 \) et \( A = 1 \) . Posons d’abord, pour simplifier l'écriture,

> Proof. Multiplying by \( {e}^{-{at}}/A \), we can already assume \( a = 0 \) and \( A = 1 \). Let us first set, to simplify the notation,

\[
\varphi \left( t\right)  = \frac{1}{\beta }\Gamma \left( \frac{\alpha  + 1}{\beta }\right) {\left( ct\right) }^{-\left( {\alpha  + 1}\right) /\beta }.
\]

Nous allons, pour \( \varepsilon \in \rbrack 0,1\left\lbrack \right. \) , montrer successivement

> We are going to show, for \( \varepsilon \in \rbrack 0,1\left\lbrack \right. \), successively

(i) \( \exists \delta \in \rbrack 0,{\delta }_{0}\left\lbrack {,\exists {t}_{1} > 0}\right. \) tels que, pour tout \( t \geq {t}_{1} \) ,

> (i) \( \exists \delta \in \rbrack 0,{\delta }_{0}\left\lbrack {,\exists {t}_{1} > 0}\right. \) such that, for all \( t \geq {t}_{1} \),

\[
{\left( 1 - \varepsilon \right) }^{2}{\left( 1 + \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta }\varphi \left( t\right)  \leq  {\int }_{0}^{\delta }g\left( x\right) {e}^{{th}\left( x\right) }{dx} \leq  {\left( 1 + \varepsilon \right) }^{2}{\left( 1 - \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta }\varphi \left( t\right) ;
\]

(ii) \( \delta > 0 \) et \( {t}_{1} \) étant ainsi fixés, déterminer \( {t}_{2} > 0 \) tel que

> (ii) \( \delta > 0 \) and \( {t}_{1} \) being thus fixed, determine \( {t}_{2} > 0 \) such that

\[
\forall t \geq  {t}_{2},\;{\int }_{\delta }^{+\infty }\left| {g\left( x\right) }\right| {e}^{{th}\left( x\right) }{dx} \leq  {\varepsilon \varphi }\left( t\right) .
\]

On en conclura que pour tout \( t \geq \sup \left\{ {{t}_{1},{t}_{2}}\right\} \) , on a

> We will conclude that for all \( t \geq \sup \left\{ {{t}_{1},{t}_{2}}\right\} \), we have

\[
\left( {{\left( 1 - \varepsilon \right) }^{2}{\left( 1 + \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta } - \varepsilon }\right) \varphi \left( t\right)  \leq  I\left( t\right)  \leq  \left( {{\left( 1 + \varepsilon \right) }^{2}{\left( 1 - \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta } + \varepsilon }\right) \varphi \left( t\right) ,
\]

ce qui, en vertu de la continuité des fonctions de \( \varepsilon \) qui interviennent, prouvera le théorème.

> which, by virtue of the continuity of the functions of \( \varepsilon \) involved, will prove the theorem.

1. Par hypothèse, il existe \( \delta \in \rbrack 0,{\delta }_{0}\lbrack \) tel que

> 1. By hypothesis, there exists \( \delta \in \rbrack 0,{\delta }_{0}\lbrack \) such that

\[
\forall x \in  \rbrack 0,\delta \rbrack ,\;\left\{  {\begin{matrix} \left( {1 - \varepsilon }\right) {x}^{\alpha } &  \leq  g\left( x\right)  \leq  \;\left( {1 + \varepsilon }\right) {x}^{\alpha } \\   - c\left( {1 + \varepsilon }\right) {x}^{\beta } &  \leq  h\left( x\right)  \leq   - c\left( {1 - \varepsilon }\right) {x}^{\beta } \end{matrix},}\right.
\]

donc

> therefore

\[
\left( {1 - \varepsilon }\right) {\int }_{0}^{\delta }{x}^{\alpha }{e}^{-c\left( {1 + \varepsilon }\right) t{x}^{\beta }}{dx} \leq  {\int }_{0}^{\delta }g\left( x\right) {e}^{{th}\left( x\right) }{dx} \leq  \left( {1 + \varepsilon }\right) {\int }_{0}^{\delta }{x}^{\alpha }{e}^{-c\left( {1 - \varepsilon }\right) t{x}^{\beta }}{dx}.
\]

(*)

> Le nombre \( \delta \) étant fixé, on sait d’après le lemme 1 que les deux membres extrêmes de (*) on respectivement pour équivalent, lorsque \( t \rightarrow + \infty \)

With \( \delta \) fixed, we know from Lemma 1 that the two extreme members of (*) have as an equivalent, as \( t \rightarrow + \infty \)

\[
\frac{1 - \varepsilon }{\beta }\Gamma \left( \frac{\alpha  + 1}{\beta }\right) {\left( c\left( 1 + \varepsilon \right) t\right) }^{-\left( {\alpha  + 1}\right) /\beta } = \left( {1 - \varepsilon }\right) {\left( 1 + \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta }\varphi \left( t\right)
\]

et

\[
\frac{1 + \varepsilon }{\beta }\Gamma \left( \frac{\alpha  + 1}{\beta }\right) {\left( c\left( 1 - \varepsilon \right) t\right) }^{-\left( {\alpha  + 1}\right) /\beta } = \left( {1 + \varepsilon }\right) {\left( 1 - \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta }\varphi \left( t\right) .
\]

Par définition d’un équivalent, il existe donc \( {t}_{1} > 0 \) tel que pour tout \( t \geq {t}_{1} \) , on ait

> By the definition of an equivalent, there therefore exists \( {t}_{1} > 0 \) such that for all \( t \geq {t}_{1} \), we have

\[
\left( {1 - \varepsilon }\right) {\int }_{0}^{\delta }{x}^{\alpha }{e}^{-c\left( {1 + \varepsilon }\right) t{x}^{\beta }}{dx} \geq  \left( {1 - \varepsilon }\right) \left\lbrack  {\left( {1 - \varepsilon }\right) {\left( 1 + \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta }\varphi \left( t\right) }\right\rbrack
\]

et

\[
\left( {1 + \varepsilon }\right) {\int }_{0}^{\delta }{x}^{\alpha }{e}^{-c\left( {1 - \varepsilon }\right) t{x}^{\beta }}{dx} \geq  \left( {1 + \varepsilon }\right) \left\lbrack  {\left( {1 + \varepsilon }\right) {\left( 1 - \varepsilon \right) }^{-\left( {\alpha  + 1}\right) /\beta }\varphi \left( t\right) }\right\rbrack  .
\]

Il est donc clair, d’après (*), que l’on a (i) pour tout \( t \geq {t}_{1} \) .

> It is therefore clear, from (*), that we have (i) for all \( t \geq {t}_{1} \).

2. Posons \( h\left( \delta \right) = - \mu < 0 \) . D’après les hypothèses, on a \( h\left( x\right) + \mu \leq 0 \) pour tout \( x \geq \delta \) , donc

> 2. Let \( h\left( \delta \right) = - \mu < 0 \). According to the hypotheses, we have \( h\left( x\right) + \mu \leq 0 \) for all \( x \geq \delta \), therefore

\[
\forall x \geq  \delta ,\forall t > 1,\;{th}\left( x\right)  = \left( {t - 1}\right) h\left( x\right)  + h\left( x\right)  \leq   - \left( {t - 1}\right) \mu  + h\left( x\right)
\]

ce qui entraîne la convergence de \( {\int }_{\delta }^{+\infty }\left| {g\left( x\right) }\right| {e}^{{th}\left( x\right) }{dx} \) et l’inégalité

> which entails the convergence of \( {\int }_{\delta }^{+\infty }\left| {g\left( x\right) }\right| {e}^{{th}\left( x\right) }{dx} \) and the inequality

\[
{\int }_{\delta }^{+\infty }\left| {g\left( x\right) }\right| {e}^{{th}\left( x\right) }{dx} \leq  {e}^{-\left( {t - 1}\right) \mu }{\int }_{\delta }^{+\infty }\left| {g\left( x\right) }\right| {e}^{h\left( x\right) }{dx}.
\]

Or \( \mu > 0 \) , d’où l’existence d’un réel \( {t}_{2} > 0 \) pour lequel on a (ii).

> However \( \mu > 0 \), hence the existence of a real \( {t}_{2} > 0 \) for which we have (ii).

Remarque 3. Le cas d’intégrales de la forme \( {\int }_{0}^{b}g\left( x\right) {e}^{{th}\left( x\right) }{dx} \) avec \( 0 < b < + \infty \) , lorsque \( g \) et \( h \) sont continues par morceaux sur \( \rbrack 0, b\rbrack \) , se ramène au cas du théorème en prolongeant \( g \) et \( h \) sur \( \rbrack 0, + \infty \lbrack \) par \( g\left( x\right) = 0 \) et \( h\left( x\right) = a - 1 \) pour \( x > b \) .

> Remark 3. The case of integrals of the form \( {\int }_{0}^{b}g\left( x\right) {e}^{{th}\left( x\right) }{dx} \) with \( 0 < b < + \infty \), when \( g \) and \( h \) are piecewise continuous on \( \rbrack 0, b\rbrack \), reduces to the case of the theorem by extending \( g \) and \( h \) on \( \rbrack 0, + \infty \lbrack \) by \( g\left( x\right) = 0 \) and \( h\left( x\right) = a - 1 \) for \( x > b \).

Le cas typique d'application du théorème précédent fait l'objet du corollaire qui suit.

> The typical case of application of the previous theorem is the subject of the following corollary.

COROLLAIRE 2. Soient \( g \) et \( h \) deux fonctions réelles de classe \( {\mathcal{C}}^{2} \) sur \( \rbrack a, b\lbrack ( \) avec \( - \infty \leq \; a < b \leq + \infty ) \) telles que

> COROLLARY 2. Let \( g \) and \( h \) be two real functions of class \( {\mathcal{C}}^{2} \) on \( \rbrack a, b\lbrack ( \) with \( - \infty \leq \; a < b \leq + \infty ) \) such that

(i) La fonction \( x \mapsto g\left( x\right) {e}^{h\left( x\right) } \) est intégrable sur \( \rbrack a, b\lbrack \) ,

> (i) The function \( x \mapsto g\left( x\right) {e}^{h\left( x\right) } \) is integrable on \( \rbrack a, b\lbrack \),

(ii) \( {h}^{\prime } \) ne change de signe qu’en un seul point \( c \in \rbrack a, b\left\lbrack \right. \) où de plus h atteint son maximum et où \( g\left( c\right) \neq 0,{h}^{\prime \prime }\left( c\right) < 0 \) .

> (ii) \( {h}^{\prime } \) only changes sign at a single point \( c \in \rbrack a, b\left\lbrack \right. \) where, moreover, h reaches its maximum and where \( g\left( c\right) \neq 0,{h}^{\prime \prime }\left( c\right) < 0 \).

Alors lorsque \( t \rightarrow + \infty \) , on a

> Then when \( t \rightarrow + \infty \), we have

\[
{\int }_{a}^{b}g\left( x\right) {e}^{{th}\left( x\right) }{dx} \sim  \Gamma \left( \frac{1}{2}\right) g\left( c\right) {e}^{{th}\left( c\right) }\sqrt{\frac{2}{-t{h}^{\prime \prime }\left( c\right) }}.
\]

Démonstration. On coupe l’intégrale en deux : \( {\int }_{a}^{b} = {\int }_{a}^{c} + {\int }_{c}^{b} \) , puis on ramène \( c \) à 0 en effectuant un changement de variable affine. On utilise ensuite le théorème précédent. Pour chacun des deux cas, on a ici

> Proof. We split the integral into two: \( {\int }_{a}^{b} = {\int }_{a}^{c} + {\int }_{c}^{b} \), then we reduce \( c \) to 0 by performing an affine change of variable. We then use the previous theorem. For each of the two cases, we have here

\[
\alpha  = 0,\;A = g\left( c\right) ,\;\beta  = 2,\;c =  - \frac{{h}^{\prime \prime }\left( c\right) }{2},\;a = h\left( c\right) ,
\]

et l'équivalent est le double de celui du théorème précédent (il y a deux intégrales).

> and the equivalent is double that of the previous theorem (there are two integrals).

Remarque 4. On peut utiliser la valeur \( \Gamma \left( {1/2}\right) = \sqrt{\pi } \) dans le corollaire précédent.

> Remark 4. One can use the value \( \Gamma \left( {1/2}\right) = \sqrt{\pi } \) in the previous corollary.

Dans la pratique, l'intégrande n'a pas toujours la forme de celle requise pour appliquer la méthode de Laplace. On effectue souvent un changement de variable pour amener le maximum de la fonction apparaissant dans l'exponentielle à une abscisse fixe puis on applique le corollaire précédent. C'est cette technique qui est utilisée dans l'exemple qui suit.

> In practice, the integrand does not always have the form required to apply Laplace's method. We often perform a change of variable to bring the maximum of the function appearing in the exponential to a fixed abscissa, then apply the previous corollary. This is the technique used in the following example.

Exemple 2. On veut trouver le comportement asymptotique, lorsque \( x \rightarrow + \infty \) , de

> Example 2. We want to find the asymptotic behavior, as \( x \rightarrow + \infty \) , of

\[
\Gamma \left( {x + 1}\right)  = {\int }_{0}^{+\infty }{e}^{x\log t - t}{dt}.
\]

Comme il est dit plus haut, on cherche l’abscisse \( t \) du maximum de la fonction \( h\left( t\right) = \; x\log t - t \) (c’est ce maximum qui va dicter le comportement de \( \Gamma \) en \( + \infty \) ). On a \( {h}^{\prime }\left( t\right) = \; x/t - 1 \) , le maximum est donc atteint en \( t = x \) . Pour se ramener au cas où \( h \) atteint son maximum en une abscisse indépendante de \( x \) , on effectue le changement de variable \( u = t/x \) . On trouve

> As stated above, we look for the abscissa \( t \) of the maximum of the function \( h\left( t\right) = \; x\log t - t \) (it is this maximum that will dictate the behavior of \( \Gamma \) as \( + \infty \) ). We have \( {h}^{\prime }\left( t\right) = \; x/t - 1 \) , so the maximum is reached at \( t = x \) . To reduce it to the case where \( h \) reaches its maximum at an abscissa independent of \( x \) , we perform the change of variable \( u = t/x \) . We find

\[
\Gamma \left( {x + 1}\right)  = {x}^{x + 1}{\int }_{0}^{+\infty }{e}^{x\left( {\log u - u}\right) }{du}.
\]

La fonction \( u \mapsto \log u - u \) atteint son maximum en \( u = 1 \) , et on peut appliquer le corollaire, qui donne

> The function \( u \mapsto \log u - u \) reaches its maximum at \( u = 1 \) , and we can apply the corollary, which gives

\[
\Gamma \left( {x + 1}\right)  \sim  {x}^{x + 1}\Gamma \left( \frac{1}{2}\right) {e}^{-x}\sqrt{\frac{2}{x}} = \sqrt{2\pi }{x}^{x + 1/2}{e}^{-x}.
\]

Ce résultat est connu sous le nom de formule de Stirling. Elle généralise celle obtenue dans l’exercice 3 page 219 pour \( x \) entier (car \( \Gamma \left( {n + 1}\right) = n \) ! pour tout \( n \in {\mathbb{N}}^{ * } \) ).

> This result is known as Stirling's formula. It generalizes the one obtained in exercise 3 on page 219 for \( x \) integer (since \( \Gamma \left( {n + 1}\right) = n \) ! for all \( n \in {\mathbb{N}}^{ * } \) ).

Remarque 5. Dans les exercices qui suivent, on utilisera tels quels les résultats concer-nant la méthode de Laplace. Néanmoins, le jour du concours, il faut être capable de tout redémontrer (en appliquant directement aux fonctions concernées les démonstrations précédentes).

> Remark 5. In the following exercises, we will use the results concerning Laplace's method as they are. Nevertheless, on the day of the competitive exam, you must be able to re-derive everything (by applying the previous proofs directly to the functions concerned).
