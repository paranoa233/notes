#### 1.3. Exercises

*Français : 1.3. Exercices*

EXERCICE 1. Soit \( \mathbb{K} \) un corps commutatif et \( E \) un \( \mathbb{K} \) -e.v.

> EXERCISE 1. Let \( \mathbb{K} \) be a commutative field and \( E \) a \( \mathbb{K} \) -v.s.

a) Soient \( F \) et \( G \) deux s.e.v de \( E \) . Si \( F \cup G \) est un s.e.v de \( E \) , montrer que \( F \subset G \) ou \( G \subset F \) .

> a) Let \( F \) and \( G \) be two v.s.s. of \( E \) . If \( F \cup G \) is a v.s.s. of \( E \) , show that \( F \subset G \) or \( G \subset F \) .

b) Soit \( k \geq 2 \) et \( {\left( {V}_{i}\right) }_{1 \leq i \leq k} \) une famille finie de \( k \) s.e.v stricts de \( E \) (i. e. pour tout \( i \) , \( {V}_{i} \neq \{ 0\} \) et \( \left. {{V}_{i} \neq E}\right) \) . Si \( E = {V}_{1} \cup \cdots \cup {V}_{k} \) , montrer que \( \mathbb{K} \) est fini et que \( k \geq \operatorname{Card}\left( \mathbb{K}\right) + 1 \) . Cette inégalité peut-elle être une égalité ?

> b) Let \( k \geq 2 \) and \( {\left( {V}_{i}\right) }_{1 \leq i \leq k} \) be a finite family of \( k \) proper v.s.s. of \( E \) (i.e., for all \( i \) , \( {V}_{i} \neq \{ 0\} \) and \( \left. {{V}_{i} \neq E}\right) \) . If \( E = {V}_{1} \cup \cdots \cup {V}_{k} \) , show that \( \mathbb{K} \) is finite and that \( k \geq \operatorname{Card}\left( \mathbb{K}\right) + 1 \) . Can this inequality be an equality?

Solution. a) Raisonnons par l’absurde et supposons que \( F \text{ ⊄ } G \) et \( G \text{ ⊄ } F \) , de sorte qu’il existe \( x \in F, x \notin G \) , et il existe \( y \in G, y \notin F \) . Le vecteur \( x + y \) est dans le s.e.v \( F \cup G \) , donc \( x + y \in F \) ou \( x + y \in G \) . Supposons par exemple \( x + y \in F \) . Comme \( F \) est un s.e.v et que \( x \in F \) , on a \( \left( {x + y}\right) - x \in F \) , c’est-à-dire \( y \in F \) , ce qui est absurde. D’où le résultat.

> Solution. a) Let us reason by contradiction and assume that \( F \text{ ⊄ } G \) and \( G \text{ ⊄ } F \) , so that there exists \( x \in F, x \notin G \) , and there exists \( y \in G, y \notin F \) . The vector \( x + y \) is in the subspace \( F \cup G \) , so \( x + y \in F \) or \( x + y \in G \) . Assume for example \( x + y \in F \) . Since \( F \) is a subspace and \( x \in F \) , we have \( \left( {x + y}\right) - x \in F \) , that is to say \( y \in F \) , which is absurd. Hence the result.

b) C’est plus délicat. Quitte à retirer \( {V}_{1} \) , on peut supposer \( {V}_{1} \text{ ⊄ } \left( {{V}_{2} \cup \cdots \cup {V}_{k}}\right) \) . Il existe donc \( x \in {V}_{1} \) tel que \( x \notin {V}_{2} \cup \cdots \cup {V}_{k} \) . Or \( \left( {{V}_{2} \cup \cdots \cup {V}_{k}}\right) \text{ ⊄ } {V}_{1} \) (sinon \( {V}_{1} = E \) ), donc il existe \( y \in {V}_{2} \cup \cdots \cup {V}_{k} \) tel que \( y \notin {V}_{1} \) .

> b) This is more delicate. By removing \( {V}_{1} \) if necessary, we can assume \( {V}_{1} \text{ ⊄ } \left( {{V}_{2} \cup \cdots \cup {V}_{k}}\right) \) . There therefore exists \( x \in {V}_{1} \) such that \( x \notin {V}_{2} \cup \cdots \cup {V}_{k} \) . However \( \left( {{V}_{2} \cup \cdots \cup {V}_{k}}\right) \text{ ⊄ } {V}_{1} \) (otherwise \( {V}_{1} = E \) ), so there exists \( y \in {V}_{2} \cup \cdots \cup {V}_{k} \) such that \( y \notin {V}_{1} \) .

Si \( \lambda \in \mathbb{K} \) , alors \( y + {\lambda x} \in E \) . Or \( y + {\lambda x} \notin {V}_{1} \) (sinon \( y \in {V}_{1} \) car \( x \in {V}_{1} \) ), donc pour tout \( \lambda \in \mathbb{K} \) , il existe \( {i}_{\lambda } \in \{ 2,\ldots , k\} \) tel que \( y + {\lambda x} \in {V}_{{i}_{\lambda }} \) . L’application \( \mathbb{K} \rightarrow \{ 2,\ldots , k\} \;\lambda \mapsto {i}_{\lambda } \) est injective (en effet, si \( {i}_{\lambda } = {i}_{\mu } \) , alors \( y + {\lambda x} \) et \( y + {\mu x} \in {V}_{{i}_{\lambda }} \) donc \( \left( {\lambda - \mu }\right) x \in {V}_{{i}_{\lambda }} \) , et comme \( x \notin {V}_{{i}_{\lambda }} \) , on doit avoir \( \lambda = \mu \) ). De cette injectivité, on déduit que \( \operatorname{Card}\left( \mathbb{K}\right) \leq \operatorname{Card}\{ 2,\ldots , k\} = k - 1 \) , d’où l'inégalité souhaitée.

> If \( \lambda \in \mathbb{K} \) , then \( y + {\lambda x} \in E \) . However \( y + {\lambda x} \notin {V}_{1} \) (otherwise \( y \in {V}_{1} \) because \( x \in {V}_{1} \) ), so for all \( \lambda \in \mathbb{K} \) , there exists \( {i}_{\lambda } \in \{ 2,\ldots , k\} \) such that \( y + {\lambda x} \in {V}_{{i}_{\lambda }} \) . The map \( \mathbb{K} \rightarrow \{ 2,\ldots , k\} \;\lambda \mapsto {i}_{\lambda } \) is injective (indeed, if \( {i}_{\lambda } = {i}_{\mu } \) , then \( y + {\lambda x} \) and \( y + {\mu x} \in {V}_{{i}_{\lambda }} \) so \( \left( {\lambda - \mu }\right) x \in {V}_{{i}_{\lambda }} \) , and since \( x \notin {V}_{{i}_{\lambda }} \) , we must have \( \lambda = \mu \) ). From this injectivity, we deduce that \( \operatorname{Card}\left( \mathbb{K}\right) \leq \operatorname{Card}\{ 2,\ldots , k\} = k - 1 \) , hence the desired inequality.

Cette inégalité peut être une égalité. Par exemple, si \( \mathbb{K} = \mathbb{Z}/2\mathbb{Z} \) et \( E = {\mathbb{K}}^{2} \) , si \( {V}_{1} = \; \left\{ {\left( {\dot{0},\dot{0}}\right) ,\left( {\dot{0},\dot{1}}\right) }\right\} ,{V}_{2} = \{ \left( {\dot{0},\dot{0}}\right) ,\left( {\dot{1},\dot{0}}\right) \} \) et \( {V}_{3} = \{ \left( {\dot{0},\dot{0}}\right) ,\left( {\dot{1},\dot{1}}\right) \} \) , alors \( {V}_{1},{V}_{2} \) et \( {V}_{3} \) sont des s.e.v stricts de \( E \) et \( {V}_{1} \cup {V}_{2} \cup {V}_{3} = E \) .

> This inequality can be an equality. For example, if \( \mathbb{K} = \mathbb{Z}/2\mathbb{Z} \) and \( E = {\mathbb{K}}^{2} \) , if \( {V}_{1} = \; \left\{ {\left( {\dot{0},\dot{0}}\right) ,\left( {\dot{0},\dot{1}}\right) }\right\} ,{V}_{2} = \{ \left( {\dot{0},\dot{0}}\right) ,\left( {\dot{1},\dot{0}}\right) \} \) and \( {V}_{3} = \{ \left( {\dot{0},\dot{0}}\right) ,\left( {\dot{1},\dot{1}}\right) \} \) , then \( {V}_{1},{V}_{2} \) and \( {V}_{3} \) are strict subspaces of \( E \) and \( {V}_{1} \cup {V}_{2} \cup {V}_{3} = E \) .

EXERCICE 2. Montrer que dans le \( \mathbb{R} \) -e.v des fonctions continues de \( \mathbb{R} \) dans \( \mathbb{R} \) , les familles de fonctions suivantes sont des familles libres :

> EXERCISE 2. Show that in the \( \mathbb{R} \) -v.s. of continuous functions from \( \mathbb{R} \) to \( \mathbb{R} \) , the following families of functions are linearly independent:

a) \( {\left( {f}_{\lambda }\right) }_{\lambda \in \mathbb{R}} \) où \( {f}_{\lambda } : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {e}^{\lambda x} \) .

> a) \( {\left( {f}_{\lambda }\right) }_{\lambda \in \mathbb{R}} \) where \( {f}_{\lambda } : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {e}^{\lambda x} \) .

b) \( {\left( {f}_{\lambda }\right) }_{\lambda \in {\mathbb{R}}^{ + }} \) où \( {f}_{\lambda } : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \cos \left( {\lambda x}\right) \) .

> b) \( {\left( {f}_{\lambda }\right) }_{\lambda \in {\mathbb{R}}^{ + }} \) where \( {f}_{\lambda } : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \cos \left( {\lambda x}\right) \) .

c) \( {\left( {f}_{\lambda }\right) }_{\lambda \in \mathbb{R}} \) où \( {f}_{\lambda } : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \left| {x - \lambda }\right| \) .

> c) \( {\left( {f}_{\lambda }\right) }_{\lambda \in \mathbb{R}} \) where \( {f}_{\lambda } : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \left| {x - \lambda }\right| \) .

Solution. a) Supposons cette famille liée, de sorte qu’il existe \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n} \in {\mathbb{R}}^{n} \) et \( \left( {\mu }_{i}\right) \in {\mathbb{R}}^{n} \) tels que \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} = 0 \) avec les \( {\mu }_{i} \) non tous nuls. Quitte à retirer des termes, on peut supposer \( {\mu }_{i} \neq 0 \) pour tout \( i \) . Quitte à réordonner des termes, on peut même supposer \( {\lambda }_{1} > {\lambda }_{2} > \cdots > {\lambda }_{n} \) . On a

> Solution. a) Suppose this family is linearly dependent, such that there exist \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n} \in {\mathbb{R}}^{n} \) and \( \left( {\mu }_{i}\right) \in {\mathbb{R}}^{n} \) such that \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} = 0 \) with the \( {\mu }_{i} \) not all zero. By removing terms, we can assume \( {\mu }_{i} \neq 0 \) for all \( i \) . By reordering terms, we can even assume \( {\lambda }_{1} > {\lambda }_{2} > \cdots > {\lambda }_{n} \) . We have

\[
\mathop{\lim }\limits_{{x \rightarrow   + \infty }}{e}^{-{\lambda }_{1}x}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{e}^{{\lambda }_{i}x}}\right)  = \mathop{\lim }\limits_{{x \rightarrow   + \infty }}\mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{e}^{\left( {{\lambda }_{i} - {\lambda }_{1}}\right) x} = {\mu }_{1},
\]

car pour \( i \geq 2,{\lambda }_{i} - {\lambda }_{1} < 0 \) . Or \( \mathop{\sum }\limits_{i}{\mu }_{i}{f}_{{\lambda }_{i}} = 0 \) , et cette limite est donc nulle, donc \( {\mu }_{1} = 0 \) , ce qui est contradictoire.

> because for \( i \geq 2,{\lambda }_{i} - {\lambda }_{1} < 0 \) . However \( \mathop{\sum }\limits_{i}{\mu }_{i}{f}_{{\lambda }_{i}} = 0 \) , and this limit is therefore zero, so \( {\mu }_{1} = 0 \) , which is a contradiction.

b) Montrons par récurrence sur \( n \in {\mathbb{N}}^{ * } \) que si \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} = 0 \) (avec les \( {\lambda }_{i} \) distincts dans \( {\mathbb{R}}^{ + } \) ), alors pour tout \( i,{\mu }_{i} = 0 \) . Pour \( n = 1 \) c’est évident. Supposons maintenant le résultat vrai jusqu’au rang \( n - 1 \) et montrons le au rang \( n \) . Si \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} = 0\;\left( *\right) \) , les \( \left( {\lambda }_{i}\right) \) distincts dans \( {\mathbb{R}}^{ + } \) , par double dérivation, on obtient \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}\left( {-{\lambda }_{i}^{2}{f}_{{\lambda }_{i}}}\right) = 0\;\left( {* * }\right) \) . En multipliant l’égalité (*) par \( {\lambda }_{n}^{2} \) et en l’ajoutant à \( \left( {* * }\right) \) , on obtient \( \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{\mu }_{i}\left( {{\lambda }_{i}^{2} - {\lambda }_{n}^{2}}\right) {f}_{{\lambda }_{i}} = 0 \) , donc d’après l’hypothèse de récurrence, pour tout \( 1 \leq i \leq n - 1,{\mu }_{i}\left( {{\lambda }_{i}^{2} - {\lambda }_{n}^{2}}\right) = 0 \) . Les \( {\lambda }_{i} \) étant positifs et distincts. on en déduit \( {\mu }_{i} = 0 \) pour \( 1 \leq i \leq n - 1 \) . Donc d’après \( \left( *\right) ,{\mu }_{n}{f}_{{\lambda }_{n}} = 0 \) , d’où \( {\mu }_{n} = 0 \) . Finalement on a montré \( {\mu }_{i} = 0 \) pour \( 1 \leq i \leq n \) .

> b) Let us show by induction on \( n \in {\mathbb{N}}^{ * } \) that if \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} = 0 \) (with the \( {\lambda }_{i} \) distinct in \( {\mathbb{R}}^{ + } \) ), then for all \( i,{\mu }_{i} = 0 \) . For \( n = 1 \) it is obvious. Now assume the result is true up to rank \( n - 1 \) and show it for rank \( n \) . If \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} = 0\;\left( *\right) \) , the \( \left( {\lambda }_{i}\right) \) distinct in \( {\mathbb{R}}^{ + } \) , by double differentiation, we obtain \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}\left( {-{\lambda }_{i}^{2}{f}_{{\lambda }_{i}}}\right) = 0\;\left( {* * }\right) \) . By multiplying the equality (*) by \( {\lambda }_{n}^{2} \) and adding it to \( \left( {* * }\right) \) , we obtain \( \mathop{\sum }\limits_{{i = 1}}^{{n - 1}}{\mu }_{i}\left( {{\lambda }_{i}^{2} - {\lambda }_{n}^{2}}\right) {f}_{{\lambda }_{i}} = 0 \) , therefore according to the induction hypothesis, for all \( 1 \leq i \leq n - 1,{\mu }_{i}\left( {{\lambda }_{i}^{2} - {\lambda }_{n}^{2}}\right) = 0 \) . The \( {\lambda }_{i} \) being positive and distinct, we deduce \( {\mu }_{i} = 0 \) for \( 1 \leq i \leq n - 1 \) . Thus according to \( \left( *\right) ,{\mu }_{n}{f}_{{\lambda }_{n}} = 0 \) , hence \( {\mu }_{n} = 0 \) . Finally, we have shown \( {\mu }_{i} = 0 \) for \( 1 \leq i \leq n \) .

c) Supposons la famille \( {\left( {f}_{\lambda }\right) }_{\lambda \in \mathbb{R}} \) liée. Alors il existe \( {\lambda }_{0} \in \mathbb{R} \) tel que \( {f}_{{\lambda }_{0}} \) s’écrive comme une combinaison linéaire des \( {\left( {f}_{\lambda }\right) }_{\lambda \neq {\lambda }_{0}} \) , autrement dit :

> c) Suppose the family \( {\left( {f}_{\lambda }\right) }_{\lambda \in \mathbb{R}} \) is linearly dependent. Then there exists \( {\lambda }_{0} \in \mathbb{R} \) such that \( {f}_{{\lambda }_{0}} \) can be written as a linear combination of the \( {\left( {f}_{\lambda }\right) }_{\lambda \neq {\lambda }_{0}} \) , in other words:

\[
\exists n \in  {\mathbb{N}}^{ * },\exists {\lambda }_{1},\ldots ,{\lambda }_{n} \in  \mathbb{R} \smallsetminus  \left\{  {\lambda }_{0}\right\}  ,\exists {\mu }_{1},\ldots ,{\mu }_{n} \in  \mathbb{R},\;{f}_{{\lambda }_{0}} = \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}}.
\]

Or pour tout \( i \geq 1,{\lambda }_{i} \neq {\lambda }_{0} \) donc \( {f}_{{\lambda }_{i}} \) est dérivable au point \( {\lambda }_{0} \) (l’application \( x \mapsto \left| {x - \lambda }\right| \) est dérivable partout sauf en \( \lambda \) ), d’où on tire que \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} \) est dérivable en \( {\lambda }_{0} \) , ce qui est absurde car ceci égale \( {f}_{{\lambda }_{0}} \) . D’où le résultat.

> However, for all \( i \geq 1,{\lambda }_{i} \neq {\lambda }_{0} \) , \( {f}_{{\lambda }_{i}} \) is differentiable at point \( {\lambda }_{0} \) (the mapping \( x \mapsto \left| {x - \lambda }\right| \) is differentiable everywhere except at \( \lambda \) ), from which we derive that \( \mathop{\sum }\limits_{{i = 1}}^{n}{\mu }_{i}{f}_{{\lambda }_{i}} \) is differentiable at \( {\lambda }_{0} \) , which is absurd because this equals \( {f}_{{\lambda }_{0}} \) . Hence the result.

Remarque. On aurait pu résoudre le a) comme on l'a fait pour b). L'avantage de cette dernière méthode est qu'elle aurait permit de conclure même si l'intervalle de définition des \( \left( {f}_{\lambda }\right) \) n’était pas \( \mathbb{R} \) tout entier.

> Remark. We could have solved a) as we did for b). The advantage of the latter method is that it would have allowed us to conclude even if the interval of definition of the \( \left( {f}_{\lambda }\right) \) was not the entire \( \mathbb{R} \).

EXERCICE 3. Soit \( E \) un \( \mathbb{K} \) -espace vectoriel de dimension finie, et \( A \) et \( B \) deux s.e.v de \( E \) de même dimension \( r \) . Montrer que \( A \) et \( B \) admettent un supplémentaire commun (i. e. il existe un s.e.v \( S \) de \( E \) tel que \( A \oplus S = B \oplus S = E \) ).

> EXERCISE 3. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -vector space, and \( A \) and \( B \) be two subspaces of \( E \) of the same dimension \( r \) . Show that \( A \) and \( B \) admit a common supplementary subspace (i.e., there exists a subspace \( S \) of \( E \) such that \( A \oplus S = B \oplus S = E \) ).

Solution. Nous allons effectuer une récurrence descendante sur \( r \leq \dim E \) . Si \( r = \dim E \) , c’est évident car \( \{ 0\} \) est un supplémentaire commun à \( A \) et à \( B \) . Supposons le résultat vérifié au rang \( r + 1 \leq \dim E \) et démontrons le au rang \( r \) .

> Solution. We will perform a downward induction on \( r \leq \dim E \) . If \( r = \dim E \) , it is obvious because \( \{ 0\} \) is a common supplementary subspace to \( A \) and \( B \) . Assume the result holds for rank \( r + 1 \leq \dim E \) and prove it for rank \( r \) .

On a \( A \cup B \neq E \) . En effet, supposons \( A \cup B = E \) . Comme \( A \text{ ⊄ } B \) (sinon \( E = A \cup B = B \) ), il existe \( x \in A \) tel que \( x \notin B \) . De même, il existe \( y \in B, y \notin A \) . Or \( x + y \in E = A \cup B \) , donc \( x + y \in A \) ou \( x + y \in B \) , par exemple \( x + y \in A \) . Alors \( y = \left( {x + y}\right) - x \in A \) , ce qui est absurde. On a donc bien \( A \cup B \neq E \) .

> We have \( A \cup B \neq E \) . Indeed, suppose \( A \cup B = E \) . Since \( A \text{ ⊄ } B \) (otherwise \( E = A \cup B = B \) ), there exists \( x \in A \) such that \( x \notin B \) . Similarly, there exists \( y \in B, y \notin A \) . However, \( x + y \in E = A \cup B \) , so \( x + y \in A \) or \( x + y \in B \) , for example \( x + y \in A \) . Then \( y = \left( {x + y}\right) - x \in A \) , which is absurd. Thus, we indeed have \( A \cup B \neq E \) .

Donc il existe \( x \in E, x \notin A \cup B \) . Soit \( {A}^{\prime } = A + \operatorname{Vect}\left( x\right) ,{B}^{\prime } = B + \operatorname{Vect}\left( x\right) \) . On a \( \dim {A}^{\prime } = \; \dim {B}^{\prime } = r + 1 \) , donc d’après l’hypothèse de récurrence, il existe un s.e.v \( {S}^{\prime } \) de \( E \) tel que \( {A}^{\prime } \oplus {S}^{\prime } = {B}^{\prime } \oplus {S}^{\prime } = E \) . Si \( S = {S}^{\prime } + \operatorname{Vect}\left( x\right) \) , on a donc \( E = {A}^{\prime } \oplus {S}^{\prime } = A \oplus \operatorname{Vect}\left( x\right) \oplus {S}^{\prime } = A \oplus S \) et \( E = {B}^{\prime } \oplus {S}^{\prime } = B \oplus \operatorname{Vect}\left( x\right) \oplus {S}^{\prime } = B \oplus S \) , d’où le résultat.

> Therefore, there exists \( x \in E, x \notin A \cup B \) . Let \( {A}^{\prime } = A + \operatorname{Vect}\left( x\right) ,{B}^{\prime } = B + \operatorname{Vect}\left( x\right) \) . We have \( \dim {A}^{\prime } = \; \dim {B}^{\prime } = r + 1 \) , so according to the induction hypothesis, there exists a subspace \( {S}^{\prime } \) of \( E \) such that \( {A}^{\prime } \oplus {S}^{\prime } = {B}^{\prime } \oplus {S}^{\prime } = E \) . If \( S = {S}^{\prime } + \operatorname{Vect}\left( x\right) \) , we then have \( E = {A}^{\prime } \oplus {S}^{\prime } = A \oplus \operatorname{Vect}\left( x\right) \oplus {S}^{\prime } = A \oplus S \) and \( E = {B}^{\prime } \oplus {S}^{\prime } = B \oplus \operatorname{Vect}\left( x\right) \oplus {S}^{\prime } = B \oplus S \) , hence the result.
