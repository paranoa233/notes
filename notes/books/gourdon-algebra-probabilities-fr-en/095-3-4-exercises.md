#### 3.4. Exercises

*Français : 3.4. Exercices*

\( \rightarrow \) EXERCICE 1 (DENSITÉ DES MATRICES DIAGONALISABLES DANS \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) ). a) Montrer que l’ensemble des matrices diagonalisables de \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) est dense dans \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . b) Que dire dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ?

> \( \rightarrow \) EXERCISE 1 (DENSITY OF DIAGONALIZABLE MATRICES IN \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) ). a) Show that the set of diagonalizable matrices of \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) is dense in \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . b) What can be said in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) ?

Solution. a) Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Il s’agit de montrer que \( A \) est limite de matrices diagonalisables. Le corps \( \mathbb{C} \) étant algébriquement clos, \( A \) est trigonalisable, donc

> Solution. a) Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . We must show that \( A \) is the limit of diagonalizable matrices. Since the field \( \mathbb{C} \) is algebraically closed, \( A \) is triangularizable, therefore

\[
\exists P \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) ,{P}^{-1}{AP} = T\text{ avec }T = \left( \begin{matrix} {\lambda }_{1} &  \times  & \cdots &  \times  \\   & {\lambda }_{2} &  \ddots  & \vdots \\   & 0 &  \ddots  &  \times  \\   & & & {\lambda }_{n} \end{matrix}\right) .
\]

Soit \( \mu = \inf \left\{ {\left| {{\lambda }_{i} - {\lambda }_{j}}\right| ,{\lambda }_{i} \neq {\lambda }_{j}}\right\} > 0,\mu = 1 \) si les \( {\lambda }_{i} \) sont tous égaux. Pour tout \( p \in {\mathbb{N}}^{ * } \) , on pose

> Let \( \mu = \inf \left\{ {\left| {{\lambda }_{i} - {\lambda }_{j}}\right| ,{\lambda }_{i} \neq {\lambda }_{j}}\right\} > 0,\mu = 1 \) if the \( {\lambda }_{i} \) are all equal. For all \( p \in {\mathbb{N}}^{ * } \) , we define

\[
{T}_{p} = \left( \begin{matrix} {\lambda }_{1} + \frac{\mu }{p} &  \times  & \cdots &  \times  \\   & {\lambda }_{2} + \frac{\mu }{2p} &  \ddots  & \vdots \\  \left( 0\right) & &  \ddots  &  \times  \\   & & & {\lambda }_{n} + \frac{\mu }{np} \end{matrix}\right)  = T + \frac{\mu }{p}\left( \begin{matrix} 1 & & & \left( 0\right) \\   & \frac{1}{2} & & \\  \left( 0\right) & &  \ddots  & \\   & & & \frac{1}{n} \end{matrix}\right) .
\]

Les valeurs propres de \( {T}_{p} \) , les \( {\lambda }_{i} + \left( {\mu /{ip}}\right) \) , sont deux à deux distinctes. En effet, supposons \( i \neq j \) :

> The eigenvalues of \( {T}_{p} \) , the \( {\lambda }_{i} + \left( {\mu /{ip}}\right) \) , are pairwise distinct. Indeed, suppose \( i \neq j \) :

- Si \( {\lambda }_{i} = {\lambda }_{j} \) , il est clair que \( {\lambda }_{i} + \left( {\mu /{ip}}\right)  \neq  {\lambda }_{j} + \left( {\mu /{jp}}\right) \) .

> - If \( {\lambda }_{i} = {\lambda }_{j} \) , it is clear that \( {\lambda }_{i} + \left( {\mu /{ip}}\right)  \neq  {\lambda }_{j} + \left( {\mu /{jp}}\right) \) .

- Sinon \( {\lambda }_{i} \neq  {\lambda }_{j} \) , donc si \( {\lambda }_{i} + \left( {\mu /{ip}}\right)  = {\lambda }_{j} + \left( {\mu /{jp}}\right) \) , alors \( \left| {{\lambda }_{i} - {\lambda }_{j}}\right|  = \mu \left| {\left( {1/{ip}}\right)  - \left( {1/{jp}}\right) }\right|  < \mu \) , absurde par construction de \( \mu \) .

> - Otherwise \( {\lambda }_{i} \neq  {\lambda }_{j} \) , so if \( {\lambda }_{i} + \left( {\mu /{ip}}\right)  = {\lambda }_{j} + \left( {\mu /{jp}}\right) \) , then \( \left| {{\lambda }_{i} - {\lambda }_{j}}\right|  = \mu \left| {\left( {1/{ip}}\right)  - \left( {1/{jp}}\right) }\right|  < \mu \) , absurd by construction of \( \mu \) .

Pour tout \( p \in {\mathbb{N}}^{ * },{T}_{p} \) a donc toutes ses valeurs propres deux à deux distinctes, donc est dia-gonalisable. Or \( T = \mathop{\lim }\limits_{{p \rightarrow + \infty }}{T}_{p} \) , donc \( A = {PT}{P}^{-1} = \mathop{\lim }\limits_{{p \rightarrow + \infty }}P{T}_{p}{P}^{-1} \) est limite de matrices diagonalisables, d'où le résultat.

> For any \( p \in {\mathbb{N}}^{ * },{T}_{p} \) therefore has all its eigenvalues pairwise distinct, so is diagonalizable. However \( T = \mathop{\lim }\limits_{{p \rightarrow + \infty }}{T}_{p} \) , so \( A = {PT}{P}^{-1} = \mathop{\lim }\limits_{{p \rightarrow + \infty }}P{T}_{p}{P}^{-1} \) is the limit of diagonalizable matrices, hence the result.

b) Dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , le résultat est faux. Nous donnons un contre-exemple. Soit \( A = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \in \; {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) . On considère l’application

> b) In \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , the result is false. We provide a counterexample. Let \( A = \left( \begin{matrix} 0 & - 1 \\ 1 & 0 \end{matrix}\right) \in \; {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) . Consider the map

\[
\Delta  : {\mathcal{M}}_{2}\left( \mathbb{R}\right)  \rightarrow  \mathbb{R}\;M \mapsto  {\Delta }_{M}
\]

où \( {\Delta }_{M} \) désigne le discriminant du polynôme caractéristique \( {P}_{M} \) de \( M \) . Comme \( {\Delta }_{M} \) s’exprime comme un polynôme en les coefficients de \( M,\Delta \) est continue.

> where \( {\Delta }_{M} \) denotes the discriminant of the characteristic polynomial \( {P}_{M} \) of \( M \) . Since \( {\Delta }_{M} \) is expressed as a polynomial in the coefficients of \( M,\Delta \) it is continuous.

Si \( A \) était limite d’une suite \( \left( {A}_{n}\right) \in {\mathcal{M}}_{2}{\left( \mathbb{R}\right) }^{\mathbb{N}} \) de matrices diagonalisables dans \( {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) , on aurait \( {\Delta }_{n} \geq 0 \) pour tout \( n \) (car \( {P}_{{A}_{n}} \) est scindé sur \( \mathbb{R} \) ), et donc \( \Delta \) étant continue, \( {\Delta }_{A} = \; \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\Delta }_{{A}_{n}} \geq 0 \) , ce qui est absurde car après calculs on trouve \( {\Delta }_{A} = - 4 \) .

> If \( A \) were the limit of a sequence \( \left( {A}_{n}\right) \in {\mathcal{M}}_{2}{\left( \mathbb{R}\right) }^{\mathbb{N}} \) of diagonalizable matrices in \( {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) , we would have \( {\Delta }_{n} \geq 0 \) for all \( n \) (since \( {P}_{{A}_{n}} \) splits over \( \mathbb{R} \) ), and thus \( \Delta \) being continuous, \( {\Delta }_{A} = \; \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\Delta }_{{A}_{n}} \geq 0 \) , which is absurd because after calculations we find \( {\Delta }_{A} = - 4 \) .

Remarque. Grâce au résultat a), on peut parfois prouver certains résultats sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) en les montrant d'abord pour les matrices diagonalisables, puis en les étendant par densité. Le lecteur pourra par exemple démontrer par cette méthode le théorème de Cayley-Hamilton pour les matrices complexes.

> Remark. Thanks to result a), one can sometimes prove certain results on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) by showing them first for diagonalizable matrices, then extending them by density. The reader may for example prove by this method the Cayley-Hamilton theorem for complex matrices.

- Si \( A \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est trigonalisable, alors \( A \) est limite d’une suite de matrices diagonali-sables de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (la solution de la question a) ne repose en effet que sur l’hypothèse que \( A \) est trigonalisable).

> - If \( A \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is trigonalizable, then \( A \) is the limit of a sequence of diagonalizable matrices of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) (the solution to question a) indeed relies only on the hypothesis that \( A \) is trigonalizable).

\( \rightarrow \) EXERCICE 2. a) Soit \( n \in {\mathbb{N}}^{ * } \) et \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer que \( \det \left( {\exp \left( A\right) }\right) = \exp \left( {\operatorname{tr}\left( A\right) }\right) \) .

> \( \rightarrow \) EXERCISE 2. a) Let \( n \in {\mathbb{N}}^{ * } \) and \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Show that \( \det \left( {\exp \left( A\right) }\right) = \exp \left( {\operatorname{tr}\left( A\right) }\right) \) .

b) Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Montrer que si \( M \) est l’exponentielle d’une matrice réelle, alors \( \det \left( M\right) > 0 \) . Montrer que la réciproque est fausse (indication : montrer que la matrice \( M = \left( \begin{matrix} - 1 & 1 \\ 0 & - 1 \end{matrix}\right) \) n’est pas un carré)

> b) Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Show that if \( M \) is the exponential of a real matrix, then \( \det \left( M\right) > 0 \) . Show that the converse is false (hint: show that the matrix \( M = \left( \begin{matrix} - 1 & 1 \\ 0 & - 1 \end{matrix}\right) \) is not a square)

Solution. a) Le corps \( \mathbb{C} \) étant algébriquement clos, on peut trigonaliser la matrice \( A \) , donc

> Solution. a) Since the field \( \mathbb{C} \) is algebraically closed, we can triangularize the matrix \( A \) , thus

\[
\exists P \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) ,\;A = {P}^{-1}{TP}\text{ avec }T = \left( \begin{matrix} {\lambda }_{1} &  \times  & \cdots &  \times  \\   & {\lambda }_{2} &  \ddots  & \vdots \\   & 0 &  \ddots  &  \times  \\   & & & {\lambda }_{n} \end{matrix}\right) .
\]

La matrice \( {T}^{k} \) est une matrice triangulaire supérieure dont les coefficients diagonaux sont les \( {\lambda }_{i}^{k} \) , donc

> The matrix \( {T}^{k} \) is an upper triangular matrix whose diagonal coefficients are the \( {\lambda }_{i}^{k} \) , thus

\[
\exp \left( T\right)  = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{1}{k!}{T}^{k} = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{1}{k!}\left( \begin{matrix} {\lambda }_{1}^{k} &  \times  & \cdots &  \times  \\   & {\lambda }_{2}^{k} &  \ddots  & \vdots \\  0 & &  \ddots  &  \times  \\   & & & {\lambda }_{n}^{k} \end{matrix}\right)  = \left( \begin{matrix} {e}^{{\lambda }_{1}} &  \times  & \cdots &  \times  \\   & {e}^{{\lambda }_{2}} &  \ddots  & \vdots \\   & &  \ddots  &  \times  \\  0 & & & {e}^{{\lambda }_{n}} \end{matrix}\right) .
\]

Ceci entraîne

> This implies

\[
\det \left( {\exp \left( T\right) }\right)  = \mathop{\prod }\limits_{{i = 1}}^{n}{e}^{{\lambda }_{i}} = \exp \left( {\mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}}\right)  = \exp \left( {\operatorname{tr}\left( T\right) }\right) .
\]

Comme \( A \) et \( T \) sont semblables, il en est de même de \( \exp \left( A\right) \) et \( \exp \left( T\right) \) , et on en déduit

> Since \( A \) and \( T \) are similar, the same holds for \( \exp \left( A\right) \) and \( \exp \left( T\right) \) , and we deduce

\[
\det \left( {\exp \left( A\right) }\right)  = \det \left( {\exp \left( T\right) }\right)  = \exp \left( {\operatorname{tr}\left( T\right) }\right)  = \exp \left( {\operatorname{tr}\left( A\right) }\right) .
\]

b) \( \operatorname{Si}M = \exp \left( A\right) \) avec \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , alors on a \( \det \left( M\right) = \exp \left( {\operatorname{tr}\left( A\right) }\right) \) d’après le résultat précédent, donc \( \det \left( M\right) > 0 \) car \( \operatorname{tr}\left( A\right) \) est un nombre réel. La réciproque est fausse, comme le montre le contre-exemple de la matrice \( M = \left( \begin{matrix} - 1 & 1 \\ 0 & - 1 \end{matrix}\right) \) . Si \( M \) était l’exponentielle d’une matrice réelle \( A \) , la matrice réelle \( N = \exp \left( {\frac{1}{2}A}\right) \) vérifierait \( {N}^{2} = \exp \left( A\right) = M \) . Or ceci est impossible car en écrivant \( N = \left( \begin{array}{ll} a & b \\ c & d \end{array}\right) \) , on aurait

> b) \( \operatorname{Si}M = \exp \left( A\right) \) with \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , then we have \( \det \left( M\right) = \exp \left( {\operatorname{tr}\left( A\right) }\right) \) according to the previous result, thus \( \det \left( M\right) > 0 \) because \( \operatorname{tr}\left( A\right) \) is a real number. The converse is false, as shown by the counterexample of the matrix \( M = \left( \begin{matrix} - 1 & 1 \\ 0 & - 1 \end{matrix}\right) \) . If \( M \) were the exponential of a real matrix \( A \) , the real matrix \( N = \exp \left( {\frac{1}{2}A}\right) \) would satisfy \( {N}^{2} = \exp \left( A\right) = M \) . However, this is impossible because by writing \( N = \left( \begin{array}{ll} a & b \\ c & d \end{array}\right) \) , we would have

\[
M = \left( \begin{matrix}  - 1 & 1 \\  0 &  - 1 \end{matrix}\right)  = {N}^{2} = \left( \begin{matrix} {a}^{2} + {bc} & {ab} + {bd} \\  {ca} + {dc} & {cb} + {d}^{2} \end{matrix}\right) .
\]

Ceci entraîne 1 \( = b\left( {a + d}\right) \) , donc \( a + d \) est non nul. Les termes inférieurs gauches donnent \( 0 = c\left( {a + d}\right) \) , donc \( c = 0 \) . L’égalité des termes diagonaux donneraient alors \( {a}^{2} = - 1 \) et \( {d}^{2} = - 1 \) , ce qui est impossible puisque \( a \) et \( d \) sont des nombres réels. Ainsi, la matrice \( M \) a bien un déterminant positif (on a \( \det \left( M\right) = 1 \) ) mais cette matrice réelle n’est pas l’exponentielle d’une matrice réelle.

> This implies 1 \( = b\left( {a + d}\right) \) , so \( a + d \) is non-zero. The lower left terms give \( 0 = c\left( {a + d}\right) \) , so \( c = 0 \) . The equality of the diagonal terms would then give \( {a}^{2} = - 1 \) and \( {d}^{2} = - 1 \) , which is impossible since \( a \) and \( d \) are real numbers. Thus, the matrix \( M \) indeed has a positive determinant (we have \( \det \left( M\right) = 1 \) ) but this real matrix is not the exponential of a real matrix.

Remarque. On peut montrer qu'une matrice réelle est l'exponentielle d'une matrice réelle si et seulement si elle est le carré d'une matrice réelle inversible.

> Remark. It can be shown that a real matrix is the exponential of a real matrix if and only if it is the square of an invertible real matrix.

- Toute matrice complexe inversible est l'exponentielle d'une matrice complexe (voir l'exercice 5 page 212).

> - Every invertible complex matrix is the exponential of a complex matrix (see exercise 5 on page 212).

\( \rightarrow \) EXERCICE 3. 1/ Soit \( \mathbb{K} \) un corps commutatif. Soient \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> \( \rightarrow \) EXERCISE 3. 1/ Let \( \mathbb{K} \) be a commutative field. Let \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

a) Si \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , montrer que \( {P}_{AB} \) , le polynôme caractéristique de \( {AB} \) , est égal à celui de \( {BA},{P}_{BA} \) .

> a) If \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , show that \( {P}_{AB} \) , the characteristic polynomial of \( {AB} \) , is equal to that of \( {BA},{P}_{BA} \) .

b) Si \( A \) est quelconque et \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) , montrer, en utilisant un argument de densité, que le résultat reste vrai.

> b) If \( A \) is arbitrary and \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \) , show, using a density argument, that the result remains true.

c) Si \( A \) est quelconque et \( \mathbb{K} \) est infini, montrer que le résultat est encore vrai.

> c) If \( A \) is arbitrary and \( \mathbb{K} \) is infinite, show that the result is still true.

\( \mathbf{2}/\mathbb{K} \) est un corps commutatif quelconque. Soient \( p, q \in {\mathbb{N}}^{ * } \) . Soit \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) et \( B \in \; {\mathcal{M}}_{q, p}\left( \mathbb{K}\right) \) . Comparer \( {P}_{AB} \) et \( {P}_{BA} \) .

> \( \mathbf{2}/\mathbb{K} \) is an arbitrary commutative field. Let \( p, q \in {\mathbb{N}}^{ * } \) . Let \( A \in {\mathcal{M}}_{p, q}\left( \mathbb{K}\right) \) and \( B \in \; {\mathcal{M}}_{q, p}\left( \mathbb{K}\right) \) . Compare \( {P}_{AB} \) and \( {P}_{BA} \) .

Solution. 1/ a) Il suffit de remarquer que les matrices \( {AB} \) et \( {BA} \) sont semblables, comme le montre la relation \( {BA} = {A}^{-1}\left( {AB}\right) A \) , elles ont donc même polynôme caractéristique.

> Solution. 1/ a) It suffices to note that the matrices \( {AB} \) and \( {BA} \) are similar, as shown by the relation \( {BA} = {A}^{-1}\left( {AB}\right) A \) , they therefore have the same characteristic polynomial.

b) On sait que \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) est dense dans \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) (voir la proposition 2). On peut donc écrire \( A = \; \mathop{\lim }\limits_{{n \rightarrow + \infty }}{A}_{n} \) avec pour tout \( n,{A}_{n} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Or d’après a), pour tout \( n,{P}_{{A}_{n}B} = {P}_{B{A}_{n}} \) et par continuité de l’application déterminant, en faisant tendre \( n \) vers \( + \infty \) , on en déduit \( {P}_{AB} = {P}_{BA} \) . c) Le corps \( \mathbb{K} \) étant infini, \( A \) n’ayant qu’un nombre fini de valeurs propres, il existe \( \Gamma \subset \mathbb{K},\Gamma \) infini, tel que pour tout \( \lambda \in \Gamma ,\lambda \) n’est pas valeur propre de \( A \) , i.e \( A - \lambda {I}_{n} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Fixons \( x \in \mathbb{K} \) . D’après \( 1/ \) a), on a

> b) We know that \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) is dense in \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) (see proposition 2). We can therefore write \( A = \; \mathop{\lim }\limits_{{n \rightarrow + \infty }}{A}_{n} \) with for all \( n,{A}_{n} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Now, according to a), for all \( n,{P}_{{A}_{n}B} = {P}_{B{A}_{n}} \) and by continuity of the determinant map, by letting \( n \) tend to \( + \infty \) , we deduce \( {P}_{AB} = {P}_{BA} \) . c) Since the field \( \mathbb{K} \) is infinite, and \( A \) has only a finite number of eigenvalues, there exists an infinite \( \Gamma \subset \mathbb{K},\Gamma \) such that for all \( \lambda \in \Gamma ,\lambda \) is not an eigenvalue of \( A \) , i.e \( A - \lambda {I}_{n} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Let us fix \( x \in \mathbb{K} \) . According to \( 1/ \) a), we have

\[
\forall \lambda  \in  \Gamma ,\;{P}_{\left( {A - \lambda {I}_{n}}\right) B}\left( x\right)  = {P}_{B\left( {A - \lambda {I}_{n}}\right) }\left( x\right) .
\]

Le polynôme \( {P}_{\left( {A - X{I}_{n}}\right) B}\left( x\right) - {P}_{B\left( {A - X{I}_{n}}\right) }\left( x\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) s’annule donc sur \( \Gamma \) , donc est nul puisque \( \Gamma \) est infini. En particulier, ce polynôme s’annule lorsque \( X \) prend la valeur0, c’est à dire \( {P}_{AB}\left( x\right) = {P}_{BA}\left( x\right) \) . Ceci étant vrai pour tout \( x \in \mathbb{K} \) , on en déduit, \( \mathbb{K} \) étant infini, que \( {P}_{AB} = {P}_{BA} \) . 2/ Soit \( r = \operatorname{rg}A \) . Supposons dans un premier temps que \( r > 0 \) . On sait que \( A \) est équivalente à la matrice \( \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , c’est-à-dire

> The polynomial \( {P}_{\left( {A - X{I}_{n}}\right) B}\left( x\right) - {P}_{B\left( {A - X{I}_{n}}\right) }\left( x\right) \in \mathbb{K}\left\lbrack X\right\rbrack \) therefore vanishes on \( \Gamma \), and is thus zero since \( \Gamma \) is infinite. In particular, this polynomial vanishes when \( X \) takes the value 0, that is to say \( {P}_{AB}\left( x\right) = {P}_{BA}\left( x\right) \). Since this is true for all \( x \in \mathbb{K} \), we deduce, \( \mathbb{K} \) being infinite, that \( {P}_{AB} = {P}_{BA} \). 2/ Let \( r = \operatorname{rg}A \). Suppose initially that \( r > 0 \). We know that \( A \) is equivalent to the matrix \( \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \), that is to say

\[
\exists P \in  \mathcal{G}{\ell }_{p}\left( \mathbb{K}\right) ,\exists Q \in  \mathcal{G}{\ell }_{q}\left( \mathbb{K}\right) ,\;A = {P}^{-1}\left( \begin{matrix} {I}_{r} & 0 \\  0 & 0 \end{matrix}\right) Q.
\]

Ecrivons

> Let us write

\[
B = {Q}^{-1}\left( \begin{array}{ll} {B}_{1} & {B}_{3} \\  {B}_{2} & {B}_{4} \end{array}\right) P
\]

où \( {B}_{1} \in {\mathcal{M}}_{r}\left( \mathbb{K}\right) \) . On a

> where \( {B}_{1} \in {\mathcal{M}}_{r}\left( \mathbb{K}\right) \). We have

\[
{AB} = {P}^{-1}\left( \begin{matrix} {B}_{1} & {B}_{3} \\  0 & 0 \end{matrix}\right) P\;\text{ et }\;{BA} = {Q}^{-1}\left( \begin{matrix} {B}_{1} & 0 \\  {B}_{2} & 0 \end{matrix}\right) Q
\]

d'où

> whence

\[
{P}_{AB} = \left| \begin{matrix} {B}_{1} - X{I}_{r} & {B}_{3} \\  0 &  - X{I}_{p - r} \end{matrix}\right|  = {\left( -1\right) }^{p - r}{X}^{p - r}{P}_{{B}_{1}}.
\]

De même, on trouve \( {P}_{BA} = {\left( -1\right) }^{q - r}{X}^{q - r}{P}_{{B}_{1}} \) . On a donc \( {\left( -X\right) }^{q}{P}_{AB} = {\left( -X\right) }^{p}{P}_{BA} \) . (Si \( p = q \) , on retrouve les résultats de 1/). Lorsque \( r = \operatorname{rg}A = 0 \) , on a \( A = 0 \) et cette identité reste vraie.

> Similarly, we find \( {P}_{BA} = {\left( -1\right) }^{q - r}{X}^{q - r}{P}_{{B}_{1}} \). We therefore have \( {\left( -X\right) }^{q}{P}_{AB} = {\left( -X\right) }^{p}{P}_{BA} \). (If \( p = q \), we recover the results of 1/). When \( r = \operatorname{rg}A = 0 \), we have \( A = 0 \) and this identity remains true.

EXERCICE 4. Soient \( n \) un entier naturel, \( n \geq 2 \) , et \( p \in \mathbb{N},1 \leq p \leq n - 1 \) . a) Montrer que \( \Gamma = \left\{ {A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \mid \operatorname{rg}A \leq p}\right\} \) est fermé dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . b) Déterminer l’adhérence de l’ensemble \( \Delta = \left\{ {A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \mid \operatorname{rg}A = p}\right\} \) .

> EXERCISE 4. Let \( n \) be a natural integer, \( n \geq 2 \), and \( p \in \mathbb{N},1 \leq p \leq n - 1 \). a) Show that \( \Gamma = \left\{ {A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \mid \operatorname{rg}A \leq p}\right\} \) is closed in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). b) Determine the closure of the set \( \Delta = \left\{ {A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \mid \operatorname{rg}A = p}\right\} \).

Solution. a) Il suffit de montrer que l'ensemble

> Solution. a) It suffices to show that the set

\[
\Lambda  = {\mathcal{M}}_{n}\left( \mathbb{R}\right)  \smallsetminus  \Gamma  = \left\{  {A \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right)  \mid  \operatorname{rg}A \geq  p + 1}\right\}
\]

est ouvert. Fixons \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \Lambda \) . Commerg \( A \geq p + 1 \) , il existe une matrice carrée extraite de \( A \) inversible d’ordre \( p + 1 \) (voir le théorème 2 page 128). Autrement dit, il existe \( I \) et \( J \) inclus dans \( \{ 1,\ldots , n\} \) avec \( \operatorname{Card}I = \operatorname{Card}J = p + 1 \) , tels que la matrice extraite \( {A}^{\prime } = {\left( {a}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) vérifie det \( {A}^{\prime } \neq 0 \) . Définissons l’application

> is open. Let us fix \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \Lambda \). Since \( A \geq p + 1 \), there exists a square submatrix of \( A \) of order \( p + 1 \) that is invertible (see theorem 2 on page 128). In other words, there exist \( I \) and \( J \) included in \( \{ 1,\ldots , n\} \) with \( \operatorname{Card}I = \operatorname{Card}J = p + 1 \), such that the submatrix \( {A}^{\prime } = {\left( {a}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) satisfies det \( {A}^{\prime } \neq 0 \). Let us define the map

\[
\varphi  : {\mathcal{M}}_{n}\left( \mathbb{R}\right)  \rightarrow  \mathbb{R}\;B = {\left( {b}_{i, j}\right) }_{1 \leq  i, j \leq  n} \mapsto  \det {\left( {b}_{i, j}\right) }_{\begin{matrix} {i \in  I} \\  {j \in  J} \end{matrix}}.
\]

L’application \( \varphi \) s’exprime comme polynôme en certains des coefficients de \( B \) , elle est donc continue. Or \( \varphi \left( A\right) = \det {A}^{\prime } \neq 0 \) , donc il existe un voisinage \( \mathcal{V} \) de \( A \) dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) tel que pour tout \( B \in \mathcal{V},\varphi \left( B\right) \neq 0 \) . Autrement dit, pour tout \( B \in \mathcal{V} \) , la matrice extraite \( {\left( {b}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) est inversible, donc rg \( B \geq p + 1 \) . Ainsi, on a trouvé un voisinage de \( A \) inclus dans \( \Lambda \) . L’ensemble \( \Lambda \) est donc ouvert.

> The map \( \varphi \) is expressed as a polynomial in some of the coefficients of \( B \), so it is continuous. However, \( \varphi \left( A\right) = \det {A}^{\prime } \neq 0 \), so there exists a neighborhood \( \mathcal{V} \) of \( A \) in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) such that for all \( B \in \mathcal{V},\varphi \left( B\right) \neq 0 \). In other words, for all \( B \in \mathcal{V} \), the extracted matrix \( {\left( {b}_{i, j}\right) }_{\begin{matrix} {i \in I} \\ {j \in J} \end{matrix}} \) is invertible, so rg \( B \geq p + 1 \). Thus, we have found a neighborhood of \( A \) included in \( \Lambda \). The set \( \Lambda \) is therefore open.

b) Nous allons montrer \( \overline{\Delta } = \Gamma \) .

> b) We will show \( \overline{\Delta } = \Gamma \) .

D’après a), \( \Gamma \) est fermé. Or \( \Delta \subset \Gamma \) , donc \( \overline{\Delta } \subset \Gamma \) .

> According to a), \( \Gamma \) is closed. However, \( \Delta \subset \Gamma \), so \( \overline{\Delta } \subset \Gamma \) .

Montrons maintenant l’inclusion réciproque. Soit \( A \in \Gamma \) . Il s’agit de montrer que \( A \) est limite d’une suite de points de \( \Delta \) . Si rg \( A = p \) , alors \( A \in \Delta \) et c’est terminé. Sinon, \( r = \operatorname{rg}A < p \) . On sait que \( A \) est équivalente à la matrice \( \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , ce qui s’écrit aussi

> Let us now show the reverse inclusion. Let \( A \in \Gamma \) . We must show that \( A \) is the limit of a sequence of points in \( \Delta \) . If rg \( A = p \), then \( A \in \Delta \) and we are done. Otherwise, \( r = \operatorname{rg}A < p \) . We know that \( A \) is equivalent to the matrix \( \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \), which can also be written as

\[
\exists P, Q \in  \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) ,\;A = {P}^{-1}\left( \begin{matrix} {I}_{r} & 0 \\  0 & 0 \end{matrix}\right) Q.
\]

Pour tout \( m \in {\mathbb{N}}^{ * } \) , on note \( {B}_{m} \) la matrice définie par blocs par

> For all \( m \in {\mathbb{N}}^{ * } \), we denote by \( {B}_{m} \) the block matrix defined by

\[
{B}_{m} = \left( \begin{matrix} {I}_{r} & 0 & 0 \\  0 & \frac{1}{m}{I}_{p - r} & 0 \\  0 & 0 & 0 \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) .
\]

Pour tout \( m,\operatorname{rg}{B}_{m} = p \) donc \( {A}_{m} = {P}^{-1}{B}_{m}Q \) est de rang \( p \) . Or \( \mathop{\lim }\limits_{{m \rightarrow + \infty }}{B}_{m} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , donc \( \mathop{\lim }\limits_{{m \rightarrow + \infty }}{A}_{m} = A \) et pour tout \( m,{A}_{m} \in \Delta \) . On a donc \( A \in \overline{\Delta } \) .

> For all \( m,\operatorname{rg}{B}_{m} = p \), therefore \( {A}_{m} = {P}^{-1}{B}_{m}Q \) has rank \( p \) . However, \( \mathop{\lim }\limits_{{m \rightarrow + \infty }}{B}_{m} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \), so \( \mathop{\lim }\limits_{{m \rightarrow + \infty }}{A}_{m} = A \) and for all \( m,{A}_{m} \in \Delta \) . We thus have \( A \in \overline{\Delta } \) .

EXERCICE 5. a) Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Pour tout \( \varepsilon > 0 \) , montrer qu’il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tel que

> EXERCISE 5. a) Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . For all \( \varepsilon > 0 \), show that there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that

\[
T = {P}^{-1}{MP} = \left( \begin{matrix} {t}_{1,1} & & \left( {t}_{i, j}\right) & \\   & {t}_{2,2} & & \\  0 & &  \ddots  & \\   & & & {t}_{n, n} \end{matrix}\right) \;\text{ avec }\;\forall i < j,\left| {t}_{i, j}\right|  < \varepsilon .
\]

b) Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer que \( A \) est nilpotente si et seulement s’il existe une suite de matrices \( {\left( {A}_{p}\right) }_{p \in \mathbb{N}} \) vérifiant

> b) Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Show that \( A \) is nilpotent if and only if there exists a sequence of matrices \( {\left( {A}_{p}\right) }_{p \in \mathbb{N}} \) satisfying

Solution. a) Soit \( f \) l’endomorphisme de \( {\mathbb{C}}^{n} \) dont la matrice dans la base canonique de \( {\mathbb{C}}^{n} \) est égale à \( M \) . Le corps \( \mathbb{C} \) étant algébriquement clos, \( f \) est trigonalisable. Il existe donc une base \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{C}}^{n} \) telle que \( {\left\lbrack f\right\rbrack }_{\mathcal{B}} \) (matrice de \( f \) dans la base \( \mathcal{B} \) ) soit triangulaire supérieure. Ecrivons \( {\left\lbrack f\right\rbrack }_{\mathcal{B}} = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \) .

> Solution. a) Let \( f \) be the endomorphism of \( {\mathbb{C}}^{n} \) whose matrix in the canonical basis of \( {\mathbb{C}}^{n} \) is equal to \( M \). Since the field \( \mathbb{C} \) is algebraically closed, \( f \) is trigonalizable. There exists, therefore, a basis \( \mathcal{B} = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{C}}^{n} \) such that \( {\left\lbrack f\right\rbrack }_{\mathcal{B}} \) (the matrix of \( f \) in the basis \( \mathcal{B} \)) is upper triangular. Let us write \( {\left\lbrack f\right\rbrack }_{\mathcal{B}} = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \).

Pour tout \( p \in {\mathbb{N}}^{ * },{\mathcal{B}}_{p} = \left( {{e}_{1},\frac{1}{p}{e}_{2},\ldots ,\frac{1}{{p}^{n - 1}}{e}_{n}}\right) \) est une base de \( {\mathbb{C}}^{n} \) . Calculons l’image par \( f \) de cette base, exprimée dans cette même base. Pour tout \( j \) , on a

> For all \( p \in {\mathbb{N}}^{ * },{\mathcal{B}}_{p} = \left( {{e}_{1},\frac{1}{p}{e}_{2},\ldots ,\frac{1}{{p}^{n - 1}}{e}_{n}}\right) \), \( {\mathbb{C}}^{n} \) is a basis of \( {\mathbb{C}}^{n} \). Let us calculate the image of this basis under \( f \), expressed in the same basis. For all \( j \), we have

\[
f\left( {\frac{1}{{p}^{j - 1}}{e}_{j}}\right)  = \mathop{\sum }\limits_{{i = 1}}^{j}{p}^{1 - j}{a}_{i, j}{e}_{i} = \mathop{\sum }\limits_{{i = 1}}^{j}{p}^{i - j}{a}_{i, j}\left( {\frac{1}{{p}^{i - 1}}{e}_{i}}\right) .
\]

On en déduit

> We deduce from this

\[
{T}_{p} = {\left\lbrack  f\right\rbrack  }_{{\mathcal{B}}_{p}} = \left( \begin{matrix} {a}_{1,1} & \frac{{a}_{1,2}}{p} & \frac{{a}_{1,3}}{{p}^{2}} & \cdots & \frac{{a}_{1, n}}{{p}^{n - 1}} \\   & {a}_{2,2} & \frac{{a}_{2,3}}{p} & & \frac{{a}_{2, n}}{{p}^{n - 2}} \\   & & {a}_{3,3} &  \ddots  & \vdots \\   & 0 & &  \ddots  & \frac{{a}_{n - 1, n}}{p} \\   & & & & {a}_{n, n} \end{matrix}\right) .
\]

Ceci étant, soit \( \mu = \mathop{\sup }\limits_{{i, j}}\left| {a}_{i, j}\right| \) et soit \( p \in {\mathbb{N}}^{ * } \) tel que \( \mu /p < \varepsilon \) . La matrice \( T = {T}_{p} = {\left( {t}_{i, j}\right) }_{1 \leq i, j \leq n} = \; {\left\lbrack f\right\rbrack }_{{\mathcal{B}}_{p}} \) est triangulaire supérieure et pour tout \( i < j,\left| {t}_{i, j}\right| = \left| {{a}_{i, j} \cdot {p}^{i - j}}\right| \leq \mu /p < \varepsilon \) . De plus \( T \) est semblable à \( {\left\lbrack f\right\rbrack }_{\mathcal{B}} \) donc à \( M \) , d’où le résultat.

> Given this, let \( \mu = \mathop{\sup }\limits_{{i, j}}\left| {a}_{i, j}\right| \) and let \( p \in {\mathbb{N}}^{ * } \) be such that \( \mu /p < \varepsilon \). The matrix \( T = {T}_{p} = {\left( {t}_{i, j}\right) }_{1 \leq i, j \leq n} = \; {\left\lbrack f\right\rbrack }_{{\mathcal{B}}_{p}} \) is upper triangular and for all \( i < j,\left| {t}_{i, j}\right| = \left| {{a}_{i, j} \cdot {p}^{i - j}}\right| \leq \mu /p < \varepsilon \). Furthermore, \( T \) is similar to \( {\left\lbrack f\right\rbrack }_{\mathcal{B}} \) and therefore to \( M \), hence the result.

b) Condition nécessaire. D’après a), pour tout \( p \in {\mathbb{N}}^{ * } \) , il existe \( {A}_{p} = {\left\lbrack {a}_{i, j}\left( p\right) \right\rbrack }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) semblable à \( A \) , triangulaire supérieure et telle que pour tout \( i < j,\left| {{a}_{i, j}\left( p\right) }\right| < 1/p \) . Or pour tout \( i > j,{a}_{i, j}\left( p\right) = 0 \) et pour tout \( i,{a}_{i, i}\left( p\right) = 0\left( {A}_{p}\right. \) étant nilpotente, ses valeurs propres \( {a}_{i, i}\left( p\right) \) sont nulles). On en déduit que pour tout \( \left( {i, j}\right) ,\left| {{a}_{i, j}\left( p\right) }\right| < 1/p \) . Donc \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{A}_{p} = 0 \) , d’où le résultat.

> b) Necessary condition. According to a), for all \( p \in {\mathbb{N}}^{ * } \), there exists \( {A}_{p} = {\left\lbrack {a}_{i, j}\left( p\right) \right\rbrack }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) similar to \( A \), upper triangular and such that for all \( i < j,\left| {{a}_{i, j}\left( p\right) }\right| < 1/p \). However, for all \( i > j,{a}_{i, j}\left( p\right) = 0 \) and for all \( i,{a}_{i, i}\left( p\right) = 0\left( {A}_{p}\right. \) being nilpotent, its eigenvalues \( {a}_{i, i}\left( p\right) \) are zero). We deduce that for all \( \left( {i, j}\right) ,\left| {{a}_{i, j}\left( p\right) }\right| < 1/p \). Thus \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{A}_{p} = 0 \), hence the result.

Condition suffisante. Pour toute matrice \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) , on note \( {P}_{M} \) son polynôme caractéris-tique. L’application \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \rightarrow \mathbb{C}\left\lbrack X\right\rbrack \;M \mapsto {P}_{M} \) est continue (en effet, les coefficients de \( {P}_{M} \) s’expriment comme des polynômes en les coefficients de \( M \) ). Or \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{A}_{p} = 0 \) , on a donc \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{P}_{{A}_{p}} = {P}_{0} = {\left( -1\right) }^{n}{X}^{n} \) . Or pour tout \( p,{A}_{p} \) est semblable à \( A \) donc \( {P}_{{A}_{p}} = {P}_{A} \) . On en déduit \( {P}_{A} = {\left( -1\right) }^{n}{X}^{n} \) . Le théorème de Cayley-Hamilton entraîne alors \( {A}^{n} = 0 \) .

> Sufficient condition. For any matrix \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \), let \( {P}_{M} \) be its characteristic polynomial. The map \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \rightarrow \mathbb{C}\left\lbrack X\right\rbrack \;M \mapsto {P}_{M} \) is continuous (indeed, the coefficients of \( {P}_{M} \) are expressed as polynomials in the coefficients of \( M \)). Since \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{A}_{p} = 0 \), we therefore have \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{P}_{{A}_{p}} = {P}_{0} = {\left( -1\right) }^{n}{X}^{n} \). However, for any \( p,{A}_{p} \), it is similar to \( A \), so \( {P}_{{A}_{p}} = {P}_{A} \). We deduce \( {P}_{A} = {\left( -1\right) }^{n}{X}^{n} \). The Cayley-Hamilton theorem then implies \( {A}^{n} = 0 \).

EXERCICE 6. Soit \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et une suite réelle \( \left( {a}_{m}\right) \) telle que \( B = \mathop{\sum }\limits_{{m = 0}}^{{+\infty }}{a}_{m}{A}^{m} \) existe. Montrer qu’il existe \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) tel que \( B = P\left( A\right) \) .

> EXERCISE 6. Let \( A \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and a real sequence \( \left( {a}_{m}\right) \) such that \( B = \mathop{\sum }\limits_{{m = 0}}^{{+\infty }}{a}_{m}{A}^{m} \) exists. Show that there exists \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( B = P\left( A\right) \).

Solution. L’ensemble \( \Gamma = \{ P\left( A\right) \mid P \in \mathbb{R}\left\lbrack X\right\rbrack \} \) est un s.e.v de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , et \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) étant de dimension finie, \( \Gamma \) est fermé.

> Solution. The set \( \Gamma = \{ P\left( A\right) \mid P \in \mathbb{R}\left\lbrack X\right\rbrack \} \) is a subspace of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), and since \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is finite-dimensional, \( \Gamma \) is closed.

Pour tout \( k \in \mathbb{N} \) , on pose \( {P}_{k} = \mathop{\sum }\limits_{{m = 0}}^{k}{a}_{m}{X}^{m} \) de sorte que \( B = \mathop{\lim }\limits_{{k \rightarrow + \infty }}{P}_{k}\left( A\right) \) . En d’autres termes, \( B \) est limite d’une suite de points de \( \Gamma \) . Comme \( \Gamma \) est fermé, on en déduit \( B \in \Gamma \) , donc il existe \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) tel que \( B = P\left( A\right) \) .

> For any \( k \in \mathbb{N} \), we set \( {P}_{k} = \mathop{\sum }\limits_{{m = 0}}^{k}{a}_{m}{X}^{m} \) such that \( B = \mathop{\lim }\limits_{{k \rightarrow + \infty }}{P}_{k}\left( A\right) \). In other words, \( B \) is the limit of a sequence of points in \( \Gamma \). Since \( \Gamma \) is closed, we deduce \( B \in \Gamma \), so there exists \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) such that \( B = P\left( A\right) \).

Remarque. En particulier, l’exponentielle d’une matrice \( M \) est un polynôme en \( M \) . La formule de Rodrigues (voir l'exercice 5 page 277) est un exemple de calcul explicite de l'exponentielle d'une matrice sous forme d'un polynôme de cette matrice.

> Remark. In particular, the exponential of a matrix \( M \) is a polynomial in \( M \). Rodrigues' formula (see exercise 5 on page 277) is an example of an explicit calculation of the exponential of a matrix as a polynomial of that matrix.

EXERCICE 7. Soit \( E \) un \( \mathbb{K} \) -e.v.n (avec \( \mathbb{K} = \mathbb{R} \) ou \( \mathbb{C} \) ). On note \( {\mathcal{L}}_{c}\left( E\right) \) l’algèbre des endo-morphismes continus de \( E \) . Soit \( f \in {\mathcal{L}}_{c}\left( E\right) \) .

> EXERCISE 7. Let \( E \) be a \( \mathbb{K} \)-normed vector space (with \( \mathbb{K} = \mathbb{R} \) or \( \mathbb{C} \)). Let \( {\mathcal{L}}_{c}\left( E\right) \) denote the algebra of continuous endomorphisms of \( E \). Let \( f \in {\mathcal{L}}_{c}\left( E\right) \).

a) Montrer que

> a) Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\left( {\operatorname{Id}}_{E} + \frac{1}{n}f\right) }^{n} = \exp \left( f\right) .
\]

b) Plus généralement, si \( \left( {f}_{n}\right) \) est une suite de \( {\mathcal{L}}_{c}\left( E\right) \) qui tend vers \( f \) , montrer

> b) More generally, if \( \left( {f}_{n}\right) \) is a sequence of \( {\mathcal{L}}_{c}\left( E\right) \) that converges to \( f \) , show

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\left( {\operatorname{Id}}_{E} + \frac{1}{n}{f}_{n}\right) }^{n} = \exp \left( f\right) .
\]

c) Soient \( u, v \in {\mathcal{L}}_{c}\left( E\right) \) . Montrer

> c) Let \( u, v \in {\mathcal{L}}_{c}\left( E\right) \) . Show

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{\left( \exp \left( \frac{u}{n}\right) \exp \left( \frac{v}{n}\right) \right) }^{n} = \exp \left( {u + v}\right) .
\]

Solution. a) Le résultat suivant nous sera utile.

> Solution. a) The following result will be useful to us.

\[
\forall g \in  {\mathcal{L}}_{c}\left( E\right) ,\;\begin{Vmatrix}{\exp \left( g\right)  - {\left( \operatorname{Id} + \frac{1}{n}g\right) }^{n}}\end{Vmatrix} \leq  \exp \left( {\parallel g\parallel }\right)  - {\left( 1 + \frac{\parallel g\parallel }{n}\right) }^{n}.
\]

(*)

> En effet. On a

Indeed. We have

\[
\exp \left( g\right)  - {\left( \operatorname{Id} + \frac{1}{n}g\right) }^{n} = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{1}{k!}{g}^{k} - \mathop{\sum }\limits_{{k = 0}}^{n}\left( \begin{array}{l} n \\  k \end{array}\right) \frac{1}{{n}^{k}}{g}^{k}.
\]

Or

\[
\forall k,1 \leq  k \leq  n,\;\left( \begin{array}{l} n \\  k \end{array}\right) \frac{1}{{n}^{k}} = \frac{n}{n} \cdot  \frac{n - 1}{n}\cdots \frac{n - k + 1}{n} \cdot  \frac{1}{k!} \leq  \frac{1}{k!},
\]

donc

> therefore

\[
\begin{Vmatrix}{\exp \left( g\right)  - {\left( \operatorname{Id} + \frac{g}{n}\right) }^{n}}\end{Vmatrix} \leq  \mathop{\sum }\limits_{{k = 1}}^{n}\left( {\frac{1}{k!} - \frac{1}{{n}^{k}}\left( \begin{array}{l} n \\  k \end{array}\right) }\right) \parallel g{\parallel }^{k} + \mathop{\sum }\limits_{{k > n}}\frac{\parallel g{\parallel }^{k}}{k!} = \exp \left( {\parallel g\parallel }\right)  - {\left( 1 + \frac{\parallel g\parallel }{n}\right) }^{n}.
\]

En appliquant \( \left( *\right) \) à \( f \) , on en déduit le résultat demandé car \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\left( 1 + \parallel f\parallel /n\right) }^{n} = \; \exp \left( {\parallel f\parallel }\right) \) .

> By applying \( \left( *\right) \) to \( f \) , we deduce the requested result because \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}{\left( 1 + \parallel f\parallel /n\right) }^{n} = \; \exp \left( {\parallel f\parallel }\right) \) .

b) On remarque déjà que

> b) We first note that

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\exp \left( {f}_{n}\right)  - {\left( \operatorname{Id} + \frac{1}{n}{f}_{n}\right) }^{n} = 0.
\]

(**)

> En effet, en posant \( {M}_{n} = \begin{Vmatrix}{f}_{n}\end{Vmatrix} \) , on a d’après (*)

Indeed, by setting \( {M}_{n} = \begin{Vmatrix}{f}_{n}\end{Vmatrix} \) , we have according to (*)

\[
\begin{Vmatrix}{\exp \left( {f}_{n}\right)  - {\left( \operatorname{Id} + \frac{{f}_{n}}{n}\right) }^{n}}\end{Vmatrix} \leq  \exp \left( {M}_{n}\right)  - {\left( 1 + \frac{{M}_{n}}{n}\right) }^{n}.
\]

(***)

> Or \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{M}_{n} = \parallel f\parallel = M \) , donc \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\exp \left( {M}_{n}\right) = \exp \left( M\right) \) et comme

However \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{M}_{n} = \parallel f\parallel = M \) , so \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\exp \left( {M}_{n}\right) = \exp \left( M\right) \) and since

\[
{\left( 1 + \frac{{M}_{n}}{n}\right) }^{n} = \exp \left( {n\log \left( {1 + \frac{{M}_{n}}{n}}\right) }\right)  = \exp \left( {n\left( {\frac{{M}_{n}}{n} + o\left( \frac{1}{n}\right) }\right) }\right)  = \exp \left( {{M}_{n} + o\left( 1\right) }\right) ,
\]

on a aussi lim \( {}_{n \rightarrow \infty }{\left( 1 + {M}_{n}/n\right) }^{n} = \exp \left( M\right) \) . D’où \( \left( {* * }\right) \) avec \( \left( {* * * }\right) \) .

> we also have lim \( {}_{n \rightarrow \infty }{\left( 1 + {M}_{n}/n\right) }^{n} = \exp \left( M\right) \) . Hence \( \left( {* * }\right) \) with \( \left( {* * * }\right) \) .

Par ailleurs, la continuité de l’application \( g \mapsto \exp \left( g\right) \) (voir la proposition 3) entraîne que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\exp \left( {f}_{n}\right) - \exp \left( f\right) = 0 \) . On en déduit avec (**) le résultat car

> Furthermore, the continuity of the map \( g \mapsto \exp \left( g\right) \) (see proposition 3) implies that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\exp \left( {f}_{n}\right) - \exp \left( f\right) = 0 \) . We deduce the result from (**) because

\[
{\left( \operatorname{Id} + \frac{1}{n}{f}_{n}\right) }^{n} = \left( {{\left( \operatorname{Id} + \frac{1}{n}{f}_{n}\right) }^{n} - \exp \left( {f}_{n}\right) }\right)  + \left( {\exp \left( {f}_{n}\right)  - \exp \left( f\right) }\right)  + \exp \left( f\right) .
\]

c) Lorsque \( n \) tend vers \( + \infty \) , on a

> c) When \( n \) converges to \( + \infty \) , we have

\[
\exp \left( \frac{u}{n}\right)  = \operatorname{Id} + \frac{u}{n} + o\left( \frac{1}{n}\right) \;\text{ et }\;\exp \left( \frac{v}{n}\right)  = \operatorname{Id} + \frac{v}{n} + o\left( \frac{1}{n}\right) ,
\]

donc

> therefore

\[
{f}_{n} = n\left( {\exp \left( \frac{u}{n}\right) \exp \left( \frac{v}{n}\right)  - \operatorname{Id}}\right) \;\text{ vérifie }\;{f}_{n} = u + v + o\left( 1\right) .
\]

Autrement dit \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{n} = u + v \) , donc d’après la question précédente, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\left( \operatorname{Id} + {f}_{n}/n\right) }^{n} = \; \exp \left( {u + v}\right) \) , d’où le résultat car \( \left( {\operatorname{Id} + {f}_{n}/n}\right) = \exp \left( {u/n}\right) \exp \left( {v/n}\right) \) .

> In other words \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{f}_{n} = u + v \) , so according to the previous question, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{\left( \operatorname{Id} + {f}_{n}/n\right) }^{n} = \; \exp \left( {u + v}\right) \) , hence the result because \( \left( {\operatorname{Id} + {f}_{n}/n}\right) = \exp \left( {u/n}\right) \exp \left( {v/n}\right) \) .

Remarque. La proposition 5 (page 194) peut se déduire facilement du résultat de la question a).

> Remark. Proposition 5 (page 194) can be easily deduced from the result of question a).

EXERCICE 8. Soit \( E \) un \( \mathbb{C} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Soit \( g \in \mathcal{L}\left( E\right) \) . Montrer que \( g \) est diagonalisable si et seulement si l’ensemble \( \Phi = \left\{ {{\varphi }^{-1}{g\varphi } \mid \varphi \in \mathcal{G}\ell \left( E\right) }\right\} \) est fermé.

> EXERCISE 8. Let \( E \) be a finite-dimensional \( \mathbb{C} \) -v.s. \( n \in {\mathbb{N}}^{ * } \) . Let \( g \in \mathcal{L}\left( E\right) \) . Show that \( g \) is diagonalizable if and only if the set \( \Phi = \left\{ {{\varphi }^{-1}{g\varphi } \mid \varphi \in \mathcal{G}\ell \left( E\right) }\right\} \) is closed.

Solution. Condition nécessaire. Soit \( \Pi \) le polynôme minimal de \( g \) . Comme \( g \) est diagonalisable, \( \Pi \) n’a que des racines simples. Pour tout \( \varphi \in \mathcal{G}\ell \left( E\right) \) , on a \( \Pi \left( {{\varphi }^{-1}{g\varphi }}\right) = {\varphi }^{-1}\Pi \left( g\right) \varphi = 0 \) , donc pour tout \( h \in \Phi ,\Pi \left( h\right) = 0 \) .

> Solution. Necessary condition. Let \( \Pi \) be the minimal polynomial of \( g \) . Since \( g \) is diagonalizable, \( \Pi \) has only simple roots. For all \( \varphi \in \mathcal{G}\ell \left( E\right) \) , we have \( \Pi \left( {{\varphi }^{-1}{g\varphi }}\right) = {\varphi }^{-1}\Pi \left( g\right) \varphi = 0 \) , therefore for all \( h \in \Phi ,\Pi \left( h\right) = 0 \) .

Soit \( h \in \overline{\Phi } \) . L’endomorphisme \( h \) est limite d’une suite \( \left( {h}_{p}\right) \) de points de \( \Phi \) . Comme pour tout \( p,\Pi \left( {h}_{p}\right) = 0 \) , on a \( \Pi \left( h\right) = \mathop{\lim }\limits_{{p \rightarrow \infty }}\Pi \left( {h}_{p}\right) = 0 \) . L’endomorphisme \( h \) étant annulé par un polynôme n’ayant que des racines simples, on en déduit que \( h \) est diagonalisable. Or le polynôme caractéristique \( {P}_{h} \) de \( h \) vérifie \( {P}_{h} = \mathop{\lim }\limits_{{p \rightarrow + \infty }}{P}_{{h}_{p}} = {P}_{g} \) car pour tout \( p,{P}_{{h}_{p}} = {P}_{g} \) . Les endomorphismes \( g \) et \( h \) ont donc même liste de valeurs propres; comme ils sont de plus diagonalisables, on en déduit que \( g \) et \( h \) sont semblables, donc que \( h \in \Phi \) .

> Let \( h \in \overline{\Phi } \) . The endomorphism \( h \) is the limit of a sequence \( \left( {h}_{p}\right) \) of points in \( \Phi \) . Since for all \( p,\Pi \left( {h}_{p}\right) = 0 \) , we have \( \Pi \left( h\right) = \mathop{\lim }\limits_{{p \rightarrow \infty }}\Pi \left( {h}_{p}\right) = 0 \) . As the endomorphism \( h \) is annihilated by a polynomial having only simple roots, we deduce that \( h \) is diagonalizable. However, the characteristic polynomial \( {P}_{h} \) of \( h \) satisfies \( {P}_{h} = \mathop{\lim }\limits_{{p \rightarrow + \infty }}{P}_{{h}_{p}} = {P}_{g} \) because for all \( p,{P}_{{h}_{p}} = {P}_{g} \) . The endomorphisms \( g \) and \( h \) therefore have the same list of eigenvalues; since they are also diagonalizable, we deduce that \( g \) and \( h \) are similar, and thus that \( h \in \Phi \) .

Condition suffisante. Supposons \( \Phi \) fermé. Le corps \( \mathbb{C} \) étant algébriquement clos, \( g \) est trigonali-sable. Il existe donc une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) dans laquelle la matrice de \( g \) ait la forme

> Sufficient condition. Suppose \( \Phi \) is closed. Since the field \( \mathbb{C} \) is algebraically closed, \( g \) is triangularizable. There exists a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) in which the matrix of \( g \) has the form

\[
{\left\lbrack  g\right\rbrack  }_{B} = \left( \begin{matrix} {\lambda }_{1} & {t}_{1,2} & \cdots & {t}_{1, n} \\  0 & {\lambda }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  & {t}_{n - 1, n} \\  0 & \cdots & 0 & {\lambda }_{n} \end{matrix}\right)
\]

Pour tout \( p \in {\mathbb{N}}^{ * } \) , on définit \( {\varphi }_{p} \in \mathcal{L}\left( E\right) \) sur la base \( B \) par \( {\varphi }_{p}\left( {e}_{i}\right) = \frac{1}{{p}^{i}}{e}_{i} \) pour tout \( i \) . On a

> For all \( p \in {\mathbb{N}}^{ * } \) , we define \( {\varphi }_{p} \in \mathcal{L}\left( E\right) \) on the basis \( B \) by \( {\varphi }_{p}\left( {e}_{i}\right) = \frac{1}{{p}^{i}}{e}_{i} \) for all \( i \) . We have

\[
{\left\lbrack  {\varphi }_{p}^{-1}g{\varphi }_{p}\right\rbrack  }_{B} = \left( \begin{matrix} {\lambda }_{1} & \frac{{t}_{1,2}}{p} & \frac{{t}_{1,3}}{{p}^{2}} & \cdots & \frac{{t}_{1, n}}{{p}^{n - 1}} \\   & {\lambda }_{2} & \frac{{t}_{2,3}}{p} & & \frac{{t}_{2, n}}{{p}^{n - 2}} \\   & & {\lambda }_{3} &  \ddots  & \vdots \\   & 0 & &  \ddots  & \frac{{t}_{n - 1, n}}{p} \\   & & & & {\lambda }_{n} \end{matrix}\right)
\]

donc lorsque \( p \) tend vers \( + \infty ,{\varphi }_{p}^{-1}g{\varphi }_{p} \) tend vers un endomorphisme diagonalisable \( h \) . Comme \( \Phi \) est fermé, on a \( h \in \Phi \) donc \( g \) est semblable à \( h \) , donc \( g \) est diagonalisable.

> therefore when \( p \) tends to \( + \infty ,{\varphi }_{p}^{-1}g{\varphi }_{p} \) , it tends to a diagonalizable endomorphism \( h \) . Since \( \Phi \) is closed, we have \( h \in \Phi \) , therefore \( g \) is similar to \( h \) , and thus \( g \) is diagonalizable.

Remarque. La condition suffisante fait appel au résultat de la question a) de l'exercice 5 page 198, redémontré ici.

> Remark. The sufficient condition relies on the result from question a) of exercise 5 on page 198, re-proven here.
