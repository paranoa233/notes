#### 1.1. Differential

*Français : 1.1. Différentielle*

La théorie des fonctions de la variable réelle s'est considérablement développée avec l’introduction de la notion de dérivée. L’expression \( f\left( {x + h}\right) = f\left( x\right) + h{f}^{\prime }\left( x\right) + o\left( h\right) \) s’interprète en disant qu’au voisinage de \( x, f \) est approchée par la fonction affine \( f\left( x\right) + \; h{f}^{\prime }\left( x\right) \) : on a linéarisé \( f \) . De la même manière, il est naturel de chercher à linéariser une fonction \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{p} \) , en étudiant l’existence d’une fonction linéaire \( \varphi : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{p} \) telle que \( f\left( {x + h}\right) = f\left( x\right) + \varphi \left( h\right) \) à \( o\left( h\right) \) près. Ceci motive la définition suivante.

> The theory of functions of a real variable developed considerably with the introduction of the concept of the derivative. The expression \( f\left( {x + h}\right) = f\left( x\right) + h{f}^{\prime }\left( x\right) + o\left( h\right) \) is interpreted by saying that in the neighborhood of \( x, f \) is approximated by the affine function \( f\left( x\right) + \; h{f}^{\prime }\left( x\right) \) : we have linearized \( f \) . In the same way, it is natural to seek to linearize a function \( f : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{p} \) , by studying the existence of a linear function \( \varphi : {\mathbb{R}}^{n} \rightarrow {\mathbb{R}}^{p} \) such that \( f\left( {x + h}\right) = f\left( x\right) + \varphi \left( h\right) \) to within \( o\left( h\right) \) . This motivates the following definition.

DéFINITION 1. Soient \( E \) et \( F \) deux \( \mathbb{R} \) -e.v.n, \( U \) un ouvert de \( E \) et \( a \in U \) . Une application \( f : U \rightarrow F \) est dite différentiable en a s’il existe \( \varphi \in {\mathcal{L}}_{c}\left( {E, F}\right) \) (e.v des applications linéaires et continues de \( E \) dans \( F \) ) telle que

> DEFINITION 1. Let \( E \) and \( F \) be two \( \mathbb{R} \) -n.v.s., \( U \) an open set of \( E \) and \( a \in U \) . A mapping \( f : U \rightarrow F \) is said to be differentiable at a if there exists \( \varphi \in {\mathcal{L}}_{c}\left( {E, F}\right) \) (v.s. of continuous linear mappings from \( E \) to \( F \) ) such that

\[
f\left( {a + h}\right)  = f\left( a\right)  + \varphi \left( h\right)  + o\left( {\parallel h\parallel }\right) \;\text{ lorsque }\;h \rightarrow  0.
\]

Si \( \varphi \) existe, \( \varphi \) est unique et s’appelle la différentielle de \( f \) en a. On la note \( d{f}_{a} \) .

> If \( \varphi \) exists, \( \varphi \) is unique and is called the differential of \( f \) at a. It is denoted by \( d{f}_{a} \) .

Si \( f \) est différentiable en tout point de \( U \) , on dit que \( f \) est différentiable sur \( U \) et l’application \( {df} : U \mapsto {\mathcal{L}}_{c}\left( {E, F}\right) \;a \mapsto d{f}_{a} \) est appelée application différentielle de \( f \) . Si \( {df} \) est continue, on dit que \( f \) est de classe \( {\mathcal{C}}^{1} \) .

> If \( f \) is differentiable at every point of \( U \) , we say that \( f \) is differentiable on \( U \) and the mapping \( {df} : U \mapsto {\mathcal{L}}_{c}\left( {E, F}\right) \;a \mapsto d{f}_{a} \) is called the differential mapping of \( f \) . If \( {df} \) is continuous, we say that \( f \) is of class \( {\mathcal{C}}^{1} \) .

Remarque 1. - Une application de la variable réelle \( f \) est dérivable en \( a \) si et seule-ment si elle est différentiable en \( a \) , et on a \( d{f}_{a} : h \mapsto {f}^{\prime }\left( a\right) h \) . Pour cette raison, on trouve parfois la notation \( {f}^{\prime }\left( a\right) \) pour désigner la différentielle de \( f \) en \( a \) .

> Remark 1. - A mapping of the real variable \( f \) is differentiable at \( a \) if and only if it is differentiable at \( a \), and we have \( d{f}_{a} : h \mapsto {f}^{\prime }\left( a\right) h \). For this reason, one sometimes finds the notation \( {f}^{\prime }\left( a\right) \) to denote the differential of \( f \) at \( a \).

- En dimension quelconque, \( d{f}_{a} \) dépend a priori des normes \( \parallel .{\parallel }_{E} \) et \( \parallel .{\parallel }_{F} \) choisies sur \( E \) et \( F \) . Cependant, en dimension finie, les normes sont toutes équivalentes et on montre facilement que l’existence et la valeur de \( d{f}_{a} \) ne dépend pas des normes choisies.

> - In any dimension, \( d{f}_{a} \) depends a priori on the norms \( \parallel .{\parallel }_{E} \) and \( \parallel .{\parallel }_{F} \) chosen on \( E \) and \( F \). However, in finite dimension, all norms are equivalent and it is easily shown that the existence and value of \( d{f}_{a} \) do not depend on the chosen norms.

- Noter qu'une différentielle \( d{f}_{a} \) doit être continue. En dimension finie, toutes les fonctions linéaires sont continues et le problème de la continuité de la différentielle ne se pose donc pas.

> - Note that a differential \( d{f}_{a} \) must be continuous. In finite dimension, all linear functions are continuous and the problem of the continuity of the differential therefore does not arise.

- Enfin, si \( f \) est linéaire et continue, l’égalité \( f\left( {a + h}\right)  = f\left( a\right)  + f\left( h\right) \) montre que \( f \) est différentiable sur \( E \) et que \( d{f}_{a} = f \) pour tout \( a \in  E \) .

> - Finally, if \( f \) is linear and continuous, the equality \( f\left( {a + h}\right)  = f\left( a\right)  + f\left( h\right) \) shows that \( f \) is differentiable on \( E \) and that \( d{f}_{a} = f \) for all \( a \in  E \).

Exemple 1. Soit \( f : {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {X, Y}\right) \mapsto {XY} \) . Donnons nous une norme d’algèbre \( \parallel .\parallel \) sur \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) et considérons un point \( \left( {{X}_{0},{Y}_{0}}\right) \in {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \) . On a

> Example 1. Let \( f : {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {X, Y}\right) \mapsto {XY} \). Let us provide an algebra norm \( \parallel .\parallel \) on \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) and consider a point \( \left( {{X}_{0},{Y}_{0}}\right) \in {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \). We have

\[
\forall \left( {H, K}\right)  \in  {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2},\;f\left( {{X}_{0} + H,{Y}_{0} + K}\right)  = f\left( {{X}_{0},{Y}_{0}}\right)  + \left( {H{Y}_{0} + {X}_{0}K}\right)  + {HK}.
\]

(*)

> Si on munit \( {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \) de la norme produit \( \parallel \left( {H, K}\right) {\parallel }_{1} = \sup \{ \parallel H\parallel ,\parallel K\parallel \} \) , on a \( \parallel {HK}\parallel \leq \; \parallel H\parallel \cdot \parallel K\parallel \leq {\begin{Vmatrix}\left( H, K\right) \end{Vmatrix}}_{1}^{2} \) donc (*) entraîne \( f\left( {{X}_{0} + H,{Y}_{0} + K}\right) = f\left( {{X}_{0},{Y}_{0}}\right) + \varphi \left( {H, K}\right) + \; o\left( {\parallel \left( {H, K}\right) {\parallel }_{1}}\right) \) , où \( \varphi : {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {H, K}\right) \mapsto H{Y}_{0} + {X}_{0}K \) (attention à la non-commutativité des matrices) est linéaire. Comme de plus \( \varphi \) est continue (on est en dimension finie), ceci montre que \( f \) est différentiable en \( \left( {{X}_{0},{Y}_{0}}\right) \) et que \( d{f}_{\left( {X}_{0},{Y}_{0}\right) } = \varphi \) .

If we equip \( {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \) with the product norm \( \parallel \left( {H, K}\right) {\parallel }_{1} = \sup \{ \parallel H\parallel ,\parallel K\parallel \} \), we have \( \parallel {HK}\parallel \leq \; \parallel H\parallel \cdot \parallel K\parallel \leq {\begin{Vmatrix}\left( H, K\right) \end{Vmatrix}}_{1}^{2} \) so (*) leads to \( f\left( {{X}_{0} + H,{Y}_{0} + K}\right) = f\left( {{X}_{0},{Y}_{0}}\right) + \varphi \left( {H, K}\right) + \; o\left( {\parallel \left( {H, K}\right) {\parallel }_{1}}\right) \), where \( \varphi : {\mathcal{M}}_{n}{\left( \mathbb{R}\right) }^{2} \rightarrow {\mathcal{M}}_{n}\left( \mathbb{R}\right) \;\left( {H, K}\right) \mapsto H{Y}_{0} + {X}_{0}K \) (beware of the non-commutativity of matrices) is linear. Since, moreover, \( \varphi \) is continuous (we are in finite dimension), this shows that \( f \) is differentiable at \( \left( {{X}_{0},{Y}_{0}}\right) \) and that \( d{f}_{\left( {X}_{0},{Y}_{0}\right) } = \varphi \).

> PROPOSITION 1. Une fonction différentiable en un point est continue en ce point.

PROPOSITION 1. A function differentiable at a point is continuous at that point.

> Gradient.

Gradient.

> DéFINITION 2. Soient \( E \) un espace euclidien et \( f : U \subset E \rightarrow \mathbb{R} \) une application différentiable en \( a \in U \) (où \( U \) est un ouvert de \( E \) ). Alors \( d{f}_{a} \in \mathcal{L}\left( {E,\mathbb{R}}\right) = {E}^{ * } \) et il existe un unique vecteur \( v \) de \( E \) tel que \( d{f}_{a}\left( h\right) = v \cdot h \) pour tout \( h \in E \) . Le vecteur \( v \) s’appelle le gradient de \( f \) en \( a \) et est noté grad \( {}_{a}f \) .

DEFINITION 2. Let \( E \) be a Euclidean space and \( f : U \subset E \rightarrow \mathbb{R} \) a mapping differentiable at \( a \in U \) (where \( U \) is an open subset of \( E \)). Then \( d{f}_{a} \in \mathcal{L}\left( {E,\mathbb{R}}\right) = {E}^{ * } \) and there exists a unique vector \( v \) in \( E \) such that \( d{f}_{a}\left( h\right) = v \cdot h \) for all \( h \in E \). The vector \( v \) is called the gradient of \( f \) at \( a \) and is denoted by grad \( {}_{a}f \).

> Remarque 2. On peut également définir la notion de gradient lorsque \( E \) est un espace hilbertien réel, car la propriété d’existence et d’unicité d’un vecteur \( v \) de \( E \) tel que \( d{f}_{a}\left( h\right) = \; v \cdot h \) pour tout \( h \in E \) reste vraie (voir le théorème de Représentation de Riesz, question 3/ du problème 1 page 427).

Remark 2. One can also define the notion of gradient when \( E \) is a real Hilbert space, because the property of existence and uniqueness of a vector \( v \) in \( E \) such that \( d{f}_{a}\left( h\right) = \; v \cdot h \) for all \( h \in E \) remains true (see the Riesz Representation theorem, question 3/ of problem 1 on page 427).

##### Properties of differentials.

*Français : Propriétés des différentielles.*

Proposition 2. Soient \( E \) et \( F \) deux e.v.n et \( f, g \) deux applications de \( U \) dans \( F \) , où \( U \) est un ouvert de \( E \) , toutes deux différentiables en \( a \in U \) . Alors

> Proposition 2. Let \( E \) and \( F \) be two n.v.s. and \( f, g \) be two mappings from \( U \) to \( F \), where \( U \) is an open subset of \( E \), both differentiable at \( a \in U \). Then

- \( f + g \) est différentiable en a et \( d{\left( f + g\right) }_{a} = d{f}_{a} + d{g}_{a} \) ;

> - \( f + g \) is differentiable at a and \( d{\left( f + g\right) }_{a} = d{f}_{a} + d{g}_{a} \) ;

- pour tout \( \lambda  \in  \mathbb{R},{\lambda f} \) est différentiable en a et \( d{\left( \lambda f\right) }_{a} = {\lambda d}{f}_{a} \) .

> - for all \( \lambda  \in  \mathbb{R},{\lambda f} \) is differentiable at a and \( d{\left( \lambda f\right) }_{a} = {\lambda d}{f}_{a} \) .

\( \rightarrow \) Proposition 3. Soient \( E, F, G \) des \( \mathbb{R} \) -e.v.n, \( U \subset E \) et \( V \subset F \) deux ouverts, et deux applications \( f : U \subset E \rightarrow F, g : V \subset F \rightarrow G \) vérifiant \( f\left( U\right) \subset V \) . Si \( f \) est différentiable en \( a \in U \) et \( g \) différentiable en \( f\left( a\right) \) , alors \( g \circ f : U \rightarrow G \) est différentiable en a et on a

> \( \rightarrow \) Proposition 3. Let \( E, F, G \) be \( \mathbb{R} \)-n.v.s., \( U \subset E \) and \( V \subset F \) two open sets, and two mappings \( f : U \subset E \rightarrow F, g : V \subset F \rightarrow G \) satisfying \( f\left( U\right) \subset V \). If \( f \) is differentiable at \( a \in U \) and \( g \) is differentiable at \( f\left( a\right) \), then \( g \circ f : U \rightarrow G \) is differentiable at a and we have

\[
d{\left( g \circ  f\right) }_{a} = d{g}_{f\left( a\right) } \circ  d{f}_{a}.
\]

Remarque 3. - Si \( E = \mathbb{R} \) , cette formule s’écrit aussi \( {\left( g \circ f\right) }^{\prime }\left( a\right) = d{g}_{f\left( a\right) }\left( {{f}^{\prime }\left( a\right) }\right) \) .

> Remark 3. - If \( E = \mathbb{R} \), this formula is also written \( {\left( g \circ f\right) }^{\prime }\left( a\right) = d{g}_{f\left( a\right) }\left( {{f}^{\prime }\left( a\right) }\right) \).

- Si \( f \) et \( g : U \subset  E \rightarrow  \mathbb{R} \) sont différentiables en \( a \) , alors le produit \( {fg} \) l’est aussi et \( d{\left( fg\right) }_{a} = d{f}_{a}g + {fd}{g}_{a} \) (appliquer la proposition précédente en remarquant que \( {fg} \) est la composée des applications \( \varphi  : U \rightarrow  {\mathbb{R}}^{2}\;x \mapsto  \left( {f\left( x\right) , g\left( x\right) }\right) \) et \( \psi  : {\mathbb{R}}^{2} \rightarrow \; \mathbb{R}\;\left( {x, y}\right)  \mapsto  {xy}) \) . Ce résultat reste d’ailleurs valable en remplaçant \( \mathbb{R} \) par \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \) , ou plus généralement par toute algèbre normée.

> - If \( f \) and \( g : U \subset  E \rightarrow  \mathbb{R} \) are differentiable at \( a \), then the product \( {fg} \) is also differentiable and \( d{\left( fg\right) }_{a} = d{f}_{a}g + {fd}{g}_{a} \) (apply the previous proposition by noting that \( {fg} \) is the composition of the mappings \( \varphi  : U \rightarrow  {\mathbb{R}}^{2}\;x \mapsto  \left( {f\left( x\right) , g\left( x\right) }\right) \) and \( \psi  : {\mathbb{R}}^{2} \rightarrow \; \mathbb{R}\;\left( {x, y}\right)  \mapsto  {xy}) \). This result remains valid by replacing \( \mathbb{R} \) with \( {\mathcal{M}}_{n}\left( \mathbb{R}\right) \), or more generally with any normed algebra.
