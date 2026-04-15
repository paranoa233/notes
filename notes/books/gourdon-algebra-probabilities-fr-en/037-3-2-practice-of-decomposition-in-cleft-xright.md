#### 3.2. Practice of decomposition in \( \mathbb{C}\left( X\right) \)

*Français : 3.2. Pratique de la décomposition dans \( \mathbb{C}\left( X\right) \)*

Il est indispensable de bien savoir décomposer en éléments simples (on s'en sert en particulier pour le calcul de primitives de fractions rationnelles).

> It is essential to be proficient in partial fraction decomposition (it is used in particular for calculating primitives of rational fractions).

Soit \( F \in \mathbb{C}\left( X\right) , F \neq 0 \) , de forme réduite \( N/D \) . Le corps \( \mathbb{C} \) étant algébriquement clos, on peut écrire \( D = {\left( X - {a}_{1}\right) }^{{\alpha }_{1}}\cdots {\left( X - {a}_{n}\right) }^{{\alpha }_{n}} \) avec \( {a}_{i} \in \mathbb{C} \) pour tout \( i \) et \( {\alpha }_{i} \in {\mathbb{N}}^{ * } \) . Appliquant le théorème précédent, on voit que l'on peut écrire de manière unique

> Let \( F \in \mathbb{C}\left( X\right) , F \neq 0 \) be in reduced form \( N/D \) . Since the field \( \mathbb{C} \) is algebraically closed, we can write \( D = {\left( X - {a}_{1}\right) }^{{\alpha }_{1}}\cdots {\left( X - {a}_{n}\right) }^{{\alpha }_{n}} \) with \( {a}_{i} \in \mathbb{C} \) for all \( i \) and \( {\alpha }_{i} \in {\mathbb{N}}^{ * } \) . Applying the previous theorem, we see that it can be written uniquely

\[
F = E + \mathop{\sum }\limits_{{i = 1}}^{n}\left( {\mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{a}_{i, j}}{{\left( X - {a}_{i}\right) }^{j}}}\right) \;\text{ avec }\;{a}_{i, j} \in  \mathbb{C}\text{ et }E \in  \mathbb{C}\left\lbrack  X\right\rbrack  .
\]

Nous avons déjà vu plus haut que \( E \) s’obtient comme le quotient de la division euclidienne de \( N \) par \( D \) . Pour tout \( i \) , le terme \( \mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{a}_{i, j}}{{\left( X - {a}_{i}\right) }^{j}} \) s’appelle partie principale de \( F \) relative au pôle \( {a}_{i} \) . Nous allons donner des méthodes pratiques de calcul des \( {a}_{i, j} \) .

> We have already seen above that \( E \) is obtained as the quotient of the Euclidean division of \( N \) by \( D \) . For any \( i \) , the term \( \mathop{\sum }\limits_{{j = 1}}^{{\alpha }_{i}}\frac{{a}_{i, j}}{{\left( X - {a}_{i}\right) }^{j}} \) is called the principal part of \( F \) relative to the pole \( {a}_{i} \) . We will provide practical methods for calculating \( {a}_{i, j} \) .

Partie principale relative à un pôle simple. Soit \( F \in \mathbb{C}\left( X\right) , F \neq 0, N/D \) sa forme réduite. Soit \( a \) un pôle simple de \( F \) . La partie principale de \( F \) relative à \( a \) est de la forme \( \frac{\lambda }{X - a} \) avec \( \lambda \in \mathbb{C} \) , et on peut écrire \( F = \frac{N}{D} = \frac{\lambda }{X - a} + G \) avec \( G \in \mathbb{C}\left( X\right) \) , a n’étant pas un pôle de \( G \) . On peut également écrire \( D = \left( {X - a}\right) {D}_{1} \) avec \( {D}_{1} \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( {D}_{1}\left( a\right) \neq 0 \) , de sorte que

> Principal part relative to a simple pole. Let \( F \in \mathbb{C}\left( X\right) , F \neq 0, N/D \) be its reduced form. Let \( a \) be a simple pole of \( F \) . The principal part of \( F \) relative to \( a \) is of the form \( \frac{\lambda }{X - a} \) with \( \lambda \in \mathbb{C} \) , and we can write \( F = \frac{N}{D} = \frac{\lambda }{X - a} + G \) with \( G \in \mathbb{C}\left( X\right) \) , where a is not a pole of \( G \) . We can also write \( D = \left( {X - a}\right) {D}_{1} \) with \( {D}_{1} \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( {D}_{1}\left( a\right) \neq 0 \) , such that

\[
\frac{N}{{D}_{1}} = \lambda  + \left( {X - a}\right) G\;\text{ donc }\;\lambda  = \frac{N\left( a\right) }{{D}_{1}\left( a\right) }.
\]

(*)

> Par ailleurs, l’égalité \( {D}^{\prime } = {D}_{1} + \left( {X - a}\right) {D}_{1}^{\prime } \) donne \( {D}^{\prime }\left( a\right) = {D}_{1}\left( a\right) \) , ce qui donne un autre moyen de calculer \( \lambda \) :

Furthermore, the equality \( {D}^{\prime } = {D}_{1} + \left( {X - a}\right) {D}_{1}^{\prime } \) gives \( {D}^{\prime }\left( a\right) = {D}_{1}\left( a\right) \) , which provides another way to calculate \( \lambda \) :

\[
\lambda  = \frac{N\left( a\right) }{{D}^{\prime }\left( a\right) }
\]

\( \left( {* * }\right) \)

> Remarque 1. \( \left( *\right) \) et \( \left( {* * }\right) \) s’utilisent dans des circonstances différentes : \( \left( *\right) \) quand on connaît une forme explicite de \( {D}_{1},\left( {* * }\right) \) sinon (voir les exemples qui suivent).

Remark 1. \( \left( *\right) \) and \( \left( {* * }\right) \) are used in different circumstances: \( \left( *\right) \) when an explicit form of \( {D}_{1},\left( {* * }\right) \) is known, otherwise (see the examples that follow).

> Exemple 1. - Soit \( F = \frac{X + 3}{\left( {X - 1}\right) \left( {X + 2}\right) } \) , et \( F = \frac{a}{X - 1} + \frac{b}{X + 2} \) sa décomposition en éléments simples. Grâce à \( \left( *\right) \) , on trouve \( a = 4/3 \) et \( b = - 1/3 \) .

Example 1. - Let \( F = \frac{X + 3}{\left( {X - 1}\right) \left( {X + 2}\right) } \) , and \( F = \frac{a}{X - 1} + \frac{b}{X + 2} \) be its partial fraction decomposition. Thanks to \( \left( *\right) \) , we find \( a = 4/3 \) and \( b = - 1/3 \) .

> - Soit \( F = \frac{P}{{X}^{n} - 1} \) , avec \( P \in  \mathbb{C}\left\lbrack  X\right\rbrack  ,\deg \left( P\right)  < n \) . Notons \( \omega  = {e}^{{2i\pi }/n} \) . On a \( {X}^{n} - 1 = \; \mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {X - {\omega }^{k}}\right) \) , donc \( F = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{{a}_{k}}{X - {\omega }^{k}},{a}_{k} \in  \mathbb{C} \) . Grâce à \( \left( {* * }\right) \) , on trouve

- Let \( F = \frac{P}{{X}^{n} - 1} \) , with \( P \in  \mathbb{C}\left\lbrack  X\right\rbrack  ,\deg \left( P\right)  < n \) . Let \( \omega  = {e}^{{2i\pi }/n} \) . We have \( {X}^{n} - 1 = \; \mathop{\prod }\limits_{{k = 0}}^{{n - 1}}\left( {X - {\omega }^{k}}\right) \) , so \( F = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{{a}_{k}}{X - {\omega }^{k}},{a}_{k} \in  \mathbb{C} \) . Thanks to \( \left( {* * }\right) \) , we find

\[
{a}_{k} = \frac{P\left( {\omega }^{k}\right) }{n{\left( {\omega }^{k}\right) }^{n - 1}} = \frac{{\omega }^{k}}{n}P\left( {\omega }^{k}\right) ,\;\text{ donc }\;F = \frac{1}{n}\mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{{\omega }^{k}P\left( {\omega }^{k}\right) }{X - {\omega }^{k}}.
\]

Partie principale relative \( \dot{a} \) un pôle multiple. Soit \( F \in \mathbb{C}\left\lbrack X\right\rbrack , N/D \) sa forme réduite, et \( a \in \mathbb{C} \) un pôle d’ordre \( h \geq 2 \) de \( F \) . On peut écrire \( D = {\left( X - a\right) }^{h}{D}_{0} \) avec \( {D}_{0} \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( {D}_{0}\left( a\right) \neq 0 \) . Posons \( {D}_{1}\left( T\right) = {D}_{0}\left( {T + a}\right) ,{N}_{1}\left( T\right) = N\left( {T + a}\right) \) et \( {F}_{1}\left( T\right) = F\left( {T + a}\right) \) . On a \( {F}_{1}\left( T\right) = \frac{{N}_{1}\left( T\right) }{{T}^{h}{D}_{1}\left( T\right) } \) . Ainsi, si \( {N}_{1} = \left( {{a}_{h} + \cdots + {a}_{1}{T}^{h - 1}}\right) {D}_{1} + {T}^{h}S,\left( {S \in \mathbb{C}\left\lbrack X\right\rbrack }\right) \) est la division selon les puissances croissantes de \( {N}_{1} \) par \( {D}_{1} \) à l’ordre \( h - 1 \) , on a :

> Principal part relative to \( \dot{a} \) a multiple pole. Let \( F \in \mathbb{C}\left\lbrack X\right\rbrack , N/D \) be its reduced form, and \( a \in \mathbb{C} \) a pole of order \( h \geq 2 \) of \( F \) . We can write \( D = {\left( X - a\right) }^{h}{D}_{0} \) with \( {D}_{0} \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( {D}_{0}\left( a\right) \neq 0 \) . Let \( {D}_{1}\left( T\right) = {D}_{0}\left( {T + a}\right) ,{N}_{1}\left( T\right) = N\left( {T + a}\right) \) and \( {F}_{1}\left( T\right) = F\left( {T + a}\right) \) . We have \( {F}_{1}\left( T\right) = \frac{{N}_{1}\left( T\right) }{{T}^{h}{D}_{1}\left( T\right) } \) . Thus, if \( {N}_{1} = \left( {{a}_{h} + \cdots + {a}_{1}{T}^{h - 1}}\right) {D}_{1} + {T}^{h}S,\left( {S \in \mathbb{C}\left\lbrack X\right\rbrack }\right) \) is the division by increasing powers of \( {N}_{1} \) by \( {D}_{1} \) to the order \( h - 1 \) , we have:

\[
{F}_{1}\left( T\right)  = \frac{{a}_{1}}{T} + \frac{{a}_{2}}{{T}^{2}} + \cdots  + \frac{{a}_{h}}{{T}^{h}} + \frac{S\left( T\right) }{{D}_{1}\left( T\right) }
\]

et donc

> and therefore

\[
F\left( X\right)  = \frac{{a}_{1}}{X - a} + \cdots  + \frac{{a}_{h}}{{\left( X - a\right) }^{h}} + \frac{S\left( {X - a}\right) }{{D}_{0}\left( X\right) }.
\]

On a ainsi obtenu la partie principale relative au pôle \( a \) .

> We have thus obtained the principal part relative to the pole \( a \) .

Exemple 2. Recherchons la partie principale de \( F = \frac{X + 3}{{\left( X - 1\right) }^{4}\left( {X + 1}\right) } \) relative au pôle 1 d’ordre 4. On a, avec les notations précédentes, \( {N}_{1}\left( T\right) = T + 4 \) et \( {D}_{1}\left( T\right) = T + 2 \) . On effectue la division euclidienne de \( T + 4 \) par \( T + 2 \) selon les puissances croissantes à l’ordre 3, ce qui donne

> Example 2. Let us find the principal part of \( F = \frac{X + 3}{{\left( X - 1\right) }^{4}\left( {X + 1}\right) } \) relative to the pole 1 of order 4. Using the previous notation, we have \( {N}_{1}\left( T\right) = T + 4 \) and \( {D}_{1}\left( T\right) = T + 2 \) . We perform the Euclidean division of \( T + 4 \) by \( T + 2 \) in increasing powers up to order 3, which gives

\[
\begin{array}{l} 4 + T \\   - T \\  \frac{1}{2}{T}^{2} \\  \end{array}
\]

On en déduit que la partie principale de \( F \) relative au pôle 1 est

> We deduce that the principal part of \( F \) relative to the pole 1 is

\[
\frac{-1}{8\left( {X - 1}\right) } + \frac{1}{4{\left( X - 1\right) }^{2}} - \frac{1}{2{\left( X - 1\right) }^{3}} + \frac{2}{{\left( X - 1\right) }^{4}}.
\]

En pratique, on n'utilise cette méthode que si l'ordre du pôle est grand (typiquement supérieur à 3 ou 4). La plupart du temps, on procède par identification en donnant à \( X \) certaines valeurs particulières et en utilisant certaines propriétés de \( F \) comme la parité, le fait que \( F \) est à coefficients réels, et en utilisant la remarque suivante : Si a est un pôle d’ordre \( h \) de \( F \) , on peut écrire \( F = \frac{N}{{\left( X - a\right) }^{h}{D}_{0}},{D}_{0}\left( a\right) \neq 0 \) , et

> In practice, this method is only used if the order of the pole is large (typically greater than 3 or 4). Most of the time, we proceed by identification by assigning certain specific values to \( X \) and using certain properties of \( F \) such as parity, the fact that \( F \) has real coefficients, and by using the following remark: If a is a pole of order \( h \) of \( F \) , we can write \( F = \frac{N}{{\left( X - a\right) }^{h}{D}_{0}},{D}_{0}\left( a\right) \neq 0 \) , and

\[
F = \frac{{a}_{1}}{X - a} + \cdots  + \frac{{a}_{h}}{{\left( X - a\right) }^{h}} + G,
\]

\( a \) n’étant pas un pôle de \( G \) . En multipliant cette dernière égalité par \( {\left( X - a\right) }^{h} \) , on obtient

> \( a \) not being a pole of \( G \) . By multiplying this last equality by \( {\left( X - a\right) }^{h} \) , we obtain

\[
\frac{N}{{D}_{0}} = {a}_{h} + \left( {X - a}\right) \left\lbrack  {{a}_{h - 1} + \cdots  + {a}_{1}{\left( X - a\right) }^{h - 2} + {\left( X - a\right) }^{h - 1}G}\right\rbrack  .
\]

En donnant à \( X \) la valeur \( a \) , on trouve un moyen commode de calculer \( {a}_{h} \) :

> By assigning the value \( a \) to \( X \) , we find a convenient way to calculate \( {a}_{h} \) :

\[
{a}_{h} = \frac{N\left( a\right) }{{D}_{0}\left( a\right) }
\]

\( \left( {* * * }\right) \)

> Exemple 3. \( F = \frac{X + 2}{{\left( X + 1\right) }^{2}{\left( X - 2\right) }^{2}} \) se décompose en éléments simples sous la forme

Example 3. \( F = \frac{X + 2}{{\left( X + 1\right) }^{2}{\left( X - 2\right) }^{2}} \) decomposes into partial fractions in the form

\[
F = \frac{a}{X - 2} + \frac{b}{{\left( X - 2\right) }^{2}} + \frac{c}{X + 1} + \frac{d}{{\left( X + 1\right) }^{2}}.
\]

En utilisant la relation \( \left( {* * * }\right) \) , on trouve \( b = 4/9 \) et \( d = 1/9 \) .

> Using the relation \( \left( {* * * }\right) \) , we find \( b = 4/9 \) and \( d = 1/9 \) .

Par ailleurs, en multipliant \( F \) par \( X \) , en regardant \( X \) comme un nombre réel et en le faisant tendre vers \( + \infty \) , on trouve \( \left( i\right) \;0 = a + c \) . Or \( F\left( 0\right) = \frac{1}{2} = \frac{-a}{2} + \frac{b}{4} + c + d \) , donc (ii) \( \frac{5}{9} = - a + {2c} \) . De (i) et (ii), on trouve \( a = \frac{-5}{27} \) et \( c = \frac{5}{27} \) .

> Furthermore, by multiplying \( F \) by \( X \) , viewing \( X \) as a real number and letting it tend towards \( + \infty \) , we find \( \left( i\right) \;0 = a + c \) . Now \( F\left( 0\right) = \frac{1}{2} = \frac{-a}{2} + \frac{b}{4} + c + d \) , therefore (ii) \( \frac{5}{9} = - a + {2c} \) . From (i) and (ii), we find \( a = \frac{-5}{27} \) and \( c = \frac{5}{27} \) .

D’autres décompositions en éléments simples dans \( \mathbb{C}\left( X\right) \) sont traitées à l'exercice 1.

> Other partial fraction decompositions in \( \mathbb{C}\left( X\right) \) are covered in exercise 1.
