#### 1.3. Diagonalizable endomorphisms

*Français : 1.3. Endomorphismes diagonalisables*

DéFINITION 5. Soit \( f \in \mathcal{L}\left( E\right) \) . On dit que \( f \) est diagonalisable s’il existe une base de vecteurs propres de \( f \) . On dit que \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) est diagonalisable si \( A \) est semblable à une matrice diagonale.

> DEFINITION 5. Let \( f \in \mathcal{L}\left( E\right) \). We say that \( f \) is diagonalizable if there exists a basis of eigenvectors of \( f \). We say that \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) is diagonalizable if \( A \) is similar to a diagonal matrix.

Remarque 7. Un endomorphisme \( f \) est diagonalisable si et seulement si sa matrice dans une base quelconque de \( E \) est diagonalisable.

> Remark 7. An endomorphism \( f \) is diagonalizable if and only if its matrix in any basis of \( E \) is diagonalizable.

PROPOSITION 4. Soit \( f \in \mathcal{L}\left( E\right) \) . Si \( {P}_{f} \) est scindé sur \( \mathbb{K} \) et a toutes ses racines simples, alors \( f \) est diagonalisable.

> PROPOSITION 4. Let \( f \in \mathcal{L}\left( E\right) \). If \( {P}_{f} \) splits over \( \mathbb{K} \) and has all simple roots, then \( f \) is diagonalizable.

Démonstration. Écrivons \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) . Pour tout \( i,{\lambda }_{i} \) est valeur propre de \( f \) donc il existe \( {x}_{i} \) un vecteur propre de \( f \) associé à la valeur propre \( {\lambda }_{i} \) . D’après le théorème 1, les \( {x}_{i} \) forment une famille libre,à \( n \) éléments, et forment donc une base de \( E \) .

> Proof. Let us write \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \) . For any \( i,{\lambda }_{i} \) is an eigenvalue of \( f \) so there exists \( {x}_{i} \) an eigenvector of \( f \) associated with the eigenvalue \( {\lambda }_{i} \) . According to theorem 1, the \( {x}_{i} \) form a linearly independent family, with \( n \) elements, and thus form a basis of \( E \) .

Proposition 5. Soit \( f \in \mathcal{L}\left( E\right) ,\lambda \in \mathbb{K} \) une racine de \( {P}_{f} \) d’ordre de multiplicité h. Alors \( \dim {E}_{\lambda } \leq h \) .

> Proposition 5. Let \( f \in \mathcal{L}\left( E\right) ,\lambda \in \mathbb{K} \) be a root of \( {P}_{f} \) with multiplicity order h. Then \( \dim {E}_{\lambda } \leq h \) .

Démonstration. Le sous-espace propre \( {E}_{\lambda } \) est stable par \( f \) . Soit \( g = {f}_{\mid {E}_{\lambda }} \in \mathcal{L}\left( {E}_{\lambda }\right) \) . D’après la proposition 2, \( {P}_{g} \) divise \( {P}_{f} \) . Comme \( g = \lambda {\operatorname{Id}}_{{E}_{\lambda }} \) , on a \( {P}_{g} = {\left( \lambda - X\right) }^{\dim {E}_{\lambda }} \) , donc dim \( {E}_{\lambda } \leq h \) .

> Proof. The eigenspace \( {E}_{\lambda } \) is stable by \( f \) . Let \( g = {f}_{\mid {E}_{\lambda }} \in \mathcal{L}\left( {E}_{\lambda }\right) \) . According to proposition 2, \( {P}_{g} \) divides \( {P}_{f} \) . Since \( g = \lambda {\operatorname{Id}}_{{E}_{\lambda }} \) , we have \( {P}_{g} = {\left( \lambda - X\right) }^{\dim {E}_{\lambda }} \) , so dim \( {E}_{\lambda } \leq h \) .

- THÉORÉME 2. Soit \( f \in  \mathcal{L}\left( E\right) \) . Les propositions suivantes sont équivalentes.

> - THEOREM 2. Let \( f \in  \mathcal{L}\left( E\right) \) . The following propositions are equivalent.

(i) \( f \) est diagonalisable.

> (i) \( f \) is diagonalizable.

(ii) \( {P}_{f} \) est scindé sur \( \mathbb{K} \) et pour toute racine \( {\lambda }_{i} \) de \( {P}_{f} \) d’ordre de multiplicité \( {h}_{i},{h}_{i} = \; \dim {E}_{{\lambda }_{i}} \) .

> (ii) \( {P}_{f} \) splits over \( \mathbb{K} \) and for every root \( {\lambda }_{i} \) of \( {P}_{f} \) with multiplicity order \( {h}_{i},{h}_{i} = \; \dim {E}_{{\lambda }_{i}} \) .

(iii) Il existe des valeurs propres \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) de \( f \) vérifiant \( E = {E}_{{\lambda }_{1}} \oplus \cdots \oplus {E}_{{\lambda }_{p}} \) .

> (iii) There exist eigenvalues \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) of \( f \) satisfying \( E = {E}_{{\lambda }_{1}} \oplus \cdots \oplus {E}_{{\lambda }_{p}} \) .

Démonstration. (i) \( \Rightarrow \) (ii). Soit \( B \) une base de vecteurs propres de \( f \) . La matrice \( M \) de \( f \) dans \( B \) est diagonale, et si \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) désignent les valeurs propres de \( f \) , la diagonale de \( M \) est constituée des \( {\lambda }_{i} \) . Pour tout \( i,1 \leq i \leq p \) , notons \( {h}_{i} \) le nombre de fois que \( {\lambda }_{i} \) apparaît dans la diagonale de \( M \) , de sorte que \( {P}_{f} = {P}_{M} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{p}{\left( X - {\lambda }_{i}\right) }^{{h}_{i}} \) . Pour tout \( i,1 \leq i \leq p \) , il existe \( {h}_{i} \) vecteurs de la base \( B \) vérifiant \( f\left( x\right) = {\lambda }_{i}x \) , c’est-à-dire \( {h}_{i} \) vecteurs linéairement indépendants dans \( {E}_{{\lambda }_{i}} \) , donc dim \( {E}_{{\lambda }_{i}} \geq {h}_{i} \) . Donc dim \( {E}_{{\lambda }_{i}} = {h}_{i} \) d’après la proposition précédente.

> Proof. (i) \( \Rightarrow \) (ii). Let \( B \) be a basis of eigenvectors of \( f \) . The matrix \( M \) of \( f \) in \( B \) is diagonal, and if \( {\lambda }_{1},\ldots ,{\lambda }_{p} \) denote the eigenvalues of \( f \) , the diagonal of \( M \) consists of the \( {\lambda }_{i} \) . For any \( i,1 \leq i \leq p \) , let \( {h}_{i} \) denote the number of times \( {\lambda }_{i} \) appears on the diagonal of \( M \) , such that \( {P}_{f} = {P}_{M} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{p}{\left( X - {\lambda }_{i}\right) }^{{h}_{i}} \) . For any \( i,1 \leq i \leq p \) , there exist \( {h}_{i} \) vectors of the basis \( B \) satisfying \( f\left( x\right) = {\lambda }_{i}x \) , that is to say \( {h}_{i} \) linearly independent vectors in \( {E}_{{\lambda }_{i}} \) , so dim \( {E}_{{\lambda }_{i}} \geq {h}_{i} \) . Thus dim \( {E}_{{\lambda }_{i}} = {h}_{i} \) according to the previous proposition.

(ii) \( \Rightarrow \) (iii). Écrivons \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{p}{\left( X - {\lambda }_{i}\right) }^{{h}_{i}} \) , les \( {\lambda }_{i} \) étant distincts. Soit \( F = { \oplus }_{i = 1}^{p}{E}_{{\lambda }_{i}} \) . On a dim \( F = \mathop{\sum }\limits_{{i = 1}}^{p}\dim {E}_{{\lambda }_{i}} = \mathop{\sum }\limits_{{i = 1}}^{p}{h}_{i} = \deg \left( {P}_{f}\right) = n \) , donc \( F = E \) .

> (ii) \( \Rightarrow \) (iii). Let us write \( {P}_{f} = {\left( -1\right) }^{n}\mathop{\prod }\limits_{{i = 1}}^{p}{\left( X - {\lambda }_{i}\right) }^{{h}_{i}} \) , where the \( {\lambda }_{i} \) are distinct. Let \( F = { \oplus }_{i = 1}^{p}{E}_{{\lambda }_{i}} \) . We have dim \( F = \mathop{\sum }\limits_{{i = 1}}^{p}\dim {E}_{{\lambda }_{i}} = \mathop{\sum }\limits_{{i = 1}}^{p}{h}_{i} = \deg \left( {P}_{f}\right) = n \) , thus \( F = E \) .

(iii) \( \Rightarrow \) (i). Si pour tout \( i,{B}_{i} \) désigne une base de \( {E}_{{\lambda }_{i}} \) , alors il est clair que \( B = {B}_{1} \cup \cdots \cup {B}_{p} \) est une base de vecteurs propres de \( f \) .

> (iii) \( \Rightarrow \) (i). If for every \( i,{B}_{i} \) denotes a basis of \( {E}_{{\lambda }_{i}} \) , then it is clear that \( B = {B}_{1} \cup \cdots \cup {B}_{p} \) is a basis of eigenvectors of \( f \) .

Proposition 6. Soit \( f \in \mathcal{L}\left( E\right) \) diagonalisable et \( F \) un s.e.v de \( E \) stable par \( f \) . Alors \( {f}_{\mid F} \in \mathcal{L}\left( F\right) \) est diagonalisable.

> Proposition 6. Let \( f \in \mathcal{L}\left( E\right) \) be diagonalizable and \( F \) a subspace of \( E \) stable under \( f \) . Then \( {f}_{\mid F} \in \mathcal{L}\left( F\right) \) is diagonalizable.

A ce stade du cours, ce résultat est non trivial. Il sera démontré ultérieurement dans ce chapitre (voir la conséquence du théorème 2 page 185).

> At this stage of the course, this result is non-trivial. It will be proven later in this chapter (see the consequence of theorem 2 on page 185).
