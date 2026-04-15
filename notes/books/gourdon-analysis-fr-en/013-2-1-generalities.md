#### 2.1. Generalities

*Français : 2.1. Généralités*

DéFINITION 1. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) une suite de points de \( E \) . On dit que \( \left( {x}_{n}\right) \) converge vers \( \ell \in E \) si pour tout voisinage \( V \) de \( \ell \) dans \( E \) , il existe \( N \in \mathbb{N} \) tel que pour tout \( n \geq N,{x}_{n} \in V \) , ou de manière équivalente si

> DEFINITION 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) a sequence of points in \( E \) . We say that \( \left( {x}_{n}\right) \) converges to \( \ell \in E \) if for every neighborhood \( V \) of \( \ell \) in \( E \) , there exists \( N \in \mathbb{N} \) such that for all \( n \geq N,{x}_{n} \in V \) , or equivalently if

\[
\left( {\forall \varepsilon  > 0,\exists N \in  \mathbb{N}}\right) ,\;\left( {n \geq  N \Rightarrow  \mathrm{d}\left( {{x}_{n},\ell }\right)  < \varepsilon }\right) .
\]

Si \( \ell \) existe, \( \ell \) est unique est s’appelle limite de \( \left( {x}_{n}\right) \) . On note alors \( \ell = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{x}_{n} \) .

> If \( \ell \) exists, \( \ell \) is unique and is called the limit of \( \left( {x}_{n}\right) \) . We then denote it \( \ell = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{x}_{n} \) .

Remarque 1. - Toute suite convergente est bornée.

> Remark 1. - Every convergent sequence is bounded.

- On rappelle qu’une suite extraite (ou sous-suite) d’une suite \( {\left( {x}_{n}\right) }_{n \in  \mathbb{N}} \) est une suite de la forme \( {\left( {y}_{n}\right) }_{n \in  \mathbb{N}} \) où \( {y}_{n} = {x}_{\varphi \left( n\right) } \) , avec \( \varphi  : \mathbb{N} \rightarrow  \mathbb{N} \) strictement croissante. Si \( \left( {x}_{n}\right) \) converge vers \( \ell \) , toute sous-suite de \( \left( {x}_{n}\right) \) converge vers \( \ell \) .

> - Recall that an extracted sequence (or subsequence) of a sequence \( {\left( {x}_{n}\right) }_{n \in  \mathbb{N}} \) is a sequence of the form \( {\left( {y}_{n}\right) }_{n \in  \mathbb{N}} \) where \( {y}_{n} = {x}_{\varphi \left( n\right) } \) , with \( \varphi  : \mathbb{N} \rightarrow  \mathbb{N} \) strictly increasing. If \( \left( {x}_{n}\right) \) converges to \( \ell \) , every subsequence of \( \left( {x}_{n}\right) \) converges to \( \ell \) .

- La notion de convergence d'une suite est topologique, autrement dit, elle ne dépend que de la topologie de \( E \) .

> - The notion of convergence of a sequence is topological, in other words, it depends only on the topology of \( E \) .

DéFINITION 2. Soit \( \left( {x}_{n}\right) \) une suite d’un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) . On dit que \( a \in E \) est valeur d'adhérence de \( \left( {x}_{n}\right) \) si

> DEFINITION 2. Let \( \left( {x}_{n}\right) \) be a sequence in a metric space \( \left( {E,\mathrm{\;d}}\right) \) . We say that \( a \in E \) is a cluster point of \( \left( {x}_{n}\right) \) if

\[
\left( {\forall \varepsilon  > 0,\forall p \in  \mathbb{N},\exists n \geq  p}\right) ,\;\mathrm{d}\left( {{x}_{n}, a}\right)  < \varepsilon .
\]

Proposition 1. Soit \( \left( {x}_{n}\right) \) une suite \( {de}\left( {E,\mathrm{\;d}}\right) \) , soit \( a \in E \) . Les assertions suivantes sont équivalentes.

> Proposition 1. Let \( \left( {x}_{n}\right) \) be a sequence \( {de}\left( {E,\mathrm{\;d}}\right) \) , let \( a \in E \) . The following assertions are equivalent.

(i) a est valeur d'adhérence de \( \left( {x}_{n}\right) \) .

> (i) a is a cluster point of \( \left( {x}_{n}\right) \) .

(ii) Il existe une sous-suite de \( \left( {x}_{n}\right) \) qui converge vers a.

> (ii) There exists a subsequence of \( \left( {x}_{n}\right) \) that converges to a.

(iii) Pour tout \( p \in \mathbb{N}, a \in \overline{{A}_{p}} \) où \( {A}_{p} = \left\{ {{x}_{n}, n \geq p}\right\} \) .

> (iii) For all \( p \in \mathbb{N}, a \in \overline{{A}_{p}} \) where \( {A}_{p} = \left\{ {{x}_{n}, n \geq p}\right\} \) .

(iv) a est point d’accumulation de \( A = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \) ou a est point de répétition de \( \left( {x}_{n}\right) \) (i. e. l’ensemble \( \left\{ {n \in \mathbb{N} \mid {x}_{n} = a}\right\} \) est infini).

> (iv) a is an accumulation point of \( A = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \) or a is a cluster point of \( \left( {x}_{n}\right) \) (i.e., the set \( \left\{ {n \in \mathbb{N} \mid {x}_{n} = a}\right\} \) is infinite).

L’ensemble des valeurs d’adhérences de \( \left( {x}_{n}\right) \) est donc égal à \( { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \) , donc fermé.

> The set of cluster points of \( \left( {x}_{n}\right) \) is therefore equal to \( { \cap }_{p \in \mathbb{N}}\overline{{A}_{p}} \) , and thus closed.

Remarque 2. Si \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{n} = \ell ,\ell \) est l’unique valeur d’adhérence de \( \left( {x}_{n}\right) \) .

> Remark 2. If \( \mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{n} = \ell ,\ell \) is the unique cluster point of \( \left( {x}_{n}\right) \) .
