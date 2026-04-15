#### 1.1. Fields

*Français : 1.1. Corps*

DÉFINITION 1. Soit \( \mathbb{K} \) un ensemble muni de deux lois internes " +" et ".". On dit que \( \left( {\mathbb{K},+, \cdot }\right) \) est un corps si

> DEFINITION 1. Let \( \mathbb{K} \) be a set equipped with two internal laws "+" and ".". We say that \( \left( {\mathbb{K},+, \cdot }\right) \) is a field if

(i) \( \left( {\mathbb{K}, + }\right) \) est un groupe abélien.

> (i) \( \left( {\mathbb{K}, + }\right) \) is an abelian group.

(ii) \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) est un groupe.

> (ii) \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) is a group.

(iii) La loi ⋅ est distributive par rapport à la loi +.

> (iii) The law ⋅ is distributive with respect to the law +.

Remarque 1. - Si la loi ⋅ est commutative, on parle de corps commutatif.

> Remark 1. - If the law ⋅ is commutative, we speak of a commutative field.

- Il revient au même de dire qu'un corps est un anneau unitaire dans lequel tout élément non nul est inversible.

> - It amounts to the same thing to say that a field is a unitary ring in which every non-zero element is invertible.

- Les corps les plus couramment rencontrés sont \( \mathbb{Q},\mathbb{R},\mathbb{C} \) et \( \mathbb{Z}/p\mathbb{Z} \) ( \( p \) premier).

> - The most commonly encountered fields are \( \mathbb{Q},\mathbb{R},\mathbb{C} \) and \( \mathbb{Z}/p\mathbb{Z} \) ( \( p \) prime).

DéFINITION 2. Soit \( \left( {\mathbb{L},+, \cdot }\right) \) un corps et \( \mathbb{K} \subset \mathbb{L} \) . On dit que \( \mathbb{K} \) est un sous-corps de \( \mathbb{L} \) si la restriction à \( \mathbb{K} \) des lois + et - lui confère une structure de corps (on dit aussi que \( \mathbb{L} \) est un surcorps ou une extension de \( \mathbb{K} \) ).

> DEFINITION 2. Let \( \left( {\mathbb{L},+, \cdot }\right) \) be a field and \( \mathbb{K} \subset \mathbb{L} \) . We say that \( \mathbb{K} \) is a subfield of \( \mathbb{L} \) if the restriction of the laws + and - to \( \mathbb{K} \) gives it a field structure (we also say that \( \mathbb{L} \) is an extension field or an extension of \( \mathbb{K} \) ).

Remarque 2. Si \( \mathbb{K} \) est un sous-corps commutatif de \( \mathbb{L},\mathbb{L} \) est un \( \mathbb{K} \) -espace vectoriel.

> Remark 2. If \( \mathbb{K} \) is a commutative subfield of \( \mathbb{L},\mathbb{L} \) , then \( \mathbb{L},\mathbb{L} \) is a \( \mathbb{K} \) -vector space.

Avec la définition de la caractéristique d'un anneau donnée page 32, on a :

> With the definition of the characteristic of a ring given on page 32, we have:

PROPOSITION 1. La caractéristique d'un corps est 0 ou un nombre premier.

> PROPOSITION 1. The characteristic of a field is 0 or a prime number.

Démonstration. Immédiat car un corps est un anneau unitaire intègre (cf. proposition 3 p. 32)

> Proof. Immediate because a field is a unital integral ring (cf. proposition 3 p. 32)

Exemple 1. Les corps \( \mathbb{Q},\mathbb{R} \) et \( \mathbb{C} \) sont de caractéristique 0; si \( p \) est un nombre premier, le corps \( \mathbb{Z}/p\mathbb{Z} \) est de caractéristique \( p \) .

> Example 1. The fields \( \mathbb{Q},\mathbb{R} \) and \( \mathbb{C} \) are of characteristic 0; if \( p \) is a prime number, the field \( \mathbb{Z}/p\mathbb{Z} \) is of characteristic \( p \) .

##### Prime field, prime subfield.

*Français : Corps premier, sous-corps premier.*

DÉFINITION 3. Un corps est dit premier s'il n'admet pas d'autres sous-corps que lui même.

> DEFINITION 3. A field is said to be prime if it admits no subfields other than itself.

Exemple 2. Les corps \( \mathbb{Q},\mathbb{Z}/p\mathbb{Z} \) (où \( p \) est un nombre premier) sont premiers.

> Example 2. The fields \( \mathbb{Q},\mathbb{Z}/p\mathbb{Z} \) (where \( p \) is a prime number) are prime.

DéFINITION 4. Soit \( \left( {\mathbb{K},+, \cdot }\right) \) un corps dont l’élément neutre de \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) est noté e.

> DEFINITION 4. Let \( \left( {\mathbb{K},+, \cdot }\right) \) be a field whose identity element of \( \left( {{\mathbb{K}}^{ * }, \cdot }\right) \) is denoted by e.

- Si \( \mathbb{K} \) est de caractéristique 0, alors \( {\mathbb{Q}}_{1} = \left\{  {\frac{ne}{me},\left( {n, m}\right)  \in  \mathbb{Z} \times  {\mathbb{Z}}^{ * }}\right\} \) est un corps premier isomorphe à Q. C’est le sous-corps premier de \( \mathbb{K} \) .

> - If \( \mathbb{K} \) is of characteristic 0, then \( {\mathbb{Q}}_{1} = \left\{  {\frac{ne}{me},\left( {n, m}\right)  \in  \mathbb{Z} \times  {\mathbb{Z}}^{ * }}\right\} \) is a prime field isomorphic to Q. It is the prime subfield of \( \mathbb{K} \) .

- Si K est de caractéristique \( p \) premier, l’application \( f : \mathbb{Z} \rightarrow  \mathbb{K}\;n \mapsto  {ne} \) est un morphisme d’anneaux et Ker \( f = p\mathbb{Z} \) . Donc \( \mathbb{Z}/ \) Ker \( f = \mathbb{Z}/p\mathbb{Z} \) est isomorphe à \( {\mathbb{K}}^{\prime } = f\left( \mathbb{Z}\right) \) , donc \( {\mathbb{K}}^{\prime } \) est un corps premier. C’est le sous-corps premier de \( \mathbb{K} \) .

> - If K is of characteristic \( p \) prime, the map \( f : \mathbb{Z} \rightarrow  \mathbb{K}\;n \mapsto  {ne} \) is a ring homomorphism and Ker \( f = p\mathbb{Z} \) . Thus \( \mathbb{Z}/ \) Ker \( f = \mathbb{Z}/p\mathbb{Z} \) is isomorphic to \( {\mathbb{K}}^{\prime } = f\left( \mathbb{Z}\right) \) , so \( {\mathbb{K}}^{\prime } \) is a prime field. It is the prime subfield of \( \mathbb{K} \) .

Exemple 3. Le corps \( \mathbb{Q} \) est le sous-corps premier de \( \mathbb{R} \) (ou de \( \mathbb{C} \) ). Le corps \( \mathbb{Z}/p\mathbb{Z} \) est le sous-corps premier de \( \mathbb{Z}/p\mathbb{Z} \) (où \( p \) est un nombre premier).

> Example 3. The field \( \mathbb{Q} \) is the prime subfield of \( \mathbb{R} \) (or of \( \mathbb{C} \) ). The field \( \mathbb{Z}/p\mathbb{Z} \) is the prime subfield of \( \mathbb{Z}/p\mathbb{Z} \) (where \( p \) is a prime number).
