#### 4.1. Second-order linear differential equations

*Français : 4.1. Équations différentielles linéaires du second ordre*

Les équations différentielles linéaires du second ordre sont les plus simples des équations différentielles linéaires que l'on ne sache pas en général intégrer. Elles interviennent en outre dans de nombreux problèmes de mécanique et de physique. Il parait donc normal de les étudier plus particulièrement.

> Second-order linear differential equations are the simplest linear differential equations that we generally do not know how to integrate. Furthermore, they appear in numerous problems in mechanics and physics. It therefore seems natural to study them in particular.

On désigne par \( \mathbb{K} \) l’un des corps \( \mathbb{R} \) ou \( \mathbb{C} \) .

> We denote by \( \mathbb{K} \) one of the fields \( \mathbb{R} \) or \( \mathbb{C} \) .

On s'intéresse à l'équation différentielle linéaire homogène

> We are interested in the homogeneous linear differential equation

\[
{y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = 0 \tag{L}
\]

où \( p \) et \( q \) sont deux fonctions continues de \( I \) dans \( \mathbb{K} \) , où \( I \) est un intervalle ouvert de \( \mathbb{R} \) , et où on étudie les solutions à valeurs dans \( \mathbb{K} \) .

> where \( p \) and \( q \) are two continuous functions from \( I \) to \( \mathbb{K} \) , where \( I \) is an open interval of \( \mathbb{R} \) , and where we study solutions with values in \( \mathbb{K} \) .

Rappel. Les équations différentielles du type \( \left( L\right) \) sont un cas particulier d'équations différentielles linéaires homogènes, pour lesquels on a les résultats suivant (voir la partie 2.1 de ce chapitre) :

> Reminder. Differential equations of the type \( \left( L\right) \) are a special case of homogeneous linear differential equations, for which we have the following results (see part 2.1 of this chapter):

- toute solution maximale de \( \left( L\right) \) est définie sur \( I \) tout entier ;

> - every maximal solution of \( \left( L\right) \) is defined on the entire interval \( I \) ;

- l’ensemble \( \mathcal{S} \) des solutions maximales de \( \left( L\right) \) est un \( \mathbb{K} \) -e.v de dimension 2. De plus, pour tout \( {t}_{0} \in  I \) , l’application \( \mathcal{S} \rightarrow  {\mathbb{K}}^{2}\;f \mapsto  \left( {f\left( {t}_{0}\right) ,{f}^{\prime }\left( {t}_{0}\right) }\right) \) est un isomorphisme ; - tous les éléments \( f \in  \mathcal{S} \) sont de classe \( {\mathcal{C}}^{\infty } \) ;

> - the set \( \mathcal{S} \) of maximal solutions of \( \left( L\right) \) is a \( \mathbb{K} \) -vector space of dimension 2. Moreover, for any \( {t}_{0} \in  I \) , the map \( \mathcal{S} \rightarrow  {\mathbb{K}}^{2}\;f \mapsto  \left( {f\left( {t}_{0}\right) ,{f}^{\prime }\left( {t}_{0}\right) }\right) \) is an isomorphism; - all elements \( f \in  \mathcal{S} \) are of class \( {\mathcal{C}}^{\infty } \) ;

Wronskien. Le wronskien d’un couple de solutions maximales \( \left( {u, v}\right) \) de \( \left( L\right) \) , défini par wronskien \( \left( {u, v}\right) = u{v}^{\prime } - {u}^{\prime }v \) vérifie

> Wronskian. The Wronskian of a pair of maximal solutions \( \left( {u, v}\right) \) of \( \left( L\right) \) , defined by Wronskian \( \left( {u, v}\right) = u{v}^{\prime } - {u}^{\prime }v \) satisfies

\[
\forall {t}_{0} \in  I,\forall t \in  I,\;\operatorname{wronskien}\left( {u, v}\right) \left( t\right)  = \operatorname{wronskien}\left( {u, v}\right) \left( {t}_{0}\right) \exp \left( {-{\int }_{{t}_{0}}^{t}p\left( s\right) {ds}}\right)
\]

(voir l'exercice 7 page 388). En particulier, on retrouve le résultat du corollaire 1 page 379. Par ailleurs, si \( p \) est identiquement nulle, le wronskien de \( \left( {u, v}\right) \) est constant.

> (see exercise 7 on page 388). In particular, we recover the result of corollary 1 on page 379. Furthermore, if \( p \) is identically zero, the Wronskian of \( \left( {u, v}\right) \) is constant.

Astuces de calcul. On peut toujours ramener \( \left( L\right) \) au cas où \( p = 0 \) en procédant comme suit. Posons \( y = z \cdot x \) , où \( z \) et \( x \) sont deux fonctions de classe \( {\mathcal{C}}^{2} \) de \( I \) dans \( \mathbb{K} \) encore inconnues. En remplaçant dans \( \left( L\right) \) on obtient :

> Calculation tips. One can always reduce \( \left( L\right) \) to the case where \( p = 0 \) by proceeding as follows. Let \( y = z \cdot x \) , where \( z \) and \( x \) are two functions of class \( {\mathcal{C}}^{2} \) from \( I \) to \( \mathbb{K} \) that are still unknown. Substituting into \( \left( L\right) \) , we obtain:

\[
z{x}^{\prime \prime } + \left( {2{z}^{\prime } + {pz}}\right) {x}^{\prime } + \left( {{z}^{\prime \prime } + p{z}^{\prime } + {qz}}\right) x = 0.
\]

Il suffit donc de choisir \( z \) tel que \( 2{z}^{\prime } + {pz} = 0 \) , et le tour est joué (on doit supposer \( p \) de classe \( {\mathcal{C}}^{1} \) pour que \( z \) soit \( {\mathcal{C}}^{2} \) ).

> It is therefore sufficient to choose \( z \) such that \( 2{z}^{\prime } + {pz} = 0 \) , and the trick is done (we must assume \( p \) is of class \( {\mathcal{C}}^{1} \) for \( z \) to be \( {\mathcal{C}}^{2} \) ).

Si \( p = 0,\left( L\right) \) s’écrit \( {y}^{\prime \prime } + {qy} = 0 \) , et par produit par \( {y}^{\prime } \) on a \( {y}^{\prime \prime }{y}^{\prime } + {qy}{y}^{\prime } = 0 \) , ou encore \( \frac{d}{dt}\left( {y}^{\prime 2}\right) + q\left( t\right) \frac{d}{dt}\left( {y}^{2}\right) = 0 \) . Cette expression peut parfois rendre des services.

> If \( p = 0,\left( L\right) \) is written as \( {y}^{\prime \prime } + {qy} = 0 \) , and by multiplying by \( {y}^{\prime } \) we have \( {y}^{\prime \prime }{y}^{\prime } + {qy}{y}^{\prime } = 0 \) , or also \( \frac{d}{dt}\left( {y}^{\prime 2}\right) + q\left( t\right) \frac{d}{dt}\left( {y}^{2}\right) = 0 \) . This expression can sometimes be useful.

Rappelons enfin que la connaissance de deux solutions indépendantes de \( \left( L\right) \) permet de résoudre \( \left( {L}^{\prime }\right) : {y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = r\left( t\right) \) par la méthode de variation des constantes (voir page 380). Si on ne connaît qu’une seule solution particulière de \( \left( L\right) \) , on peut en trouver une autre indépendante grâce à la méthode d'abaissement de l'ordre exposée à la page 380.

> Finally, recall that knowing two independent solutions of \( \left( L\right) \) allows one to solve \( \left( {L}^{\prime }\right) : {y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = r\left( t\right) \) using the method of variation of constants (see page 380). If only one particular solution of \( \left( L\right) \) is known, another independent one can be found using the reduction of order method presented on page 380.

Exercices.

> Exercises.

EXERCICE 1. On considère l’équation différentielle \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) , où \( q : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) est une fonction continue telle que \( {\int }_{0}^{+\infty }\left| {q\left( t\right) }\right| {dt} \) converge.

> EXERCISE 1. Consider the differential equation \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) , where \( q : {\mathbb{R}}^{ + } \rightarrow \mathbb{R} \) is a continuous function such that \( {\int }_{0}^{+\infty }\left| {q\left( t\right) }\right| {dt} \) converges.

a) Soit \( y \) une solution bornée de \( \left( L\right) \) . Étudier le comportement de \( {y}^{\prime } \) en \( + \infty \) .

> a) Let \( y \) be a bounded solution of \( \left( L\right) \) . Study the behavior of \( {y}^{\prime } \) at \( + \infty \) .

b) Montrer que \( \left( L\right) \) admet des solutions non bornées.

> b) Show that \( \left( L\right) \) admits unbounded solutions.

Solution. a) Comme \( y \) est bornée et que \( {\int }_{0}^{+\infty }\left| {q\left( t\right) }\right| {dt} \) converge, on voit que \( {\int }_{0}^{+\infty }q\left( t\right) y\left( t\right) {dt} = \; - {\int }_{0}^{+\infty }{y}^{\prime \prime }\left( t\right) {dt} \) converge. On en conclut que \( {y}^{\prime } \) converge en \( + \infty \) . Notons \( \alpha = \mathop{\lim }\limits_{{t \rightarrow + \infty }}{y}^{\prime }\left( t\right) \) . Si \( \alpha \neq 0,{y}^{\prime }\left( t\right) \sim \alpha \) en \( + \infty \) , donc lorsque \( x \rightarrow + \infty ,{\int }_{0}^{x}{y}^{\prime }\left( t\right) {dt} \sim {\int }_{0}^{x}{\alpha dt} = {\alpha x} \) , donc \( y\left( x\right) \sim {\alpha x} \) , ce qui absurde car \( y \) est bornée. On en déduit \( \alpha = 0 \) , donc \( {y}^{\prime } \) tend vers 0 en \( + \infty \) .

> Solution. a) Since \( y \) is bounded and \( {\int }_{0}^{+\infty }\left| {q\left( t\right) }\right| {dt} \) converges, we see that \( {\int }_{0}^{+\infty }q\left( t\right) y\left( t\right) {dt} = \; - {\int }_{0}^{+\infty }{y}^{\prime \prime }\left( t\right) {dt} \) converges. We conclude that \( {y}^{\prime } \) converges at \( + \infty \). Let \( \alpha = \mathop{\lim }\limits_{{t \rightarrow + \infty }}{y}^{\prime }\left( t\right) \). If \( \alpha \neq 0,{y}^{\prime }\left( t\right) \sim \alpha \) at \( + \infty \), then as \( x \rightarrow + \infty ,{\int }_{0}^{x}{y}^{\prime }\left( t\right) {dt} \sim {\int }_{0}^{x}{\alpha dt} = {\alpha x} \), thus \( y\left( x\right) \sim {\alpha x} \), which is absurd because \( y \) is bounded. We deduce \( \alpha = 0 \), so \( {y}^{\prime } \) tends to 0 at \( + \infty \).

b) Raisonnons par l'absurde en supposant que \( \left( L\right) \) n'admette que des solutions bornées. Soit \( \left( {u, v}\right) \) une base des solutions de \( \left( L\right) \) . On a vu dans la question précédente que \( {u}^{\prime } \) et \( {v}^{\prime } \) tendent vers 0 en \( + \infty \) , donc wronskien \( \left( {u, v}\right) = u{v}^{\prime } - {u}^{\prime }v \) tend vers 0 en \( + \infty \) . Or la forme de l’équation différentielle \( \left( L\right) \) montre que le wronskien de \( u \) et \( v \) est constant (voir plus haut la sous-partie sur le wronskien), et comme sa limite est nulle, il est identiquement nul. Ceci est absurde car comme \( \left( {u, v}\right) \) est une base des solutions de \( \left( L\right) \) , on a wronskien \( \left( {u, v}\right) \left( t\right) \neq 0 \) pour tout \( t \) .

> b) Let us reason by contradiction by assuming that \( \left( L\right) \) only admits bounded solutions. Let \( \left( {u, v}\right) \) be a basis of solutions for \( \left( L\right) \). We saw in the previous question that \( {u}^{\prime } \) and \( {v}^{\prime } \) tend to 0 at \( + \infty \), so the Wronskian \( \left( {u, v}\right) = u{v}^{\prime } - {u}^{\prime }v \) tends to 0 at \( + \infty \). However, the form of the differential equation \( \left( L\right) \) shows that the Wronskian of \( u \) and \( v \) is constant (see the subsection on the Wronskian above), and since its limit is zero, it is identically zero. This is absurd because since \( \left( {u, v}\right) \) is a basis of solutions for \( \left( L\right) \), we have Wronskian \( \left( {u, v}\right) \left( t\right) \neq 0 \) for all \( t \).

EXERCICE 2. On considère l’équation différentielle \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) , où \( q : \mathbb{R} \rightarrow \mathbb{R} \) est une fonction continue et strictement négative sur \( \mathbb{R} \) .

> EXERCISE 2. Consider the differential equation \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \), where \( q : \mathbb{R} \rightarrow \mathbb{R} \) is a continuous and strictly negative function on \( \mathbb{R} \).

a) Montrer que la seule solution réelle de \( \left( L\right) \) bornée sur \( \mathbb{R} \) est la fonction nulle.

> a) Show that the only real solution of \( \left( L\right) \) bounded on \( \mathbb{R} \) is the zero function.

b) Montrer qu'une solution non nulle s'annule au plus une fois sur \( \mathbb{R} \) .

> b) Show that a non-zero solution vanishes at most once on \( \mathbb{R} \).

Solution. a) Soit \( f \) une solution de \( \left( L\right) \) sur \( \mathbb{R} \) , et posons \( z = {f}^{2} \) . On a

> Solution. a) Let \( f \) be a solution of \( \left( L\right) \) on \( \mathbb{R} \), and let \( z = {f}^{2} \). We have

\[
{z}^{\prime \prime } = {2f}{f}^{\prime \prime } + {f}^{\prime 2} =  - {2q}\left( t\right) {f}^{2} + {f}^{\prime 2} \geq  0,
\]

la fonction \( z \) est donc convexe. Deux cas se présentent.

> the function \( z \) is therefore convex. Two cases arise.

- Si \( z \) est constante, \( f \) est constante donc nulle.

> - If \( z \) is constant, \( f \) is constant and therefore zero.

- Sinon, il existe \( {t}_{0} \in  \mathbb{R} \) tel que \( {z}^{\prime }\left( {t}_{0}\right)  \neq  0 \) . Comme \( z \) est convexe, sa courbe représentative est au dessus de sa tangente en \( {t}_{0} \) , ce qui s’écrit \( z\left( t\right)  \geq  z\left( {t}_{0}\right)  + {z}^{\prime }\left( {t}_{0}\right) \left( {t - {t}_{0}}\right) \) . On en déduit, selon le signe de \( {z}^{\prime }\left( {t}_{0}\right) \) , que \( z \) tend vers \( + \infty \) en \( - \infty \) ou en \( + \infty \) . Donc \( z \) n’est pas bornée sur \( \mathbb{R} \) , donc \( y \) n’est pas bornée sur \( \mathbb{R} \) .

> - Otherwise, there exists \( {t}_{0} \in  \mathbb{R} \) such that \( {z}^{\prime }\left( {t}_{0}\right)  \neq  0 \) . Since \( z \) is convex, its representative curve lies above its tangent at \( {t}_{0} \) , which is written as \( z\left( t\right)  \geq  z\left( {t}_{0}\right)  + {z}^{\prime }\left( {t}_{0}\right) \left( {t - {t}_{0}}\right) \) . We deduce, depending on the sign of \( {z}^{\prime }\left( {t}_{0}\right) \) , that \( z \) tends to \( + \infty \) at \( - \infty \) or at \( + \infty \) . Thus \( z \) is not bounded on \( \mathbb{R} \) , so \( y \) is not bounded on \( \mathbb{R} \) .

b) Avec les notations précédentes, si \( y \) s’annule en deux points \( {t}_{1} \) et \( {t}_{2}\left( {{t}_{1} < {t}_{2}}\right) \) , alors \( z = {y}^{2} \) aussi. Comme \( z \) est convexe et positive, ceci entraîne \( z\left( t\right) = 0 \) sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) , donc \( y\left( t\right) = 0 \) sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) , donc d’après le théorème de Cauchy-Lipschitz, \( y \) est nulle sur \( \mathbb{R} \) tout entier. Ainsi, une solution \( y \) qui s’annule en deux points est identiquement nulle.

> b) With the previous notations, if \( y \) vanishes at two points \( {t}_{1} \) and \( {t}_{2}\left( {{t}_{1} < {t}_{2}}\right) \) , then \( z = {y}^{2} \) does as well. Since \( z \) is convex and positive, this implies \( z\left( t\right) = 0 \) on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) , therefore \( y\left( t\right) = 0 \) on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) , so according to the Cauchy-Lipschitz theorem, \( y \) is zero on the entire \( \mathbb{R} \) . Thus, a solution \( y \) that vanishes at two points is identically zero.

- EXERCICE 3 (THÉORÉMES D'OSCILLATION ET DE COMPARAISON). 1/ On considère l’équation différentielle \( \left( L\right)  : {y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = 0 \) , où \( p \) et \( q \) sont deux fonctions réelles continues sur un intervalle \( I \) de \( \mathbb{R} \) .

> - EXERCISE 3 (OSCILLATION AND COMPARISON THEOREMS). 1/ Consider the differential equation \( \left( L\right)  : {y}^{\prime \prime } + p\left( t\right) {y}^{\prime } + q\left( t\right) y = 0 \) , where \( p \) and \( q \) are two real functions continuous on an interval \( I \) of \( \mathbb{R} \) .

a) Montrer qu’une solution non nulle \( f \) de \( \left( L\right) \) n’a qu’un nombre fini de zéros dans tout segment de \( I \) .

> a) Show that a non-zero solution \( f \) of \( \left( L\right) \) has only a finite number of zeros in any segment of \( I \) .

b) Soient \( f, g \) deux fonctions qui forment une base des solutions de \( \left( L\right) \) . Soient \( {t}_{1} \) et \( {t}_{2} \; \left( {{t}_{1} < {t}_{2}}\right) \) deux zéros consécutifs de \( f \) . Montrer qu’il existe un unique point \( {t}_{0} \in \rbrack {t}_{1},{t}_{2}\left\lbrack \text{ tel }\right\rbrack \) que \( g\left( {t}_{0}\right) = 0 \) .

> b) Let \( f, g \) be two functions that form a basis of solutions for \( \left( L\right) \) . Let \( {t}_{1} \) and \( {t}_{2} \; \left( {{t}_{1} < {t}_{2}}\right) \) be two consecutive zeros of \( f \) . Show that there exists a unique point \( {t}_{0} \in \rbrack {t}_{1},{t}_{2}\left\lbrack \text{ tel }\right\rbrack \) such that \( g\left( {t}_{0}\right) = 0 \) .

2 / a) Soient \( I \) un intervalle de \( \mathbb{R} \) , et \( r, s : I \rightarrow \mathbb{R} \) deux fonctions continues telles que \( r \leq s \) sur \( I \) . Soit \( x \) une solution non nulle de \( \left( {L}_{1}\right) : {x}^{\prime \prime } + r\left( t\right) x = 0, y \) une solution non nulle de \( \left( {L}_{2}\right) : {y}^{\prime \prime } + s\left( t\right) y = 0 \) . Soient \( {t}_{1} \) et \( {t}_{2}\left( {{t}_{1} < {t}_{2}}\right) \) deux zéros consécutifs de \( x \) . Montrer que si \( x \) et \( y \) ne sont pas proportionnelles sur \( \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) , il existe \( \left. {{t}_{0} \in }\right\rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) tel que \( y\left( {t}_{0}\right) = 0 \) .

> 2 / a) Let \( I \) be an interval of \( \mathbb{R} \), and \( r, s : I \rightarrow \mathbb{R} \) be two continuous functions such that \( r \leq s \) on \( I \). Let \( x \) be a non-zero solution of \( \left( {L}_{1}\right) : {x}^{\prime \prime } + r\left( t\right) x = 0, y \) and \( \left( {L}_{2}\right) : {y}^{\prime \prime } + s\left( t\right) y = 0 \) be a non-zero solution of \( \left( {L}_{2}\right) : {y}^{\prime \prime } + s\left( t\right) y = 0 \). Let \( {t}_{1} \) and \( {t}_{2}\left( {{t}_{1} < {t}_{2}}\right) \) be two consecutive zeros of \( x \). Show that if \( x \) and \( y \) are not proportional on \( \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \), there exists \( \left. {{t}_{0} \in }\right\rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) such that \( y\left( {t}_{0}\right) = 0 \).

b) Si \( q \) est une fonction continue sur \( I \) qui vérifie \( q\left( t\right) \leq {\mu }^{2} \) pour tout \( t \) (avec \( \mu > \) 0), montrer que deux zéros consécutifs \( {t}_{1} \) et \( {t}_{2}\left( {{t}_{1} < {t}_{2}}\right) \) d’une solution non nulle de \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) vérifient \( {t}_{2} - {t}_{1} \geq \pi /\mu . \)

> b) If \( q \) is a continuous function on \( I \) that satisfies \( q\left( t\right) \leq {\mu }^{2} \) for all \( t \) (with \( \mu > \) 0), show that two consecutive zeros \( {t}_{1} \) and \( {t}_{2}\left( {{t}_{1} < {t}_{2}}\right) \) of a non-zero solution of \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) satisfy \( {t}_{2} - {t}_{1} \geq \pi /\mu . \)

c) Si \( q \) est une fonction continue sur \( I \) qui vérifie \( q\left( t\right) \geq {\lambda }^{2} \) pour tout \( t \) (avec \( \lambda > 0 \) ), montrer que toute solution de \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) s’annule au moins une fois dans tout intervalle fermé de longueur \( \pi /\lambda \) .

> c) If \( q \) is a continuous function on \( I \) that satisfies \( q\left( t\right) \geq {\lambda }^{2} \) for all \( t \) (with \( \lambda > 0 \)), show that any solution of \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) vanishes at least once in any closed interval of length \( \pi /\lambda \).

---

Solution. 1/ a) On sait déjà (voir l’exercice 2 page 376), que les zéros de \( f \) sont isolés.

> Solution. 1/ a) We already know (see exercise 2 on page 376) that the zeros of \( f \) are isolated.

Supposons que \( f \) ait une infinité de zéros dans un segment \( \left\lbrack {a, b}\right\rbrack \subset I \) . Comme \( \left\lbrack {a, b}\right\rbrack \) est compact, il existe un élément \( x \in \left\lbrack {a, b}\right\rbrack \) qui est un point d’accumulation des zéros de \( f \) . Par continuité de \( f \) , on a \( f\left( x\right) = 0 \) , autrement dit \( x \) est un zéro de \( f \) . Ceci est absurde car \( x \) est un point d’accumulation des zéros de \( f \) et les zéros de \( f \) sont isolés.

> Suppose that \( f \) has an infinite number of zeros in a segment \( \left\lbrack {a, b}\right\rbrack \subset I \). Since \( \left\lbrack {a, b}\right\rbrack \) is compact, there exists an element \( x \in \left\lbrack {a, b}\right\rbrack \) which is an accumulation point of the zeros of \( f \). By continuity of \( f \), we have \( f\left( x\right) = 0 \), in other words \( x \) is a zero of \( f \). This is absurd because \( x \) is an accumulation point of the zeros of \( f \) and the zeros of \( f \) are isolated.

b) La fonction \( f \) ne s’annule pas sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) . Quitte à changer \( f \) en \( - f \) , on peut donc supposer \( f > 0 \) sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) . Comme \( f\left( {t}_{1}\right) = 0 \) , on a

> b) The function \( f \) does not vanish on \( \rbrack {t}_{1},{t}_{2}\lbrack \). By replacing \( f \) with \( - f \) if necessary, we can assume \( f > 0 \) on \( \rbrack {t}_{1},{t}_{2}\lbrack \). Since \( f\left( {t}_{1}\right) = 0 \), we have

\[
{f}^{\prime }\left( {t}_{1}\right)  = \mathop{\lim }\limits_{\substack{{t \rightarrow  {t}_{1}} \\  {t > {t}_{1}} }}\frac{f\left( t\right)  - f\left( {t}_{1}\right) }{t - {t}_{1}} = \mathop{\lim }\limits_{\substack{{t \rightarrow  {t}_{1}} \\  {t > {t}_{1}} }}\frac{f\left( t\right) }{t - {t}_{1}} \geq  0,
\]

et comme \( {f}^{\prime }\left( {t}_{1}\right) \neq 0 \) (sinon \( f \) serait la fonction nulle d’après le théorème de Cauchy-Lipschitz), on a \( {f}^{\prime }\left( {t}_{1}\right) > 0 \) . On montrerait de même \( {f}^{\prime }\left( {t}_{2}\right) < 0 \) .

> and since \( {f}^{\prime }\left( {t}_{1}\right) \neq 0 \) (otherwise \( f \) would be the zero function according to the Cauchy-Lipschitz theorem), we have \( {f}^{\prime }\left( {t}_{1}\right) > 0 \) . We would show \( {f}^{\prime }\left( {t}_{2}\right) < 0 \) in the same way.

Ceci étant, posons \( W = f{g}^{\prime } - {f}^{\prime }g = \) wronskien \( \left( {f, g}\right) \) . Comme \( \left( {f, g}\right) \) est une base de solutions de \( \left( L\right) , W \) ne s’annule pas, donc garde un signe constant sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) . Quitte à changer \( g \) en \( - g \) , on peut même supposer \( W > 0 \) sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) . On a \( W\left( {t}_{1}\right) = - {f}^{\prime }\left( {t}_{1}\right) g\left( {t}_{1}\right) > 0 \) , donc \( g\left( {t}_{1}\right) < 0 \) , et de même,à partir de \( W\left( {t}_{2}\right) = - {f}^{\prime }\left( {t}_{2}\right) g\left( {t}_{2}\right) > 0 \) , on obtient \( g\left( {t}_{2}\right) > 0 \) . Comme \( g \) est continue, le théorème des valeurs intermédiaires nous assure donc l’existence de \( {t}_{0} \in \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) tel que \( g\left( {t}_{0}\right) = 0 \) .

> Given this, let us define \( W = f{g}^{\prime } - {f}^{\prime }g = \) Wronskian \( \left( {f, g}\right) \) . Since \( \left( {f, g}\right) \) is a basis of solutions of \( \left( L\right) , W \) it does not vanish, and therefore maintains a constant sign on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) . By potentially changing \( g \) to \( - g \) , we can even assume \( W > 0 \) on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) . We have \( W\left( {t}_{1}\right) = - {f}^{\prime }\left( {t}_{1}\right) g\left( {t}_{1}\right) > 0 \) , therefore \( g\left( {t}_{1}\right) < 0 \) , and similarly, starting from \( W\left( {t}_{2}\right) = - {f}^{\prime }\left( {t}_{2}\right) g\left( {t}_{2}\right) > 0 \) , we obtain \( g\left( {t}_{2}\right) > 0 \) . Since \( g \) is continuous, the intermediate value theorem ensures the existence of \( {t}_{0} \in \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) such that \( g\left( {t}_{0}\right) = 0 \) .

Il nous reste à montrer que \( g \) ne s’annule qu’une fois dans \( \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) . Supposons que outre le point \( {t}_{0}, g \) s’annule en un autre point \( {t}_{0}^{\prime } \) de \( \rbrack {t}_{1},{t}_{2}\lbrack \) . En appliquant à \( f \) ce que l’on vient de montrer pour \( g \) , on en déduit que \( f \) s’annule entre \( {t}_{0} \) et \( {t}_{0}^{\prime } \) , ce qui absurde car \( {t}_{1} \) et \( {t}_{2} \) sont deux zéros consécutifs de \( f \) . D’où l’unicité de \( {t}_{0} \in \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) tel que \( g\left( {t}_{0}\right) = 0 \) .

> It remains for us to show that \( g \) vanishes only once in \( \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) . Suppose that besides the point \( {t}_{0}, g \) it vanishes at another point \( {t}_{0}^{\prime } \) in \( \rbrack {t}_{1},{t}_{2}\lbrack \) . By applying to \( f \) what we have just shown for \( g \) , we deduce that \( f \) vanishes between \( {t}_{0} \) and \( {t}_{0}^{\prime } \) , which is absurd because \( {t}_{1} \) and \( {t}_{2} \) are two consecutive zeros of \( f \) . Hence the uniqueness of \( {t}_{0} \in \rbrack {t}_{1},{t}_{2}\left\lbrack \right. \) such that \( g\left( {t}_{0}\right) = 0 \) .

2 / a) Supposons que \( y \) ne s’annule pas sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) . Par hypothèse, \( x \) ne s’annule pas sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) , et quitte à changer \( x \) en \( - x \) et \( y \) en \( - y \) , on peut supposer que \( x \) et \( y \) prennent des valeurs \( > 0 \) sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) . On généralise maintenant la méthode utilisée dans la question précédente. On pose \( W\left( t\right) = x{y}^{\prime } - {x}^{\prime }y \) . Comme précédemment, on a \( {x}^{\prime }\left( {t}_{1}\right) > 0 \) et \( {x}^{\prime }\left( {t}_{2}\right) < 0 \) . Comme \( x\left( {t}_{1}\right) = x\left( {t}_{2}\right) = 0 \) , on a donc \( W\left( {t}_{1}\right) \leq 0 \) et \( W\left( {t}_{2}\right) \geq 0 \) .

> 2 / a) Suppose that \( y \) does not vanish on \( \rbrack {t}_{1},{t}_{2}\lbrack \). By hypothesis, \( x \) does not vanish on \( \rbrack {t}_{1},{t}_{2}\lbrack \), and by replacing \( x \) with \( - x \) and \( y \) with \( - y \) if necessary, we can assume that \( x \) and \( y \) take \( > 0 \) values on \( \rbrack {t}_{1},{t}_{2}\lbrack \). We now generalize the method used in the previous question. Let \( W\left( t\right) = x{y}^{\prime } - {x}^{\prime }y \). As before, we have \( {x}^{\prime }\left( {t}_{1}\right) > 0 \) and \( {x}^{\prime }\left( {t}_{2}\right) < 0 \). Since \( x\left( {t}_{1}\right) = x\left( {t}_{2}\right) = 0 \), we therefore have \( W\left( {t}_{1}\right) \leq 0 \) and \( W\left( {t}_{2}\right) \geq 0 \).

Par ailleurs, \( {W}^{\prime } = x{y}^{\prime \prime } - {x}^{\prime \prime }y = x\left( {-s\left( t\right) y}\right) - y\left( {-r\left( t\right) x}\right) = {xy}\left( {r\left( t\right) - s\left( t\right) }\right) \leq 0 \) sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) , donc \( W \) décroît de \( W\left( {t}_{1}\right) \leq 0 \) à \( W\left( {t}_{2}\right) \geq 0 \) . Autrement dit, \( W \) est nulle sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) . On en conclut que \( {x}^{\prime }/x = {y}^{\prime }/y \) sur \( \rbrack {t}_{1},{t}_{2}\left\lbrack {\text{ , donc }x\text{ et }y\text{ sont proportionnelles sur }\rbrack {t}_{1},{t}_{2}\lbrack }\right. \) . D’où le résultat.

> Furthermore, \( {W}^{\prime } = x{y}^{\prime \prime } - {x}^{\prime \prime }y = x\left( {-s\left( t\right) y}\right) - y\left( {-r\left( t\right) x}\right) = {xy}\left( {r\left( t\right) - s\left( t\right) }\right) \leq 0 \) on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \), so \( W \) decreases from \( W\left( {t}_{1}\right) \leq 0 \) to \( W\left( {t}_{2}\right) \geq 0 \). In other words, \( W \) is zero on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \). We conclude that \( {x}^{\prime }/x = {y}^{\prime }/y \) on \( \rbrack {t}_{1},{t}_{2}\left\lbrack {\text{ , donc }x\text{ et }y\text{ sont proportionnelles sur }\rbrack {t}_{1},{t}_{2}\lbrack }\right. \). Hence the result.

b) Soit \( f \) une solution non nulle de \( \left( L\right) \) et \( {t}_{1},{t}_{2} \) deux zéros consécutifs de \( f \) . Supposons \( {t}_{2} - {t}_{1} < \; \pi /\mu \) . Alors il existe \( \varphi \in \mathbb{R} \) telle que la fonction \( g : t \mapsto \sin \left( {{\mu t} + \varphi }\right) \) , ne s’annule pas sur \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) . Une telle fonction ne peut pas être proportionnelle à \( f \) car \( f\left( {t}_{1}\right) = f\left( {t}_{2}\right) = 0 \) . Comme \( g \) est solution de l’équation différentielle \( {y}^{\prime \prime } + {\mu }^{2}y = 0 \) , le résultat de la question précédente nous dit que \( g \) s’annule au moins une fois sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) , ce qui est absurde. On a donc bien \( {t}_{2} - {t}_{1} \geq \pi /\mu \) .

> b) Let \( f \) be a non-zero solution of \( \left( L\right) \) and \( {t}_{1},{t}_{2} \) be two consecutive zeros of \( f \). Suppose \( {t}_{2} - {t}_{1} < \; \pi /\mu \). Then there exists \( \varphi \in \mathbb{R} \) such that the function \( g : t \mapsto \sin \left( {{\mu t} + \varphi }\right) \) does not vanish on \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \). Such a function cannot be proportional to \( f \) because \( f\left( {t}_{1}\right) = f\left( {t}_{2}\right) = 0 \). Since \( g \) is a solution to the differential equation \( {y}^{\prime \prime } + {\mu }^{2}y = 0 \), the result of the previous question tells us that \( g \) vanishes at least once on \( \rbrack {t}_{1},{t}_{2}\lbrack \), which is absurd. We therefore have \( {t}_{2} - {t}_{1} \geq \pi /\mu \).

c) Soit \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) un segment de longueur \( \pi /\lambda \) . On peut trouver \( \varphi \in \mathbb{R} \) tel que la fonction \( g : t \mapsto \; \sin \left( {{\lambda t} + \varphi }\right) \) s’annule aux points \( {t}_{1} \) et \( {t}_{2} \) . La fonction \( g \) est solution de l’équation différentielle \( {y}^{\prime \prime } + {\lambda }^{2}y = 0 \) . Si \( f \) et \( g \) sont proportionnelles, alors \( f \) s’annule en \( {t}_{1} \) et \( {t}_{2} \) . Sinon d’après \( 2/\mathrm{a} \) ), \( f \) doit s’annuler au moins une fois sur \( \rbrack {t}_{1},{t}_{2}\lbrack \) . Ainsi \( f \) s’annule toujours au moins une fois sur le segment \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) .

> c) Let \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \) be a segment of length \( \pi /\lambda \). We can find \( \varphi \in \mathbb{R} \) such that the function \( g : t \mapsto \; \sin \left( {{\lambda t} + \varphi }\right) \) vanishes at points \( {t}_{1} \) and \( {t}_{2} \). The function \( g \) is a solution to the differential equation \( {y}^{\prime \prime } + {\lambda }^{2}y = 0 \). If \( f \) and \( g \) are proportional, then \( f \) vanishes at \( {t}_{1} \) and \( {t}_{2} \). Otherwise, according to \( 2/\mathrm{a} \)), \( f \) must vanish at least once on \( \rbrack {t}_{1},{t}_{2}\lbrack \). Thus, \( f \) always vanishes at least once on the segment \( \left\lbrack {{t}_{1},{t}_{2}}\right\rbrack \).

---

EXERCICE 4. On considère l’équation différentielle \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \) , où \( q : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) est une fonction continue. On suppose que \( \left( L\right) \) possède une solution \( y \) nulle en \( a \) et \( b \) et \( > 0 \) sur \( \rbrack a, b\lbrack \) . Montrer

> EXERCISE 4. Consider the differential equation \( \left( L\right) : {y}^{\prime \prime } + q\left( t\right) y = 0 \), where \( q : \left\lbrack {a, b}\right\rbrack \rightarrow \mathbb{R} \) is a continuous function. Suppose that \( \left( L\right) \) has a solution \( y \) that is zero at \( a \) and \( b \) and \( > 0 \) on \( \rbrack a, b\lbrack \). Show that

\[
{\int }_{a}^{b}\left| {q\left( t\right) }\right| {dt} > \frac{4}{b - a}.
\]

Solution. La fonction \( y \) est continue sur \( \left\lbrack {a, b}\right\rbrack \) , donc il existe \( c \in \left\lbrack {a, b}\right\rbrack \) tel que \( y\left( c\right) = \mathop{\sup }\limits_{{t \in \left\lbrack {a, b}\right\rbrack }}y\left( t\right) \) . Comme de plus \( y\left( a\right) = y\left( b\right) = 0 \) et que \( y > 0 \) sur \( \rbrack a, b\left\lbrack {\text{ , on a }c \in }\right\rbrack a, b\lbrack \) . On écrit maintenant, pour tout \( \alpha ,\beta \) tels que \( a < \alpha < \beta < b \) ,

> Solution. The function \( y \) is continuous on \( \left\lbrack {a, b}\right\rbrack \), so there exists \( c \in \left\lbrack {a, b}\right\rbrack \) such that \( y\left( c\right) = \mathop{\sup }\limits_{{t \in \left\lbrack {a, b}\right\rbrack }}y\left( t\right) \). Since, moreover, \( y\left( a\right) = y\left( b\right) = 0 \) and \( y > 0 \) on \( \rbrack a, b\left\lbrack {\text{ , on a }c \in }\right\rbrack a, b\lbrack \). We now write, for all \( \alpha ,\beta \) such that \( a < \alpha < \beta < b \),

\[
{\int }_{a}^{b}\left| {q\left( t\right) }\right| {dt} = {\int }_{a}^{b}\left| \frac{{y}^{\prime \prime }\left( t\right) }{y\left( t\right) }\right| {dt} > \frac{1}{y\left( c\right) }{\int }_{a}^{b}\left| {{y}^{\prime \prime }\left( t\right) }\right| {dt} \geq  \frac{1}{y\left( c\right) }\left| {{y}^{\prime }\left( \beta \right)  - {y}^{\prime }\left( \alpha \right) }\right| .
\]

Or, d’après le théorème des accroissements finis, on peut trouver \( \alpha \in \rbrack a, c\left\lbrack {\text{ et }\beta \in }\right\rbrack c, b\lbrack \) tels que

> However, according to the mean value theorem, we can find \( \alpha \in \rbrack a, c\left\lbrack {\text{ et }\beta \in }\right\rbrack c, b\lbrack \) such that

\[
\frac{y\left( c\right)  - y\left( a\right) }{c - a} = {y}^{\prime }\left( \alpha \right) \;\text{ et }\;\frac{y\left( b\right)  - y\left( c\right) }{c - b} = {y}^{\prime }\left( \beta \right) .
\]

On en conclut

> We conclude that

\[
{\int }_{a}^{b}\left| {q\left( t\right) }\right| {dt} > \frac{1}{y\left( c\right) }\left| {{y}^{\prime }\left( \beta \right)  - {y}^{\prime }\left( \alpha \right) }\right|  = \frac{1}{y\left( c\right) }\left| {\frac{y\left( c\right)  - y\left( a\right) }{c - a} - \frac{y\left( b\right)  - y\left( c\right) }{b - c}}\right|  = \frac{1}{c - a} + \frac{1}{b - c}
\]

(car \( y\left( a\right) = y\left( b\right) = 0 \) ). Une rapide étude de la fonction \( c \mapsto \frac{1}{c - a} + \frac{1}{b - c} \) montre qu’elle atteint son minimum pour \( c = \left( {a + b}\right) /2 \) , point en laquelle elle vaut \( 4/\left( {b - a}\right) \) . Donc finalement

> (because \( y\left( a\right) = y\left( b\right) = 0 \)). A quick study of the function \( c \mapsto \frac{1}{c - a} + \frac{1}{b - c} \) shows that it reaches its minimum at \( c = \left( {a + b}\right) /2 \), a point where it equals \( 4/\left( {b - a}\right) \). So finally

\[
{\int }_{a}^{b}\left| {q\left( t\right) }\right| {dt} > \frac{1}{c - a} + \frac{1}{b - c} \geq  \frac{4}{b - a},
\]

d'où le résultat.

> hence the result.
