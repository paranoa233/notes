#### 2.4. Group acting on a set

*Français : 2.4. Groupe opérant sur un ensemble*

Dans cette partie, \( G \) désigne un groupe dont l’élément neutre est noté \( e, X \) un ensemble quelconque.

> In this part, \( G \) denotes a group whose identity element is denoted by \( e, X \) an arbitrary set.

Définition 16. On dit que \( G \) opère sur \( X \) s’il existe une application

> Definition 16. We say that \( G \) acts on \( X \) if there exists a mapping

\[
G \times  X \rightarrow  X\;\left( {s, x}\right)  \mapsto  s \cdot  x
\]

telle que

> such that

(i) \( \forall \left( {s, t}\right) \in {G}^{2},\forall x \in X, s \cdot \left( {t \cdot x}\right) = \left( {st}\right) \cdot x \)

> (ii) \( \forall x \in X, e \cdot x = x \) .

(ii) \( \forall x \in X, e \cdot x = x \) .

> (Remarquer l'analogie avec un espace vectoriel sur un corps K.)

(Note the analogy with a vector space over a field K.)

> Exemple 7. - Le groupe \( G \) opère sur lui même par l’application

Example 7. - The group \( G \) acts on itself by the map

\[
G \times  G \rightarrow  G\;\left( {s, x}\right)  \mapsto  {sx}.
\]

- Le groupe des permutations \( S \) d’un ensemble \( X \) opère sur \( X \) par l’application

> - The permutation group \( S \) of a set \( X \) acts on \( X \) by the map

\[
S \times  X \rightarrow  X\;\left( {s, x}\right)  \mapsto  s\left( x\right) .
\]

Équivalence d'intransitivité. Dans ce paragraphe, \( G \) est un groupe opérant sur un ensemble \( X \) .

> Equivalence of intransitivity. In this paragraph, \( G \) is a group acting on a set \( X \) .

DéFINITION 17. La relation sur \( X \) définie par

> DEFINITION 17. The relation on \( X \) defined by

\[
x\mathcal{T}y \Leftrightarrow  \exists s \in  G, y = s \cdot  x
\]

est une relation d'équivalence, appelée relation d'intransitivité. La classe d'équivalence d’un élément \( x \) de \( X \) est \( {G}_{x} = \{ s \cdot x \mid s \in G\} \) , on l’appelle classe d’intransitivité (ou orbite, ou trajectoire) de \( x \) .

> is an equivalence relation, called the relation of intransitivity. The equivalence class of an element \( x \) of \( X \) is \( {G}_{x} = \{ s \cdot x \mid s \in G\} \) , it is called the intransitivity class (or orbit, or trajectory) of \( x \) .

DÉFINITION 18. Le stabilisateur d’un élément \( x \) de \( X \) est le sous-ensemble de \( G \) défini par \( {S}_{x} = \{ s \in G \mid s \cdot x = x\} \) .

> DEFINITION 18. The stabilizer of an element \( x \) of \( X \) is the subset of \( G \) defined by \( {S}_{x} = \{ s \in G \mid s \cdot x = x\} \) .

Proposition 8. Pour tout élément \( x \) de \( X,{S}_{x} \) est un sous-groupe de \( G \) .

> Proposition 8. For any element \( x \) of \( X,{S}_{x} \) is a subgroup of \( G \) .

Démonstration. L’ensemble \( {S}_{x} \) n’est pas vide car \( e \in {S}_{x} \) . Par ailleurs, pour tout \( s, t \in G \) on a \( t \cdot x = x \) donc \( x = {t}^{-1} \cdot \left( {t \cdot x}\right) = {t}^{-1} \cdot x \) . Ainsi, \( \left( {s{t}^{-1}}\right) \cdot x = s \cdot \left( {{t}^{-1} \cdot x}\right) = s \cdot x = x \) , d’où \( s{t}^{-1} \in {S}_{x} \) .

> Proof. The set \( {S}_{x} \) is not empty because \( e \in {S}_{x} \) . Furthermore, for any \( s, t \in G \) we have \( t \cdot x = x \) so \( x = {t}^{-1} \cdot \left( {t \cdot x}\right) = {t}^{-1} \cdot x \) . Thus, \( \left( {s{t}^{-1}}\right) \cdot x = s \cdot \left( {{t}^{-1} \cdot x}\right) = s \cdot x = x \) , hence \( s{t}^{-1} \in {S}_{x} \) .

THÉORÉME 7. Si \( G \) est fini, pour tout \( x \in X \) on a \( \operatorname{Card}\left( G\right) = \operatorname{Card}\left( {G}_{x}\right) \cdot \operatorname{Card}\left( {S}_{x}\right) \) .

> THEOREM 7. If \( G \) is finite, for any \( x \in X \) we have \( \operatorname{Card}\left( G\right) = \operatorname{Card}\left( {G}_{x}\right) \cdot \operatorname{Card}\left( {S}_{x}\right) \) .

Démonstration. On fixe \( x \) . Soit \( {\mathcal{R}}_{x} \) la relation d’équivalence sur \( G \) définie par : \( s{\mathcal{R}}_{x}t \Leftrightarrow \; s \cdot x = t \cdot x \) . On a \( s{\mathcal{R}}_{x}t \Leftrightarrow \left( {{t}^{-1}s}\right) \cdot x = x \Leftrightarrow {t}^{-1}s \in {S}_{x} \Leftrightarrow s \in t{S}_{x} \) . Les classes d’équivalences sont donc de la forme \( t{S}_{x}, t \in G \) , ce qui montre qu’elles sont toutes de cardinal \( \operatorname{Card}\left( {S}_{x}\right) \) . Il y a autant de classes d’équivalences que de valeurs prises par \( s \cdot x, s \in G \) , c’est-à-dire qu’il y a Card \( \left( {G}_{x}\right) \) classes d’équivalence. Donc \( \operatorname{Card}\left( G\right) = \operatorname{Card}\left( {G}_{x}\right) \cdot \operatorname{Card}\left( {S}_{x}\right) \) .

> Proof. We fix \( x \) . Let \( {\mathcal{R}}_{x} \) be the equivalence relation on \( G \) defined by: \( s{\mathcal{R}}_{x}t \Leftrightarrow \; s \cdot x = t \cdot x \) . We have \( s{\mathcal{R}}_{x}t \Leftrightarrow \left( {{t}^{-1}s}\right) \cdot x = x \Leftrightarrow {t}^{-1}s \in {S}_{x} \Leftrightarrow s \in t{S}_{x} \) . The equivalence classes are therefore of the form \( t{S}_{x}, t \in G \) , which shows that they all have cardinality \( \operatorname{Card}\left( {S}_{x}\right) \) . There are as many equivalence classes as there are values taken by \( s \cdot x, s \in G \) , that is to say there are Card \( \left( {G}_{x}\right) \) equivalence classes. Therefore \( \operatorname{Card}\left( G\right) = \operatorname{Card}\left( {G}_{x}\right) \cdot \operatorname{Card}\left( {S}_{x}\right) \) .

COROLLAIRE 1 (ÉQUATION AUX CLASSES). Si \( X \) et \( G \) sont finis, en désignant par \( \Theta \) une partie de \( X \) contenant exactement un représentant de chacune des classes d’intransitivité, on a

> COROLLARY 1 (CLASS EQUATION). If \( X \) and \( G \) are finite, by denoting by \( \Theta \) a subset of \( X \) containing exactly one representative of each of the intransitivity classes, we have

\[
\operatorname{Card}\left( X\right)  = \mathop{\sum }\limits_{{x \in  \Theta }}\operatorname{Card}\left( {G}_{x}\right)  = \mathop{\sum }\limits_{{x \in  \Theta }}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {S}_{x}\right) }.
\]

Application aux automorphismes intérieurs.

> Application to inner automorphisms.

THÉORÉME 8. Soit \( G \) un groupe fini. Il existe une famille finie de sous-groupes stricts de \( G \) (i.e. \( \neq \{ e\} {et} \neq G \) ) \( {\left( {H}_{i}\right) }_{i \in I} \) telle que

> THEOREM 8. Let \( G \) be a finite group. There exists a finite family of proper subgroups of \( G \) (i.e. \( \neq \{ e\} {et} \neq G \) ) \( {\left( {H}_{i}\right) }_{i \in I} \) such that

\[
\operatorname{Card}\left( G\right)  = \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right)  + \mathop{\sum }\limits_{{i \in  I}}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {H}_{i}\right) }
\]

où \( \mathcal{Z}\left( G\right) \) désigne le centre du groupe \( G \) .

> where \( \mathcal{Z}\left( G\right) \) denotes the center of the group \( G \) .

Démonstration. Faisons opérer \( G \) sur lui même par les automorphismes intérieurs : \( G \times G \rightarrow \; G,\;\left( {s, x}\right) \mapsto {\varphi }_{s}\left( x\right) = {sx}{s}^{-1} \) . Si \( x \in G \) , on a \( {G}_{x} = \left\{ {{sx}{s}^{-1} \mid s \in G}\right\} \) et \( {S}_{x} = \{ s \in G \mid {sx} = {xs}\} \) (dans ce cas, \( {S}_{x} \) est aussi appelé centralisateur ou normalisateur de \( x \) ). D’après le corollaire précédent il existe \( \Theta \subset G \) tel que

> Proof. Let \( G \) act on itself by inner automorphisms: \( G \times G \rightarrow \; G,\;\left( {s, x}\right) \mapsto {\varphi }_{s}\left( x\right) = {sx}{s}^{-1} \) . If \( x \in G \) , we have \( {G}_{x} = \left\{ {{sx}{s}^{-1} \mid s \in G}\right\} \) and \( {S}_{x} = \{ s \in G \mid {sx} = {xs}\} \) (in this case, \( {S}_{x} \) is also called the centralizer or normalizer of \( x \) ). According to the previous corollary, there exists \( \Theta \subset G \) such that

\[
\operatorname{Card}\left( G\right)  = \mathop{\sum }\limits_{{x \in  \Theta }}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {S}_{x}\right) }.
\]

Or \( {S}_{x} = G \Leftrightarrow \forall s \in G,{sx} = {xs} \Leftrightarrow x \in \mathcal{Z}\left( G\right) \) . En notant \( {\Theta }^{\prime } = \Theta \smallsetminus \mathcal{Z}\left( G\right) \) , on a donc

> However, \( {S}_{x} = G \Leftrightarrow \forall s \in G,{sx} = {xs} \Leftrightarrow x \in \mathcal{Z}\left( G\right) \) . By denoting \( {\Theta }^{\prime } = \Theta \smallsetminus \mathcal{Z}\left( G\right) \) , we therefore have

\[
\operatorname{Card}\left( G\right)  = \mathop{\sum }\limits_{{x \in  \mathcal{Z}\left( G\right) }}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {S}_{x}\right) } + \mathop{\sum }\limits_{{x \in  {\Theta }^{\prime }}}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {S}_{x}\right) } = \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right)  + \mathop{\sum }\limits_{{x \in  {\Theta }^{\prime }}}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {S}_{x}\right) },
\]

d’où le théorème car les \( {\left( {S}_{x}\right) }_{x \in {\Theta }^{\prime }} \) constituent une famille finie de sous-groupes stricts de \( G \) (ce sont des sous-groupes d’après la proposition 8, différents de \( G \) car \( x \notin \mathcal{Z}\left( G\right) \) , différents de \( \{ e\} \) car \( \{ e, x\} \subset {G}_{x} \) ).

> whence the theorem, because the \( {\left( {S}_{x}\right) }_{x \in {\Theta }^{\prime }} \) constitute a finite family of proper subgroups of \( G \) (they are subgroups according to proposition 8, distinct from \( G \) because \( x \notin \mathcal{Z}\left( G\right) \) , distinct from \( \{ e\} \) because \( \{ e, x\} \subset {G}_{x} \) ).

Remarque 10. Ce dernier résultat est très puissant car il permet d'avoir des renseignements sur \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \) connaissant a priori la forme des ordres des sous-groupes de \( G \) (voir l'exercice 11 page 29, le problème 9 page 44 et le problème 11 page 45). Cependant, cette formule n'est pas au programme de mathématiques spéciales et il faut au besoin savoir la redémontrer.

> Remark 10. This last result is very powerful because it allows one to obtain information about \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \) knowing a priori the form of the orders of the subgroups of \( G \) (see exercise 11 on page 29, problem 9 on page 44, and problem 11 on page 45). However, this formula is not in the special mathematics curriculum and one must know how to re-prove it if necessary.
