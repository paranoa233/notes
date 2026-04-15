#### 4.2. Symmetric polynomials

*Français : 4.2. Polynômes symétriques*

DÉFINITION 3. Un polynôme \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) est dit symétrique si pour tout \( \sigma \in {\mathcal{S}}_{n} \) (où \( {\mathcal{S}}_{n} \) désigne le groupe symétrique d’indice \( n \) ), \( P\left( {{X}_{\sigma \left( 1\right) },\ldots ,{X}_{\sigma \left( n\right) }}\right) = P\left( {{X}_{1},\ldots ,{X}_{n}}\right) \) .

> DEFINITION 3. A polynomial \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) is said to be symmetric if for all \( \sigma \in {\mathcal{S}}_{n} \) (where \( {\mathcal{S}}_{n} \) denotes the symmetric group of degree \( n \)), \( P\left( {{X}_{\sigma \left( 1\right) },\ldots ,{X}_{\sigma \left( n\right) }}\right) = P\left( {{X}_{1},\ldots ,{X}_{n}}\right) \).

Exemple 1. Dans \( \mathbb{R}\left\lbrack {X, Y, Z}\right\rbrack , P = {XY} + {YZ} + {ZX} \) est symétrique.

> Example 1. In \( \mathbb{R}\left\lbrack {X, Y, Z}\right\rbrack , P = {XY} + {YZ} + {ZX} \) is symmetric.

DéFINITION 4 (SYMÉTRISÉ D’UN MONÔME). Soit \( M = {X}_{1}^{{\alpha }_{1}}\cdots {X}_{n}^{{\alpha }_{n}} \in A\left\lbrack {{X}_{1},\cdots {X}_{n}}\right\rbrack \) . Si \( \sigma \in {\mathcal{S}}_{n} \) , on pose \( {M}_{\sigma } = {X}_{\sigma \left( 1\right) }^{{\alpha }_{1}}\cdots {X}_{\sigma \left( n\right) }^{{\alpha }_{n}} \) . Le polynôme \( \mathop{\sum }\limits_{{M}_{\sigma }}{M}_{\sigma } \) est symétrique dans \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . On l’appelle symétrisé de \( M \) dans \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) et on le note \( \sum M \) .

> DEFINITION 4 (SYMMETRIZATION OF A MONOMIAL). Let \( M = {X}_{1}^{{\alpha }_{1}}\cdots {X}_{n}^{{\alpha }_{n}} \in A\left\lbrack {{X}_{1},\cdots {X}_{n}}\right\rbrack \). If \( \sigma \in {\mathcal{S}}_{n} \), we set \( {M}_{\sigma } = {X}_{\sigma \left( 1\right) }^{{\alpha }_{1}}\cdots {X}_{\sigma \left( n\right) }^{{\alpha }_{n}} \). The polynomial \( \mathop{\sum }\limits_{{M}_{\sigma }}{M}_{\sigma } \) is symmetric in \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \). It is called the symmetrization of \( M \) in \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) and is denoted by \( \sum M \).

Exemple 2. Dans \( \mathbb{K}\left\lbrack {{X}_{1},{X}_{2}}\right\rbrack ,\sum {X}_{1}^{2}{X}_{2} = {X}_{1}^{2}{X}_{2} + {X}_{1}{X}_{2}^{2} \) .

> Example 2. In \( \mathbb{K}\left\lbrack {{X}_{1},{X}_{2}}\right\rbrack ,\sum {X}_{1}^{2}{X}_{2} = {X}_{1}^{2}{X}_{2} + {X}_{1}{X}_{2}^{2} \).

Dans \( \mathbb{K}\left\lbrack {{X}_{1},{X}_{2},{X}_{3}}\right\rbrack ,\sum {X}_{1}^{2}{X}_{2} = {X}_{1}^{2}{X}_{2} + {X}_{1}{X}_{2}^{2} + {X}_{2}^{2}{X}_{3} + {X}_{3}^{2}{X}_{2} + {X}_{1}^{2}{X}_{3} + {X}_{1}{X}_{3}^{2} \) . (On voit sur cet exemple que les symétrisés d’un monôme dans \( A\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) et dans \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) sont différents si \( n \neq m) \) .

> In \( \mathbb{K}\left\lbrack {{X}_{1},{X}_{2},{X}_{3}}\right\rbrack ,\sum {X}_{1}^{2}{X}_{2} = {X}_{1}^{2}{X}_{2} + {X}_{1}{X}_{2}^{2} + {X}_{2}^{2}{X}_{3} + {X}_{3}^{2}{X}_{2} + {X}_{1}^{2}{X}_{3} + {X}_{1}{X}_{3}^{2} \). (We see in this example that the symmetrizations of a monomial in \( A\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) and in \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) are different if \( n \neq m) \).

Polynômes symétriques élémentaires. On appelle polynômes symétriques élémen-taires de \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) les polynômes notés \( {\sum }_{p}\left( {1 \leq p \leq n}\right) \) et définis par

> Elementary symmetric polynomials. The elementary symmetric polynomials of \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) are the polynomials denoted by \( {\sum }_{p}\left( {1 \leq p \leq n}\right) \) and defined by

\[
{\sum }_{p} = \sum {X}_{1}\cdots {X}_{p} = \mathop{\sum }\limits_{{{i}_{1} < \cdots  < {i}_{p}}}{X}_{{i}_{1}}\cdots {X}_{{i}_{p}}.
\]

On a en particulier

> In particular, we have

\[
{\sum }_{1} = \sum {X}_{1} = {X}_{1} + \cdots  + {X}_{n},\;{\sum }_{2} = \sum {X}_{1}{X}_{2} = \mathop{\sum }\limits_{{i < j}}{X}_{i}{X}_{j},\;{\sum }_{n} = {X}_{1}\cdots {X}_{n}.
\]

Les polynômes symétriques élémentaires vérifient l'égalité fondamentale

> The elementary symmetric polynomials satisfy the fundamental equality

\[
\left( {T - {X}_{1}}\right) \cdots \left( {T - {X}_{n}}\right)  = {T}^{n} - {\sum }_{1}{T}^{n - 1} + {\sum }_{2}{T}^{n - 2} + \cdots  + {\left( -1\right) }^{n - 1}{\sum }_{n - 1}T + {\left( -1\right) }^{n}{\sum }_{n}.
\]

En particulier, si \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) est un polynôme de \( \mathbb{K}\left\lbrack X\right\rbrack \) scindé sur \( \mathbb{K} \) et si \( {u}_{1},\ldots ,{u}_{n} \) sont ses racines, alors \( \forall i,1 \leq i \leq n,{\left( -1\right) }^{i}{a}_{i} = {\sum }_{i}\left( {{u}_{1},\ldots ,{u}_{n}}\right) \) .

> In particular, if \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) is a polynomial in \( \mathbb{K}\left\lbrack X\right\rbrack \) that splits over \( \mathbb{K} \) and if \( {u}_{1},\ldots ,{u}_{n} \) are its roots, then \( \forall i,1 \leq i \leq n,{\left( -1\right) }^{i}{a}_{i} = {\sum }_{i}\left( {{u}_{1},\ldots ,{u}_{n}}\right) \) .

Remarque 2. Si \( \Phi \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) , alors \( \Phi \left\lbrack {{\sum }_{1}\left( {{X}_{1},\ldots ,{X}_{n}}\right) ,\ldots ,{\sum }_{n}\left( {{X}_{1},\ldots ,{X}_{n}}\right) }\right\rbrack \) est un polynôme symétrique de \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . La réciproque est vraie : tout polynôme symé- trique peut se mettre sous cette forme. Plus précisément, on a le théorème suivant :

> Remark 2. If \( \Phi \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) , then \( \Phi \left\lbrack {{\sum }_{1}\left( {{X}_{1},\ldots ,{X}_{n}}\right) ,\ldots ,{\sum }_{n}\left( {{X}_{1},\ldots ,{X}_{n}}\right) }\right\rbrack \) is a symmetric polynomial of \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . The converse is true: every symmetric polynomial can be written in this form. More precisely, we have the following theorem:

\( \rightarrow \) THÉORÉME 1. Soit \( A \) un anneau commutatif unitaire et \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) un polynôme symétrique dans \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . Il existe un unique polynôme \( \Phi \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) tel que \( P = \Phi \left( {{\sum }_{1},\ldots ,{\sum }_{n}}\right) . \)

> \( \rightarrow \) THEOREM 1. Let \( A \) be a commutative unitary ring and \( P \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) be a symmetric polynomial in \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . There exists a unique polynomial \( \Phi \in A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) such that \( P = \Phi \left( {{\sum }_{1},\ldots ,{\sum }_{n}}\right) . \)

Remarque 3. Une preuve classique de ce résultat consiste à utiliser la méthode de Waring dont le principe est de faire diminuer la hauteur de \( P \) en lui retranchant le produit d’une constante et de polynômes symétriques élémentaires. Un cas typique d'utilisation de cette méthode fait l'objet de l'exercice 1.

> Remark 3. A classic proof of this result consists of using Waring's method, the principle of which is to decrease the height of \( P \) by subtracting from it the product of a constant and elementary symmetric polynomials. A typical case of using this method is the subject of exercise 1.

Exemple 3. Dans \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack ,\sum {X}_{1}^{2} = {\sum }_{1}^{2} - 2{\sum }_{2} \) et \( \sum {X}_{1}^{2}{X}_{2} = {\sum }_{1}{\sum }_{2} - 3{\sum }_{3} \) .

> Example 3. In \( A\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack ,\sum {X}_{1}^{2} = {\sum }_{1}^{2} - 2{\sum }_{2} \) and \( \sum {X}_{1}^{2}{X}_{2} = {\sum }_{1}{\sum }_{2} - 3{\sum }_{3} \) .

Remarque 4. Ce théorème entraîne le résultat suivant. Soit \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) un polynôme unitaire. Les fonctions symétriques \( {\sigma }_{1},\ldots ,{\sigma }_{n} \) de ses racines \( {u}_{1},\ldots ,{u}_{n} \) sont donc en-tières. Si \( F \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) est symétrique, alors \( F\left( {{u}_{1},\ldots ,{u}_{n}}\right) \in \mathbb{Z} \) (l’existence de \( G \in \; \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) tel que \( F = G\left( {{\sum }_{1},\ldots ,{\sum }_{n}}\right) \) , entraîne \( F\left( {{u}_{1},\ldots ,{u}_{n}}\right) = G\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right) \in \mathbb{Z} \) ).

> Remark 4. This theorem leads to the following result. Let \( P \in \mathbb{Z}\left\lbrack X\right\rbrack \) be a monic polynomial. The symmetric functions \( {\sigma }_{1},\ldots ,{\sigma }_{n} \) of its roots \( {u}_{1},\ldots ,{u}_{n} \) are therefore integral. If \( F \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) is symmetric, then \( F\left( {{u}_{1},\ldots ,{u}_{n}}\right) \in \mathbb{Z} \) (the existence of \( G \in \; \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) such that \( F = G\left( {{\sum }_{1},\ldots ,{\sum }_{n}}\right) \) implies \( F\left( {{u}_{1},\ldots ,{u}_{n}}\right) = G\left( {{\sigma }_{1},\ldots ,{\sigma }_{n}}\right) \in \mathbb{Z} \) ).
