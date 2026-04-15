#### 1.1. Definitions

Une équation différentielle est une équation portant sur les dérivées d'une fonction. Plus précisément :

> A differential equation is an equation involving the derivatives of a function. More precisely:

DéFINITION 1. Soit \( n \in {\mathbb{N}}^{ * } \) et \( E \) un espace de Banach. Soit une application \( F : \Omega \subset \; \mathbb{R} \times {E}^{n} \rightarrow E \) (où \( \Omega \) est un ouvert de \( \mathbb{R} \times {E}^{n} \) ). On appelle solution de l’équation différentielle d'ordre n

> DEFINITION 1. Let \( n \in {\mathbb{N}}^{ * } \) and \( E \) be a Banach space. Let \( F : \Omega \subset \; \mathbb{R} \times {E}^{n} \rightarrow E \) be a mapping (where \( \Omega \) is an open set of \( \mathbb{R} \times {E}^{n} \) ). A solution to the n-th order differential equation is called

\[
{y}^{\left( n\right) } = F\left( {t, y,{y}^{\prime },\ldots ,{y}^{\left( n - 1\right) }}\right)
\]

(*)

> toute application \( \varphi : I \rightarrow E \) (où \( I \) est un intervalle de \( \mathbb{R} \) ), \( n \) fois dérivable et vérifiant

any mapping \( \varphi : I \rightarrow E \) (where \( I \) is an interval of \( \mathbb{R} \) ), \( n \) times differentiable and satisfying

> (i) pour tout \( t \in I,\;\left( {t,\varphi \left( t\right) ,\ldots ,{\varphi }^{\left( n - 1\right) }\left( t\right) }\right) \in \Omega \) ;

(i) for all \( t \in I,\;\left( {t,\varphi \left( t\right) ,\ldots ,{\varphi }^{\left( n - 1\right) }\left( t\right) }\right) \in \Omega \) ;

> (ii) pour tout \( t \in I,\;F\left( {t,\varphi \left( t\right) ,\ldots ,{\varphi }^{\left( n - 1\right) }\left( t\right) }\right) = {\varphi }^{\left( n\right) }\left( t\right) \) .

(ii) for all \( t \in I,\;F\left( {t,\varphi \left( t\right) ,\ldots ,{\varphi }^{\left( n - 1\right) }\left( t\right) }\right) = {\varphi }^{\left( n\right) }\left( t\right) \) .

> Dans la suite de cette partie, nous utiliserons les notations de cette définition.

In the remainder of this section, we will use the notation from this definition.

> Toute équation différentielle peut se ramener à une équation différentielle d'ordre 1. Avec les notations de la définition précédente, si on définit les applications

Any differential equation can be reduced to a first-order differential equation. With the notation from the previous definition, if we define the mappings

\[
\Phi  : I \rightarrow  {E}^{n}\;t \mapsto  \left( {\varphi \left( t\right) ,\ldots ,{\varphi }^{\left( n - 1\right) }\left( t\right) }\right)
\]

\[
G : \Omega  \subset  \mathbb{R} \times  {E}^{n} \rightarrow  {E}^{n}\;\left( {t, y}\right)  = \left( {t,{x}_{0},{x}_{1},\ldots ,{x}_{n - 1}}\right)  \mapsto  \left( {{x}_{1},\ldots ,{x}_{n - 1}, F\left( {t, y}\right) }\right) ,
\]

il est équivalent de dire que \( \varphi \) est solution de (*) ou que \( \Phi \) est solution de \( {\Phi }^{\prime } = G\left( {t,\Phi }\right) \) . On peut donc se limiter à étudier les équations différentielles du premier ordre.

> it is equivalent to say that \( \varphi \) is a solution of (*) or that \( \Phi \) is a solution of \( {\Phi }^{\prime } = G\left( {t,\Phi }\right) \) . We can therefore limit ourselves to studying first-order differential equations.

Remarque 1. Nous n'avons considéré ici que les équations différentielles dites résolues, i. e. celles qui se mettent sous la forme \( {y}^{\left( n\right) } = F\left( {t, y,\ldots ,{y}^{\left( n - 1\right) }}\right) \) . De manière plus générale, on peut étudier les équations différentielles non résolues d'ordre \( n \) qui sont du type \( F\left( {t, y,\ldots ,{y}^{\left( n - 1\right) },{y}^{\left( n\right) }}\right) = 0 \) . Ces dernières peuvent également se ramener à des équations différentielles non résolues du premier ordre \( G\left( {t, Y,{Y}^{\prime }}\right) = 0 \) (en utilisant les mêmes techniques).

> Remark 1. We have only considered here so-called resolved differential equations, i.e., those that can be written in the form \( {y}^{\left( n\right) } = F\left( {t, y,\ldots ,{y}^{\left( n - 1\right) }}\right) \) . More generally, one can study unresolved differential equations of order \( n \) which are of the type \( F\left( {t, y,\ldots ,{y}^{\left( n - 1\right) },{y}^{\left( n\right) }}\right) = 0 \) . The latter can also be reduced to unresolved first-order differential equations \( G\left( {t, Y,{Y}^{\prime }}\right) = 0 \) (using the same techniques).

##### Maximal solution.

*Français : Solution maximale.*

DéFINITION 2. Une fonction \( \varphi : I \rightarrow E \) (où \( I \) est un intervalle de \( \mathbb{R} \) ) est dite solution maximale de l’équation différentielle \( {y}^{\left( n\right) } = F\left( {t, y,\ldots ,{y}^{\left( n - 1\right) }}\right) \) s’il n’existe pas d’autre solution \( \psi : J \rightarrow E \) de cette équation différentielle telle que \( I \subset J, I \neq J \) et \( \psi = \varphi \) sur \( I \) , où \( J \) est un intervalle de \( \mathbb{R} \) .

> DEFINITION 2. A function \( \varphi : I \rightarrow E \) (where \( I \) is an interval of \( \mathbb{R} \) ) is called a maximal solution of the differential equation \( {y}^{\left( n\right) } = F\left( {t, y,\ldots ,{y}^{\left( n - 1\right) }}\right) \) if there exists no other solution \( \psi : J \rightarrow E \) of this differential equation such that \( I \subset J, I \neq J \) and \( \psi = \varphi \) on \( I \) , where \( J \) is an interval of \( \mathbb{R} \) .
