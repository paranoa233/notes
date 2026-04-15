### 6. Problems

*Français : 6. Problèmes*

Problem 1. Résoudre dans \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) l’équation \( {A}^{2} = - {I}_{n} \) .

> Problem 1. Solve the equation \( {A}^{2} = - {I}_{n} \) in \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

Solution. Comme \( {A}^{2} = - {I}_{n} \) , on a \( \det \left( {A}^{2}\right) = {\left( \det A\right) }^{2} = {\left( -1\right) }^{n} \) donc \( n \) est pair. Soit \( p \in {\mathbb{N}}^{ * } \) tel que \( n = {2p} \) . Soit \( f \) l’endomorphisme de \( {\mathbb{R}}^{n} \) dont \( A \) est la matrice dans la base canonique de \( {\mathbb{R}}^{n} \) . On va démontrer, en procédant par récurrence sur \( k \) , le résultat suivant : pour tout \( k,1 \leq k \leq p \) , il existe \( {x}_{1},\ldots ,{x}_{k} \in E = {\mathbb{R}}^{n} \) tels que \( \left( {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{k}, f\left( {x}_{k}\right) }\right) \) forme une famille libre.

> Solution. Since \( {A}^{2} = - {I}_{n} \) , we have \( \det \left( {A}^{2}\right) = {\left( \det A\right) }^{2} = {\left( -1\right) }^{n} \) therefore \( n \) is even. Let \( p \in {\mathbb{N}}^{ * } \) be such that \( n = {2p} \) . Let \( f \) be the endomorphism of \( {\mathbb{R}}^{n} \) whose matrix in the canonical basis of \( {\mathbb{R}}^{n} \) is \( A \) . We will prove, by proceeding by induction on \( k \) , the following result: for all \( k,1 \leq k \leq p \) , there exist \( {x}_{1},\ldots ,{x}_{k} \in E = {\mathbb{R}}^{n} \) such that \( \left( {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{k}, f\left( {x}_{k}\right) }\right) \) forms a free family.

Montrons ce résultat pour \( k = 1 \) . Soit \( {x}_{1} \in E,{x}_{1} \neq 0 \) . Si \( \lambda {x}_{1} + {\mu f}\left( {x}_{1}\right) = 0 \) , alors par composition par \( f \) , on tire \( {\lambda f}\left( {x}_{1}\right) - \mu {x}_{1} = 0 \) . Finalement, on en déduit :

> Let us show this result for \( k = 1 \) . Let \( {x}_{1} \in E,{x}_{1} \neq 0 \) . If \( \lambda {x}_{1} + {\mu f}\left( {x}_{1}\right) = 0 \) , then by composition with \( f \) , we obtain \( {\lambda f}\left( {x}_{1}\right) - \mu {x}_{1} = 0 \) . Finally, we deduce:

\[
\left( {{\lambda }^{2} + {\mu }^{2}}\right) {x}_{1} = \lambda \left\lbrack  {\lambda {x}_{1} + {\mu f}\left( {x}_{1}\right) }\right\rbrack   - \mu \left\lbrack  {{\lambda f}\left( {x}_{1}\right)  - \mu {x}_{1}}\right\rbrack   = 0.
\]

Donc \( {\lambda }^{2} + {\mu }^{2} = 0 \) , c’est-à-dire \( \lambda = \mu = 0 \) . La famille \( \left( {{x}_{1}, f\left( {x}_{1}\right) }\right) \) est donc libre.

> Therefore \( {\lambda }^{2} + {\mu }^{2} = 0 \) , that is to say \( \lambda = \mu = 0 \) . The family \( \left( {{x}_{1}, f\left( {x}_{1}\right) }\right) \) is therefore free.

Supposons maintenant le résultat vrai au rang \( k - 1 \) et montrons le au rang \( k \leq p \) . D’après l’hypothèse de récurrence, il existe \( {x}_{1},\ldots ,{x}_{k - 1} \in E \) tels que \( \left( {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{k - 1}, f\left( {x}_{k - 1}\right) }\right) \) forme une famille libre. Soit \( {F}_{k - 1} = \operatorname{Vect}\left\{ {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{k - 1}, f\left( {x}_{k - 1}\right) }\right\} \) . On a \( \dim {F}_{k - 1} = {2k} - 2 < {2p} \) , donc on peut choisir \( {x}_{k} \in E,{x}_{k} \notin {F}_{k - 1} \) . Supposons maintenant une égalité du type :

> Now assume the result is true at rank \( k - 1 \) and show it at rank \( k \leq p \) . According to the induction hypothesis, there exist \( {x}_{1},\ldots ,{x}_{k - 1} \in E \) such that \( \left( {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{k - 1}, f\left( {x}_{k - 1}\right) }\right) \) forms a free family. Let \( {F}_{k - 1} = \operatorname{Vect}\left\{ {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{k - 1}, f\left( {x}_{k - 1}\right) }\right\} \) . We have \( \dim {F}_{k - 1} = {2k} - 2 < {2p} \) , so we can choose \( {x}_{k} \in E,{x}_{k} \notin {F}_{k - 1} \) . Now assume an equality of the type:

\[
{\lambda }_{1}{x}_{1} + {\mu }_{1}f\left( {x}_{1}\right)  + \cdots  + {\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right)  = 0.
\]

Alors \( {\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right) \in {F}_{k - 1} \) et \( {F}_{k - 1} \) étant stable par \( f, f\left\lbrack {{\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right) }\right\rbrack = {\lambda }_{k}f\left( {x}_{k}\right) - {\mu }_{k}{x}_{k} \in \; {F}_{k - 1} \) . Donc : \( \left( {{\lambda }_{k}^{2} + {\mu }_{k}^{2}}\right) {x}_{k} = {\lambda }_{k}\left\lbrack {{\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right) }\right\rbrack - {\mu }_{k}\left\lbrack {{\lambda }_{k}f\left( {x}_{k}\right) - {\mu }_{k}{x}_{k}}\right\rbrack \in {F}_{k - 1} \) . Or \( {x}_{k} \notin {F}_{k - 1} \) , donc \( {\lambda }_{k}^{2} + {\mu }_{k}^{2} = 0 \) , d’où \( {\lambda }_{k} = {\mu }_{k} = 0 \) . On a donc \( {\lambda }_{1}{x}_{1} + {\mu }_{1}f\left( {x}_{1}\right) + \cdots + {\lambda }_{k - 1}{x}_{k - 1} + {\mu }_{k - 1}f\left( {x}_{k - 1}\right) = 0 \) , donc d’après l’hypothèse de récurrence, \( \forall i,{\lambda }_{i} = {\mu }_{i} = 0 \) .

> Then \( {\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right) \in {F}_{k - 1} \) and \( {F}_{k - 1} \) being stable by \( f, f\left\lbrack {{\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right) }\right\rbrack = {\lambda }_{k}f\left( {x}_{k}\right) - {\mu }_{k}{x}_{k} \in \; {F}_{k - 1} \) . Therefore: \( \left( {{\lambda }_{k}^{2} + {\mu }_{k}^{2}}\right) {x}_{k} = {\lambda }_{k}\left\lbrack {{\lambda }_{k}{x}_{k} + {\mu }_{k}f\left( {x}_{k}\right) }\right\rbrack - {\mu }_{k}\left\lbrack {{\lambda }_{k}f\left( {x}_{k}\right) - {\mu }_{k}{x}_{k}}\right\rbrack \in {F}_{k - 1} \) . However \( {x}_{k} \notin {F}_{k - 1} \) , so \( {\lambda }_{k}^{2} + {\mu }_{k}^{2} = 0 \) , hence \( {\lambda }_{k} = {\mu }_{k} = 0 \) . We thus have \( {\lambda }_{1}{x}_{1} + {\mu }_{1}f\left( {x}_{1}\right) + \cdots + {\lambda }_{k - 1}{x}_{k - 1} + {\mu }_{k - 1}f\left( {x}_{k - 1}\right) = 0 \) , so according to the induction hypothesis, \( \forall i,{\lambda }_{i} = {\mu }_{i} = 0 \) .

Le cas particulier \( k = p \) , entraîne l’existence de \( {x}_{1},\ldots ,{x}_{p} \in E \) tels que la famille \( B = \; \left( {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{p}, f\left( {x}_{p}\right) }\right) \) soit libre. Comme \( n = {2p}, B \) est une base de \( E \) . La matrice \( A \) est donc semblable à

> The special case \( k = p \) implies the existence of \( {x}_{1},\ldots ,{x}_{p} \in E \) such that the family \( B = \; \left( {{x}_{1}, f\left( {x}_{1}\right) ,\ldots ,{x}_{p}, f\left( {x}_{p}\right) }\right) \) is free. As \( n = {2p}, B \) is a basis of \( E \) . The matrix \( A \) is therefore similar to

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} J & & \left( 0\right) \\   &  \ddots  & \\  \left( 0\right) & & J \end{matrix}\right) ,\;\text{ où }\;J = \left( \begin{matrix} 0 &  - 1 \\  1 & 0 \end{matrix}\right) ,
\]

et réciproquement, si \( A \) est semblable à une matrice de cette forme, \( {A}^{2} = - {I}_{n} \) .

> and conversely, if \( A \) is similar to a matrix of this form, \( {A}^{2} = - {I}_{n} \) .

\( \rightarrow \) ProblèmE 2 (ENDOMORPHISMES NILPOTENTS, DÉCOMPOSITION DE FITTING). Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Soit \( f \in \mathcal{L}\left( E\right) \) , nilpotent (i. e. il existe \( p \in {\mathbb{N}}^{ * } \) tel que \( \left. {{f}^{p} = 0}\right) \) . On note \( q \in {\mathbb{N}}^{ * } \) l’indice de nilpotence de \( f \) , défini par \( q = \inf \left\{ {p \in {\mathbb{N}}^{ * } \mid {f}^{p} = 0}\right\} \) .

> \( \rightarrow \) PROBLEM 2 (NILPOTENT ENDOMORPHISMS, FITTING DECOMPOSITION). Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s. \( n \in {\mathbb{N}}^{ * } \) . Let \( f \in \mathcal{L}\left( E\right) \) be nilpotent (i.e., there exists \( p \in {\mathbb{N}}^{ * } \) such that \( \left. {{f}^{p} = 0}\right) \) . We denote by \( q \in {\mathbb{N}}^{ * } \) the index of nilpotence of \( f \) , defined by \( q = \inf \left\{ {p \in {\mathbb{N}}^{ * } \mid {f}^{p} = 0}\right\} \) .

1 / On veut montrer que \( q \leq n \) .

> 1 / We want to show that \( q \leq n \) .

a) (Première méthode). Montrer que la suite (Im \( {\left. {f}^{p}\right) }_{p \in \mathbb{N}} \) décroît strictement jusqu’à \( p = q \) puis devient stationnaire. Conclure.

> a) (First method). Show that the sequence (Im \( {\left. {f}^{p}\right) }_{p \in \mathbb{N}} \) decreases strictly until \( p = q \) then becomes stationary. Conclude.

b) (Deuxième méthode). Montrer qu’il existe \( {x}_{0} \in E \) tel que \( \left( {{x}_{0}, f\left( {x}_{0}\right) ,\ldots ,{f}^{q - 1}\left( {x}_{0}\right) }\right) \) forme une famille libre. Conclure.

> b) (Second method). Show that there exists \( {x}_{0} \in E \) such that \( \left( {{x}_{0}, f\left( {x}_{0}\right) ,\ldots ,{f}^{q - 1}\left( {x}_{0}\right) }\right) \) forms a linearly independent family. Conclude.

2/ Si \( r = \dim \left( {\operatorname{Ker}f}\right) \) , montrer que \( r \neq 0 \) et que \( n/r \leq q \leq n + 1 - r \) .

> 2/ If \( r = \dim \left( {\operatorname{Ker}f}\right) \) , show that \( r \neq 0 \) and that \( n/r \leq q \leq n + 1 - r \) .

3/ (Décomposition de Fitting.) On ne suppose plus \( f \) nilpotent. Montrer qu’il existe un unique couple \( \left( {F, G}\right) \) de sous-espaces vectoriels de \( E \) stables par \( f \) , tels que \( F \oplus G = E \) , \( {f}_{\mid F} \) est nilpotent et \( {f}_{\mid G} \) est inversible.

> 3/ (Fitting decomposition.) We no longer assume \( f \) is nilpotent. Show that there exists a unique pair \( \left( {F, G}\right) \) of vector subspaces of \( E \) stable under \( f \) , such that \( F \oplus G = E \) , \( {f}_{\mid F} \) is nilpotent and \( {f}_{\mid G} \) is invertible.

Solution. 1/a) Dans un premier temps, on ne suppose pas \( f \) nilpotente. Pour tout \( p \) , comme \( f\left( E\right) \subset E \) , on a \( {f}^{p + 1}\left( E\right) = {f}^{p}\left\lbrack {f\left( E\right) }\right\rbrack \subset {f}^{p}\left( E\right) \) . La suite \( {\left( \operatorname{Im}{f}^{p}\right) }_{p \in \mathbb{N}} \) est donc décroissante. Donc la suite d’entiers naturels \( {\left( \operatorname{rg}{f}^{p}\right) }_{p \in \mathbb{N}} \) décroit, donc il existe un plus petit entier \( s \in \mathbb{N} \) tel que \( \operatorname{rg}{f}^{s + 1} = \operatorname{rg}{f}^{s} \) . Comme Im \( {f}^{s + 1} \subset \operatorname{Im}{f}^{s} \) on en déduit Im \( {f}^{s + 1} = \operatorname{Im}{f}^{s} \) . Pour tout \( p \geq s \) , on a

> Solution. 1/a) Initially, we do not assume \( f \) is nilpotent. For any \( p \) , since \( f\left( E\right) \subset E \) , we have \( {f}^{p + 1}\left( E\right) = {f}^{p}\left\lbrack {f\left( E\right) }\right\rbrack \subset {f}^{p}\left( E\right) \) . The sequence \( {\left( \operatorname{Im}{f}^{p}\right) }_{p \in \mathbb{N}} \) is therefore decreasing. Thus the sequence of natural integers \( {\left( \operatorname{rg}{f}^{p}\right) }_{p \in \mathbb{N}} \) decreases, so there exists a smallest integer \( s \in \mathbb{N} \) such that \( \operatorname{rg}{f}^{s + 1} = \operatorname{rg}{f}^{s} \) . As Im \( {f}^{s + 1} \subset \operatorname{Im}{f}^{s} \) we deduce Im \( {f}^{s + 1} = \operatorname{Im}{f}^{s} \) . For any \( p \geq s \) , we have

\[
\operatorname{Im}{f}^{p + 1} = {f}^{p - s}\left\lbrack  {{f}^{s + 1}\left( E\right) }\right\rbrack   = {f}^{p - s}\left\lbrack  {{f}^{s}\left( E\right) }\right\rbrack   = \operatorname{Im}{f}^{p}.
\]

La suite (Im \( {f}^{p}{)}_{p \in \mathbb{N}} \) est donc stationnaire à partir du rang \( s \) . Comme la suite \( {\left( \operatorname{rg}{f}^{p}\right) }_{p \in \mathbb{N}} \) décroît et par définition de \( s \) , on a rg \( {f}^{p + 1} \leq \operatorname{rg}{f}^{p} - 1 \) lorsque \( p < s \) . Une récurrence immédiate fournit \( \operatorname{rg}{f}^{p} \leq \operatorname{rg}{f}^{0} - p = n - p \) pour \( 0 \leq p \leq s \) , en particulier \( \operatorname{rg}{f}^{s} \leq \operatorname{rg}{f}^{0} - s = n - s \) . On en déduit \( s \leq n \) .

> The sequence (Im \( {f}^{p}{)}_{p \in \mathbb{N}} \) is therefore stationary from rank \( s \) . As the sequence \( {\left( \operatorname{rg}{f}^{p}\right) }_{p \in \mathbb{N}} \) decreases and by definition of \( s \) , we have rank \( {f}^{p + 1} \leq \operatorname{rg}{f}^{p} - 1 \) when \( p < s \) . An immediate induction provides \( \operatorname{rg}{f}^{p} \leq \operatorname{rg}{f}^{0} - p = n - p \) for \( 0 \leq p \leq s \) , in particular \( \operatorname{rg}{f}^{s} \leq \operatorname{rg}{f}^{0} - s = n - s \) . We deduce \( s \leq n \) .

Pour conclure, on utilise l’hypothèse de nilpotence de \( f \) , pour noter que Im \( {f}^{p} \) est stationnaire à partir de \( p = q \) . On en déduit \( q = s \) , donc \( q \leq n \) .

> To conclude, we use the nilpotency hypothesis of \( f \) , to note that Im \( {f}^{p} \) is stationary from \( p = q \) . We deduce \( q = s \) , therefore \( q \leq n \) .

b) Comme \( {f}^{q - 1} \neq 0 \) , il existe \( {x}_{0} \in E \) tel que \( {f}^{q - 1}\left( {x}_{0}\right) \neq 0 \) . Nous allons montrer que la famille \( \left( {{x}_{0}, f\left( {x}_{0}\right) ,\ldots ,{f}^{q - 1}\left( {x}_{0}\right) }\right) \) est libre. Si \( \mathop{\sum }\limits_{{i = 0}}^{{q - 1}}{\lambda }_{i}{f}^{i}\left( {x}_{0}\right) = 0 \) avec les \( {\lambda }_{i} \) non tous nuls, on considère le plus petit entier \( k \) tel que \( {\lambda }_{k} \neq 0 \) . On a \( \mathop{\sum }\limits_{{i = k}}^{{q - 1}}{\lambda }_{i}{f}^{i}\left( {x}_{0}\right) = 0 \) , donc en composant par \( {f}^{q - 1 - k} \) à gauche,

> b) As \( {f}^{q - 1} \neq 0 \) , there exists \( {x}_{0} \in E \) such that \( {f}^{q - 1}\left( {x}_{0}\right) \neq 0 \) . We will show that the family \( \left( {{x}_{0}, f\left( {x}_{0}\right) ,\ldots ,{f}^{q - 1}\left( {x}_{0}\right) }\right) \) is linearly independent. If \( \mathop{\sum }\limits_{{i = 0}}^{{q - 1}}{\lambda }_{i}{f}^{i}\left( {x}_{0}\right) = 0 \) with the \( {\lambda }_{i} \) not all zero, we consider the smallest integer \( k \) such that \( {\lambda }_{k} \neq 0 \) . We have \( \mathop{\sum }\limits_{{i = k}}^{{q - 1}}{\lambda }_{i}{f}^{i}\left( {x}_{0}\right) = 0 \) , so by composing with \( {f}^{q - 1 - k} \) on the left,

\[
{\lambda }_{k}{f}^{q - 1}\left( {x}_{0}\right)  + {\lambda }_{k + 1}{f}^{q}\left( {x}_{0}\right)  + \cdots  + {\lambda }_{q - 1}{f}^{2\left( {q - 1}\right)  - k}\left( {x}_{0}\right)  = 0.
\]

Comme \( {f}^{p} = 0 \) pour \( p \geq q \) , cette dernière égalité entraîne \( {\lambda }_{k}{f}^{q - 1}\left( {x}_{0}\right) = 0 \) , et comme \( {f}^{q - 1}\left( {x}_{0}\right) \neq \; 0,{\lambda }_{k} = 0 \) , ce qui est absurde. La famille considérée est donc libre. Elle a \( q \) éléments, donc \( q \leq \dim E = n. \)

> As \( {f}^{p} = 0 \) for \( p \geq q \) , this last equality implies \( {\lambda }_{k}{f}^{q - 1}\left( {x}_{0}\right) = 0 \) , and since \( {f}^{q - 1}\left( {x}_{0}\right) \neq \; 0,{\lambda }_{k} = 0 \) , which is absurd. The considered family is therefore linearly independent. It has \( q \) elements, so \( q \leq \dim E = n. \)

2 / On a vu au 1/a) que si \( p < q,\operatorname{rg}{f}^{p + 1} \leq \operatorname{rg}{f}^{p} - 1 \) , ce qui entraîne que \( 0 = \operatorname{rg}{f}^{q} \leq \operatorname{rg}f - \left( {q - 1}\right) = \; n - r - \left( {q - 1}\right) \) , donc \( q \leq n - r + 1 \) .

> 2 / We saw in 1/a) that if \( p < q,\operatorname{rg}{f}^{p + 1} \leq \operatorname{rg}{f}^{p} - 1 \) , which implies that \( 0 = \operatorname{rg}{f}^{q} \leq \operatorname{rg}f - \left( {q - 1}\right) = \; n - r - \left( {q - 1}\right) \) , therefore \( q \leq n - r + 1 \) .

Il reste à montrer l’inégalité \( n/r \leq q \) . Pour cela, commençons par montrer que

> It remains to show the inequality \( n/r \leq q \) . To do this, let us begin by showing that

\[
\forall p \in  \mathbb{N},\;\operatorname{rg}{f}^{p + 1} = \operatorname{rg}{f}^{p} - \dim \left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right) .
\]

(*)

> - Soit \( S \) un s.e.v de \( E \) tel que \( \left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right)  \oplus  S = \operatorname{Im}{f}^{p} \) . On a \( S \cap  \operatorname{Ker}f \subset  \left( {\operatorname{Im}{f}^{p} \cap  }\right. \) Ker \( f) \cap  S = \{ 0\} \) , donc \( S \cap  \operatorname{Ker}f = \{ 0\} \) . Ceci entraîne que \( {f}_{\mid S} \) (restriction de \( f \) à \( S \) ) est injective, et donc \( \dim f\left( S\right)  = \dim S \) . Or \( \operatorname{Im}{f}^{p + 1} = f\left( {\operatorname{Im}{f}^{p}}\right)  = f\left\lbrack  {\left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right)  \oplus  S}\right\rbrack   = f\left( S\right) \) , donc \( \operatorname{rg}{f}^{p + 1} = \dim f\left( S\right)  = \dim S = \operatorname{rg}{f}^{p} - \dim \left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right) . \)

- Let \( S \) be a subspace of \( E \) such that \( \left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right)  \oplus  S = \operatorname{Im}{f}^{p} \) . We have \( S \cap  \operatorname{Ker}f \subset  \left( {\operatorname{Im}{f}^{p} \cap  }\right. \) Ker \( f) \cap  S = \{ 0\} \) , therefore \( S \cap  \operatorname{Ker}f = \{ 0\} \) . This implies that \( {f}_{\mid S} \) (restriction of \( f \) to \( S \) ) is injective, and therefore \( \dim f\left( S\right)  = \dim S \) . However \( \operatorname{Im}{f}^{p + 1} = f\left( {\operatorname{Im}{f}^{p}}\right)  = f\left\lbrack  {\left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right)  \oplus  S}\right\rbrack   = f\left( S\right) \) , therefore \( \operatorname{rg}{f}^{p + 1} = \dim f\left( S\right)  = \dim S = \operatorname{rg}{f}^{p} - \dim \left( {\operatorname{Im}{f}^{p} \cap  \operatorname{Ker}f}\right) . \)

> L’égalité (*) entraîne que pour tout \( p,\operatorname{rg}{f}^{p + 1} \geq \operatorname{rg}{f}^{p} - r \) . Ceci entraîne \( 0 = \operatorname{rg}{f}^{q} \geq \; \operatorname{rg}{f}^{0} - {qr} = n - {qr} \) , donc \( q \geq n/r \) .

The equality (*) implies that for all \( p,\operatorname{rg}{f}^{p + 1} \geq \operatorname{rg}{f}^{p} - r \) . This implies \( 0 = \operatorname{rg}{f}^{q} \geq \; \operatorname{rg}{f}^{0} - {qr} = n - {qr} \) , therefore \( q \geq n/r \) .

> 3/ Rappelons que nous avons montré en \( 1/ \) a) que \( {\left( \operatorname{Im}{f}^{p}\right) }_{p \in \mathbb{N}} \) décroit strictement puis devient stationnaire à partir d’un certain rang \( s \) ( \( f \) n’était pas supposé nilpotent dans cette preuve).

3/ Let us recall that we showed in \( 1/ \) a) that \( {\left( \operatorname{Im}{f}^{p}\right) }_{p \in \mathbb{N}} \) strictly decreases and then becomes stationary from a certain rank \( s \) ( \( f \) was not assumed to be nilpotent in this proof).

> Supposons que \( F \) et \( G \) existent. Soit \( q \) l’indice de nilpotence de \( {f}_{\mid F} \) , de sorte que \( {f}^{q}\left( F\right) = 0 \) . Pour tout \( p \geq q \) on a \( {f}^{p}\left( F\right) = {f}^{p - q}\left( {{f}^{q}\left( F\right) }\right) = 0 \) , et \( {f}^{p}\left( G\right) = G \) car \( {f}_{\mid G} \) est inversible. Comme \( F \oplus G = E \) , on en déduit que pour tout \( p \geq q \) , \( \operatorname{Im}{f}^{p} = {f}^{p}\left( F\right) + {f}^{p}\left( G\right) = G \) . Ainsi \( G \) est forcément la valeur stationnaire de la suite \( {\left( \operatorname{Im}{f}^{p}\right) }_{p \in \mathbb{N}} \) , donc \( G = \operatorname{Im}{f}^{s} \) et \( q \geq s \) . Par ailleurs \( {f}^{q}\left( F\right) = 0 \) donc \( F \subset \operatorname{Ker}{f}^{q} \) . Or \( n = \dim \operatorname{Ker}{f}^{q} + \dim \operatorname{Im}{f}^{q} = \dim \operatorname{Ker}{f}^{q} + \dim G \) , et comme \( n = \dim F + \dim G \) on en déduit \( \dim F = \dim \operatorname{Ker}{f}^{q} \) , donc \( F = \operatorname{Ker}{f}^{q} \) . Par définition de \( s \) on a \( \operatorname{rg}{f}^{s} = \operatorname{rg}{f}^{q} \) , donc dim \( \operatorname{Ker}{f}^{q} = n - \operatorname{rg}{f}^{q} = n - \operatorname{rg}{f}^{s} = \dim \operatorname{Ker}{f}^{s} \) et comme Ker \( {f}^{s} \subset \operatorname{Ker}{f}^{q} \) (car si \( {f}^{s}\left( x\right) = 0 \) , on a \( {f}^{q}\left( x\right) = {f}^{q - s}\left( {{f}^{s}\left( x\right) }\right) = 0 \) ) on en déduit \( F = \operatorname{Ker}{f}^{q} = \operatorname{Ker}{f}^{s} \) . Ainsi si \( F \) et \( G \) existent, ils vérifient forcément \( F = \operatorname{Ker}{f}^{s} \) et \( G = \operatorname{Im}{f}^{s} \) , ce qui assure leur unicité.

Suppose that \( F \) and \( G \) exist. Let \( q \) be the index of nilpotence of \( {f}_{\mid F} \) , so that \( {f}^{q}\left( F\right) = 0 \) . For all \( p \geq q \) we have \( {f}^{p}\left( F\right) = {f}^{p - q}\left( {{f}^{q}\left( F\right) }\right) = 0 \) , and \( {f}^{p}\left( G\right) = G \) because \( {f}_{\mid G} \) is invertible. As \( F \oplus G = E \) , we deduce that for all \( p \geq q \) , \( \operatorname{Im}{f}^{p} = {f}^{p}\left( F\right) + {f}^{p}\left( G\right) = G \) . Thus \( G \) is necessarily the stationary value of the sequence \( {\left( \operatorname{Im}{f}^{p}\right) }_{p \in \mathbb{N}} \) , therefore \( G = \operatorname{Im}{f}^{s} \) and \( q \geq s \) . Furthermore \( {f}^{q}\left( F\right) = 0 \) so \( F \subset \operatorname{Ker}{f}^{q} \) . However \( n = \dim \operatorname{Ker}{f}^{q} + \dim \operatorname{Im}{f}^{q} = \dim \operatorname{Ker}{f}^{q} + \dim G \) , and as \( n = \dim F + \dim G \) we deduce \( \dim F = \dim \operatorname{Ker}{f}^{q} \) , therefore \( F = \operatorname{Ker}{f}^{q} \) . By definition of \( s \) we have \( \operatorname{rg}{f}^{s} = \operatorname{rg}{f}^{q} \) , therefore dim \( \operatorname{Ker}{f}^{q} = n - \operatorname{rg}{f}^{q} = n - \operatorname{rg}{f}^{s} = \dim \operatorname{Ker}{f}^{s} \) and as Ker \( {f}^{s} \subset \operatorname{Ker}{f}^{q} \) (because if \( {f}^{s}\left( x\right) = 0 \) , we have \( {f}^{q}\left( x\right) = {f}^{q - s}\left( {{f}^{s}\left( x\right) }\right) = 0 \) ) we deduce \( F = \operatorname{Ker}{f}^{q} = \operatorname{Ker}{f}^{s} \) . Thus if \( F \) and \( G \) exist, they necessarily satisfy \( F = \operatorname{Ker}{f}^{s} \) and \( G = \operatorname{Im}{f}^{s} \) , which ensures their uniqueness.

> Réciproquement, définissons \( F \) et \( G \) par \( F = \operatorname{Ker}{f}^{s} \) et \( G = \operatorname{Im}{f}^{s} \) . Il est immédiat que \( F \) et \( G \) sont stables par \( f \) .

Conversely, let us define \( F \) and \( G \) by \( F = \operatorname{Ker}{f}^{s} \) and \( G = \operatorname{Im}{f}^{s} \). It is immediate that \( F \) and \( G \) are stable under \( f \).

> - On a \( F \cap  G = \{ 0\} \) car si \( x \in  F \cap  G \) , on a \( {f}^{s}\left( x\right)  = 0 \) et \( x = {f}^{s}\left( y\right) \) avec \( y \in  E \) , donc \( {f}^{2s}\left( y\right)  = 0 \) . Or \( \operatorname{Ker}{f}^{s} \subset  \operatorname{Ker}{f}^{2s} \) et \( \dim \operatorname{Ker}{f}^{s} = n - \operatorname{rg}{f}^{s} = n - \operatorname{rg}{f}^{2s} = \dim \operatorname{Ker}{f}^{2s} \) , donc Ker \( {f}^{2s} = \operatorname{Ker}{f}^{s} \) . Donc \( y \in  \operatorname{Ker}{f}^{s} \) , donc \( x = {f}^{s}\left( y\right)  = 0 \) . Comme dim \( F + \dim G = n \) , on en déduit \( F \oplus  G = E \) .

- We have \( F \cap  G = \{ 0\} \) because if \( x \in  F \cap  G \), we have \( {f}^{s}\left( x\right)  = 0 \) and \( x = {f}^{s}\left( y\right) \) with \( y \in  E \), thus \( {f}^{2s}\left( y\right)  = 0 \). However, \( \operatorname{Ker}{f}^{s} \subset  \operatorname{Ker}{f}^{2s} \) and \( \dim \operatorname{Ker}{f}^{s} = n - \operatorname{rg}{f}^{s} = n - \operatorname{rg}{f}^{2s} = \dim \operatorname{Ker}{f}^{2s} \), so Ker \( {f}^{2s} = \operatorname{Ker}{f}^{s} \). Thus \( y \in  \operatorname{Ker}{f}^{s} \), therefore \( x = {f}^{s}\left( y\right)  = 0 \). As dim \( F + \dim G = n \), we deduce \( F \oplus  G = E \).

> - Par définition de \( F = \operatorname{Ker}{f}^{s} \) , on a \( {f}^{s}\left( F\right)  = 0 \) donc \( {f}_{\mid F} \) est nilpotent.

- By definition of \( F = \operatorname{Ker}{f}^{s} \), we have \( {f}^{s}\left( F\right)  = 0 \), so \( {f}_{\mid F} \) is nilpotent.

> - Par ailleurs on a \( \operatorname{Im}{f}^{s + 1} = \operatorname{Im}{f}^{s} \) , ce qui s’écrit \( f\left( G\right)  = G \) donc \( {f}_{\mid G} \) est surjective et comme c’est un endomorphisme en dimension finie, on en déduit que \( {f}_{\mid G} \) est inversible.

- Furthermore, we have \( \operatorname{Im}{f}^{s + 1} = \operatorname{Im}{f}^{s} \), which is written as \( f\left( G\right)  = G \), so \( {f}_{\mid G} \) is surjective, and as it is an endomorphism in finite dimension, we deduce that \( {f}_{\mid G} \) is invertible.

> Remarque. En particulier,2/ montre que si \( f \) est nilpotent et si dimKer \( f = 1 \) , alors l’indice de nilpotence de \( f \) est \( q = n \) .

Remark. In particular, 2/ shows that if \( f \) is nilpotent and if dimKer \( f = 1 \), then the index of nilpotence of \( f \) is \( q = n \).

> - Nous avons montré que dans tous les cas,(Im \( {\left. {f}^{p}\right) }_{p \in  \mathbb{N}} \) décroit strictement puis devient stationnaire à partir d'un certain rang s. L'entier \( s \) s’appelle l’indice de \( f \) . On montre facilement que la suite (Ker \( {\left. {f}^{p}\right) }_{p \in  \mathbb{N}} \) croît strictement puis devient stationnaire à partir de ce même rang \( s \) . On retrouve ce résultat dans la définition 2 page 202

- We have shown that in all cases, (Im \( {\left. {f}^{p}\right) }_{p \in  \mathbb{N}} \) strictly decreases then becomes stationary from a certain rank s. The integer \( s \) is called the index of \( f \). It is easily shown that the sequence (Ker \( {\left. {f}^{p}\right) }_{p \in  \mathbb{N}} \) strictly increases then becomes stationary from this same rank \( s \). We find this result in definition 2 on page 202.

> Problem 3. 1/a) Soit \( N \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice nilpotente (i.e. il existe \( p \in {\mathbb{N}}^{ * } \) tel que \( {N}^{p} = 0 \) ) d’indice \( q \) (i. e. \( q \) est le plus petit entier naturel vérifiant \( {N}^{q} = 0 \) ). Montrer que \( {I}_{n} - N \) est inversible et donner son inverse.

Problem 3. 1/a) Let \( N \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a nilpotent matrix (i.e., there exists \( p \in {\mathbb{N}}^{ * } \) such that \( {N}^{p} = 0 \)) of index \( q \) (i.e., \( q \) is the smallest natural integer satisfying \( {N}^{q} = 0 \)). Show that \( {I}_{n} - N \) is invertible and provide its inverse.

> b) (Application). Montrer l'inversibilité et calculer l'inverse de la matrice

b) (Application). Show the invertibility and calculate the inverse of the matrix

\[
M = \left( \begin{array}{rrrr} 1 &  - a & 0 &  \ddots  \\  0 & 1 &  \ddots  & 0 \\  \vdots & &  \ddots  &  - a \\  0 & \cdots & 0 & 1 \end{array}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) .
\]

2/a) Soit \( N \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) une matrice nilpotente d’indice 2. Pour tout \( p \in {\mathbb{N}}^{ * } \) , calculer \( {\left( {I}_{n} + N\right) }^{p} \) .

> 2/a) Let \( N \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be a nilpotent matrix of index 2. For any \( p \in {\mathbb{N}}^{ * } \), calculate \( {\left( {I}_{n} + N\right) }^{p} \).

b) (Application). Soit \( M = \left( \begin{array}{rr} 1 & 1 \\ - 1 & 3 \end{array}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) . Calculer \( {M}^{100} \) .

> b) (Application). Let \( M = \left( \begin{array}{rr} 1 & 1 \\ - 1 & 3 \end{array}\right) \in {\mathcal{M}}_{2}\left( \mathbb{R}\right) \) . Calculate \( {M}^{100} \) .

Solution. 1/a) Il suffit de remarquer que \( \left( {{I}_{n} - N}\right) \left( {{I}_{n} + N + \cdots + {N}^{q - 1}}\right) = {I}_{n} - {N}^{q} = {I}_{n} \) , donc \( {I}_{n} - N \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) et \( {\left( {I}_{n} - N\right) }^{-1} = {I}_{n} + N + \cdots + {N}^{q - 1}. \)

> Solution. 1/a) It suffices to note that \( \left( {{I}_{n} - N}\right) \left( {{I}_{n} + N + \cdots + {N}^{q - 1}}\right) = {I}_{n} - {N}^{q} = {I}_{n} \) , therefore \( {I}_{n} - N \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) \) and \( {\left( {I}_{n} - N\right) }^{-1} = {I}_{n} + N + \cdots + {N}^{q - 1}. \)

b) On peut écrire \( M = {I}_{n} - {aN} \) avec \( N = \left( \begin{matrix} 0 & {I}_{n - 1} \\ 0 & 0 \end{matrix}\right) \) . Une récurrence facile donne

> b) We can write \( M = {I}_{n} - {aN} \) with \( N = \left( \begin{matrix} 0 & {I}_{n - 1} \\ 0 & 0 \end{matrix}\right) \) . An easy induction gives

\[
\forall p \in  {\mathbb{N}}^{ * },1 \leq  p \leq  n - 1,\;{N}^{p} = \left( \begin{matrix} 0 & {I}_{n - p} \\  0 & 0 \end{matrix}\right) \;\text{ et }{N}^{n} = 0.
\]

En appliquant \( 1/\mathrm{a} \) ), on voit donc que \( M = {I}_{n} - {aN} \) est inversible et que

> By applying \( 1/\mathrm{a} \) ), we see that \( M = {I}_{n} - {aN} \) is invertible and that

\[
{M}^{-1} = {I}_{n} + {aN} + {a}^{2}{N}^{2} + \cdots  + {a}^{n - 1}{N}^{n - 1} = \left( \begin{matrix} 1 & a & {a}^{2} & \cdots & {a}^{n - 1} \\  0 & 1 & a &  \ddots  & \vdots \\  \vdots &  \ddots  &  \ddots  &  \ddots  & {a}^{2} \\  \vdots & &  \ddots  &  \ddots  & a \\  0 & \cdots & \cdots & 0 & 1 \end{matrix}\right) .
\]

\( \mathbf{2}/\mathbf{a} \) ) Les matrices \( {I}_{n} \) et \( N \) commutant, on peut écrire

> \( \mathbf{2}/\mathbf{a} \) ) Since the matrices \( {I}_{n} \) and \( N \) commute, we can write

\[
{\left( {I}_{n} + N\right) }^{p} = \mathop{\sum }\limits_{{k = 0}}^{p}\left( \begin{array}{l} p \\  k \end{array}\right) {N}^{k}{I}_{n}^{p - k} = \mathop{\sum }\limits_{{k = 0}}^{p}\left( \begin{array}{l} p \\  k \end{array}\right) {N}^{k} = \left( \begin{array}{l} p \\  0 \end{array}\right) {I}_{n} + \left( \begin{array}{l} p \\  1 \end{array}\right) N = {I}_{n} + {pN}.
\]

b) Si \( N = \left( \begin{matrix} - 1 & 1 \\ - 1 & 1 \end{matrix}\right) \) , on a \( M = 2{I}_{2} + N \) et \( {N}^{2} = 0 \) , donc d’après la question précédente,

> b) If \( N = \left( \begin{matrix} - 1 & 1 \\ - 1 & 1 \end{matrix}\right) \) , we have \( M = 2{I}_{2} + N \) and \( {N}^{2} = 0 \) , therefore according to the previous question,

\[
{M}^{100} = {2}^{100}{\left( {I}_{2} + \frac{1}{2}N\right) }^{100} = {2}^{100}\left( {{I}_{2} + {50N}}\right)  = {2}^{100}\left( \begin{matrix}  - {49} & {50} \\   - {50} & {51} \end{matrix}\right) .
\]

Remarque. Au 1/a), on a forcément \( q \leq n \) . On peut montrer ce résultat sans faire appel au théorème de Cayley-Hamilton, en procédant comme suit. Soit \( f \) l’endomorphisme de \( {\mathbb{R}}^{n} \) dont \( N \) est la matrice dans la base canonique \( B \) de \( {\mathbb{R}}^{n} \) . Pour tout entier \( r \) , l’égalité \( {\left\lbrack {f}^{r}\right\rbrack }_{B} = {N}^{r} \) entraîne que les ordres de nilpotence de \( f \) et de \( N \) sont égaux. Or d’après le problème précédent, l’ordre \( r \) de nilpotence de \( f \) est \( \leq n \) , et donc \( q \leq n \) .

> Remark. In 1/a), we necessarily have \( q \leq n \) . This result can be shown without invoking the Cayley-Hamilton theorem, by proceeding as follows. Let \( f \) be the endomorphism of \( {\mathbb{R}}^{n} \) whose matrix in the canonical basis \( B \) of \( {\mathbb{R}}^{n} \) is \( N \) . For any integer \( r \) , the equality \( {\left\lbrack {f}^{r}\right\rbrack }_{B} = {N}^{r} \) implies that the nilpotency orders of \( f \) and \( N \) are equal. However, according to the previous problem, the nilpotency order \( r \) of \( f \) is \( \leq n \) , and therefore \( q \leq n \) .

- On identifie souvent une matrice \( M \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) et l’endomorphisme \( f \) de \( {\mathbb{K}}^{n} \) dont \( M \) est la matrice dans la base canonique de \( {\mathbb{K}}^{n} \) . Si les vecteurs de \( {\mathbb{K}}^{n} \) sont notés en matrices colonnes, on a \( f\left( X\right)  = {MX} \) .

> - We often identify a matrix \( M \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) and the endomorphism \( f \) of \( {\mathbb{K}}^{n} \) whose matrix in the canonical basis of \( {\mathbb{K}}^{n} \) is \( M \) . If the vectors of \( {\mathbb{K}}^{n} \) are denoted as column matrices, we have \( f\left( X\right)  = {MX} \) .

Problem 4. Soit \( E \) un ensemble et \( {f}_{1},{f}_{2},\ldots ,{f}_{n}n \) fonctions de \( E \) dans \( \mathbb{K} \) , formant un système libre dans le \( \mathbb{K} \) -espace vectoriel des fonctions de \( E \) dans \( \mathbb{K} \) . Démontrer qu’il existe \( n \) points \( {x}_{1},\ldots ,{x}_{n} \) de \( E \) tels que la matrice \( {\left( {f}_{i}\left( {x}_{j}\right) \right) }_{1 \leq i, j \leq n} \) soit inversible :

> Problem 4. Let \( E \) be a set and \( {f}_{1},{f}_{2},\ldots ,{f}_{n}n \) functions from \( E \) to \( \mathbb{K} \) , forming a free system in the \( \mathbb{K} \) -vector space of functions from \( E \) to \( \mathbb{K} \) . Prove that there exist \( n \) points \( {x}_{1},\ldots ,{x}_{n} \) of \( E \) such that the matrix \( {\left( {f}_{i}\left( {x}_{j}\right) \right) }_{1 \leq i, j \leq n} \) is invertible :

a) En procédant par récurrence sur \( n \in {\mathbb{N}}^{ * } \) .

> a) By proceeding by induction on \( n \in {\mathbb{N}}^{ * } \) .

b) En considérant \( F = \operatorname{Vect}\left( {{f}_{1},\ldots ,{f}_{n}}\right) \) et si \( x \in E \) en notant \( \widetilde{x} : F \rightarrow \mathbb{K}\;f \mapsto f\left( x\right) \) , en montrant que \( \exists {x}_{1},\ldots ,{x}_{n} \in E \) tels que \( {\widetilde{x}}_{1},\ldots ,{\widetilde{x}}_{n} \) forment une base de \( {F}^{ * } \) , dual de \( F \) .

> b) By considering \( F = \operatorname{Vect}\left( {{f}_{1},\ldots ,{f}_{n}}\right) \) and if \( x \in E \) by denoting \( \widetilde{x} : F \rightarrow \mathbb{K}\;f \mapsto f\left( x\right) \) , by showing that \( \exists {x}_{1},\ldots ,{x}_{n} \in E \) such that \( {\widetilde{x}}_{1},\ldots ,{\widetilde{x}}_{n} \) form a basis of \( {F}^{ * } \) , dual of \( F \) .

Solution. a) Pour \( n = 1 \) , c’est évident. Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . On définit la fonction

> Solution. a) For \( n = 1 \) , it is obvious. Assume the result is true at rank \( n - 1 \) and show it at rank \( n \) . We define the function

\[
\Delta  : E \rightarrow  \mathbb{K}\;x \mapsto  \left| \begin{matrix} {f}_{1}\left( {x}_{1}\right) & \cdots & {f}_{1}\left( {x}_{n - 1}\right) & {f}_{1}\left( x\right) \\  {f}_{2}\left( {x}_{1}\right) & \cdots & {f}_{2}\left( {x}_{n - 1}\right) & {f}_{2}\left( x\right) \\  \vdots & & \vdots & \vdots \\  {f}_{n}\left( {x}_{1}\right) & \cdots & {f}_{n}\left( {x}_{n - 1}\right) & {f}_{n}\left( x\right)  \end{matrix}\right| ,
\]

\( {x}_{1},\ldots ,{x}_{n - 1} \) étant pris tels que \( \det {\left( {f}_{i}\left( {x}_{j}\right) \right) }_{1 \leq i, j \leq n - 1} \neq 0 \) . En notant, pour tout \( i,{\Delta }_{i} \) le mineur de l’élément \( {f}_{i}\left( x\right) \) de \( \Delta \) , on a, en développant \( \Delta \left( x\right) \) par rapport à la dernière colonne :

> \( {x}_{1},\ldots ,{x}_{n - 1} \) being taken such that \( \det {\left( {f}_{i}\left( {x}_{j}\right) \right) }_{1 \leq i, j \leq n - 1} \neq 0 \) . By denoting, for all \( i,{\Delta }_{i} \) the minor of the element \( {f}_{i}\left( x\right) \) of \( \Delta \) , we have, by expanding \( \Delta \left( x\right) \) with respect to the last column :

\[
\forall x \in  E,\;\Delta \left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\left( -1\right) }^{n + i}{\Delta }_{i} \cdot  {f}_{i}\left( x\right) .
\]

Or \( {\Delta }_{n} \neq 0 \) , et comme les \( \left( {f}_{i}\right) \) forment une famille libre, on ne peut avoir \( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( -1\right) }^{n + i}{\Delta }_{i}{f}_{i}\left( x\right) = 0 \) pour tout \( x \) , donc \( \exists {x}_{n} \in E,\Delta \left( {x}_{n}\right) \neq 0 \) , de sorte que \( {\left( {f}_{i}\left( {x}_{j}\right) \right) }_{1 \leq i, j \leq n} \) est inversible.

> However \( {\Delta }_{n} \neq 0 \) , and since the \( \left( {f}_{i}\right) \) form a linearly independent family, we cannot have \( \mathop{\sum }\limits_{{i = 1}}^{n}{\left( -1\right) }^{n + i}{\Delta }_{i}{f}_{i}\left( x\right) = 0 \) for all \( x \) , therefore \( \exists {x}_{n} \in E,\Delta \left( {x}_{n}\right) \neq 0 \) , so that \( {\left( {f}_{i}\left( {x}_{j}\right) \right) }_{1 \leq i, j \leq n} \) is invertible.

b) Pour tout \( x \in E \) , l’application \( \widetilde{x} : F \rightarrow \mathbb{K}\;f \mapsto f\left( x\right) \) est un élément de \( {F}^{ * } \) . Soit \( \Gamma = \; \{ \widetilde{x} \mid x \in E\} \) . L’orthogonal de \( \Gamma \) dans \( F \) est :

> b) For all \( x \in E \) , the map \( \widetilde{x} : F \rightarrow \mathbb{K}\;f \mapsto f\left( x\right) \) is an element of \( {F}^{ * } \) . Let \( \Gamma = \; \{ \widetilde{x} \mid x \in E\} \) . The orthogonal of \( \Gamma \) in \( F \) is :

\[
{\Gamma }^{ \circ  } = \{ f \in  F \mid  \forall x \in  E,\widetilde{x}\left( f\right)  = 0\}  = \{ f \in  F \mid  \forall x \in  E, f\left( x\right)  = 0\}  = \{ 0\} .
\]

Soit \( G = \operatorname{Vect}\left( \Gamma \right) \) . On a \( {G}^{ \circ } = {\Gamma }^{ \circ } = \{ 0\} \) donc dim \( G = \dim F - \dim {G}^{ \circ } = \dim F = n \) , et comme \( G \subset {F}^{ * } \) on en déduit \( G = {F}^{ * } = \operatorname{Vect}\left( \Gamma \right) \) . Donc il existe \( {x}_{1},\ldots ,{x}_{n} \in E \) tels que \( \left( {\widetilde{{x}_{1}},\ldots ,\widetilde{{x}_{n}}}\right) \) soit une base de \( {F}^{ * } \) . Les vecteurs \( \left( \begin{matrix} \widetilde{{x}_{j}}\left( {f}_{1}\right) \\ \vdots \\ \widetilde{{x}_{j}}\left( {f}_{n}\right) \end{matrix}\right) \) pour \( 1 \leq j \leq n \) sont donc linéairement indépendants, ce qui revient à dire que la matrice \( A = {\left\lbrack \widetilde{{x}_{j}}\left( {f}_{i}\right) \right\rbrack }_{1 \leq i, j \leq n} = {\left\lbrack {f}_{i}\left( {x}_{j}\right) \right\rbrack }_{1 \leq i, j \leq n} \) est inversible.

> Let \( G = \operatorname{Vect}\left( \Gamma \right) \). We have \( {G}^{ \circ } = {\Gamma }^{ \circ } = \{ 0\} \) so dim \( G = \dim F - \dim {G}^{ \circ } = \dim F = n \), and since \( G \subset {F}^{ * } \) we deduce \( G = {F}^{ * } = \operatorname{Vect}\left( \Gamma \right) \). Thus there exist \( {x}_{1},\ldots ,{x}_{n} \in E \) such that \( \left( {\widetilde{{x}_{1}},\ldots ,\widetilde{{x}_{n}}}\right) \) is a basis of \( {F}^{ * } \). The vectors \( \left( \begin{matrix} \widetilde{{x}_{j}}\left( {f}_{1}\right) \\ \vdots \\ \widetilde{{x}_{j}}\left( {f}_{n}\right) \end{matrix}\right) \) for \( 1 \leq j \leq n \) are therefore linearly independent, which is equivalent to saying that the matrix \( A = {\left\lbrack \widetilde{{x}_{j}}\left( {f}_{i}\right) \right\rbrack }_{1 \leq i, j \leq n} = {\left\lbrack {f}_{i}\left( {x}_{j}\right) \right\rbrack }_{1 \leq i, j \leq n} \) is invertible.

Problem 5. Soit \( n \in {\mathbb{N}}^{ * } \) et \( {\alpha }_{1} < \ldots < {\alpha }_{n} \) des entiers naturels. On considère des nombres réels \( {x}_{1},\ldots ,{x}_{n} \) deux à deux distincts et strictements positifs. Montrer que la matrice \( M = {\left( {x}_{i}^{{\alpha }_{j}}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est inversible (indication : commencer par le cas \( {\alpha }_{k} = k - 1 \) sans utiliser le déterminant de Vandermonde).

> Problem 5. Let \( n \in {\mathbb{N}}^{ * } \) and \( {\alpha }_{1} < \ldots < {\alpha }_{n} \) be natural numbers. Consider real numbers \( {x}_{1},\ldots ,{x}_{n} \) that are pairwise distinct and strictly positive. Show that the matrix \( M = {\left( {x}_{i}^{{\alpha }_{j}}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is invertible (hint: start with the case \( {\alpha }_{k} = k - 1 \) without using the Vandermonde determinant).

Solution. On traite déja le cas particulier \( {\alpha }_{j} = j - 1 \) . On prouve l’inversibilité de \( M \) (sans utiliser l’expression du déterminant de Vandermonde qui permet d’affirmer que det \( M \neq 0 \) dès que les \( {x}_{i} \) sont distincts), en remarquant que pour tout vecteur colonne \( A = {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) de \( {\mathbb{R}}^{n} \) , on a

> Solution. We first treat the special case \( {\alpha }_{j} = j - 1 \). We prove the invertibility of \( M \) (without using the expression of the Vandermonde determinant which allows us to state that det \( M \neq 0 \) as soon as the \( {x}_{i} \) are distinct), by noting that for any column vector \( A = {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) of \( {\mathbb{R}}^{n} \), we have

\[
{MA} = \left( \begin{matrix} 1 & {x}_{1} & \cdots & {x}_{1}^{n - 1} \\  \vdots & \vdots & & \vdots \\  1 & {x}_{n} & \cdots & {x}_{n}^{n - 1} \end{matrix}\right) \left( \begin{matrix} {a}_{1} \\  \vdots \\  {a}_{n} \end{matrix}\right)  = \left( \begin{matrix} P\left( {x}_{1}\right) \\  \vdots \\  P\left( {x}_{n}\right)  \end{matrix}\right) ,\;P\left( X\right)  = {a}_{1} + {a}_{2}X + \cdots  + {a}_{n}{X}^{n - 1}.
\]

Si \( {MA} = 0 \) on a donc \( P\left( {x}_{i}\right) = 0 \) pour \( 1 \leq i \leq n \) . Or les \( {x}_{i} \) sont distincts et deg \( P < n \) on a donc \( P = 0 \) , donc \( A = 0 \) . Ainsi \( M \) est bien inversible (ici l’hypothèse \( {x}_{i} > 0 \) est inutile).

> If \( {MA} = 0 \) we therefore have \( P\left( {x}_{i}\right) = 0 \) for \( 1 \leq i \leq n \). However, the \( {x}_{i} \) are distinct and deg \( P < n \) we therefore have \( P = 0 \), so \( A = 0 \). Thus \( M \) is indeed invertible (here the hypothesis \( {x}_{i} > 0 \) is unnecessary).

Traitons maintenant le cas général. On va utiliser la même approche, mais c'est moins im-médiat car le degré de \( P \) n’est pas forcément \( < n \) . De manière similaire au cas Vandermonde, pour tout vecteur colonne \( A = {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) de \( {\mathbb{R}}^{n} \) , on a

> Let us now treat the general case. We will use the same approach, but it is less immediate because the degree of \( P \) is not necessarily \( < n \). Similarly to the Vandermonde case, for any column vector \( A = {\left( {a}_{i}\right) }_{1 \leq i \leq n} \) of \( {\mathbb{R}}^{n} \), we have

\[
{MA} = \left( \begin{matrix} {x}_{1}^{{\alpha }_{1}} & \cdots & {x}_{1}^{{\alpha }_{n}} \\  \vdots & & \vdots \\  {x}_{n}^{{\alpha }_{1}} & \cdots & {x}_{n}^{{\alpha }_{n}} \end{matrix}\right) \left( \begin{matrix} {a}_{1} \\  \vdots \\  {a}_{n} \end{matrix}\right)  = \left( \begin{matrix} P\left( {x}_{1}\right) \\  \vdots \\  P\left( {x}_{n}\right)  \end{matrix}\right) ,\;P\left( X\right)  = {a}_{1}{X}^{{\alpha }_{1}} + {a}_{2}{X}^{{\alpha }_{2}} + \cdots  + {a}_{n}{X}^{{\alpha }_{n}}.\left( *\right)
\]

(*)

> Le résultat va alors découler du lemme suivant :

The result will then follow from the following lemma:

> LEMME. Soit \( n \in {\mathbb{N}}^{ * } \) et \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) ayant au plus \( n \) coefficients non nuls, qui s’annule en \( n \) nombres réels distincts strictement positifs. Alors \( P = 0 \) .

LEMMA. Let \( n \in {\mathbb{N}}^{ * } \) and \( P \in \mathbb{R}\left\lbrack X\right\rbrack \) have at most \( n \) non-zero coefficients, which vanishes at \( n \) distinct strictly positive real numbers. Then \( P = 0 \) .

> Nous prouvons ce lemme en procédant par récurrence sur \( n \) . Pour \( n = 1 \) c’est immédiat. Supposons le résultat vrai pour \( n - 1 \) et montrons le au rang \( n \) . Notons \( 0 < {x}_{1} < \ldots < {x}_{n} \) des nombres réels tels que \( P\left( {x}_{i}\right) = 0 \) pour \( 1 \leq i \leq n \) , où \( P \) est un polynôme ayant au plus \( n \) coefficients non nuls. Écrivons \( P = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{X}^{{\alpha }_{i}} \) ou \( 0 \leq {\alpha }_{1} < \ldots < {\alpha }_{n} \) . On a \( P = {X}^{{\alpha }_{1}}Q \) où \( Q = {a}_{1} + \mathop{\sum }\limits_{{i = 2}}^{n}{a}_{i}{X}^{{\alpha }_{i} - {\alpha }_{1}} \) , et \( {Q}^{\prime } = \mathop{\sum }\limits_{{i = 2}}^{n}\left( {{\alpha }_{i} - {\alpha }_{1}}\right) {a}_{i}{X}^{{\alpha }_{i} - {\alpha }_{1}} \) , donc \( {Q}^{\prime } \) a au plus \( n - 1 \) coefficients non nuls. Par ailleurs, \( Q\left( {x}_{i}\right) = 0 \) pour \( 1 \leq i \leq n \) donc d’après le théorème de Rolle, \( {Q}^{\prime } \) s’annule sur chaque intervalle ouvert \( \rbrack {x}_{i},{x}_{i + 1}\left\lbrack \right. \) pour \( 1 \leq i \leq n - 1 \) , donc s’annule en \( n - 1 \) nombres réels \( > 0 \) distincts. Les hypothèses de récurrence appliquées à \( {Q}^{\prime } \) sont vérifiées, et on en déduit \( {Q}^{\prime } = 0 \) . Donc \( P = {a}_{1}{X}_{1}^{{\alpha }_{1}} \) , et comme \( P\left( {x}_{1}\right) = 0 \) on a forcément \( {a}_{1} = 0 \) . Le lemme est donc prouvé.

We prove this lemma by proceeding by induction on \( n \) . For \( n = 1 \) it is immediate. Assume the result is true for \( n - 1 \) and show it for rank \( n \) . Let \( 0 < {x}_{1} < \ldots < {x}_{n} \) be real numbers such that \( P\left( {x}_{i}\right) = 0 \) for \( 1 \leq i \leq n \) , where \( P \) is a polynomial having at most \( n \) non-zero coefficients. Let us write \( P = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{X}^{{\alpha }_{i}} \) or \( 0 \leq {\alpha }_{1} < \ldots < {\alpha }_{n} \) . We have \( P = {X}^{{\alpha }_{1}}Q \) where \( Q = {a}_{1} + \mathop{\sum }\limits_{{i = 2}}^{n}{a}_{i}{X}^{{\alpha }_{i} - {\alpha }_{1}} \) , and \( {Q}^{\prime } = \mathop{\sum }\limits_{{i = 2}}^{n}\left( {{\alpha }_{i} - {\alpha }_{1}}\right) {a}_{i}{X}^{{\alpha }_{i} - {\alpha }_{1}} \) , so \( {Q}^{\prime } \) has at most \( n - 1 \) non-zero coefficients. Furthermore, \( Q\left( {x}_{i}\right) = 0 \) for \( 1 \leq i \leq n \) so, according to Rolle's theorem, \( {Q}^{\prime } \) vanishes on each open interval \( \rbrack {x}_{i},{x}_{i + 1}\left\lbrack \right. \) for \( 1 \leq i \leq n - 1 \) , and thus vanishes at \( n - 1 \) distinct real numbers \( > 0 \) . The induction hypotheses applied to \( {Q}^{\prime } \) are satisfied, and we deduce \( {Q}^{\prime } = 0 \) . Thus \( P = {a}_{1}{X}_{1}^{{\alpha }_{1}} \) , and since \( P\left( {x}_{1}\right) = 0 \) we necessarily have \( {a}_{1} = 0 \) . The lemma is therefore proven.

> Supposons maintenant \( {MA} = 0 \) . La formule (*) montre que \( P = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{X}^{{\alpha }_{i}} \) s’annule sur les \( n \) points distincts \( {x}_{1},\ldots ,{x}_{n} \) qui sont \( > 0 \) , on peut donc appliquer le lemme qui entraîne \( P = 0 \) , donc \( A = 0 \) . Donc \( M \) est inversible.

Assume now \( {MA} = 0 \) . The formula (*) shows that \( P = \mathop{\sum }\limits_{{i = 1}}^{n}{a}_{i}{X}^{{\alpha }_{i}} \) vanishes at the \( n \) distinct points \( {x}_{1},\ldots ,{x}_{n} \) which are \( > 0 \) , we can therefore apply the lemma which leads to \( P = 0 \) , thus \( A = 0 \) . Therefore \( M \) is invertible.

> Remarque. Sans l’hypothèse \( {x}_{i} > 0 \) pour \( 1 \leq i \leq n \) , le résultat est faux, comme le montre le contre-exemple \( n = 2,\left( {{\alpha }_{1},{\alpha }_{2}}\right) = \left( {0,2}\right) \) et \( \left( {{x}_{1},{x}_{2}}\right) = \left( {-1,1}\right) \) .

Remark. Without the hypothesis \( {x}_{i} > 0 \) for \( 1 \leq i \leq n \) , the result is false, as shown by the counterexample \( n = 2,\left( {{\alpha }_{1},{\alpha }_{2}}\right) = \left( {0,2}\right) \) and \( \left( {{x}_{1},{x}_{2}}\right) = \left( {-1,1}\right) \) .

> PROBLÉME 6 (IDENTITÉ DE JACOBI, IDENTITÉ DE SYLVESTER). 1/ (Identité de Jacobi) a) Soit \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . On note \( T = {A}^{-1} \) et on considère l’écriture par blocs

PROBLEM 6 (JACOBI IDENTITY, SYLVESTER IDENTITY). 1/ (Jacobi identity) a) Let \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . We denote \( T = {A}^{-1} \) and consider the block form

\[
A = \left( \begin{array}{ll} B & C \\  D & E \end{array}\right) \text{ et }T = \left( \begin{matrix} W & X \\  Y & Z \end{matrix}\right) \text{ avec }B, W \in  {\mathcal{M}}_{r}\left( \mathbb{K}\right) ,
\]

où \( r \) vérifie \( 1 \leq r < n \) . Montrer que \( \left( {\det A}\right) \left( {\det W}\right) = \det E \) .

> where \( r \) satisfies \( 1 \leq r < n \) . Show that \( \left( {\det A}\right) \left( {\det W}\right) = \det E \) .

b) Soient \( I \) et \( J \) deux sous-ensembles de \( \{ 1,\ldots , n\} \) de même cardinal \( r \) et \( A = \left( {a}_{i, j}\right) \in \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . On note \( {A}_{I, J} = {\left( {a}_{i, j}\right) }_{i \in I, j \in J} \) la matrice de \( {\mathcal{M}}_{r}\left( \mathbb{K}\right) \) obtenue à partir de \( A \) en ne conservant que les lignes d’indice \( i \in I \) et les colonnes d’indice \( j \in J \) . Si \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) et \( T = {A}^{-1} \) , montrer que

> b) Let \( I \) and \( J \) be two subsets of \( \{ 1,\ldots , n\} \) with the same cardinality \( r \) and \( A = \left( {a}_{i, j}\right) \in \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . We denote \( {A}_{I, J} = {\left( {a}_{i, j}\right) }_{i \in I, j \in J} \) as the matrix of \( {\mathcal{M}}_{r}\left( \mathbb{K}\right) \) obtained from \( A \) by keeping only the rows with indices \( i \in I \) and the columns with indices \( j \in J \) . If \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) and \( T = {A}^{-1} \) , show that

\[
\left( {\det A}\right) \left( {\det {T}_{J, I}}\right)  = {\left( -1\right) }^{S\left( {I, J}\right) }\left( {\det {A}_{{I}^{ * },{J}^{ * }}}\right) ,\;\text{ avec }\;S\left( {I, J}\right)  = \mathop{\sum }\limits_{{i \in  I}}i + \mathop{\sum }\limits_{{j \in  J}}j,
\]

où \( {I}^{ * } \) et \( {J}^{ * } \) sont les complémentaires de \( I \) et \( J \) dans \( \{ 1,\ldots , n\} \) .

> where \( {I}^{ * } \) and \( {J}^{ * } \) are the complements of \( I \) and \( J \) in \( \{ 1,\ldots , n\} \) .

2/ (Identité de Sylvester.) Soit \( A = \left( {a}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) et \( \widetilde{A} = \left( {A}_{i, j}\right) \) sa comatrice. Soient \( I \) et \( J \) deux sous-ensembles de \( \{ 1,\ldots , n\} \) de \( r \) éléments, avec \( 1 \leq r < n \) . Montrer

> 2/ (Sylvester identity.) Let \( A = \left( {a}_{i, j}\right) \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) and \( \widetilde{A} = \left( {A}_{i, j}\right) \) be its comatrix. Let \( I \) and \( J \) be two subsets of \( \{ 1,\ldots , n\} \) with \( r \) elements, with \( 1 \leq r < n \) . Show

\[
{\Gamma }_{I, J} = {\left( -1\right) }^{S\left( {I, J}\right) } \cdot  {\Delta }_{I, J} \cdot  {\left( \det A\right) }^{r - 1}
\]

où \( {\Gamma }_{I, J} = \det {\left( \widetilde{A}\right) }_{I, J} = \det {\left( {A}_{i, j}\right) }_{i \in I, j \in J} \) et où \( {\Delta }_{I, J} = \det {A}_{{I}^{ * },{J}^{ * }} = \det {\left( {a}_{i, j}\right) }_{i \notin I, j \notin J} \) .

> where \( {\Gamma }_{I, J} = \det {\left( \widetilde{A}\right) }_{I, J} = \det {\left( {A}_{i, j}\right) }_{i \in I, j \in J} \) and where \( {\Delta }_{I, J} = \det {A}_{{I}^{ * },{J}^{ * }} = \det {\left( {a}_{i, j}\right) }_{i \notin I, j \notin J} \) .

Solution. a) En écrivant par blocs l'égalité \( {AT} = {I}_{n} \) puis en considérant les blocs à gauche on obtient \( {BW} + {CY} = {I}_{r} \) et \( {DW} + {EY} = 0 \) . On en déduit

> Solution. a) By writing the equality \( {AT} = {I}_{n} \) in block form and then considering the blocks on the left, we obtain \( {BW} + {CY} = {I}_{r} \) and \( {DW} + {EY} = 0 \) . We deduce

\[
\left( \begin{matrix} B & C \\  D & E \end{matrix}\right) \left( \begin{matrix} W & 0 \\  Y & {I}_{n - r} \end{matrix}\right)  = \left( \begin{matrix} {BW} + {CY} & C \\  {DW} + {EY} & E \end{matrix}\right)  = \left( \begin{matrix} {I}_{r} & C \\  0 & E \end{matrix}\right)
\]

et en prenant le déterminant on a donc \( \left( {\det A}\right) \left( {\det W}\right) = \det E \) .

> and by taking the determinant, we therefore have \( \left( {\det A}\right) \left( {\det W}\right) = \det E \) .

b) L’idée est de se ramener au cas précédent (qui correspond au cas où \( I = J = \{ 1,\ldots , r\} \) ) par permutation des indices. Considérons l’endomorphisme \( f \) de \( {\mathbb{K}}^{n} \) dont \( A \) est la matrice dans la base canonique \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( {\mathbb{K}}^{n} \) . Notons \( {i}_{1} < \ldots < {i}_{r} \) les éléments de \( I \) et \( {k}_{1} < \ldots < {k}_{n - r} \) ceux de \( {I}^{ * },{j}_{1} < \ldots < {j}_{r} \) les éléments de \( J \) et \( {\ell }_{1} < \ldots < {\ell }_{n - r} \) ceux de \( {J}^{ * } \) . Considérons les bases \( {B}_{I} = \left( {{e}_{{i}_{1}},\ldots ,{e}_{{i}_{r}},{e}_{{k}_{1}},\ldots ,{e}_{{k}_{n - r}}}\right) \) et \( {B}_{J} = \left( {{e}_{{j}_{1}},\ldots ,{e}_{{j}_{r}},{e}_{{\ell }_{1}},\ldots ,{e}_{{\ell }_{n - r}}}\right) \) . La matrice de \( f \) dans les bases \( {B}_{I} \) et \( {B}_{J} \) s’écrit sous la forme par blocs \( {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}} = \left( \begin{array}{ll} B & C \\ D & E \end{array}\right) \) , où \( E = {A}_{{I}^{ * },{J}^{ * }} \) . De même on peut écrire \( {\left\lbrack {f}^{-1}\right\rbrack }_{{B}_{J}}^{{B}_{I}} = \left( \begin{matrix} W & X \\ Y & Z \end{matrix}\right) \) , avec \( W = {T}_{J, I} \) . La matrice \( {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}} \) est inversible, d’inverse \( {\left\lbrack {f}^{-1}\right\rbrack }_{{B}_{J}}^{{B}_{I}} \) . On peut donc appliquer le résultat de la question précédente, qui donne \( \left( {\det {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}}}\right) \left( {\det W}\right) = \det E \) . Si \( {P}_{I} \) (resp. \( {P}_{J} \) ) désigne la matrice de passage de la base \( B \) à la base \( {B}_{I} \) (resp. \( {B}_{J} \) ), on a \( {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}} = {P}_{J}^{-1}A{P}_{I} \) , et donc

> b) The idea is to reduce it to the previous case (which corresponds to the case where \( I = J = \{ 1,\ldots , r\} \) ) by permuting the indices. Let us consider the endomorphism \( f \) of \( {\mathbb{K}}^{n} \) whose matrix in the canonical basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( {\mathbb{K}}^{n} \) is \( A \) . Let \( {i}_{1} < \ldots < {i}_{r} \) denote the elements of \( I \) and \( {k}_{1} < \ldots < {k}_{n - r} \) those of \( {I}^{ * },{j}_{1} < \ldots < {j}_{r} \) , the elements of \( J \) and \( {\ell }_{1} < \ldots < {\ell }_{n - r} \) those of \( {J}^{ * } \) . Let us consider the bases \( {B}_{I} = \left( {{e}_{{i}_{1}},\ldots ,{e}_{{i}_{r}},{e}_{{k}_{1}},\ldots ,{e}_{{k}_{n - r}}}\right) \) and \( {B}_{J} = \left( {{e}_{{j}_{1}},\ldots ,{e}_{{j}_{r}},{e}_{{\ell }_{1}},\ldots ,{e}_{{\ell }_{n - r}}}\right) \) . The matrix of \( f \) in the bases \( {B}_{I} \) and \( {B}_{J} \) is written in block form as \( {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}} = \left( \begin{array}{ll} B & C \\ D & E \end{array}\right) \) , where \( E = {A}_{{I}^{ * },{J}^{ * }} \) . Similarly, we can write \( {\left\lbrack {f}^{-1}\right\rbrack }_{{B}_{J}}^{{B}_{I}} = \left( \begin{matrix} W & X \\ Y & Z \end{matrix}\right) \) , with \( W = {T}_{J, I} \) . The matrix \( {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}} \) is invertible, with inverse \( {\left\lbrack {f}^{-1}\right\rbrack }_{{B}_{J}}^{{B}_{I}} \) . We can therefore apply the result of the previous question, which gives \( \left( {\det {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}}}\right) \left( {\det W}\right) = \det E \) . If \( {P}_{I} \) (resp. \( {P}_{J} \) ) denotes the transition matrix from basis \( B \) to basis \( {B}_{I} \) (resp. \( {B}_{J} \) ), we have \( {\left\lbrack f\right\rbrack }_{{B}_{I}}^{{B}_{J}} = {P}_{J}^{-1}A{P}_{I} \) , and thus

\[
\left( {\det {P}_{J}^{-1}}\right) \left( {\det A}\right) \left( {\det {P}_{I}}\right) \left( {\det {T}_{J, I}}\right)  = \det {A}_{{I}^{ * },{J}^{ * }}.
\]

(*)

> Il reste à calculer det \( {P}_{I} \) et det \( {P}_{J} \) . La matrice \( {P}_{I} \) est obtenue à partir de \( {I}_{n} \) en effectuant sur les colonnes la permutation \( \sigma \) définie par \( \sigma \left( {i}_{s}\right) = s \) pour \( 1 \leq s \leq r \) et \( \sigma \left( {k}_{s}\right) = r + s \) pour \( 1 \leq s \leq n - r \) . On a donc \( \det {P}_{I} = \varepsilon \left( \sigma \right) \det {I}_{n} = \varepsilon \left( \sigma \right) \) , où \( \varepsilon \left( \sigma \right) \) est la signature de \( \sigma \) . En notant \( C\left( {i, j}\right) \) le cycle \( \left( {i, i + 1,\ldots , j}\right) \) , un peu d’attention montre que \( \sigma = C\left( {r,{i}_{r}}\right) \cdots C\left( {2,{i}_{2}}\right) C\left( {1,{i}_{1}}\right) \) . On a donc

It remains to calculate det \( {P}_{I} \) and det \( {P}_{J} \) . The matrix \( {P}_{I} \) is obtained from \( {I}_{n} \) by performing the permutation \( \sigma \) on the columns, defined by \( \sigma \left( {i}_{s}\right) = s \) for \( 1 \leq s \leq r \) and \( \sigma \left( {k}_{s}\right) = r + s \) for \( 1 \leq s \leq n - r \) . We therefore have \( \det {P}_{I} = \varepsilon \left( \sigma \right) \det {I}_{n} = \varepsilon \left( \sigma \right) \) , where \( \varepsilon \left( \sigma \right) \) is the signature of \( \sigma \) . By noting \( C\left( {i, j}\right) \) as the cycle \( \left( {i, i + 1,\ldots , j}\right) \) , a little attention shows that \( \sigma = C\left( {r,{i}_{r}}\right) \cdots C\left( {2,{i}_{2}}\right) C\left( {1,{i}_{1}}\right) \) . We therefore have

\[
\det {P}_{I} = \varepsilon \left( \sigma \right)  = \mathop{\prod }\limits_{{s = 1}}^{r}\varepsilon \left( {C\left( {s,{i}_{s}}\right) }\right)  = \mathop{\prod }\limits_{{s = 1}}^{r}{\left( -1\right) }^{{i}_{s} - s}.
\]

De même on trouve det \( {P}_{J} = \mathop{\prod }\limits_{{s = 1}}^{r}{\left( -1\right) }^{{j}_{s} - s} \) . Avec \( \left( *\right) \) on en déduit finalement

> Similarly, we find det \( {P}_{J} = \mathop{\prod }\limits_{{s = 1}}^{r}{\left( -1\right) }^{{j}_{s} - s} \) . With \( \left( *\right) \) , we finally deduce

\[
\left( {\det A}\right) \left( {\det {T}_{J, I}}\right)  = \left( {\det {P}_{j}}\right) {\left( \det {P}_{I}\right) }^{-1}\left( {\det {A}_{{I}^{ * },{J}^{ * }}}\right)
\]

\[
= \mathop{\prod }\limits_{{s = 1}}^{r}{\left( -1\right) }^{{i}_{s} + {j}_{s} - {2s}}\det {A}_{{I}^{ * },{J}^{ * }} = {\left( -1\right) }^{S\left( {I, J}\right) }\det {A}_{{I}^{ * },{J}^{ * }}.
\]

2/ Remarquons que le cas \( r = 1 \) est une conséquence immédiate de la définition des cofacteurs de \( A \) . Supposons donc \( 2 \leq r \leq n - 1 \) .

> 2/ Let us note that the case \( r = 1 \) is an immediate consequence of the definition of the cofactors of \( A \) . Let us therefore assume \( 2 \leq r \leq n - 1 \) .

Lorsque det \( A = 0 \) , la comatrice de \( A \) est de rang 0 ou 1 (voir l’exercice 11 page 152), donc comme \( r \geq 2 \) , on a \( {\Gamma }_{I, J} = 0 \) , donc l’identité souhaitée est bien vérifiée.

> When det \( A = 0 \) , the comatrix of \( A \) has rank 0 or 1 (see exercise 11 on page 152), so since \( r \geq 2 \) , we have \( {\Gamma }_{I, J} = 0 \) , and thus the desired identity is indeed verified.

Supposons maintenant \( \det A \neq 0 \) . L’égalité \( \widetilde{A} = {\left( \det A\right) }^{\mathrm{t}}T \) avec \( T = {A}^{-1} \) montre que \( {\left( \widetilde{A}\right) }_{I, J} = \left( {\det A}\right) {T}_{J, I} \) , donc \( {\Gamma }_{I, J} = {\left( \det A\right) }^{r}\det {T}_{J, I} \) . On conclue aisément car d’après le résul-tat de la question \( 1/\mathrm{b} \) ), on a \( \left( {\det A}\right) \det {T}_{J, I} = {\left( -1\right) }^{S\left( {I, J}\right) }{\Delta }_{I, J} \) .

> Now assume \( \det A \neq 0 \) . The equality \( \widetilde{A} = {\left( \det A\right) }^{\mathrm{t}}T \) with \( T = {A}^{-1} \) shows that \( {\left( \widetilde{A}\right) }_{I, J} = \left( {\det A}\right) {T}_{J, I} \) , therefore \( {\Gamma }_{I, J} = {\left( \det A\right) }^{r}\det {T}_{J, I} \) . We conclude easily because, according to the result of question \( 1/\mathrm{b} \) ), we have \( \left( {\det A}\right) \det {T}_{J, I} = {\left( -1\right) }^{S\left( {I, J}\right) }{\Delta }_{I, J} \) .

Problem 7. a) Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Montrer l’équivalence

> Problem 7. a) Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) . Show the equivalence

\[
\left( {M \notin  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) }\right)  \Leftrightarrow  \left( {\left( {\exists P \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) }\right) ,\forall \lambda  \in  \mathbb{C}, P - {\lambda M} \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) }\right) .
\]

b) Soit \( \varphi \in \mathcal{L}\left( {{\mathcal{M}}_{n}\left( \mathbb{C}\right) }\right) \) telle que

> b) Let \( \varphi \in \mathcal{L}\left( {{\mathcal{M}}_{n}\left( \mathbb{C}\right) }\right) \) such that

\[
\forall M \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) ,\;\varphi \left( M\right)  \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) .
\]

Montrer que si \( \varphi \left( M\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , alors \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) .

> Show that if \( \varphi \left( M\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , then \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) .

Solution. a) Condition nécessaire. Supposons \( M \) non inversible. Si \( r = \operatorname{rg}M \) , on sait que \( M \) est équivalente à la matrice \( {K}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , autrement dit il existe \( A, B \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) tels que \( M = A{K}_{r}B \) . Posons \( J = \left( \begin{matrix} 0 & 1 \\ {I}_{n - 1} & 0 \end{matrix}\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . Pour tout \( \lambda \in \mathbb{C} \) on a

> Solution. a) Necessary condition. Suppose \( M \) is not invertible. If \( r = \operatorname{rg}M \) , we know that \( M \) is equivalent to the matrix \( {K}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) , in other words there exist \( A, B \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that \( M = A{K}_{r}B \) . Let \( J = \left( \begin{matrix} 0 & 1 \\ {I}_{n - 1} & 0 \end{matrix}\right) \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . For any \( \lambda \in \mathbb{C} \) we have

\[
\left. {J - \lambda {K}_{r} = \left( \begin{matrix}  - \lambda & 0 & \cdots & \cdots & 0 & 1 \\  1 &  \ddots  &  \ddots  & & & 0 \\  0 &  \ddots  &  - \lambda & 0 & & \vdots \\  \vdots &  \ddots  & 1 & 0 & & \vdots \\  \vdots & &  \ddots  &  \ddots  &  \ddots  & \vdots \\  0 & \cdots & \cdots & 0 & 1 & 0 \end{matrix}\right) .}\right\}  r\text{ lignes }
\]

(*)

> Le rang d'une matrice reste inchangé lorsque l'on ajoute à une ligne une combinaison linéaire des autres. En ajoutant à la \( r \) -ième ligne dans \( \left( *\right) \lambda \) fois la suivante, on fait disparaître le \( - \lambda \) se trouvant à la position \( \left( {r, r}\right) \) . En itérant ainsi le procédé aux lignes d’indice \( r - 1,\ldots ,1 \) , on fait disparaître tous les \( - \lambda \) , de sorte que \( \operatorname{rg}\left( {J - \lambda {K}_{r}}\right) = \operatorname{rg}J = n \) . Ainsi, \( J - \lambda {K}_{r} \in {\mathcal{G}}_{{\ell }_{n}}\left( \mathbb{C}\right) \) , donc \( A\left( {J - \lambda {K}_{r}}\right) B = P - {\lambda M} \) (avec \( P = {AJB} \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) ) est inversible pour tout \( \lambda \in \mathbb{C} \) , d’où la condition nécessaire.

The rank of a matrix remains unchanged when a linear combination of other rows is added to a row. By adding \( \left( *\right) \lambda \) times the following row to the \( r \) -th row in \( - \lambda \) , we eliminate the \( - \lambda \) located at position \( \left( {r, r}\right) \) . By iterating this process for rows with index \( r - 1,\ldots ,1 \) , we eliminate all \( - \lambda \) , so that \( \operatorname{rg}\left( {J - \lambda {K}_{r}}\right) = \operatorname{rg}J = n \) . Thus, \( J - \lambda {K}_{r} \in {\mathcal{G}}_{{\ell }_{n}}\left( \mathbb{C}\right) \) , therefore \( A\left( {J - \lambda {K}_{r}}\right) B = P - {\lambda M} \) (with \( P = {AJB} \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) ) is invertible for any \( \lambda \in \mathbb{C} \) , hence the necessary condition.

> Condition suffisante. Raisonnons par l’absurde et supposons \( M \) inversible. Si \( Q = {M}^{-1}P \) , on a

Sufficient condition. Let us reason by contradiction and assume \( M \) is invertible. If \( Q = {M}^{-1}P \) , we have

\[
\forall \lambda  \in  \mathbb{C},\;\det \left( {P - {\lambda M}}\right)  = \left( {\det M}\right) \left( {\det \left( {Q - \lambda {I}_{n}}\right) }\right)  \neq  0
\]

donc \( \det \left( {Q - \lambda {I}_{n}}\right) \neq 0 \) pour tout \( \lambda \in \mathbb{C} \) . Ceci est impossible puisque \( \det \left( {Q - \lambda {I}_{n}}\right) \) est un polynôme de degré \( n \) en \( \lambda \) (c’est le polynôme caractéristique de \( Q \) ) donc s’annule au moins une fois sur \( \mathbb{C} \) . D'où la condition suffisante.

> therefore \( \det \left( {Q - \lambda {I}_{n}}\right) \neq 0 \) for any \( \lambda \in \mathbb{C} \) . This is impossible since \( \det \left( {Q - \lambda {I}_{n}}\right) \) is a polynomial of degree \( n \) in \( \lambda \) (it is the characteristic polynomial of \( Q \) ) and thus vanishes at least once on \( \mathbb{C} \) . Hence the sufficient condition.

b) Raisonnons par l’absurde en supposant \( M \notin \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . D’après la question précédente, il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que pour tout \( \lambda \in \mathbb{C}, P - {\lambda M} \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . En vertu de l’hypothèse faite sur \( \varphi \) et de la linéarité de \( \varphi \) , ceci entraîne

> b) Let us reason by contradiction by assuming \( M \notin \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . According to the previous question, there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that for any \( \lambda \in \mathbb{C}, P - {\lambda M} \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) . By virtue of the hypothesis made on \( \varphi \) and the linearity of \( \varphi \) , this implies

\[
\forall \lambda  \in  \mathbb{C},\;\varphi \left( P\right)  - {\lambda \varphi }\left( M\right)  \in  \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) ,
\]

donc d’après la question précédente, \( \varphi \left( M\right) \notin \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , ce qui est contradictoire. Finalement, on a \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) .

> therefore, according to the previous question, \( \varphi \left( M\right) \notin \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) , which is a contradiction. Finally, we have \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) .

Problem 8. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

> Problem 8. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) .

1/ Soit \( \psi : {\mathbb{N}}^{ * } \rightarrow \mathbb{R} \) une fonction. Si pour tout \( \left( {i, j}\right) \) ,

> 1/ Let \( \psi : {\mathbb{N}}^{ * } \rightarrow \mathbb{R} \) be a function. If for all \( \left( {i, j}\right) \) ,

\[
{a}_{i, j} = \mathop{\sum }\limits_{{k\left| {i\text{ et }k}\right| j}}\psi \left( k\right)
\]

montrer que \( \det A = \psi \left( 1\right) \psi \left( 2\right) \cdots \psi \left( n\right) \) .

> show that \( \det A = \psi \left( 1\right) \psi \left( 2\right) \cdots \psi \left( n\right) \) .

2 / (Applications). Calculer det \( A \) si

> 2 / (Applications). Calculate det \( A \) if

a) \( {a}_{i, j} \) est le nombre de diviseurs communs à \( i \) et à \( j \) .

> a) \( {a}_{i, j} \) is the number of common divisors of \( i \) and \( j \) .

b) \( {a}_{i, j} \) est la somme des diviseurs communs à \( i \) et à \( j \) .

> b) \( {a}_{i, j} \) is the sum of the common divisors of \( i \) and \( j \) .

c) \( {a}_{i, j} = i \land j = \operatorname{pgcd}\left( {i, j}\right) \) .

> Solution. 1 / On définit la matrice \( B = {\left( {b}_{i, j}\right) }_{1 \leq i, j \leq n} \) par \( {b}_{i, j} = 1 \) si \( i \mid j,{b}_{i, j} = 0 \) si \( i \nmid j \) . Elle est triangulaire supérieure et n’a que des 1 sur la diagonale principale, donc det \( B = 1 \) . On définit aussi la matrice \( C = {\left( {c}_{i, j}\right) }_{1 \leq i, j \leq n} \) comme étant une matrice diagonale avec \( {c}_{i, i} = \psi \left( i\right) \) . On pose maintenant \( D = {}^{\mathrm{t}}{BCB} = {\left( {d}_{i, j}\right) }_{1 \leq i, j \leq n} \) . Pour tout \( \left( {i, j}\right) \) , on a

Solution. 1 / We define the matrix \( B = {\left( {b}_{i, j}\right) }_{1 \leq i, j \leq n} \) by \( {b}_{i, j} = 1 \) if \( i \mid j,{b}_{i, j} = 0 \) if \( i \nmid j \) . It is upper triangular and has only 1s on the main diagonal, so det \( B = 1 \) . We also define the matrix \( C = {\left( {c}_{i, j}\right) }_{1 \leq i, j \leq n} \) as a diagonal matrix with \( {c}_{i, i} = \psi \left( i\right) \) . We now set \( D = {}^{\mathrm{t}}{BCB} = {\left( {d}_{i, j}\right) }_{1 \leq i, j \leq n} \) . For all \( \left( {i, j}\right) \) , we have

\[
{d}_{i, j} = \mathop{\sum }\limits_{{k,\ell }}{b}_{k, i}{c}_{k,\ell }{b}_{\ell , j} = \mathop{\sum }\limits_{k}{b}_{k, i}\psi \left( k\right) {b}_{k, j} = \mathop{\sum }\limits_{{k \mid  i\text{ et }k \mid  j}}\psi \left( k\right)  = {a}_{i, j}.
\]

Donc \( D = A = {}^{\mathrm{t}}{BCB} \) , et donc det \( A = \det \left( {{}^{\mathrm{t}}B}\right) \cdot \det C \cdot \det B = \det C \) . Le déterminant de la matrice diagonale \( C \) est le produit de ses coefficients diagonaux, donc det \( A = \psi \left( 1\right) \cdots \psi \left( n\right) \) .

> Therefore \( D = A = {}^{\mathrm{t}}{BCB} \) , and thus det \( A = \det \left( {{}^{\mathrm{t}}B}\right) \cdot \det C \cdot \det B = \det C \) . The determinant of the diagonal matrix \( C \) is the product of its diagonal coefficients, so det \( A = \psi \left( 1\right) \cdots \psi \left( n\right) \) .

2 / a) Il suffit d’appliquer 1 / avec \( \psi \left( k\right) = 1 \) . On en tire det \( A = 1 \) .

> 2 / a) It suffices to apply 1 / with \( \psi \left( k\right) = 1 \) . We derive det \( A = 1 \) .

b) On applique cette fois ci \( 1/ \) avec \( \psi \left( k\right) = k \) , et on en tire det \( A = n \) !.

> b) We apply this time \( 1/ \) with \( \psi \left( k\right) = k \) , and we derive det \( A = n \) !.

c) Remarquons d'abord que l'on a l'équivalence

> c) Let us first note that we have the equivalence

\[
\left( {k\left| {i\text{ et }k}\right| j}\right)  \Leftrightarrow  \left( {k \mid  \operatorname{pgcd}\left( {i, j}\right) }\right) .
\]

Rappelons que \( \varphi \) , l’indicateur d’Euler, possède la propriété suivante : pour tout \( m,\mathop{\sum }\limits_{{k \mid m}}\varphi \left( k\right) = \; m \) (voir la proposition 6 page 34). On a donc

> Recall that \( \varphi \) , Euler's totient function, has the following property: for all \( m,\mathop{\sum }\limits_{{k \mid m}}\varphi \left( k\right) = \; m \) (see proposition 6 on page 34). We therefore have

\[
{a}_{i, j} = \operatorname{pgcd}\left( {i, j}\right)  = \mathop{\sum }\limits_{{k \mid  \operatorname{pgcd}\left( {i, j}\right) }}\varphi \left( k\right)  = \mathop{\sum }\limits_{{k\left| {i\text{ et }k}\right| j}}\varphi \left( k\right)
\]

et d’après \( 1/ \) appliqué à \( \psi = \varphi \) , on a det \( A = \varphi \left( 1\right) \cdots \varphi \left( n\right) \) .

> and according to \( 1/ \) applied to \( \psi = \varphi \) , we have det \( A = \varphi \left( 1\right) \cdots \varphi \left( n\right) \) .

Problem 9. Soient \( n \geq 2 \) un entier et \( \mathbb{K} \) un corps commutatif. Montrer que tout hyperplan de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) contient au moins une matrice inversible.

> Problem 9. Let \( n \geq 2 \) be an integer and \( \mathbb{K} \) a commutative field. Show that every hyperplane of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) contains at least one invertible matrix.

Solution. Soit \( H \) un hyperplan de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Il existe une forme linéaire non nulle \( \varphi \) de \( {\left( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \right) }^{ * } \) telle que \( H = \operatorname{Ker}\varphi \) . D’après l’exercice 3 de la partie 4.6 (page 138), il existe une matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telle que \( \varphi \left( M\right) = \operatorname{tr}\left( {AM}\right) \) pour tout \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . Comme \( \varphi \neq 0 \) , on a \( A \neq 0 \) . Finalement, \( H = \operatorname{Ker}\varphi = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \mid \operatorname{tr}\left( {AM}\right) = 0}\right\} \) . Il s’agit donc de montrer que

> Solution. Let \( H \) be a hyperplane of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). There exists a non-zero linear form \( \varphi \) on \( {\left( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \right) }^{ * } \) such that \( H = \operatorname{Ker}\varphi \). According to exercise 3 of part 4.6 (page 138), there exists a matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) such that \( \varphi \left( M\right) = \operatorname{tr}\left( {AM}\right) \) for all \( M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). Since \( \varphi \neq 0 \), we have \( A \neq 0 \). Finally, \( H = \operatorname{Ker}\varphi = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \mid \operatorname{tr}\left( {AM}\right) = 0}\right\} \). It is therefore a matter of showing that

\[
\left( {\forall A \in  {\mathcal{M}}_{n}\left( \mathbb{R}\right) , A \neq  0,\exists M \in  \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) }\right) ,\;\operatorname{tr}\left( {AM}\right)  = 0.
\]

(*)

> On se place dans un cas où \( A \) est plus simple. En posant \( r = \operatorname{rg}\left( A\right) \geq 1 \) (car \( A \neq 0 \) ), on sait que \( A \) est équivalente à la matrice par bloc \( \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) (voir le théorème 1 page 128), c’est-à-dire

We consider a case where \( A \) is simpler. By setting \( r = \operatorname{rg}\left( A\right) \geq 1 \) (since \( A \neq 0 \)), we know that \( A \) is equivalent to the block matrix \( \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) (see theorem 1 on page 128), that is to say

\[
\exists P, Q \in  \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \;\text{ tels que }\;{PAQ} = {J}_{r}\;\text{ avec }\;{J}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\  0 & 0 \end{matrix}\right) .
\]

Fixons une matrice inversible \( M \) n’ayant que des 0 sur sa diagonale principale (on peut prendre par exemple \( M = \left( \begin{matrix} 0 & {I}_{n - 1} \\ 1 & 0 \end{matrix}\right) \) ). En écrivant la matrice \( M \) sous forme de blocs \( M = \left( \begin{matrix} {A}_{r} & {B}_{r} \\ {C}_{r} & {D}_{r} \end{matrix}\right) \) , avec \( {A}_{r} \in {\mathcal{M}}_{r}\left( \mathbb{K}\right) \) , on a

> Let us fix an invertible matrix \( M \) having only 0s on its main diagonal (we can take, for example, \( M = \left( \begin{matrix} 0 & {I}_{n - 1} \\ 1 & 0 \end{matrix}\right) \)). By writing the matrix \( M \) in block form \( M = \left( \begin{matrix} {A}_{r} & {B}_{r} \\ {C}_{r} & {D}_{r} \end{matrix}\right) \), with \( {A}_{r} \in {\mathcal{M}}_{r}\left( \mathbb{K}\right) \), we have

\[
{J}_{r}M = \left( \begin{matrix} {A}_{r} & {B}_{r} \\  0 & 0 \end{matrix}\right) ,
\]

ce qui montre que, comme \( M \) , la matrice \( {J}_{r}M\mathrm{n} \) ’a que des 0 sur sa diagonale principale. Ainsi, \( \operatorname{tr}\left( {{J}_{r}M}\right) = 0 \) . En posant \( N = {QMP} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , on a \( M = {Q}^{-1}N{P}^{-1} \) et

> which shows that, like \( M \), the matrix \( {J}_{r}M\mathrm{n} \) has only 0s on its main diagonal. Thus, \( \operatorname{tr}\left( {{J}_{r}M}\right) = 0 \). By setting \( N = {QMP} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \), we have \( M = {Q}^{-1}N{P}^{-1} \) and

\[
0 = \operatorname{tr}\left( {{J}_{r}M}\right)  = \operatorname{tr}\left( {\left( {PAQ}\right) \left( {{Q}^{-1}N{P}^{-1}}\right) }\right)  = \operatorname{tr}\left( {P\left( {AN}\right) {P}^{-1}}\right)  = \operatorname{tr}\left( {AN}\right)
\]

(deux matrices semblables ont même trace), d'où le résultat d'après (*).

> (two similar matrices have the same trace), hence the result according to (*).

Remarque. Le problème suivant montre un résultat plus fort qui entraîne que la dimension maximale d’un sous-espace de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) ne contenant aucune matrice inversible est \( n\left( {n - 1}\right) \) .

> Remark. The following problem shows a stronger result which implies that the maximum dimension of a subspace of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) containing no invertible matrix is \( n\left( {n - 1}\right) \).

Problem 10. Soit \( n \in {\mathbb{N}}^{ * }, n \geq 2 \) , et \( \mathbb{K} \) un corps commutatif infini. Soit \( V \) un sous-espace vectoriel non nul de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , tel que \( p = \max \{ \operatorname{rg}M \mid M \in V\} \) vérifie \( p < n \) . On veut montrer que \( \dim V \leq {np} \) .

> Problem 10. Let \( n \in {\mathbb{N}}^{ * }, n \geq 2 \), and \( \mathbb{K} \) be an infinite commutative field. Let \( V \) be a non-zero vector subspace of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), such that \( p = \max \{ \operatorname{rg}M \mid M \in V\} \) satisfies \( p < n \). We want to show that \( \dim V \leq {np} \).

1/ Montrer qu’on peut se ramener au cas où la matrice \( J = \left( \begin{matrix} {I}_{p} & 0 \\ 0 & 0 \end{matrix}\right) \) appartient à \( V \) . On suppose ceci vérifié dans la suite. Montrer que toute matrice \( M \) de \( V \) s’écrit sous la forme

> 1/ Show that one can reduce to the case where the matrix \( J = \left( \begin{matrix} {I}_{p} & 0 \\ 0 & 0 \end{matrix}\right) \) belongs to \( V \). We assume this is verified in the following. Show that any matrix \( M \) of \( V \) can be written in the form

\[
M = \left( \begin{array}{ll} A & C \\  B & 0 \end{array}\right) \;\text{ avec }\;A \in  {\mathcal{M}}_{p}\left( \mathbb{K}\right) , B \in  {\mathcal{M}}_{n - p, p}\left( \mathbb{K}\right) , C \in  {\mathcal{M}}_{p, n - p}\left( \mathbb{K}\right) \text{ et }{BC} = 0.
\]

On note alors \( A = a\left( M\right) , B = b\left( M\right) \) et \( C = c\left( M\right) \) . 2/a) Soit \( M \in V \) telle que \( c\left( M\right) = 0 \) . Montrer que \( E \subset \operatorname{Ker}b\left( M\right) \) , où \( E \) est le s.e.v de \( {\mathbb{K}}^{p} \) défini par \( E = { \cup }_{N \in V}\operatorname{Im}c\left( N\right) \) .

> We then denote \( A = a\left( M\right) , B = b\left( M\right) \) and \( C = c\left( M\right) \). 2/a) Let \( M \in V \) be such that \( c\left( M\right) = 0 \). Show that \( E \subset \operatorname{Ker}b\left( M\right) \), where \( E \) is the subspace of \( {\mathbb{K}}^{p} \) defined by \( E = { \cup }_{N \in V}\operatorname{Im}c\left( N\right) \).

b) On note \( r = \dim E \) et on considère une base \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) de \( E \) , complétée en une base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) de \( {\mathbb{K}}^{p} \) . Montrer que l’application définie sur \( V \) par

> b) We denote \( r = \dim E \) and consider a basis \( \left( {{e}_{1},\ldots ,{e}_{r}}\right) \) of \( E \), extended to a basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) of \( {\mathbb{K}}^{p} \). Show that the map defined on \( V \) by

\[
\Phi  : M = \left( \begin{array}{ll} A & C \\  B & 0 \end{array}\right)  \mapsto  \left( {A, B{e}_{r + 1},\ldots , B{e}_{p}, C}\right)
\]

(où \( A = a\left( M\right) , B = b\left( M\right) \) et \( C = c\left( M\right) \) ) est injective et en déduire que \( \dim V \leq {np} \) .

> (where \( A = a\left( M\right) , B = b\left( M\right) \) and \( C = c\left( M\right) \)) is injective and deduce that \( \dim V \leq {np} \).

Solution. 1/ Par définition de \( p \) , il existe une matrice \( M \in V \) telle que rg \( M = p \) . La matrice \( M \) est donc équivalente à \( J \) , de sorte qu’il existe deux matrices \( P, Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) telles que \( {PMQ} = J \) . L’application \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) M \mapsto {PMQ} \) est un isomorphisme, il est donc équivalent de montrer que \( W = {PVQ} \) , s.e.v de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) qui contient \( J \) , vérifie \( \dim W \leq {np} \) . On peut donc supposer \( J \in V \) .

> Solution. 1/ By definition of \( p \), there exists a matrix \( M \in V \) such that rg \( M = p \). The matrix \( M \) is therefore equivalent to \( J \), so that there exist two matrices \( P, Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) such that \( {PMQ} = J \). The map \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \rightarrow {\mathcal{M}}_{n}\left( \mathbb{K}\right) M \mapsto {PMQ} \) is an isomorphism, so it is equivalent to show that \( W = {PVQ} \), a subspace of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) which contains \( J \), satisfies \( \dim W \leq {np} \). We can therefore assume \( J \in V \).

Soit \( M \in V, M = \left( \begin{array}{ll} A & C \\ B & D \end{array}\right) \) son écriture par blocs avec \( A \in {\mathcal{M}}_{p}\left( \mathbb{K}\right) \) . Comme \( V \) est un sous-espace vectoriel, pour tout \( \lambda \in \mathbb{K} \) on a \( M + {\lambda J} \in V \) , donc \( \operatorname{rg}\left( {M + {\lambda J}}\right) \leq p \) . Soient \( i, j \) tels que \( 1 \leq i, j \leq n - p \) . En restreignant la matrice \( M + {\lambda J} \) aux indices de lignes \( 1,\ldots , p, p + i \) et de colonnes \( 1,\ldots , p, p + j \) , on obtient une matrice extraite \( {R}_{\lambda } \) de \( M \) de taille \( p + 1 \) qui s’écrit sous la forme \( {R}_{\lambda } = \left( \begin{matrix} A + \lambda {I}_{p} & {C}_{j} \\ {B}_{i} & {d}_{i, j} \end{matrix}\right) \) où \( {B}_{i} \) est la \( i \) -ième ligne de \( B,{C}_{j} \) la \( j \) -ième colonne de \( C \) , et \( {d}_{i, j} \) le coefficient d’indice \( \left( {i, j}\right) \) de \( D \) . Pour tout \( \lambda \in \mathbb{K} \) , rg \( {R}_{\lambda } \leq p \) donc det \( {R}_{\lambda } = 0 \) . Or det \( {R}_{\lambda } \) est un polynôme en \( \lambda \) ; il s’annule en une infinité de valeurs, donc ses coefficients sont nuls. En particulier son coefficient dominant,égal à \( {d}_{i, j} \) , est nul, donc \( D = 0 \) . Calculons le coefficient de \( {\lambda }^{p - 1} \) de det \( {R}_{\lambda } \) . Notons \( {r}_{k,\ell } \) les coefficients de \( {R}_{\lambda } \) et utilisons l’expression

> Let \( M \in V, M = \left( \begin{array}{ll} A & C \\ B & D \end{array}\right) \) be its block representation with \( A \in {\mathcal{M}}_{p}\left( \mathbb{K}\right) \) . Since \( V \) is a vector subspace, for any \( \lambda \in \mathbb{K} \) we have \( M + {\lambda J} \in V \) , thus \( \operatorname{rg}\left( {M + {\lambda J}}\right) \leq p \) . Let \( i, j \) be such that \( 1 \leq i, j \leq n - p \) . By restricting the matrix \( M + {\lambda J} \) to the row indices \( 1,\ldots , p, p + i \) and column indices \( 1,\ldots , p, p + j \) , we obtain a submatrix \( {R}_{\lambda } \) of \( M \) of size \( p + 1 \) which is written in the form \( {R}_{\lambda } = \left( \begin{matrix} A + \lambda {I}_{p} & {C}_{j} \\ {B}_{i} & {d}_{i, j} \end{matrix}\right) \) where \( {B}_{i} \) is the \( i \) -th row of \( B,{C}_{j} \) , the \( j \) -th column of \( C \) , and \( {d}_{i, j} \) the coefficient with index \( \left( {i, j}\right) \) of \( D \) . For any \( \lambda \in \mathbb{K} \) , rg \( {R}_{\lambda } \leq p \) thus det \( {R}_{\lambda } = 0 \) . However, det \( {R}_{\lambda } \) is a polynomial in \( \lambda \) ; it vanishes at infinitely many values, so its coefficients are zero. In particular, its leading coefficient, equal to \( {d}_{i, j} \) , is zero, thus \( D = 0 \) . Let us calculate the coefficient of \( {\lambda }^{p - 1} \) of det \( {R}_{\lambda } \) . Let \( {r}_{k,\ell } \) denote the coefficients of \( {R}_{\lambda } \) and use the expression

\[
\det {R}_{\lambda } = \mathop{\sum }\limits_{{\sigma  \in  {\mathcal{S}}_{p + 1}}}{\Pi }_{\sigma },\;{\Pi }_{\sigma } = \mathop{\prod }\limits_{{k = 1}}^{{p + 1}}{r}_{k,\sigma \left( k\right) }.
\]

(*)

> Les seuls coefficients de \( {R}_{\lambda } \) qui contiennent \( \lambda \) sont les \( {r}_{k, k} \) avec \( k \leq p \) , donc le degré (en \( \lambda \) ) de \( {\Pi }_{\sigma } \) est inférieur à \( {f}_{\sigma } = \left| {\{ k \leq p \mid \sigma \left( k\right) = k\} }\right| \) . Ainsi, les termes de la somme (*) qui contribuent au coefficient de \( {\lambda }^{p - 1} \) dans det \( {R}_{\lambda } \) sont ceux pour lequels \( {f}_{\sigma } \geq p - 1 \) . Lorsque \( {f}_{\sigma } = p \) , on a forcément \( \sigma \left( {p + 1}\right) = p + 1 \) donc \( {\Pi }_{\sigma } = 0 \) puisqu’il contient le terme \( {r}_{p + 1, p + 1} \) qui est nul (vu plus haut). Les permutations \( \sigma \) vérifiant \( {f}_{\sigma } = p - 1 \) , sont les transpositions de la forme \( \sigma = {\tau }_{k, p + 1} \) où \( k \leq p \) , et dans ce cas le coefficient de \( {\lambda }^{p - 1} \) dans \( {\Pi }_{\sigma } \) est égal à \( {r}_{k, p + 1}{r}_{p + 1, k} \) . Le coefficient de \( {\lambda }^{p - 1} \) dans det \( {R}_{\lambda } \) est donc égal à

The only coefficients of \( {R}_{\lambda } \) that contain \( \lambda \) are the \( {r}_{k, k} \) with \( k \leq p \) , so the degree (in \( \lambda \) ) of \( {\Pi }_{\sigma } \) is less than \( {f}_{\sigma } = \left| {\{ k \leq p \mid \sigma \left( k\right) = k\} }\right| \) . Thus, the terms of the sum (*) that contribute to the coefficient of \( {\lambda }^{p - 1} \) in det \( {R}_{\lambda } \) are those for which \( {f}_{\sigma } \geq p - 1 \) . When \( {f}_{\sigma } = p \) , we necessarily have \( \sigma \left( {p + 1}\right) = p + 1 \) thus \( {\Pi }_{\sigma } = 0 \) since it contains the term \( {r}_{p + 1, p + 1} \) which is zero (seen above). The permutations \( \sigma \) satisfying \( {f}_{\sigma } = p - 1 \) are the transpositions of the form \( \sigma = {\tau }_{k, p + 1} \) where \( k \leq p \) , and in this case the coefficient of \( {\lambda }^{p - 1} \) in \( {\Pi }_{\sigma } \) is equal to \( {r}_{k, p + 1}{r}_{p + 1, k} \) . The coefficient of \( {\lambda }^{p - 1} \) in det \( {R}_{\lambda } \) is therefore equal to

\[
\det {R}_{\lambda } = \mathop{\sum }\limits_{{k = 1}}^{p}{r}_{k, p + 1}{r}_{p + 1, k} = {B}_{i}{C}_{j}.
\]

Donc \( {B}_{i}{C}_{j} = 0 \) , et vu que \( {B}_{i}{C}_{j} \) est le coefficient d’indice \( \left( {i, j}\right) \) de \( {BC} \) , on en déduit \( {BC} = 0 \) .

> Therefore \( {B}_{i}{C}_{j} = 0 \) , and since \( {B}_{i}{C}_{j} \) is the coefficient with index \( \left( {i, j}\right) \) of \( {BC} \) , we deduce \( {BC} = 0 \) .

2/a) Pour toute matrice \( N \in V \) , on a \( M + N \in V \) , donc d’après le résultat précédent \( 0 = \; b\left( {M + N}\right) c\left( {M + N}\right) \) , ce qui entraîne 0 \( = \left( {b\left( M\right) + b\left( N\right) }\right) c\left( N\right) = b\left( M\right) c\left( N\right) \) . Ainsi pour tout \( N \in V \) on a \( \operatorname{Im}c\left( N\right) \subset \operatorname{Ker}b\left( M\right) \) . On en déduit le résultat.

> 2/a) For any matrix \( N \in V \) , we have \( M + N \in V \) , so according to the previous result \( 0 = \; b\left( {M + N}\right) c\left( {M + N}\right) \) , which implies 0 \( = \left( {b\left( M\right) + b\left( N\right) }\right) c\left( N\right) = b\left( M\right) c\left( N\right) \) . Thus for any \( N \in V \) we have \( \operatorname{Im}c\left( N\right) \subset \operatorname{Ker}b\left( M\right) \) . We deduce the result.

b) Supposons \( \Phi \left( M\right) = 0 \) avec \( M = \left( \begin{array}{ll} A & C \\ B & 0 \end{array}\right) \in V \) . Alors \( A = 0 \) et \( C = 0 \) . On a aussi \( B{e}_{k} = 0 \) pour \( r < k \leq p \) , et d’après la question précédente on a \( B{e}_{k} = 0 \) pour \( k \leq r \) . Donc \( B \) s’annule sur la base \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) , donc \( B = 0 \) . L’application linéaire \( \Phi \) vérifie donc Ker \( \Phi = \{ 0\} \) .

> b) Suppose \( \Phi \left( M\right) = 0 \) with \( M = \left( \begin{array}{ll} A & C \\ B & 0 \end{array}\right) \in V \) . Then \( A = 0 \) and \( C = 0 \) . We also have \( B{e}_{k} = 0 \) for \( r < k \leq p \) , and according to the previous question we have \( B{e}_{k} = 0 \) for \( k \leq r \) . Therefore \( B \) vanishes on the basis \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) , so \( B = 0 \) . The linear map \( \Phi \) therefore satisfies Ker \( \Phi = \{ 0\} \) .

L’image de \( \Phi \) est incluse dans \( {\mathcal{M}}_{p}\left( \mathbb{K}\right) \times {\left( {\mathbb{K}}^{n - p}\right) }^{p - r} \times U \) , où \( U = \{ c\left( M\right) \mid M \in V\} \) . Or pour tout \( M \in V \) , on a \( \operatorname{Im}c\left( N\right) \subset E \) , donc le s.e.v. \( U \) est inclus (à un isomorphisme près) dans \( \mathcal{L}\left( {{\mathbb{K}}^{n - p}, E}\right) \) . On en déduit \( \dim U \leq \left( {n - p}\right) r \) et

> The image of \( \Phi \) is included in \( {\mathcal{M}}_{p}\left( \mathbb{K}\right) \times {\left( {\mathbb{K}}^{n - p}\right) }^{p - r} \times U \) , where \( U = \{ c\left( M\right) \mid M \in V\} \) . However, for any \( M \in V \) , we have \( \operatorname{Im}c\left( N\right) \subset E \) , so the subspace \( U \) is included (up to an isomorphism) in \( \mathcal{L}\left( {{\mathbb{K}}^{n - p}, E}\right) \) . We deduce \( \dim U \leq \left( {n - p}\right) r \) and

\[
\dim \operatorname{Im}\Phi  \leq  \dim {\mathcal{M}}_{p}\left( \mathbb{K}\right)  + \left( {n - p}\right) \left( {p - r}\right)  + \dim U \leq  {p}^{2} + \left( {n - p}\right) \left( {p - r}\right)  + \left( {n - p}\right) r = {np}.
\]

On conclut en écrivant \( \dim V = \dim \operatorname{Ker}\Phi + \dim \operatorname{Im}\Phi = \dim \operatorname{Im}\Phi \) .

> We conclude by writing \( \dim V = \dim \operatorname{Ker}\Phi + \dim \operatorname{Im}\Phi = \dim \operatorname{Im}\Phi \) .

Remarque. L’égalité peut avoir lieu, par exemple le s.e.v \( V \) des matrices dont les \( n - p \) dernières lignes sont nulles, vérifie \( \dim V = {np} \) , et on a \( \max \{ \operatorname{rg}M, M \in V\} = p \) .

> Remark. Equality can occur, for example the subspace \( V \) of matrices whose \( n - p \) last rows are zero, satisfies \( \dim V = {np} \) , and we have \( \max \{ \operatorname{rg}M, M \in V\} = p \) .

Problem 11. Soit \( n \in {\mathbb{N}}^{ * } \) et une application \( p : {\mathcal{M}}_{n}\left( \mathbb{C}\right) \rightarrow {\mathbb{R}}^{ + } \) vérifiant

> Problem 11. Let \( n \in {\mathbb{N}}^{ * } \) and a map \( p : {\mathcal{M}}_{n}\left( \mathbb{C}\right) \rightarrow {\mathbb{R}}^{ + } \) satisfying

(i) \( \forall A \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\forall \lambda \in \mathbb{C},\;p\left( {\lambda A}\right) \leq \left| \lambda \right| p\left( A\right) \) .

> (ii) \( \forall A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\;p\left( {A + B}\right) \leq p\left( A\right) + p\left( B\right) \) .

(ii) \( \forall A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\;p\left( {A + B}\right) \leq p\left( A\right) + p\left( B\right) \) .

> (iii) \( \forall A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\;p\left( {AB}\right) \leq p\left( A\right) p\left( B\right) \) .

(iii) \( \forall A, B \in {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\;p\left( {AB}\right) \leq p\left( A\right) p\left( B\right) \) .

> Montrer que \( p = 0 \) ou que \( p \) est une norme sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

Show that \( p = 0 \) or that \( p \) is a norm on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> Solution. Commençons par remarquer que d'après (i),

Solution. Let us begin by noting that according to (i),

\[
\forall \lambda  \in  {\mathbb{C}}^{ * },\forall A \in  {\mathcal{M}}_{n}\left( \mathbb{C}\right) ,\;p\left( {\lambda A}\right)  \leq  \left| \lambda \right| p\left( A\right)  = \left| \lambda \right| p\left( {\frac{1}{\lambda }\left( {\lambda A}\right) }\right)  \leq  \left| \lambda \right|  \cdot  \left| \frac{1}{\lambda }\right| p\left( {\lambda A}\right)  = p\left( {\lambda A}\right) ,
\]

ce qui entraîne \( p\left( {\lambda A}\right) = \left| \lambda \right| p\left( A\right) \) pour tout \( \lambda \in \mathbb{C} \) .

> which implies \( p\left( {\lambda A}\right) = \left| \lambda \right| p\left( A\right) \) for all \( \lambda \in \mathbb{C} \) .

Supposons \( p \neq 0 \) . Pour montrer que \( p \) est une norme, il nous reste à prouver que \( p\left( A\right) = 0 \) implique \( A = 0 \) . Pour cela, raisonnons par l’absurde en supposant \( p\left( A\right) = 0 \) et \( A \neq 0 \) . Si \( r = \operatorname{rg}A > 0 \) , on sait \( A \) est équivalente à la matrice \( {J}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) de sorte qu’il existe \( P, Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telles que \( {J}_{r} = {PAQ} \) . D’après la propriété (iii), on a \( p\left( {J}_{r}\right) = p\left( {PAQ}\right) \leq p\left( P\right) p\left( A\right) p\left( Q\right) = 0 \) , donc \( p\left( {J}_{r}\right) = 0 \) . La propriété (iii) appliquée à l’égalité \( {J}_{1} = {J}_{1}{J}_{r} \) donne \( p\left( {J}_{1}\right) \leq p\left( {J}_{1}\right) p\left( {J}_{r}\right) = 0 \) , donc \( p\left( {J}_{1}\right) = 0 \) . Désignons par \( {D}_{i} \) la matrice dont tous les coefficients sont nuls sauf celui d’indice \( \left( {i, i}\right) \) qui vaut 1. La matrice \( {D}_{i} \) est de rang 1, donc équivalente à la matrice \( {J}_{1} \) , et comme \( p\left( {J}_{1}\right) = 0 \) , un raisonnement similaire au précédent donne \( p\left( {D}_{i}\right) = 0 \) . Maintenant, l’assertion (ii) entraîne

> Assume \( p \neq 0 \) . To show that \( p \) is a norm, we still need to prove that \( p\left( A\right) = 0 \) implies \( A = 0 \) . To do this, let us reason by contradiction by assuming \( p\left( A\right) = 0 \) and \( A \neq 0 \) . If \( r = \operatorname{rg}A > 0 \) , we know \( A \) is equivalent to the matrix \( {J}_{r} = \left( \begin{matrix} {I}_{r} & 0 \\ 0 & 0 \end{matrix}\right) \) such that there exists \( P, Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) where \( {J}_{r} = {PAQ} \) . According to property (iii), we have \( p\left( {J}_{r}\right) = p\left( {PAQ}\right) \leq p\left( P\right) p\left( A\right) p\left( Q\right) = 0 \) , therefore \( p\left( {J}_{r}\right) = 0 \) . Property (iii) applied to the equality \( {J}_{1} = {J}_{1}{J}_{r} \) gives \( p\left( {J}_{1}\right) \leq p\left( {J}_{1}\right) p\left( {J}_{r}\right) = 0 \) , therefore \( p\left( {J}_{1}\right) = 0 \) . Let us denote by \( {D}_{i} \) the matrix whose coefficients are all zero except for the one with index \( \left( {i, i}\right) \) which equals 1. The matrix \( {D}_{i} \) has rank 1, therefore it is equivalent to the matrix \( {J}_{1} \) , and since \( p\left( {J}_{1}\right) = 0 \) , a similar reasoning to the previous one gives \( p\left( {D}_{i}\right) = 0 \) . Now, assertion (ii) implies

\[
p\left( {I}_{n}\right)  = p\left( {{D}_{1} + \cdots  + {D}_{n}}\right)  \leq  p\left( {D}_{1}\right)  + \cdots  + p\left( {D}_{n}\right)  = 0.
\]

Donc pour toute matrice \( A, p\left( A\right) = p\left( {A{I}_{n}}\right) \leq p\left( A\right) p\left( {I}_{n}\right) = 0 \) donc \( p\left( A\right) = 0 \) . Ainsi \( p = 0 \) , ce qui est contraire aux hypothèses que nous avons faites. Finalement, on a montré que \( p = 0 \) ou que \( p \) est une norme sur \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

> Therefore for any matrix \( A, p\left( A\right) = p\left( {A{I}_{n}}\right) \leq p\left( A\right) p\left( {I}_{n}\right) = 0 \) thus \( p\left( A\right) = 0 \) . Thus \( p = 0 \) , which contradicts the hypotheses we have made. Finally, we have shown that \( p = 0 \) or that \( p \) is a norm on \( {\mathcal{M}}_{n}\left( \mathbb{C}\right) \) .

Problem 12. Soit \( n \in {\mathbb{N}}^{ * } \) et \( p \) un nombre premier.

> Problem 12. Let \( n \in {\mathbb{N}}^{ * } \) and \( p \) be a prime number.

1/ Montrer que pour \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) , on a \( \operatorname{tr}{\left( A + B\right) }^{p} \equiv \operatorname{tr}{A}^{p} + \operatorname{tr}{B}^{p}\left( {\;\operatorname{mod}\;p}\right) \) .

> 1/ Show that for \( A, B \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) , we have \( \operatorname{tr}{\left( A + B\right) }^{p} \equiv \operatorname{tr}{A}^{p} + \operatorname{tr}{B}^{p}\left( {\;\operatorname{mod}\;p}\right) \) .

2/ Montrer que pour tout \( A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) , \( \operatorname{tr}{A}^{p} \equiv \operatorname{tr}A\left( {\;\operatorname{mod}\;p}\right) \) .

> 2/ Show that for all \( A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) , \( \operatorname{tr}{A}^{p} \equiv \operatorname{tr}A\left( {\;\operatorname{mod}\;p}\right) \) .

Solution. 1/ Lorsque \( A \) et \( B \) commutent, la preuve est facile à partir de la linéarité de la trace, en écrivant

> Solution. 1/ When \( A \) and \( B \) commute, the proof is easy from the linearity of the trace, by writing

\[
{\left( A + B\right) }^{p} = {A}^{p} + {B}^{p} + \mathop{\sum }\limits_{{k = 1}}^{{p - 1}}\left( \begin{array}{l} p \\  k \end{array}\right) {A}^{k}{B}^{p - k},
\]

et en remarquant que pour \( 1 \leq k \leq p - 1 \) on a \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) , et que \( \operatorname{tr}\left( {{A}^{k}{B}^{p - k}}\right) \) est un nombre entier.

> and noting that for \( 1 \leq k \leq p - 1 \) we have \( p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) , and that \( \operatorname{tr}\left( {{A}^{k}{B}^{p - k}}\right) \) is an integer.

Dans le cas général, on écrit

> In the general case, we write

\[
\operatorname{tr}{\left( A + B\right) }^{p} = \mathop{\sum }\limits_{{\left( {{M}_{1},\ldots ,{M}_{p}}\right)  \in  \{ A, B{\} }^{p}}}\operatorname{tr}\left( {{M}_{1}{M}_{2}\cdots {M}_{p}}\right)  = \mathop{\sum }\limits_{{x \in  \{ A, B{\} }^{p}}}T\left( x\right)
\]

(*)

> où pour \( x = \left( {{M}_{1},\ldots ,{M}_{p}}\right) \) , nous avons noté \( T\left( x\right) = \operatorname{tr}\left( {{M}_{1}\cdots {M}_{p}}\right) \) On regroupe les termes iden-tiques de cette expression. L’identité \( \operatorname{tr}\left( {PQ}\right) = \operatorname{tr}\left( {QP}\right) \) appliquée à \( P = {M}_{1} \) et \( Q = {M}_{2}\cdots {M}_{p} \) donne \( \operatorname{tr}\left( {{M}_{1}{M}_{2}\cdots {M}_{p}}\right) = \operatorname{tr}\left( {{M}_{2}\cdots {M}_{p}{M}_{1}}\right) \) . En notant \( \sigma \left( {{M}_{1},\ldots ,{M}_{p}}\right) = \left( {{M}_{\sigma \left( 1\right) },\ldots ,{M}_{\sigma \left( p\right) }}\right) \) pour \( \sigma \in {\mathcal{S}}_{p} \) et en notant \( G \) le sous-groupe de \( {\mathcal{S}}_{p} \) engendré par le cycle \( \gamma = \left( {1,2,\ldots , p}\right) \) , on a ainsi \( T\left( {\sigma \left( x\right) }\right) = T\left( x\right) \) pour tout \( \sigma \in G \) (on fait ainsi opérer \( G \) sur \( \{ A, B{\} }^{p} \) , voir la section 2.4 page 23). Les orbites \( {O}_{x} = \{ \sigma \left( x\right) ,\sigma \in G\} \) de \( x \in \{ A, B{\} }^{p} \) ont pour cardinal un nombre qui divise \( \left| G\right| = p \) , donc contiennent \( p \) éléments sauf lorsque \( x = \left( {A,\ldots , A}\right) \) ou \( x = \left( {B,\ldots , B}\right) \) . Soit \( \Theta \) une partie de \( \{ A, B{\} }^{p} \) contenant exactement un représentant des classes d’intransitivité (définie par \( \left. {x\mathcal{R}y \Leftrightarrow y \in {O}_{x}}\right) \) , et \( {\Theta }^{ * } = \Theta \smallsetminus \{ \left( {A,\ldots , A}\right) ,\left( {B,\ldots , B}\right) \} \) . L’égalité (*) s’écrit

where for \( x = \left( {{M}_{1},\ldots ,{M}_{p}}\right) \) , we have denoted \( T\left( x\right) = \operatorname{tr}\left( {{M}_{1}\cdots {M}_{p}}\right) \) We group the identical terms of this expression. The identity \( \operatorname{tr}\left( {PQ}\right) = \operatorname{tr}\left( {QP}\right) \) applied to \( P = {M}_{1} \) and \( Q = {M}_{2}\cdots {M}_{p} \) gives \( \operatorname{tr}\left( {{M}_{1}{M}_{2}\cdots {M}_{p}}\right) = \operatorname{tr}\left( {{M}_{2}\cdots {M}_{p}{M}_{1}}\right) \) . By denoting \( \sigma \left( {{M}_{1},\ldots ,{M}_{p}}\right) = \left( {{M}_{\sigma \left( 1\right) },\ldots ,{M}_{\sigma \left( p\right) }}\right) \) for \( \sigma \in {\mathcal{S}}_{p} \) and denoting \( G \) the subgroup of \( {\mathcal{S}}_{p} \) generated by the cycle \( \gamma = \left( {1,2,\ldots , p}\right) \) , we thus have \( T\left( {\sigma \left( x\right) }\right) = T\left( x\right) \) for all \( \sigma \in G \) (we thus let \( G \) act on \( \{ A, B{\} }^{p} \) , see section 2.4 page 23). The orbits \( {O}_{x} = \{ \sigma \left( x\right) ,\sigma \in G\} \) of \( x \in \{ A, B{\} }^{p} \) have a cardinality that divides \( \left| G\right| = p \) , and therefore contain \( p \) elements except when \( x = \left( {A,\ldots , A}\right) \) or \( x = \left( {B,\ldots , B}\right) \) . Let \( \Theta \) be a subset of \( \{ A, B{\} }^{p} \) containing exactly one representative of the intransitivity classes (defined by \( \left. {x\mathcal{R}y \Leftrightarrow y \in {O}_{x}}\right) \) , and \( {\Theta }^{ * } = \Theta \smallsetminus \{ \left( {A,\ldots , A}\right) ,\left( {B,\ldots , B}\right) \} \) . The equality (*) is written

\[
\operatorname{tr}{\left( A + B\right) }^{p} = \mathop{\sum }\limits_{{x \in  \Theta }}\mathop{\sum }\limits_{{y \in  {O}_{x}}}T\left( y\right)  = \operatorname{tr}{A}^{p} + \operatorname{tr}{B}^{p} + \mathop{\sum }\limits_{{x \in  {\Theta }^{ * }}}\left| {O}_{x}\right| T\left( x\right)  \equiv  \operatorname{tr}{A}^{p} + \operatorname{tr}{B}^{p}\;\left( {\;\operatorname{mod}\;p}\right)
\]

car pour tout \( x \in {\Theta }^{ * } \) on a \( \left| {O}_{x}\right| = p \) .

> because for all \( x \in {\Theta }^{ * } \) we have \( \left| {O}_{x}\right| = p \) .

2 / On va montrer que l’ensemble \( \Gamma = \left\{ {A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \mid \operatorname{tr}\left( {A}^{p}\right) \equiv \operatorname{tr}\left( A\right) \left( {\;\operatorname{mod}\;p}\right) }\right\} \) est égal à \( {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) . Notons \( {E}_{i, j} \) la matrice de la base canonique de \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) dont tous les coefficients sont nuls sauf celui d’indice \( \left( {i, j}\right) \) qui vaut 1 . Pour tout \( i \) on a \( {E}_{i, i}^{p} = {E}_{i, i} \) donc \( {E}_{i, i} \in \Gamma \) . Si \( i \neq j \) on a \( {E}_{i, j}^{p} = 0 \) et \( \operatorname{tr}{E}_{i, j} = 0 \) donc \( {E}_{i, j} \in \Gamma \) . Si \( A \in \Gamma \) , on a \( {kA} \in \Gamma \) pour tout \( k \in \mathbb{Z} \) , car la propriété \( {k}^{\widetilde{p}} \equiv k \; \left( {\;\operatorname{mod}\;p}\right) \) entraîne \( \operatorname{tr}{\left( kA\right) }^{p} = {k}^{p}\operatorname{tr}{A}^{p} \equiv k\operatorname{tr}{A}^{p} \equiv k\operatorname{tr}A\left( {\;\operatorname{mod}\;p}\right) \) . La question 1/ montre qu’une somme de deux éléments de \( \Gamma \) est encore dans \( \Gamma \) , et par récurrence sur le nombre de termes de la somme on en déduit que toute somme finie d’éléments de \( \Gamma \) est dans \( \Gamma \) . Toute matrice \( A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) s’écrit sous la forme \( A = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}{E}_{i, j} \) avec \( {a}_{i, j} \in \mathbb{Z} \) on en déduit donc que \( A \in \Gamma \) pour tout \( A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) .

> 2 / We will show that the set \( \Gamma = \left\{ {A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \mid \operatorname{tr}\left( {A}^{p}\right) \equiv \operatorname{tr}\left( A\right) \left( {\;\operatorname{mod}\;p}\right) }\right\} \) is equal to \( {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) . Let \( {E}_{i, j} \) be the matrix of the canonical basis of \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) where all coefficients are zero except for the one with index \( \left( {i, j}\right) \) which is 1 . For any \( i \) we have \( {E}_{i, i}^{p} = {E}_{i, i} \) therefore \( {E}_{i, i} \in \Gamma \) . If \( i \neq j \) we have \( {E}_{i, j}^{p} = 0 \) and \( \operatorname{tr}{E}_{i, j} = 0 \) therefore \( {E}_{i, j} \in \Gamma \) . If \( A \in \Gamma \) , we have \( {kA} \in \Gamma \) for any \( k \in \mathbb{Z} \) , because the property \( {k}^{\widetilde{p}} \equiv k \; \left( {\;\operatorname{mod}\;p}\right) \) implies \( \operatorname{tr}{\left( kA\right) }^{p} = {k}^{p}\operatorname{tr}{A}^{p} \equiv k\operatorname{tr}{A}^{p} \equiv k\operatorname{tr}A\left( {\;\operatorname{mod}\;p}\right) \) . Question 1/ shows that a sum of two elements of \( \Gamma \) is still in \( \Gamma \) , and by induction on the number of terms in the sum, we deduce that any finite sum of elements of \( \Gamma \) is in \( \Gamma \) . Any matrix \( A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) can be written in the form \( A = \mathop{\sum }\limits_{{i, j}}{a}_{i, j}{E}_{i, j} \) with \( {a}_{i, j} \in \mathbb{Z} \) we therefore deduce that \( A \in \Gamma \) for any \( A \in {\mathcal{M}}_{n}\left( \mathbb{Z}\right) \) .

Remarque. On peut aussi prouver 2/ en trigonalisant \( A \) (en se plaçant dans le corps des racines de son polynôme caractéristique), puis en utilisant la propriété \( {\left( {\lambda }_{1} + \cdots + {\lambda }_{n}\right) }^{p} = \; {\lambda }_{1}^{p} + \cdots + {\lambda }_{n}^{p} \) , vraie dans un corps de caractéristique \( p.1/ \) en découle ensuite facilement.

> Remark. One can also prove 2/ by trigonalizing \( A \) (by working in the splitting field of its characteristic polynomial), then by using the property \( {\left( {\lambda }_{1} + \cdots + {\lambda }_{n}\right) }^{p} = \; {\lambda }_{1}^{p} + \cdots + {\lambda }_{n}^{p} \) , true in a field of characteristic \( p.1/ \) follows easily thereafter.

Problems 13 (MATRICES DE TRANSVECTION). On se fixe un entier naturel non nul n et on note \( {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \mid \det M = 1}\right\} \) . Pour \( i, j \in \{ 1,\ldots , n\} \) , on note \( {E}_{i, j} \) la matrice de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) dont tous les coefficients sont nuls sauf celui d’indice \( \left( {i, j}\right) \) qui vaut 1 . On appelle matrices de transvection les matrices de la forme \( {I}_{n} + \lambda {E}_{i, j} \) avec \( i \neq j \) et \( \lambda \in \mathbb{K} \) , matrices de dilatation les matrices

> Problems 13 (TRANSVECTION MATRICES). Let n be a non-zero natural number and let \( {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) = \left\{ {M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \mid \det M = 1}\right\} \) . For \( i, j \in \{ 1,\ldots , n\} \) , let \( {E}_{i, j} \) be the matrix in \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) where all coefficients are zero except for the one at index \( \left( {i, j}\right) \) which is 1. Matrices of the form \( {I}_{n} + \lambda {E}_{i, j} \) with \( i \neq j \) and \( \lambda \in \mathbb{K} \) are called transvection matrices, and matrices of the form

\[
{S}_{n}\left( \alpha \right)  = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 &  \ddots  &  \ddots  & \vdots \\  \vdots &  \ddots  & 1 & 0 \\  0 & \cdots & 0 & \alpha  \end{matrix}\right)  \in  {\mathcal{M}}_{n}\left( \mathbb{K}\right) ,\;\text{ avec }\;\alpha  \in  \mathbb{K}.
\]

1/a) Montrer qu'une matrice de transvection est inversible et que son inverse est aussi une matrice de transvection.

> 1/a) Show that a transvection matrix is invertible and that its inverse is also a transvection matrix.

b) Si \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , montrer qu’il existe des matrices de transvection \( {B}_{1},\ldots ,{B}_{p},{B}_{1}^{\prime },\ldots ,{B}_{q}^{\prime } \) telles que \( A = {B}_{1}\cdots {B}_{p} \cdot {S}_{n}\left( {\det A}\right) \cdot {B}_{1}^{\prime }\cdots {B}_{q}^{\prime } \) .

> b) If \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , show that there exist transvection matrices \( {B}_{1},\ldots ,{B}_{p},{B}_{1}^{\prime },\ldots ,{B}_{q}^{\prime } \) such that \( A = {B}_{1}\cdots {B}_{p} \cdot {S}_{n}\left( {\det A}\right) \cdot {B}_{1}^{\prime }\cdots {B}_{q}^{\prime } \) .

2 / On appelle commutateur toute matrice pouvant se mettre sous la forme \( {AB}{A}^{-1}{B}^{-1} \) avec \( A, B \in {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) \) . Soit \( D \) le sous-groupe de \( {\mathcal{G\ell }}_{n}\left( \mathbb{K}\right) \) engendré par les commutateurs.

> 2 / A commutator is any matrix that can be written in the form \( {AB}{A}^{-1}{B}^{-1} \) with \( A, B \in {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) \) . Let \( D \) be the subgroup of \( {\mathcal{G\ell }}_{n}\left( \mathbb{K}\right) \) generated by the commutators.

a) Montrer que \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) si \( n \geq 3 \) .

> a) Show that \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) if \( n \geq 3 \) .

b) Montrer que \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) si \( n = 2 \) et \( \operatorname{Card}\left( \mathbb{K}\right) \geq 4 \) .

> b) Show that \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) if \( n = 2 \) and \( \operatorname{Card}\left( \mathbb{K}\right) \geq 4 \) .

3 / On suppose \( \operatorname{Card}\left( \mathbb{K}\right) \geq 4 \) et \( n \geq 2 \) . Soit \( \varphi \) un morphisme de groupe de \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) dans un groupe commutatif \( G \) .

> 3 / Assume \( \operatorname{Card}\left( \mathbb{K}\right) \geq 4 \) and \( n \geq 2 \) . Let \( \varphi \) be a group homomorphism from \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) into a commutative group \( G \) .

a) Montrer qu’il existe un morphisme de groupes \( g : {\mathbb{K}}^{ * } \rightarrow G \) tel que \( \varphi = g \circ \) det.

> a) Show that there exists a group homomorphism \( g : {\mathbb{K}}^{ * } \rightarrow G \) such that \( \varphi = g \circ \) det.

b) Si \( G = {\mathbb{K}}^{ * } \) et \( \mathbb{K} \) est fini, montrer qu’il existe \( p \in \mathbb{N} \) tel que pour tout \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , \( \varphi \left( A\right) = {\left( \det A\right) }^{p} \) (on pourra utiliser le fait que \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) est cyclique, voir la remarque de l'exercice 10 page 28).

> b) If \( G = {\mathbb{K}}^{ * } \) and \( \mathbb{K} \) is finite, show that there exists \( p \in \mathbb{N} \) such that for all \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) , \( \varphi \left( A\right) = {\left( \det A\right) }^{p} \) (one may use the fact that \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) is cyclic, see the remark in exercise 10 on page 28).

Solution. 1/a) Il suffit de remarquer que lorsque \( i \neq j,{E}_{i, j}^{2} = 0 \) . Ainsi, \( {E}_{i, j} \) est une matrice nilpotente d’indice 2, donc \( \left( {{I}_{n} + \lambda {E}_{i, j}}\right) \left( {{I}_{n} - \lambda {E}_{i, j}}\right) = {I}_{n} - {\lambda }^{2}{E}_{i, j}^{2} = {I}_{n} \) . La matrice de transvection \( {I}_{n} + \lambda {E}_{i, j} \) est donc inversible, et son inverse est la matrice de transvection \( {I}_{n} - \lambda {E}_{i, j} \) .

> Solution. 1/a) It suffices to note that when \( i \neq j,{E}_{i, j}^{2} = 0 \) . Thus, \( {E}_{i, j} \) is a nilpotent matrix of index 2, so \( \left( {{I}_{n} + \lambda {E}_{i, j}}\right) \left( {{I}_{n} - \lambda {E}_{i, j}}\right) = {I}_{n} - {\lambda }^{2}{E}_{i, j}^{2} = {I}_{n} \) . The transvection matrix \( {I}_{n} + \lambda {E}_{i, j} \) is therefore invertible, and its inverse is the transvection matrix \( {I}_{n} - \lambda {E}_{i, j} \) .

b) Soit \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Si \( i \neq j \) , on remarque que

> b) Let \( M \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . If \( i \neq j \) , we note that

(i) \( \left( {{I}_{n} + \lambda {E}_{i, j}}\right) M \) se déduit de \( M \) en ajoutant à la \( i \) -ième ligne de \( {M\lambda } \) fois la \( j \) -ième,

> (i) \( \left( {{I}_{n} + \lambda {E}_{i, j}}\right) M \) is obtained from \( M \) by adding to the \( i \) -th row \( {M\lambda } \) times the \( j \) -th,

(ii) \( M\left( {{I}_{n} + \lambda {E}_{i, j}}\right) \) se déduit de \( M \) en ajoutant à la \( j \) -ième colonne de \( {M\lambda } \) fois la \( i \) -ième.

> (ii) \( M\left( {{I}_{n} + \lambda {E}_{i, j}}\right) \) is obtained from \( M \) by adding to the \( j \) -th column \( {M\lambda } \) times the \( i \) -th.

Ceci étant, on va maintenant prouver le résultat par récurrence sur \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est évident car \( A = \left( {\det A}\right) \) . Supposons le résultat vrai au rang \( n - 1 \) et montrons le au rang \( n \) . Soit \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Comme \( A \) est inversible, la première colonne de \( A \) est non nulle. Il existe donc une matrice de transvection \( {T}_{1} = {I}_{n} + \lambda {E}_{2, j} \) telle que le coefficient d’indice \( \left( {2,1}\right) \) de \( {T}_{1}A \) soit non nul. On voit alors qu’il existe \( \mu \) tel que si \( {T}_{2} = {I}_{n} + \mu {E}_{1,2} \) , alors \( {T}_{2}{T}_{1}A \) ait son coefficient d’indice \( \left( {1,1}\right) \) égal à 1. D'après (i), on voit maintenant que l'on peut trouver des matrices de transvection \( {B}_{1},\ldots ,{B}_{p} \) (de la forme \( {I}_{n} + \lambda {E}_{i,1} \) ) telles que

> Given this, we will now prove the result by induction on \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) , it is obvious because \( A = \left( {\det A}\right) \) . Assume the result is true at rank \( n - 1 \) and show it at rank \( n \) . Let \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Since \( A \) is invertible, the first column of \( A \) is non-zero. There exists, therefore, a transvection matrix \( {T}_{1} = {I}_{n} + \lambda {E}_{2, j} \) such that the coefficient with index \( \left( {2,1}\right) \) of \( {T}_{1}A \) is non-zero. We then see that there exists \( \mu \) such that if \( {T}_{2} = {I}_{n} + \mu {E}_{1,2} \) , then \( {T}_{2}{T}_{1}A \) has its coefficient with index \( \left( {1,1}\right) \) equal to 1. According to (i), we now see that we can find transvection matrices \( {B}_{1},\ldots ,{B}_{p} \) (of the form \( {I}_{n} + \lambda {E}_{i,1} \) ) such that

\[
\left( {{B}_{1}\cdots {B}_{p}}\right) \left( {{T}_{1}{T}_{2}A}\right)  = \left( \begin{matrix} 1 &  \times  & \cdots &  \times  \\  0 &  \times  & \cdots &  \times  \\  \vdots & \vdots & & \vdots \\  0 &  \times  & \cdots &  \times   \end{matrix}\right) ,
\]

puis d’après (ii), on voit que l’on peut trouver des matrices de transvection \( {B}_{1}^{\prime },\ldots ,{B}_{q}^{\prime } \) (de la forme \( {I}_{n} + \lambda {E}_{1, j} \) ) telles que

> then according to (ii), we see that we can find transvection matrices \( {B}_{1}^{\prime },\ldots ,{B}_{q}^{\prime } \) (of the form \( {I}_{n} + \lambda {E}_{1, j} \) ) such that

\[
\left( {{B}_{1}\cdots {B}_{p}{T}_{1}{T}_{2}A}\right) \left( {{B}_{1}^{\prime }\cdots {B}_{q}^{\prime }}\right)  = {A}^{\prime }\;\text{ avec }\;{A}^{\prime } = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & B & \\  0 & & &  \end{matrix}\right) .
\]

Or det \( A = \det B \) donc d’après l’hypothèse de récurrence, il existe des matrices de transvection \( {C}_{1},\ldots ,{C}_{r} \) et \( {C}_{1}^{\prime },\ldots ,{C}_{s}^{\prime } \) de \( {\mathcal{M}}_{n - 1}\left( \mathbb{K}\right) \) telles que

> However, det \( A = \det B \) , so according to the induction hypothesis, there exist transvection matrices \( {C}_{1},\ldots ,{C}_{r} \) and \( {C}_{1}^{\prime },\ldots ,{C}_{s}^{\prime } \) of \( {\mathcal{M}}_{n - 1}\left( \mathbb{K}\right) \) such that

\[
B = {C}_{1}\cdots {C}_{r} \cdot  {S}_{n - 1}\left( {\det A}\right)  \cdot  {C}_{1}^{\prime }\cdots {C}_{s}^{\prime }.
\]

Les matrices

> The matrices

\[
{D}_{i} = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & {C}_{i} & \\  0 & & &  \end{matrix}\right) \;\text{ et }\;{D}_{j}^{\prime } = \left( \begin{matrix} 1 & 0 & \cdots & 0 \\  0 & & & \\  \vdots & & {C}_{j}^{\prime } & \\  0 & & &  \end{matrix}\right)
\]

sont des matrices de transvection de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , et on a

> are transvection matrices of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , and we have

\[
{A}^{\prime } = {D}_{1}\cdots {D}_{r} \cdot  {S}_{n}\left( {\det A}\right)  \cdot  {D}_{1}^{\prime }\cdots {D}_{s}^{\prime }
\]

et donc

> and therefore

\[
A = \left( {{T}_{2}^{-1}{T}_{1}^{-1}}\right) \left( {{B}_{p}^{-1} \cdot  {B}_{1}^{-1}}\right) \left( {{D}_{1}\cdots {D}_{r}}\right)  \cdot  {S}_{n}\left( {\det A}\right)  \cdot  \left( {{D}_{1}^{\prime }\cdots {D}_{s}^{\prime }}\right) {\left( {B}_{q}^{\prime }\right) }^{-1}\cdots {\left( {B}_{1}^{\prime }\right) }^{-1},
\]

d'où le résultat puisque l'on a vu plus haut que l'inverse d'une matrice de transvection est une matrice de transvection.

> hence the result, since we saw above that the inverse of a transvection matrix is a transvection matrix.

2/a) Tout d’abord, tout commutateur \( {AB}{A}^{-1}{B}^{-1} \) est dans \( \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) puisque \( \det \left( {{AB}{A}^{-1}{B}^{-1}}\right) = \; \left( {\det A}\right) \left( {\det B}\right) \left( {\det {A}^{-1}}\right) \left( {\det {B}^{-1}}\right) = 1 \) . On en déduit donc \( D \subset \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) .

> 2/a) First of all, every commutator \( {AB}{A}^{-1}{B}^{-1} \) is in \( \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) since \( \det \left( {{AB}{A}^{-1}{B}^{-1}}\right) = \; \left( {\det A}\right) \left( {\det B}\right) \left( {\det {A}^{-1}}\right) \left( {\det {B}^{-1}}\right) = 1 \) . We therefore deduce \( D \subset \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) .

Montrons maintenant que \( {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) \subset D \) . Soit \( M \in {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) \) . D’après la question précédente, \( M \) est le produit de matrices de transvection, et \( D \) étant un groupe, il suffit donc de montrer que les matrices de transvection sont des commutateurs pour montrer que \( M \in D \) . Soit \( T = {I}_{n} + \lambda {E}_{i, j} \) avec \( i \neq j \) une matrice de transvection. Comme \( n \geq 3 \) , il existe \( k \in \{ 1,\ldots , n\} \) tel que \( k \notin \{ i, j\} \) . On remarque alors que

> Now let us show that \( {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) \subset D \) . Let \( M \in {\mathcal{S\ell }}_{n}\left( \mathbb{K}\right) \) . According to the previous question, \( M \) is the product of transvection matrices, and since \( D \) is a group, it suffices to show that transvection matrices are commutators to show that \( M \in D \) . Let \( T = {I}_{n} + \lambda {E}_{i, j} \) with \( i \neq j \) a transvection matrix. Since \( n \geq 3 \) , there exists \( k \in \{ 1,\ldots , n\} \) such that \( k \notin \{ i, j\} \) . We then note that

\[
T = \left( {{I}_{n} + \lambda {E}_{i, k}}\right) \left( {{I}_{n} + {E}_{k, j}}\right) \left( {{I}_{n} - \lambda {E}_{i, k}}\right) \left( {{I}_{n} - {E}_{k, j}}\right)
\]

et comme \( {I}_{n} - \lambda {E}_{i, k} = {\left( {I}_{n} + \lambda {E}_{i, k}\right) }^{-1} \) et \( {I}_{n} - {E}_{k, j} = {\left( {I}_{n} + {E}_{k, j}\right) }^{-1} \) , on en déduit que \( T \) est un commutateur, d'où le résultat.

> and since \( {I}_{n} - \lambda {E}_{i, k} = {\left( {I}_{n} + \lambda {E}_{i, k}\right) }^{-1} \) and \( {I}_{n} - {E}_{k, j} = {\left( {I}_{n} + {E}_{k, j}\right) }^{-1} \) , we deduce that \( T \) is a commutator, hence the result.

b) Remarquons tout d’abord que si \( \left( {\alpha ,\beta }\right) \in \mathbb{K} \times {\mathbb{K}}^{ * } \) ,

> b) Let us first note that if \( \left( {\alpha ,\beta }\right) \in \mathbb{K} \times {\mathbb{K}}^{ * } \) ,

\[
\left( \begin{matrix} \beta & 0 \\  0 & {\beta }^{-1} \end{matrix}\right) \left( \begin{array}{ll} 1 & \alpha \\  0 & 1 \end{array}\right) \left( \begin{matrix} {\beta }^{-1} & 0 \\  0 & \beta  \end{matrix}\right) \left( \begin{matrix} 1 &  - \alpha \\  0 & 1 \end{matrix}\right)  = \left( \begin{matrix} 1 & \alpha \left( {{\beta }^{2} - 1}\right) \\  0 & 1 \end{matrix}\right) .
\]

(*)

> On choisit maintenant \( \beta \) tel que \( {\beta }^{2} - 1 \neq 0 \) et \( \beta \neq 0 \) (c’est possible car \( \operatorname{Card}\left( {\mathbb{K}}^{ * }\right) \geq 3 \) et l’équation polynomiale \( {\beta }^{2} - 1 = 0 \) a au plus deux racines dans \( \mathbb{K} \) ). La relation (*) prouve alors que toute matrice du type \( \left( \begin{array}{ll} 1 & a \\ 0 & 1 \end{array}\right) \) est un commutateur. De même, on montrerait que toute matrice du type \( \left( \begin{array}{ll} 1 & 0 \\ a & 1 \end{array}\right) \) est un commutateur. Autrement dit, toutes les matrices de transvection sont des commutateurs, et comme à la question précédente, ceci suffit pour conclure que \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) .

We now choose \( \beta \) such that \( {\beta }^{2} - 1 \neq 0 \) and \( \beta \neq 0 \) (this is possible because \( \operatorname{Card}\left( {\mathbb{K}}^{ * }\right) \geq 3 \) and the polynomial equation \( {\beta }^{2} - 1 = 0 \) has at most two roots in \( \mathbb{K} \) ). The relation (*) then proves that any matrix of the type \( \left( \begin{array}{ll} 1 & a \\ 0 & 1 \end{array}\right) \) is a commutator. Similarly, we could show that any matrix of the type \( \left( \begin{array}{ll} 1 & 0 \\ a & 1 \end{array}\right) \) is a commutator. In other words, all transvection matrices are commutators, and as in the previous question, this is sufficient to conclude that \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) .

> 3/a) Notons \( e \) l’élément neutre de \( G \) . Si \( M = {AB}{A}^{-1}{B}^{-1} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) est un commutateur, alors

3/a) Let \( e \) be the neutral element of \( G \) . If \( M = {AB}{A}^{-1}{B}^{-1} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) is a commutator, then

\[
\varphi \left( M\right)  = \varphi \left( A\right) \varphi \left( B\right) \varphi \left( {A}^{-1}\right) \varphi \left( {B}^{-1}\right)
\]

et le groupe \( G \) étant commutatif,

> and since the group \( G \) is commutative,

\[
\varphi \left( M\right)  = \varphi \left( A\right) \varphi \left( {A}^{-1}\right) \varphi \left( B\right) \varphi \left( {B}^{-1}\right)  = \varphi \left( {A{A}^{-1}}\right) \varphi \left( {B{B}^{-1}}\right)  = \varphi {\left( {I}_{n}\right) }^{2} = e.
\]

Comme \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) est engendré par les commutateurs, on en déduit que tout élément \( M \in \; \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) vérifie \( \varphi \left( M\right) = e \) .

> Since \( D = \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) is generated by the commutators, we deduce that every element \( M \in \; \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) satisfies \( \varphi \left( M\right) = e \) .

Ceci étant, soit \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Soit \( {A}^{\prime } \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) telle que \( A = {A}^{\prime }{S}_{n}\left( {\det A}\right) \) . On a det \( A = \; \det {A}^{\prime } \cdot \det \left( {{S}_{n}\left( {\det A}\right) }\right) \) donc det \( {A}^{\prime } = 1 \) car \( \det \left( {{S}_{n}\left( {\det A}\right) }\right) = \det A \neq 0 \) . Autrement dit, \( {A}^{\prime } \in \; \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) et donc \( \varphi \left( {A}^{\prime }\right) = e \) , d’où on tire \( \varphi \left( A\right) = \varphi \left( {A}^{\prime }\right) \varphi \left( {{S}_{n}\left( {\det A}\right) }\right) = \varphi \left( {{S}_{n}\left( {\det A}\right) }\right) \) . Si \( g : {\mathbb{K}}^{ * } \rightarrow \; G\;\alpha \mapsto \varphi \left\lbrack {{S}_{n}\left( \alpha \right) }\right\rbrack , g \) est un morphisme de groupe de \( {\mathbb{K}}^{ * } \) dans \( G \) , et on vient donc de montrer que \( \varphi = g \circ \) det, d’où le résultat.

> That being said, let \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Let \( {A}^{\prime } \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) be such that \( A = {A}^{\prime }{S}_{n}\left( {\det A}\right) \) . We have det \( A = \; \det {A}^{\prime } \cdot \det \left( {{S}_{n}\left( {\det A}\right) }\right) \) so det \( {A}^{\prime } = 1 \) because \( \det \left( {{S}_{n}\left( {\det A}\right) }\right) = \det A \neq 0 \) . In other words, \( {A}^{\prime } \in \; \mathcal{S}{\ell }_{n}\left( \mathbb{K}\right) \) and thus \( \varphi \left( {A}^{\prime }\right) = e \) , from which we derive \( \varphi \left( A\right) = \varphi \left( {A}^{\prime }\right) \varphi \left( {{S}_{n}\left( {\det A}\right) }\right) = \varphi \left( {{S}_{n}\left( {\det A}\right) }\right) \) . If \( g : {\mathbb{K}}^{ * } \rightarrow \; G\;\alpha \mapsto \varphi \left\lbrack {{S}_{n}\left( \alpha \right) }\right\rbrack , g \) is a group morphism from \( {\mathbb{K}}^{ * } \) to \( G \) , and we have just shown that \( \varphi = g \circ \) det, hence the result.

b) On recherche la forme de \( g \) . Le groupe \( {\mathbb{K}}^{ * } \) est cyclique donc il existe \( a \in {\mathbb{K}}^{ * } \) tel que \( {\mathbb{K}}^{ * } = \langle a\rangle \) . En particulier, il existe \( p \in \mathbb{N} \) tel que \( g\left( a\right) = {a}^{p} \) . Donc pour tout \( x \in {\mathbb{K}}^{ * }, x = {a}^{q} \) , on a

> b) We are looking for the form of \( g \) . The group \( {\mathbb{K}}^{ * } \) is cyclic so there exists \( a \in {\mathbb{K}}^{ * } \) such that \( {\mathbb{K}}^{ * } = \langle a\rangle \) . In particular, there exists \( p \in \mathbb{N} \) such that \( g\left( a\right) = {a}^{p} \) . So for all \( x \in {\mathbb{K}}^{ * }, x = {a}^{q} \) , we have

\[
g\left( x\right)  = g\left( {a}^{q}\right)  = g{\left( a\right) }^{q} = {\left( {a}^{p}\right) }^{q} = {\left( {a}^{q}\right) }^{p} = {x}^{p},
\]

et donc pour tout \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) ,\varphi \left( A\right) = g\left( {\det A}\right) = {\left( \det A\right) }^{p} \) .

> and thus for all \( A \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) ,\varphi \left( A\right) = g\left( {\det A}\right) = {\left( \det A\right) }^{p} \) .

Problem 14. a) Soient \( A \) et \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) deux matrices semblables sur \( \mathbb{C} \) (i.e. il existe \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que \( A = {P}^{-1}{BP} \) ). Montrer que \( A \) et \( B \) sont semblables sur \( \mathbb{R} \) (i.e. il existe \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) , A = {Q}^{-1}{BQ}) \) .

> Problem 14. a) Let \( A \) and \( B \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) be two similar matrices over \( \mathbb{C} \) (i.e. there exists \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) such that \( A = {P}^{-1}{BP} \) ). Show that \( A \) and \( B \) are similar over \( \mathbb{R} \) (i.e. there exists \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{R}\right) , A = {Q}^{-1}{BQ}) \) .

b) Plus généralement, soit \( \mathbb{K} \) un corps infini et \( \mathbb{L} \) une extension de \( \mathbb{K} \) . Soient \( A \) et \( B \in \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) deux matrices semblables sur \( \mathbb{L} \) . Montrer que \( A \) et \( B \) sont semblables sur \( \mathbb{K} \) .

> b) More generally, let \( \mathbb{K} \) be an infinite field and \( \mathbb{L} \) an extension of \( \mathbb{K} \) . Let \( A \) and \( B \in \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) be two similar matrices over \( \mathbb{L} \) . Show that \( A \) and \( B \) are similar over \( \mathbb{K} \) .

Solution. a) Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) telle que \( A = {P}^{-1}{BP} \) , ou encore \( {PA} = {BP} \) . Écrivons \( P = {P}_{1} + i{P}_{2} \) avec \( {P}_{1},{P}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) . En égalant parties réelles et imaginaires, il vient \( {P}_{1}A = B{P}_{1} \) et \( {P}_{2}A = \; B{P}_{2} \) . (*) On définit le polynôme \( \varphi \left( X\right) = \det \left( {{P}_{1} + X{P}_{2}}\right) \in \mathbb{R}\left\lbrack X\right\rbrack \) . Comme \( \varphi \left( i\right) = \det P \neq 0 \) , \( \varphi \) est non nul et donc n’a qu’un nombre fini de racines, de sorte qu’il existe \( x \in \mathbb{R} \) tel que \( \varphi \left( x\right) \neq 0 \) , c’est-à-dire que \( Q = {P}_{1} + x{P}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) est inversible. De (*) on tire \( {QA} = {BQ} \) donc \( A = {Q}^{-1}{BQ} \) , d’où le résultat.

> Solution. a) Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{C}\right) \) be such that \( A = {P}^{-1}{BP} \), or \( {PA} = {BP} \). Let us write \( P = {P}_{1} + i{P}_{2} \) with \( {P}_{1},{P}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \). Equating real and imaginary parts, we get \( {P}_{1}A = B{P}_{1} \) and \( {P}_{2}A = \; B{P}_{2} \). (*) We define the polynomial \( \varphi \left( X\right) = \det \left( {{P}_{1} + X{P}_{2}}\right) \in \mathbb{R}\left\lbrack X\right\rbrack \). Since \( \varphi \left( i\right) = \det P \neq 0 \), \( \varphi \) is non-zero and thus has only a finite number of roots, so there exists \( x \in \mathbb{R} \) such that \( \varphi \left( x\right) \neq 0 \), meaning \( Q = {P}_{1} + x{P}_{2} \in {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) is invertible. From (*) we derive \( {QA} = {BQ} \) so \( A = {Q}^{-1}{BQ} \), hence the result.

b) On procède un peu comme précédemment. Soit \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{L}\right) \) tel que \( A = {P}^{-1}{BP} \) , ou encore \( {PA} = {BP} \) . On écrit \( P = {\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \) . Le corps \( \mathbb{L} \) est un \( \mathbb{K} \) -e.v. Soit \( E = \operatorname{Vect}{\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \) , s.e.v de \( \mathbb{L} \) de dimension finie sur \( \mathbb{K} \) . Soit \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) une base de \( E \) . Pour tout \( \left( {i, j}\right) \) on peut écrire \( {p}_{i, j} = \mathop{\sum }\limits_{{k = 1}}^{p}{p}_{i, j, k}{e}_{k} \) avec les \( {p}_{i, j, k} \in \mathbb{K} \) . Pour tout \( k \) , on note \( {P}_{k} = {\left( {p}_{i, j, k}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , de sorte que \( P = {e}_{1}{P}_{1} + \cdots + {e}_{p}{P}_{p} \) . Comme \( {PA} = {BP} \) , on a pour tout \( k,1 \leq k \leq p,{P}_{k}A = \; B{P}_{k}\;\left( {* * }\right) \) . Posons \( F\left( {{X}_{1},\ldots ,{X}_{p}}\right) = \det \left( {{X}_{1}{P}_{1} + \cdots + {X}_{p}{P}_{p}}\right) \in \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{p}}\right\rbrack \) . On a \( F \neq 0 \) car \( F\left( {{e}_{1},\ldots ,{e}_{p}}\right) = \det \left( P\right) \neq 0 \) . Or \( \mathbb{K} \) est un corps infini, donc \( F \) ne s’annule pas sur \( {\mathbb{K}}^{p} \) , et donc il existe \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \in {\mathbb{K}}^{p} \) tel que \( F\left( {{x}_{1},\ldots ,{x}_{p}}\right) \neq 0 \) . Si \( Q = {x}_{1}{P}_{1} + \cdots {x}_{p}{P}_{p} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on a donc \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) et d’après \( \left( {* * }\right) ,{QA} = {BQ} \) donc \( A = {Q}^{-1}{BQ} \) , d’où le résultat.

> b) We proceed somewhat as before. Let \( P \in \mathcal{G}{\ell }_{n}\left( \mathbb{L}\right) \) be such that \( A = {P}^{-1}{BP} \), or \( {PA} = {BP} \). We write \( P = {\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \). The field \( \mathbb{L} \) is an \( \mathbb{K} \)-v.s. Let \( E = \operatorname{Vect}{\left( {p}_{i, j}\right) }_{1 \leq i, j \leq n} \) be a f.d. subspace of \( \mathbb{L} \) over \( \mathbb{K} \). Let \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) be a basis of \( E \). For any \( \left( {i, j}\right) \), we can write \( {p}_{i, j} = \mathop{\sum }\limits_{{k = 1}}^{p}{p}_{i, j, k}{e}_{k} \) with the \( {p}_{i, j, k} \in \mathbb{K} \). For any \( k \), we denote \( {P}_{k} = {\left( {p}_{i, j, k}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), so that \( P = {e}_{1}{P}_{1} + \cdots + {e}_{p}{P}_{p} \). As \( {PA} = {BP} \), we have for any \( k,1 \leq k \leq p,{P}_{k}A = \; B{P}_{k}\;\left( {* * }\right) \). Let \( F\left( {{X}_{1},\ldots ,{X}_{p}}\right) = \det \left( {{X}_{1}{P}_{1} + \cdots + {X}_{p}{P}_{p}}\right) \in \mathbb{K}\left\lbrack {{X}_{1},\ldots ,{X}_{p}}\right\rbrack \). We have \( F \neq 0 \) because \( F\left( {{e}_{1},\ldots ,{e}_{p}}\right) = \det \left( P\right) \neq 0 \). However, \( \mathbb{K} \) is an infinite field, so \( F \) does not vanish on \( {\mathbb{K}}^{p} \), and thus there exists \( \left( {{x}_{1},\ldots ,{x}_{p}}\right) \in {\mathbb{K}}^{p} \) such that \( F\left( {{x}_{1},\ldots ,{x}_{p}}\right) \neq 0 \). If \( Q = {x}_{1}{P}_{1} + \cdots {x}_{p}{P}_{p} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), we then have \( Q \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) and according to \( \left( {* * }\right) ,{QA} = {BQ} \), thus \( A = {Q}^{-1}{BQ} \), hence the result.

Remarque. Le résultat reste vrai lorsque \( \mathbb{K} \) est un corps fini (voir l’annexe B, page 400).

> Remark. The result remains true when \( \mathbb{K} \) is a finite field (see Appendix B, page 400).

Problem 15 (SPLINES CUBIQUES). Soit \( I = \left\lbrack {a, b}\right\rbrack \) un segment de \( \mathbb{R} \) avec \( a < b, n \in \mathbb{N} \) , \( n \geq 2 \) et \( a = {x}_{0} < {x}_{1} < \ldots < {x}_{n} = b \) une subdivision de \( \left\lbrack {a, b}\right\rbrack \) . Une fonction \( s : I \rightarrow \mathbb{R} \) est appelée spline cubique si elle est de classe \( {\mathcal{C}}^{2} \) sur \( I \) et si pour tout \( i\left( {1 \leq i \leq n}\right) \) , la restriction de \( s \) à \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) est une fonction polynôme de degré \( \leq 3 \) .

> Problem 15 (CUBIC SPLINES). Let \( I = \left\lbrack {a, b}\right\rbrack \) be a segment of \( \mathbb{R} \) with \( a < b, n \in \mathbb{N} \) , \( n \geq 2 \) and \( a = {x}_{0} < {x}_{1} < \ldots < {x}_{n} = b \) a subdivision of \( \left\lbrack {a, b}\right\rbrack \) . A function \( s : I \rightarrow \mathbb{R} \) is called a cubic spline if it is of class \( {\mathcal{C}}^{2} \) on \( I \) and if for all \( i\left( {1 \leq i \leq n}\right) \) , the restriction of \( s \) to \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) is a polynomial function of degree \( \leq 3 \) .

a) Soit \( {a}_{0} < {a}_{1} \) deux réels, et \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \in \mathbb{R} \) . Montrer l’existence et l’unicité d’un polynôme \( H \) de degré \( \leq 3 \) tel que \( H\left( {a}_{0}\right) = {z}_{0},{H}^{\prime }\left( {a}_{0}\right) = {q}_{0}, H\left( {a}_{1}\right) = {z}_{1},{H}^{\prime }\left( {a}_{1}\right) = {q}_{1} \) , et expliciter la valeur de \( {H}^{\prime \prime }\left( {a}_{0}\right) \) et \( {H}^{\prime \prime }\left( {a}_{1}\right) \) en fonction de \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \) et \( {a}_{1} - {a}_{0} \) .

> a) Let \( {a}_{0} < {a}_{1} \) be two real numbers, and \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \in \mathbb{R} \) . Show the existence and uniqueness of a polynomial \( H \) of degree \( \leq 3 \) such that \( H\left( {a}_{0}\right) = {z}_{0},{H}^{\prime }\left( {a}_{0}\right) = {q}_{0}, H\left( {a}_{1}\right) = {z}_{1},{H}^{\prime }\left( {a}_{1}\right) = {q}_{1} \) , and express the value of \( {H}^{\prime \prime }\left( {a}_{0}\right) \) and \( {H}^{\prime \prime }\left( {a}_{1}\right) \) in terms of \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \) and \( {a}_{1} - {a}_{0} \) .

b) On fixe dorénavant des nombres réels \( {\left( {y}_{i}\right) }_{0 \leq i \leq n} \) et \( {p}_{0},{p}_{n} \) . On cherche une spline cubique vérifiant les trois conditions

> b) We now fix real numbers \( {\left( {y}_{i}\right) }_{0 \leq i \leq n} \) and \( {p}_{0},{p}_{n} \) . We are looking for a cubic spline satisfying the three conditions

\[
\text{ (i) }\forall i \in  \{ 0,1,\ldots , n\} ,\;s\left( {x}_{i}\right)  = {y}_{i}\;\text{ (ii) }{s}^{\prime }\left( a\right)  = {p}_{0}\;\text{ (iii) }{s}^{\prime }\left( b\right)  = {p}_{n}\text{ . }
\]

(*)

> Soit \( s \) une fonction \( {\mathcal{C}}^{1} \) sur \( I \) vérifiant (*), et telle que pour \( i = 1,\ldots , n \) , la restriction \( {s}_{i} \) de \( s \) à \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) soit polynomiale de degré \( \leq 3 \) . Exprimer sous forme d’un système linéaire une condition nécessaire et suffisante sur les inconnues \( {p}_{i} = {s}^{\prime }\left( {x}_{i}\right) \left( {1 \leq i \leq n - 1}\right) \) pour que \( s \) soit une spline cubique.

Let \( s \) be a function \( {\mathcal{C}}^{1} \) on \( I \) satisfying (*), and such that for \( i = 1,\ldots , n \) , the restriction \( {s}_{i} \) of \( s \) to \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) is a polynomial of degree \( \leq 3 \) . Express as a linear system a necessary and sufficient condition on the unknowns \( {p}_{i} = {s}^{\prime }\left( {x}_{i}\right) \left( {1 \leq i \leq n - 1}\right) \) for \( s \) to be a cubic spline.

> c) Montrer que ce système linéaire est inversible et en déduire l'existence et l'unicité d'une spline cubique \( s \) vérifiant (*) (une telle spline est appelée spline scellée).

c) Show that this linear system is invertible and deduce the existence and uniqueness of a cubic spline \( s \) satisfying (*) (such a spline is called a clamped spline).

> d) (Théorème de Holladay). On note \( {H}_{2} \) l’espace vectoriel des fonctions de classe \( {\mathcal{C}}^{1} \) sur \( I \) et dont la restriction à chaque intervalle \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \left( {1 \leq i \leq n}\right) \) est de classe \( {\mathcal{C}}^{2} \) . On note \( {H}_{2}^{ * } \) l’ensemble des fonctions de \( {H}_{2} \) vérifiant les conditions (*). Montrer qu’il existe une unique fonction \( s \in {H}_{2}^{ * } \) vérifiant

d) (Holladay's Theorem). Let \( {H}_{2} \) be the vector space of functions of class \( {\mathcal{C}}^{1} \) on \( I \) whose restriction to each interval \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \left( {1 \leq i \leq n}\right) \) is of class \( {\mathcal{C}}^{2} \) . Let \( {H}_{2}^{ * } \) be the set of functions in \( {H}_{2} \) satisfying the conditions (*). Show that there exists a unique function \( s \in {H}_{2}^{ * } \) satisfying

\[
{\int }_{a}^{b}{\left( {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = \mathop{\inf }\limits_{{f \in  {H}_{2}^{ * }}}{\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) \right) }^{2}{dx}
\]

et que cette fonction \( s \) est la spline scellée vérifiant les conditions \( \left( *\right) \) . (Indication : si \( s \) est la spline scellée vérifiant \( \left( *\right) \) , montrer que \( {\int }_{a}^{b}{s}^{\prime \prime }\left( {{f}^{\prime \prime } - {s}^{\prime \prime }}\right) = 0 \) pour tout \( f \in {H}_{2}^{ * } \) .)

> and that this function \( s \) is the clamped spline satisfying the conditions \( \left( *\right) \) . (Hint: if \( s \) is the clamped spline satisfying \( \left( *\right) \) , show that \( {\int }_{a}^{b}{s}^{\prime \prime }\left( {{f}^{\prime \prime } - {s}^{\prime \prime }}\right) = 0 \) for all \( f \in {H}_{2}^{ * } \) .)

---

Solution. a) L’existence et l’unicité du polynôme \( H \) de degré \( \leq 3 \) vérifiant ces conditions d’interpolation est une conséquence du résultat de l'exercice 7 page 70. Nous allons retrouver ce résultat directement, et calculer explicitement \( {H}^{\prime \prime }\left( {a}_{0}\right) \) et \( {H}^{\prime \prime }\left( {a}_{1}\right) \) en fonction de \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \) .

> Solution. a) The existence and uniqueness of the polynomial \( H \) of degree \( \leq 3 \) satisfying these interpolation conditions is a consequence of the result of exercise 7 on page 70. We will derive this result directly, and explicitly calculate \( {H}^{\prime \prime }\left( {a}_{0}\right) \) and \( {H}^{\prime \prime }\left( {a}_{1}\right) \) in terms of \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \) .

Notons \( {m}_{0} = {H}^{\prime \prime }\left( {a}_{0}\right) \) et \( {m}_{1} = {H}^{\prime \prime }\left( {a}_{1}\right) \) . Comme \( H \) est polynomiale de degré \( \leq 3,{H}^{\prime \prime } \) est une fonction affine, donc par interpolation linéaire on obtient

> Let \( {m}_{0} = {H}^{\prime \prime }\left( {a}_{0}\right) \) and \( {m}_{1} = {H}^{\prime \prime }\left( {a}_{1}\right) \) . Since \( H \) is a polynomial of degree \( \leq 3,{H}^{\prime \prime } \) is an affine function, then by linear interpolation we obtain

\[
{H}^{\prime \prime }\left( x\right)  = \frac{{m}_{0}}{h}\left( {{a}_{1} - x}\right)  + \frac{{m}_{1}}{h}\left( {x - {a}_{0}}\right) ,\;h = {a}_{1} - {a}_{0}.
\]

Une double intégration de la formule précédente entraîne, après une manipulation simple, l'existence de \( \alpha ,\beta \in \mathbb{R} \) tels que

> A double integration of the previous formula leads, after simple manipulation, to the existence of \( \alpha ,\beta \in \mathbb{R} \) such that

\[
H\left( x\right)  = \frac{{m}_{0}}{6h}{\left( {a}_{1} - x\right) }^{3} + \frac{{m}_{1}}{6h}{\left( x - {a}_{0}\right) }^{3} + \alpha \left( {{a}_{1} - x}\right)  + \beta \left( {x - {a}_{0}}\right) .
\]

Les égalités \( H\left( {a}_{0}\right) = {z}_{0} \) et \( H\left( {a}_{1}\right) = {z}_{1} \) donnent les égalités \( {z}_{0} = \frac{{m}_{0}}{6}{h}^{2} + {\alpha h} \) et \( {z}_{1} = \frac{{m}_{1}}{6}{h}^{2} + {\beta h} \) . On en déduit les valeurs de \( \alpha \) et \( \beta \) et après substitution on obtient

> The equalities \( H\left( {a}_{0}\right) = {z}_{0} \) and \( H\left( {a}_{1}\right) = {z}_{1} \) yield the equalities \( {z}_{0} = \frac{{m}_{0}}{6}{h}^{2} + {\alpha h} \) and \( {z}_{1} = \frac{{m}_{1}}{6}{h}^{2} + {\beta h} \) . We deduce the values of \( \alpha \) and \( \beta \) and after substitution we obtain

\[
H\left( x\right)  = \frac{{m}_{0}}{6h}{\left( {a}_{1} - x\right) }^{3} + \frac{{m}_{1}}{6h}{\left( x - {a}_{0}\right) }^{3} + \left( {\frac{{z}_{0}}{h} - \frac{{m}_{0}h}{6}}\right) \left( {{a}_{1} - x}\right)  + \left( {\frac{{z}_{1}}{h} - \frac{{m}_{1}h}{6}}\right) \left( {x - {a}_{0}}\right) .
\]

(**)

> En dérivant cette expression, et en substituant \( x \) par \( {a}_{0} \) et \( {a}_{1} \) , on obtient

By differentiating this expression, and substituting \( x \) with \( {a}_{0} \) and \( {a}_{1} \) , we obtain

\[
{q}_{0} = {H}^{\prime }\left( {a}_{0}\right)  =  - \frac{{m}_{0}}{3}h - \frac{{m}_{1}}{6}h + \frac{{z}_{1} - {z}_{0}}{h},\;{q}_{1} = {H}^{\prime }\left( {a}_{1}\right)  = \frac{{m}_{1}}{3}h + \frac{{m}_{0}}{6}h + \frac{{z}_{1} - {z}_{0}}{h}.
\]

Ceci permet d’obtenir directement les valeurs \( {m}_{0} \) et \( {m}_{1} \) sous la forme

> This allows us to directly obtain the values \( {m}_{0} \) and \( {m}_{1} \) in the form

\[
\frac{{H}^{\prime \prime }\left( {a}_{0}\right) }{2} = \frac{{m}_{0}}{2} =  - \frac{2{q}_{0} + {q}_{1}}{h} + 3\frac{{z}_{1} - {z}_{0}}{{h}^{2}},\;\frac{{H}^{\prime \prime }\left( {a}_{1}\right) }{2} = \frac{{m}_{1}}{2} = \frac{{q}_{0} + 2{q}_{1}}{h} - 3\frac{{z}_{1} - {z}_{0}}{{h}^{2}}.
\]

\( \left( {* * * }\right) \)

> Ainsi, partant de \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \) il y a une et une seule valeur possible pour \( {m}_{0} \) et \( {m}_{1} \) , donc on a bien l’existence et l’unicité de \( H \) d’après la formule \( \left( {* * }\right) \) .

Thus, starting from \( {z}_{0},{z}_{1},{q}_{0},{q}_{1} \) there is one and only one possible value for \( {m}_{0} \) and \( {m}_{1} \) , so we indeed have the existence and uniqueness of \( H \) according to formula \( \left( {* * }\right) \) .

> b) Soit \( {p}_{i} = {s}^{\prime }\left( {x}_{i}\right) \) . La restriction \( {s}_{i} \) de \( s \) à \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) est un polynôme de degré \( \leq 3 \) vérifiant \( {s}_{i}\left( {x}_{i - 1}\right) = {y}_{i - 1},{s}_{i}^{\prime }\left( {x}_{i - 1}\right) = {p}_{i - 1},{s}_{i}\left( {x}_{i}\right) = {y}_{i},{s}_{i}^{\prime }\left( {x}_{i}\right) = {p}_{i} \) . D’après le résultat de la question précédente, \( {s}_{i} \) existe et est unique, ce qui définit \( s \) de manière unique dès que \( s \) vérifie (*) et \( {s}^{\prime }\left( {x}_{i}\right) = {p}_{i} \) pour \( i = 1,\ldots , n - 1 \) . La seule condition manquante pour que \( s \) soit une spline cubique est qu’elle soit de classe \( {\mathcal{C}}^{2} \) . Ceci est équivalent à la condition \( {s}_{i}^{\prime \prime }\left( {x}_{i}\right) = {s}_{i + 1}^{\prime \prime }\left( {x}_{i}\right) \) pour \( 1 \leq i \leq n - 1 \) , ce qui d’après la formule (***) s’écrit aussi

b) Let \( {p}_{i} = {s}^{\prime }\left( {x}_{i}\right) \) . The restriction \( {s}_{i} \) of \( s \) to \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) is a polynomial of degree \( \leq 3 \) satisfying \( {s}_{i}\left( {x}_{i - 1}\right) = {y}_{i - 1},{s}_{i}^{\prime }\left( {x}_{i - 1}\right) = {p}_{i - 1},{s}_{i}\left( {x}_{i}\right) = {y}_{i},{s}_{i}^{\prime }\left( {x}_{i}\right) = {p}_{i} \) . According to the result of the previous question, \( {s}_{i} \) exists and is unique, which uniquely defines \( s \) as soon as \( s \) satisfies (*) and \( {s}^{\prime }\left( {x}_{i}\right) = {p}_{i} \) for \( i = 1,\ldots , n - 1 \) . The only missing condition for \( s \) to be a cubic spline is that it be of class \( {\mathcal{C}}^{2} \) . This is equivalent to the condition \( {s}_{i}^{\prime \prime }\left( {x}_{i}\right) = {s}_{i + 1}^{\prime \prime }\left( {x}_{i}\right) \) for \( 1 \leq i \leq n - 1 \) , which according to formula (***) is also written as

\[
\frac{{p}_{i - 1} + 2{p}_{i}}{{h}_{i - 1}} - 3\frac{{y}_{i} - {y}_{i - 1}}{{h}_{i - 1}^{2}} =  - \frac{2{p}_{i} + {p}_{i + 1}}{{h}_{i}} + 3\frac{{y}_{i + 1} - {y}_{i}}{{h}_{i}^{2}},\;{h}_{i - 1} = {x}_{i} - {x}_{i - 1},\;{h}_{i} = {x}_{i + 1} - {x}_{i}.
\]

---

En résumé, \( s \) est une spline cubique si et seulement si le système linéaire suivant est satisfait :

> In summary, \( s \) is a cubic spline if and only if the following linear system is satisfied:

\[
\forall i \in  \{ 1,\ldots , n - 1\} ,\;\frac{{p}_{i - 1}}{{h}_{i - 1}} + 2{p}_{i}\left( {\frac{1}{{h}_{i - 1}} + \frac{1}{{h}_{i}}}\right)  + \frac{{p}_{i + 1}}{{h}_{i}} = {c}_{i},\;{c}_{i} = 3\frac{{y}_{i} - {y}_{i - 1}}{{h}_{i - 1}^{2}} + 3\frac{{y}_{i + 1} - {y}_{i}}{{h}_{i}^{2}}.
\]

c) En posant

> c) By setting

\[
{\ell }_{i} = \frac{1}{{h}_{i}}\;\text{ et }\;{d}_{1} = {c}_{1} - \frac{{p}_{0}}{{h}_{0}},\;{d}_{2} = {c}_{2},\;\ldots ,\;{d}_{n - 2} = {c}_{n - 2},\;{d}_{n - 1} = {c}_{n - 1} - \frac{{p}_{n}}{{h}_{n - 1}}
\]

le système linéaire précédent s’écrit aussi en fonction des inconnues \( {p}_{1},\ldots ,{p}_{n - 1} \) sous la forme

> the previous linear system can also be written in terms of the unknowns \( {p}_{1},\ldots ,{p}_{n - 1} \) in the form

\[
\left( \begin{matrix} 2\left( {{\ell }_{0} + {\ell }_{1}}\right) & {\ell }_{1} & 0 & \cdots & 0 \\  {\ell }_{1} & 2\left( {{\ell }_{1} + {\ell }_{2}}\right) & {\ell }_{2} &  \ddots  & \vdots \\  0 & {\ell }_{2} &  \ddots  &  \ddots  & 0 \\  \vdots &  \ddots  &  \ddots  &  \ddots  & {\ell }_{n - 2} \\  0 & \cdots & 0 & {\ell }_{n - 2} & 2\left( {{\ell }_{n - 2} + {\ell }_{n - 1}}\right)  \end{matrix}\right) \left( \begin{matrix} {p}_{1} \\  {p}_{2} \\  \vdots \\  \vdots \\  {p}_{n - 1} \end{matrix}\right)  = \left( \begin{matrix} {d}_{1} \\  {d}_{2} \\  \vdots \\  \vdots \\  {d}_{n - 1} \end{matrix}\right) .
\]

Notons \( M \) la matrice carrée d’ordre \( n - 1 \) du membre de gauche de cette égalité. Si \( {MX} = 0 \) avec \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n - 1} \end{matrix}\right) \) , alors si \( k \) est tel que \( \left| {x}_{k}\right| = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) , la ligne \( k \) du système \( {MX} = 0 \) s’écrit \( {\ell }_{k - 1}{x}_{k - 1} + 2\left( {{\ell }_{k - 1} + {\ell }_{k}}\right) {x}_{k} + {\ell }_{k}{x}_{k + 1} = 0 \) (où on pose \( {x}_{0} = {x}_{n} = 0 \) ). Ceci entraîne \( 2\left( {{\ell }_{k - 1} + {\ell }_{k}}\right) {x}_{k} = \; - {\ell }_{k - 1}{x}_{k - 1} - {\ell }_{k}{x}_{k + 1} \) donc \( 2\left( {{\ell }_{k - 1} + {\ell }_{k}}\right) \left| {x}_{k}\right| \leq {\ell }_{k - 1}\left| {x}_{k - 1}\right| + {\ell }_{k}\left| {x}_{k + 1}\right| \leq \left( {{\ell }_{k - 1} + {\ell }_{k}}\right) \left| {x}_{k}\right| \) ce qui \( {n}^{\text{ ’ est }} \) possible que si \( {x}_{k} = 0 \) (nous venons d’utiliser la propriété que \( M \) est diagonalement dominante, voir l’exercice 1 page 129). On en déduit que \( X = 0 \) , donc que \( M \) est inversible, ce qui prouve bien l’existence et l’unicité des inconnues \( {\left( {p}_{i}\right) }_{1 \leq i \leq n - 1} \) . D’après le résultat de la question précédente, ceci montre l'existence et l'unicité d'une spline cubique vérifiant les conditions \( \left( *\right) \) .

> Let \( M \) be the square matrix of order \( n - 1 \) on the left-hand side of this equality. If \( {MX} = 0 \) with \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n - 1} \end{matrix}\right) \) , then if \( k \) is such that \( \left| {x}_{k}\right| = \mathop{\sup }\limits_{i}\left| {x}_{i}\right| \) , the \( k \)-th row of the system \( {MX} = 0 \) is written as \( {\ell }_{k - 1}{x}_{k - 1} + 2\left( {{\ell }_{k - 1} + {\ell }_{k}}\right) {x}_{k} + {\ell }_{k}{x}_{k + 1} = 0 \) (where we set \( {x}_{0} = {x}_{n} = 0 \) ). This implies \( 2\left( {{\ell }_{k - 1} + {\ell }_{k}}\right) {x}_{k} = \; - {\ell }_{k - 1}{x}_{k - 1} - {\ell }_{k}{x}_{k + 1} \) therefore \( 2\left( {{\ell }_{k - 1} + {\ell }_{k}}\right) \left| {x}_{k}\right| \leq {\ell }_{k - 1}\left| {x}_{k - 1}\right| + {\ell }_{k}\left| {x}_{k + 1}\right| \leq \left( {{\ell }_{k - 1} + {\ell }_{k}}\right) \left| {x}_{k}\right| \) which \( {n}^{\text{ ’ est }} \) possible only if \( {x}_{k} = 0 \) (we have just used the property that \( M \) is diagonally dominant, see exercise 1 page 129). We deduce that \( X = 0 \) , therefore that \( M \) is invertible, which proves the existence and uniqueness of the unknowns \( {\left( {p}_{i}\right) }_{1 \leq i \leq n - 1} \) . According to the result of the previous question, this shows the existence and uniqueness of a cubic spline satisfying the conditions \( \left( *\right) \) .

d) Soit \( s \) la spline scellée vérifiant les conditions (*). Soit \( f \in {H}_{2}^{ * } \) . On note \( u = f - s \) . On a

> d) Let \( s \) be the sealed spline satisfying the conditions (*). Let \( f \in {H}_{2}^{ * } \) . We denote \( u = f - s \) . We have

\[
{\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = {\int }_{a}^{b}{\left( {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} + 2{\int }_{a}^{b}{s}^{\prime \prime }\left( x\right) {u}^{\prime \prime }\left( x\right) {dx} + {\int }_{a}^{b}{\left( {u}^{\prime \prime }\left( x\right) \right) }^{2}{dx}.
\]

\( \left( {* * * * }\right) \)

> Sur \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) , la fonction \( s \) est égale à la fonction polynomiale \( {s}_{i} \) , sa dérivée troisième y est donc bien définie, et on peut écrire l'intégration par partie

On \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) , the function \( s \) is equal to the polynomial function \( {s}_{i} \) , its third derivative is therefore well-defined there, and we can write the integration by parts

\[
{\int }_{{x}_{i - 1}}^{{x}_{i}}{s}^{\prime \prime }\left( x\right) {u}^{\prime \prime }\left( x\right) {dx} = {\left\lbrack  {s}^{\prime \prime }\left( x\right) {u}^{\prime }\left( x\right) \right\rbrack  }_{{x}_{i - 1}}^{{x}_{i}} - {\int }_{{x}_{i - 1}}^{{x}_{i}}{s}^{\prime \prime \prime }\left( x\right) {u}^{\prime }\left( x\right) {dx}.
\]

Comme \( s = {s}_{i} \) est polynomiale de degré 3 sur \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) , la fonction \( {s}^{\prime \prime \prime } \) est constante sur cet intervalle. On peut donc écrire

> Since \( s = {s}_{i} \) is a polynomial of degree 3 on \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) , the function \( {s}^{\prime \prime \prime } \) is constant on this interval. We can therefore write

\[
{\int }_{{x}_{i - 1}}^{{x}_{i}}{s}^{\prime \prime }\left( x\right) {u}^{\prime \prime }\left( x\right) {dx} = {\left\lbrack  {s}^{\prime \prime }\left( x\right) {u}^{\prime }\left( x\right) \right\rbrack  }_{{x}_{i - 1}}^{{x}_{i}} - {s}_{i}^{\prime \prime \prime }\left( {x}_{i}\right) {\int }_{{x}_{i - 1}}^{{x}_{i}}{u}^{\prime }\left( x\right) {dx} = {\left\lbrack  {s}^{\prime \prime }\left( x\right) {u}^{\prime }\left( x\right) \right\rbrack  }_{{x}_{i - 1}}^{{x}_{i}},
\]

car comme \( f \) et \( s \) vérifient les conditions \( \left( *\right) \) , la fonction \( u = f - s \) s’annule aux points \( {x}_{i} \) donc \( {\int }_{{x}_{i - 1}}^{{x}_{i}}{u}^{\prime }\left( x\right) {dx} = u\left( {x}_{i}\right) - u\left( {x}_{i - 1}\right) = 0 \) . En sommant cette relation sur \( i \) , on en déduit

> because as \( f \) and \( s \) satisfy the conditions \( \left( *\right) \) , the function \( u = f - s \) vanishes at the points \( {x}_{i} \) therefore \( {\int }_{{x}_{i - 1}}^{{x}_{i}}{u}^{\prime }\left( x\right) {dx} = u\left( {x}_{i}\right) - u\left( {x}_{i - 1}\right) = 0 \) . By summing this relation over \( i \) , we deduce

\[
{\int }_{a}^{b}{s}^{\prime \prime }\left( x\right) {u}^{\prime \prime }\left( x\right) {dx} = {\left\lbrack  {s}^{\prime \prime }\left( x\right) {u}^{\prime }\left( x\right) \right\rbrack  }_{a}^{b} = {s}^{\prime \prime }\left( b\right) {u}^{\prime }\left( b\right)  - {s}^{\prime \prime }\left( a\right) {u}^{\prime }\left( a\right)  = 0
\]

car comme \( f \) et \( s \) vérifie la condition (ii) et (iii) de \( \left( *\right) \) , on a \( {u}^{\prime }\left( a\right) = {u}^{\prime }\left( b\right) = 0 \) . Finalement la formule (***) s'écrit

> as \( f \) and \( s \) satisfy conditions (ii) and (iii) of \( \left( *\right) \), we have \( {u}^{\prime }\left( a\right) = {u}^{\prime }\left( b\right) = 0 \). Finally, formula (***) is written

\[
{\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = {\int }_{a}^{b}{\left( {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} + {\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right)  - {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx}.
\]

On en déduit bien que \( {\int }_{a}^{b}{\left( {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = \mathop{\inf }\limits_{{f \in {H}_{2}^{ * }}}{\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) \right) }^{2}{dx} \) . La fonction \( s \) est bien la seule à atteindre ce minimum. En effet, considérons une autre fonction \( f \in {H}_{2}^{ * } \) qui l’atteint. La formule précédente entraîne \( {\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) - {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = 0 \) , donc \( {\int }_{{x}_{i - 1}}^{{x}_{i}}{\left( {f}^{\prime \prime }\left( x\right) - {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = 0 \) pour tout \( i \) . Donc sur chaque intervalle \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack ,{f}^{\prime \prime } - {s}^{\prime \prime } \) s’annule donc \( \left( {f - s}\right) \) y est affine. Comme de plus

> We thus deduce that \( {\int }_{a}^{b}{\left( {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = \mathop{\inf }\limits_{{f \in {H}_{2}^{ * }}}{\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) \right) }^{2}{dx} \). The function \( s \) is indeed the only one to reach this minimum. Indeed, let us consider another function \( f \in {H}_{2}^{ * } \) that reaches it. The previous formula implies \( {\int }_{a}^{b}{\left( {f}^{\prime \prime }\left( x\right) - {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = 0 \), therefore \( {\int }_{{x}_{i - 1}}^{{x}_{i}}{\left( {f}^{\prime \prime }\left( x\right) - {s}^{\prime \prime }\left( x\right) \right) }^{2}{dx} = 0 \) for all \( i \). Thus, on each interval \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack ,{f}^{\prime \prime } - {s}^{\prime \prime } \), it vanishes, so \( \left( {f - s}\right) \) is affine there. Since, moreover,

\( f \) et \( s \) vérifient \( \left( *\right) , f - s \) s’annule aux extrémités de \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) donc \( f - s = 0 \) sur \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) . On en déduit \( f = s \) , d’où le résultat.

> \( f \) and \( s \) satisfy \( \left( *\right) , f - s \) vanishes at the endpoints of \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \) so \( f - s = 0 \) on \( \left\lbrack {{x}_{i - 1},{x}_{i}}\right\rbrack \). We deduce \( f = s \), hence the result.

Remarque. On définit également les splines cubiques dans le plan ou l'espace. Ces der-nières sont utilisées en conception assistée par ordinateur, pour faire passer une courbe par des points donnés. Le théorème de Holladay exprime que ces courbes ont la propriété de "minimiser" la courbure tout en passant par les points.

> Remark. Cubic splines are also defined in the plane or in space. The latter are used in computer-aided design to make a curve pass through given points. Holladay's theorem states that these curves have the property of "minimizing" curvature while passing through the points.

- Les splines sont des courbes interpolantes qui oscillent moins que les polynômes d'interpolation de Lagrange, et elles évitent le phénomène de Runge (voir le tome Analyse).

> - Splines are interpolating curves that oscillate less than Lagrange interpolation polynomials, and they avoid the Runge phenomenon (see the Analysis volume).

- En remplaçant les conditions (ii) et (iii) de (*) par \( {s}^{\prime \prime }\left( a\right)  = {s}^{\prime \prime }\left( b\right)  = 0 \) , on définit de même les splines cubiques naturelles. Les propriétés d'existence et d'unicité, ainsi que le théorème de Holladay, restent vraies pour les splines naturelles. On peut également définir les splines d’ordre quelconque \( r \) , lorsque \( s \) est polynomiale de degré \( < r \) sur \( \left\lbrack  {{x}_{i - 1},{x}_{i}}\right\rbrack \) .

> - By replacing conditions (ii) and (iii) of (*) with \( {s}^{\prime \prime }\left( a\right)  = {s}^{\prime \prime }\left( b\right)  = 0 \), natural cubic splines are defined in the same way. The existence and uniqueness properties, as well as Holladay's theorem, remain true for natural splines. One can also define splines of arbitrary order \( r \), when \( s \) is a polynomial of degree \( < r \) on \( \left\lbrack  {{x}_{i - 1},{x}_{i}}\right\rbrack \).

Chapitre 4

> Chapter 4
