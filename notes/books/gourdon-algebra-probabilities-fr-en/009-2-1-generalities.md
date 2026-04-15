#### 2.1. Generalities

*Français : 2.1. Généralités*

DÉFINITION 1. On appelle groupe un ensemble \( G \) muni d’une loi interne * telle que

> DEFINITION 1. A group is a set \( G \) equipped with an internal law * such that

(i) La loi * est associative (i. e. pour tous \( x, y, z \) dans \( G,\left( {x * y}\right) * z = x * \left( {y * z}\right) \) ).

> (i) The law * is associative (i. e. for all \( x, y, z \) in \( G,\left( {x * y}\right) * z = x * \left( {y * z}\right) \) ).

(ii) Il existe un élément neutre \( e \) (i. e. pour tout \( x \in G, x * e = e * x = x \) ).

> (ii) There exists a neutral element \( e \) (i. e. for all \( x \in G, x * e = e * x = x \) ).

(iii) Tout élément a un symétrique (i. e. pour tout \( x \in G \) , il existe \( y \in G \) tel que \( x * y = \; y * x = e) \) .

> (iii) Every element has an inverse (i. e. for all \( x \in G \) , there exists \( y \in G \) such that \( x * y = \; y * x = e) \) .

Si la loi * est commutative, on parle de groupe commutatif (ou abélien).

> If the law * is commutative, it is called a commutative (or abelian) group.

Remarque 1. - L’élément neutre \( e \) de \( \left( {G, * }\right) \) est unique.

> Remark 1. - The neutral element \( e \) of \( \left( {G, * }\right) \) is unique.

- Pour tout \( x \in  G, x \) a un unique symétrique, souvent noté \( {x}^{-1} \) .

> - For every \( x \in  G, x \) , there is a unique inverse, often denoted \( {x}^{-1} \) .

DéFINITION 2. Soit \( \left( {G, * }\right) \) un groupe; on dit que \( H \subset G \) est un sous-groupe de \( G \) si la restriction de la loi * à \( H \) lui confère une structure de groupe.

> DEFINITION 2. Let \( \left( {G, * }\right) \) be a group; we say that \( H \subset G \) is a subgroup of \( G \) if the restriction of the law * to \( H \) gives it a group structure.

Exemple 1. L'ensemble \( \mathbb{Z} \) des entiers, muni de la loi d'addition, est un groupe. Pour tout \( n \in \mathbb{N}, n\mathbb{Z} \) est un sous-groupe de \( \left( {\mathbb{Z}, + }\right) \) . Réciproquement, on peut démontrer que tous les sous-groupes de \( \left( {\mathbb{Z}, + }\right) \) sont de la forme \( n\mathbb{Z} \) avec \( n \in \mathbb{N} \) .

> Example 1. The set \( \mathbb{Z} \) of integers, equipped with the addition law, is a group. For any \( n \in \mathbb{N}, n\mathbb{Z} \) is a subgroup of \( \left( {\mathbb{Z}, + }\right) \) . Conversely, it can be shown that all subgroups of \( \left( {\mathbb{Z}, + }\right) \) are of the form \( n\mathbb{Z} \) with \( n \in \mathbb{N} \) .

Dorénavant, la loi * d'un groupe sera notée multiplicativement (la notation additive est réservée aux groupes abéliens).

> From now on, the law * of a group will be denoted multiplicatively (additive notation is reserved for abelian groups).

Proposition 1. Soit \( G \) un groupe et \( H \subset G \) . L’ensemble \( H \) est un sous-groupe de \( G \) si et seulement si \( H \neq \varnothing \) et pour tout couple \( \left( {x, y}\right) \in H \) on a \( x{y}^{-1} \in H \) .

> Proposition 1. Let \( G \) be a group and \( H \subset G \) . The set \( H \) is a subgroup of \( G \) if and only if \( H \neq \varnothing \) and for any pair \( \left( {x, y}\right) \in H \) we have \( x{y}^{-1} \in H \) .

Proposition 2. Une intersection de sous-groupes d'un groupe \( G \) est un sous-groupe de \( G \) .

> Proposition 2. An intersection of subgroups of a group \( G \) is a subgroup of \( G \) .

Remarque 2. Le résultat est faux dans le cas d'une réunion (voir l'exercice 2).

> Remark 2. The result is false in the case of a union (see exercise 2).

DéFINITION 3. Soit \( \left( {G, \cdot }\right) \) un groupe. On appelle centre de \( G \) , noté \( \mathcal{Z}\left( G\right) \) , l’ensemble des éléments de \( G \) commutant avec tous les éléments de \( G \) . L’ensemble \( \mathcal{Z}\left( G\right) \) est un sous-groupe de \( G \) . DéFINITION 4. Si \( G \) est un groupe fini, Card \( \left( G\right) \) s’appelle l’ordre de \( G \) .

> DEFINITION 3. Let \( \left( {G, \cdot }\right) \) be a group. We call the center of \( G \) , denoted \( \mathcal{Z}\left( G\right) \) , the set of elements of \( G \) that commute with all elements of \( G \) . The set \( \mathcal{Z}\left( G\right) \) is a subgroup of \( G \) . DEFINITION 4. If \( G \) is a finite group, Card \( \left( G\right) \) is called the order of \( G \) .

- THéORÉME 1 (LAGRANGE). Soit \( G \) un groupe fini. L’ordre de tout sous-groupe \( H \) de \( G \) divise l’ordre de \( G \) .

> - THEOREM 1 (LAGRANGE). Let \( G \) be a finite group. The order of any subgroup \( H \) of \( G \) divides the order of \( G \) .

Démonstration. La relation \( x\mathcal{R}y \Leftrightarrow x{y}^{-1} \in H \) est une relation d’équivalence. Si on note \( \dot{x} \) la classe de \( x \in G \) , on a \( \dot{x} = {Hx} = \{ {zx}, z \in H\} \) . (En effet : \( y \in \dot{x} \Leftrightarrow y\mathcal{R}x \Leftrightarrow y{x}^{-1} \in H \Leftrightarrow \; y \in {Hx}) \) .

> Proof. The relation \( x\mathcal{R}y \Leftrightarrow x{y}^{-1} \in H \) is an equivalence relation. If we denote \( \dot{x} \) as the class of \( x \in G \) , we have \( \dot{x} = {Hx} = \{ {zx}, z \in H\} \) . (Indeed: \( y \in \dot{x} \Leftrightarrow y\mathcal{R}x \Leftrightarrow y{x}^{-1} \in H \Leftrightarrow \; y \in {Hx}) \) .

Pour tout \( x \in G \) , l’application \( H \rightarrow {Hx}\;y \mapsto {yx} \) est une bijection comme on le vérifie facilement, donc \( \operatorname{Card}\left( {Hx}\right) = \operatorname{Card}\left( H\right) \) . Ainsi, les classes ont toutes \( \operatorname{Card}\left( H\right) \) éléments. Les classes d’équivalences formant une partition de \( G \) , on a donc \( \operatorname{Card}\left( G\right) = n\operatorname{Card}\left( H\right) \) où \( n = \; \operatorname{Card}\left( {G/\mathcal{R}}\right) \) désigne le nombre de classes d’équivalence.

> For any \( x \in G \) , the map \( H \rightarrow {Hx}\;y \mapsto {yx} \) is a bijection as can be easily verified, so \( \operatorname{Card}\left( {Hx}\right) = \operatorname{Card}\left( H\right) \) . Thus, the classes all have \( \operatorname{Card}\left( H\right) \) elements. Since the equivalence classes form a partition of \( G \) , we therefore have \( \operatorname{Card}\left( G\right) = n\operatorname{Card}\left( H\right) \) where \( n = \; \operatorname{Card}\left( {G/\mathcal{R}}\right) \) denotes the number of equivalence classes.

Remarque 3. - Les classes utilisées dans la preuve du théorème (de la forme \( {Hx} \) ) sont appelées classes à droite suivant le sous-groupe \( H \) . On aurait aussi pu considérer la relation d’équivalence définie par \( x\mathcal{R}y \Leftrightarrow {x}^{-1}y \in H \) , dont les classes sont de la forme \( {xH} \) et sont appelées classes à gauche suivant \( H \) .

> Remark 3. - The classes used in the proof of the theorem (of the form \( {Hx} \) ) are called right cosets of the subgroup \( H \) . One could also have considered the equivalence relation defined by \( x\mathcal{R}y \Leftrightarrow {x}^{-1}y \in H \) , whose classes are of the form \( {xH} \) and are called left cosets of \( H \) .

- L’entier \( \operatorname{Card}\left( {G/\mathcal{R}}\right) \) est appelé indice de \( H \) dans \( G \) , et noté \( \left\lbrack  {G : H}\right\rbrack \) . On a \( \operatorname{Card}\left( G\right)  = \left\lbrack  {G : H}\right\rbrack   \times  \operatorname{Card}\left( H\right) . \)

> - The integer \( \operatorname{Card}\left( {G/\mathcal{R}}\right) \) is called the index of \( H \) in \( G \) , and denoted by \( \left\lbrack  {G : H}\right\rbrack \) . We have \( \operatorname{Card}\left( G\right)  = \left\lbrack  {G : H}\right\rbrack   \times  \operatorname{Card}\left( H\right) . \)

Sous-groupes distingués.

> Normal subgroups.

DéFINITION 5. Soit \( G \) un groupe. Un sous-groupe \( H \) de \( G \) est dit distingué (ou normal, ou invariant) dans \( G \) si pour tout \( x \in G,{xH} = {Hx} \) .

> DEFINITION 5. Let \( G \) be a group. A subgroup \( H \) of \( G \) is said to be normal (or invariant) in \( G \) if for all \( x \in G,{xH} = {Hx} \) .

Exemple 2. - Tout sous-groupe d’un groupe abélien \( G \) est distingué dans \( G \) .

> Example 2. - Every subgroup of an abelian group \( G \) is normal in \( G \) .

- Le centre \( \mathcal{Z}\left( G\right) \) d’un groupe \( G \) est distingué dans \( G \) . Plus généralement, tout sous-groupe de \( \mathcal{Z}\left( G\right) \) est un sous-groupe distingué dans \( G \) .

> - The center \( \mathcal{Z}\left( G\right) \) of a group \( G \) is normal in \( G \) . More generally, any subgroup of \( \mathcal{Z}\left( G\right) \) is a normal subgroup in \( G \) .

Remarque 4. Lorsque \( H \) est un sous-groupe distingué de \( G \) , on note parfois \( H \vartriangleleft G \) . Il faut prendre garde à cette notation qui n’est pas transitive. Autrement dit, si \( L \vartriangleleft H \) et si \( H \vartriangleleft G \) , il est faux d’écrire \( L \vartriangleleft G \) .

> Remark 4. When \( H \) is a normal subgroup of \( G \) , we sometimes write \( H \vartriangleleft G \) . One must be careful with this notation, which is not transitive. In other words, if \( L \vartriangleleft H \) and if \( H \vartriangleleft G \) , it is incorrect to write \( L \vartriangleleft G \) .

Le résultat qui suit est parfois un moyen pratique de montrer qu'un sous-groupe est distingué.

> The following result is sometimes a practical way to show that a subgroup is normal.

Proposition 3. Soit \( G \) un groupe. Un sous-groupe \( H \) de \( G \) est distingué dans \( G \) si et seulement si pour tout \( x \in G,{xH}{x}^{-1} \subset H \) .

> Proposition 3. Let \( G \) be a group. A subgroup \( H \) of \( G \) is normal in \( G \) if and only if for all \( x \in G,{xH}{x}^{-1} \subset H \) .

Groupes quotient. Soit \( G \) un groupe. On recherche les relations d’équivalence \( \mathcal{R} \) sur \( G \) telles que \( G/\mathcal{R} \) soit un groupe. Un moyen naturel de faire de \( G/\mathcal{R} \) un groupe est de le munir de la loi \( \bar{x} \cdot \bar{y} = \overline{\left( xy\right) } \) (la notation \( \bar{x} \) désigne la classe de l’élément \( x \) ). Encore faut-il que \( \overline{\left( xy\right) } \) ne dépende pas des représentants \( x \) et \( y \) des classes \( \bar{x} \) et \( \bar{y} \) , c’est-à-dire que si \( x\mathcal{R}{x}^{\prime } \) et \( y\mathcal{R}{y}^{\prime } \) , on veut \( \left( {xy}\right) \mathcal{R}\left( {{x}^{\prime }{y}^{\prime }}\right) \) . Si tel est le cas, on dit que \( \mathcal{R} \) est compatible avec la structure de groupe.

> Quotient groups. Let \( G \) be a group. We look for equivalence relations \( \mathcal{R} \) on \( G \) such that \( G/\mathcal{R} \) is a group. A natural way to make \( G/\mathcal{R} \) a group is to equip it with the operation \( \bar{x} \cdot \bar{y} = \overline{\left( xy\right) } \) (the notation \( \bar{x} \) denotes the class of the element \( x \) ). It is still necessary that \( \overline{\left( xy\right) } \) does not depend on the representatives \( x \) and \( y \) of the classes \( \bar{x} \) and \( \bar{y} \) , that is to say that if \( x\mathcal{R}{x}^{\prime } \) and \( y\mathcal{R}{y}^{\prime } \) , we want \( \left( {xy}\right) \mathcal{R}\left( {{x}^{\prime }{y}^{\prime }}\right) \) . If this is the case, we say that \( \mathcal{R} \) is compatible with the group structure.

On montre que les relations d'équivalence compatibles avec la structure de groupe sont les relations \( x\mathcal{R}y \Leftrightarrow x{y}^{-1} \in H \) , où \( H \) est un sous-groupe distingué de \( G \) (dans ce cas, les classes à gauche suivant \( H \) coïncident avec les classes à droite suivant \( H \) ). Muni de la loi quotient définie plus haut, l’ensemble quotient \( G/\mathcal{R} \) est alors un groupe appelé groupe quotient et noté \( G/H \) . Si \( G \) est fini, on a \( \operatorname{Card}\left( G\right) = \operatorname{Card}\left( {G/H}\right) \cdot \operatorname{Card}\left( H\right) \) .

> We show that the equivalence relations compatible with the group structure are the relations \( x\mathcal{R}y \Leftrightarrow x{y}^{-1} \in H \), where \( H \) is a normal subgroup of \( G \) (in this case, the left cosets modulo \( H \) coincide with the right cosets modulo \( H \)). Equipped with the quotient operation defined above, the quotient set \( G/\mathcal{R} \) is then a group called the quotient group and denoted by \( G/H \). If \( G \) is finite, we have \( \operatorname{Card}\left( G\right) = \operatorname{Card}\left( {G/H}\right) \cdot \operatorname{Card}\left( H\right) \).

Exemple 3. Si \( n \) est un entier naturel non nul, \( n\mathbb{Z} \) est un sous-groupe du groupe additif \( \left( {\mathbb{Z}, + }\right) \) . Ce dernier étant commutatif, on est même assuré du fait que \( n\mathbb{Z} \) est un sous-groupe distingué de \( \mathbb{Z} \) . Ainsi, on peut définir le groupe quotient \( \mathbb{Z}/n\mathbb{Z} \) (défini tel quel, \( \mathbb{Z}/n\mathbb{Z} \) ne possède qu'une structure additive; la structure d'anneau de \( \mathbb{Z}/n\mathbb{Z} \) n'est introduite que lorsque l'on parle d'anneau quotient - voir l'exemple 3 de la partie 3.2).

> Example 3. If \( n \) is a non-zero natural number, \( n\mathbb{Z} \) is a subgroup of the additive group \( \left( {\mathbb{Z}, + }\right) \). Since the latter is commutative, we are even guaranteed that \( n\mathbb{Z} \) is a normal subgroup of \( \mathbb{Z} \). Thus, we can define the quotient group \( \mathbb{Z}/n\mathbb{Z} \) (defined as such, \( \mathbb{Z}/n\mathbb{Z} \) only possesses an additive structure; the ring structure of \( \mathbb{Z}/n\mathbb{Z} \) is only introduced when discussing quotient rings - see example 3 of section 3.2).

Morphismes de groupes. Dans ce paragraphe, \( G \) et \( {G}^{\prime } \) désignent deux groupes, dont les éléments neutres sont notés respectivement \( e \) et \( {e}^{\prime } \) .

> Group morphisms. In this paragraph, \( G \) and \( {G}^{\prime } \) denote two groups, whose identity elements are denoted respectively by \( e \) and \( {e}^{\prime } \).

DéFINITION 6. Soit \( \varphi : G \rightarrow {G}^{\prime } \) une application. On dit que \( \varphi \) est un morphisme de groupes si pour tous \( x, y \in G,\varphi \left( {xy}\right) = \varphi \left( x\right) \varphi \left( y\right) \) .

> DEFINITION 6. Let \( \varphi : G \rightarrow {G}^{\prime } \) be a mapping. We say that \( \varphi \) is a group morphism if for all \( x, y \in G,\varphi \left( {xy}\right) = \varphi \left( x\right) \varphi \left( y\right) \).

- Si \( \varphi \) est bijective, on dit que \( \varphi \) est un isomorphisme de groupes; si de plus \( {G}^{\prime } = G \) , on dit que \( \varphi \) est un automorphisme du groupe \( G \) .

> - If \( \varphi \) is bijective, we say that \( \varphi \) is a group isomorphism; if furthermore \( {G}^{\prime } = G \), we say that \( \varphi \) is an automorphism of the group \( G \).

- L’ensemble \( {\varphi }^{-1}\left( \left\{  {e}^{\prime }\right\}  \right) \) est appelé noyau de \( \varphi \) et noté Ker \( \varphi \) . Le morphisme \( \varphi \) est injectif si et seulement si Ker \( \varphi  = \{ e\} \) .

> - The set \( {\varphi }^{-1}\left( \left\{  {e}^{\prime }\right\}  \right) \) is called the kernel of \( \varphi \) and is denoted by Ker \( \varphi \). The morphism \( \varphi \) is injective if and only if Ker \( \varphi  = \{ e\} \).

Proposition 4. Soit \( \varphi : G \rightarrow {G}^{\prime } \) un morphisme de groupes, \( H \) et \( {H}^{\prime } \) deux sous-groupes de \( G,{G}^{\prime } \) . Alors

> Proposition 4. Let \( \varphi : G \rightarrow {G}^{\prime } \) be a group morphism, \( H \) and \( {H}^{\prime } \) two subgroups of \( G,{G}^{\prime } \). Then

— \( \varphi \left( H\right) \) est un sous-groupe de \( {G}^{\prime } \) , distingué si H est distingué dans \( G \) et si \( \varphi \) est surjectif.

> — \( \varphi \left( H\right) \) is a subgroup of \( {G}^{\prime } \), normal if H is normal in \( G \) and if \( \varphi \) is surjective.

— \( {\varphi }^{-1}\left( {H}^{\prime }\right) \) est un sous-groupe de \( G \) , distingué dans \( G \) si \( {H}^{\prime } \) est distingué dans \( {G}^{\prime } \) .

> — \( {\varphi }^{-1}\left( {H}^{\prime }\right) \) is a subgroup of \( G \), normal in \( G \) if \( {H}^{\prime } \) is normal in \( {G}^{\prime } \).

En particulier, \( \left\{ {e}^{\prime }\right\} \) étant distingué dans \( {G}^{\prime } \) , \( \operatorname{Ker}\varphi = {\varphi }^{-1}\left( \left\{ {e}^{\prime }\right\} \right) \) est distingué dans \( G \) . De plus, le groupe quotient \( G/\operatorname{Ker}\varphi \) est isomorphe \( \dot{a}\varphi \left( G\right) \) .

> In particular, since \( \left\{ {e}^{\prime }\right\} \) is normal in \( {G}^{\prime } \), \( \operatorname{Ker}\varphi = {\varphi }^{-1}\left( \left\{ {e}^{\prime }\right\} \right) \) is normal in \( G \). Furthermore, the quotient group \( G/\operatorname{Ker}\varphi \) is isomorphic to \( \dot{a}\varphi \left( G\right) \).

\( \rightarrow \) Remarque 5. Ce dernier résultat est important. En particulier, si \( \varphi : G \rightarrow {G}^{\prime } \) est un morphisme surjectif, le groupe \( {G}^{\prime } \) est isomorphe à \( G/\operatorname{Ker}\varphi \) . Cet isomorphisme est souvent utilisé lors de la résolution d'un exercice ou d'un problème sur les groupes.

> \( \rightarrow \) Remark 5. This last result is important. In particular, if \( \varphi : G \rightarrow {G}^{\prime } \) is a surjective morphism, the group \( {G}^{\prime } \) is isomorphic to \( G/\operatorname{Ker}\varphi \). This isomorphism is often used when solving an exercise or a problem on groups.

##### Group of inner automorphisms.

*Français : Groupe des automorphismes intérieurs.*

DéFINITION 7. Soit \( G \) un groupe. Pour tout \( a \in G \) , l’application \( {\varphi }_{a} : G \rightarrow G\;x \mapsto {ax}{a}^{-1} \) est un automorphisme de \( G \) . L’ensemble \( \mathcal{A} = \left\{ {{\varphi }_{a}, a \in G}\right\} \) , muni de la loi de composition, est un groupe (on a d’ailleurs \( {\varphi }_{a} \circ {\varphi }_{b} = {\varphi }_{ab} \) ), appelé groupe des automorphismes intérieurs de \( G \) .

> DEFINITION 7. Let \( G \) be a group. For any \( a \in G \), the map \( {\varphi }_{a} : G \rightarrow G\;x \mapsto {ax}{a}^{-1} \) is an automorphism of \( G \). The set \( \mathcal{A} = \left\{ {{\varphi }_{a}, a \in G}\right\} \), equipped with the composition law, is a group (we have \( {\varphi }_{a} \circ {\varphi }_{b} = {\varphi }_{ab} \)), called the group of inner automorphisms of \( G \).
