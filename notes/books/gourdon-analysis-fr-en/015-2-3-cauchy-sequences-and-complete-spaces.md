#### 2.3. Cauchy sequences and complete spaces

*Français : 2.3. Suites de Cauchy et espaces complets*

DéFINITION 3. Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( \left( {x}_{n}\right) \) une suite de points de \( E \) . On dit que \( \left( {x}_{n}\right) \) est une suite de Cauchy (ou que la suite \( \left( {x}_{n}\right) \) vérifie le critère de Cauchy) si

> DEFINITION 3. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( \left( {x}_{n}\right) \) a sequence of points in \( E \) . We say that \( \left( {x}_{n}\right) \) is a Cauchy sequence (or that the sequence \( \left( {x}_{n}\right) \) satisfies the Cauchy criterion) if

\[
\left( {\forall \varepsilon  > 0,\exists N \in  \mathbb{N}}\right) ,\;\forall p > N,\forall q > N,\;\mathrm{d}\left( {{x}_{p},{x}_{q}}\right)  < \varepsilon .
\]

Remarque 3. - Une suite convergente est de Cauchy.

> Remark 3. - A convergent sequence is Cauchy.

- Une suite de Cauchy est bornée.

> - A Cauchy sequence is bounded.

— Attention ! La notion de suite de Cauchy n'est pas topologique (i. e. elle ne peut pas être définie à partir des ouverts de \( E \) ). Cependant, on a le résultat suivant.

> — Warning! The notion of a Cauchy sequence is not topological (i.e., it cannot be defined using the open sets of \( E \) ). However, we have the following result.

Proposition 6. Soient d et \( {\mathrm{d}}^{\prime } \) deux distances uniformément équivalentes de E. Une suite \( \left( {x}_{n}\right) \) est de Cauchy dans \( \left( {E,\mathrm{\;d}}\right) \) si et seulement si c’est une suite de Cauchy dans \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) . Le résultat reste vrai en particulier lorsque d et \( {\mathrm{d}}^{\prime } \) sont équivalentes.

> Proposition 6. Let d and \( {\mathrm{d}}^{\prime } \) be two uniformly equivalent metrics on E. A sequence \( \left( {x}_{n}\right) \) is Cauchy in \( \left( {E,\mathrm{\;d}}\right) \) if and only if it is a Cauchy sequence in \( \left( {E,{\mathrm{\;d}}^{\prime }}\right) \) . The result remains true in particular when d and \( {\mathrm{d}}^{\prime } \) are equivalent.

DÉFINITION 4. On dit qu'un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est complet si toute suite de Cauchy de \( E \) converge.

> DEFINITION 4. A metric space \( \left( {E,\mathrm{\;d}}\right) \) is said to be complete if every Cauchy sequence in \( E \) converges.

Un espace vectoriel normé complet s'appelle un espace de Banach.

> A complete normed vector space is called a Banach space.

Exemple 1. - Les espaces \( \mathbb{R},{\mathbb{R}}^{n}\left( {n \in {\mathbb{N}}^{ * }}\right) \) sont complets.

> Example 1. - The spaces \( \mathbb{R},{\mathbb{R}}^{n}\left( {n \in {\mathbb{N}}^{ * }}\right) \) are complete.

- L’ensemble \( \mathbb{Q} \) n’est pas complet. Par exemple, si \( \alpha  \in  \mathbb{R} \smallsetminus  \mathbb{Q} \) , une suite de points de \( \mathbb{Q} \) tendant vers \( \alpha \) est de Cauchy mais ne converge pas dans \( \mathbb{Q} \) . On verra cependant (voir l'exercice 6) que tout espace métrique peut se plonger dans un espace complet.

> - The set \( \mathbb{Q} \) is not complete. For example, if \( \alpha  \in  \mathbb{R} \smallsetminus  \mathbb{Q} \) , a sequence of points in \( \mathbb{Q} \) tending toward \( \alpha \) is Cauchy but does not converge in \( \mathbb{Q} \) . We will see, however (see exercise 6), that every metric space can be embedded into a complete space.

##### Properties of complete spaces.

*Français : Propriétés des espaces complets.*

Proposition 7. - Toute partie complète d'un espace métrique est fermée.

> Proposition 7. - Every complete subset of a metric space is closed.

- Toute partie fermée d'un espace complet est complète.

> - Every closed subset of a complete space is complete.

Proposition 8. Soient \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\ldots ,\left( {{E}_{n},{\mathrm{\;d}}_{n}}\right) \) des espaces métriques. L’espace métrique \( {E}_{1} \times \cdots \times {E}_{n} \) est complet (au sens de la distance produit) si et seulement si pour tout i, l’espace métrique \( \left( {{E}_{i},{\mathrm{\;d}}_{i}}\right) \) est complet.

> Proposition 8. Let \( \left( {{E}_{1},{\mathrm{\;d}}_{1}}\right) ,\ldots ,\left( {{E}_{n},{\mathrm{\;d}}_{n}}\right) \) be metric spaces. The metric space \( {E}_{1} \times \cdots \times {E}_{n} \) is complete (in the sense of the product metric) if and only if for every i, the metric space \( \left( {{E}_{i},{\mathrm{\;d}}_{i}}\right) \) is complete.

Proposition 9. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace complet et \( \left( {F}_{n}\right) \) une suite décroissante de fermés non vides de \( E \) , telle que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {F}_{n}\right) = 0 \) (où \( \delta \left( {F}_{n}\right) \) désigne le diamètre de \( {F}_{n} \) ). Alors il existe \( x \in E \) tel que \( { \cap }_{n \in \mathbb{N}}{F}_{n} = \{ x\} \) .

> Proposition 9. Let \( \left( {E,\mathrm{\;d}}\right) \) be a complete space and \( \left( {F}_{n}\right) \) be a decreasing sequence of non-empty closed sets in \( E \) , such that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {F}_{n}\right) = 0 \) (where \( \delta \left( {F}_{n}\right) \) denotes the diameter of \( {F}_{n} \) ). Then there exists \( x \in E \) such that \( { \cap }_{n \in \mathbb{N}}{F}_{n} = \{ x\} \) .

Démonstration. Notons \( \Gamma = { \cap }_{n \in \mathbb{N}}{F}_{n} \) .

> Proof. Let us denote \( \Gamma = { \cap }_{n \in \mathbb{N}}{F}_{n} \) .

L’ensemble \( \Gamma \) est non vide. En effet, choisissons pour tout \( n \in \mathbb{N} \) un point \( {x}_{n} \) dans \( {F}_{n} \) . Le fait que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {F}_{n}\right) = 0 \) entraîne que la suite \( \left( {x}_{n}\right) \) est de Cauchy (si \( \varepsilon > 0 \) , si \( N \) est choisi tel que \( \delta \left( {F}_{N}\right) < \varepsilon \) , alors pour tout \( p, q > N,\mathrm{\;d}\left( {{x}_{p},{x}_{q}}\right) < \varepsilon \) car \( {x}_{p},{x}_{q} \in {F}_{N} \) ), donc converge dans \( E \) puisque \( E \) est complet. Comme les \( {F}_{p} \) sont fermés et que \( {x}_{n} \in {F}_{p} \) lorsque \( n \geq p \) , la limite \( \ell \) de \( \left( {x}_{n}\right) \) appartient à \( {F}_{p} \) pour tout \( p \) , donc à \( \Gamma \) . Ainsi, \( \Gamma \neq \varnothing \) .

> The set \( \Gamma \) is non-empty. Indeed, let us choose for every \( n \in \mathbb{N} \) a point \( {x}_{n} \) in \( {F}_{n} \). The fact that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\delta \left( {F}_{n}\right) = 0 \) implies that the sequence \( \left( {x}_{n}\right) \) is Cauchy (if \( \varepsilon > 0 \), if \( N \) is chosen such that \( \delta \left( {F}_{N}\right) < \varepsilon \), then for all \( p, q > N,\mathrm{\;d}\left( {{x}_{p},{x}_{q}}\right) < \varepsilon \) because \( {x}_{p},{x}_{q} \in {F}_{N} \)), therefore it converges in \( E \) since \( E \) is complete. As the \( {F}_{p} \) are closed and \( {x}_{n} \in {F}_{p} \) when \( n \geq p \), the limit \( \ell \) of \( \left( {x}_{n}\right) \) belongs to \( {F}_{p} \) for all \( p \), and thus to \( \Gamma \). Thus, \( \Gamma \neq \varnothing \).

Le fait que \( \left( {\delta \left( {F}_{n}\right) }\right) \) tende vers 0 montre que \( \Gamma \) a au plus un élément, d’où le résultat.

> The fact that \( \left( {\delta \left( {F}_{n}\right) }\right) \) tends to 0 shows that \( \Gamma \) has at most one element, hence the result.

- THÉORÉME 0 (DU POINT FIXE). Soit (E, d) un espace métrique complet, et une application \( f : E \rightarrow  E \) telle que

> - THEOREM 0 (FIXED POINT). Let (E, d) be a complete metric space, and a mapping \( f : E \rightarrow  E \) such that

\[
\exists k \in  \rbrack 0,1\lbrack ,\forall \left( {x, y}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {f\left( x\right) , f\left( y\right) }\right)  \leq  k\mathrm{\;d}\left( {x, y}\right)
\]

(on dit alors que \( f \) est \( k \) -contractante). Alors \( f \) admet un unique point fixe, i.e. il existe un unique \( x \in E \) tel que \( f\left( x\right) = x \) .

> (we then say that \( f \) is \( k \)-contractive). Then \( f \) admits a unique fixed point, i.e., there exists a unique \( x \in E \) such that \( f\left( x\right) = x \).

Démonstration. Existence. Fixons \( {x}_{0} \in E \) . On définit la suite \( \left( {x}_{n}\right) \) par \( {x}_{n + 1} = f\left( {x}_{n}\right) \) . Une récurrence immédiate donne \( \mathrm{d}\left( {{x}_{n + 1},{x}_{n}}\right) \leq {k}^{n}\mathrm{\;d}\left( {{x}_{1},{x}_{0}}\right) \) pour tout entier naturel \( n \) . Ainsi, lorsque \( p < q \)

> Proof. Existence. Let us fix \( {x}_{0} \in E \). We define the sequence \( \left( {x}_{n}\right) \) by \( {x}_{n + 1} = f\left( {x}_{n}\right) \). An immediate induction gives \( \mathrm{d}\left( {{x}_{n + 1},{x}_{n}}\right) \leq {k}^{n}\mathrm{\;d}\left( {{x}_{1},{x}_{0}}\right) \) for every natural integer \( n \). Thus, when \( p < q \)

\[
\mathrm{d}\left( {{x}_{p},{x}_{q}}\right)  \leq  \mathrm{d}\left( {{x}_{p},{x}_{p + 1}}\right)  + \cdots  + \mathrm{d}\left( {{x}_{q - 1},{x}_{q}}\right)  \leq  \left( {{k}^{p} + \cdots  + {k}^{q - 1}}\right) \mathrm{d}\left( {{x}_{1},{x}_{0}}\right)  \leq  \frac{{k}^{p}}{1 - k}\mathrm{\;d}\left( {{x}_{1},{x}_{0}}\right) ,
\]

ce qui prouve que la suite \( \left( {x}_{n}\right) \) est de Cauchy. Comme \( E \) est complet, \( \left( {x}_{n}\right) \) converge. Notons \( x \) sa limite. Par continuité de \( f \) ( \( f \) est continue car \( k \) -lipschitzienne), on a

> which proves that the sequence \( \left( {x}_{n}\right) \) is Cauchy. Since \( E \) is complete, \( \left( {x}_{n}\right) \) converges. Let \( x \) be its limit. By continuity of \( f \) (\( f \) is continuous because it is \( k \)-Lipschitz), we have

\[
f\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {x}_{n}\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{x}_{n + 1} = x.
\]

Le point \( x \) est donc un point fixe de \( f \) .

> The point \( x \) is therefore a fixed point of \( f \).

Unicité. Supposons \( f\left( x\right) = x \) et \( f\left( y\right) = y \) . Alors

> Uniqueness. Suppose \( f\left( x\right) = x \) and \( f\left( y\right) = y \). Then

\[
0 \leq  \mathrm{d}\left( {x, y}\right)  = \mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right)  \leq  k\mathrm{\;d}\left( {x, y}\right) ,
\]

et comme \( k < 1 \) , ceci n’est possible que si \( \mathrm{d}\left( {x, y}\right) = 0 \) , i. e. \( x = y \) .

> and since \( k < 1 \), this is only possible if \( \mathrm{d}\left( {x, y}\right) = 0 \), i.e., \( x = y \).

Remarque 4. Attention Le théorème est faux si l’on suppose seulement \( \mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right) < \; \mathrm{d}\left( {x, y}\right) \) pour tout \( x \neq y \) . Cependant, dans un compact, une telle condition suffit à montrer l'existence et l'unicité d'un point fixe (voir l'exercice 4 page 34).

> Remark 4. Warning: The theorem is false if we only assume \( \mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right) < \; \mathrm{d}\left( {x, y}\right) \) for all \( x \neq y \). However, in a compact space, such a condition is sufficient to show the existence and uniqueness of a fixed point (see exercise 4 on page 34).

Critère de Cauchy pour les fonctions. à l'aide de la proposition 5, on montre facilement le résultat qui suit.

> Cauchy criterion for functions. Using proposition 5, the following result is easily shown.

Proposition 10. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( \left( {F,\delta }\right) \) un espace métrique complet. Soit une application \( f : D \subset E \rightarrow F \) , soient \( A \subset E \) et \( a \in \bar{A} \) . La fonction \( f \) admet une limite lorsque \( x \) tend vers a selon \( A \) si et seulement si

> Proposition 10. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( \left( {F,\delta }\right) \) a complete metric space. Let \( f : D \subset E \rightarrow F \) be a mapping, let \( A \subset E \) and \( a \in \bar{A} \) be. The function \( f \) has a limit as \( x \) approaches a along \( A \) if and only if

\[
\left( {\forall \varepsilon  > 0,\exists \alpha  > 0,\forall \left( {x, y}\right)  \in  {A}^{2}}\right) ,\;\left( {\mathrm{d}\left( {a, x}\right)  < \alpha \;\text{ et }\;\mathrm{d}\left( {a, y}\right)  < \alpha }\right)  \Rightarrow  \delta \left( {f\left( x\right) , f\left( y\right) }\right)  < \varepsilon .
\]
