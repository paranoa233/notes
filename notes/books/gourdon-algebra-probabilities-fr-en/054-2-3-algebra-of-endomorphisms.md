#### 2.3. Algebra of endomorphisms

*Français : 2.3. Algèbre des endomorphismes*

Les endomorphismes sont des applications linéaires très importantes. Ils vérifient de nombreuses propriétés et c'est pour cela qu'on les étudie plus particulièrement. Dans toute la suite de cette section, \( E \) désigne un \( \mathbb{K} \) -e.v.

> Endomorphisms are very important linear maps. They satisfy numerous properties, which is why we study them more specifically. Throughout the rest of this section, \( E \) denotes a \( \mathbb{K} \) -v.s.

On note \( \mathcal{L}\left( E\right) = \mathcal{L}\left( {E, E}\right) \) . Muni de la loi \( \circ \) de composition, \( \mathcal{L}\left( E\right) \) est une \( \mathbb{K} \) -algèbre unitaire. On note \( \mathcal{G}\ell \left( E\right) \) l’ensemble des endomorphismes bijectifs (encore appelés auto-morphismes) de \( E \) . Muni de la loi o de composition, \( \mathcal{G}\ell \left( E\right) \) est un groupe appelé groupe linéaire de \( E \) .

> We denote \( \mathcal{L}\left( E\right) = \mathcal{L}\left( {E, E}\right) \) . Equipped with the composition law \( \circ \) , \( \mathcal{L}\left( E\right) \) is a unital \( \mathbb{K} \) -algebra. We denote \( \mathcal{G}\ell \left( E\right) \) the set of bijective endomorphisms (also called automorphisms) of \( E \) . Equipped with the composition law o, \( \mathcal{G}\ell \left( E\right) \) is a group called the general linear group of \( E \) .

DÉFINITION 6. On dit que \( f \in \mathcal{L}\left( E\right) \) est une homothétie de rapport \( \lambda \in \mathbb{K} \) si \( f = \lambda {\operatorname{Id}}_{E} \) (où \( {\mathrm{{Id}}}_{E} \) désigne l’application identité de \( E \) ).

> DEFINITION 6. \( f \in \mathcal{L}\left( E\right) \) is said to be a homothety of ratio \( \lambda \in \mathbb{K} \) if \( f = \lambda {\operatorname{Id}}_{E} \) (where \( {\mathrm{{Id}}}_{E} \) denotes the identity map of \( E \) ).

Remarque 3. L'ensemble des homothéties de rapport non nul forme un sous-groupe de \( \mathcal{G}\ell \left( E\right) \) . On montre à l’exercice 6 page 124 que c’est le centre du groupe \( \mathcal{G}\ell \left( E\right) \) .

> Remark 3. The set of homotheties with non-zero ratio forms a subgroup of \( \mathcal{G}\ell \left( E\right) \) . It is shown in exercise 6 on page 124 that this is the center of the group \( \mathcal{G}\ell \left( E\right) \) .

Proposition 3. Soit \( f \in \mathcal{L}\left( E\right) \) . Alors \( f \) est une homothétie si et seulement si pour tout \( x \in E \) , la famille \( \left( {x, f\left( x\right) }\right) \) est liée.

> Proposition 3. Let \( f \in \mathcal{L}\left( E\right) \) . Then \( f \) is a homothety if and only if for all \( x \in E \) , the family \( \left( {x, f\left( x\right) }\right) \) is linearly dependent.

Démonstration. Condition nécessaire. C'est immédiat.

> Proof. Necessary condition. This is immediate.

Condition suffisante. Par hypothèse, pour tout \( x \in E \) , il existe \( {\lambda }_{x} \in \mathbb{K} \) tel que \( f\left( x\right) = {\lambda }_{x} \cdot x \) . Fixons \( {x}_{0} \in E,{x}_{0} \neq 0 \) . Nous allons montrer que pour tout \( x \in E\left( {x \neq 0}\right) ,{\lambda }_{x} = {\lambda }_{{x}_{0}} \) .

> Sufficient condition. By hypothesis, for all \( x \in E \) , there exists \( {\lambda }_{x} \in \mathbb{K} \) such that \( f\left( x\right) = {\lambda }_{x} \cdot x \) . Let us fix \( {x}_{0} \in E,{x}_{0} \neq 0 \) . We will show that for all \( x \in E\left( {x \neq 0}\right) ,{\lambda }_{x} = {\lambda }_{{x}_{0}} \) .

- Si \( x \in  \mathbb{K}{x}_{0} \) et \( x \neq  0 \) , alors il existe \( \mu  \in  \mathbb{K} \) tel que \( x = \mu {x}_{0} \) . Donc \( {\lambda }_{x}x = f\left( x\right)  = {\mu f}\left( {x}_{0}\right)  = \; \mu {\lambda }_{{x}_{0}}{x}_{0} = {\lambda }_{{x}_{0}}\left( {\mu {x}_{0}}\right)  = {\lambda }_{{x}_{0}}x \) . On en conclut \( {\lambda }_{x} = {\lambda }_{{x}_{0}} \) .

> - If \( x \in  \mathbb{K}{x}_{0} \) and \( x \neq  0 \) , then there exists \( \mu  \in  \mathbb{K} \) such that \( x = \mu {x}_{0} \) . Thus \( {\lambda }_{x}x = f\left( x\right)  = {\mu f}\left( {x}_{0}\right)  = \; \mu {\lambda }_{{x}_{0}}{x}_{0} = {\lambda }_{{x}_{0}}\left( {\mu {x}_{0}}\right)  = {\lambda }_{{x}_{0}}x \) . We conclude \( {\lambda }_{x} = {\lambda }_{{x}_{0}} \) .

- Sinon \( x \) et \( {x}_{0} \) forment une famille libre, et on a alors

> - Otherwise, \( x \) and \( {x}_{0} \) form a linearly independent family, and we then have

\[
{\lambda }_{x + {x}_{0}}\left( {x + {x}_{0}}\right)  = f\left( {x + {x}_{0}}\right)  = f\left( x\right)  + f\left( {x}_{0}\right)  = {\lambda }_{x}x + {\lambda }_{{x}_{0}}{x}_{0},
\]

donc comme \( \left( {x,{x}_{0}}\right) \) est libre, \( {\lambda }_{{x}_{0} + x} = {\lambda }_{{x}_{0}} = {\lambda }_{x} \) , d’où le résultat.

> therefore, since \( \left( {x,{x}_{0}}\right) \) is linearly independent, \( {\lambda }_{{x}_{0} + x} = {\lambda }_{{x}_{0}} = {\lambda }_{x} \) , hence the result.

##### Projectors and symmetries.

*Français : Projecteurs et symétries.*

DéFINITION 7. Soient \( {E}_{1} \) et \( {E}_{2} \) deux s.e.v de \( E \) tels que \( {E}_{1} \oplus {E}_{2} = E \) , de sorte que

> DEFINITION 7. Let \( {E}_{1} \) and \( {E}_{2} \) be two subspaces of \( E \) such that \( {E}_{1} \oplus {E}_{2} = E \) , so that

\[
\forall x \in  E,\exists !\left( {{x}_{1},{x}_{2}}\right)  \in  {E}_{1} \times  {E}_{2}\;\text{ tel que }\;x = {x}_{1} + {x}_{2}.
\]

L’application \( p : E \rightarrow E\;x \mapsto {x}_{1} \) est linéaire et s’appelle projection sur \( {E}_{1} \) parallèlement à \( {E}_{2} \) . On a Ker \( p = {E}_{2},\operatorname{Im}p = {E}_{1} \) et \( p \circ p = p \) .

> The map \( p : E \rightarrow E\;x \mapsto {x}_{1} \) is linear and is called the projection onto \( {E}_{1} \) parallel to \( {E}_{2} \) . We have Ker \( p = {E}_{2},\operatorname{Im}p = {E}_{1} \) and \( p \circ p = p \) .

DéFINITION 8. Un endomorphisme \( p \in \mathcal{L}\left( E\right) \) est appelé projecteur si \( p \circ p = p \) .

> DEFINITION 8. An endomorphism \( p \in \mathcal{L}\left( E\right) \) is called a projector if \( p \circ p = p \) .

PROPOSITION 4. Soit \( p \in \mathcal{L}\left( E\right) \) . Alors \( p \) est un projecteur si et seulement si \( p \) est la projection sur Imp parallèlement à Ker \( p \) . On a alors \( E = \operatorname{Ker}p \oplus \operatorname{Im}p \) .

> PROPOSITION 4. Let \( p \in \mathcal{L}\left( E\right) \) . Then \( p \) is a projector if and only if \( p \) is the projection onto Imp parallel to Ker \( p \) . We then have \( E = \operatorname{Ker}p \oplus \operatorname{Im}p \) .

Remarque 4. Si \( p \) est un projecteur, alors \( y \in \operatorname{Im}p \) si et seulement si \( y = p\left( y\right) \) .

> Remark 4. If \( p \) is a projector, then \( y \in \operatorname{Im}p \) if and only if \( y = p\left( y\right) \) .

Définition 9. Soient \( {E}_{1} \) et \( {E}_{2} \) deux s.e.v de \( E \) tels que \( E = {E}_{1} \oplus {E}_{2} \) , de sorte que

> Definition 9. Let \( {E}_{1} \) and \( {E}_{2} \) be two subspaces of \( E \) such that \( E = {E}_{1} \oplus {E}_{2} \) , so that

\[
\forall x \in  E,\exists !\left( {{x}_{1},{x}_{2}}\right)  \in  {E}_{1} \times  {E}_{2}\;\text{ tel que }\;x = {x}_{1} + {x}_{2}.
\]

L’application \( s : E \rightarrow E\;x \mapsto {x}_{1} - {x}_{2} \) s’appelle symétrie par rapport à \( {E}_{1} \) parallèlement à \( {E}_{2} \) . On a \( s \in \mathcal{L}\left( E\right) \) et si \( p \) est la projection sur \( {E}_{1} \) parallèlement à \( {E}_{2}, s = {2p} - {\operatorname{Id}}_{E} \) .

> The map \( s : E \rightarrow E\;x \mapsto {x}_{1} - {x}_{2} \) is called a symmetry with respect to \( {E}_{1} \) parallel to \( {E}_{2} \). We have \( s \in \mathcal{L}\left( E\right) \) and if \( p \) is the projection onto \( {E}_{1} \) parallel to \( {E}_{2}, s = {2p} - {\operatorname{Id}}_{E} \).

PROPOSITION 5. Supposons que la caractéristique du corps \( \mathbb{K} \) soit différente de 2. Alors \( s \in \mathcal{L}\left( E\right) \) est une symétrie si et seulement si \( s \circ s = {\operatorname{Id}}_{E} \) . Si \( p = \frac{1}{2}\left( {s + {\operatorname{Id}}_{E}}\right) \) , p est un projecteur et \( s \) est la symétrie par rapport à \( \operatorname{Im}p \) parallèlement à \( \operatorname{Ker}p \) .

> PROPOSITION 5. Suppose the characteristic of the field \( \mathbb{K} \) is not 2. Then \( s \in \mathcal{L}\left( E\right) \) is a symmetry if and only if \( s \circ s = {\operatorname{Id}}_{E} \). If \( p = \frac{1}{2}\left( {s + {\operatorname{Id}}_{E}}\right) \), p is a projector and \( s \) is the symmetry with respect to \( \operatorname{Im}p \) parallel to \( \operatorname{Ker}p \).

Remarque 5. Si \( \mathbb{K} \) est de caractéristique 2, on peut avoir \( {s}^{2} = {\operatorname{Id}}_{E} \) sans que \( s \) soit une symétrie (prendre par exemple \( s \) telle que \( \left\lbrack s\right\rbrack = \left( \begin{array}{ll} 1 & 1 \\ 0 & 1 \end{array}\right) \in {\mathcal{M}}_{2}\left( {\mathbb{Z}/2\mathbb{Z}}\right) \) ).

> Remark 5. If \( \mathbb{K} \) has characteristic 2, we can have \( {s}^{2} = {\operatorname{Id}}_{E} \) without \( s \) being a symmetry (take for example \( s \) such that \( \left\lbrack s\right\rbrack = \left( \begin{array}{ll} 1 & 1 \\ 0 & 1 \end{array}\right) \in {\mathcal{M}}_{2}\left( {\mathbb{Z}/2\mathbb{Z}}\right) \)).
