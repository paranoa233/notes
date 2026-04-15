### 2. Similarity invariants

*Français : 2. Invariants de similitude*

Le théorème qui suit est le point central de notre discussion.

> The following theorem is the central point of our discussion.

THÉORÉME 1. Soit \( f \in \mathcal{L}\left( E\right) \) . Il existe une suite \( {F}_{1},{F}_{2},\ldots ,{F}_{r} \) de s.e.v de \( E \) , tous stables par \( f \) , telle que

> THEOREM 1. Let \( f \in \mathcal{L}\left( E\right) \) . There exists a sequence \( {F}_{1},{F}_{2},\ldots ,{F}_{r} \) of subspaces of \( E \) , all stable under \( f \) , such that

(i) \( E = {F}_{1} \oplus {F}_{2} \oplus \cdots \oplus {F}_{r} \) ,

> (ii) pour tout \( i \in \{ 1,\ldots , r\} \) , la restriction \( {f}_{i} = {f}_{\mid {F}_{i}} \) de l’endomorphisme \( f \) au s.e.v \( {F}_{i} \) est un endomorphisme de \( {F}_{i} \) cyclique,

(ii) for all \( i \in \{ 1,\ldots , r\} \) , the restriction \( {f}_{i} = {f}_{\mid {F}_{i}} \) of the endomorphism \( f \) to the subspace \( {F}_{i} \) is a cyclic endomorphism of \( {F}_{i} \) ,

> (iii) si \( {P}_{i} \) désigne le polynôme minimal de \( {f}_{i} \) , on a \( {P}_{i + 1} \mid {P}_{i} \) pour tout \( i \in \{ 1,\ldots , r - 1\} \) . La suite de polynômes \( {P}_{1},\ldots ,{P}_{r} \) ne dépend que de \( f \) et non du choix de la décomposition. On l’appelle suite des invariants de similitude \( {de}f \) .

(iii) if \( {P}_{i} \) denotes the minimal polynomial of \( {f}_{i} \) , we have \( {P}_{i + 1} \mid {P}_{i} \) for all \( i \in \{ 1,\ldots , r - 1\} \) . The sequence of polynomials \( {P}_{1},\ldots ,{P}_{r} \) depends only on \( f \) and not on the choice of the decomposition. It is called the sequence of similarity invariants \( {de}f \) .

> Démonstration. Existence. Soit \( k = \deg \left( {\Pi }_{f}\right) \) et soit \( x \in E \) tel que \( {P}_{x} = {\Pi }_{f} \) . Le s.e.v \( F = {E}_{x} \) est de dimension \( k \) et il est stable par \( f \) . Comme \( \deg \left( {P}_{x}\right) = k \) , la famille de vecteurs

Proof. Existence. Let \( k = \deg \left( {\Pi }_{f}\right) \) and let \( x \in E \) be such that \( {P}_{x} = {\Pi }_{f} \) . The subspace \( F = {E}_{x} \) has dimension \( k \) and is stable under \( f \) . Since \( \deg \left( {P}_{x}\right) = k \) , the family of vectors

\[
{e}_{1} = x,\;{e}_{2} = f\left( x\right) ,\cdots ,\;{e}_{k} = {f}^{k - 1}\left( x\right)
\]

forme une base de \( F = {E}_{x} \) . Complétons cette base en une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) . En désignant par \( \left( {{e}_{1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) la base duale associée, on note

> forms a basis of \( F = {E}_{x} \) . Let us complete this basis into a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) . Denoting by \( \left( {{e}_{1}^{ * },\ldots ,{e}_{n}^{ * }}\right) \) the associated dual basis, we note

\[
G = {\Gamma }^{ \circ  }\text{ où }\Gamma  = \left\{  {{}^{\mathrm{t}}{f}^{i}\left( {e}_{k}^{ * }\right)  \mid  i \in  \mathbb{N}}\right\}   = \left\{  {{e}_{k}^{ * } \circ  {f}^{i}, i \in  \mathbb{N}}\right\}
\]

(orthogonal vis-à-vis du dual). En d’autres termes, \( G \) est l’ensemble des \( x \in E \) tels que la \( k \) -ième coordonnée de \( {f}^{i}\left( x\right) \) (dans la base \( \left. \left( {{e}_{1},\ldots ,{e}_{n}}\right) \right) \) soit nulle pour tout \( i \) . L’ensemble \( G \) est un s.e.v de \( E \) , et il est stable par \( f \) comme on le vérifie facilement.

> (orthogonal with respect to the dual). In other words, \( G \) is the set of \( x \in E \) such that the \( k \) -th coordinate of \( {f}^{i}\left( x\right) \) (in the basis \( \left. \left( {{e}_{1},\ldots ,{e}_{n}}\right) \right) \) is zero for all \( i \) . The set \( G \) is a subspace of \( E \) , and it is stable under \( f \) as is easily verified.

Nous allons montrer \( F \oplus G = E \) , et pour cela, nous prouvons successivement \( F \cap G = \{ 0\} \) et \( \dim F + \dim G = n \) .

> We will show \( F \oplus G = E \) , and for this, we prove successively \( F \cap G = \{ 0\} \) and \( \dim F + \dim G = n \) .

Soit \( y \in F \cap G \) . Si \( y \neq 0 \) , on peut écrire \( y = {a}_{1}{e}_{1} + \cdots + {a}_{p}{e}_{p} \) avec \( {a}_{p} \neq 0 \) et \( p \leq k \) . En composant par \( {}^{\mathrm{t}}{f}^{k - p}\left( {e}_{k}^{ * }\right) = {e}_{k}^{ * } \circ {f}^{k - p} \) , on obtient

> Let \( y \in F \cap G \) . If \( y \neq 0 \) , we can write \( y = {a}_{1}{e}_{1} + \cdots + {a}_{p}{e}_{p} \) with \( {a}_{p} \neq 0 \) and \( p \leq k \) . By composing with \( {}^{\mathrm{t}}{f}^{k - p}\left( {e}_{k}^{ * }\right) = {e}_{k}^{ * } \circ {f}^{k - p} \) , we obtain

\[
0 = {e}_{k}^{ * }\left( {{a}_{1}{e}_{k - p + 1} + \cdots  + {a}_{p}{e}_{k}}\right)  = {a}_{p},
\]

ce qui est absurde. Donc \( F \cap G = \{ 0\} \) .

> which is absurd. Therefore \( F \cap G = \{ 0\} \) .

Comme \( G = {\left( \operatorname{Vect}\Gamma \right) }^{ \circ } \) , pour montrer \( \dim G = n - \dim F = n - k \) , il suffit de prouver \( \dim \left( {\operatorname{Vect}\Gamma }\right) = k \) . Pour cela, on considère l’application linéaire

> Since \( G = {\left( \operatorname{Vect}\Gamma \right) }^{ \circ } \) , to show \( \dim G = n - \dim F = n - k \) , it suffices to prove \( \dim \left( {\operatorname{Vect}\Gamma }\right) = k \) . For this, we consider the linear map

\[
\varphi  : {\mathcal{L}}_{f} = \{ P\left( f\right)  \mid  P \in  \mathbb{K}\left\lbrack  X\right\rbrack  \}  \rightarrow  \operatorname{Vect}\Gamma \;g \mapsto  {e}_{k}^{ * } \circ  g.
\]

Par définition de \( \operatorname{Vect}\Gamma ,\varphi \) est surjective. De plus, \( \varphi \) est injective. En effet, si \( {e}_{k}^{ * } \circ g = 0 \) avec \( g \neq 0 \) , on peut écrire \( g = {a}_{1}{\operatorname{Id}}_{E} + \cdots + {a}_{p}{f}^{p - 1} \in {\mathcal{L}}_{f} \) (avec \( p \leq k \) et \( {a}_{p} \neq 0 \) ) et

> By definition of \( \operatorname{Vect}\Gamma ,\varphi \) is surjective. Furthermore, \( \varphi \) is injective. Indeed, if \( {e}_{k}^{ * } \circ g = 0 \) with \( g \neq 0 \) , we can write \( g = {a}_{1}{\operatorname{Id}}_{E} + \cdots + {a}_{p}{f}^{p - 1} \in {\mathcal{L}}_{f} \) (with \( p \leq k \) and \( {a}_{p} \neq 0 \) ) and

\[
0 = {e}_{k}^{ * } \circ  g\left( {{f}^{k - p}\left( x\right) }\right)  = {e}_{k}^{ * }\left( {{a}_{1}{f}^{k - p}\left( x\right)  + \cdots  + {a}_{p}{f}^{k - 1}\left( x\right) }\right)  = {e}_{k}^{ * }\left( {{a}_{1}{e}_{k - p + 1} + \cdots  + {a}_{p}{e}_{k}}\right)  = {a}_{p},
\]

ce qui est absurde. Finalement, \( \varphi \) est un isomorphisme donc dim(Vect \( \Gamma ) = \dim {\mathcal{L}}_{f} = k \) .

> which is absurd. Finally, \( \varphi \) is an isomorphism, therefore dim(Vect \( \Gamma ) = \dim {\mathcal{L}}_{f} = k \) .

Résumons. Nous avons trouvé un sous espace \( G \) stable par \( f \) tel que \( F \oplus G = E \) . Notons \( {P}_{1} \) le polynôme minimal de \( {f}_{\mid F} \) ,(qui est le polynôme minimal de \( f \) car \( {P}_{1} = {P}_{x} = {\Pi }_{f} \) ), et \( {P}_{2} \) le polynôme minimal de \( {f}_{\mid G} \) . Comme \( G \) est stable par \( f,{P}_{2} \mid {P}_{1} \) . On applique ce qui précède à \( {f}_{\mid G} \) , et au bout d'un nombre fini d'étapes, on obtient la décomposition voulue.

> Let's summarize. We have found a subspace \( G \) invariant under \( f \) such that \( F \oplus G = E \) . Let \( {P}_{1} \) be the minimal polynomial of \( {f}_{\mid F} \) (which is the minimal polynomial of \( f \) because \( {P}_{1} = {P}_{x} = {\Pi }_{f} \) ), and \( {P}_{2} \) be the minimal polynomial of \( {f}_{\mid G} \) . Since \( G \) is invariant under \( f,{P}_{2} \mid {P}_{1} \) . We apply the above to \( {f}_{\mid G} \) , and after a finite number of steps, we obtain the desired decomposition.

Unicité. Supposons l’existence de deux suites de sous espaces \( {F}_{1},\ldots ,{F}_{r} \) et \( {G}_{1},\ldots ,{G}_{s} \) tous stables par \( f \) et vérifiant les conditions (i),(ii) et (iii). Notons \( {P}_{i} = {\Pi }_{{f}_{\mid {F}_{i}}} \) et \( {Q}_{j} = {\Pi }_{{f}_{\mid {G}_{j}}} \) .

> Uniqueness. Suppose the existence of two sequences of subspaces \( {F}_{1},\ldots ,{F}_{r} \) and \( {G}_{1},\ldots ,{G}_{s} \) all invariant under \( f \) and satisfying conditions (i), (ii), and (iii). Let \( {P}_{i} = {\Pi }_{{f}_{\mid {F}_{i}}} \) and \( {Q}_{j} = {\Pi }_{{f}_{\mid {G}_{j}}} \) .

On voit que \( {P}_{1} = {\Pi }_{f} = {Q}_{1} \) . Supposons la liste \( \left( {{P}_{1},\ldots ,{P}_{r}}\right) \) différente de \( \left( {{Q}_{1},\ldots ,{Q}_{s}}\right) \) et notons \( j \) le premier indice tel que \( {P}_{j} \neq {Q}_{j} \) (un tel indice existe toujours même si \( r \neq s \) , car \( \mathop{\sum }\limits_{i}\deg \left( {P}_{i}\right) = n = \mathop{\sum }\limits_{j}\deg \left( {Q}_{j}\right) ) \) . L’égalité \( E = {F}_{1} \oplus \cdots \oplus {F}_{r} \) avec les \( {F}_{i} \) stables par \( f \) , et la propriété \( {P}_{j}\left( f\right) \left( {F}_{k}\right) = 0 \) pour \( k \geq j \) , entraînent

> We see that \( {P}_{1} = {\Pi }_{f} = {Q}_{1} \) . Suppose the list \( \left( {{P}_{1},\ldots ,{P}_{r}}\right) \) is different from \( \left( {{Q}_{1},\ldots ,{Q}_{s}}\right) \) and let \( j \) be the first index such that \( {P}_{j} \neq {Q}_{j} \) (such an index always exists even if \( r \neq s \) , because \( \mathop{\sum }\limits_{i}\deg \left( {P}_{i}\right) = n = \mathop{\sum }\limits_{j}\deg \left( {Q}_{j}\right) ) \) . The equality \( E = {F}_{1} \oplus \cdots \oplus {F}_{r} \) with the \( {F}_{i} \) invariant under \( f \) , and the property \( {P}_{j}\left( f\right) \left( {F}_{k}\right) = 0 \) for \( k \geq j \) , imply

\[
{P}_{j}\left( f\right) \left( E\right)  = {P}_{j}\left( f\right) \left( {F}_{1}\right)  \oplus  \cdots  \oplus  {P}_{j}\left( f\right) \left( {F}_{j - 1}\right)
\]

(*)

> et par ailleurs l’égalité \( E = {G}_{1} \oplus \cdots \oplus {G}_{s} \) avec les \( {G}_{j} \) stables par \( f \) entraîne

and furthermore the equality \( E = {G}_{1} \oplus \cdots \oplus {G}_{s} \) with the \( {G}_{j} \) invariant under \( f \) implies

\[
{P}_{j}\left( f\right) \left( E\right)  = {P}_{j}\left( f\right) \left( {G}_{1}\right)  \oplus  \cdots  \oplus  {P}_{j}\left( f\right) \left( {G}_{j - 1}\right)  \oplus  {P}_{j}\left( f\right) \left( {G}_{j}\right)  \oplus  \cdots  \oplus  {P}_{j}\left( f\right) \left( {G}_{s}\right)
\]

\( \left( {* * }\right) \)

> On a dim \( {P}_{j}\left( f\right) \left( {F}_{i}\right) = \dim {P}_{j}\left( f\right) \left( {G}_{i}\right) \) pour \( 1 \leq i \leq j - 1 \) (en effet, d’après la proposition 3, on peut trouver une base \( {B}_{i} \) de \( {F}_{i} \) et une base \( {B}_{i}^{\prime } \) de \( {G}_{i} \) telles que la matrice de \( {f}_{\mid {F}_{i}} \) dans \( {B}_{i} \) coïncide avec la matrice de \( {f}_{\mid {G}_{i}} \) dans \( {B}_{i}^{\prime } \) ). En prenant les dimensions dans \( \left( *\right) \) et \( \left( {* * }\right) \) , on en déduit

We have dim \( {P}_{j}\left( f\right) \left( {F}_{i}\right) = \dim {P}_{j}\left( f\right) \left( {G}_{i}\right) \) for \( 1 \leq i \leq j - 1 \) (indeed, according to proposition 3, we can find a basis \( {B}_{i} \) of \( {F}_{i} \) and a basis \( {B}_{i}^{\prime } \) of \( {G}_{i} \) such that the matrix of \( {f}_{\mid {F}_{i}} \) in \( {B}_{i} \) coincides with the matrix of \( {f}_{\mid {G}_{i}} \) in \( {B}_{i}^{\prime } \) ). By taking the dimensions in \( \left( *\right) \) and \( \left( {* * }\right) \) , we deduce

\[
0 = \dim {P}_{j}\left( f\right) \left( {G}_{j}\right)  = \cdots  = \dim {P}_{j}\left( f\right) \left( {G}_{s}\right) ,
\]

ce qui prouve que \( {Q}_{j} \mid {P}_{j} \) . Par symétrie de rôle, on a aussi \( {P}_{j} \mid {Q}_{j} \) , donc \( {P}_{j} = {Q}_{j} \) ce qui est absurde. Finalement, on doit avoir \( r = s \) et \( {P}_{i} = {Q}_{i} \) pour tout \( i \) .

> which proves that \( {Q}_{j} \mid {P}_{j} \) . By symmetry of roles, we also have \( {P}_{j} \mid {Q}_{j} \) , so \( {P}_{j} = {Q}_{j} \) which is absurd. Finally, we must have \( r = s \) and \( {P}_{i} = {Q}_{i} \) for all \( i \) .

THÉORÉME 2 (RÉDUCTION DE FROBENIUS). Si \( {P}_{1},\ldots ,{P}_{r} \) désigne la suite des invariants de similitude de \( f \in \mathcal{L}\left( E\right) \) , il existe une base \( B \) de \( E \) telle que

> THEOREM 2 (FROBENIUS REDUCTION). If \( {P}_{1},\ldots ,{P}_{r} \) denotes the sequence of similarity invariants of \( f \in \mathcal{L}\left( E\right) \), there exists a basis \( B \) of \( E \) such that

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} \mathcal{C}\left( {P}_{1}\right) & & 0 \\   &  \ddots  & \\  0 & & \mathcal{C}\left( {P}_{r}\right)  \end{matrix}\right) .
\]

On a d’ailleurs \( {P}_{1} = {\Pi }_{f} \) et \( {P}_{1}\cdots {P}_{r} \) est le polynôme caractéristique de \( f \) (au facteur \( {\left( -1\right) }^{n} \) près).

> Moreover, we have \( {P}_{1} = {\Pi }_{f} \) and \( {P}_{1}\cdots {P}_{r} \) is the characteristic polynomial of \( f \) (up to a factor of \( {\left( -1\right) }^{n} \)).

Démonstration. Il suffit pour tout \( i \) de considérer une base \( {B}_{i} \) de \( {F}_{i} \) dans laquelle la matrice de \( {f}_{i} = {f}_{\mid {F}_{i}} \) est \( \mathcal{C}\left( {P}_{i}\right) \) (ce qui est possible d’après la proposition 3), puis d’écrire la matrice de \( f \) dans la base \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \) .

> Proof. It suffices for every \( i \) to consider a basis \( {B}_{i} \) of \( {F}_{i} \) in which the matrix of \( {f}_{i} = {f}_{\mid {F}_{i}} \) is \( \mathcal{C}\left( {P}_{i}\right) \) (which is possible according to proposition 3), then to write the matrix of \( f \) in the basis \( B = \left( {{B}_{1},\ldots ,{B}_{r}}\right) \).

Comme pour les matrices, on dit que deux endomorphismes \( f, g \in \mathcal{L}\left( E\right) \) sont sem-blables s’il existe \( h \in \mathcal{G}\ell \left( E\right) \) tel que \( f = {h}^{-1}{gh} \) . Muni de cette définition, on a le résultat suivant.

> As with matrices, we say that two endomorphisms \( f, g \in \mathcal{L}\left( E\right) \) are similar if there exists \( h \in \mathcal{G}\ell \left( E\right) \) such that \( f = {h}^{-1}{gh} \). Equipped with this definition, we have the following result.

COROLLAIRE 1. Deux endomorphismes \( f \) et \( g \in \mathcal{L}\left( E\right) \) sont semblables si et seulement s'ils ont les mêmes invariants de similitude.

> COROLLARY 1. Two endomorphisms \( f \) and \( g \in \mathcal{L}\left( E\right) \) are similar if and only if they have the same similarity invariants.

Démonstration. Si \( f \) et \( g \) sont semblables, on montre facilement en reprenant la preuve de l’unicité dans le théorème 1 que \( f \) et \( g \) ont les mêmes invariants de similitude.

> Proof. If \( f \) and \( g \) are similar, it is easily shown by revisiting the proof of uniqueness in theorem 1 that \( f \) and \( g \) have the same similarity invariants.

Réciproquement, si \( f \) et \( g \) ont les mêmes invariants de similitude, le théorème précédent assure l’existence de deux bases \( B \) et \( {B}^{\prime } \) de \( E \) telles que \( {\left\lbrack f\right\rbrack }_{B} = {\left\lbrack g\right\rbrack }_{{B}^{\prime }} \) ce qui signifie que \( f \) et \( g \) sont semblables.

> Conversely, if \( f \) and \( g \) have the same similarity invariants, the previous theorem ensures the existence of two bases \( B \) and \( {B}^{\prime } \) of \( E \) such that \( {\left\lbrack f\right\rbrack }_{B} = {\left\lbrack g\right\rbrack }_{{B}^{\prime }} \), which means that \( f \) and \( g \) are similar.
