#### 3.4. Exercises

*Français : 3.4. Exercices*

EXERCICE 1. Décomposer en éléments simples dans \( \mathbb{C}\left( X\right) \) les fractions rationnelles sui-vantes :

> EXERCISE 1. Decompose the following rational fractions into partial fractions in \( \mathbb{C}\left( X\right) \):

\[
\text{ a) }F = \frac{X}{{\left( {X}^{2} - 1\right) }^{2}\left( {{X}^{2} + 1}\right) }\text{ . }
\]

b) \( F = \frac{{X}^{4}}{{X}^{5} + 1} \) .

> Solution. a) On commence par scinder le dénominateur de \( F \) dans \( \mathbb{C}\left\lbrack X\right\rbrack \) , ce qui donne

Solution. a) We begin by splitting the denominator of \( F \) in \( \mathbb{C}\left\lbrack X\right\rbrack \), which gives

\[
{\left( {X}^{2} - 1\right) }^{2}\left( {{X}^{2} + 1}\right)  = {\left( X - 1\right) }^{2}{\left( X + 1\right) }^{2}\left( {X + i}\right) \left( {X - i}\right) .
\]

On peut donc écrire

> We can therefore write

\[
F = \frac{a}{X - 1} + \frac{b}{{\left( X - 1\right) }^{2}} + \frac{{a}^{\prime }}{X + 1} + \frac{{b}^{\prime }}{{\left( X + 1\right) }^{2}} + \frac{c}{X - i} + \frac{{c}^{\prime }}{X + i},\;a, b, c,{a}^{\prime },{b}^{\prime },{c}^{\prime } \in  \mathbb{C}.
\]

Comme \( F \) est impaire, l’unicité de la décomposition de \( F \) en éléments simples permet d’identifier la décomposition de \( F\left( X\right) \) et de \( - F\left( {-X}\right) \) , ce qui donne \( a = {a}^{\prime } \) et \( b = - {b}^{\prime } \) .

> Since \( F \) is odd, the uniqueness of the partial fraction decomposition of \( F \) allows us to identify the decomposition of \( F\left( X\right) \) and \( - F\left( {-X}\right) \), which gives \( a = {a}^{\prime } \) and \( b = - {b}^{\prime } \).

De plus \( F \) est à coefficients réels, donc \( F\left( X\right) = \bar{F}\left( X\right) \) et par identification \( c = \overline{{c}^{\prime }} \) .

> Furthermore, \( F \) has real coefficients, so \( F\left( X\right) = \bar{F}\left( X\right) \) and by identification \( c = \overline{{c}^{\prime }} \).

La relation (***) de la partie 3.2 donne \( b = \frac{1}{8} \) et \( c = \frac{i}{4 \cdot {2i}} = \frac{1}{8} \) . Donc \( {b}^{\prime } = - \frac{1}{8} \) et \( {c}^{\prime } = \frac{1}{8} \) .

> Relation (***) from section 3.2 gives \( b = \frac{1}{8} \) and \( c = \frac{i}{4 \cdot {2i}} = \frac{1}{8} \). Thus \( {b}^{\prime } = - \frac{1}{8} \) and \( {c}^{\prime } = \frac{1}{8} \).

Multipliant \( F \) par \( X \) , regardant \( X \) comme un nombre réel et en le faisant tendre vers \( + \infty \) , on tire \( 0 = a + {a}^{\prime } + c + {c}^{\prime } \) . Donc \( {2a} = a + {a}^{\prime } = - \left( {{c}^{\prime } + c}\right) = - \frac{1}{4} \) , d’où \( a = {a}^{\prime } = - \frac{1}{8} \) .

> Multiplying \( F \) by \( X \), viewing \( X \) as a real number and letting it tend towards \( + \infty \), we obtain \( 0 = a + {a}^{\prime } + c + {c}^{\prime } \). Thus \( {2a} = a + {a}^{\prime } = - \left( {{c}^{\prime } + c}\right) = - \frac{1}{4} \), from which \( a = {a}^{\prime } = - \frac{1}{8} \).

b) Recherchons les racines de \( {X}^{5} + 1 \) . On a

> b) Let us find the roots of \( {X}^{5} + 1 \). We have

\[
{x}^{5} + 1 = 0 \Leftrightarrow  {x}^{5} =  - 1 = {e}^{i\pi } \Leftrightarrow  x = {e}^{i\left( {\pi /5 + {2k\pi }/5}\right) } = {\omega }_{k},\;\left( {k \in  \{ 0,1,2,3,4\} }\right) .
\]

Ainsi les \( {\left( {\omega }_{k}\right) }_{0 \leq k \leq 4} \) sont 5 racines distinctes du dénominateur de \( F \) , et comme ce dernier est de degré 5, tous les pôles de \( F \) sont simples. On obtient le coefficient de la partie principale \( {a}_{k}/\left( {X - {\omega }_{k}}\right) \) de \( F \) en utilisant l’identité (**) page 76, qui donne \( {a}_{k} = {\omega }_{k}^{4}/\left( {5{\omega }_{k}^{4}}\right) = 1/5 \) . Donc

> Thus the \( {\left( {\omega }_{k}\right) }_{0 \leq k \leq 4} \) are 5 distinct roots of the denominator of \( F \), and since the latter is of degree 5, all poles of \( F \) are simple. We obtain the coefficient of the principal part \( {a}_{k}/\left( {X - {\omega }_{k}}\right) \) of \( F \) using identity (**) on page 76, which gives \( {a}_{k} = {\omega }_{k}^{4}/\left( {5{\omega }_{k}^{4}}\right) = 1/5 \). Therefore

\[
F = \frac{1}{5}\mathop{\sum }\limits_{{k = 0}}^{4}\frac{1}{X - {\omega }_{k}}.
\]

EXERCICE 2. Décomposer en éléments simples dans \( \mathbb{R}\left( X\right) \) les fractions rationnelles sui-vantes.

> EXERCISE 2. Decompose the following rational fractions into partial fractions in \( \mathbb{R}\left( X\right) \).

\[
\text{ a) }F = \frac{{X}^{2}}{{\left( {X}^{4} + {X}^{2} + 1\right) }^{2}}\text{ . }
\]

b) \( F = \frac{1}{X{\left( {X}^{2} + 1\right) }^{2}} \) .

\[
\text{ c) }F = \frac{{X}^{7} + 2}{{\left( {X}^{2} + X + 1\right) }^{3}}\text{ . }
\]

d) \( F = \frac{1}{{X}^{2n} - 1}, n \in {\mathbb{N}}^{ * } \) .

> Solution. a) On a \( {\left( {X}^{4} + {X}^{2} + 1\right) }^{2} = {\left( {X}^{2} + X + 1\right) }^{2}{\left( {X}^{2} - X + 1\right) }^{2} \) donc

Solution. a) We have \( {\left( {X}^{4} + {X}^{2} + 1\right) }^{2} = {\left( {X}^{2} + X + 1\right) }^{2}{\left( {X}^{2} - X + 1\right) }^{2} \) therefore

> \( \exists a, b, c, d, e, f, g, h \in \mathbb{R},\;F = \frac{{aX} + b}{{X}^{2} + X + 1} + \frac{{cX} + d}{{\left( {X}^{2} + X + 1\right) }^{2}} + \frac{{eX} + f}{{X}^{2} - X + 1} + \frac{{gX} + h}{{\left( {X}^{2} - X + 1\right) }^{2}}. \)

Comme \( F \) est paire, l’unicité de la décomposition en éléments simples permet d’obtenir

> Since \( F \) is even, the uniqueness of the partial fraction decomposition allows us to obtain

\[
e =  - a,\;f = b,\;g =  - c,\;h = d.
\]

Multipliant \( F \) par \( {\left( {X}^{2} + X + 1\right) }^{2} \) puis en remplaçant \( X \) par \( j = {e}^{{2i\pi }/3} \) , on obtient

> Multiplying \( F \) by \( {\left( {X}^{2} + X + 1\right) }^{2} \) and then replacing \( X \) with \( j = {e}^{{2i\pi }/3} \), we obtain

\[
{cj} + d = \frac{{j}^{2}}{{\left( {j}^{2} - j + 1\right) }^{2}} = \frac{{j}^{2}}{4{j}^{2}} = \frac{1}{4}\;\text{ donc }\;c = 0\text{ et }d = \frac{1}{4}.
\]

On a \( F\left( 0\right) = 0 = b + d + f + h = {2b} + \frac{1}{2} \) , d’où \( b = - \frac{1}{4} \) .

> We have \( F\left( 0\right) = 0 = b + d + f + h = {2b} + \frac{1}{2} \), from which \( b = - \frac{1}{4} \).

On a \( F\left( i\right) = - 1 = \frac{{ai} + b}{i} - \left( {{ci} + d}\right) - \frac{{ei} + f}{i} - \left( {{gi} + h}\right) \) , donc -1 = 2a + \( \frac{\left( b - f\right) }{i} - i\left( {c + g}\right) - \left( {d + h}\right) = \; {2a} - {2d} = {2a} - \frac{1}{2} \) , d’où \( a = - \frac{1}{4} \) .

> We have \( F\left( i\right) = - 1 = \frac{{ai} + b}{i} - \left( {{ci} + d}\right) - \frac{{ei} + f}{i} - \left( {{gi} + h}\right) \) , so -1 = 2a + \( \frac{\left( b - f\right) }{i} - i\left( {c + g}\right) - \left( {d + h}\right) = \; {2a} - {2d} = {2a} - \frac{1}{2} \) , whence \( a = - \frac{1}{4} \) .

Finalement on a trouvé

> Finally, we have found

\[
a =  - \frac{1}{4},\;b =  - \frac{1}{4},\;c = 0,\;d = \frac{1}{4},\;e = \frac{1}{4},\;f =  - \frac{1}{4},\;g = 0,\;h = \frac{1}{4}.
\]

b) Il existe \( a, b, c, d, e \in \mathbb{R} \) tels que \( F = \frac{a}{X} + \frac{{bX} + c}{{X}^{2} + 1} + \frac{{dX} + e}{{\left( {X}^{2} + 1\right) }^{2}} \) . La fraction \( F \) est impaire, donc \( c = e = 0 \) . D’après la relation (*) de la partie 3.2, on a \( a = 1 \) . Multiplions \( F \) par \( {\left( {X}^{2} + 1\right) }^{2} \) puis remplaçons \( X \) par \( i \) . On obtient \( \frac{1}{i} = {di} + e = {di} \) donc \( d = - 1 \) .

> b) There exist \( a, b, c, d, e \in \mathbb{R} \) such that \( F = \frac{a}{X} + \frac{{bX} + c}{{X}^{2} + 1} + \frac{{dX} + e}{{\left( {X}^{2} + 1\right) }^{2}} \) . The fraction \( F \) is odd, so \( c = e = 0 \) . According to relation (*) from part 3.2, we have \( a = 1 \) . Let us multiply \( F \) by \( {\left( {X}^{2} + 1\right) }^{2} \) then replace \( X \) with \( i \) . We obtain \( \frac{1}{i} = {di} + e = {di} \) so \( d = - 1 \) .

Multipliant \( F \) par \( X \) , regardant \( X \) comme un nombre réel et en le faisant tendre vers \( + \infty \) , on obtient \( 0 = a + b \) , donc \( b = - a = - 1 \) .

> Multiplying \( F \) by \( X \) , viewing \( X \) as a real number and letting it tend to \( + \infty \) , we obtain \( 0 = a + b \) , so \( b = - a = - 1 \) .

c) Il s'agit d'un cas classique, qui se traite par divisions euclidiennes successives. On trouve \( {X}^{7} + 2 = \left( {{X}^{2} + X + 1}\right) \left( {{X}^{5} - {X}^{4} + {X}^{2} - X}\right) + \left( {X + 2}\right) \) , d’où

> c) This is a classic case, which is handled by successive Euclidean divisions. We find \( {X}^{7} + 2 = \left( {{X}^{2} + X + 1}\right) \left( {{X}^{5} - {X}^{4} + {X}^{2} - X}\right) + \left( {X + 2}\right) \) , whence

\[
F = \frac{{X}^{7} + 2}{{\left( {X}^{2} + X + 1\right) }^{3}} = \frac{X + 2}{{\left( {X}^{2} + X + 1\right) }^{3}} + \frac{{X}^{5} - {X}^{4} + {X}^{2} - X}{{\left( {X}^{2} + X + 1\right) }^{2}}.
\]

(*)

> On recommence, en divisant cette fois ci \( {X}^{5} - {X}^{4} + {X}^{2} - X \) par \( {X}^{2} + X + 1 \) . On obtient \( {X}^{5} - {X}^{4} + {X}^{2} - X = \left( {{X}^{2} + X + 1}\right) \left( {{X}^{3} - 2{X}^{2} + X + 2}\right) - {4X} - 2 \) , donc

We start again, this time dividing \( {X}^{5} - {X}^{4} + {X}^{2} - X \) by \( {X}^{2} + X + 1 \) . We obtain \( {X}^{5} - {X}^{4} + {X}^{2} - X = \left( {{X}^{2} + X + 1}\right) \left( {{X}^{3} - 2{X}^{2} + X + 2}\right) - {4X} - 2 \) , so

\[
\frac{{X}^{5} - {X}^{4} + {X}^{2} - X}{{\left( {X}^{2} + X + 1\right) }^{2}} =  - \frac{{4X} + 2}{{\left( {X}^{2} + X + 1\right) }^{2}} + \frac{{X}^{3} - 2{X}^{2} + X + 2}{{X}^{2} + X + 1}.
\]

\( \left( {* * }\right) \)

> De même la division \( {X}^{3} - 2{X}^{2} + X + 2 = \left( {{X}^{2} + X + 1}\right) \left( {X - 3}\right) + \left( {{3X} + 5}\right) \) entraîne

Similarly, the division \( {X}^{3} - 2{X}^{2} + X + 2 = \left( {{X}^{2} + X + 1}\right) \left( {X - 3}\right) + \left( {{3X} + 5}\right) \) leads to

\[
\frac{{X}^{3} - 2{X}^{2} + X + 2}{{X}^{2} + X + 1} = \frac{{3X} + 5}{{X}^{2} + X + 1} + X - 3.
\]

(***)

> De \( \left( *\right) ,\left( {* * }\right) \) et \( \left( {* * * }\right) \) , on tire

From \( \left( *\right) ,\left( {* * }\right) \) and \( \left( {* * * }\right) \) , we derive

\[
F = \frac{X + 2}{{\left( {X}^{2} + X + 1\right) }^{3}} - \frac{{4X} + 2}{{\left( {X}^{2} + X + 1\right) }^{2}} + \frac{{3X} + 5}{{X}^{2} + X + 1} + \left( {X - 3}\right) .
\]

Ce procédé est facile et à retenir.

> This process is easy and worth remembering.

d) On décompose d’abord dans \( \mathbb{C}\left( X\right) \) . On pose \( \omega = {e}^{{i\pi }/n} \) , de sorte que \( {X}^{2n} - 1 = \mathop{\prod }\limits_{{k = 0}}^{{{2n} - 1}}\left( {X - {\omega }^{k}}\right) \) . Donc \( F = \mathop{\sum }\limits_{{k = 0}}^{{{2n} - 1}}\frac{{a}_{k}}{X - {\omega }^{k}} \) , où d’après l’identité (**) page 76, \( {a}_{k} = \frac{1}{{2n}{\left( {\omega }^{k}\right) }^{{2n} - 1}} = \frac{{\omega }^{k}}{2n} \) .

> d) We first decompose in \( \mathbb{C}\left( X\right) \). We set \( \omega = {e}^{{i\pi }/n} \), such that \( {X}^{2n} - 1 = \mathop{\prod }\limits_{{k = 0}}^{{{2n} - 1}}\left( {X - {\omega }^{k}}\right) \). Thus \( F = \mathop{\sum }\limits_{{k = 0}}^{{{2n} - 1}}\frac{{a}_{k}}{X - {\omega }^{k}} \), where according to identity (**) on page 76, \( {a}_{k} = \frac{1}{{2n}{\left( {\omega }^{k}\right) }^{{2n} - 1}} = \frac{{\omega }^{k}}{2n} \).

Il ne reste plus qu’à regrouper les termes conjugués. Lorsque \( 1 \leq k \leq n - 1 \) , on a

> All that remains is to group the conjugate terms. When \( 1 \leq k \leq n - 1 \), we have

\[
\frac{{\omega }^{k}}{X - {\omega }^{k}} + \frac{{\omega }^{\left( 2n - k\right) }}{X - {\omega }^{\left( 2n - k\right) }} = \frac{{\omega }^{k}}{X - {\omega }^{k}} + \frac{{\overline{\omega }}^{k}}{X - {\overline{\omega }}^{k}} = \frac{2\cos \left( {{k\pi }/n}\right) X - 2}{{X}^{2} - 2\cos \left( {{k\pi }/n}\right) X + 1},
\]

donc

> therefore

\[
F = \frac{1}{2n}\mathop{\sum }\limits_{{k = 0}}^{{{2n} - 1}}\frac{{\omega }^{k}}{X - {\omega }^{k}} = \frac{1}{2n}\left( {\frac{1}{X - 1} - \frac{1}{X + 1} + \mathop{\sum }\limits_{{k = 1}}^{{n - 1}}\frac{2\cos \left( {{k\pi }/n}\right) X - 2}{{X}^{2} - 2\cos \left( {{k\pi }/n}\right) X + 1}}\right) .
\]

EXERCICE 3. a) Soit \( n \in {\mathbb{N}}^{ * } \) . Montrer qu’il existe \( {P}_{n} \in \mathbb{R}\left\lbrack X\right\rbrack \) de degré \( n \) tel que

> EXERCISE 3. a) Let \( n \in {\mathbb{N}}^{ * } \). Show that there exists \( {P}_{n} \in \mathbb{R}\left\lbrack X\right\rbrack \) of degree \( n \) such that

\[
{X}^{n} + \frac{1}{{X}^{n}} = {P}_{n}\left( {X + \frac{1}{X}}\right) .
\]

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , décomposer la fraction rationnelle \( {F}_{n} = 1/{P}_{n} \) en éléments simples dans \( \mathbb{R}\left( X\right) \) .

> b) For all \( n \in {\mathbb{N}}^{ * } \), decompose the rational fraction \( {F}_{n} = 1/{P}_{n} \) into partial fractions in \( \mathbb{R}\left( X\right) \).

Solution. a) On procède par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident en prenant \( {P}_{1}\left( X\right) = X \) . Supposons le résultat vrai jusqu’au rang \( n - 1 \) et démontrons le au rang \( n \) . On a

> Solution. a) We proceed by induction on \( n \in {\mathbb{N}}^{ * } \). For \( n = 1 \), it is obvious by taking \( {P}_{1}\left( X\right) = X \). Assume the result is true up to rank \( n - 1 \) and prove it for rank \( n \). We have

\[
{\left( X + \frac{1}{X}\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) {X}^{n - k}{\left( \frac{1}{X}\right) }^{k} = {X}^{n} + \frac{1}{{X}^{n}} + \mathop{\sum }\limits_{{k = 1}}^{m}\left( \begin{array}{l} n \\  k \end{array}\right) \left( {{X}^{n - {2k}} + \frac{1}{{X}^{n - {2k}}}}\right)  + {r}_{n},
\]

où \( m = \left\lbrack {\left( {n - 1}\right) /2}\right\rbrack \) est la partie entière de \( \left( {n - 1}\right) /2 \) et où \( {r}_{n} = \left( \begin{matrix} n \\ n/2 \end{matrix}\right) \) si \( n \) est pair, \( {r}_{n} = 0 \) si \( n \) est impair. On peut donc écrire

> where \( m = \left\lbrack {\left( {n - 1}\right) /2}\right\rbrack \) is the integer part of \( \left( {n - 1}\right) /2 \) and where \( {r}_{n} = \left( \begin{matrix} n \\ n/2 \end{matrix}\right) \) if \( n \) is even, \( {r}_{n} = 0 \) if \( n \) is odd. We can therefore write

\[
{X}^{n} + \frac{1}{{X}^{n}} = {\left( X + \frac{1}{X}\right) }^{n} - \mathop{\sum }\limits_{{k = 1}}^{m}\left( \begin{array}{l} n \\  k \end{array}\right) {P}_{n - {2k}}\left( {X + \frac{1}{X}}\right)  - {r}_{n},
\]

Ainsi, \( {P}_{n}\left( X\right) = {X}^{n} - \mathop{\sum }\limits_{{k = 1}}^{m}\left( \begin{array}{l} n \\ k \end{array}\right) {P}_{n - {2k}}\left( X\right) - {r}_{n} \) vérifie la propriété requise, et on a bien \( \deg {P}_{n} = n \) .

> Thus, \( {P}_{n}\left( X\right) = {X}^{n} - \mathop{\sum }\limits_{{k = 1}}^{m}\left( \begin{array}{l} n \\ k \end{array}\right) {P}_{n - {2k}}\left( X\right) - {r}_{n} \) satisfies the required property, and we indeed have \( \deg {P}_{n} = n \).

b) Commençons par chercher les pôles de \( {F}_{n} \) , qui sont les racines de \( {P}_{n} \) . On a

> b) Let us begin by finding the poles of \( {F}_{n} \), which are the roots of \( {P}_{n} \). We have

\[
{P}_{n}\left( {x + \frac{1}{x}}\right)  = 0 \Leftrightarrow  {x}^{n} + \frac{1}{{x}^{n}} = 0 \Leftrightarrow  {x}^{2n} =  - 1 \Leftrightarrow  x = {\omega }_{k} = {e}^{i\left( {{2k} + 1}\right) \pi /\left( {2n}\right) }\;\left( {k \in  \mathbb{Z}}\right) .
\]

Ainsi, pour tout \( k \in \mathbb{Z} \) , la valeur

> Thus, for all \( k \in \mathbb{Z} \), the value

\[
{x}_{k} = {\omega }_{k} + \frac{1}{{\omega }_{k}} = {e}^{i\left( {{2k} + 1}\right) \pi /\left( {2n}\right) } + {e}^{-i\left( {{2k} + 1}\right) \pi /\left( {2n}\right) } = 2\cos \frac{\left( {{2k} + 1}\right) \pi }{2n}
\]

est une racine de \( {P}_{n} \) . On remarque que les \( {x}_{k} \) sont deux à deux distincts lorsque \( 0 \leq k \leq n - 1 \) , et comme \( \deg \left( {P}_{n}\right) = n \) , ceci montre que \( {x}_{0},{x}_{1},\ldots ,{x}_{n - 1} \) sont les racines de \( {P}_{n} \) et qu’elles sont simples. Maintenant, on peut écrire (grâce à la relation (**) page 76)

> is a root of \( {P}_{n} \). We note that the \( {x}_{k} \) are pairwise distinct when \( 0 \leq k \leq n - 1 \), and since \( \deg \left( {P}_{n}\right) = n \), this shows that \( {x}_{0},{x}_{1},\ldots ,{x}_{n - 1} \) are the roots of \( {P}_{n} \) and that they are simple. Now, we can write (thanks to relation (**) on page 76)

\[
{F}_{n} = \frac{1}{{P}_{n}} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}\frac{1}{{P}_{n}^{\prime }\left( {x}_{k}\right) } \cdot  \frac{1}{X - {x}_{k}}.
\]

(*)

> Il ne reste plus qu’à remarquer, après dérivation de la relation \( {P}_{n}\left( {X + 1/X}\right) = {X}^{n} + 1/{X}^{n} \) , que

It only remains to note, after differentiating the relation \( {P}_{n}\left( {X + 1/X}\right) = {X}^{n} + 1/{X}^{n} \), that

\[
\left( {1 - \frac{1}{{\omega }_{k}^{2}}}\right) {P}_{n}^{\prime }\left( {{\omega }_{k} + \frac{1}{{\omega }_{k}}}\right)  = n{\omega }_{k}^{n - 1} - \frac{n}{{\omega }_{k}^{n + 1}} = \frac{n}{{\omega }_{k}}\left( {{\omega }_{k}^{n} - {\omega }_{k}^{-n}}\right)
\]

donc

> therefore

\[
{P}_{n}^{\prime }\left( {x}_{k}\right)  = \frac{n}{{\omega }_{k} - {\omega }_{k}^{-1}}\left( {{\omega }_{k}^{n} - {\omega }_{k}^{-n}}\right)  = n\frac{\sin \frac{\left( {{2k} + 1}\right) \pi }{2}}{\sin \frac{\left( {{2k} + 1}\right) \pi }{2n}} = {\left( -1\right) }^{k}\frac{n}{\sin \frac{\left( {{2k} + 1}\right) \pi }{2n}},
\]

d’où la décomposition en éléments simples de \( {F}_{n} \) en reportant cette égalité dans (*).

> hence the partial fraction decomposition of \( {F}_{n} \) by substituting this equality into (*).

EXERCICE 4. Pour tout \( F \in \mathbb{C}\left( X\right) \) , on note \( {D}_{F} = \mathbb{C} \smallsetminus \left\{ {{a}_{1},\ldots ,{a}_{n}}\right\} \) , où \( {a}_{1},\ldots ,{a}_{n} \) sont les pôles de \( F \) , et on identifie \( F \) avec la fonction rationnelle \( {D}_{F} \rightarrow \mathbb{C}\;z \mapsto F\left( z\right) \) . a) Si \( F \in \mathbb{C}\left( X\right) \) est non constante, montrer que

> EXERCISE 4. For any \( F \in \mathbb{C}\left( X\right) \), we denote \( {D}_{F} = \mathbb{C} \smallsetminus \left\{ {{a}_{1},\ldots ,{a}_{n}}\right\} \), where \( {a}_{1},\ldots ,{a}_{n} \) are the poles of \( F \), and we identify \( F \) with the rational function \( {D}_{F} \rightarrow \mathbb{C}\;z \mapsto F\left( z\right) \). a) If \( F \in \mathbb{C}\left( X\right) \) is non-constant, show that

\[
\text{ (i) }F\left( {D}_{F}\right)  = \mathbb{C}\text{ ou (ii) }\exists \alpha  \in  \mathbb{C} \mid  F\left( {D}_{F}\right)  = \mathbb{C} \smallsetminus  \{ \alpha \}
\]

et caractériser les fractions rationnelles \( F \) vérifiant l’assertion (ii).

> and characterize the rational functions \( F \) satisfying assertion (ii).

b) Si \( F, G \in \mathbb{C}\left( X\right) \) , et si \( G \) n’est pas une constante qui est un pôle de \( F \) , il est possible de définir la composée \( F \circ G \in \mathbb{C}\left( X\right) \) . Donner la forme des fractions rationnelles \( F \) et \( G \in \mathbb{C}\left( X\right) \) telles que la fraction rationnelle \( F \circ G \) soit un polynôme.

> b) If \( F, G \in \mathbb{C}\left( X\right) \), and if \( G \) is not a constant that is a pole of \( F \), it is possible to define the composition \( F \circ G \in \mathbb{C}\left( X\right) \). Give the form of the rational functions \( F \) and \( G \in \mathbb{C}\left( X\right) \) such that the rational function \( F \circ G \) is a polynomial.

Solution. a) Soit \( F = N/D \) la forme réduite de \( F \) . Par hypothèse, \( F \) est non constante donc l’un au moins des polynômes \( N, D \) est non constant. Pour tout \( \lambda \in \mathbb{C} \) , l’équation \( F\left( z\right) = \lambda \left( {z \in {D}_{F}}\right) \) est équivalente à \( \left( {N - {\lambda D}}\right) \left( z\right) = 0\left( {z \in \mathbb{C}}\right) \) . (En effet, si \( \left( {N - {\lambda D}}\right) \left( z\right) = 0 \) alors on doit avoir \( D\left( z\right) \neq 0 \) sinon \( N \) et \( D \) ont une racine commune, donc \( z \in {D}_{F} \) ). Deux cas se présentent :

> Solution. a) Let \( F = N/D \) be the reduced form of \( F \). By hypothesis, \( F \) is non-constant, so at least one of the polynomials \( N, D \) is non-constant. For any \( \lambda \in \mathbb{C} \), the equation \( F\left( z\right) = \lambda \left( {z \in {D}_{F}}\right) \) is equivalent to \( \left( {N - {\lambda D}}\right) \left( z\right) = 0\left( {z \in \mathbb{C}}\right) \). (Indeed, if \( \left( {N - {\lambda D}}\right) \left( z\right) = 0 \), then we must have \( D\left( z\right) \neq 0 \), otherwise \( N \) and \( D \) have a common root, so \( z \in {D}_{F} \)). Two cases arise:

(i) Pour tout \( \lambda \in \mathbb{C} \) , le polynôme \( N - {\lambda D} \) est non constant. Le corps des nombres complexes étant algébriquement clos, \( N - {\lambda D} \) admet une racine \( {z}_{\lambda } \) pour tout \( \lambda \in \mathbb{C} \) . Ainsi, pour tout \( \lambda \in \mathbb{C}, F\left( {z}_{\lambda }\right) = \lambda \) et on en déduit \( F\left( {D}_{F}\right) = \mathbb{C} \) .

> (i) For any \( \lambda \in \mathbb{C} \), the polynomial \( N - {\lambda D} \) is non-constant. Since the field of complex numbers is algebraically closed, \( N - {\lambda D} \) admits a root \( {z}_{\lambda } \) for any \( \lambda \in \mathbb{C} \). Thus, for any \( \lambda \in \mathbb{C}, F\left( {z}_{\lambda }\right) = \lambda \), and we deduce \( F\left( {D}_{F}\right) = \mathbb{C} \).

(ii) Il existe \( \alpha \in \mathbb{C} \) tel que \( N - {\alpha D} \) est constant. Pour tout \( \lambda \neq \alpha \) , le polynôme \( N - {\lambda D} \) est non constant (si \( N - {\lambda D} \) est constant pour \( \lambda \neq \alpha \) , il est facile de voir que l’on doit avoir \( N \) et \( D \) constants, ce qui est contraire aux hypothèses) donc admet au moins une racine \( {z}_{\lambda } \) qui vérifie \( F\left( {z}_{\lambda }\right) = \lambda \) . Ainsi, \( \mathbb{C} \smallsetminus \{ \alpha \} \subset F\left( {D}_{F}\right) \) . De plus, le polynôme \( N - {\alpha D} \) est une constante non nulle (si elle est nulle, \( F \) est constant égal à \( \alpha \) ), donc l’équation \( N - {\alpha D} = 0 \) n’a pas de solution. Finalement, \( F\left( {D}_{F}\right) = \mathbb{C} \smallsetminus \{ \alpha \} \) .

> (ii) There exists \( \alpha \in \mathbb{C} \) such that \( N - {\alpha D} \) is constant. For any \( \lambda \neq \alpha \), the polynomial \( N - {\lambda D} \) is non-constant (if \( N - {\lambda D} \) were constant for \( \lambda \neq \alpha \), it is easy to see that \( N \) and \( D \) would have to be constant, which contradicts the hypotheses) and thus admits at least one root \( {z}_{\lambda } \) satisfying \( F\left( {z}_{\lambda }\right) = \lambda \). Thus, \( \mathbb{C} \smallsetminus \{ \alpha \} \subset F\left( {D}_{F}\right) \). Furthermore, the polynomial \( N - {\alpha D} \) is a non-zero constant (if it were zero, \( F \) would be the constant \( \alpha \)), so the equation \( N - {\alpha D} = 0 \) has no solution. Finally, \( F\left( {D}_{F}\right) = \mathbb{C} \smallsetminus \{ \alpha \} \).

Les fractions rationnelles \( F = N/D \) vérifiant (ii) sont celles vérifiant \( \exists c \in {\mathbb{C}}^{ * } \mid N - {\alpha D} = c \) . Ainsi, \( F = N/D = \left( {{\alpha D} + c}\right) /D = \alpha + c/D \) est de la forme \( F = \alpha + 1/P \) où \( P \) est un polynôme non constant et réciproquement, une fraction rationnelle de cette forme vérifie (ii).

> The rational fractions \( F = N/D \) satisfying (ii) are those satisfying \( \exists c \in {\mathbb{C}}^{ * } \mid N - {\alpha D} = c \). Thus, \( F = N/D = \left( {{\alpha D} + c}\right) /D = \alpha + c/D \) is of the form \( F = \alpha + 1/P \) where \( P \) is a non-constant polynomial, and conversely, a rational fraction of this form satisfies (ii).

b) Si \( F \) est constant, \( F \circ G = F \) est toujours un polynôme. De même, si \( G \) est constant et si \( G \) n’est pas un pôle de \( F, F \circ G \) est une constante donc un polynôme.

> b) If \( F \) is constant, \( F \circ G = F \) is always a polynomial. Similarly, if \( G \) is constant and if \( G \) is not a pole of \( F, F \circ G \), it is a constant and therefore a polynomial.

Supposons maintenant \( F \) et \( G \) non constants. Si \( \alpha \) est un pôle de \( F \) , on a \( \mathop{\lim }\limits_{\substack{{z \rightarrow \alpha } \\ {z \neq \alpha } }}\left| {F\left( z\right) }\right| = + \infty \) , donc si \( \alpha = G\left( \beta \right) \in G\left( {D}_{G}\right) \) , le théorème de composition des limites entraîne

> Now suppose \( F \) and \( G \) are non-constant. If \( \alpha \) is a pole of \( F \), we have \( \mathop{\lim }\limits_{\substack{{z \rightarrow \alpha } \\ {z \neq \alpha } }}\left| {F\left( z\right) }\right| = + \infty \), so if \( \alpha = G\left( \beta \right) \in G\left( {D}_{G}\right) \), the composition theorem for limits implies

\[
\mathop{\lim }\limits_{\substack{{z \rightarrow  \beta } \\  {z \neq  \beta } }}\left| {F \circ  G\left( z\right) }\right|  =  + \infty
\]

ce qui est impossible si \( F \circ G \) est un polynôme. Ainsi nous venons de montrer

> which is impossible if \( F \circ G \) is a polynomial. Thus we have just shown

Si \( F \circ G \) est un polynôme, tout pôle de \( F \) appartient à \( \mathbb{C} \smallsetminus G\left( {D}_{G}\right) \) .

> If \( F \circ G \) is a polynomial, every pole of \( F \) belongs to \( \mathbb{C} \smallsetminus G\left( {D}_{G}\right) \).(*)

D’après la question précédente, l’ensemble \( \mathbb{C} \smallsetminus G\left( {D}_{G}\right) \) a au plus un élément, ce qui montre que nécessairement \( F \) a au plus un pôle.

> According to the previous question, the set \( \mathbb{C} \smallsetminus G\left( {D}_{G}\right) \) has at most one element, which shows that necessarily \( F \) has at most one pole.

- Si \( F \) n’a pas de pôle, c’est-à-dire si \( F \) est un polynôme, alors si \( F \circ  G \) est un polynôme, \( G \) est un polynôme. En effet, si \( G \) admet un pôle \( \beta \) , alors \( \mathop{\lim }\limits_{\substack{{z \rightarrow  \beta } \\  {z \neq  \beta } }}\left| {G\left( z\right) }\right|  =  + \infty \) et le polynôme \( F \) étant non constant on en déduit

> - If \( F \) has no pole, that is to say if \( F \) is a polynomial, then if \( F \circ  G \) is a polynomial, \( G \) is a polynomial. Indeed, if \( G \) admits a pole \( \beta \), then \( \mathop{\lim }\limits_{\substack{{z \rightarrow  \beta } \\  {z \neq  \beta } }}\left| {G\left( z\right) }\right|  =  + \infty \) and since the polynomial \( F \) is non-constant, we deduce

\[
\mathop{\lim }\limits_{\substack{{z \rightarrow  \beta } \\  {z \neq  \beta } }}\left| {F \circ  G\left( z\right) }\right|  =  + \infty \;\text{ car }\;\mathop{\lim }\limits_{{\left| z\right|  \rightarrow   + \infty }}\left| {F\left( z\right) }\right|  =  + \infty ,
\]

et \( F \circ G \) ne peut donc pas être un polynôme.

> and \( F \circ G \) therefore cannot be a polynomial.

- Si \( F \) admet un seul pôle \( \alpha \) , on peut écrire \( F \) sous la forme

> - If \( F \) admits a single pole \( \alpha \), we can write \( F \) in the form

\[
F = \frac{P\left( {X - \alpha }\right) }{{\left( X - \alpha \right) }^{h}},\;P \in  \mathbb{C}\left\lbrack  X\right\rbrack  \;\text{ et }\;h \in  {\mathbb{N}}^{ * }.
\]

Pour que \( F \circ G \) soit un polynôme, la propriété (*) entraîne \( \mathbb{C} \smallsetminus G\left( {D}_{G}\right) = \{ \alpha \} \) . Comme \( G \) n'est pas constant (le cas \( G \) constant a été traité plus haut), d'après la question a), ceci entraîne \( G = \alpha + 1/Q \) où \( Q \) est un polynôme non constant. On a alors

> For \( F \circ G \) to be a polynomial, property (*) implies \( \mathbb{C} \smallsetminus G\left( {D}_{G}\right) = \{ \alpha \} \) . Since \( G \) is not constant (the case where \( G \) is constant was treated above), according to question a), this implies \( G = \alpha + 1/Q \) where \( Q \) is a non-constant polynomial. We then have

\[
F \circ  G = \frac{P\left( {1/Q}\right) }{{\left( 1/Q\right) }^{h}} = {Q}^{h}P\left( {1/Q}\right) .
\]

En écrivant \( P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k}\left( {\text{ où }n = \deg P}\right) \) , ceci s’écrit aussi \( F \circ G = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{Q}^{h - k} \) , et ceci est un polynôme si et seulement si \( n = \deg \left( P\right) \leq h \) .

> By writing \( P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k}\left( {\text{ où }n = \deg P}\right) \) , this can also be written as \( F \circ G = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{Q}^{h - k} \) , and this is a polynomial if and only if \( n = \deg \left( P\right) \leq h \) .

Réciproquement, il est facile de vérifier que les solutions trouvées conviennent. Finalement, \( F \circ G \) est un polynôme si et seulement si l’une des conditions suivantes est vérifiée :

> Conversely, it is easy to verify that the solutions found are valid. Finally, \( F \circ G \) is a polynomial if and only if one of the following conditions is satisfied:

(i) \( F \) est constant.

> (i) \( F \) is constant.

(ii) \( G \) est constant et n’est pas un pôle de \( F \) .

> (ii) \( G \) is constant and is not a pole of \( F \) .

(iii) \( F \) et \( G \) sont des polynômes.

> (iii) \( F \) and \( G \) are polynomials.

(iv) \( F = \frac{P\left( X\right) }{{\left( X - \alpha \right) }^{h}} \) où \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( \deg \left( P\right) \leq h \) , et \( G = \alpha + 1/Q \) où \( Q \in \mathbb{C}\left\lbrack X\right\rbrack \) .

> (iv) \( F = \frac{P\left( X\right) }{{\left( X - \alpha \right) }^{h}} \) where \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( \deg \left( P\right) \leq h \) , and \( G = \alpha + 1/Q \) where \( Q \in \mathbb{C}\left\lbrack X\right\rbrack \) .

EXERCICE 5. 1/ Déterminer les polynômes de \( \mathbb{C}\left\lbrack X\right\rbrack \) qui laissent stable le cercle unité \( \mathbb{U} = \{ z \in \mathbb{C}\left| \right| z \mid = 1\} \) de \( \mathbb{C} \) .

> EXERCISE 5. 1/ Determine the polynomials of \( \mathbb{C}\left\lbrack X\right\rbrack \) that leave the unit circle \( \mathbb{U} = \{ z \in \mathbb{C}\left| \right| z \mid = 1\} \) of \( \mathbb{C} \) invariant.

2/ Déterminer les fractions rationnelles de \( \mathbb{C}\left( X\right) \) qui laissent stable \( \mathbb{U} \) .

> 2/ Determine the rational fractions of \( \mathbb{C}\left( X\right) \) that leave \( \mathbb{U} \) invariant.

Solution. 1/ Pour tout polynôme \( P = {a}_{0} + \cdots + {a}_{n}{X}^{n} \in \mathbb{C}\left\lbrack X\right\rbrack \) de degré \( n \in \mathbb{N} \) , on note \( {P}^{ * } \) le polynôme défini par

> Solution. 1/ For any polynomial \( P = {a}_{0} + \cdots + {a}_{n}{X}^{n} \in \mathbb{C}\left\lbrack X\right\rbrack \) of degree \( n \in \mathbb{N} \) , we denote by \( {P}^{ * } \) the polynomial defined by

\[
{P}^{ * }\left( X\right)  = {\bar{a}}_{0}{X}^{n} + {\bar{a}}_{1}{X}^{n - 1} + \cdots  + {\bar{a}}_{n} = {X}^{n}\bar{P}\left( {1/X}\right) .
\]

Lorsque \( z \in \mathbb{U} \) , on a \( 1/z = \bar{z} \) donc \( {P}^{ * }\left( z\right) = {z}^{n}\bar{P}\left( \bar{z}\right) = {z}^{n}\overline{P\left( z\right) } \) , et lorsque \( P \) stabilise \( \mathbb{U} \) on a donc \( P\left( z\right) {P}^{ * }\left( z\right) = {z}^{n}{\left| P\left( z\right) \right| }^{2} = {z}^{n} \) . Ainsi, le polynôme \( P\left( X\right) {P}^{ * }\left( X\right) - {X}^{n} \) s’annule sur \( \mathbb{U} \) , donc une infinité de fois, donc c’est le polynôme nul. On en déduit \( P\left( X\right) {P}^{ * }\left( X\right) = {X}^{n} \) , et comme \( \deg \left( P\right) = n \) il existe \( \lambda \in {\mathbb{C}}^{ * } \) tel que \( P\left( X\right) = \lambda {X}^{n} \) et \( {P}^{ * }\left( X\right) = 1/\lambda \) . Comme \( \left| {P\left( 1\right) }\right| = 1 \) on a forcément \( \left| \lambda \right| = 1 \) , donc finalement \( P\left( X\right) = \lambda {X}^{n} \) avec \( \left| \lambda \right| = 1 \) .

> When \( z \in \mathbb{U} \), we have \( 1/z = \bar{z} \) thus \( {P}^{ * }\left( z\right) = {z}^{n}\bar{P}\left( \bar{z}\right) = {z}^{n}\overline{P\left( z\right) } \), and when \( P \) stabilizes \( \mathbb{U} \) we therefore have \( P\left( z\right) {P}^{ * }\left( z\right) = {z}^{n}{\left| P\left( z\right) \right| }^{2} = {z}^{n} \). Thus, the polynomial \( P\left( X\right) {P}^{ * }\left( X\right) - {X}^{n} \) vanishes on \( \mathbb{U} \), hence infinitely many times, so it is the zero polynomial. We deduce \( P\left( X\right) {P}^{ * }\left( X\right) = {X}^{n} \), and since \( \deg \left( P\right) = n \) there exists \( \lambda \in {\mathbb{C}}^{ * } \) such that \( P\left( X\right) = \lambda {X}^{n} \) and \( {P}^{ * }\left( X\right) = 1/\lambda \). Since \( \left| {P\left( 1\right) }\right| = 1 \) we necessarily have \( \left| \lambda \right| = 1 \), so finally \( P\left( X\right) = \lambda {X}^{n} \) with \( \left| \lambda \right| = 1 \).

Réciproquement, il est immédiat que tout polynôme de cette forme stabilise le cercle unité. 2/ Soit \( F \in \mathbb{C}\left( X\right) \) laissant stable \( \mathbb{U} \) . On peut écrire \( F \) sous la forme \( F = {X}^{n}P/Q \) où \( n \in \mathbb{Z} \) et \( P, Q \in \mathbb{C}\left\lbrack X\right\rbrack \) sont premiers entre eux, avec \( P\left( 0\right) \neq 0 \) et \( Q\left( 0\right) \neq 0 \) . Soit \( a = \deg P, b = \deg Q \) . Pour tout \( z \in \mathbb{U} \) qui n’est pas un zéro de \( Q \) ou de \( {Q}^{ * } \) , on peut écrire

> Conversely, it is immediate that any polynomial of this form stabilizes the unit circle. 2/ Let \( F \in \mathbb{C}\left( X\right) \) leave \( \mathbb{U} \) stable. We can write \( F \) in the form \( F = {X}^{n}P/Q \) where \( n \in \mathbb{Z} \) and \( P, Q \in \mathbb{C}\left\lbrack X\right\rbrack \) are coprime, with \( P\left( 0\right) \neq 0 \) and \( Q\left( 0\right) \neq 0 \). Let \( a = \deg P, b = \deg Q \). For any \( z \in \mathbb{U} \) that is not a zero of \( Q \) or \( {Q}^{ * } \), we can write

\[
\frac{{P}^{ * }\left( z\right) }{{Q}^{ * }\left( z\right) } = \frac{{z}^{a}\overline{P\left( z\right) }}{{z}^{b}\overline{Q\left( z\right) }},\;\text{ donc }\;\frac{P\left( z\right) }{Q\left( z\right) }\frac{{P}^{ * }\left( z\right) }{{Q}^{ * }\left( z\right) } = {z}^{a - b}\frac{{\left| P\left( z\right) \right| }^{2}}{{\left| Q\left( z\right) \right| }^{2}} = {z}^{a - b}{\left| \frac{P\left( z\right) }{Q\left( z\right) }\right| }^{2} = {z}^{a - b}.
\]

Si \( a \geq b \) , on en déduit que le polynôme \( P\left( X\right) {P}^{ * }\left( X\right) - {X}^{a - b}Q\left( X\right) {Q}^{ * }\left( X\right) \) s’annule sur \( \mathbb{U} \) (sauf eventuellement sur les zéros de \( Q \) et \( {Q}^{ * } \) ), donc il s’annule une infinité de fois, donc il est nul. Donc \( P\left( X\right) {P}^{ * }\left( X\right) = {X}^{a - b}Q\left( X\right) {Q}^{ * }\left( X\right) \) . Comme \( P\left( 0\right) Q\left( 0\right) \neq 0 \) on a \( \deg {P}^{ * } = \deg P = a \) et \( \deg {Q}^{ * } = \deg Q = b \) , donc l’égalité implique \( {2a} = a - b + {2b} = a + b \) donc \( a = b \) . Donc \( P{P}^{ * } = Q{Q}^{ * } \) . Si \( a < b \) , un raisonnement similaire à partir de \( Q\left( X\right) {Q}^{ * }\left( X\right) - {X}^{b - a}P\left( X\right) {P}^{ * }\left( X\right) \) abouti à la même conclusion.

> If \( a \geq b \), we deduce that the polynomial \( P\left( X\right) {P}^{ * }\left( X\right) - {X}^{a - b}Q\left( X\right) {Q}^{ * }\left( X\right) \) vanishes on \( \mathbb{U} \) (except possibly at the zeros of \( Q \) and \( {Q}^{ * } \)), so it vanishes infinitely many times, and is therefore zero. Thus \( P\left( X\right) {P}^{ * }\left( X\right) = {X}^{a - b}Q\left( X\right) {Q}^{ * }\left( X\right) \). Since \( P\left( 0\right) Q\left( 0\right) \neq 0 \), we have \( \deg {P}^{ * } = \deg P = a \) and \( \deg {Q}^{ * } = \deg Q = b \), so the equality implies \( {2a} = a - b + {2b} = a + b \), thus \( a = b \). Therefore \( P{P}^{ * } = Q{Q}^{ * } \). If \( a < b \), a similar argument starting from \( Q\left( X\right) {Q}^{ * }\left( X\right) - {X}^{b - a}P\left( X\right) {P}^{ * }\left( X\right) \) leads to the same conclusion.

On a donc \( Q \mid P{P}^{ * } \) et comme \( P \) et \( Q \) sont premiers entre eux, on en déduit \( Q \mid {P}^{ * } \) . On a vu que ces polynômes ont même degré, on en déduit l’existence de \( \alpha \in {\mathbb{C}}^{ * } \) tel que \( Q = \alpha {P}^{ * } \) , donc \( F = \left( {{X}^{n}/\alpha }\right) P\left( X\right) /{P}^{ * }\left( X\right) \) . Donc \( F = \beta {X}^{m}P\left( X\right) /\bar{P}\left( {1/X}\right) \) avec \( \beta = 1/\alpha \) et \( m = n - a \) . Comme \( F\left( 1\right) \in \mathbb{U} \) on a forcément \( \beta \in \mathbb{U} \) . Réciproquement, on vérifie facilement que tout fraction rationnelle de la forme \( F\left( X\right) = \beta {X}^{m}P\left( X\right) /\bar{P}\left( {1/X}\right) \) avec \( m \in \mathbb{Z},\beta \in \mathbb{U} \) et \( P \in \mathbb{C}\left\lbrack X\right\rbrack \left( {P \neq 0}\right) \) stabilise bien le cercle unité.

> We thus have \( Q \mid P{P}^{ * } \), and since \( P \) and \( Q \) are coprime, we deduce \( Q \mid {P}^{ * } \). We have seen that these polynomials have the same degree, so we deduce the existence of \( \alpha \in {\mathbb{C}}^{ * } \) such that \( Q = \alpha {P}^{ * } \), thus \( F = \left( {{X}^{n}/\alpha }\right) P\left( X\right) /{P}^{ * }\left( X\right) \). Therefore \( F = \beta {X}^{m}P\left( X\right) /\bar{P}\left( {1/X}\right) \) with \( \beta = 1/\alpha \) and \( m = n - a \). Since \( F\left( 1\right) \in \mathbb{U} \), we necessarily have \( \beta \in \mathbb{U} \). Conversely, it is easy to verify that any rational fraction of the form \( F\left( X\right) = \beta {X}^{m}P\left( X\right) /\bar{P}\left( {1/X}\right) \) with \( m \in \mathbb{Z},\beta \in \mathbb{U} \) and \( P \in \mathbb{C}\left\lbrack X\right\rbrack \left( {P \neq 0}\right) \) indeed stabilizes the unit circle.
