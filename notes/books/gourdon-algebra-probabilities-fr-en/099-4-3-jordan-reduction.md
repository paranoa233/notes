#### 4.3. Jordan reduction

*Français : 4.3. Réduction de Jordan*

Nous allons maintenant donner une réduction encore plus poussée que la précédente, appelée réduction de Jordan. En un certain sens, la réduction de Jordan est la plus poussée que l'on puisse obtenir. Il existe cependant d'autres types de réduction qui ont aussi leurs avantages et qui s'utilisent dans des circonstances différentes (voir l'annexe B).

> We will now provide a reduction even more advanced than the previous one, called Jordan reduction. In a certain sense, Jordan reduction is the most advanced one can obtain. There are, however, other types of reduction that also have their advantages and are used in different circumstances (see Appendix B).

La réduction de Jordan ne figure pas au programme des classes de mathématiques spéciales. Cependant, les techniques utilisées dans sa démonstration sont très classiques et leurs connaissances permettent de répondre à beaucoup de problèmes.

> Jordan reduction is not part of the curriculum for special mathematics classes. However, the techniques used in its proof are very standard and knowledge of them allows one to solve many problems.

Réduction de Jordan d'un endomorphisme nilpotent. Nous allons commencer par donner la réduite de Jordan d'un endomorphisme nilpotent. Nous verrons par la suite que la réduction d'un endomorphisme quelconque s'en déduit facilement.

> Jordan reduction of a nilpotent endomorphism. We will begin by providing the Jordan form of a nilpotent endomorphism. We will see later that the reduction of any endomorphism can be easily deduced from it.

THÉORÉME 4 (RÉDUCTION DE JORDAN D'UN ENDOMORPHISME NILPOTENT).

> THEOREM 4 (JORDAN REDUCTION OF A NILPOTENT ENDOMORPHISM).

Soit \( u \in \mathcal{L}\left( E\right) \) un endomorphisme nilpotent. Alors il existe une base \( B \) de \( E \) dans laquelle la matrice de u a la forme

> Let \( u \in \mathcal{L}\left( E\right) \) be a nilpotent endomorphism. Then there exists a basis \( B \) of \( E \) in which the matrix of u has the form

\[
{\left\lbrack  u\right\rbrack  }_{B} = \left( \begin{matrix} 0 & {v}_{1} & & \left( 0\right) \\  \vdots &  \ddots  &  \ddots  & \\  \vdots & &  \ddots  & {v}_{n - 1} \\  0 & \cdots & \cdots & 0 \end{matrix}\right) \;\text{ avec }\;\forall i,{v}_{i} \in  \{ 0,1\} .
\]

Démonstration. Soit \( r \in {\mathbb{N}}^{ * } \) l’indice de nilpotence de \( u \) , de sorte que \( {u}^{r - 1} \neq 0 \) et \( {u}^{r} = 0 \) . Pour tout \( i \in \mathbb{N} \) , on note \( {F}_{i} = \operatorname{Ker}\left( {u}^{i}\right) \) .

> Proof. Let \( r \in {\mathbb{N}}^{ * } \) be the index of nilpotence of \( u \), such that \( {u}^{r - 1} \neq 0 \) and \( {u}^{r} = 0 \). For all \( i \in \mathbb{N} \), we denote \( {F}_{i} = \operatorname{Ker}\left( {u}^{i}\right) \).

1) Montrons que

> 1) Let us show that

(i) \( \{ 0\} = {F}_{0} \subsetneq {F}_{1} \subsetneq \cdots \subsetneq {F}_{r - 1} \subsetneq {F}_{r} = E \) .

> (ii) Pour tout \( i \in \mathbb{N},1 \leq i \leq r, u\left( {F}_{i}\right) \subset {F}_{i - 1} \) .

(ii) For all \( i \in \mathbb{N},1 \leq i \leq r, u\left( {F}_{i}\right) \subset {F}_{i - 1} \).

> La partie (i) résulte de la définition 2, car \( r \) n’est autre que l’indice de \( u \) (voir la remarque 1).

Part (i) follows from definition 2, because \( r \) is none other than the index of \( u \) (see remark 1).

> Montrons (ii). Soit \( i \in \mathbb{N},1 \leq i \leq r \) . Pour tout \( x \in {F}_{i},{u}^{i - 1}\left\lbrack {u\left( x\right) }\right\rbrack = {u}^{i}\left( x\right) = 0 \) donc \( u\left( x\right) \in {F}_{i - 1} \) . Donc \( u\left( {F}_{i}\right) \subset {F}_{i - 1} \) .

Let us show (ii). Let \( i \in \mathbb{N},1 \leq i \leq r \) . For all \( x \in {F}_{i},{u}^{i - 1}\left\lbrack {u\left( x\right) }\right\rbrack = {u}^{i}\left( x\right) = 0 \) thus \( u\left( x\right) \in {F}_{i - 1} \) . Therefore \( u\left( {F}_{i}\right) \subset {F}_{i - 1} \) .

> 2) Nous allons maintenant montrer l’existence de s.e.v \( {G}_{1},\ldots ,{G}_{r} \) et \( {H}_{1},\ldots ,{H}_{r - 1} \) de \( E \) tels que

2) We will now show the existence of subspaces \( {G}_{1},\ldots ,{G}_{r} \) and \( {H}_{1},\ldots ,{H}_{r - 1} \) of \( E \) such that

> (i) \( \forall i,1 \leq i \leq r,{F}_{i} = {G}_{i} \oplus {F}_{i - 1} \) .

(ii) \( \forall i,1 \leq i \leq r - 1, u \) applique injectivement \( {G}_{i + 1} \) dans \( {G}_{i} \) .

> (ii) \( \forall i,1 \leq i \leq r - 1, u \) maps \( {G}_{i + 1} \) injectively into \( {G}_{i} \) .

(iii) \( \forall i,1 \leq i \leq r - 1,{G}_{i} = u\left( {G}_{i + 1}\right) \oplus {H}_{i} \) .

> (iii) \( \forall i,1 \leq i \leq r - 1,{G}_{i} = u\left( {G}_{i + 1}\right) \oplus {H}_{i} \) .

Soit \( {G}_{r} \) un supplémentaire de \( {F}_{r - 1} \) dans \( {F}_{r} \) , de sorte que \( {F}_{r} = {G}_{r} \oplus {F}_{r - 1} \) . On a

> Let \( {G}_{r} \) be a supplementary subspace of \( {F}_{r - 1} \) in \( {F}_{r} \) , so that \( {F}_{r} = {G}_{r} \oplus {F}_{r - 1} \) . We have

\[
\left\{  \begin{array}{l} \left( {\operatorname{Ker}u}\right)  \cap  {G}_{r} = {F}_{1} \cap  {G}_{r} \subset  {F}_{r - 1} \cap  {G}_{r} = \{ 0\} \\  u\left( {G}_{r}\right)  \subset  u\left( {F}_{r}\right)  \subset  {F}_{r - 1} \end{array}\right.
\]

donc \( u \) applique injectivement \( {G}_{r} \) dans \( {F}_{r - 1} \) .

> thus \( u \) maps \( {G}_{r} \) injectively into \( {F}_{r - 1} \) .

\( u\left( {G}_{r}\right) \cap {F}_{r - 2} = \{ 0\} \) . En effet, soit \( x \in u\left( {G}_{r}\right) \cap {F}_{r - 2} \) . Il existe \( y \in {G}_{r} \) tel que \( u\left( y\right) = x \) , et on a \( 0 = {u}^{r - 2}\left( x\right) = {u}^{r - 1}\left( y\right) \) , donc \( y \in {F}_{r - 1} \cap {G}_{r} = \{ 0\} \) , donc \( y = 0 \) , donc \( x = u\left( y\right) = 0 \) .

> \( u\left( {G}_{r}\right) \cap {F}_{r - 2} = \{ 0\} \) . Indeed, let \( x \in u\left( {G}_{r}\right) \cap {F}_{r - 2} \) . There exists \( y \in {G}_{r} \) such that \( u\left( y\right) = x \) , and we have \( 0 = {u}^{r - 2}\left( x\right) = {u}^{r - 1}\left( y\right) \) , thus \( y \in {F}_{r - 1} \cap {G}_{r} = \{ 0\} \) , thus \( y = 0 \) , thus \( x = u\left( y\right) = 0 \) .

On a donc \( u\left( {G}_{r}\right) \oplus {F}_{r - 2} \subset {F}_{r - 1} \) . Il existe donc un s.e.v \( {H}_{r - 1} \) tel que \( u\left( {G}_{r}\right) \oplus {F}_{r - 2} \oplus {H}_{r - 1} = \; {F}_{r - 1} \) . Si on pose \( {G}_{r - 1} = u\left( {G}_{r}\right) \oplus {H}_{r - 1} \) , on a donc \( {F}_{r - 1} = {G}_{r - 1} \oplus {F}_{r - 2} \) , et \( u \) applique injectivement \( {G}_{r} \) dans \( {G}_{r - 1} \) .

> We therefore have \( u\left( {G}_{r}\right) \oplus {F}_{r - 2} \subset {F}_{r - 1} \) . There thus exists a subspace \( {H}_{r - 1} \) such that \( u\left( {G}_{r}\right) \oplus {F}_{r - 2} \oplus {H}_{r - 1} = \; {F}_{r - 1} \) . If we set \( {G}_{r - 1} = u\left( {G}_{r}\right) \oplus {H}_{r - 1} \) , we then have \( {F}_{r - 1} = {G}_{r - 1} \oplus {F}_{r - 2} \) , and \( u \) maps \( {G}_{r} \) injectively into \( {G}_{r - 1} \) .

Ainsi (i),(ii) et (iii) sont démontrés pour \( i = r - 1 \) . Pour montrer (i),(ii) et (iii) pour \( i \in \; \{ 1,\ldots , r - 2\} \) , nous allons utiliser une récurrence descendante. Supposons le résultat prouvé pour \( i + 1 \in \{ 2,\ldots , r - 1\} \) et montrons le pour \( i \) .

> Thus (i),(ii) and (iii) are proven for \( i = r - 1 \) . To show (i),(ii) and (iii) for \( i \in \; \{ 1,\ldots , r - 2\} \) , we will use downward induction. Assume the result is proven for \( i + 1 \in \{ 2,\ldots , r - 1\} \) and let us show it for \( i \) .

On s’intéresse au comportement de \( u \) sur \( {G}_{i + 1} \) . On a

> We are interested in the behavior of \( u \) on \( {G}_{i + 1} \) . We have

\[
\left\{  \begin{array}{l} \left( {\operatorname{Ker}u}\right)  \cap  {G}_{i + 1} = {F}_{1} \cap  {G}_{i + 1} \subset  {F}_{i} \cap  {G}_{i + 1} = \{ 0\} \\  u\left( {G}_{i + 1}\right)  \subset  u\left( {F}_{i + 1}\right)  \subset  {F}_{i} \end{array}\right.
\]

donc \( u \) applique injectivement \( {G}_{i + 1} \) dans \( {F}_{i} \) .

> thus \( u \) maps \( {G}_{i + 1} \) injectively into \( {F}_{i} \) .

\( u\left( {G}_{i + 1}\right) \cap {F}_{i - 1} = \{ 0\} \) . En effet, soit \( x \in u\left( {G}_{i + 1}\right) \cap {F}_{i - 1} \) . Il existe \( y \in {G}_{i + 1} \) tel que \( x = u\left( y\right) \) . Or \( x \in {F}_{i - 1} \) donc \( 0 = {u}^{i - 1}\left( x\right) = {u}^{i}\left( y\right) \) , d’où \( y \in {F}_{i} \cap {G}_{i + 1} = \{ 0\} \) , c’est-à-dire \( y = 0 \) , donc \( x = u\left( y\right) = 0. \)

> \( u\left( {G}_{i + 1}\right) \cap {F}_{i - 1} = \{ 0\} \) . Indeed, let \( x \in u\left( {G}_{i + 1}\right) \cap {F}_{i - 1} \) . There exists \( y \in {G}_{i + 1} \) such that \( x = u\left( y\right) \) . However, \( x \in {F}_{i - 1} \) so \( 0 = {u}^{i - 1}\left( x\right) = {u}^{i}\left( y\right) \) , hence \( y \in {F}_{i} \cap {G}_{i + 1} = \{ 0\} \) , that is to say \( y = 0 \) , therefore \( x = u\left( y\right) = 0. \)

On a donc \( u\left( {G}_{i + 1}\right) \oplus {F}_{i - 1} \subset {F}_{i} \) . On peut donc trouver un s.e.v \( {H}_{i} \) tel que \( u\left( {G}_{i + 1}\right) \oplus {F}_{i - 1} \oplus {H}_{i} = \; {F}_{i} \) . On pose alors \( {G}_{i} = u\left( {G}_{i + 1}\right) \oplus {H}_{i} \) , de sorte que \( {F}_{i} = {G}_{i} \oplus {F}_{i - 1} \) et \( u \) applique injectivement \( {G}_{i + 1} \) dans \( {G}_{i} \) .

> We thus have \( u\left( {G}_{i + 1}\right) \oplus {F}_{i - 1} \subset {F}_{i} \) . We can therefore find a subspace \( {H}_{i} \) such that \( u\left( {G}_{i + 1}\right) \oplus {F}_{i - 1} \oplus {H}_{i} = \; {F}_{i} \) . We then set \( {G}_{i} = u\left( {G}_{i + 1}\right) \oplus {H}_{i} \) , so that \( {F}_{i} = {G}_{i} \oplus {F}_{i - 1} \) and \( u \) maps \( {G}_{i + 1} \) injectively into \( {G}_{i} \) .

Les s.e.v \( {G}_{r},\ldots ,{G}_{1} \) et \( {H}_{r - 1},\ldots ,{H}_{1} \) sont ainsi construits de proche en proche. Les propriétés (i) et (iii) à l'ordre 1 sont

> The subspaces \( {G}_{r},\ldots ,{G}_{1} \) and \( {H}_{r - 1},\ldots ,{H}_{1} \) are thus constructed step by step. Properties (i) and (iii) at order 1 are

\[
\left\{  \begin{array}{l} \operatorname{Ker}u = {F}_{1} = {G}_{1} \oplus  {F}_{0} = {G}_{1} \oplus  \{ 0\}  = {G}_{1} \\  {G}_{1} = u\left( {G}_{2}\right)  \oplus  {H}_{1} \end{array}\right.
\]

En résumé, la suite \( {G}_{1},\ldots ,{G}_{r} \) vérifie

> In summary, the sequence \( {G}_{1},\ldots ,{G}_{r} \) satisfies

\[
\left\{  \begin{array}{l} E = {G}_{r} \oplus  {G}_{r - 1} \oplus  \cdots  \oplus  {G}_{1} \\  {G}_{1} = {F}_{1} = \operatorname{Ker}u \\  \forall i,2 \leq  i \leq  r, u\text{ applique injectivement }{G}_{i}\text{ dans }{G}_{i - 1} \end{array}\right.
\]

3) Partant d’une base \( {\varepsilon }_{i,1},\ldots ,{\varepsilon }_{i,{s}_{i}} \) de \( {G}_{i}, u\left( {\varepsilon }_{i,1}\right) ,\ldots , u\left( {\varepsilon }_{i,{s}_{i}}\right) \) est une famille libre de \( {G}_{i - 1} \) que l’on peut compléter par \( {\varepsilon }_{i - 1,1},\ldots ,{\varepsilon }_{i - 1,{s}_{i - 1}} \) pour obtenir une base de \( {G}_{i - 1} \) . Nous obtenons en réunissant toutes ces bases une base de \( E \) que nous pouvons écrire sous la forme du tableau à double entrée suivant.

> 3) Starting from a basis \( {\varepsilon }_{i,1},\ldots ,{\varepsilon }_{i,{s}_{i}} \) of \( {G}_{i}, u\left( {\varepsilon }_{i,1}\right) ,\ldots , u\left( {\varepsilon }_{i,{s}_{i}}\right) \) is a linearly independent family of \( {G}_{i - 1} \) that can be completed by \( {\varepsilon }_{i - 1,1},\ldots ,{\varepsilon }_{i - 1,{s}_{i - 1}} \) to obtain a basis of \( {G}_{i - 1} \) . By uniting all these bases, we obtain a basis of \( E \) which we can write in the form of the following double-entry table.

<table><tr><td>\( {G}_{r} \)</td><td>\( {e}_{r,1} \)</td><td>...</td><td>\( {e}_{r,{s}_{r}} \)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>\( {G}_{r - 1} \)</td><td>\( u\left( {e}_{r,1}\right) \)</td><td>...</td><td>\( u\left( {e}_{r,{s}_{r}}\right) \)</td><td>\( {e}_{r - 1,1} \)</td><td>...</td><td>\( {e}_{r - 1,{s}_{r - 1}} \)</td><td></td><td></td><td></td></tr><tr><td>\( {G}_{r - 2} \)</td><td>\( {u}^{2}\left( {e}_{r,1}\right) \)</td><td>...</td><td>\( {u}^{2}\left( {e}_{r,{s}_{r}}\right) \)</td><td>\( u\left( {e}_{r - 1,1}\right) \)</td><td>...</td><td>\( u\left( {e}_{r - 1,{s}_{r - 1}}\right) \)</td><td>\( {e}_{r - 2,1} \)</td><td>...</td><td></td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td></td></tr><tr><td>\( {G}_{1} \)</td><td>\( {u}^{r - 1}\left( {e}_{r,1}\right) \)</td><td>...</td><td>\( {u}^{r - 1}\left( {e}_{r,{s}_{r}}\right) \)</td><td>\( {u}^{r - 2}\left( {e}_{r - 1,1}\right) \)</td><td>...</td><td>\( {u}^{r - 2}\left( {e}_{r - 1,{s}_{r - 1}}\right) \)</td><td>\( {u}^{r - 3}\left( {e}_{r - 2,1}\right) \)</td><td>... \( {e}_{1,1} \)</td><td>\( {e}_{1,{s}_{1}} \)</td></tr></table>

> <table><tr><td>\( {G}_{r} \)</td><td>\( {e}_{r,1} \)</td><td>...</td><td>\( {e}_{r,{s}_{r}} \)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>\( {G}_{r - 1} \)</td><td>\( u\left( {e}_{r,1}\right) \)</td><td>...</td><td>\( u\left( {e}_{r,{s}_{r}}\right) \)</td><td>\( {e}_{r - 1,1} \)</td><td>...</td><td>\( {e}_{r - 1,{s}_{r - 1}} \)</td><td></td><td></td><td></td></tr><tr><td>\( {G}_{r - 2} \)</td><td>\( {u}^{2}\left( {e}_{r,1}\right) \)</td><td>...</td><td>\( {u}^{2}\left( {e}_{r,{s}_{r}}\right) \)</td><td>\( u\left( {e}_{r - 1,1}\right) \)</td><td>...</td><td>\( u\left( {e}_{r - 1,{s}_{r - 1}}\right) \)</td><td>\( {e}_{r - 2,1} \)</td><td>...</td><td></td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td><td></td></tr><tr><td>\( {G}_{1} \)</td><td>\( {u}^{r - 1}\left( {e}_{r,1}\right) \)</td><td>...</td><td>\( {u}^{r - 1}\left( {e}_{r,{s}_{r}}\right) \)</td><td>\( {u}^{r - 2}\left( {e}_{r - 1,1}\right) \)</td><td>...</td><td>\( {u}^{r - 2}\left( {e}_{r - 1,{s}_{r - 1}}\right) \)</td><td>\( {u}^{r - 3}\left( {e}_{r - 2,1}\right) \)</td><td>... \( {e}_{1,1} \)</td><td>\( {e}_{1,{s}_{1}} \)</td></tr></table>

4) En lisant le tableau précédent colonne par colonne, de bas en haut puis de gauche à droite, nous obtenons un nouvel ordre \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) des vecteurs de cette base. On voit alors que \( u\left( {e}_{j}\right) = {e}_{j - 1} \) si \( {e}_{j} \) n’est pas situé sur la dernière ligne, \( u\left( {e}_{j}\right) = 0 \) si \( {e}_{j} \) est situé sur la dernière ligne. La base \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) convient donc pour le théorème.

> 4) By reading the previous table column by column, from bottom to top and then from left to right, we obtain a new order \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of the vectors of this basis. We then see that \( u\left( {e}_{j}\right) = {e}_{j - 1} \) if \( {e}_{j} \) is not located on the last row, \( u\left( {e}_{j}\right) = 0 \) if \( {e}_{j} \) is located on the last row. The basis \( B = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is therefore suitable for the theorem.

Remarque 3. Une autre manière de voir les choses est de remarquer que \( {\left\lbrack u\right\rbrack }_{B} \) est constituée de blocs nuls et de blocs de la forme

> Remark 3. Another way to look at things is to note that \( {\left\lbrack u\right\rbrack }_{B} \) consists of zero blocks and blocks of the form

\[
\left( \begin{matrix} 0 & 1 & & \left( 0\right) \\  \vdots &  \ddots  &  \ddots  & \\  \vdots & &  \ddots  & 1 \\  0 & \cdots & \cdots & 0 \end{matrix}\right)
\]

centrés sur sa diagonale principale.

> centered on its main diagonal.

- On peut aussi obtenir la réduction de Jordan d'un endomorphisme nilpotent dans le cadre de la théorie des invariants de similitude (voir l'annexe B page 400).

> - One can also obtain the Jordan reduction of a nilpotent endomorphism within the framework of the theory of similarity invariants (see Appendix B, page 400).

THÉORÉME 5 (RÉDUCTION DE JORDAN D'UN ENDOMORPHISME). Soit \( f \in \mathcal{L}\left( E\right) \) tel que son polynôme caractéristique \( {P}_{f} \) soit scindé sur \( \mathbb{K} \) :

> THEOREM 5 (JORDAN REDUCTION OF AN ENDOMORPHISM). Let \( f \in \mathcal{L}\left( E\right) \) be such that its characteristic polynomial \( {P}_{f} \) splits over \( \mathbb{K} \):

\[
{P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}},\;\left( {{\lambda }_{i} \neq  {\lambda }_{j}\text{ si }i \neq  j}\right) .
\]

Alors il existe une base \( B \) de \( E \) dans laquelle la matrice de \( f \) ait la forme

> Then there exists a basis \( B \) of \( E \) in which the matrix of \( f \) has the form

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} {A}_{1} & & 0 \\   & {A}_{2} & \\  0 &  \ddots  & \\   & & {A}_{s} \end{matrix}\right) ,\;o\dot{u}\;\forall i,{A}_{i} = \left( \begin{matrix} {\lambda }_{i} & {v}_{i,1} & & 0 \\  0 & {\lambda }_{i} &  \ddots  & \\  \vdots &  \ddots  &  \ddots  & {v}_{i,{\alpha }_{i} - 1} \\  0 & \cdots & 0 & {\lambda }_{i} \end{matrix}\right)  \in  {\mathcal{M}}_{{\alpha }_{i}}(\mathbb{K}
\]

avec pour tout \( \left( {i, j}\right) ,{v}_{i, j} \in \{ 0,1\} \) .

> with for all \( \left( {i, j}\right) ,{v}_{i, j} \in \{ 0,1\} \) .

Démonstration. Pour tout \( i \) , on note \( {N}_{i} = \operatorname{Ker}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} \) les sous-espaces caractéristiques de \( f \) . On a \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) et les \( {N}_{i} \) sont stables par \( f \) . Pour tout \( i \) , on pose \( {f}_{i} = {f}_{\mid {N}_{i}} \) . On a \( {f}_{i} \in \mathcal{L}\left( {N}_{i}\right) \) et \( {\left( {f}_{i} - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} = 0 \) , donc \( {n}_{i} = {f}_{i} - {\lambda }_{i}\operatorname{Id} \) est nilpotent. D’après le théorème précédent, il existe donc une base \( {B}_{i} \) de \( {N}_{i} \) telle que

> Proof. For all \( i \) , we denote by \( {N}_{i} = \operatorname{Ker}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} \) the characteristic subspaces of \( f \) . We have \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) and the \( {N}_{i} \) are stable under \( f \) . For all \( i \) , we set \( {f}_{i} = {f}_{\mid {N}_{i}} \) . We have \( {f}_{i} \in \mathcal{L}\left( {N}_{i}\right) \) and \( {\left( {f}_{i} - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} = 0 \) , so \( {n}_{i} = {f}_{i} - {\lambda }_{i}\operatorname{Id} \) is nilpotent. According to the previous theorem, there therefore exists a basis \( {B}_{i} \) of \( {N}_{i} \) such that

\[
{\left\lbrack  {n}_{i}\right\rbrack  }_{{B}_{i}} = \left( \begin{matrix} 0 & {v}_{i,1} & & \left( 0\right) \\  \vdots &  \ddots  &  \ddots  & \\  \vdots & &  \ddots  & {v}_{i,{\alpha }_{i} - 1} \\  0 & \ldots & \ldots & 0 \end{matrix}\right) \;\text{ donc }\;{\left\lbrack  {f}_{i}\right\rbrack  }_{{B}_{i}} = {\left\lbrack  {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} + {n}_{i}\right\rbrack  }_{{B}_{i}} = \left( \begin{matrix} {\lambda }_{i} & {v}_{i,1} & & \left( 0\right) \\  0 & {\lambda }_{i} &  \ddots  & \\  \vdots &  \ddots  &  \ddots  & {v}_{i,{\alpha }_{i} - 1} \\  0 & \ldots & 0 & {\lambda }_{i} \end{matrix}\right)
\]

avec pour tout \( j,1 \leq j \leq {\alpha }_{i} - 1,{v}_{i, j} \in \{ 0,1\} \) . Comme \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) , on voit que \( B = \left( {{B}_{1},\ldots ,{B}_{s}}\right) \) est une base de \( E \) et que

> with for all \( j,1 \leq j \leq {\alpha }_{i} - 1,{v}_{i, j} \in \{ 0,1\} \) . As \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) , we see that \( B = \left( {{B}_{1},\ldots ,{B}_{s}}\right) \) is a basis of \( E \) and that

\[
{\left\lbrack  f\right\rbrack  }_{B} = \left( \begin{matrix} {\left\lbrack  {f}_{1}\right\rbrack  }_{{B}_{1}} & \left( 0\right) \\  \left( 0\right) &  \ddots  \\  \left( 0\right) & {\left\lbrack  {f}_{s}\right\rbrack  }_{{B}_{s}} \end{matrix}\right)
\]

d’où le résultat en posant, pour tout \( i,{A}_{i} = {\left\lbrack {f}_{i}\right\rbrack }_{{B}_{i}} \) .

> whence the result by setting, for all \( i,{A}_{i} = {\left\lbrack {f}_{i}\right\rbrack }_{{B}_{i}} \) .

Remarque 4. Ce théorème peut aussi s’interpréter comme suit : \( {\left\lbrack f\right\rbrack }_{B} \) est constituée de blocs de taille 1 du type \( \left( {\lambda }_{i}\right) \) ou de taille \( > 1 \) du type

> Remark 4. This theorem can also be interpreted as follows: \( {\left\lbrack f\right\rbrack }_{B} \) consists of blocks of size 1 of the type \( \left( {\lambda }_{i}\right) \) or of size \( > 1 \) of the type

![bo_d7fjffs91nqc73erehlg_209_622_1453_316_202_0.jpg](images/gourdon_algebra_probabilities_fr_en_007_bod7fjffs91nqc73erehlg20962214533162020.jpg)

centrés sur sa diagonale principale.

> centered on its main diagonal.
