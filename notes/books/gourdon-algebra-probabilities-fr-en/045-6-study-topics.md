### 6. Study topics

*Français : 6. Sujets d'étude*

SUJET D’ÉTUDE 1. Soit \( p \) un nombre premier. On note \( {\mathbb{F}}_{p} = \mathbb{Z}/p\mathbb{Z} \) .

> STUDY TOPIC 1. Let \( p \) be a prime number. We denote \( {\mathbb{F}}_{p} = \mathbb{Z}/p\mathbb{Z} \) .

1 / Soit \( \mathbb{K} \) un corps commutatif contenant \( {\mathbb{F}}_{p} \) . Montrer que pour tout \( R \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) et pour tout \( x \in \mathbb{K} \) , on a pour tout \( n \in \mathbb{N} \) la relation \( R\left( {x}^{{p}^{n}}\right) = {\left( R\left( x\right) \right) }^{{p}^{n}} \) .

> 1 / Let \( \mathbb{K} \) be a commutative field containing \( {\mathbb{F}}_{p} \) . Show that for all \( R \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) and for all \( x \in \mathbb{K} \) , we have for all \( n \in \mathbb{N} \) the relation \( R\left( {x}^{{p}^{n}}\right) = {\left( R\left( x\right) \right) }^{{p}^{n}} \) .

2/a) Soit \( Q \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) , irréductible dans \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) , de degré \( d \) . Soit \( n \in {\mathbb{N}}^{ * } \) . Montrer que \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \) si et seulement si \( d \mid n \) .

> 2/a) Let \( Q \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) be irreducible in \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) , of degree \( d \) . Let \( n \in {\mathbb{N}}^{ * } \) . Show that \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \) if and only if \( d \mid n \) .

b) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {K}_{p}^{n} \) l’ensemble des polynômes unitaires irréductibles de \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) , de degré \( n \) . Montrer que

> b) For all \( n \in {\mathbb{N}}^{ * } \) , let \( {K}_{p}^{n} \) denote the set of monic irreducible polynomials of \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) , of degree \( n \) . Show that

\[
{X}^{{p}^{n}} - X = \mathop{\prod }\limits_{{d \mid  n}}\left( {\mathop{\prod }\limits_{{Q \in  {K}_{p}^{d}}}Q}\right) .
\]

3/a) Pour tout \( n \in {\mathbb{N}}^{ * } \) , on note \( {I}_{p}^{n} = \operatorname{Card}\left( {K}_{p}^{n}\right) \) . Montrer que \( {p}^{n} = \mathop{\sum }\limits_{{d \mid n}}d{I}_{p}^{d} \) .

> 3/a) For all \( n \in {\mathbb{N}}^{ * } \) , let \( {I}_{p}^{n} = \operatorname{Card}\left( {K}_{p}^{n}\right) \) . Show that \( {p}^{n} = \mathop{\sum }\limits_{{d \mid n}}d{I}_{p}^{d} \) .

b) Montrer que pour tout \( n \in {\mathbb{N}}^{ * },{I}_{p}^{n} \neq 0 \) .

> b) Show that for all \( n \in {\mathbb{N}}^{ * },{I}_{p}^{n} \neq 0 \) .

4/ Une application aux corps finis (on rappelle que tout corps fini est commutatif, voir le problème 11 page 100).

> 4/ An application to finite fields (recall that every finite field is commutative, see problem 11 page 100).

a) Soit \( \mathbb{K} \) un corps fini. Montrer qu’il existe un nombre premier \( p \) et un entier \( n \in {\mathbb{N}}^{ * } \) tels que \( \operatorname{Card}\left( \mathbb{K}\right) = {p}^{n} \) . Réciproquement, si \( p \) est un nombre premier et si \( n \in {\mathbb{N}}^{ * } \) , montrer qu’il existe un corps fini \( \mathbb{K} \) de cardinal \( {p}^{n} \) .

> a) Let \( \mathbb{K} \) be a finite field. Show that there exists a prime number \( p \) and an integer \( n \in {\mathbb{N}}^{ * } \) such that \( \operatorname{Card}\left( \mathbb{K}\right) = {p}^{n} \) . Conversely, if \( p \) is a prime number and if \( n \in {\mathbb{N}}^{ * } \) , show that there exists a finite field \( \mathbb{K} \) of cardinality \( {p}^{n} \) .

b) Soit \( \mathbb{K} \) un surcorps de \( {\mathbb{F}}_{p} \) tel que \( \operatorname{Card}\left( \mathbb{K}\right) = {p}^{n} \) avec \( n \in {\mathbb{N}}^{ * } \) . Soit \( P \in {K}_{p}^{n} \) . Montrer qu’il existe \( x \in \mathbb{K} \) tel que \( P\left( x\right) = 0 \) .

> b) Let \( \mathbb{K} \) be an extension field of \( {\mathbb{F}}_{p} \) such that \( \operatorname{Card}\left( \mathbb{K}\right) = {p}^{n} \) with \( n \in {\mathbb{N}}^{ * } \) . Let \( P \in {K}_{p}^{n} \) . Show that there exists \( x \in \mathbb{K} \) such that \( P\left( x\right) = 0 \) .

c) En déduire que deux corps finis de même cardinal sont isomorphes.

> c) Deduce that two finite fields of the same cardinality are isomorphic.

Solution. 1 / Le corps \( \mathbb{K} \) contenant \( {\mathbb{F}}_{p} \) , il est de caractéristique \( p \) . On peut donc écrire

> Solution. 1 / The field \( \mathbb{K} \) containing \( {\mathbb{F}}_{p} \) , it is of characteristic \( p \) . We can therefore write

\[
\forall x, y \in  \mathbb{K},\;{\left( x + y\right) }^{p} = {x}^{p} + {y}^{p} + \mathop{\sum }\limits_{{k = 1}}^{{p - 1}}\left( \begin{array}{l} p \\  k \end{array}\right) {x}^{k}{y}^{p - k} = {x}^{p} + {y}^{p}
\]

car si \( 1 \leq k \leq p - 1, p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) .

> because if \( 1 \leq k \leq p - 1, p \mid \left( \begin{array}{l} p \\ k \end{array}\right) \) .

En procédant par récurrence sur \( n \) , on en déduit que pour tout \( n \in \mathbb{N},{\left( x + y\right) }^{{p}^{n}} = {x}^{{p}^{n}} + {y}^{{p}^{n}} \) , puis par récurrence sur \( k \) , on montre que pour tout \( \left( {{x}_{1},\ldots ,{x}_{k}}\right) \in {\mathbb{K}}^{k} \) , pour tout \( n \in \mathbb{N} \) ,

> By proceeding by induction on \( n \), we deduce that for all \( n \in \mathbb{N},{\left( x + y\right) }^{{p}^{n}} = {x}^{{p}^{n}} + {y}^{{p}^{n}} \), then by induction on \( k \), we show that for all \( \left( {{x}_{1},\ldots ,{x}_{k}}\right) \in {\mathbb{K}}^{k} \), for all \( n \in \mathbb{N} \),

\[
{\left( {x}_{1} + \cdots  + {x}_{k}\right) }^{{p}^{n}} = {x}_{1}^{{p}^{n}} + \cdots  + {x}_{k}^{{p}^{n}}.
\]

Par ailleurs, pour tout \( a \in {\mathbb{F}}_{p},{a}^{p} = a \) donc (par récurrence), pour tout \( n \in \mathbb{N},{a}^{{p}^{n}} = a \) .

> Furthermore, for all \( a \in {\mathbb{F}}_{p},{a}^{p} = a \) therefore (by induction), for all \( n \in \mathbb{N},{a}^{{p}^{n}} = a \).

Ceci étant, soit \( R = {a}_{0} + {a}_{1}X + \cdots + {a}_{d}{X}^{d} \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) . Pour tout \( x \in \mathbb{K} \) ,, on a

> That being said, let \( R = {a}_{0} + {a}_{1}X + \cdots + {a}_{d}{X}^{d} \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \). For all \( x \in \mathbb{K} \), we have

\[
R{\left( x\right) }^{{p}^{n}} = {\left( \mathop{\sum }\limits_{{i = 0}}^{d}{a}_{i}{x}^{i}\right) }^{{p}^{n}} = \mathop{\sum }\limits_{{i = 0}}^{d}{a}_{i}^{{p}^{n}}{\left( {x}^{i}\right) }^{{p}^{n}} = \mathop{\sum }\limits_{{i = 0}}^{d}{a}_{i}{\left( {x}^{{p}^{n}}\right) }^{i} = R\left( {x}^{{p}^{n}}\right) .
\]

2/a) Le polynôme \( Q \) étant irréductible dans \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack ,\mathbb{K} = {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( Q\right) \) est un corps ; \( \mathbb{K} \) est d’ailleurs un \( {\mathbb{F}}_{p} \) -espace vectoriel de dimension \( d \) , donc isomorphe (comme \( {\mathbb{F}}_{p} \) -espace vectoriel) à \( {\mathbb{F}}_{p}^{d} \) , d’où \( \operatorname{Card}\left( \mathbb{K}\right) = \operatorname{Card}\left( {\mathbb{F}}_{p}^{d}\right) = {p}^{d} \) . Le groupe multiplicatif \( {\mathbb{K}}^{ * } \) est donc d’ordre \( {p}^{d} - 1 \) , et donc pour tout \( y \in {\mathbb{K}}^{ * },{y}^{{p}^{d} - 1} = 1 \) , ce qui entraîne que pour tout \( y \in \mathbb{K},{y}^{{p}^{d}} = y \) , et par récurrence sur \( k \) :

> 2/a) The polynomial \( Q \) being irreducible in \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack ,\mathbb{K} = {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( Q\right) \) is a field; \( \mathbb{K} \) is moreover a \( {\mathbb{F}}_{p} \)-vector space of dimension \( d \), thus isomorphic (as a \( {\mathbb{F}}_{p} \)-vector space) to \( {\mathbb{F}}_{p}^{d} \), hence \( \operatorname{Card}\left( \mathbb{K}\right) = \operatorname{Card}\left( {\mathbb{F}}_{p}^{d}\right) = {p}^{d} \). The multiplicative group \( {\mathbb{K}}^{ * } \) is therefore of order \( {p}^{d} - 1 \), and thus for all \( y \in {\mathbb{K}}^{ * },{y}^{{p}^{d} - 1} = 1 \), which implies that for all \( y \in \mathbb{K},{y}^{{p}^{d}} = y \), and by induction on \( k \):

\[
\forall y \in  \mathbb{K},\forall k \in  \mathbb{N},\;{y}^{{p}^{kd}} = y.
\]

(*)

> Ceci étant, montrons l'équivalence demandée.

That being said, let us show the requested equivalence.

> Condition suffisante. Supposons \( d \mid n \) . En notant \( \bar{X} \) la classe de \( X \) dans le corps \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( Q\right) = \mathbb{K} \) , on a d’après \( \left( *\right) ,{\bar{X}}^{{p}^{kd}} = \bar{X} \) pour tout \( k \in \mathbb{N} \) . Comme \( d \mid n \) , on en déduit \( {\bar{X}}^{{p}^{n}} = \bar{X} \) , c’est-à-dire \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \) .

Sufficient condition. Suppose \( d \mid n \). By denoting \( \bar{X} \) the class of \( X \) in the field \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( Q\right) = \mathbb{K} \), we have according to \( \left( *\right) ,{\bar{X}}^{{p}^{kd}} = \bar{X} \) for all \( k \in \mathbb{N} \). As \( d \mid n \), we deduce \( {\bar{X}}^{{p}^{n}} = \bar{X} \), that is to say \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \).

> Condition nécessaire. Supposons \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \) , c’est-à-dire \( {\bar{X}}^{{p}^{n}} = \bar{X} \) . Soit \( y \in \mathbb{K} \) . Il existe \( R \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) tel que \( y = R\left( \bar{X}\right) \) , donc \( {y}^{{p}^{n}} = R{\left( \bar{X}\right) }^{{p}^{n}} = R\left( {\bar{X}}^{{p}^{n}}\right) = R\left( \bar{X}\right) = y\;\left( {* * }\right) \) . Effectuons maintenant la division euclidienne de \( n \) par \( d : n = {qd} + r,0 \leq r \leq d - 1 \) . La relation \( \left( {* * }\right) \) s’écrit \( {\left( {y}^{{p}^{qd}}\right) }^{{p}^{r}} = y \) , et d’après \( \left( *\right) \) , on a \( {y}^{{p}^{r}} = y \) . On a donc \( {y}^{{p}^{r} - 1} = 1 \) pour tout \( y \in {\mathbb{K}}^{ * } \) . Or \( {\mathbb{K}}^{ * } \) , sous groupe multiplicatif fini d’un corps commutatif, est cyclique (voir la remarque de l’exercice 10 page 28). On peut donc choisir \( y \in {\mathbb{K}}^{ * } \) d’ordre \( {p}^{d} - 1 \) . Or on a vu que \( {y}^{{p}^{r} - 1} = 1 \) . comme \( 0 \leq r < d \) , ceci entraíne \( r = 0 \) , c’est-à-dire \( d \mid n \) .

Necessary condition. Suppose \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \) , that is to say \( {\bar{X}}^{{p}^{n}} = \bar{X} \) . Let \( y \in \mathbb{K} \) . There exists \( R \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) such that \( y = R\left( \bar{X}\right) \) , therefore \( {y}^{{p}^{n}} = R{\left( \bar{X}\right) }^{{p}^{n}} = R\left( {\bar{X}}^{{p}^{n}}\right) = R\left( \bar{X}\right) = y\;\left( {* * }\right) \) . Now let us perform the Euclidean division of \( n \) by \( d : n = {qd} + r,0 \leq r \leq d - 1 \) . The relation \( \left( {* * }\right) \) is written as \( {\left( {y}^{{p}^{qd}}\right) }^{{p}^{r}} = y \) , and according to \( \left( *\right) \) , we have \( {y}^{{p}^{r}} = y \) . We therefore have \( {y}^{{p}^{r} - 1} = 1 \) for all \( y \in {\mathbb{K}}^{ * } \) . However \( {\mathbb{K}}^{ * } \) , a finite multiplicative subgroup of a commutative field, is cyclic (see the remark in exercise 10 on page 28). We can therefore choose \( y \in {\mathbb{K}}^{ * } \) of order \( {p}^{d} - 1 \) . But we have seen that \( {y}^{{p}^{r} - 1} = 1 \) . as \( 0 \leq r < d \) , this implies \( r = 0 \) , that is to say \( d \mid n \) .

> b) Commençons par montrer que \( {X}^{{p}^{n}} - X \) est sans facteur carré non constant dans \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) . Supposons \( {X}^{{p}^{n}} - X = {Q}^{2}P \) , avec \( P, Q \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) . Par dérivation, on a \( {p}^{n}{X}^{{p}^{n} - 1} - 1 = {2Q}{Q}^{\prime }P + {Q}^{2}{P}^{\prime } \) donc \( Q \mid \left( {{p}^{n}{X}^{{p}^{n} - 1} - 1}\right) = - 1\left( {{p}^{n} = 0\text{ dans }{\mathbb{F}}_{p}}\right) \) , et donc \( Q \) est constant.

b) Let us begin by showing that \( {X}^{{p}^{n}} - X \) is square-free in \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) . Suppose \( {X}^{{p}^{n}} - X = {Q}^{2}P \) , with \( P, Q \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) . By differentiation, we have \( {p}^{n}{X}^{{p}^{n} - 1} - 1 = {2Q}{Q}^{\prime }P + {Q}^{2}{P}^{\prime } \) therefore \( Q \mid \left( {{p}^{n}{X}^{{p}^{n} - 1} - 1}\right) = - 1\left( {{p}^{n} = 0\text{ dans }{\mathbb{F}}_{p}}\right) \) , and thus \( Q \) is constant.

> Le résultat précédent entraîne que dans la décomposition de \( {X}^{{p}^{n}} - X \) en facteurs irréductibles de \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack : {X}^{{p}^{n}} - X = \mathop{\prod }\limits_{{i = 1}}^{k}{Q}_{i}^{{\alpha }_{i}} \) , on a \( {\alpha }_{i} = 1 \) pour tout \( i \) . Or d’après la question précédente, pour tout \( i \) on a \( {Q}_{i} \in {K}_{p}^{d} \) avec \( d \mid n \) . On en tire \( \left( {{X}^{{p}^{n}} - X}\right) \mid \mathop{\prod }\limits_{{d \mid n}}\left( {\mathop{\prod }\limits_{{Q \in {K}_{p}^{d}}}Q}\right) \) .

The previous result implies that in the factorization of \( {X}^{{p}^{n}} - X \) into irreducible factors of \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack : {X}^{{p}^{n}} - X = \mathop{\prod }\limits_{{i = 1}}^{k}{Q}_{i}^{{\alpha }_{i}} \), we have \( {\alpha }_{i} = 1 \) for all \( i \). However, according to the previous question, for all \( i \) we have \( {Q}_{i} \in {K}_{p}^{d} \) with \( d \mid n \). From this, we derive \( \left( {{X}^{{p}^{n}} - X}\right) \mid \mathop{\prod }\limits_{{d \mid n}}\left( {\mathop{\prod }\limits_{{Q \in {K}_{p}^{d}}}Q}\right) \).

> Pour tout entier \( d, d \mid n \) , et pour tout \( Q \in {K}_{p}^{d} \) , on a \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \) . Ces facteurs \( Q \) étant irréductibles, ils sont premiers entre eux deux à deux, et donc \( \mathop{\prod }\limits_{{d \mid n}}\left( {\mathop{\prod }\limits_{{Q \in {K}_{p}^{d}}}Q}\right) \mid \left( {{X}^{{p}^{n}} - X}\right) \) . On conclut à l'égalité en remarquant que ces polynômes sont unitaires.

For any integer \( d, d \mid n \), and for any \( Q \in {K}_{p}^{d} \), we have \( Q \mid \left( {{X}^{{p}^{n}} - X}\right) \). Since these factors \( Q \) are irreducible, they are pairwise coprime, and thus \( \mathop{\prod }\limits_{{d \mid n}}\left( {\mathop{\prod }\limits_{{Q \in {K}_{p}^{d}}}Q}\right) \mid \left( {{X}^{{p}^{n}} - X}\right) \). We conclude the equality by noting that these polynomials are monic.

> 3/a) L'identité souhaitée se déduit de 2/b) en passant aux degrés.

3/a) The desired identity is deduced from 2/b) by considering the degrees.

> b) Le résultat précédent entraîne que pour tout \( n \in {\mathbb{N}}^{ * }, n{I}_{p}^{n} \leq \mathop{\sum }\limits_{{d \mid n}}d{I}_{p}^{d} = {p}^{n} \) . Si on fixe maintenant \( n \in {\mathbb{N}}^{ * } \) , on en déduit

b) The previous result implies that for all \( n \in {\mathbb{N}}^{ * }, n{I}_{p}^{n} \leq \mathop{\sum }\limits_{{d \mid n}}d{I}_{p}^{d} = {p}^{n} \). If we now fix \( n \in {\mathbb{N}}^{ * } \), we deduce

\[
n{I}_{p}^{n} = {p}^{n} - \mathop{\sum }\limits_{\substack{{d \mid  n} \\  {d \neq  n} }}d{I}_{p}^{d} \geq  {p}^{n} - \mathop{\sum }\limits_{\substack{{d \mid  n} \\  {d \neq  n} }}{p}^{d} \geq  {p}^{n} - \mathop{\sum }\limits_{{d = 1}}^{{n - 1}}{p}^{d} = {p}^{n} - \frac{{p}^{n} - p}{p - 1} > 0.
\]

4/a) Soit \( p \) la caractéristique de \( \mathbb{K} \) . On a \( p \neq 0 \) car \( \mathbb{K} \) est fini, et \( p \) est un nombre premier (voir la proposition 1 page 57). Notons \( e \) l’élément unité de \( \mathbb{K} \) . L’application \( \varphi : \mathbb{Z} \rightarrow \mathbb{K}\;n \mapsto {ne} \) est un morphisme d’anneaux et Ker \( \varphi = p\mathbb{Z} \) . Si \( {\mathbb{K}}^{\prime } = \operatorname{Im}\varphi \subset \mathbb{K},{\mathbb{K}}^{\prime } \) est isomorphe à \( \mathbb{Z}/\operatorname{Ker}\varphi = \mathbb{Z}/p\mathbb{Z} = \; {\mathbb{F}}_{p} \) et c’est donc un sous-corps de \( \mathbb{K} \) isomorphe à \( {\mathbb{F}}_{p}\left( {\mathbb{K}}^{\prime }\right. \) s’appelle le sous corps premier de \( \mathbb{K} \) , voir la définition 4 page 58). Le corps \( \mathbb{K} \) apparaît alors comme étant un \( {\mathbb{K}}^{\prime } \) -espace vectoriel, de dimension finie \( n \) car \( \mathbb{K} \) est fini. Le corps \( \mathbb{K} \) est donc isomorphe (comme \( {\mathbb{K}}^{\prime } \) -espace vectoriel) à \( {\mathbb{K}}^{\prime n} \) , donc Card \( \left( \mathbb{K}\right) = \operatorname{Card}\left( {\mathbb{K}}^{\prime n}\right) = {\left( \operatorname{Card}\left( {\mathbb{K}}^{\prime }\right) \right) }^{n} = {\left( \operatorname{Card}\left( {\mathbb{F}}_{p}\right) \right) }^{n} = {p}^{n} \) .

> 4/a) Let \( p \) be the characteristic of \( \mathbb{K} \). We have \( p \neq 0 \) because \( \mathbb{K} \) is finite, and \( p \) is a prime number (see proposition 1 on page 57). Let \( e \) denote the identity element of \( \mathbb{K} \). The map \( \varphi : \mathbb{Z} \rightarrow \mathbb{K}\;n \mapsto {ne} \) is a ring homomorphism and Ker \( \varphi = p\mathbb{Z} \). If \( {\mathbb{K}}^{\prime } = \operatorname{Im}\varphi \subset \mathbb{K},{\mathbb{K}}^{\prime } \) is isomorphic to \( \mathbb{Z}/\operatorname{Ker}\varphi = \mathbb{Z}/p\mathbb{Z} = \; {\mathbb{F}}_{p} \) and is therefore a subfield of \( \mathbb{K} \) isomorphic to \( {\mathbb{F}}_{p}\left( {\mathbb{K}}^{\prime }\right. \), it is called the prime subfield of \( \mathbb{K} \) (see definition 4 on page 58). The field \( \mathbb{K} \) then appears as a \( {\mathbb{K}}^{\prime } \)-vector space of finite dimension \( n \) because \( \mathbb{K} \) is finite. The field \( \mathbb{K} \) is therefore isomorphic (as a \( {\mathbb{K}}^{\prime } \)-vector space) to \( {\mathbb{K}}^{\prime n} \), so Card \( \left( \mathbb{K}\right) = \operatorname{Card}\left( {\mathbb{K}}^{\prime n}\right) = {\left( \operatorname{Card}\left( {\mathbb{K}}^{\prime }\right) \right) }^{n} = {\left( \operatorname{Card}\left( {\mathbb{F}}_{p}\right) \right) }^{n} = {p}^{n} \).

Réciproquement, soit \( p \) un nombre premier et \( n \in {\mathbb{N}}^{ * } \) . D’après \( 3/b),{K}_{p}^{n} \neq \varnothing \) . Soit \( P \in {K}_{p}^{n} \) . \( \mathbb{K} = {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( P\right) \) est un corps (car \( P \) est irréductible), de cardinal \( {p}^{n} \) car \( \mathbb{K} \) est un \( {\mathbb{F}}_{p} \) -espace vectoriel de dimension \( n \) .

> Conversely, let \( p \) be a prime number and \( n \in {\mathbb{N}}^{ * } \). According to \( 3/b),{K}_{p}^{n} \neq \varnothing \). Let \( P \in {K}_{p}^{n} \). \( \mathbb{K} = {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( P\right) \) is a field (because \( P \) is irreducible), of cardinality \( {p}^{n} \) because \( \mathbb{K} \) is an \( {\mathbb{F}}_{p} \)-vector space of dimension \( n \).

b) Le groupe multiplicatif \( {\mathbb{K}}^{ * } \) étant de cardinal \( {p}^{n} - 1 \) , pour tout \( x \in {\mathbb{K}}^{ * },{x}^{{p}^{n} - 1} = 1 \) , donc pour tout \( x \in \mathbb{K},{x}^{{p}^{n}} = x \) . Autrement dit, les éléments de \( \mathbb{K} \) sont tous racine du polynôme \( {X}^{{p}^{n}} - X \) . Le degré de ce polynôme étant \( {p}^{n} = \operatorname{Card}\left( \mathbb{K}\right) \) , on en déduit que les racines de \( {X}^{{p}^{n}} - X \) sont exactement les éléments de \( \mathbb{K} \) . Or d’après \( 2/\mathrm{b}), P \mid \left( {{X}^{{p}^{n}} - X}\right) \) , donc il existe \( x \in \mathbb{K} \) tel que \( P\left( x\right) = 0. \)

> b) The multiplicative group \( {\mathbb{K}}^{ * } \) having cardinality \( {p}^{n} - 1 \), for all \( x \in {\mathbb{K}}^{ * },{x}^{{p}^{n} - 1} = 1 \), therefore for all \( x \in \mathbb{K},{x}^{{p}^{n}} = x \). In other words, the elements of \( \mathbb{K} \) are all roots of the polynomial \( {X}^{{p}^{n}} - X \). Since the degree of this polynomial is \( {p}^{n} = \operatorname{Card}\left( \mathbb{K}\right) \), we deduce that the roots of \( {X}^{{p}^{n}} - X \) are exactly the elements of \( \mathbb{K} \). However, according to \( 2/\mathrm{b}), P \mid \left( {{X}^{{p}^{n}} - X}\right) \), there exists \( x \in \mathbb{K} \) such that \( P\left( x\right) = 0. \)

c) Soit \( {P}_{0} \in {K}_{p}^{n} \) , soit \( \mathbb{K} \) un corps de cardinal \( {p}^{n} \) . La caractéristique de \( \mathbb{K} \) est \( p \) (en effet, c’est un nombre premier qui de plus divise \( {p}^{n} \) car \( \left( {\mathbb{K}, + }\right) \) est un groupe d’ordre \( {p}^{n} \) ), et on a vu au \( 4/\mathrm{a} \) ) que \( {\mathbb{F}}_{p} \) est isomorphe à un sous-corps de \( \mathbb{K} \) . Autrement dit,à un isomorphisme près, \( \mathbb{K} \) est un surcorps de \( {\mathbb{F}}_{p} \) , et donc d’après \( 4/\mathrm{b} \) ), il existe \( {x}_{0} \in \mathbb{K} \) tel que \( {P}_{0}\left( {x}_{0}\right) = 0 \) .

> c) Let \( {P}_{0} \in {K}_{p}^{n} \) , let \( \mathbb{K} \) be a field of cardinality \( {p}^{n} \) . The characteristic of \( \mathbb{K} \) is \( p \) (indeed, it is a prime number which moreover divides \( {p}^{n} \) because \( \left( {\mathbb{K}, + }\right) \) is a group of order \( {p}^{n} \) ), and we saw in \( 4/\mathrm{a} \) ) that \( {\mathbb{F}}_{p} \) is isomorphic to a subfield of \( \mathbb{K} \) . In other words, up to an isomorphism, \( \mathbb{K} \) is an extension field of \( {\mathbb{F}}_{p} \) , and therefore according to \( 4/\mathrm{b} \) ), there exists \( {x}_{0} \in \mathbb{K} \) such that \( {P}_{0}\left( {x}_{0}\right) = 0 \) .

Soit \( \Phi \) le morphisme \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \rightarrow \mathbb{K}\;Q \mapsto Q\left( {x}_{0}\right) \) . On a Ker \( \Phi = \left\{ {Q \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \mid Q\left( {x}_{0}\right) = 0}\right\} \) . C’est un idéal de \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) donc principal. Soit \( P \) unitaire tel que Ker \( \Phi = \left( P\right) \) . On a \( {P}_{0} \in \) Ker \( \Phi = \left( P\right) \) et \( {P}_{0} \) est irréductible, donc \( P = {P}_{0} \) , et donc Ker \( \Phi = \left( {P}_{0}\right) \) . Donc Im \( \Phi \) est isomorphe à \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\operatorname{Ker}\Phi = {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( {P}_{0}\right) \) . Ce dernier est un \( {\mathbb{F}}_{p} \) -espace vectoriel de dimension \( n \) , donc de cardinal \( {p}^{n} \) , et donc Im \( \Phi \) est de cardinal \( {p}^{n} \) . Or \( \operatorname{Card}\left( \mathbb{K}\right) = {p}^{n} \) , donc Im \( \Phi = \mathbb{K} \) .

> Let \( \Phi \) be the morphism \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \rightarrow \mathbb{K}\;Q \mapsto Q\left( {x}_{0}\right) \) . We have Ker \( \Phi = \left\{ {Q \in {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \mid Q\left( {x}_{0}\right) = 0}\right\} \) . It is an ideal of \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack \) , therefore principal. Let \( P \) be monic such that Ker \( \Phi = \left( P\right) \) . We have \( {P}_{0} \in \) Ker \( \Phi = \left( P\right) \) and \( {P}_{0} \) is irreducible, therefore \( P = {P}_{0} \) , and thus Ker \( \Phi = \left( {P}_{0}\right) \) . So Im \( \Phi \) is isomorphic to \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\operatorname{Ker}\Phi = {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( {P}_{0}\right) \) . The latter is an \( {\mathbb{F}}_{p} \) -vector space of dimension \( n \) , therefore of cardinality \( {p}^{n} \) , and thus Im \( \Phi \) is of cardinality \( {p}^{n} \) . However \( \operatorname{Card}\left( \mathbb{K}\right) = {p}^{n} \) , therefore Im \( \Phi = \mathbb{K} \) .

En résumé, \( \mathbb{K} \) est isomorphe au corps \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( {P}_{0}\right) \) , et ceci pour tout corps \( \mathbb{K} \) à \( {p}^{n} \) éléments. Deux corps de même cardinal sont donc isomorphes.

> In summary, \( \mathbb{K} \) is isomorphic to the field \( {\mathbb{F}}_{p}\left\lbrack X\right\rbrack /\left( {P}_{0}\right) \) , and this for any field \( \mathbb{K} \) with \( {p}^{n} \) elements. Two fields of the same cardinality are therefore isomorphic.

SUJET D’ÉTUDE 2 (TRANSCENDANCE DE \( e \) ET DE \( \pi \) ). 1/ Si \( F \in \mathbb{C}\left\lbrack X\right\rbrack \) ,(deg \( \left( F\right) = n \) ), on définit (avec \( {F}^{\left( 0\right) } = F \) par convention) :

> STUDY TOPIC 2 (TRANSCENDENCE OF \( e \) AND \( \pi \) ). 1/ If \( F \in \mathbb{C}\left\lbrack X\right\rbrack \) ,(deg \( \left( F\right) = n \) ), we define (with \( {F}^{\left( 0\right) } = F \) by convention) :

\[
\mathcal{D}\left( F\right)  = \mathop{\sum }\limits_{{k = 0}}^{{+\infty }}{F}^{\left( k\right) } = \mathop{\sum }\limits_{{k = 0}}^{n}{F}^{\left( k\right) } = F + {F}^{\prime } + \cdots  + {F}^{\left( n\right) }.
\]

a) Si \( F \in \mathbb{C}\left\lbrack X\right\rbrack \) et \( a \in \mathbb{C} \) , montrer que

> a) If \( F \in \mathbb{C}\left\lbrack X\right\rbrack \) and \( a \in \mathbb{C} \) , show that

\[
{e}^{a}\mathcal{D}\left( F\right) \left( 0\right)  = a{\int }_{0}^{1}{e}^{a\left( {1 - t}\right) }F\left( {at}\right) {dt} + \mathcal{D}\left( F\right) \left( a\right) .
\]

b) Soit \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) et \( p \in \mathbb{N}, p \geq 2 \) . Si \( F\left( X\right) = Q\left( X\right) {X}^{p - 1}/\left( {p - 1}\right) ! \) , montrer que \( \mathcal{D}\left( F\right) \left( 0\right) \) est un entier vérifiant \( \mathcal{D}\left( F\right) \left( 0\right) \equiv Q\left( 0\right) \left( {\;\operatorname{mod}\;p}\right) \) .

> b) Let \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack \) and \( p \in \mathbb{N}, p \geq 2 \). If \( F\left( X\right) = Q\left( X\right) {X}^{p - 1}/\left( {p - 1}\right) ! \), show that \( \mathcal{D}\left( F\right) \left( 0\right) \) is an integer satisfying \( \mathcal{D}\left( F\right) \left( 0\right) \equiv Q\left( 0\right) \left( {\;\operatorname{mod}\;p}\right) \).

2/ (Transcendance de \( e \) ). On rappelle qu’un nombre transcendant est un nombre non algébrique sur \( \mathbb{Q} \) . Supposons \( e \) algébrique. Alors il existe \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack , Q \neq 0 \) , tel que \( Q\left( e\right) = 0 \) . Soit \( n = \deg \left( Q\right) \) . Pour tout nombre premier \( p \) , on note

> 2/ (Transcendence of \( e \)). Recall that a transcendental number is a number that is not algebraic over \( \mathbb{Q} \). Suppose \( e \) is algebraic. Then there exists \( Q \in \mathbb{Z}\left\lbrack X\right\rbrack , Q \neq 0 \), such that \( Q\left( e\right) = 0 \). Let \( n = \deg \left( Q\right) \). For every prime number \( p \), we denote

\[
{F}_{p}\left( X\right)  = \frac{{X}^{p - 1}}{\left( {p - 1}\right) !}{\left\lbrack  \left( X - 1\right) \cdots \left( X - n\right) \right\rbrack  }^{p}.
\]

a) Si \( k \in \mathbb{N},1 \leq k \leq n \) , montrer que \( \mathcal{D}\left( {F}_{p}\right) \left( k\right) \) est un entier divisible par \( p \) .

> a) If \( k \in \mathbb{N},1 \leq k \leq n \), show that \( \mathcal{D}\left( {F}_{p}\right) \left( k\right) \) is an integer divisible by \( p \).

b) Si \( k \in \mathbb{N},1 \leq k \leq n \) , montrer que \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{\int }_{0}^{1}{e}^{k\left( {1 - t}\right) }{F}_{p}\left( {kt}\right) {dt} = 0 \) .

> b) If \( k \in \mathbb{N},1 \leq k \leq n \), show that \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{\int }_{0}^{1}{e}^{k\left( {1 - t}\right) }{F}_{p}\left( {kt}\right) {dt} = 0 \).

c) Conclure.

> c) Conclude.

3/ (Transcendance de \( \pi \) ). Supposons \( \pi \) algébrique sur \( \mathbb{Q} \) .

> 3/ (Transcendence of \( \pi \)). Suppose \( \pi \) is algebraic over \( \mathbb{Q} \).

a) Montrer qu’alors \( {i\pi } \) est algébrique.

> a) Show that \( {i\pi } \) is then algebraic.

Il existe donc \( Q = d{X}^{n} + {d}_{1}{X}^{n - 1} + \cdots + {d}_{n - 1}X + {d}_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack , d \neq 0 \) , tel que \( Q\left( {i\pi }\right) = 0 \) . Soient \( {\omega }_{1},\ldots ,{\omega }_{n} \) les racines de \( Q \) , de sorte que \( Q = d\left( {X - {\omega }_{1}}\right) \cdots \left( {X - {\omega }_{n}}\right) \) .

> There therefore exists \( Q = d{X}^{n} + {d}_{1}{X}^{n - 1} + \cdots + {d}_{n - 1}X + {d}_{n} \in \mathbb{Z}\left\lbrack X\right\rbrack , d \neq 0 \), such that \( Q\left( {i\pi }\right) = 0 \). Let \( {\omega }_{1},\ldots ,{\omega }_{n} \) be the roots of \( Q \), such that \( Q = d\left( {X - {\omega }_{1}}\right) \cdots \left( {X - {\omega }_{n}}\right) \).

b) Si \( \Phi \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) est symétrique, montrer que \( \Phi \left( {d{\omega }_{1},\ldots , d{\omega }_{n}}\right) \) est un entier.

> b) If \( \Phi \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) is symmetric, show that \( \Phi \left( {d{\omega }_{1},\ldots , d{\omega }_{n}}\right) \) is an integer.

Comme il existe \( k \) tel que \( {\omega }_{k} = {i\pi } \) , on a \( \mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + {e}^{{\omega }_{k}}}\right) = 0 \) , ce qui en développant s'écrit aussi

> Since there exists \( k \) such that \( {\omega }_{k} = {i\pi } \), we have \( \mathop{\prod }\limits_{{k = 1}}^{n}\left( {1 + {e}^{{\omega }_{k}}}\right) = 0 \), which, when expanded, is also written as

\[
1 + \mathop{\sum }\limits_{{j = 1}}^{{{2}^{n} - 1}}{e}^{{\alpha }_{j}} = 0
\]

\( {\alpha }_{1},\ldots ,{\alpha }_{{2}^{n} - 1} \) étant les nombres de la forme \( \mathop{\sum }\limits_{{i \in I}}{\omega }_{i}, I \) étant une partie non vide de \( \{ 1,\ldots , n\} \) . Supposons que \( C \) de ces \( {2}^{n} - 1 \) nombres soient nuls. Si \( m = {2}^{n} - 1 - C \) , on peut, quitte à renuméroter, supposer que les \( {\alpha }_{j} \) non nuls sont \( {\alpha }_{1},\ldots ,{\alpha }_{m} \) . c) Montrer que si un polynôme \( \Phi \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) est symétrique dans \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) , alors \( \Phi \left( {d{\alpha }_{1},\ldots , d{\alpha }_{m}}\right) \) est entier.

> \( {\alpha }_{1},\ldots ,{\alpha }_{{2}^{n} - 1} \) being the numbers of the form \( \mathop{\sum }\limits_{{i \in I}}{\omega }_{i}, I \) being a non-empty subset of \( \{ 1,\ldots , n\} \) . Suppose that \( C \) of these \( {2}^{n} - 1 \) numbers are zero. If \( m = {2}^{n} - 1 - C \) , we can, by renumbering, assume that the \( {\alpha }_{j} \) non-zero ones are \( {\alpha }_{1},\ldots ,{\alpha }_{m} \) . c) Show that if a polynomial \( \Phi \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) is symmetric in \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) , then \( \Phi \left( {d{\alpha }_{1},\ldots , d{\alpha }_{m}}\right) \) is an integer.

Pour tout nombre premier \( p \) , on pose

> For any prime number \( p \) , we define

\[
{F}_{p}\left( X\right)  = \frac{{d}^{{mp} + p - 1}{X}^{p - 1}}{\left( {p - 1}\right) !}{\left\lbrack  \left( X - {\alpha }_{1}\right) \cdots \left( X - {\alpha }_{m}\right) \right\rbrack  }^{p}.
\]

d) Montrer que \( \mathop{\sum }\limits_{{k = 1}}^{m}\mathcal{D}\left( {F}_{p}\right) \left( {\alpha }_{k}\right) \) est un entier divisible par \( p \) . e) En procédant comme au 2/, conclure.

> d) Show that \( \mathop{\sum }\limits_{{k = 1}}^{m}\mathcal{D}\left( {F}_{p}\right) \left( {\alpha }_{k}\right) \) is an integer divisible by \( p \) . e) By proceeding as in 2/, conclude.

Solution. 1/a) On pose \( f\left( t\right) = {e}^{-{at}}\mathcal{D}\left( F\right) \left( {at}\right) \) . Comme \( \mathcal{D}{\left( F\right) }^{\prime } = \mathcal{D}\left( F\right) - F \) , on a pour tout \( t \in \left\lbrack {0,1}\right\rbrack : {f}^{\prime }\left( t\right) = - a{e}^{-{at}}\mathcal{D}\left( F\right) \left( {at}\right) + a{e}^{-{at}}\mathcal{D}{\left( F\right) }^{\prime }\left( {at}\right) = - a{e}^{-{at}}F\left( {at}\right) \) , et donc par intégration \( f\left( 1\right) - f\left( 0\right) = - a{\int }_{0}^{1}{e}^{-{at}}F\left( {at}\right) {dt} \) , d’où le résultat compte tenu de la valeur de \( f \) .

> Solution. 1/a) Let \( f\left( t\right) = {e}^{-{at}}\mathcal{D}\left( F\right) \left( {at}\right) \) . Since \( \mathcal{D}{\left( F\right) }^{\prime } = \mathcal{D}\left( F\right) - F \) , we have for all \( t \in \left\lbrack {0,1}\right\rbrack : {f}^{\prime }\left( t\right) = - a{e}^{-{at}}\mathcal{D}\left( F\right) \left( {at}\right) + a{e}^{-{at}}\mathcal{D}{\left( F\right) }^{\prime }\left( {at}\right) = - a{e}^{-{at}}F\left( {at}\right) \) , and thus by integration \( f\left( 1\right) - f\left( 0\right) = - a{\int }_{0}^{1}{e}^{-{at}}F\left( {at}\right) {dt} \) , hence the result given the value of \( f \) .

b) Écrivons \( Q = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \) , de sorte que \( F = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\frac{{X}^{k + p - 1}}{\left( {p - 1}\right) !} \) . Alors

> b) Let us write \( Q = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \) , so that \( F = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\frac{{X}^{k + p - 1}}{\left( {p - 1}\right) !} \) . Then

\[
\mathcal{D}\left( F\right) \left( 0\right)  = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\frac{\left( {k + p - 1}\right) !}{\left( {p - 1}\right) !} = {a}_{0} + \mathop{\sum }\limits_{{k = 1}}^{n}{a}_{k}\left( {k + p - 1}\right) \cdots p,
\]

donc \( \mathcal{D}\left( F\right) \left( 0\right) \) est un entier qui vérifie \( \mathcal{D}\left( F\right) \left( 0\right) \equiv {a}_{0} \equiv Q\left( 0\right) \left( {\;\operatorname{mod}\;p}\right) \) .

> therefore \( \mathcal{D}\left( F\right) \left( 0\right) \) is an integer that satisfies \( \mathcal{D}\left( F\right) \left( 0\right) \equiv {a}_{0} \equiv Q\left( 0\right) \left( {\;\operatorname{mod}\;p}\right) \) .

2/a) Fixons \( k \in \mathbb{N},1 \leq k \leq n \) . Si \( G\left( X\right) = {F}_{p}\left( {X + k}\right) \) , on voit facilement que \( G \) a la forme \( G\left( X\right) = \frac{{X}^{p - 1}}{\left( {p - 1}\right) !}X \cdot H\left( X\right) \) avec \( H \in \mathbb{Z}\left\lbrack X\right\rbrack \) , donc d’après 1/b), \( N = \mathcal{D}\left( G\right) \left( 0\right) = \mathcal{D}\left( {F}_{p}\right) \left( k\right) \) est un entier vérifiant \( N \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) .

> 2/a) Let us fix \( k \in \mathbb{N},1 \leq k \leq n \) . If \( G\left( X\right) = {F}_{p}\left( {X + k}\right) \) , we easily see that \( G \) has the form \( G\left( X\right) = \frac{{X}^{p - 1}}{\left( {p - 1}\right) !}X \cdot H\left( X\right) \) with \( H \in \mathbb{Z}\left\lbrack X\right\rbrack \) , so according to 1/b), \( N = \mathcal{D}\left( G\right) \left( 0\right) = \mathcal{D}\left( {F}_{p}\right) \left( k\right) \) is an integer satisfying \( N \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) .

b) Si \( t \in \left\lbrack {0,1}\right\rbrack ,{e}^{k\left( {1 - t}\right) }\left| {{F}_{p}\left( {kt}\right) }\right| \leq {e}^{k}{k}^{p - 1}{\left( {n}^{n}\right) }^{p}/\left( {p - 1}\right) \) !, donc

> b) If \( t \in \left\lbrack {0,1}\right\rbrack ,{e}^{k\left( {1 - t}\right) }\left| {{F}_{p}\left( {kt}\right) }\right| \leq {e}^{k}{k}^{p - 1}{\left( {n}^{n}\right) }^{p}/\left( {p - 1}\right) \) !, therefore

\[
\left| {{\int }_{0}^{1}{e}^{k\left( {1 - t}\right) }{F}_{p}\left( {kt}\right) {dt}}\right|  \leq  {n}^{n}{e}^{k}\frac{{\left( k{n}^{n}\right) }^{p - 1}}{\left( {p - 1}\right) !}.
\]

Or \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{\left( k{n}^{n}\right) }^{p - 1}/\left( {p - 1}\right) ! = 0 \) , d’où \( 2/\mathrm{b} \) ).

> However \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{\left( k{n}^{n}\right) }^{p - 1}/\left( {p - 1}\right) ! = 0 \) , hence \( 2/\mathrm{b} \) ).

c) Écrivons \( Q = {a}_{0} + {a}_{1}X + \cdots + {a}_{n}{X}^{n} \) , avec \( Q\left( e\right) = 0 \) et \( Q \neq 0 \) . Quitte à diviser \( Q \) par \( X \) , on peut supposer \( {a}_{0} \neq 0 \) .

> c) Let us write \( Q = {a}_{0} + {a}_{1}X + \cdots + {a}_{n}{X}^{n} \) , with \( Q\left( e\right) = 0 \) and \( Q \neq 0 \) . By dividing \( Q \) by \( X \) if necessary, we can assume \( {a}_{0} \neq 0 \) .

Pour tout nombre premier \( p \) , on a d’après 1/a)

> For any prime number \( p \) , we have according to 1/a)

\[
\left( {\mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{e}^{k}}\right) \mathcal{D}\left( {F}_{p}\right) \left( 0\right)  = {S}_{p} + {T}_{p}\;\text{ avec }\;{S}_{p} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}k{\int }_{0}^{1}{e}^{k\left( {1 - t}\right) }{F}_{p}\left( {kt}\right) {dt},{T}_{p} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\mathcal{D}\left( {F}_{p}\right) \left( k\right) .
\]

Or \( \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{e}^{k} = Q\left( e\right) = 0 \) , donc \( 0 = {S}_{p} + {T}_{p}\;\left( *\right) \) . D’après \( 2/\mathrm{a}) \) , pour \( k \in \mathbb{N},1 \leq k \leq n \) , on a \( \mathcal{D}\left( {F}_{p}\right) \left( k\right) \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) donc d’après \( 1/\mathrm{b}) \) :

> However \( \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{e}^{k} = Q\left( e\right) = 0 \) , so \( 0 = {S}_{p} + {T}_{p}\;\left( *\right) \) . According to \( 2/\mathrm{a}) \) , for \( k \in \mathbb{N},1 \leq k \leq n \) , we have \( \mathcal{D}\left( {F}_{p}\right) \left( k\right) \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) so according to \( 1/\mathrm{b}) \) :

\[
{T}_{p} = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}\mathcal{D}\left( {F}_{p}\right) \left( k\right)  \equiv  {a}_{0}\mathcal{D}\left( {F}_{p}\right) \left( 0\right)  \equiv  {a}_{0}{\left( -1\right) }^{pn}{\left( n!\right) }^{p}\;\left( {\;\operatorname{mod}\;p}\right) .
\]

Or \( {a}_{0} \neq 0 \) , et donc pour tout nombre premier \( p \) supérieur à \( \max \left\{ {\left| {a}_{0}\right| , n}\right\} \) , on a \( {T}_{p} \text{ ≢ } 0\left( {\;\operatorname{mod}\;p}\right) \) . \( {T}_{p} \) est donc un entier non nul, et vérifie donc \( \left| {T}_{p}\right| \geq 1 \) . Or d’après \( 2/\mathrm{b}),\mathop{\lim }\limits_{{p \rightarrow \infty }}{S}_{p} = 0 \) , ce qui est absurde d’après (*). Le nombre réel e est donc transcendant.

> However \( {a}_{0} \neq 0 \) , and thus for any prime number \( p \) greater than \( \max \left\{ {\left| {a}_{0}\right| , n}\right\} \) , we have \( {T}_{p} \text{ ≢ } 0\left( {\;\operatorname{mod}\;p}\right) \) . \( {T}_{p} \) is therefore a non-zero integer, and thus satisfies \( \left| {T}_{p}\right| \geq 1 \) . However, according to \( 2/\mathrm{b}),\mathop{\lim }\limits_{{p \rightarrow \infty }}{S}_{p} = 0 \) , which is absurd according to (*). The real number e is therefore transcendental.

3/a) Avec le résultat du problème 5, c’est immédiat. En effet, l’ensemble des nombres algébriques étant un corps, si \( \pi \) est algébrique, comme \( i \) est algébrique (racine de \( {X}^{2} + 1 \) ), \( {i\pi } \) est algébrique.

> 3/a) With the result of problem 5, it is immediate. Indeed, since the set of algebraic numbers is a field, if \( \pi \) is algebraic, as \( i \) is algebraic (root of \( {X}^{2} + 1 \) ), \( {i\pi } \) is algebraic.

Nous allons néanmoins montrer ce résultat directement. Si \( \pi \) est algébrique, il existe \( n \in {\mathbb{N}}^{ * } \) et \( {a}_{0},\ldots ,{a}_{n} \in \mathbb{Z},{a}_{n} \neq 0 \) , tels que \( {a}_{0} + {a}_{1}\pi + \cdots + {a}_{n}{\pi }^{n} = 0 \) . En notant \( \theta = {i\pi } \) , on a

> We will nevertheless show this result directly. If \( \pi \) is algebraic, there exist \( n \in {\mathbb{N}}^{ * } \) and \( {a}_{0},\ldots ,{a}_{n} \in \mathbb{Z},{a}_{n} \neq 0 \) such that \( {a}_{0} + {a}_{1}\pi + \cdots + {a}_{n}{\pi }^{n} = 0 \) . By denoting \( \theta = {i\pi } \) , we have

\[
\left( {{a}_{0} - {a}_{2}{\theta }^{2} + \cdots }\right)  - i\left( {{a}_{1}\theta  - {a}_{3}{\theta }^{3} + \cdots }\right)  = 0,
\]

et en posant \( Q = {\left( {a}_{0} - {a}_{2}{X}^{2} + \cdots \right) }^{2} + {\left( {a}_{1}X - {a}_{3}{X}^{3} + \cdots \right) }^{2} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , on a donc \( Q\left( \theta \right) = Q\left( {i\pi }\right) = 0 \) et \( Q \neq 0 \) . D’où le résultat.

> and by setting \( Q = {\left( {a}_{0} - {a}_{2}{X}^{2} + \cdots \right) }^{2} + {\left( {a}_{1}X - {a}_{3}{X}^{3} + \cdots \right) }^{2} \in \mathbb{Z}\left\lbrack X\right\rbrack \) , we therefore have \( Q\left( \theta \right) = Q\left( {i\pi }\right) = 0 \) and \( Q \neq 0 \) . Hence the result.

b) Les nombres complexes \( d{\omega }_{1},\ldots , d{\omega }_{n} \) sont les racines du polynôme \( {d}^{n - 1}Q\left( {X/d}\right) = {X}^{n} + \; {d}_{1}{X}^{n - 1} + d{d}_{2}{X}^{n - 2} + \cdots + {d}^{n - 2}{d}_{n - 1}X + {d}^{n - 1}{d}_{n} = R\left( X\right) \) . Ce polynôme est unitaire à coefficients entiers, donc toute expression polynomiale à coefficients entiers et symétrique en les racines de \( R\left( X\right) \) , est un entier (voir la remarque 4 page 84), d'où le résultat.

> b) The complex numbers \( d{\omega }_{1},\ldots , d{\omega }_{n} \) are the roots of the polynomial \( {d}^{n - 1}Q\left( {X/d}\right) = {X}^{n} + \; {d}_{1}{X}^{n - 1} + d{d}_{2}{X}^{n - 2} + \cdots + {d}^{n - 2}{d}_{n - 1}X + {d}^{n - 1}{d}_{n} = R\left( X\right) \) . This polynomial is monic with integer coefficients, so any polynomial expression with integer coefficients that is symmetric in the roots of \( R\left( X\right) \) is an integer (see remark 4 on page 84), hence the result.

c) Le polynôme \( \Phi \) étant symétrique dans \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) , il existe \( P \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) tel que \( \Phi = P\left( {{\sum }_{1}^{ * },\ldots ,{\sum }_{m}^{ * }}\right) \) , les \( {\sum }_{i}^{ * } \) désignant les fonctions symétriques élémentaires de \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) .

> c) Since the polynomial \( \Phi \) is symmetric in \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) , there exists \( P \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) such that \( \Phi = P\left( {{\sum }_{1}^{ * },\ldots ,{\sum }_{m}^{ * }}\right) \) , where \( {\sum }_{i}^{ * } \) denote the elementary symmetric functions of \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{m}}\right\rbrack \) .

Si on note \( {\sum }_{i} \) les fonctions symétriques élémentaires de \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{{2}^{n} - 1}}\right\rbrack \) , on a facilement

> If we denote \( {\sum }_{i} \) as the elementary symmetric functions of \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{{2}^{n} - 1}}\right\rbrack \) , we easily have

\[
\forall i,1 \leq  i \leq  m,\;{\sigma }_{i} = {\sum }_{i}^{ * }\left( {d{\alpha }_{1},\ldots , d{\alpha }_{m}}\right)  = {\sum }_{i}\left( {d{\alpha }_{1},\ldots , d{\alpha }_{m},0,\ldots ,0}\right)  = {\sum }_{i}\left( {d{\alpha }_{1},\ldots , d{\alpha }_{{2}^{n} - 1}}\right) .
\]

Nous allons montrer que les \( {\sigma }_{i} \) sont entiers, ce qui prouvera le résultat compte tenu du fait que \( \Phi \left( {d{\alpha }_{1},\ldots , d{\alpha }_{m}}\right) = P\left( {{\sigma }_{1},\ldots ,{\sigma }_{m}}\right) \) et que \( P \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . Notons \( \mathcal{P} \) l’ensemble des parties non vides de \( \{ 1,\ldots , n\} \) , et désignons par \( I \) la bijection de \( J = \left\{ {1,\ldots ,{2}^{n} - 1}\right\} \) vers \( \mathcal{P} \) telle que \( {\alpha }_{j} = \mathop{\sum }\limits_{{i \in I\left( j\right) }}{\omega }_{i} \) . Pour tout \( j \in J \) on note \( {M}_{j} = \mathop{\sum }\limits_{{i \in I\left( j\right) }}{X}_{i} \) . Le polynôme

> We will show that the \( {\sigma }_{i} \) are integers, which will prove the result given that \( \Phi \left( {d{\alpha }_{1},\ldots , d{\alpha }_{m}}\right) = P\left( {{\sigma }_{1},\ldots ,{\sigma }_{m}}\right) \) and that \( P \in \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) . Let \( \mathcal{P} \) be the set of non-empty subsets of \( \{ 1,\ldots , n\} \) , and let \( I \) denote the bijection from \( J = \left\{ {1,\ldots ,{2}^{n} - 1}\right\} \) to \( \mathcal{P} \) such that \( {\alpha }_{j} = \mathop{\sum }\limits_{{i \in I\left( j\right) }}{\omega }_{i} \) . For all \( j \in J \) we denote \( {M}_{j} = \mathop{\sum }\limits_{{i \in I\left( j\right) }}{X}_{i} \) . The polynomial

\[
{Q}_{i}\left( {{X}_{1},\ldots ,{X}_{n}}\right)  = {\sum }_{i}\left( {{M}_{1},\ldots ,{M}_{{2}^{n} - 1}}\right)  \in  \mathbb{Z}\left\lbrack  {{X}_{1},\ldots ,{X}_{n}}\right\rbrack
\]

est symétrique dans \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) (puisqu’une permutation des indéterminées \( {\left( {X}_{i}\right) }_{1 \leq i \leq n} \) donne lieu à une permutation des \( {\left( {M}_{j}\right) }_{1 \leq j < {2}^{n}} \) et que \( {\sum }_{i} \) est symétrique dans \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{{2}^{n} - 1}}\right\rbrack \) ). Comme \( d{\alpha }_{j} = {M}_{j}\left( {d{\omega }_{1},\ldots , d{\omega }_{n}}\right) \) , on a

> is symmetric in \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) (since a permutation of the indeterminates \( {\left( {X}_{i}\right) }_{1 \leq i \leq n} \) results in a permutation of the \( {\left( {M}_{j}\right) }_{1 \leq j < {2}^{n}} \) and \( {\sum }_{i} \) is symmetric in \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{{2}^{n} - 1}}\right\rbrack \) ). As \( d{\alpha }_{j} = {M}_{j}\left( {d{\omega }_{1},\ldots , d{\omega }_{n}}\right) \) , we have

\[
{\sigma }_{i} = {\sum }_{i}\left( {d{\alpha }_{1},\ldots , d{\alpha }_{{2}^{n} - 1}}\right)  = {Q}_{i}\left( {d{\omega }_{1},\ldots , d{\omega }_{n}}\right)
\]

d’où on déduit \( {\sigma }_{i} \in \mathbb{Z} \) d’après 3/b) puisque \( {Q}_{i} \) est symétrique dans \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) .

> from which we deduce \( {\sigma }_{i} \in \mathbb{Z} \) according to 3/b) since \( {Q}_{i} \) is symmetric in \( \mathbb{Z}\left\lbrack {{X}_{1},\ldots ,{X}_{n}}\right\rbrack \) .

d) On peut aussi écrire \( {F}_{p}\left( X\right) \) sous la forme

> d) We can also write \( {F}_{p}\left( X\right) \) in the form

\[
{F}_{p}\left( X\right)  = \frac{1}{\left( {p - 1}\right) !}{\left( dX\right) }^{p - 1}{\left\lbrack  \left( dX - d{\alpha }_{1}\right) \cdots \left( dX - d{\alpha }_{m}\right) \right\rbrack  }^{p}.
\]

\( \left( {* * }\right) \)

> Un peu d’attention montre alors que le polynôme \( G\left( X\right) = \left( {p - 1}\right) !\mathop{\sum }\limits_{{k = 1}}^{m}{F}_{p}\left( {X + {\alpha }_{k}}\right) \) a pour coefficients des polynômes symétriques à coefficients entiers en les \( {\left( d{\alpha }_{k}\right) }_{1 \leq k \leq m} \) , et donc d’après \( 3/\mathrm{c}), G\left( X\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) . Or pour tout \( k,1 \leq k \leq m,{X}^{p} \mid {F}_{p}\left( {X + {\alpha }_{k}}\right) \) , donc \( {X}^{p} \mid G\left( X\right) \) , et donc il existe \( H \in \mathbb{Z}\left\lbrack X\right\rbrack \) tel que \( G\left( X\right) = {X}^{p}H\left( X\right) \) . Finalement, on a montré que \( F\left( X\right) = \; \mathop{\sum }\limits_{{k = 1}}^{m}{F}_{p}\left( {X + {\alpha }_{k}}\right) \) s’écrit sous la forme \( F\left( X\right) = \frac{{X}^{p}}{\left( {p - 1}\right) !}H\left( X\right) \) , et donc d’après \( 1/\mathrm{b}) \) ,

A little attention then shows that the polynomial \( G\left( X\right) = \left( {p - 1}\right) !\mathop{\sum }\limits_{{k = 1}}^{m}{F}_{p}\left( {X + {\alpha }_{k}}\right) \) has as coefficients symmetric polynomials with integer coefficients in the \( {\left( d{\alpha }_{k}\right) }_{1 \leq k \leq m} \) , and therefore according to \( 3/\mathrm{c}), G\left( X\right) \in \mathbb{Z}\left\lbrack X\right\rbrack \) . However, for all \( k,1 \leq k \leq m,{X}^{p} \mid {F}_{p}\left( {X + {\alpha }_{k}}\right) \) , therefore \( {X}^{p} \mid G\left( X\right) \) , and thus there exists \( H \in \mathbb{Z}\left\lbrack X\right\rbrack \) such that \( G\left( X\right) = {X}^{p}H\left( X\right) \) . Finally, we have shown that \( F\left( X\right) = \; \mathop{\sum }\limits_{{k = 1}}^{m}{F}_{p}\left( {X + {\alpha }_{k}}\right) \) can be written in the form \( F\left( X\right) = \frac{{X}^{p}}{\left( {p - 1}\right) !}H\left( X\right) \) , and therefore according to \( 1/\mathrm{b}) \) ,

\[
\mathcal{D}\left( F\right) \left( 0\right)  = \mathop{\sum }\limits_{{k = 1}}^{m}\mathcal{D}\left( {F}_{p}\right) \left( {\alpha }_{k}\right)  \equiv  0\;\left( {\;\operatorname{mod}\;p}\right) .
\]

e) L’égalité de 3/b) s’écrit \( \left( {C + 1}\right) + \mathop{\sum }\limits_{{j = 1}}^{m}{e}^{{\alpha }_{j}} = 0 \) avec \( C \in \mathbb{N} \) et d’après \( 1/\mathrm{a} \) ), en posant

> e) The equality from 3/b) is written \( \left( {C + 1}\right) + \mathop{\sum }\limits_{{j = 1}}^{m}{e}^{{\alpha }_{j}} = 0 \) with \( C \in \mathbb{N} \) and according to \( 1/\mathrm{a} \) ), by setting

\[
{S}_{p} = \mathop{\sum }\limits_{{k = 1}}^{m}{\alpha }_{k}{\int }_{0}^{1}{e}^{{\alpha }_{k}\left( {1 - t}\right) }{F}_{p}\left( {{\alpha }_{k}t}\right) {dt},\;{T}_{p} = \left( {C + 1}\right) \mathcal{D}\left( {F}_{p}\right) \left( 0\right) ,\;{U}_{p} = \mathop{\sum }\limits_{{k = 1}}^{m}\mathcal{D}\left( {F}_{p}\right) \left( {\alpha }_{k}\right) ,
\]

on a \( 0 = {S}_{p} + {T}_{p} + {U}_{p}\;\left( {* * * }\right) \) . Or pour tout \( k \) , pour tout \( p \) , pour tout \( t \in \left\lbrack {0,1}\right\rbrack \) ,

> we have \( 0 = {S}_{p} + {T}_{p} + {U}_{p}\;\left( {* * * }\right) \) . However, for all \( k \) , for all \( p \) , for all \( t \in \left\lbrack {0,1}\right\rbrack \) ,

\[
\left| {{F}_{p}\left( {{\alpha }_{k}t}\right) }\right|  \leq  \frac{{\left| d\right| }^{{mp} + p - 1}{M}^{p - 1}}{\left( {p - 1}\right) !}{\left\lbrack  {\left( 2M\right) }^{m}\right\rbrack  }^{p} = {\left| d\right| }^{m}{\left( 2M\right) }^{m}\frac{{K}^{p - 1}}{\left( {p - 1}\right) !}
\]

où \( M = \mathop{\sup }\limits_{{1 \leq k \leq n}}\left| {\alpha }_{k}\right| \) et \( K = {\left| d\right| }^{m + 1}M{\left( 2M\right) }^{m} \) sont des constantes. On en déduit que

> where \( M = \mathop{\sup }\limits_{{1 \leq k \leq n}}\left| {\alpha }_{k}\right| \) and \( K = {\left| d\right| }^{m + 1}M{\left( 2M\right) }^{m} \) are constants. We deduce that

\[
\left| {{\int }_{0}^{1}{e}^{{\alpha }_{k}\left( {1 - t}\right) }{F}_{p}\left( {{\alpha }_{k}t}\right) {dt}}\right|  \leq  {e}^{M}{\left| d\right| }^{m}{\left( 2M\right) }^{m}\frac{{K}^{p - 1}}{\left( {p - 1}\right) !},
\]

et donc \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{\int }_{0}^{1}{e}^{{\alpha }_{k}\left( {1 - t}\right) }{F}_{p}\left( {{\alpha }_{k}t}\right) {dt} = 0 \) , et ceci pour tout \( k \) , donc

> and thus \( \mathop{\lim }\limits_{{p \rightarrow + \infty }}{\int }_{0}^{1}{e}^{{\alpha }_{k}\left( {1 - t}\right) }{F}_{p}\left( {{\alpha }_{k}t}\right) {dt} = 0 \) , and this for all \( k \) , therefore

\[
\mathop{\lim }\limits_{{p \rightarrow   + \infty }}{S}_{p} = 0
\]

(***)

> D'après (**), on peut écrire

According to (**), we can write

\[
{F}_{p}\left( X\right)  = \frac{{X}^{p - 1}}{\left( {p - 1}\right) !} \cdot  \left( {\mathop{\sum }\limits_{{\ell  = 0}}^{{mp}}{a}_{\ell }{X}^{\ell }}\right) ,
\]

où les \( {a}_{\ell } \) sont des polynômes à coefficients entiers symétriques en \( d{\alpha }_{1},\ldots , d{\alpha }_{m} \) , donc d’après \( 3/\mathrm{c}) \) les \( {a}_{\ell } \) sont entiers. Par ailleurs, on vérifie facilement que \( {a}_{0} = {\left( -1\right) }^{mp}{d}^{p - 1}{\left( d{\alpha }_{1}\cdots d{\alpha }_{m}\right) }^{p} = \; {d}^{p - 1}{L}^{p} \) où \( L = {\left( -1\right) }^{m}\left( {d{\alpha }_{1}\cdots d{\alpha }_{m}}\right) \) est une constante, entière d’après \( 3/\mathrm{c}) \) . D’après \( 1/\mathrm{b}) \) , on voit donc que \( \mathcal{D}\left( {F}_{p}\right) \left( 0\right) \) est un entier vérifiant \( \mathcal{D}\left( {F}_{p}\right) \left( 0\right) \equiv {a}_{0}\left( {\;\operatorname{mod}\;p}\right) \) . Finalement, on obtient \( {T}_{p} \equiv \left( {C + 1}\right) {a}_{0} \equiv \left( {C + 1}\right) {d}^{p - 1}{L}^{p}\left( {\;\operatorname{mod}\;p}\right) \) . Comme de plus \( {U}_{p} \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) d’après \( 3/\mathrm{d}) \) , on voit que \( {T}_{p} + {U}_{p} \equiv \left( {C + 1}\right) {d}^{p - 1}{L}^{p}\left( {\;\operatorname{mod}\;p}\right) \) . Donc si \( p > \sup \{ C + 1, d, L\} \) est un nombre premier, \( {T}_{p} + {U}_{p} \) est un entier non nul, donc \( \left| {{T}_{p} + {U}_{p}}\right| \geq 1 \) . De (***), on tire alors \( \left| {S}_{p}\right| \geq 1 \) , ce qui est absurde d’après (***). Le nombre \( \pi \) est donc transcendant.

> where the \( {a}_{\ell } \) are polynomials with integer coefficients symmetric in \( d{\alpha }_{1},\ldots , d{\alpha }_{m} \) , so according to \( 3/\mathrm{c}) \) the \( {a}_{\ell } \) are integers. Furthermore, it is easy to verify that \( {a}_{0} = {\left( -1\right) }^{mp}{d}^{p - 1}{\left( d{\alpha }_{1}\cdots d{\alpha }_{m}\right) }^{p} = \; {d}^{p - 1}{L}^{p} \) where \( L = {\left( -1\right) }^{m}\left( {d{\alpha }_{1}\cdots d{\alpha }_{m}}\right) \) is a constant, an integer according to \( 3/\mathrm{c}) \) . According to \( 1/\mathrm{b}) \) , we therefore see that \( \mathcal{D}\left( {F}_{p}\right) \left( 0\right) \) is an integer satisfying \( \mathcal{D}\left( {F}_{p}\right) \left( 0\right) \equiv {a}_{0}\left( {\;\operatorname{mod}\;p}\right) \) . Finally, we obtain \( {T}_{p} \equiv \left( {C + 1}\right) {a}_{0} \equiv \left( {C + 1}\right) {d}^{p - 1}{L}^{p}\left( {\;\operatorname{mod}\;p}\right) \) . Since, moreover, \( {U}_{p} \equiv 0\left( {\;\operatorname{mod}\;p}\right) \) according to \( 3/\mathrm{d}) \) , we see that \( {T}_{p} + {U}_{p} \equiv \left( {C + 1}\right) {d}^{p - 1}{L}^{p}\left( {\;\operatorname{mod}\;p}\right) \) . Thus, if \( p > \sup \{ C + 1, d, L\} \) is a prime number, \( {T}_{p} + {U}_{p} \) is a non-zero integer, so \( \left| {{T}_{p} + {U}_{p}}\right| \geq 1 \) . From (***), we then derive \( \left| {S}_{p}\right| \geq 1 \) , which is absurd according to (***). The number \( \pi \) is therefore transcendental.

Remarque. La transcendance de \( \pi \) a été démontrée pour la première fois par Lindemann en 1882, qui a établit de manière plus générale que si \( {\alpha }_{i} \) et \( {\beta }_{i} \) sont algébriques (avec les \( {\alpha }_{i} \) non nuls et les \( {\beta }_{i} \) distincts), alors \( \sum {\alpha }_{i}{e}^{{\beta }_{i}} \neq 0 \) .

> Remark. The transcendence of \( \pi \) was first proven by Lindemann in 1882, who established more generally that if \( {\alpha }_{i} \) and \( {\beta }_{i} \) are algebraic (with the \( {\alpha }_{i} \) non-zero and the \( {\beta }_{i} \) distinct), then \( \sum {\alpha }_{i}{e}^{{\beta }_{i}} \neq 0 \) .

- Un autre résultat célèbre de transcendance est le théorème de Gelfond-Schneider (1934), qui affime que \( \mathrm{{Si}}\alpha \) et \( \beta \) sont algébriques, \( \alpha  \notin  \{ 0,1\} ,\beta  \notin  \mathbb{Q} \) , alors \( {\alpha }^{\beta } \) est transcendant.

> - Another famous transcendence result is the Gelfond-Schneider theorem (1934), which states that if \( \mathrm{{Si}}\alpha \) and \( \beta \) are algebraic, \( \alpha  \notin  \{ 0,1\} ,\beta  \notin  \mathbb{Q} \) , then \( {\alpha }^{\beta } \) is transcendental.

- On connaît peu de classes de nombres transcendants. On sait que \( e,\pi ,\log 2,\log 3/\log 2 \) , \( {e}^{\pi },\Gamma \left( {1/4}\right) \) sont transcendants, mais on ne sait même pas si \( {2}^{e},{2}^{\pi },{\pi }^{e}, e + \pi ,\zeta \left( 5\right) \) ou \( \gamma \) (constante d'Euler) sont irrationnels (on sait que \( \zeta \left( 3\right) \) est irrationnel).

> - Few classes of transcendental numbers are known. We know that \( e,\pi ,\log 2,\log 3/\log 2 \) , \( {e}^{\pi },\Gamma \left( {1/4}\right) \) are transcendental, but we do not even know if \( {2}^{e},{2}^{\pi },{\pi }^{e}, e + \pi ,\zeta \left( 5\right) \) or \( \gamma \) (Euler's constant) are irrational (we know that \( \zeta \left( 3\right) \) is irrational).

- On peut démontrer assez facilement que \( {\pi }^{2} \) (donc \( \pi \) ) est irrationnel (voir le chapitre intégration du tome analyse). Ceci est aussi une conséquence de la transcendance de \( \pi \) .

> - It can be shown quite easily that \( {\pi }^{2} \) (and thus \( \pi \) ) is irrational (see the integration chapter of the analysis volume). This is also a consequence of the transcendence of \( \pi \) .

- En démontrant la transcendance de \( \pi \) , Lindemann résolvait le célèbre problème de la quadrature du cercle. Ce problème consiste à tracer à l'aide d'une règle et d'un compas un carré ayant même aire qu'un disque donné. Le transcendance de \( \pi \) montre que ce problème est insoluble (on montre en effet que tout point construit avec une règle et un compas à partir du cercle unité a des coordonnées algébriques).

> - By proving the transcendence of \( \pi \) , Lindemann solved the famous problem of squaring the circle. This problem consists of drawing, using a straightedge and compass, a square with the same area as a given disk. The transcendence of \( \pi \) shows that this problem is insoluble (it is indeed shown that any point constructed with a straightedge and compass from the unit circle has algebraic coordinates).

SUJET D'ÉTUDE 3 (POLYNÔMES ORTHOGONAUX). Soit \( I \) un intervalle réel non réduit à un singleton, et \( w : I \rightarrow \mathbb{R} \) une fonction continue strictement positive sur \( I \) . On suppose que pour tout \( n \in \mathbb{N} \) , la fonction \( x \mapsto {x}^{n}w\left( x\right) \) est intégrable sur \( I \) . On note \( \mathcal{C} \) l’ensemble des fonctions continues \( f : I \rightarrow \mathbb{R} \) telles que \( x \mapsto {f}^{2}\left( x\right) w\left( x\right) \) est intégrable sur \( I \) . Les fonctions polynômes appartiennent à \( \mathcal{C} \) d’après l’hypothèse sur \( w \) .

> STUDY TOPIC 3 (ORTHOGONAL POLYNOMIALS). Let \( I \) be a real interval not reduced to a singleton, and \( w : I \rightarrow \mathbb{R} \) a strictly positive continuous function on \( I \) . We assume that for all \( n \in \mathbb{N} \) , the function \( x \mapsto {x}^{n}w\left( x\right) \) is integrable on \( I \) . We denote by \( \mathcal{C} \) the set of continuous functions \( f : I \rightarrow \mathbb{R} \) such that \( x \mapsto {f}^{2}\left( x\right) w\left( x\right) \) is integrable on \( I \) . Polynomial functions belong to \( \mathcal{C} \) according to the hypothesis on \( w \) .

1/a) Montrer que \( \mathcal{C} \) est un espace vectoriel, et que

> 1/a) Show that \( \mathcal{C} \) is a vector space, and that

\[
\langle f, g\rangle  = {\int }_{I}f\left( x\right) g\left( x\right) w\left( x\right) {dx}
\]

définit un produit scalaire sur \( \mathcal{C} \) . On munit \( \mathcal{C} \) de ce produit scalaire et on note \( \parallel \cdot \parallel \) la norme associée.

> defines an inner product on \( \mathcal{C} \) . We equip \( \mathcal{C} \) with this inner product and denote by \( \parallel \cdot \parallel \) the associated norm.

b) Montrer qu’il existe une unique base \( \left( {P}_{n}\right) \) de l’e.v des polynômes \( \mathbb{R}\left\lbrack X\right\rbrack \) , orthonormale pour ce produit scalaire, et vérifiant \( \deg {P}_{n} = n \) pour tout \( n \in \mathbb{N} \) et telle que le coefficient dominant \( {\gamma }_{n} \) de \( {P}_{n} \) est positif. Les \( {P}_{n} \) sont appelés polynômes orthogonaux associés à \( w \) . c) Montrer que les polynômes \( {P}_{n} \) vérifient une relation de récurrence de la forme

> b) Show that there exists a unique basis \( \left( {P}_{n}\right) \) of the vector space of polynomials \( \mathbb{R}\left\lbrack X\right\rbrack \) , orthonormal for this inner product, satisfying \( \deg {P}_{n} = n \) for all \( n \in \mathbb{N} \) and such that the leading coefficient \( {\gamma }_{n} \) of \( {P}_{n} \) is positive. The \( {P}_{n} \) are called orthogonal polynomials associated with \( w \) . c) Show that the polynomials \( {P}_{n} \) satisfy a recurrence relation of the form

\[
\forall n \geq  2,\;{P}_{n}\left( X\right)  = \left( {{a}_{n}X + {b}_{n}}\right) {P}_{n - 1}\left( X\right)  + {c}_{n}{P}_{n - 2}\left( X\right)
\]

(*)

> pour des suites réelles \( \left( {a}_{n}\right) ,\left( {b}_{n}\right) \) et \( \left( {c}_{n}\right) \) que l’on explicitera.

for real sequences \( \left( {a}_{n}\right) ,\left( {b}_{n}\right) \) and \( \left( {c}_{n}\right) \) which will be made explicit.

> d) (Formule de Darboux). En déduire que le noyau \( {K}_{n}\left( {x, y}\right) = \mathop{\sum }\limits_{{i = 0}}^{n}{P}_{i}\left( x\right) {P}_{i}\left( y\right) \) vérifie

d) (Darboux's formula). Deduce that the kernel \( {K}_{n}\left( {x, y}\right) = \mathop{\sum }\limits_{{i = 0}}^{n}{P}_{i}\left( x\right) {P}_{i}\left( y\right) \) satisfies

\[
\forall n \in  \mathbb{N},\forall \left( {x, y}\right)  \in  {\mathbb{R}}^{2}, x \neq  y,\;\mathop{\sum }\limits_{{i = 0}}^{n}{P}_{i}\left( x\right) {P}_{i}\left( y\right)  = \frac{{\gamma }_{n}}{{\gamma }_{n + 1}}\frac{{P}_{n + 1}\left( x\right) {P}_{n}\left( y\right)  - {P}_{n}\left( x\right) {P}_{n + 1}\left( y\right) }{x - y}
\]

et calculer également \( {K}_{n}\left( {x, y}\right) \) lorsque \( x = y \) .

> and also calculate \( {K}_{n}\left( {x, y}\right) \) when \( x = y \) .

2 / (Zéros des polynômes orthogonaux).

> 2 / (Zeros of orthogonal polynomials).

a) Montrer que pour tout \( n \in {\mathbb{N}}^{ * },{P}_{n} \) a \( n \) zéros réels distincts dans l’intervalle \( I \) .

> a) Show that for all \( n \in {\mathbb{N}}^{ * },{P}_{n} \) there are \( n \) distinct real zeros in the interval \( I \) .

b) Montrer qu’entre deux zéros consécutifs de \( {P}_{n + 1} \) , il y a un et un seul zéro de \( {P}_{n} \) .

> b) Show that between two consecutive zeros of \( {P}_{n + 1} \) , there is one and only one zero of \( {P}_{n} \) .

c) Soit \( f \in \mathcal{C} \) et \( n \in \mathbb{N} \) . Soit \( {f}_{n} \) le meilleur approximant de \( f \) , au sens de la norme \( \parallel \cdot \parallel \) , dans Vect \( \left( {{P}_{0},\ldots ,{P}_{n}}\right) \) . Montrer que \( f - {f}_{n} \) s’annule au moins en \( n + 1 \) points à l’intérieur de \( I \) .

> c) Let \( f \in \mathcal{C} \) and \( n \in \mathbb{N} \) . Let \( {f}_{n} \) be the best approximant of \( f \) , in the sense of the norm \( \parallel \cdot \parallel \) , in Vect \( \left( {{P}_{0},\ldots ,{P}_{n}}\right) \) . Show that \( f - {f}_{n} \) vanishes at least at \( n + 1 \) points inside \( I \) .

3/ (Quadrature de Gauss). Soit \( n \in {\mathbb{N}}^{ * } \) . On note \( {x}_{1} < \ldots < {x}_{n} \) les zéros de \( {P}_{n} \) . a) Montrer qu’il existe des nombres réels uniques \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) tels que

> 3/ (Gauss quadrature). Let \( n \in {\mathbb{N}}^{ * } \) . Let \( {x}_{1} < \ldots < {x}_{n} \) denote the zeros of \( {P}_{n} \) . a) Show that there exist unique real numbers \( {\lambda }_{1},\ldots ,{\lambda }_{n} \) such that

\[
\forall Q \in  \mathbb{R}\left\lbrack  X\right\rbrack  ,\deg \left( Q\right)  < {2n},\;{\int }_{I}Q\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}Q\left( {x}_{i}\right) .
\]

(**)

> Montrer \( {\lambda }_{i} > 0 \) pour tout \( i \) .

Show \( {\lambda }_{i} > 0 \) for all \( i \) .

> b) Montrer que

b) Show that

\[
\forall i,1 \leq  i \leq  n,\;{\lambda }_{i} =  - \frac{{\gamma }_{n + 1}}{{\gamma }_{n}}\frac{1}{{P}_{n + 1}\left( {x}_{i}\right) {P}_{n}^{\prime }\left( {x}_{i}\right) }.
\]

c) Montrer l’unicité des nombres réels \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) et \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n} \) vérifiant l’identité (**). d) Si \( I \) est un segment de \( \mathbb{R} \) , et \( f : I \rightarrow \mathbb{R} \) est de classe \( {\mathcal{C}}^{2n} \) , montrer que

> c) Show the uniqueness of the real numbers \( {\left( {x}_{i}\right) }_{1 \leq i \leq n} \) and \( {\left( {\lambda }_{i}\right) }_{1 \leq i \leq n} \) satisfying the identity (**). d) If \( I \) is a segment of \( \mathbb{R} \) , and \( f : I \rightarrow \mathbb{R} \) is of class \( {\mathcal{C}}^{2n} \) , show that

\[
\left| {{\int }_{I}f\left( x\right) w\left( x\right) {dx} - \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}f\left( {x}_{i}\right) }\right|  \leq  \frac{1}{{\gamma }_{n}^{2}}\frac{\mathop{\sup }\limits_{{x \in  I}}\left| {{f}^{\left( 2n\right) }\left( x\right) }\right| }{\left( {2n}\right) !}.
\]

(Indication : utiliser le résultat de l'exercice 7 page 70).

> (Hint: use the result of exercise 7 on page 70).

Solution. 1/a) Si \( f \in \mathcal{C} \) il est immédiat que \( {\lambda f} \in \mathcal{C} \) pour tout \( \lambda \in \mathbb{R} \) , et si \( f, g \in \mathcal{C} \) alors \( {\left( f + g\right) }^{2}w \) est intégrable puisque positive et majorée par \( \left\lbrack {{\left( f + g\right) }^{2} + {\left( f - g\right) }^{2}}\right\rbrack w = 2\left( {{f}^{2} + {g}^{2}}\right) w \) . Ainsi, \( \mathcal{C} \) est bien un espace vectoriel.

> Solution. 1/a) If \( f \in \mathcal{C} \) it is immediate that \( {\lambda f} \in \mathcal{C} \) for all \( \lambda \in \mathbb{R} \) , and if \( f, g \in \mathcal{C} \) then \( {\left( f + g\right) }^{2}w \) is integrable since it is positive and bounded by \( \left\lbrack {{\left( f + g\right) }^{2} + {\left( f - g\right) }^{2}}\right\rbrack w = 2\left( {{f}^{2} + {g}^{2}}\right) w \) . Thus, \( \mathcal{C} \) is indeed a vector space.

L’application \( \left( {f, g}\right) \mapsto \langle f, g\rangle \) est un produit scalaire : en effet, c’est une forme bilinéaire symétrique, elle est positive car \( w > 0 \) , et elle est bien définie car si \( {\int }_{I}{f}^{2}w = 0 \) , alors la fonction \( {f}^{2}w \) étant continue et positive, ceci entraîne \( {f}^{2}w = 0 \) donc \( f = 0 \) car \( w \) ne s’annule pas.

> The mapping \( \left( {f, g}\right) \mapsto \langle f, g\rangle \) is an inner product: indeed, it is a symmetric bilinear form, it is positive because \( w > 0 \) , and it is well-defined because if \( {\int }_{I}{f}^{2}w = 0 \) , then the function \( {f}^{2}w \) being continuous and positive, this implies \( {f}^{2}w = 0 \) therefore \( f = 0 \) because \( w \) does not vanish.

b) Il est immédiat que le procédé d'orthogonalisation de Schmidt s'étend à une famille dénom-brable de vecteurs. Ainsi,à partir de la base canonique \( {\left( {X}^{n}\right) }_{n \in \mathbb{N}} \) de \( \mathbb{R}\left\lbrack X\right\rbrack \) , on peut former une famille libre \( {\left( {P}_{n}\right) }_{n \in \mathbb{N}} \) orthogonale pour le produit scalaire \( \varphi \) telle que \( {P}_{0} = 1 \) et pour tout \( n \) , \( {P}_{n} = {X}^{n} + {r}_{n} \) avec \( {r}_{n} \in \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 1}}\right) \) . Une récurrence immédiate sur \( n \) montre alors que \( \deg \left( {P}_{n}\right) = n \) pour tout \( n \) . Par construction du procédé d’orthonormalisation de Schmidt, on a

> b) It is immediate that the Schmidt orthogonalization process extends to a countable family of vectors. Thus, starting from the canonical basis \( {\left( {X}^{n}\right) }_{n \in \mathbb{N}} \) of \( \mathbb{R}\left\lbrack X\right\rbrack \), one can form an orthogonal free family \( {\left( {P}_{n}\right) }_{n \in \mathbb{N}} \) for the scalar product \( \varphi \) such that \( {P}_{0} = 1 \) and for all \( n \), \( {P}_{n} = {X}^{n} + {r}_{n} \) with \( {r}_{n} \in \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 1}}\right) \). An immediate induction on \( n \) then shows that \( \deg \left( {P}_{n}\right) = n \) for all \( n \). By construction of the Schmidt orthonormalization process, we have

\[
\operatorname{Vect}\left( {1, X,\ldots ,{X}^{n}}\right)  = \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n}}\right)
\]

pour tout \( n \) , ce qui prouve que la famille libre orthogonale \( {\left( {P}_{n}\right) }_{n \in \mathbb{N}} \) est une base de \( \mathbb{R}\left\lbrack X\right\rbrack \) . En normant les polynômes \( {P}_{n} \) , on obtient alors une base orthonormale de \( \mathbb{R}\left\lbrack X\right\rbrack \) , et le coefficient dominant de \( {P}_{n} \) est bien positif.

> for all \( n \), which proves that the orthogonal free family \( {\left( {P}_{n}\right) }_{n \in \mathbb{N}} \) is a basis of \( \mathbb{R}\left\lbrack X\right\rbrack \). By normalizing the polynomials \( {P}_{n} \), we then obtain an orthonormal basis of \( \mathbb{R}\left\lbrack X\right\rbrack \), and the leading coefficient of \( {P}_{n} \) is indeed positive.

Une telle base est bien unique. En effet, supposons qu’une autre base \( \left( {Q}_{n}\right) \) vérifiant les mêmes propriétés diffère de \( \left( {P}_{n}\right) \) . Soit \( k \) le plus petit indice tel que \( {Q}_{k} \neq {P}_{k} \) . Comme deg \( {Q}_{k} = k \) on peut écrire \( {Q}_{k} = \mathop{\sum }\limits_{{i = 0}}^{k}{\lambda }_{i}{P}_{i} \) avec les \( {\lambda }_{i} \in \mathbb{R} \) . Lorsque \( 0 \leq i < k \) , on a \( {\lambda }_{i} = \left\langle {{Q}_{k},{P}_{i}}\right\rangle = \left\langle {{Q}_{k},{Q}_{i}}\right\rangle = 0 \) , donc \( {Q}_{k} = {\lambda }_{k}{P}_{k} \) . On a \( 1 = {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}^{2} = {\lambda }_{k}^{2}{\begin{Vmatrix}{P}_{k}\end{Vmatrix}}^{2} = {\lambda }_{k}^{2} \) , donc \( {\lambda }_{k} = 1 \) ou \( {\lambda }_{k} = - 1 \) . Comme les coefficients dominants de \( {P}_{k} \) et \( {Q}_{k} \) sont strictement positifs, on a forcément \( {\lambda }_{k} = 1 \) , donc \( {P}_{k} = {Q}_{k} \) ce qui est absurde.

> Such a basis is indeed unique. Indeed, suppose that another basis \( \left( {Q}_{n}\right) \) satisfying the same properties differs from \( \left( {P}_{n}\right) \). Let \( k \) be the smallest index such that \( {Q}_{k} \neq {P}_{k} \). Since deg \( {Q}_{k} = k \) we can write \( {Q}_{k} = \mathop{\sum }\limits_{{i = 0}}^{k}{\lambda }_{i}{P}_{i} \) with the \( {\lambda }_{i} \in \mathbb{R} \). When \( 0 \leq i < k \), we have \( {\lambda }_{i} = \left\langle {{Q}_{k},{P}_{i}}\right\rangle = \left\langle {{Q}_{k},{Q}_{i}}\right\rangle = 0 \), therefore \( {Q}_{k} = {\lambda }_{k}{P}_{k} \). We have \( 1 = {\begin{Vmatrix}{Q}_{k}\end{Vmatrix}}^{2} = {\lambda }_{k}^{2}{\begin{Vmatrix}{P}_{k}\end{Vmatrix}}^{2} = {\lambda }_{k}^{2} \), therefore \( {\lambda }_{k} = 1 \) or \( {\lambda }_{k} = - 1 \). Since the leading coefficients of \( {P}_{k} \) and \( {Q}_{k} \) are strictly positive, we necessarily have \( {\lambda }_{k} = 1 \), therefore \( {P}_{k} = {Q}_{k} \) which is absurd.

c) Supposons la relation (*) vérifiée. En la projetant sur les vecteurs \( {P}_{n},{P}_{n - 1} \) et \( {P}_{n - 2} \) on obtient

> c) Suppose the relation (*) is satisfied. By projecting it onto the vectors \( {P}_{n},{P}_{n - 1} \) and \( {P}_{n - 2} \) we obtain

\[
1 = {a}_{n}\left\langle  {X{P}_{n - 1},{P}_{n}}\right\rangle  ,\;0 = {a}_{n}\left\langle  {X{P}_{n - 1},{P}_{n - 1}}\right\rangle   + {b}_{n}\;0 = {a}_{n}\left\langle  {X{P}_{n - 1},{P}_{n - 2}}\right\rangle   + {c}_{n}.\;\left( {* *  * }\right)
\]

(***)

> Montrons que \( \left\langle {X{P}_{n - 1},{P}_{n}}\right\rangle \) est non nul en explicitant sa valeur. Comme \( X{P}_{n - 1} \) est de degré \( n \) , il existe des réels \( {\lambda }_{k} \) tels que

Let us show that \( \left\langle {X{P}_{n - 1},{P}_{n}}\right\rangle \) is non-zero by making its value explicit. Since \( X{P}_{n - 1} \) is of degree \( n \), there exist real numbers \( {\lambda }_{k} \) such that

\[
X{P}_{n - 1} = \mathop{\sum }\limits_{{k = 0}}^{n}{\lambda }_{k}{P}_{k}
\]

ce qui entraîne \( \left\langle {X{P}_{n - 1},{P}_{n}}\right\rangle = {\lambda }_{n} \) , et l’égalité des coefficients dominants donne \( {\gamma }_{n - 1} = {\lambda }_{n}{\gamma }_{n} \) donc finalement \( \left\langle {X{P}_{n - 1},{P}_{n}}\right\rangle = {\gamma }_{n - 1}/{\gamma }_{n} \) . De même, on a

> which leads to \( \left\langle {X{P}_{n - 1},{P}_{n}}\right\rangle = {\lambda }_{n} \) , and the equality of the leading coefficients gives \( {\gamma }_{n - 1} = {\lambda }_{n}{\gamma }_{n} \) so finally \( \left\langle {X{P}_{n - 1},{P}_{n}}\right\rangle = {\gamma }_{n - 1}/{\gamma }_{n} \) . Similarly, we have

\[
\left\langle  {X{P}_{n - 1},{P}_{n - 2}}\right\rangle   = {\int }_{I}{P}_{n - 1}\left( x\right) x{P}_{n - 2}\left( x\right) w\left( x\right) {dx} = \left\langle  {{P}_{n - 1}, X{P}_{n - 2}}\right\rangle   = \left\langle  {X{P}_{n - 2},{P}_{n - 1}}\right\rangle   = \frac{{\gamma }_{n - 2}}{{\gamma }_{n - 1}}.
\]

Finalement, les trois égalités (***) sont équivalentes à

> Finally, the three equalities (***) are equivalent to

\[
{a}_{n} = \frac{{\gamma }_{n}}{{\gamma }_{n - 1}},\;{b}_{n} =  - \frac{{\gamma }_{n}\left\langle  {X{P}_{n - 1},{P}_{n - 1}}\right\rangle  }{{\gamma }_{n - 1}},\;{c}_{n} =  - \frac{{\gamma }_{n}{\gamma }_{n - 2}}{{\gamma }_{n - 1}^{2}}.
\]

Réciproquement, le choix de ces valeurs entraîne que la projection de (*) le long des vecteurs \( {P}_{n},{P}_{n - 1} \) et \( {P}_{n - 2} \) est vérifiée. Les deux termes de (*) sont également égaux le long des vecteurs \( {P}_{k} \) pour \( k < n - 2 \) car \( \left\langle {X{P}_{n - 1},{P}_{k}}\right\rangle = \left\langle {{P}_{n - 1}, X{P}_{k}}\right\rangle = 0 \) vu que \( \deg \left( {X{P}_{k}}\right) < n - 1 \) donc \( X{P}_{k} \in \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 2}}\right) \) . Ainsi, nous avons démontré que le choix des valeurs \( {a}_{n},{b}_{n} \) et \( {c}_{n} \) entraîne que (*) est vrai le long de chaque vecteur \( {P}_{k} \) pour \( k \leq n \) , et comme les polynômes de \( \left( *\right) \) sont de degré \( \leq n \) , cela montre que \( \left( *\right) \) est bien vérifié.

> Conversely, the choice of these values implies that the projection of (*) along the vectors \( {P}_{n},{P}_{n - 1} \) and \( {P}_{n - 2} \) is satisfied. Both terms of (*) are also equal along the vectors \( {P}_{k} \) for \( k < n - 2 \) because \( \left\langle {X{P}_{n - 1},{P}_{k}}\right\rangle = \left\langle {{P}_{n - 1}, X{P}_{k}}\right\rangle = 0 \) given that \( \deg \left( {X{P}_{k}}\right) < n - 1 \) so \( X{P}_{k} \in \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 2}}\right) \) . Thus, we have shown that the choice of values \( {a}_{n},{b}_{n} \) and \( {c}_{n} \) implies that (*) is true along each vector \( {P}_{k} \) for \( k \leq n \) , and since the polynomials of \( \left( *\right) \) are of degree \( \leq n \) , this shows that \( \left( *\right) \) is indeed satisfied.

d) On procède par récurrence sur \( n \) . Pour \( n = 0 \) la relation est vraie car

> d) We proceed by induction on \( n \) . For \( n = 0 \) the relation is true because

\[
\frac{{\gamma }_{0}}{{\gamma }_{1}} \cdot  \frac{{P}_{1}\left( x\right) {P}_{0}\left( y\right)  - {P}_{1}\left( y\right) {P}_{0}\left( x\right) }{x - y} = \frac{{\gamma }_{0}}{{\gamma }_{1}} \cdot  \frac{{\gamma }_{0}\left( {{P}_{1}\left( x\right)  - {P}_{1}\left( y\right) }\right) }{x - y} = \frac{{\gamma }_{0}}{{\gamma }_{1}}{\gamma }_{0}{\gamma }_{1} = {\gamma }_{0}^{2} = {P}_{0}\left( x\right) {P}_{0}\left( y\right) .
\]

Supposons maintenant la formule de Darboux vraie au rang \( n - 1 \) et montrons la au rang \( n \) . En remplaçant les expressions de \( {P}_{n + 1}\left( x\right) \) et \( {P}_{n + 1}\left( y\right) \) par la formule obtenue dans la question précédente, on obtient

> Now assume the Darboux formula is true at rank \( n - 1 \) and show it at rank \( n \) . By replacing the expressions of \( {P}_{n + 1}\left( x\right) \) and \( {P}_{n + 1}\left( y\right) \) with the formula obtained in the previous question, we obtain

\[
\frac{{P}_{n + 1}\left( x\right) {P}_{n}\left( y\right)  - {P}_{n}\left( x\right) {P}_{n + 1}\left( y\right) }{x - y} = {a}_{n + 1}{P}_{n}\left( x\right) {P}_{n}\left( y\right)  + {c}_{n + 1}\frac{{P}_{n - 1}\left( x\right) {P}_{n}\left( y\right)  - {P}_{n}\left( x\right) {P}_{n - 1}\left( y\right) }{x - y},
\]

ce qui compte tenu des valeurs de \( {a}_{n + 1} \) et \( {c}_{n + 1} \) obtenues précédemment entraîne

> which, taking into account the values of \( {a}_{n + 1} \) and \( {c}_{n + 1} \) obtained previously, leads to

\[
\frac{{\gamma }_{n}}{{\gamma }_{n + 1}}\frac{{P}_{n + 1}\left( x\right) {P}_{n}\left( y\right)  - {P}_{n}\left( x\right) {P}_{n + 1}\left( y\right) }{x - y} = {P}_{n}\left( x\right) {P}_{n}\left( y\right)  + \frac{{\gamma }_{n - 1}}{{\gamma }_{n}}\frac{{P}_{n}\left( x\right) {P}_{n - 1}\left( y\right)  - {P}_{n - 1}\left( x\right) {P}_{n}\left( y\right) }{x - y}.
\]

Compte tenu de l'hypothèse de récurrence, ceci démontre bien la formule de Darboux lorsque \( x \neq y \) .

> Given the induction hypothesis, this indeed proves the Darboux formula when \( x \neq y \) .

Pour calculer \( {K}_{n}\left( {x, x}\right) \) on calcule la limite de \( {K}_{n}\left( {x, x + h}\right) \) lorsque \( h \neq 0 \) tend vers 0 . En substituant \( {P}_{n}\left( {x + h}\right) \) et \( {P}_{n + 1}\left( {x + h}\right) \) par leur développement limité à l’ordre 1 dans la formule précédente appliquée à \( y = x + h \) , on obtient

> To calculate \( {K}_{n}\left( {x, x}\right) \) we calculate the limit of \( {K}_{n}\left( {x, x + h}\right) \) as \( h \neq 0 \) approaches 0 . By substituting \( {P}_{n}\left( {x + h}\right) \) and \( {P}_{n + 1}\left( {x + h}\right) \) with their Taylor expansion to order 1 in the previous formula applied to \( y = x + h \) , we obtain

\[
{K}_{n}\left( {x, x + h}\right)  = \frac{{\gamma }_{n}}{{\gamma }_{n + 1}}\frac{{P}_{n + 1}\left( x\right) \left( {{P}_{n}\left( x\right)  + h{P}_{n}^{\prime }\left( x\right)  + o\left( h\right) }\right)  - \left( {{P}_{n + 1}\left( x\right)  + h{P}_{n + 1}^{\prime }\left( x\right)  + o\left( h\right) }\right) {P}_{n}\left( x\right) }{\left( -h\right) }
\]

ce qui en faisant tendre \( h \) vers 0 donne

> which, by letting \( h \) approach 0 , gives

\[
{K}_{n}\left( {x, x}\right)  = \frac{{\gamma }_{n}}{{\gamma }_{n + 1}}\left( {{P}_{n + 1}^{\prime }\left( x\right) {P}_{n}\left( x\right)  - {P}_{n}^{\prime }\left( x\right) {P}_{n + 1}\left( x\right) }\right) .
\]

2/a) Fixons \( n \in {\mathbb{N}}^{ * } \) et notons \( k \in \mathbb{N} \) le nombre de zéros de \( {P}_{n} \) dans \( I \) d’ordre de multiplicité impaire. Si on note \( {\alpha }_{1},\cdots ,{\alpha }_{k} \) ces zéros et \( Q = \left( {X - {\alpha }_{1}}\right) \cdots \left( {X - {\alpha }_{k}}\right) \) (avec \( Q = 1 \) si \( k = 0 \) ), le polynôme \( {P}_{n}Q \) garde un signe constant sur \( I \) .

> 2/a) Let us fix \( n \in {\mathbb{N}}^{ * } \) and denote by \( k \in \mathbb{N} \) the number of zeros of \( {P}_{n} \) in \( I \) of odd multiplicity. If we denote these zeros by \( {\alpha }_{1},\cdots ,{\alpha }_{k} \) and \( Q = \left( {X - {\alpha }_{1}}\right) \cdots \left( {X - {\alpha }_{k}}\right) \) (with \( Q = 1 \) if \( k = 0 \) ), the polynomial \( {P}_{n}Q \) maintains a constant sign on \( I \) .

Supposons \( k \leq n - 1 \) . Alors \( Q \in \operatorname{Vect}\left( {1, X,\ldots ,{X}^{n - 1}}\right) = \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 1}}\right) \) . De plus pour tout \( k \leq n - 1,\left\langle {{P}_{n},{P}_{k}}\right\rangle = 0 \) . On en conclut \( \left\langle {{P}_{n}, Q}\right\rangle = 0 = {\int }_{I}{P}_{n}\left( t\right) Q\left( t\right) w\left( t\right) {dt} \) . Or la fonction \( t \mapsto {P}_{n}\left( t\right) Q\left( t\right) w\left( t\right) \) est continue et garde un signe constant sur \( I \) , donc \( {P}_{n}{Qw} = 0 \) , et comme \( w > 0 \) , ceci entraîne \( {P}_{n}Q = 0 \) sur \( I \) , ce qui est impossible vu que \( {P}_{n}Q \) est un polynôme non nul.

> Suppose \( k \leq n - 1 \) . Then \( Q \in \operatorname{Vect}\left( {1, X,\ldots ,{X}^{n - 1}}\right) = \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 1}}\right) \) . Furthermore, for all \( k \leq n - 1,\left\langle {{P}_{n},{P}_{k}}\right\rangle = 0 \) . We conclude \( \left\langle {{P}_{n}, Q}\right\rangle = 0 = {\int }_{I}{P}_{n}\left( t\right) Q\left( t\right) w\left( t\right) {dt} \) . However, the function \( t \mapsto {P}_{n}\left( t\right) Q\left( t\right) w\left( t\right) \) is continuous and maintains a constant sign on \( I \) , so \( {P}_{n}{Qw} = 0 \) , and since \( w > 0 \) , this implies \( {P}_{n}Q = 0 \) on \( I \) , which is impossible given that \( {P}_{n}Q \) is a non-zero polynomial.

Donc \( k \geq n \) , et comme \( \deg \left( {P}_{n}\right) = n,{P}_{n} \) a \( n \) racines distinctes dans \( I \) .

> Therefore \( k \geq n \) , and since \( \deg \left( {P}_{n}\right) = n,{P}_{n} \) has \( n \) distinct roots in \( I \) .

b) La formule obtenue précédemment pour \( {K}_{n}\left( {x, x}\right) \) montre que pour tout zéro \( \alpha \) de \( {P}_{n + 1} \) , on a

> b) The formula obtained previously for \( {K}_{n}\left( {x, x}\right) \) shows that for any zero \( \alpha \) of \( {P}_{n + 1} \) , we have

\[
{P}_{n + 1}^{\prime }\left( \alpha \right) {P}_{n}\left( \alpha \right)  = {P}_{n + 1}^{\prime }\left( \alpha \right) {P}_{n}\left( \alpha \right)  - {P}_{n}^{\prime }\left( \alpha \right) {P}_{n + 1}\left( \alpha \right)  = \frac{{\gamma }_{n + 1}}{{\gamma }_{n}}\mathop{\sum }\limits_{{i = 0}}^{n}{P}_{i}{\left( \alpha \right) }^{2} \geq  \frac{{\gamma }_{n + 1}}{{\gamma }_{n}}{P}_{0}{\left( \alpha \right) }^{2} > 0.
\]

Maintenant considérons deux zéros consécutifs \( \alpha \) et \( \beta \) de \( {P}_{n + 1} \) . La fonction \( {P}_{n + 1} \) garde un signe constant sur \( \left\lbrack {\alpha ,\beta }\right\rbrack \) , par exemple positif. Comme \( {P}_{n + 1}\left( \alpha \right) = 0 \) on en déduit \( {P}_{n + 1}^{\prime }\left( \alpha \right) \geq 0 \) , de même on obtient \( {P}_{n + 1}^{\prime }\left( \beta \right) \leq 0 \) . Compte tenu de l’inégalité \( {P}_{n + 1}^{\prime }\left( \alpha \right) {P}_{n}\left( \alpha \right) > 0 \) , on en déduit \( {P}_{n}\left( \alpha \right) > 0 \) . De même, l’inégalité \( {P}_{n + 1}^{\prime }\left( \beta \right) {P}_{n}\left( \beta \right) > 0 \) entraîne \( {P}_{n}\left( \beta \right) < 0 \) . Ainsi \( {P}_{n} \) change de signe dans \( \rbrack \alpha ,\beta \lbrack \) donc contient au moins un zéro dans cet intervalle. Comme \( {P}_{n + 1} \) a \( n + 1 \) zéros dans \( I,{P}_{n} \) a un zéro dans chacun des \( n \) intervalles délimités par deux zéros consécutifs de \( {P}_{n} \) . Or \( {P}_{n} \) a \( n \) zéros donc il n’y en a qu’un seul entre deux zéros consécutifs de \( {P}_{n + 1} \) . c) La propriété de projection sur un s.e.v de dimension finie (voir la proposition 2 page 254) assure que \( {f}_{n} \) est la projection orthogonale de \( f \) sur \( \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n}}\right) = \operatorname{Vect}\left( {1,\ldots ,{X}^{n}}\right) \) . Donc \( f - {f}_{n} \) est orthogonal à ce sous espace, c’est-à-dire \( \langle f - {f}_{n}, Q\rangle = 0 \) pour tout polynôme \( Q \) de degré \( \leq n \) . On procède ensuite de manière analogue à la solution de la question 2/a), (sauf qu'ici, on ne peut pas utiliser la notion de zéro de multiplicité impaire). Raisonnons par l'absurde et supposons que \( f - {f}_{n} \) ne s’annule qu’en \( k \) points \( {x}_{1} < \ldots < {x}_{k} \) de l’intérieur de \( I \) , avec \( k \leq n \) . Par commodité, notons \( {x}_{0} \) et \( {x}_{k + 1} \) les extrémités de l’intervalle \( I \) . Sur chaque intervalle \( \rbrack {x}_{j},{x}_{j + 1}\left\lbrack \right. \) la fonction continue \( f - {f}_{n} \) ne s’annule pas donc garde un signe constant. Notons \( 1 \leq {j}_{1} < \ldots < {j}_{\ell } \leq k \) les indices \( j \) pour lesquels \( f - {f}_{n} \) change de signe entre \( \rbrack {x}_{j - 1},{x}_{j}\left\lbrack \text{ et }\right\rbrack {x}_{j},{x}_{j + 1}\lbrack \) . La fonction \( f - {f}_{n} \) garde un signe constant sur chacun des intervalles \( \rbrack {x}_{0},{x}_{{j}_{1}}\left\lbrack ,\right\rbrack {x}_{{j}_{1}},{x}_{{j}_{2}}\left\lbrack {,\ldots ,}\right\rbrack {x}_{{j}_{\ell }},{x}_{k + 1}\left\lbrack \text{ et change de signe }\right\rbrack \) à chaque \( {x}_{{j}_{m}} \) . Ainsi, le polynôme défini par \( Q = \mathop{\prod }\limits_{{m = 1}}^{\ell }\left( {X - {x}_{{j}_{m}}}\right) \) (ou \( Q = 1 \) si \( \ell = 0 \) ) est tel que \( \left( {f - {f}_{n}}\right) Q \) garde un signe constant sur \( I \) tout entier. Donc la fonction continue \( \left( {f - {f}_{n}}\right) {Qw} \) garde également un signe constant sur \( I \) , et comme \( \deg \left( Q\right) \leq n \) on a \( \left\langle {f - {f}_{n}, Q}\right\rangle = {\int }_{I}\left( {f - {f}_{n}}\right) {Qw} = 0 \) donc \( \left( {f - {f}_{n}}\right) {Qw} = 0 \) , donc \( \left( {f - {f}_{n}}\right) Q = 0 \) . Ceci entraîne que \( f - {f}_{n} \) s’annule sauf éventuellement aux zéros de \( Q \) , et par continuité \( f - {f}_{n} = 0 \) sur \( I \) tout entier. Ceci est absurde car on a supposé que \( f - {f}_{n} \) ne s’annulait qu’en un nombre fini de points. Donc \( f - {f}_{n} \) s’annule bien en au moins \( n + 1 \) points de l’intérieur de \( I \) .

> Now consider two consecutive zeros \( \alpha \) and \( \beta \) of \( {P}_{n + 1} \). The function \( {P}_{n + 1} \) maintains a constant sign on \( \left\lbrack {\alpha ,\beta }\right\rbrack \), for example positive. As \( {P}_{n + 1}\left( \alpha \right) = 0 \), we deduce \( {P}_{n + 1}^{\prime }\left( \alpha \right) \geq 0 \); similarly, we obtain \( {P}_{n + 1}^{\prime }\left( \beta \right) \leq 0 \). Given the inequality \( {P}_{n + 1}^{\prime }\left( \alpha \right) {P}_{n}\left( \alpha \right) > 0 \), we deduce \( {P}_{n}\left( \alpha \right) > 0 \). Likewise, the inequality \( {P}_{n + 1}^{\prime }\left( \beta \right) {P}_{n}\left( \beta \right) > 0 \) leads to \( {P}_{n}\left( \beta \right) < 0 \). Thus, \( {P}_{n} \) changes sign in \( \rbrack \alpha ,\beta \lbrack \), therefore it contains at least one zero in this interval. Since \( {P}_{n + 1} \) has \( n + 1 \) zeros in \( I,{P}_{n} \), it has a zero in each of the \( n \) intervals delimited by two consecutive zeros of \( {P}_{n} \). However, \( {P}_{n} \) has \( n \) zeros, so there is only one between two consecutive zeros of \( {P}_{n + 1} \). c) The projection property onto a finite-dimensional subspace (see proposition 2, page 254) ensures that \( {f}_{n} \) is the orthogonal projection of \( f \) onto \( \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n}}\right) = \operatorname{Vect}\left( {1,\ldots ,{X}^{n}}\right) \). Therefore, \( f - {f}_{n} \) is orthogonal to this subspace, that is to say \( \langle f - {f}_{n}, Q\rangle = 0 \) for any polynomial \( Q \) of degree \( \leq n \). We then proceed analogously to the solution of question 2/a), (except that here, we cannot use the notion of a zero of odd multiplicity). Let us reason by contradiction and assume that \( f - {f}_{n} \) only vanishes at \( k \) points \( {x}_{1} < \ldots < {x}_{k} \) in the interior of \( I \), with \( k \leq n \). For convenience, let us denote \( {x}_{0} \) and \( {x}_{k + 1} \) as the endpoints of the interval \( I \). On each interval \( \rbrack {x}_{j},{x}_{j + 1}\left\lbrack \right. \), the continuous function \( f - {f}_{n} \) does not vanish and therefore maintains a constant sign. Let \( 1 \leq {j}_{1} < \ldots < {j}_{\ell } \leq k \) be the indices \( j \) for which \( f - {f}_{n} \) changes sign between \( \rbrack {x}_{j - 1},{x}_{j}\left\lbrack \text{ et }\right\rbrack {x}_{j},{x}_{j + 1}\lbrack \). The function \( f - {f}_{n} \) maintains a constant sign on each of the intervals \( \rbrack {x}_{0},{x}_{{j}_{1}}\left\lbrack ,\right\rbrack {x}_{{j}_{1}},{x}_{{j}_{2}}\left\lbrack {,\ldots ,}\right\rbrack {x}_{{j}_{\ell }},{x}_{k + 1}\left\lbrack \text{ et change de signe }\right\rbrack \) for each \( {x}_{{j}_{m}} \). Thus, the polynomial defined by \( Q = \mathop{\prod }\limits_{{m = 1}}^{\ell }\left( {X - {x}_{{j}_{m}}}\right) \) (or \( Q = 1 \) if \( \ell = 0 \)) is such that \( \left( {f - {f}_{n}}\right) Q \) maintains a constant sign on the entirety of \( I \). Therefore, the continuous function \( \left( {f - {f}_{n}}\right) {Qw} \) also maintains a constant sign on \( I \), and since \( \deg \left( Q\right) \leq n \), we have \( \left\langle {f - {f}_{n}, Q}\right\rangle = {\int }_{I}\left( {f - {f}_{n}}\right) {Qw} = 0 \), thus \( \left( {f - {f}_{n}}\right) {Qw} = 0 \), therefore \( \left( {f - {f}_{n}}\right) Q = 0 \). This implies that \( f - {f}_{n} \) vanishes except possibly at the zeros of \( Q \), and by continuity \( f - {f}_{n} = 0 \) on the entirety of \( I \). This is absurd because we assumed that \( f - {f}_{n} \) only vanished at a finite number of points. Therefore, \( f - {f}_{n} \) indeed vanishes at at least \( n + 1 \) points in the interior of \( I \).

3/a) Montrons l’existence des \( \left( {\lambda }_{i}\right) \) . Notons \( {L}_{i} \) le polynôme de Lagrange de degré \( < n \) qui vérifie \( {L}_{i}\left( {x}_{i}\right) = 1 \) et \( {L}_{i}\left( {x}_{j}\right) = 0 \) pour \( j \neq i \) . Soit \( Q \in \mathbb{R}\left\lbrack X\right\rbrack ,\deg \left( Q\right) < {2n} \) , et considérons le polynôme d’interpolation de Lagrange \( L\left( X\right) = \mathop{\sum }\limits_{{i = 1}}^{n}Q\left( {x}_{i}\right) {L}_{i}\left( X\right) \) qui vérifie \( Q\left( {x}_{i}\right) = L\left( {x}_{i}\right) \) pour tout \( i \) . Le polynôme \( Q - L \) s’annule aux points \( {x}_{i} \) , donc il existe un polynôme \( R \) tel que \( Q - L = {P}_{n}R \) . On a \( \deg \left( R\right) = \deg Q - \deg {P}_{n} < n \) , donc \( \left\langle {{P}_{n}, R}\right\rangle = 0 \) , donc \( {\int }_{I}\left( {Q - L}\right) \left( x\right) w\left( x\right) {dx} = 0 \) . On en déduit

> 3/a) Let us show the existence of \( \left( {\lambda }_{i}\right) \) . Let \( {L}_{i} \) be the Lagrange polynomial of degree \( < n \) which satisfies \( {L}_{i}\left( {x}_{i}\right) = 1 \) and \( {L}_{i}\left( {x}_{j}\right) = 0 \) for \( j \neq i \) . Let \( Q \in \mathbb{R}\left\lbrack X\right\rbrack ,\deg \left( Q\right) < {2n} \) , and consider the Lagrange interpolation polynomial \( L\left( X\right) = \mathop{\sum }\limits_{{i = 1}}^{n}Q\left( {x}_{i}\right) {L}_{i}\left( X\right) \) which satisfies \( Q\left( {x}_{i}\right) = L\left( {x}_{i}\right) \) for all \( i \) . The polynomial \( Q - L \) vanishes at points \( {x}_{i} \) , so there exists a polynomial \( R \) such that \( Q - L = {P}_{n}R \) . We have \( \deg \left( R\right) = \deg Q - \deg {P}_{n} < n \) , so \( \left\langle {{P}_{n}, R}\right\rangle = 0 \) , so \( {\int }_{I}\left( {Q - L}\right) \left( x\right) w\left( x\right) {dx} = 0 \) . We deduce

\[
{\int }_{I}Q\left( x\right) w\left( x\right) {dx} = {\int }_{I}L\left( x\right) w\left( x\right) {dx} = {\int }_{I}\left( {\mathop{\sum }\limits_{{i = 1}}^{n}Q\left( {x}_{i}\right) {L}_{i}\left( x\right) }\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}Q\left( {x}_{i}\right)
\]

avec \( {\lambda }_{i} = {\int }_{I}{L}_{i}\left( x\right) w\left( x\right) {dx} \) . Les \( {\lambda }_{i} \) sont bien uniques, car l’expression (**) appliquée au polynôme de Lagrange \( {L}_{i} \) montre qu’on a forcément \( {\lambda }_{i} = {\int }_{I}{L}_{i}\left( x\right) w\left( x\right) {dx} \) . Enfin, l’expression (**) appliquée à \( Q = {L}_{i}^{2} \) (dont le degré est \( \leq {2n} - 2 \) ) entraîne \( 0 < {\int }_{I}{L}_{i}{\left( x\right) }^{2}w\left( x\right) {dx} = {\lambda }_{i} \) .

> with \( {\lambda }_{i} = {\int }_{I}{L}_{i}\left( x\right) w\left( x\right) {dx} \) . The \( {\lambda }_{i} \) are indeed unique, because expression (**) applied to the Lagrange polynomial \( {L}_{i} \) shows that we necessarily have \( {\lambda }_{i} = {\int }_{I}{L}_{i}\left( x\right) w\left( x\right) {dx} \) . Finally, expression (**) applied to \( Q = {L}_{i}^{2} \) (whose degree is \( \leq {2n} - 2 \) ) leads to \( 0 < {\int }_{I}{L}_{i}{\left( x\right) }^{2}w\left( x\right) {dx} = {\lambda }_{i} \) .

b) L’idée est de calculer de deux manières différentes l’expression \( {\int }_{I}{K}_{n}\left( {x,{x}_{i}}\right) {L}_{i}\left( x\right) w\left( x\right) {dx} \) . Comme \( \deg \left( {{K}_{n}\left( {X,{x}_{i}}\right) {L}_{i}\left( X\right) }\right) < {2n} \) , on peut appliquer l’expression \( \left( {* * }\right) \) ce qui donne

> b) The idea is to calculate the expression \( {\int }_{I}{K}_{n}\left( {x,{x}_{i}}\right) {L}_{i}\left( x\right) w\left( x\right) {dx} \) in two different ways. Since \( \deg \left( {{K}_{n}\left( {X,{x}_{i}}\right) {L}_{i}\left( X\right) }\right) < {2n} \) , we can apply expression \( \left( {* * }\right) \) which gives

\[
{\int }_{I}{K}_{n}\left( {x,{x}_{i}}\right) {L}_{i}\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{j = 1}}^{n}{\lambda }_{j}{K}_{n}\left( {{x}_{j},{x}_{i}}\right) {L}_{i}\left( {x}_{j}\right)  = {\lambda }_{i}{K}_{n}\left( {{x}_{i},{x}_{i}}\right) .
\]

(***

> En utilisant maintenant l’expression du noyau \( {K}_{n} \) , on obtient

By now using the expression of the kernel \( {K}_{n} \) , we obtain

\[
{\int }_{I}{K}_{n}\left( {x,{x}_{i}}\right) {L}_{i}\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{j = 0}}^{n}{P}_{j}\left( {x}_{i}\right) {\int }_{I}{P}_{j}\left( x\right) {L}_{i}\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{j = 0}}^{n}{P}_{j}\left( {x}_{i}\right) \left\langle  {{P}_{j},{L}_{i}}\right\rangle  .
\]

Par ailleurs, \( \deg \left( {L}_{i}\right) < n \) donc \( {L}_{i} \in \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 1}}\right) \) donc on peut écrire \( {L}_{i} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{\mu }_{k}{P}_{k} \) avec les \( {\mu }_{k} \in \mathbb{R} \) , dont l’expression précédente entraîne

> Furthermore, \( \deg \left( {L}_{i}\right) < n \) so \( {L}_{i} \in \operatorname{Vect}\left( {{P}_{0},\ldots ,{P}_{n - 1}}\right) \) so we can write \( {L}_{i} = \mathop{\sum }\limits_{{k = 0}}^{{n - 1}}{\mu }_{k}{P}_{k} \) with the \( {\mu }_{k} \in \mathbb{R} \) , whose previous expression leads to

\[
{\int }_{I}{K}_{n}\left( {x,{x}_{i}}\right) {L}_{i}\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{j = 0}}^{n}{P}_{j}\left( {x}_{i}\right) \mathop{\sum }\limits_{{k = 0}}^{n}{\mu }_{k}\left\langle  {{P}_{j},{P}_{k}}\right\rangle   = \mathop{\sum }\limits_{{j = 0}}^{n}{P}_{j}\left( {x}_{i}\right) {\mu }_{j} = {L}_{i}\left( {x}_{i}\right)  = 1.
\]

Avec (****), on en déduit \( {\lambda }_{i} = 1/{K}_{n}\left( {{x}_{i},{x}_{i}}\right) \) , d’où le résultat souhaité grâce à l’expression obtenue dans \( 1/\mathrm{d}) \) pour \( {K}_{n}\left( {x, x}\right) \) .

> With (****), we deduce \( {\lambda }_{i} = 1/{K}_{n}\left( {{x}_{i},{x}_{i}}\right) \) , hence the desired result thanks to the expression obtained in \( 1/\mathrm{d}) \) for \( {K}_{n}\left( {x, x}\right) \) .

c) Supposons l’identité (**) vraie pour des nombres \( \left( {x}_{i}\right) \) et \( \left( {\lambda }_{i}\right) \) , avec \( {x}_{1} < \ldots < {x}_{n} \) . Alors le polynôme \( Q = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {x}_{i}}\right) \) vérifie

> c) Suppose the identity (**) is true for numbers \( \left( {x}_{i}\right) \) and \( \left( {\lambda }_{i}\right) \), with \( {x}_{1} < \ldots < {x}_{n} \). Then the polynomial \( Q = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {x}_{i}}\right) \) satisfies

\[
\forall P \in  \mathbb{R}\left\lbrack  X\right\rbrack  ,\deg \left( P\right)  < n,\;{\int }_{I}Q\left( x\right) P\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}Q\left( {x}_{i}\right) P\left( {x}_{i}\right)  = 0
\]

autrement dit on a \( \langle Q, P\rangle = 0 \) pour tout polynôme \( P \) de degré \( < n \) . Donc \( Q = \mathop{\sum }\limits_{{i = 0}}^{n}\left\langle {Q,{P}_{i}}\right\rangle {P}_{i} = \; \left\langle {Q,{P}_{n}}\right\rangle {P}_{n} \) , autrement dit \( Q \) et \( {P}_{n} \) sont proportionnels, ce qui entraîne que les \( \left( {x}_{i}\right) \) sont les racines de \( {P}_{n} \) , et sont donc uniques. Nous avons déjà vu qu’alors les \( \left( {\lambda }_{i}\right) \) étaient uniques, d’où le résultat.

> in other words, we have \( \langle Q, P\rangle = 0 \) for every polynomial \( P \) of degree \( < n \). Thus \( Q = \mathop{\sum }\limits_{{i = 0}}^{n}\left\langle {Q,{P}_{i}}\right\rangle {P}_{i} = \; \left\langle {Q,{P}_{n}}\right\rangle {P}_{n} \), in other words \( Q \) and \( {P}_{n} \) are proportional, which implies that the \( \left( {x}_{i}\right) \) are the roots of \( {P}_{n} \), and are therefore unique. We have already seen that in this case the \( \left( {\lambda }_{i}\right) \) were unique, hence the result.

d) Soit \( P \) le polynôme d’interpolation de Hermite, \( \deg \left( P\right) < {2n} \) , tel que \( P\left( {x}_{i}\right) = f\left( {x}_{i}\right) \) et \( {P}^{\prime }\left( {x}_{i}\right) = {f}^{\prime }\left( {x}_{i}\right) \) pour tout \( i \) . D’après l’exercice 7 page 70, on a

> d) Let \( P \) be the Hermite interpolation polynomial, \( \deg \left( P\right) < {2n} \), such that \( P\left( {x}_{i}\right) = f\left( {x}_{i}\right) \) and \( {P}^{\prime }\left( {x}_{i}\right) = {f}^{\prime }\left( {x}_{i}\right) \) for all \( i \). According to exercise 7 on page 70, we have

\[
\forall x \in  I,\;\left| {f\left( x\right)  - P\left( x\right) }\right|  \leq  M\mathop{\prod }\limits_{{i = 1}}^{n}{\left( x - {x}_{i}\right) }^{2}\;\text{ avec }\;M = \frac{\mathop{\sup }\limits_{{t \in  I}}\left| {{f}^{\left( 2n\right) }\left( t\right) }\right| }{\left( {2n}\right) !}.
\]

Comme \( {P}_{n}\left( x\right) = {\gamma }_{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {x - {x}_{i}}\right) \) on en déduit, par intégration

> Since \( {P}_{n}\left( x\right) = {\gamma }_{n}\mathop{\prod }\limits_{{i = 1}}^{n}\left( {x - {x}_{i}}\right) \), we deduce by integration

\[
{\int }_{I}\left| {f\left( x\right)  - P\left( x\right) }\right| w\left( x\right) {dx} \leq  {\int }_{I}M\frac{{P}_{n}^{2}\left( x\right) }{{\gamma }_{n}^{2}}w\left( x\right) {dx} = \frac{M}{{\gamma }_{n}^{2}}\left\langle  {{P}_{n},{P}_{n}}\right\rangle   = \frac{M}{{\gamma }_{n}^{2}}
\]

Par ailleurs, comme \( f\left( {x}_{i}\right) = P\left( {x}_{i}\right) \) , on a \( {\int }_{I}P\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}f\left( {x}_{i}\right) \) donc

> Furthermore, since \( f\left( {x}_{i}\right) = P\left( {x}_{i}\right) \), we have \( {\int }_{I}P\left( x\right) w\left( x\right) {dx} = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}f\left( {x}_{i}\right) \) therefore

\[
{\int }_{I}f\left( x\right) w\left( x\right) {dx} - \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}f\left( {x}_{i}\right)  = {\int }_{I}\left( {f\left( x\right)  - P\left( x\right) }\right) w\left( x\right) {dx}
\]

d’où le résultat souhaité à partir de la majoration \( {\int }_{I}\left| {f - P}\right| w \) obtenue juste au dessus.

> hence the desired result from the bound \( {\int }_{I}\left| {f - P}\right| w \) obtained just above.

Remarque. Les polynômes orthogonaux classiques sont les suivants :

> Remark. The classical orthogonal polynomials are as follows:

(i) Lorsque \( I = \rbrack - 1,1\left\lbrack \right. \) et \( w\left( x\right) = {\left( 1 - {x}^{2}\right) }^{-1/2} \) , les \( {P}_{n} \) sont les polynômes de Tchébycheff de première espèce, et vérifient \( {P}_{n}\left( x\right) = {T}_{n}\left( x\right) = \cos \left( {n\arccos \left( x\right) }\right) \) (déjà rencontrés dans l'exercice 13 page 74 et le problème 13 page 101).

> (i) When \( I = \rbrack - 1,1\left\lbrack \right. \) and \( w\left( x\right) = {\left( 1 - {x}^{2}\right) }^{-1/2} \), the \( {P}_{n} \) are the Chebyshev polynomials of the first kind, and satisfy \( {P}_{n}\left( x\right) = {T}_{n}\left( x\right) = \cos \left( {n\arccos \left( x\right) }\right) \) (already encountered in exercise 13 on page 74 and problem 13 on page 101).

(ii) Lorsque \( I = \rbrack - 1,1\lbrack \) et \( w\left( x\right) = {\left( 1 - {x}^{2}\right) }^{1/2} \) , les \( {P}_{n} \) sont les polynômes de Tchébycheff de seconde espèce, et vérifient \( {P}_{n}\left( x\right) = {U}_{n}\left( x\right) = \frac{1}{n + 1}{T}_{n + 1}^{\prime }\left( x\right) \) .

> (ii) When \( I = \rbrack - 1,1\lbrack \) and \( w\left( x\right) = {\left( 1 - {x}^{2}\right) }^{1/2} \), the \( {P}_{n} \) are the Chebyshev polynomials of the second kind, and satisfy \( {P}_{n}\left( x\right) = {U}_{n}\left( x\right) = \frac{1}{n + 1}{T}_{n + 1}^{\prime }\left( x\right) \).

(iii) Lorsque \( I = \left\lbrack {-1,1}\right\rbrack \) et \( w\left( x\right) = 1 \) , les \( {P}_{n} \) sont les polynômes de Legendre. Ils vérifient \( {P}_{n}\left( x\right) = \frac{1}{{2}^{n}n!}\frac{{d}^{n}}{d{x}^{n}}{\left( 1 - {x}^{2}\right) }^{n}. \)

> (iii) When \( I = \left\lbrack {-1,1}\right\rbrack \) and \( w\left( x\right) = 1 \), the \( {P}_{n} \) are the Legendre polynomials. They satisfy \( {P}_{n}\left( x\right) = \frac{1}{{2}^{n}n!}\frac{{d}^{n}}{d{x}^{n}}{\left( 1 - {x}^{2}\right) }^{n}. \)

(iv) Lorsque \( I = \rbrack - \infty , + \infty \lbrack \) et \( w\left( x\right) = {e}^{-{x}^{2}} \) , les \( {P}_{n} \) sont les polynômes d’Hermite.

> (iv) When \( I = \rbrack - \infty , + \infty \lbrack \) and \( w\left( x\right) = {e}^{-{x}^{2}} \), the \( {P}_{n} \) are the Hermite polynomials.

(v) Lorsque \( I = \left\lbrack {0, + \infty \left\lbrack \right. }\right. \) et \( w\left( x\right) = {e}^{-x} \) , les \( {P}_{n} \) sont les polynômes de Laguerre.

> (v) When \( I = \left\lbrack {0, + \infty \left\lbrack \right. }\right. \) and \( w\left( x\right) = {e}^{-x} \), the \( {P}_{n} \) are the Laguerre polynomials.

Chapitre 3

> Chapter 3
