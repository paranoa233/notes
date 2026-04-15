#### 4.1. Characteristic subspaces

*Français : 4.1. sous-espaces caractéristiques*

DÉFINITION 1. Soit \( f \in \mathcal{L}\left( E\right) \) tel que le polynôme caractéristique \( {P}_{f} \) de \( f \) soit scindé sur \( \mathbb{K} : {P}_{f} = {\left( -1\right) }^{n}{\left( X - {\lambda }_{1}\right) }^{{\alpha }_{1}}\cdots {\left( X - {\lambda }_{s}\right) }^{{\alpha }_{s}} \) . Pour tout \( i \) , le s.e.v \( {N}_{i} = \operatorname{Ker}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} \) s’appelle le sous-espace caractéristique de \( f \) associé à la valeur propre \( {\lambda }_{i} \) .

> DEFINITION 1. Let \( f \in \mathcal{L}\left( E\right) \) be such that the characteristic polynomial \( {P}_{f} \) of \( f \) splits over \( \mathbb{K} : {P}_{f} = {\left( -1\right) }^{n}{\left( X - {\lambda }_{1}\right) }^{{\alpha }_{1}}\cdots {\left( X - {\lambda }_{s}\right) }^{{\alpha }_{s}} \) . For any \( i \) , the subspace \( {N}_{i} = \operatorname{Ker}{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}} \) is called the characteristic subspace of \( f \) associated with the eigenvalue \( {\lambda }_{i} \) .

- Pour tout \( i,{N}_{i} \) est stable par \( f \) .

> - For any \( i,{N}_{i} \) is invariant under \( f \) .

- On a \( E = {N}_{1} \oplus  \cdots  \oplus  {N}_{s} \) ,

> - We have \( E = {N}_{1} \oplus  \cdots  \oplus  {N}_{s} \) ,

- Pour tout \( i,\dim {N}_{i} = {\alpha }_{i} \) .

> - For any \( i,\dim {N}_{i} = {\alpha }_{i} \) .

Démonstration. Le s.e.v \( {N}_{i} \) est bien stable par \( f \) car si \( x \in {N}_{i} \) ,

> Proof. The subspace \( {N}_{i} \) is indeed invariant under \( f \) because if \( x \in {N}_{i} \) ,

\[
{\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left( {f\left( x\right) }\right)  = f \circ  {\left( f - {\lambda }_{i}\operatorname{Id}\right) }^{{\alpha }_{i}}\left( x\right)  = 0.
\]

- Le fait que \( E = {N}_{1} \oplus  \cdots  \oplus  {N}_{s} \) résulte du théorème de décomposition des noyaux (voir 2.1, théorème 1).

> - The fact that \( E = {N}_{1} \oplus  \cdots  \oplus  {N}_{s} \) follows from the primary decomposition theorem (see 2.1, theorem 1).

- Pour tout \( i \) , la restriction \( {f}_{i} \) de \( f \) à \( {N}_{i} \) vérifie \( {\left( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}}\right) }^{{\alpha }_{i}} = 0 \) . En d’autres termes, \( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) est nilpotente, donc d’après 1.2 proposition 3, le polynôme caractéristique de \( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) est \( {\left( -X\right) }^{\dim {N}_{i}} \) , donc celui de \( {f}_{i} \) est \( {\left( {\lambda }_{i} - X\right) }^{\dim {N}_{i}} \) . Or \( {P}_{{f}_{i}} \) divise \( {P}_{f} \) d’après la proposition 2 de la page 173, et donc dim \( {N}_{i} \leq  {\alpha }_{i}\;\left( *\right) \) .

> - For any \( i \) , the restriction \( {f}_{i} \) of \( f \) to \( {N}_{i} \) satisfies \( {\left( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}}\right) }^{{\alpha }_{i}} = 0 \) . In other words, \( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) is nilpotent, so according to 1.2 proposition 3, the characteristic polynomial of \( {f}_{i} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) is \( {\left( -X\right) }^{\dim {N}_{i}} \) , therefore that of \( {f}_{i} \) is \( {\left( {\lambda }_{i} - X\right) }^{\dim {N}_{i}} \) . However, \( {P}_{{f}_{i}} \) divides \( {P}_{f} \) according to proposition 2 on page 173, and thus dim \( {N}_{i} \leq  {\alpha }_{i}\;\left( *\right) \) .

Comme \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) , on a \( n = \mathop{\sum }\limits_{{i = 1}}^{s}\dim {N}_{i} \) . De plus \( \mathop{\sum }\limits_{{i = 1}}^{s}{\alpha }_{i} = n \) , et on en déduit avec \( \left( *\right) \) que \( \dim {N}_{i} = {\alpha }_{i} \) pour tout \( i \) .

> Since \( E = {N}_{1} \oplus \cdots \oplus {N}_{s} \) , we have \( n = \mathop{\sum }\limits_{{i = 1}}^{s}\dim {N}_{i} \) . Furthermore \( \mathop{\sum }\limits_{{i = 1}}^{s}{\alpha }_{i} = n \) , and we deduce from \( \left( *\right) \) that \( \dim {N}_{i} = {\alpha }_{i} \) for any \( i \) .

Définition 2 (INDICE D’UN ENDOMORPHISME). Soit \( f \in \mathcal{L}\left( E\right) \) . Il existe un unique entier naturel \( r \) tel que

> Definition 2 (INDEX OF AN ENDOMORPHISM). Let \( f \in \mathcal{L}\left( E\right) \) . There exists a unique natural integer \( r \) such that

\[
\{ 0\}  = \operatorname{Ker}{f}^{0} \subsetneq  \operatorname{Ker}f \subsetneq  \cdots  \subsetneq  \operatorname{Ker}{f}^{r} = \operatorname{Ker}{f}^{r + 1} = \operatorname{Ker}{f}^{r + 2} = \cdots  = \operatorname{Ker}{f}^{q} = \cdots .
\]

L’entier \( r \) s’appelle l’indice de \( f \) . C’est aussi le plus petit entier naturel tel que Ker \( {f}^{r} = \) Ker \( {f}^{r + 1} \) .

> The integer \( r \) is called the index of \( f \) . It is also the smallest natural integer such that Ker \( {f}^{r} = \) Ker \( {f}^{r + 1} \) .

Démonstration. On part du fait que

> Proof. We start from the fact that

\[
\forall p \in  \mathbb{N},\operatorname{Ker}{f}^{p} \subset  \operatorname{Ker}{f}^{p + 1}
\]

(*)

> (en effet, si \( x \in \operatorname{Ker}{f}^{p} \) , alors \( {f}^{p}\left( x\right) = 0 \) donc \( {f}^{p + 1}\left( x\right) = f\left( {{f}^{p}\left( x\right) }\right) = 0 \) ). On en déduit en particulier que pour tout \( p,\dim \left( {\operatorname{Ker}{f}^{p}}\right) \leq \dim \left( {\operatorname{Ker}{f}^{p + 1}}\right) \) . Autrement dit, la suite \( {\left( {u}_{p}\right) }_{p \in \mathbb{N}} \) définie par \( {u}_{p} = \dim \left( {\operatorname{Ker}{f}^{p}}\right) \) est croissante. Cette suite est à valeurs dans \( I = \{ 0,1\ldots , n\} \) . L’ensemble \( I \) étant fini, \( \left( {u}_{p}\right) \) étant croissante, l’entier \( r = \inf \left\{ {p \in \mathbb{N} \mid {u}_{p} = {u}_{p + 1}}\right\} \) existe. On a alors

(indeed, if \( x \in \operatorname{Ker}{f}^{p} \) , then \( {f}^{p}\left( x\right) = 0 \) therefore \( {f}^{p + 1}\left( x\right) = f\left( {{f}^{p}\left( x\right) }\right) = 0 \) ). We deduce in particular that for all \( p,\dim \left( {\operatorname{Ker}{f}^{p}}\right) \leq \dim \left( {\operatorname{Ker}{f}^{p + 1}}\right) \) . In other words, the sequence \( {\left( {u}_{p}\right) }_{p \in \mathbb{N}} \) defined by \( {u}_{p} = \dim \left( {\operatorname{Ker}{f}^{p}}\right) \) is increasing. This sequence takes values in \( I = \{ 0,1\ldots , n\} \) . Since the set \( I \) is finite and \( \left( {u}_{p}\right) \) is increasing, the integer \( r = \inf \left\{ {p \in \mathbb{N} \mid {u}_{p} = {u}_{p + 1}}\right\} \) exists. We then have

> - Pour tout \( p < r \) , \( \operatorname{Ker}{f}^{p} \subsetneq  \operatorname{Ker}{f}^{p + 1} \) (d’après \( \left( *\right) \) et parce que \( {u}_{p} < {u}_{p + 1} \) ).

- For all \( p < r \) , \( \operatorname{Ker}{f}^{p} \subsetneq  \operatorname{Ker}{f}^{p + 1} \) (according to \( \left( *\right) \) and because \( {u}_{p} < {u}_{p + 1} \) ).

> - Ker \( {f}^{r} = \operatorname{Ker}{f}^{r + 1} \) (d’après (*) et parce que \( {u}_{r} = {u}_{r + 1} \) ).

- Ker \( {f}^{r} = \operatorname{Ker}{f}^{r + 1} \) (according to (*) and because \( {u}_{r} = {u}_{r + 1} \) ).

> - Pour tout \( p \geq  r \) , \( \operatorname{Ker}{f}^{p} = \operatorname{Ker}{f}^{p + 1} \) car

- For all \( p \geq  r \) , \( \operatorname{Ker}{f}^{p} = \operatorname{Ker}{f}^{p + 1} \) because

\[
\operatorname{Ker}{f}^{p + 1} = \left\{  {x \in  E \mid  {f}^{r + 1}\left( {{f}^{p - r}\left( x\right) }\right)  = 0}\right\}
\]

\[
= \left\{  {x \in  E \mid  {f}^{p - r}\left( x\right)  \in  \operatorname{Ker}{f}^{r + 1}}\right\}   = \left\{  {x \in  E \mid  {f}^{p - r}\left( x\right)  \in  \operatorname{Ker}{f}^{r}}\right\}   = \operatorname{Ker}{f}^{p}.
\]

L'unicité est évidente.

> Uniqueness is obvious.

Remarque 1. - Les propriétés vérifiées par \( r \) montrent que l’indice \( r \) de \( f \) est aussi l'unique entier naturel vérifiant

> Remark 1. - The properties satisfied by \( r \) show that the index \( r \) of \( f \) is also the unique natural integer satisfying

\[
\forall q < r,\;\dim \operatorname{Ker}{f}^{q} < \dim \operatorname{Ker}{f}^{r}\;\text{ et }\;\forall q \geq  r,\;\dim \operatorname{Ker}{f}^{q} = \dim \operatorname{Ker}{f}^{r}.
\]

- Si \( f \) est nilpotente, l’indice \( r \) de \( f \) n’est autre que \( \inf \left\{  {p \mid  {f}^{p} = 0}\right\} \) , c’est-à-dire l’indice de nilpotence de \( f \) .

> - If \( f \) is nilpotent, the index \( r \) of \( f \) is none other than \( \inf \left\{  {p \mid  {f}^{p} = 0}\right\} \), that is to say the index of nilpotency of \( f \).

- On peut montrer que si \( r \) est l’indice de \( f \) , alors

> - It can be shown that if \( r \) is the index of \( f \), then

\[
\operatorname{Ker}{f}^{r} \oplus  \operatorname{Im}{f}^{r} = E.
\]

- L’indice \( r \) de \( f \) vérifie aussi la propriété

> - The index \( r \) of \( f \) also satisfies the property

\[
E = \operatorname{Im}{f}^{0} \supsetneq  \operatorname{Im}f \supsetneq  \cdots  \supsetneq  \operatorname{Im}{f}^{r} = \operatorname{Im}{f}^{r + 1} = \operatorname{Im}{f}^{r + 2} = \cdots  = \operatorname{Im}{f}^{q} = \cdots .
\]

- Ces résultats sont à rapprocher de celui de la question 1/ a) du problème 2 page 155.

> - These results are to be compared with that of question 1/ a) of problem 2 on page 155.

THÉORÉME 1. Soit \( f \in \mathcal{L}\left( E\right) \) tel que son polynôme caractéristique \( {P}_{f} \) soit scindé sur \( \mathbb{K} \) : \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \) . Alors

> THEOREM 1. Let \( f \in \mathcal{L}\left( E\right) \) be such that its characteristic polynomial \( {P}_{f} \) is split over \( \mathbb{K} \): \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{\alpha }_{i}} \). Then

(i) Le polynôme minimal \( {\Pi }_{f} \) de \( f \) est de la forme

> (i) The minimal polynomial \( {\Pi }_{f} \) of \( f \) is of the form

\[
{\Pi }_{f}\left( X\right)  = \mathop{\prod }\limits_{{i = 1}}^{s}{\left( X - {\lambda }_{i}\right) }^{{r}_{i}}\;\text{ avec }\;\forall i,1 \leq  {r}_{i} \leq  {\alpha }_{i}.
\]

(ii) L’ordre de multiplicité \( {r}_{i} \) de \( {\lambda }_{i} \) dans \( {\Pi }_{f} \) est l’indice de l’endomorphisme (f- \( \left. {{\lambda }_{i}{\mathrm{{Id}}}_{E}}\right) \)

> (ii) The multiplicity order \( {r}_{i} \) of \( {\lambda }_{i} \) in \( {\Pi }_{f} \) is the index of the endomorphism (f- \( \left. {{\lambda }_{i}{\mathrm{{Id}}}_{E}}\right) \)

Démonstration. (i) est démontré à la remarque 6 page 187.

> Proof. (i) is proven in remark 6 on page 187.

(ii) Pour alléger les notations, nous allons montrer (ii) pour \( i = 1 \) . On pose \( Q = \mathop{\prod }\limits_{{i = 2}}^{s}{\left( X - {\lambda }_{i}\right) }^{{r}_{i}} \) , de sorte que \( {\Pi }_{f} = {\left( X - {\lambda }_{1}\right) }^{{r}_{1}}Q \) . Comme \( {\left( X - {\lambda }_{1}\right) }^{{r}_{1}} \) et \( Q \) sont premiers entre eux, on a, en appliquant le théorème de décomposition des noyaux (voir le théorème 1 page 185),

> (ii) To simplify the notation, we will show (ii) for \( i = 1 \). We set \( Q = \mathop{\prod }\limits_{{i = 2}}^{s}{\left( X - {\lambda }_{i}\right) }^{{r}_{i}} \), so that \( {\Pi }_{f} = {\left( X - {\lambda }_{1}\right) }^{{r}_{1}}Q \). Since \( {\left( X - {\lambda }_{1}\right) }^{{r}_{1}} \) and \( Q \) are coprime, we have, by applying the primary decomposition theorem (see theorem 1 on page 185),

\[
E = \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} \oplus  M\text{ avec }M = \operatorname{Ker}Q\left( f\right) .
\]

On en déduit dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} + \dim M = n\;\left( *\right) \) .

> We deduce dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} + \dim M = n\;\left( *\right) \).

Soit \( q \) un entier naturel. On pose \( P = {\left( X - {\lambda }_{1}\right) }^{q}Q \) . En appliquant le théorème de décomposition des noyaux, on a

> Let \( q \) be a natural integer. We set \( P = {\left( X - {\lambda }_{1}\right) }^{q}Q \). By applying the primary decomposition theorem, we have

\[
\operatorname{Ker}P\left( f\right)  = \operatorname{Ker}{\left( f - {\lambda }_{1}\mathrm{{Id}}\right) }^{q} \oplus  \operatorname{Ker}Q\left( f\right)  = \operatorname{Ker}{\left( f - {\lambda }_{1}\mathrm{{Id}}\right) }^{q} \oplus  M.
\]

On en déduit dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{q} + \dim M = \dim \operatorname{Ker}P\left( f\right) \;\left( {* * }\right) \) .

> We deduce dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{q} + \dim M = \dim \operatorname{Ker}P\left( f\right) \;\left( {* * }\right) \).

- Si \( q \geq  {r}_{1} \) , alors \( {\Pi }_{f} \) divise \( P \) donc \( P\left( f\right)  = 0 \) , i.e Ker \( P\left( f\right)  = E \) , donc avec \( \left( *\right) \) et \( \left( {* * }\right) \) , on tire dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{q} = \dim \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} \) .

> - If \( q \geq  {r}_{1} \), then \( {\Pi }_{f} \) divides \( P \) so \( P\left( f\right)  = 0 \), i.e. Ker \( P\left( f\right)  = E \), therefore with \( \left( *\right) \) and \( \left( {* * }\right) \), we obtain dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{q} = \dim \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} \).

- Si maintenant \( q < {r}_{1} \) , alors \( {\Pi }_{f} \) ne divise pas \( P \) , donc \( P\left( f\right)  \neq  0 \) , i.e Ker \( P\left( f\right)  \neq  E \) , et d’après \( \left( *\right) \) et \( \left( {* * }\right) \) , on tire dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{q} < \dim \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} \) .

> - If now \( q < {r}_{1} \) , then \( {\Pi }_{f} \) does not divide \( P \) , so \( P\left( f\right)  \neq  0 \) , i.e. Ker \( P\left( f\right)  \neq  E \) , and according to \( \left( *\right) \) and \( \left( {* * }\right) \) , we obtain dim \( \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{q} < \dim \operatorname{Ker}{\left( f - {\lambda }_{1}\operatorname{Id}\right) }^{{r}_{1}} \) .

On en déduit que l’indice de l’endomorphisme \( f - {\lambda }_{1}{\operatorname{Id}}_{E} \) est \( {r}_{1} \) (voir la remarque 1).

> We deduce that the index of the endomorphism \( f - {\lambda }_{1}{\operatorname{Id}}_{E} \) is \( {r}_{1} \) (see remark 1).

Remarque 2. - En conséquence, les sous-espaces caractéristiques \( {N}_{i} \) de \( f \) sont égaux à \( \operatorname{Ker}{\left( f - {\lambda }_{i}\right) }^{{r}_{i}} \) .

> Remark 2. - Consequently, the characteristic subspaces \( {N}_{i} \) of \( f \) are equal to \( \operatorname{Ker}{\left( f - {\lambda }_{i}\right) }^{{r}_{i}} \) .

- Pour tout \( i,{r}_{i} \) est aussi l’indice de nilpotence de l’endomorphisme \( {f}_{\mid {N}_{i}} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) .

> - For all \( i,{r}_{i} \) is also the index of nilpotency of the endomorphism \( {f}_{\mid {N}_{i}} - {\lambda }_{i}{\operatorname{Id}}_{{N}_{i}} \) .

- Ce théorème permet de calculer le polynôme minimal de \( f \) : on commence par calculer le polynôme caractéristique de \( f \) , puis on calcule ensuite pour tout \( i \) l’indice de \( f - {\lambda }_{i} \) Id (dans la pratique, les calculs peuvent être longs).

> - This theorem allows us to calculate the minimal polynomial of \( f \) : we start by calculating the characteristic polynomial of \( f \) , then we calculate for all \( i \) the index of \( f - {\lambda }_{i} \) Id (in practice, the calculations can be long).
