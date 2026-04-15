#### 1.3. Results on differentiability for real-valued functions

*Français : 1.3. Résultats relatifs à la dérivabilité pour les fonctions à valeurs réelles*

Dans toute cette partie, \( \left\lbrack {a, b}\right\rbrack \) désigne un segment de \( \mathbb{R} \) non réduit à un singleton.

> Throughout this section, \( \left\lbrack {a, b}\right\rbrack \) denotes a segment of \( \mathbb{R} \) not reduced to a singleton.

Proposition 5. Soit I un intervalle \( d\mathbb{R} \) et \( f : I \rightarrow \mathbb{R} \) une application. Si \( f \) admet un extremum relatif en \( c \in \overset{ \circ }{I} \) et si \( {f}^{\prime }\left( c\right) \) existe, alors \( {f}^{\prime }\left( c\right) = 0 \) .

> Proposition 5. Let I be an interval \( d\mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) a mapping. If \( f \) has a relative extremum at \( c \in \overset{ \circ }{I} \) and if \( {f}^{\prime }\left( c\right) \) exists, then \( {f}^{\prime }\left( c\right) = 0 \) .

\( \rightarrow \) THÉORÈME 1 (DE ROLLE). Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une application vérifiant :

> \( \rightarrow \) THEOREM 1 (ROLLE'S THEOREM). Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a mapping satisfying:

(i) \( f \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) .

> (i) \( f \) is continuous on \( \left\lbrack {a, b}\right\rbrack \) .

(ii) \( f \) est dérivable sur \( \rbrack a, b\lbrack \) .

> (ii) \( f \) is differentiable on \( \rbrack a, b\lbrack \) .

(iii) \( f\left( a\right) = f\left( b\right) \) .

> (iii) \( f\left( a\right) = f\left( b\right) \) .

![bo_d7fjkrs91nqc73ereoog_78_430_187_650_320_0.jpg](images/gourdon_analysis_fr_en_028_bod7fjkrs91nqc73ereoog784301876503200.jpg)

FIGURE 1. Une illustration du théorème de Rolle.

> FIGURE 1. An illustration of Rolle's theorem.

Alors il existe \( c \in \rbrack a, b\left\lbrack \right. \) tel que \( {f}^{\prime }\left( c\right) = 0 \) .

> Then there exists \( c \in \rbrack a, b\left\lbrack \right. \) such that \( {f}^{\prime }\left( c\right) = 0 \) .

Démonstration. Si \( f \) est constante sur \( \left\lbrack {a, b}\right\rbrack \) , le résultat est évident. Sinon, il existe \( {x}_{0} \in \rbrack a, b\lbrack \) tel que \( f\left( {x}_{0}\right) \neq f\left( a\right) \) , par exemple \( f\left( {x}_{0}\right) > f\left( a\right) \) . Comme \( \left\lbrack {a, b}\right\rbrack \) est un compact de \( \mathbb{R} \) et que \( f \) est continue, il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( f\left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}f\left( x\right) \) . Or \( f\left( c\right) \geq f\left( {x}_{0}\right) > f\left( a\right) = f\left( b\right) \) , donc \( c \in \rbrack a, b\lbrack \) , donc \( f\left( c\right) \) étant un extremum de \( f \) , on a \( {f}^{\prime }\left( c\right) = 0 \) d’après la proposition 5 .

> Proof. If \( f \) is constant on \( \left\lbrack {a, b}\right\rbrack \) , the result is obvious. Otherwise, there exists \( {x}_{0} \in \rbrack a, b\lbrack \) such that \( f\left( {x}_{0}\right) \neq f\left( a\right) \) , for example \( f\left( {x}_{0}\right) > f\left( a\right) \) . Since \( \left\lbrack {a, b}\right\rbrack \) is a compact set of \( \mathbb{R} \) and \( f \) is continuous, there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( f\left( c\right) = \mathop{\sup }\limits_{{x \in \left\lbrack {a, b}\right\rbrack }}f\left( x\right) \) . However, \( f\left( c\right) \geq f\left( {x}_{0}\right) > f\left( a\right) = f\left( b\right) \) , so \( c \in \rbrack a, b\lbrack \) , therefore \( f\left( c\right) \) being an extremum of \( f \) , we have \( {f}^{\prime }\left( c\right) = 0 \) according to proposition 5.

\( \rightarrow \) THÉORÉME 2 (DES ACCROISSEMENTS FINIS). Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une application continue sur \( \left\lbrack {a, b}\right\rbrack \) et dérivable sur \( \rbrack a, b\lbrack \) . Alors

> \( \rightarrow \) THEOREM 2 (MEAN VALUE THEOREM). Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a mapping continuous on \( \left\lbrack {a, b}\right\rbrack \) and differentiable on \( \rbrack a, b\lbrack \) . Then

\[
\exists c \in  \rbrack a, b\left\lbrack  {,\;{f}^{\prime }\left( c\right)  = \frac{f\left( b\right)  - f\left( a\right) }{b - a}.}\right.
\]

![bo_d7fjkrs91nqc73ereoog_78_501_1042_581_384_0.jpg](images/gourdon_analysis_fr_en_029_bod7fjkrs91nqc73ereoog7850110425813840.jpg)

Figure 2. Une illustration du théorème des accroissements finis.

> Figure 2. An illustration of the mean value theorem.

Démonstration. Posons \( A = \frac{f\left( b\right) - f\left( a\right) }{b - a} \) et \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow f\left( x\right) - A\left( {x - a}\right) \) . On a \( \varphi \left( a\right) = f\left( a\right) = \varphi \left( b\right) \) donc d’après le théorème de Rolle, il existe \( c \in \rbrack a, b\left\lbrack \right. \) tel que \( {\varphi }^{\prime }\left( c\right) = 0 \) . On en déduit \( {f}^{\prime }\left( c\right) = A \) , d'où le résultat.

> Proof. Let \( A = \frac{f\left( b\right) - f\left( a\right) }{b - a} \) and \( \varphi : \left\lbrack {a, b}\right\rbrack \rightarrow f\left( x\right) - A\left( {x - a}\right) \) . We have \( \varphi \left( a\right) = f\left( a\right) = \varphi \left( b\right) \) so, according to Rolle's theorem, there exists \( c \in \rbrack a, b\left\lbrack \right. \) such that \( {\varphi }^{\prime }\left( c\right) = 0 \) . We deduce \( {f}^{\prime }\left( c\right) = A \) , hence the result.

Conséquence : Une fonction continue sur \( \left\lbrack {a, b}\right\rbrack \) , dérivable sur \( \rbrack a, b\lbrack \) est croissante si et seulement si \( {f}^{\prime }\left( x\right) \geq 0 \) pour tout \( x \in \rbrack a, b\left\lbrack \right. \) . Elle est constante si et seulement si \( {f}^{\prime }\left( x\right) = 0 \) pour tout \( x \in \rbrack a, b\lbrack \) .

> Consequence: A function continuous on \( \left\lbrack {a, b}\right\rbrack \) and differentiable on \( \rbrack a, b\lbrack \) is increasing if and only if \( {f}^{\prime }\left( x\right) \geq 0 \) for all \( x \in \rbrack a, b\left\lbrack \right. \) . It is constant if and only if \( {f}^{\prime }\left( x\right) = 0 \) for all \( x \in \rbrack a, b\lbrack \) .

Remarque 2. Les théorèmes de Rolle et des accroissements finis sont faux lorsque \( f \) est à valeurs dans un \( \mathbb{R} \) -e.v.n. Par exemple, l’application \( f : \left\lbrack {0,{2\pi }}\right\rbrack \rightarrow \mathbb{C}\;t \mapsto {e}^{it} \) vérifie \( f\left( 0\right) = f\left( {2\pi }\right) \) et pourtant pour tout \( t \in \left\lbrack {0,{2\pi }}\right\rbrack ,{f}^{\prime }\left( t\right) = i{e}^{it} \) n’est jamais nul.

> Remark 2. Rolle's theorem and the mean value theorem are false when \( f \) takes values in a \( \mathbb{R} \) -n.v.s. For example, the mapping \( f : \left\lbrack {0,{2\pi }}\right\rbrack \rightarrow \mathbb{C}\;t \mapsto {e}^{it} \) satisfies \( f\left( 0\right) = f\left( {2\pi }\right) \) and yet for all \( t \in \left\lbrack {0,{2\pi }}\right\rbrack ,{f}^{\prime }\left( t\right) = i{e}^{it} \) is never zero.

THÉORÉME 3 (DES ACCROISSEMENTS FINIS GÉNÉRALISÉS). Soient \( f \) , \( g \) deux applications de \( \left\lbrack {a, b}\right\rbrack \) dans \( \mathbb{R} \) , continues sur \( \left\lbrack {a, b}\right\rbrack \) et dérivables sur \( \rbrack a, b\lbrack \) . Alors

> THEOREM 3 (GENERALIZED MEAN VALUE THEOREM). Let \( f \) and \( g \) be two mappings from \( \left\lbrack {a, b}\right\rbrack \) to \( \mathbb{R} \) , continuous on \( \left\lbrack {a, b}\right\rbrack \) and differentiable on \( \rbrack a, b\lbrack \) . Then

\[
\exists c \in  \rbrack a, b\lbrack ,\;\left( {f\left( b\right)  - f\left( a\right) }\right) {g}^{\prime }\left( c\right)  = \left( {g\left( b\right)  - g\left( a\right) }\right) {f}^{\prime }\left( c\right) .
\]

Si \( {g}^{\prime }\left( c\right) \neq 0 \) et \( g\left( a\right) \neq g\left( b\right) \) , cette égalité s’écrit aussi \( \frac{f\left( b\right) - f\left( a\right) }{g\left( b\right) - g\left( a\right) } = \frac{{f}^{\prime }\left( c\right) }{{g}^{\prime }\left( c\right) } \) .

> If \( {g}^{\prime }\left( c\right) \neq 0 \) and \( g\left( a\right) \neq g\left( b\right) \) , this equality is also written as \( \frac{f\left( b\right) - f\left( a\right) }{g\left( b\right) - g\left( a\right) } = \frac{{f}^{\prime }\left( c\right) }{{g}^{\prime }\left( c\right) } \) .

Démonstration. Il suffit d'appliquer le théorème de Rolle à l'application

> Proof. It suffices to apply Rolle's theorem to the mapping

\[
\left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  \left\lbrack  {f\left( b\right)  - f\left( a\right) }\right\rbrack  \left\lbrack  {g\left( x\right)  - g\left( a\right) }\right\rbrack   - \left\lbrack  {g\left( b\right)  - g\left( a\right) }\right\rbrack  \left\lbrack  {f\left( x\right)  - f\left( a\right) }\right\rbrack  ,
\]

qui est continue sur \( \left\lbrack {a, b}\right\rbrack \) , dérivable sur \( \rbrack a, b\lbrack \) et s’annule en \( a \) et en \( b \) .

> which is continuous on \( \left\lbrack {a, b}\right\rbrack \) , differentiable on \( \rbrack a, b\lbrack \) and vanishes at \( a \) and at \( b \) .

Conséquence : (RÉGLE DE L’HOSPITAL) Si \( f\left( a\right) = g\left( a\right) = 0 \) et si \( \ell = \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}{f}^{\prime }\left( x\right) /{g}^{\prime }\left( x\right) \) existe, alors \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}f\left( x\right) /g\left( x\right) = \ell \) .

> Consequence: (L'HÔPITAL'S RULE) If \( f\left( a\right) = g\left( a\right) = 0 \) and if \( \ell = \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}{f}^{\prime }\left( x\right) /{g}^{\prime }\left( x\right) \) exists, then \( \mathop{\lim }\limits_{\substack{{x \rightarrow a} \\ {x \neq a} }}f\left( x\right) /g\left( x\right) = \ell \) .

Remarque 3. La réciproque de la règle de L'Hospital est fausse. Autrement dit, on peut avoir \( f\left( a\right) = g\left( a\right) = 0 \) et \( f\left( x\right) /g\left( x\right) \) peut converger lorsque \( x \rightarrow a\left( {x \neq a}\right) \) , sans que \( {f}^{\prime }\left( x\right) /{g}^{\prime }\left( x\right) \) converge lorsque \( x \rightarrow a\left( {x \neq a}\right) \) .

> Remark 3. The converse of L'Hospital's rule is false. In other words, it is possible to have \( f\left( a\right) = g\left( a\right) = 0 \) and for \( f\left( x\right) /g\left( x\right) \) to converge as \( x \rightarrow a\left( {x \neq a}\right) \) , without \( {f}^{\prime }\left( x\right) /{g}^{\prime }\left( x\right) \) converging as \( x \rightarrow a\left( {x \neq a}\right) \) .

\( \rightarrow \) THÉORÉME 4 (FORMULE DE TAYLOR-LAGRANGE). Soit \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) une application de classe \( {\mathcal{C}}^{n} \) sur \( \left\lbrack {a, b}\right\rbrack \) , telle que \( {f}^{\left( n + 1\right) } \) existe sur \( \rbrack a, b\lbrack \) . Alors

> \( \rightarrow \) THEOREM 4 (TAYLOR-LAGRANGE FORMULA). Let \( f : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) be a mapping of class \( {\mathcal{C}}^{n} \) on \( \left\lbrack {a, b}\right\rbrack \) , such that \( {f}^{\left( n + 1\right) } \) exists on \( \rbrack a, b\lbrack \) . Then

\[
\exists c \in  \rbrack a, b\lbrack ,\;f\left( b\right)  = f\left( a\right)  + \left( {b - a}\right) {f}^{\prime }\left( a\right)  + \cdots  + \frac{{\left( b - a\right) }^{n}}{n!}{f}^{\left( n\right) }\left( a\right)  + \underset{\text{ rest }d c {Lagrange}}{\underbrace{\frac{{\left( b - a\right) }^{n + 1}}{\left( {n + 1}\right) !}{f}^{\left( n + 1\right) }\left( c\right) }}.
\]

Démonstration. Considérons l'application

> Proof. Consider the mapping

\[
\varphi  : \left\lbrack  {a, b}\right\rbrack   \rightarrow  \mathbb{R}\;x \mapsto  f\left( b\right)  - f\left( x\right)  - \left( {b - x}\right) {f}^{\prime }\left( x\right)  - \cdots  - \frac{{\left( b - x\right) }^{n}}{n!}{f}^{\left( n\right) }\left( x\right)  - A\frac{{\left( b - x\right) }^{n + 1}}{\left( {n + 1}\right) !},
\]

la constante \( A \) étant choisie telle que \( \varphi \left( a\right) = \varphi \left( b\right) = 0 \) . Cette application est continue sur \( \left\lbrack {a, b}\right\rbrack \) , dérivable sur \( \rbrack a, b\lbrack \) et

> the constant \( A \) being chosen such that \( \varphi \left( a\right) = \varphi \left( b\right) = 0 \) . This mapping is continuous on \( \left\lbrack {a, b}\right\rbrack \) , differentiable on \( \rbrack a, b\lbrack \) and

\[
\forall x \in  \rbrack a, b\lbrack ,\;{\varphi }^{\prime }\left( x\right)  =  - \frac{{\left( b - x\right) }^{n}}{n!}{f}^{\left( n + 1\right) }\left( x\right)  + A\frac{{\left( b - x\right) }^{n}}{n!},
\]

donc d’après le théorème de Rolle, il existe \( c \in \rbrack a, b\left\lbrack \right. \) tel que \( {\varphi }^{\prime }\left( c\right) = 0 \) , ce qui s’écrit \( A = {f}^{\left( n + 1\right) }\left( c\right) \) , d’où le résultat car \( \varphi \left( a\right) = 0 \) .

> therefore, according to Rolle's theorem, there exists \( c \in \rbrack a, b\left\lbrack \right. \) such that \( {\varphi }^{\prime }\left( c\right) = 0 \) , which is written as \( A = {f}^{\left( n + 1\right) }\left( c\right) \) , hence the result because \( \varphi \left( a\right) = 0 \) .

Remarque 4. - Avec \( n = 0 \) , on retrouve le théorème des accroissements finis.

> Remark 4. - With \( n = 0 \) , we recover the mean value theorem.

- Lorsque 0 appartient à l'intervalle de définition \( I \) de \( f \) , on a, sous les mêmes hypothèses,

> - When 0 belongs to the interval of definition \( I \) of \( f \) , we have, under the same hypotheses,

\[
\forall x \in  I,\exists \theta  \in  \rbrack 0,1\lbrack ,\;f\left( x\right)  = f\left( 0\right)  + x{f}^{\prime }\left( 0\right)  + \cdots  + \frac{{x}^{n}}{n!}{f}^{\left( n\right) }\left( 0\right)  + \frac{{x}^{n + 1}}{\left( {n + 1}\right) !}{f}^{\left( n + 1\right) }\left( {\theta x}\right) .
\]

Cette relation s'appelle formule de Maclaurin (avec reste de Lagrange).

> This relation is called the Maclaurin formula (with Lagrange remainder).
