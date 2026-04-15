#### 3.1. Definition of an integrable function

*Français : 3.1. Définition d'une fonction intégrable*

DÉFINITION 1. Une fonction est dite continue par morceaux sur \( I \) si elle est continue par morceaux sur tout segment \( J \) inclus dans \( I \) .

> DEFINITION 1. A function is said to be piecewise continuous on \( I \) if it is piecewise continuous on every segment \( J \) included in \( I \) .

##### Integrable positive functions.

*Français : Fonctions positives intégrables.*

\( \rightarrow \) DéFINITION 2 (FONCTION POSITIVE INTÉGRABLE). Soit \( f \) une fonction positive et continue par morceaux sur \( I \) . On dit que \( f \) est intégrable (ou sommable) sur \( I \) si il existe \( M \geq 0 \) tel que, pour tout segment \( J \subset I \) , on a \( {\int }_{J}f \leq M \) . On note alors

> \( \rightarrow \) DEFINITION 2 (INTEGRABLE POSITIVE FUNCTION). Let \( f \) be a positive and piecewise continuous function on \( I \) . We say that \( f \) is integrable (or summable) on \( I \) if there exists \( M \geq 0 \) such that, for every segment \( J \subset I \) , we have \( {\int }_{J}f \leq M \) . We then denote

\[
{\int }_{I}f = \mathop{\sup }\limits_{{J \subset  I}}{\int }_{J}f
\]

Proposition 1. Soit \( f \) positive et continue par morceaux sur I. Alors \( f \) est intégrable si et seulement \( s \) ’il existe une suite croissante de segments \( {J}_{n} = \left\lbrack {{a}_{n},{b}_{n}}\right\rbrack \) inclus dans I telle que \( { \cup }_{n}{J}_{n} = I \) et telle que la suite \( {\int }_{{J}_{n}}f \) soit bornée. Dans ce cas, pour toute suite \( \left( {J}_{n}\right) \) de ce type on a

> Proposition 1. Let \( f \) be positive and piecewise continuous on I. Then \( f \) is integrable if and only if \( s \) there exists an increasing sequence of segments \( {J}_{n} = \left\lbrack {{a}_{n},{b}_{n}}\right\rbrack \) included in I such that \( { \cup }_{n}{J}_{n} = I \) and such that the sequence \( {\int }_{{J}_{n}}f \) is bounded. In this case, for any sequence \( \left( {J}_{n}\right) \) of this type, we have

\[
{\int }_{I}f = \mathop{\sup }\limits_{n}{\int }_{{J}_{n}}f = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{{J}_{n}}f = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{\int }_{{a}_{n}}^{{b}_{n}}f\left( t\right) {dt}.
\]

Exemple 1 (Exemples fondamentaux). — Cas \( b = + \infty , a \in \mathbb{R} \) .

> Example 1 (Fundamental examples). — Case \( b = + \infty , a \in \mathbb{R} \) .

- Pour \( a > 0, t \mapsto  1/{t}^{\alpha } \) est intégrable sur \( \lbrack a, + \infty \lbrack \) si et seulement si \( \alpha  > 1 \) .

> - For \( a > 0, t \mapsto  1/{t}^{\alpha } \) is integrable on \( \lbrack a, + \infty \lbrack \) if and only if \( \alpha  > 1 \) .

- \( t \mapsto  {e}^{-{\lambda t}} \) est intégrable sur \( \lbrack a, + \infty \lbrack \) et seulement si \( \lambda  > 0 \) .

> - \( t \mapsto  {e}^{-{\lambda t}} \) is integrable on \( \lbrack a, + \infty \lbrack \) if and only if \( \lambda  > 0 \) .

- Cas \( a \) et \( b \) finis.

> - Case \( a \) and \( b \) finite.

- La fonction \( t \mapsto  1/{\left( b - t\right) }^{\alpha } \) est intégrable sur \( \left\lbrack  {a, b\left\lbrack  \right. }\right. \) si et seulement si \( \alpha  < 1 \) .

> - The function \( t \mapsto  1/{\left( b - t\right) }^{\alpha } \) is integrable on \( \left\lbrack  {a, b\left\lbrack  \right. }\right. \) if and only if \( \alpha  < 1 \) .

- De même, \( t \mapsto  1/{\left( t - a\right) }^{\alpha } \) est intégrable sur \( \rbrack a, b\rbrack \) et seulement si \( \alpha  < 1 \) .

> - Similarly, \( t \mapsto  1/{\left( t - a\right) }^{\alpha } \) is integrable on \( \rbrack a, b\rbrack \) if and only if \( \alpha  < 1 \) .

##### Integrable functions with arbitrary values.

*Français : Fonctions intégrables à valeurs quelconques.*

\( \rightarrow \) DéFINITION 3 (FONCTION INTÉGRABLE). Une fonction \( f : I \rightarrow E \) continue par morceaux est dite intégrable (ou sommable) sur \( I \) si \( \parallel f\parallel \) est intégrable sur \( I \) . Dans ce cas, pour toute suite croissante \( \left( {J}_{n}\right) \) de segments inclus dans \( I \) telle que \( { \cup }_{n}{J}_{n} = I \) , la limite de \( \left( {{\int }_{{J}_{n}}f}\right) \) existe et ne dépend pas du choix de la suite \( \left( {J}_{n}\right) \) . Cette limite s’appelle l’intégrale de \( f \) et est notée \( {\int }_{I}f \) .

> \( \rightarrow \) DEFINITION 3 (INTEGRABLE FUNCTION). A piecewise continuous function \( f : I \rightarrow E \) is said to be integrable (or summable) on \( I \) if \( \parallel f\parallel \) is integrable on \( I \) . In this case, for any increasing sequence \( \left( {J}_{n}\right) \) of segments included in \( I \) such that \( { \cup }_{n}{J}_{n} = I \) , the limit of \( \left( {{\int }_{{J}_{n}}f}\right) \) exists and does not depend on the choice of the sequence \( \left( {J}_{n}\right) \) . This limit is called the integral of \( f \) and is denoted by \( {\int }_{I}f \) .

Démonstration. Notons \( {J}_{n} = \left\lbrack {{a}_{n},{b}_{n}}\right\rbrack \) , de sorte que la suite \( \left( {a}_{n}\right) \) est décroissante et tend vers \( a \) , et \( \left( {b}_{n}\right) \) est croissante et tend vers \( b \) . Montrons d’abord que la suite \( {u}_{n} = {\int }_{{J}_{n}}f \) est de Cauchy.

> Proof. Let us denote \( {J}_{n} = \left\lbrack {{a}_{n},{b}_{n}}\right\rbrack \) , so that the sequence \( \left( {a}_{n}\right) \) is decreasing and tends to \( a \) , and \( \left( {b}_{n}\right) \) is increasing and tends to \( b \) . Let us first show that the sequence \( {u}_{n} = {\int }_{{J}_{n}}f \) is Cauchy.

Soit \( \varepsilon > 0 \) . Comme \( \parallel f\parallel \) est intégrable sur \( I \) , la suite \( \left( {U}_{n}\right) = \left( {{\int }_{{J}_{n}}\parallel f\parallel }\right) \) converge donc il existe \( N \in \mathbb{N} \) tel que pour tout \( p, q \geq N,\left| {{U}_{p} - {U}_{q}}\right| < \varepsilon \) . Ceci entraîne, pour \( p, q \geq N \) (et \( p < q \) ),

> Let \( \varepsilon > 0 \) . Since \( \parallel f\parallel \) is integrable on \( I \) , the sequence \( \left( {U}_{n}\right) = \left( {{\int }_{{J}_{n}}\parallel f\parallel }\right) \) converges, so there exists \( N \in \mathbb{N} \) such that for all \( p, q \geq N,\left| {{U}_{p} - {U}_{q}}\right| < \varepsilon \) . This implies, for \( p, q \geq N \) (and \( p < q \) ),

\[
\begin{Vmatrix}{{u}_{p} - {u}_{q}}\end{Vmatrix} = \begin{Vmatrix}{{\int }_{\left\lbrack  {a}_{q},{a}_{p}\right\rbrack  }f + {\int }_{\left\lbrack  {b}_{p},{b}_{q}\right\rbrack  }f}\end{Vmatrix} \leq  {\int }_{\left\lbrack  {a}_{q},{a}_{p}\right\rbrack  }\parallel f\parallel  + {\int }_{\left\lbrack  {b}_{p},{b}_{q}\right\rbrack  }\parallel f\parallel  = {U}_{q} - {U}_{p} < \varepsilon .
\]

Finalement, \( \left( {u}_{n}\right) \) est bien une suite de Cauchy dans l’e.v.n complet \( E \) , donc elle converge. Notons \( \ell \) sa limite.

> Finally, \( \left( {u}_{n}\right) \) is indeed a Cauchy sequence in the complete n.v.s. \( E \) , so it converges. Let \( \ell \) denote its limit.

Unicité de la limite. Soit \( \left( {K}_{n}\right) \) une autre suite d’intervalles vérifiant les mêmes hypothèses que \( \left( {J}_{n}\right) \) , et notons \( {\ell }^{\prime } \) la limite de la suite \( {v}_{n} = {\int }_{{K}_{n}}f \) . Construisons la suite de segments \( {L}_{n} = {J}_{n} \cup {K}_{n} = \left\lbrack {{c}_{n},{d}_{n}}\right\rbrack \) , qui est bien croissante et vérifie \( { \cup }_{n}{L}_{n} = I \) , et notons \( {\ell }^{\prime \prime } \) la limite de la suite \( {w}_{n} = {\int }_{{L}_{n}}f \) . Notons \( {W}_{n} = {\int }_{{L}_{n}}\parallel f\parallel \) . Comme \( {J}_{n} \subset {L}_{n} \) on a

> Uniqueness of the limit. Let \( \left( {K}_{n}\right) \) be another sequence of intervals satisfying the same hypotheses as \( \left( {J}_{n}\right) \) , and let \( {\ell }^{\prime } \) denote the limit of the sequence \( {v}_{n} = {\int }_{{K}_{n}}f \) . Construct the sequence of segments \( {L}_{n} = {J}_{n} \cup {K}_{n} = \left\lbrack {{c}_{n},{d}_{n}}\right\rbrack \) , which is indeed increasing and satisfies \( { \cup }_{n}{L}_{n} = I \) , and let \( {\ell }^{\prime \prime } \) denote the limit of the sequence \( {w}_{n} = {\int }_{{L}_{n}}f \) . Let \( {W}_{n} = {\int }_{{L}_{n}}\parallel f\parallel \) . Since \( {J}_{n} \subset {L}_{n} \) we have

\[
\begin{Vmatrix}{{w}_{n} - {u}_{n}}\end{Vmatrix} = \begin{Vmatrix}{{\int }_{\left\lbrack  {c}_{n},{a}_{n}\right\rbrack  }f + {\int }_{\left\lbrack  {b}_{n},{d}_{n}\right\rbrack  }f}\end{Vmatrix} \leq  {\int }_{\left\lbrack  {c}_{n},{a}_{n}\right\rbrack  }\parallel f\parallel  + {\int }_{\left\lbrack  {b}_{n},{d}_{n}\right\rbrack  }\parallel f\parallel  = {W}_{n} - {U}_{n},
\]

et comme \( \left( {U}_{n}\right) \) et \( \left( {W}_{n}\right) \) ont même limite (c’est \( {\int }_{I}\parallel f\parallel \) ), on en déduit que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{w}_{n} - {u}_{n} = 0 \) . Donc \( {\ell }^{\prime \prime } = \ell \) . On montrerait de même que \( {\ell }^{\prime \prime } = {\ell }^{\prime } \) , on a donc bien démontré que \( \ell = {\ell }^{\prime } \) .

> and since \( \left( {U}_{n}\right) \) and \( \left( {W}_{n}\right) \) have the same limit (which is \( {\int }_{I}\parallel f\parallel \) ), we deduce that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{w}_{n} - {u}_{n} = 0 \) . Thus \( {\ell }^{\prime \prime } = \ell \) . We would show similarly that \( {\ell }^{\prime \prime } = {\ell }^{\prime } \) , so we have indeed proven that \( \ell = {\ell }^{\prime } \) .

Remarque 1. - Si \( f \) est à valeurs réelles, une définition équivalente à la précédente est \( {\int }_{I}f = {\int }_{I}{f}^{ + } - {\int }_{I}{f}^{ - } \) , où \( {f}^{ + } = \max \left( {f,0}\right) \) et \( {f}^{ - } = \max \left( {-f,0}\right) \) . La définition 3 que nous proposons permet de ne pas se limiter au cadre où \( E = \mathbb{R} \) et donne une définition intrinsèque de l'intégrale sur tout e.v.n complet, en particulier sur \( \mathbb{C} \) et sur tout e.v de dimension finie (voir également la remarque 2 page 124).

> Remark 1. - If \( f \) is real-valued, an equivalent definition to the previous one is \( {\int }_{I}f = {\int }_{I}{f}^{ + } - {\int }_{I}{f}^{ - } \) , where \( {f}^{ + } = \max \left( {f,0}\right) \) and \( {f}^{ - } = \max \left( {-f,0}\right) \) . The definition 3 that we propose allows us not to be limited to the case where \( E = \mathbb{R} \) and provides an intrinsic definition of the integral on any complete n.v.s., in particular on \( \mathbb{C} \) and on any finite-dimensional v.s. (see also remark 2 on page 124).

— La proposition 1 page 125 se généralise aisément ici : Une fonction continue par morceaux \( f : I \rightarrow \mathbb{C} \) est intégrable sur \( I \) si et seulement si \( \Re \left( f\right) \) et \( \Im \left( f\right) \) le sont, et on a \( {\int }_{I}f = {\int }_{I}\Re \left( f\right) + i{\int }_{I}\Im \left( f\right) \) . De même, considérons un e.v.n \( E \) de dimension finie dont \( \left( {e}_{i}\right) \) est une base, et une fonction continue par morceaux \( f : I \rightarrow E \) qui s’écrit \( f = \mathop{\sum }\limits_{i}{f}_{i}{e}_{i} \) (avec \( {f}_{i} \in {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) ). Alors \( f \) est intégrable sur \( I \) si et seulement si les \( {f}_{i} \) sont intégrables sur \( I \) , et on a \( {\int }_{I}f = \mathop{\sum }\limits_{i}\left( {{\int }_{I}{f}_{i}}\right) {e}_{i} \) .

> — Proposition 1 on page 125 generalizes easily here: A piecewise continuous function \( f : I \rightarrow \mathbb{C} \) is integrable on \( I \) if and only if \( \Re \left( f\right) \) and \( \Im \left( f\right) \) are, and we have \( {\int }_{I}f = {\int }_{I}\Re \left( f\right) + i{\int }_{I}\Im \left( f\right) \) . Similarly, consider a finite-dimensional normed vector space \( E \) with basis \( \left( {e}_{i}\right) \) , and a piecewise continuous function \( f : I \rightarrow E \) written as \( f = \mathop{\sum }\limits_{i}{f}_{i}{e}_{i} \) (with \( {f}_{i} \in {\mathcal{C}}_{m}\left( {I,\mathbb{R}}\right) \) ). Then \( f \) is integrable on \( I \) if and only if the \( {f}_{i} \) are integrable on \( I \) , and we have \( {\int }_{I}f = \mathop{\sum }\limits_{i}\left( {{\int }_{I}{f}_{i}}\right) {e}_{i} \) .

- Si \( f \) est continue par morceaux sur un segment \( \left\lbrack  {a, b}\right\rbrack \) , alors \( f \) est bien intégrable au sens de la définition précédente, et la définition de son intégrale est bien égale à celle de la définition 4 page 124, et de plus on a \( {\int }_{\left\lbrack  a, b\right\rbrack  }f = {\int }_{\left\rbrack  a, b\right\rbrack  }f = {\int }_{\lbrack a, b\lbrack }f = {\int }_{\rbrack a, b\lbrack }f \) .

> - If \( f \) is piecewise continuous on a segment \( \left\lbrack  {a, b}\right\rbrack \) , then \( f \) is indeed integrable in the sense of the previous definition, and the definition of its integral is indeed equal to that of definition 4 on page 124, and furthermore we have \( {\int }_{\left\lbrack  a, b\right\rbrack  }f = {\int }_{\left\rbrack  a, b\right\rbrack  }f = {\int }_{\lbrack a, b\lbrack }f = {\int }_{\rbrack a, b\lbrack }f \) .

- De manière générale, \( f \) est intégrable sur \( I \) si et seulement si elle est intégrable sur l’intérieur \( I \) de \( I \) , et on a \( {\int }_{I}f = {\int }_{I}f \) . Ceci permet d’utiliser la notation \( {\int }_{a}^{b}f\left( t\right) {dt} = \; {\int }_{I}f \) . Si \( a > b \) , on définit \( {\int }_{a}^{b} =  - {\int }_{b}^{a} \) .

> - Generally speaking, \( f \) is integrable on \( I \) if and only if it is integrable on the interior \( I \) of \( I \) , and we have \( {\int }_{I}f = {\int }_{I}f \) . This allows the use of the notation \( {\int }_{a}^{b}f\left( t\right) {dt} = \; {\int }_{I}f \) . If \( a > b \) , we define \( {\int }_{a}^{b} =  - {\int }_{b}^{a} \) .

— Les propriétés élémentaires des intégrales sur un segment (linéarité, positivité, relation de Chasles, . . .) restent vraies pour les fonctions intégrables. On a notamment \( \begin{Vmatrix}{{\int }_{I}f}\end{Vmatrix} \leq {\int }_{I}\parallel f\parallel . \)

> — The elementary properties of integrals on a segment (linearity, positivity, Chasles' relation, etc.) remain true for integrable functions. In particular, we have \( \begin{Vmatrix}{{\int }_{I}f}\end{Vmatrix} \leq {\int }_{I}\parallel f\parallel . \)

##### Integrability criteria.

*Français : Critères d'intégrabilité.*

Proposition 2. Soit \( I = \lbrack a, b\lbrack \) et \( f : I \rightarrow E \) une fonction continue par morceaux sur 1. Les assertions suivantes sont équivalentes

> Proposition 2. Let \( I = \lbrack a, b\lbrack \) and \( f : I \rightarrow E \) be a piecewise continuous function on 1. The following assertions are equivalent

(i) \( f \) est intégrable sur \( \lbrack a, b\lbrack \)

> (i) \( f \) is integrable on \( \lbrack a, b\lbrack \)

(ii) \( x \mapsto {\int }_{a}^{x}\parallel f\left( t\right) \parallel {dt} \) est bornée sur \( \lbrack a, b\lbrack \)

> (ii) \( x \mapsto {\int }_{a}^{x}\parallel f\left( t\right) \parallel {dt} \) is bounded on \( \lbrack a, b\lbrack \)

(iii) \( \mathop{\lim }\limits_{\substack{{x \rightarrow b} \\ {x < b} }}{\int }_{a}^{x}\parallel f\left( t\right) \parallel {dt} \) existe

> (iii) \( \mathop{\lim }\limits_{\substack{{x \rightarrow b} \\ {x < b} }}{\int }_{a}^{x}\parallel f\left( t\right) \parallel {dt} \) exists

(iv) \( \mathop{\lim }\limits_{\substack{{x \rightarrow b} \\ {x < b} }}{\int }_{x}^{b}\parallel f\left( t\right) \parallel {dt} = 0 \)

> (iv) \( \mathop{\lim }\limits_{\substack{{x \rightarrow b} \\ {x < b} }}{\int }_{x}^{b}\parallel f\left( t\right) \parallel {dt} = 0 \)

(v) \( \forall \varepsilon > 0,\exists A \in I \) tel que \( \forall x, y \in \left\lbrack {A, b\left\lbrack \right. \left( {x < y}\right) ,\;{\int }_{x}^{y}\parallel f\left( t\right) \parallel {dt} < \varepsilon }\right. \) (critère de Cauchy)

> (v) \( \forall \varepsilon > 0,\exists A \in I \) such that \( \forall x, y \in \left\lbrack {A, b\left\lbrack \right. \left( {x < y}\right) ,\;{\int }_{x}^{y}\parallel f\left( t\right) \parallel {dt} < \varepsilon }\right. \) (Cauchy criterion)

Proposition 3. Soit \( f : I \rightarrow E \) une fonction continue par morceaux et soit \( c \in I \) . Soit \( \left. {{I}_{g} = I \cap \rbrack - \infty , c}\right\rbrack \) et \( {I}_{d} = I \cap \lbrack c, + \infty \lbrack \) . Alors \( f \) est intégrable sur \( I \) si et seulement si \( f \) est intégrable sur \( {I}_{g} \) et intégrable sur \( {I}_{d} \) , et on a \( {\int }_{I}f = {\int }_{{I}_{g}}f + {\int }_{{I}_{d}}f \) .

> Proposition 3. Let \( f : I \rightarrow E \) be a piecewise continuous function and let \( c \in I \) . Let \( \left. {{I}_{g} = I \cap \rbrack - \infty , c}\right\rbrack \) and \( {I}_{d} = I \cap \lbrack c, + \infty \lbrack \) . Then \( f \) is integrable on \( I \) if and only if \( f \) is integrable on \( {I}_{g} \) and integrable on \( {I}_{d} \) , and we have \( {\int }_{I}f = {\int }_{{I}_{g}}f + {\int }_{{I}_{d}}f \) .

Proposition 4. Soient \( f : I \rightarrow E \) et \( \varphi : I \rightarrow {\mathbb{R}}^{ + } \) continues par morceaux.

> Proposition 4. Let \( f : I \rightarrow E \) and \( \varphi : I \rightarrow {\mathbb{R}}^{ + } \) be piecewise continuous.

(i) Si \( \parallel f\parallel \leq \varphi \) sur I et si \( \varphi \) est intégrable, alors \( f \) est intégrable et on a \( \begin{Vmatrix}{{\int }_{I}f}\end{Vmatrix} \leq {\int }_{I}\varphi \) .

> (i) If \( \parallel f\parallel \leq \varphi \) on I and if \( \varphi \) is integrable, then \( f \) is integrable and we have \( \begin{Vmatrix}{{\int }_{I}f}\end{Vmatrix} \leq {\int }_{I}\varphi \) .

(ii) Si \( f \) est à valeurs positives et non intégrable, et si \( f \leq \varphi \) , alors \( \varphi \) est non intégrable.

> (ii) If \( f \) is positive-valued and non-integrable, and if \( f \leq \varphi \) , then \( \varphi \) is non-integrable.

Proposition 5. Soient \( f : \left\lbrack {a, b\left\lbrack { \rightarrow E\text{ et }g : \left\lbrack {a, b\left\lbrack { \rightarrow {\mathbb{R}}^{ + }}\right. }\right. }\right. }\right. \) continues par morceaux.

> Proposition 5. Let \( f : \left\lbrack {a, b\left\lbrack { \rightarrow E\text{ et }g : \left\lbrack {a, b\left\lbrack { \rightarrow {\mathbb{R}}^{ + }}\right. }\right. }\right. }\right. \) be piecewise continuous.

(i) Si \( f\left( x\right) = O\left( {g\left( x\right) }\right) \) lorsque \( x \rightarrow b \) et si g est intégrable, alors \( f \) est intégrable.

> (i) If \( f\left( x\right) = O\left( {g\left( x\right) }\right) \) as \( x \rightarrow b \) and if g is integrable, then \( f \) is integrable.

(ii) Si \( f\left( x\right) \sim g\left( x\right) \) lorsque \( x \rightarrow b \) (et \( f \) à valeurs réelles), alors \( f \) est intégrable si et seulement si g est intégrable.

> (ii) If \( f\left( x\right) \sim g\left( x\right) \) as \( x \rightarrow b \) (and \( f \) is real-valued), then \( f \) is integrable if and only if g is integrable.

On utilise souvent les propositions précédentes pour comparer les fonctions que l'on intègre avec les fonctions de comparaison introduites dans l'exemple 1. Par exemple

> The previous propositions are often used to compare the functions being integrated with the comparison functions introduced in Example 1. For instance

\[
\mathop{\lim }\limits_{{t \rightarrow   + \infty }}{t}^{2}{e}^{-{t}^{2}} = 0\;\text{ donc }\;{e}^{-{t}^{2}} = O\left( {t}^{-2}\right) \;\left( {t \rightarrow   + \infty }\right) ,
\]

et comme \( t \mapsto 1/{t}^{2} \) est intégrable sur \( \lbrack 1, + \infty \lbrack \) , on en déduit avec l’assertion (i) de la proposition 5 que \( t \mapsto {e}^{-{t}^{2}} \) est intégrable sur \( \lbrack 1, + \infty \lbrack \) . On peut également utiliser des comparaisons avec les intégrales de Bertrand (proposition 6).

> and since \( t \mapsto 1/{t}^{2} \) is integrable on \( \lbrack 1, + \infty \lbrack \) , we deduce from assertion (i) of Proposition 5 that \( t \mapsto {e}^{-{t}^{2}} \) is integrable on \( \lbrack 1, + \infty \lbrack \) . One can also use comparisons with Bertrand integrals (Proposition 6).

Intégrales de Bertrand. En plus des exemples fondamentaux de l'exemple 1 les inté- grales de Bertrand fournissent d'autres fonctions de comparaison qui permettent parfois, à l'aide des propositions précédentes, de décider de la convergence d'une intégrale.

> Bertrand integrals. In addition to the fundamental examples in Example 1, Bertrand integrals provide other comparison functions that sometimes allow, using the previous propositions, to decide the convergence of an integral.

Proposition 6 (Intégrales de Bertrand). Soient \( \alpha \) et \( \beta \) des nombres réels. Alors

> Proposition 6 (Bertrand integrals). Let \( \alpha \) and \( \beta \) be real numbers. Then

\[
\left( {t \mapsto  \frac{1}{{t}^{\alpha }{\log }^{\beta }t}\;\text{ est intégrable sur }\lbrack e, + \infty \lbrack }\right.  \Leftrightarrow  \left( {\left( {\alpha  > 1}\right) \;\text{ ou }\;\left( {\alpha  = 1\text{ et }\beta  > 1}\right) }\right)
\]

et

\[
\left( {t \mapsto  \frac{1}{{t}^{\alpha }{\left| \log t\right| }^{\beta }}\;\text{ est intégrable sur }\rbrack 0,1/e\rbrack }\right)  \Leftrightarrow  \left( {\left( {\alpha  < 1}\right) \;\text{ ou }\;\left( {\alpha  = 1\text{ et }\beta  > 1}\right) }\right) .
\]

Démonstration. Montrons tout d'abord la première partie de la proposition.

> Proof. Let us first show the first part of the proposition.

- Si \( \alpha  > 1 \) , on écrit \( \alpha  = 1 + {2h} \) avec \( h > 0 \) . Pour tout \( \beta  \in  \mathbb{R} \) , on a

> - If \( \alpha  > 1 \) , we write \( \alpha  = 1 + {2h} \) with \( h > 0 \) . For all \( \beta  \in  \mathbb{R} \) , we have

\[
\mathop{\lim }\limits_{{t \rightarrow   + \infty }}\frac{1}{{t}^{h}{\log }^{\beta }t} = 0\;\text{ donc }\;\frac{1}{{t}^{\alpha }{\log }^{\beta }} = \frac{1}{{t}^{1 + h}}\frac{1}{{t}^{h}{\log }^{\beta }t} = O\left( \frac{1}{{t}^{1 + h}}\right)
\]

donc \( t \mapsto {t}^{-\alpha }{\log }^{-\beta }{tdt} \) est intégrable sur \( \lbrack e, + \infty \lbrack \) .

> therefore \( t \mapsto {t}^{-\alpha }{\log }^{-\beta }{tdt} \) is integrable on \( \lbrack e, + \infty \lbrack \) .

- Si \( \alpha  = 1 \) , deux cas se présentent.

> - If \( \alpha  = 1 \) , two cases arise.

- Si \( \beta  > 1 \) , comme

> - If \( \beta  > 1 \) , as

\[
\forall X > e,\;{\int }_{e}^{X}\frac{dt}{t{\log }^{\beta }t} = {\left\lbrack  \frac{{\log }^{1 - \beta }t}{1 - \beta }\right\rbrack  }_{e}^{X} = \frac{{\log }^{1 - \beta }X - 1}{1 - \beta },
\]

on en conclut que la fonction est bien intégrable sur \( \lbrack e, + \infty \lbrack \) .

> we conclude that the function is indeed integrable on \( \lbrack e, + \infty \lbrack \) .

- Si \( \beta  \leq  1 \) , on écrit

> - If \( \beta  \leq  1 \) , we write

\[
\forall X > e,\;{\int }_{e}^{X}\frac{dt}{t{\log }^{\beta }t} \geq  {\int }_{e}^{X}\frac{dt}{t\log t} = {\left\lbrack  \log \left( \log t\right) \right\rbrack  }_{e}^{X} = \log \log X,
\]

ce qui prouve que la fonction n'est pas intégrable.

> which proves that the function is not integrable.

- Si \( \alpha  < 1 \) , on écrit \( \alpha  = 1 - {2h} \) avec \( h > 0 \) . On a pour tout \( \beta  \in  \mathbb{R} \)

> - If \( \alpha  < 1 \) , we write \( \alpha  = 1 - {2h} \) with \( h > 0 \) . We have for all \( \beta  \in  \mathbb{R} \)

\[
\mathop{\lim }\limits_{{t \rightarrow   + \infty }}\frac{{t}^{h}}{{\log }^{\beta }t} =  + \infty \;\text{ donc }\;\exists A \geq  e,\forall t > A,\;\frac{1}{{t}^{\alpha }{\log }^{\beta }t} = \frac{{t}^{h}}{{\log }^{\beta }t}\frac{1}{{t}^{1 - h}} \geq  \frac{1}{{t}^{1 - h}},
\]

ce qui montre que la fonction n’est pas intégrable car \( t \mapsto 1/{t}^{1 - h} \) n’est pas intégrable sur \( \lbrack A, + \infty \lbrack \) .

> which shows that the function is not integrable because \( t \mapsto 1/{t}^{1 - h} \) is not integrable on \( \lbrack A, + \infty \lbrack \) .

La seconde partie de la proposition se déduit de la première par le changement de variable \( u = 1/t \) grâce au théorème du changement de variable (théorème 1).

> The second part of the proposition is deduced from the first by the change of variable \( u = 1/t \) thanks to the change of variable theorem (theorem 1).
