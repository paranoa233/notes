### 5. Problems

*Français : 5. Problèmes*

PROBLÉME 1 (TRANSFORMÉE DE FOURIER DISCRÉTE D'UN POLYNÔME). On se fixe un entier \( n \geq 1 \) et on note \( \omega = {e}^{{2i\pi }/n} \) .

> PROBLEM 1 (DISCRETE FOURIER TRANSFORM OF A POLYNOMIAL). We fix an integer \( n \geq 1 \) and denote \( \omega = {e}^{{2i\pi }/n} \) .

a) Pour tout polynôme \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) , on définit les polynômes

> a) For any polynomial \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) , we define the polynomials

\[
{\mathcal{F}}_{d}\left( P\right)  = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}P\left( {\omega }^{k}\right) {X}^{k}\;\text{ et }\;{\overline{\mathcal{F}}}_{d}\left( P\right)  = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}P\left( {\omega }^{-k}\right) {X}^{k} \in  \mathbb{C}\left\lbrack  X\right\rbrack  .
\]

Si \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( \deg \left( P\right) \leq n - 1 \) , montrer que \( {\overline{\mathcal{F}}}_{d}\left\lbrack {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack = {nP} \) . b) Conséquence. Soit \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) vérifiant

> If \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( \deg \left( P\right) \leq n - 1 \) , show that \( {\overline{\mathcal{F}}}_{d}\left\lbrack {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack = {nP} \) . b) Consequence. Let \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) satisfy

\( \left( i\right) \;\forall j \in \mathbb{Z},\left| {P\left( {\omega }^{j}\right) }\right| \leq 1\;\left( {ii}\right) \;\exists k \in \{ 0,1,\ldots , n - 1\} \) tel que \( P\left( {\omega }^{k}\right) = 0 \) .

> \( \left( i\right) \;\forall j \in \mathbb{Z},\left| {P\left( {\omega }^{j}\right) }\right| \leq 1\;\left( {ii}\right) \;\exists k \in \{ 0,1,\ldots , n - 1\} \) such that \( P\left( {\omega }^{k}\right) = 0 \) .

Montrer que \( \left( {{X}^{n} - 1}\right) \) divise \( P \) .

> Show that \( \left( {{X}^{n} - 1}\right) \) divides \( P \) .

Solution. a) Écrivons \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{n - 1}{X}^{n - 1} \) . Si \( 0 \leq k \leq n - 1 \) , le coefficient de \( {X}^{k} \) dans \( {\overline{\mathcal{F}}}_{d}\left\lbrack {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack \) est

> Solution. a) Let us write \( P = {a}_{0} + {a}_{1}X + \cdots + {a}_{n - 1}{X}^{n - 1} \) . If \( 0 \leq k \leq n - 1 \) , the coefficient of \( {X}^{k} \) in \( {\overline{\mathcal{F}}}_{d}\left\lbrack {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack \) is

\[
\left\lbrack  {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack  \left( {\omega }^{-k}\right)  = \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}P\left( {\omega }^{j}\right) {\omega }^{-{jk}} = \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}\left\lbrack  {\mathop{\sum }\limits_{{i = 0}}^{{n - 1}}{a}_{i}{\omega }^{ij}}\right\rbrack  {\omega }^{-{jk}}
\]

\[
= \mathop{\sum }\limits_{{0 \leq  i, j \leq  n - 1}}{a}_{i}{\omega }^{\left( {i - k}\right) j} = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}{a}_{i}\left\lbrack  {\mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\left( {\omega }^{i - k}\right) }^{j}}\right\rbrack  .
\]

(*)

> Lorsque \( 0 \leq i \leq n - 1,\xi = {\omega }^{i - k} \) est une racine \( n \) -ième de l’unité égale à1si et seulement si \( i = k \) , donc

When \( 0 \leq i \leq n - 1,\xi = {\omega }^{i - k} \) is an \( n \) -th root of unity equal to 1 if and only if \( i = k \) , therefore

\[
\mathop{\sum }\limits_{{j = 0}}^{{n - 1}}{\left( {\omega }^{i - k}\right) }^{j} = \left\{  {\begin{array}{ll} 0 & \text{ si }i \neq  k \\  n & \text{ si }i = k \end{array}.}\right.
\]

Ainsi, \( \left( *\right) \) s’écrit \( \left\lbrack {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack \left( {\omega }^{-k}\right) = n{a}_{k} \) . Donc

> Thus, \( \left( *\right) \) is written as \( \left\lbrack {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack \left( {\omega }^{-k}\right) = n{a}_{k} \) . Therefore

\[
{\overline{\mathcal{F}}}_{d}\left\lbrack  {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack   = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\left\lbrack  {{\mathcal{F}}_{d}\left( P\right) }\right\rbrack  \left( {\omega }^{-k}\right) {X}^{k} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}n{a}_{k}{X}^{k} = {nP}.
\]

b) Commençons par effectuer la division euclidienne de \( P \) par \( {X}^{n} - 1 : P = \left( {{X}^{n} - 1}\right) Q + R \) , \( \deg \left( R\right) \leq n - 1 \) et \( \left( {Q, R}\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) (le quotient et le reste sont à coefficients entiers car \( {X}^{n} - 1 \) est unitaire, voir la remarque 3 de la partie 1.3 - page 58). Pour tout entier \( j \) , on a \( P\left( {\omega }^{j}\right) = R\left( {\omega }^{j}\right) \) dont \( R \) vérifie également (i) et (ii). Or \( \deg \left( R\right) \leq n - 1 \) , donc d’après a),

> b) Let us begin by performing the Euclidean division of \( P \) by \( {X}^{n} - 1 : P = \left( {{X}^{n} - 1}\right) Q + R \) , \( \deg \left( R\right) \leq n - 1 \) and \( \left( {Q, R}\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) (the quotient and remainder have integer coefficients because \( {X}^{n} - 1 \) is monic, see remark 3 in part 1.3 - page 58). For any integer \( j \) , we have \( P\left( {\omega }^{j}\right) = R\left( {\omega }^{j}\right) \) where \( R \) also satisfies (i) and (ii). However \( \deg \left( R\right) \leq n - 1 \) , so according to a),

\[
R = \frac{1}{n}{\overline{\mathcal{F}}}_{d}\left\lbrack  {{\mathcal{F}}_{d}\left( R\right) }\right\rbrack   = \mathop{\sum }\limits_{{j = 0}}^{{n - 1}}\frac{\left\lbrack  {{\mathcal{F}}_{d}\left( R\right) }\right\rbrack  \left( {\omega }^{-j}\right) }{n}{X}^{j}.
\]

\( \left( {* * }\right) \)

> Or \( {\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}R\left( {\omega }^{i}\right) {\omega }^{-{ij}} \) , donc \( \left| {{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) }\right| \leq \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left| {R\left( {\omega }^{i}\right) }\right| \) , et \( R \) vérifiant (i) et (ii), cette dernière inégalité entraîne

However \( {\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) = \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}R\left( {\omega }^{i}\right) {\omega }^{-{ij}} \) , so \( \left| {{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) }\right| \leq \mathop{\sum }\limits_{{i = 0}}^{{n - 1}}\left| {R\left( {\omega }^{i}\right) }\right| \) , and \( R \) satisfying (i) and (ii), this last inequality implies

\[
\left| \frac{{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) }{n}\right|  \leq  \frac{n - 1}{n} < 1.
\]

\( \left( {* * * }\right) \)

> D’après \( \left( {* * }\right) \) , comme \( R \) est à coefficients entiers, on a \( \frac{1}{n}{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) \in \mathbb{Z} \) , donc d’après (***), \( \frac{1}{n}{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) = 0 \) , et ceci pour tout \( j,0 \leq j \leq n - 1 \) . De (**) on en déduit \( R = 0 \) et donc \( {X}^{n} - 1 \) divise \( P \) .

According to \( \left( {* * }\right) \) , since \( R \) has integer coefficients, we have \( \frac{1}{n}{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) \in \mathbb{Z} \) , so according to (***), \( \frac{1}{n}{\mathcal{F}}_{d}\left( R\right) \left( {\omega }^{-j}\right) = 0 \) , and this for all \( j,0 \leq j \leq n - 1 \) . From (**) we deduce \( R = 0 \) and therefore \( {X}^{n} - 1 \) divides \( P \) .

> Problem 2. 1/ Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) tel que \( \forall n \in \mathbb{N}, P\left( n\right) \in \mathbb{Z} \) .

Problem 2. 1/ Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) such that \( \forall n \in \mathbb{N}, P\left( n\right) \in \mathbb{Z} \) .

> a) Montrer que \( P \in \mathbb{Q}\left\lbrack X\right\rbrack \) .

a) Show that \( P \in \mathbb{Q}\left\lbrack X\right\rbrack \) .

> b) Plus précisément, si \( d = \deg \left( P\right) \) , montrer que \( d!P \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

b) More precisely, if \( d = \deg \left( P\right) \) , show that \( d!P \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

> 2 / Soit \( F \in \mathbb{C}\left( X\right) \) une fraction rationnelle telle que pour tout entier \( n \in \mathbb{N} \) qui n’est pas un pôle de \( F, F\left( n\right) \in \mathbb{Q} \) . Montrer que \( F \in \mathbb{Q}\left( X\right) \) .

2/ Let \( F \in \mathbb{C}\left( X\right) \) be a rational fraction such that for every integer \( n \in \mathbb{N} \) which is not a pole of \( F, F\left( n\right) \in \mathbb{Q} \) . Show that \( F \in \mathbb{Q}\left( X\right) \) .

> 3 / Soit \( F \in \mathbb{C}\left( X\right) \) une fraction rationnelle vérifiant : pour tout entier \( n \in \mathbb{N} \) qui n’est pas un pôle de \( F, F\left( n\right) \in \mathbb{Z} \) . Montrer que \( F \) est un polynôme de \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

3/ Let \( F \in \mathbb{C}\left( X\right) \) be a rational fraction satisfying: for every integer \( n \in \mathbb{N} \) which is not a pole of \( F, F\left( n\right) \in \mathbb{Z} \) . Show that \( F \) is a polynomial of \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> Solution. 1/ a) Si \( P \) est constant, le résultat est évident. Sinon \( d = \deg \left( P\right) \geq 1 \) . Considérons les polynômes d’interpolation de Lagrange \( {L}_{k} = \mathop{\prod }\limits_{\substack{{0 \leq i \leq d} \\ {i \neq k} }}\left( \frac{X - i}{k - i}\right) \) pour \( 0 \leq k \leq d \) , de sorte que si

Solution. 1/ a) If \( P \) is constant, the result is obvious. Otherwise \( d = \deg \left( P\right) \geq 1 \) . Consider the Lagrange interpolation polynomials \( {L}_{k} = \mathop{\prod }\limits_{\substack{{0 \leq i \leq d} \\ {i \neq k} }}\left( \frac{X - i}{k - i}\right) \) for \( 0 \leq k \leq d \) , such that if

> \( j \in \mathbb{N},0 \leq j \leq d,{L}_{k}\left( j\right) = 0 \) si \( j \neq k \) et \( {L}_{k}\left( k\right) = 1 \) . Le polynôme \( Q = \mathop{\sum }\limits_{{k = 0}}^{d}P\left( k\right) {L}_{k} \) prend les mêmes valeurs que \( P \) aux \( d + 1 \) points \( 0,1,\ldots , d \) . Autrement dit, \( P - Q \) s’annule en \( d + 1 \) points. Or \( \deg \left( {P - Q}\right) \leq d \) , donc \( P - Q = 0 \) , et donc \( P = Q = \mathop{\sum }\limits_{{k = 0}}^{d}P\left( k\right) {L}_{k} \in \mathbb{Q}\left\lbrack X\right\rbrack \) car \( P\left( k\right) \in \mathbb{Z} \) et \( {L}_{k} \in \mathbb{Q}\left\lbrack X\right\rbrack \)

\( j \in \mathbb{N},0 \leq j \leq d,{L}_{k}\left( j\right) = 0 \) if \( j \neq k \) and \( {L}_{k}\left( k\right) = 1 \) . The polynomial \( Q = \mathop{\sum }\limits_{{k = 0}}^{d}P\left( k\right) {L}_{k} \) takes the same values as \( P \) at the \( d + 1 \) points \( 0,1,\ldots , d \) . In other words, \( P - Q \) vanishes at \( d + 1 \) points. However \( \deg \left( {P - Q}\right) \leq d \) , so \( P - Q = 0 \) , and thus \( P = Q = \mathop{\sum }\limits_{{k = 0}}^{d}P\left( k\right) {L}_{k} \in \mathbb{Q}\left\lbrack X\right\rbrack \) because \( P\left( k\right) \in \mathbb{Z} \) and \( {L}_{k} \in \mathbb{Q}\left\lbrack X\right\rbrack \)

> b) Il suffit s’écrire \( d!{L}_{k} = {\left( -1\right) }^{d - k}\frac{d!}{k!\left( {d - k}\right) !}\mathop{\prod }\limits_{\substack{{0 \leq i \leq d} \\ {i \neq k} }}\left( {X - i}\right) = {\left( -1\right) }^{d - k}\left( \begin{array}{l} d \\ k \end{array}\right) \mathop{\prod }\limits_{\substack{{0 \leq i \leq d} \\ {i \neq k} }}\left( {X - i}\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) donc \( d!P = \mathop{\sum }\limits_{{k = 0}}^{d}P\left( k\right) \cdot d!{L}_{k} \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

b) It suffices to write \( d!{L}_{k} = {\left( -1\right) }^{d - k}\frac{d!}{k!\left( {d - k}\right) !}\mathop{\prod }\limits_{\substack{{0 \leq i \leq d} \\ {i \neq k} }}\left( {X - i}\right) = {\left( -1\right) }^{d - k}\left( \begin{array}{l} d \\ k \end{array}\right) \mathop{\prod }\limits_{\substack{{0 \leq i \leq d} \\ {i \neq k} }}\left( {X - i}\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) therefore \( d!P = \mathop{\sum }\limits_{{k = 0}}^{d}P\left( k\right) \cdot d!{L}_{k} \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

> Remarque : On ne peut pas faire mieux. Par exemple, \( P = X\left( {X - 1}\right) \cdots \left( {X - d + 1}\right) /d \) ! est de degré \( d \) et vérifie \( \forall n \in \mathbb{N}, P\left( n\right) \in \mathbb{Z} \) .

Remark: We cannot do better. For example, \( P = X\left( {X - 1}\right) \cdots \left( {X - d + 1}\right) /d \) ! is of degree \( d \) and satisfies \( \forall n \in \mathbb{N}, P\left( n\right) \in \mathbb{Z} \) .

> 2 / Nous allons montrer le résultat plus fort suivant : si \( F \in \mathbb{C}\left( X\right) \) est tel que \( F\left( n\right) \in \mathbb{Q} \) pour une infinité d’entiers naturels \( n \) , alors \( F \in \mathbb{Q}\left( X\right) \) .

2 / We will show the following stronger result: if \( F \in \mathbb{C}\left( X\right) \) is such that \( F\left( n\right) \in \mathbb{Q} \) for an infinite number of natural integers \( n \) , then \( F \in \mathbb{Q}\left( X\right) \) .

> En notant \( F = P/Q \) la forme réduite de \( F \) , où \( P \) et \( Q \in \mathbb{C}\left\lbrack X\right\rbrack \) sont premiers entre eux, nous allons prouver le résultat par récurrence sur \( r = \deg \left( P\right) + \deg \left( Q\right) \) (si \( F = 0 \) , il n’y a rien à montrer).

By denoting \( F = P/Q \) as the reduced form of \( F \) , where \( P \) and \( Q \in \mathbb{C}\left\lbrack X\right\rbrack \) are coprime, we will prove the result by induction on \( r = \deg \left( P\right) + \deg \left( Q\right) \) (if \( F = 0 \) , there is nothing to show).

> - Lorsque \( r = 0, P \) et \( Q \) sont constants et le résultat est évident.

- When \( r = 0, P \) and \( Q \) are constant, the result is obvious.

> - Supposons le résultat vrai jusqu’au rang \( r - 1 \) et montrons le au rang \( r \) . Quitte à considérer \( 1/F \) , on peut supposer \( \deg \left( P\right)  \geq  \deg \left( Q\right) \) . Soit \( a \in  \mathbb{N} \) tel que \( P\left( a\right) /Q\left( a\right)  \in  \mathbb{Q} \) . Notons

- Suppose the result is true up to rank \( r - 1 \) and show it for rank \( r \) . By considering \( 1/F \) , we can assume \( \deg \left( P\right)  \geq  \deg \left( Q\right) \) . Let \( a \in  \mathbb{N} \) be such that \( P\left( a\right) /Q\left( a\right)  \in  \mathbb{Q} \) . Let us denote

\[
G = \frac{1}{X - a}\left\lbrack  {F\left( X\right)  - \frac{P\left( a\right) }{Q\left( a\right) }}\right\rbrack   = \frac{{P}^{ * }}{Q}\;\text{ où }\;{P}^{ * }\left( X\right)  = \frac{P\left( X\right) Q\left( a\right)  - Q\left( X\right) P\left( a\right) }{Q\left( a\right) \left( {X - a}\right) }.
\]

On a \( {P}^{ * } \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( \deg \left( {P}^{ * }\right) < \deg \left( P\right) \) . De plus \( G\left( n\right) \in \mathbb{Q} \) pour une infinité de \( n \in \mathbb{N} \) . On peut donc appliquer l’hypothèse de récurrence qui entraîne \( G \in \mathbb{Q}\left( X\right) \) . Donc \( F = \left( {X - a}\right) G + \; P\left( a\right) /Q\left( a\right) \in \mathbb{Q}\left( X\right) . \)

> We have \( {P}^{ * } \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( \deg \left( {P}^{ * }\right) < \deg \left( P\right) \) . Furthermore, \( G\left( n\right) \in \mathbb{Q} \) for an infinite number of \( n \in \mathbb{N} \) . We can therefore apply the induction hypothesis which implies \( G \in \mathbb{Q}\left( X\right) \) . Thus \( F = \left( {X - a}\right) G + \; P\left( a\right) /Q\left( a\right) \in \mathbb{Q}\left( X\right) . \)

3/ D’après \( 2/, F \in \mathbb{Q}\left( X\right) \) . Écrivons \( F = E + P/Q \) , où \( E, P \) et \( Q \) sont des polynômes de \( \mathbb{Q}\left\lbrack X\right\rbrack \) avec \( \deg \left( P\right) < \deg \left( Q\right) \) . Soit \( \alpha \in {\mathbb{N}}^{ * } \) tel que \( {\alpha E} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Comme \( \deg \left( P\right) < \deg \left( Q\right) \) on a \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( n\right) /Q\left( n\right) = 0 \) et donc il existe \( N > 0 \) tel que pour tout \( n > N,\left| {{\alpha P}\left( n\right) /Q\left( n\right) }\right| < 1 \) . Or \( {\alpha E} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , donc pour tout \( n \in \mathbb{N}, n > N,{\alpha P}\left( n\right) /Q\left( n\right) = {\alpha F}\left( n\right) - {\alpha E}\left( n\right) \in \mathbb{Z} \) . On en déduit \( P\left( n\right) = 0 \) pour tout \( n \in \mathbb{N} \) tel que \( n > N \) . Ceci implique \( P = 0 \) et donc \( F = E \in \mathbb{Q}\left\lbrack X\right\rbrack \) .

> 3/ According to \( 2/, F \in \mathbb{Q}\left( X\right) \) . Let us write \( F = E + P/Q \) , where \( E, P \) and \( Q \) are polynomials of \( \mathbb{Q}\left\lbrack X\right\rbrack \) with \( \deg \left( P\right) < \deg \left( Q\right) \) . Let \( \alpha \in {\mathbb{N}}^{ * } \) be such that \( {\alpha E} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Since \( \deg \left( P\right) < \deg \left( Q\right) \) we have \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}P\left( n\right) /Q\left( n\right) = 0 \) and thus there exists \( N > 0 \) such that for all \( n > N,\left| {{\alpha P}\left( n\right) /Q\left( n\right) }\right| < 1 \) . However \( {\alpha E} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , so for all \( n \in \mathbb{N}, n > N,{\alpha P}\left( n\right) /Q\left( n\right) = {\alpha F}\left( n\right) - {\alpha E}\left( n\right) \in \mathbb{Z} \) . We deduce \( P\left( n\right) = 0 \) for all \( n \in \mathbb{N} \) such that \( n > N \) . This implies \( P = 0 \) and thus \( F = E \in \mathbb{Q}\left\lbrack X\right\rbrack \) .

Problem 3. Soit \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n - 1}X + {a}_{n} \in \mathbb{C}\left\lbrack X\right\rbrack \) . On note \( \rho \geq 0 \) le plus grand des modules des racines de \( P \) , et on suppose que les \( {a}_{i} \) ne sont pas tous nuls, de sorte que \( \rho \neq 0 \) .

> Problem 3. Let \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n - 1}X + {a}_{n} \in \mathbb{C}\left\lbrack X\right\rbrack \) . We denote by \( \rho \geq 0 \) the largest of the moduli of the roots of \( P \) , and we assume that the \( {a}_{i} \) are not all zero, so that \( \rho \neq 0 \) .

1 / a) Montrer que \( \rho \leq \sup \left\{ {1,\mathop{\sum }\limits_{{i = 1}}^{n}\left| {a}_{i}\right| }\right\} \) .

> 1 / a) Show that \( \rho \leq \sup \left\{ {1,\mathop{\sum }\limits_{{i = 1}}^{n}\left| {a}_{i}\right| }\right\} \) .

b) Montrer que \( \rho \leq 1 + \mathop{\sup }\limits_{{1 \leq i \leq n}}\left| {a}_{i}\right| \) .

> b) Show that \( \rho \leq 1 + \mathop{\sup }\limits_{{1 \leq i \leq n}}\left| {a}_{i}\right| \) .

2 / a) On pose \( f\left( x\right) = {x}^{n} - \left( {\left| {a}_{1}\right| {x}^{n - 1} + \cdots + \left| {a}_{n - 1}\right| x + \left| {a}_{n}\right| }\right) \) . Montrer que \( f \) admet une unique racine strictement positive \( \alpha \) , que si \( 0 < x < \alpha \) alors \( f\left( x\right) < 0 \) , et que si \( x > \alpha \) alors \( f\left( x\right) > 0 \) . Prouver ensuite \( \left( {{2}^{1/n} - 1}\right) \alpha \leq \rho \leq \alpha \) .

> 2 / a) Let \( f\left( x\right) = {x}^{n} - \left( {\left| {a}_{1}\right| {x}^{n - 1} + \cdots + \left| {a}_{n - 1}\right| x + \left| {a}_{n}\right| }\right) \) . Show that \( f \) admits a unique strictly positive root \( \alpha \) , that if \( 0 < x < \alpha \) then \( f\left( x\right) < 0 \) , and that if \( x > \alpha \) then \( f\left( x\right) > 0 \) . Then prove \( \left( {{2}^{1/n} - 1}\right) \alpha \leq \rho \leq \alpha \) .

b) Si \( R = \mathop{\sup }\limits_{{1 \leq k \leq n}}{\left| {a}_{k}\right| }^{1/k} \) , montrer \( R/n \leq \rho \leq {2R} \) .

> b) If \( R = \mathop{\sup }\limits_{{1 \leq k \leq n}}{\left| {a}_{k}\right| }^{1/k} \) , show \( R/n \leq \rho \leq {2R} \) .

Solution. 1/a) Si \( \rho \leq 1 \) , c’est terminé. Sinon, considérons \( \alpha \in \mathbb{C} \) une racine de \( P \) telle que \( \left| \alpha \right| = \rho \) . L’égalité \( P\left( \alpha \right) = 0 \) s’écrit aussi \( {\alpha }^{n} = - {a}_{1}{\alpha }^{n - 1} - \cdots - {a}_{n - 1}\alpha - {a}_{n} \) , donc

> Solution. 1/a) If \( \rho \leq 1 \) , it is finished. Otherwise, let us consider \( \alpha \in \mathbb{C} \) a root of \( P \) such that \( \left| \alpha \right| = \rho \) . The equality \( P\left( \alpha \right) = 0 \) can also be written as \( {\alpha }^{n} = - {a}_{1}{\alpha }^{n - 1} - \cdots - {a}_{n - 1}\alpha - {a}_{n} \) , therefore

\[
\alpha  =  - {a}_{1} - \frac{{a}_{2}}{\alpha } - \cdots  - \frac{{a}_{n - 1}}{{\alpha }^{n - 2}} - \frac{{a}_{n}}{{\alpha }^{n - 1}},
\]

ce qui entraîne

> which leads to

\[
\rho  = \left| \alpha \right|  \leq  \left| {a}_{1}\right|  + \frac{\left| {a}_{2}\right| }{\rho } + \cdots  + \frac{\left| {a}_{n}\right| }{{\rho }^{n - 1}}.
\]

(*)

> Comme \( \rho \geq 1 \) , on en déduit \( \rho \leq \left| {a}_{1}\right| + \left| {a}_{2}\right| + \cdots + \left| {a}_{n}\right| \) .

Since \( \rho \geq 1 \) , we deduce \( \rho \leq \left| {a}_{1}\right| + \left| {a}_{2}\right| + \cdots + \left| {a}_{n}\right| \) .

> b) Si \( \rho \leq 1 \) , c’est terminé. Sinon, en posant \( a = \mathop{\sup }\limits_{{1 \leq i \leq n}}\left| {a}_{i}\right| \) , l’inégalité (*) entraîne

b) If \( \rho \leq 1 \) , it is finished. Otherwise, by setting \( a = \mathop{\sup }\limits_{{1 \leq i \leq n}}\left| {a}_{i}\right| \) , the inequality (*) leads to

\[
\rho  \leq  a + \frac{a}{\rho } + \cdots  + \frac{a}{{\rho }^{n - 1}} \leq  a\left( {\mathop{\sum }\limits_{{p = 0}}^{{+\infty }}\frac{1}{{\rho }^{p}}}\right)  = \frac{a}{1 - 1/\rho }
\]

et donc \( \rho - 1 \leq a \) d’où \( \rho \leq 1 + a \) .

> and thus \( \rho - 1 \leq a \) from which \( \rho \leq 1 + a \) .

2/a) La fonction \( g\left( x\right) = f\left( x\right) /{x}^{n} \) est croissante (somme de fonctions croissantes) strictement sur ] \( 0, + \infty \left\lbrack \right. \) . De plus, \( \mathop{\lim }\limits_{{x \rightarrow {0}^{ + }}}g\left( x\right) = - \infty \; \) et \( \;\mathop{\lim }\limits_{{x \rightarrow + \infty }}g\left( x\right) = 1 \) . Ceci montre qu’il existe \( a > 0 \) et \( b > a \) tels que \( g\left( a\right) < 0 \) et \( g\left( b\right) > 0 \) . D’après le théorème des valeurs intermédiaires, il existe donc \( \alpha > 0 \) (compris entre \( a \) et \( b \) ) tel que \( g\left( \alpha \right) = 0 \) . Comme \( g \) est strictement croissante, on a \( g\left( x\right) < 0 \) pour \( 0 < x < \alpha \) et \( g\left( x\right) > 0 \) pour \( x > \alpha \) . Comme \( f\left( x\right) = {x}^{n}g\left( x\right) \) , on en déduit

> 2/a) The function \( g\left( x\right) = f\left( x\right) /{x}^{n} \) is strictly increasing (sum of increasing functions) on ] \( 0, + \infty \left\lbrack \right. \) . Furthermore, \( \mathop{\lim }\limits_{{x \rightarrow {0}^{ + }}}g\left( x\right) = - \infty \; \) and \( \;\mathop{\lim }\limits_{{x \rightarrow + \infty }}g\left( x\right) = 1 \) . This shows that there exist \( a > 0 \) and \( b > a \) such that \( g\left( a\right) < 0 \) and \( g\left( b\right) > 0 \) . According to the intermediate value theorem, there exists \( \alpha > 0 \) (between \( a \) and \( b \) ) such that \( g\left( \alpha \right) = 0 \) . Since \( g \) is strictly increasing, we have \( g\left( x\right) < 0 \) for \( 0 < x < \alpha \) and \( g\left( x\right) > 0 \) for \( x > \alpha \) . Since \( f\left( x\right) = {x}^{n}g\left( x\right) \) , we deduce

\[
f\left( \alpha \right)  = 0,\;f\left( x\right)  < 0\text{ pour }0 < x < \alpha ,\;f\left( x\right)  > 0\text{ pour }x > \alpha .
\]

(**)

> Ceci étant, l’inégalité \( \left( *\right) \) entraîne \( f\left( \rho \right) \leq 0 \) , d’où on tire \( \rho \leq \alpha \) d’après \( \left( {* * }\right) \) .

That being said, the inequality \( \left( *\right) \) implies \( f\left( \rho \right) \leq 0 \), from which we derive \( \rho \leq \alpha \) according to \( \left( {* * }\right) \).

> Il reste à prouver l’inégalité \( \left( {{2}^{1/n} - 1}\right) \alpha \leq \rho \) . L’expression des coefficients d’un polynôme en fonction de ses racines montre que \( \left| {a}_{k}\right| \leq \left( \begin{array}{l} n \\ k \end{array}\right) {\rho }^{k} \) pour \( 1 \leq k \leq n \) , donc

It remains to prove the inequality \( \left( {{2}^{1/n} - 1}\right) \alpha \leq \rho \). The expression of a polynomial's coefficients in terms of its roots shows that \( \left| {a}_{k}\right| \leq \left( \begin{array}{l} n \\ k \end{array}\right) {\rho }^{k} \) for \( 1 \leq k \leq n \), therefore

\[
\forall x > 0,\;\mathop{\sum }\limits_{{k = 1}}^{n}\left| {a}_{k}\right| {x}^{n - k} \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {\rho }^{k}{x}^{n - k} = {\left( \rho  + x\right) }^{n} - {x}^{n},
\]

ce qui entraîne

> which implies

\[
\forall x > 0,\;f\left( x\right)  \geq  {x}^{n} - \left( {{\left( \rho  + x\right) }^{n} - {x}^{n}}\right)  = 2{x}^{n} - {\left( \rho  + x\right) }^{n}.
\]

Le terme \( 2{x}^{n} - {\left( \rho + x\right) }^{n} \) s’annule lorsque \( {2}^{1/n}x = \rho + x \) , c’est-à-dire lorsque \( x = \frac{\rho }{{2}^{1/n} - 1} \) . Ainsi, \( f\left( \frac{\rho }{{2}^{1/n} - 1}\right) \geq 0 \) et on en déduit grâce à \( \left( {* * }\right) \) que \( \frac{\rho }{{2}^{1/n} - 1} \geq \alpha \) , ou encore \( \rho \geq \left( {{2}^{1/n} - 1}\right) \alpha \) .

> The term \( 2{x}^{n} - {\left( \rho + x\right) }^{n} \) vanishes when \( {2}^{1/n}x = \rho + x \), that is to say when \( x = \frac{\rho }{{2}^{1/n} - 1} \). Thus, \( f\left( \frac{\rho }{{2}^{1/n} - 1}\right) \geq 0 \) and we deduce from \( \left( {* * }\right) \) that \( \frac{\rho }{{2}^{1/n} - 1} \geq \alpha \), or also \( \rho \geq \left( {{2}^{1/n} - 1}\right) \alpha \).

b) Pour montrer \( \rho \leq {2R} \) il suffit de montrer \( \alpha \leq {2R} \) d’après la question précédente. En vertu de l’assertion \( \left( {* * }\right) \) , on se ramène donc à prouver que \( f\left( {2R}\right) \geq 0 \) . Par définition de \( R \) , on a \( \left| {a}_{k}\right| \leq {R}^{k} \) pour tout \( k,1 \leq k \leq n \) . Si \( r = {2R} \) , on a donc \( \left| {a}_{k}\right| {r}^{n - k} \leq {r}^{n}/{2}^{k} \) , d’où

> b) To show \( \rho \leq {2R} \), it suffices to show \( \alpha \leq {2R} \) according to the previous question. By virtue of assertion \( \left( {* * }\right) \), we are thus reduced to proving that \( f\left( {2R}\right) \geq 0 \). By definition of \( R \), we have \( \left| {a}_{k}\right| \leq {R}^{k} \) for all \( k,1 \leq k \leq n \). If \( r = {2R} \), we therefore have \( \left| {a}_{k}\right| {r}^{n - k} \leq {r}^{n}/{2}^{k} \), whence

\[
\left| {a}_{1}\right| {r}^{n - 1} + \cdots  + \left| {a}_{n - 1}\right| r + \left| {a}_{n}\right|  \leq  {r}^{n}\left( {\frac{1}{2} + \cdots  + \frac{1}{{2}^{n}}}\right)  \leq  {r}^{n},
\]

d’où \( f\left( r\right) = f\left( {2R}\right) \geq 0 \) . - Montrons \( R/n \leq \rho \) . On a vu plus haut que \( \left| {a}_{k}\right| \leq \left( \begin{array}{l} n \\ k \end{array}\right) {\rho }^{k} \) pour \( 1 \leq k \leq n \) . Or \( \left( \begin{array}{l} n \\ k \end{array}\right) = \; n\cdots \left( {n - k + 1}\right) /k! \leq {n}^{k} \) , donc \( \left| {a}_{k}\right| \leq {n}^{k}{\rho }^{k} \) , donc si \( 1 \leq k \leq n,\frac{{\left| {a}_{k}\right| }^{1/k}}{n} \leq \rho \) , d’où le résultat.

> whence \( f\left( r\right) = f\left( {2R}\right) \geq 0 \). - Let us show \( R/n \leq \rho \). We saw above that \( \left| {a}_{k}\right| \leq \left( \begin{array}{l} n \\ k \end{array}\right) {\rho }^{k} \) for \( 1 \leq k \leq n \). However, \( \left( \begin{array}{l} n \\ k \end{array}\right) = \; n\cdots \left( {n - k + 1}\right) /k! \leq {n}^{k} \), therefore \( \left| {a}_{k}\right| \leq {n}^{k}{\rho }^{k} \), so if \( 1 \leq k \leq n,\frac{{\left| {a}_{k}\right| }^{1/k}}{n} \leq \rho \), whence the result.

PROBLEME 4 (THÉORÉME FONDAMENTAL DE L'ALGÉBRE). Le but du problème est de provver que tout polynôme de \( \mathbb{C}\left\lbrack X\right\rbrack \) de degré \( \geq 1 \) admet au moins une racine dans \( \mathbb{C} \) , c'est-à-dire que le corps \( \mathbb{C} \) est algébriquement clos.

> PROBLEM 4 (FUNDAMENTAL THEOREM OF ALGEBRA). The goal of the problem is to prove that every polynomial of \( \mathbb{C}\left\lbrack X\right\rbrack \) of degree \( \geq 1 \) admits at least one root in \( \mathbb{C} \), that is to say that the field \( \mathbb{C} \) is algebraically closed.

1 / Première méthode. Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) , unitaire, \( \deg \left( P\right) \geq 1 \) .

> 1 / First method. Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) be monic, \( \deg \left( P\right) \geq 1 \) .

a) Montrer qu’il existe \( {z}_{0} \in \mathbb{C} \) tel que \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in \mathbb{C}}}\left| {P\left( z\right) }\right| \) .

> a) Show that there exists \( {z}_{0} \in \mathbb{C} \) such that \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in \mathbb{C}}}\left| {P\left( z\right) }\right| \) .

b) Montrer que \( P\left( {z}_{0}\right) = 0 \) .

> b) Show that \( P\left( {z}_{0}\right) = 0 \) .

2/ Seconde méthode. Soit \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) unitaire, \( d = \deg \left( P\right) = {2}^{n}q \) avec \( q \) impair et \( d \geq 1 \) . On veut montrer par récurrence sur \( n \in \mathbb{N} \) que \( P \) admet au moins une racine dans \( \mathbb{C} \) . a) \( \alpha \) ) Montrer le résultat pour \( n = 0 \) .

> 2/ Second method. Let \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) be monic, \( d = \deg \left( P\right) = {2}^{n}q \) with \( q \) odd and \( d \geq 1 \) . We want to show by induction on \( n \in \mathbb{N} \) that \( P \) has at least one root in \( \mathbb{C} \) . a) \( \alpha \) ) Show the result for \( n = 0 \) .

\( \beta ) \) Supposons le résultat vrai jusqu’au rang \( n - 1 \) . On sait (voir le théorème 5 page 66) qu’il existe une extension de corps \( \mathbb{K} \) de \( \mathbb{C} \) et \( {x}_{1},\ldots ,{x}_{d} \in \mathbb{K} \) tels que \( P = \mathop{\prod }\limits_{{i = 1}}^{d}\left( {X - {x}_{i}}\right) \) . Pour tout \( c \in \mathbb{R} \) et pour \( 1 \leq i < j \leq d \) , on pose \( {y}_{i, j}\left( c\right) = {x}_{i} + {x}_{j} + c{x}_{i}{x}_{j} \) . Montrer que pour tout \( c \in \mathbb{R} \) , il existe \( \left( {{i}_{c},{j}_{c}}\right) \) tels que \( {y}_{{i}_{c},{j}_{c}}\left( c\right) \in \mathbb{C} \) .

> \( \beta ) \) Assume the result is true up to rank \( n - 1 \) . We know (see theorem 5 on page 66) that there exists a field extension \( \mathbb{K} \) of \( \mathbb{C} \) and \( {x}_{1},\ldots ,{x}_{d} \in \mathbb{K} \) such that \( P = \mathop{\prod }\limits_{{i = 1}}^{d}\left( {X - {x}_{i}}\right) \) . For all \( c \in \mathbb{R} \) and for \( 1 \leq i < j \leq d \) , let \( {y}_{i, j}\left( c\right) = {x}_{i} + {x}_{j} + c{x}_{i}{x}_{j} \) . Show that for all \( c \in \mathbb{R} \) , there exist \( \left( {{i}_{c},{j}_{c}}\right) \) such that \( {y}_{{i}_{c},{j}_{c}}\left( c\right) \in \mathbb{C} \) .

\( \gamma ) \) Montrer qu’il existe \( c \in \mathbb{R} \) tel que \( {x}_{{i}_{c}} + {y}_{{i}_{c}} \) et \( {x}_{{i}_{c}}{y}_{{i}_{c}} \in \mathbb{C} \) . Conclure. b) En déduire le théorème fondamental de l'algèbre.

> \( \gamma ) \) Show that there exists \( c \in \mathbb{R} \) such that \( {x}_{{i}_{c}} + {y}_{{i}_{c}} \) and \( {x}_{{i}_{c}}{y}_{{i}_{c}} \in \mathbb{C} \) . Conclude. b) Deduce the fundamental theorem of algebra.

Solution. 1/ a) Écrivons \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{{n}_{1}}X + {a}_{n} \) . Pour tout \( z \in {\mathbb{C}}^{ * } \) , on a \( P\left( z\right) = {z}^{n}\left( {1 + \frac{{a}_{1}}{z} + \cdots + \frac{{a}_{n}}{{z}^{n}}}\right) \) , donc \( \mathop{\lim }\limits_{{\left| z\right| \rightarrow + \infty }}\left| {P\left( z\right) }\right| = + \infty \) , et donc il existe \( M > 0 \) tel que pour tout nombre complexe \( z \) tel que \( \left| z\right| > M \) , on ait \( \left| {P\left( z\right) }\right| > \left| {P\left( 0\right) }\right| \) . Ceci entraîne

> Solution. 1/ a) Let us write \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{{n}_{1}}X + {a}_{n} \) . For all \( z \in {\mathbb{C}}^{ * } \) , we have \( P\left( z\right) = {z}^{n}\left( {1 + \frac{{a}_{1}}{z} + \cdots + \frac{{a}_{n}}{{z}^{n}}}\right) \) , so \( \mathop{\lim }\limits_{{\left| z\right| \rightarrow + \infty }}\left| {P\left( z\right) }\right| = + \infty \) , and therefore there exists \( M > 0 \) such that for any complex number \( z \) such that \( \left| z\right| > M \) , we have \( \left| {P\left( z\right) }\right| > \left| {P\left( 0\right) }\right| \) . This implies

\[
\mathop{\inf }\limits_{{z \in  \mathbb{C}}}\left| {P\left( z\right) }\right|  = \mathop{\inf }\limits_{{\left| z\right|  \leq  M}}\left| {P\left( z\right) }\right| .
\]

Or \( K = \{ z \in \mathbb{C}\left| \right| z \mid \leq M\} \) , fermé borné de \( \mathbb{C} \) , est compact, et l’application \( z \mapsto \left| {P\left( z\right) }\right| \) étant continue, il existe \( {z}_{0} \in K \) tel que \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in K}}\left| {P\left( z\right) }\right| \) . On a donc \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in \mathbb{C}}}\left| {P\left( z\right) }\right| \) .

> Since \( K = \{ z \in \mathbb{C}\left| \right| z \mid \leq M\} \) is a closed bounded subset of \( \mathbb{C} \) , it is compact, and since the mapping \( z \mapsto \left| {P\left( z\right) }\right| \) is continuous, there exists \( {z}_{0} \in K \) such that \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in K}}\left| {P\left( z\right) }\right| \) . We therefore have \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in \mathbb{C}}}\left| {P\left( z\right) }\right| \) .

b) Raisonnons par l’absurde. Si \( P\left( {z}_{0}\right) \neq 0 \) , posons

> b) Let us reason by contradiction. If \( P\left( {z}_{0}\right) \neq 0 \) , let us set

\[
Q\left( X\right)  = \frac{P\left( {{z}_{0} + X}\right) }{P\left( {z}_{0}\right) } = \mathop{\sum }\limits_{{i = 0}}^{n}{b}_{i}{X}^{i}.
\]

Ici, \( {b}_{0} = Q\left( 0\right) = 1 \) et \( {b}_{n} \neq 0 \) , donc \( k = \inf \left\{ {i \in \mathbb{N},1 \leq i \leq n \mid {b}_{i} \neq 0}\right\} \) existe bien. On peut d'ailleurs écrire

> Here, \( {b}_{0} = Q\left( 0\right) = 1 \) and \( {b}_{n} \neq 0 \) , so \( k = \inf \left\{ {i \in \mathbb{N},1 \leq i \leq n \mid {b}_{i} \neq 0}\right\} \) does indeed exist. We can moreover write

\[
Q\left( z\right)  = 1 + {b}_{k}{z}^{k}\left( {1 + \varphi \left( z\right) }\right) \;\text{ avec }\;\mathop{\lim }\limits_{{z \rightarrow  0}}\varphi \left( z\right)  = 0.
\]

Soit \( r > 0 \) tel que \( \left| {\varphi \left( z\right) }\right| \leq 1/2 \) pour \( \left| z\right| \leq r \) . Écrivons \( {b}_{k} = \left| {b}_{k}\right| {e}^{i\theta },\theta \in \mathbb{R} \) . Soit \( z = r{e}^{-i\left( {\theta + \pi }\right) /k} \) . On a

> Let \( r > 0 \) be such that \( \left| {\varphi \left( z\right) }\right| \leq 1/2 \) for \( \left| z\right| \leq r \) . Let us write \( {b}_{k} = \left| {b}_{k}\right| {e}^{i\theta },\theta \in \mathbb{R} \) . Let \( z = r{e}^{-i\left( {\theta + \pi }\right) /k} \) . We have

\[
Q\left( z\right)  = 1 - \left| {b}_{k}\right| {r}^{k}\left( {1 + \varphi \left( z\right) }\right) .
\]

Quitte à diminuer \( r > 0 \) on peut supposer \( \left| {b}_{k}\right| {r}^{k} < 1 \) , et donc

> By potentially decreasing \( r > 0 \) we can assume \( \left| {b}_{k}\right| {r}^{k} < 1 \) , and therefore

\[
\left| {Q\left( z\right) }\right|  \leq  \left| {1 - \left| {b}_{k}\right| {r}^{k}}\right|  + \left| {{b}_{k}{r}^{k}\varphi \left( z\right) }\right|  \leq  \left( {1 - \left| {b}_{k}\right| {r}^{k}}\right)  + \frac{1}{2}\left| {b}_{k}\right| {r}^{k} = 1 - \frac{1}{2}\left| {b}_{k}\right| {r}^{k} < 1.
\]

Ceci prouve que \( \left| {P\left( {z + {z}_{0}}\right) }\right| /\left| {P\left( {z}_{0}\right) }\right| < 1 \) , donc que \( \left| {P\left( {z + {z}_{0}}\right) }\right| < \left| {P\left( {z}_{0}\right) }\right| \) , ce qui est absurde car \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in \mathbb{C}}}\left| {P\left( z\right) }\right| \) . On a donc bien \( P\left( {z}_{0}\right) = 0 \) .

> This proves that \( \left| {P\left( {z + {z}_{0}}\right) }\right| /\left| {P\left( {z}_{0}\right) }\right| < 1 \) , and thus that \( \left| {P\left( {z + {z}_{0}}\right) }\right| < \left| {P\left( {z}_{0}\right) }\right| \) , which is absurd because \( \left| {P\left( {z}_{0}\right) }\right| = \mathop{\inf }\limits_{{z \in \mathbb{C}}}\left| {P\left( z\right) }\right| \) . We therefore have indeed \( P\left( {z}_{0}\right) = 0 \) .

2/a) \( \alpha \) ) Si \( n = 0 \) , alors \( \deg \left( P\right) = q \) est impair. Le polynôme \( P \) étant à coefficient réels et unitaire, \( P\left( x\right) \) est équivalent à \( {x}^{q} \) lorsque \( x \rightarrow + \infty \) où lorsque \( x \rightarrow - \infty \) , donc \( q \) étant impair,

> 2/a) \( \alpha \) ) If \( n = 0 \) , then \( \deg \left( P\right) = q \) is odd. Since the polynomial \( P \) has real coefficients and is monic, \( P\left( x\right) \) is equivalent to \( {x}^{q} \) when \( x \rightarrow + \infty \) or when \( x \rightarrow - \infty \) , therefore \( q \) being odd,

\[
\mathop{\lim }\limits_{{x \rightarrow   + \infty }}P\left( x\right)  =  + \infty \;\text{ et }\;\mathop{\lim }\limits_{{x \rightarrow   - \infty }}P\left( x\right)  =  - \infty .
\]

On en déduit qu’il existe \( a \in {\mathbb{R}}^{ + } \) tel que \( P\left( a\right) > 0 \) et \( P\left( {-a}\right) < 0 \) . La fonction polynôme \( P \) étant continue sur \( \mathbb{R} \) , d’après le théorème des valeurs intermédiaires il existe \( c \in \rbrack - a, a\lbrack \) tel que \( P\left( c\right) = 0 \) . D’où \( \alpha ) \) .

> We deduce that there exists \( a \in {\mathbb{R}}^{ + } \) such that \( P\left( a\right) > 0 \) and \( P\left( {-a}\right) < 0 \) . Since the polynomial function \( P \) is continuous on \( \mathbb{R} \) , by the intermediate value theorem there exists \( c \in \rbrack - a, a\lbrack \) such that \( P\left( c\right) = 0 \) . Hence \( \alpha ) \) .

\( \beta ) \) Fixons \( c \in \mathbb{R} \) . Soit \( Q = \mathop{\prod }\limits_{{1 \leq i < j \leq d}}\left( {X - {y}_{i, j}\left( c\right) }\right) \) . Les coefficients de \( Q \) sont des polynômes symétriques à coefficients réels en les \( {x}_{i} \) , et donc (voir le théorème 1 page 84) ce sont des poly-nômes à coefficients réels en les fonctions symétriques élémentaires des \( {x}_{i} \) , qui sont eux mêmes les coefficients de \( P \) donc réels; ainsi, les coefficients de \( Q \) sont réels, c’est-à-dire \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) .

> \( \beta ) \) Let us fix \( c \in \mathbb{R} \) . Let \( Q = \mathop{\prod }\limits_{{1 \leq i < j \leq d}}\left( {X - {y}_{i, j}\left( c\right) }\right) \) . The coefficients of \( Q \) are symmetric polynomials with real coefficients in the \( {x}_{i} \) , and thus (see theorem 1 on page 84) they are polynomials with real coefficients in the elementary symmetric functions of the \( {x}_{i} \) , which are themselves the coefficients of \( P \) and therefore real; thus, the coefficients of \( Q \) are real, that is to say \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) .

On a \( \deg \left( Q\right) = \operatorname{Card}\{ \left( {i, j}\right) ,1 \leq i < j \leq d\} = \mathop{\sum }\limits_{{j = 1}}^{d}\left( {j - 1}\right) = d\left( {d - 1}\right) /2 = {2}^{n - 1}q\left( {d - 1}\right) \) , où \( q\left( {d - 1}\right) \) est impair (car \( q \) est impair et \( d \) est pair). On peut donc appliquer à \( Q \) l’hypothèse de récurrence, ce qui entraîne l’existence de \( \left( {{i}_{c},{j}_{c}}\right) \) tel que \( {y}_{{i}_{c},{j}_{c}}\left( c\right) \in \mathbb{C} \) .

> We have \( \deg \left( Q\right) = \operatorname{Card}\{ \left( {i, j}\right) ,1 \leq i < j \leq d\} = \mathop{\sum }\limits_{{j = 1}}^{d}\left( {j - 1}\right) = d\left( {d - 1}\right) /2 = {2}^{n - 1}q\left( {d - 1}\right) \) , where \( q\left( {d - 1}\right) \) is odd (because \( q \) is odd and \( d \) is even). We can therefore apply the induction hypothesis to \( Q \) , which implies the existence of \( \left( {{i}_{c},{j}_{c}}\right) \) such that \( {y}_{{i}_{c},{j}_{c}}\left( c\right) \in \mathbb{C} \) .

\( \gamma ) \) Notons \( \Gamma = \left\{ {\left( {i, j}\right) \in {\mathbb{N}}^{2},1 \leq i < j \leq d}\right\} \) . D’après la question \( \beta ) \) , on peut construire une application \( \mathbb{R} \rightarrow \Gamma \;c \mapsto \left( {{i}_{c},{j}_{c}}\right) \) telle que pour tout \( c \in \mathbb{R},{y}_{{i}_{c},{j}_{c}}\left( c\right) \in \mathbb{C} \) . Comme \( \mathbb{R} \) est infini et \( \Gamma \) fini, cette application n’est pas injective donc il existe \( \left( {c,{c}^{\prime }}\right) \in {\mathbb{R}}^{2} \) avec \( c \neq {c}^{\prime } \) , tels ques \( \left( {{i}_{c},{j}_{c}}\right) = \left( {{i}_{{c}^{\prime }},{j}_{{c}^{\prime }}}\right) \) . Posons \( \left( {r, s}\right) = \left( {{i}_{c},{j}_{c}}\right) \) . Du fait que

> \( \gamma ) \) Let us denote \( \Gamma = \left\{ {\left( {i, j}\right) \in {\mathbb{N}}^{2},1 \leq i < j \leq d}\right\} \) . According to question \( \beta ) \) , we can construct a map \( \mathbb{R} \rightarrow \Gamma \;c \mapsto \left( {{i}_{c},{j}_{c}}\right) \) such that for all \( c \in \mathbb{R},{y}_{{i}_{c},{j}_{c}}\left( c\right) \in \mathbb{C} \) . Since \( \mathbb{R} \) is infinite and \( \Gamma \) is finite, this map is not injective, so there exist \( \left( {c,{c}^{\prime }}\right) \in {\mathbb{R}}^{2} \) with \( c \neq {c}^{\prime } \) , such that \( \left( {{i}_{c},{j}_{c}}\right) = \left( {{i}_{{c}^{\prime }},{j}_{{c}^{\prime }}}\right) \) . Let us set \( \left( {r, s}\right) = \left( {{i}_{c},{j}_{c}}\right) \) . Due to the fact that

\[
\left( {{x}_{r} + {x}_{s}}\right)  + c\left( {{x}_{r}{x}_{s}}\right)  \in  \mathbb{C}\;\text{ et }\;\left( {{x}_{r} + {x}_{s}}\right)  + {c}^{\prime }\left( {{x}_{r}{x}_{c}}\right)  \in  \mathbb{C}
\]

avec \( c \neq {c}^{\prime } \) , on tire \( S = {x}_{r} + {x}_{s} \in \mathbb{C} \) et \( P = {x}_{r}{x}_{s} \in \mathbb{C} \) . Les éléments \( {x}_{r} \) et \( {x}_{s} \) sont donc les racines de \( {X}^{2} - {SX} + P \in \mathbb{C}\left\lbrack X\right\rbrack + \) , ce qui permet facilement de conclure que \( {x}_{r} \in \mathbb{C} \) et \( {x}_{s} \in \mathbb{C} \) . Le polynôme \( P \) a donc au moins une racine complexe (on en a même trouvé deux, \( {x}_{r} \) et \( {x}_{s} \) ).

> with \( c \neq {c}^{\prime } \) , we derive \( S = {x}_{r} + {x}_{s} \in \mathbb{C} \) and \( P = {x}_{r}{x}_{s} \in \mathbb{C} \) . The elements \( {x}_{r} \) and \( {x}_{s} \) are therefore the roots of \( {X}^{2} - {SX} + P \in \mathbb{C}\left\lbrack X\right\rbrack + \) , which easily allows us to conclude that \( {x}_{r} \in \mathbb{C} \) and \( {x}_{s} \in \mathbb{C} \) . The polynomial \( P \) therefore has at least one complex root (we have even found two, \( {x}_{r} \) and \( {x}_{s} \) ).

b) Le raisonnement par récurrence de a) prouve que tout polynôme à coefficients réels a au moins une racine dans \( \mathbb{C} \) . On veut maintenant prouver le résultat dans \( \mathbb{C}\left\lbrack X\right\rbrack \) . Soit \( F = \mathop{\sum }\limits_{{i = 0}}^{d}{a}_{i}{X}^{i} \in \; \mathbb{C}\left\lbrack X\right\rbrack \) . On pose \( \bar{F} = \mathop{\sum }\limits_{{i = 0}}^{d}\overline{{a}_{i}}{X}^{i} \) , et on voit que \( P = F\bar{F} \in \mathbb{R}\left\lbrack X\right\rbrack \) . Le polynôme \( P \) admet donc au moins une racine complexe \( \alpha \) , donc \( F\left( \alpha \right) \bar{F}\left( \alpha \right) = 0 \) , et donc \( F\left( \alpha \right) = 0 \) ou \( \bar{F}\left( \alpha \right) = 0 \) . Si \( F\left( \alpha \right) = 0 \) , c’est terminé, sinon \( \bar{F}\left( \alpha \right) = 0 \) donc \( F\left( \overline{\alpha }\right) = 0 \) , d’où le résultat.

> b) The reasoning by induction in a) proves that every polynomial with real coefficients has at least one root in \( \mathbb{C} \). We now want to prove the result in \( \mathbb{C}\left\lbrack X\right\rbrack \). Let \( F = \mathop{\sum }\limits_{{i = 0}}^{d}{a}_{i}{X}^{i} \in \; \mathbb{C}\left\lbrack X\right\rbrack \). We set \( \bar{F} = \mathop{\sum }\limits_{{i = 0}}^{d}\overline{{a}_{i}}{X}^{i} \), and we see that \( P = F\bar{F} \in \mathbb{R}\left\lbrack X\right\rbrack \). The polynomial \( P \) therefore admits at least one complex root \( \alpha \), so \( F\left( \alpha \right) \bar{F}\left( \alpha \right) = 0 \), and thus \( F\left( \alpha \right) = 0 \) or \( \bar{F}\left( \alpha \right) = 0 \). If \( F\left( \alpha \right) = 0 \), we are done; otherwise \( \bar{F}\left( \alpha \right) = 0 \) so \( F\left( \overline{\alpha }\right) = 0 \), hence the result.

Remarque. La deuxième méthode, plus longue, présente l'avantage de n'utiliser qu'une simple conséquence de la topologie : tout polynôme de \( \mathbb{R}\left\lbrack X\right\rbrack \) de degré impair admet une racine réelle, résultat connu au dix-huitième siècle.

> Remark. The second method, while longer, has the advantage of using only a simple consequence of topology: every polynomial in \( \mathbb{R}\left\lbrack X\right\rbrack \) of odd degree admits a real root, a result known in the eighteenth century.

Problem 5. Soit \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) un polynôme non constant tel que

> Problem 5. Let \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) be a non-constant polynomial such that

\[
\forall n \in  \mathbb{N},\exists m \in  \mathbb{N},\;P\left( n\right)  = {m}^{2}.
\]

1/a) Pour toute suite réelle \( u = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) , on note \( {\Delta u} = {\left( \Delta {u}_{n}\right) }_{n \in \mathbb{N}} \) la suite définie par \( \Delta {u}_{n} = {u}_{n + 1} - {u}_{n} \) . Ainsi défini, \( \Delta \) est un endomorphisme sur l’e.v. des suites réelles. D’après les hypothèses, il existe une suite \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) d’entiers naturels tels que \( P\left( n\right) = {f}_{n}^{2} \) pour tout \( n \in \mathbb{N} \) . En notant \( p = \deg P > 0 \) , montrer que pour tout \( k \in \mathbb{N},{\Delta }^{k}{f}_{n} = O\left( {n}^{p/2 - k}\right) \) . b) Montrer que \( {\Delta }^{p}{f}_{n} \) est nulle à partir d’un certain rang, et en déduire la forme de la suite \( \left( {f}_{n}\right) \) à partir d’un certain rang.

> 1/a) For any real sequence \( u = {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \), we denote by \( {\Delta u} = {\left( \Delta {u}_{n}\right) }_{n \in \mathbb{N}} \) the sequence defined by \( \Delta {u}_{n} = {u}_{n + 1} - {u}_{n} \). Defined this way, \( \Delta \) is an endomorphism on the vector space of real sequences. According to the hypotheses, there exists a sequence \( {\left( {f}_{n}\right) }_{n \in \mathbb{N}} \) of natural integers such that \( P\left( n\right) = {f}_{n}^{2} \) for all \( n \in \mathbb{N} \). By denoting \( p = \deg P > 0 \), show that for all \( k \in \mathbb{N},{\Delta }^{k}{f}_{n} = O\left( {n}^{p/2 - k}\right) \). b) Show that \( {\Delta }^{p}{f}_{n} \) is zero from a certain rank onwards, and deduce the form of the sequence \( \left( {f}_{n}\right) \) from a certain rank onwards.

2/ En déduire qu’il existe \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) tel que \( P = {Q}^{2} \) .

> 2/ Deduce that there exists \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( P = {Q}^{2} \).

Solution. 1/a) On écrit d’abord \( P \) sous la forme \( P = {a}_{0}{X}^{p} + {a}_{1}{X}^{p - 1} + \cdots + {a}_{p} \) avec \( {a}_{0} \neq 0 \) . Comme \( P \) est positif sur \( \mathbb{N} \) on a forcément \( {a}_{0} > 0 \) . On écrit ensuite

> Solution. 1/a) We first write \( P \) in the form \( P = {a}_{0}{X}^{p} + {a}_{1}{X}^{p - 1} + \cdots + {a}_{p} \) with \( {a}_{0} \neq 0 \). Since \( P \) is positive on \( \mathbb{N} \), we necessarily have \( {a}_{0} > 0 \). We then write

\[
\forall n \in  {\mathbb{N}}^{ * },\;{f}_{n} = \sqrt{P\left( n\right) } = {n}^{p/2}{\left( {a}_{0} + \frac{{a}_{1}}{n} + \cdots  + \frac{{a}_{p}}{{n}^{p}}\right) }^{1/2} = {n}^{p/2}g\left( {1/n}\right) ,
\]

où \( g\left( u\right) = {\left( {a}_{0} + {a}_{1}u + \cdots + {a}_{p}{u}^{p}\right) }^{1/2} \) est définie et de classe \( {\mathcal{C}}^{\infty } \) sur un voisinage de 0, donc admet un développement limité en 0 de la forme \( g\left( u\right) = {b}_{0} + {b}_{1}u + \cdots + {b}_{k - 1}{u}^{k - 1} + O\left( {u}^{k}\right) \) . Ainsi, lorsque \( n \) est suffisamment grand, on peut écrire

> where \( g\left( u\right) = {\left( {a}_{0} + {a}_{1}u + \cdots + {a}_{p}{u}^{p}\right) }^{1/2} \) is defined and of class \( {\mathcal{C}}^{\infty } \) on a neighborhood of 0, thus admits a Taylor expansion at 0 of the form \( g\left( u\right) = {b}_{0} + {b}_{1}u + \cdots + {b}_{k - 1}{u}^{k - 1} + O\left( {u}^{k}\right) \) . Thus, when \( n \) is sufficiently large, we can write

\[
{f}_{n} = \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{b}_{j}{n}^{p/2 - j} + O\left( {n}^{p/2 - k}\right) ,
\]

donc

> therefore

\[
{\Delta }^{k}{f}_{n} = \mathop{\sum }\limits_{{j = 0}}^{{k - 1}}{b}_{j}{\Delta }^{k}\left( {n}^{p/2 - j}\right)  + O\left( {n}^{p/2 - k}\right) .
\]

Nous allons prouver que pour tout \( \alpha \in \mathbb{R},{\Delta }^{k}{n}^{\alpha } = O\left( {n}^{\alpha - k}\right) \) ce qui prouvera le résultat souhaité compte tenu de l’estimation précédente. On procède par récurrence sur \( k \) . Pour \( k = 0 \) c’est immédiat. Supposons le résultat vérifié pour \( k \) et montrons le pour \( k + 1 \) . On écrit d’abord \( {\left( n + 1\right) }^{\alpha } - {n}^{\alpha } = {n}^{\alpha }{h}_{\alpha }\left( {1/n}\right) \) où \( {h}_{\alpha }\left( u\right) = {\left( 1 + u\right) }^{\alpha } - 1 \) est de classe \( {\mathcal{C}}^{\infty } \) sur un voisinage de 0, nulle en 0, donc on peut écrire \( {h}_{\alpha }\left( u\right) = {c}_{1}u + \cdots + {c}_{k}{u}^{k} + O\left( {u}^{k + 1}\right) \) , donc

> We will prove that for all \( \alpha \in \mathbb{R},{\Delta }^{k}{n}^{\alpha } = O\left( {n}^{\alpha - k}\right) \) which will prove the desired result given the previous estimate. We proceed by induction on \( k \) . For \( k = 0 \) it is immediate. Assume the result holds for \( k \) and show it for \( k + 1 \) . We first write \( {\left( n + 1\right) }^{\alpha } - {n}^{\alpha } = {n}^{\alpha }{h}_{\alpha }\left( {1/n}\right) \) where \( {h}_{\alpha }\left( u\right) = {\left( 1 + u\right) }^{\alpha } - 1 \) is of class \( {\mathcal{C}}^{\infty } \) on a neighborhood of 0, zero at 0, so we can write \( {h}_{\alpha }\left( u\right) = {c}_{1}u + \cdots + {c}_{k}{u}^{k} + O\left( {u}^{k + 1}\right) \) , therefore

\[
{\Delta }^{k + 1}{n}^{\alpha } = {\Delta }^{k}\left( {{\left( n + 1\right) }^{\alpha } - {n}^{\alpha }}\right)  = \mathop{\sum }\limits_{{j = 1}}^{k}{c}_{j}{\Delta }^{k}\left( {n}^{\alpha  - j}\right)  + O\left( {n}^{\alpha  - k - 1}\right) .
\]

L’hypothèse de récurrence entraîne \( {\Delta }^{k}\left( {n}^{\alpha - j}\right) = O\left( {n}^{\alpha - j - k}\right) \) , on en déduit que chaque terme de la somme précédente est un \( O\left( {n}^{\alpha - k - 1}\right) \) , donc \( {\Delta }^{k + 1}{n}^{\alpha } = O\left( {n}^{\alpha - k - 1}\right) \) , ce qui achève la récurrence.

> The induction hypothesis implies \( {\Delta }^{k}\left( {n}^{\alpha - j}\right) = O\left( {n}^{\alpha - j - k}\right) \) , we deduce that each term of the previous sum is a \( O\left( {n}^{\alpha - k - 1}\right) \) , thus \( {\Delta }^{k + 1}{n}^{\alpha } = O\left( {n}^{\alpha - k - 1}\right) \) , which completes the induction.

b) Comme \( \left( {f}_{n}\right) \) est une suite d’entiers, la suite \( \left( {{\Delta }^{p}{f}_{n}}\right) \) également. Or \( {\Delta }^{p}{f}_{n} = O\left( {n}^{-p/2}\right) \) d’après la question précédente, donc \( \left( {{\Delta }^{p}{f}_{n}}\right) \) converge vers 0, et comme cette suite est entière, elle est nulle à partir d’un certain rang \( N \) . Or une suite \( {\left( {u}_{n}\right) }_{n \geq N} \) verifiant \( {\Delta }^{p}{u}_{n} = 0 \) est forcément une suite polynomiale de degré \( < p \) . En effet, les suites \( {\left( {u}_{n}\right) }_{n \geq N} \) vérifiant \( {\Delta }^{p}u = 0 \) suivent une récurrence linéaire d’ordre \( p \) , donc elles forment un \( \mathbb{R} \) -espace vectoriel de dimension \( p \) . Par ailleurs toute suite polynomiale \( \left( {u}_{n}\right) \) de degré \( < p \) vérifie \( {\Delta }^{p}{u}_{n} = 0 \) (immédiat par récurrence sur \( p \) , car si \( {v}_{n} = F\left( n\right) \) est polynomiale de degré \( d \) alors \( \Delta {v}_{n} = {v}_{n + 1} - {v}_{n} = F\left( {n + 1}\right) - F\left( n\right) \) est polynomiale de degré \( d - 1 \) ), et comme les suites polynomiales de degré \( < p \) forment un e.v de dimension \( p \) on a bien déterminé l’ensemble des suites possibles. Donc \( {\left( {f}_{n}\right) }_{n \geq N} \) est polynomiale de degré \( < p \) .

> b) Since \( \left( {f}_{n}\right) \) is a sequence of integers, the sequence \( \left( {{\Delta }^{p}{f}_{n}}\right) \) is as well. However, \( {\Delta }^{p}{f}_{n} = O\left( {n}^{-p/2}\right) \) according to the previous question, so \( \left( {{\Delta }^{p}{f}_{n}}\right) \) converges to 0, and since this sequence is integer-valued, it is zero from a certain rank \( N \) onwards. Now, a sequence \( {\left( {u}_{n}\right) }_{n \geq N} \) satisfying \( {\Delta }^{p}{u}_{n} = 0 \) is necessarily a polynomial sequence of degree \( < p \) . Indeed, sequences \( {\left( {u}_{n}\right) }_{n \geq N} \) satisfying \( {\Delta }^{p}u = 0 \) follow a linear recurrence of order \( p \) , so they form a \( \mathbb{R} \) -vector space of dimension \( p \) . Furthermore, any polynomial sequence \( \left( {u}_{n}\right) \) of degree \( < p \) satisfies \( {\Delta }^{p}{u}_{n} = 0 \) (immediate by induction on \( p \) , because if \( {v}_{n} = F\left( n\right) \) is polynomial of degree \( d \) then \( \Delta {v}_{n} = {v}_{n + 1} - {v}_{n} = F\left( {n + 1}\right) - F\left( n\right) \) is polynomial of degree \( d - 1 \) ), and since polynomial sequences of degree \( < p \) form a vector space of dimension \( p \) , we have indeed determined the set of possible sequences. Thus \( {\left( {f}_{n}\right) }_{n \geq N} \) is polynomial of degree \( < p \) .

2 / La question précédente assure l’existence de \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) tel que \( {f}_{n} = Q\left( n\right) \) pour \( n \geq N \) . On a ainsi \( P\left( n\right) = {Q}^{2}\left( n\right) \) pour tout entier \( n \geq N \) , donc le polynôme \( P - {Q}^{2} \) s’annule une infinité de fois, donc est nul, donc \( P = {Q}^{2} \) est bien le carré d’un polynome.

> 2 / The previous question ensures the existence of \( Q \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( {f}_{n} = Q\left( n\right) \) for \( n \geq N \) . We thus have \( P\left( n\right) = {Q}^{2}\left( n\right) \) for every integer \( n \geq N \) , so the polynomial \( P - {Q}^{2} \) vanishes infinitely many times, and is therefore zero, so \( P = {Q}^{2} \) is indeed the square of a polynomial.

Remarque. Le polynôme \( Q \) vérifie également \( Q\left( n\right) \in \mathbb{Z} \) pour tout \( n \in \mathbb{N} \) donc d’après la partie 1/ du problème 2 page 88, on a \( d!Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) , où \( d = \deg Q \) .

> Remark. The polynomial \( Q \) also satisfies \( Q\left( n\right) \in \mathbb{Z} \) for all \( n \in \mathbb{N} \) , so according to part 1/ of problem 2 on page 88, we have \( d!Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) , where \( d = \deg Q \) .

- Nous aurions pu résoudre 1/a) en prouvant que \( f\left( x\right)  = \sqrt{P\left( x\right) } \) vérifie, pour \( x \) as-sez grand, l’existence de \( \theta  \in  \left\lbrack  {0,1}\right\rbrack \) tel que \( {\Delta }^{k}f\left( x\right)  = {f}^{\left( k\right) }\left( {x + {n\theta }}\right) \) (en procèdant par récurrence sur \( k \) à partir de l’égalité des accroissements finis), puis en montrant que \( {f}^{\left( k\right) }\left( x\right)  = O\left( {x}^{p/2 - k}\right) \) (par exemple par récurrence sur \( k \) en dérivant \( k \) fois l’égalité \( {f}^{2} = P \) ).

> - We could have solved 1/a) by proving that \( f\left( x\right)  = \sqrt{P\left( x\right) } \) satisfies, for sufficiently large \( x \), the existence of \( \theta  \in  \left\lbrack  {0,1}\right\rbrack \) such that \( {\Delta }^{k}f\left( x\right)  = {f}^{\left( k\right) }\left( {x + {n\theta }}\right) \) (by proceeding by induction on \( k \) starting from the mean value theorem), then by showing that \( {f}^{\left( k\right) }\left( x\right)  = O\left( {x}^{p/2 - k}\right) \) (for example by induction on \( k \) by differentiating the equality \( {f}^{2} = P \) \( k \) times).

PROBLEME 6 (EXISTENCE DE NOMBRES TRANSCENDANTS, NOMBRES DE LIOUVILLE). On rappelle qu’un nombre complexe \( \alpha \) est algébrique sur \( \mathbb{Q} \) si il existe un polynôme \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) non nul, tel que \( P\left( \alpha \right) = 0 \) . Dans le cas contraire, \( \alpha \) est dit transcendant. On se propose de prouver par deux méthodes différentes l'existence de nombres transcendants.

> PROBLEM 6 (EXISTENCE OF TRANSCENDENTAL NUMBERS, LIOUVILLE NUMBERS). Recall that a complex number \( \alpha \) is algebraic over \( \mathbb{Q} \) if there exists a non-zero polynomial \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) such that \( P\left( \alpha \right) = 0 \). Otherwise, \( \alpha \) is said to be transcendental. We propose to prove the existence of transcendental numbers using two different methods.

1/ Méthode non constructiviste. Montrer que l'ensemble des nombres réels algébriques sur Q est dénombrable. Conclure.

> 1/ Non-constructive method. Show that the set of real numbers algebraic over Q is countable. Conclude.

2 / Méthode constructiviste. a) Soit \( a \in \mathbb{R} \) algébrique sur \( \mathbb{Q} \) , racine de \( P \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( P\right) = \; n > 0 \) . Si \( a \notin \mathbb{Q} \) , montrer que

> 2/ Constructive method. a) Let \( a \in \mathbb{R} \) be algebraic over \( \mathbb{Q} \), a root of \( P \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( P\right) = \; n > 0 \). If \( a \notin \mathbb{Q} \), show that

\[
\exists \alpha  > 0,\forall \left( {p, q}\right)  \in  \mathbb{Z} \times  {\mathbb{N}}^{ * },\;\left| {a - \frac{p}{q}}\right|  \geq  \frac{\alpha }{{q}^{n}}.
\]

(Indication. On pourra remarquer que \( {q}^{n}P\left( {p/q}\right) \in \mathbb{Z} \) .)

> (Hint. One may note that \( {q}^{n}P\left( {p/q}\right) \in \mathbb{Z} \).)

b) (Nombres de Liouville). Soit \( a \in \mathbb{R}, a \notin \mathbb{Q} \) , tel que

> b) (Liouville numbers). Let \( a \in \mathbb{R}, a \notin \mathbb{Q} \), such that

\[
\forall k \in  {\mathbb{N}}^{ * },\exists \left( {p, q}\right)  \in  \mathbb{Z} \times  {\mathbb{N}}^{ * }, q \geq  2\;\text{ tel que }\left| {a - \frac{p}{q}}\right|  < \frac{1}{{q}^{k}}
\]

( \( a \) est appelé nombre de Liouville). Montrer que \( a \) est transcendant.

> (\( a \) is called a Liouville number). Show that \( a \) is transcendental.

c) Montrer que \( a = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{10}^{-k!} \) est un nombre de Liouville.

> c) Show that \( a = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{10}^{-k!} \) is a Liouville number.

Solution. 1/ Pour tout \( n \in {\mathbb{N}}^{ * } \) , notons \( {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{Z}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . L’application \( {\mathbb{Z}}^{n + 1} \rightarrow {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \;\left( {{a}_{0},\ldots ,{a}_{n}}\right) \mapsto {a}_{0} + \cdots + {a}_{n}{X}^{n} \) est bijective. Ainsi, \( {\mathbb{Z}}^{n + 1} \) étant dénombrable, \( {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \) est dénombrable, et donc \( \mathbb{Z}\left\lbrack X\right\rbrack = { \cup }_{n \in \mathbb{N}}{\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \) est dénombrable (réunion dénombrable d'ensembles dénombrables).

> Solution. 1/ For all \( n \in {\mathbb{N}}^{ * } \), let us denote \( {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack = \{ P \in \mathbb{Z}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \). The map \( {\mathbb{Z}}^{n + 1} \rightarrow {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \;\left( {{a}_{0},\ldots ,{a}_{n}}\right) \mapsto {a}_{0} + \cdots + {a}_{n}{X}^{n} \) is bijective. Thus, \( {\mathbb{Z}}^{n + 1} \) being countable, \( {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \) is countable, and therefore \( \mathbb{Z}\left\lbrack X\right\rbrack = { \cup }_{n \in \mathbb{N}}{\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \) is countable (countable union of countable sets).

Pour tout \( P \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1 \) , l’ensemble noté \( R\left( P\right) \) des racines de \( P \) est fini. Si \( A \) désigne l’ensemble des nombres réels algébriques sur \( \mathbb{Q} \) , on a donc

> For any \( P \in \mathbb{Z}\left\lbrack X\right\rbrack ,\deg \left( P\right) \geq 1 \), the set denoted by \( R\left( P\right) \) of the roots of \( P \) is finite. If \( A \) denotes the set of real numbers algebraic over \( \mathbb{Q} \), we therefore have

\[
A = \mathop{\bigcup }\limits_{\substack{{P \in  \mathbb{Z}\left\lbrack  X\right\rbrack  } \\  {\deg \left( P\right)  \geq  1} }}R\left( P\right)
\]

et donc \( A \) est dénombrable (réunion dénombrable d’ensembles finis).

> and thus \( A \) is countable (countable union of finite sets).

L'ensemble des nombres réels n'étant pas dénombrable, on en déduit qu'il existe dans \( \mathbb{R} \) des nombres transcendants.

> Since the set of real numbers is not countable, we deduce that there exist transcendental numbers in \( \mathbb{R} \).

2 / a) On a \( P\left( a\right) = 0 \) et \( P \) n’a qu’un nombre fini de racines, donc

> 2 / a) We have \( P\left( a\right) = 0 \) and \( P \) has only a finite number of roots, so

\[
\left( {\exists \eta  > 0}\right) ,\forall x \in  \left\lbrack  {a - \eta , a + \eta }\right\rbrack  , x \neq  a,\;P\left( x\right)  \neq  0.
\]

- Si \( p/q \in  \left\lbrack  {a - \eta , a + \eta }\right\rbrack \) , alors \( p/q \neq  a \) (car \( a \notin  \mathbb{Q} \) par hypothèse), donc \( P\left( {p/q}\right)  \neq  0 \) . Or \( {q}^{n}P\left( {p/q}\right)  \in  \mathbb{Z} \) , et ce terme étant non nul, \( \left| {{q}^{n}P\left( {p/q}\right) }\right|  \geq  1 \) . D’après l’inégalité des accroissements finis, si \( M = \mathop{\sup }\limits_{{x \in  \left\lbrack  {a - \eta , a + \eta }\right\rbrack  }}\left| {{P}^{\prime }\left( x\right) }\right| \) , on a

> - If \( p/q \in  \left\lbrack  {a - \eta , a + \eta }\right\rbrack \), then \( p/q \neq  a \) (because \( a \notin  \mathbb{Q} \) by hypothesis), so \( P\left( {p/q}\right)  \neq  0 \). However, \( {q}^{n}P\left( {p/q}\right)  \in  \mathbb{Z} \), and since this term is non-zero, \( \left| {{q}^{n}P\left( {p/q}\right) }\right|  \geq  1 \). According to the mean value inequality, if \( M = \mathop{\sup }\limits_{{x \in  \left\lbrack  {a - \eta , a + \eta }\right\rbrack  }}\left| {{P}^{\prime }\left( x\right) }\right| \), we have

\[
\left| {P\left( \frac{p}{q}\right) }\right|  = \left| {P\left( \frac{p}{q}\right)  - P\left( a\right) }\right|  \leq  M\left| {\frac{p}{q} - a}\right| \;\text{ donc }\;\left| {\frac{p}{q} - a}\right|  \geq  \frac{1}{M}\left| {P\left( \frac{p}{q}\right) }\right|  \geq  \frac{1}{M{q}^{n}}.
\]

- Si \( p/q \notin  \left\lbrack  {a - \eta , a + \eta }\right\rbrack \) , alors \( \left| {p/q - a}\right|  > \eta  > \eta /{q}^{n} \) . On conclut de tout ceci que \( \alpha  = \inf \{ 1/M,\eta \} \) convient.

> - If \( p/q \notin  \left\lbrack  {a - \eta , a + \eta }\right\rbrack \), then \( \left| {p/q - a}\right|  > \eta  > \eta /{q}^{n} \). We conclude from all this that \( \alpha  = \inf \{ 1/M,\eta \} \) is suitable.

b) Supposons \( a \) algébrique. D’après la question précédente,

> b) Suppose \( a \) is algebraic. According to the previous question,

\[
\exists n \in  {\mathbb{N}}^{ * },\exists \alpha  > 0,\forall \left( {p, q}\right)  \in  \mathbb{Z} \times  {\mathbb{N}}^{ * },\;\left| {a - \frac{p}{q}}\right|  \geq  \frac{\alpha }{{q}^{n}}.
\]

Fixons \( k \in {\mathbb{N}}^{ * }, k \geq n \) , tel que \( {2}^{n - k} < \alpha \) . Par hypothèse, il existe \( \left( {p, q}\right) \in \mathbb{Z} \times {\mathbb{N}}^{ * }, q \geq 2 \) , tel que \( \left| {a - p/q}\right| < 1/{q}^{k} \) . On a donc \( \alpha /{q}^{n} \leq \left| {a - p/q}\right| < 1/{q}^{k} \) , donc \( \alpha < {q}^{n - k} \leq {2}^{n - k} < \alpha \) , ce qui est absurde. Le nombre réel \( a \) est donc transcendant.

> Let us fix \( k \in {\mathbb{N}}^{ * }, k \geq n \), such that \( {2}^{n - k} < \alpha \). By hypothesis, there exists \( \left( {p, q}\right) \in \mathbb{Z} \times {\mathbb{N}}^{ * }, q \geq 2 \), such that \( \left| {a - p/q}\right| < 1/{q}^{k} \). We therefore have \( \alpha /{q}^{n} \leq \left| {a - p/q}\right| < 1/{q}^{k} \), so \( \alpha < {q}^{n - k} \leq {2}^{n - k} < \alpha \), which is absurd. The real number \( a \) is therefore transcendental.

c) Le développement décimal de \( a \) n’est pas périodique, donc \( a \notin \mathbb{Q} \) .

> c) The decimal expansion of \( a \) is not periodic, so \( a \notin \mathbb{Q} \).

Soit \( n \in {\mathbb{N}}^{ * } \) . Le nombre \( p = {10}^{n!}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}{10}^{-k!}}\right) \) est un entier \( \geq 2 \) , et avec \( q = {10}^{n!} \) , on a

> Let \( n \in {\mathbb{N}}^{ * } \). The number \( p = {10}^{n!}\left( {\mathop{\sum }\limits_{{k = 0}}^{n}{10}^{-k!}}\right) \) is an integer \( \geq 2 \), and with \( q = {10}^{n!} \), we have

\[
\left| {a - \frac{p}{q}}\right| {q}^{n} = {10}^{{nn}!}\left( {\mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{10}^{-k!}}\right)  = \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{10}^{{nn}! - k!} \leq  \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{10}^{n - k} = \frac{1}{9}
\]

(lorsque \( k \geq n + 1 \) nous avons utilisé la majoration \( {nn}! - k! = n!\left\lbrack {n - \left( {n + 1}\right) \cdots k}\right\rbrack \leq n - k \) ). Ainsi, on a

> (when \( k \geq n + 1 \) we used the upper bound \( {nn}! - k! = n!\left\lbrack {n - \left( {n + 1}\right) \cdots k}\right\rbrack \leq n - k \)). Thus, we have

\[
\left| {a - \frac{p}{q}}\right| {q}^{n} < 1,\;\text{ c’est-à-dire }\;\left| {a - \frac{p}{q}}\right|  < \frac{1}{{q}^{n}}
\]

et ceci est possible pour tout \( n \in {\mathbb{N}}^{ * } \) . Finalement, le réel \( a \) un nombre de Liouville, donc transcendant.

> and this is possible for any \( n \in {\mathbb{N}}^{ * } \) . Finally, the real number \( a \) is a Liouville number, and therefore transcendental.

Remarque. Le résultat 2/ date de 1844 et est historiquement la première preuve d'existence de nombres transcendants. Il n'admet pas de réciproque. Par exemple, \( \pi \) est transcendant, et on sait que \( \left| {\pi - p/q}\right| < 1/{q}^{7.104} \) n’a qu’un nombre fini de solutions (Zeilberger, Zudilin,2020). Ainsi \( \pi \mathrm{n} \) ’est pas un nombre de Liouville.

> Remark. Result 2/ dates back to 1844 and is historically the first proof of the existence of transcendental numbers. It does not admit a converse. For example, \( \pi \) is transcendental, and it is known that \( \left| {\pi - p/q}\right| < 1/{q}^{7.104} \) has only a finite number of solutions (Zeilberger, Zudilin, 2020). Thus, \( \pi \mathrm{n} \) is not a Liouville number.

- La preuve 1/ est plus récente. Les notions d'équipotence introduites par Cantor datent en effet de la fin du XIX-ième siècle.

> - Proof 1/ is more recent. The notions of equipotence introduced by Cantor indeed date from the end of the 19th century.

- S'il est relativement simple, avec 2 /, de construire des nombres transcendants, il est beaucoup plus difficile de dire si un nombre donné est transcendant ou non. Le sujet d’étude 2 page 107 démontre que \( e \) et \( \pi \) sont transcendants.

> - While it is relatively simple, with 2/, to construct transcendental numbers, it is much more difficult to determine whether a given number is transcendental or not. Study topic 2 on page 107 demonstrates that \( e \) and \( \pi \) are transcendental.

Problem 7 (NOMBRES ALGÉBRIQUES). Soient \( \mathbb{K} \) et \( \mathbb{L} \) deux corps commutatifs, \( \mathbb{K} \) étant un sous-corps de \( \mathbb{L} \) . On dit que \( a \in \mathbb{L} \) est algébrique sur \( \mathbb{K} \) s’il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \neq 0 \) , tel que \( P\left( a\right) = 0 \) .

> Problem 7 (ALGEBRAIC NUMBERS). Let \( \mathbb{K} \) and \( \mathbb{L} \) be two commutative fields, with \( \mathbb{K} \) being a subfield of \( \mathbb{L} \) . We say that \( a \in \mathbb{L} \) is algebraic over \( \mathbb{K} \) if there exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \neq 0 \) , such that \( P\left( a\right) = 0 \) .

1 / Pour tout \( a \in \mathbb{L} \) , on pose \( \mathbb{K}\left\lbrack a\right\rbrack = \{ P\left( a\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) et \( {I}_{a} = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( a\right) = 0\} \) . a) Soit \( a \in \mathbb{L} \) algébrique sur \( \mathbb{K} \) . Montrer que \( \mathbb{K}\left\lbrack a\right\rbrack \) est un corps, et que c’est un \( \mathbb{K} \) -espace vectoriel de dimension finie.

> 1/ For any \( a \in \mathbb{L} \) , let \( \mathbb{K}\left\lbrack a\right\rbrack = \{ P\left( a\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) and \( {I}_{a} = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( a\right) = 0\} \) . a) Let \( a \in \mathbb{L} \) be algebraic over \( \mathbb{K} \) . Show that \( \mathbb{K}\left\lbrack a\right\rbrack \) is a field, and that it is a finite-dimensional \( \mathbb{K} \) -vector space.

b) Montrer que si le \( \mathbb{K} \) -espace vectoriel \( \mathbb{K}\left\lbrack a\right\rbrack \) est de dimension finie, alors \( a \) est algébrique sur \( \mathbb{K} \) .

> b) Show that if the \( \mathbb{K} \) -vector space \( \mathbb{K}\left\lbrack a\right\rbrack \) is finite-dimensional, then \( a \) is algebraic over \( \mathbb{K} \) .

\( 2/\operatorname{Si}{\mathbb{K}}_{1} \subset {\mathbb{K}}_{2} \) sont deux corps commutatifs, on note \( \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack \in {\mathbb{N}}^{ * } \cup \{ + \infty \} \) la dimension de \( {\mathbb{K}}_{2} \) considéré comme un \( {\mathbb{K}}_{1} \) -espace vectoriel.

> \( 2/\operatorname{Si}{\mathbb{K}}_{1} \subset {\mathbb{K}}_{2} \) are two commutative fields, we denote by \( \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack \in {\mathbb{N}}^{ * } \cup \{ + \infty \} \) the dimension of \( {\mathbb{K}}_{2} \) considered as an \( {\mathbb{K}}_{1} \) -vector space.

a) Soient \( {\mathbb{K}}_{1} \subset {\mathbb{K}}_{2} \subset {\mathbb{K}}_{3} \) trois corps commutatifs. Montrer l’équivalence

> a) Let \( {\mathbb{K}}_{1} \subset {\mathbb{K}}_{2} \subset {\mathbb{K}}_{3} \) be three commutative fields. Show the equivalence

\[
\left( {\left\lbrack  {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack   <  + \infty \text{ et }\left\lbrack  {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack   <  + \infty }\right)  \Leftrightarrow  \left( {\left\lbrack  {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack   <  + \infty }\right) .
\]

b) Soit \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{L} \) . On rappelle que la notation \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) désigne le plus petit sous-corps de \( \mathbb{L} \) contenant \( \mathbb{K} \) et \( {a}_{1},\ldots ,{a}_{n} \) . Montrer que \( {a}_{1},\ldots ,{a}_{n} \) sont algébriques sur \( \mathbb{K} \) si et seulement si \( \left\lbrack {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) : \mathbb{K}}\right\rbrack < + \infty \) .

> b) Let \( {a}_{1},\ldots ,{a}_{n} \in \mathbb{L} \) . Recall that the notation \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) denotes the smallest subfield of \( \mathbb{L} \) containing \( \mathbb{K} \) and \( {a}_{1},\ldots ,{a}_{n} \) . Show that \( {a}_{1},\ldots ,{a}_{n} \) are algebraic over \( \mathbb{K} \) if and only if \( \left\lbrack {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) : \mathbb{K}}\right\rbrack < + \infty \) .

c) Montrer que A, l'ensemble des nombres algébriques sur \( \mathbb{K} \) , est un corps.

> c) Show that A, the set of algebraic numbers over \( \mathbb{K} \) , is a field.

3 / Si L est algébriquement clos, montrer que A est algébriquement clos.

> 3 / If L is algebraically closed, show that A is algebraically closed.

Solution. 1/a) Comme \( {I}_{a} \) est un idéal non nul de l’anneau principal \( \mathbb{K}\left\lbrack X\right\rbrack \) , donc il existe un unique polynôme \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) unitaire tel que \( {I}_{a} = \left( P\right) \) .

> Solution. 1/a) Since \( {I}_{a} \) is a non-zero ideal of the principal ideal domain \( \mathbb{K}\left\lbrack X\right\rbrack \) , there exists a unique monic polynomial \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {I}_{a} = \left( P\right) \) .

Le polynôme \( P \) est irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) . En effet, si \( P = {QR} \) avec \( Q, R \in \mathbb{K}\left\lbrack X\right\rbrack \) , alors \( 0 = P\left( a\right) = Q\left( a\right) R\left( a\right) \) et donc \( Q\left( a\right) = 0 \) ou \( R\left( a\right) = 0 \) , donc \( Q \) ou \( R \) appartient à \( {I}_{a} = \left( P\right) \) donc \( \deg \left( Q\right) \geq \deg \left( P\right) \) ou \( \deg \left( R\right) \geq \deg \left( P\right) \) , ce qui prouve l’irréductibilité de \( P \) . ( \( P \) s’appelle le polynôme minimal de \( a,\deg \left( P\right) \) le degré de \( a \) ).

> The polynomial \( P \) is irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) . Indeed, if \( P = {QR} \) with \( Q, R \in \mathbb{K}\left\lbrack X\right\rbrack \) , then \( 0 = P\left( a\right) = Q\left( a\right) R\left( a\right) \) and thus \( Q\left( a\right) = 0 \) or \( R\left( a\right) = 0 \) , so \( Q \) or \( R \) belongs to \( {I}_{a} = \left( P\right) \) , therefore \( \deg \left( Q\right) \geq \deg \left( P\right) \) or \( \deg \left( R\right) \geq \deg \left( P\right) \) , which proves the irreducibility of \( P \) . ( \( P \) is called the minimal polynomial of \( a,\deg \left( P\right) \) , the degree of \( a \) ).

L’application \( \varphi : \mathbb{K}\left\lbrack X\right\rbrack \rightarrow \mathbb{L}\;F \mapsto F\left( a\right) \) est un morphisme d’anneaux. Or \( \operatorname{Ker}\varphi = {I}_{a} = \left( P\right) \) , donc \( \operatorname{Im}\varphi = \mathbb{K}\left\lbrack a\right\rbrack \) est isomorphe à \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) . Le polynôme \( P \) étant irréductible, c’est donc un corps (voir proposition 4 page 65) de dimension \( \deg \left( P\right) \) en tant que \( \mathbb{K} \) -espace vectoriel.

> The map \( \varphi : \mathbb{K}\left\lbrack X\right\rbrack \rightarrow \mathbb{L}\;F \mapsto F\left( a\right) \) is a ring homomorphism. Now \( \operatorname{Ker}\varphi = {I}_{a} = \left( P\right) \) , so \( \operatorname{Im}\varphi = \mathbb{K}\left\lbrack a\right\rbrack \) is isomorphic to \( \mathbb{K}\left\lbrack X\right\rbrack /\left( P\right) \) . Since the polynomial \( P \) is irreducible, it is therefore a field (see proposition 4 page 65) of dimension \( \deg \left( P\right) \) as a \( \mathbb{K} \) -vector space.

b) Soit \( n \) la dimension du \( \mathbb{K} \) -espace vectoriel \( \mathbb{K}\left\lbrack a\right\rbrack \) . La famille \( \left( {1, a,\ldots ,{a}^{n}}\right) \) constitue un système de \( n + 1 \) vecteurs de \( \mathbb{K}\left\lbrack a\right\rbrack \) , ces vecteurs sont donc liés. Autrement dit, il existe \( {x}_{0},\ldots ,{x}_{n} \in \mathbb{K} \) tels que \( {x}_{0} + {x}_{1}a + \cdots + {x}_{n}{a}^{n} = 0 \) , avec les \( {\left( {x}_{i}\right) }_{0 \leq i \leq n} \) non tous nuls. Donc si \( P = \mathop{\sum }\limits_{{i = 0}}^{n}{x}_{i}{X}^{i} \) , \( P\left( a\right) = 0 \) et \( P \neq 0 \) . Donc \( a \) est algébrique sur \( \mathbb{K} \) .

> b) Let \( n \) be the dimension of the \( \mathbb{K} \) -vector space \( \mathbb{K}\left\lbrack a\right\rbrack \) . The family \( \left( {1, a,\ldots ,{a}^{n}}\right) \) constitutes a system of \( n + 1 \) vectors in \( \mathbb{K}\left\lbrack a\right\rbrack \) , these vectors are therefore linearly dependent. In other words, there exist \( {x}_{0},\ldots ,{x}_{n} \in \mathbb{K} \) such that \( {x}_{0} + {x}_{1}a + \cdots + {x}_{n}{a}^{n} = 0 \) , with the \( {\left( {x}_{i}\right) }_{0 \leq i \leq n} \) not all zero. Thus, if \( P = \mathop{\sum }\limits_{{i = 0}}^{n}{x}_{i}{X}^{i} \) , \( P\left( a\right) = 0 \) and \( P \neq 0 \) . Therefore \( a \) is algebraic over \( \mathbb{K} \) .

2/a) Condition nécessaire. \( \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) donc \( {\mathbb{K}}_{2} \) est isomorphe comme \( {\mathbb{K}}_{1} \) -espace vectoriel à \( {\mathbb{K}}_{1}^{\left\lbrack {\mathbb{K}}_{2} : {\mathbb{K}}_{1}\right\rbrack } \) . De même \( {\mathbb{K}}_{3} \) est isomorphe comme \( {\mathbb{K}}_{2} \) -espace vectoriel à \( {\mathbb{K}}_{2}^{\left\lbrack {\mathbb{K}}_{3} : {\mathbb{K}}_{2}\right\rbrack } \) , a fortiori isomorphe comme \( {\mathbb{K}}_{1} \) -espace vectoriel à \( {\mathbb{K}}_{2}^{\left\lbrack {\mathbb{K}}_{3} : {\mathbb{K}}_{2}\right\rbrack } \) (comme \( {\mathbb{K}}_{1} \subset {\mathbb{K}}_{2} \) , tout isomorphisme de \( {\mathbb{K}}_{2} \) -espace vector-riel est un isomorphisme de \( {\mathbb{K}}_{1} \) -espace vectoriel), donc isomorphe comme \( {\mathbb{K}}_{1} \) -espace vectoriel à \( {\left( {\mathbb{K}}_{1}^{\left\lbrack {\mathbb{K}}_{2} : {\mathbb{K}}_{1}\right\rbrack }\right) }^{\left\lbrack {\mathbb{K}}_{3} : {\mathbb{K}}_{2}\right\rbrack } \) , donc à \( {\mathbb{K}}_{1}^{\left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack \cdot \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack } \) . Donc \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack = \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack \cdot \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) . Condition suffisante. \( {\mathbb{K}}_{2} \subset {\mathbb{K}}_{3} \) donc \( \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack \leq \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) .

> 2/a) Necessary condition. \( \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) thus \( {\mathbb{K}}_{2} \) is isomorphic as a \( {\mathbb{K}}_{1} \) -vector space to \( {\mathbb{K}}_{1}^{\left\lbrack {\mathbb{K}}_{2} : {\mathbb{K}}_{1}\right\rbrack } \) . Similarly \( {\mathbb{K}}_{3} \) is isomorphic as a \( {\mathbb{K}}_{2} \) -vector space to \( {\mathbb{K}}_{2}^{\left\lbrack {\mathbb{K}}_{3} : {\mathbb{K}}_{2}\right\rbrack } \) , a fortiori isomorphic as a \( {\mathbb{K}}_{1} \) -vector space to \( {\mathbb{K}}_{2}^{\left\lbrack {\mathbb{K}}_{3} : {\mathbb{K}}_{2}\right\rbrack } \) (as \( {\mathbb{K}}_{1} \subset {\mathbb{K}}_{2} \) , any isomorphism of \( {\mathbb{K}}_{2} \) -vector spaces is an isomorphism of \( {\mathbb{K}}_{1} \) -vector spaces), thus isomorphic as a \( {\mathbb{K}}_{1} \) -vector space to \( {\left( {\mathbb{K}}_{1}^{\left\lbrack {\mathbb{K}}_{2} : {\mathbb{K}}_{1}\right\rbrack }\right) }^{\left\lbrack {\mathbb{K}}_{3} : {\mathbb{K}}_{2}\right\rbrack } \) , and therefore to \( {\mathbb{K}}_{1}^{\left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack \cdot \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack } \) . Thus \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack = \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack \cdot \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) . Sufficient condition. \( {\mathbb{K}}_{2} \subset {\mathbb{K}}_{3} \) thus \( \left\lbrack {{\mathbb{K}}_{2} : {\mathbb{K}}_{1}}\right\rbrack \leq \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) .

Montrons maintenant \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack < + \infty \) . Comme \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) , il existe une base finie \( {e}_{1},\ldots ,{e}_{n} \) du \( {\mathbb{K}}_{1} \) -espace vectoriel \( {\mathbb{K}}_{3} \) . On remarque alors que \( {e}_{1},\ldots ,{e}_{n} \) est une famille génératrice finie de \( {\mathbb{K}}_{3} \) vu comme un \( {\mathbb{K}}_{2} \) espace vectoriel. Donc \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack < + \infty \) .

> Let us now show \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack < + \infty \) . Since \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{1}}\right\rbrack < + \infty \) , there exists a finite basis \( {e}_{1},\ldots ,{e}_{n} \) of the \( {\mathbb{K}}_{1} \) -vector space \( {\mathbb{K}}_{3} \) . We then note that \( {e}_{1},\ldots ,{e}_{n} \) is a finite generating set of \( {\mathbb{K}}_{3} \) viewed as a \( {\mathbb{K}}_{2} \) vector space. Thus \( \left\lbrack {{\mathbb{K}}_{3} : {\mathbb{K}}_{2}}\right\rbrack < + \infty \) .

b) Condition nécessaire. Procédons par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est une conséquence de 1/. Supposons le résultat vrai au rang \( n \) , montrons le au rang \( n + 1 \) . D’après l’hypothèse de récurrence,

> b) Necessary condition. Let us proceed by induction on \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) , it is a consequence of 1/. Assume the result is true at rank \( n \) , let us show it at rank \( n + 1 \) . According to the induction hypothesis,

\[
\left\lbrack  {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right)  : \mathbb{K}}\right\rbrack   <  + \infty .
\]

(*)

> L’élément \( {a}_{n + 1} \) est algébrique sur \( \mathbb{K} \) , a fortiori sur \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) . Le résultat 1/ reste évidemment vrai si on remplace \( \mathbb{K} \) par \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \subset \mathbb{L} \) , donc

The element \( {a}_{n + 1} \) is algebraic over \( \mathbb{K} \) , and a fortiori over \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) . The result 1/ obviously remains true if we replace \( \mathbb{K} \) by \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \subset \mathbb{L} \) , therefore

\[
\left\lbrack  {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \left( {a}_{n + 1}\right)  : \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) }\right\rbrack   <  + \infty .
\]

Or \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \left( {a}_{n + 1}\right) = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n + 1}}\right) \) , donc cette dernière assertion s’écrit

> However \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \left( {a}_{n + 1}\right) = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n + 1}}\right) \) , so this last assertion is written

\[
\left\lbrack  {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n + 1}}\right)  : \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) }\right\rbrack   <  + \infty .
\]

\( \left( {* * }\right) \)

> De \( \left( *\right) \) et \( \left( {* * }\right) \) , on tire d’après \( 2/ \) a) \( \left\lbrack {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n + 1}}\right) : \mathbb{K}}\right\rbrack < + \infty \) , d’où la condition nécessaire. Condition suffisante. Pour tout \( i,\mathbb{K}\left\lbrack {a}_{i}\right\rbrack \subset \mathbb{K}\left( {a}_{i}\right) \subset \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , donc \( \mathbb{K}\left\lbrack {a}_{i}\right\rbrack \) est un \( \mathbb{K} \) -espace vectoriel de dimension finie, et donc \( {a}_{i} \) est algébrique sur \( \mathbb{K} \) d’après \( 1/\mathrm{b} \) ).

From \( \left( *\right) \) and \( \left( {* * }\right) \) , we deduce from \( 2/ \) a) \( \left\lbrack {\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n + 1}}\right) : \mathbb{K}}\right\rbrack < + \infty \) , whence the necessary condition. Sufficient condition. For all \( i,\mathbb{K}\left\lbrack {a}_{i}\right\rbrack \subset \mathbb{K}\left( {a}_{i}\right) \subset \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , thus \( \mathbb{K}\left\lbrack {a}_{i}\right\rbrack \) is a finite-dimensional \( \mathbb{K} \) -vector space, and therefore \( {a}_{i} \) is algebraic over \( \mathbb{K} \) according to \( 1/\mathrm{b} \) ).

> c) Soient \( \left( {x, y}\right) \in {\mathbb{A}}^{2} \) . On a \( \mathbb{K}\left( {x - y}\right) \subset \mathbb{K}\left( {x, y}\right) \) donc comme \( \left\lbrack {\mathbb{K}\left( {x, y}\right) : \mathbb{K}}\right\rbrack < + \infty \) , on a \( \lbrack \mathbb{K}\left( {x - y}\right) \) : \( \mathbb{K}\rbrack < + \infty \) , et donc \( x - y \in \mathbb{A} \) d’après \( 2/\mathrm{b}) \) . De même si \( y \neq 0 \) , comme \( \mathbb{K}\left( {x{y}^{-1}}\right) \subset \mathbb{K}\left( {x, y}\right) \) , on tire \( x{y}^{-1} \in \mathbb{A} \) . Finalement, \( \mathbb{A} \) est un corps.

c) Let \( \left( {x, y}\right) \in {\mathbb{A}}^{2} \) . We have \( \mathbb{K}\left( {x - y}\right) \subset \mathbb{K}\left( {x, y}\right) \) so as \( \left\lbrack {\mathbb{K}\left( {x, y}\right) : \mathbb{K}}\right\rbrack < + \infty \) , we have \( \lbrack \mathbb{K}\left( {x - y}\right) \) : \( \mathbb{K}\rbrack < + \infty \) , and thus \( x - y \in \mathbb{A} \) according to \( 2/\mathrm{b}) \) . Similarly if \( y \neq 0 \) , as \( \mathbb{K}\left( {x{y}^{-1}}\right) \subset \mathbb{K}\left( {x, y}\right) \) , we derive \( x{y}^{-1} \in \mathbb{A} \) . Finally, \( \mathbb{A} \) is a field.

> 3/ Soit \( P = {a}_{0} + {a}_{1}X + \cdots {a}_{n}{X}^{n} \in \mathbb{A}\left\lbrack X\right\rbrack , P \neq 0 \) . Le corps \( \mathbb{L} \) étant algébriquement clos, il existe \( a \in \mathbb{L} \) tel que \( P\left( a\right) = 0 \) , et donc d’après 1/a) appliqué au corps \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \) , \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \left\lbrack a\right\rbrack \) est un corps (donc égal à \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \left( a\right) = \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}, a}\right) \) ) de dimension finie comme \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \) -espace vectoriel. Autrement dit, \( \left\lbrack {\mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}, a}\right) : \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) }\right\rbrack < + \infty \) . Or \( \left\lbrack {\mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) : \mathbb{K}}\right\rbrack < + \infty \) d’après \( 2/\mathrm{b}) \) , donc d’après \( 2/\mathrm{a}),\left\lbrack {\mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}, a}\right) : \mathbb{K}}\right\rbrack < + \infty \) , et donc \( a \in \mathbb{A} \) d’après \( 2/\mathrm{b}) \) , d’où le résultat.

3/ Let \( P = {a}_{0} + {a}_{1}X + \cdots {a}_{n}{X}^{n} \in \mathbb{A}\left\lbrack X\right\rbrack , P \neq 0 \) . The field \( \mathbb{L} \) being algebraically closed, there exists \( a \in \mathbb{L} \) such that \( P\left( a\right) = 0 \) , and thus according to 1/a) applied to the field \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \) , \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \left\lbrack a\right\rbrack \) is a field (therefore equal to \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \left( a\right) = \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}, a}\right) \) ) of finite dimension as an \( \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) \) -vector space. In other words, \( \left\lbrack {\mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}, a}\right) : \mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) }\right\rbrack < + \infty \) . However \( \left\lbrack {\mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}}\right) : \mathbb{K}}\right\rbrack < + \infty \) according to \( 2/\mathrm{b}) \) , so according to \( 2/\mathrm{a}),\left\lbrack {\mathbb{K}\left( {{a}_{0},\ldots ,{a}_{n}, a}\right) : \mathbb{K}}\right\rbrack < + \infty \) , and thus \( a \in \mathbb{A} \) according to \( 2/\mathrm{b}) \) , hence the result.

> Remarque. En particulier, l’ensemble A des nombres complexes algébriques sur \( \mathbb{Q} \) est un corps algébriquement clos. On l'appelle la clôture algébrique de \( \mathbb{Q} \) (c'est la plus petite extension de \( \mathbb{Q} \) algébriquement close).

Remark. In particular, the set A of algebraic complex numbers over \( \mathbb{Q} \) is an algebraically closed field. It is called the algebraic closure of \( \mathbb{Q} \) (it is the smallest algebraically closed extension of \( \mathbb{Q} \) ).

> Problem 8 (THÉORÉME DE KRONECKER). Soit \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) un polynôme unitaire de degré \( n \geq 1 \) et irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) . On suppose que toutes les racines de \( P \) sont de module \( \leq 1 \) . Montrer qu’alors \( P = X \) ou bien il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( P \mid \left( {{X}^{k} - 1}\right) \) . (Indication. On pourra utiliser le résultat suivant, conséquence d'un exercice du tome d’Analyse : Si \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \) , alors \( \left( {\forall \varepsilon > 0,\exists n \in {\mathbb{N}}^{ * }}\right) ,\left| {{e}^{2i\pi n\alpha } - 1}\right| < \varepsilon \) .)

Problem 8 (KRONECKER'S THEOREM). Let \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) be a monic polynomial of degree \( n \geq 1 \) and irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \). Suppose that all roots of \( P \) have modulus \( \leq 1 \). Show that then \( P = X \) or there exists \( k \in {\mathbb{N}}^{ * } \) such that \( P \mid \left( {{X}^{k} - 1}\right) \). (Hint. One may use the following result, a consequence of an exercise in the Analysis volume: If \( \alpha \in \mathbb{R} \smallsetminus \mathbb{Q} \), then \( \left( {\forall \varepsilon > 0,\exists n \in {\mathbb{N}}^{ * }}\right) ,\left| {{e}^{2i\pi n\alpha } - 1}\right| < \varepsilon \).)

---

Solution. Soient \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) les racines de \( P \) . Notons \( a \in \mathbb{Z} \) le terme constant de \( P \) . Le polynôme \( P \) étant unitaire, on a \( {\alpha }_{1}\cdots {\alpha }_{n} = {\left( -1\right) }^{n}a \) . S’il existe \( i \) tel que \( \left| {\alpha }_{i}\right| < 1 \) , par exemple \( \left| {\alpha }_{1}\right| < 1 \) , alors \( \left| a\right| = \left| {\alpha }_{1}\right| \cdot \left| {{\alpha }_{2}\cdots {\alpha }_{n}}\right| \leq \left| {\alpha }_{1}\right| < 1 \) , et comme \( a \in \mathbb{Z}, a = 0 \) . Donc \( X \) divise \( P \) , et \( P \) étant irréductible et unitaire, \( P = X \) .

> Solution. Let \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) be the roots of \( P \). Let \( a \in \mathbb{Z} \) denote the constant term of \( P \). Since the polynomial \( P \) is monic, we have \( {\alpha }_{1}\cdots {\alpha }_{n} = {\left( -1\right) }^{n}a \). If there exists \( i \) such that \( \left| {\alpha }_{i}\right| < 1 \), for example \( \left| {\alpha }_{1}\right| < 1 \), then \( \left| a\right| = \left| {\alpha }_{1}\right| \cdot \left| {{\alpha }_{2}\cdots {\alpha }_{n}}\right| \leq \left| {\alpha }_{1}\right| < 1 \), and since \( a \in \mathbb{Z}, a = 0 \). Thus \( X \) divides \( P \), and since \( P \) is irreducible and monic, \( P = X \).

Dans le cas contraire, on a \( \left| {\alpha }_{i}\right| = 1 \) pour tout \( i \) . Considérons pour tout entier \( k \geq 1 \)

> In the opposite case, we have \( \left| {\alpha }_{i}\right| = 1 \) for all \( i \). Consider for every integer \( k \geq 1 \)

\[
{\pi }_{k} = \left( {{\alpha }_{1}^{k} - 1}\right) \left( {{\alpha }_{2}^{k} - 1}\right) \cdots \left( {{\alpha }_{n}^{k} - 1}\right) .
\]

Pour tout \( k,{\pi }_{k} \) s’écrit comme un polynôme à coefficients entiers symétrique en les \( {\alpha }_{i} \) , et donc \( {\pi }_{k} \in \mathbb{Z} \) d’après la remarque 4 page 84. Nous allons montrer qu’il existe \( k \) tel que \( {\pi }_{k} = 0 \) . Comme \( \left| {\alpha }_{1}\right| = 1 \) , il existe \( \theta \in \mathbb{R} \) tel que \( {\alpha }_{1} = {e}^{2i\pi \theta } \) . Si \( \theta \in \mathbb{Q} \) , alors il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( {k\theta } \in \mathbb{Z} \) , donc \( {\alpha }_{1}^{k} = {e}^{2i\pi k\theta } = 1 \) , donc \( {\pi }_{k} = 0 \) . Sinon, \( \theta \in \mathbb{R} \smallsetminus \mathbb{Q} \) . Compte tenu de la majoration \( \left| {{\alpha }_{i}^{k} - 1}\right| \leq 2 \) , l’expression de \( {\pi }_{k} \) entraîne \( \left| {\pi }_{k}\right| \leq \left| {{\alpha }_{1}^{k} - 1}\right| \cdot {2}^{n - 1} \) . Or \( \theta \in \mathbb{R} \smallsetminus \mathbb{Q} \) donc (on utilise l’indication) il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( \left| {{\alpha }_{1}^{k} - 1}\right| < {2}^{1 - n} \) , ce qui entraîne \( \left| {\pi }_{k}\right| < 1 \) et comme \( {\pi }_{k} \) est un entier, on a forcément \( {\pi }_{k} = 0 \) .

> For any \( k,{\pi }_{k} \) can be written as a symmetric polynomial with integer coefficients in the \( {\alpha }_{i} \) , and thus \( {\pi }_{k} \in \mathbb{Z} \) according to remark 4 on page 84. We will show that there exists \( k \) such that \( {\pi }_{k} = 0 \) . Since \( \left| {\alpha }_{1}\right| = 1 \) , there exists \( \theta \in \mathbb{R} \) such that \( {\alpha }_{1} = {e}^{2i\pi \theta } \) . If \( \theta \in \mathbb{Q} \) , then there exists \( k \in {\mathbb{N}}^{ * } \) such that \( {k\theta } \in \mathbb{Z} \) , therefore \( {\alpha }_{1}^{k} = {e}^{2i\pi k\theta } = 1 \) , and thus \( {\pi }_{k} = 0 \) . Otherwise, \( \theta \in \mathbb{R} \smallsetminus \mathbb{Q} \) . Given the upper bound \( \left| {{\alpha }_{i}^{k} - 1}\right| \leq 2 \) , the expression for \( {\pi }_{k} \) leads to \( \left| {\pi }_{k}\right| \leq \left| {{\alpha }_{1}^{k} - 1}\right| \cdot {2}^{n - 1} \) . However, \( \theta \in \mathbb{R} \smallsetminus \mathbb{Q} \) so (using the hint) there exists \( k \in {\mathbb{N}}^{ * } \) such that \( \left| {{\alpha }_{1}^{k} - 1}\right| < {2}^{1 - n} \) , which leads to \( \left| {\pi }_{k}\right| < 1 \) and since \( {\pi }_{k} \) is an integer, we necessarily have \( {\pi }_{k} = 0 \) .

Il existe donc \( k \in {\mathbb{N}}^{ * } \) tel que \( {\pi }_{k} = 0 \) , ce qui entraîne l’existence de \( i \) tel que \( {\alpha }_{i}^{k} = 1 \) , par exemple \( {\alpha }_{1}^{k} = 1 \) . Soit \( {X}^{k} - 1 = {P}_{1}\cdots {P}_{r} \) la décomposition de \( {X}^{k} - 1 \) en polynômes irréductibles unitaires de \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Comme \( {\alpha }_{1} \) est racine de \( {X}^{k} - 1 \) , il existe \( i \) tel que \( {P}_{i}\left( {\alpha }_{1}\right) = 0 \) , par exemple \( {P}_{1}\left( {\alpha }_{1}\right) = 0 \) . Ainsi, \( {P}_{1} \) et \( P \) ont \( {\alpha }_{1} \) comme racine commune et ne sont donc pas premiers entre eux dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) (l’égalité de Bezout \( U{P}_{1} + {VP} = 1 \) appliquée à \( {\alpha }_{1} \) mène à une contradiction). Ces polynômes,étant de plus irréductibles et unitaires, sont donc égaux. En définitive \( P = {P}_{1} \) divise \( {X}^{k} - 1 \) .

> There therefore exists \( k \in {\mathbb{N}}^{ * } \) such that \( {\pi }_{k} = 0 \) , which leads to the existence of \( i \) such that \( {\alpha }_{i}^{k} = 1 \) , for example \( {\alpha }_{1}^{k} = 1 \) . Let \( {X}^{k} - 1 = {P}_{1}\cdots {P}_{r} \) be the decomposition of \( {X}^{k} - 1 \) into monic irreducible polynomials in \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Since \( {\alpha }_{1} \) is a root of \( {X}^{k} - 1 \) , there exists \( i \) such that \( {P}_{i}\left( {\alpha }_{1}\right) = 0 \) , for example \( {P}_{1}\left( {\alpha }_{1}\right) = 0 \) . Thus, \( {P}_{1} \) and \( P \) have \( {\alpha }_{1} \) as a common root and are therefore not coprime in \( \mathbb{Q}\left\lbrack X\right\rbrack \) (Bézout's identity \( U{P}_{1} + {VP} = 1 \) applied to \( {\alpha }_{1} \) leads to a contradiction). These polynomials, being moreover irreducible and monic, are therefore equal. Ultimately \( P = {P}_{1} \) divides \( {X}^{k} - 1 \) .

---

Remarque. Dans le second cas, \( P \) est un polynôme irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) divisant \( {X}^{k} - 1 \) . C'est donc un polynôme cyclotomique (voir le problème 10).

> Remark. In the second case, \( P \) is an irreducible polynomial in \( \mathbb{Q}\left\lbrack X\right\rbrack \) dividing \( {X}^{k} - 1 \). It is therefore a cyclotomic polynomial (see problem 10).

Problem 9 (THÉORÉME DE L'ÉLÉMENT PRIMITIF). 1/ Soit \( \mathbb{K} \) un corps commutatif de caractéristique nulle (donc \( \mathbb{K} \) est infini) et \( \mathbb{L} \) un surcorps commutatif de \( \mathbb{K} \) . Le corps \( \mathbb{L} \) est un \( \mathbb{K} \) -espace vectoriel. S’il est de dimension finie, on va montrer qu’il existe \( x \in \mathbb{L} \) tel que \( \mathbb{L} = \mathbb{K}\left\lbrack x\right\rbrack = \{ P\left( x\right) , P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

> Problem 9 (PRIMITIVE ELEMENT THEOREM). 1/ Let \( \mathbb{K} \) be a commutative field of characteristic zero (thus \( \mathbb{K} \) is infinite) and \( \mathbb{L} \) a commutative extension field of \( \mathbb{K} \). The field \( \mathbb{L} \) is an \( \mathbb{K} \)-vector space. If it is of finite dimension, we will show that there exists \( x \in \mathbb{L} \) such that \( \mathbb{L} = \mathbb{K}\left\lbrack x\right\rbrack = \{ P\left( x\right) , P \in \mathbb{K}\left\lbrack X\right\rbrack \} \).

a) Pour tout \( x \in \mathbb{L} \) , montrer qu’il existe un unique polynôme unitaire de degré minimal \( {M}_{x} \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( {M}_{x}\left( x\right) = 0\left( {{M}_{x}\text{ s’appelle le polynôme minimal de }}\right. x \) ). Montrer que \( {M}_{x} \) est irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) .

> a) For any \( x \in \mathbb{L} \), show that there exists a unique monic polynomial of minimal degree \( {M}_{x} \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( {M}_{x}\left( x\right) = 0\left( {{M}_{x}\text{ s’appelle le polynôme minimal de }}\right. x \)). Show that \( {M}_{x} \) is irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \).

b) On rappelle que pour \( {a}_{1},\ldots ,{a}_{m} \in \mathbb{L},\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{m}}\right) \) désigne le plus petit sous-corps de \( \mathbb{L} \) contenant \( \mathbb{K} \) et \( {a}_{1},\ldots ,{a}_{m} \) . Soient \( x, y \in \mathbb{L} \) . On veut montrer qu’il existe \( z \in \mathbb{L} \) tel que \( \mathbb{K}\left( {x, y}\right) = \mathbb{K}\left( z\right) \) . On sait (voir le théorème 5 page 66) qu’il existe un surcorps \( \mathbb{M} \) de \( \mathbb{L} \) , commutatif, sur lequel \( {M}_{x}{M}_{y} \) soit scindé. Autrement dit, dans \( \mathbb{M}\left\lbrack X\right\rbrack \) , on peut écrire

> b) Recall that for \( {a}_{1},\ldots ,{a}_{m} \in \mathbb{L},\mathbb{K}\left( {{a}_{1},\ldots ,{a}_{m}}\right) \) denotes the smallest subfield of \( \mathbb{L} \) containing \( \mathbb{K} \) and \( {a}_{1},\ldots ,{a}_{m} \). Let \( x, y \in \mathbb{L} \). We want to show that there exists \( z \in \mathbb{L} \) such that \( \mathbb{K}\left( {x, y}\right) = \mathbb{K}\left( z\right) \). We know (see theorem 5 page 66) that there exists a commutative extension field \( \mathbb{M} \) of \( \mathbb{L} \) over which \( {M}_{x}{M}_{y} \) splits. In other words, in \( \mathbb{M}\left\lbrack X\right\rbrack \), we can write

\[
{M}_{x} = \mathop{\prod }\limits_{{i = 1}}^{p}\left( {X - {x}_{i}}\right) ,{M}_{y} = \mathop{\prod }\limits_{{j = 1}}^{q}\left( {X - {y}_{j}}\right) \;\left( {\text{ avec }x = {x}_{1}, y = {y}_{1}}\right) .
\]

\( \alpha ) \) Montrer qu’il existe \( t \in {\mathbb{K}}^{ * } \) tel que les nombres \( {x}_{i} + t{y}_{j}\left( {1 \leq i \leq p,1 \leq j \leq q}\right) \) soient deux à deux distincts.

> \( \alpha ) \) Show that there exists \( t \in {\mathbb{K}}^{ * } \) such that the numbers \( {x}_{i} + t{y}_{j}\left( {1 \leq i \leq p,1 \leq j \leq q}\right) \) are pairwise distinct.

\( \beta ) \) On pose \( z = x + {ty} \) . Montrer le pgcd de \( {M}_{y}\left( X\right) \) et \( {M}_{x}\left( {z - {tX}}\right) \) dans \( \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) est \( X - y \) . \( \gamma ) \) Montrer que \( \mathbb{K}\left( z\right) = \mathbb{K}\left( {x, y}\right) \) .

> \( \beta ) \) Let \( z = x + {ty} \). Show that the gcd of \( {M}_{y}\left( X\right) \) and \( {M}_{x}\left( {z - {tX}}\right) \) in \( \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) is \( X - y \). \( \gamma ) \) Show that \( \mathbb{K}\left( z\right) = \mathbb{K}\left( {x, y}\right) \).

c) Montrer qu’il existe \( x \in \mathbb{L} \) tel que \( \mathbb{L} = \mathbb{K}\left\lbrack x\right\rbrack \) .

> c) Show that there exists \( x \in \mathbb{L} \) such that \( \mathbb{L} = \mathbb{K}\left\lbrack x\right\rbrack \).

2/ Montrer que ce résultat reste vrai si K est fini.

> 2/ Show that this result remains true if K is finite.

Solution. 1/a) Si \( n \) désigne la dimension du \( \mathbb{K} \) -espace vectoriel \( \mathbb{L} \) , les \( n + 1 \) vecteurs \( 1, x,\ldots ,{x}^{n} \) de \( \mathbb{L} \) sont linéairement dépendants sur \( \mathbb{K} \) . Donc il existe \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \neq 0 \) , tel que \( P\left( x\right) = 0 \) .

> Solution. 1/a) If \( n \) denotes the dimension of the \( \mathbb{K} \) -vector space \( \mathbb{L} \) , the \( n + 1 \) vectors \( 1, x,\ldots ,{x}^{n} \) of \( \mathbb{L} \) are linearly dependent over \( \mathbb{K} \) . Thus there exists \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \neq 0 \) , such that \( P\left( x\right) = 0 \) .

Donc \( {I}_{x} = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( x\right) = 0\} \) est différent de \( \{ 0\} \) . L’ensemble \( {I}_{x} \) étant un idéal de l’anneau principal \( \mathbb{K}\left\lbrack X\right\rbrack \) , il existe \( {M}_{x} \in \mathbb{K}\left\lbrack X\right\rbrack \) , unitaire, tel que \( {I}_{x} = \left( {M}_{x}\right) \) . Tout polynôme \( P \) unitaire s’annulant en \( x \) est donc un multiple de \( {M}_{x} \) . Ceci suffit pour affirmer que \( {M}_{x} \) est l’unique polynôme unitaire de plus bas degré s’annulant en \( x \) .

> Thus \( {I}_{x} = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( x\right) = 0\} \) is different from \( \{ 0\} \) . Since the set \( {I}_{x} \) is an ideal of the principal ideal domain \( \mathbb{K}\left\lbrack X\right\rbrack \) , there exists \( {M}_{x} \in \mathbb{K}\left\lbrack X\right\rbrack \) , monic, such that \( {I}_{x} = \left( {M}_{x}\right) \) . Any monic polynomial \( P \) vanishing at \( x \) is therefore a multiple of \( {M}_{x} \) . This is sufficient to state that \( {M}_{x} \) is the unique monic polynomial of lowest degree vanishing at \( x \) .

Supposons \( {M}_{x} = {PQ} \) avec \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) . On a \( P\left( x\right) Q\left( x\right) = {M}_{x}\left( x\right) = 0 \) donc \( P\left( x\right) = 0 \) ou \( Q\left( x\right) = 0 \) , donc \( \deg \left( P\right) \geq \deg \left( {M}_{x}\right) \) ou \( \deg \left( Q\right) \geq \deg \left( {M}_{x}\right) \) , et donc \( {M}_{x} \) est irréductible dans \( \mathbb{K}\left\lbrack X\right\rbrack \) .

> Suppose \( {M}_{x} = {PQ} \) with \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) . We have \( P\left( x\right) Q\left( x\right) = {M}_{x}\left( x\right) = 0 \) so \( P\left( x\right) = 0 \) or \( Q\left( x\right) = 0 \) , thus \( \deg \left( P\right) \geq \deg \left( {M}_{x}\right) \) or \( \deg \left( Q\right) \geq \deg \left( {M}_{x}\right) \) , and therefore \( {M}_{x} \) is irreducible in \( \mathbb{K}\left\lbrack X\right\rbrack \) .

b) \( \alpha ) \) Les \( {x}_{i} \) sont distincts. En effet, \( {M}_{x} \) étant irréductible, \( {M}_{x} \) et \( {M}_{x}^{\prime } \) sont premiers entre eux dans \( \mathbb{K}\left\lbrack X\right\rbrack \) (car \( \deg \left( {M}_{x}^{\prime }\right) < \deg \left( {M}_{x}\right) \) et \( {M}_{x}^{\prime } \neq 0,\mathbb{K} \) étant de caractéristique non nulle). Donc il existe \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) tels que \( U{M}_{x} + V{M}_{x}^{\prime } = 1 \) ,égalité qui vaut aussi dans \( \mathbb{M}\left\lbrack X\right\rbrack \) . Les polynômes \( {M}_{x} \) et \( {M}_{x}^{\prime } \) sont donc premiers entre eux dans \( \mathbb{M}\left\lbrack X\right\rbrack \) et n’ont donc aucune racine commune dans \( \mathbb{M} \) . On en déduit que \( {M}_{x} \) n’a que des racines simples et les \( {x}_{i} \) sont donc distincts. De même, les \( {y}_{j} \) sont distincts.

> b) \( \alpha ) \) The \( {x}_{i} \) are distinct. Indeed, since \( {M}_{x} \) is irreducible, \( {M}_{x} \) and \( {M}_{x}^{\prime } \) are coprime in \( \mathbb{K}\left\lbrack X\right\rbrack \) (because \( \deg \left( {M}_{x}^{\prime }\right) < \deg \left( {M}_{x}\right) \) and \( {M}_{x}^{\prime } \neq 0,\mathbb{K} \) are of non-zero characteristic). Thus there exist \( U, V \in \mathbb{K}\left\lbrack X\right\rbrack \) such that \( U{M}_{x} + V{M}_{x}^{\prime } = 1 \) , an equality that also holds in \( \mathbb{M}\left\lbrack X\right\rbrack \) . The polynomials \( {M}_{x} \) and \( {M}_{x}^{\prime } \) are therefore coprime in \( \mathbb{M}\left\lbrack X\right\rbrack \) and thus have no common root in \( \mathbb{M} \) . We deduce that \( {M}_{x} \) has only simple roots and the \( {x}_{i} \) are therefore distinct. Similarly, the \( {y}_{j} \) are distinct.

Soit

> Let

\[
\Gamma  = \left\{  {\left. \frac{{x}_{i} - {x}_{{i}^{\prime }}}{{y}_{{j}^{\prime }} - {y}_{j}}\right| \;1 \leq  i,{i}^{\prime } \leq  p,1 \leq  j \neq  {j}^{\prime } \leq  q}\right\}  .
\]

L’ensemble \( \Gamma \) est fini et \( \mathbb{K} \) est infini, donc il existe \( t \in {\mathbb{K}}^{ * }, t \notin \Gamma \) . Ainsi choisi, \( t \) convient (l’égalité \( {x}_{i} + t{y}_{j} = {x}_{{i}^{\prime }} + t{y}_{{j}^{\prime }} \) entraîne en effet \( t \in \Gamma \) si \( j \neq {j}^{\prime } \) et \( i = {i}^{\prime } \) si \( j = {j}^{\prime } \) ).

> The set \( \Gamma \) is finite and \( \mathbb{K} \) is infinite, so there exists \( t \in {\mathbb{K}}^{ * }, t \notin \Gamma \) . Chosen this way, \( t \) is suitable (the equality \( {x}_{i} + t{y}_{j} = {x}_{{i}^{\prime }} + t{y}_{{j}^{\prime }} \) indeed implies \( t \in \Gamma \) if \( j \neq {j}^{\prime } \) and \( i = {i}^{\prime } \) if \( j = {j}^{\prime } \) ).

\( \beta ) \) Plaçons nous pour commencer dans \( \mathbb{M}\left\lbrack X\right\rbrack \) . Soit \( a \in \mathbb{M} \) une racine commune de \( {M}_{y}\left( X\right) \) et \( {M}_{x}\left( {z - {tX}}\right) \) . Il existe \( j \) tel que \( a = {y}_{j} \) et il existe \( i \) tel que \( z - {ta} = {x}_{i} \) , et donc \( z = {x}_{i} + t{y}_{j} \) . Or par définition, \( z = {x}_{1} + t{y}_{1} \) donc d’après \( \alpha ){x}_{i} = {x}_{1} \) et \( {y}_{j} = {y}_{1} \) , donc \( a = {y}_{1} = y \) . Par conséquent, dans \( \mathbb{M}, y \) est la seule racine commune à \( {M}_{y}\left( X\right) \) et \( {M}_{x}\left( {z - {tX}}\right) \) . Ces polynômes étant scindés sur \( \mathbb{M} \) à racines toutes simples, on en déduit que le pgcd de ces polynômes dans \( \mathbb{M}\left\lbrack X\right\rbrack \) est \( X - y\;\left( *\right) \) .

> \( \beta ) \) Let us start by working in \( \mathbb{M}\left\lbrack X\right\rbrack \) . Let \( a \in \mathbb{M} \) be a common root of \( {M}_{y}\left( X\right) \) and \( {M}_{x}\left( {z - {tX}}\right) \) . There exists \( j \) such that \( a = {y}_{j} \) and there exists \( i \) such that \( z - {ta} = {x}_{i} \) , and thus \( z = {x}_{i} + t{y}_{j} \) . However, by definition, \( z = {x}_{1} + t{y}_{1} \) so according to \( \alpha ){x}_{i} = {x}_{1} \) and \( {y}_{j} = {y}_{1} \) , thus \( a = {y}_{1} = y \) . Consequently, in \( \mathbb{M}, y \) is the only common root of \( {M}_{y}\left( X\right) \) and \( {M}_{x}\left( {z - {tX}}\right) \) . Since these polynomials are split over \( \mathbb{M} \) with all simple roots, we deduce that the gcd of these polynomials in \( \mathbb{M}\left\lbrack X\right\rbrack \) is \( X - y\;\left( *\right) \) .

Ceci étant, soit \( D\left( X\right) \) le pgcd de \( {M}_{y}\left( X\right) \) et \( {M}_{x}\left( {z - {tX}}\right) \) dans \( \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) . On peut écrire

> That being said, let \( D\left( X\right) \) be the gcd of \( {M}_{y}\left( X\right) \) and \( {M}_{x}\left( {z - {tX}}\right) \) in \( \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) . We can write

\[
{M}_{y}\left( X\right)  = {P}_{1}\left( X\right) D\left( X\right) \;\text{ et }\;{M}_{x}\left( {z - {tX}}\right)  = {P}_{2}\left( X\right) D\left( X\right) ,\;\text{ avec }\;{P}_{1},{P}_{2} \in  \mathbb{K}\left( z\right) \left\lbrack  X\right\rbrack  ,
\]

où \( {P}_{1} \) et \( {P}_{2} \) sont premiers entre eux dans \( \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) . Donc il existe \( U, V \in \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) tels que \( U{P}_{1} + V{P}_{2} = 1 \) ,égalité qui vaut aussi dans \( \mathbb{M}\left\lbrack X\right\rbrack \) , donc \( {P}_{1} \) et \( {P}_{2} \) sont premiers entre eux dans \( \mathbb{M}\left\lbrack X\right\rbrack \) . Le pgcd de \( {M}_{y}\left( X\right) \) et \( {M}_{x}\left( {z - {tX}}\right) \) dans \( \mathbb{M}\left\lbrack X\right\rbrack \) est donc \( D\left( X\right) \) , d’où le résultat demandé d’après \( \left( *\right) \) .

> where \( {P}_{1} \) and \( {P}_{2} \) are coprime in \( \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) . Thus there exists \( U, V \in \mathbb{K}\left( z\right) \left\lbrack X\right\rbrack \) such that \( U{P}_{1} + V{P}_{2} = 1 \) , an equality that also holds in \( \mathbb{M}\left\lbrack X\right\rbrack \) , so \( {P}_{1} \) and \( {P}_{2} \) are coprime in \( \mathbb{M}\left\lbrack X\right\rbrack \) . The gcd of \( {M}_{y}\left( X\right) \) and \( {M}_{x}\left( {z - {tX}}\right) \) in \( \mathbb{M}\left\lbrack X\right\rbrack \) is therefore \( D\left( X\right) \) , hence the requested result according to \( \left( *\right) \) .

\( \gamma ) \) D’après \( \beta ), y \in \mathbb{K}\left( z\right) \) . La relation \( x = z - {ty} \) montre que \( x \in \mathbb{K}\left( z\right) \) . Donc \( \mathbb{K}\left( {x, y}\right) \subset \mathbb{K}\left( z\right) \) . Or \( z = x + {ty} \) donc \( \mathbb{K}\left( z\right) \subset \mathbb{K}\left( {x, y}\right) \) . Finalement, on a prouvé que \( \mathbb{K}\left( z\right) = \mathbb{K}\left( {x, y}\right) \) .

> \( \gamma ) \) According to \( \beta ), y \in \mathbb{K}\left( z\right) \) . The relation \( x = z - {ty} \) shows that \( x \in \mathbb{K}\left( z\right) \) . Thus \( \mathbb{K}\left( {x, y}\right) \subset \mathbb{K}\left( z\right) \) . However, \( z = x + {ty} \) so \( \mathbb{K}\left( z\right) \subset \mathbb{K}\left( {x, y}\right) \) . Finally, we have proven that \( \mathbb{K}\left( z\right) = \mathbb{K}\left( {x, y}\right) \) .

c) L’utilisation du résultat \( 1/\mathrm{b}\gamma ) \) permet de montrer par récurrence sur \( m \) que si \( {a}_{1},\ldots ,{a}_{m} \in \mathbb{L} \) , alors il existe \( z \in \mathbb{L} \) tel que \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{m}}\right) = \mathbb{K}\left( z\right) \) .

> c) Using the result \( 1/\mathrm{b}\gamma ) \) allows us to show by induction on \( m \) that if \( {a}_{1},\ldots ,{a}_{m} \in \mathbb{L} \) , then there exists \( z \in \mathbb{L} \) such that \( \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{m}}\right) = \mathbb{K}\left( z\right) \) .

Ceci étant, soit \( {a}_{1},\ldots ,{a}_{n} \) une base du \( \mathbb{K} \) -espace vectoriel \( \mathbb{L} \) . On a \( \mathbb{L} = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , et donc il existe \( x \in \mathbb{L} \) tel que \( \mathbb{L} = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) = \mathbb{K}\left( x\right) \) .

> Given this, let \( {a}_{1},\ldots ,{a}_{n} \) be a basis of the \( \mathbb{K} \) -vector space \( \mathbb{L} \) . We have \( \mathbb{L} = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) \) , and thus there exists \( x \in \mathbb{L} \) such that \( \mathbb{L} = \mathbb{K}\left( {{a}_{1},\ldots ,{a}_{n}}\right) = \mathbb{K}\left( x\right) \) .

Il reste à montrer que \( \mathbb{K}\left( x\right) = \mathbb{K}\left\lbrack x\right\rbrack \) . Considérons le morphisme d’anneau \( \varphi : \mathbb{K}\left\lbrack X\right\rbrack \rightarrow \; \mathbb{K}\left\lbrack x\right\rbrack \;P \mapsto P\left( x\right) \) . Avec les notations de 1/a), on voit que \( \operatorname{Ker}\varphi = \left\{ {P \mid P\left( x\right) = 0}\right\} = {I}_{x} = \left( {M}_{x}\right) \) . Comme \( \varphi \) est surjective, \( \mathbb{K}\left\lbrack x\right\rbrack \) est isomorphe à \( \mathbb{K}\left\lbrack X\right\rbrack /\operatorname{Ker}\varphi = \mathbb{K}\left\lbrack X\right\rbrack /\left( {M}_{x}\right) \) qui est un corps car \( {M}_{x} \) est irréductible (voir la proposition 4 page 65). L’anneau \( \mathbb{K}\left\lbrack x\right\rbrack \) est donc un corps, et donc \( \mathbb{K}\left( x\right) \subset \mathbb{K}\left\lbrack x\right\rbrack \) . L’inclusion réciproque étant évidente, on a montré \( \mathbb{K}\left\lbrack x\right\rbrack = \mathbb{K}\left( x\right) = \mathbb{L} \) .

> It remains to show that \( \mathbb{K}\left( x\right) = \mathbb{K}\left\lbrack x\right\rbrack \) . Consider the ring morphism \( \varphi : \mathbb{K}\left\lbrack X\right\rbrack \rightarrow \; \mathbb{K}\left\lbrack x\right\rbrack \;P \mapsto P\left( x\right) \) . With the notation from 1/a), we see that \( \operatorname{Ker}\varphi = \left\{ {P \mid P\left( x\right) = 0}\right\} = {I}_{x} = \left( {M}_{x}\right) \) . Since \( \varphi \) is surjective, \( \mathbb{K}\left\lbrack x\right\rbrack \) is isomorphic to \( \mathbb{K}\left\lbrack X\right\rbrack /\operatorname{Ker}\varphi = \mathbb{K}\left\lbrack X\right\rbrack /\left( {M}_{x}\right) \) which is a field because \( {M}_{x} \) is irreducible (see proposition 4 on page 65). The ring \( \mathbb{K}\left\lbrack x\right\rbrack \) is therefore a field, and thus \( \mathbb{K}\left( x\right) \subset \mathbb{K}\left\lbrack x\right\rbrack \) . The reverse inclusion being obvious, we have shown \( \mathbb{K}\left\lbrack x\right\rbrack = \mathbb{K}\left( x\right) = \mathbb{L} \) .

2/ Si K est fini, \( \mathbb{L} \) est fini (c’est un \( \mathbb{K} \) -espace vectoriel de dimension finie). On sait (voir la remarque de l’exercice 10 page 10) que \( \left( {{\mathbb{L}}^{ * }, \cdot }\right) \) est un groupe cyclique. Soit \( x \) l’engendrant. On voit facilement que \( \mathbb{L} = \mathbb{K}\left\lbrack x\right\rbrack \) .

> 2/ If K is finite, \( \mathbb{L} \) is finite (it is a finite-dimensional \( \mathbb{K} \) -vector space). We know (see the remark in exercise 10 on page 10) that \( \left( {{\mathbb{L}}^{ * }, \cdot }\right) \) is a cyclic group. Let \( x \) be its generator. It is easy to see that \( \mathbb{L} = \mathbb{K}\left\lbrack x\right\rbrack \) .

Remarque. Cet exercice utilise le résultat suivant, qu'il est utile de garder en mémoire.

> Remark. This exercise uses the following result, which is useful to keep in mind.

Si \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) et si \( \mathbb{L} \) est un surcorps de \( \mathbb{K} \) alors les pgcd de \( P \) et \( Q \) dans \( \mathbb{K}\left\lbrack X\right\rbrack \) et dans \( \mathbb{L}\left\lbrack X\right\rbrack \) coïncident.

> If \( P, Q \in \mathbb{K}\left\lbrack X\right\rbrack \) and if \( \mathbb{L} \) is an extension field of \( \mathbb{K} \) , then the gcds of \( P \) and \( Q \) in \( \mathbb{K}\left\lbrack X\right\rbrack \) and in \( \mathbb{L}\left\lbrack X\right\rbrack \) coincide.

Problem 10 (Polynômes cyclotomologie). Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {U}_{n} = \; \left\{ {{e}^{{2ik\pi }/n} \mid k \in \mathbb{Z}}\right\} \subset \mathbb{C} \) . On dit qu’un élément \( x \in {U}_{n} \) est une racine primitive n-ième de l’unité si \( x \) engendre le groupe multiplicatif \( {U}_{n} \) . On note \( {\Pi }_{n} \) l’ensemble des racines primitives \( n \) -ièmes de l’unité, et on définit le polynôme cyclotomique d’indice \( n \) par

> Problem 10 (Cyclotomic polynomials). For any \( n \in {\mathbb{N}}^{ * } \) , we denote \( {U}_{n} = \; \left\{ {{e}^{{2ik\pi }/n} \mid k \in \mathbb{Z}}\right\} \subset \mathbb{C} \) . An element \( x \in {U}_{n} \) is said to be a primitive n-th root of unity if \( x \) generates the multiplicative group \( {U}_{n} \) . We denote \( {\Pi }_{n} \) as the set of primitive \( n \) -th roots of unity, and we define the cyclotomic polynomial of index \( n \) by

\[
{\Phi }_{n} = \mathop{\prod }\limits_{{\xi  \in  {\Pi }_{n}}}\left( {X - \xi }\right)
\]

1/ a) Calculer \( {\Phi }_{p} \) lorsque \( p \) est un nombre premier.

> 1/ a) Calculate \( {\Phi }_{p} \) when \( p \) is a prime number.

b) Montrer que \( {X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) . En déduire que pour tout \( n \in {\mathbb{N}}^{ * },{\Phi }_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

> b) Show that \( {X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) . Deduce that for all \( n \in {\mathbb{N}}^{ * },{\Phi }_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack \) .

2/ On veut prouver que les \( {\Phi }_{n} \) sont irréductibles dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> 2/ We want to prove that the \( {\Phi }_{n} \) are irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

a) Montrer que l’on peut écrire \( {\Phi }_{n} = {F}_{1}{F}_{2}\cdots {F}_{r} \) avec les \( {F}_{i} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , unitaires et irréduc-tibles dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) (on pourra utiliser le lemme de Gauss, voir l’exercice 4 page 62).

> a) Show that we can write \( {\Phi }_{n} = {F}_{1}{F}_{2}\cdots {F}_{r} \) with the \( {F}_{i} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , monic and irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) (one may use Gauss's lemma, see exercise 4 on page 62).

b) Soit \( \xi \) une racine de \( {F}_{1} \) dans \( \mathbb{C} \) . Soit \( p \) un nombre premier tel que \( p \nmid n \) . Montrer qu’il existe \( i \in \mathbb{N},1 \leq i \leq r \) tel que \( {F}_{i}\left( {\xi }^{p}\right) = 0 \) .

> b) Let \( \xi \) be a root of \( {F}_{1} \) in \( \mathbb{C} \) . Let \( p \) be a prime number such that \( p \nmid n \) . Show that there exists \( i \in \mathbb{N},1 \leq i \leq r \) such that \( {F}_{i}\left( {\xi }^{p}\right) = 0 \) .

c) Pour tout \( F = \mathop{\sum }\limits_{{k = 0}}^{m}{a}_{k}{X}^{k} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , on pose \( \bar{F} = \mathop{\sum }\limits_{{k = 0}}^{m}\overline{{a}_{k}}{X}^{k} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack (\bar{x} \) désignant la classe dans \( \mathbb{Z}/p\mathbb{Z} \) de \( x \in \mathbb{Z} \) ). Montrer que pour tout \( F \in \mathbb{Z}\left\lbrack X\right\rbrack ,\bar{F}\left( {X}^{p}\right) = {\left\lbrack \bar{F}\left( X\right) \right\rbrack }^{p} \) .

> c) For any \( F = \mathop{\sum }\limits_{{k = 0}}^{m}{a}_{k}{X}^{k} \in \mathbb{Z}\left\lbrack X\right\rbrack \), let \( \bar{F} = \mathop{\sum }\limits_{{k = 0}}^{m}\overline{{a}_{k}}{X}^{k} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack (\bar{x} \) denote the class in \( \mathbb{Z}/p\mathbb{Z} \) of \( x \in \mathbb{Z} \). Show that for any \( F \in \mathbb{Z}\left\lbrack X\right\rbrack ,\bar{F}\left( {X}^{p}\right) = {\left\lbrack \bar{F}\left( X\right) \right\rbrack }^{p} \).

d) Montrer que dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack ,{\overline{\Phi }}_{n} \) n’est divisible par le carré d’aucun polynôme non constant.

> d) Show that in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack ,{\overline{\Phi }}_{n} \), it is not divisible by the square of any non-constant polynomial.

e) Montrer que \( i = 1 \) , c’est-à-dire que \( {F}_{1}\left( {\xi }^{p}\right) = 0 \) .

> e) Show that \( i = 1 \), that is to say \( {F}_{1}\left( {\xi }^{p}\right) = 0 \).

f) Montrer que pour tout entier \( k \) premier avec \( n,{F}_{1}\left( {\xi }^{k}\right) = 0 \) . Conclure.

> f) Show that for any integer \( k \) coprime to \( n,{F}_{1}\left( {\xi }^{k}\right) = 0 \). Conclude.

Solution. 1/ Posons \( \omega = {e}^{{2i\pi }/n} \) , de sorte que \( {U}_{n} = \langle \omega \rangle \) . D’après la proposition 5 page 22, on a \( {\Pi }_{n} = \left\{ {{\omega }^{k} \mid 1 \leq k \leq n - 1, k \land n = 1}\right\} \) , et donc deg \( \left( {\Phi }_{n}\right) = \varphi \left( n\right) \) où \( \varphi \) désigne l’indicateur d’Euler. a) Le nombre \( p \) étant premier, on a ici \( {\Pi }_{p} = \left\{ {{\omega }^{k} \mid 1 \leq k \leq p - 1}\right\} \) (où \( \omega = {e}^{{2i\pi }/p} \) ), et donc

> Solution. 1/ Let \( \omega = {e}^{{2i\pi }/n} \), such that \( {U}_{n} = \langle \omega \rangle \). According to proposition 5 on page 22, we have \( {\Pi }_{n} = \left\{ {{\omega }^{k} \mid 1 \leq k \leq n - 1, k \land n = 1}\right\} \), and thus deg \( \left( {\Phi }_{n}\right) = \varphi \left( n\right) \) where \( \varphi \) denotes Euler's totient function. a) Since the number \( p \) is prime, we have here \( {\Pi }_{p} = \left\{ {{\omega }^{k} \mid 1 \leq k \leq p - 1}\right\} \) (where \( \omega = {e}^{{2i\pi }/p} \)), and thus

\[
{\Phi }_{p} = \frac{1}{X - 1}\mathop{\prod }\limits_{{\xi  \in  {U}_{p}}}\left( {X - \xi }\right)  = \frac{{X}^{p} - 1}{X - 1} = 1 + X + \cdots  + {X}^{p - 1}.
\]

b) Soit \( \omega = {e}^{{2i\pi }/n} \) . Soit \( k,0 \leq k \leq n - 1 \) . Soit \( d \) l’ordre de \( {\omega }^{k} \) dans \( {U}_{n} \) . On a \( d \mid n \) . Par ailleurs \( {\left( {\omega }^{k}\right) }^{d} = 1 \) , donc \( {\omega }^{k} \in {U}_{d} \) , et \( {\omega }^{k} \) étant d’ordre \( d \) , on a même \( {\omega }^{k} \in {\Pi }_{d} \) . Ainsi, \( \left( {X - {\omega }^{k}}\right) \) divise \( {\Phi }_{d} \) donc divise \( \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) . Les valeurs \( {\omega }^{k}\left( {0 \leq k \leq n - 1}\right) \) étant distinctes, on en déduit que \( {X}^{n} - 1 = \mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {X - {\omega }^{k}}\right) \) divise \( \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) . Ces polynômes étant de plus unitaires et de même degré (car \( \mathop{\sum }\limits_{{d \mid n}}\deg \left( {\Phi }_{d}\right) = \mathop{\sum }\limits_{{d \mid n}}\varphi \left( d\right) = n \) ), ils sont égaux.

> b) Let \( \omega = {e}^{{2i\pi }/n} \). Let \( k,0 \leq k \leq n - 1 \). Let \( d \) be the order of \( {\omega }^{k} \) in \( {U}_{n} \). We have \( d \mid n \). Furthermore \( {\left( {\omega }^{k}\right) }^{d} = 1 \), so \( {\omega }^{k} \in {U}_{d} \), and since \( {\omega }^{k} \) is of order \( d \), we even have \( {\omega }^{k} \in {\Pi }_{d} \). Thus, \( \left( {X - {\omega }^{k}}\right) \) divides \( {\Phi }_{d} \) and therefore divides \( \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \). Since the values \( {\omega }^{k}\left( {0 \leq k \leq n - 1}\right) \) are distinct, we deduce that \( {X}^{n} - 1 = \mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {X - {\omega }^{k}}\right) \) divides \( \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \). As these polynomials are also monic and of the same degree (because \( \mathop{\sum }\limits_{{d \mid n}}\deg \left( {\Phi }_{d}\right) = \mathop{\sum }\limits_{{d \mid n}}\varphi \left( d\right) = n \)), they are equal.

Montrons maintenant par récurrence sur \( n \in {\mathbb{N}}^{ * } \) que \( {\Phi }_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Pour \( n = 1 \) , c’est vrai car \( {\Phi }_{1} = X - 1 \) . Supposons le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . D’après l’hypothèse de récurrence, le polynôme \( P = \mathop{\prod }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\Phi }_{d} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Par ailleurs, on a \( {X}^{n} - 1 = {\Phi }_{n}P \) . Comme \( P \) est unitaire, on peut effectuer la division euclidienne de \( {X}^{n} - 1 \) par \( P \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) (voir la remarque 3 page 58) :

> Let us now show by induction on \( n \in {\mathbb{N}}^{ * } \) that \( {\Phi }_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack \). For \( n = 1 \), it is true because \( {\Phi }_{1} = X - 1 \). Assume the result is true up to rank \( n - 1 \) and show it for rank \( n \). According to the induction hypothesis, the polynomial \( P = \mathop{\prod }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\Phi }_{d} \in \mathbb{Z}\left\lbrack X\right\rbrack \). Furthermore, we have \( {X}^{n} - 1 = {\Phi }_{n}P \). Since \( P \) is monic, we can perform the Euclidean division of \( {X}^{n} - 1 \) by \( P \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) (see remark 3 on page 58):

\[
\left( {\exists Q, R \in  \mathbb{Z}\left\lbrack  X\right\rbrack  }\right) ,\;{X}^{n} - 1 = {PQ} + R\;\text{ avec }\;\deg \left( R\right)  < \deg \left( P\right) .
\]

Il y a unicité du couple \( \left( {Q, R}\right) \) dans \( \mathbb{C}\left\lbrack X\right\rbrack \) donc dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) , et comme \( {X}^{n} - 1 = P{\Phi }_{n} \) on en déduit \( R = 0 \) et \( {\Phi }_{n} = Q \) . Donc \( {\Phi }_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , ce qui achève le raisonnement par récurrence.

> There is uniqueness of the pair \( \left( {Q, R}\right) \) in \( \mathbb{C}\left\lbrack X\right\rbrack \) and therefore in \( \mathbb{Z}\left\lbrack X\right\rbrack \), and since \( {X}^{n} - 1 = P{\Phi }_{n} \) we deduce \( R = 0 \) and \( {\Phi }_{n} = Q \). Thus \( {\Phi }_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack \), which completes the reasoning by induction.

2/a) Soit \( {\Phi }_{n} = {G}_{1}\cdots {G}_{r} \) la décomposition de \( {\Phi }_{n} \) en facteurs irréductibles unitaires de \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Pour tout \( i \) , il existe \( {\alpha }_{i} \in {\mathbb{N}}^{ * } \) tel que \( {\alpha }_{i}{G}_{i} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . On a \( {\alpha }_{1}\cdots {\alpha }_{r}{\Phi }_{n} = \left( {{\alpha }_{1}{G}_{1}}\right) \cdots \left( {{\alpha }_{r}{G}_{r}}\right) \) . Utilisons le lemme de Gauss (voir l'exercice 4 page 62, dont on reprend les notations). Comme \( c\left( {\Phi }_{n}\right) = 1 \) (car \( {\Phi }_{n} \) est unitaire), on a

> 2/a) Let \( {\Phi }_{n} = {G}_{1}\cdots {G}_{r} \) be the decomposition of \( {\Phi }_{n} \) into monic irreducible factors of \( \mathbb{Q}\left\lbrack X\right\rbrack \) . For any \( i \) , there exists \( {\alpha }_{i} \in {\mathbb{N}}^{ * } \) such that \( {\alpha }_{i}{G}_{i} \in \mathbb{Z}\left\lbrack X\right\rbrack \) . We have \( {\alpha }_{1}\cdots {\alpha }_{r}{\Phi }_{n} = \left( {{\alpha }_{1}{G}_{1}}\right) \cdots \left( {{\alpha }_{r}{G}_{r}}\right) \) . Let us use Gauss's lemma (see exercise 4 on page 62, using the same notation). Since \( c\left( {\Phi }_{n}\right) = 1 \) (because \( {\Phi }_{n} \) is monic), we have

\[
{\alpha }_{1}\cdots {\alpha }_{r} = c\left( {{\alpha }_{1}\cdots {\alpha }_{r}{\Phi }_{n}}\right)  = \mathop{\prod }\limits_{{i = 1}}^{r}c\left( {{\alpha }_{i}{G}_{i}}\right) .
\]

(*)

> Pour tout \( i \) , le polynôme \( {F}_{i} = {\alpha }_{i}{G}_{i}/c\left( {{\alpha }_{i}{G}_{i}}\right) \) est dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) et d’après \( \left( *\right) \) , on a \( {\Phi }_{n} = {F}_{1}\cdots {F}_{r} \) . Pour tout \( i,{F}_{i} \in \mathbb{Z}\left\lbrack X\right\rbrack \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) et est forcément unitaire puisque \( {\Phi }_{n} \) est unitaire.

For any \( i \) , the polynomial \( {F}_{i} = {\alpha }_{i}{G}_{i}/c\left( {{\alpha }_{i}{G}_{i}}\right) \) is in \( \mathbb{Z}\left\lbrack X\right\rbrack \) and according to \( \left( *\right) \) , we have \( {\Phi }_{n} = {F}_{1}\cdots {F}_{r} \) . For any \( i,{F}_{i} \in \mathbb{Z}\left\lbrack X\right\rbrack \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \) and is necessarily monic since \( {\Phi }_{n} \) is monic.

> b) L’élément \( \xi \) est racine de \( {F}_{1} \) donc de \( {\Phi }_{n} \) , donc \( \xi \in {\Pi }_{n} \) . Or \( p \) est premier et \( p \nmid n \) , donc \( p \land n = 1 \) , et donc \( {\xi }^{p} \in {\Pi }_{n} \) , d’où \( {\xi }^{p} \) est racine de \( {\Phi }_{n} \) . Il existe donc \( i \) tel que \( {F}_{i}\left( {\xi }^{p}\right) = 0 \) .

b) The element \( \xi \) is a root of \( {F}_{1} \) and therefore of \( {\Phi }_{n} \) , so \( \xi \in {\Pi }_{n} \) . However, \( p \) is prime and \( p \nmid n \) , so \( p \land n = 1 \) , and therefore \( {\xi }^{p} \in {\Pi }_{n} \) , whence \( {\xi }^{p} \) is a root of \( {\Phi }_{n} \) . There therefore exists \( i \) such that \( {F}_{i}\left( {\xi }^{p}\right) = 0 \) .

> c) On montre cette relation par récurrence sur \( m \in \mathbb{N} \) , où \( m = \deg \left( F\right) \) . Pour \( m = 0 \) , c’est évident. Supposons le résultat vrai jusqu’au rang \( m - 1 \) et montrons au rang \( m \) . Écrivons \( F = \; \mathop{\sum }\limits_{{k = 0}}^{m}{a}_{k}{X}^{k} = G + {a}_{m}{X}^{m} \) . D’après l’hypothèse de récurrence, on a \( \bar{G}{\left( X\right) }^{p} = \bar{G}\left( {X}^{p}\right) \) . Or

c) We show this relation by induction on \( m \in \mathbb{N} \) , where \( m = \deg \left( F\right) \) . For \( m = 0 \) , it is obvious. Assume the result is true up to rank \( m - 1 \) and show it for rank \( m \) . Let us write \( F = \; \mathop{\sum }\limits_{{k = 0}}^{m}{a}_{k}{X}^{k} = G + {a}_{m}{X}^{m} \) . According to the induction hypothesis, we have \( \bar{G}{\left( X\right) }^{p} = \bar{G}\left( {X}^{p}\right) \) . However

\[
{\bar{F}}^{p} = {\left( \bar{G} + \overline{{a}_{m}}{X}^{m}\right) }^{p} = {\bar{G}}^{p} + {\overline{{a}_{m}}}^{p}{X}^{mp} + \mathop{\sum }\limits_{{k = 1}}^{{p - 1}}\left( \begin{array}{l} p \\  k \end{array}\right) {\bar{G}}^{k}{\overline{{a}_{m}}}^{n - k}{X}^{\left( {p - k}\right) m},
\]

et comme \( {\overline{{a}_{m}}}^{p} = \overline{{a}_{m}} \) et que pour \( 1 \leq k \leq p - 1, p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) , on en déduit

> and since \( {\overline{{a}_{m}}}^{p} = \overline{{a}_{m}} \) and that for \( 1 \leq k \leq p - 1, p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) , we deduce

\[
\bar{F}{\left( X\right) }^{p} = \bar{G}{\left( X\right) }^{p} + \overline{{a}_{m}}{X}^{mp} = \bar{G}\left( {X}^{p}\right)  + \overline{{a}_{m}}{\left( {X}^{p}\right) }^{m} = \bar{F}\left( {X}^{p}\right) .
\]

d) Supposons \( {\overline{\Phi }}_{n} = {\bar{Q}}^{2}\bar{P} \) dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . On peut écrire \( {X}^{n} - 1 = {\Phi }_{n}R \) d’après 1/b), avec \( R = \mathop{\prod }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\Phi }_{d} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , et donc \( {X}^{n} - \overline{1} = {\overline{\Phi }}_{n}\bar{R} = {\bar{Q}}^{2}\bar{S} \) (avec \( S = {PR} \) ), d’où par dérivation

> d) Suppose \( {\overline{\Phi }}_{n} = {\bar{Q}}^{2}\bar{P} \) in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . We can write \( {X}^{n} - 1 = {\Phi }_{n}R \) according to 1/b), with \( R = \mathop{\prod }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\Phi }_{d} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , and thus \( {X}^{n} - \overline{1} = {\overline{\Phi }}_{n}\bar{R} = {\bar{Q}}^{2}\bar{S} \) (with \( S = {PR} \) ), hence by differentiation

\[
\bar{n}{X}^{n - 1} = 2\bar{Q}{\bar{Q}}^{\prime }\bar{S} + {\bar{Q}}^{2}{\bar{S}}^{\prime } = \bar{Q}\left( {2{\bar{Q}}^{\prime }\bar{S} + \bar{Q}{\bar{S}}^{\prime }}\right) .
\]

Donc \( \bar{Q} \mid \bar{n}{X}^{n} \) . Or \( \bar{Q} \mid \left( {\bar{n}{X}^{n} - \bar{n}}\right) \) donc \( \bar{Q} \) divise la différence, c’est-à-dire \( \bar{Q} \mid \bar{n} \) . Or \( p \nmid n \) donc \( \bar{n} \neq 0 \) , et donc \( \bar{Q} \) est constant.

> Therefore \( \bar{Q} \mid \bar{n}{X}^{n} \) . However \( \bar{Q} \mid \left( {\bar{n}{X}^{n} - \bar{n}}\right) \) so \( \bar{Q} \) divides the difference, that is to say \( \bar{Q} \mid \bar{n} \) . But \( p \nmid n \) so \( \bar{n} \neq 0 \) , and thus \( \bar{Q} \) is constant.

e) Comme \( {F}_{i}\left( {\xi }^{p}\right) = 0,{F}_{1}\left( X\right) \) et \( {F}_{i}\left( {X}^{p}\right) \) admettent \( \xi \) comme racine commune donc ne sont pas premiers entre eux dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) (l’égalité de Bezout \( U\left( X\right) {F}_{1}\left( X\right) + V\left( X\right) {F}_{i}\left( {X}^{p}\right) = 1 \) avec \( U, V \in \mathbb{Q}\left\lbrack X\right\rbrack \) appliquée à \( X = \xi \) mène à une contradiction). De plus \( {F}_{1} \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) donc \( {F}_{1}\left( X\right) \mid {F}_{i}\left( {X}^{p}\right) \) dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) . Comme \( {F}_{1} \) est unitaire, \( {F}_{1}\left( X\right) \) divise \( {F}_{i}\left( {X}^{p}\right) \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) (voir la remarque 3 de la partie 1.3, page 58). On en déduit que \( \overline{{F}_{1}}\left( X\right) \mid \overline{{F}_{i}}\left( {X}^{p}\right) = \overline{{F}_{i}}{\left( X\right) }^{p} \) . Ceci étant, soit \( \bar{P} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) un facteur irréductible de \( \overline{{F}_{1}} \) dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . On a \( \bar{P} \mid \overline{{F}_{i}}{\left( X\right) }^{p} \) donc \( \bar{P} \mid \overline{{F}_{i}}\left( X\right) \) . Par conséquent, si \( i \neq 1 \) , on a forcément \( {\bar{P}}^{2} \mid {\overline{\Phi }}_{n} = \overline{{F}_{1}}\cdots \overline{{F}_{r}} \) , ce qui est impossible d’après la question précédente. On a donc \( i = 1 \) .

> e) Since \( {F}_{i}\left( {\xi }^{p}\right) = 0,{F}_{1}\left( X\right) \) and \( {F}_{i}\left( {X}^{p}\right) \) share \( \xi \) as a common root, they are not coprime in \( \mathbb{Q}\left\lbrack X\right\rbrack \) (Bézout's identity \( U\left( X\right) {F}_{1}\left( X\right) + V\left( X\right) {F}_{i}\left( {X}^{p}\right) = 1 \) with \( U, V \in \mathbb{Q}\left\lbrack X\right\rbrack \) applied to \( X = \xi \) leads to a contradiction). Furthermore, \( {F}_{1} \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \), so \( {F}_{1}\left( X\right) \mid {F}_{i}\left( {X}^{p}\right) \) in \( \mathbb{Q}\left\lbrack X\right\rbrack \). Since \( {F}_{1} \) is monic, \( {F}_{1}\left( X\right) \) divides \( {F}_{i}\left( {X}^{p}\right) \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) (see remark 3 in part 1.3, page 58). We deduce that \( \overline{{F}_{1}}\left( X\right) \mid \overline{{F}_{i}}\left( {X}^{p}\right) = \overline{{F}_{i}}{\left( X\right) }^{p} \). That being said, let \( \bar{P} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) be an irreducible factor of \( \overline{{F}_{1}} \) in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \). We have \( \bar{P} \mid \overline{{F}_{i}}{\left( X\right) }^{p} \), so \( \bar{P} \mid \overline{{F}_{i}}\left( X\right) \). Consequently, if \( i \neq 1 \), we necessarily have \( {\bar{P}}^{2} \mid {\overline{\Phi }}_{n} = \overline{{F}_{1}}\cdots \overline{{F}_{r}} \), which is impossible according to the previous question. We therefore have \( i = 1 \).

f) Soit \( k \) premier avec \( n \) . Écrivons \( k = {p}_{1}{p}_{2}\cdots {p}_{s} \) , les \( {p}_{i} \) étant des nombres premiers. Nous allons prouver par récurrence sur \( s \) que \( {F}_{1}\left( {\xi }^{k}\right) = 0 \) . Pour \( s = 1 \) , c’est le résultat de la question précédente. Supposons la résultat vrai au rang \( s - 1 \) et montrons le au rang \( s \) . Comme \( k \land n = 1 \) , on a \( {p}_{1}\cdots {p}_{s - 1} \land n = 1 \) , donc d’après l’hypothèse de récurrence \( {F}_{1}\left( {\xi }^{{p}_{1}\cdots {p}_{s - 1}}\right) = 0 \) . Or \( {p}_{s} \land n = 1 \) donc \( {F}_{1}\left\lbrack {\left( {\xi }^{{p}_{1}\cdots {p}_{s - 1}}\right) }^{{p}_{s}}\right\rbrack = {F}_{1}\left( {\xi }^{k}\right) = 0 \) , ce qui achève le raisonnement par récurrence.

> f) Let \( k \) be coprime to \( n \). Let us write \( k = {p}_{1}{p}_{2}\cdots {p}_{s} \), where the \( {p}_{i} \) are prime numbers. We will prove by induction on \( s \) that \( {F}_{1}\left( {\xi }^{k}\right) = 0 \). For \( s = 1 \), this is the result of the previous question. Assume the result is true for rank \( s - 1 \) and show it for rank \( s \). Since \( k \land n = 1 \), we have \( {p}_{1}\cdots {p}_{s - 1} \land n = 1 \), so according to the induction hypothesis \( {F}_{1}\left( {\xi }^{{p}_{1}\cdots {p}_{s - 1}}\right) = 0 \). However, \( {p}_{s} \land n = 1 \) so \( {F}_{1}\left\lbrack {\left( {\xi }^{{p}_{1}\cdots {p}_{s - 1}}\right) }^{{p}_{s}}\right\rbrack = {F}_{1}\left( {\xi }^{k}\right) = 0 \), which completes the reasoning by induction.

Pour tout nombre premier \( k \) premier avec \( n \) , on a donc \( {F}_{1}\left( {\xi }^{k}\right) = 0 \) . Or \( \xi \in {\Pi }_{n} \) donc \( {\Pi }_{n} = \; \left\{ {{\xi }^{k} \mid k \land n = 1}\right\} \) . Tous les éléments de \( {\Pi }_{n} \) sont donc des racines de \( {F}_{1} \) , ce qui prouve que \( {\Phi }_{n} = {F}_{1} \) , donc \( {\Phi }_{n} \) est irréductible dans \( \mathbb{Q}\left\lbrack X\right\rbrack \) .

> For any prime number \( k \) coprime to \( n \), we therefore have \( {F}_{1}\left( {\xi }^{k}\right) = 0 \). However, \( \xi \in {\Pi }_{n} \) so \( {\Pi }_{n} = \; \left\{ {{\xi }^{k} \mid k \land n = 1}\right\} \). All elements of \( {\Pi }_{n} \) are therefore roots of \( {F}_{1} \), which proves that \( {\Phi }_{n} = {F}_{1} \), so \( {\Phi }_{n} \) is irreducible in \( \mathbb{Q}\left\lbrack X\right\rbrack \).

Remarque. Avec 1/a) et 2/, on retrouve le résultat 3/b) de l'exercice 4 page 62.

> Remark. With 1/a) and 2/, we recover the result 3/b) of exercise 4 on page 62.

PROBLÉME 11 (THÉORÉME DE DIRICHLET, VERSION FAIBLE). Ce problème réutilise les résultats sur les polynômes cyclotomiques de la question 1/ du problème précédent.

> PROBLEM 11 (DIRICHLET'S THEOREM, WEAK VERSION). This problem reuses the results on cyclotomic polynomials from question 1/ of the previous problem.

Soit entier naturel \( n \geq 2 \) . L’objectif du problème est de montrer qu’il y a une infinité de nombres premiers \( p \) vérifiant \( p \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) .

> Let \( n \geq 2 \) be a natural number. The objective of the problem is to show that there are infinitely many prime numbers \( p \) satisfying \( p \equiv 1\left( {\;\operatorname{mod}\;n}\right) \).

a) Soit \( p \) un nombre premier. Montrer que s’il existe \( a \in \mathbb{Z} \) et \( h \in \mathbb{Z}\left\lbrack X\right\rbrack \) tels que \( {X}^{n} - 1 \equiv \; {\left( X - a\right) }^{2}h\left( X\right) \left( {\;\operatorname{mod}\;p}\right) \) (i.e. si \( {X}^{n} - \overline{1} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) admet une racine d’ordre \( \geq 2 \) dans \( \mathbb{Z}/p\mathbb{Z} \) ), alors \( p \) divise \( n \) .

> a) Let \( p \) be a prime number. Show that if there exist \( a \in \mathbb{Z} \) and \( h \in \mathbb{Z}\left\lbrack X\right\rbrack \) such that \( {X}^{n} - 1 \equiv \; {\left( X - a\right) }^{2}h\left( X\right) \left( {\;\operatorname{mod}\;p}\right) \) (i.e., if \( {X}^{n} - \overline{1} \in \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) admits a root of order \( \geq 2 \) in \( \mathbb{Z}/p\mathbb{Z} \)), then \( p \) divides \( n \).

b) Soit \( a \in \mathbb{N} \) . Montrer que si un nombre premier \( p \) divise \( {\Phi }_{n}\left( a\right) \) (où \( {\Phi }_{n}\left( X\right) \) désigne le polynôme cyclotomique d’indice \( n \) ), alors \( p \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) ou \( p \mid n \) .

> b) Let \( a \in \mathbb{N} \). Show that if a prime number \( p \) divides \( {\Phi }_{n}\left( a\right) \) (where \( {\Phi }_{n}\left( X\right) \) denotes the cyclotomic polynomial of index \( n \)), then \( p \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) or \( p \mid n \).

c) Montrer qu’il existe une infinité de nombres premiers de la forme \( {kn} + 1 \) , avec \( k \in \mathbb{N} \) .

> c) Show that there are infinitely many prime numbers of the form \( {kn} + 1 \), with \( k \in \mathbb{N} \).

Solution. a) Si \( {X}^{n} - 1 \equiv {\left( X - a\right) }^{2}h\left( X\right) \left( {\;\operatorname{mod}\;p}\right) \) , alors en substituant \( X \) par \( X + a \) on obtient \( {\left( X + a\right) }^{n} - 1 \equiv {X}^{2}h\left( {X + a}\right) \left( {\;\operatorname{mod}\;p}\right) \) . Ainsi, les coefficients des termes de degré 0 et 1 du polynôme \( {\left( X + a\right) }^{n} - 1 \) sont divisibles par \( p \) . Ceci s’écrit \( p \mid \left( {{a}^{n} - 1}\right) \) et \( p \mid \left( \begin{array}{l} n \\ 1 \end{array}\right) {a}^{n - 1} = n{a}^{n - 1} \) . Comme \( p \mid \left( {{a}^{n} - 1}\right) , p \nmid a \) donc \( a \) est premier avec \( p \) . Comme \( p \mid n{a}^{n - 1} \) et que \( p \) est premier avec \( {a}^{n - 1} \) (car premier avec \( a \) ), on a donc \( p \mid n \) .

> Solution. a) If \( {X}^{n} - 1 \equiv {\left( X - a\right) }^{2}h\left( X\right) \left( {\;\operatorname{mod}\;p}\right) \), then by substituting \( X \) with \( X + a \) we obtain \( {\left( X + a\right) }^{n} - 1 \equiv {X}^{2}h\left( {X + a}\right) \left( {\;\operatorname{mod}\;p}\right) \). Thus, the coefficients of the degree 0 and 1 terms of the polynomial \( {\left( X + a\right) }^{n} - 1 \) are divisible by \( p \). This is written as \( p \mid \left( {{a}^{n} - 1}\right) \) and \( p \mid \left( \begin{array}{l} n \\ 1 \end{array}\right) {a}^{n - 1} = n{a}^{n - 1} \). Since \( p \mid \left( {{a}^{n} - 1}\right) , p \nmid a \), then \( a \) is coprime to \( p \). As \( p \mid n{a}^{n - 1} \) and \( p \) is coprime to \( {a}^{n - 1} \) (because it is coprime to \( a \)), we therefore have \( p \mid n \).

b) La propriété \( {X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) des polynômes cyclotomiques (voir la question \( 1/\mathrm{b} \) ) du problème précédent) entraîne l’existence d’un polynôme \( F \in \mathbb{Z}\left\lbrack X\right\rbrack \) tel que \( {X}^{n} - 1 = {\Phi }_{n}F \) . On a donc \( {a}^{n} - 1 = {\Phi }_{n}\left( a\right) F\left( a\right) \) , et comme \( F\left( a\right) \in \mathbb{Z} \) , on a \( p \mid \left( {{a}^{n} - 1}\right) \) , autrement dit \( {a}^{n} \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . Notons \( m \) l’ordre de \( \bar{a} \) dans le sous groupe multiplicatif \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) . Comme \( {\bar{a}}^{n} = \overline{1} \) dans \( \mathbb{Z}/p\mathbb{Z} \) , on a \( m \mid n \) . On traite maintenant deux cas selon la valeur de \( m \) .

> b) The property \( {X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) of cyclotomic polynomials (see question \( 1/\mathrm{b} \) of the previous problem) implies the existence of a polynomial \( F \in \mathbb{Z}\left\lbrack X\right\rbrack \) such that \( {X}^{n} - 1 = {\Phi }_{n}F \). We therefore have \( {a}^{n} - 1 = {\Phi }_{n}\left( a\right) F\left( a\right) \), and since \( F\left( a\right) \in \mathbb{Z} \), we have \( p \mid \left( {{a}^{n} - 1}\right) \), in other words \( {a}^{n} \equiv 1\left( {\;\operatorname{mod}\;p}\right) \). Let \( m \) be the order of \( \bar{a} \) in the multiplicative subgroup \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \). As \( {\bar{a}}^{n} = \overline{1} \) in \( \mathbb{Z}/p\mathbb{Z} \), we have \( m \mid n \). We now consider two cases depending on the value of \( m \).

- Si \( m = n \) , alors \( \bar{a} \) est d’ordre \( n \) , donc \( n \) divise le cardinal du sous groupe \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) . Autrement dit \( n \mid  \left( {p - 1}\right) \) , c’est-à-dire \( p \equiv  1\left( {\;\operatorname{mod}\;n}\right) \) .

> - If \( m = n \), then \( \bar{a} \) is of order \( n \), so \( n \) divides the cardinality of the subgroup \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \). In other words \( n \mid  \left( {p - 1}\right) \), that is to say \( p \equiv  1\left( {\;\operatorname{mod}\;n}\right) \).

- Sinon on a \( m < n \) . Comme \( m \mid  n \) , on a

> - Otherwise we have \( m < n \). Since \( m \mid  n \), we have

\[
{X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid  n}}{\Phi }_{d} = {\Phi }_{n}\left( {\mathop{\prod }\limits_{{d \mid  m}}{\Phi }_{d}}\right) \left( {\mathop{\prod }\limits_{{d \mid  n, d \nmid  m, d \neq  n}}{\Phi }_{d}}\right)  = {\Phi }_{n} \cdot  \left( {{X}^{m} - 1}\right) \left( {\mathop{\prod }\limits_{{d \mid  n, d \nmid  m, d \neq  n}}{\Phi }_{d}}\right) .
\]

(*)

> Par hypothèse, on a \( p \mid {\Phi }_{n}\left( a\right) \) donc \( {\Phi }_{n}\left( a\right) \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) , et par ailleurs \( {a}^{m} \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . Autrement dit, \( \bar{a} \) est racine de \( {\overline{\Phi }}_{n} \) et de \( {X}^{m} - \overline{1} \) dans \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . D’après \( \left( *\right) \) , ceci entraîne le fait que \( \bar{a} \) est racine au moins double de \( {X}^{n} - \overline{1} \) , donc \( p \mid n \) d’après la question précédente.

By hypothesis, we have \( p \mid {\Phi }_{n}\left( a\right) \) so \( {\Phi }_{n}\left( a\right) \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) , and furthermore \( {a}^{m} \equiv 1\left( {\;\operatorname{mod}\;p}\right) \) . In other words, \( \bar{a} \) is a root of \( {\overline{\Phi }}_{n} \) and of \( {X}^{m} - \overline{1} \) in \( \mathbb{Z}/p\mathbb{Z}\left\lbrack X\right\rbrack \) . According to \( \left( *\right) \) , this implies that \( \bar{a} \) is at least a double root of \( {X}^{n} - \overline{1} \) , therefore \( p \mid n \) according to the previous question.

> c) Raisonnons par l'absurde et supposons qu'il n'y ait qu'un nombre fini de nombres premiers de la forme \( 1 + {kn} \) . Nous les notons \( {p}_{1},\ldots ,{p}_{m} \) . On considère l’entier \( N = {\Phi }_{n}\left( \alpha \right) \) avec \( \alpha = n{p}_{1}\cdots {p}_{m} \) . On a \( N \equiv {a}_{0}\left( {\;\operatorname{mod}\;\alpha }\right) \) , od \( {a}_{0} \) est le coefficient constant de \( {\Phi }_{n} \) . L’identité \( {X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) entraîne \( - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d}\left( 0\right) \) et comme les \( {\Phi }_{d}\left( 0\right) \) sont entiers, on a forcément \( {a}_{0} = {\Phi }_{n}\left( 0\right) = \pm 1 \) . Ainsi, \( N \equiv \pm 1\left( {\;\operatorname{mod}\;\alpha }\right) \) . Or \( \left| N\right| \geq 2\left( {\Pi }_{n}\right. \) désignant l’ensemble des racines primitives \( n \) -ièmes de

c) Let us reason by contradiction and assume that there is only a finite number of prime numbers of the form \( 1 + {kn} \) . We denote them \( {p}_{1},\ldots ,{p}_{m} \) . Consider the integer \( N = {\Phi }_{n}\left( \alpha \right) \) with \( \alpha = n{p}_{1}\cdots {p}_{m} \) . We have \( N \equiv {a}_{0}\left( {\;\operatorname{mod}\;\alpha }\right) \) , where \( {a}_{0} \) is the constant coefficient of \( {\Phi }_{n} \) . The identity \( {X}^{n} - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d} \) implies \( - 1 = \mathop{\prod }\limits_{{d \mid n}}{\Phi }_{d}\left( 0\right) \) and since the \( {\Phi }_{d}\left( 0\right) \) are integers, we necessarily have \( {a}_{0} = {\Phi }_{n}\left( 0\right) = \pm 1 \) . Thus, \( N \equiv \pm 1\left( {\;\operatorname{mod}\;\alpha }\right) \) . However, \( \left| N\right| \geq 2\left( {\Pi }_{n}\right. \) denoting the set of primitive \( n \) -th roots of

> l’unité, on a \( \left| N\right| = \left| {{\Phi }_{n}\left( \alpha \right) }\right| = \mathop{\prod }\limits_{{\xi \in {\Pi }_{n}}}\left| {\alpha - \xi }\right| \) , et comme \( \alpha \geq n \) , on a \( \left| {\alpha - \xi }\right| > 1 \) pour tout \( \xi \in {\Pi }_{n} \) donc \( \left| N\right| > 1 \) ). Il existe donc un nombre premier \( p \) divisant \( N \) . D’après la question précédente, on doit avoir \( p \mid n \) ou \( p \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) . Mais ceci est impossible étant donnée la congruence \( N \equiv \pm 1 \; \left( {{\;\operatorname{mod}\;n}{p}_{1}\cdots {p}_{m}}\right) \) .

unity, we have \( \left| N\right| = \left| {{\Phi }_{n}\left( \alpha \right) }\right| = \mathop{\prod }\limits_{{\xi \in {\Pi }_{n}}}\left| {\alpha - \xi }\right| \) , and since \( \alpha \geq n \) , we have \( \left| {\alpha - \xi }\right| > 1 \) for all \( \xi \in {\Pi }_{n} \) therefore \( \left| N\right| > 1 \) ). There exists therefore a prime number \( p \) dividing \( N \) . According to the previous question, we must have \( p \mid n \) or \( p \equiv 1\left( {\;\operatorname{mod}\;n}\right) \) . But this is impossible given the congruence \( N \equiv \pm 1 \; \left( {{\;\operatorname{mod}\;n}{p}_{1}\cdots {p}_{m}}\right) \) .

> Remarque. La version forte du théorème de Dirichlet est discutée dans la remarque qui suit l'exercice 7 page 14.

Remark. The strong version of Dirichlet's theorem is discussed in the remark following exercise 7 on page 14.

> PROBLEME 12 (THÉORÉME DE WEDDERBURN : TOUT CORPS FINI EST COMMUTATIF). Pour faire ce problème, il est nécessaire de connaître la partie 1/ du problème 10 page 97 ainsi que l'équation aux classes (voir le corollaire 1 page 24).

PROBLEM 12 (WEDDERBURN'S THEOREM: EVERY FINITE DIVISION RING IS COMMUTATIVE). To do this problem, it is necessary to know part 1/ of problem 10 on page 97 as well as the class equation (see corollary 1 on page 24).

> Soit \( \mathbb{K} \) un corps fini. On veut montrer que \( \mathbb{K} \) est commutatif. Pour cela, on procède par récurrence sur \( \operatorname{Card}\left( \mathbb{K}\right) \) . Si \( \operatorname{Card}\left( \mathbb{K}\right) = 2 \) , le résultat est évident. On suppose maintenant que pour tout corps \( \mathbb{L} \) tel que \( \operatorname{Card}\left( \mathbb{L}\right) < \operatorname{Card}\left( \mathbb{K}\right) ,\mathbb{L} \) est commutatif \( \left( *\right) \) . Nous allons montrer que \( \mathbb{K} \) est lui aussi commutatif. Nous raisonnerons par l’absurde en supposant \( \mathbb{K} \) non commutatif.

Let \( \mathbb{K} \) be a finite field. We want to show that \( \mathbb{K} \) is commutative. To do this, we proceed by induction on \( \operatorname{Card}\left( \mathbb{K}\right) \). If \( \operatorname{Card}\left( \mathbb{K}\right) = 2 \), the result is obvious. We now assume that for any field \( \mathbb{L} \) such that \( \operatorname{Card}\left( \mathbb{L}\right) < \operatorname{Card}\left( \mathbb{K}\right) ,\mathbb{L} \) is commutative \( \left( *\right) \). We will show that \( \mathbb{K} \) is also commutative. We will reason by contradiction by assuming \( \mathbb{K} \) is non-commutative.

> a) Montrer que le centre de \( \mathbb{K} \) défini par \( \mathcal{Z} = \{ x \in \mathbb{K} \mid \forall y \in \mathbb{K},{xy} = {yx}\} \) est un sous-corps de \( \mathbb{K} \) . Prouver ensuite qu’il existe \( n \in \mathbb{N}, n \geq 2 \) , tel que \( \operatorname{Card}\left( \mathbb{K}\right) = {q}^{n} \) où \( q = \operatorname{Card}\mathcal{Z} \) .

a) Show that the center of \( \mathbb{K} \) defined by \( \mathcal{Z} = \{ x \in \mathbb{K} \mid \forall y \in \mathbb{K},{xy} = {yx}\} \) is a subfield of \( \mathbb{K} \). Then prove that there exists \( n \in \mathbb{N}, n \geq 2 \), such that \( \operatorname{Card}\left( \mathbb{K}\right) = {q}^{n} \) where \( q = \operatorname{Card}\mathcal{Z} \).

> b) Pour tout \( x \in \mathbb{K} \) , on pose \( {\mathbb{K}}_{x} = \{ y \in \mathbb{K} \mid {yx} = {xy}\} \) . Prouver qu’il existe un entier \( d \) divisant \( n \) tel que \( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) = {q}^{d} \) .

b) For any \( x \in \mathbb{K} \), we set \( {\mathbb{K}}_{x} = \{ y \in \mathbb{K} \mid {yx} = {xy}\} \). Prove that there exists an integer \( d \) dividing \( n \) such that \( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) = {q}^{d} \).

> c) Montrer que l'on peut écrire

c) Show that one can write

\[
\operatorname{Card}\left( {\mathbb{K}}^{ * }\right)  = q - 1 + \mathop{\sum }\limits_{\substack{{d \mid  n} \\  {d \neq  n} }}{\lambda }_{d}\frac{{q}^{n} - 1}{{q}^{d} - 1},\;\text{ avec }\;\forall d,{\lambda }_{d} \in  \mathbb{Z}.
\]

d) En observant que le polynôme cyclotomique \( {\Phi }_{n} \) divise \( \left( {{X}^{n} - 1}\right) /\left( {{X}^{d} - 1}\right) \) si \( d \mid n \) , \( d \neq n \) , montrer que \( \mathbb{K} \) est commutatif.

> d) By observing that the cyclotomic polynomial \( {\Phi }_{n} \) divides \( \left( {{X}^{n} - 1}\right) /\left( {{X}^{d} - 1}\right) \) if \( d \mid n \), \( d \neq n \), show that \( \mathbb{K} \) is commutative.

Solution. a) Nous aurons besoin du lemme suivant.

> Solution. a) We will need the following lemma.

LEMME. Soient \( {\mathbb{L}}_{1} \subset {\mathbb{L}}_{2} \) deux corps finis, avec \( {\mathbb{L}}_{1} \) commutatif. Alors il existe \( k \in {\mathbb{N}}^{ * } \) tel que \( \operatorname{Card}\left( {\mathbb{L}}_{2}\right) = {\left( \operatorname{Card}\left( {\mathbb{L}}_{1}\right) \right) }^{k} \) .

> LEMMA. Let \( {\mathbb{L}}_{1} \subset {\mathbb{L}}_{2} \) be two finite fields, with \( {\mathbb{L}}_{1} \) commutative. Then there exists \( k \in {\mathbb{N}}^{ * } \) such that \( \operatorname{Card}\left( {\mathbb{L}}_{2}\right) = {\left( \operatorname{Card}\left( {\mathbb{L}}_{1}\right) \right) }^{k} \).

En effet, \( {\mathbb{L}}_{1} \) étant un sous-corps commutatif de \( {\mathbb{L}}_{2},{\mathbb{L}}_{2} \) est un \( {\mathbb{L}}_{1} \) -espace vectoriel, de dimension finie \( k \) car \( {\mathbb{L}}_{2} \) est fini. Le corps \( {\mathbb{L}}_{2} \) est donc isomorphe comme \( {\mathbb{L}}_{1} \) -espace vectoriel à \( {\mathbb{L}}_{1}^{k} \) , et on en déduit que \( \operatorname{Card}\left( {\mathbb{L}}_{2}\right) = \operatorname{Card}\left( {\mathbb{L}}_{1}^{k}\right) = {\left( \operatorname{Card}\left( {\mathbb{L}}_{1}\right) \right) }^{k} \) .

> Indeed, \( {\mathbb{L}}_{1} \) being a commutative subfield of \( {\mathbb{L}}_{2},{\mathbb{L}}_{2} \) is an \( {\mathbb{L}}_{1} \)-vector space of finite dimension \( k \) because \( {\mathbb{L}}_{2} \) is finite. The field \( {\mathbb{L}}_{2} \) is therefore isomorphic as an \( {\mathbb{L}}_{1} \)-vector space to \( {\mathbb{L}}_{1}^{k} \), and we deduce that \( \operatorname{Card}\left( {\mathbb{L}}_{2}\right) = \operatorname{Card}\left( {\mathbb{L}}_{1}^{k}\right) = {\left( \operatorname{Card}\left( {\mathbb{L}}_{1}\right) \right) }^{k} \).

Ceci étant, on vérifie facilement que \( \mathcal{Z} \) est un sous corps commutatif de \( \mathbb{K} \) . D’après le lemme, il existe donc \( n \in {\mathbb{N}}^{ * } \) tel que \( \operatorname{Card}\left( \mathbb{K}\right) = {\left( \operatorname{Card}\left( \mathcal{Z}\right) \right) }^{n} \) . Or \( \mathbb{K} \neq \mathcal{Z} \) (car \( \mathbb{K} \) n’est pas commutatif alors que \( \mathcal{Z} \) l’est), donc \( n > 1 \) , d’où le résultat.

> That being said, it is easy to verify that \( \mathcal{Z} \) is a commutative subfield of \( \mathbb{K} \). According to the lemma, there therefore exists \( n \in {\mathbb{N}}^{ * } \) such that \( \operatorname{Card}\left( \mathbb{K}\right) = {\left( \operatorname{Card}\left( \mathcal{Z}\right) \right) }^{n} \). However, \( \mathbb{K} \neq \mathcal{Z} \) (because \( \mathbb{K} \) is not commutative while \( \mathcal{Z} \) is), so \( n > 1 \), hence the result.

b) On remarque ici aussi que pour tout \( x,{\mathbb{K}}_{x} \) est un sous corps de \( \mathbb{K} \) . Si \( {\mathbb{K}}_{x} = \mathbb{K} \) , alors on a \( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) = \operatorname{Card}\left( \mathbb{K}\right) = {q}^{n} \) . Sinon, \( {\mathbb{K}}_{x} \) est strictement inclus dans \( \mathbb{K} \) et donc d’après \( \left( *\right) ,{\mathbb{K}}_{x} \) est commutatif. On peut donc appliquer le lemme qui entraîne l’existence de \( k \in {\mathbb{N}}^{ * } \) tel que \( \operatorname{Card}\left( \mathbb{K}\right) = {\left( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) \right) }^{k}\;\left( {* * }\right) \) . Par ailleurs, \( \mathcal{Z} \) est aussi un sous-corps commutatif de \( {\mathbb{K}}_{x} \) , donc d’après le lemme il existe \( d \in {\mathbb{N}}^{ * } \) tel que \( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) = {\left( \operatorname{Card}\mathcal{Z}\right) }^{d} = {q}^{d} \) . Avec \( \left( {* * }\right) \) , on trouve donc \( {q}^{n} = \operatorname{Card}\left( \mathbb{K}\right) = {\left( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) \right) }^{k} = {\left( {q}^{d}\right) }^{k} = {q}^{dk} \) . Donc \( n = {dk} \) , ce qui entraîne que \( d \mid n \) , d’où le résultat.

> b) We note here too that for all \( x,{\mathbb{K}}_{x} \) is a subfield of \( \mathbb{K} \). If \( {\mathbb{K}}_{x} = \mathbb{K} \), then we have \( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) = \operatorname{Card}\left( \mathbb{K}\right) = {q}^{n} \). Otherwise, \( {\mathbb{K}}_{x} \) is strictly included in \( \mathbb{K} \) and therefore, according to \( \left( *\right) ,{\mathbb{K}}_{x} \), is commutative. We can thus apply the lemma which leads to the existence of \( k \in {\mathbb{N}}^{ * } \) such that \( \operatorname{Card}\left( \mathbb{K}\right) = {\left( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) \right) }^{k}\;\left( {* * }\right) \). Furthermore, \( \mathcal{Z} \) is also a commutative subfield of \( {\mathbb{K}}_{x} \), so according to the lemma there exists \( d \in {\mathbb{N}}^{ * } \) such that \( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) = {\left( \operatorname{Card}\mathcal{Z}\right) }^{d} = {q}^{d} \). With \( \left( {* * }\right) \), we therefore find \( {q}^{n} = \operatorname{Card}\left( \mathbb{K}\right) = {\left( \operatorname{Card}\left( {\mathbb{K}}_{x}\right) \right) }^{k} = {\left( {q}^{d}\right) }^{k} = {q}^{dk} \). Thus \( n = {dk} \), which implies that \( d \mid n \), hence the result.

c) C'est l'équation aux classes appliquée au groupe multiplicatif \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) . En effet, le centre de ce groupe est \( {\mathcal{Z}}^{ * } \) . Avec les notations de la partie 2.4 du chapitre I, on a

> c) This is the class equation applied to the multiplicative group \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \). Indeed, the center of this group is \( {\mathcal{Z}}^{ * } \). Using the notation from part 2.4 of chapter I, we have

\[
\operatorname{Card}\left( {\mathbb{K}}^{ * }\right)  = \operatorname{Card}{\mathcal{Z}}^{ * } + \mathop{\sum }\limits_{{x \in  {\theta }^{\prime }}}\frac{\operatorname{Card}\left( {\mathbb{K}}^{ * }\right) }{\operatorname{Card}\left( {S}_{x}\right) }
\]

où \( {S}_{x} \) désigne le stabilisateur de \( x \) , c’est-à-dire \( {S}_{x} = \left\{ {y \in {\mathbb{K}}^{ * } \mid {xy} = {yx}}\right\} = {\mathbb{K}}_{x}^{ * } \) . D’après la question précédente, il existe donc \( d \in {\mathbb{N}}^{ * } \) divisant \( n \) tel que \( \operatorname{Card}\left( {S}_{x}\right) = {q}^{d} - 1 \) , et \( d \neq n \) (car

> where \( {S}_{x} \) denotes the stabilizer of \( x \), that is to say \( {S}_{x} = \left\{ {y \in {\mathbb{K}}^{ * } \mid {xy} = {yx}}\right\} = {\mathbb{K}}_{x}^{ * } \). According to the previous question, there therefore exists \( d \in {\mathbb{N}}^{ * } \) dividing \( n \) such that \( \operatorname{Card}\left( {S}_{x}\right) = {q}^{d} - 1 \), and \( d \neq n \) (because

\( x \in {\theta }^{\prime } \) et \( {\theta }^{\prime } \cap {\mathcal{Z}}^{ * } = \varnothing \) ). Si maintenant pour tout \( d \mid n,{\lambda }_{d} \) désigne le nombre de \( x \in {\theta }^{\prime } \) tel que \( \operatorname{Card}\left( {S}_{x}\right) = {q}^{d} - 1 \) , on peut réécrire l’équation aux classes sous la forme

> \( x \in {\theta }^{\prime } \) and \( {\theta }^{\prime } \cap {\mathcal{Z}}^{ * } = \varnothing \) ). If now for all \( d \mid n,{\lambda }_{d} \) denotes the number of \( x \in {\theta }^{\prime } \) such that \( \operatorname{Card}\left( {S}_{x}\right) = {q}^{d} - 1 \) , we can rewrite the class equation in the form

\[
{q}^{n} - 1 = \operatorname{Card}\left( {\mathbb{K}}^{ * }\right)  = \left( {q - 1}\right)  + \mathop{\sum }\limits_{\substack{{d \mid  n} \\  {d \neq  n} }}{\lambda }_{d}\left( \frac{{q}^{n} - 1}{{q}^{d} - 1}\right) .
\]

\( \left( {* * * }\right) \)

> d) Si \( d \mid n, d \neq n \) , on a

d) If \( d \mid n, d \neq n \) , we have

\[
{X}^{n} - 1 = {\Phi }_{n}\mathop{\prod }\limits_{{e \mid  n, e \neq  n}}{\Phi }_{e} = {\Phi }_{n}\left( {\mathop{\prod }\limits_{{e \mid  d}}{\Phi }_{e}}\right) \left( {\mathop{\prod }\limits_{{e \mid  n, e \neq  n, e \nmid  d}}{\Phi }_{e}}\right)  = {\Phi }_{n} \cdot  \left( {{X}^{d} - 1}\right) \left( {\mathop{\prod }\limits_{{e \mid  n, e \neq  n, e \nmid  d}}{\Phi }_{e}}\right) ,
\]

donc \( {\Phi }_{n} \) divise \( \left( {{X}^{n} - 1}\right) /\left( {{X}^{d} - 1}\right) \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) . Ceci étant vrai pour tout diviseur \( d\mathrm{\;d}en \) distinct de \( n,{\Phi }_{n} \) divise \( \mathop{\sum }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\lambda }_{d}\frac{{X}^{n} - 1}{{X}^{d} - 1} \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) . Comme de plus \( {\Phi }_{n} \) divise \( {X}^{n} - 1 \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) , il divise

> therefore \( {\Phi }_{n} \) divides \( \left( {{X}^{n} - 1}\right) /\left( {{X}^{d} - 1}\right) \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) . This being true for any divisor \( d\mathrm{\;d}en \) distinct from \( n,{\Phi }_{n} \) divides \( \mathop{\sum }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\lambda }_{d}\frac{{X}^{n} - 1}{{X}^{d} - 1} \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) . As moreover \( {\Phi }_{n} \) divides \( {X}^{n} - 1 \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) , it divides

\( \left\lbrack {\left( {{X}^{n} - 1}\right) - \mathop{\sum }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\lambda }_{d}\frac{{X}^{n} - 1}{{X}^{d} - 1}}\right\rbrack \) dans \( \mathbb{Z}\left\lbrack X\right\rbrack \) . Donc \( {\Phi }_{n}\left( q\right) \) divise \( \left\lbrack {\left( {{q}^{n} - 1}\right) - \mathop{\sum }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\lambda }_{d}\frac{{q}^{n} - 1}{{q}^{d} - 1}}\right\rbrack \) , et ce

> \( \left\lbrack {\left( {{X}^{n} - 1}\right) - \mathop{\sum }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\lambda }_{d}\frac{{X}^{n} - 1}{{X}^{d} - 1}}\right\rbrack \) in \( \mathbb{Z}\left\lbrack X\right\rbrack \) . Thus \( {\Phi }_{n}\left( q\right) \) divides \( \left\lbrack {\left( {{q}^{n} - 1}\right) - \mathop{\sum }\limits_{\substack{{d \mid n} \\ {d \neq n} }}{\lambda }_{d}\frac{{q}^{n} - 1}{{q}^{d} - 1}}\right\rbrack \) , and this

dernier égale \( q - 1 \) d’après (***). Donc \( \left| {{\Phi }_{n}\left( q\right) }\right| \leq q - 1 \) . Or \( n \geq 2 \) donc \( \left| {{\Phi }_{n}\left( q\right) }\right| = \mathop{\prod }\limits_{{\xi \in {\Pi }_{n}}}\left| {q - \xi }\right| > \)

> latter equals \( q - 1 \) according to (***). Thus \( \left| {{\Phi }_{n}\left( q\right) }\right| \leq q - 1 \) . However \( n \geq 2 \) therefore \( \left| {{\Phi }_{n}\left( q\right) }\right| = \mathop{\prod }\limits_{{\xi \in {\Pi }_{n}}}\left| {q - \xi }\right| > \)

\( \mathop{\prod }\limits_{{i = 1}}^{{\varphi \left( n\right) }}\left| {q - 1}\right| \geq \left| {q - 1}\right| \) , ce qui est absurde. Le corps fini \( \mathbb{K} \) est donc commutatif. Le raisonnement

> \( \mathop{\prod }\limits_{{i = 1}}^{{\varphi \left( n\right) }}\left| {q - 1}\right| \geq \left| {q - 1}\right| \) , which is absurd. The finite field \( \mathbb{K} \) is therefore commutative. The reasoning

par récurrence est ainsi achevé et montre que tout corps fini est commutatif.

> by induction is thus completed and shows that every finite field is commutative.

Remarque. Si on veut trouver un corps non commutatif, il faut donc que celui ci soit infini. Hamilton fut le premier en 1843 à exhiber un corps non commutatif : le corps \( \mathbb{H} \) des quaternions ( \( \mathbb{H} \) est un surcorps de \( \mathbb{C} \) . Ses éléments sont des quadruplets \( a + {bi} + {cj} + {dk} \) , munis de la loi d'addition usuelle et d'une loi de multiplication associative et distributive par rapport à l’addition, vérifiant \( {ij} = - {ji} = k,{jk} = - {kj} = i,{ki} = - {ik} = j \) et \( {i}^{2} = {j}^{2} = {k}^{2} = - 1 \) . Le lecteur pourra bien sûr vérifier que l’on a bien affaire à un corps).

> Remark. If one wishes to find a non-commutative field, it must therefore be infinite. Hamilton was the first in 1843 to exhibit a non-commutative field: the field \( \mathbb{H} \) of quaternions (\( \mathbb{H} \) is an extension field of \( \mathbb{C} \). Its elements are quadruplets \( a + {bi} + {cj} + {dk} \), equipped with the usual addition law and a multiplication law that is associative and distributive with respect to addition, satisfying \( {ij} = - {ji} = k,{jk} = - {kj} = i,{ki} = - {ik} = j \) and \( {i}^{2} = {j}^{2} = {k}^{2} = - 1 \). The reader may, of course, verify that this is indeed a field).

PROBLÉME 13 (POLYNÔMES DE TCHÉBYCHEFF ET APPLICATIONS). Soit \( I = \left\lbrack {-1,1}\right\rbrack \) . On muni \( \mathcal{C}\left( {I,\mathbb{C}}\right) \) (espace vectoriel des fonctions continues de \( I \) dans \( \mathbb{C} \) ) de la norme \( \parallel .{\parallel }_{\infty } \) définie pour tout \( f \in \mathcal{C}\left( {I,\mathbb{C}}\right) \) par \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in I}}\left| {f\left( x\right) }\right| \) . De même, si \( f : \mathbb{R} \rightarrow \mathbb{C} \) est \( {2\pi } \) -périodique, on note \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in \mathbb{R}}}\left| {f\left( x\right) }\right| \) .

> PROBLEM 13 (CHEBYSHEV POLYNOMIALS AND APPLICATIONS). Let \( I = \left\lbrack {-1,1}\right\rbrack \). We equip \( \mathcal{C}\left( {I,\mathbb{C}}\right) \) (vector space of continuous functions from \( I \) to \( \mathbb{C} \)) with the norm \( \parallel .{\parallel }_{\infty } \) defined for all \( f \in \mathcal{C}\left( {I,\mathbb{C}}\right) \) by \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in I}}\left| {f\left( x\right) }\right| \). Similarly, if \( f : \mathbb{R} \rightarrow \mathbb{C} \) is \( {2\pi } \)-periodic, we denote \( \parallel f{\parallel }_{\infty } = \mathop{\sup }\limits_{{x \in \mathbb{R}}}\left| {f\left( x\right) }\right| \).

Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {T}_{n} : I \rightarrow \mathbb{R}\;x \mapsto \cos \left\lbrack {n\arccos \left( x\right) }\right\rbrack \) et \( {U}_{n} = {T}_{n + 1}^{\prime }/\left( {n + 1}\right) \) . 1/ Montrer que \( {T}_{n} \) et \( {U}_{n} \) sont des fonctions polynômes de degré \( n \) . Après avoir explicité \( {U}_{n} \) , calculer \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } \) et \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \) .

> For all \( n \in {\mathbb{N}}^{ * } \), we denote \( {T}_{n} : I \rightarrow \mathbb{R}\;x \mapsto \cos \left\lbrack {n\arccos \left( x\right) }\right\rbrack \) and \( {U}_{n} = {T}_{n + 1}^{\prime }/\left( {n + 1}\right) \). 1/ Show that \( {T}_{n} \) and \( {U}_{n} \) are polynomial functions of degree \( n \). After expressing \( {U}_{n} \) explicitly, calculate \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } \) and \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \).

2 / Soit \( n \in {\mathbb{N}}^{ * } \) . Pour \( 1 \leq i \leq n \) , on pose \( {x}_{i} = \cos \frac{\left( {{2i} - 1}\right) \pi }{2n} \) . Montrer

> 2/ Let \( n \in {\mathbb{N}}^{ * } \). For \( 1 \leq i \leq n \), we set \( {x}_{i} = \cos \frac{\left( {{2i} - 1}\right) \pi }{2n} \). Show

\[
\forall P \in  \mathbb{C}\left\lbrack  X\right\rbrack  ,\deg \left( P\right)  \leq  n - 1,\;P\left( X\right)  = \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}{\left( -1\right) }^{i - 1}\sqrt{1 - {x}_{i}^{2}}P\left( {x}_{i}\right) \frac{{T}_{n}\left( X\right) }{X - {x}_{i}}.
\]

3/ a) Soit \( P \in \mathcal{C}\left( {I,\mathbb{C}}\right) \) une fonction polynôme de degré \( n - 1 \) telle que pour tout \( x \in I \) , \( \left| {\sqrt{1 - {x}^{2}}P\left( x\right) }\right| \leq 1 \) . Montrer que \( \parallel P{\parallel }_{\infty } \leq n \) .

> 3/ a) Let \( P \in \mathcal{C}\left( {I,\mathbb{C}}\right) \) be a polynomial function of degree \( n - 1 \) such that for all \( x \in I \), \( \left| {\sqrt{1 - {x}^{2}}P\left( x\right) }\right| \leq 1 \). Show that \( \parallel P{\parallel }_{\infty } \leq n \).

b) Soit \( S : \mathbb{R} \rightarrow \mathbb{C}\;\theta \mapsto \mathop{\sum }\limits_{{k = 1}}^{n}{\mu }_{k}\sin \left( {k\theta }\right) \) avec les \( {\mu }_{k} \in \mathbb{C} \) . Si \( \parallel S{\parallel }_{\infty } = 1 \) , montrer que

> b) Let \( S : \mathbb{R} \rightarrow \mathbb{C}\;\theta \mapsto \mathop{\sum }\limits_{{k = 1}}^{n}{\mu }_{k}\sin \left( {k\theta }\right) \) with the \( {\mu }_{k} \in \mathbb{C} \). If \( \parallel S{\parallel }_{\infty } = 1 \), show that

\[
\forall \theta  \in  \mathbb{R} \smallsetminus  \pi \mathbb{Z},\left| \frac{S\left( \theta \right) }{\sin \theta }\right|  \leq  n.
\]

4/ Inégalité de Bernstein. Soit \( g : \mathbb{R} \rightarrow \mathbb{C}\;\theta \mapsto \mathop{\sum }\limits_{{k = - n}}^{n}{\lambda }_{k}{e}^{ik\theta } \) , où les \( {\lambda }_{k} \in \mathbb{C} \) . Montrer que \( {\begin{Vmatrix}{g}^{\prime }\end{Vmatrix}}_{\infty } \leq n\parallel g{\parallel }_{\infty } \) .

> 4/ Bernstein's inequality. Let \( g : \mathbb{R} \rightarrow \mathbb{C}\;\theta \mapsto \mathop{\sum }\limits_{{k = - n}}^{n}{\lambda }_{k}{e}^{ik\theta } \) , where \( {\lambda }_{k} \in \mathbb{C} \) . Show that \( {\begin{Vmatrix}{g}^{\prime }\end{Vmatrix}}_{\infty } \leq n\parallel g{\parallel }_{\infty } \) .

5/ Inégalité de Markov. Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( P\right) = n \in {\mathbb{N}}^{ * } \) . On regarde \( P \) comme un élément de \( \mathcal{C}\left( {I,\mathbb{C}}\right) \) . Montrer que \( {\begin{Vmatrix}{P}^{\prime }\end{Vmatrix}}_{\infty } \leq {n}^{2}\parallel P{\parallel }_{\infty } \) .

> 5/ Markov's inequality. Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( P\right) = n \in {\mathbb{N}}^{ * } \) . We view \( P \) as an element of \( \mathcal{C}\left( {I,\mathbb{C}}\right) \) . Show that \( {\begin{Vmatrix}{P}^{\prime }\end{Vmatrix}}_{\infty } \leq {n}^{2}\parallel P{\parallel }_{\infty } \) .

Solution. 1/ Soit \( x \in I \) . Posons \( \theta = \arccos \left( x\right) \) , de sorte que \( x = \cos \theta \) . On a

> Solution. 1/ Let \( x \in I \) . Let \( \theta = \arccos \left( x\right) \) , so that \( x = \cos \theta \) . We have

\[
{T}_{n}\left( x\right)  = \Re \left\lbrack  {\left( \cos \theta  + i\sin \theta \right) }^{n}\right\rbrack   = \mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/2\right\rbrack  }\left( \begin{matrix} n \\  {2k} \end{matrix}\right) {\cos }^{n - {2k}}\theta {\left( -{\sin }^{2}\theta \right) }^{k} = \mathop{\sum }\limits_{{k = 0}}^{\left\lbrack  n/2\right\rbrack  }\left( \begin{matrix} n \\  {2k} \end{matrix}\right) {x}^{n - {2k}}{\left( {x}^{2} - 1\right) }^{k}.
\]

Ainsi, \( {T}_{n} \) est une fonction polynôme de degré \( n \) (son terme dominant est \( \mathop{\sum }\limits_{{0 < {2k} \leq n}}\left( \begin{matrix} n \\ {2k} \end{matrix}\right) \neq 0 \) ). Donc \( {U}_{n} = {T}_{n + 1}^{\prime }/\left( {n + 1}\right) \) également, et par ailleurs, lorsque \( x \in \rbrack - 1,1\lbrack \) on a

> Thus, \( {T}_{n} \) is a polynomial function of degree \( n \) (its leading term is \( \mathop{\sum }\limits_{{0 < {2k} \leq n}}\left( \begin{matrix} n \\ {2k} \end{matrix}\right) \neq 0 \) ). Therefore \( {U}_{n} = {T}_{n + 1}^{\prime }/\left( {n + 1}\right) \) as well, and furthermore, when \( x \in \rbrack - 1,1\lbrack \) we have

\[
{U}_{n}\left( x\right)  = \frac{{T}_{n + 1}^{\prime }\left( x\right) }{n + 1} =  - \frac{n + 1}{\sqrt{1 - {x}^{2}}} \cdot  \left( {-\frac{\sin \left\lbrack  {\left( {n + 1}\right) \arccos \left( x\right) }\right\rbrack  }{n + 1}}\right)  = \frac{\sin \left\lbrack  {\left( {n + 1}\right) \arccos \left( x\right) }\right\rbrack  }{\sin \left\lbrack  {\arccos \left( x\right) }\right\rbrack  }.
\]

(*)

> Calculons maintenant \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } \) et \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \) . Lorsque \( x \in I \) , la forme \( {T}_{n}\left( x\right) = \cos \left\lbrack {n\arccos \left( x\right) }\right\rbrack \) , entraîne \( \left| {{T}_{n}\left( x\right) }\right| \leq 1 \) , et comme \( {T}_{n}\left( 1\right) = 1 \) , on a \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } = 1 \) . Lorsque \( x \in \rbrack - 1,1\lbrack \) , A partir de l’inégalité \( \left| {\sin \left( {n\theta }\right) }\right| \leq n\left| {\sin \left( \theta \right) }\right| \) (que l’on obtient immédiatement par récurrence sur \( n \) ), la forme (*) montre que pour \( x \in \rbrack - 1,1\left\lbrack {,\left| {{U}_{n}\left( x\right) }\right| \leq n + 1}\right. \) . Or \( \mathop{\lim }\limits_{\substack{{x \rightarrow 1} \\ {x \neq 1} }}{U}_{n}\left( x\right) = n + 1 \) . Donc \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } = n + 1 \) . 2 / Si \( 1 \leq i \leq n \) , on a \( {T}_{n}\left( {x}_{i}\right) = \cos \left\lbrack {n\arccos \left( {x}_{i}\right) }\right\rbrack = \cos \left\lbrack {\left( {{2i} - 1}\right) \pi /2}\right\rbrack = 0 \) . Les \( n \) valeurs distinctes \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) sont donc des racines de \( {T}_{n} \) . Or \( \deg \left( {T}_{n}\right) = n \) , donc il existe \( \lambda \neq 0 \) tel que \( {T}_{n}\left( X\right) = \; \lambda \left( {X - {x}_{1}}\right) \cdots \left( {X - {x}_{n}}\right) . \)

Let us now calculate \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } \) and \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } \) . When \( x \in I \) , the form \( {T}_{n}\left( x\right) = \cos \left\lbrack {n\arccos \left( x\right) }\right\rbrack \) , leads to \( \left| {{T}_{n}\left( x\right) }\right| \leq 1 \) , and since \( {T}_{n}\left( 1\right) = 1 \) , we have \( {\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } = 1 \) . When \( x \in \rbrack - 1,1\lbrack \) , From the inequality \( \left| {\sin \left( {n\theta }\right) }\right| \leq n\left| {\sin \left( \theta \right) }\right| \) (which is obtained immediately by induction on \( n \) ), the form (*) shows that for \( x \in \rbrack - 1,1\left\lbrack {,\left| {{U}_{n}\left( x\right) }\right| \leq n + 1}\right. \) . However \( \mathop{\lim }\limits_{\substack{{x \rightarrow 1} \\ {x \neq 1} }}{U}_{n}\left( x\right) = n + 1 \) . Therefore \( {\begin{Vmatrix}{U}_{n}\end{Vmatrix}}_{\infty } = n + 1 \) . 2 / If \( 1 \leq i \leq n \) , we have \( {T}_{n}\left( {x}_{i}\right) = \cos \left\lbrack {n\arccos \left( {x}_{i}\right) }\right\rbrack = \cos \left\lbrack {\left( {{2i} - 1}\right) \pi /2}\right\rbrack = 0 \) . The \( n \) distinct values \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) are therefore roots of \( {T}_{n} \) . However \( \deg \left( {T}_{n}\right) = n \) , so there exists \( \lambda \neq 0 \) such that \( {T}_{n}\left( X\right) = \; \lambda \left( {X - {x}_{1}}\right) \cdots \left( {X - {x}_{n}}\right) . \)

> L’interpolation de Lagrange assure l’existence d’un unique polynôme de degré \( \leq n - 1 \) égal à \( P\left( {x}_{i}\right) \) en \( {x}_{i} \) (voir la page 65). Ce polynôme est donc \( P \) et on a

Lagrange interpolation ensures the existence of a unique polynomial of degree \( \leq n - 1 \) equal to \( P\left( {x}_{i}\right) \) at \( {x}_{i} \) (see page 65). This polynomial is therefore \( P \) and we have

\[
P\left( X\right)  = {T}_{n}\left( X\right) \mathop{\sum }\limits_{{i = 1}}^{n}\frac{P\left( {x}_{i}\right) }{\left( {X - {x}_{i}}\right) {T}_{n}^{\prime }\left( {x}_{i}\right) }.
\]

La forme (*) donne \( {T}_{n}^{\prime }\left( {x}_{i}\right) = n{U}_{n - 1}\left( {x}_{i}\right) = {\left( -1\right) }^{i - 1}n/\sqrt{1 - {x}_{i}^{2}} \) , d’où le résultat.

> The form (*) gives \( {T}_{n}^{\prime }\left( {x}_{i}\right) = n{U}_{n - 1}\left( {x}_{i}\right) = {\left( -1\right) }^{i - 1}n/\sqrt{1 - {x}_{i}^{2}} \) , hence the result.

3 / a) L’hypothèse \( \left| {\sqrt{1 - {x}^{2}}P\left( x\right) }\right| \leq 1 \) entraîne, compte tenu du résultat de la question précédente et du fait que \( {T}_{n}\left( x\right) > 0 \) et \( x - {x}_{i} > 0 \) pour \( {x}_{1} < x \leq 1 \) , l’inégalité

> 3 / a) The hypothesis \( \left| {\sqrt{1 - {x}^{2}}P\left( x\right) }\right| \leq 1 \) implies, given the result of the previous question and the fact that \( {T}_{n}\left( x\right) > 0 \) and \( x - {x}_{i} > 0 \) for \( {x}_{1} < x \leq 1 \) , the inequality

\[
\forall x \in  \left\rbrack  {{x}_{1},1}\right\rbrack  ,\;\left| {P\left( x\right) }\right|  \leq  \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}\left| \frac{{T}_{n}\left( x\right) }{x - {x}_{i}}\right|  = \frac{1}{n}\mathop{\sum }\limits_{{i = 1}}^{n}\frac{{T}_{n}\left( x\right) }{x - {x}_{i}} = \frac{1}{n}{T}_{n}^{\prime }\left( x\right)  = {U}_{n - 1}\left( x\right)  \leq  n.
\]

On montrerait de même l’inégalité \( \left| {P\left( x\right) }\right| \leq n \) lorsque \( x \in \left\lbrack {-1,{x}_{n}\lbrack }\right. \) .

> We would show the inequality \( \left| {P\left( x\right) }\right| \leq n \) in the same way when \( x \in \left\lbrack {-1,{x}_{n}\lbrack }\right. \) .

Si maintenant \( x \in \left\lbrack {{x}_{n},{x}_{1}}\right\rbrack \) , alors

> If now \( x \in \left\lbrack {{x}_{n},{x}_{1}}\right\rbrack \) , then

\[
\sqrt{1 - {x}^{2}} \geq  \sqrt{1 - {x}_{1}^{2}} = \sin \left( \frac{\pi }{2n}\right)  \geq  \frac{2}{\pi } \cdot  \frac{\pi }{2n} = \frac{1}{n}
\]

(l’inégalité sin \( \theta \geq \frac{2}{\pi }\theta \) sur \( \left\lbrack {0,\pi /2}\right\rbrack \) est une conséquence de la concavité du sinus sur \( \left\lbrack {0,\pi /2}\right\rbrack \) ), donc \( \left| {P\left( x\right) }\right| \leq 1/\sqrt{1 - {x}^{2}} \leq n \) , d’où le résultat.

> (the inequality sin \( \theta \geq \frac{2}{\pi }\theta \) on \( \left\lbrack {0,\pi /2}\right\rbrack \) is a consequence of the concavity of the sine function on \( \left\lbrack {0,\pi /2}\right\rbrack \) ), so \( \left| {P\left( x\right) }\right| \leq 1/\sqrt{1 - {x}^{2}} \leq n \) , hence the result.

b) L’expression \( \left( *\right) \) donnant \( {U}_{n} \) s’écrit aussi \( \forall \theta \in \mathbb{R} \smallsetminus \pi \mathbb{Z},{U}_{n - 1}\left( {\cos \theta }\right) = \sin \left( {n\theta }\right) /\sin \left( \theta \right) \) .

> b) The expression \( \left( *\right) \) giving \( {U}_{n} \) can also be written as \( \forall \theta \in \mathbb{R} \smallsetminus \pi \mathbb{Z},{U}_{n - 1}\left( {\cos \theta }\right) = \sin \left( {n\theta }\right) /\sin \left( \theta \right) \) .

Si \( P \) désigne le polynôme \( \mathop{\sum }\limits_{{k = 1}}^{n}{\mu }_{k}{U}_{k - 1} \) , son degré est \( \leq n - 1 \) et on a \( P\left( {\cos \theta }\right) = S\left( \theta \right) /\sin \theta \) pour \( \theta \notin \pi \mathbb{Z} \) . Or \( \parallel S{\parallel }_{\infty } = 1 \) , donc pour tout \( \theta ,\left| {P\left( {\cos \theta }\right) }\right| \cdot \left| {\sin \theta }\right| \leq 1 \) , ce qui entraîne que pour tout \( x \in I,\left| {P\left( x\right) }\right| \sqrt{1 - {x}^{2}} \leq 1 \) . Donc d’après la question précédente, on a \( \parallel P{\parallel }_{\infty } \leq n \) , ce qui entraîne que pour tout \( \theta \notin \pi \mathbb{Z},\left| {S\left( \theta \right) /\sin \theta }\right| \leq n \) .

> If \( P \) denotes the polynomial \( \mathop{\sum }\limits_{{k = 1}}^{n}{\mu }_{k}{U}_{k - 1} \) , its degree is \( \leq n - 1 \) and we have \( P\left( {\cos \theta }\right) = S\left( \theta \right) /\sin \theta \) for \( \theta \notin \pi \mathbb{Z} \) . However \( \parallel S{\parallel }_{\infty } = 1 \) , so for all \( \theta ,\left| {P\left( {\cos \theta }\right) }\right| \cdot \left| {\sin \theta }\right| \leq 1 \) , which implies that for all \( x \in I,\left| {P\left( x\right) }\right| \sqrt{1 - {x}^{2}} \leq 1 \) . Thus, according to the previous question, we have \( \parallel P{\parallel }_{\infty } \leq n \) , which implies that for all \( \theta \notin \pi \mathbb{Z},\left| {S\left( \theta \right) /\sin \theta }\right| \leq n \) .

4 / Fixons \( {\theta }_{0} \in \mathbb{R} \) . Quitte à diviser \( g \) par \( \parallel g{\parallel }_{\infty } \) , on peut supposer \( \parallel g{\parallel }_{\infty } = 1 \) (si \( g = 0 \) , le résultat est évident). Soit \( S \) l’application définie sur \( \mathbb{R} \) par \( S\left( \theta \right) = \frac{1}{2}\left\lbrack {g\left( {{\theta }_{0} + \theta }\right) - g\left( {{\theta }_{0} - \theta }\right) }\right\rbrack \) . Comme \( \frac{1}{2}\left\lbrack {{e}^{{ik}\left( {{\theta }_{0} + \theta }\right) } - {e}^{{ik}\left( {{\theta }_{0} - \theta }\right) }}\right\rbrack = i\left( {\sin {k\theta }}\right) {e}^{{ik}{\theta }_{0}} \) , on voit que \( S \) a la forme de \( 3/\mathrm{b} \) ), et donc si \( \theta \notin \pi \mathbb{Z} \) , \( \left| {S\left( \theta \right) /\sin \theta }\right| \leq n \) . On en déduit

> 4 / Let us fix \( {\theta }_{0} \in \mathbb{R} \) . By dividing \( g \) by \( \parallel g{\parallel }_{\infty } \) if necessary, we can assume \( \parallel g{\parallel }_{\infty } = 1 \) (if \( g = 0 \) , the result is obvious). Let \( S \) be the mapping defined on \( \mathbb{R} \) by \( S\left( \theta \right) = \frac{1}{2}\left\lbrack {g\left( {{\theta }_{0} + \theta }\right) - g\left( {{\theta }_{0} - \theta }\right) }\right\rbrack \) . Since \( \frac{1}{2}\left\lbrack {{e}^{{ik}\left( {{\theta }_{0} + \theta }\right) } - {e}^{{ik}\left( {{\theta }_{0} - \theta }\right) }}\right\rbrack = i\left( {\sin {k\theta }}\right) {e}^{{ik}{\theta }_{0}} \) , we see that \( S \) has the form of \( 3/\mathrm{b} \) ), and therefore if \( \theta \notin \pi \mathbb{Z} \) , \( \left| {S\left( \theta \right) /\sin \theta }\right| \leq n \) . We deduce from this

\[
\left| {{g}^{\prime }\left( {\theta }_{0}\right) }\right|  = \left| {\mathop{\lim }\limits_{\substack{{\theta  \rightarrow  0} \\  {\theta  \neq  0} }}\frac{S\left( \theta \right) }{\theta }}\right|  = \left| {\mathop{\lim }\limits_{\substack{{\theta  \rightarrow  0} \\  {\theta  \neq  0} }}\frac{S\left( \theta \right) }{\sin \theta }}\right|  \leq  n.
\]

Ceci est vrai pour tout \( {\theta }_{0} \in \mathbb{R} \) , d’où le résultat.

> This is true for any \( {\theta }_{0} \in \mathbb{R} \), hence the result.

5 / Là encore, quitte à diviser \( P \) par \( \parallel P{\parallel }_{\infty } \) , on peut supposer \( \parallel P{\parallel }_{\infty } = 1 \) (le cas \( P = 0 \) est évident). Posons \( g\left( \theta \right) = P\left( {\cos \theta }\right) = P\left\lbrack {\left( {{e}^{i\theta } + {e}^{-{i\theta }}}\right) /2}\right\rbrack \) . Cette application a la forme de l’application \( g \) de 4/, et donc on a

> 5 / Here again, by dividing \( P \) by \( \parallel P{\parallel }_{\infty } \) if necessary, we can assume \( \parallel P{\parallel }_{\infty } = 1 \) (the case \( P = 0 \) is obvious). Let \( g\left( \theta \right) = P\left( {\cos \theta }\right) = P\left\lbrack {\left( {{e}^{i\theta } + {e}^{-{i\theta }}}\right) /2}\right\rbrack \) . This map has the form of the map \( g \) from 4/, and thus we have

\[
\forall \theta  \in  \mathbb{R},\;\left| {{g}^{\prime }\left( \theta \right) }\right|  = \left| {\sin \theta }\right|  \cdot  \left| {{P}^{\prime }\left( {\cos \theta }\right) }\right|  \leq  n.
\]

Cette inégalité entraîne que sur \( \left\lbrack {-1,1}\right\rbrack \) , on a \( \sqrt{1 - {x}^{2}}\left| {{P}^{\prime }\left( x\right) }\right| \leq n \) , donc d’après \( 3/a),\left| {{P}^{\prime }\left( x\right) }\right| \leq {n}^{2} \) sur I. D'où le résultat.

> This inequality implies that on \( \left\lbrack {-1,1}\right\rbrack \) , we have \( \sqrt{1 - {x}^{2}}\left| {{P}^{\prime }\left( x\right) }\right| \leq n \) , therefore according to \( 3/a),\left| {{P}^{\prime }\left( x\right) }\right| \leq {n}^{2} \) on I. Hence the result.

Remarque. Les polynômes \( {T}_{n} \) (resp. \( {U}_{n} \) ) s’appellent les polynômes de Tchébycheff de première espèce (resp. de deuxième espèce). Ce sont des polynômes orthogonaux, dont l'étude générale fait l'objet du sujet d'étude 3 page 110.

> Remark. The polynomials \( {T}_{n} \) (resp. \( {U}_{n} \) ) are called Chebyshev polynomials of the first kind (resp. second kind). They are orthogonal polynomials, the general study of which is the subject of study 3 on page 110.

- On retrouve les polynômes de Tchébycheff de première espèce dans l'exercice 13 page 74, ou il est démontré qu’ils vérifient la propriété de mini-max suivante : le minimum de \( \parallel P{\parallel }_{\infty } \) lorsque \( P \) parcourt les polynômes unitaires de degré \( n \) est égal à \( {2}^{1 - n}{\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } = {2}^{1 - n} \) .

> - We encounter Chebyshev polynomials of the first kind in exercise 13 on page 74, where it is proven that they satisfy the following mini-max property: the minimum of \( \parallel P{\parallel }_{\infty } \) as \( P \) ranges over monic polynomials of degree \( n \) is equal to \( {2}^{1 - n}{\begin{Vmatrix}{T}_{n}\end{Vmatrix}}_{\infty } = {2}^{1 - n} \) .

Problem 14. Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( \pi \left( n\right) \) le nombre de nombres premiers \( p \) vé- rifiant \( p \leq n \) . Le but du problème est d’obtenir des minorations intéressantes de \( \pi \left( n\right) \) , en utilisant des intégrales de polynômes à coefficients entiers. Pour tout \( n \in \mathbb{N} \) , on note \( {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \) l’ensemble des polynômes de degré \( \leq n \) à coefficients entiers.

> Problem 14. For any \( n \in {\mathbb{N}}^{ * } \) , let \( \pi \left( n\right) \) denote the number of prime numbers \( p \) satisfying \( p \leq n \) . The goal of the problem is to obtain interesting lower bounds for \( \pi \left( n\right) \) , using integrals of polynomials with integer coefficients. For any \( n \in \mathbb{N} \) , let \( {\mathbb{Z}}_{n}\left\lbrack X\right\rbrack \) denote the set of polynomials of degree \( \leq n \) with integer coefficients.

\( 1/\mathbf{a} \) ) Pour tout \( k \in \mathbb{N} \) , on considère l’ensemble

> \( 1/\mathbf{a} \) ) For any \( k \in \mathbb{N} \) , we consider the set

\[
{E}_{k} = \left\{  {P \in  {\mathbb{Z}}_{k}\left\lbrack  X\right\rbrack   \mid  P\left( {1 - X}\right)  = {\left( -1\right) }^{k}P\left( X\right) }\right\}
\]

et on note \( {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack = \left\{ {P\left( {X\left( {1 - X}\right) }\right) \mid P \in {\mathbb{Z}}_{k}\left\lbrack X\right\rbrack }\right\} \) . Montrer que pour tout \( k \in \mathbb{N} \) , on a \( {E}_{2k} = {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) et \( {E}_{{2k} + 1} = \left( {1 - {2X}}\right) {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) .

> and we denote \( {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack = \left\{ {P\left( {X\left( {1 - X}\right) }\right) \mid P \in {\mathbb{Z}}_{k}\left\lbrack X\right\rbrack }\right\} \) . Show that for any \( k \in \mathbb{N} \) , we have \( {E}_{2k} = {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) and \( {E}_{{2k} + 1} = \left( {1 - {2X}}\right) {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) .

b) Pour tout \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) , on note \( \parallel P{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in \left\lbrack {0,1}\right\rbrack }}\left| {P\left( t\right) }\right| \) . Montrer que pour tout \( k \in \mathbb{N} \) , il existe \( {P}_{k} \in {E}_{k} \) tel que

> b) For any \( P \in \mathbb{R}\left\lbrack X\right\rbrack \), we denote \( \parallel P{\parallel }_{\infty } = \mathop{\sup }\limits_{{t \in \left\lbrack {0,1}\right\rbrack }}\left| {P\left( t\right) }\right| \). Show that for any \( k \in \mathbb{N} \), there exists \( {P}_{k} \in {E}_{k} \) such that

\[
{\begin{Vmatrix}{P}_{k}\end{Vmatrix}}_{\infty } = {m}_{k},\;\text{ où }\;{m}_{k} = \mathop{\inf }\limits_{{P \in  {\mathbb{Z}}_{k}\left\lbrack  X\right\rbrack  , P \neq  0}}\parallel P{\parallel }_{\infty }.
\]

2/a) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {d}_{n} = \operatorname{ppcm}\left( {1,2,\ldots , n}\right) \) . Montrer que \( {d}_{n} \leq {n}^{\pi \left( n\right) } \) .

> 2/a) For any \( n \in {\mathbb{N}}^{ * } \), we denote \( {d}_{n} = \operatorname{ppcm}\left( {1,2,\ldots , n}\right) \). Show that \( {d}_{n} \leq {n}^{\pi \left( n\right) } \).

b) Soit \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) de degré \( n \) tel que \( I\left( P\right) = {\int }_{0}^{1}P\left( t\right) {dt} \neq 0 \) . Montrer que \( \left| {I\left( P\right) }\right| \geq 1/{d}_{n + 1} \) . c) Soit \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) non nul tel que \( \parallel P{\parallel }_{\infty } < 1 \) . Montrer que

> b) Let \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) be of degree \( n \) such that \( I\left( P\right) = {\int }_{0}^{1}P\left( t\right) {dt} \neq 0 \). Show that \( \left| {I\left( P\right) }\right| \geq 1/{d}_{n + 1} \). c) Let \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) be non-zero such that \( \parallel P{\parallel }_{\infty } < 1 \). Show that

\[
\pi \left( n\right)  \geq  C\left( P\right) \frac{n}{\log n} + O\left( \frac{1}{\log n}\right) \;\text{ avec }\;C\left( P\right)  =  - \frac{1}{\deg \left( P\right) }\log \parallel P{\parallel }_{\infty }.
\]

Cette borne inférieure motive la recherche de polynômes \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) maximisant \( C\left( P\right) \) .

> This lower bound motivates the search for polynomials \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) maximizing \( C\left( P\right) \).

3/a) Pour tout \( k \in {\mathbb{N}}^{ * } \) , on note \( {C}_{k} = - \left( {\log {m}_{k}}\right) /k \) . Calculer \( {C}_{2} \) et en déduire une première borne inférieure sur \( \pi \left( n\right) \) .

> 3/a) For any \( k \in {\mathbb{N}}^{ * } \), we denote \( {C}_{k} = - \left( {\log {m}_{k}}\right) /k \). Calculate \( {C}_{2} \) and deduce a first lower bound on \( \pi \left( n\right) \).

b) Calculer \( {C}_{5} \) puis une nouvelle borne inférieure sur \( \pi \left( n\right) \) (on pourra utiliser l’inégalité de Markov \( {\begin{Vmatrix}{P}^{\prime }\end{Vmatrix}}_{\infty } \leq 2{\left( \deg P\right) }^{2}\parallel P{\parallel }_{\infty } \) , conséquence de la question 5/ du problème précédent). il existe \( Q \in \mathbb{Q}\left\lbrack X\right\rbrack \) tel que \( P = \left( {1 - {2X}}\right) Q \) . Lorsque \( \left| x\right| < 1/2 \) , l’égalité

> b) Calculate \( {C}_{5} \) then a new lower bound on \( \pi \left( n\right) \) (one may use Markov's inequality \( {\begin{Vmatrix}{P}^{\prime }\end{Vmatrix}}_{\infty } \leq 2{\left( \deg P\right) }^{2}\parallel P{\parallel }_{\infty } \), a consequence of question 5/ of the previous problem). there exists \( Q \in \mathbb{Q}\left\lbrack X\right\rbrack \) such that \( P = \left( {1 - {2X}}\right) Q \). When \( \left| x\right| < 1/2 \), the equality

\[
Q\left( x\right)  = \frac{P\left( x\right) }{1 - {2x}} = P\left( x\right) \left( {1 + {2x} + 4{x}^{2} + \cdots }\right)
\]

---

Solution. 1/a) Montrons d’abord le résultat pour \( {E}_{2k} \) . L’inclusion \( {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \subset {E}_{2k} \) est immédiate. Pour montrer l’inclusion réciproque, on procède par récurrence sur \( k \) . Pour \( k = 0 \) c’est immédiat. Supposons le résultat vrai au rang \( k - 1 \) et montrons le au rang \( k \in {\mathbb{N}}^{ * } \) . Soit \( P \in {E}_{2k} \) . Le polynôme \( P\left( X\right) - P\left( 0\right) \) s’annule en \( X = 0 \) ainsi qu’en \( X = 1 \) par symétrie. On peut donc écrire \( P\left( X\right) - P\left( 0\right) = X\left( {1 - X}\right) Q\left( X\right) \) où \( Q \in \mathbb{Q}\left\lbrack X\right\rbrack \) . La division euclidienne d’un polynôme à coefficients entiers par un polynôme dont le terme dominant vaut \( \pm 1 \) est à coefficients entiers, donc \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) (voir la remarque 3 page 58). De plus \( Q \in {E}_{{2k} - 2} \) , et il suffit d’appliquer l’hypothèse de récurrence à \( Q \) pour montrer que \( P = P\left( 0\right) + X\left( {1 - X}\right) Q \in {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) .

> Solution. 1/a) Let us first show the result for \( {E}_{2k} \). The inclusion \( {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \subset {E}_{2k} \) is immediate. To show the reverse inclusion, we proceed by induction on \( k \). For \( k = 0 \), it is immediate. Assume the result is true at rank \( k - 1 \) and show it at rank \( k \in {\mathbb{N}}^{ * } \). Let \( P \in {E}_{2k} \). The polynomial \( P\left( X\right) - P\left( 0\right) \) vanishes at \( X = 0 \) as well as at \( X = 1 \) by symmetry. We can therefore write \( P\left( X\right) - P\left( 0\right) = X\left( {1 - X}\right) Q\left( X\right) \) where \( Q \in \mathbb{Q}\left\lbrack X\right\rbrack \). The Euclidean division of a polynomial with integer coefficients by a polynomial whose leading term is \( \pm 1 \) results in integer coefficients, so \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) (see remark 3 on page 58). Furthermore \( Q \in {E}_{{2k} - 2} \), and it suffices to apply the induction hypothesis to \( Q \) to show that \( P = P\left( 0\right) + X\left( {1 - X}\right) Q \in {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \).

Il s’agit maintenant de montrer \( {E}_{{2k} + 1} \subset \left( {1 - {2X}}\right) {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) . Soit \( P \in {E}_{{2k} + 1} \) . On a \( P\left( {1/2}\right) = {\left( -1\right) }^{{2k} + 1}P\left( {1/2}\right) = - P\left( {1/2}\right) \) donc \( P\left( {1/2}\right) = 0 \) . Ainsi, \( P \) est divisible par \( \left( {1 - {2X}}\right) \) donc

> It is now a matter of showing \( {E}_{{2k} + 1} \subset \left( {1 - {2X}}\right) {\mathbb{Z}}_{k}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \). Let \( P \in {E}_{{2k} + 1} \). We have \( P\left( {1/2}\right) = {\left( -1\right) }^{{2k} + 1}P\left( {1/2}\right) = - P\left( {1/2}\right) \) so \( P\left( {1/2}\right) = 0 \). Thus, \( P \) is divisible by \( \left( {1 - {2X}}\right) \) therefore

---

montre que les coefficients de \( Q\left( x\right) \) (vu comme une série entière) sont entiers, donc \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) . On conclut en remarquant que \( Q \in {E}_{2k} \) .

> shows that the coefficients of \( Q\left( x\right) \) (viewed as a power series) are integers, so \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \). We conclude by noting that \( Q \in {E}_{2k} \).

b) On montre d’abord l’existence de \( {Q}_{k} \in {\mathbb{Z}}_{k}\left\lbrack X\right\rbrack \) tel que \( {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } = {m}_{k} \) . On remarque que l’ensemble \( \Gamma = \left\{ {P \in {\mathbb{Z}}_{k}\left\lbrack X\right\rbrack \smallsetminus \{ 0\} \mid \parallel P\parallel \leq 1 + {m}_{k}}\right\} \) est fini (les normes dans le s.e.v de dimension finie \( {\mathbb{R}}_{k}\left\lbrack X\right\rbrack \) sont équivalentes, donc si \( P = \mathop{\sum }\limits_{{\ell = 0}}^{k}{a}_{\ell }{X}^{\ell } \in \Gamma \) il existe \( A > 0 \) tel que \( \mathop{\sum }\limits_{{\ell = 0}}^{k}\left| {a}_{\ell }\right| \leq \; A\parallel P{\parallel }_{\infty } \leq B = A\left( {1 + {m}_{k}}\right) ) \) . Donc il existe \( {Q}_{k} \in \Gamma \) tel que \( {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } = \mathop{\inf }\limits_{{P \in \Gamma }}\parallel P{\parallel }_{\infty } \) , et comme \( \mathop{\inf }\limits_{{P \in \Gamma }}\parallel P{\parallel }_{\infty } = {m}_{k} \) par définition de \( \Gamma \) , on a bien le résultat voulu.

> b) We first show the existence of \( {Q}_{k} \in {\mathbb{Z}}_{k}\left\lbrack X\right\rbrack \) such that \( {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } = {m}_{k} \) . We note that the set \( \Gamma = \left\{ {P \in {\mathbb{Z}}_{k}\left\lbrack X\right\rbrack \smallsetminus \{ 0\} \mid \parallel P\parallel \leq 1 + {m}_{k}}\right\} \) is finite (norms in the finite-dimensional subspace \( {\mathbb{R}}_{k}\left\lbrack X\right\rbrack \) are equivalent, so if \( P = \mathop{\sum }\limits_{{\ell = 0}}^{k}{a}_{\ell }{X}^{\ell } \in \Gamma \) there exists \( A > 0 \) such that \( \mathop{\sum }\limits_{{\ell = 0}}^{k}\left| {a}_{\ell }\right| \leq \; A\parallel P{\parallel }_{\infty } \leq B = A\left( {1 + {m}_{k}}\right) ) \) . Thus there exists \( {Q}_{k} \in \Gamma \) such that \( {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } = \mathop{\inf }\limits_{{P \in \Gamma }}\parallel P{\parallel }_{\infty } \) , and since \( \mathop{\inf }\limits_{{P \in \Gamma }}\parallel P{\parallel }_{\infty } = {m}_{k} \) by definition of \( \Gamma \) , we have the desired result.)

On considère maintenant les deux polynômes

> We now consider the two polynomials

\[
{R}_{1}\left( X\right)  = X{Q}_{k}\left( X\right)  + {\left( -1\right) }^{k}\left( {1 - X}\right) {Q}_{k}\left( {1 - X}\right) ,\;{R}_{2}\left( X\right)  = \left( {1 - X}\right) {Q}_{k}\left( X\right)  + {\left( -1\right) }^{k}X{Q}_{k}\left( {1 - X}\right) .
\]

Ces polynômes sont de degré \( \leq k \) (le terme éventuel de degré \( k + 1 \) s’annule) et on a \( {R}_{i}\left( X\right) = \; {\left( -1\right) }^{k}{R}_{i}\left( {1 - X}\right) \) donc \( {R}_{i} \in {E}_{k} \) . Lorsque \( t \in \left\lbrack {0,1}\right\rbrack \) on a \( \left| {{R}_{i}\left( t\right) }\right| \leq t{\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } + \left( {1 - t}\right) {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } = {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } \) , donc \( {\begin{Vmatrix}{R}_{i}\end{Vmatrix}}_{\infty } \leq {m}_{k} \) . Le déterminant \( \left| \begin{matrix} X & {\left( -1\right) }^{k}\left( {1 - X}\right) \\ \left( {1 - X}\right) & {\left( -1\right) }^{k}X \end{matrix}\right| = {\left( -1\right) }^{k}\left( {{2X} - 1}\right) \) est non nul, donc \( {Q}_{k}\left( X\right) \) et \( {Q}_{k}\left( {1 - X}\right) \) s’expriment linéairement en fonction de \( {R}_{1} \) et \( {R}_{2} \) donc l’un des deux polynômes \( {R}_{1},{R}_{2} \) est non nul. Il suffit alors de choisir \( {P}_{k} \) comme l’un non nul de ces deux polynômes.

> These polynomials are of degree \( \leq k \) (the potential term of degree \( k + 1 \) cancels out) and we have \( {R}_{i}\left( X\right) = \; {\left( -1\right) }^{k}{R}_{i}\left( {1 - X}\right) \) so \( {R}_{i} \in {E}_{k} \) . When \( t \in \left\lbrack {0,1}\right\rbrack \) we have \( \left| {{R}_{i}\left( t\right) }\right| \leq t{\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } + \left( {1 - t}\right) {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } = {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}_{\infty } \) , so \( {\begin{Vmatrix}{R}_{i}\end{Vmatrix}}_{\infty } \leq {m}_{k} \) . The determinant \( \left| \begin{matrix} X & {\left( -1\right) }^{k}\left( {1 - X}\right) \\ \left( {1 - X}\right) & {\left( -1\right) }^{k}X \end{matrix}\right| = {\left( -1\right) }^{k}\left( {{2X} - 1}\right) \) is non-zero, so \( {Q}_{k}\left( X\right) \) and \( {Q}_{k}\left( {1 - X}\right) \) are expressed linearly in terms of \( {R}_{1} \) and \( {R}_{2} \) , therefore one of the two polynomials \( {R}_{1},{R}_{2} \) is non-zero. It then suffices to choose \( {P}_{k} \) as one of these two non-zero polynomials.

2/a) Notons \( k = \pi \left( n\right) \) et \( {p}_{1},\ldots ,{p}_{k} \) les nombres premiers \( \leq n \) . On a \( {d}_{n} = \mathop{\prod }\limits_{{i = 1}}^{k}{p}_{i}^{{\alpha }_{i}} \) où pour tout \( i,{\alpha }_{i} \) est la plus grande puissance de \( {p}_{i} \) dans la décomposition en facteurs premiers des \( n \) premiers entiers. Ainsi, \( {p}_{i}^{{\alpha }_{i}} \leq n \) , donc \( {d}_{n} \leq {n}^{k} = {n}^{\pi \left( n\right) } \) .

> 2/a) Let \( k = \pi \left( n\right) \) and \( {p}_{1},\ldots ,{p}_{k} \) be the prime numbers \( \leq n \) . We have \( {d}_{n} = \mathop{\prod }\limits_{{i = 1}}^{k}{p}_{i}^{{\alpha }_{i}} \) where for all \( i,{\alpha }_{i} \) is the largest power of \( {p}_{i} \) in the prime factorization of the first \( n \) integers. Thus, \( {p}_{i}^{{\alpha }_{i}} \leq n \) , so \( {d}_{n} \leq {n}^{k} = {n}^{\pi \left( n\right) } \) .

b) En écrivant \( P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \) , on a \( I\left( P\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}/\left( {k + 1}\right) \) donc en réduisant au même dénominateur, on voit que \( I\left( P\right) = m/{d}_{n + 1} \) avec \( m \in \mathbb{Z} \) . Comme \( m \in {\mathbb{Z}}^{ * } \) , on en déduit le résultat.

> b) By writing \( P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \) , we have \( I\left( P\right) = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}/\left( {k + 1}\right) \) so by reducing to a common denominator, we see that \( I\left( P\right) = m/{d}_{n + 1} \) with \( m \in \mathbb{Z} \) . Since \( m \in {\mathbb{Z}}^{ * } \) , we deduce the result.

c) Notons \( k = \deg \left( P\right) \) . Pour tout \( \alpha \in {\mathbb{N}}^{ * } \) , le polynôme \( {P}^{2\alpha } \in \mathbb{Z}\left\lbrack X\right\rbrack \) est positif non nul et de degré \( {2k\alpha } \) , donc \( I\left( {P}^{2\alpha }\right) \geq 1/{d}_{{2k\alpha } + 1} \) . Par ailleurs \( I\left( {P}^{2\alpha }\right) \leq \parallel P{\parallel }_{\infty }^{2\alpha } \) ce qui entraîne

> c) Let \( k = \deg \left( P\right) \) . For all \( \alpha \in {\mathbb{N}}^{ * } \) , the polynomial \( {P}^{2\alpha } \in \mathbb{Z}\left\lbrack X\right\rbrack \) is positive non-zero and of degree \( {2k\alpha } \) , so \( I\left( {P}^{2\alpha }\right) \geq 1/{d}_{{2k\alpha } + 1} \) . Furthermore \( I\left( {P}^{2\alpha }\right) \leq \parallel P{\parallel }_{\infty }^{2\alpha } \) which implies

\[
{\left( 2k\alpha  + 1\right) }^{\pi \left( {{2k\alpha } + 1}\right) } \geq  {d}_{{2k\alpha } + 1} \geq  \frac{1}{I\left( {P}^{2\alpha }\right) } \geq  \frac{1}{\parallel P{\parallel }_{\infty }^{2\alpha }}\text{ donc }\pi \left( {{2k\alpha } + 1}\right)  \geq  \frac{2k\alpha }{\log \left( {{2k\alpha } + 1}\right) }C\left( P\right) .
\]

On en déduit facilement le résultat demandé.

> We easily deduce the requested result.

3/a) D’après \( 1/\mathrm{b}) \) , il existe \( P \in {\mathbb{Z}}_{1}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) tel que \( \parallel P{\parallel }_{\infty } = {m}_{2} \) . Le polynôme \( P \) a la forme \( P = a + {bX}\left( {1 - X}\right) \) avec \( a, b \in \mathbb{Z} \) . Comme \( {m}_{2} \leq \parallel X\left( {1 - X}\right) {\parallel }_{\infty } = 1/4 \) , on doit avoir \( \left| a\right| = \left| {P\left( 0\right) }\right| \leq {m}_{2} \leq 1/4 \) donc \( a = 0 \) . On en conclut que \( P = {bX}\left( {1 - X}\right) \) et forcément, \( b = \pm 1 \) . Ainsi, \( {m}_{2} = 1/4 \) donc \( {C}_{2} = \log 2 \) . On en conclut grâce à la question précédente que \( \pi \left( n\right) \geq \left( {\log 2}\right) n/\log n + O\left( {1/\log n}\right) . \)

> 3/a) According to \( 1/\mathrm{b}) \) , there exists \( P \in {\mathbb{Z}}_{1}\left\lbrack {X\left( {1 - X}\right) }\right\rbrack \) such that \( \parallel P{\parallel }_{\infty } = {m}_{2} \) . The polynomial \( P \) has the form \( P = a + {bX}\left( {1 - X}\right) \) with \( a, b \in \mathbb{Z} \) . Since \( {m}_{2} \leq \parallel X\left( {1 - X}\right) {\parallel }_{\infty } = 1/4 \) , we must have \( \left| a\right| = \left| {P\left( 0\right) }\right| \leq {m}_{2} \leq 1/4 \) so \( a = 0 \) . We conclude that \( P = {bX}\left( {1 - X}\right) \) and necessarily, \( b = \pm 1 \) . Thus, \( {m}_{2} = 1/4 \) so \( {C}_{2} = \log 2 \) . We conclude thanks to the previous question that \( \pi \left( n\right) \geq \left( {\log 2}\right) n/\log n + O\left( {1/\log n}\right) . \)

b) La question \( 1/ \) b) assure qu’il existe \( P \) de la forme \( P = \left( {1 - {2X}}\right) \left\lbrack {a + {bX}\left( {1 - X}\right) + c{X}^{2}{\left( 1 - X\right) }^{2}}\right\rbrack \) avec \( a, b, c \in \mathbb{Z} \) tel que \( \parallel P{\parallel }_{\infty } = {m}_{5} \) . Comme \( {m}_{5} \leq {m}_{2} < 1 \) , on a forcément \( a = P\left( 0\right) = 0 \) . Un calcul facile montre que \( Q = \left( {1 - {2X}}\right) {X}^{2}{\left( 1 - X\right) }^{2} \) vêrifie \( \parallel Q{\parallel }_{\infty } = {5}^{-5/2} \) . D’après l’inégalité de Markov on a donc

> b) Question \( 1/ \) b) ensures that there exists \( P \) of the form \( P = \left( {1 - {2X}}\right) \left\lbrack {a + {bX}\left( {1 - X}\right) + c{X}^{2}{\left( 1 - X\right) }^{2}}\right\rbrack \) with \( a, b, c \in \mathbb{Z} \) such that \( \parallel P{\parallel }_{\infty } = {m}_{5} \) . Since \( {m}_{5} \leq {m}_{2} < 1 \) , we necessarily have \( a = P\left( 0\right) = 0 \) . An easy calculation shows that \( Q = \left( {1 - {2X}}\right) {X}^{2}{\left( 1 - X\right) }^{2} \) satisfies \( \parallel Q{\parallel }_{\infty } = {5}^{-5/2} \) . According to Markov's inequality, we therefore have

\[
\left| b\right|  = \left| {{P}^{\prime }\left( 0\right) }\right|  \leq  {\begin{Vmatrix}{P}^{\prime }\end{Vmatrix}}_{\infty } \leq  2 \cdot  {5}^{2}\parallel P{\parallel }_{\infty } \leq  2 \cdot  {5}^{2}\frac{1}{{5}^{5/2}} = \frac{2}{\sqrt{5}} < 1
\]

donc \( b = 0 \) . Ainsi, \( P \) est de la forme \( P = c\left( {1 - {2X}}\right) {X}^{2}{\left( 1 - X\right) }^{2} \) , et on a forcément \( c = \pm 1 \) donc \( P = \pm Q \) . Donc \( {m}_{5} = \parallel Q{\parallel }_{\infty } = {5}^{-5/2} \) , d’où \( {C}_{5} = \log \left( 5\right) /2 \) . Ceci donne la minoration \( \pi \left( n\right) \geq \frac{\log \left( 5\right) }{2}n/\log n + O\left( {1/\log n}\right) \) pour \( n \) suffisamment grand.

> thus \( b = 0 \) . Thus, \( P \) is of the form \( P = c\left( {1 - {2X}}\right) {X}^{2}{\left( 1 - X\right) }^{2} \) , and we necessarily have \( c = \pm 1 \) so \( P = \pm Q \) . Therefore \( {m}_{5} = \parallel Q{\parallel }_{\infty } = {5}^{-5/2} \) , whence \( {C}_{5} = \log \left( 5\right) /2 \) . This gives the lower bound \( \pi \left( n\right) \geq \frac{\log \left( 5\right) }{2}n/\log n + O\left( {1/\log n}\right) \) for sufficiently large \( n \) .

Remarque. Nous avons montré \( \pi \left( n\right) \geq {C}_{k}n/\log n + O\left( {1/\log n}\right) \) dans \( 3/a) \) et \( 3/b) \) , avec \( {C}_{2} \simeq 0,{6931} \) et \( {C}_{5} \simeq 0,{8047} \) . Le théorème des nombres premiers (dont une démonstration est proposée en annexe du tome d'analyse - à partir de la deuxième édition) assure que \( \pi \left( n\right) \sim n/\log n \) . Cependant on ne peut pas, en utilisant la technique du problème, obtenir des minorations du type \( \pi \left( n\right) \geq {Cn}/\log \left( n\right) + O\left( {1/\log n}\right) \) avec \( C \) arbitrairement proche de 1 (en effet, on peut montrer que \( {C}_{k} \leq 0,{866} \) pour tout \( k \) ).

> Remark. We have shown \( \pi \left( n\right) \geq {C}_{k}n/\log n + O\left( {1/\log n}\right) \) in \( 3/a) \) and \( 3/b) \) , with \( {C}_{2} \simeq 0,{6931} \) and \( {C}_{5} \simeq 0,{8047} \) . The prime number theorem (a proof of which is provided in the appendix of the analysis volume - starting from the second edition) ensures that \( \pi \left( n\right) \sim n/\log n \) . However, one cannot, using the technique of the problem, obtain lower bounds of the type \( \pi \left( n\right) \geq {Cn}/\log \left( n\right) + O\left( {1/\log n}\right) \) with \( C \) arbitrarily close to 1 (indeed, one can show that \( {C}_{k} \leq 0,{866} \) for any \( k \) ).

- Ce type de minoration de \( \pi \left( n\right) \) est à rapprocher du théorème de Tchébycheff (voir le sujet d'étude 1 page 47). En effet, les questions 1/ et 5/ de ce sujet d'étude entraînent facilement la minoration \( \pi \left( {2n}\right)  \geq  \left( {\log 2 + o\left( 1\right) }\right) \frac{2n}{\log {2n}} \) .

> - This type of lower bound for \( \pi \left( n\right) \) is to be compared with Chebyshev's theorem (see study topic 1 page 47). Indeed, questions 1/ and 5/ of this study topic easily lead to the lower bound \( \pi \left( {2n}\right)  \geq  \left( {\log 2 + o\left( 1\right) }\right) \frac{2n}{\log {2n}} \) .
