#### 2.3. Exercises

*Français : 2.3. Exercices*

EXERCICE 1. Déterminer les solutions réelles définies sur \( \mathbb{R} \) (sauf dans la question 2/ b) où on demande les solutions sur \( \rbrack - \pi /2,\pi /2\lbrack ) \) des équations différentielles suivantes.

> EXERCISE 1. Determine the real solutions defined on \( \mathbb{R} \) (except in question 2/ b, where solutions on \( \rbrack - \pi /2,\pi /2\lbrack ) \) are requested) for the following differential equations.

1/ (Équations linéaires du premier ordre.)

> 1/ (First-order linear equations.)

a) \( {y}^{\prime } + y = \sin t;\; \) b) \( \left( {1 + {t}^{2}}\right) {y}^{\prime } = {ty} + \left( {1 + {t}^{2}}\right) ;\; \) c) \( \left( {1 - {t}^{2}}\right) {y}^{\prime } + {ty} = 0 \) .

> a) \( {y}^{\prime } + y = \sin t;\; \) b) \( \left( {1 + {t}^{2}}\right) {y}^{\prime } = {ty} + \left( {1 + {t}^{2}}\right) ;\; \) c) \( \left( {1 - {t}^{2}}\right) {y}^{\prime } + {ty} = 0 \) .

2/ (Équations linéaires du second ordre.)

> 2/ (Second-order linear equations.)

a) \( {y}^{\prime \prime } + 2{y}^{\prime } + y = t{e}^{t};\; \) b) \( {y}^{\prime \prime } + y = {\tan }^{2}t\;\left( {-\frac{\pi }{2} < t < \frac{\pi }{2}}\right) ;\; \) c) \( {t}^{2}{y}^{\prime \prime } - {2y} = 3{t}^{2} \) .

> a) \( {y}^{\prime \prime } + 2{y}^{\prime } + y = t{e}^{t};\; \) b) \( {y}^{\prime \prime } + y = {\tan }^{2}t\;\left( {-\frac{\pi }{2} < t < \frac{\pi }{2}}\right) ;\; \) c) \( {t}^{2}{y}^{\prime \prime } - {2y} = 3{t}^{2} \) .

---

Solution. 1/ a) On commence par résoudre l’équation homogène associée \( \left( H\right) : {y}^{\prime } + y = 0 \) , dont les solutions sont \( t \mapsto \lambda {e}^{-t}\left( {\lambda \in \mathbb{R}}\right) \) .

> Solution. 1/ a) We begin by solving the associated homogeneous equation \( \left( H\right) : {y}^{\prime } + y = 0 \) , whose solutions are \( t \mapsto \lambda {e}^{-t}\left( {\lambda \in \mathbb{R}}\right) \) .

Pour résoudre ( \( L \) ): \( {y}^{\prime } + y = \sin t \) , on applique la méthode de variation de la constante. On cherche une solution sous la forme \( t \mapsto \lambda \left( t\right) {e}^{-t} \) . Celle ci sera solution de \( \left( L\right) \) si et seulement si \( {\lambda }^{\prime }\left( t\right) {e}^{-t} = \sin t \) , c’est-à-dire \( {\lambda }^{\prime }\left( t\right) = {e}^{t}\sin t \) , ce qui par intégration équivaut à \( \lambda \left( t\right) = \mu + {e}^{t}(\sin t - \; \cos t)/2 \) , où \( \mu \) est une constante réelle. Finalement, les solutions sur \( \mathbb{R} \) de \( \left( L\right) \) sont les fonctions

> To solve ( \( L \) ): \( {y}^{\prime } + y = \sin t \) , we apply the method of variation of constants. We look for a solution in the form \( t \mapsto \lambda \left( t\right) {e}^{-t} \) . This will be a solution to \( \left( L\right) \) if and only if \( {\lambda }^{\prime }\left( t\right) {e}^{-t} = \sin t \) , that is to say \( {\lambda }^{\prime }\left( t\right) = {e}^{t}\sin t \) , which by integration is equivalent to \( \lambda \left( t\right) = \mu + {e}^{t}(\sin t - \; \cos t)/2 \) , where \( \mu \) is a real constant. Finally, the solutions on \( \mathbb{R} \) of \( \left( L\right) \) are the functions

\[
t \mapsto  \frac{\sin t - \cos t}{2} + \mu {e}^{-t},\;\mu  \in  \mathbb{R}.
\]

---

b) On procède de la même manière. Ici, l’équation homogène associée est \( \left( H\right) : \left( {1 + {t}^{2}}\right) {y}^{\prime } = {ty} \) , qui équivaut à \( {y}^{\prime } = \frac{t}{1 + {t}^{2}}y \) , dont les solutions sont les fonctions \( t \mapsto \lambda \sqrt{1 + {t}^{2}}\left( {\lambda \in \mathbb{R}}\right) \) .

> b) We proceed in the same way. Here, the associated homogeneous equation is \( \left( H\right) : \left( {1 + {t}^{2}}\right) {y}^{\prime } = {ty} \) , which is equivalent to \( {y}^{\prime } = \frac{t}{1 + {t}^{2}}y \) , whose solutions are the functions \( t \mapsto \lambda \sqrt{1 + {t}^{2}}\left( {\lambda \in \mathbb{R}}\right) \) .

Pour résoudre ( \( L \) ): \( {y}^{\prime } = \frac{t}{1 + {t}^{2}}y + 1 \) , on applique la méthode de variation de la constan La fonction \( t \mapsto \lambda \left( t\right) \sqrt{1 + {t}^{2}} \) est solution si et seulement si

> To solve ( \( L \) ): \( {y}^{\prime } = \frac{t}{1 + {t}^{2}}y + 1 \) , we apply the method of variation of constants. The function \( t \mapsto \lambda \left( t\right) \sqrt{1 + {t}^{2}} \) is a solution if and only if

\[
{\lambda }^{\prime }\left( t\right)  = \frac{1}{\sqrt{1 + {t}^{2}}} \Leftrightarrow  \lambda \left( t\right)  = \mu  + \log \left( {t + \sqrt{1 + {t}^{2}}}\right) ,\;\mu  \in  \mathbb{R}.
\]

Les solutions de \( \left( L\right) \) sont donc celles de la forme \( t \mapsto \mu \sqrt{1 + {t}^{2}} + \sqrt{1 + {t}^{2}}\log \left( {t + \sqrt{1 + {t}^{2}}}\right) \left( {\mu \in \mathbb{R}}\right) \) . c) On ne peut diviser l’équation par \( \left( {1 - {t}^{2}}\right) \) pour la rendre résolue que si \( t \notin \{ - 1,1\} \) . On a donc affaire à une équation incomplète. Nous allons la résoudre sur chacun des intervalles \( \rbrack - \infty , - 1\lbrack \) , \( \rbrack - 1,1\left\lbrack \text{ et }\right\rbrack 1, + \infty \lbrack \) puis "recoller" éventuellement les solutions pour trouver une solution définie sur \( \mathbb{R} \) tout entier.

> The solutions of \( \left( L\right) \) are therefore those of the form \( t \mapsto \mu \sqrt{1 + {t}^{2}} + \sqrt{1 + {t}^{2}}\log \left( {t + \sqrt{1 + {t}^{2}}}\right) \left( {\mu \in \mathbb{R}}\right) \) . c) We can only divide the equation by \( \left( {1 - {t}^{2}}\right) \) to put it in solved form if \( t \notin \{ - 1,1\} \) . We are therefore dealing with an incomplete equation. We will solve it on each of the intervals \( \rbrack - \infty , - 1\lbrack \) , \( \rbrack - 1,1\left\lbrack \text{ et }\right\rbrack 1, + \infty \lbrack \) and then potentially "glue" the solutions together to find a solution defined on the whole of \( \mathbb{R} \) .

On montre facilement que les solutions de \( \left( L\right) : {y}^{\prime } = \frac{t}{{t}^{2} - 1}y \) sont

> It is easy to show that the solutions of \( \left( L\right) : {y}^{\prime } = \frac{t}{{t}^{2} - 1}y \) are

- sur] \( - \infty , - 1\left\lbrack  {, t \mapsto  \lambda \sqrt{{t}^{2} - 1}\left( {\lambda  \in  \mathbb{R}}\right) }\right. \) ;

> - on] \( - \infty , - 1\left\lbrack  {, t \mapsto  \lambda \sqrt{{t}^{2} - 1}\left( {\lambda  \in  \mathbb{R}}\right) }\right. \) ;

- sur \( \rbrack  - 1,1\left\lbrack  {, t \mapsto  \mu \sqrt{1 - {t}^{2}}\left( {\mu  \in  \mathbb{R}}\right) }\right. \) ;

> - on \( \rbrack  - 1,1\left\lbrack  {, t \mapsto  \mu \sqrt{1 - {t}^{2}}\left( {\mu  \in  \mathbb{R}}\right) }\right. \) ;

- sur \( \rbrack 1, + \infty \left\lbrack  {, t \mapsto  \nu \sqrt{{t}^{2} - 1}\left( {\nu  \in  \mathbb{R}}\right) .}\right. \)

> - on \( \rbrack 1, + \infty \left\lbrack  {, t \mapsto  \nu \sqrt{{t}^{2} - 1}\left( {\nu  \in  \mathbb{R}}\right) .}\right. \)

Si \( \left( {\lambda ,\mu ,\nu }\right) \neq \left( {0,0,0}\right) \) , ces solutions ne peuvent, après prolongement, donner une solution sur \( \mathbb{R} \) tout entier (elle ne serait pas dérivable en -1 ou en 1). La seule solution de \( \left( L\right) \) définie sur \( \mathbb{R} \) est donc la fonction nulle.

> If \( \left( {\lambda ,\mu ,\nu }\right) \neq \left( {0,0,0}\right) \), these solutions cannot, after extension, provide a solution on the entire \( \mathbb{R} \) (it would not be differentiable at -1 or 1). The only solution to \( \left( L\right) \) defined on \( \mathbb{R} \) is therefore the zero function.

2/ a) L’équation homogène associée est \( \left( H\right) : {y}^{\prime \prime } + 2{y}^{\prime } + y = 0 \) . Son polynôme caractéristique est \( {X}^{2} + {2X} + 1 = {\left( X + 1\right) }^{2} \) , qui a une racine double en -1 . Les solutions de \( \left( H\right) \) sont donc celles de la forme \( t \mapsto \left( {{\lambda t} + \mu }\right) {e}^{-t}\left( {\lambda ,\mu \in \mathbb{R}}\right) \) .

> 2/ a) The associated homogeneous equation is \( \left( H\right) : {y}^{\prime \prime } + 2{y}^{\prime } + y = 0 \). Its characteristic polynomial is \( {X}^{2} + {2X} + 1 = {\left( X + 1\right) }^{2} \), which has a double root at -1. The solutions to \( \left( H\right) \) are therefore those of the form \( t \mapsto \left( {{\lambda t} + \mu }\right) {e}^{-t}\left( {\lambda ,\mu \in \mathbb{R}}\right) \).

Il nous reste à trouver une solution de \( \left( L\right) : {y}^{\prime \prime } + 2{y}^{\prime } + y = t{e}^{t} \) . On pourrait pour cela utiliser la méthode de variation des constantes. Ici, la forme du second membre nous invite à faire plus simple, et à rechercher une solution sous la forme \( t \mapsto \left( {a{t}^{2} + {bt} + c}\right) {e}^{t} \) . En reportant dans \( \left( L\right) \) et après identification, on trouve \( a = 0, b = 1/4, c = - 1/4 \) .

> We still need to find a solution to \( \left( L\right) : {y}^{\prime \prime } + 2{y}^{\prime } + y = t{e}^{t} \). We could use the method of variation of constants for this. Here, the form of the right-hand side invites us to do something simpler and look for a solution in the form \( t \mapsto \left( {a{t}^{2} + {bt} + c}\right) {e}^{t} \). By substituting into \( \left( L\right) \) and after identification, we find \( a = 0, b = 1/4, c = - 1/4 \).

La solution générale de \( \left( L\right) \) , somme d’une solution particulière de \( \left( L\right) \) et de la solution générale de \( \left( H\right) \) , est donc

> The general solution to \( \left( L\right) \), the sum of a particular solution to \( \left( L\right) \) and the general solution to \( \left( H\right) \), is therefore

\[
t \mapsto  \left( \frac{t - 1}{4}\right) {e}^{t} + \left( {{\lambda t} + \mu }\right) {e}^{-t},\;\left( {\lambda ,\mu }\right)  \in  {\mathbb{R}}^{2}.
\]

b) Les solutions de l’équation homogène associée sont les fonctions \( t \mapsto \lambda \cos t + \mu \sin t \) avec \( \left( {\lambda ,\mu }\right) \in {\mathbb{R}}^{2} \) . Pour trouver une solution de \( \left( L\right) : {y}^{\prime \prime } + y = {\tan }^{2}t \) , on applique la méthode de variation des constantes. Une fonction de la forme \( t \mapsto \lambda \left( t\right) \cos t + \mu \left( t\right) \sin t \) sera solution de \( \left( L\right) \) si et seulement si

> b) The solutions to the associated homogeneous equation are the functions \( t \mapsto \lambda \cos t + \mu \sin t \) with \( \left( {\lambda ,\mu }\right) \in {\mathbb{R}}^{2} \). To find a solution to \( \left( L\right) : {y}^{\prime \prime } + y = {\tan }^{2}t \), we apply the method of variation of constants. A function of the form \( t \mapsto \lambda \left( t\right) \cos t + \mu \left( t\right) \sin t \) will be a solution to \( \left( L\right) \) if and only if

\[
\left\{  {\begin{matrix} {\lambda }^{\prime }\cos t + {\mu }^{\prime }\sin t = 0 \\  {\lambda }^{\prime }\left( {-\sin t}\right)  + {\mu }^{\prime }\cos t = {\tan }^{2}t \end{matrix} \Leftrightarrow  {\lambda }^{\prime }\left( t\right)  =  - \frac{{\sin }^{3}t}{{\cos }^{2}t}\text{ et }{\mu }^{\prime }\left( t\right)  = \frac{{\sin }^{2}t}{\cos t},}\right.
\]

et par intégration on en déduit

> and by integration we deduce

\[
\lambda \left( t\right)  = \alpha  - \cos t - \frac{1}{\cos t},\;\mu \left( t\right)  = \beta  - \sin t + \log \left\lbrack  {\tan \left( {\frac{\pi }{4} + \frac{t}{2}}\right) }\right\rbrack  ,\;\left( {\alpha ,\beta }\right)  \in  {\mathbb{R}}^{2}.
\]

La solution générale de \( \left( L\right) \) est donc

> The general solution to \( \left( L\right) \) is therefore

\[
\rbrack  - \frac{\pi }{2},\frac{\pi }{2}\left\lbrack  { \rightarrow  \mathbb{R}\;t \mapsto  \alpha \cos t + \beta \sin t - 2 + \sin t\log \left\lbrack  {\tan \left( {\frac{\pi }{4} + \frac{t}{2}}\right) }\right\rbrack  ,\;\left( {\alpha ,\beta }\right)  \in  {\mathbb{R}}^{2}.}\right.
\]

c) Remarquons que les fonctions \( t \mapsto {t}^{2} \) et \( t \mapsto 1/t \) sont solutions de \( \left( H\right) : {t}^{2}{y}^{\prime \prime } - {2y} = 0 \) (attention, ici l’équation est incomplète ; il faut résoudre sur ] — ∞, 0 [ et sur ]0, +∞[, puis recoller les solutions par prolongement pour trouver des solutions définies sur \( \mathbb{R} \) tout entier). Sur chaque intervalle \( \rbrack - \infty ,0\left\lbrack \text{ et }\right\rbrack 0, + \infty \lbrack \) , ces deux solutions forment une base de l’e.v des solutions de \( \left( H\right) \) .

> c) Note that the functions \( t \mapsto {t}^{2} \) and \( t \mapsto 1/t \) are solutions to \( \left( H\right) : {t}^{2}{y}^{\prime \prime } - {2y} = 0 \) (be careful, here the equation is incomplete; one must solve on ] — ∞, 0 [ and on ]0, +∞[, then join the solutions by extension to find solutions defined on the entire \( \mathbb{R} \)). On each interval \( \rbrack - \infty ,0\left\lbrack \text{ et }\right\rbrack 0, + \infty \lbrack \), these two solutions form a basis for the vector space of solutions to \( \left( H\right) \).

La méthode de variation des constantes va une fois de plus nous permettre de trouver une solution de \( \left( L\right) : {y}^{\prime \prime } - {2y}/{t}^{2} = 3 \) . La fonction \( t \mapsto \lambda \left( t\right) {t}^{2} + \mu \left( t\right) /t \) sera solution si et seulement si

> The method of variation of constants will once again allow us to find a solution to \( \left( L\right) : {y}^{\prime \prime } - {2y}/{t}^{2} = 3 \). The function \( t \mapsto \lambda \left( t\right) {t}^{2} + \mu \left( t\right) /t \) will be a solution if and only if

\[
\left\{  \begin{array}{l} {\lambda }^{\prime }{t}^{2} + {\mu }^{\prime }/t = 0 \\  {2t}{\lambda }^{\prime } - {\mu }^{\prime }/{t}^{2} = 3 \end{array}\right.  \Leftrightarrow  {\lambda }^{\prime } = \frac{1}{t}\text{ et }{\mu }^{\prime } =  - {t}^{2},
\]

ce qui équivaut à \( \lambda \left( t\right) = \alpha + \log \left| t\right| \) et \( \mu \left( t\right) = \beta - {t}^{3}/3\left( {\alpha ,\beta \in \mathbb{R}}\right) \) , d’où les solutions de \( \left( L\right) \) :

> which is equivalent to \( \lambda \left( t\right) = \alpha + \log \left| t\right| \) and \( \mu \left( t\right) = \beta - {t}^{3}/3\left( {\alpha ,\beta \in \mathbb{R}}\right) \) , hence the solutions of \( \left( L\right) \) :

\[
t \mapsto  {\alpha }_{1}{t}^{2} + \frac{{\beta }_{1}}{t} + {t}^{2}\log \left| t\right|  - \frac{{t}^{2}}{3}\;\text{ sur }\;\rbrack  - \infty ,0\lbrack ,\;{\alpha }_{1},{\beta }_{1} \in  \mathbb{R}
\]

\[
t \mapsto  {\alpha }_{2}{t}^{2} + \frac{{\beta }_{2}}{t} + {t}^{2}\log t - \frac{{t}^{2}}{3}\;\text{ sur }\;\rbrack 0, + \infty \lbrack ,\;{\alpha }_{2},{\beta }_{2} \in  \mathbb{R}.
\]

Pour que ces solutions puissent se prolonger pour donner une solution sur \( \mathbb{R} \) tout entier, il faut avoir \( {\beta }_{1} = {\beta }_{2} = 0 \) (pour avoir une limite finie en 0 \( ) \) . Dans ce cas, on remarque que le raccord est dérivable en 0, n’est pas deux fois dérivable en 0 (à cause du terme en \( {t}^{2}\log \left| t\right| \) ). Il n’y a donc pas de solution sur \( \mathbb{R} \) .

> For these solutions to be extended to provide a solution on the whole of \( \mathbb{R} \) , we must have \( {\beta }_{1} = {\beta }_{2} = 0 \) (to have a finite limit at 0 \( ) \) . In this case, we note that the junction is differentiable at 0, but not twice differentiable at 0 (due to the term in \( {t}^{2}\log \left| t\right| \) ). There is therefore no solution on \( \mathbb{R} \) .

Remarque. La méthode utilisée dans la question 2/ a) se généralise comme suit. Soit (L) : \( {y}^{\left( n\right) } + {a}_{1}{y}^{\left( n - 1\right) } + \cdots + {a}_{n - 1}{y}^{\prime } + {a}_{n}y = {e}^{\lambda t}P\left( t\right) \) une équation différentielle linéaire, où les \( {a}_{i} \) et \( \lambda \) sont des constantes et \( P \) un polynôme de degré \( q \) . Soit \( \chi \) le polynôme caractéristique \( {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) , et soit \( m \) l’ordre de multiplicité de la racine éventuelle \( \lambda \) de \( \chi \) (en convenant \( m = 0 \) si \( \chi \left( \lambda \right) \neq 0 \) ). Alors l’équation \( \left( L\right) \) admet une unique solution de la forme \( t \mapsto {t}^{m}{e}^{\lambda t}Q\left( t\right) \) , où \( Q \) est un polynôme de degré \( q \) .

> Remark. The method used in question 2/ a) generalizes as follows. Let (L) : \( {y}^{\left( n\right) } + {a}_{1}{y}^{\left( n - 1\right) } + \cdots + {a}_{n - 1}{y}^{\prime } + {a}_{n}y = {e}^{\lambda t}P\left( t\right) \) be a linear differential equation, where the \( {a}_{i} \) and \( \lambda \) are constants and \( P \) is a polynomial of degree \( q \) . Let \( \chi \) be the characteristic polynomial \( {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) , and let \( m \) be the multiplicity of the potential root \( \lambda \) of \( \chi \) (agreeing \( m = 0 \) if \( \chi \left( \lambda \right) \neq 0 \) ). Then the equation \( \left( L\right) \) admits a unique solution of the form \( t \mapsto {t}^{m}{e}^{\lambda t}Q\left( t\right) \) , where \( Q \) is a polynomial of degree \( q \) .

EXERCICE 2. Déterminer les solutions réelles des systèmes différentiels suivant :

> EXERCISE 2. Determine the real solutions of the following differential systems:

\[
\text{ a) }\left\{  \begin{array}{l} {x}^{\prime } = x + z \\  {y}^{\prime } =  - y - z \\  {z}^{\prime } = {2y} + z \end{array}\right. \;\text{ b) }\left\{  \begin{array}{l} {x}^{\prime \prime } + {x}^{\prime } + 4{y}^{\prime } - x - {3y} = 0 \\  {y}^{\prime \prime } - 2{y}^{\prime } + x + {3y} = 0 \end{array}\right.
\]

Solution. a) Soit \( A \) la matrice \( \left( \begin{matrix} 1 & 0 & 1 \\ 0 & - 1 & - 1 \\ 0 & 2 & 1 \end{matrix}\right) \) , de sorte que le système s’écrit \( {X}^{\prime } = {AX} \) , avec \( X = \left( \begin{matrix} x \\ y \\ z \end{matrix}\right) \) . Pour déterminer les solutions, nous diagonalisons \( A \) . On calcule facilement son polynôme caractéristique \( {P}_{A} = - \left( {X - 1}\right) \left( {{X}^{2} + 1}\right) = - \left( {X - 1}\right) \left( {X + i}\right) \left( {X - i}\right) \) , et après calculs, les sous-espaces propres sont

> Solution. a) Let \( A \) be the matrix \( \left( \begin{matrix} 1 & 0 & 1 \\ 0 & - 1 & - 1 \\ 0 & 2 & 1 \end{matrix}\right) \) , so that the system is written \( {X}^{\prime } = {AX} \) , with \( X = \left( \begin{matrix} x \\ y \\ z \end{matrix}\right) \) . To determine the solutions, we diagonalize \( A \) . We easily calculate its characteristic polynomial \( {P}_{A} = - \left( {X - 1}\right) \left( {{X}^{2} + 1}\right) = - \left( {X - 1}\right) \left( {X + i}\right) \left( {X - i}\right) \) , and after calculations, the eigenspaces are

\[
\operatorname{Ker}\left( {A - I}\right)  = \mathbb{C}\left( \begin{array}{l} 1 \\  0 \\  0 \end{array}\right) ,\;\operatorname{Ker}\left( {A - {iI}}\right)  = \mathbb{C}\left( \begin{matrix} 1 + i \\  1 - i \\   - 2 \end{matrix}\right) ,\;\operatorname{Ker}\left( {A + {iI}}\right)  = \mathbb{C}\left( \begin{matrix} 1 - i \\  1 + i \\   - 2 \end{matrix}\right) .
\]

Remarquons que \( A \) se diagonalise dans \( {\mathbb{C}}^{3} \) . On va donc trouver des solutions complexes, puis on déterminera les solutions réelles en prenant les parties réelles et imaginaires.

> Note that \( A \) diagonalizes in \( {\mathbb{C}}^{3} \) . We will therefore find complex solutions, then we will determine the real solutions by taking the real and imaginary parts.

Soit \( \lambda \in \{ 1, i, - i\} \) . Si \( X : \mathbb{R} \rightarrow {\mathbb{C}}^{3}\;t \mapsto X\left( t\right) \) est solution et vérifie \( X\left( t\right) \in \operatorname{Ker}\left( {A - {\lambda I}}\right) \) pour tout \( t \) , on a \( {X}^{\prime } = {AX} = {\lambda X} \) , donc \( X = {e}^{\lambda t}X\left( 0\right) \) , où \( X\left( 0\right) \in \operatorname{Ker}\left( {A - {\lambda I}}\right) \) . Réciproquement, on vérifie facilement que ainsi définie, \( X \) est bien solution. Par linéarité, on en déduit donc que les fonctions

> Let \( \lambda \in \{ 1, i, - i\} \) . If \( X : \mathbb{R} \rightarrow {\mathbb{C}}^{3}\;t \mapsto X\left( t\right) \) is a solution and satisfies \( X\left( t\right) \in \operatorname{Ker}\left( {A - {\lambda I}}\right) \) for all \( t \) , we have \( {X}^{\prime } = {AX} = {\lambda X} \) , thus \( X = {e}^{\lambda t}X\left( 0\right) \) , where \( X\left( 0\right) \in \operatorname{Ker}\left( {A - {\lambda I}}\right) \) . Conversely, it is easy to verify that \( X \) , as defined, is indeed a solution. By linearity, we therefore deduce that the functions

\[
t \mapsto  \alpha {e}^{t}\left( \begin{array}{l} 1 \\  0 \\  0 \end{array}\right)  + \beta {e}^{it}\left( \begin{matrix} 1 + i \\  1 - i \\   - 2 \end{matrix}\right)  + \gamma {e}^{-{it}}\left( \begin{matrix} 1 - i \\  1 + i \\   - 2 \end{matrix}\right) ,\;\left( {\alpha ,\beta ,\gamma  \in  \mathbb{C}}\right)
\]

sont des solutions. L'espace des solutions étant de dimension 3 (voir le théorème 2), on en déduit que ceci est la solution générale (complexe). Pour obtenir la solution réelle générale, on prend les parties réelles et imaginaires. On en conclut facilement que la solution réelle générale est

> are solutions. Since the solution space is of dimension 3 (see theorem 2), we deduce that this is the general (complex) solution. To obtain the general real solution, we take the real and imaginary parts. We easily conclude that the general real solution is

\[
t \mapsto  \left( \begin{matrix} x\left( t\right) \\  y\left( t\right) \\  z\left( t\right)  \end{matrix}\right)  = \lambda {e}^{t}\left( \begin{array}{l} 1 \\  0 \\  0 \end{array}\right)  + \mu \left( \begin{matrix} \cos t - \sin t \\  \cos t + \sin t \\   - 2\cos t \end{matrix}\right)  + \nu \left( \begin{matrix} \sin t + \cos t \\  \sin t - \cos t \\   - 2\sin t \end{matrix}\right) ,\;\lambda ,\mu ,\nu  \in  \mathbb{R}.
\]

b) Notons (i) la première équation du système et (ii) la seconde. En additionnant (i) et (ii), on obtient \( {\left( {x}^{\prime } + {y}^{\prime }\right) }^{\prime } + \left( {{x}^{\prime } + {y}^{\prime }}\right) = 0 \) , donc \( {x}^{\prime } + {y}^{\prime } \) est solution de l’équation différentielle \( {z}^{\prime } + z = 0 \) , donc il existe \( \lambda \in \mathbb{R} \) tel que \( {x}^{\prime } + {y}^{\prime } = \lambda {e}^{-t} \) . Par intégration, on en déduit l’existence de deux constantes \( \alpha ,\beta \in \mathbb{R} \) telles que \( x + y = \alpha + \beta {e}^{-t} \) . En remplaçant cette égalité dans (ii), on obtient (iii) : \( {y}^{\prime \prime } - 3{y}^{\prime } + {2y} = - \alpha - \beta {e}^{-t} \) . L’équation homogène associée est \( \left( {iv}\right) : {y}^{\prime \prime } - 3{y}^{\prime } + {2y} = 0 \) . Son polynôme caractéristique est \( \left( {X - 1}\right) \left( {X - 2}\right) \) , les solutions de (iv) sont donc de la forme \( t \mapsto \gamma {e}^{t} + \delta {e}^{2t} \) , avec \( \gamma ,\delta \in \mathbb{R} \) . On recherche une solution particulière de (iii) sous la forme \( t \mapsto a + b{e}^{-t} \) . En remplaçant et après identification, on obtient \( a = - \beta /2, b = - \alpha /6 \) , et on en déduit que la solution générale de (iii) est

> b) Let (i) be the first equation of the system and (ii) the second. By adding (i) and (ii), we obtain \( {\left( {x}^{\prime } + {y}^{\prime }\right) }^{\prime } + \left( {{x}^{\prime } + {y}^{\prime }}\right) = 0 \) , so \( {x}^{\prime } + {y}^{\prime } \) is a solution to the differential equation \( {z}^{\prime } + z = 0 \) , therefore there exists \( \lambda \in \mathbb{R} \) such that \( {x}^{\prime } + {y}^{\prime } = \lambda {e}^{-t} \) . By integration, we deduce the existence of two constants \( \alpha ,\beta \in \mathbb{R} \) such that \( x + y = \alpha + \beta {e}^{-t} \) . Substituting this equality into (ii), we obtain (iii): \( {y}^{\prime \prime } - 3{y}^{\prime } + {2y} = - \alpha - \beta {e}^{-t} \) . The associated homogeneous equation is \( \left( {iv}\right) : {y}^{\prime \prime } - 3{y}^{\prime } + {2y} = 0 \) . Its characteristic polynomial is \( \left( {X - 1}\right) \left( {X - 2}\right) \) , so the solutions to (iv) are of the form \( t \mapsto \gamma {e}^{t} + \delta {e}^{2t} \) , with \( \gamma ,\delta \in \mathbb{R} \) . We look for a particular solution to (iii) in the form \( t \mapsto a + b{e}^{-t} \) . By substituting and after identification, we obtain \( a = - \beta /2, b = - \alpha /6 \) , and we deduce that the general solution to (iii) is

\[
t \mapsto   - \frac{\beta }{2} - \frac{\alpha }{6}{e}^{-t} + \gamma {e}^{t} + \delta {e}^{2t},\;\gamma ,\delta  \in  \mathbb{R}.
\]

Or on a vu plus haut que \( x = \beta + \alpha {e}^{-t} - y \) , donc la solution générale du système est

> However, we saw above that \( x = \beta + \alpha {e}^{-t} - y \) , so the general solution to the system is

\[
t \mapsto  \left( \begin{matrix} x\left( t\right) \\  y\left( t\right)  \end{matrix}\right)  = \beta \left( \begin{matrix} 3 \\   - 1 \end{matrix}\right)  + \alpha {e}^{-t}\left( \begin{matrix} 7 \\   - 1 \end{matrix}\right)  + \gamma {e}^{t}\left( \begin{matrix} 1 \\   - 1 \end{matrix}\right)  + \delta {e}^{2t}\left( \begin{matrix} 1 \\   - 1 \end{matrix}\right) ,\;\left( {\alpha ,\beta ,\gamma ,\delta }\right)  \in  {\mathbb{R}}^{4}.
\]

Remarque. Dans la question a), on aurait aussi pu trouver les solutions en passant par les exponentielles de matrice. D'ailleurs, la méthode que nous avons utilisée ne s'applique plus lorsque la matrice n'est pas diagonalisable.

> Remark. In question a), we could also have found the solutions by using matrix exponentials. Moreover, the method we used no longer applies when the matrix is not diagonalizable.

Dans la question b), la technique que nous avons employée n'est pas toujours applicable : parfois, des transformations linéaires simples sur les équations du système ne permettent pas de le réduire facilement. On peut utiliser une méthode systématique, qui consiste a transformer le système en un système d'ordre 1. Ici, le système b) s'écrit aussi \( {X}^{\prime \prime } + A{X}^{\prime } + {BX} = 0 \) avec \( X = \left( \begin{matrix} x \\ y \end{matrix}\right) , A = \left( \begin{matrix} 1 & 4 \\ 0 & - 3 \end{matrix}\right) \) et \( A = \left( \begin{matrix} - 1 & - 3 \\ 1 & 3 \end{matrix}\right) \) , et on le transforme en

> In question b), the technique we used is not always applicable: sometimes, simple linear transformations on the system's equations do not allow for easy reduction. We can use a systematic method, which consists of transforming the system into a first-order system. Here, system b) can also be written as \( {X}^{\prime \prime } + A{X}^{\prime } + {BX} = 0 \) with \( X = \left( \begin{matrix} x \\ y \end{matrix}\right) , A = \left( \begin{matrix} 1 & 4 \\ 0 & - 3 \end{matrix}\right) \) and \( A = \left( \begin{matrix} - 1 & - 3 \\ 1 & 3 \end{matrix}\right) \), and we transform it into

\[
\left( \begin{matrix} {X}^{\prime } \\  {Y}^{\prime } \end{matrix}\right)  = \left( \begin{matrix} 0 & I \\   - B &  - A \end{matrix}\right) \left( \begin{array}{l} X \\  Y \end{array}\right) ,
\]

système que l'on sait désormais résoudre.

> a system that we now know how to solve.

EXERCICE 3. Déterminer l’ensemble des fonctions \( f : \rbrack 0, + \infty \lbrack \rightarrow \mathbb{R} \) qui sont dérivables et qui vérifient \( \left( E\right) : {f}^{\prime }\left( t\right) = f\left( {1/t}\right) \) pour tout \( t > 0 \) .

> EXERCISE 3. Determine the set of functions \( f : \rbrack 0, + \infty \lbrack \rightarrow \mathbb{R} \) that are differentiable and satisfy \( \left( E\right) : {f}^{\prime }\left( t\right) = f\left( {1/t}\right) \) for all \( t > 0 \).

Solution. Si \( f \) vérifie \( \left( E\right) \) , alors \( {f}^{\prime } \) est dérivable sur \( \rbrack 0, + \infty \left\lbrack \right. \) (car \( \left. {{f}^{\prime }\left( t\right) = f\left( {1/t}\right) }\right) \) , et en dérivant \( \left( E\right) \) , on voit que

> Solution. If \( f \) satisfies \( \left( E\right) \), then \( {f}^{\prime } \) is differentiable on \( \rbrack 0, + \infty \left\lbrack \right. \) (because \( \left. {{f}^{\prime }\left( t\right) = f\left( {1/t}\right) }\right) \), and by differentiating \( \left( E\right) \), we see that

\[
\forall t > 0,\;{f}^{\prime \prime }\left( t\right)  =  - \frac{1}{{t}^{2}}{f}^{\prime }\left( \frac{1}{t}\right)  =  - \frac{1}{{t}^{2}}f\left( \frac{1}{1/t}\right)  =  - \frac{f\left( t\right) }{{t}^{2}},
\]

autrement dit, \( f \) est solution sur \( \rbrack 0, + \infty \left\lbrack \right. \) de l’équation différentielle \( \left( L\right) : {t}^{2}{y}^{\prime \prime } + y = 0 \) . Ce type d'équation différentielle est classique et s'appelle équation d'Euler. On peut la résoudre sur chacun des intervalles \( \rbrack - \infty ,0\left\lbrack \text{ et }\right\rbrack 0, + \infty \lbrack \) en effectuant le changement de variable \( t = \pm {e}^{x} \) , nous ramenant ainsi à une équation différentielle linéaire homogène d'ordre 2 à coefficients constants (voir la remarque à la fin de l'exercice). Ici, nous allons utiliser une technique différente.

> in other words, \( f \) is a solution on \( \rbrack 0, + \infty \left\lbrack \right. \) to the differential equation \( \left( L\right) : {t}^{2}{y}^{\prime \prime } + y = 0 \). This type of differential equation is classic and is called an Euler equation. It can be solved on each of the intervals \( \rbrack - \infty ,0\left\lbrack \text{ et }\right\rbrack 0, + \infty \lbrack \) by performing the change of variable \( t = \pm {e}^{x} \), thus reducing it to a second-order homogeneous linear differential equation with constant coefficients (see the remark at the end of the exercise). Here, we will use a different technique.

On veut résoudre \( \left( L\right) \) sur ]0, \( + \infty \) [. Nous allons commencer par en rechercher les solutions complexes. La forme de \( \left( L\right) \) nous invite à rechercher des solutions particulières sous la forme \( t \mapsto \; {t}^{\alpha } \) , où \( \alpha \) est une constante complexe. Ceci sera le cas si et seulement si \( {t}^{2}\left( {\alpha \left( {\alpha - 1}\right) {t}^{\alpha - 2}}\right) + {t}^{\alpha } = 0 \) pour tout \( t > 0 \) , ce qui équivaut à \( \alpha \left( {\alpha - 1}\right) + 1 = 0 \) . Ainsi, si \( \alpha \) est racine du polynôme \( P = X\left( {X - 1}\right) + 1 = {X}^{2} - X + 1 \) , l’application \( t \mapsto {t}^{\alpha } \) est solution de \( \left( L\right) \) sur ] \( 0, + \infty \lbrack \) . Le polynôme \( P \) a deux racines distinctes qui sont \( {\alpha }_{1} = \frac{1}{2} + i\frac{\sqrt{3}}{2} \) et \( {\alpha }_{2} = \frac{1}{2} - i\frac{\sqrt{3}}{2} = \overline{{\alpha }_{1}} \) , on a donc trouvé deux solutions de \( \left( L\right) \) qui sont linéairement indépendantes. L'ensemble des solutions de l’équation linéaire homogène \( \left( L\right) \) formant un \( \mathbb{C} \) -espace vectoriel de dimension 2, on en déduit que la solution générale de \( \left( L\right) \) est

> We want to solve \( \left( L\right) \) on ]0, \( + \infty \) [. We will start by looking for its complex solutions. The form of \( \left( L\right) \) invites us to look for particular solutions of the form \( t \mapsto \; {t}^{\alpha } \) , where \( \alpha \) is a complex constant. This will be the case if and only if \( {t}^{2}\left( {\alpha \left( {\alpha - 1}\right) {t}^{\alpha - 2}}\right) + {t}^{\alpha } = 0 \) for all \( t > 0 \) , which is equivalent to \( \alpha \left( {\alpha - 1}\right) + 1 = 0 \) . Thus, if \( \alpha \) is a root of the polynomial \( P = X\left( {X - 1}\right) + 1 = {X}^{2} - X + 1 \) , the mapping \( t \mapsto {t}^{\alpha } \) is a solution to \( \left( L\right) \) on ] \( 0, + \infty \lbrack \) . The polynomial \( P \) has two distinct roots which are \( {\alpha }_{1} = \frac{1}{2} + i\frac{\sqrt{3}}{2} \) and \( {\alpha }_{2} = \frac{1}{2} - i\frac{\sqrt{3}}{2} = \overline{{\alpha }_{1}} \) , so we have found two solutions to \( \left( L\right) \) that are linearly independent. Since the set of solutions to the homogeneous linear equation \( \left( L\right) \) forms a \( \mathbb{C} \) -vector space of dimension 2, we deduce that the general solution to \( \left( L\right) \) is

\[
t \mapsto  a{t}^{{\alpha }_{1}} + b{t}^{{\alpha }_{2}},\;a, b \in  \mathbb{C}.
\]

(*)

> Finalement, nous venons de montrer que si \( f \) est une solution complexe de \( \left( E\right) \) , elle est de la forme (*). Réciproquement, une fonction de la forme (*) est solution si et seulement si

Finally, we have just shown that if \( f \) is a complex solution to \( \left( E\right) \) , it is of the form (*). Conversely, a function of the form (*) is a solution if and only if

\[
\forall t > 0,\;a{\alpha }_{1}{t}^{{\alpha }_{1} - 1} + b{\alpha }_{2}{t}^{{\alpha }_{2} - 1} = a{t}^{-{\alpha }_{1}} + b{t}^{-{\alpha }_{2}},
\]

ce qui en remplaçant \( {\alpha }_{1} \) et \( {\alpha }_{2} \) par leurs valeurs s’écrit aussi

> which, by replacing \( {\alpha }_{1} \) and \( {\alpha }_{2} \) with their values, can also be written as

\[
\forall t > 0,\;a\left( {\frac{1}{2} + i\frac{\sqrt{3}}{2}}\right) {t}^{-1/2 + i\sqrt{3}/2} + b\left( {\frac{1}{2} - i\frac{\sqrt{3}}{2}}\right) {t}^{-1/2 - i\sqrt{3}/2} = a{t}^{-1/2 - i\sqrt{3}/2} + b{t}^{-1/2 + i\sqrt{3}/2}.
\]

Ceci sera vérifié si et seulement si

> This will be verified if and only if

\[
a\left( {\frac{1}{2} + i\frac{\sqrt{3}}{2}}\right)  = b\;\text{ et }\;b\left( {\frac{1}{2} - i\frac{\sqrt{3}}{2}}\right)  = a,\;\text{ ou encore }\;a{e}^{{i\pi }/3} = b\;\text{ et }\;b{e}^{-{i\pi }/3} = a.
\]

Ces deux équations sont liées, et elles sont équivalentes à l'existence d'un nombre complexe \( c \) tel que \( a = c{e}^{-{i\pi }/6} \) et \( b = c{e}^{{i\pi }/6} \) . Finalement, \( f \) est une solution complexe \( \operatorname{de}\left( E\right) \) si et seulement si elle est de la forme

> These two equations are linked, and they are equivalent to the existence of a complex number \( c \) such that \( a = c{e}^{-{i\pi }/6} \) and \( b = c{e}^{{i\pi }/6} \) . Finally, \( f \) is a complex solution \( \operatorname{de}\left( E\right) \) if and only if it is of the form

\[
t \mapsto  c\left( {{e}^{-{i\pi }/6}{t}^{1/2 + i\sqrt{3}/2} + {e}^{{i\pi }/6}{t}^{1/2 - i\sqrt{3}/2}}\right)  = c{t}^{1/2}\cos \left( {\frac{\sqrt{3}}{2}\log t - \frac{\pi }{6}}\right) ,\;c \in  \mathbb{C}.
\]

On en déduit que la solution réelle générale de \( \left( E\right) \) est la même que la précédente, où la constante \( c \) doit être prise dans \( \mathbb{R} \) .

> We deduce that the general real solution to \( \left( E\right) \) is the same as the previous one, where the constant \( c \) must be taken in \( \mathbb{R} \) .

Remarque. De manière générale, on appelle équation d'Euler les équations linéaires ho-mogènes du type

> Remark. In general, Euler equations are homogeneous linear equations of the type

\[
{t}^{n}{y}^{\left( n\right) } + {a}_{1}{t}^{n - 1}{y}^{\left( n - 1\right) } + \cdots  + {a}_{n - 1}t{y}^{\prime } + {a}_{n}y = 0,
\]

\( \left( {* * }\right) \)

> où les \( {a}_{i} \) sont des constantes complexes. En effectuant le changement de variable \( t = \varepsilon {e}^{x} \) , \( \left( {\varepsilon \in \{ - 1,1\} }\right) \) , on ramène cette équation à une équation linéaire homogène à coefficients constants d'ordre \( n \) que l’on sait résoudre.

where the \( {a}_{i} \) are complex constants. By performing the change of variable \( t = \varepsilon {e}^{x} \) , \( \left( {\varepsilon \in \{ - 1,1\} }\right) \) , we reduce this equation to a homogeneous linear equation with constant coefficients of order \( n \) that we know how to solve.

> La technique que nous avons utilisée dans l'exercice pour résoudre ce type d'équations est de rechercher des solutions particulières sous la forme \( t \mapsto {t}^{\alpha } \) . En remplaçant dans (**), on trouve que ceci donne une solution si et seulement si \( \alpha \) est racine d’un certain polynôme \( P \) de degré \( n \) . Si \( P \) a ses \( n \) racines distinctes, alors cette méthode nous donne \( n \) solutions linéairement indépendantes, et on en déduit toutes les solutions puisque l'espace des solutions est de dimension \( n \) . Par contre, si \( P \) a une ou plusieurs racines multiples, ceci ne nous donne qu’un nombre \( < n \) de solutions indépendantes, et on ne peut donc pas en déduire toutes les solutions par cette méthode. Il faut procéder comme décrit précédemment.

The technique we used in the exercise to solve this type of equation is to look for particular solutions in the form \( t \mapsto {t}^{\alpha } \) . By substituting into (**), we find that this yields a solution if and only if \( \alpha \) is a root of a certain polynomial \( P \) of degree \( n \) . If \( P \) has its \( n \) distinct roots, then this method gives us \( n \) linearly independent solutions, and we can deduce all solutions from this since the solution space is of dimension \( n \) . However, if \( P \) has one or more multiple roots, this only gives us a number \( < n \) of independent solutions, and we therefore cannot deduce all solutions using this method. We must proceed as described previously.

> EXERCICE 4 (SOLUTIONS D'UNE ÉQUATION DIFFÉRENTIELLE D'ORDRE n À COEFFICIENTS CONSTANTS). Pour tout polynôme complexe \( P = \mathop{\sum }\limits_{{i = 0}}^{n}{a}_{i}{X}^{i} \) et pour toute fonc-tion \( f : \mathbb{R} \rightarrow \mathbb{C} \) de classe \( {\mathcal{C}}^{n} \) , on note

EXERCISE 4 (SOLUTIONS TO AN n-th ORDER DIFFERENTIAL EQUATION WITH CONSTANT COEFFICIENTS). For any complex polynomial \( P = \mathop{\sum }\limits_{{i = 0}}^{n}{a}_{i}{X}^{i} \) and any function \( f : \mathbb{R} \rightarrow \mathbb{C} \) of class \( {\mathcal{C}}^{n} \), we denote

\[
P\left( D\right) \left( f\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{a}_{i}{f}^{\left( i\right) } = {a}_{n}{f}^{\left( n\right) } + \cdots  + {a}_{1}{f}^{\prime } + {a}_{0}f
\]

(D est l'opérateur de dérivation).

> (D is the differentiation operator).

a) Pour tout polynôme \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) , on note \( {\mathcal{S}}_{P} \) l’espace des solutions de l’équation différentielle \( P\left( D\right) \left( y\right) = 0 \) . Si \( {P}_{1},\ldots ,{P}_{k} \in \mathbb{C}\left\lbrack X\right\rbrack \) sont des polynômes premiers entre eux deux à deux, montrer que \( {\mathcal{S}}_{{P}_{1}\cdots {P}_{k}} = {\mathcal{S}}_{{P}_{1}} \oplus \cdots \oplus {\mathcal{S}}_{{P}_{k}} \) .

> a) For any polynomial \( P \in \mathbb{C}\left\lbrack X\right\rbrack \), we denote by \( {\mathcal{S}}_{P} \) the space of solutions to the differential equation \( P\left( D\right) \left( y\right) = 0 \). If \( {P}_{1},\ldots ,{P}_{k} \in \mathbb{C}\left\lbrack X\right\rbrack \) are pairwise coprime polynomials, show that \( {\mathcal{S}}_{{P}_{1}\cdots {P}_{k}} = {\mathcal{S}}_{{P}_{1}} \oplus \cdots \oplus {\mathcal{S}}_{{P}_{k}} \).

b) Si \( {P}_{n}\left( X\right) = {\left( X - \alpha \right) }^{n} \) , déterminer la forme des solutions de l’équation différentielle \( {P}_{n}\left( D\right) \left( y\right) = 0. \)

> b) If \( {P}_{n}\left( X\right) = {\left( X - \alpha \right) }^{n} \), determine the form of the solutions to the differential equation \( {P}_{n}\left( D\right) \left( y\right) = 0. \)

c) En déduire, pour tout \( P \in \mathbb{C}\left\lbrack X\right\rbrack \left( {\deg \left( P\right) \geq 1}\right) \) , la forme des solutions de l’équation différentielle \( P\left( D\right) \left( y\right) = 0 \) .

> c) Deduce from this, for any \( P \in \mathbb{C}\left\lbrack X\right\rbrack \left( {\deg \left( P\right) \geq 1}\right) \), the form of the solutions to the differential equation \( P\left( D\right) \left( y\right) = 0 \).

Solution. Nous faisons tout de suite la remarque suivante, qui nous sera utile :

> Solution. We immediately make the following remark, which will be useful to us:

\[
\forall P, Q \in  \mathbb{C}\left\lbrack  X\right\rbrack  ,\;{PQ}\left( D\right) \left( y\right)  = P\left( D\right) \left\lbrack  {Q\left( D\right) \left( y\right) }\right\rbrack   = Q\left( D\right) \left\lbrack  {P\left( D\right) \left( y\right) }\right\rbrack  .
\]

Remarquons aussi que pour tout polynôme \( P \) , toute solution de \( P\left( D\right) \left( y\right) = 0 \) est de classe \( {\mathcal{C}}^{\infty } \) . a) On regarde \( D \) comme l’endomorphisme de \( {\mathcal{C}}^{\infty }\left( {\mathbb{R},\mathbb{C}}\right) \) (e.v des fonctions de classe \( {\mathcal{C}}^{\infty } \) de \( \mathbb{R} \) dans \( \mathbb{C} \) ) qui a tout \( u \) associe \( {u}^{\prime } \) . Soit \( P \in \mathbb{C}\left\lbrack X\right\rbrack \) . Dire que \( u \) est solution de l’équation différentielle \( P\left( D\right) \left( u\right) = 0 \) , c’est dire que \( u \in \operatorname{Ker}P\left( D\right) \) . Autrement dit, \( {\mathcal{S}}_{P} = \operatorname{Ker}P\left( D\right) \) .

> Let us also note that for any polynomial \( P \), any solution to \( P\left( D\right) \left( y\right) = 0 \) is of class \( {\mathcal{C}}^{\infty } \). a) We view \( D \) as the endomorphism of \( {\mathcal{C}}^{\infty }\left( {\mathbb{R},\mathbb{C}}\right) \) (v.s. of functions of class \( {\mathcal{C}}^{\infty } \) from \( \mathbb{R} \) to \( \mathbb{C} \)) which associates \( {u}^{\prime } \) to any \( u \). Let \( P \in \mathbb{C}\left\lbrack X\right\rbrack \). Saying that \( u \) is a solution to the differential equation \( P\left( D\right) \left( u\right) = 0 \) is equivalent to saying that \( u \in \operatorname{Ker}P\left( D\right) \). In other words, \( {\mathcal{S}}_{P} = \operatorname{Ker}P\left( D\right) \).

Maintenant, si les polynômes \( {P}_{1},\ldots ,{P}_{k} \) sont premiers entre eux deux à deux, on a d’après le théorème de décomposition des noyaux (voir le tome Algèbre) Ker \( {P}_{1}\cdots {P}_{k}\left( D\right) = \operatorname{Ker}{P}_{1}\left( D\right) \oplus \; \cdots \oplus \operatorname{Ker}{P}_{k}\left( D\right) \) . En d’autres termes, \( {\mathcal{S}}_{{P}_{1}\cdots {P}_{k}} = {\mathcal{S}}_{{P}_{1}} \oplus \cdots \oplus {\mathcal{S}}_{{P}_{k}} \) .

> Now, if the polynomials \( {P}_{1},\ldots ,{P}_{k} \) are pairwise coprime, we have, according to the kernel decomposition theorem (see the Algebra volume), Ker \( {P}_{1}\cdots {P}_{k}\left( D\right) = \operatorname{Ker}{P}_{1}\left( D\right) \oplus \; \cdots \oplus \operatorname{Ker}{P}_{k}\left( D\right) \). In other words, \( {\mathcal{S}}_{{P}_{1}\cdots {P}_{k}} = {\mathcal{S}}_{{P}_{1}} \oplus \cdots \oplus {\mathcal{S}}_{{P}_{k}} \).

b) L’intuition nous guide et nous fait pressentir que les solutions de \( {P}_{n}\left( D\right) \left( y\right) = 0 \) sont les fonctions \( t \mapsto {e}^{\alpha t}F\left( t\right) \) où \( F \) est un polynôme complexe de degré \( < n \) . Montrons donc ce résultat par récurrence sur \( n \in {\mathbb{N}}^{ * } \) .

> b) Intuition guides us and suggests that the solutions to \( {P}_{n}\left( D\right) \left( y\right) = 0 \) are the functions \( t \mapsto {e}^{\alpha t}F\left( t\right) \) where \( F \) is a complex polynomial of degree \( < n \) . Let us prove this result by induction on \( n \in {\mathbb{N}}^{ * } \) .

Pour \( n = 1 \) , c’est facile car \( {P}_{1}\left( D\right) \left( y\right) = 0 \) équivaut à \( {y}^{\prime } = {\alpha y} \) , dont les solutions sont les fonctions \( t \mapsto \lambda {e}^{\alpha t},\lambda \in \mathbb{R} \) .

> For \( n = 1 \) , it is easy because \( {P}_{1}\left( D\right) \left( y\right) = 0 \) is equivalent to \( {y}^{\prime } = {\alpha y} \) , whose solutions are the functions \( t \mapsto \lambda {e}^{\alpha t},\lambda \in \mathbb{R} \) .

Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . L’équation \( {P}_{n}\left( D\right) \left( y\right) = 0 \) s’écrit aussi \( {P}_{n - 1}\left( D\right) \left\lbrack {{P}_{1}\left( D\right) \left( y\right) }\right\rbrack = 0 \) , ce qui équivaut à dire que \( {P}_{1}\left( D\right) \left( y\right) \) a la forme \( t \mapsto {e}^{\alpha y}F\left( t\right) \) , où \( F \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( F\right) < n - 1 \) . Or l’équation \( {y}^{\prime } - {\alpha y} = {e}^{\alpha t}F\left( t\right) \) s’écrit aussi \( {\left( y{e}^{-{\alpha t}}\right) }^{\prime } = F\left( t\right) \) , ce qui équivaut à \( y = {e}^{\alpha t}G\left( t\right) \) où \( G \) est une primitive de \( F \) , c’est-à-dire \( G \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( \deg \left( G\right) < n \) . On en déduit le résultat au rang \( n \) , donc pour tout \( n \in {\mathbb{N}}^{ * } \) .

> Assume the result is true for rank \( n - 1 \) and show it for rank \( n \) . The equation \( {P}_{n}\left( D\right) \left( y\right) = 0 \) can also be written as \( {P}_{n - 1}\left( D\right) \left\lbrack {{P}_{1}\left( D\right) \left( y\right) }\right\rbrack = 0 \) , which is equivalent to saying that \( {P}_{1}\left( D\right) \left( y\right) \) has the form \( t \mapsto {e}^{\alpha y}F\left( t\right) \) , where \( F \in \mathbb{C}\left\lbrack X\right\rbrack ,\deg \left( F\right) < n - 1 \) . Now, the equation \( {y}^{\prime } - {\alpha y} = {e}^{\alpha t}F\left( t\right) \) can also be written as \( {\left( y{e}^{-{\alpha t}}\right) }^{\prime } = F\left( t\right) \) , which is equivalent to \( y = {e}^{\alpha t}G\left( t\right) \) where \( G \) is an antiderivative of \( F \) , that is \( G \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( \deg \left( G\right) < n \) . We deduce the result for rank \( n \) , and thus for all \( n \in {\mathbb{N}}^{ * } \) .

c) Soit \( P = \lambda \mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {\alpha }_{i}\right) }^{{n}_{i}} \) la décomposition de \( P \) en facteurs irréductibles de \( \mathbb{C}\left\lbrack X\right\rbrack \) . D’après le résultat de la question a), on a

> c) Let \( P = \lambda \mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {\alpha }_{i}\right) }^{{n}_{i}} \) be the decomposition of \( P \) into irreducible factors of \( \mathbb{C}\left\lbrack X\right\rbrack \) . According to the result from question a), we have

\[
{\mathcal{S}}_{P} = {\mathcal{S}}_{{\left( X - {\alpha }_{1}\right) }^{{n}_{1}}} \oplus  \cdots  \oplus  {\mathcal{S}}_{{\left( X - {\alpha }_{k}\right) }^{{n}_{k}}},
\]

et comme d’après b), \( {\mathcal{S}}_{{\left( X - {\alpha }_{i}\right) }^{{n}_{i}}} \) est le s.e.v des fonctions de la forme \( t \mapsto {e}^{{\alpha }_{i}t}{F}_{i}\left( t\right) \) avec \( {F}_{i} \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( \deg \left( {F}_{i}\right) < {n}_{i} \) , on en déduit que \( {\mathcal{S}}_{P} \) est l’ensemble des fonctions de la forme \( t \mapsto {e}^{{\alpha }_{1}t}{F}_{1}\left( t\right) + \; \cdots + {e}^{{\alpha }_{k}t}{F}_{k}\left( t\right) \) où pour tout \( i,{F}_{i} \) est un polynôme complexe de degré \( < {n}_{i} \) .

> and since according to b), \( {\mathcal{S}}_{{\left( X - {\alpha }_{i}\right) }^{{n}_{i}}} \) is the subspace of functions of the form \( t \mapsto {e}^{{\alpha }_{i}t}{F}_{i}\left( t\right) \) with \( {F}_{i} \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( \deg \left( {F}_{i}\right) < {n}_{i} \) , we deduce that \( {\mathcal{S}}_{P} \) is the set of functions of the form \( t \mapsto {e}^{{\alpha }_{1}t}{F}_{1}\left( t\right) + \; \cdots + {e}^{{\alpha }_{k}t}{F}_{k}\left( t\right) \) where for all \( i,{F}_{i} \) is a complex polynomial of degree \( < {n}_{i} \) .

EXERCICE 5. a) Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) une fonction de classe \( {\mathcal{C}}^{1} \) telle que

> EXERCISE 5. a) Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) be a function of class \( {\mathcal{C}}^{1} \) such that

\[
\exists \alpha  \in  \mathbb{C},\;\mathop{\lim }\limits_{{t \rightarrow   + \infty }}{f}^{\prime }\left( t\right)  + {\alpha f}\left( t\right)  = 0.
\]

Si \( \Re \left( \alpha \right) > 0 \) , montrer que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

> If \( \Re \left( \alpha \right) > 0 \) , show that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

b) Pour tout polynôme complexe \( P = \mathop{\sum }\limits_{{i = 0}}^{n}{a}_{i}{X}^{i} \) de degré \( n \geq 1 \) et pour toute fonction \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) de classe \( {\mathcal{C}}^{n} \) , on pose \( P\left( D\right) \left( f\right) = {a}_{n}{f}^{\left( n\right) } + \cdots + {a}_{1}{f}^{\prime } + {a}_{0}f \) . Donner une condition nécessaire et suffisante sur un polynôme complexe \( P \) de degré \( n \) pour que la propriété suivante soit vraie : pour toute fonction \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) de classe \( {\mathcal{C}}^{n} \) vérifiant \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}\left\lbrack {P\left( D\right) \left( f\right) }\right\rbrack \left( t\right) = 0 \) , on a \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

> b) For any complex polynomial \( P = \mathop{\sum }\limits_{{i = 0}}^{n}{a}_{i}{X}^{i} \) of degree \( n \geq 1 \) and for any function \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) of class \( {\mathcal{C}}^{n} \) , we define \( P\left( D\right) \left( f\right) = {a}_{n}{f}^{\left( n\right) } + \cdots + {a}_{1}{f}^{\prime } + {a}_{0}f \) . Give a necessary and sufficient condition on a complex polynomial \( P \) of degree \( n \) for the following property to be true: for any function \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) of class \( {\mathcal{C}}^{n} \) satisfying \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}\left\lbrack {P\left( D\right) \left( f\right) }\right\rbrack \left( t\right) = 0 \) , we have \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

Solution. a) Soit \( \varepsilon > 0 \) et soit \( A > 0 \) tel que \( \left| {{f}^{\prime }\left( t\right) + {\alpha f}\left( t\right) }\right| < \varepsilon \) pour tout \( t \geq A \) . En notant \( a = \Re \left( \alpha \right) \) , on a

> Solution. a) Let \( \varepsilon > 0 \) and let \( A > 0 \) be such that \( \left| {{f}^{\prime }\left( t\right) + {\alpha f}\left( t\right) }\right| < \varepsilon \) for all \( t \geq A \) . By denoting \( a = \Re \left( \alpha \right) \) , we have

\[
\forall t \geq  A,\;\left| {\frac{d}{dt}\left\lbrack  {{e}^{\alpha t}f\left( t\right) }\right\rbrack  }\right|  = \left| {{e}^{\alpha t}\left\lbrack  {{f}^{\prime }\left( t\right)  + {\alpha f}\left( t\right) }\right\rbrack  }\right|  = {e}^{at}\left| {{f}^{\prime }\left( t\right)  + {\alpha f}\left( t\right) }\right|  \leq  \varepsilon {e}^{at},
\]

ce qui entraîne par intégration

> which implies by integration

\[
\forall t \geq  A,\;\left| {{e}^{\alpha t}f\left( t\right)  - {e}^{\alpha A}f\left( A\right) }\right|  \leq  {\int }_{A}^{t}\left| {\frac{d}{du}\left\lbrack  {{e}^{\alpha u}f\left( u\right) }\right\rbrack  }\right| {du} \leq  {\int }_{A}^{t}\varepsilon {e}^{au}{du} = \frac{\varepsilon }{a}\left( {{e}^{at} - {e}^{aA}}\right) ,
\]

donc

> therefore

\[
\forall t \geq  A,\;\left| {f\left( t\right) }\right|  \leq  {e}^{a\left( {A - t}\right) }\left| {f\left( A\right) }\right|  + \frac{\varepsilon }{a}\left( {1 - {e}^{a\left( {A - t}\right) }}\right) .
\]

Comme \( a > 0 \) , on en déduit l’existence de \( B > A \) tel que \( \left| {f\left( t\right) }\right| \leq {2\varepsilon }/a \) pour tout \( t \geq B \) , d’où le résultat.

> Since \( a > 0 \) , we deduce the existence of \( B > A \) such that \( \left| {f\left( t\right) }\right| \leq {2\varepsilon }/a \) for all \( t \geq B \) , hence the result.

b) La relation \( {PQ}\left( D\right) \left( f\right) = P\left( D\right) \left\lbrack {Q\left( D\right) \left( f\right) }\right\rbrack \) pour tout \( P, Q \in \mathbb{C}\left\lbrack X\right\rbrack \) va nous permettre de montrer que la condition nécessaire est suffisante recherchée est que toutes les racines de \( P \) aient une partie réelle strictement négative.

> b) The relation \( {PQ}\left( D\right) \left( f\right) = P\left( D\right) \left\lbrack {Q\left( D\right) \left( f\right) }\right\rbrack \) for all \( P, Q \in \mathbb{C}\left\lbrack X\right\rbrack \) will allow us to show that the necessary and sufficient condition sought is that all roots of \( P \) have a strictly negative real part.

Condition nécessaire. Nous montrons le résultat par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est précisément le résultat démontré dans la question précédente. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Écrivons \( P = \lambda \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\alpha }_{i}}\right) \left( {\lambda \in {\mathbb{C}}^{ * }}\right) \) , et supposons que toutes les racines \( {\alpha }_{i} \) de \( P \) vérifient \( \Re \left( {\alpha }_{i}\right) < 0 \) . On peut écrire \( P = Q\left( {X - {\alpha }_{n}}\right) \) , où \( Q \) est un polynôme de degré \( n - 1 \) dont toutes les racines ont une partie réelle \( < 0 \) . Soit \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) une fonction de classe \( {\mathcal{C}}^{n} \) telle que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}P\left( D\right) \left( f\right) \left( t\right) = 0 \) . On a \( P\left( D\right) \left( f\right) = Q\left( D\right) \left\lbrack {\left( {D - {\alpha }_{n}\operatorname{Id}}\right) \left( f\right) }\right\rbrack = Q\left( D\right) \left( g\right) \) , où \( g = {f}^{\prime } - {\alpha }_{n}f \) , et comme \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}Q\left( D\right) \left( g\right) \left( t\right) = 0 \) , on en déduit d’après l’hypothèse de récurrence que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}g\left( t\right) = 0 \) . En d’autres termes, \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{f}^{\prime }\left( t\right) - {\alpha }_{n}f\left( t\right) = 0 \) , et d’après la question a), on en déduit que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

> Necessary condition. We prove the result by induction on \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) , it is precisely the result proven in the previous question. Assume the result is true for rank \( n - 1 \) and show it for rank \( n \) . Let us write \( P = \lambda \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\alpha }_{i}}\right) \left( {\lambda \in {\mathbb{C}}^{ * }}\right) \) , and assume that all roots \( {\alpha }_{i} \) of \( P \) satisfy \( \Re \left( {\alpha }_{i}\right) < 0 \) . We can write \( P = Q\left( {X - {\alpha }_{n}}\right) \) , where \( Q \) is a polynomial of degree \( n - 1 \) whose roots all have a real part \( < 0 \) . Let \( f : {\mathbb{R}}^{ + } \rightarrow \mathbb{C} \) be a function of class \( {\mathcal{C}}^{n} \) such that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}P\left( D\right) \left( f\right) \left( t\right) = 0 \) . We have \( P\left( D\right) \left( f\right) = Q\left( D\right) \left\lbrack {\left( {D - {\alpha }_{n}\operatorname{Id}}\right) \left( f\right) }\right\rbrack = Q\left( D\right) \left( g\right) \) , where \( g = {f}^{\prime } - {\alpha }_{n}f \) , and since \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}Q\left( D\right) \left( g\right) \left( t\right) = 0 \) , we deduce from the induction hypothesis that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}g\left( t\right) = 0 \) . In other words, \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}{f}^{\prime }\left( t\right) - {\alpha }_{n}f\left( t\right) = 0 \) , and according to question a), we deduce that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}f\left( t\right) = 0 \) .

Condition suffisante. Supposons que \( P \) ait une racine \( \alpha \) dont la partie réelle vérifie \( \Re \left( \alpha \right) \geq 0 \) . On peut écrire \( P = Q\left( {X - \alpha }\right) \) , où \( Q \in \mathbb{C}\left\lbrack X\right\rbrack \) . La fonction \( f : t \mapsto {e}^{\alpha t} \) ne tend pas vers 0 en \( + \infty \) , et comme \( {f}^{\prime } - {\alpha f} = 0 \) , on a \( P\left( D\right) \left( f\right) = Q\left( D\right) \left\lbrack {{f}^{\prime } - {\alpha f}}\right\rbrack = 0 \) . Ainsi, nous avons trouvé une fonction \( f \) ne tendant pas vers0à l’infini telle que \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}P\left( D\right) \left( f\right) = 0 \) . Ceci est absurde, donc toutes les racines de \( P \) ont nécessairement leur partie réelle \( < 0 \) .

> Sufficient condition. Assume that \( P \) has a root \( \alpha \) whose real part satisfies \( \Re \left( \alpha \right) \geq 0 \) . We can write \( P = Q\left( {X - \alpha }\right) \) , where \( Q \in \mathbb{C}\left\lbrack X\right\rbrack \) . The function \( f : t \mapsto {e}^{\alpha t} \) does not tend to 0 at \( + \infty \) , and since \( {f}^{\prime } - {\alpha f} = 0 \) , we have \( P\left( D\right) \left( f\right) = Q\left( D\right) \left\lbrack {{f}^{\prime } - {\alpha f}}\right\rbrack = 0 \) . Thus, we have found a function \( f \) that does not tend to 0 at infinity such that \( \mathop{\lim }\limits_{{t \rightarrow + \infty }}P\left( D\right) \left( f\right) = 0 \) . This is absurd, therefore all roots of \( P \) necessarily have their real part \( < 0 \) .

EXERCICE 6 (THÉORÉME DE FLOQUET). On considère un système différentiel sur \( {\mathbb{C}}^{n} \; \left( E\right) : {Y}^{\prime } = A\left( t\right) Y \) où \( A : \mathbb{R} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) est une fonction continue et \( T \) -périodique. a) Montrer que \( \left( E\right) \) admet une solution \( V \) non nulle telle que

> EXERCISE 6 (FLOQUET'S THEOREM). Consider a differential system on \( {\mathbb{C}}^{n} \; \left( E\right) : {Y}^{\prime } = A\left( t\right) Y \) where \( A : \mathbb{R} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is a continuous and \( T \)-periodic function. a) Show that \( \left( E\right) \) admits a non-zero solution \( V \) such that

\[
\exists \lambda  \in  \mathbb{C},\forall t \in  \mathbb{R},\;V\left( {t + T}\right)  = {\lambda V}\left( t\right) .
\]

b) On considère \( n \) solutions \( {V}_{1},\ldots ,{V}_{n} \) de \( \left( E\right) \) linéairement indépendantes. En notant \( M\left( t\right) \) la matrice carrée dont les vecteurs colonnes sont \( {V}_{1}\left( t\right) ,\ldots ,{V}_{n}\left( t\right) \) , montrer

> b) Consider \( n \) linearly independent solutions \( {V}_{1},\ldots ,{V}_{n} \) of \( \left( E\right) \). By denoting \( M\left( t\right) \) as the square matrix whose column vectors are \( {V}_{1}\left( t\right) ,\ldots ,{V}_{n}\left( t\right) \), show

\[
\exists C \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) ,\forall t \in  \mathbb{R},\;M\left( {t + T}\right)  = M\left( t\right) C.
\]

Solution. a) On sait (voir le théorème 2 page 378) que l’ensemble \( \mathcal{S} \) des solutions de \( \left( E\right) \) est un \( \mathbb{C} \) -e.v de dimension \( n \) . Comme \( A \) est \( T \) -périodique, on voit que pour toute solution \( V \) de (E), l’application \( {V}_{T} : t \mapsto V\left( {t + T}\right) \) est aussi une solution. On construit ainsi une application \( \Phi : \mathcal{S} \rightarrow \mathcal{S}\;V \mapsto {V}_{T} \) . Cette application est évidemment un endomorphisme de \( \mathcal{S} \) . Comme \( \mathcal{S} \) est un \( \mathbb{C} \) -e.v de dimension finie, \( \Phi \) admet au moins une valeur propre \( \lambda \in \mathbb{C} \) . Si \( V \in \mathcal{S} \) est un vecteur propre non nul associé, on a \( \Phi \left( V\right) = {\lambda V} \) , ce qui s’écrit aussi \( V\left( {t + T}\right) = {\lambda V}\left( t\right) \) pour tout \( t \in \mathbb{R} \) .

> Solution. a) We know (see theorem 2 on page 378) that the set \( \mathcal{S} \) of solutions to \( \left( E\right) \) is a \( \mathbb{C} \)-vector space of dimension \( n \). Since \( A \) is \( T \)-periodic, we see that for any solution \( V \) of (E), the mapping \( {V}_{T} : t \mapsto V\left( {t + T}\right) \) is also a solution. We thus construct a mapping \( \Phi : \mathcal{S} \rightarrow \mathcal{S}\;V \mapsto {V}_{T} \). This mapping is obviously an endomorphism of \( \mathcal{S} \). Since \( \mathcal{S} \) is a \( \mathbb{C} \)-vector space of finite dimension, \( \Phi \) admits at least one eigenvalue \( \lambda \in \mathbb{C} \). If \( V \in \mathcal{S} \) is an associated non-zero eigenvector, we have \( \Phi \left( V\right) = {\lambda V} \), which is also written as \( V\left( {t + T}\right) = {\lambda V}\left( t\right) \) for all \( t \in \mathbb{R} \).

b) Comme \( \mathcal{S} \) est un espace vectoriel de dimension \( n,\left( {{V}_{1},\ldots ,{V}_{n}}\right) \) est une base de \( \mathcal{S} \) . Notons \( B = \left( {b}_{i, j}\right) \) la matrice de l’endomorphisme \( \Phi \) dans cette base, de sorte que

> b) Since \( \mathcal{S} \) is a vector space of dimension \( n,\left( {{V}_{1},\ldots ,{V}_{n}}\right) \) is a basis of \( \mathcal{S} \). Let \( B = \left( {b}_{i, j}\right) \) be the matrix of the endomorphism \( \Phi \) in this basis, such that

\[
\forall i \in  \{ 1,\ldots , n\} ,\;{V}_{i, T} = \mathop{\sum }\limits_{{j = 1}}^{n}{b}_{i, j}{V}_{j}\;\text{ ou encore }\;\forall t \in  \mathbb{R},\;{V}_{i}\left( {t + T}\right)  = \mathop{\sum }\limits_{{j = 1}}^{n}{b}_{i, j}{V}_{j}\left( t\right) .
\]

En désignant par \( {V}_{i, k} \) la \( k \) -ième composante de \( {V}_{i} \) , on a donc

> By designating \( {V}_{i, k} \) as the \( k \)-th component of \( {V}_{i} \), we therefore have

\[
\forall i, k \in  \{ 1,\ldots , n\} ,\forall t \in  \mathbb{R},\;{V}_{i, k}\left( {t + T}\right)  = \mathop{\sum }\limits_{{j = 1}}^{n}{b}_{i, j}{V}_{j, k}\left( t\right) .
\]

Comme \( M\left( t\right) \) est la matrice dont l’élément d’indice \( \left( {i, j}\right) \) est \( {V}_{j, i}\left( t\right) \) , ceci s’écrit aussi \( {}^{t}M\left( {t + T}\right) = \; {B}^{t}M\left( t\right) \) , donc \( M\left( {t + T}\right) = M{\left( t\right) }^{t}B \) pour tout \( t \in \mathbb{R} \) . La matrice \( B \) étant inversible (car \( \Phi \) est inversible, puisque si \( {V}_{T} = 0 \) , alors \( V = 0 \) donc Ker \( \Phi = \{ 0\} \) ), la matrice \( C = {}^{t}B \) est aussi inversible.

> Since \( M\left( t\right) \) is the matrix whose element with index \( \left( {i, j}\right) \) is \( {V}_{j, i}\left( t\right) \), this is also written as \( {}^{t}M\left( {t + T}\right) = \; {B}^{t}M\left( t\right) \), therefore \( M\left( {t + T}\right) = M{\left( t\right) }^{t}B \) for all \( t \in \mathbb{R} \). The matrix \( B \) being invertible (because \( \Phi \) is invertible, since if \( {V}_{T} = 0 \), then \( V = 0 \) therefore Ker \( \Phi = \{ 0\} \)), the matrix \( C = {}^{t}B \) is also invertible.

EXERCICE 7 (CALCUL DU WRONSKIEN). a) Soient \( I \) un intervalle de \( \mathbb{R} \) et deux applications \( p, q : I \rightarrow \mathbb{C} \) continues. On considère deux solutions \( u \) et \( v \) de l’équation différentielle (L) : \( {y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = 0 \) . Calculer le wronskien de \( u \) et \( v \) en fonction de sa valeur en un point \( a \) de \( I \) .

> EXERCISE 7 (CALCULATION OF THE WRONSKIAN). a) Let \( I \) be an interval of \( \mathbb{R} \) and \( p, q : I \rightarrow \mathbb{C} \) be two continuous mappings. Consider two solutions \( u \) and \( v \) of the differential equation (L): \( {y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = 0 \) . Calculate the Wronskian of \( u \) and \( v \) in terms of its value at a point \( a \) of \( I \) .

b) On veut étendre ce résultat aux systèmes linéaires. Soient \( I \) un intervalle de \( \mathbb{R} \) et \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) une fonction continue. On considère \( {f}_{1},\ldots ,{f}_{n}n \) solutions sur \( I \) de l’équation différentielle \( \left( S\right) : {Y}^{\prime } = A\left( t\right) Y \) . Calculer le wronskien de \( {f}_{1},\ldots ,{f}_{n} \) en fonction de sa valeur en un point \( a \) de \( I \) .

> b) We wish to extend this result to linear systems. Let \( I \) be an interval of \( \mathbb{R} \) and \( A : I \rightarrow {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) be a continuous function. Consider \( {f}_{1},\ldots ,{f}_{n}n \) solutions on \( I \) of the differential equation \( \left( S\right) : {Y}^{\prime } = A\left( t\right) Y \) . Calculate the Wronskian of \( {f}_{1},\ldots ,{f}_{n} \) in terms of its value at a point \( a \) of \( I \) .

Solution. a) Posons \( W\left( t\right) = \operatorname{wronskien}\left( {u, v}\right) \left( t\right) = \left( {u{v}^{\prime } - {u}^{\prime }v}\right) \left( t\right) \) . L’idée est de rechercher une équation différentielle vérifiée par \( W \) . Pour tout \( t \in I \) , on a \( {W}^{\prime }\left( t\right) = \left( {u{v}^{\prime \prime } - {u}^{\prime \prime }v}\right) \left( t\right) \) . En multipliant par \( u \) l’égalité \( {v}^{\prime \prime } + p\left( t\right) {v}^{\prime } + q\left( t\right) v = 0 \) et par \( v \) l’égalité \( {u}^{\prime \prime } + p\left( t\right) {u}^{\prime } + q\left( t\right) u = 0 \) , puis en retranchant, on obtient \( u{v}^{\prime \prime } - {u}^{\prime \prime }v + p\left( t\right) \left( {u{v}^{\prime } - {u}^{\prime }v}\right) = 0 \) . Autrement dit, \( {W}^{\prime } + p\left( t\right) W = 0 \) . On en déduit en résolvant cette équation différentielle linéaire d'ordre 1 que

> Solution. a) Let \( W\left( t\right) = \operatorname{wronskien}\left( {u, v}\right) \left( t\right) = \left( {u{v}^{\prime } - {u}^{\prime }v}\right) \left( t\right) \) . The idea is to look for a differential equation satisfied by \( W \) . For all \( t \in I \) , we have \( {W}^{\prime }\left( t\right) = \left( {u{v}^{\prime \prime } - {u}^{\prime \prime }v}\right) \left( t\right) \) . By multiplying the equality \( {v}^{\prime \prime } + p\left( t\right) {v}^{\prime } + q\left( t\right) v = 0 \) by \( u \) and the equality \( {u}^{\prime \prime } + p\left( t\right) {u}^{\prime } + q\left( t\right) u = 0 \) by \( v \) , then subtracting, we obtain \( u{v}^{\prime \prime } - {u}^{\prime \prime }v + p\left( t\right) \left( {u{v}^{\prime } - {u}^{\prime }v}\right) = 0 \) . In other words, \( {W}^{\prime } + p\left( t\right) W = 0 \) . By solving this first-order linear differential equation, we deduce that

\[
\forall t \in  I,\;W\left( t\right)  = W\left( a\right) \exp \left( {-{\int }_{a}^{t}p\left( u\right) {du}}\right) .
\]

b) On pose \( W\left( t\right) = \operatorname{wronskien}\left( {{f}_{1},\ldots ,{f}_{n}}\right) \left( t\right) = \det \left( {{f}_{1},\ldots ,{f}_{n}}\right) \left( t\right) \) . Nous allons comme plus haut rechercher une équation différentielle satisfaite par \( W \) .

> b) Let \( W\left( t\right) = \operatorname{wronskien}\left( {{f}_{1},\ldots ,{f}_{n}}\right) \left( t\right) = \det \left( {{f}_{1},\ldots ,{f}_{n}}\right) \left( t\right) \) . As above, we will look for a differential equation satisfied by \( W \) .

La formule de dérivation d'un déterminant (qui peut s'obtenir facilement à partir de son développement en fonction de ses coefficients - voir le tome Algèbre) entraîne

> The formula for the derivative of a determinant (which can be easily obtained from its expansion in terms of its coefficients - see the Algebra volume) implies

\[
\forall t \in  I,\;{W}^{\prime }\left( t\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{f}_{1},\ldots ,{f}_{i - 1},{f}_{i}^{\prime },{f}_{i + 1},\ldots ,{f}_{n}}\right) \left( t\right)
\]

\[
= \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{f}_{1}\left( t\right) ,\ldots ,{f}_{i - 1}\left( t\right) , A\left( t\right) {f}_{i}\left( t\right) ,{f}_{i + 1}\left( t\right) ,\ldots ,{f}_{n}\left( t\right) }\right) .
\]

Fixons un élément quelconque \( t \) de \( I \) . L’application \( {\Phi }_{t} : {\left( {\mathbb{C}}^{n}\right) }^{n} \rightarrow \mathbb{C} \) définie par

> Let us fix an arbitrary element \( t \) of \( I \) . The mapping \( {\Phi }_{t} : {\left( {\mathbb{C}}^{n}\right) }^{n} \rightarrow \mathbb{C} \) defined by

\[
{\Phi }_{t}\left( {{v}_{1},\ldots ,{v}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{v}_{1},\ldots ,{v}_{i - 1}, A\left( t\right) {v}_{i},{v}_{i + 1},\ldots ,{v}_{n}}\right)
\]

est une forme \( n \) -linéaire antisymétrique, donc alternée, donc proportionnelle à l’application déterminant (voir le tome Algèbre). On peut donc trouver \( \lambda \in \mathbb{R} \) tel que \( {\Phi }_{t}\left( {{v}_{1},\ldots ,{v}_{n}}\right) = \; \lambda \det \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) pour tous vecteurs \( {v}_{1},\ldots ,{v}_{n} \in {\mathbb{C}}^{n} \) . Or, en désignant par \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) la base canonique de \( {\mathbb{C}}^{n} \) , on a facilement

> is an antisymmetric \( n \) -linear form, therefore alternating, and thus proportional to the determinant map (see the Algebra volume). We can therefore find \( \lambda \in \mathbb{R} \) such that \( {\Phi }_{t}\left( {{v}_{1},\ldots ,{v}_{n}}\right) = \; \lambda \det \left( {{v}_{1},\ldots ,{v}_{n}}\right) \) for all vectors \( {v}_{1},\ldots ,{v}_{n} \in {\mathbb{C}}^{n} \) . Now, by denoting the canonical basis of \( {\mathbb{C}}^{n} \) by \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) , we easily have

\[
{\Phi }_{t}\left( {{e}_{1},\ldots ,{e}_{n}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}\det \left( {{e}_{1},\ldots ,{e}_{i - 1}, A\left( t\right) {e}_{i},{e}_{i + 1},\ldots ,{e}_{n}}\right)  = \operatorname{tr}A\left( t\right) ,
\]

donc \( \operatorname{tr}A\left( t\right) = \lambda \det \left( {{e}_{1},\ldots ,{e}_{n}}\right) = \lambda \) . On connaît donc \( {\Phi }_{t} \) , et

> therefore \( \operatorname{tr}A\left( t\right) = \lambda \det \left( {{e}_{1},\ldots ,{e}_{n}}\right) = \lambda \) . We thus know \( {\Phi }_{t} \) , and

\[
\forall t \in  I,\;{W}^{\prime }\left( t\right)  = {\Phi }_{t}\left( {{f}_{1},\ldots ,{f}_{n}}\right)  = \operatorname{tr}A\left( t\right)  \cdot  \det \left( {{f}_{1},\ldots ,{f}_{n}}\right) \left( t\right)  = \operatorname{tr}A\left( t\right)  \cdot  W\left( t\right) .
\]

On en déduit finalement

> We finally deduce

\[
\forall t \in  I,\;W\left( t\right)  = W\left( a\right) \exp \left( {{\int }_{a}^{t}\operatorname{tr}A\left( u\right) {du}}\right) .
\]

Remarque. Ce résultat peut être utile, surtout le cas particulier de a) car beaucoup d'exercices portent sur les équations linéaires d'ordre 2.

> Remark. This result can be useful, especially the special case of a) because many exercises focus on second-order linear equations.

En transformant les équations différentielles linéaires sur \( \mathbb{C} \) d’ordre \( n \) en un système différentiel sur \( {\mathbb{C}}^{n} \) , un corollaire du résultat de la question b) est que le wronskien \( W \) de \( n \) solutions d’une équation différentielle sur \( \mathbb{C} \) du type \( {y}^{\left( n\right) } + {a}_{1}\left( t\right) {y}^{\left( n - 1\right) } + \cdots + {a}_{n}\left( t\right) y = 0 \) vérifie

> By transforming linear differential equations on \( \mathbb{C} \) of order \( n \) into a differential system on \( {\mathbb{C}}^{n} \) , a corollary of the result in question b) is that the Wronskian \( W \) of \( n \) solutions of a differential equation on \( \mathbb{C} \) of the type \( {y}^{\left( n\right) } + {a}_{1}\left( t\right) {y}^{\left( n - 1\right) } + \cdots + {a}_{n}\left( t\right) y = 0 \) satisfies

\[
\forall t \in  I,\;W\left( t\right)  = W\left( a\right) \exp \left( {-{\int }_{a}^{t}{a}_{1}\left( u\right) {du}}\right) .
\]

EXERCICE 8. Soit \( f \in \mathcal{L}\left( {\mathbb{C}}^{n}\right) \) . Soient \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) les valeurs propres distinctes de \( f \) . Pour tout \( i \) , on note \( {N}_{i} \) le sous-espace caractéristique de \( f \) associé à la valeur propre \( {\lambda }_{i} \) et on note \( {\alpha }_{i} = \dim {N}_{i} \) (de sorte que \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) ). Pour tout s.e.v \( N \) de \( {\mathbb{C}}^{n} \) , pour tout \( \alpha \in {\mathbb{N}}^{ * } \) et pour tout \( \lambda \in \mathbb{C} \) , on note \( {\mathcal{S}}_{N,\alpha ,\lambda } \) l’e.v des fonctions \( \mathbb{R} \rightarrow \mathbb{C}\;t \mapsto {e}^{\lambda t}P\left( t\right) \) , où \( P \) est un polynôme à coefficients dans \( N \) de degré \( < \alpha \) .

> EXERCISE 8. Let \( f \in \mathcal{L}\left( {\mathbb{C}}^{n}\right) \) . Let \( {\lambda }_{1},\ldots ,{\lambda }_{k} \) be the distinct eigenvalues of \( f \) . For any \( i \) , we denote by \( {N}_{i} \) the characteristic subspace of \( f \) associated with the eigenvalue \( {\lambda }_{i} \) and we denote \( {\alpha }_{i} = \dim {N}_{i} \) (so that \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{k}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) ). For any subspace \( N \) of \( {\mathbb{C}}^{n} \) , for any \( \alpha \in {\mathbb{N}}^{ * } \) and for any \( \lambda \in \mathbb{C} \) , we denote by \( {\mathcal{S}}_{N,\alpha ,\lambda } \) the vector space of functions \( \mathbb{R} \rightarrow \mathbb{C}\;t \mapsto {e}^{\lambda t}P\left( t\right) \) , where \( P \) is a polynomial with coefficients in \( N \) of degree \( < \alpha \) .

Soit \( \mathcal{S} \) l’e.v des solutions de l’équation différentielle \( {X}^{\prime } = f\left( X\right) \) . Montrer

> Let \( \mathcal{S} \) be the vector space of solutions to the differential equation \( {X}^{\prime } = f\left( X\right) \) . Show

\[
\mathcal{S} \subset  {S}_{{N}_{1},{\alpha }_{1},{\lambda }_{1}} \oplus  \cdots  \oplus  {S}_{{N}_{k},{\alpha }_{k},{\lambda }_{k}}.
\]

Quand peut-on dire que cette inclusion est une égalité ?

> When can we say that this inclusion is an equality?

Solution. Commençons par donner quelques rappels d'algèbre (voir le tome Algèbre). On a \( {\mathbb{C}}^{n} = {N}_{1} \oplus \cdots \oplus {N}_{k} \) , et pour tout \( i,{N}_{i} \) est stable par \( f \) ce qui fait de \( {f}_{i} = {f}_{\mid {N}_{i}} \) un endomorphisme de \( {N}_{i} \) . Pour tout \( i \) , on peut aussi écrire \( {f}_{i} \) sous la forme \( {f}_{i} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} + {n}_{i} \) , ou \( {n}_{i} \) est nilpotent (et plus précisément \( {n}_{i}^{{\alpha }_{i}} = 0 \) ).

> Solution. Let us begin by recalling some algebra (see the Algebra volume). We have \( {\mathbb{C}}^{n} = {N}_{1} \oplus \cdots \oplus {N}_{k} \), and for all \( i,{N}_{i} \) is stable by \( f \) which makes \( {f}_{i} = {f}_{\mid {N}_{i}} \) an endomorphism of \( {N}_{i} \). For all \( i \), we can also write \( {f}_{i} \) in the form \( {f}_{i} = {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} + {n}_{i} \), where \( {n}_{i} \) is nilpotent (and more precisely \( {n}_{i}^{{\alpha }_{i}} = 0 \)).

Soit \( u \) une solution de \( {X}^{\prime } = f\left( X\right) \) . Pour tout \( i \) , notons \( {\pi }_{i} \) la projection sur \( {N}_{i} \) parallèlement à \( { \oplus }_{j \neq i}{N}_{j} \) , puis \( {u}_{i} = {\pi }_{i}\left( u\right) \) , de sorte que \( u = {u}_{1} + \cdots + {u}_{k} \) et pour tout \( i,{u}_{i}^{\prime } = {f}_{i}\left( {u}_{i}\right) \) . Nous allons montrer que pour tout \( i,{u}_{i} \in {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \) . Posons \( {v}_{i} = {e}^{-{\lambda }_{i}t}{u}_{i} \) . On a

> Let \( u \) be a solution of \( {X}^{\prime } = f\left( X\right) \). For all \( i \), let \( {\pi }_{i} \) denote the projection onto \( {N}_{i} \) parallel to \( { \oplus }_{j \neq i}{N}_{j} \), then \( {u}_{i} = {\pi }_{i}\left( u\right) \), such that \( u = {u}_{1} + \cdots + {u}_{k} \) and for all \( i,{u}_{i}^{\prime } = {f}_{i}\left( {u}_{i}\right) \). We will show that for all \( i,{u}_{i} \in {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \). Let \( {v}_{i} = {e}^{-{\lambda }_{i}t}{u}_{i} \). We have

\[
{v}_{i}^{\prime } =  - {\lambda }_{i}{v}_{i} + {e}^{-{\lambda }_{i}t}{u}_{i}^{\prime } =  - {\lambda }_{i}{v}_{i} + {e}^{-{\lambda }_{i}t}{f}_{i}\left( {u}_{i}\right)  =  - {\lambda }_{i}{v}_{i} + {f}_{i}\left( {v}_{i}\right)  = {n}_{i}\left( {v}_{i}\right) ,
\]

et une récurrence immédiate donne ensuite \( {v}_{i}^{\left( r\right) } = {n}_{i}^{r}\left( {v}_{i}\right) \) (on peut bien dériver autant de fois que l’on veut puisque la relation \( {v}_{i}^{\prime } = {n}_{i}\left( {v}_{i}\right) \) entraîne le fait que \( {v}_{i} \) est de classe \( {\mathcal{C}}^{\infty } \) ). Or \( {n}_{i}^{{\alpha }_{i}} = 0 \) , on a donc \( {v}_{i}^{\left( {\alpha }_{i}\right) } = 0 \) . Autrement dit, \( {v}_{i} = P \) est un polynôme de degré \( < {\alpha }_{i} \) ,à coefficients dans \( {N}_{i} \) , et comme \( {u}_{i} = {e}^{{\lambda }_{i}t}{v}_{i} \) , on en déduit \( {u}_{i} \in {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \) .

> and an immediate induction then gives \( {v}_{i}^{\left( r\right) } = {n}_{i}^{r}\left( {v}_{i}\right) \) (we can indeed differentiate as many times as we want since the relation \( {v}_{i}^{\prime } = {n}_{i}\left( {v}_{i}\right) \) implies that \( {v}_{i} \) is of class \( {\mathcal{C}}^{\infty } \)). Now \( {n}_{i}^{{\alpha }_{i}} = 0 \), so we have \( {v}_{i}^{\left( {\alpha }_{i}\right) } = 0 \). In other words, \( {v}_{i} = P \) is a polynomial of degree \( < {\alpha }_{i} \), with coefficients in \( {N}_{i} \), and since \( {u}_{i} = {e}^{{\lambda }_{i}t}{v}_{i} \), we deduce \( {u}_{i} \in {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \).

On a donc montré \( \mathcal{S} \subset {\mathcal{S}}_{{N}_{1},{\alpha }_{1},{\lambda }_{1}} + \cdots + {\mathcal{S}}_{{N}_{k},{\alpha }_{k},{\lambda }_{k}} \) . De plus, il est immédiat que les \( {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \) sont en somme directe, d'où le premier résultat demandé.

> We have therefore shown \( \mathcal{S} \subset {\mathcal{S}}_{{N}_{1},{\alpha }_{1},{\lambda }_{1}} + \cdots + {\mathcal{S}}_{{N}_{k},{\alpha }_{k},{\lambda }_{k}} \). Furthermore, it is immediate that the \( {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \) are in direct sum, hence the first requested result.

Comme il y a inclusion, il y aura égalité si et seulement si les dimensions des sous-espaces correspondants sont égales, c’est-à-dire dim \( \mathcal{S} = \mathop{\sum }\limits_{{i = 1}}^{k}\dim {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \) . Or \( \dim S = n = \mathop{\sum }\limits_{{i = 1}}^{k}{\alpha }_{i} \) et pour tout \( i \) , \( \dim {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} = {\alpha }_{i}\dim {N}_{i} = {\alpha }_{i}^{2} \) . Il y aura donc l’égalité si et seulement si \( \mathop{\sum }\limits_{i}{\alpha }_{i} = \; \mathop{\sum }\limits_{i}{\alpha }_{i}^{2} \) , ce qui équivaut à dire \( {\alpha }_{i} = 1 \) pour tout \( i \) , ou encore que les valeurs propres de \( f \) sont toutes distinctes.

> Since there is inclusion, there will be equality if and only if the dimensions of the corresponding subspaces are equal, that is, dim \( \mathcal{S} = \mathop{\sum }\limits_{{i = 1}}^{k}\dim {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} \) . However, \( \dim S = n = \mathop{\sum }\limits_{{i = 1}}^{k}{\alpha }_{i} \) and for all \( i \) , \( \dim {\mathcal{S}}_{{N}_{i},{\alpha }_{i},{\lambda }_{i}} = {\alpha }_{i}\dim {N}_{i} = {\alpha }_{i}^{2} \) . There will therefore be equality if and only if \( \mathop{\sum }\limits_{i}{\alpha }_{i} = \; \mathop{\sum }\limits_{i}{\alpha }_{i}^{2} \) , which is equivalent to saying \( {\alpha }_{i} = 1 \) for all \( i \) , or also that the eigenvalues of \( f \) are all distinct.

Remarque. Ce résultat reste évidemment vrai, par isomorphisme, pour les systèmes linéaires du type \( {X}^{\prime } = {AX} \) , où \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Dans la pratique, pour résoudre \( \left( S\right) : {X}^{\prime } = \; {AX} \) , on ne cherche pas directement les sous-espaces \( {N}_{i} \) . On écrit qu’une solution \( V \) s’écrit nécessairement sous la forme \( V = \mathop{\sum }\limits_{{i = 1}}^{k}{e}^{{\lambda }_{i}t}{P}_{i}\left( t\right) \) , où \( {P}_{i} \) est un polynôme de degré \( < {\alpha }_{i} \) à valeurs dans \( {\mathbb{C}}^{n} \) , puis on trouve la forme des coefficients des \( {P}_{i} \) par identification en remplaçant dans \( \left( S\right) \) .

> Remark. This result obviously remains true, by isomorphism, for linear systems of the type \( {X}^{\prime } = {AX} \) , where \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . In practice, to solve \( \left( S\right) : {X}^{\prime } = \; {AX} \) , we do not directly look for the subspaces \( {N}_{i} \) . We write that a solution \( V \) is necessarily written in the form \( V = \mathop{\sum }\limits_{{i = 1}}^{k}{e}^{{\lambda }_{i}t}{P}_{i}\left( t\right) \) , where \( {P}_{i} \) is a polynomial of degree \( < {\alpha }_{i} \) with values in \( {\mathbb{C}}^{n} \) , then we find the form of the coefficients of \( {P}_{i} \) by identification by substituting into \( \left( S\right) \) .
