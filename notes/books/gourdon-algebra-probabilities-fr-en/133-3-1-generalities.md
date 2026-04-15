#### 3.1. Generalities

*Français : 3.1. Généralités*

DéFINITION 1. Soient \( \left( {\Omega ,\mathcal{A}, P}\right) \) un espace probabilisé et \( \left( {E,\mathcal{F}}\right) \) un espace probabilisable. On appelle variable aléatoire de \( \Omega \) vers \( E \) une application \( X : \Omega \rightarrow E \) telle que \( \forall F \in \; \mathcal{F},{X}^{-1}\left( F\right) \in \mathcal{A} \) . La fonction \( {P}_{X} : \mathcal{F} \rightarrow \left\lbrack {0,1}\right\rbrack , F \mapsto P\left( {{X}^{-1}\left( F\right) }\right) \) est alors une probabilité sur \( \left( {E,\mathcal{F}}\right) \) , appelée loi de probabilité de \( X \) .

> DEFINITION 1. Let \( \left( {\Omega ,\mathcal{A}, P}\right) \) be a probability space and \( \left( {E,\mathcal{F}}\right) \) a measurable space. A random variable from \( \Omega \) to \( E \) is a mapping \( X : \Omega \rightarrow E \) such that \( \forall F \in \; \mathcal{F},{X}^{-1}\left( F\right) \in \mathcal{A} \) . The function \( {P}_{X} : \mathcal{F} \rightarrow \left\lbrack {0,1}\right\rbrack , F \mapsto P\left( {{X}^{-1}\left( F\right) }\right) \) is then a probability on \( \left( {E,\mathcal{F}}\right) \) , called the probability distribution of \( X \) .

En pratique, on peut avoir \( \left( {E,\mathcal{F}}\right) = \left( {E,\mathcal{P}\left( E\right) }\right) \) avec \( E \) un ensemble fini ou dé- nombrable (cas des variables aléatoires discrètes, qui est le cadre de cette section), soit \( \left( {E,\mathcal{F}}\right) = \left( {\mathbb{R},\mathcal{B}}\right) \) (on parle alors de variable aléatoire réelle, \( \mathcal{B} \) étant la tribu borélienne), soit \( E = {\mathbb{R}}^{d} \) , soit un espace plus sophistiqué (comme par exemple l’espace des fonctions continues de \( \left\lbrack {0,1}\right\rbrack \) dans \( \mathbb{R} \) ).

> In practice, we may have \( \left( {E,\mathcal{F}}\right) = \left( {E,\mathcal{P}\left( E\right) }\right) \) with \( E \) a finite or countable set (the case of discrete random variables, which is the framework of this section), or \( \left( {E,\mathcal{F}}\right) = \left( {\mathbb{R},\mathcal{B}}\right) \) (we then speak of a real random variable, \( \mathcal{B} \) being the Borel sigma-algebra), or \( E = {\mathbb{R}}^{d} \) , or a more sophisticated space (such as, for example, the space of continuous functions from \( \left\lbrack {0,1}\right\rbrack \) to \( \mathbb{R} \) ).

NOTATION. On utilise en général la notation \( \{ X \in B\} \) pour désigner l’ensemble \( {X}^{-1}\left( B\right) \) . On écrira donc \( P\left( {X \in B}\right) \) pour désigner \( P\left( {{X}^{-1}\left( B\right) }\right) \) . On utilisera également la notation \( P\left( {X = x}\right) = P\left( {{X}^{-1}\left( {\{ x\} }\right) }\right) \) pour \( x \in E \) . Pour les variables aléatoires réelles, on écrira \( P\left( {X \leq a}\right) = P\left( {{X}^{-1}\left( {\rbrack - \infty , a\rbrack }\right) }\right) , P\left( {X \geq b}\right) = P\left( {{X}^{-1}\left( {\lbrack b, + \infty \lbrack }\right) }\right. ), P\left( {a \leq X < b}\right) = \; P\left( {{X}^{-1}\left( {\lbrack a, b\lbrack }\right) }\right. \) ), etc.

> NOTATION. We generally use the notation \( \{ X \in B\} \) to denote the set \( {X}^{-1}\left( B\right) \) . We will therefore write \( P\left( {X \in B}\right) \) to denote \( P\left( {{X}^{-1}\left( B\right) }\right) \) . We will also use the notation \( P\left( {X = x}\right) = P\left( {{X}^{-1}\left( {\{ x\} }\right) }\right) \) for \( x \in E \) . For real random variables, we will write \( P\left( {X \leq a}\right) = P\left( {{X}^{-1}\left( {\rbrack - \infty , a\rbrack }\right) }\right) , P\left( {X \geq b}\right) = P\left( {{X}^{-1}\left( {\lbrack b, + \infty \lbrack }\right) }\right. ), P\left( {a \leq X < b}\right) = \; P\left( {{X}^{-1}\left( {\lbrack a, b\lbrack }\right) }\right. \) ), etc.

Cas des variables aléatoires réelles. Même si ces dernières ne sont pas au programme des classes préparatoires, il est bon de connaitre les définitions et propriétés suivantes.

> Case of real random variables. Even if these are not in the preparatory classes curriculum, it is good to know the following definitions and properties.

- La loi \( {P}_{X} \) d’une variable aléatoire réelle \( X \) est entièrement déterminée par les probabilités \( P\left( {X \leq  x}\right) , x \in  \mathbb{R} \) .

> - The distribution \( {P}_{X} \) of a real random variable \( X \) is entirely determined by the probabilities \( P\left( {X \leq  x}\right) , x \in  \mathbb{R} \) .

- La fonction \( {F}_{X} : \mathbb{R} \rightarrow  \left\lbrack  {0,1}\right\rbrack  \;x \mapsto  P\left( {X \leq  x}\right) \) est appelée fonction de répartition de \( X \) . Elle est croissante. Elle est continue à droite en tout point de \( \mathbb{R} \) , car pour toute suite réelle \( \left( {x}_{n}\right) \) convergeant vers \( x \) et décroissante on a

> - The function \( {F}_{X} : \mathbb{R} \rightarrow  \left\lbrack  {0,1}\right\rbrack  \;x \mapsto  P\left( {X \leq  x}\right) \) is called the cumulative distribution function of \( X \) . It is increasing. It is right-continuous at every point of \( \mathbb{R} \) , because for any real sequence \( \left( {x}_{n}\right) \) converging to \( x \) and decreasing, we have

\[
\left. \left. {\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{F}_{X}\left( {x}_{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}P\left( {{X}^{-1}\left( \right\rbrack   - \infty ,{x}_{n}\rbrack }\right) }\right) \right)  = P\left( \left. {{ \cap  }_{n \in  \mathbb{N}}{X}^{-1}\left( \right)  - \infty ,{x}_{n}}\right\rbrack  \right) )
\]

\[
= P\left( {{X}^{-1}\left( {{ \cap  }_{n \in  \mathbb{N}}\rbrack  - \infty ,{x}_{n}\rbrack }\right) }\right)  = P\left( {{X}^{-1}\left( {\rbrack  - \infty , x\rbrack }\right) }\right)  = {F}_{X}\left( x\right) .
\]

Elle vérifie \( \mathop{\lim }\limits_{{x \rightarrow - \infty }}{F}_{X}\left( x\right) = 0 \) et \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}{F}_{X}\left( x\right) = 1 \) .

> It satisfies \( \mathop{\lim }\limits_{{x \rightarrow - \infty }}{F}_{X}\left( x\right) = 0 \) and \( \mathop{\lim }\limits_{{x \rightarrow + \infty }}{F}_{X}\left( x\right) = 1 \) .

- On a \( P\left( {X < b}\right)  = \mathop{\lim }\limits_{{x \rightarrow  {b}^{ - }}}F\left( x\right) \) et \( P\left( {X \geq  a}\right)  = 1 - \mathop{\lim }\limits_{{x \rightarrow  {a}^{ - }}}F\left( x\right) \) .

> - We have \( P\left( {X < b}\right)  = \mathop{\lim }\limits_{{x \rightarrow  {b}^{ - }}}F\left( x\right) \) and \( P\left( {X \geq  a}\right)  = 1 - \mathop{\lim }\limits_{{x \rightarrow  {a}^{ - }}}F\left( x\right) \) .

- Les sauts de discontinuité de \( {F}_{X} \) correspondent aux probabilités ponctuelles non nulles : \( P\left( {X = x}\right)  = {F}_{X}\left( x\right)  - \mathop{\lim }\limits_{{t \rightarrow  {x}^{ - }}}{F}_{X}\left( t\right) \) .

> - The discontinuity jumps of \( {F}_{X} \) correspond to non-zero point probabilities: \( P\left( {X = x}\right)  = {F}_{X}\left( x\right)  - \mathop{\lim }\limits_{{t \rightarrow  {x}^{ - }}}{F}_{X}\left( t\right) \) .

- On dit que \( X \) possède une densité s’il existe une fonction \( f : \mathbb{R} \rightarrow  {\mathbb{R}}^{ + } \) , continue sur \( \mathbb{R} \) sauf éventuellement en un nombre fini de points, intégrable sur \( \mathbb{R} \) , telle que pour tout \( x \in  \mathbb{R},{F}_{X}\left( x\right)  = {\int }_{-\infty }^{x}f\left( t\right) {dt} \) . Dans ce cas, \( {F}_{X} \) est continue et pour tout \( x \in  \mathbb{R} \) on a \( P\left( {X = x}\right)  = 0 \) .

> - We say that \( X \) has a density if there exists a function \( f : \mathbb{R} \rightarrow  {\mathbb{R}}^{ + } \) , continuous on \( \mathbb{R} \) except possibly at a finite number of points, integrable on \( \mathbb{R} \) , such that for all \( x \in  \mathbb{R},{F}_{X}\left( x\right)  = {\int }_{-\infty }^{x}f\left( t\right) {dt} \) . In this case, \( {F}_{X} \) is continuous and for all \( x \in  \mathbb{R} \) we have \( P\left( {X = x}\right)  = 0 \) .

##### Discrete random variables.

*Français : Variables aléatoires discrètes.*

DÉFINITION 2. On dit qu’une variable aléatoire \( X : \Omega \rightarrow E \) est discrète si \( X\left( \Omega \right) \) est fini ou dénombrable.

> DEFINITION 2. A random variable \( X : \Omega \rightarrow E \) is said to be discrete if \( X\left( \Omega \right) \) is finite or countable.

Remarque 1. - Lorsque \( X\left( \Omega \right) \) est fini, on dit que la variable aléatoire est finie.

> Remark 1. - When \( X\left( \Omega \right) \) is finite, the random variable is said to be finite.

- Dans le cas des variables aléatoires discrètes, la tribu considérée pour l'espace d’arrivée est en général \( \mathcal{P}\left( {X\left( \Omega \right) }\right) \) .

> - In the case of discrete random variables, the sigma-algebra considered for the arrival space is generally \( \mathcal{P}\left( {X\left( \Omega \right) }\right) \) .

- L’espace \( \Omega \) n’est pas forcément fini ou dénombrable. Par exemple l’espace \( \Omega \) des suites \( w = {\left( {w}_{n}\right) }_{n \in  \mathbb{N}} \) à valeur dans \( \{ 0,1\} \) est infini non dénombrable (c’est classique), et la variable aléatoire \( X \) définie par \( X\left( w\right)  = \inf \left\{  {n \in  \mathbb{N} \mid  {w}_{n} = 0}\right\} \) est discrète,à valeur dans \( \mathbb{N} \cup  \{  + \infty \} \) (la valeur \( + \infty \) est l’image de la suite constante égale à 1).

> - The space \( \Omega \) is not necessarily finite or countable. For example, the space \( \Omega \) of sequences \( w = {\left( {w}_{n}\right) }_{n \in  \mathbb{N}} \) with values in \( \{ 0,1\} \) is uncountable (this is standard), and the random variable \( X \) defined by \( X\left( w\right)  = \inf \left\{  {n \in  \mathbb{N} \mid  {w}_{n} = 0}\right\} \) is discrete, with values in \( \mathbb{N} \cup  \{  + \infty \} \) (the value \( + \infty \) is the image of the constant sequence equal to 1).

— D’après la proposition 3 page 322, une variable aléatoire discrète \( X \) est caractérisée par les valeurs \( P\left( {X = x}\right) \) , avec \( x \in X\left( \Omega \right) \) . Ainsi, pour tout \( A \subset X\left( \Omega \right) \) , on a

> — According to proposition 3 on page 322, a discrete random variable \( X \) is characterized by the values \( P\left( {X = x}\right) \), with \( x \in X\left( \Omega \right) \). Thus, for any \( A \subset X\left( \Omega \right) \), we have

\[
P\left( {X \in  A}\right)  = \mathop{\sum }\limits_{{x \in  A}}P\left( {X = x}\right) .
\]

Vecteurs aléatoires discrets.

> Discrete random vectors.

DéFINITION 3. Soit \( n \in {\mathbb{N}}^{ * } \) et \( {X}_{1},\ldots ,{X}_{n} \) des variables aléatoires discrètes de \( \Omega \) vers \( E \) . L’application \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) est une variable aléatoire discrète de \( \Omega \) vers \( {E}^{n} \) , appelée vecteur aléatoire discret. La loi du \( n \) -uplet \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) est appelée loi conjointe des variables aléatoires \( {X}_{1},\ldots ,{X}_{n} \) . Les lois des variables aléatoires \( {X}_{1},\ldots ,{X}_{n} \) sont appelées les lois marginales du \( n \) -uplet \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) .

> DEFINITION 3. Let \( n \in {\mathbb{N}}^{ * } \) and \( {X}_{1},\ldots ,{X}_{n} \) be discrete random variables from \( \Omega \) to \( E \). The mapping \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) is a discrete random variable from \( \Omega \) to \( {E}^{n} \), called a discrete random vector. The distribution of the \( n \)-tuple \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) is called the joint distribution of the random variables \( {X}_{1},\ldots ,{X}_{n} \). The distributions of the random variables \( {X}_{1},\ldots ,{X}_{n} \) are called the marginal distributions of the \( n \)-tuple \( \left( {{X}_{1},\ldots ,{X}_{n}}\right) \).

NOTATION. On généralise l’usage de la notation \( P\left( {X \in A}\right) \) aux vecteurs aléatoires : \( P\left( {{X}_{1} \in {A}_{1},\ldots ,{X}_{n} \in {A}_{n}}\right) \) désigne la valeur \( P\left( {{X}^{-1}\left( {{A}_{1} \times \ldots \times {A}_{n}}\right) }\right) \) (on la note parfois \( \left. {P\left( {\left\{ {{X}_{1} \in {A}_{1}}\right\} \cap \ldots \cap \left\{ {{X}_{n} \in {A}_{n}}\right\} }\right) }\right) \) . On utilise aussi la notation \( P\left( {{X}_{1} = {a}_{1},\ldots ,{X}_{n} = {a}_{n}}\right) \) , ou toute expression de cette forme où les égalités sont remplacées par des inégalités.

> NOTATION. We generalize the use of the notation \( P\left( {X \in A}\right) \) to random vectors: \( P\left( {{X}_{1} \in {A}_{1},\ldots ,{X}_{n} \in {A}_{n}}\right) \) denotes the value \( P\left( {{X}^{-1}\left( {{A}_{1} \times \ldots \times {A}_{n}}\right) }\right) \) (it is sometimes denoted \( \left. {P\left( {\left\{ {{X}_{1} \in {A}_{1}}\right\} \cap \ldots \cap \left\{ {{X}_{n} \in {A}_{n}}\right\} }\right) }\right) \)). We also use the notation \( P\left( {{X}_{1} = {a}_{1},\ldots ,{X}_{n} = {a}_{n}}\right) \), or any expression of this form where the equalities are replaced by inequalities.

Remarque 2. - Un vecteur aléatoire discret \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) est caractérisé par les valeurs \( P\left( {{X}_{1} = {x}_{1},\ldots ,{X}_{n} = {x}_{n}}\right) \) , avec \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in \left( {{X}_{1}\left( \Omega \right) ,\ldots ,{X}_{n}\left( \Omega \right) }\right) \) .

> Remark 2. - A discrete random vector \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) \) is characterized by the values \( P\left( {{X}_{1} = {x}_{1},\ldots ,{X}_{n} = {x}_{n}}\right) \), with \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \in \left( {{X}_{1}\left( \Omega \right) ,\ldots ,{X}_{n}\left( \Omega \right) }\right) \).

- On déduit les lois marginales à partir de la loi conjointe à partir de l'égalité

> - We deduce the marginal distributions from the joint distribution using the equality

\[
\forall a \in  {X}_{k}\left( \Omega \right) ,\;P\left( {{X}_{k} = a}\right)  = \mathop{\sum }\limits_{{{x}_{j} \in  {X}_{j}\left( \Omega \right) , j \neq  k}}P\left( {{ \cup  }_{j \neq  k}\left\{  {{X}_{j} = {x}_{j}}\right\}   \cup  \left\{  {{X}_{k} = a}\right\}  }\right) .
\]

Réciproquement on ne peut pas déduire la loi conjointe à partir des lois marginales.

> Conversely, one cannot deduce the joint distribution from the marginal distributions.

Proposition 1. Soit \( n \in {\mathbb{N}}^{ * } \) et \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) : \Omega \rightarrow {E}^{n} \) un vecteur aléatoire discret. Soit \( f : {E}^{n} \rightarrow F \) une fonction. Alors \( f\left( X\right) : \Omega \rightarrow F \) est une variable aléatoire discrète, dont la loi de probabilité vérifie, pour tout \( y \in f\left( {X\left( \Omega \right) }\right) \)

> Proposition 1. Let \( n \in {\mathbb{N}}^{ * } \) and \( X = \left( {{X}_{1},\ldots ,{X}_{n}}\right) : \Omega \rightarrow {E}^{n} \) be a discrete random vector. Let \( f : {E}^{n} \rightarrow F \) be a function. Then \( f\left( X\right) : \Omega \rightarrow F \) is a discrete random variable, whose probability distribution satisfies, for any \( y \in f\left( {X\left( \Omega \right) }\right) \)

\[
P\left( {f\left( X\right)  = y}\right)  = \mathop{\sum }\limits_{\substack{{x \in  X\left( \Omega \right) } \\  {f\left( x\right)  = y} }}P\left( {X = x}\right)  = \mathop{\sum }\limits_{\substack{{{x}_{1} \in  {X}_{1}\left( \Omega \right) ,\ldots ,{x}_{n} \in  {X}_{n}\left( \Omega \right) } \\  {f\left( {{x}_{1},\ldots ,{x}_{n}}\right)  = y} }}P\left( {{X}_{1} = {x}_{1},\ldots ,{X}_{n} = {x}_{n}}\right) .
\]

Exemple 1. Une conséquence typique de ce résultat, est que la somme \( X + Y \) de deux variables aléatoires discrètes réelles \( X \) et \( Y \) , est une variable aléatoire discrète réelle, dont la valeur sur les singletons est donnée par

> Example 1. A typical consequence of this result is that the sum \( X + Y \) of two real discrete random variables \( X \) and \( Y \) is a real discrete random variable, whose value on singletons is given by

\[
P\left( {X + Y = z}\right)  = \mathop{\sum }\limits_{\substack{{x \in  X\left( \Omega \right) , y \in  Y\left( \Omega \right) } \\  {x + y = z} }}P\left( {X = x, Y = y}\right) .
\]

(Une somme de cette forme est appelée convolution). De même \( \min \left( {X, Y}\right) \) est une variable aléatoire discrète réelle, pour laquelle

> (A sum of this form is called a convolution). Similarly, \( \min \left( {X, Y}\right) \) is a real discrete random variable, for which

\[
P\left( {\min \left( {X, Y}\right)  = z}\right)  = \mathop{\sum }\limits_{\substack{{x \in  X\left( \Omega \right) , y \in  Y\left( \Omega \right) } \\  {y \geq  z} }}P\left( {X = z, Y = y}\right)  + \mathop{\sum }\limits_{\substack{{x \in  X\left( \Omega \right) , y \in  Y\left( \Omega \right) } \\  {x > z} }}P\left( {X = x, Y = z}\right) .
\]

Lois conditionnelles, indépendance.

> Conditional distributions, independence.

DéFINITION 4. Soient \( X \) et \( Y \) deux variables aléatoires discrètes de \( \Omega \) vers \( E \) . Soit \( y \in E \) tel que \( P\left( {Y = y}\right) \neq 0 \) . On appelle loi conditionnelle de \( X \) sachant \( \left( {Y = y}\right) \) la probabilité \( {P}_{y} \) définie sur \( X\left( \Omega \right) \) par

> DEFINITION 4. Let \( X \) and \( Y \) be two discrete random variables from \( \Omega \) to \( E \). Let \( y \in E \) be such that \( P\left( {Y = y}\right) \neq 0 \). The conditional distribution of \( X \) given \( \left( {Y = y}\right) \) is the probability \( {P}_{y} \) defined on \( X\left( \Omega \right) \) by

\[
\forall x \in  X\left( \Omega \right) ,\;{P}_{y}\left( {\{ x\} }\right)  = \frac{P\left( {X = x, Y = y}\right) }{P\left( {Y = y}\right) }.
\]

DéFINITION 5. Deux variables aléatoires discrètes \( X \) et \( Y \) de \( \Omega \) vers \( E \) sont dites indé- pendantes si pour toutes parties \( A \subset X\left( \Omega \right) \) et \( B \subset Y\left( \Omega \right) \) , on a

> DEFINITION 5. Two discrete random variables \( X \) and \( Y \) from \( \Omega \) to \( E \) are said to be independent if for all sets \( A \subset X\left( \Omega \right) \) and \( B \subset Y\left( \Omega \right) \), we have

\[
P\left( {X \in  A, Y \in  B}\right)  = P\left( {X \in  A}\right) P\left( {Y \in  B}\right) .
\]

Plus généralement,étant donnée une famille \( {\left( {X}_{i}\right) }_{i \in I} \) (éventuellement infinie) de variables aléatoires discrètes de \( \Omega \) vers \( E \) , on dit que les variables \( {\left( {X}_{i}\right) }_{i \in I} \) sont mutuellement indé- pendantes (ou plus simplement indépendantes) si pour toute partie finie \( J \subset I \) et pour toutes parties \( {\left( {A}_{j}\right) }_{j \in J} \) avec \( {A}_{j} \subset {X}_{j}\left( \Omega \right) \) pour tout \( j \in J \) , on a

> More generally, given a family \( {\left( {X}_{i}\right) }_{i \in I} \) (possibly infinite) of discrete random variables from \( \Omega \) to \( E \), the variables \( {\left( {X}_{i}\right) }_{i \in I} \) are said to be mutually independent (or more simply independent) if for any finite set \( J \subset I \) and for all sets \( {\left( {A}_{j}\right) }_{j \in J} \) with \( {A}_{j} \subset {X}_{j}\left( \Omega \right) \) for all \( j \in J \), we have

\[
P\left( {{ \cap  }_{j \in  J}\left\{  {{X}_{j} \in  {A}_{j}}\right\}  }\right)  = \mathop{\prod }\limits_{{j \in  J}}P\left( {{X}_{j} \in  {A}_{j}}\right) .
\]

Remarque 3. La définition ci dessous est générale et peut s'appliquer aux variables aléa-toires non discrètes. Dans le cas discret, il suffit d'avoir l'indépendance sur les singletons, comme l'affirme la propostion suivante.

> Remark 3. The definition below is general and can be applied to non-discrete random variables. In the discrete case, it suffices to have independence on singletons, as stated in the following proposition.

PROPOSITION 2. Avec les notations de la définition précédente, les variables aléatoires discrètes \( X \) et \( Y \) sont indépendantes si et seulement si

> PROPOSITION 2. With the notation of the previous definition, the discrete random variables \( X \) and \( Y \) are independent if and only if

\[
\forall \left( {x, y}\right)  \in  X\left( \Omega \right)  \times  Y\left( \Omega \right) ,\;P\left( {X = x, Y = y}\right)  = P\left( {X = x}\right) P\left( {Y = y}\right) .
\]

Les variables aléatoires discrètes \( {\left( {X}_{i}\right) }_{i \in I} \) sont mutuellement indépendantes si et seulement si pour toute partie finie \( J \subset I \) , on a

> The discrete random variables \( {\left( {X}_{i}\right) }_{i \in I} \) are mutually independent if and only if for any finite set \( J \subset I \), we have

\[
\forall {\left( {x}_{j}\right) }_{j \in  J} \in  \mathop{\prod }\limits_{{j \in  J}}{X}_{j}\left( \Omega \right) ,\;P\left( {{ \cap  }_{j \in  J}\left\{  {{X}_{j} = {x}_{j}}\right\}  }\right)  = \mathop{\prod }\limits_{{j \in  J}}P\left( {{X}_{j} = {x}_{j}}\right) .
\]

PROPOSITION 3. Soit \( m, n \in \mathbb{N} \) avec \( 1 \leq m < n \) . Soient \( {X}_{1},\ldots ,{X}_{n} \) des variables aléa-toires discrètes sur un espace probabilisé \( \left( {\Omega ,\mathcal{A}, P}\right) \) , et \( f : {X}_{1}\left( \Omega \right) \times \ldots \times {X}_{m}\left( \Omega \right) \rightarrow F \) , \( g : {X}_{m + 1}\left( \Omega \right) \times \ldots \times {X}_{n}\left( \Omega \right) \rightarrow {F}^{\prime } \) deux fonctions. Si les variables \( {X}_{1},\ldots ,{X}_{n} \) sont indé- pendantes, il en est de même des variables \( f\left( {{X}_{1},\ldots ,{X}_{m}}\right) \) et \( g\left( {{X}_{m + 1},\ldots ,{X}_{n}}\right) \) .

> PROPOSITION 3. Let \( m, n \in \mathbb{N} \) with \( 1 \leq m < n \). Let \( {X}_{1},\ldots ,{X}_{n} \) be discrete random variables on a probability space \( \left( {\Omega ,\mathcal{A}, P}\right) \), and \( f : {X}_{1}\left( \Omega \right) \times \ldots \times {X}_{m}\left( \Omega \right) \rightarrow F \), \( g : {X}_{m + 1}\left( \Omega \right) \times \ldots \times {X}_{n}\left( \Omega \right) \rightarrow {F}^{\prime } \) be two functions. If the variables \( {X}_{1},\ldots ,{X}_{n} \) are independent, then the variables \( f\left( {{X}_{1},\ldots ,{X}_{m}}\right) \) and \( g\left( {{X}_{m + 1},\ldots ,{X}_{n}}\right) \) are also independent.

Remarque 4. Dans le cas particulier \( m = 1 \) et \( n = 2 \) , cette proposition s’écrit : si \( X \) et \( Y \) sont deux variables aléatoires indépendantes et \( f \) et \( g \) deux fonctions définies sur \( X\left( \Omega \right) \) et \( Y\left( \Omega \right) \) , alors \( f\left( X\right) \) et \( g\left( Y\right) \) sont indépendantes.

> Remark 4. In the special case \( m = 1 \) and \( n = 2 \), this proposition is written as: if \( X \) and \( Y \) are two independent random variables and \( f \) and \( g \) are two functions defined on \( X\left( \Omega \right) \) and \( Y\left( \Omega \right) \), then \( f\left( X\right) \) and \( g\left( Y\right) \) are independent.
