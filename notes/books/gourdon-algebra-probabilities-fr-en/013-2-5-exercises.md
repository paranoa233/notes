#### 2.5. Exercises

*Français : 2.5. Exercices*

EXERCICE 1. Soit \( G \) un groupe quelconque, soient \( x, y \in G \) . On suppose que \( {xy} \) est d’ordre fini \( p \) dans \( G \) . Montrer que \( {yx} \) est également fini d’ordre \( p \) .

> EXERCISE 1. Let \( G \) be an arbitrary group, let \( x, y \in G \) . Suppose that \( {xy} \) is of finite order \( p \) in \( G \) . Show that \( {yx} \) is also finite of order \( p \) .

Solution. Si \( x \) et \( y \) commutent, c’est bien sûr évident. Plaçons nous maintenant dans le cas général. On commence par remarquer que pour tout \( n \in {\mathbb{N}}^{ * } \) ,

> Solution. If \( x \) and \( y \) commute, it is of course obvious. Let us now consider the general case. We begin by noting that for all \( n \in {\mathbb{N}}^{ * } \) ,

\[
{\left( xy\right) }^{n} = \underset{n\text{ termes }}{\underbrace{\left( {xy}\right) \cdots \left( {xy}\right) }} = x\underset{n - 1\text{ termes }}{\underbrace{\left( {yx}\right) \cdots \left( {yx}\right) }}y = x{\left( yx\right) }^{n - 1}y.
\]

Ainsi, en désignant par \( e \) l’élément neutre de \( G \) , on a

> Thus, by denoting by \( e \) the identity element of \( G \) , we have

\[
{\left( xy\right) }^{n} = e \Leftrightarrow  x{\left( yx\right) }^{n - 1}y = e \Leftrightarrow  {yx}{\left( yx\right) }^{n - 1}y = y \Leftrightarrow  {\left( yx\right) }^{n} = e
\]

ce qui prouve que les ordres de \( {xy} \) et de \( {yx} \) sont identiques.

> which proves that the orders of \( {xy} \) and \( {yx} \) are identical.

EXERCICE 2. Soient \( G \) un groupe et \( {H}_{1},{H}_{2} \) deux sous-groupes de \( G \) .

> EXERCISE 2. Let \( G \) be a group and \( {H}_{1},{H}_{2} \) two subgroups of \( G \) .

a) On suppose que \( {H}_{1} \cup {H}_{2} \) est un sous-groupe de \( G \) . Montrer que \( {H}_{1} \subset {H}_{2} \) ou \( {H}_{2} \subset {H}_{1} \) . b) Si les ordres de \( {H}_{1} \) et \( {H}_{2} \) sont finis et premiers entre eux, que dire de \( {H}_{1} \cap {H}_{2} \) ?

> a) Assume \( {H}_{1} \cup {H}_{2} \) is a subgroup of \( G \). Show that \( {H}_{1} \subset {H}_{2} \) or \( {H}_{2} \subset {H}_{1} \). b) If the orders of \( {H}_{1} \) and \( {H}_{2} \) are finite and coprime, what can be said about \( {H}_{1} \cap {H}_{2} \)?

Solution. a) Raisonnons par l’absurde. Si \( {H}_{1} \text{ ⊄ } {H}_{2} \) et \( {H}_{2} \text{ ⊄ } {H}_{1} \) , il existe \( {x}_{1} \in {H}_{1},{x}_{1} \notin {H}_{2} \) et il existe \( {x}_{2} \in {H}_{2},{x}_{2} \notin {H}_{1} \) . Comme \( {H}_{1} \cup {H}_{2} \) est un sous-groupe, le produit \( {x}_{1}{x}_{2} \) appartient à \( {H}_{1} \cup {H}_{2} \) . Si \( {x}_{1}{x}_{2} \in {H}_{1} \) , alors \( {x}_{2} = {x}_{1}^{-1}\left( {{x}_{1}{x}_{2}}\right) \in {H}_{1} \) , ce qui est absurde. De même, on parvient à une absurdité en supposant \( {x}_{1}{x}_{2} \in {H}_{2} \) . D’où le résultat.

> Solution. a) Let us reason by contradiction. If \( {H}_{1} \text{ ⊄ } {H}_{2} \) and \( {H}_{2} \text{ ⊄ } {H}_{1} \), there exists \( {x}_{1} \in {H}_{1},{x}_{1} \notin {H}_{2} \) and there exists \( {x}_{2} \in {H}_{2},{x}_{2} \notin {H}_{1} \). Since \( {H}_{1} \cup {H}_{2} \) is a subgroup, the product \( {x}_{1}{x}_{2} \) belongs to \( {H}_{1} \cup {H}_{2} \). If \( {x}_{1}{x}_{2} \in {H}_{1} \), then \( {x}_{2} = {x}_{1}^{-1}\left( {{x}_{1}{x}_{2}}\right) \in {H}_{1} \), which is absurd. Similarly, we reach an absurdity by assuming \( {x}_{1}{x}_{2} \in {H}_{2} \). Hence the result.

b) On sait que \( {H}_{1} \cap {H}_{2} \) est un sous-groupe de \( {H}_{1} \) et \( {H}_{2} \) . Ainsi, l’ordre de \( {H}_{1} \cap {H}_{2} \) divise l’ordre de \( {H}_{1} \) et l’ordre de \( {H}_{2} \) , et vaut donc 1. Finalement, en désignant par \( e \) l’élément neutre de \( G \) , on a \( {H}_{1} \cap {H}_{2} = \{ e\} \) .

> b) We know that \( {H}_{1} \cap {H}_{2} \) is a subgroup of \( {H}_{1} \) and \( {H}_{2} \). Thus, the order of \( {H}_{1} \cap {H}_{2} \) divides the order of \( {H}_{1} \) and the order of \( {H}_{2} \), and is therefore equal to 1. Finally, denoting by \( e \) the identity element of \( G \), we have \( {H}_{1} \cap {H}_{2} = \{ e\} \).

EXERCICE 3. Soient \( G \) un groupe et \( {H}_{1},{H}_{2} \) deux sous-groupes de \( G \) . On pose \( {H}_{1}{H}_{2} = \; \left\{ {{xy} \mid x \in {H}_{1}, y \in {H}_{2}}\right\} . \)

> EXERCISE 3. Let \( G \) be a group and \( {H}_{1},{H}_{2} \) be two subgroups of \( G \). Let \( {H}_{1}{H}_{2} = \; \left\{ {{xy} \mid x \in {H}_{1}, y \in {H}_{2}}\right\} . \)

a) A quelle condition nécessaire et suffisante \( {H}_{1}{H}_{2} \) est-il un sous-groupe de \( G \) ?

> a) What is the necessary and sufficient condition for \( {H}_{1}{H}_{2} \) to be a subgroup of \( G \)?

b) Si \( {H}_{1} \) et \( {H}_{2} \) sont finis et si \( {H}_{1} \cap {H}_{2} = \{ e\} \) (où \( e \) désigne l’élément neutre de \( G \) ), montrer \( \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) = \operatorname{Card}\left( {H}_{1}\right) \cdot \operatorname{Card}\left( {H}_{2}\right) . \)

> b) If \( {H}_{1} \) and \( {H}_{2} \) are finite and if \( {H}_{1} \cap {H}_{2} = \{ e\} \) (where \( e \) denotes the identity element of \( G \)), show \( \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) = \operatorname{Card}\left( {H}_{1}\right) \cdot \operatorname{Card}\left( {H}_{2}\right) . \)

c) On suppose \( G \) abélien, \( {H}_{1} \) et \( {H}_{2} \) d’ordres finis \( p \) et \( q \) , où \( p \) et \( q \) sont deux nombres premiers distincts. Montrer que \( {H}_{1}{H}_{2} \) est un sous-groupe cyclique de \( G \) .

> c) Assume \( G \) is abelian, \( {H}_{1} \) and \( {H}_{2} \) have finite orders \( p \) and \( q \), where \( p \) and \( q \) are two distinct prime numbers. Show that \( {H}_{1}{H}_{2} \) is a cyclic subgroup of \( G \).

Solution. a) Nous allons montrer que \( {H}_{1}{H}_{2} \) est un sous-groupe de \( G \) si et seulement si \( {H}_{1}{H}_{2} = \; {\mathrm{H}}_{2}{\mathrm{H}}_{1} \) .

> Solution. a) We will show that \( {H}_{1}{H}_{2} \) is a subgroup of \( G \) if and only if \( {H}_{1}{H}_{2} = \; {\mathrm{H}}_{2}{\mathrm{H}}_{1} \).

Condition nécessaire. Soit \( a \in {H}_{1}{H}_{2} \) . Alors \( {a}^{-1} \in {H}_{1}{H}_{2} \) autrement dit \( \exists \left( {x, y}\right) \in {H}_{1} \times {H}_{2},{a}^{-1} = \; {xy} \) . Ainsi \( a = {y}^{-1}{x}^{-1} \) , d’où \( a \in {H}_{2}{H}_{1} \) . Donc \( {H}_{1}{H}_{2} \subset {H}_{2}{H}_{1} \) .

> Necessary condition. Let \( a \in {H}_{1}{H}_{2} \) . Then \( {a}^{-1} \in {H}_{1}{H}_{2} \) in other words \( \exists \left( {x, y}\right) \in {H}_{1} \times {H}_{2},{a}^{-1} = \; {xy} \) . Thus \( a = {y}^{-1}{x}^{-1} \) , hence \( a \in {H}_{2}{H}_{1} \) . Therefore \( {H}_{1}{H}_{2} \subset {H}_{2}{H}_{1} \) .

Il reste à montrer l’inclusion réciproque. Soit \( a = {yx} \in {H}_{2}{H}_{1} \) avec \( x \in {H}_{1} \) et \( y \in {H}_{2} \) . Comme \( {a}^{-1} = {x}^{-1}{y}^{-1} \in {H}_{1}{H}_{2} \) , on a \( a \in {H}_{1}{H}_{2} \) car \( {H}_{1}{H}_{2} \) est un sous-groupe. Ainsi, \( {H}_{2}{H}_{1} \subset {H}_{1}{H}_{2} \) .

> It remains to show the reverse inclusion. Let \( a = {yx} \in {H}_{2}{H}_{1} \) with \( x \in {H}_{1} \) and \( y \in {H}_{2} \) . Since \( {a}^{-1} = {x}^{-1}{y}^{-1} \in {H}_{1}{H}_{2} \) , we have \( a \in {H}_{1}{H}_{2} \) because \( {H}_{1}{H}_{2} \) is a subgroup. Thus, \( {H}_{2}{H}_{1} \subset {H}_{1}{H}_{2} \) .

Condition suffisante. Bien sûr, \( {H}_{1}{H}_{2} \neq \varnothing \) . Soient \( a, b \in {H}_{1}{H}_{2} \) . Il s’agit de montrer \( a{b}^{-1} \in {H}_{1}{H}_{2} \) . Écrivons \( a = {a}_{1}{a}_{2} \) et \( b = {b}_{1}{b}_{2} \) , avec \( {a}_{1},{b}_{1} \in {H}_{1} \) et \( {a}_{2},{b}_{2} \in {H}_{2} \) . On a \( a{b}^{-1} = {a}_{1}{a}_{2}{b}_{2}^{-1}{b}_{1}^{-1} = {a}_{1}{yx} \) avec \( y = {a}_{2}{b}_{2}^{-1} \in {H}_{2} \) et \( x = {b}_{1}^{-1} \in {H}_{1} \) . Comme \( {H}_{1}{H}_{2} = {H}_{2}{H}_{1} \) , il existe \( \left( {{x}^{\prime },{y}^{\prime }}\right) \in {H}_{1} \times {H}_{2} \) tel que \( {yx} = {x}^{\prime }{y}^{\prime } \) . Donc \( a{b}^{-1} = {a}_{1}{x}^{\prime }{y}^{\prime } = \left( {{a}_{1}{x}^{\prime }}\right) \left( {y}^{\prime }\right) \in {H}_{1}{H}_{2} \) , d’où le résultat.

> Sufficient condition. Of course, \( {H}_{1}{H}_{2} \neq \varnothing \) . Let \( a, b \in {H}_{1}{H}_{2} \) . We must show \( a{b}^{-1} \in {H}_{1}{H}_{2} \) . Let us write \( a = {a}_{1}{a}_{2} \) and \( b = {b}_{1}{b}_{2} \) , with \( {a}_{1},{b}_{1} \in {H}_{1} \) and \( {a}_{2},{b}_{2} \in {H}_{2} \) . We have \( a{b}^{-1} = {a}_{1}{a}_{2}{b}_{2}^{-1}{b}_{1}^{-1} = {a}_{1}{yx} \) with \( y = {a}_{2}{b}_{2}^{-1} \in {H}_{2} \) and \( x = {b}_{1}^{-1} \in {H}_{1} \) . Since \( {H}_{1}{H}_{2} = {H}_{2}{H}_{1} \) , there exists \( \left( {{x}^{\prime },{y}^{\prime }}\right) \in {H}_{1} \times {H}_{2} \) such that \( {yx} = {x}^{\prime }{y}^{\prime } \) . Therefore \( a{b}^{-1} = {a}_{1}{x}^{\prime }{y}^{\prime } = \left( {{a}_{1}{x}^{\prime }}\right) \left( {y}^{\prime }\right) \in {H}_{1}{H}_{2} \) , hence the result.

b) Considérons l'application

> b) Consider the map

\[
\varphi  : {H}_{1} \times  {H}_{2} \rightarrow  {H}_{1}{H}_{2}\;\left( {{x}_{1},{x}_{2}}\right)  \mapsto  {x}_{1}{x}_{2}.
\]

Elle est surjective (par construction de l’ensemble d’arrivée \( {H}_{1}{H}_{2} \) ), et injective car si \( \varphi \left( {{x}_{1},{x}_{2}}\right) = \; \varphi \left( {{y}_{1},{y}_{2}}\right) \) , alors \( {x}_{1}{x}_{2} = {y}_{1}{y}_{2} \) donc \( {y}_{1}^{-1}{x}_{1} = {y}_{2}{x}_{2}^{-1} \) , d’où \( {y}_{1}^{-1}{x}_{1} \in {H}_{1} \cap {H}_{2} = \{ e\} \) , donc \( {x}_{1} = {y}_{1} \) et donc \( {x}_{2} = {y}_{2} \) . Finalement, \( \varphi \) est une bijection, donc \( \operatorname{Card}\left( {H}_{1}\right) \cdot \operatorname{Card}\left( {H}_{2}\right) = \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) \) .

> It is surjective (by construction of the codomain \( {H}_{1}{H}_{2} \)), and injective because if \( \varphi \left( {{x}_{1},{x}_{2}}\right) = \; \varphi \left( {{y}_{1},{y}_{2}}\right) \), then \( {x}_{1}{x}_{2} = {y}_{1}{y}_{2} \) so \( {y}_{1}^{-1}{x}_{1} = {y}_{2}{x}_{2}^{-1} \), hence \( {y}_{1}^{-1}{x}_{1} \in {H}_{1} \cap {H}_{2} = \{ e\} \), therefore \( {x}_{1} = {y}_{1} \) and thus \( {x}_{2} = {y}_{2} \). Finally, \( \varphi \) is a bijection, so \( \operatorname{Card}\left( {H}_{1}\right) \cdot \operatorname{Card}\left( {H}_{2}\right) = \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) \).

c) Le groupe \( G \) étant ici abélien, on a \( {H}_{1}{H}_{2} = {H}_{2}{H}_{1} \) donc \( {H}_{1}{H}_{2} \) est un sous-groupe de \( G \) d’après a). Par ailleurs, on a \( \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) = {pq} \) d’après \( b) \) car \( {H}_{1} \cap {H}_{2} = \{ e\} \) (voir l’exercice précédent, question b)).

> c) Since the group \( G \) is abelian here, we have \( {H}_{1}{H}_{2} = {H}_{2}{H}_{1} \), so \( {H}_{1}{H}_{2} \) is a subgroup of \( G \) according to a). Furthermore, we have \( \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) = {pq} \) according to \( b) \) because \( {H}_{1} \cap {H}_{2} = \{ e\} \) (see the previous exercise, question b)).

Les sous-groupes \( {H}_{1} \) et \( {H}_{2} \) sont cycliques car leur ordre est un nombre premier. Soient \( x \in {H}_{1} \) et \( y \in {H}_{2} \) tels que \( {H}_{1} = \langle x\rangle \) et \( {H}_{2} = \langle y\rangle \) . Montrons que \( {H}_{1}{H}_{2} = \langle {xy}\rangle \) . Il s’agit de prouver que l’élément \( {xy} \) est d’ordre \( {pq} = \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) \) . Le fait que \( {\left( xy\right) }^{n} = e \) entraîne \( {x}^{n} = {\left( {y}^{-1}\right) }^{n} \) . Or \( {H}_{1} \cap {H}_{2} = \{ e\} \) , donc \( {x}^{n} = {\left( {y}^{-1}\right) }^{n} = e \) , donc \( p \mid n \) et \( q \mid n \) , et \( p \) et \( q \) étant premiers entre eux (car premiers et distincts), \( {pq} \mid n \) . Donc l’ordre de \( {xy} \) est supérieur à \( {pq} \) et comme il est toujours inférieur à \( \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) = {pq} \) , son ordre est bien \( {pq} \) .

> The subgroups \( {H}_{1} \) and \( {H}_{2} \) are cyclic because their order is a prime number. Let \( x \in {H}_{1} \) and \( y \in {H}_{2} \) be such that \( {H}_{1} = \langle x\rangle \) and \( {H}_{2} = \langle y\rangle \). Let us show that \( {H}_{1}{H}_{2} = \langle {xy}\rangle \). We must prove that the element \( {xy} \) is of order \( {pq} = \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) \). The fact that \( {\left( xy\right) }^{n} = e \) implies \( {x}^{n} = {\left( {y}^{-1}\right) }^{n} \). However, \( {H}_{1} \cap {H}_{2} = \{ e\} \), so \( {x}^{n} = {\left( {y}^{-1}\right) }^{n} = e \), therefore \( p \mid n \) and \( q \mid n \), and since \( p \) and \( q \) are coprime (because they are prime and distinct), \( {pq} \mid n \). Thus the order of \( {xy} \) is greater than \( {pq} \) and since it is always less than \( \operatorname{Card}\left( {{H}_{1}{H}_{2}}\right) = {pq} \), its order is indeed \( {pq} \).

EXERCICE 4. Soient \( {G}_{1},\ldots ,{G}_{n} \) des groupes cycliques d’ordres respectifs \( {\alpha }_{1},\ldots ,{\alpha }_{n} \) . Donner une condition nécessaire et suffisante portant sur les \( {\alpha }_{i} \) pour que le groupe \( G = \; {G}_{1} \times \cdots \times {G}_{n} \) soit cyclique.

> EXERCISE 4. Let \( {G}_{1},\ldots ,{G}_{n} \) be cyclic groups of respective orders \( {\alpha }_{1},\ldots ,{\alpha }_{n} \). Give a necessary and sufficient condition on the \( {\alpha }_{i} \) for the group \( G = \; {G}_{1} \times \cdots \times {G}_{n} \) to be cyclic.

Solution. Commençons par montrer le résultat suivant :

> Solution. Let us begin by proving the following result:

LEMME. Pour tout i, soit \( {x}_{i} \) un élément de \( {G}_{i} \) d’ordre \( {\beta }_{i} \) . Alors \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) est d’ordre ppcm \( \left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) \) dans \( {G}_{1} \times \cdots \times {G}_{n} \) .

> LEMMA. For any i, let \( {x}_{i} \) be an element of \( {G}_{i} \) of order \( {\beta }_{i} \). Then \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is of order lcm \( \left( {{\beta }_{1},\ldots ,{\beta }_{n}}\right) \) in \( {G}_{1} \times \cdots \times {G}_{n} \).

Preuve. Pour \( 1 \leq i \leq n \) , notons \( {e}_{i} \) l’élément neutre de \( {G}_{i} \) , de sorte que \( e = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) est l’élément neutre de \( G \) . On a : \( \left( {{x}^{p} = e}\right) \Leftrightarrow \left( {\forall i,{x}_{i}^{p} = {e}_{i}}\right) \Leftrightarrow \left( {\forall i,{\beta }_{i} \mid p}\right) \) . Le plus petit entier naturel non nul \( p \) tel que \( {x}^{p} = e \) est donc le plus petit multiple communs aux \( {\beta }_{i} \) , d’où le lemme.

> Proof. For \( 1 \leq i \leq n \), let \( {e}_{i} \) denote the identity element of \( {G}_{i} \), such that \( e = \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) is the identity element of \( G \). We have: \( \left( {{x}^{p} = e}\right) \Leftrightarrow \left( {\forall i,{x}_{i}^{p} = {e}_{i}}\right) \Leftrightarrow \left( {\forall i,{\beta }_{i} \mid p}\right) \). The smallest non-zero natural integer \( p \) such that \( {x}^{p} = e \) is therefore the least common multiple of the \( {\beta }_{i} \), hence the lemma.

Montrons maintenant la condition nécessaire et suffisante :

> Let us now show the necessary and sufficient condition:

Le groupe \( G \) est cyclique si et seulement si les \( {\alpha }_{i} \) sont premiers entre eux deux à deux.

> The group \( G \) is cyclic if and only if the \( {\alpha }_{i} \) are pairwise coprime.

Condition nécessaire. Soit \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) engendrant \( G \) . Il est clair que pour tout \( i,{x}_{i} \) engendre \( {G}_{i} \) , donc est d’ordre \( {\alpha }_{i} \) . D’après le lemme, l’ordre de \( x \) est ppcm \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) . Comme \( x \) engendre \( G \) , son ordre est aussi \( \operatorname{Card}\left( G\right) = {\alpha }_{1}\cdots {\alpha }_{n} \) . Donc ppcm \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) = {\alpha }_{1}\cdots {\alpha }_{n} \) , ce qui entraîne que les \( {\alpha }_{i} \) sont premiers entre eux deux à deux.

> Necessary condition. Let \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) generate \( G \). It is clear that for any \( i,{x}_{i} \), it generates \( {G}_{i} \), and is thus of order \( {\alpha }_{i} \). According to the lemma, the order of \( x \) is lcm \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \). Since \( x \) generates \( G \), its order is also \( \operatorname{Card}\left( G\right) = {\alpha }_{1}\cdots {\alpha }_{n} \). Thus lcm \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) = {\alpha }_{1}\cdots {\alpha }_{n} \), which implies that the \( {\alpha }_{i} \) are pairwise coprime.

Condition suffisante. Pour tout \( i \) , considérons \( {x}_{i} \in {G}_{i} \) d’ordre \( {\alpha }_{i} \) ( \( {x}_{i} \) existe puisque \( {G}_{i} \) est cy-clique par hypothèse). D’après le lemme, \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) est d’ordre ppcm \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) dans \( G \) , et ce dernier terme égale \( {\alpha }_{1}\cdots {\alpha }_{n} = \operatorname{Card}\left( G\right) \) puisque les \( {\alpha }_{i} \) sont premiers entre eux deux à deux. Finalement, \( G = \langle x\rangle \) est cyclique.

> Sufficient condition. For any \( i \), consider \( {x}_{i} \in {G}_{i} \) of order \( {\alpha }_{i} \) (\( {x}_{i} \) exists since \( {G}_{i} \) is cyclic by hypothesis). According to the lemma, \( x = \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is of order lcm \( \left( {{\alpha }_{1},\ldots ,{\alpha }_{n}}\right) \) in \( G \), and this last term equals \( {\alpha }_{1}\cdots {\alpha }_{n} = \operatorname{Card}\left( G\right) \) since the \( {\alpha }_{i} \) are pairwise coprime. Finally, \( G = \langle x\rangle \) is cyclic.

EXERCICE 5. Soit \( G \) un groupe, \( e \) son élément neutre. On suppose que tout élément \( x \) de \( G \) vérifie \( {x}^{2} = e \) .

> EXERCISE 5. Let \( G \) be a group, \( e \) its identity element. Suppose that every element \( x \) of \( G \) satisfies \( {x}^{2} = e \).

a) Montrer que \( G \) est un groupe abélien.

> a) Show that \( G \) is an abelian group.

b) Si \( G \) est fini et si \( G \neq \{ e\} \) , montrer qu’il existe un entier \( n \) tel que \( G \) soit isomorphe au groupe \( \left\lbrack {{\left( \mathbb{Z}/2\mathbb{Z}\right) }^{n}, + }\right\rbrack \) .

> b) If \( G \) is finite and if \( G \neq \{ e\} \), show that there exists an integer \( n \) such that \( G \) is isomorphic to the group \( \left\lbrack {{\left( \mathbb{Z}/2\mathbb{Z}\right) }^{n}, + }\right\rbrack \).

Solution. a) Si \( x \in G \) l’égalité \( {x}^{2} = e \) s’écrit aussi \( x = {x}^{-1} \) . Si \( x \) et \( y \) sont dans \( G \) , on a donc \( {xy} = {\left( xy\right) }^{-1} = {y}^{-1}{x}^{-1} = {yx}. \)

> Solution. a) If \( x \in G \), the equality \( {x}^{2} = e \) can also be written as \( x = {x}^{-1} \). If \( x \) and \( y \) are in \( G \), then we have \( {xy} = {\left( xy\right) }^{-1} = {y}^{-1}{x}^{-1} = {yx}. \)

b) Soit \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) un système de générateurs minimal de \( G \) (il en existe car \( G \) est fini). Si \( \dot{\alpha } = \dot{\beta } \) dans \( \mathbb{Z}/2\mathbb{Z} \) , alors \( 2 \mid \alpha - \beta \) donc pour \( x \in G,{x}^{\alpha } = {x}^{\beta } \) . Ceci permet d’affirmer que l’application

> b) Let \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) be a minimal generating set of \( G \) (one exists because \( G \) is finite). If \( \dot{\alpha } = \dot{\beta } \) in \( \mathbb{Z}/2\mathbb{Z} \), then \( 2 \mid \alpha - \beta \) so for \( x \in G,{x}^{\alpha } = {x}^{\beta } \). This allows us to assert that the map

\[
\varphi  : \left\lbrack  {{\left( \mathbb{Z}/2\mathbb{Z}\right) }^{n}, + }\right\rbrack   \rightarrow  G\;\left( {\dot{{\alpha }_{1}},\ldots ,\dot{{\alpha }_{n}}}\right)  \mapsto  {x}_{1}^{{\alpha }_{1}}\cdots {x}_{n}^{{\alpha }_{n}}
\]

est bien définie. Le groupe \( G \) étant abélien, \( \varphi \) est un morphisme de groupe, et il est surjectif par définition d’un système de générateurs. Montrons que \( \varphi \) est injectif. Soit \( \left( {\dot{{\alpha }_{1}},\ldots ,\dot{{\alpha }_{n}}}\right) \in \) Ker \( \varphi \) . S’il existe \( i \) tel que \( {\dot{\alpha }}_{i} = 1 \) , par exemple \( {\dot{\alpha }}_{n} = 1 \) , l’égalité \( {x}_{1}^{{\alpha }_{1}}\cdots {x}_{n - 1}^{{\alpha }_{n - 1}}{x}_{n} = e \) entraîne \( {x}_{n} = {x}_{n}^{-1} = {x}_{1}^{{\alpha }_{1}}\cdots {x}_{n - 1}^{{\alpha }_{n - 1}} \) . Donc \( \left( {{x}_{1},\ldots ,{x}_{n - 1}}\right) \) est un système de générateurs, ce qui est absurde puisque \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) est un système de générateurs minimal. Finalement \( \operatorname{Ker}\varphi = \{ \left( {\dot{0},\ldots ,\dot{0}}\right) \} \) et \( \varphi \) est injectif. C’est un isomorphisme.

> is well-defined. Since the group \( G \) is abelian, \( \varphi \) is a group homomorphism, and it is surjective by the definition of a generating set. Let us show that \( \varphi \) is injective. Let \( \left( {\dot{{\alpha }_{1}},\ldots ,\dot{{\alpha }_{n}}}\right) \in \) Ker \( \varphi \). If there exists \( i \) such that \( {\dot{\alpha }}_{i} = 1 \), for example \( {\dot{\alpha }}_{n} = 1 \), the equality \( {x}_{1}^{{\alpha }_{1}}\cdots {x}_{n - 1}^{{\alpha }_{n - 1}}{x}_{n} = e \) implies \( {x}_{n} = {x}_{n}^{-1} = {x}_{1}^{{\alpha }_{1}}\cdots {x}_{n - 1}^{{\alpha }_{n - 1}} \). Thus \( \left( {{x}_{1},\ldots ,{x}_{n - 1}}\right) \) is a generating set, which is absurd since \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is a minimal generating set. Finally \( \operatorname{Ker}\varphi = \{ \left( {\dot{0},\ldots ,\dot{0}}\right) \} \) and \( \varphi \) is injective. It is an isomorphism.

EXERCICE 6. Soit \( n \in {\mathbb{N}}^{ * }, n \geq 2 \) . Montrer que tout élément du groupe des permutations \( {\mathcal{S}}_{n} \) s’écrit comme le produit de transpositions de la forme \( \left( {i, i + 1}\right) \) avec \( 1 \leq i \leq n - 1 \) .

> EXERCISE 6. Let \( n \in {\mathbb{N}}^{ * }, n \geq 2 \) . Show that every element of the permutation group \( {\mathcal{S}}_{n} \) can be written as a product of transpositions of the form \( \left( {i, i + 1}\right) \) with \( 1 \leq i \leq n - 1 \) .

Solution. Soit \( P \) le sous-ensemble des permutations de \( {\mathcal{S}}_{n} \) qui s’écrivent comme le produit de transpositions de la forme \( \left( {i, i + 1}\right) \) . Soient \( i \) et \( j \) deux entiers vérifiant \( 1 \leq i < j \leq n \) . Le cycle \( \left( {i, i + 1,\ldots , j}\right) \) s’écrit sous la forme

> Solution. Let \( P \) be the subset of permutations of \( {\mathcal{S}}_{n} \) that can be written as a product of transpositions of the form \( \left( {i, i + 1}\right) \) . Let \( i \) and \( j \) be two integers satisfying \( 1 \leq i < j \leq n \) . The cycle \( \left( {i, i + 1,\ldots , j}\right) \) can be written in the form

\[
\left( {i, i + 1,\ldots , j}\right)  = \left( {i, i + 1}\right) \left( {i + 1, i + 2}\right) \cdots \left( {j - 1, j}\right)
\]

donc \( \left( {i, i + 1,\ldots , j}\right) \in P \) . De même,

> therefore \( \left( {i, i + 1,\ldots , j}\right) \in P \) . Similarly,

\[
\left( {j, j - 1,\ldots , i}\right)  = \left( {j - 1, j}\right) \cdots \left( {i + 1, i + 2}\right) \left( {i, i + 1}\right)  \in  P.
\]

Or lorsque \( 1 \leq i < j \leq n \) , on a

> However, when \( 1 \leq i < j \leq n \) , we have

\[
\left( {i, j}\right)  = \left( {j, j - 1,\ldots , i + 1}\right) \left( {i, i + 1,\ldots , j}\right)
\]

donc toute transposition appartient à \( P \) . Comme toute permutation peut s’écrire sous forme d’un produit de transpositions, on en déduit \( P = {\mathcal{S}}_{n} \) .

> therefore every transposition belongs to \( P \) . Since every permutation can be written as a product of transpositions, we deduce \( P = {\mathcal{S}}_{n} \) .

EXERCICE 7. On rappelle que le groupe alterné \( {\mathcal{A}}_{n} \) d’indice \( n \) est le sous-groupe de \( {\mathcal{S}}_{n} \) constitué des permutations paires. Si \( n \geq 3 \) , montrer que les cycles de longueur 3 engendrent \( {\mathcal{A}}_{n} \) .

> EXERCISE 7. Recall that the alternating group \( {\mathcal{A}}_{n} \) of index \( n \) is the subgroup of \( {\mathcal{S}}_{n} \) consisting of even permutations. If \( n \geq 3 \) , show that 3-cycles generate \( {\mathcal{A}}_{n} \) .

Solution. Puisque tout élément de \( {\mathcal{S}}_{n} \) peut s’écrire comme un produit de transpositions et qu’une transposition est de signature -1, \( {\mathcal{A}}_{n} \) est aussi l’ensemble des produits pairs de transpositions.

> Solution. Since every element of \( {\mathcal{S}}_{n} \) can be written as a product of transpositions and a transposition has signature -1, \( {\mathcal{A}}_{n} \) is also the set of even products of transpositions.

Appelons \( {\mathcal{A}}^{\prime }{}_{n} \) le sous-groupe de \( {\mathcal{S}}_{n} \) engendré par les cycles de longueur 3. On a \( {\mathcal{A}}^{\prime }{}_{n} \subset {\mathcal{A}}_{n} \) car un cycle de longueur 3 est de signature 1 (voir la proposition 7). Montrons maintenant \( {\mathcal{A}}_{n} \subset {\mathcal{A}}^{\prime }{}_{n} \) . D'après la remarque précédente, il suffit de prouver que le produit de deux transpositions est dans \( {\mathcal{A}}^{\prime }{}_{n} \) . Ceci est vrai car :

> Let \( {\mathcal{A}}^{\prime }{}_{n} \) be the subgroup of \( {\mathcal{S}}_{n} \) generated by 3-cycles. We have \( {\mathcal{A}}^{\prime }{}_{n} \subset {\mathcal{A}}_{n} \) because a 3-cycle has signature 1 (see Proposition 7). Now let us show \( {\mathcal{A}}_{n} \subset {\mathcal{A}}^{\prime }{}_{n} \) . According to the previous remark, it suffices to prove that the product of two transpositions is in \( {\mathcal{A}}^{\prime }{}_{n} \) . This is true because:

- Si \( i, j, k, l \) sont distincts deux à deux, \( \left( {i, j}\right) \left( {k, l}\right)  = \left( {i, j, k}\right) \left( {j, k, l}\right) \)

> - If \( i, j, k, l \) are pairwise distinct, \( \left( {i, j}\right) \left( {k, l}\right)  = \left( {i, j, k}\right) \left( {j, k, l}\right) \)

- Si \( i, j, k \) sont distincts deux à deux, \( \left( {i, j}\right) \left( {i, k}\right)  = \left( {i, k, j}\right) \) .

> - If \( i, j, k \) are pairwise distinct, \( \left( {i, j}\right) \left( {i, k}\right)  = \left( {i, k, j}\right) \) .

- Si \( i \neq  j,\left( {i, j}\right) \left( {j, i}\right)  = \) Id.

> - If \( i \neq  j,\left( {i, j}\right) \left( {j, i}\right)  = \) Id.

EXERCICE 8. On rappelle que si \( G \) est un groupe fini et \( H \) un sous-groupe de \( G \) , l’indice de \( H \) dans \( G \) est l’entier \( \left\lbrack {G : H}\right\rbrack = \frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( H\right) } \) .

> EXERCISE 8. Recall that if \( G \) is a finite group and \( H \) is a subgroup of \( G \) , the index of \( H \) in \( G \) is the integer \( \left\lbrack {G : H}\right\rbrack = \frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( H\right) } \) .

Soit \( p \geq 5 \) un nombre premier. Si \( H \) est un sous-groupe du groupe symétrique \( {\mathcal{S}}_{p} \) tel que \( \left\lbrack {{\mathcal{S}}_{p} : H}\right\rbrack \leq p - 1 \) , montrer que \( \left\lbrack {{\mathcal{S}}_{p} : H}\right\rbrack \in \{ 1,2\} \) . (Indications : Montrer que \( H \) contient tous les cycles de longueur \( p \) puis utiliser le résultat de l’exercice précédent.)

> Let \( p \geq 5 \) be a prime number. If \( H \) is a subgroup of the symmetric group \( {\mathcal{S}}_{p} \) such that \( \left\lbrack {{\mathcal{S}}_{p} : H}\right\rbrack \leq p - 1 \) , show that \( \left\lbrack {{\mathcal{S}}_{p} : H}\right\rbrack \in \{ 1,2\} \) . (Hints: Show that \( H \) contains all cycles of length \( p \) then use the result of the previous exercise.)

Solution. Montrons d’abord que \( H \) contient tous les cycles de longueur \( p \) . Soit \( \gamma \in {\mathcal{S}}_{p} \) un cycle de longueur \( p \) . Pour tout entier \( i \) , l’ensemble \( {\gamma }^{i}H \) est de cardinal Card \( \left( H\right) \) . Comme \( H \) est d’indice \( \leq p - 1 \) dans \( {\mathcal{S}}_{p} \) , les ensembles \( H,{\gamma H},\ldots ,{\gamma }^{p - 1}H \) ne peuvent pas être deux à deux disjoints (sinon \( \operatorname{Card}\left( {\mathcal{S}}_{p}\right) \geq \mathop{\sum }\limits_{{i = 0}}^{{p - 1}}\operatorname{Card}\left( {{\gamma }^{i}H}\right) = p \cdot \operatorname{Card}\left( H\right) ) \) . Donc il existe deux entiers \( i \) et \( j,0 \leq i < j \leq p - 1 \) , tels que \( {\gamma }^{i}H \cap {\gamma }^{j}H \neq \varnothing \) . On en déduit facilement \( {\gamma }^{j - i} \in H \) . Or \( 1 \leq j - i < p \) donc \( {\gamma }^{j - i} \) engendre le sous-groupe \( \langle \gamma \rangle \) d’ordre \( p \) (voir le théorème 4 page 22), ce qui entraîne \( \gamma \in \left\langle {\gamma }^{j - i}\right\rangle \subset H \) .

> Solution. Let us first show that \( H \) contains all cycles of length \( p \) . Let \( \gamma \in {\mathcal{S}}_{p} \) be a cycle of length \( p \) . For any integer \( i \) , the set \( {\gamma }^{i}H \) has cardinality Card \( \left( H\right) \) . Since \( H \) is of index \( \leq p - 1 \) in \( {\mathcal{S}}_{p} \) , the sets \( H,{\gamma H},\ldots ,{\gamma }^{p - 1}H \) cannot be pairwise disjoint (otherwise \( \operatorname{Card}\left( {\mathcal{S}}_{p}\right) \geq \mathop{\sum }\limits_{{i = 0}}^{{p - 1}}\operatorname{Card}\left( {{\gamma }^{i}H}\right) = p \cdot \operatorname{Card}\left( H\right) ) \) . Thus there exist two integers \( i \) and \( j,0 \leq i < j \leq p - 1 \) such that \( {\gamma }^{i}H \cap {\gamma }^{j}H \neq \varnothing \) . We easily deduce \( {\gamma }^{j - i} \in H \) . However \( 1 \leq j - i < p \) so \( {\gamma }^{j - i} \) generates the subgroup \( \langle \gamma \rangle \) of order \( p \) (see theorem 4 page 22), which implies \( \gamma \in \left\langle {\gamma }^{j - i}\right\rangle \subset H \) .

- Montrons maintenant que \( H \) contient tous les cycles d’ordre 3 . Comme \( p > 3 \) , il suffit de remarquer que \( H \) contenant tous les cycles d’ordre \( p \) , on a

> - Let us now show that \( H \) contains all cycles of order 3. Since \( p > 3 \) , it suffices to note that since \( H \) contains all cycles of order \( p \) , we have

\[
\left( {i, j, k}\right)  = \left( {k, j, i,{a}_{1},{a}_{2},\ldots ,{a}_{p - 3}}\right) \left( {i, k, j,{a}_{p - 3},\ldots ,{a}_{2},{a}_{1}}\right)  \in  H.
\]

- D’après le résultat de l’exercice précédent, \( H \) contient donc \( {\mathcal{A}}_{p} \) , le groupe alterné d’indice d’indice \( p \) . Donc \( \operatorname{Card}\left( H\right)  \geq  \operatorname{Card}\left( {\mathcal{A}}_{p}\right)  = \frac{1}{2}\operatorname{Card}\left( {\mathcal{S}}_{p}\right) \) , d’où \( \left\lbrack  {{\mathcal{S}}_{p} : H}\right\rbrack   \in  \{ 1,2\} \) .

> - According to the result of the previous exercise, \( H \) therefore contains \( {\mathcal{A}}_{p} \) , the alternating group of index \( p \) . Thus \( \operatorname{Card}\left( H\right)  \geq  \operatorname{Card}\left( {\mathcal{A}}_{p}\right)  = \frac{1}{2}\operatorname{Card}\left( {\mathcal{S}}_{p}\right) \) , whence \( \left\lbrack  {{\mathcal{S}}_{p} : H}\right\rbrack   \in  \{ 1,2\} \) .

Remarque. Ce résultat appliqué avec \( p = 5 \) montre qu’il n’existe pas de sous-groupe de \( {\mathcal{S}}_{5} \) d’ordre 30 ou 40, bien que \( \operatorname{Card}\left( {\mathcal{S}}_{5}\right) = {120} \) . Ainsi, un entier peut diviser l’ordre d’un groupe fini sans qu'il n'existe de sous-groupe d'ordre cet entier.

> Remark. This result applied with \( p = 5 \) shows that there is no subgroup of \( {\mathcal{S}}_{5} \) of order 30 or 40, even though \( \operatorname{Card}\left( {\mathcal{S}}_{5}\right) = {120} \) . Thus, an integer can divide the order of a finite group without there existing a subgroup of that order.

EXERCICE 9. Soit \( G \) un groupe fini d’ordre pair \( {2n}\left( {n \in {\mathbb{N}}^{ * }}\right) \) .

> EXERCISE 9. Let \( G \) be a finite group of even order \( {2n}\left( {n \in {\mathbb{N}}^{ * }}\right) \) .

a) Soit \( H \) un sous-groupe de \( G \) d’ordre \( n \) . Montrer que \( H \) est distingué dans \( G \) .

> a) Let \( H \) be a subgroup of \( G \) of order \( n \). Show that \( H \) is normal in \( G \).

b) On suppose qu’il existe deux sous-groupes \( {H}_{1} \) et \( {H}_{2} \) de \( G \) d’ordre \( n \) et tels que \( {H}_{1} \cap {H}_{2} = \; \{ e\} \) , où \( e \) désigne l’élément neutre de \( G \) . Montrer que \( n = 1 \) ou \( n = 2 \) .

> b) Suppose there exist two subgroups \( {H}_{1} \) and \( {H}_{2} \) of \( G \) of order \( n \) such that \( {H}_{1} \cap {H}_{2} = \; \{ e\} \), where \( e \) denotes the identity element of \( G \). Show that \( n = 1 \) or \( n = 2 \).

c) On suppose qu’il existe deux sous-groupes \( {H}_{1} \) et \( {H}_{2} \) de \( G \) , distincts et tout deux d’ordre \( n \) . Montrer que \( H = {H}_{1} \cap {H}_{2} \) est un sous-groupe distingué dans \( G \) . En déduire que l’ordre de \( G \) est un multiple de 4.

> c) Suppose there exist two distinct subgroups \( {H}_{1} \) and \( {H}_{2} \) of \( G \), both of order \( n \). Show that \( H = {H}_{1} \cap {H}_{2} \) is a normal subgroup of \( G \). Deduce that the order of \( G \) is a multiple of 4.

Solution. a) Il s’agit de montrer : \( {xH} = {Hx} \) pour tout \( x \in G \) .

> Solution. a) We must show: \( {xH} = {Hx} \) for all \( x \in G \).

- Si \( x \in  H \) , on a \( {xH} = {Hx} = H \) .

> - If \( x \in  H \), we have \( {xH} = {Hx} = H \).

- Si \( x \notin  H,{xH} \cap  H = \varnothing \) (en effet, si \( y \in  {xH} \cap  H \) , il existe \( a \in  H \) tel que \( y = {xa} \) donc \( x = y{a}^{-1} \in  H \) , absurde), c’est-à-dire \( {xH} \subset  G \smallsetminus  H \) . Or \( {xH} \) et \( G \smallsetminus  H \) sont de cardinal \( n \) , donc \( {xH} = G \smallsetminus  H \) . On montrerait de même que \( {Hx} = G \smallsetminus  H \) , donc \( {xH} = {Hx} \) .

> - If \( x \notin  H,{xH} \cap  H = \varnothing \) (indeed, if \( y \in  {xH} \cap  H \), there exists \( a \in  H \) such that \( y = {xa} \) so \( x = y{a}^{-1} \in  H \), which is absurd), that is \( {xH} \subset  G \smallsetminus  H \). Now \( {xH} \) and \( G \smallsetminus  H \) have cardinality \( n \), so \( {xH} = G \smallsetminus  H \). We would show similarly that \( {Hx} = G \smallsetminus  H \), so \( {xH} = {Hx} \).

b) Comme \( \operatorname{Card}\left( {{H}_{1} \cup {H}_{2}}\right) = \operatorname{Card}\left( {H}_{1}\right) + \operatorname{Card}\left( {H}_{2}\right) - \operatorname{Card}\left( {{H}_{1} \cap {H}_{2}}\right) = {2n} - 1 \) , il existe \( \alpha \in G \) , \( \alpha \notin {H}_{1},\alpha \notin {H}_{2} \) , tel que \( G = {H}_{1} \cup {H}_{2} \cup \{ \alpha \} \) .

> b) Since \( \operatorname{Card}\left( {{H}_{1} \cup {H}_{2}}\right) = \operatorname{Card}\left( {H}_{1}\right) + \operatorname{Card}\left( {H}_{2}\right) - \operatorname{Card}\left( {{H}_{1} \cap {H}_{2}}\right) = {2n} - 1 \), there exists \( \alpha \in G \), \( \alpha \notin {H}_{1},\alpha \notin {H}_{2} \), such that \( G = {H}_{1} \cup {H}_{2} \cup \{ \alpha \} \).

Si \( n = 1 \) , c’est terminé. Sinon \( n \geq 2 \) . On remarque alors que

> If \( n = 1 \), we are done. Otherwise \( n \geq 2 \). We then note that

\[
\forall \left( {x, y}\right)  \in  \left( {{H}_{1}\smallsetminus \{ e\} }\right)  \times  \left( {{H}_{2}\smallsetminus \{ e\} }\right) ,\;{xy} = \alpha .
\]

(En effet. Si \( {xy} \in {H}_{1} \) , alors \( y \in {x}^{-1}{H}_{1} = {H}_{1} \) donc \( y \in {H}_{1} \cap {H}_{2} = \{ e\} \) , donc \( y = e \) , ce qui est absurde; de même, \( {xy} \notin {H}_{2} \) .) Ceci n’est possible que si \( \operatorname{Card}\left( {{H}_{1}\smallsetminus \{ e\} }\right) = \operatorname{Card}\left( {{H}_{2}\smallsetminus \{ e\} }\right) = 1 \) , c'est-à-dire \( n = 2 \) . D'où le résultat.

> (Indeed. If \( {xy} \in {H}_{1} \), then \( y \in {x}^{-1}{H}_{1} = {H}_{1} \) so \( y \in {H}_{1} \cap {H}_{2} = \{ e\} \), so \( y = e \), which is absurd; likewise, \( {xy} \notin {H}_{2} \).) This is only possible if \( \operatorname{Card}\left( {{H}_{1}\smallsetminus \{ e\} }\right) = \operatorname{Card}\left( {{H}_{2}\smallsetminus \{ e\} }\right) = 1 \), that is \( n = 2 \). Hence the result.

c) D’après a), \( {H}_{1} \) et \( {H}_{2} \) sont distingués dans \( G \) donc pour tout \( x \in G,{xH} = x{H}_{1} \cap x{H}_{2} = \; {H}_{1}x \cap {H}_{2}x = {Hx} \) , ce qui prouve que \( H \) est distingué dans \( G \) .

> c) According to a), \( {H}_{1} \) and \( {H}_{2} \) are normal in \( G \) so for all \( x \in G,{xH} = x{H}_{1} \cap x{H}_{2} = \; {H}_{1}x \cap {H}_{2}x = {Hx} \), which proves that \( H \) is normal in \( G \).

Notons \( \pi \) la surjection canonique de \( G \) dans le groupe quotient \( G/H \) . Comme \( H \) est un sous-groupe de \( {H}_{1},\pi \left( {H}_{1}\right) = {H}_{1}/H \) est de cardinal \( \frac{\operatorname{Card}\left( {H}_{1}\right) }{\operatorname{Card}\left( H\right) } = \frac{n}{\operatorname{Card}\left( H\right) } \) . De même, \( \pi \left( {H}_{2}\right) = {H}_{2}/H \) est de cardinal \( \frac{n}{\operatorname{Card}\left( H\right) } \) . Or \( \left( {{H}_{1}/H}\right) \cap \left( {{H}_{2}/H}\right) = \left( {{H}_{1} \cap {H}_{2}}\right) /H \) est réduit à l’élément neutre de \( G/H \) . Le groupe quotient \( G/H \) étant d’ordre \( \frac{2n}{\operatorname{Card}\left( H\right) } \) , on peut appliquer b) à \( G/H,{H}_{1}/H \) et \( {H}_{2}/H \) ce qui donne \( \frac{n}{\operatorname{Card}\left( H\right) } \in \{ 1,2\} \) . Comme \( {H}_{1} \neq {H}_{2} \) , on a \( \operatorname{Card}\left( H\right) = \operatorname{Card}\left( {{H}_{1} \cap {H}_{2}}\right) < n \) donc \( \frac{n}{\operatorname{Card}\left( H\right) } = 2 \) . Finalement, \( \operatorname{Card}\left( G\right) = {2n} = 4\operatorname{Card}\left( H\right) \) , d’où le résultat.

> Let \( \pi \) be the canonical surjection from \( G \) to the quotient group \( G/H \). Since \( H \) is a subgroup of \( {H}_{1},\pi \left( {H}_{1}\right) = {H}_{1}/H \), it has cardinality \( \frac{\operatorname{Card}\left( {H}_{1}\right) }{\operatorname{Card}\left( H\right) } = \frac{n}{\operatorname{Card}\left( H\right) } \). Similarly, \( \pi \left( {H}_{2}\right) = {H}_{2}/H \) has cardinality \( \frac{n}{\operatorname{Card}\left( H\right) } \). However, \( \left( {{H}_{1}/H}\right) \cap \left( {{H}_{2}/H}\right) = \left( {{H}_{1} \cap {H}_{2}}\right) /H \) is reduced to the identity element of \( G/H \). Since the quotient group \( G/H \) is of order \( \frac{2n}{\operatorname{Card}\left( H\right) } \), we can apply b) to \( G/H,{H}_{1}/H \) and \( {H}_{2}/H \), which gives \( \frac{n}{\operatorname{Card}\left( H\right) } \in \{ 1,2\} \). Since \( {H}_{1} \neq {H}_{2} \), we have \( \operatorname{Card}\left( H\right) = \operatorname{Card}\left( {{H}_{1} \cap {H}_{2}}\right) < n \), thus \( \frac{n}{\operatorname{Card}\left( H\right) } = 2 \). Finally, \( \operatorname{Card}\left( G\right) = {2n} = 4\operatorname{Card}\left( H\right) \), hence the result.

EXERCICE 10 (EXPOSANT D'UN GROUPE ABÉLIEN FINI). Soit \( G \) un groupe abélien fini. a) Si \( x, y \) sont deux éléments de \( G \) d’ordres respectifs \( m \) et \( n \) , avec \( m \land n = 1 \) , quel est l’ordre de \( {xy} \) ?

> EXERCISE 10 (EXPONENT OF A FINITE ABELIAN GROUP). Let \( G \) be a finite abelian group. a) If \( x, y \) are two elements of \( G \) with respective orders \( m \) and \( n \), with \( m \land n = 1 \), what is the order of \( {xy} \)?

b) On appelle exposant de \( G \) le plus grand des ordres des éléments de \( G \) et on le note \( r \) . Montrer que \( r \) divise \( \operatorname{Card}\left( G\right) \) et que si \( x \in G \) , l’ordre de \( x \) divise \( r \) .

> b) The exponent of \( G \) is defined as the largest of the orders of the elements of \( G \) and is denoted by \( r \). Show that \( r \) divides \( \operatorname{Card}\left( G\right) \) and that if \( x \in G \), the order of \( x \) divides \( r \).

c) Montrer que \( r \) a les mêmes facteurs premiers que \( \operatorname{Card}\left( G\right) \) . En déduire que pour tout facteur premier \( p \) de \( \operatorname{Card}\left( G\right) \) , il existe un élément de \( G \) d’ordre \( p \) .

> c) Show that \( r \) has the same prime factors as \( \operatorname{Card}\left( G\right) \). Deduce that for every prime factor \( p \) of \( \operatorname{Card}\left( G\right) \), there exists an element of \( G \) of order \( p \).

Solution. a) Si \( {\left( xy\right) }^{p} = e \) alors \( {x}^{p} = {\left( {y}^{-1}\right) }^{p} \) donc \( {x}^{p} \in \langle y\rangle \) , d’où \( {\left( {x}^{p}\right) }^{n} = {x}^{pn} = e \) , donc \( m \mid {pn} \) . Or \( m \land n = 1 \) donc d’après le théorème de Gauss, \( m \mid p \) . De même \( n \mid p \) et les entiers \( m \) et \( n \) étant premiers entre eux, \( {mn} \mid p \) . Or \( {\left( xy\right) }^{mn} = {\left( {x}^{m}\right) }^{n}{\left( {y}^{n}\right) }^{m} = e \) , l’ordre de \( {xy} \) est donc \( {mn} \) .

> Solution. a) If \( {\left( xy\right) }^{p} = e \) then \( {x}^{p} = {\left( {y}^{-1}\right) }^{p} \) so \( {x}^{p} \in \langle y\rangle \), hence \( {\left( {x}^{p}\right) }^{n} = {x}^{pn} = e \), therefore \( m \mid {pn} \). However, \( m \land n = 1 \) so according to Gauss's theorem, \( m \mid p \). Similarly, \( n \mid p \) and since the integers \( m \) and \( n \) are coprime, \( {mn} \mid p \). Now \( {\left( xy\right) }^{mn} = {\left( {x}^{m}\right) }^{n}{\left( {y}^{n}\right) }^{m} = e \), the order of \( {xy} \) is therefore \( {mn} \).

b) Par définition de \( r \) , il existe un élément \( x \) de \( G \) d’ordre \( r \) et on a \( r \mid \operatorname{Card}\left( G\right) \) d’après le théorème 2 page 21.

> b) By definition of \( r \), there exists an element \( x \) of \( G \) of order \( r \) and we have \( r \mid \operatorname{Card}\left( G\right) \) according to theorem 2 on page 21.

Soit \( y \in G, q \) son ordre. Il s’agit de montrer que \( q \mid r \) . Supposons \( q \nmid r \) . En écrivant la décomposition en facteurs premiers de \( q \) et \( r \) , on voit qu’il existe un nombre premier \( p \) vérifiant

> Let \( y \in G, q \) be its order. We must show that \( q \mid r \). Suppose \( q \nmid r \). By writing the prime factorization of \( q \) and \( r \), we see that there exists a prime number \( p \) satisfying

\[
\left\{  \begin{array}{l} q = {p}^{\alpha }{q}^{\prime } \\  r = {p}^{\beta }{r}^{\prime } \end{array}\right. \;\text{ avec }\;\alpha  > \beta  \geq  0\text{ et }p \land  {q}^{\prime } = p \land  {r}^{\prime } = 1.
\]

Or \( a = {x}^{{p}^{\beta }} \) est d’ordre \( {r}^{\prime } \) et \( b = {y}^{{q}^{\prime }} \) est d’ordre \( {p}^{\alpha } \) . D’après a), \( {ab} \) est donc d’ordre \( {r}^{\prime }{p}^{\alpha } > r \) , ce qui contredit la définition de \( r \) . Donc \( q \mid r \) .

> However, \( a = {x}^{{p}^{\beta }} \) is of order \( {r}^{\prime } \) and \( b = {y}^{{q}^{\prime }} \) is of order \( {p}^{\alpha } \). According to a), \( {ab} \) is therefore of order \( {r}^{\prime }{p}^{\alpha } > r \), which contradicts the definition of \( r \). Thus \( q \mid r \).

c) Soit \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) un système de générateurs de \( G \) . Notons \( {r}_{1},\ldots ,{r}_{n} \) les ordres de \( {x}_{1},\ldots ,{x}_{n} \) . Considérons l'application

> c) Let \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) be a system of generators of \( G \). Let \( {r}_{1},\ldots ,{r}_{n} \) denote the orders of \( {x}_{1},\ldots ,{x}_{n} \). Consider the map

\[
\varphi  : \left\langle  {x}_{1}\right\rangle   \times  \cdots  \times  \left\langle  {x}_{n}\right\rangle   \rightarrow  G\;\left( {{y}_{1},\ldots ,{y}_{n}}\right)  \mapsto  {y}_{1}\cdots {y}_{n}.
\]

Le groupe \( G \) étant abélien, \( \varphi \) est un morphisme de groupes. De plus, \( \varphi \) est surjectif (puisque \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) est un système de générateurs de \( G \) ), donc \( G \) est isomorphe au groupe quotient \( \left( {\left\langle {x}_{1}\right\rangle \times \cdots \times \left\langle {x}_{n}\right\rangle }\right) /\operatorname{Ker}\varphi \) , donc

> Since the group \( G \) is abelian, \( \varphi \) is a group homomorphism. Furthermore, \( \varphi \) is surjective (since \( \left( {{x}_{1},\ldots ,{x}_{n}}\right) \) is a system of generators of \( G \)), so \( G \) is isomorphic to the quotient group \( \left( {\left\langle {x}_{1}\right\rangle \times \cdots \times \left\langle {x}_{n}\right\rangle }\right) /\operatorname{Ker}\varphi \), therefore

\[
\operatorname{Card}\left( G\right)  \times  \operatorname{Card}\left( {\operatorname{Ker}\varphi }\right)  = \operatorname{Card}\left( {\left\langle  {x}_{1}\right\rangle   \times  \cdots  \times  \left\langle  {x}_{n}\right\rangle  }\right)  = {r}_{1}\cdots {r}_{n},
\]

donc \( \operatorname{Card}\left( G\right) \mid {r}_{1}\cdots {r}_{n} \) . Or tous les \( {r}_{i} \) divisent \( r \) d’après b), donc \( \operatorname{Card}\left( G\right) \mid {r}^{n} \) . On en déduit que tout facteur premier \( p \) de Card \( \left( G\right) \) divise \( r \) .

> thus \( \operatorname{Card}\left( G\right) \mid {r}_{1}\cdots {r}_{n} \). However, all \( {r}_{i} \) divide \( r \) according to b), so \( \operatorname{Card}\left( G\right) \mid {r}^{n} \). We deduce that every prime factor \( p \) of Card \( \left( G\right) \) divides \( r \).

Soit \( p \) un facteur premier de \( \operatorname{Card}\left( G\right) \) . On vient de prouver que \( p \mid r \) donc on peut écrire \( r = p{r}^{\prime } \) avec \( {r}^{\prime } \) entier. Si on choisit un élément \( x \) de \( G \) d’ordre \( r \) , l’élément \( {x}^{{r}^{\prime }} \) est d’ordre \( p \) , d’où le résultat.

> Let \( p \) be a prime factor of \( \operatorname{Card}\left( G\right) \). We have just proven that \( p \mid r \), so we can write \( r = p{r}^{\prime } \) with \( {r}^{\prime } \) as an integer. If we choose an element \( x \) of \( G \) of order \( r \), the element \( {x}^{{r}^{\prime }} \) is of order \( p \), hence the result.

Remarque. Les résultats de cet exercice permettent de montrer que si K est un corps commutatif et \( G \) un sous-groupe fini du groupe multiplicatif \( \left( {{\mathbb{K}}^{ * }, \times }\right) \) , alors \( G \) est cyclique. En effet. Soit \( r \) l’exposant de \( G.\mathbb{K} \) étant un corps commutatif, l’équation \( {x}^{r} = 1 \) a au plus \( r \) solutions dans \( \mathbb{K} \) , donc au plus \( r \) solutions dans \( G \) . Or \( \forall x \in G,{x}^{r} = 1 \) d’après b). On en déduit \( \operatorname{Card}\left( G\right) \leq r \) , et comme \( r \mid \operatorname{Card}\left( G\right) \) , on a \( r = \operatorname{Card}\left( G\right) \) et le résultat annoncé. - Ce dernier résultat est également une conséquence du problème 7 page 42.

> Remark. The results of this exercise allow us to show that if K is a commutative field and \( G \) is a finite subgroup of the multiplicative group \( \left( {{\mathbb{K}}^{ * }, \times }\right) \), then \( G \) is cyclic. Indeed. Let \( r \) be the exponent of \( G.\mathbb{K} \) being a commutative field, the equation \( {x}^{r} = 1 \) has at most \( r \) solutions in \( \mathbb{K} \), and therefore at most \( r \) solutions in \( G \). However, \( \forall x \in G,{x}^{r} = 1 \) according to b). We deduce \( \operatorname{Card}\left( G\right) \leq r \), and since \( r \mid \operatorname{Card}\left( G\right) \), we have \( r = \operatorname{Card}\left( G\right) \) and the announced result. - This last result is also a consequence of problem 7 on page 42.

- En l’appliquant au corps \( \mathbb{Z}/p\mathbb{Z} \) (où \( p \) est un nombre premier), on démontre que le groupe multiplicatif \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) est cyclique, résultat non évident a priori.

> - By applying it to the field \( \mathbb{Z}/p\mathbb{Z} \) (where \( p \) is a prime number), we prove that the multiplicative group \( {\left( \mathbb{Z}/p\mathbb{Z}\right) }^{ * } \) is cyclic, a result not obvious a priori.

EXERCICE 11 (LES \( p \) -GROUPES). Soit \( p \) un nombre premier et \( G \) un groupe fini d’ordre \( {p}^{\alpha } \) avec \( \alpha \in {\mathbb{N}}^{ * } \) (on dit que \( G \) est un \( p \) -groupe).

> EXERCISE 11 (\( p \)-GROUPS). Let \( p \) be a prime number and \( G \) a finite group of order \( {p}^{\alpha } \) with \( \alpha \in {\mathbb{N}}^{ * } \) (we say that \( G \) is a \( p \)-group).

a) Montrer que \( \mathcal{Z}\left( G\right) \) , le centre de \( G \) , est différent de \( \{ e\} \) , où \( e \) désigne l’élément neutre de \( G \) . (On pourra utiliser l’équation aux classes - voir le théorème 8 page 24).

> a) Show that \( \mathcal{Z}\left( G\right) \), the center of \( G \), is different from \( \{ e\} \), where \( e \) denotes the identity element of \( G \). (One may use the class equation - see theorem 8 on page 24).

b) Que dire si \( \alpha = 1 \) ? si \( \alpha = 2 \) ?

> b) What can be said if \( \alpha = 1 \)? if \( \alpha = 2 \)?

c) Montrer que pour tout entier \( m,0 \leq m \leq \alpha \) , il existe un sous-groupe de \( G \) d’ordre \( {p}^{m} \) .

> c) Show that for any integer \( m,0 \leq m \leq \alpha \), there exists a subgroup of \( G \) of order \( {p}^{m} \).

Solution. a) D’après le théorème 8, il existe une famille finie \( {\left( {H}_{i}\right) }_{i \in I} \) de sous-groupes stricts de \( G \) telle que

> Solution. a) According to theorem 8, there exists a finite family \( {\left( {H}_{i}\right) }_{i \in I} \) of proper subgroups of \( G \) such that

\[
\operatorname{Card}\left( G\right)  = \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right)  + \mathop{\sum }\limits_{{i \in  I}}\frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {H}_{i}\right) }.
\]

(*)

> Pour tout \( i \in I,{H}_{i} \) est un sous-groupe strict de \( G \) donc d’après le théorème de Lagrange, son ordre divise \( \operatorname{Card}\left( G\right) = {p}^{\alpha } \) , de sorte qu’il existe un entier \( {\beta }_{i},1 \leq {\beta }_{i} < \alpha \) , tel que \( \operatorname{Card}\left( {H}_{i}\right) = {p}^{{\beta }_{i}} \) . Donc pour tout \( i \in I, p \) divise \( \frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {H}_{i}\right) } = {p}^{\alpha - {\beta }_{i}} \) . Or \( p \mid \operatorname{Card}\left( G\right) \) donc d’après \( \left( *\right) , p \mid \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \) . Comme de plus \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \geq 1 \) car \( e \in \mathcal{Z}\left( G\right) \) , ceci entraîne \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \geq p \) .

For any \( i \in I,{H}_{i} \) is a proper subgroup of \( G \), so according to Lagrange's theorem, its order divides \( \operatorname{Card}\left( G\right) = {p}^{\alpha } \), such that there exists an integer \( {\beta }_{i},1 \leq {\beta }_{i} < \alpha \) such that \( \operatorname{Card}\left( {H}_{i}\right) = {p}^{{\beta }_{i}} \). Therefore, for any \( i \in I, p \) divides \( \frac{\operatorname{Card}\left( G\right) }{\operatorname{Card}\left( {H}_{i}\right) } = {p}^{\alpha - {\beta }_{i}} \). However, \( p \mid \operatorname{Card}\left( G\right) \) so according to \( \left( *\right) , p \mid \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \). As furthermore \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \geq 1 \) because \( e \in \mathcal{Z}\left( G\right) \), this implies \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \geq p \).

> b) Si \( \alpha = 1, G \) est cyclique d’après le théorème 4.

b) If \( \alpha = 1, G \) is cyclic according to theorem 4.

> Si \( \alpha = 2 \) , comme \( \mathcal{Z}\left( G\right) \) est un sous-groupe de \( G \) , différent de \( \{ e\} \) d’après a), on a forcément \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \in \left\{ {p,{p}^{2}}\right\} \) . Nous allons montrer que \( \mathcal{Z}\left( G\right) = G \) en raisonnant par l’absurde. Sup-posons \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) = p \) . Soit \( x \in G, x \notin \mathcal{Z}\left( G\right) \) . L’ensemble \( {S}_{x} = \{ u \in G \mid {ux} = {xu}\} \) (appelé normalisateur de \( x \) ) est un sous-groupe de \( G \) . Or \( x \in {S}_{x} \) et \( \mathcal{Z}\left( G\right) \subset {S}_{x} \) , donc Card \( \left( {S}_{x}\right) \geq p + 1 \) . Comme \( \operatorname{Card}\left( {S}_{x}\right) \mid {p}^{2} = \operatorname{Card}\left( G\right) \) , ceci entraine \( \operatorname{Card}\left( {S}_{x}\right) = {p}^{2} \) donc \( {S}_{x} = G \) , et par définition de \( {S}_{x} \) , on a \( x \in \mathcal{Z}\left( G\right) \) , ce qui est contradictoire. Finalement \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) = {p}^{2} \) , c’est-à-dire \( G \) est abélien.

If \( \alpha = 2 \), as \( \mathcal{Z}\left( G\right) \) is a subgroup of \( G \), distinct from \( \{ e\} \) according to a), we necessarily have \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) \in \left\{ {p,{p}^{2}}\right\} \). We will show that \( \mathcal{Z}\left( G\right) = G \) by contradiction. Suppose \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) = p \). Let \( x \in G, x \notin \mathcal{Z}\left( G\right) \). The set \( {S}_{x} = \{ u \in G \mid {ux} = {xu}\} \) (called the normalizer of \( x \)) is a subgroup of \( G \). However, \( x \in {S}_{x} \) and \( \mathcal{Z}\left( G\right) \subset {S}_{x} \), so Card \( \left( {S}_{x}\right) \geq p + 1 \). As \( \operatorname{Card}\left( {S}_{x}\right) \mid {p}^{2} = \operatorname{Card}\left( G\right) \), this implies \( \operatorname{Card}\left( {S}_{x}\right) = {p}^{2} \) therefore \( {S}_{x} = G \), and by definition of \( {S}_{x} \), we have \( x \in \mathcal{Z}\left( G\right) \), which is a contradiction. Finally \( \operatorname{Card}\left( {\mathcal{Z}\left( G\right) }\right) = {p}^{2} \), that is to say \( G \) is abelian.

> c) Nous allons montrer ce résultat par récurrence sur \( \alpha \in {\mathbb{N}}^{ * } \) . (Le principe est de considérer le quotient par un sous-groupe distingué d’ordre \( p \) pour se ramener à l’hypothèse de récurrence).

c) We will show this result by induction on \( \alpha \in {\mathbb{N}}^{ * } \). (The principle is to consider the quotient by a normal subgroup of order \( p \) to reduce it to the induction hypothesis).

> - Si \( \alpha  = 1 \) , le résultat est évident.

- If \( \alpha  = 1 \), the result is obvious.

> - Supposons le résultat vrai pour \( \alpha \) , montrons le pour \( \alpha  + 1 \) . Soit \( m,0 \leq  m \leq  \alpha  + 1 \) . Si \( m = 0 \) , \( \{ e\} \) est un sous-groupe d’ordre \( {p}^{m} \) et le résultat est montré. Sinon, supposons \( m \geq  1 \) . D’après a), \( \mathcal{Z}\left( G\right) \) est différent de \( \{ e\} \) . Soit \( x \in  \mathcal{Z}\left( G\right) , x \neq  e \) . L’ordre de \( x \) divisant \( {p}^{\alpha  + 1} \) , il est de la forme \( {p}^{\beta } \) avec \( \beta  \geq  1 \) . Donc \( y = {x}^{{p}^{\beta  - 1}} \) est d’ordre \( p \) , et le groupe \( H = \langle y\rangle \) est d’ordre \( p \) . Par ailleurs, c’est un sous-groupe de \( \mathcal{Z}\left( G\right) \) et il est donc distingué dans \( G \) . Le groupe quotient \( G/H \) est d’ordre \( {p}^{\alpha } \) et d’après l’hypothèse de récurrence, il existe un sous-groupe \( K \) de \( G/H \) d’ordre \( {p}^{m - 1} \) . Soit \( \pi \) la surjection canonique de \( G \) dans \( G/H \) et considérons \( F = {\pi }^{-1}\left( K\right) \) . Comme \( \pi \) est un morphisme de groupes, \( F \) est un sous-groupe de \( G \) , et par ailleurs \( K = \pi \left( F\right) \) est isomorphe à \( F/\operatorname{Ker}\pi  = F/H \) ce qui entraîne \( \operatorname{Card}\left( F\right)  = \operatorname{Card}\left( K\right)  \times  \operatorname{Card}\left( H\right)  = {p}^{m} \) . D’où le résultat.

- Assume the result is true for \( \alpha \), let us show it for \( \alpha  + 1 \). Let \( m,0 \leq  m \leq  \alpha  + 1 \). If \( m = 0 \), \( \{ e\} \) is a subgroup of order \( {p}^{m} \) and the result is shown. Otherwise, assume \( m \geq  1 \). According to a), \( \mathcal{Z}\left( G\right) \) is different from \( \{ e\} \). Let \( x \in  \mathcal{Z}\left( G\right) , x \neq  e \). The order of \( x \) dividing \( {p}^{\alpha  + 1} \), it is of the form \( {p}^{\beta } \) with \( \beta  \geq  1 \). Thus \( y = {x}^{{p}^{\beta  - 1}} \) is of order \( p \), and the group \( H = \langle y\rangle \) is of order \( p \). Furthermore, it is a subgroup of \( \mathcal{Z}\left( G\right) \) and is therefore normal in \( G \). The quotient group \( G/H \) is of order \( {p}^{\alpha } \) and according to the induction hypothesis, there exists a subgroup \( K \) of \( G/H \) of order \( {p}^{m - 1} \). Let \( \pi \) be the canonical surjection from \( G \) to \( G/H \) and consider \( F = {\pi }^{-1}\left( K\right) \). Since \( \pi \) is a group homomorphism, \( F \) is a subgroup of \( G \), and furthermore \( K = \pi \left( F\right) \) is isomorphic to \( F/\operatorname{Ker}\pi  = F/H \) which implies \( \operatorname{Card}\left( F\right)  = \operatorname{Card}\left( K\right)  \times  \operatorname{Card}\left( H\right)  = {p}^{m} \). Hence the result.

> Remarque. Ce résultat est un cas particulier du théorème de Sylow (voir le problème 9 page 44).

Remark. This result is a special case of Sylow's theorem (see problem 9 on page 44).

> EXERCICE 12 (UN THÉORÉME DE CAUCHY SUR LES GROUPES FINIS). On suppose que la théorie des groupes opérant sur un ensemble est connue (voir la partie 2.4).

EXERCISE 12 (A CAUCHY THEOREM ON FINITE GROUPS). We assume that the theory of groups acting on a set is known (see part 2.4).

> Soit \( G \) un groupe fini (non forcément abélien) d’ordre \( h \) , et soit \( p \) un nombre premier divisant \( h \) . On note

Let \( G \) be a finite group (not necessarily abelian) of order \( h \), and let \( p \) be a prime number dividing \( h \). We denote

\[
S = \left\{  {\left( {{a}_{1},\ldots ,{a}_{p}}\right)  \in  {G}^{p} \mid  {a}_{1}\cdots {a}_{p} = e}\right\}  ,
\]

où \( e \) désigne l’élément neutre de \( G \) , et on note \( \gamma \) le cycle \( \left( {1,2,\ldots , p}\right) \in {\mathcal{S}}_{p} \) . a) On fait opérer \( \langle \gamma \rangle \) sur \( S \) en posant

> where \( e \) denotes the identity element of \( G \), and we denote \( \gamma \) as the cycle \( \left( {1,2,\ldots , p}\right) \in {\mathcal{S}}_{p} \). a) We let \( \langle \gamma \rangle \) act on \( S \) by setting

\[
\forall k \in  \mathbb{Z},\;{\gamma }^{k}\left( {{a}_{1},\ldots ,{a}_{p}}\right)  = \left( {{a}_{{\gamma }^{k}\left( 1\right) },\ldots ,{a}_{{\gamma }^{k}\left( p\right) }}\right) .
\]

Déterminer le cardinal des orbites.

> Determine the cardinality of the orbits.

b) (Théorème de Cauchy). Démontrer que le nombre de solutions dans \( G \) de l’équation \( {x}^{p} = e \) est un multiple de \( p \) .

> b) (Cauchy's Theorem). Prove that the number of solutions in \( G \) to the equation \( {x}^{p} = e \) is a multiple of \( p \).

En déduire qu'il existe au moins un élément d'ordre \( p \) dans \( G \) .

> Deduce that there exists at least one element of order \( p \) in \( G \).

Solution. a) Pour tout \( x \in S \) , on note \( {G}_{x} \) l’orbite de \( x \) et \( {S}_{x} \) son stabilisateur. On sait que l’on a \( p = \operatorname{Card}\left( {\langle \gamma \rangle }\right) = \operatorname{Card}\left( {G}_{x}\right) \times \operatorname{Card}\left( {S}_{x}\right) \) , et \( p \) étant premier, \( \operatorname{Card}\left( {G}_{x}\right) = 1 \) ou \( \operatorname{Card}\left( {G}_{x}\right) = p \) .

> Solution. a) For any \( x \in S \), we denote \( {G}_{x} \) as the orbit of \( x \) and \( {S}_{x} \) as its stabilizer. We know that \( p = \operatorname{Card}\left( {\langle \gamma \rangle }\right) = \operatorname{Card}\left( {G}_{x}\right) \times \operatorname{Card}\left( {S}_{x}\right) \), and since \( p \) is prime, \( \operatorname{Card}\left( {G}_{x}\right) = 1 \) or \( \operatorname{Card}\left( {G}_{x}\right) = p \).

b) L’application \( f : S \rightarrow {G}^{p - 1}\;\left( {{a}_{1},\ldots ,{a}_{p}}\right) \mapsto \left( {{a}_{1},\ldots ,{a}_{p - 1}}\right) \) est bijective puisque chaque élé- ment \( \left( {{a}_{1},\ldots ,{a}_{p - 1}}\right) \) de \( {G}^{p - 1} \) a un unique antécédent par \( f \) qui est \( \left( {{a}_{1},\ldots ,{a}_{p - 1},{\left( {a}_{1}\cdots {a}_{p - 1}\right) }^{-1}}\right) \) . Donc Card \( \left( S\right) = \operatorname{Card}\left( {G}^{p - 1}\right) = {h}^{p - 1} \) .

> b) The map \( f : S \rightarrow {G}^{p - 1}\;\left( {{a}_{1},\ldots ,{a}_{p}}\right) \mapsto \left( {{a}_{1},\ldots ,{a}_{p - 1}}\right) \) is bijective since each element \( \left( {{a}_{1},\ldots ,{a}_{p - 1}}\right) \) of \( {G}^{p - 1} \) has a unique antecedent by \( f \) which is \( \left( {{a}_{1},\ldots ,{a}_{p - 1},{\left( {a}_{1}\cdots {a}_{p - 1}\right) }^{-1}}\right) \). Thus Card \( \left( S\right) = \operatorname{Card}\left( {G}^{p - 1}\right) = {h}^{p - 1} \).

Soit \( \Theta \) une partie de \( S \) contenant exactement un représentant de chaque orbite \( {G}_{x} \) . Soit \( A = \left\{ {x \in S \mid \operatorname{Card}\left( {G}_{x}\right) = 1}\right\} \) . Soit \( {\Theta }^{\prime } = \Theta \smallsetminus A \) . D’après a), \( \forall x \in {\Theta }^{\prime },\operatorname{Card}\left( {G}_{x}\right) = p \) . Or

> Let \( \Theta \) be a subset of \( S \) containing exactly one representative of each orbit \( {G}_{x} \). Let \( A = \left\{ {x \in S \mid \operatorname{Card}\left( {G}_{x}\right) = 1}\right\} \). Let \( {\Theta }^{\prime } = \Theta \smallsetminus A \). According to a), \( \forall x \in {\Theta }^{\prime },\operatorname{Card}\left( {G}_{x}\right) = p \). However

\[
{h}^{p - 1} = \operatorname{Card}\left( S\right)  = \mathop{\sum }\limits_{{x \in  \Theta }}\operatorname{Card}\left( {G}_{x}\right)  = \operatorname{Card}\left( A\right)  + \mathop{\sum }\limits_{{x \in  {\Theta }^{\prime }}}\operatorname{Card}\left( {G}_{x}\right) .
\]

Comme de plus \( p \mid h \) , on en déduit que \( p \mid \operatorname{Card}\left( A\right) = {h}^{p - 1} - p\operatorname{Card}\left( {\Theta }^{\prime }\right) \) . Par définition de \( A \) , \( A \) est l’ensemble des \( p \) -uplets \( \left( {x,\ldots , x}\right) \) tels que \( {x}^{p} = e \) . Le nombre \( \operatorname{Card}\left( A\right) \) représente donc le nombre de solutions de \( {x}^{p} = e \) , et comme \( p \mid \operatorname{Card}\left( A\right) \) , on en déduit le théorème de Cauchy.

> Since, moreover, \( p \mid h \), we deduce that \( p \mid \operatorname{Card}\left( A\right) = {h}^{p - 1} - p\operatorname{Card}\left( {\Theta }^{\prime }\right) \). By definition of \( A \), \( A \) is the set of \( p \)-tuples \( \left( {x,\ldots , x}\right) \) such that \( {x}^{p} = e \). The number \( \operatorname{Card}\left( A\right) \) therefore represents the number of solutions to \( {x}^{p} = e \), and since \( p \mid \operatorname{Card}\left( A\right) \), we deduce Cauchy's theorem.

On a \( {e}^{p} = e \) , ce qui entraîne \( \operatorname{Card}\left( A\right) \geq 1 \) , et comme \( p \mid \operatorname{Card}\left( A\right) ,\operatorname{Card}\left( A\right) \geq p \) . Donc il existe \( x \in G, x \neq e \) tel que \( {x}^{p} = e \) . Le nombre \( p \) étant premier, \( x \) est d’ordre \( p \) .

> We have \( {e}^{p} = e \), which implies \( \operatorname{Card}\left( A\right) \geq 1 \), and since \( p \mid \operatorname{Card}\left( A\right) ,\operatorname{Card}\left( A\right) \geq p \). Thus there exists \( x \in G, x \neq e \) such that \( {x}^{p} = e \). Since the number \( p \) is prime, \( x \) is of order \( p \).

Remarque. Ce résultat entraîne que lorsqu’un nombre premier \( p \) divise l’ordre d’un groupe, il existe un sous-groupe de cardinal \( p \) . On savait que c’était déjà vrai dans le cas d’un groupe abélien (voir l'exercice 10). Le problème 9 page 44 généralise ce dernier résultat.

> Remark. This result implies that when a prime number \( p \) divides the order of a group, there exists a subgroup of cardinality \( p \). We already knew this was true in the case of an abelian group (see exercise 10). Problem 9 on page 44 generalizes this latter result.
