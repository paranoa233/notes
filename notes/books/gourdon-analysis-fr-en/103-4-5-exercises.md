#### 4.5. Exercises

*Français : 4.5. Exercices*

EXERCICE 1. a) Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence \( R > 0 \) telle que \( {a}_{n} > 0 \) pour tout \( n \) . Discuter en fonction du paramètre \( \alpha \in \mathbb{R} \) le rayon de convergence \( {R}^{\prime } \) de la série entière \( \sum {a}_{n}^{\alpha }{z}^{n} \) .

> EXERCISE 1. a) Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence \( R > 0 \) such that \( {a}_{n} > 0 \) for all \( n \). Discuss, depending on the parameter \( \alpha \in \mathbb{R} \), the radius of convergence \( {R}^{\prime } \) of the power series \( \sum {a}_{n}^{\alpha }{z}^{n} \).

b) Soient \( \sum {a}_{n}{z}^{n} \) et \( \sum {b}_{n}{z}^{n} \) deux séries entières de rayon de convergence respectifs \( R \) et \( {R}^{\prime } \) . Que dire du rayon de convergence \( {R}^{\prime \prime } \) de la série entière \( \sum {a}_{n}{b}_{n}{z}^{n} \) ? (Cette dernière série entière est appelée produit de Hadamard de \( \sum {a}_{n}{z}^{n} \) et \( \sum {b}_{n}{z}^{n} \) .)

> b) Let \( \sum {a}_{n}{z}^{n} \) and \( \sum {b}_{n}{z}^{n} \) be two power series with respective radii of convergence \( R \) and \( {R}^{\prime } \). What can be said about the radius of convergence \( {R}^{\prime \prime } \) of the power series \( \sum {a}_{n}{b}_{n}{z}^{n} \)? (This latter power series is called the Hadamard product of \( \sum {a}_{n}{z}^{n} \) and \( \sum {b}_{n}{z}^{n} \).)

Solution. a) Les rayons de convergence \( R \) et \( {R}^{\prime } \) vérifient \( R = \sup \Gamma ,{R}^{\prime } = \sup {\Gamma }^{\prime } \) , où

> Solution. a) The radii of convergence \( R \) and \( {R}^{\prime } \) satisfy \( R = \sup \Gamma ,{R}^{\prime } = \sup {\Gamma }^{\prime } \), where

\[
\Gamma  = \left\{  {r \geq  0 \mid  \text{ la suite }\left( {{a}_{n}{r}^{n}}\right) }\right. \text{ est bornée }\} \text{ et }{\Gamma }^{\prime } = \left\{  {r \geq  0 \mid  \left( {{a}_{n}^{\alpha }{r}^{n}}\right) \text{ est bornée }}\right\}  .
\]

Maintenant, nous traitons plusieurs cas selon la position de \( \alpha \) par rapport à 0 .

> Now, we address several cases depending on the position of \( \alpha \) relative to 0.

- Supposons \( \alpha  > 0 \) . L’égalité \( {a}_{n}^{\alpha }{r}^{n} = {\left( {a}_{n}{r}^{n/\alpha }\right) }^{\alpha } \) montre que la suite \( \left( {{a}_{n}^{\alpha }{r}^{n}}\right) \) est bornée si et seulement si \( \left( {{a}_{n}{r}^{n/\alpha }}\right) \) est bornée. Ainsi, \( r \in  {\Gamma }^{\prime } \) si et seulement si \( {r}^{1/\alpha } \in  \Gamma \) . On en déduit \( {R}^{\prime } = {R}^{1/\alpha } \) (avec par convention \( {\left( +\infty \right) }^{1/\alpha } =  + \infty \) ).

> - Suppose \( \alpha  > 0 \) . The equality \( {a}_{n}^{\alpha }{r}^{n} = {\left( {a}_{n}{r}^{n/\alpha }\right) }^{\alpha } \) shows that the sequence \( \left( {{a}_{n}^{\alpha }{r}^{n}}\right) \) is bounded if and only if \( \left( {{a}_{n}{r}^{n/\alpha }}\right) \) is bounded. Thus, \( r \in  {\Gamma }^{\prime } \) if and only if \( {r}^{1/\alpha } \in  \Gamma \) . We deduce \( {R}^{\prime } = {R}^{1/\alpha } \) (with the convention \( {\left( +\infty \right) }^{1/\alpha } =  + \infty \) ).

- Si \( \alpha  = 0,{a}_{n}^{\alpha } = 1 \) pour tout \( n \) donc \( {R}^{\prime } = 1 \) .

> - If \( \alpha  = 0,{a}_{n}^{\alpha } = 1 \) for all \( n \) then \( {R}^{\prime } = 1 \) .

- Supposons \( \alpha  < 0 \) . Si \( r \in  \rbrack 0, R\lbrack \) , la suite \( \left( {{a}_{n}{r}^{n}}\right) \) tend vers 0, donc la suite \( \left( {{a}_{n}^{\alpha }{r}^{n\alpha }}\right) \) tend vers \( + \infty \) , donc \( {r}^{\alpha } \notin  {\Gamma }^{\prime } \) . Ceci étant vrai pour tout \( r \in  \rbrack 0, R\lbrack \) , on en déduit que \( \rbrack {R}^{\alpha }, + \infty \left\lbrack  {\cap {\Gamma }^{\prime } = \varnothing }\right. \) , donc \( {R}^{\prime } \leq  {R}^{\alpha } \) . On ne peut rien dire de plus en général. Par exemple, si \( {a}_{2n} = {2}^{2n} \) et \( {a}_{{2n} + 1} = {2}^{-{2n}} \) pour tout \( n \) , on a \( R = 1/2 \) et \( {R}^{\prime } = {2}^{\alpha } < {R}^{\alpha } \) .

> - Suppose \( \alpha  < 0 \) . If \( r \in  \rbrack 0, R\lbrack \) , the sequence \( \left( {{a}_{n}{r}^{n}}\right) \) tends to 0, so the sequence \( \left( {{a}_{n}^{\alpha }{r}^{n\alpha }}\right) \) tends to \( + \infty \) , therefore \( {r}^{\alpha } \notin  {\Gamma }^{\prime } \) . Since this is true for all \( r \in  \rbrack 0, R\lbrack \) , we deduce that \( \rbrack {R}^{\alpha }, + \infty \left\lbrack  {\cap {\Gamma }^{\prime } = \varnothing }\right. \) , therefore \( {R}^{\prime } \leq  {R}^{\alpha } \) . Nothing more can be said in general. For example, if \( {a}_{2n} = {2}^{2n} \) and \( {a}_{{2n} + 1} = {2}^{-{2n}} \) for all \( n \) , we have \( R = 1/2 \) and \( {R}^{\prime } = {2}^{\alpha } < {R}^{\alpha } \) .

b) Pour tout \( \left( {r,{r}^{\prime }}\right) \in \left\lbrack {0, R\left\lbrack {\times \left\lbrack {0,{R}^{\prime }\left\lbrack \right. }\right. }\right. }\right. \) , les suites \( \left( {{a}_{n}{r}^{n}}\right) \) et \( \left( {{b}_{n}{r}^{\prime n}}\right) \) sont bornées, donc \( \left( {{a}_{n}{b}_{n}{\left( r{r}^{\prime }\right) }^{n}}\right) \) est bornée. On voit donc que pour tout \( {r}^{\prime \prime } \in \left\lbrack {0, R{R}^{\prime }\left\lbrack \right. }\right. \) , la suite \( \left( {{a}_{n}{b}_{n}{r}^{\prime \prime n}}\right) \) est bornée. Ceci entraîne \( {R}^{\prime \prime } \geq R{R}^{\prime } \) .

> b) For all \( \left( {r,{r}^{\prime }}\right) \in \left\lbrack {0, R\left\lbrack {\times \left\lbrack {0,{R}^{\prime }\left\lbrack \right. }\right. }\right. }\right. \) , the sequences \( \left( {{a}_{n}{r}^{n}}\right) \) and \( \left( {{b}_{n}{r}^{\prime n}}\right) \) are bounded, so \( \left( {{a}_{n}{b}_{n}{\left( r{r}^{\prime }\right) }^{n}}\right) \) is bounded. We thus see that for all \( {r}^{\prime \prime } \in \left\lbrack {0, R{R}^{\prime }\left\lbrack \right. }\right. \) , the sequence \( \left( {{a}_{n}{b}_{n}{r}^{\prime \prime n}}\right) \) is bounded. This implies \( {R}^{\prime \prime } \geq R{R}^{\prime } \) .

On ne peut rien dire de plus en général. Par exemple, les séries entières \( \sum {z}^{2n} \) et \( \sum {z}^{{2n} + 1} \) sont de rayon de convergence 1, et leur produit de Hadamard est nul donc son rayon de convergence est infini.

> Nothing more can be said in general. For example, the power series \( \sum {z}^{2n} \) and \( \sum {z}^{{2n} + 1} \) have a radius of convergence of 1, and their Hadamard product is zero, so its radius of convergence is infinite.

EXERCICE 2. Après avoir donné leur rayon de convergence \( R \) , sommer les séries entières suivantes :

> EXERCISE 2. After providing their radius of convergence \( R \) , sum the following power series:

\[
\text{ a) }\mathop{\sum }\limits_{{n \in  \mathbb{N}}}{n}^{2}{x}^{n}
\]

b) \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\frac{{x}^{n}}{{2n} + 1}\;\left( {\text{ pour }x > 0}\right) \)

\[
\text{ c) }\mathop{\sum }\limits_{{n \in  {\mathbb{N}}^{ * }}}\frac{{x}^{n}}{n\left( {n + 2}\right) }\text{ pour }x \in  \mathbb{R}
\]

d) \( \mathop{\sum }\limits_{{n \in \mathbb{N}}}\frac{{x}^{n}}{n!}\cos \left( {n\theta }\right) \) .

> Solution. a) En utilisant la règle de d'Alembert, on voit que le rayon de convergence est \( R = 1 \) . Pour sommer la série entière, on part de l'égalité

Solution. a) Using the d'Alembert ratio test, we see that the radius of convergence is \( R = 1 \) . To sum the power series, we start from the equality

\[
\forall x \in  \mathbb{R},\left| x\right|  < 1,\;f\left( x\right)  = \frac{1}{1 - x} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n},
\]

d’où on déduit par dérivation que si \( x \in \mathbb{R},\left| x\right| < 1 \) ,

> from which we deduce by differentiation that if \( x \in \mathbb{R},\left| x\right| < 1 \) ,

\[
x{f}^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}n{x}^{n}\;\text{ et }\;{x}^{2}{f}^{\prime \prime }\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}n\left( {n - 1}\right) {x}^{n}.
\]

Finalement, pour tout \( x \in \mathbb{R},\left| x\right| < 1 \) ,

> Finally, for all \( x \in \mathbb{R},\left| x\right| < 1 \) ,

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{n}^{2}{x}^{n} = {x}^{2}{f}^{\prime \prime }\left( x\right)  + x{f}^{\prime }\left( x\right)  = \frac{2{x}^{2}}{{\left( 1 - x\right) }^{3}} + \frac{x}{{\left( 1 - x\right) }^{2}} = \frac{{x}^{2} + x}{{\left( 1 - x\right) }^{3}}.
\]

Cette formule reste valable pour tout \( x \in \mathbb{C},\left| x\right| < 1 \) car on sait qu’une fraction rationnelle est développable en série entière pour la variable complexe, et les coefficients sont déterminés si l'on connaît la somme de la série sur un voisinage de 0 dans \( \mathbb{R} \) .

> This formula remains valid for all \( x \in \mathbb{C},\left| x\right| < 1 \) because we know that a rational fraction can be expanded into a power series for the complex variable, and the coefficients are determined if the sum of the series is known on a neighborhood of 0 in \( \mathbb{R} \) .

b) Toujours grâce à la règle de d’Alembert, on trouve \( R = 1 \) . On note \( f \) la somme de la série entière proposée. On a

> b) Still using d’Alembert’s rule, we find \( R = 1 \) . Let \( f \) be the sum of the proposed power series. We have

\[
\forall x \in  \lbrack 0,1\lbrack ,\;g\left( x\right)  = {xf}\left( {x}^{2}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{{2n} + 1}}{{2n} + 1}\;\text{ et }\;{g}^{\prime }\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{2n} = \frac{1}{1 - {x}^{2}},
\]

donc par intégration

> therefore by integration

\[
\forall x \in  \lbrack 0,1\lbrack ,\;g\left( x\right)  = \frac{1}{2}\log \left( \frac{1 + x}{1 - x}\right) \text{ d’où }f\left( x\right)  = \frac{g\left( \sqrt{x}\right) }{\sqrt{x}} = \frac{1}{2\sqrt{x}}\log \left( \frac{1 + \sqrt{x}}{1 - \sqrt{x}}\right) .
\]

c) Ici \( R = 1 \) (règle de d’Alembert). Une décomposition en éléments simples fournit

> c) Here \( R = 1 \) (d’Alembert’s rule). A partial fraction decomposition provides

\[
\forall n \in  \mathbb{N},\;\frac{1}{n\left( {n + 2}\right) } = \frac{1}{2}\left( {\frac{1}{n} - \frac{1}{n + 2}}\right)
\]

donc en notant \( f\left( x\right) \) la somme de la série entière proposée sur \( \rbrack - 1,1\lbrack \) ,

> therefore, by denoting \( f\left( x\right) \) as the sum of the proposed power series on \( \rbrack - 1,1\lbrack \) ,

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {, x \neq  0,\;f\left( x\right)  = \frac{1}{2}\left( {\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{x}^{n}}{n} - \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{x}^{n}}{n + 2}}\right)  =  - \frac{\log \left( {1 - x}\right) }{2} - \frac{1}{2{x}^{2}}\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{{x}^{n + 2}}{n + 2}}\right.
\]

\[
=  - \frac{\log \left( {1 - x}\right) }{2} - \frac{1}{2{x}^{2}}\left( {-\log \left( {1 - x}\right)  - x - \frac{{x}^{2}}{2}}\right)  =  - \frac{\log \left( {1 - x}\right) }{2} + \frac{\log \left( {1 - x}\right) }{2{x}^{2}} + \frac{1}{2x} + \frac{1}{4}.
\]

d) Comme \( \left| {\cos \left( {n\theta }\right) /n!}\right| \leq 1/n \) !, on a \( R = + \infty \) . Par ailleurs, on a \( \cos {n\theta } = \left( {{e}^{ni\theta } + {e}^{-{ni\theta }}}\right) /2 \) pour tout \( n \) , donc

> d) Since \( \left| {\cos \left( {n\theta }\right) /n!}\right| \leq 1/n \) !, we have \( R = + \infty \) . Furthermore, we have \( \cos {n\theta } = \left( {{e}^{ni\theta } + {e}^{-{ni\theta }}}\right) /2 \) for all \( n \) , therefore

\[
\forall x \in  \mathbb{C},\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{n}}{n!}\cos {n\theta } = \frac{1}{2}\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( x{e}^{i\theta }\right) }^{n}}{n!} + \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( x{e}^{-{i\theta }}\right) }^{n}}{n!}}\right)  = \frac{\exp \left( {x{e}^{i\theta }}\right)  + \exp \left( {x{e}^{-{i\theta }}}\right) }{2}.
\]

EXERCICE 3. a) Développer en série entière la fonction \( f : \rbrack - 1,1\lbrack \rightarrow \mathbb{R}\;x \mapsto {\left( \arcsin x\right) }^{2} \) . b) Montrer que la fonction

> EXERCISE 3. a) Expand the function \( f : \rbrack - 1,1\lbrack \rightarrow \mathbb{R}\;x \mapsto {\left( \arcsin x\right) }^{2} \) into a power series. b) Show that the function

\[
f : \rbrack 0,1\lbrack  \rightarrow  \mathbb{R}\;x \mapsto  \frac{\arcsin \sqrt{x}}{\sqrt{x\left( {1 - x}\right) }}
\]

coïncide sur ]0, 1 [ avec la somme d'une série entière, et calculer en les coefficients.

> coincides on ]0, 1[ with the sum of a power series, and calculate the coefficients.

Solution. Tout repose sur la méthode de l'équation différentielle.

> Solution. Everything relies on the differential equation method.

a) La fonction arcsinus est développable en série entière sur ] - 1, 1 [ (c'est du cours), son carré l’est donc également (par un produit de Cauchy). Ainsi, il existe une série entière \( \sum {a}_{n}{x}^{n} \) qui coïncide avec \( f \) sur \( \rbrack - 1,1\lbrack \) . Pour calculer les \( {a}_{n} \) , on recherche une équation différentielle vérifiée par \( f \) . On a

> a) The arcsine function can be expanded into a power series on ] - 1, 1 [ (this is in the course), so its square can be as well (via a Cauchy product). Thus, there exists a power series \( \sum {a}_{n}{x}^{n} \) that coincides with \( f \) on \( \rbrack - 1,1\lbrack \) . To calculate the \( {a}_{n} \) , we look for a differential equation satisfied by \( f \) . We have

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;{f}^{\prime }\left( x\right)  = \frac{2\arcsin x}{\sqrt{1 - {x}^{2}}}\;\text{ donc }\;\left( {1 - {x}^{2}}\right) {f}^{\prime }{\left( x\right) }^{2} = 4{\left( \arcsin x\right) }^{2} = {4f}\left( x\right) ,}\right.
\]

et par dérivation de la dernière égalité

> and by differentiating the last equality

\[
2\left( {1 - {x}^{2}}\right) {f}^{\prime }\left( x\right) {f}^{\prime \prime }\left( x\right)  - {2x}{f}^{\prime }{\left( x\right) }^{2} = 4{f}^{\prime }\left( x\right) \;\text{ donc }\;\left( {1 - {x}^{2}}\right) {f}^{\prime \prime }\left( x\right)  - x{f}^{\prime }\left( x\right)  = 2.
\]

En reportant la somme de la série entière dans cette dernière équation, on obtient

> By substituting the sum of the power series into this last equation, we obtain

\[
\forall x \in  \rbrack  - 1,1\left\lbrack  {,\;\left( {1 - {x}^{2}}\right) \left( {\mathop{\sum }\limits_{{n = 2}}^{{+\infty }}n\left( {n - 1}\right) {a}_{n}{x}^{n - 2}}\right)  - x\left( {\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{a}_{n}{x}^{n - 1}}\right)  = 2}\right.
\]

\[
\text{ donc }\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left\lbrack  {\left( {n + 1}\right) \left( {n + 2}\right) {a}_{n + 2} - {n}^{2}{a}_{n}}\right\rbrack  {x}^{n} = 2.
\]

Cette dernière égalité est vraie sur \( \rbrack - 1,1\lbrack \) tout entier, on en déduit par identification des coefficients (on peut, voir la conséquence du corollaire 1 page 249)

> This last equality is true on the entire \( \rbrack - 1,1\lbrack \) , we deduce from it by identification of the coefficients (we can, see the consequence of corollary 1 on page 249)

\[
2{a}_{2} = 2\;\text{ et }\;\forall n \in  {\mathbb{N}}^{ * },\;{a}_{n + 2} = \frac{{n}^{2}}{\left( {n + 1}\right) \left( {n + 2}\right) }{a}_{n}.
\]

(*)

> Par ailleurs, \( {a}_{0} = f\left( 0\right) = 0 \) et \( {a}_{1} = {f}^{\prime }\left( 0\right) = 0 \) . Avec (*), on trouve finalement

Furthermore, \( {a}_{0} = f\left( 0\right) = 0 \) and \( {a}_{1} = {f}^{\prime }\left( 0\right) = 0 \) . With (*), we finally find

\[
\forall n \in  \mathbb{N},\;{a}_{{2n} + 1} = 0\;\text{ et }\;\forall n \in  {\mathbb{N}}^{ * },\;{a}_{2n} = \frac{{2}^{{2n} - 2}{\left( \left( n - 1\right) !\right) }^{2}}{n\left( {{2n} - 1}\right) !}.
\]

Les coefficients d’indice impair sont nuls, ceci est cohérent car \( f \) est paire. Remarquez au passage que le rayon de convergence de la série entière \( \sum {a}_{2n}{z}^{2n} \) est égal à 1 (ceci car le rayon de \( \sum {a}_{2n}{z}^{n} \) est égal à 1 par la règle de d'Alembert).

> The odd-indexed coefficients are zero; this is consistent because \( f \) is even. Note in passing that the radius of convergence of the power series \( \sum {a}_{2n}{z}^{2n} \) is equal to 1 (this is because the radius of \( \sum {a}_{2n}{z}^{n} \) is equal to 1 by d'Alembert's rule).

b) On sait que la fonction impaire arcsinus admet un développement en série entière sur \( \rbrack - 1,1\lbrack \) de la forme \( \sum {a}_{n}{x}^{{2n} + 1} \) . Donc

> b) We know that the odd function arcsine admits a power series expansion on \( \rbrack - 1,1\lbrack \) of the form \( \sum {a}_{n}{x}^{{2n} + 1} \) . Therefore

\[
\forall x \in  \rbrack 0,1\lbrack ,\;f\left( x\right)  = \frac{\arcsin \sqrt{x}}{\sqrt{x\left( {1 - x}\right) }} = \frac{1}{\sqrt{1 - x}}\frac{1}{\sqrt{x}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{\left( \sqrt{x}\right) }^{{2n} + 1} = \frac{1}{\sqrt{1 - x}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n},
\]

et comme \( x \mapsto {\left( 1 - x\right) }^{-1/2} \) coincide avec la somme d’une série entière sur \( \rbrack 0,1\lbrack \) , on en déduit par un produit de Cauchy que c’est aussi le cas pour \( f \) .

> and since \( x \mapsto {\left( 1 - x\right) }^{-1/2} \) coincides with the sum of a power series on \( \rbrack 0,1\lbrack \) , we deduce by a Cauchy product that this is also the case for \( f \) .

Il existe donc une série entière \( \sum {b}_{n}{x}^{n} \) dont la somme coïncide avec \( f \) sur \( \rbrack 0,1\lbrack \) (au passage, elle a forcément un rayon de convergence \( \geq 1 \) ). Recherchons une équation différentielle vérifiée par \( f \) . Par dérivation de \( x\left( {1 - x}\right) f{\left( x\right) }^{2} = {\left( \arcsin \sqrt{x}\right) }^{2} \) , on tire

> There exists, therefore, a power series \( \sum {b}_{n}{x}^{n} \) whose sum coincides with \( f \) on \( \rbrack 0,1\lbrack \) (incidentally, it necessarily has a radius of convergence \( \geq 1 \) ). Let us look for a differential equation satisfied by \( f \) . By differentiating \( x\left( {1 - x}\right) f{\left( x\right) }^{2} = {\left( \arcsin \sqrt{x}\right) }^{2} \) , we obtain

\[
\forall x \in  \rbrack 0,1\left\lbrack  \right. ,\;{2x}\left( {1 - x}\right) {f}^{\prime }\left( x\right) f\left( x\right)  + \left( {1 - {2x}}\right) f{\left( x\right) }^{2} = \frac{2\arcsin \sqrt{x}}{\sqrt{1 - x}}\frac{1}{2\sqrt{x}} = f\left( x\right) ,
\]

donc

> therefore

\[
\forall x \in  \rbrack 0,1\lbrack ,\;{2x}\left( {1 - x}\right) {f}^{\prime }\left( x\right)  + \left( {1 - {2x}}\right) f\left( x\right)  = 1,
\]

et finalement

> and finally

\[
\forall x \in  \rbrack 0,1\lbrack ,\;{b}_{0} + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left\lbrack  {\left( {{2n} + 1}\right) {b}_{n} - {2n}{b}_{n - 1}}\right\rbrack  {x}^{n} - 1 = 0.
\]

D'après le principe des zéros isolés, tous les coefficients de cette série entière sont nuls, ce qui s'écrit

> According to the isolated zeros principle, all the coefficients of this power series are zero, which is written

\[
{b}_{0} = 1,\;\forall n \in  {\mathbb{N}}^{ * },\;{b}_{n} = \frac{2n}{{2n} + 1}{b}_{n - 1}\;\text{ donc }\;\forall n \in  {\mathbb{N}}^{ * },\;{b}_{n} = \frac{2 \cdot  4\cdots \left( {2n}\right) }{3 \cdot  5\cdots \left( {{2n} + 1}\right) }.
\]

\( \rightarrow \) EXERCICE 4. Soient \( \sum {a}_{n}{x}^{n} \) et \( \sum {b}_{n}{x}^{n} \) deux séries entières de rayon de convergence \( \geq 1 \) . On suppose que \( {b}_{n} > 0 \) pour tout \( n \) et que la série \( \sum {b}_{n} \) diverge. Pour tout \( n \in \mathbb{N} \) , on pose \( {A}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) et \( {B}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{b}_{k} \) . a) S’il existe \( \ell \in \mathbb{C} \) tel que

> \( \rightarrow \) EXERCISE 4. Let \( \sum {a}_{n}{x}^{n} \) and \( \sum {b}_{n}{x}^{n} \) be two power series with radius of convergence \( \geq 1 \) . Suppose that \( {b}_{n} > 0 \) for all \( n \) and that the series \( \sum {b}_{n} \) diverges. For all \( n \in \mathbb{N} \) , let \( {A}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) and \( {B}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{b}_{k} \) . a) If there exists \( \ell \in \mathbb{C} \) such that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{a}_{n}}{{b}_{n}} = \ell \;\text{ ou }\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{A}_{n}}{{B}_{n}} = \ell ,
\]

montrer que

> show that

\[
\mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {x < 1} }}\frac{\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n}}{\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n}} = \ell .
\]

b) Si on suppose simplement

> b) If we simply assume

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{A}_{0} + \cdots  + {A}_{n - 1}}{n} = \ell \;\text{ avec }\;\ell  \in  \mathbb{C},
\]

montrer que \( \mathop{\lim }\limits_{\substack{{x \rightarrow 1} \\ {x < 1} }}\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n} = \ell \) .

> show that \( \mathop{\lim }\limits_{\substack{{x \rightarrow 1} \\ {x < 1} }}\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n} = \ell \) .

c) (Application.) Lorsque \( x \) tend vers 1 par valeurs inférieures, montrer les équivalents

> c) (Application.) As \( x \) tends to 1 from below, show the equivalents

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{{n}^{2}} \sim  \frac{\sqrt{\pi }}{2\sqrt{1 - x}},\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{{a}^{n}} \sim   - \frac{\log \left( {1 - x}\right) }{\log a}\;\left( {a \in  \mathbb{N}, a \geq  2}\right) ,\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}{x}^{{4n} + 1} \sim  \frac{1}{2}.
\]

Solution. a) Supposons tout d’abord \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{a}_{n}/{b}_{n} = \ell \) . Soit \( \varepsilon > 0 \) et \( {n}_{0} \in \mathbb{N} \) tel que \( \left| {{a}_{n} - \ell {b}_{n}}\right| < \; \varepsilon {b}_{n} \) pour tout \( n \geq {n}_{0} \) . Pour tout \( x \in \lbrack 0,1\lbrack \) , on a

> Solution. a) Let us first assume \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{a}_{n}/{b}_{n} = \ell \) . Let \( \varepsilon > 0 \) and \( {n}_{0} \in \mathbb{N} \) be such that \( \left| {{a}_{n} - \ell {b}_{n}}\right| < \; \varepsilon {b}_{n} \) for all \( n \geq {n}_{0} \) . For all \( x \in \lbrack 0,1\lbrack \) , we have

\[
\left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {{a}_{n} - \ell {b}_{n}}\right) {x}^{n}}\right|  \leq  \mathop{\sum }\limits_{{n = 0}}^{{{n}_{0} - 1}}\left| {{a}_{n} - \ell {b}_{n}}\right| {x}^{n} + \mathop{\sum }\limits_{{n = {n}_{0}}}^{{+\infty }}\left| {{a}_{n} - \ell {b}_{n}}\right| {x}^{n} \leq  \mathop{\sum }\limits_{{n = 0}}^{{{n}_{0} - 1}}\left| {{a}_{n} - \ell {b}_{n}}\right|  + \varepsilon \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{x}^{n}}\right) .
\]

(*)

> Or \( \sum {b}_{n} \) est une série à termes positifs divergente, donc \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n} = + \infty \) (en effet, pour tout \( N \in \mathbb{N},\mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n} \geq \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{N}{b}_{n}{x}^{n} = \mathop{\sum }\limits_{{n = 0}}^{N}{b}_{n} \) ), on en déduit

Now \( \sum {b}_{n} \) is a divergent series with positive terms, so \( \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n} = + \infty \) (indeed, for all \( N \in \mathbb{N},\mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n} \geq \mathop{\lim }\limits_{{x \rightarrow {1}^{ - }}}\mathop{\sum }\limits_{{n = 0}}^{N}{b}_{n}{x}^{n} = \mathop{\sum }\limits_{{n = 0}}^{N}{b}_{n} \) ), we deduce

\[
\exists \lambda  \in  \rbrack 0,1\left\lbrack  {,\forall x \in  }\right\rbrack  \lambda ,1\left\lbrack  \right. ,\;\varepsilon \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{x}^{n}}\right)  \geq  \mathop{\sum }\limits_{{n = 0}}^{{{n}_{0} - 1}}\left| {{a}_{n} - \ell {b}_{n}}\right| ,
\]

donc d'après (*)

> therefore according to (*)

\[
\forall x \in  \rbrack \lambda ,1\lbrack ,\;\left| {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {{a}_{n} - \ell {b}_{n}}\right) {x}^{n}}\right|  \leq  {2\varepsilon }\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{x}^{n}}\right) \;\text{ c’est-à-dire }\;\left| {\frac{\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n}}{\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n}} - \ell }\right|  \leq  {2\varepsilon },
\]

d'où le résultat.

> hence the result.

Si \( {A}_{n}/{B}_{n} \rightarrow \ell \) , tout repose sur la remarque suivante, conséquence d’un produit de Cauchy :

> If \( {A}_{n}/{B}_{n} \rightarrow \ell \) , everything relies on the following remark, a consequence of a Cauchy product:

\[
\mathop{\sum }\limits_{{n = 0}}^{\infty }\frac{{a}_{n}{x}^{n}}{1 - x} = \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{n}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{A}_{n}{x}^{n},\;\frac{\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n}}{1 - x} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{B}_{n}{x}^{n}.
\]

\( \left( {* * }\right) \)

> L'étude du cas précédent montre que

The study of the previous case shows that

\[
\mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {x < 1} }}\frac{\mathop{\sum }\limits_{{n = 0}}^{\infty }{A}_{n}{x}^{n}}{\mathop{\sum }\limits_{{n = 0}}^{\infty }{B}_{n}{x}^{n}} = \ell ,
\]

et on en déduit le résultat avec (**).

> and we deduce the result from it with (**).

b) Un produit de Cauchy donne

> b) A Cauchy product gives

\[
\forall x \in  \lbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\left( {{A}_{0} + \cdots  + {A}_{n - 1}}\right) {x}^{n} = \frac{x}{1 - x}\mathop{\sum }\limits_{{n = 0}}^{\infty }{A}_{n}{x}^{n} = \frac{x}{{\left( 1 - x\right) }^{2}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n}
\]

et par ailleurs,

> and furthermore,

\[
\forall x \in  \lbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}n{x}^{n} = x\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}n{x}^{n - 1} = x\frac{d}{dx}\left( \frac{1}{1 - x}\right)  = \frac{x}{{\left( 1 - x\right) }^{2}}.
\]

Comme d'après la question précédente

> Since according to the previous question

\[
\mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {x < 1} }}\frac{\mathop{\sum }\limits_{{n = 0}}^{\infty }\left( {{A}_{0} + \cdots  + {A}_{n - 1}}\right) {x}^{n}}{\mathop{\sum }\limits_{{n = 0}}^{\infty }n{x}^{n}} = \ell ,\;\text{ on en déduit }\;\mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {x < 1} }}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n} = \ell .
\]

c) Pour la série entière \( \sum {a}_{n}{x}^{n} = \sum {x}^{{n}^{2}} \) , on a avec les notations précédentes \( {A}_{n} = 1 + \left\lbrack \sqrt{n}\right\rbrack \) (où la notation \( \left\lbrack t\right\rbrack \) désigne la partie entière de \( t \) ). Or

> c) For the power series \( \sum {a}_{n}{x}^{n} = \sum {x}^{{n}^{2}} \) , we have with the previous notations \( {A}_{n} = 1 + \left\lbrack \sqrt{n}\right\rbrack \) (where the notation \( \left\lbrack t\right\rbrack \) denotes the integer part of \( t \) ). Now

\[
\frac{1}{\sqrt{1 - x}} = 1 + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}\frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n}
\]

et d'après la formule de Wallis

> and according to Wallis's formula

\[
{b}_{n} = \frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) } \sim  \frac{1}{\sqrt{n\pi }}\;n \rightarrow   + \infty
\]

(on peut aussi obtenir ce dernier équivalent en utilisant la formule de Stirling). On en déduit que \( \sum {b}_{n} \) diverge et que \( {B}_{n} \sim \frac{1}{\sqrt{\pi }}\mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{\sqrt{k}} \) (sommation d’équivalents, voir le théorème 5 page 210). Un équivalent de cette dernière somme s'obtient facilement par comparaison série-intégrale, en écrivant

> (one can also obtain this last equivalent using Stirling's formula). We deduce that \( \sum {b}_{n} \) diverges and that \( {B}_{n} \sim \frac{1}{\sqrt{\pi }}\mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{\sqrt{k}} \) (summation of equivalents, see theorem 5 page 210). An equivalent of this last sum is easily obtained by series-integral comparison, by writing

\[
{\int }_{1}^{n + 1}\frac{dt}{\sqrt{t}} = \mathop{\sum }\limits_{{k = 1}}^{n}{\int }_{k}^{k + 1}\frac{dt}{\sqrt{t}} \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{\sqrt{k}} \leq  \mathop{\sum }\limits_{{k = 1}}^{n}{\int }_{k - 1}^{k}\frac{dt}{\sqrt{t}} = {\int }_{0}^{n}\frac{dt}{\sqrt{t}},\;\text{ d’où }\;\mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{\sqrt{k}} \sim  2\sqrt{n},
\]

et finalement \( {B}_{n} \sim 2\sqrt{n}/\sqrt{\pi } \) . Ainsi, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{A}_{n}/{B}_{n} = \sqrt{\pi }/2 \) , et d’après a) on en déduit

> and finally \( {B}_{n} \sim 2\sqrt{n}/\sqrt{\pi } \) . Thus, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{A}_{n}/{B}_{n} = \sqrt{\pi }/2 \) , and according to a) we deduce

\[
\mathop{\lim }\limits_{{x \rightarrow  {1}^{ - }}}\frac{\mathop{\sum }\limits_{{n = 0}}^{\infty }{a}_{n}{x}^{n}}{\mathop{\sum }\limits_{{n = 0}}^{\infty }{b}_{n}{x}^{n}} = \frac{\sqrt{\pi }}{2},\;\text{ ce qui s’écrit aussi }\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{{n}^{2}} \sim  \frac{\sqrt{\pi }}{2\sqrt{1 - x}}.
\]

Pour la série entière \( \sum {a}_{n}{x}^{n} = \sum {x}^{{a}^{n}} \) , on a \( {A}_{n} = 1 + \left\lbrack {\log n/\log a}\right\rbrack \sim \log n/\log a \) . Or si \( {b}_{n} = 1/n \) on a

> For the power series \( \sum {a}_{n}{x}^{n} = \sum {x}^{{a}^{n}} \) , we have \( {A}_{n} = 1 + \left\lbrack {\log n/\log a}\right\rbrack \sim \log n/\log a \) . Now if \( {b}_{n} = 1/n \) we have

\[
\mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{b}_{n}{x}^{n} =  - \log \left( {1 - x}\right) \;\text{ et }\;{B}_{n} = 1 + \frac{1}{2} + \cdots  + \frac{1}{n} \sim  \log n,
\]

donc \( {A}_{n}/{B}_{n} \rightarrow 1/\log a \) . On en déduit d’après a) que lorsque \( x \rightarrow 1 - \) ,

> therefore \( {A}_{n}/{B}_{n} \rightarrow 1/\log a \) . We deduce from a) that when \( x \rightarrow 1 - \) ,

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{x}^{{a}^{n}} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{x}^{n} \sim  \frac{1}{\log a}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{x}^{n} =  - \frac{\log \left( {1 - x}\right) }{\log a}.
\]

Pour \( \sum {a}_{n}{x}^{n} = \sum {\left( -1\right) }^{n}{x}^{{4n} + 1} \) , on a \( {A}_{{8n} + k} = 1 \) pour \( 1 \leq k \leq 4 \) et \( {A}_{{8n} + k} = 0 \) pour \( 5 \leq k < 8 \) , donc \( \left( {{A}_{0} + {A}_{1} + \cdots + {A}_{n - 1}}\right) /n \rightarrow 1/2 \) , d’où l’équivalent recherché d’après la question b).

> For \( \sum {a}_{n}{x}^{n} = \sum {\left( -1\right) }^{n}{x}^{{4n} + 1} \) , we have \( {A}_{{8n} + k} = 1 \) for \( 1 \leq k \leq 4 \) and \( {A}_{{8n} + k} = 0 \) for \( 5 \leq k < 8 \) , therefore \( \left( {{A}_{0} + {A}_{1} + \cdots + {A}_{n - 1}}\right) /n \rightarrow 1/2 \) , hence the sought equivalent according to question b).

EXERCICE 5 (THÉORÉME DE LIOUVILLE). Soit \( \sum {a}_{n}{z}^{n} \) une série entière dont le rayon de convergence est infini. Soit \( f : \mathbb{C} \rightarrow \mathbb{C} \) la somme de cette série entière.

> EXERCISE 5 (LIOUVILLE'S THEOREM). Let \( \sum {a}_{n}{z}^{n} \) be a power series whose radius of convergence is infinite. Let \( f : \mathbb{C} \rightarrow \mathbb{C} \) be the sum of this power series.

a) Si la fonction entière \( f \) est bornée sur \( \mathbb{C} \) , montrer que \( f \) est constante.

> a) If the entire function \( f \) is bounded on \( \mathbb{C} \) , show that \( f \) is constant.

b) Plus généralement, s’il existe un polynôme \( P \) à coefficients positifs tel que \( \left| {f\left( z\right) }\right| \leq \; P\left( \left| z\right| \right) \) pour tout \( z \in \mathbb{C} \) , montrer que \( f \) est un polynôme.

> b) More generally, if there exists a polynomial \( P \) with positive coefficients such that \( \left| {f\left( z\right) }\right| \leq \; P\left( \left| z\right| \right) \) for all \( z \in \mathbb{C} \), show that \( f \) is a polynomial.

Solution. a) C'est immédiat si l'on connaît la formule de Cauchy (voir le théorème 4 page 250). En désignant par \( M \) un majorant de \( \left| f\right| \) sur \( \mathbb{C} \) , on a en effet

> Solution. a) This is immediate if one knows Cauchy's formula (see theorem 4 on page 250). By denoting \( M \) as an upper bound of \( \left| f\right| \) on \( \mathbb{C} \), we indeed have

\[
\forall n \in  \mathbb{N},\forall r > 0,\;{a}_{n}{r}^{n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }f\left( {r{e}^{i\theta }}\right) {e}^{-{ni\theta }}{d\theta }\;\text{ donc }\left| {a}_{n}\right| {r}^{n} \leq  M.
\]

Si \( n \in {\mathbb{N}}^{ * } \) , la majoration \( \left| {a}_{n}\right| \leq M/{r}^{n} \) est vraie pour tout \( r > 0 \) et on peut donc faire \( r \rightarrow + \infty \) , ce qui entraîne \( {a}_{n} = 0 \) pour tout \( n \in {\mathbb{N}}^{ * } \) , d’où le résultat.

> If \( n \in {\mathbb{N}}^{ * } \), the bound \( \left| {a}_{n}\right| \leq M/{r}^{n} \) is true for all \( r > 0 \) and we can therefore let \( r \rightarrow + \infty \), which implies \( {a}_{n} = 0 \) for all \( n \in {\mathbb{N}}^{ * } \), hence the result.

b) Notons \( m = \deg \left( P\right) \) . Si \( m = 0 \) , la réponse a été apportée dans la résolution de la question précédente. Sinon, on pose

> b) Let \( m = \deg \left( P\right) \). If \( m = 0 \), the answer was provided in the resolution of the previous question. Otherwise, we set

\[
g\left( z\right)  = \mathop{\sum }\limits_{{n = m}}^{{+\infty }}{a}_{n}{z}^{n - m}
\]

somme d’une série entière de rayon de convergence infini. La fonction \( g \) vérifie

> sum of a power series with an infinite radius of convergence. The function \( g \) satisfies

\[
\forall z \in  {\mathbb{C}}^{ * },\;g\left( z\right)  = \frac{f\left( z\right)  - {a}_{0} - {a}_{1}z - \cdots  - {a}_{m - 1}{z}^{m - 1}}{{z}^{m}},
\]

et comme \( m = \deg \left( P\right) \) , ceci montre que \( g \) est bornée sur \( \mathbb{C} \) tout entier. Comme on l’a vu plus haut, \( g \) est donc constante, donc \( {a}_{n} = 0 \) dès que \( n > m \) , d’où le résultat.

> and since \( m = \deg \left( P\right) \), this shows that \( g \) is bounded on the entire \( \mathbb{C} \). As seen above, \( g \) is therefore constant, so \( {a}_{n} = 0 \) as soon as \( n > m \), hence the result.

Remarque. On aurait pu aussi résoudre la question a) de l'exercice en utilisant la formule de Parseval au lieu de la formule de Cauchy.

> Remark. One could also have solved question a) of the exercise by using Parseval's formula instead of Cauchy's formula.

- La considération des valeurs complexes de la variable permet seule de comprendre des phénomènes qui seraient surprenant si on se confinait à la variable réelle. Par exemple, la fonction sinus est développable en série entière sur \( \mathbb{R} \) , bornée sur \( \mathbb{R} \) , mais elle n’est pas constante.

> - Considering complex values of the variable is the only way to understand phenomena that would be surprising if one were confined to the real variable. For example, the sine function can be expanded as a power series on \( \mathbb{R} \), is bounded on \( \mathbb{R} \), but is not constant.

- Le théorème de Liouville (question a)) admet une généralisation étonnante, connue sous le nom de théorème de Picard : toute fonction entière \( f \) qui évite deux valeurs est forcément constante. Autrement dit, s’il existe deux valeurs distinctes \( a \) et \( b \) de \( \mathbb{C} \) telles que \( f\left( z\right)  \neq  a \) et \( f\left( z\right)  \neq  b \) pour tout \( z \in  \mathbb{C} \) , alors \( f \) est constante.

> - Liouville's theorem (question a)) admits an astonishing generalization, known as Picard's theorem: any entire function \( f \) that avoids two values is necessarily constant. In other words, if there exist two distinct values \( a \) and \( b \) of \( \mathbb{C} \) such that \( f\left( z\right)  \neq  a \) and \( f\left( z\right)  \neq  b \) for all \( z \in  \mathbb{C} \), then \( f \) is constant.

EXERCICE 6. Soit \( \Phi \) la somme d’une série entière \( \sum {a}_{n}{z}^{n} \) dont le rayon de convergence \( R \) est non nul.

> EXERCISE 6. Let \( \Phi \) be the sum of a power series \( \sum {a}_{n}{z}^{n} \) whose radius of convergence \( R \) is non-zero.

a) Montrer que la série entière \( \sum {a}_{n}{z}^{n}/n \) ! a un rayon de convergence infini.

> a) Show that the power series \( \sum {a}_{n}{z}^{n}/n \)! has an infinite radius of convergence.

b) On note \( \varphi \) la somme de la série entière \( \sum {a}_{n}{z}^{n}/n \) !. Montrer

> b) Let \( \varphi \) be the sum of the power series \( \sum {a}_{n}{z}^{n}/n \)!. Show

\[
\forall z \in  \mathbb{C},\left| z\right|  < R,\;\Phi \left( z\right)  = {\int }_{0}^{+\infty }\varphi \left( {zx}\right) {e}^{-x}{dx}.
\]

---

Solution. a) Fixons \( {r}_{0} \) tel que \( 0 < {r}_{0} < R \) , de sorte que la suite \( \left( {{a}_{n}{r}_{0}^{n}}\right) \) est bornée (elle tend même vers 0). Pour tout \( r > 0 \) , on a \( {a}_{n}{r}^{n}/n! = \left( {{a}_{n}{r}_{0}^{n}}\right) \left( {{q}^{n}/n!}\right) \) (avec \( q = r/{r}_{0} \) ), et comme \( \left( {{q}^{n}/n!}\right) \) est bornée (le rayon de convergence de la série \( \sum {z}^{n}/n \) ! est infini), on en déduit que la suite \( \left( {{a}_{n}{r}^{n}/n!}\right) \) est bornée.

> Solution. a) Let us fix \( {r}_{0} \) such that \( 0 < {r}_{0} < R \) , so that the sequence \( \left( {{a}_{n}{r}_{0}^{n}}\right) \) is bounded (it even tends to 0). For any \( r > 0 \) , we have \( {a}_{n}{r}^{n}/n! = \left( {{a}_{n}{r}_{0}^{n}}\right) \left( {{q}^{n}/n!}\right) \) (with \( q = r/{r}_{0} \) ), and since \( \left( {{q}^{n}/n!}\right) \) is bounded (the radius of convergence of the series \( \sum {z}^{n}/n \) ! is infinite), we deduce that the sequence \( \left( {{a}_{n}{r}^{n}/n!}\right) \) is bounded.

---

b) Soit \( z \in \mathbb{C} \) tel que \( \left| z\right| < R \) . Commençons par montrer l’existence de l’intégrale. On fixe \( r \) tel \( \left| z\right| < r < R \) . La suite \( \left( {{a}_{n}{r}^{n}}\right) \) est bornée, donc si \( M \) désigne un majorant de \( \left( {\left| {a}_{n}\right| {r}^{n}}\right) \) , on a

> b) Let \( z \in \mathbb{C} \) be such that \( \left| z\right| < R \) . Let us begin by showing the existence of the integral. We fix \( r \) such that \( \left| z\right| < r < R \) . The sequence \( \left( {{a}_{n}{r}^{n}}\right) \) is bounded, so if \( M \) denotes an upper bound of \( \left( {\left| {a}_{n}\right| {r}^{n}}\right) \) , we have

\[
\forall x \geq  0,\forall n \in  \mathbb{N},\;\left| \frac{{a}_{n}{\left( zx\right) }^{n}}{n!}\right|  = \left| {{a}_{n}{r}^{n}}\right| \frac{{\left| zx/r\right| }^{n}}{n!} \leq  M\frac{{\left( qx\right) }^{n}}{n!},\;q = \frac{\left| z\right| }{r} < 1,
\]

(*)

> ce qui par sommation entraîne \( \left| {\varphi \left( {xz}\right) }\right| \leq M{e}^{qx} \) pour tout \( x \geq 0 \) . Ainsi, \( \left| {\varphi \left( {xz}\right) {e}^{-x}}\right| \leq M{e}^{\left( {q - 1}\right) x} \) pour tout \( x \geq 0 \) et comme \( q < 1 \) , l’intégrale proposée converge bien.

which by summation implies \( \left| {\varphi \left( {xz}\right) }\right| \leq M{e}^{qx} \) for all \( x \geq 0 \) . Thus, \( \left| {\varphi \left( {xz}\right) {e}^{-x}}\right| \leq M{e}^{\left( {q - 1}\right) x} \) for all \( x \geq 0 \) and since \( q < 1 \) , the proposed integral indeed converges.

> Il suffit maintenant d'écrire

It now suffices to write

\[
{\int }_{0}^{+\infty }\varphi \left( {xz}\right) {e}^{-x}{dx} = {\int }_{0}^{+\infty }\left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{a}_{n}{\left( xz\right) }^{n}}{n!}}\right) {e}^{-x}{dx} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{a}_{n}{z}^{n}}{n!}{\int }_{0}^{+\infty }{x}^{n}{e}^{-x}{dx} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n},
\]

car \( {\int }_{0}^{+\infty }{x}^{n}{e}^{-x}{dx} = \Gamma \left( {n + 1}\right) = n \) ! pour tout \( n \in \mathbb{N} \) . Nous avons bien le droit d’inverser les signes de sommations car d'après (*) les sommes partielles de la série vérifient la majoration

> because \( {\int }_{0}^{+\infty }{x}^{n}{e}^{-x}{dx} = \Gamma \left( {n + 1}\right) = n \) ! for all \( n \in \mathbb{N} \) . We are indeed allowed to swap the summation signs because, according to (*), the partial sums of the series satisfy the bound

\[
\forall N \in  {\mathbb{N}}^{ * },\;\left| {\mathop{\sum }\limits_{{n = 1}}^{N}\frac{{a}_{n}{\left( zx\right) }^{n}}{n!}{e}^{-x}}\right|  \leq  M\mathop{\sum }\limits_{{n = 1}}^{N}\frac{{\left( qx\right) }^{n}}{n!}{e}^{-x} \leq  {e}^{\left( {q - 1}\right) x}
\]

et \( x \mapsto {e}^{\left( {q - 1}\right) x} \) est intégrable sur \( {\mathbb{R}}^{ + } \) , donc l’hypothèse de domination du théorème de convergence dominée est vérifiée.

> and \( x \mapsto {e}^{\left( {q - 1}\right) x} \) is integrable on \( {\mathbb{R}}^{ + } \) , so the domination hypothesis of the dominated convergence theorem is satisfied.

EXERCICE 7. Soient \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) des entiers naturels non nuls premiers entre eux dans leur ensemble. Pour tout \( n \in \mathbb{N} \) , on note \( {S}_{n} \) le nombre de solutions \( \left( {{n}_{1},\ldots ,{n}_{p}}\right) \in {\mathbb{N}}^{p} \) de l'équation

> EXERCISE 7. Let \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) be non-zero natural numbers that are coprime as a set. For any \( n \in \mathbb{N} \) , let \( {S}_{n} \) denote the number of solutions \( \left( {{n}_{1},\ldots ,{n}_{p}}\right) \in {\mathbb{N}}^{p} \) to the equation

\[
{\alpha }_{1}{n}_{1} + \cdots  + {\alpha }_{p}{n}_{p} = n
\]

Donner un équivalent de \( {S}_{n} \) lorsque \( n \rightarrow + \infty \) . (Indication : interpréter \( {S}_{n} \) comme le coefficient d’une série entière qui s’exprime simplement en fonction de \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) .)

> Provide an equivalent for \( {S}_{n} \) as \( n \rightarrow + \infty \) . (Hint: interpret \( {S}_{n} \) as the coefficient of a power series that can be expressed simply in terms of \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) .)

Solution. Considérons la série entière définie par le produit de Cauchy des séries entières

> Solution. Consider the power series defined by the Cauchy product of the power series

\[
\left( {\mathop{\sum }\limits_{{{n}_{1} \in  \mathbb{N}}}{z}^{{\alpha }_{1}{n}_{1}}}\right) ,\ldots ,\left( {\mathop{\sum }\limits_{{{n}_{p} \in  \mathbb{N}}}{z}^{{\alpha }_{p}{n}_{p}}}\right) .
\]

Toute l’astuce est de remarquer que le coefficient de \( {z}^{n} \) dans ce produit de Cauchy est le nombre de manière de combiner les puissances de \( z \) de chaque terme du produit pour que leur somme fasse \( n \) . En d’autres termes, on a

> The whole trick is to notice that the coefficient of \( {z}^{n} \) in this Cauchy product is the number of ways to combine the powers of \( z \) from each term of the product so that their sum equals \( n \) . In other words, we have

\[
F\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{S}_{n}{z}^{n} = \left( {\mathop{\sum }\limits_{{{n}_{1} = 0}}^{{+\infty }}{z}^{{\alpha }_{1}{n}_{1}}}\right) \cdots \left( {\mathop{\sum }\limits_{{{n}_{p} = 0}}^{{+\infty }}{z}^{{\alpha }_{p}{n}_{p}}}\right)  = \frac{1}{1 - {z}^{{\alpha }_{1}}}\cdots \frac{1}{1 - {z}^{{\alpha }_{p}}},
\]

et toutes les séries entières correspondantes ont leur rayon de convergence égal à 1. La fonction \( F\left( z\right) \) est une fraction rationnelle, dont les pôles se trouvent aux racines \( {\alpha }_{1} \) -ièmes, \( \ldots ,{\alpha }_{p} \) -ièmes de l’unité. Le pôle \( z = 1 \) est de multiplicité \( p \) , et tous les autres pôles ont une multiplicité \( < p \) (en effet, si \( {\omega }^{{\alpha }_{1}} = \cdots = {\omega }^{{\alpha }_{p}} = 1 \) avec \( \omega = {e}^{{2ia\pi }/b} \) une racine de l’unité et \( a \land b = 1 \) , alors \( b \) divise \( {\alpha }_{1}a,\ldots ,{\alpha }_{p}a \) donc \( b \) divise \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) d’après le théorème de Gauss, donc \( b = 1 \) car les \( {\alpha }_{i} \) sont premiers entre eux dans leur ensemble). On peut donc écrire la décomposition en éléments simples de \( F \) sous la forme

> and all corresponding power series have a radius of convergence equal to 1. The function \( F\left( z\right) \) is a rational fraction whose poles are located at the \( {\alpha }_{1} \)-th and \( \ldots ,{\alpha }_{p} \)-th roots of unity. The pole \( z = 1 \) has multiplicity \( p \), and all other poles have multiplicity \( < p \) (indeed, if \( {\omega }^{{\alpha }_{1}} = \cdots = {\omega }^{{\alpha }_{p}} = 1 \) with \( \omega = {e}^{{2ia\pi }/b} \) a root of unity and \( a \land b = 1 \), then \( b \) divides \( {\alpha }_{1}a,\ldots ,{\alpha }_{p}a \), so \( b \) divides \( {\alpha }_{1},\ldots ,{\alpha }_{p} \) by Gauss's theorem, thus \( b = 1 \) because the \( {\alpha }_{i} \) are coprime as a set). We can therefore write the partial fraction decomposition of \( F \) in the form

\[
F\left( z\right)  = \frac{A}{{\left( 1 - z\right) }^{p}} + G\left( z\right) ,\;G\left( z\right)  = \mathop{\sum }\limits_{{\omega  \in  \Pi }}\left( {\frac{{a}_{1,\omega }}{\omega  - z} + \cdots  + \frac{{a}_{p - 1,\omega }}{{\left( \omega  - z\right) }^{p - 1}}}\right) ,
\]

(*)

> où \( \Pi \) désigne un sous-ensemble fini des racines de l’unité et les \( {a}_{k,\omega } \) des constantes complexes (notez que \( 1 \in \Pi \) ). On trouve la constante \( A \) par les techniques usuelles, en écrivant

where \( \Pi \) denotes a finite subset of the roots of unity and the \( {a}_{k,\omega } \) are complex constants (note that \( 1 \in \Pi \)). We find the constant \( A \) using standard techniques by writing

\[
{\left( 1 - z\right) }^{p}F\left( z\right)  = \left( \frac{1}{1 + z + \cdots  + {z}^{{\alpha }_{1} - 1}}\right) \cdots \left( \frac{1}{1 + z + \cdots  + {z}^{{\alpha }_{p} - 1}}\right) ,
\]

ce qui en faisant \( z = 1 \) dans cette expression fournit \( A = {\left( {\alpha }_{1}\cdots {\alpha }_{p}\right) }^{-1} \) . Maintenant, comme

> which, by setting \( z = 1 \) in this expression, yields \( A = {\left( {\alpha }_{1}\cdots {\alpha }_{p}\right) }^{-1} \). Now, since

\[
\frac{1}{{\left( \omega  - z\right) }^{k}} = \frac{1}{\left( {k - 1}\right) !}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{\left( {n + k - 1}\right) !}{n!}{\omega }^{-n - k}{z}^{n}
\]

\( \left( {* * }\right) \)

> (voir la page 251), on en déduit que si \( \left| \omega \right| = 1 \) , le coefficient de \( {z}^{n} \) dans cette série entière est un \( O\left( {n}^{k - 1}\right) \) . Ainsi, d’après (*), le coefficient de \( {z}^{n} \) dans la série entière définissant \( G\left( z\right) \) est un \( O\left( {n}^{p - 2}\right) \) . On en déduit, avec (*) et (**) que

(see page 251), we deduce that if \( \left| \omega \right| = 1 \), the coefficient of \( {z}^{n} \) in this power series is a \( O\left( {n}^{k - 1}\right) \). Thus, according to (*), the coefficient of \( {z}^{n} \) in the power series defining \( G\left( z\right) \) is a \( O\left( {n}^{p - 2}\right) \). We deduce, with (*) and (**), that

\[
{S}_{n} = \frac{A}{\left( {p - 1}\right) !}\left( {n + p - 1}\right) \left( {n + p - 2}\right) \cdots \left( {n + 1}\right)  + O\left( {n}^{p - 2}\right)  \sim  \frac{1}{{\alpha }_{1}\cdots {\alpha }_{p}}\frac{{n}^{p - 1}}{\left( {p - 1}\right) !}.
\]

Remarque. En calculant toute la décomposition en éléments simples de \( F\left( z\right) \) , on peut obtenir une formule exacte (mais compliquée) pour \( {S}_{n} \) . En exercice, vous pourrez calculer exactement le nombre de solutions entières \( a, b, c \) de \( {5a} + {3b} + {2c} = {10000} \) .

> Remark. By calculating the entire partial fraction decomposition of \( F\left( z\right) \), one can obtain an exact (though complicated) formula for \( {S}_{n} \). As an exercise, you may calculate exactly the number of integer solutions \( a, b, c \) to \( {5a} + {3b} + {2c} = {10000} \).

EXERCICE 8 (THÉORÉME DE S.BERNSTEIN SUR LES SÉRIES ENTIÊRES). Soient \( a > 0 \) et \( f : \rbrack - a, a\lbrack \rightarrow \mathbb{R} \) une fonction de classe \( {\mathcal{C}}^{\infty } \) . On suppose que

> EXERCISE 8 (S. BERNSTEIN'S THEOREM ON POWER SERIES). Let \( a > 0 \) and \( f : \rbrack - a, a\lbrack \rightarrow \mathbb{R} \) be a function of class \( {\mathcal{C}}^{\infty } \). Suppose that

\[
\forall k \in  \mathbb{N},\forall x \in  \rbrack  - a, a\left\lbrack  {,\;{f}^{\left( 2k\right) }\left( x\right)  \geq  0.}\right.
\]

Montrer que \( f \) est développable en série entière sur \( \rbrack - a, a\lbrack \) . (Indication : commencer par traiter la fonction \( F\left( x\right) = f\left( x\right) + f\left( {-x}\right) \) .)

> Show that \( f \) can be expanded as a power series on \( \rbrack - a, a\lbrack \). (Hint: start by treating the function \( F\left( x\right) = f\left( x\right) + f\left( {-x}\right) \).)

Solution. Il suffit de montrer que pour tout \( b \in \rbrack 0, a\lbrack \) , la fonction \( f \) est développable en série entière sur \( \rbrack - b, b\lbrack \) (en effet, les coefficients du développement en série entière sur ] \( - b, b\lbrack \) ne dépendent pas de \( b) \) . Fixons donc \( b \in \rbrack 0, a\lbrack \) .

> Solution. It suffices to show that for any \( b \in \rbrack 0, a\lbrack \), the function \( f \) can be expanded as a power series on \( \rbrack - b, b\lbrack \) (indeed, the coefficients of the power series expansion on ] \( - b, b\lbrack \) do not depend on \( b) \)). Let us therefore fix \( b \in \rbrack 0, a\lbrack \).

Suivons l’indication et commencer par développer la fonction \( F : x \mapsto f\left( x\right) + f\left( {-x}\right) \) . Cette fonction est paire donc pour tout \( k \in \mathbb{N},{F}^{\left( 2k + 1\right) }\left( 0\right) = 0 \) , donc en appliquant la formule de Taylor avec reste intégral, on obtient, pour tout \( n \in \mathbb{N} \) et pour tout \( x \in \left\lbrack {0, b}\right\rbrack \)

> Let's follow the hint and start by expanding the function \( F : x \mapsto f\left( x\right) + f\left( {-x}\right) \) . This function is even, so for all \( k \in \mathbb{N},{F}^{\left( 2k + 1\right) }\left( 0\right) = 0 \) , and by applying Taylor's formula with integral remainder, we obtain, for all \( n \in \mathbb{N} \) and for all \( x \in \left\lbrack {0, b}\right\rbrack \)

\[
F\left( x\right)  = F\left( 0\right)  + \frac{{x}^{2}}{2!}{F}^{\prime \prime }\left( 0\right)  + \cdots  + \frac{{x}^{2n}}{\left( {2n}\right) !}{F}^{\left( 2n\right) }\left( 0\right)  + {R}_{n}\left( x\right) ,\;{R}_{n}\left( x\right)  = {\int }_{0}^{x}\frac{{\left( x - t\right) }^{{2n} + 1}}{\left( {{2n} + 1}\right) !}{F}^{\left( 2n + 2\right) }\left( t\right) {dt}.
\]

Remarquons que pour tout \( k \in \mathbb{N},{F}^{\left( 2k\right) }\left( 0\right) = 2{f}^{\left( 2k\right) }\left( 0\right) \geq 0 \) , donc la formule précédente entraîne \( 0 \leq {R}_{n}\left( b\right) \leq F\left( b\right) \) pour tout \( n \) . Pour montrer que \( {R}_{n}\left( x\right) \) tend vers 0 lorsque \( 0 \leq x < b \) , nous comparons sa valeur à \( {R}_{n}\left( b\right) \) en écrivant

> Note that for all \( k \in \mathbb{N},{F}^{\left( 2k\right) }\left( 0\right) = 2{f}^{\left( 2k\right) }\left( 0\right) \geq 0 \) , so the previous formula implies \( 0 \leq {R}_{n}\left( b\right) \leq F\left( b\right) \) for all \( n \) . To show that \( {R}_{n}\left( x\right) \) tends to 0 as \( 0 \leq x < b \) , we compare its value to \( {R}_{n}\left( b\right) \) by writing

\[
0 \leq  {R}_{n}\left( x\right)  = {\int }_{0}^{x}{\left( \frac{x - t}{b - t}\right) }^{{2n} + 1}\frac{{\left( b - t\right) }^{{2n} + 1}}{\left( {{2n} + 1}\right) !}{F}^{\left( 2n + 2\right) }\left( t\right) {dt} \leq  {\left( \frac{x}{b}\right) }^{{2n} + 1}{\int }_{0}^{x}\frac{{\left( b - t\right) }^{{2n} + 1}}{\left( {{2n} + 1}\right) !}{F}^{\left( 2n + 2\right) }\left( t\right) {dt}
\]

\[
\leq  {\left( \frac{x}{b}\right) }^{{2n} + 1}{R}_{n}\left( b\right)  \leq  {\left( \frac{x}{b}\right) }^{{2n} + 1}F\left( b\right)
\]

(on a utilisé la majoration \( \left( {x - t}\right) /\left( {b - t}\right) \leq x/b < 1 \) pour tout \( t \in \left\lbrack {0, x}\right\rbrack \) , qui provient du caractère décroissant de \( t \mapsto \frac{x - t}{b - t} \) sur \( \left\lbrack {0, x}\right\rbrack ) \) . Comme \( 0 \leq x/b < 1 \) , on en déduit \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{R}_{n}\left( x\right) = 0 \) , ce qui s'écrit aussi

> (we used the bound \( \left( {x - t}\right) /\left( {b - t}\right) \leq x/b < 1 \) for all \( t \in \left\lbrack {0, x}\right\rbrack \) , which comes from the decreasing nature of \( t \mapsto \frac{x - t}{b - t} \) on \( \left\lbrack {0, x}\right\rbrack ) \) . Since \( 0 \leq x/b < 1 \) , we deduce \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{R}_{n}\left( x\right) = 0 \) , which is also written

\[
\forall x \in  \lbrack 0, b\lbrack ,\;F\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{x}^{2n}}{\left( {2n}\right) !}{F}^{\left( 2n\right) }\left( 0\right) .
\]

La fonction \( F \) est paire, ce résultat vaut donc sur \( \rbrack - b, b\lbrack \) .

> The function \( F \) is even, so this result holds on \( \rbrack - b, b\lbrack \) .

Il nous reste à montrer le résultat pour \( f \) . Fixons \( x \in \rbrack - b, b\lbrack \) . Pour tout \( n \in \mathbb{N} \) , on écrit

> It remains for us to show the result for \( f \) . Let us fix \( x \in \rbrack - b, b\lbrack \) . For all \( n \in \mathbb{N} \) , we write

\[
f\left( x\right)  = f\left( 0\right)  + \cdots  + \frac{{x}^{{2n} + 1}}{\left( {{2n} + 1}\right) !}{f}^{\left( 2n + 1\right) }\left( 0\right)  + {r}_{n}\left( x\right) \;\text{ avec }\;{r}_{n}\left( x\right)  = {\int }_{0}^{x}\frac{{\left( x - t\right) }^{{2n} + 1}}{\left( {{2n} + 1}\right) !}{f}^{\left( 2n + 2\right) }\left( t\right) {dt}.
\]

Comme \( 0 \leq {f}^{\left( 2n + 2\right) }\left( t\right) \leq {f}^{\left( 2n + 2\right) }\left( t\right) + {f}^{\left( 2n + 2\right) }\left( {-t}\right) = {F}^{\left( 2n + 2\right) }\left( t\right) \) pour tout \( t \) , on a \( \left| {{r}_{n}\left( x\right) }\right| \leq {R}_{n}\left( \left| x\right| \right) \) donc \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{r}_{n}\left( x\right) = 0 \) . Ainsi, en notant

> Since \( 0 \leq {f}^{\left( 2n + 2\right) }\left( t\right) \leq {f}^{\left( 2n + 2\right) }\left( t\right) + {f}^{\left( 2n + 2\right) }\left( {-t}\right) = {F}^{\left( 2n + 2\right) }\left( t\right) \) for all \( t \) , we have \( \left| {{r}_{n}\left( x\right) }\right| \leq {R}_{n}\left( \left| x\right| \right) \) so \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{r}_{n}\left( x\right) = 0 \) . Thus, by noting

\[
\forall p \in  \mathbb{N},\;{S}_{p}\left( x\right)  = \mathop{\sum }\limits_{{k = 0}}^{p}\frac{{x}^{k}}{k!}{f}^{\left( k\right) }\left( 0\right) ,
\]

nous venons de montrer que

> we have just shown that

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}{S}_{{2n} + 1}\left( x\right)  = f\left( x\right)
\]

(*)

> Or

\[
{S}_{2n}\left( x\right)  - {S}_{{2n} - 1}\left( x\right)  = \frac{{x}^{2n}}{\left( {2n}\right) !}{f}^{\left( 2n\right) }\left( 0\right)  = \frac{1}{2}\frac{{x}^{2n}}{\left( {2n}\right) !}{F}^{\left( 2n\right) }\left( 0\right) \;\text{ donc }\;\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{S}_{2n}\left( x\right)  - {S}_{{2n} - 1}\left( x\right)  = 0,
\]

et on en déduit avec (*) que \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{2n}\left( x\right) = f\left( x\right) \) . Donc d’après (*), on a \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{S}_{n}\left( x\right) = \; f\left( x\right) \) c’est-à-dire

> and we deduce from (*) that \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{S}_{2n}\left( x\right) = f\left( x\right) \) . Therefore, according to (*), we have \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{S}_{n}\left( x\right) = \; f\left( x\right) \) that is to say

\[
\forall x \in  \rbrack  - b, b\lbrack ,\;f\left( x\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{f}^{\left( n\right) }\left( 0\right) }{n!}{x}^{n}.
\]

D'où le résultat.

> Hence the result.

Remarque. Considérons la fonction \( f : \rbrack - \pi /2,\pi /2\lbrack \rightarrow \mathbb{R}\;x \mapsto \tan x \) . La fonction \( {f}^{\prime } \) satisfait les hypothèses précédentes comme on le vérifie facilement, et on en déduit que \( {f}^{\prime } \) , donc \( f \) , est développable en série entière sur \( \rbrack - \pi /2,\pi /2\lbrack \) .

> Remark. Consider the function \( f : \rbrack - \pi /2,\pi /2\lbrack \rightarrow \mathbb{R}\;x \mapsto \tan x \). The function \( {f}^{\prime } \) satisfies the previous hypotheses as is easily verified, and we deduce that \( {f}^{\prime } \), and therefore \( f \), can be expanded as a power series on \( \rbrack - \pi /2,\pi /2\lbrack \).

EXERCICE 9 (INVERSE D'UNE SÉRIE ENTIERE). Soit \( 1 + \mathop{\sum }\limits_{{n \geq 1}}{a}_{n}{z}^{n} \) une série entière de rayon de convergence non nul, et \( S \) la somme de cette série entière sur son disque de convergence. Montrer que \( 1/S \) est développable en série entière autour de l’origine.

> EXERCISE 9 (INVERSE OF A POWER SERIES). Let \( 1 + \mathop{\sum }\limits_{{n \geq 1}}{a}_{n}{z}^{n} \) be a power series with a non-zero radius of convergence, and \( S \) be the sum of this power series on its disk of convergence. Show that \( 1/S \) can be expanded as a power series around the origin.

Solution. Commençons par montrer le lemme suivant.

> Solution. Let us begin by proving the following lemma.

LEMME 1. Une série entière \( \sum {u}_{n}{z}^{n} \) a un rayon de convergence non nul si et seulement s’il existe \( q > 0 \) tel que \( \left| {u}_{n}\right| \leq {q}^{n} \) pour tout \( n \in {\mathbb{N}}^{ * } \) .

> LEMMA 1. A power series \( \sum {u}_{n}{z}^{n} \) has a non-zero radius of convergence if and only if there exists \( q > 0 \) such that \( \left| {u}_{n}\right| \leq {q}^{n} \) for all \( n \in {\mathbb{N}}^{ * } \).

En effet :

> Indeed:

Condition nécessaire. Notons \( r \) le rayon de convergence de \( \sum {u}_{n}{z}^{n} \) . Soit \( {r}^{\prime } \) tel que \( 0 < {r}^{\prime } < r \) . On a \( {u}_{n}{r}^{\prime n} \rightarrow 0 \) , donc il existe \( M \geq 1 \) tel que \( \left| {{u}_{n}{r}^{\prime n}}\right| \leq M \) pour tout \( n \in {\mathbb{N}}^{ * } \) , donc

> Necessary condition. Let \( r \) be the radius of convergence of \( \sum {u}_{n}{z}^{n} \). Let \( {r}^{\prime } \) be such that \( 0 < {r}^{\prime } < r \). We have \( {u}_{n}{r}^{\prime n} \rightarrow 0 \), so there exists \( M \geq 1 \) such that \( \left| {{u}_{n}{r}^{\prime n}}\right| \leq M \) for all \( n \in {\mathbb{N}}^{ * } \), therefore

\[
\forall n \in  {\mathbb{N}}^{ * },\;\left| {u}_{n}\right|  \leq  M{\left( \frac{1}{{r}^{\prime }}\right) }^{n} \leq  {q}^{n}\;\text{ avec }\;q = \frac{M}{{r}^{\prime }}.
\]

Condition suffisante. La suite \( \left| {{u}_{n}{\left( 1/q\right) }^{n}}\right| \) est bornée d’après les hypothèses donc le rayon de convergence de \( \sum {u}_{n}{z}^{n} \) est supérieur à \( 1/q \) , d’où le résultat.

> Sufficient condition. The sequence \( \left| {{u}_{n}{\left( 1/q\right) }^{n}}\right| \) is bounded according to the hypotheses, so the radius of convergence of \( \sum {u}_{n}{z}^{n} \) is greater than \( 1/q \), hence the result.

Résolvons maintenant l’exercice. L’hypothétique développement en série entière \( \sum {b}_{n}{z}^{n} \) vérifie, s'il existe

> Let us now solve the exercise. The hypothetical power series expansion \( \sum {b}_{n}{z}^{n} \) satisfies, if it exists

\[
\left( {1 + \mathop{\sum }\limits_{{n = 1}}^{{+\infty }}{a}_{n}{z}^{n}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{b}_{n}{z}^{n}}\right)  = 1,
\]

(*)

> donc par un produit de Cauchy

therefore by a Cauchy product

\[
{b}_{0} = 1,\;\forall n \in  {\mathbb{N}}^{ * },\;{b}_{n} =  - {a}_{1}{b}_{n - 1} - \cdots  - {a}_{n - 1}{b}_{1} - {a}_{n}{b}_{0}.
\]

Définissons \( \left( {b}_{n}\right) \) comme l’unique suite vérifiant ces récurrences. D’après le lemme précédent, il existe \( q > 0 \) tel que \( \left| {a}_{n}\right| \leq {q}^{n} \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Posons \( r = {2q} \) . On va montrer par récurrence sur \( n \) que \( \left| {b}_{n}\right| \leq {r}^{n} \) pour tout \( n \) . Pour \( n = 0 \) c’est vrai car \( {b}_{0} = 1 \) , et pour passer du rang \( n - 1 \) au rang \( n \) , on écrit

> Define \( \left( {b}_{n}\right) \) as the unique sequence satisfying these recurrences. According to the previous lemma, there exists \( q > 0 \) such that \( \left| {a}_{n}\right| \leq {q}^{n} \) for all \( n \in {\mathbb{N}}^{ * } \). Let \( r = {2q} \). We will show by induction on \( n \) that \( \left| {b}_{n}\right| \leq {r}^{n} \) for all \( n \). For \( n = 0 \) it is true because \( {b}_{0} = 1 \), and to move from rank \( n - 1 \) to rank \( n \), we write

\[
\left| {b}_{n}\right|  \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\left| {a}_{k}\right| \left| {b}_{n - k}\right|  \leq  \mathop{\sum }\limits_{{k = 1}}^{n}{q}^{k}{r}^{n - k} = \mathop{\sum }\limits_{{k = 1}}^{n}\frac{1}{{2}^{k}}{r}^{n} \leq  {r}^{n}.
\]

Ainsi, \( \sum {b}_{n}{z}^{n} \) a un rayon de convergence non nul d’après le lemme. Les relations vérifiées par \( \left( {b}_{n}\right) \) montrent que sur l’intersection des disques de convergence, l’égalité (*) est bien vérifiée, d'où le résultat.

> Thus, \( \sum {b}_{n}{z}^{n} \) has a non-zero radius of convergence according to the lemma. The relations satisfied by \( \left( {b}_{n}\right) \) show that on the intersection of the disks of convergence, the equality (*) is indeed satisfied, hence the result.

Remarque. Si \( S \) s’annule, on peut montrer que le rayon de convergence du développement en série entière de \( 1/S \) est égal au plus petit des modules des zéros de \( S \) . N’essayez pas de prouver ce résultat, il ne s'obtient de manière naturelle que dans le cadre général des fonctions analytiques (voir la remarque de l'exercice 13 page 265).

> Remark. If \( S \) vanishes, one can show that the radius of convergence of the power series expansion of \( 1/S \) is equal to the smallest of the moduli of the zeros of \( S \). Do not try to prove this result; it is only obtained naturally within the general framework of analytic functions (see the remark in exercise 13 on page 265).

EXERCICE 10 (THÉORÉME D'ABEL). Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence \( \geq 1 \) telle que \( \sum {a}_{n} \) converge. On note \( f \) la somme de cette série entière sur le disque unité. On fixe \( {\theta }_{0} \in \lbrack 0,\pi /2\lbrack \) et on pose

> EXERCISE 10 (ABEL'S THEOREM). Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence \( \geq 1 \) such that \( \sum {a}_{n} \) converges. Let \( f \) denote the sum of this power series on the unit disk. Fix \( {\theta }_{0} \in \lbrack 0,\pi /2\lbrack \) and let

\[
{\Delta }_{{\theta }_{0}} = \left\{  {z \in  \mathbb{C},\left| z\right|  < 1\text{ et }\exists \rho  > 0,\exists \theta  \in  \left\lbrack  {-{\theta }_{0},{\theta }_{0}}\right\rbrack  ,\;z = 1 - \rho {e}^{i\theta }}\right\}
\]

(voir la figure ci-dessous). Montrer que

> (see the figure below). Show that

\[
\mathop{\lim }\limits_{\substack{{z \rightarrow  1} \\  {z \in  {\Delta }_{{\theta }_{0}}} }}f\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}
\]

![bo_d7fjkrs91nqc73ereoog_267_559_950_427_256_0.jpg](images/gourdon_analysis_fr_en_010_bod7fjkrs91nqc73ereoog2675599504272560.jpg)

Figure 1. La région \( {\Delta }_{{\theta }_{0}} \) . L’écartement du secteur angulaire est \( 2{\theta }_{0} \) .

> Figure 1. The region \( {\Delta }_{{\theta }_{0}} \) . The angular sector width is \( 2{\theta }_{0} \) .

Solution. Notons \( S = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n},{S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) et \( {R}_{n} = S - {S}_{n} \) pour tout \( n \in \mathbb{N} \) . Pour majorer \( \left| {f\left( z\right) - S}\right| \) , on va effectuer une transformation d’Abel en écrivant \( {a}_{n} = {R}_{n - 1} - {R}_{n} \) pour tout \( n \) . Soit \( z \in {\mathbb{C}}^{ * },\left| z\right| < 1 \) . Pour tout \( N \in {\mathbb{N}}^{ * } \) , on a

> Solution. Let \( S = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n},{S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) and \( {R}_{n} = S - {S}_{n} \) for all \( n \in \mathbb{N} \) . To bound \( \left| {f\left( z\right) - S}\right| \) , we will perform an Abel transformation by writing \( {a}_{n} = {R}_{n - 1} - {R}_{n} \) for all \( n \) . Let \( z \in {\mathbb{C}}^{ * },\left| z\right| < 1 \) . For all \( N \in {\mathbb{N}}^{ * } \) , we have

\[
\left( {\mathop{\sum }\limits_{{n = 0}}^{N}{a}_{n}{z}^{n}}\right)  - {S}_{n} = \mathop{\sum }\limits_{{n = 1}}^{N}\left( {{R}_{n - 1} - {R}_{n}}\right) \left( {{z}^{n} - 1}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{N - 1}}{R}_{n}\left( {{z}^{n + 1} - 1}\right)  - \mathop{\sum }\limits_{{n = 1}}^{N}{R}_{n}\left( {{z}^{n} - 1}\right)
\]

\[
= \mathop{\sum }\limits_{{n = 0}}^{{N - 1}}{R}_{n}\left( {{z}^{n + 1} - {z}^{n}}\right)  - {R}_{N}\left( {{z}^{N} - 1}\right)  = \left( {z - 1}\right) \mathop{\sum }\limits_{{n = 0}}^{{N - 1}}{R}_{n}{z}^{n} - {R}_{N}\left( {{z}^{N} - 1}\right) ,
\]

et en faisant tendre \( N \) vers \( + \infty \) on en déduit

> and by letting \( N \) tend to \( + \infty \) we deduce

\[
f\left( z\right)  - S = \left( {z - 1}\right) \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{R}_{n}{z}^{n}.
\]

(*)

> Fixons maintenant \( \varepsilon > 0 \) , puis \( N \in \mathbb{N} \) tel que \( \left| {R}_{n}\right| < \varepsilon \) pour tout \( n > N \) . D’après (*), pour tout \( z \in \mathbb{C},\left| z\right| < 1, \)

Now fix \( \varepsilon > 0 \) , then \( N \in \mathbb{N} \) such that \( \left| {R}_{n}\right| < \varepsilon \) for all \( n > N \) . According to (*), for all \( z \in \mathbb{C},\left| z\right| < 1, \)

\[
\left| {f\left( z\right)  - S}\right|  \leq  \left| {z - 1}\right| \left| {\mathop{\sum }\limits_{{n = 0}}^{N}{R}_{n}{z}^{n}}\right|  + \varepsilon \left| {z - 1}\right| \left( {\mathop{\sum }\limits_{{n = N + 1}}^{{+\infty }}{\left| z\right| }^{n}}\right)  \leq  \left| {z - 1}\right| \left( {\mathop{\sum }\limits_{{n = 0}}^{N}\left| {R}_{n}\right| }\right)  + \varepsilon \frac{\left| z - 1\right| }{1 - \left| z\right| }\left( {* * }\right)
\]

\( \left( {* * }\right) \)

> Soit \( z \in {\Delta }_{{\theta }_{0}} \) , de sorte que \( z = 1 - \rho {e}^{i\varphi } \) avec \( \rho > 0 \) et \( \left| \varphi \right| \leq {\theta }_{0} \) . On a \( {\left| z\right| }^{2} = 1 - {2\rho }\cos \varphi + {\rho }^{2} \) , et lorsque \( \rho \leq \cos {\theta }_{0} \) on a la majoration

Let \( z \in {\Delta }_{{\theta }_{0}} \) , such that \( z = 1 - \rho {e}^{i\varphi } \) with \( \rho > 0 \) and \( \left| \varphi \right| \leq {\theta }_{0} \) . We have \( {\left| z\right| }^{2} = 1 - {2\rho }\cos \varphi + {\rho }^{2} \) , and when \( \rho \leq \cos {\theta }_{0} \) we have the bound

\[
\frac{\left| z - 1\right| }{1 - \left| z\right| } = \frac{\left| z - 1\right| }{1 - {\left| z\right| }^{2}}\left( {1 + \left| z\right| }\right)  = \frac{\rho }{{2\rho }\cos \varphi  - {\rho }^{2}}\left( {1 + \left| z\right| }\right)  \leq  \frac{2}{2\cos \varphi  - \rho } \leq  \frac{2}{2\cos {\theta }_{0} - \cos {\theta }_{0}} = \frac{2}{\cos {\theta }_{0}}.
\]

Si on choisit maintenant \( \alpha > 0 \) tel que \( \alpha \mathop{\sum }\limits_{{n = 0}}^{N}\left| {R}_{n}\right| < \varepsilon \) , on voit donc que si \( z \in {\Delta }_{{\theta }_{0}} \) et \( \left| {z - 1}\right| \leq \inf \left\{ {\alpha ,\cos {\theta }_{0}}\right\} \) la majoration (**) entraîne

> If we now choose \( \alpha > 0 \) such that \( \alpha \mathop{\sum }\limits_{{n = 0}}^{N}\left| {R}_{n}\right| < \varepsilon \) , we see that if \( z \in {\Delta }_{{\theta }_{0}} \) and \( \left| {z - 1}\right| \leq \inf \left\{ {\alpha ,\cos {\theta }_{0}}\right\} \) the bound (**) implies

\[
\left| {f\left( z\right)  - S}\right|  \leq  \varepsilon  + \varepsilon \frac{2}{\cos {\theta }_{0}} = \varepsilon \left( {1 + \frac{2}{\cos {\theta }_{0}}}\right) ,
\]

d'où le résultat.

> whence the result.

Remarque. En appliquant ce résultat à la série \( \sum {\left( -1\right) }^{n}/\left( {{2n} + 1}\right) \) , on en déduit

> Remark. By applying this result to the series \( \sum {\left( -1\right) }^{n}/\left( {{2n} + 1}\right) \) , we deduce

\[
\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{{2n} + 1} = \mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {n < 1} }}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{\left( -1\right) }^{n}}{{2n} + 1}{x}^{n} = \mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {x < 1} }}\arctan x = \arctan 1 = \frac{\pi }{4}.
\]

De même, on montrerait \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n - 1}/n = \log 2 \) .

> Similarly, one could show \( \mathop{\sum }\limits_{{n = 1}}^{\infty }{\left( -1\right) }^{n - 1}/n = \log 2 \) .

- Si la série \( \sum {a}_{n} \) converge absolument, le résultat est évident (en effet, \( \sum {a}_{n}{z}^{n} \) converge alors normalement sur \( \left| z\right|  \leq  1 \) , donc est continue sur \( \left| z\right|  \leq  1 \) , donc en 1).

> - If the series \( \sum {a}_{n} \) converges absolutely, the result is obvious (indeed, \( \sum {a}_{n}{z}^{n} \) then converges normally on \( \left| z\right|  \leq  1 \) , and is therefore continuous on \( \left| z\right|  \leq  1 \) , and thus at 1).

- La réciproque de ce théorème est fausse. Par exemple, on a

> - The converse of this theorem is false. For example, we have

\[
\mathop{\lim }\limits_{\substack{{z \rightarrow  1} \\  {\left| z\right|  < 1} }}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -1\right) }^{n}{z}^{n} = \mathop{\lim }\limits_{\substack{{z \rightarrow  1} \\  {\left| z\right|  < 1} }}\frac{1}{1 + z} = \frac{1}{2}
\]

et pourtant, \( \sum {\left( -1\right) }^{n} \) diverge. Cependant, si \( {a}_{n} = o\left( {1/n}\right) \) (voir l’exercice suivant) ou mieux, si \( {a}_{n} = O\left( {1/n}\right) \) (voir le problème 27 page 308), la réciproque est vraie.

> and yet, \( \sum {\left( -1\right) }^{n} \) diverges. However, if \( {a}_{n} = o\left( {1/n}\right) \) (see the following exercise) or better, if \( {a}_{n} = O\left( {1/n}\right) \) (see problem 27 on page 308), the converse is true.

EXERCICE 11 (THÉORÉME TAUBÉRIEN FAIBLE). Soit \( \sum {a}_{n}{z}^{n} \) une série entière de rayon de convergence 1 et \( f \) la somme de cette série entière sur le disque unité. On suppose que

> EXERCISE 11 (WEAK TAUBERIAN THEOREM). Let \( \sum {a}_{n}{z}^{n} \) be a power series with radius of convergence 1 and \( f \) be the sum of this power series on the unit disk. Suppose that

\[
\exists S \in  \mathbb{C},\;\mathop{\lim }\limits_{\substack{{x \rightarrow  1} \\  {x < 1} }}f\left( x\right)  = S.
\]

Si \( {a}_{n} = o\left( {1/n}\right) \) , montrer que \( \sum {a}_{n} \) converge et que \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n} = S \) .

> If \( {a}_{n} = o\left( {1/n}\right) \) , show that \( \sum {a}_{n} \) converges and that \( \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n} = S \) .

Solution. Pour tout \( n \in \mathbb{N} \) , on note \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) . On a

> Solution. For all \( n \in \mathbb{N} \) , let \( {S}_{n} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k} \) . We have

\[
\left. {\forall n \in  {\mathbb{N}}^{ * },\forall x \in  }\right\rbrack  0,1\left\lbrack  {,\;{S}_{n} - f\left( x\right)  = \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}\left( {1 - {x}^{k}}\right)  - \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}{a}_{k}{x}^{k}}\right.
\]

et comme \( \left( {1 - {x}^{k}}\right) = \left( {1 - x}\right) \left( {1 + x + \cdots + {x}^{k - 1}}\right) \leq k\left( {1 - x}\right) \) pour \( 0 < x < 1 \) , on en déduit

> and since \( \left( {1 - {x}^{k}}\right) = \left( {1 - x}\right) \left( {1 + x + \cdots + {x}^{k - 1}}\right) \leq k\left( {1 - x}\right) \) for \( 0 < x < 1 \) , we deduce

\[
\left| {{S}_{n} - f\left( x\right) }\right|  \leq  \left( {1 - x}\right) \mathop{\sum }\limits_{{k = 1}}^{n}k\left| {a}_{k}\right|  + \mathop{\sum }\limits_{{k = n + 1}}^{{+\infty }}\frac{k\left| {a}_{k}\right| }{n}{x}^{k} \leq  \left( {1 - x}\right) {Mn} + \frac{\mathop{\sup }\limits_{{k > n}}k\left| {a}_{k}\right| }{n\left( {1 - x}\right) },
\]

où \( M \) désigne un majorant de la suite \( \left( {k\left| {a}_{k}\right| }\right) \) (elle est bien majorée car elle tend vers 0 ). Fixons maintenant \( \varepsilon > 0 \) tel que \( \varepsilon < 1 \) . L’inégalité précédente entraîne

> where \( M \) denotes an upper bound of the sequence \( \left( {k\left| {a}_{k}\right| }\right) \) (it is indeed bounded since it tends to 0). Now let us fix \( \varepsilon > 0 \) such that \( \varepsilon < 1 \) . The previous inequality implies

\[
\forall n \in  {\mathbb{N}}^{ * },\;\left| {{S}_{n} - f\left( {1 - \frac{\varepsilon }{n}}\right) }\right|  \leq  {M\varepsilon } + \frac{\mathop{\sup }\limits_{{k > n}}k\left| {a}_{k}\right| }{\varepsilon },
\]

donc si \( {N}_{0} \) est choisi tel que \( \mathop{\sup }\limits_{{k > {N}_{0}}}k\left| {a}_{k}\right| < {\varepsilon }^{2} \) (on peut car \( \left. {k{a}_{k} \rightarrow 0}\right) \) , on en déduit

> so if \( {N}_{0} \) is chosen such that \( \mathop{\sup }\limits_{{k > {N}_{0}}}k\left| {a}_{k}\right| < {\varepsilon }^{2} \) (we can because \( \left. {k{a}_{k} \rightarrow 0}\right) \) , we deduce

\[
\forall n \geq  {N}_{0},\;\left| {{S}_{n} - f\left( {1 - \frac{\varepsilon }{n}}\right) }\right|  \leq  {M\varepsilon } + \varepsilon  = \left( {M + 1}\right) \varepsilon .
\]

D’après les hypothèses, \( f\left( x\right) \) tend vers \( S \) lorsque \( x \rightarrow {1}^{ - } \) , donc il existe \( {N}_{1} \geq {N}_{0} \) tel que \( \left| {f\left( {1 - \varepsilon /n}\right) - S}\right| < \varepsilon \) pour tout \( n \geq {N}_{1} \) . Ainsi,

> According to the hypotheses, \( f\left( x\right) \) tends to \( S \) as \( x \rightarrow {1}^{ - } \) , so there exists \( {N}_{1} \geq {N}_{0} \) such that \( \left| {f\left( {1 - \varepsilon /n}\right) - S}\right| < \varepsilon \) for all \( n \geq {N}_{1} \) . Thus,

\[
\forall n \geq  {N}_{1},\;\left| {{S}_{n} - S}\right|  \leq  \left| {{S}_{n} - f\left( {1 - \frac{\varepsilon }{n}}\right) }\right|  + \left| {f\left( {1 - \frac{\varepsilon }{n}}\right)  - S}\right|  \leq  \left( {M + 1}\right) \varepsilon  + \varepsilon  = \left( {M + 2}\right) \varepsilon .
\]

On en déduit que \( \left( {S}_{n}\right) \) converge vers \( S \) , d’où le résultat.

> We deduce that \( \left( {S}_{n}\right) \) converges to \( S \) , hence the result.

Remarque. Ce résultat est une réciproque partielle du théorème d'Abel (voir l'exercice précédent). Il reste vrai en supposant seulement \( {a}_{n} = O\left( {1/n}\right) \) (cf. problème 27 page 308).

> Remark. This result is a partial converse of Abel's theorem (see the previous exercise). It remains true by assuming only \( {a}_{n} = O\left( {1/n}\right) \) (cf. problem 27 on page 308).

EXERCICE 12. Soit \( f \) la somme d’une série entière \( \sum {a}_{n}{z}^{n} \) de rayon de convergence \( \geq 1 \) telle que \( {a}_{n} \in \mathbb{Z} \) pour tout \( n \in \mathbb{N} \) . On suppose que \( f \) est bornée sur le disque unité. Montrer que \( f \) est une fonction polynôme.

> EXERCISE 12. Let \( f \) be the sum of a power series \( \sum {a}_{n}{z}^{n} \) with radius of convergence \( \geq 1 \) such that \( {a}_{n} \in \mathbb{Z} \) for all \( n \in \mathbb{N} \) . Suppose that \( f \) is bounded on the unit disk. Show that \( f \) is a polynomial function.

Solution. Tout découle de l’égalité de Parseval qui entraîne, pour tout \( r \in \rbrack 0,1\lbrack \) , la convergence de \( \sum {\left| {a}_{n}\right| }^{2}{r}^{2n} \) et

> Solution. Everything follows from Parseval's identity, which implies, for all \( r \in \rbrack 0,1\lbrack \) , the convergence of \( \sum {\left| {a}_{n}\right| }^{2}{r}^{2n} \) and

\[
\forall r \in  \rbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left| {a}_{n}\right| }^{2}{r}^{2n} = \frac{1}{2\pi }{\int }_{0}^{2\pi }{\left| f\left( r{e}^{i\theta }\right) \right| }^{2}{d\theta }.
\]

Si \( M \) désigne un majorant de \( \left| f\right| \) sur le disque unité, on en conclut que pour tout \( N \in {\mathbb{N}}^{ * } \) ,

> If \( M \) denotes an upper bound of \( \left| f\right| \) on the unit disk, we conclude that for all \( N \in {\mathbb{N}}^{ * } \) ,

\[
\forall r \in  \rbrack 0,1\lbrack ,\;\mathop{\sum }\limits_{{n = 0}}^{N}{\left| {a}_{n}\right| }^{2}{r}^{2n} \leq  \frac{{M}^{2}}{2\pi }.
\]

En faisant \( r \rightarrow {1}^{ - } \) , on en déduit \( \mathop{\sum }\limits_{{n = 0}}^{N}{\left| {a}_{n}\right| }^{2} \leq {M}^{2}/{2\pi } \) , et ceci pour tout \( N \in {\mathbb{N}}^{ * } \) , donc la série \( \sum {\left| {a}_{n}\right| }^{2} \) est bornée, donc convergente. On en déduit que \( \left( {a}_{n}\right) \) tend vers 0, et comme les \( {a}_{n} \) sont entiers, ceci entraîne que tous les \( {a}_{n} \) sont nuls à partir d’un certain rang. D’où le résultat.

> By setting \( r \rightarrow {1}^{ - } \) , we deduce \( \mathop{\sum }\limits_{{n = 0}}^{N}{\left| {a}_{n}\right| }^{2} \leq {M}^{2}/{2\pi } \) , and this for all \( N \in {\mathbb{N}}^{ * } \) , so the series \( \sum {\left| {a}_{n}\right| }^{2} \) is bounded, therefore convergent. We deduce that \( \left( {a}_{n}\right) \) tends to 0, and since the \( {a}_{n} \) are integers, this implies that all \( {a}_{n} \) are zero from a certain rank onwards. Hence the result.

EXERCICE 13. Pour tout \( r \in \rbrack 0, + \infty \rbrack \) , on note \( D\left( r\right) = \{ z \in \mathbb{C}\left| \right| z \mid < r\} \) . Soit \( R \in \rbrack 0, + \infty \rbrack \) et \( f : D\left( R\right) \rightarrow \mathbb{C} \) une application dérivable par rapport à la variable complexe sur \( D\left( R\right) \) et telle que \( {f}^{\prime }\left( z\right) \) soit continue sur \( D\left( R\right) \) (on rappelle que \( f \) est dérivable par rapport à la variable complexe en \( {z}_{0} \) si \( \left( {f\left( {{z}_{0} + u}\right) - f\left( {z}_{0}\right) }\right) /u \) converge lorsque \( u \in \mathbb{C} \) tend vers 0 en restant non nul ; la limite est alors notée \( \left. {{f}^{\prime }\left( {z}_{0}\right) }\right) \) .

> EXERCISE 13. For all \( r \in \rbrack 0, + \infty \rbrack \) , we denote \( D\left( r\right) = \{ z \in \mathbb{C}\left| \right| z \mid < r\} \) . Let \( R \in \rbrack 0, + \infty \rbrack \) and \( f : D\left( R\right) \rightarrow \mathbb{C} \) be a function differentiable with respect to the complex variable on \( D\left( R\right) \) and such that \( {f}^{\prime }\left( z\right) \) is continuous on \( D\left( R\right) \) (recall that \( f \) is differentiable with respect to the complex variable at \( {z}_{0} \) if \( \left( {f\left( {{z}_{0} + u}\right) - f\left( {z}_{0}\right) }\right) /u \) converges as \( u \in \mathbb{C} \) tends to 0 while remaining non-zero; the limit is then denoted \( \left. {{f}^{\prime }\left( {z}_{0}\right) }\right) \) .

1 / a) Soit \( I \) un intervalle de \( \mathbb{R} \) et \( \gamma : I \rightarrow D\left( R\right) \) une application de classe \( {\mathcal{C}}^{1} \) . Montrer que \( f \circ \gamma \) est de classe \( {\mathcal{C}}^{1} \) sur \( I \) et calculer \( {\left( f \circ \gamma \right) }^{\prime } \) .

> 1 / a) Let \( I \) be an interval of \( \mathbb{R} \) and \( \gamma : I \rightarrow D\left( R\right) \) a function of class \( {\mathcal{C}}^{1} \) . Show that \( f \circ \gamma \) is of class \( {\mathcal{C}}^{1} \) on \( I \) and calculate \( {\left( f \circ \gamma \right) }^{\prime } \) .

b) Soit \( r > 0 \) et \( g \) une fonction définie et continue de \( \{ z \in \mathbb{C},\left| z\right| = r\} \) dans \( \mathbb{C} \) . Montrer que l'application

> b) Let \( r > 0 \) and \( g \) be a function defined and continuous from \( \{ z \in \mathbb{C},\left| z\right| = r\} \) to \( \mathbb{C} \) . Show that the mapping

\[
D\left( r\right)  \rightarrow  \mathbb{C}\;z \mapsto  \frac{r}{2\pi }{\int }_{0}^{2\pi }\frac{g\left( {r{e}^{it}}\right) {e}^{it}}{r{e}^{it} - z}{dt}
\]

est la somme d’une série entière qui converge sur \( D\left( r\right) \) .

> is the sum of a power series that converges on \( D\left( r\right) \) .

2 / Montrer que

> 2 / Show that

\[
\forall r \in  \rbrack 0, R\lbrack ,\forall z \in  D\left( r\right) ,\;f\left( z\right)  = \frac{r}{2\pi }{\int }_{0}^{2\pi }\frac{f\left( {r{e}^{it}}\right) {e}^{it}}{r{e}^{it} - z}{dt}.
\]

\( \left( *\right) \)

> En déduire que \( f \) est la somme d’une série entière qui converge sur \( D\left( R\right) \) (Indication : montrer que la fonction \( \lambda \mapsto \frac{r}{2\pi }{\int }_{0}^{2\pi }\frac{f\left( {z + \lambda \left( {r{e}^{it} - z}\right) }\right) {e}^{it}}{r{e}^{it} - z}{dt} \) est constante sur \( \left\lbrack {0,1}\right\rbrack ) \) .

Deduce that \( f \) is the sum of a power series that converges on \( D\left( R\right) \) (Hint: show that the function \( \lambda \mapsto \frac{r}{2\pi }{\int }_{0}^{2\pi }\frac{f\left( {z + \lambda \left( {r{e}^{it} - z}\right) }\right) {e}^{it}}{r{e}^{it} - z}{dt} \) is constant on \( \left\lbrack {0,1}\right\rbrack ) \) .

> Solution. 1/ a) On procède comme pour la dérivation par rapport à la variable réelle. Soit \( t \in I \) . La fonction \( f \) est dérivable par rapport à la variable complexe en \( \gamma \left( t\right) \) , ce qui s’écrit

Solution. 1/ a) We proceed as for differentiation with respect to the real variable. Let \( t \in I \) . The function \( f \) is differentiable with respect to the complex variable at \( \gamma \left( t\right) \) , which is written

\[
f\left( {\gamma \left( t\right)  + u}\right)  = f\left( {\gamma \left( t\right) }\right)  + u{f}^{\prime }\left( {\gamma \left( t\right) }\right)  + o\left( u\right) \;\text{ lorsque }\;u \rightarrow  0\left( {u \in  \mathbb{C}}\right) .
\]

On en conclut que lorsque \( v \) est un nombre réel tendant vers 0

> We conclude that when \( v \) is a real number tending to 0

\[
f\left( {\gamma \left( {t + v}\right) }\right)  = f\left( {\gamma \left( t\right)  + v{\gamma }^{\prime }\left( t\right)  + o\left( v\right) }\right)  = f\left( {\gamma \left( t\right) }\right)  + \left( {v{\gamma }^{\prime }\left( t\right)  + o\left( v\right) }\right) {f}^{\prime }\left( {\gamma \left( t\right) }\right)  + o\left( v\right)
\]

\[
= f\left( {\gamma \left( t\right) }\right)  + v{\gamma }^{\prime }\left( t\right) {f}^{\prime }\left( {\gamma \left( t\right) }\right)  + o\left( v\right) ,
\]

donc \( f \circ \gamma \) est dérivable en \( t \) et \( {\left( f \circ \gamma \right) }^{\prime }\left( t\right) = {\gamma }^{\prime }\left( t\right) {f}^{\prime }\left( {\gamma \left( t\right) }\right) \) . On déduit de cette dernière expression que \( {\left( f \circ \gamma \right) }^{\prime } \) est continue, donc \( f \circ \gamma \) est de classe \( {\mathcal{C}}^{1} \) .

> therefore \( f \circ \gamma \) is differentiable at \( t \) and \( {\left( f \circ \gamma \right) }^{\prime }\left( t\right) = {\gamma }^{\prime }\left( t\right) {f}^{\prime }\left( {\gamma \left( t\right) }\right) \) . We deduce from this last expression that \( {\left( f \circ \gamma \right) }^{\prime } \) is continuous, therefore \( f \circ \gamma \) is of class \( {\mathcal{C}}^{1} \) .

b) Il suffit d’écrire que pour tout \( z \in D\left( r\right) \) on a

> b) It suffices to write that for all \( z \in D\left( r\right) \) we have

\[
\frac{1}{2\pi }{\int }_{0}^{2\pi }\frac{g\left( {r{e}^{it}}\right) }{1 - z/\left( {r{e}^{it}}\right) }{dt} = \frac{1}{2\pi }{\int }_{0}^{2\pi }g\left( {r{e}^{it}}\right) \left( {\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\frac{{z}^{n}}{{r}^{n}}{e}^{-{int}}}\right) {dt}
\]

\[
= \frac{1}{2\pi }\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{z}^{n}\left( {\frac{1}{{r}^{n}}{\int }_{0}^{2\pi }g\left( {r{e}^{it}}\right) {e}^{-{int}}{dt}}\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{a}_{n}{z}^{n},\;{a}_{n} = \frac{1}{{2\pi }{r}^{n}}{\int }_{0}^{2\pi }g\left( {r{e}^{it}}\right) {e}^{-{int}}{dt}
\]

\( \left( {* * }\right) \)

> où le coefficient \( {a}_{n} \) est indépendant de \( z \) . On a bien le droit d’échanger les signes de sommation car si \( \left| z\right| < r \) , la série de fonctions \( \sum g\left( {r{e}^{it}}\right) \left( {{z}^{n}/{r}^{n}}\right) {e}^{-{int}} \) (de la variable \( t \) ) converge normalement sur \( \left\lbrack {0,{2\pi }}\right\rbrack \) puisque \( g \) est continue, donc bornée, sur le compact \( \left| z\right| = r \) .

where the coefficient \( {a}_{n} \) is independent of \( z \) . We are indeed allowed to exchange the summation signs because if \( \left| z\right| < r \) , the series of functions \( \sum g\left( {r{e}^{it}}\right) \left( {{z}^{n}/{r}^{n}}\right) {e}^{-{int}} \) (of the variable \( t \) ) converges normally on \( \left\lbrack {0,{2\pi }}\right\rbrack \) since \( g \) is continuous, and therefore bounded, on the compact \( \left| z\right| = r \) .

> 2/ Montrons (*). Fixons \( r \in \rbrack 0, R\lbrack \) et \( z \in D\left( r\right) \) . On considère la fonction

2/ Let us show (*). Fix \( r \in \rbrack 0, R\lbrack \) and \( z \in D\left( r\right) \) . Consider the function

\[
\varphi  : \left\lbrack  {0,1}\right\rbrack   \rightarrow  \mathbb{C}\;\lambda  \mapsto  \frac{r}{2\pi }{\int }_{0}^{2\pi }\frac{f\left( {z + \lambda \left( {r{e}^{it} - z}\right) }\right) {e}^{it}}{r{e}^{it} - z}{dt}.
\]

Il s’agit de montrer que \( \varphi \left( 1\right) = f\left( z\right) \) . La valeur \( \varphi \left( 0\right) \) est un cas particulier de la formule (**) lorsque \( t \mapsto g\left( {r{e}^{it}}\right) \) est la fonction constante égale à \( f\left( z\right) \) , donc

> It is a matter of showing that \( \varphi \left( 1\right) = f\left( z\right) \) . The value \( \varphi \left( 0\right) \) is a special case of the formula (**) when \( t \mapsto g\left( {r{e}^{it}}\right) \) is the constant function equal to \( f\left( z\right) \) , therefore

\[
\varphi \left( 0\right)  = \frac{r}{2\pi }f\left( z\right) {\int }_{0}^{2\pi }\frac{f\left( z\right) {e}^{it}}{r{e}^{it} - z}{dt} = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}\left( {\frac{f\left( z\right) }{{2\pi }{r}^{n}}{\int }_{0}^{2\pi }{e}^{-{int}}{dt}}\right) {z}^{n} = f\left( z\right) ,
\]

car \( {\int }_{0}^{2\pi }{e}^{-{int}}{dt} = 0 \) si \( n \neq 0 \) ,égal à \( {2\pi } \) si \( n = 0 \) . Il faut donc montrer \( \varphi \left( 0\right) = \varphi \left( 1\right) \) . D’après la question \( 1/\mathrm{a}),\varphi \) est dérivable et

> because \( {\int }_{0}^{2\pi }{e}^{-{int}}{dt} = 0 \) if \( n \neq 0 \) , equal to \( {2\pi } \) if \( n = 0 \) . It is therefore necessary to show \( \varphi \left( 0\right) = \varphi \left( 1\right) \) . According to question \( 1/\mathrm{a}),\varphi \) is differentiable and

\[
\forall \lambda  \in  \left\lbrack  {0,1}\right\rbrack  ,\;{\varphi }^{\prime }\left( \lambda \right)  = \frac{r}{2\pi }{\int }_{0}^{2\pi }{f}^{\prime }\left( {z + \lambda \left( {r{e}^{it} - z}\right) }\right) {e}^{it}{dt}.
\]

(***)

> Or, toujours d'après la question a), on a

However, still according to question a), we have

\[
\frac{\partial }{\partial t}\left( {f\left( {z + \lambda \left( {r{e}^{it} - z}\right) }\right)  = {i\lambda r}{e}^{it}{f}^{\prime }\left( {z + \lambda \left( {r{e}^{it} - z}\right) }\right) ,}\right.
\]

donc d'après (***)

> therefore according to (***)

\[
\forall \lambda ,0 < \lambda  < 1,\;{\varphi }^{\prime }\left( \lambda \right)  = \frac{1}{2\pi i\lambda }{\left\lbrack  f\left( z + \lambda \left( r{e}^{it} - z\right) \right) \right\rbrack  }_{0}^{2\pi } = 0.
\]

Ainsi, \( \varphi \) est constante donc \( \varphi \left( 0\right) = \varphi \left( 1\right) \) , d’où (*).

> Thus, \( \varphi \) is constant therefore \( \varphi \left( 0\right) = \varphi \left( 1\right) \) , hence (*).

La fonction \( f \) est continue sur \( \left| z\right| = r \) car elle y est dérivable par rapport à la variable complexe. Grâce à (*) et à 1/b), on en déduit que pour tout \( r \in \rbrack 0, R\lbrack , f \) est la somme d’une série entière \( \sum {a}_{n}{z}^{n} \) sur \( D\left( r\right) \) . Or les coefficients \( {a}_{n} \) ne dépendent pas de \( r \) (ce sont les \( {f}^{\left( n\right) }\left( 0\right) /n! \) ). Ce développement en série entière est donc valable sur \( D\left( R\right) \) tout entier.

> The function \( f \) is continuous on \( \left| z\right| = r \) because it is differentiable there with respect to the complex variable. Thanks to (*) and 1/b), we deduce that for all \( r \in \rbrack 0, R\lbrack , f \) is the sum of a power series \( \sum {a}_{n}{z}^{n} \) on \( D\left( r\right) \). However, the coefficients \( {a}_{n} \) do not depend on \( r \) (they are the \( {f}^{\left( n\right) }\left( 0\right) /n! \)). This power series expansion is therefore valid on the entirety of \( D\left( R\right) \).

Remarque. (Petite digression sur les fonctions analytiques.) Les séries entières rentrent dans le contexte plus général de l'élégante théorie des fonctions analytiques.

> Remark. (A brief digression on analytic functions.) Power series fall within the more general context of the elegant theory of analytic functions.

DéFINITION 1. Une fonction \( f : \Omega \rightarrow \mathbb{C} \) (où \( \Omega \) est un ouvert de \( \mathbb{C} \) ) est dite analytique dans \( \Omega \) si pour tout \( {z}_{0} \in \Omega \) , il existe un disque ouvert \( \Delta : \left| {z - {z}_{0}}\right| < r \) contenu dans \( \Omega \) tel que

> DEFINITION 1. A function \( f : \Omega \rightarrow \mathbb{C} \) (where \( \Omega \) is an open set of \( \mathbb{C} \)) is said to be analytic in \( \Omega \) if for every \( {z}_{0} \in \Omega \), there exists an open disk \( \Delta : \left| {z - {z}_{0}}\right| < r \) contained in \( \Omega \) such that

\[
\forall z \in  \Delta ,\;f\left( z\right)  = \mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{c}_{n}{\left( z - {z}_{0}\right) }^{n},
\]

où le second membre est une série entière en \( z - {z}_{0} \) convergente dans \( \Delta \) .

> where the second member is a power series in \( z - {z}_{0} \) convergent in \( \Delta \).

Elle est dite holomorphe dans \( \Omega \) si elle est continûment dérivable par rapport à la variable complexe dans \( \Omega \) .

> It is said to be holomorphic in \( \Omega \) if it is continuously differentiable with respect to the complex variable in \( \Omega \).

Par exemple, la fonction \( f : z \rightarrow 1/z \) est analytique dans \( {\mathbb{C}}^{ * } \) . En effet, pour tout \( {z}_{0} \in {\mathbb{C}}^{ * } \) , et pour tout \( z \) que \( \left| {z - {z}_{0}}\right| < \left| {z}_{0}\right| \) , on a

> For example, the function \( f : z \rightarrow 1/z \) is analytic in \( {\mathbb{C}}^{ * } \). Indeed, for every \( {z}_{0} \in {\mathbb{C}}^{ * } \), and for every \( z \) such that \( \left| {z - {z}_{0}}\right| < \left| {z}_{0}\right| \), we have

\[
f\left( z\right)  = \frac{1}{{z}_{0}}\frac{1}{1 + \left( {z - {z}_{0}}\right) /{z}_{0}} = \frac{1}{{z}_{0}}\mathop{\sum }\limits_{{n = 0}}^{{+\infty }}{\left( -\frac{1}{{z}_{0}}\right) }^{n}{\left( z - {z}_{0}\right) }^{n}.
\]

Le résultat de l’exercice montre que toute fonction \( f \) holomorphe sur un ouvert \( \Omega \) de \( \mathbb{C} \) est analytique sur \( \Omega \) . En effet, si \( {z}_{0} \in \Omega \) et si \( r > 0 \) est tel que \( D\left( {{z}_{0}, r}\right) \) (disque ouvert de centre \( {z}_{0} \) de rayon \( r \) ) vérifie \( D\left( {{z}_{0}, r}\right) \subset \Omega \) , la fonction \( g : D\left( r\right) \rightarrow \mathbb{C}\;z \mapsto f\left( {{z}_{0} + z}\right) \) est holomorphe sur \( D\left( r\right) \) donc \( g \) est développable en série entière sur \( D\left( r\right) \) d’après \( 2/ \) . Réciproquement, on montre que toute fonction analytique est holomorphe (c'est plus facile).

> The result of the exercise shows that any function \( f \) holomorphic on an open set \( \Omega \) of \( \mathbb{C} \) is analytic on \( \Omega \). Indeed, if \( {z}_{0} \in \Omega \) and if \( r > 0 \) is such that \( D\left( {{z}_{0}, r}\right) \) (open disk centered at \( {z}_{0} \) with radius \( r \)) satisfies \( D\left( {{z}_{0}, r}\right) \subset \Omega \), the function \( g : D\left( r\right) \rightarrow \mathbb{C}\;z \mapsto f\left( {{z}_{0} + z}\right) \) is holomorphic on \( D\left( r\right) \), therefore \( g \) can be expanded as a power series on \( D\left( r\right) \) according to \( 2/ \). Conversely, it can be shown that any analytic function is holomorphic (this is easier).

En particulier, la somme d'une série entière est analytique sur son disque de convergence (résultat non évident a priori).

> In particular, the sum of a power series is analytic on its disk of convergence (a result not obvious a priori).

On montre facilement que la composée de deux fonctions holomorphes est holomorphe. En particulier, si \( f \) est la somme d’une série entière qui converge dans un disque \( D\left( r\right) \) et ne s’y annule pas, alors \( 1/f \) est holomorphe dans \( D\left( r\right) \) , donc développable en série entière sur \( D\left( r\right) \) d’après le résultat de l’exercice. On obtient ainsi une version plus forte que celle obtenue à l'exercice 9 page 262, car on a des renseignements sur le rayon de convergence \( r \) de l’inverse ( \( r \) est le plus petit des modules des zéros de \( f \) ).

> It is easily shown that the composition of two holomorphic functions is holomorphic. In particular, if \( f \) is the sum of a power series that converges in a disk \( D\left( r\right) \) and does not vanish there, then \( 1/f \) is holomorphic in \( D\left( r\right) \), and therefore can be expanded as a power series on \( D\left( r\right) \) according to the result of the exercise. We thus obtain a stronger version than the one obtained in exercise 9 on page 262, because we have information about the radius of convergence \( r \) of the inverse (\( r \) is the smallest of the moduli of the zeros of \( f \)).
