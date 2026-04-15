#### 1.2. Bases and dimension of a vector space

*Français : 1.2. Bases et dimension d'un espace vectoriel*

##### Basis of a vector space.

*Français : Base d'un espace vectoriel.*

DéFINITION 9. Une famille libre et génératrice d’un e.v \( E \) est appelée une base de \( E \) .

> DEFINITION 9. A linearly independent and generating family of a v.s. \( E \) is called a basis of \( E \) .

Proposition 4. Soit \( E \) un \( \mathbb{K} \) -e.v admettant une base \( {\left( {e}_{i}\right) }_{i \in I} \) . Alors tout vecteur \( x \) de \( E \) s’écrit de manière unique comme combinaison linéaire des \( {\left( {e}_{i}\right) }_{i \in I} : x = \mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}{x}_{i} \) (avec les \( {\lambda }_{i} \) tous nuls sauf un nombre fini). Les \( {\left( {\lambda }_{i}\right) }_{i \in I} \) s’appellent les coordonnées de \( x \) dans la base \( {\left( {e}_{i}\right) }_{i \in I} \) .

> Proposition 4. Let \( E \) be a \( \mathbb{K} \) -v.s. admitting a basis \( {\left( {e}_{i}\right) }_{i \in I} \) . Then any vector \( x \) of \( E \) can be written uniquely as a linear combination of \( {\left( {e}_{i}\right) }_{i \in I} : x = \mathop{\sum }\limits_{{i \in I}}{\lambda }_{i}{x}_{i} \) (with the \( {\lambda }_{i} \) all zero except for a finite number). The \( {\left( {\lambda }_{i}\right) }_{i \in I} \) are called the coordinates of \( x \) in the basis \( {\left( {e}_{i}\right) }_{i \in I} \) .

Exemple 3. La famille \( {\left( {e}_{i}\right) }_{1 \leq i \leq n} \) (où \( {e}_{i} = \left( {0,\ldots ,0,1,0,\ldots ,0}\right) \) , le 1 se trouvant à la \( i \) -ième coordonnée), est une base de \( {\mathbb{K}}^{n} \) appelée base canonique de \( {\mathbb{K}}^{n} \) .

> Example 3. The family \( {\left( {e}_{i}\right) }_{1 \leq i \leq n} \) (where \( {e}_{i} = \left( {0,\ldots ,0,1,0,\ldots ,0}\right) \) , the 1 being at the \( i \) -th coordinate), is a basis of \( {\mathbb{K}}^{n} \) called the canonical basis of \( {\mathbb{K}}^{n} \) .

- La famille \( {\left( {X}^{n}\right) }_{n \in  \mathbb{N}} \) est une base de \( \mathbb{K}\left\lbrack  X\right\rbrack \) appelée base canonique de \( \mathbb{K}\left\lbrack  X\right\rbrack \) .

> - The family \( {\left( {X}^{n}\right) }_{n \in  \mathbb{N}} \) is a basis of \( \mathbb{K}\left\lbrack  X\right\rbrack \) called the canonical basis of \( \mathbb{K}\left\lbrack  X\right\rbrack \) .

DÉFINITION 10. On dit qu'un \( \mathbb{K} \) -e.v \( E \) est de dimension finie s’il existe une famille géné- ratrice finie de \( E \) . Dans la cas contraire, on dit que \( E \) est de dimension infinie.

> DEFINITION 10. A \( \mathbb{K} \) -v.s. \( E \) is said to be finite-dimensional if there exists a finite generating family of \( E \) . Otherwise, \( E \) is said to be infinite-dimensional.

L'existence de base en dimension finie est assurée par le théorème suivant.

> The existence of a basis in finite dimension is guaranteed by the following theorem.

THÉORÉME 2. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, \( \mathcal{G} \) un système fini de générateurs de \( E,\mathcal{L} \subset \mathcal{G} \) un système libre. Alors il existe une base \( B \) de \( E \) telle que \( \mathcal{L} \subset B \subset \mathcal{G} \) .

> THEOREM 2. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s., \( \mathcal{G} \) a finite system of generators of \( E,\mathcal{L} \subset \mathcal{G} \) a free system. Then there exists a basis \( B \) of \( E \) such that \( \mathcal{L} \subset B \subset \mathcal{G} \) .

Conséquences en dimension finie.

> Consequences in finite dimension.

- Tout K-e.v de dimension finie admet une base.

> - Every finite-dimensional K-v.s. admits a basis.

- De toute famille génératrice de \( E \) on peut extraire une base de \( E \) .

> - From any generating family of \( E \) , one can extract a basis of \( E \) .

— Toute partie libre peut être complétée en une base (résultat connu sous le nom de théorème de la base incomplète).

> — Any free set can be extended to a basis (a result known as the basis extension theorem).

Remarque 6. Le théorème 2 reste vrai en dimension infinie, mais sa démonstration fait appel à l'axiome du choix.

> Remark 6. Theorem 2 remains true in infinite dimension, but its proof relies on the axiom of choice.

##### Dimension theory.

*Français : Théorie de la dimension.*

THÉORÉME 3. Soit E un \( \mathbb{K} \) -e.v de dimension finie. Toutes les bases de E ont même cardinal n. L’entier \( n \) s’appelle dimension de \( E \) , et est noté \( {\dim }_{\mathbb{K}}E \) (avec par convention \( \left. {{\dim }_{\mathbb{K}}E = 0\text{ si }E = \{ 0\} }\right) \) .

> THEOREM 3. Let E be a finite-dimensional \( \mathbb{K} \) -v.s. All bases of E have the same cardinality n. The integer \( n \) is called the dimension of \( E \) , and is denoted by \( {\dim }_{\mathbb{K}}E \) (with the convention \( \left. {{\dim }_{\mathbb{K}}E = 0\text{ si }E = \{ 0\} }\right) \) .

Proposition 5. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Alors

> Proposition 5. Let \( E \) be a \( \mathbb{K} \) -v.s. of finite dimension \( n \in {\mathbb{N}}^{ * } \) . Then

- Tout système libre de \( n \) vecteurs de \( E \) est une base de \( E \) .

> - Any free system of \( n \) vectors of \( E \) is a basis of \( E \) .

- Tout système générateur de \( n \) vecteurs de \( E \) est une base de \( E \) .

> - Any generating system of \( n \) vectors of \( E \) is a basis of \( E \) .

Proposition 6. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) . Soient \( {E}_{1},\ldots ,{E}_{k}k \) s.e.v de E. Alors \( E = {E}_{1} \oplus \cdots \oplus {E}_{k} \) si et seulement si \( E = {E}_{1} + \cdots + {E}_{k} \) et \( n = \mathop{\sum }\limits_{{\ell = 1}}^{k}\dim {E}_{\ell } \) .

> Proposition 6. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s. \( n \in {\mathbb{N}}^{ * } \) . Let \( {E}_{1},\ldots ,{E}_{k}k \) be a v.s.s. of E. Then \( E = {E}_{1} \oplus \cdots \oplus {E}_{k} \) if and only if \( E = {E}_{1} + \cdots + {E}_{k} \) and \( n = \mathop{\sum }\limits_{{\ell = 1}}^{k}\dim {E}_{\ell } \) .

Proposition 7. Soit E un \( \mathbb{K} \) -e.v et \( {E}_{1},{E}_{2} \) deux s.e.v de E de dimension finie. Alors \( {E}_{1} + {E}_{2} \) est un s.e.v de dimension finie et \( \dim \left( {{E}_{1} + {E}_{2}}\right) = \dim {E}_{1} + \dim {E}_{2} - \dim \left( {{E}_{1} \cap {E}_{2}}\right) \) . COROLLAIRE 1. Soit \( E \) un \( \mathbb{K} \) -e.v de dimension finie, \( {E}_{1} \) et \( {E}_{2} \) deux s.e.v de E. Alors (i), (ii) et (iii) sont équivalents :

> Proposition 7. Let E be a \( \mathbb{K} \) -v.s. and \( {E}_{1},{E}_{2} \) two finite-dimensional v.s.s. of E. Then \( {E}_{1} + {E}_{2} \) is a finite-dimensional v.s.s. and \( \dim \left( {{E}_{1} + {E}_{2}}\right) = \dim {E}_{1} + \dim {E}_{2} - \dim \left( {{E}_{1} \cap {E}_{2}}\right) \) . COROLLARY 1. Let \( E \) be a finite-dimensional \( \mathbb{K} \) -v.s., \( {E}_{1} \) and \( {E}_{2} \) two v.s.s. of E. Then (i), (ii) and (iii) are equivalent:

(i) \( E = {E}_{1} \oplus {E}_{2} \) .

> (ii) \( \dim E = \dim {E}_{1} + \dim {E}_{2} \) et \( {E}_{1} \cap {E}_{2} = \{ 0\} \) .

(ii) \( \dim E = \dim {E}_{1} + \dim {E}_{2} \) and \( {E}_{1} \cap {E}_{2} = \{ 0\} \) .

> (iii) \( \dim E = \dim {E}_{1} + \dim {E}_{2} \) et \( E = {E}_{1} + {E}_{2} \) .

(iii) \( \dim E = \dim {E}_{1} + \dim {E}_{2} \) and \( E = {E}_{1} + {E}_{2} \) .

> Si (i),(ii) ou (iii) est vérifié, on dit que \( {E}_{2} \) est un supplémentaire de \( {E}_{1} \) dans \( E \) .

If (i), (ii) or (iii) is satisfied, we say that \( {E}_{2} \) is a supplement of \( {E}_{1} \) in \( E \) .

> Remarque 7. Si \( F \) est un s.e.v de \( E \) , il y a en général une infinité de supplémentaires de \( F \) dans \( E \) .

Remark 7. If \( F \) is a v.s.s. of \( E \) , there are generally infinitely many supplements of \( F \) in \( E \) .
