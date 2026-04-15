#### 1.4. Trigonalization

*Français : 1.4. Trigonalisation*

DÉFINITION 6. Un endomorphisme \( f \in \mathcal{L}\left( E\right) \) est dit trigonalisable s’il existe une base \( B \) de \( E \) dans laquelle la matrice de \( f \) soit triangulaire supérieure. On dit alors que la base \( B \) trigonalise \( f \) .

> DEFINITION 6. An endomorphism \( f \in \mathcal{L}\left( E\right) \) is said to be trigonalizable if there exists a basis \( B \) of \( E \) in which the matrix of \( f \) is upper triangular. We then say that the basis \( B \) trigonalizes \( f \) .

Une matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est dite trigonalisable si \( A \) est semblable à une matrice triangulaire supérieure.

> A matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is said to be trigonalizable if \( A \) is similar to an upper triangular matrix.

Remarque 8. Un endomorphisme \( f \) est trigonalisable si et seulement si sa matrice dans une base quelconque de \( E \) est trigonalisable.

> Remark 8. An endomorphism \( f \) is trigonalizable if and only if its matrix in any basis of \( E \) is trigonalizable.

\( \rightarrow \) THÉORÉME 3. Un endomorphisme \( f \in \mathcal{L}\left( E\right) \) est trigonalisable si et seulement si son polynôme caractéristique \( {P}_{f} \) est scindé sur \( \mathbb{K} \) .

> \( \rightarrow \) THEOREM 3. An endomorphism \( f \in \mathcal{L}\left( E\right) \) is trigonalizable if and only if its characteristic polynomial \( {P}_{f} \) splits over \( \mathbb{K} \) .

Démonstration.

> Proof.

Condition nécessaire. C’est le plus facile. Soit \( B \) une base de trigonalisation de \( f \) . On a

> Necessary condition. This is the easiest part. Let \( B \) be a trigonalization basis of \( f \) . We have

\[
T = {\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} {\lambda }_{1} &  \times  & \cdots &  \times  \\  0 & {\lambda }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\lambda }_{n} \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,
\]

donc \( {P}_{f} = {P}_{T} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) est scindé sur \( \mathbb{K} \) .

> therefore \( {P}_{f} = {P}_{T} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) splits over \( \mathbb{K} \) .

Condition suffisante. Nous allons procéder par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) . Nous allons donner deux méthodes pour montrer le résultat au rang \( n \) .

> Sufficient condition. We will proceed by induction on \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) , it is obvious. Assume the result is true at rank \( n - 1 \) . We will provide two methods to show the result at rank \( n \) .

Première méthode. Le polynôme caractéristique de l’application transposée \( {}^{\mathrm{t}}f \) vérifie \( {P}^{\mathrm{t}}{}_{f} = {P}_{f} \) , don \( {P}_{{}^{\mathrm{t}}f} \) est scindé sur \( \mathbb{K} \) , donc d’après la proposition 1, \( {}^{\mathrm{t}}f \) admet un vecteur propre \( x \) dans le dual \( {E}^{ * } \) , donc \( \mathbb{K}x \) est stable par \( {}^{\mathrm{t}}f \) . On en déduit que l’orthogonal \( H \) de \( \mathbb{K}x \) dans \( E \) est un hyperplan stable par \( f \) (voir la proposition 8 page 136). D’après la proposition 2, le polynôme caractéristique de la restriction de \( f \) à \( H\left( {{f}_{\mid H}\text{ est bien un endomorphisme puisque }H}\right. \) est stable par \( f \) ) divise \( {P}_{f} \) donc est scindé sur \( \mathbb{K} \) , ce qui entraîne d’après l’hypothèse de récurrence l’existence d’une base \( {B}_{1} = \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) de \( H \) dans laquelle \( {f}_{\mid H} \) se trigonalise. Complétons cette base de \( H \) en une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . La base \( B \) triangule \( f \) car

> First method. The characteristic polynomial of the transpose map \( {}^{\mathrm{t}}f \) satisfies \( {P}^{\mathrm{t}}{}_{f} = {P}_{f} \) , so \( {P}_{{}^{\mathrm{t}}f} \) is split over \( \mathbb{K} \) , therefore according to proposition 1, \( {}^{\mathrm{t}}f \) admits an eigenvector \( x \) in the dual \( {E}^{ * } \) , so \( \mathbb{K}x \) is stable by \( {}^{\mathrm{t}}f \) . We deduce that the orthogonal \( H \) of \( \mathbb{K}x \) in \( E \) is a stable hyperplane under \( f \) (see proposition 8 page 136). According to proposition 2, the characteristic polynomial of the restriction of \( f \) to \( H\left( {{f}_{\mid H}\text{ est bien un endomorphisme puisque }H}\right. \) divides \( {P}_{f} \) and is therefore split over \( \mathbb{K} \) , which implies, by the induction hypothesis, the existence of a basis \( {B}_{1} = \left( {{e}_{1},\ldots ,{e}_{n - 1}}\right) \) of \( H \) in which \( {f}_{\mid H} \) is trigonalized. Let us complete this basis of \( H \) into a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . The basis \( B \) trigonalizes \( f \) because

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix}  & & &  \times  \\  {\left\lbrack  {f}_{\mid H}\right\rbrack  }_{{B}_{1}} & & &  \div  \\  0 & \cdots & 0 &  \times   \end{matrix}\right)  = \left( \begin{matrix}  \times  & \cdots & \cdots &  \times  \\  0 &  \ddots  & & \vdots \\  \vdots &  \ddots  &  \ddots  & \vdots \\  0 & \cdots & 0 &  \times   \end{matrix}\right) .
\]

Seconde méthode. D'après la proposition 1, il existe un vecteur propre \( {e}_{1} \) de \( f \) . Complétons \( {e}_{1} \) en une base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) , et notons \( H = \operatorname{Vect}\left( {{e}_{2},\ldots ,{e}_{n}}\right) \) . On a

> Second method. According to proposition 1, there exists an eigenvector \( {e}_{1} \) of \( f \) . Let us complete \( {e}_{1} \) into a basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) , and denote \( H = \operatorname{Vect}\left( {{e}_{2},\ldots ,{e}_{n}}\right) \) . We have

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} \alpha  \times  \cdots  \times  \\  0 \\  \vdots \\  0 \end{matrix}\right) \;\text{ avec }\;M \in  {\mathcal{M}}_{n - 1}\left( \mathbb{K}\right) ,
\]

où \( M \) est la matrice de l’endomorphisme \( g \in \mathcal{L}\left( H\right) \) défini par \( g = p \circ {f}_{\mid H} \) , où \( p \) est la projection sur \( H \) parallèlement à \( \mathbb{K}{e}_{1} \) . On a \( {P}_{f} = \left( {\alpha - X}\right) {P}_{M} = \left( {\alpha - X}\right) {P}_{g} \) , donc \( {P}_{g} \) est scindé sur \( \mathbb{K} \) , donc d’après l’hypothèse de récurrence, il existe une base \( {B}_{1} = \left( {{f}_{2},\ldots ,{f}_{n}}\right) \) de \( H \) qui trigonalise \( g \) . La base \( {B}^{\prime } = \left( {{e}_{1},{f}_{2},\ldots ,{f}_{n}}\right) \) trigonalise \( f \) car on a

> where \( M \) is the matrix of the endomorphism \( g \in \mathcal{L}\left( H\right) \) defined by \( g = p \circ {f}_{\mid H} \) , where \( p \) is the projection onto \( H \) parallel to \( \mathbb{K}{e}_{1} \) . We have \( {P}_{f} = \left( {\alpha - X}\right) {P}_{M} = \left( {\alpha - X}\right) {P}_{g} \) , so \( {P}_{g} \) is split over \( \mathbb{K} \) , therefore according to the induction hypothesis, there exists a basis \( {B}_{1} = \left( {{f}_{2},\ldots ,{f}_{n}}\right) \) of \( H \) that trigonalizes \( g \) . The basis \( {B}^{\prime } = \left( {{e}_{1},{f}_{2},\ldots ,{f}_{n}}\right) \) trigonalizes \( f \) because we have

\[
{\left\lbrack  f\right\rbrack  }_{{B}^{\prime }} = \left( \begin{matrix} \alpha &  \times  & \cdots &  \times  \\  0 & & & \\  \vdots & & {\left\lbrack  g\right\rbrack  }_{{B}_{1}} & \\  0 & & &  \end{matrix}\right) .
\]

Remarque 9. - La version matricielle de ce résultat est : une matrice \( M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est trigonalisable si et seulement si son polynôme caractéristique est scindé sur \( \mathbb{K} \) .

> Remark 9. - The matrix version of this result is: a matrix \( M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is trigonalizable if and only if its characteristic polynomial is split over \( \mathbb{K} \) .

- Si \( f \in  \mathcal{L}\left( E\right) \) est trigonalisable et si \( F \) est un s.e.v stable par \( f \) , alors l’endomor-phisme \( {f}_{\mid F} \) est trigonalisable (en effet, \( {P}_{{f}_{\mid F}} \) divise \( {P}_{f} \) donc est scindé sur \( \mathbb{K} \) ).

> - If \( f \in  \mathcal{L}\left( E\right) \) is trigonalizable and if \( F \) is a subspace stable by \( f \), then the endomorphism \( {f}_{\mid F} \) is trigonalizable (indeed, \( {P}_{{f}_{\mid F}} \) divides \( {P}_{f} \) and is therefore split over \( \mathbb{K} \)).

- Si \( \mathbb{K} \) est algébriquement clos (par exemple \( \mathbb{K} = \mathbb{C} \) ), tout endomorphisme du \( \mathbb{K} \) - espace vectoriel \( E \) est trigonalisable.

> - If \( \mathbb{K} \) is algebraically closed (for example \( \mathbb{K} = \mathbb{C} \)), any endomorphism of the \( \mathbb{K} \)-vector space \( E \) is trigonalizable.

— La trigonalisation d'une matrice peut être intéressante pour montrer une propriété.

> — The trigonalization of a matrix can be useful for proving a property.

— Le produit de deux matrices triangulaires supérieures est triangulaire supérieure, ses coefficients diagonaux sont les produits des coefficients diagonaux :

> — The product of two upper triangular matrices is upper triangular, its diagonal coefficients are the products of the diagonal coefficients:

\[
\left( \begin{matrix} {\alpha }_{1} &  \times  & \cdots &  \times  \\  0 & {\alpha }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\alpha }_{n} \end{matrix}\right) \left( \begin{matrix} {\beta }_{1} &  \times  & \cdots &  \times  \\  0 & {\beta }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\beta }_{n} \end{matrix}\right)  = \left( \begin{matrix} {\alpha }_{1}{\beta }_{1} &  \times  & \cdots &  \times  \\  0 & {\alpha }_{2}{\beta }_{2} &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \times  \\  0 & \cdots & 0 & {\alpha }_{n}{\beta }_{n} \end{matrix}\right) .
\]

- On verra dans la section 4 page 201 des réductions plus poussées.

> - We will see more advanced reductions in section 4 on page 201.
