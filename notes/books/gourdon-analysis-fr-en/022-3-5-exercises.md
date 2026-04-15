#### 3.5. Exercises

*Français : 3.5. Exercices*

EXERCICE 1. 1 / a) Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques et \( f : E \rightarrow F \) une application continue telle que pour tout compact \( K \) de \( F,{f}^{-1}\left( K\right) \) est compact. Montrer que \( f \) est une application fermée (rappel : une application \( f \) est dite fermée si l’image de tout fermé par \( f \) est un fermé).

> EXERCISE 1. 1 / a) Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces and \( f : E \rightarrow F \) be a continuous map such that for every compact set \( K \) of \( F,{f}^{-1}\left( K\right) \) is compact. Show that \( f \) is a closed map (reminder: a map \( f \) is said to be closed if the image of every closed set under \( f \) is a closed set).

b) Existe-t-il des applications continues qui ne sont pas fermées ?

> b) Do there exist continuous maps that are not closed?

2/ (Application). On fixe un entier naturel non nul \( n \) et on note

> 2/ (Application). We fix a non-zero natural number \( n \) and denote

\[
{\mathbb{R}}_{n}\left\lbrack  X\right\rbrack   = \{ P \in  \mathbb{R}\left\lbrack  X\right\rbrack   \mid  \deg \left( P\right)  \leq  n\} .
\]

Montrer que l’ensemble \( {\Gamma }_{n} \) des polynômes unitaires de degré \( n \) de \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) dont toutes les racines sont réelles est un fermé du \( \mathbb{R} \) -e.v.n \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) .

> Show that the set \( {\Gamma }_{n} \) of monic polynomials of degree \( n \) in \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) whose roots are all real is a closed subset of the \( \mathbb{R} \) -n.v.s \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) .

Solution. 1/ a) Soit \( \Gamma \) un fermé de \( E \) . Soit \( \left( {y}_{n}\right) = {\left( f\left( {x}_{n}\right) \right) }_{n \in \mathbb{N}} \) une suite de \( f\left( \Gamma \right) \) qui converge vers un point \( y \in F \) . Il s’agit de montrer que \( y \in f\left( \Gamma \right) \) .

> Solution. 1/ a) Let \( \Gamma \) be a closed set of \( E \) . Let \( \left( {y}_{n}\right) = {\left( f\left( {x}_{n}\right) \right) }_{n \in \mathbb{N}} \) be a sequence in \( f\left( \Gamma \right) \) that converges to a point \( y \in F \) . We must show that \( y \in f\left( \Gamma \right) \) .

L’ensemble \( K = \left\{ {{y}_{n}, n \in \mathbb{N}}\right\} \cup \{ y\} \) est un compact de \( F \) (voir la proposition 12), l’ensemble \( {f}^{-1}\left( K\right) \) est donc compact. La suite \( \left( {x}_{n}\right) \) de \( \Gamma \) prenant ses valeurs dans \( {f}^{-1}\left( K\right) \) , on peut en extraire une sous-suite convergente \( {\left( {x}_{\varphi \left( n\right) }\right) }_{n \in \mathbb{N}} \) . Notons \( x \) sa limite. Comme \( \Gamma \) est fermé, \( x = \; \mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{\varphi \left( n\right) } \) appartient à \( \Gamma \) , et par continuité de \( f \) ,

> The set \( K = \left\{ {{y}_{n}, n \in \mathbb{N}}\right\} \cup \{ y\} \) is a compact subset of \( F \) (see proposition 12), so the set \( {f}^{-1}\left( K\right) \) is compact. The sequence \( \left( {x}_{n}\right) \) of \( \Gamma \) taking its values in \( {f}^{-1}\left( K\right) \) , we can extract a convergent subsequence \( {\left( {x}_{\varphi \left( n\right) }\right) }_{n \in \mathbb{N}} \) . Let \( x \) denote its limit. Since \( \Gamma \) is closed, \( x = \; \mathop{\lim }\limits_{{n \rightarrow \infty }}{x}_{\varphi \left( n\right) } \) belongs to \( \Gamma \) , and by continuity of \( f \) ,

\[
f\left( x\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}f\left( {x}_{\varphi \left( n\right) }\right)  = \mathop{\lim }\limits_{{n \rightarrow  \infty }}{y}_{\varphi \left( n\right) } = y,
\]

donc \( y = f\left( x\right) \in f\left( \Gamma \right) \) . L’ensemble \( f\left( \Gamma \right) \) est donc bien fermé.

> therefore \( y = f\left( x\right) \in f\left( \Gamma \right) \) . The set \( f\left( \Gamma \right) \) is thus indeed closed.

b) Il existe des applications continues non fermées. Par exemple, \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {e}^{x} \) est continue et pourtant, \( f\left( \mathbb{R}\right) = \rbrack 0, + \infty \lbrack \) n’est pas fermé.

> b) There exist continuous maps that are not closed. For example, \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto {e}^{x} \) is continuous and yet, \( f\left( \mathbb{R}\right) = \rbrack 0, + \infty \lbrack \) is not closed.

2 / Le résultat sera prouvé si on montre que l'application continue

> 2 / The result will be proven if we show that the continuous map

\[
f : {\mathbb{R}}^{n} \rightarrow  {\mathbb{R}}_{n}\left\lbrack  X\right\rbrack  \;\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right)  \mapsto  \left( {X - {\lambda }_{1}}\right) \cdots \left( {X - {\lambda }_{n}}\right)
\]

est fermée, puisque \( {\Gamma }_{n} = f\left( {\mathbb{R}}^{n}\right) \) . En vertu du résultat de la question \( 1/ \) a), il suffit pour cela de prouver que pour tout compact \( K \) de \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack ,{f}^{-1}\left( K\right) \) est un compact.

> is closed, since \( {\Gamma }_{n} = f\left( {\mathbb{R}}^{n}\right) \) . By virtue of the result from question \( 1/ \) a), it suffices for this to prove that for every compact set \( K \) of \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack ,{f}^{-1}\left( K\right) \) is a compact set.

Donnons nous un compact \( K \) de \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) . L’ensemble \( {f}^{-1}\left( K\right) \) est déjà un fermé puisque \( K \) est fermé et que \( f \) est continue. Montrons qu’il est borné. Comme \( K \) est compact, \( K \) est borné, donc il existe \( M > 0 \) tel que

> Let \( K \) be a compact set in \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \). The set \( {f}^{-1}\left( K\right) \) is already closed since \( K \) is closed and \( f \) is continuous. Let us show that it is bounded. Since \( K \) is compact, \( K \) is bounded, so there exists \( M > 0 \) such that

\[
\forall P = \mathop{\sum }\limits_{{k = 0}}^{n}{a}_{k}{X}^{k} \in  K,\;\parallel P\parallel  = \mathop{\sup }\limits_{k}\left| {a}_{k}\right|  \leq  M.
\]

Soit \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {f}^{-1}\left( K\right) \) , de sorte que \( P = f\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \in K \) . Écrivons \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \) . Si \( \lambda \) est une racine de \( P \) , nous allons prouver que \( \left| \lambda \right| \leq 1 + \parallel P\parallel \) . Si \( \left| \lambda \right| \leq 1 \) , c’est terminé, sinon l’égalité \( P\left( \lambda \right) = 0 \) entraîne

> Let \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {f}^{-1}\left( K\right) \), such that \( P = f\left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) = \mathop{\prod }\limits_{{i = 1}}^{n}\left( {X - {\lambda }_{i}}\right) \in K \). Let us write \( P = {X}^{n} + {a}_{1}{X}^{n - 1} + \cdots + {a}_{n} \). If \( \lambda \) is a root of \( P \), we will prove that \( \left| \lambda \right| \leq 1 + \parallel P\parallel \). If \( \left| \lambda \right| \leq 1 \), we are done, otherwise the equality \( P\left( \lambda \right) = 0 \) implies

\[
\left| \lambda \right|  = \left| {{a}_{1} + \frac{{a}_{2}}{\lambda } + \cdots  + \frac{{a}_{n - 1}}{{\lambda }^{n - 2}} + \frac{{a}_{n}}{{\lambda }^{n - 1}}}\right|  \leq  \parallel P\parallel \left( {\mathop{\sum }\limits_{{k = 0}}^{{+\infty }}\frac{1}{{\left| \lambda \right| }^{k}}}\right)  = \parallel P\parallel \frac{1}{1 - 1/\left| \lambda \right| },
\]

d’où on tire facilement \( \left| \lambda \right| \leq 1 + \parallel P\parallel \leq 1 + M \) .

> from which we easily derive \( \left| \lambda \right| \leq 1 + \parallel P\parallel \leq 1 + M \).

Ainsi, nous avons prouvé que si \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {f}^{-1}\left( K\right) \) , alors pour tout \( i,\left| {\lambda }_{i}\right| \leq 1 + M \) . En d’autres termes, \( {f}^{-1}\left( K\right) \) est borné. L’ensemble \( {f}^{-1}\left( K\right) \) , fermé borné de \( {\mathbb{R}}^{n} \) , est donc compact, d'où le résultat.

> Thus, we have proven that if \( \left( {{\lambda }_{1},\ldots ,{\lambda }_{n}}\right) \in {f}^{-1}\left( K\right) \) , then for all \( i,\left| {\lambda }_{i}\right| \leq 1 + M \) . In other words, \( {f}^{-1}\left( K\right) \) is bounded. The set \( {f}^{-1}\left( K\right) \) , a closed bounded set of \( {\mathbb{R}}^{n} \) , is therefore compact, hence the result.

\( \rightarrow \) EXERCICE 2 (UN PRÉCOMPACT COMPLET EST COMPACT). On rappelle qu'un espace métrique est précompact si pour tout \( \varepsilon > 0 \) , il existe un recouvrement fini de cet espace par des boules (ouvertes) de rayon \( \varepsilon \) .

> \( \rightarrow \) EXERCISE 2 (A COMPLETE PRECOMPACT SPACE IS COMPACT). Recall that a metric space is precompact if for all \( \varepsilon > 0 \) , there exists a finite covering of this space by (open) balls of radius \( \varepsilon \) .

Montrer qu'un espace métrique précompact et complet est compact.

> Show that a complete precompact metric space is compact.

Solution. Soit \( \left( {E,\mathrm{\;d}}\right) \) un tel espace métrique. Soit \( \left( {x}_{n}\right) \) une suite de \( E \) . Il s’agit de montrer que l’on peut extraire de \( \left( {x}_{n}\right) \) une sous-suite convergente.

> Solution. Let \( \left( {E,\mathrm{\;d}}\right) \) be such a metric space. Let \( \left( {x}_{n}\right) \) be a sequence of \( E \) . We must show that we can extract a convergent subsequence from \( \left( {x}_{n}\right) \) .

Comme \( E \) est précompact, on peut recouvrir \( E \) par un nombre fini de boules de rayon 1. Il existe donc une de ces boules, \( \mathrm{B}\left( {{a}_{0},1}\right) \) , qui contient la valeur \( {x}_{n} \) pour une infinité d’indices \( n \) . On peut donc construire une sous-suite \( {\left( {x}_{{\varphi }_{0}\left( n\right) }\right) }_{n \in \mathbb{N}} \) de \( \left( {x}_{n}\right) \) telle que pour tout \( n,{x}_{{\varphi }_{0}\left( n\right) } \in \mathrm{B}\left( {{a}_{0},1}\right) \) .

> Since \( E \) is precompact, we can cover \( E \) with a finite number of balls of radius 1. There exists, therefore, one of these balls, \( \mathrm{B}\left( {{a}_{0},1}\right) \) , which contains the value \( {x}_{n} \) for an infinite number of indices \( n \) . We can thus construct a subsequence \( {\left( {x}_{{\varphi }_{0}\left( n\right) }\right) }_{n \in \mathbb{N}} \) of \( \left( {x}_{n}\right) \) such that for all \( n,{x}_{{\varphi }_{0}\left( n\right) } \in \mathrm{B}\left( {{a}_{0},1}\right) \) .

Comme \( \mathrm{B}\left( {{a}_{0},1}\right) \subset E,\mathrm{\;B}\left( {{a}_{0},1}\right) \) est précompact. On peut donc recouvrir \( \mathrm{B}\left( {{a}_{0},1}\right) \) par un nombre fini de boules de rayon \( 1/2 \) . Il existe donc une de ces boules, \( B\left( {{a}_{1},1/2}\right) \) , telle que \( \mathrm{B}\left( {{a}_{0},1}\right) \cap \mathrm{B}\left( {{a}_{1},1/2}\right) \) contienne la valeur \( {x}_{{\varphi }_{0}\left( n\right) } \) pour une infinité d’indices \( n \) . On peut donc construire une sous-suite \( {\left( {x}_{{\varphi }_{0} \circ {\varphi }_{1}\left( n\right) }\right) }_{n \in \mathbb{N}} \) de \( \left( {x}_{{\varphi }_{0}\left( n\right) }\right) \) telle que

> Since \( \mathrm{B}\left( {{a}_{0},1}\right) \subset E,\mathrm{\;B}\left( {{a}_{0},1}\right) \) is precompact. We can therefore cover \( \mathrm{B}\left( {{a}_{0},1}\right) \) with a finite number of balls of radius \( 1/2 \) . There exists, therefore, one of these balls, \( B\left( {{a}_{1},1/2}\right) \) , such that \( \mathrm{B}\left( {{a}_{0},1}\right) \cap \mathrm{B}\left( {{a}_{1},1/2}\right) \) contains the value \( {x}_{{\varphi }_{0}\left( n\right) } \) for an infinite number of indices \( n \) . We can thus construct a subsequence \( {\left( {x}_{{\varphi }_{0} \circ {\varphi }_{1}\left( n\right) }\right) }_{n \in \mathbb{N}} \) of \( \left( {x}_{{\varphi }_{0}\left( n\right) }\right) \) such that

\[
\forall n \in  \mathbb{N},\;{x}_{{\varphi }_{0} \circ  {\varphi }_{1}\left( n\right) } \in  \mathrm{B}\left( {{a}_{0},1}\right)  \cap  \mathrm{B}\left( {{a}_{1},1/2}\right) .
\]

En procédant par récurrence, on peut ainsi construire, pour tout entier naturel \( p \) , une sous-suite \( {\left( {x}_{{\varphi }_{0} \circ \cdots \circ {\varphi }_{p}\left( n\right) }\right) }_{n \in \mathbb{N}} \) et une boule \( \mathrm{B}\left( {{a}_{p},1/{2}^{p}}\right) \) telles que

> By proceeding by induction, we can thus construct, for every natural number \( p \) , a subsequence \( {\left( {x}_{{\varphi }_{0} \circ \cdots \circ {\varphi }_{p}\left( n\right) }\right) }_{n \in \mathbb{N}} \) and a ball \( \mathrm{B}\left( {{a}_{p},1/{2}^{p}}\right) \) such that

\[
\forall n \in  \mathbb{N},\;{x}_{{\varphi }_{0} \circ  \cdots  \circ  {\varphi }_{p}\left( n\right) } \in  \mathop{\bigcap }\limits_{{0 \leq  k \leq  p}}\mathrm{\;B}\left( {{a}_{k},1/{2}^{k}}\right) .
\]

Simplifions les notations. En notant \( {\psi }_{p} = {\varphi }_{0} \circ \cdots \circ {\varphi }_{p} \) pour tout \( p \) , on a construit, pour tout \( p \) , une sous-suite \( \left( {x}_{{\psi }_{p}\left( n\right) }\right) \) de \( \left( {x}_{{\psi }_{p - 1}\left( n\right) }\right) \) telle que

> Let us simplify the notation. By denoting \( {\psi }_{p} = {\varphi }_{0} \circ \cdots \circ {\varphi }_{p} \) for all \( p \), we have constructed, for all \( p \), a subsequence \( \left( {x}_{{\psi }_{p}\left( n\right) }\right) \) of \( \left( {x}_{{\psi }_{p - 1}\left( n\right) }\right) \) such that

\[
\forall n \in  \mathbb{N},\;{x}_{{\psi }_{p}\left( n\right) } \in  \mathrm{B}\left( {{a}_{p},1/{2}^{p}}\right) .
\]

On va maintenant construire une sous-suite de \( \left( {x}_{n}\right) \) par la méthode dite du procédé diagona (à retenir).

> We will now construct a subsequence of \( \left( {x}_{n}\right) \) using the so-called diagonal process (to be remembered).

- On choisit \( {x}_{\psi \left( 0\right) } \in  \left\{  {{x}_{{\psi }_{0}\left( n\right) }, n \in  \mathbb{N}}\right\} \) .

> - We choose \( {x}_{\psi \left( 0\right) } \in  \left\{  {{x}_{{\psi }_{0}\left( n\right) }, n \in  \mathbb{N}}\right\} \) .

- On choisit ensuite \( {x}_{\psi \left( 1\right) } \in  \left\{  {{x}_{{\psi }_{1}\left( n\right) }, n \in  \mathbb{N}}\right\} \) avec \( \psi \left( 1\right)  > \psi \left( 0\right) \) .

> - We then choose \( {x}_{\psi \left( 1\right) } \in  \left\{  {{x}_{{\psi }_{1}\left( n\right) }, n \in  \mathbb{N}}\right\} \) with \( \psi \left( 1\right)  > \psi \left( 0\right) \) .

— ...

> - L’indice \( \psi \left( p\right) \) étant construit, on choisit \( {x}_{\psi \left( {p + 1}\right) } \in  \left\{  {{x}_{{\psi }_{p + 1}\left( n\right) }, n \in  \mathbb{N}}\right\} \) avec \( \psi \left( {p + 1}\right)  > \psi \left( p\right) \) .

- With the index \( \psi \left( p\right) \) constructed, we choose \( {x}_{\psi \left( {p + 1}\right) } \in  \left\{  {{x}_{{\psi }_{p + 1}\left( n\right) }, n \in  \mathbb{N}}\right\} \) with \( \psi \left( {p + 1}\right)  > \psi \left( p\right) \) .

> Ainsi construite, la suite \( {\left( {x}_{\psi \left( p\right) }\right) }_{p \in \mathbb{N}} \) est une sous-suite de \( \left( {x}_{n}\right) \) . Si maintenant \( p \in \mathbb{N} \) et \( q \geq p \) , on a

Constructed in this way, the sequence \( {\left( {x}_{\psi \left( p\right) }\right) }_{p \in \mathbb{N}} \) is a subsequence of \( \left( {x}_{n}\right) \) . If we now have \( p \in \mathbb{N} \) and \( q \geq p \) , we have

\[
{x}_{\psi \left( q\right) } \in  \left\{  {{x}_{{\psi }_{q}\left( n\right) }, n \in  \mathbb{N}}\right\}   \subset  \left\{  {{x}_{{\psi }_{p}\left( n\right) }, n \in  \mathbb{N}}\right\}   \subset  \mathrm{B}\left( {{a}_{p},1/{2}^{p}}\right) ,
\]

ce qui prouve que

> which proves that

\[
\forall p, q \in  \mathbb{N}\left( {p \leq  q}\right) ,\;\mathrm{d}\left( {x}_{\psi \left( p\right) ,\psi \left( q\right) }\right)  \leq  \frac{1}{{2}^{p - 1}}.
\]

La suite \( \left( {x}_{\psi \left( p\right) }\right) \) est donc de Cauchy, et comme \( E \) est complet, elle converge. D’où le résultat.

> The sequence \( \left( {x}_{\psi \left( p\right) }\right) \) is therefore Cauchy, and since \( E \) is complete, it converges. Hence the result.

Remarque. La réciproque est immédiate : un compact est précompact et complet.

> Remark. The converse is immediate: a compact set is precompact and complete.

- EXERCICE 3 (DISTANCE ENTRE DEUX PARTIES). 1/ Soit (E, d) un espace métrique. a) Soient \( {K}_{1} \) et \( {K}_{2} \) deux compacts de \( E \) . Montrer l’existence de \( {x}_{1} \in  {K}_{1} \) et \( {x}_{2} \in  {K}_{2} \) tels que \( \mathrm{d}\left( {{x}_{1},{x}_{2}}\right)  = \mathrm{d}\left( {{K}_{1},{K}_{2}}\right) \left( { = \mathop{\inf }\limits_{\substack{{x \in  {K}_{1}} \\  {y \in  {K}_{2}} }}\mathrm{\;d}\left( {x, y}\right) }\right) \) .

> - EXERCISE 3 (DISTANCE BETWEEN TWO SETS). 1/ Let (E, d) be a metric space. a) Let \( {K}_{1} \) and \( {K}_{2} \) be two compact sets of \( E \) . Show the existence of \( {x}_{1} \in  {K}_{1} \) and \( {x}_{2} \in  {K}_{2} \) such that \( \mathrm{d}\left( {{x}_{1},{x}_{2}}\right)  = \mathrm{d}\left( {{K}_{1},{K}_{2}}\right) \left( { = \mathop{\inf }\limits_{\substack{{x \in  {K}_{1}} \\  {y \in  {K}_{2}} }}\mathrm{\;d}\left( {x, y}\right) }\right) \) .

b) Soient \( K \) un compact de \( E \) et \( F \) un fermé de \( E \) . Si \( K \cap F = \varnothing \) , montrer que \( \mathrm{d}\left( {K, F}\right) \neq 0 \) . Ce résultat subsiste t-il si \( K \) est seulement supposé fermé ?

> b) Let \( K \) be a compact set of \( E \) and \( F \) a closed set of \( E \) . If \( K \cap F = \varnothing \) , show that \( \mathrm{d}\left( {K, F}\right) \neq 0 \) . Does this result still hold if \( K \) is only assumed to be closed?

2 / Ici, \( E = {\mathbb{R}}^{n}\left( {n \in {\mathbb{N}}^{ * }}\right) \) , muni de la métrique usuelle.

> 2 / Here, \( E = {\mathbb{R}}^{n}\left( {n \in {\mathbb{N}}^{ * }}\right) \) , equipped with the usual metric.

a) Soit \( F \) un fermé non borné de \( E \) et \( f : F \rightarrow \mathbb{R} \) une application continue telle que

> a) Let \( F \) be an unbounded closed set of \( E \) and \( f : F \rightarrow \mathbb{R} \) a continuous map such that

\[
\mathop{\lim }\limits_{\substack{{\parallel x\parallel  \rightarrow  \infty } \\  {x \in  F} }}f\left( x\right)  =  + \infty
\]

Montrer qu’il existe \( x \in F \) tel que \( f\left( x\right) = \mathop{\inf }\limits_{{y \in F}}f\left( y\right) \) .

> Show that there exists \( x \in F \) such that \( f\left( x\right) = \mathop{\inf }\limits_{{y \in F}}f\left( y\right) \) .

b) Soient \( K \) un compact de \( E \) et \( F \) un fermé de \( E \) . Montrer

> b) Let \( K \) be a compact subset of \( E \) and \( F \) be a closed subset of \( E \) . Show

\[
\left( {\exists x \in  K,\exists y \in  F}\right) ,\;\mathrm{d}\left( {x, y}\right)  = \mathrm{d}\left( {K, F}\right) .
\]

Ceci reste t-il vrai si \( E \) est un \( \mathbb{R} \) -e.v.n de dimension infinie?

> Does this remain true if \( E \) is an infinite-dimensional \( \mathbb{R} \) -n.v.s.?

Solution. 1/ a) L’application d : \( {K}_{1} \times {K}_{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto \mathrm{d}\left( {x, y}\right) \) est continue sur le compact \( {K}_{1} \times {K}_{2} \) , donc elle atteint son minimum sur \( {K}_{1} \times {K}_{2} \) , c’est-à-dire qu’il existe \( \left( {{x}_{1},{x}_{2}}\right) \in {K}_{1} \times {K}_{2} \) tel que \( \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) = \mathop{\min }\limits_{{\left( {x, y}\right) \in {K}_{1} \times {K}_{2}}}\mathrm{\;d}\left( {x, y}\right) = \mathrm{d}\left( {{K}_{1},{K}_{2}}\right) \) .

> Solution. 1/ a) The map d : \( {K}_{1} \times {K}_{2} \rightarrow \mathbb{R}\;\left( {x, y}\right) \mapsto \mathrm{d}\left( {x, y}\right) \) is continuous on the compact set \( {K}_{1} \times {K}_{2} \) , therefore it attains its minimum on \( {K}_{1} \times {K}_{2} \) , meaning there exists \( \left( {{x}_{1},{x}_{2}}\right) \in {K}_{1} \times {K}_{2} \) such that \( \mathrm{d}\left( {{x}_{1},{x}_{2}}\right) = \mathop{\min }\limits_{{\left( {x, y}\right) \in {K}_{1} \times {K}_{2}}}\mathrm{\;d}\left( {x, y}\right) = \mathrm{d}\left( {{K}_{1},{K}_{2}}\right) \) .

Remarque. En remplaçant \( {K}_{1} \) par \( \{ x\} \) , on voit qu’en particulier, si \( {K}_{2} \) est compact,

> Remark. By replacing \( {K}_{1} \) with \( \{ x\} \) , we see that in particular, if \( {K}_{2} \) is compact,

\[
\exists y \in  {K}_{2},\;\mathrm{\;d}\left( {x,{K}_{2}}\right)  = \mathrm{d}\left( {x, y}\right) .
\]

b) L’application \( x \mapsto \mathrm{d}\left( {x, F}\right) \) est continue (voir l’exercice 4 page 17) sur le compact \( K \) , donc

> b) The map \( x \mapsto \mathrm{d}\left( {x, F}\right) \) is continuous (see exercise 4 on page 17) on the compact set \( K \) , therefore

\[
\exists {x}_{0} \in  K,\;\mathrm{\;d}\left( {{x}_{0}, F}\right)  = \mathop{\inf }\limits_{{x \in  K}}\mathrm{\;d}\left( {x, F}\right)  = \mathrm{d}\left( {K, F}\right) .
\]

\( \operatorname{Si}\mathrm{d}\left( {K, F}\right) = 0 \) , alors \( d\left( {{x}_{0}, F}\right) = 0 \) donc \( {x}_{0} \in F \) car \( F \) est fermé. Ceci est absurde car \( K \cap F = \varnothing \) . Donc \( \mathrm{d}\left( {K, F}\right) \neq 0 \) .

> \( \operatorname{Si}\mathrm{d}\left( {K, F}\right) = 0 \) , then \( d\left( {{x}_{0}, F}\right) = 0 \) therefore \( {x}_{0} \in F \) because \( F \) is closed. This is absurd because \( K \cap F = \varnothing \) . Thus \( \mathrm{d}\left( {K, F}\right) \neq 0 \) .

Lorsque \( K \) est seulement supposé fermé, le résultat est faux. Par exemple, dans \( {\mathbb{R}}^{2} \) , les ensembles \( K = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid y \leq 0}\right\} \) et \( F = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid y \geq {e}^{x}}\right\} \) sont fermés, disjoints, et pourtant \( \mathrm{d}\left( {K, F}\right) = 0 \) .

> When \( K \) is only assumed to be closed, the result is false. For example, in \( {\mathbb{R}}^{2} \) , the sets \( K = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid y \leq 0}\right\} \) and \( F = \left\{ {\left( {x, y}\right) \in {\mathbb{R}}^{2} \mid y \geq {e}^{x}}\right\} \) are closed, disjoint, and yet \( \mathrm{d}\left( {K, F}\right) = 0 \) .

2 / a) C’est classique. Fixons \( a \in F \) et considérons l’ensemble \( \Gamma = \{ x \in F \mid f\left( x\right) \leq f\left( a\right) \} \) . Comme \( f \) est continue, \( \left. {\Gamma = {f}^{-1}\left( {\rbrack - \infty , f\left( a\right) \rbrack }\right) }\right) \) est un fermé de \( F \) , donc de \( E \) . Comme \( \mathop{\lim }\limits_{\substack{{\parallel x\parallel \rightarrow \infty } \\ {x \in F} }}f\left( x\right) = + \infty \) , \( \Gamma \) est borné. Finalement, \( \Gamma \) est compact (fermé borné de \( {\mathbb{R}}^{n} \) ). De plus, \( \Gamma \neq \varnothing \) puisque \( a \in \Gamma \) . Donc il existe \( x \in \Gamma \) tel que \( f\left( x\right) = \mathop{\inf }\limits_{{y \in \Gamma }}f\left( y\right) \) . Or, par construction de \( \Gamma \) ,

> 2 / a) This is standard. Let us fix \( a \in F \) and consider the set \( \Gamma = \{ x \in F \mid f\left( x\right) \leq f\left( a\right) \} \) . Since \( f \) is continuous, \( \left. {\Gamma = {f}^{-1}\left( {\rbrack - \infty , f\left( a\right) \rbrack }\right) }\right) \) is a closed subset of \( F \) , and thus of \( E \) . Since \( \mathop{\lim }\limits_{\substack{{\parallel x\parallel \rightarrow \infty } \\ {x \in F} }}f\left( x\right) = + \infty \) , \( \Gamma \) is bounded. Finally, \( \Gamma \) is compact (closed and bounded in \( {\mathbb{R}}^{n} \) ). Furthermore, \( \Gamma \neq \varnothing \) since \( a \in \Gamma \) . Thus there exists \( x \in \Gamma \) such that \( f\left( x\right) = \mathop{\inf }\limits_{{y \in \Gamma }}f\left( y\right) \) . However, by the construction of \( \Gamma \) ,

\[
\mathop{\inf }\limits_{{y \in  \Gamma }}f\left( y\right)  = \mathop{\inf }\limits_{{y \in  F}}f\left( y\right)
\]

donc \( f\left( x\right) = \mathop{\inf }\limits_{{y \in F}}f\left( y\right) \) avec \( x \in F \) .

> therefore \( f\left( x\right) = \mathop{\inf }\limits_{{y \in F}}f\left( y\right) \) with \( x \in F \) .

b) L’application \( x \mapsto \mathrm{d}\left( {x, F}\right) \) étant continue sur le compact \( K \) ,

> b) Since the map \( x \mapsto \mathrm{d}\left( {x, F}\right) \) is continuous on the compact set \( K \) ,

\[
\exists x \in  K,\;\mathrm{d}\left( {x, F}\right)  = \mathop{\inf }\limits_{{y \in  K}}\mathrm{\;d}\left( {y, F}\right)  = \mathrm{d}\left( {K, F}\right) .
\]

De même l’application \( F \rightarrow \mathbb{R}\;y \mapsto \mathrm{d}\left( {x, y}\right) \) est continue. Si \( F \) est bornée, \( F \) est compact (fermé borné de \( {\mathbb{R}}^{n} \) ) et le résultat résulte de 1/ a). Sinon \( F \) n’est pas borné, et on a alors \( \mathop{\lim }\limits_{{\parallel y\parallel \rightarrow \infty }}\mathrm{d}\left( {x, y}\right) = + \infty \) ce qui en vertu de la question précédente permet d’affirmer

> Similarly, the map \( F \rightarrow \mathbb{R}\;y \mapsto \mathrm{d}\left( {x, y}\right) \) is continuous. If \( F \) is bounded, \( F \) is compact (closed and bounded in \( {\mathbb{R}}^{n} \) ) and the result follows from 1/ a). Otherwise, \( F \) is not bounded, and we then have \( \mathop{\lim }\limits_{{\parallel y\parallel \rightarrow \infty }}\mathrm{d}\left( {x, y}\right) = + \infty \) which, by virtue of the previous question, allows us to state

\[
\exists y \in  F,\;\mathrm{\;d}\left( {x, y}\right)  = \mathop{\inf }\limits_{{z \in  F}}\mathrm{\;d}\left( {x, z}\right)  = \mathrm{d}\left( {x, F}\right)  = \mathrm{d}\left( {K, F}\right) ,
\]

d'où le résultat.

> hence the result.

Ceci est faux lorsque \( E \) est de dimension infinie. Prenons par exemple pour \( E \) l’e.v des suites bornées \( \left( {u}_{n}\right) \) de \( \mathbb{R} \) , normé par \( \begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix} = \mathop{\sup }\limits_{{n \in \mathbb{N}}}\left| {u}_{n}\right| \) . Désignons pour tout \( n \) par \( {X}_{n} \) la suite dont tous les termes sont nuls sauf le \( n \) -ième qui vaut \( 1 + 1/{2}^{n} \) . L’ensemble \( F = \left\{ {{X}_{n}, n \in \mathbb{N}}\right\} \) est fermé (si \( p \neq q \) on a \( \begin{Vmatrix}{{X}_{p} - {X}_{q}}\end{Vmatrix} \geq 1 \) , donc toute suite convergente donc de Cauchy dans \( F \) devient stationnaire à partir d’un certain rang, donc converge dans \( F \) ). Si \( K = \{ \left( 0\right) \} \) (ou (0) désigne la suite nulle) il est clair que \( \mathrm{d}\left( {K, F}\right) = 1 \) et pourtant on a \( \mathrm{d}\left( {K,{X}_{n}}\right) = 1 + 1/{2}^{n} > 1 \) pour tout \( n \) .

> This is false when \( E \) is infinite-dimensional. Let us take, for example, for \( E \) the vector space of bounded sequences \( \left( {u}_{n}\right) \) of \( \mathbb{R} \) , normed by \( \begin{Vmatrix}\left( {u}_{n}\right) \end{Vmatrix} = \mathop{\sup }\limits_{{n \in \mathbb{N}}}\left| {u}_{n}\right| \) . For every \( n \) , let \( {X}_{n} \) denote the sequence whose terms are all zero except for the \( n \) -th, which is equal to \( 1 + 1/{2}^{n} \) . The set \( F = \left\{ {{X}_{n}, n \in \mathbb{N}}\right\} \) is closed (if \( p \neq q \) we have \( \begin{Vmatrix}{{X}_{p} - {X}_{q}}\end{Vmatrix} \geq 1 \) , so any convergent sequence, and thus any Cauchy sequence in \( F \) , becomes stationary from a certain rank, and therefore converges in \( F \) ). If \( K = \{ \left( 0\right) \} \) (where (0) denotes the zero sequence), it is clear that \( \mathrm{d}\left( {K, F}\right) = 1 \) and yet we have \( \mathrm{d}\left( {K,{X}_{n}}\right) = 1 + 1/{2}^{n} > 1 \) for all \( n \) .

\( \rightarrow \) EXERCICE 4. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique compact et \( f : E \rightarrow E \) une application vérifiant

> \( \rightarrow \) EXERCISE 4. Let \( \left( {E,\mathrm{\;d}}\right) \) be a compact metric space and \( f : E \rightarrow E \) a mapping satisfying

\[
\forall \left( {x, y}\right)  \in  {E}^{2}, x \neq  y,\;\mathrm{\;d}\left( {f\left( x\right) , f\left( y\right) }\right)  < \mathrm{d}\left( {x, y}\right) .
\]

(*)

> a) Montrer que \( f \) admet un unique point fixe, que nous noterons \( \alpha \) .

a) Show that \( f \) admits a unique fixed point, which we will denote by \( \alpha \) .

> b) Soit \( {x}_{0} \) un point quelconque de \( E \) . On définit la suite \( \left( {x}_{n}\right) \) par récurrence grâce à la relation \( {x}_{n + 1} = f\left( {x}_{n}\right) \) . Montrer que \( \left( {x}_{n}\right) \) converge vers \( \alpha \) .

b) Let \( {x}_{0} \) be an arbitrary point in \( E \) . Define the sequence \( \left( {x}_{n}\right) \) recursively by the relation \( {x}_{n + 1} = f\left( {x}_{n}\right) \) . Show that \( \left( {x}_{n}\right) \) converges to \( \alpha \) .

> c) Ces résultats restent-ils vrais si l’on suppose seulement \( E \) complet ?

c) Do these results remain true if we only assume \( E \) is complete?

> Solution. C'est classique ! C'est une généralisation du théorème du point fixe dans un compact.

Solution. This is a classic! It is a generalization of the fixed-point theorem in a compact space.

> a) L’application \( E \rightarrow \mathbb{R}\;x \mapsto \mathrm{d}\left( {x, f\left( x\right) }\right) \) est continue (composée d’applications continues) sur le compact \( E \) , donc

a) The mapping \( E \rightarrow \mathbb{R}\;x \mapsto \mathrm{d}\left( {x, f\left( x\right) }\right) \) is continuous (as a composition of continuous mappings) on the compact set \( E \) , therefore

\[
\exists \alpha  \in  E,\;\mathrm{\;d}\left( {\alpha , f\left( \alpha \right) }\right)  = \mathop{\inf }\limits_{{x \in  E}}\mathrm{\;d}\left( {x, f\left( x\right) }\right) .
\]

Supposons \( \alpha \neq f\left( \alpha \right) \) . Posons \( \beta = f\left( \alpha \right) \) . D’après (*),

> Suppose \( \alpha \neq f\left( \alpha \right) \) . Let \( \beta = f\left( \alpha \right) \) . According to (*),

\[
\mathrm{d}\left( {\beta , f\left( \beta \right) }\right)  = \mathrm{d}\left( {f\left( \alpha \right) , f\left( \beta \right) }\right)  < \mathrm{d}\left( {\alpha ,\beta }\right)  = \mathrm{d}\left( {\alpha , f\left( \alpha \right) }\right) ,
\]

ce qui contredit la définition de \( \alpha \) . On doit donc avoir \( \alpha = f\left( \alpha \right) \) .

> which contradicts the definition of \( \alpha \) . We must therefore have \( \alpha = f\left( \alpha \right) \) .

Montrons maintenant que \( \alpha \) est l’unique point fixe de \( f \) . Supposons \( \beta = f\left( \beta \right) \) avec \( \beta \neq \alpha \) . On a \( \mathrm{d}\left( {f\left( \alpha \right) , f\left( \beta \right) }\right) = \mathrm{d}\left( {\alpha ,\beta }\right) \) , ce qui est absurde d’après (*) appliqué au couple \( \left( {\alpha ,\beta }\right) \) .

> Now let us show that \( \alpha \) is the unique fixed point of \( f \) . Suppose \( \beta = f\left( \beta \right) \) with \( \beta \neq \alpha \) . We have \( \mathrm{d}\left( {f\left( \alpha \right) , f\left( \beta \right) }\right) = \mathrm{d}\left( {\alpha ,\beta }\right) \) , which is absurd according to (*) applied to the pair \( \left( {\alpha ,\beta }\right) \) .

b) Posons \( {u}_{n} = \mathrm{d}\left( {\alpha ,{x}_{n}}\right) \) . S’il existe \( {n}_{0} \in \mathbb{N} \) tel que \( {u}_{{n}_{0}} = \alpha \) , alors \( {u}_{n} = {u}_{{n}_{0}} = \alpha \) pour tout \( n \geq {n}_{0} \) et le résultat est évident. Sinon,

> b) Let \( {u}_{n} = \mathrm{d}\left( {\alpha ,{x}_{n}}\right) \) . If there exists \( {n}_{0} \in \mathbb{N} \) such that \( {u}_{{n}_{0}} = \alpha \) , then \( {u}_{n} = {u}_{{n}_{0}} = \alpha \) for all \( n \geq {n}_{0} \) and the result is obvious. Otherwise,

\[
\forall n \in  \mathbb{N},\;{u}_{n + 1} = \mathrm{d}\left( {f\left( \alpha \right) , f\left( {x}_{n}\right) }\right)  < \mathrm{d}\left( {\alpha ,{x}_{n}}\right)  = {u}_{n},
\]

c’est-à-dire que la suite \( \left( {u}_{n}\right) \) décroît strictement. Comme elle est minorée par 0, elle converge. Notons \( \ell \) sa limite. Il s’agit de montrer que \( \ell = 0 \) .

> that is to say, the sequence \( \left( {u}_{n}\right) \) is strictly decreasing. Since it is bounded below by 0, it converges. Let \( \ell \) be its limit. We must show that \( \ell = 0 \) .

Supposons \( \ell > 0 \) . Comme \( \left( {u}_{n}\right) \) décroît, on a \( {u}_{n} \geq \ell \) pour tout \( n \in \mathbb{N} \) . De plus, \( \left( {x}_{n}\right) \) est une suite du compact \( E \) , on peut donc en extraire une sous-suite convergente \( \left( {x}_{\varphi \left( n\right) }\right) \) . Notons \( \beta \) la limite de cette dernière. Alors \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {\alpha ,{x}_{\varphi \left( n\right) }}\right) = \mathrm{d}\left( {\alpha ,\beta }\right) = \ell \) . De plus, \( f \) étant continue, on a

> Suppose \( \ell > 0 \) . Since \( \left( {u}_{n}\right) \) is decreasing, we have \( {u}_{n} \geq \ell \) for all \( n \in \mathbb{N} \) . Furthermore, \( \left( {x}_{n}\right) \) is a sequence in the compact set \( E \) , so we can extract a convergent subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) . Let \( \beta \) be the limit of the latter. Then \( \mathop{\lim }\limits_{{n \rightarrow \infty }}\mathrm{d}\left( {\alpha ,{x}_{\varphi \left( n\right) }}\right) = \mathrm{d}\left( {\alpha ,\beta }\right) = \ell \) . Moreover, since \( f \) is continuous, we have

\[
\mathop{\lim }\limits_{{n \rightarrow  \infty }}\mathrm{d}\left( {\alpha , f\left( {x}_{\varphi \left( n\right) }\right) }\right)  = \mathrm{d}\left( {\alpha , f\left( \beta \right) }\right) .
\]

Cette dernière assertion est une absurdité puisque

> This last assertion is an absurdity since

\[
\mathrm{d}\left( {\alpha , f\left( \beta \right) }\right)  = \mathrm{d}\left( {f\left( \alpha \right) , f\left( \beta \right) }\right)  < \mathrm{d}\left( {\alpha ,\beta }\right)  = \ell \;\text{ et }\;\forall n,\;\mathrm{\;d}\left( {\alpha , f\left( {x}_{\varphi \left( n\right) }\right) }\right)  = \mathrm{d}\left( {\alpha ,{x}_{\varphi \left( n\right)  + 1}}\right)  \geq  \ell .
\]

On doit donc avoir \( \ell = 0 \) , d’où le résultat. c) Le résultat est faux si \( E \) est seulement supposé complet. Par exemple, la fonction

> We must therefore have \( \ell = 0 \) , hence the result. c) The result is false if \( E \) is only assumed to be complete. For example, the function

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;f\left( x\right)  = 1\;\text{ si }\;x < 0,\;f\left( x\right)  = x + \frac{1}{1 + x}\;\text{ si }\;x \geq  0,
\]

(voir la figure ci contre) est continue, sans point fixe et vérifie l'hypothèse (*) (immédiat par l'inégalité des accroissements finis).

> (see the figure opposite) is continuous, has no fixed point, and satisfies hypothesis (*) (immediate by the mean value inequality).

![bo_d7fjkrs91nqc73ereoog_39_473_424_608_451_0.jpg](images/gourdon_analysis_fr_en_024_bod7fjkrs91nqc73ereoog394734246084510.jpg)

Figure 1. Le graphe de l’application sans point fixe \( f \)

> Figure 1. The graph of the fixed-point-free map \( f \)

EXERCICE 5 (ISOMÉTRIES D'UN COMPACT). Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique compact et \( f : E \rightarrow E \) une application continue, vérifiant

> EXERCISE 5 (ISOMETRIES OF A COMPACT SPACE). Let \( \left( {E,\mathrm{\;d}}\right) \) be a compact metric space and \( f : E \rightarrow E \) a continuous map satisfying

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {f\left( x\right) , f\left( y\right) }\right)  \geq  \mathrm{d}\left( {x, y}\right) .
\]

(*)

> a) Montrer que \( f \) est une isométrie, c’est-à-dire

a) Show that \( f \) is an isometry, that is

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {f\left( x\right) , f\left( y\right) }\right)  = \mathrm{d}\left( {x, y}\right) .
\]

b) Montrer que \( f \) est bijective.

> b) Show that \( f \) is bijective.

c) Si \( f \) est bijective, montrer que \( f \) est encore une isométrie si elle vérifie

> c) If \( f \) is bijective, show that \( f \) is still an isometry if it satisfies

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {f\left( x\right) , f\left( y\right) }\right)  \leq  \mathrm{d}\left( {x, y}\right) ,
\]

Solution. a) Soient \( x, y \in E \) . On définit deux suites \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) et \( {\left( {y}_{n}\right) }_{n \in \mathbb{N}} \) par \( {x}_{n} = {f}^{n}\left( x\right) \) et \( {y}_{n} = {f}^{n}\left( y\right) \) pour tout \( n \in \mathbb{N} \) (où \( {f}^{n} \) désigne la composée \( n \) fois de l’application \( f \) avec elle même). Nous allons construire deux sous-suites \( \left( {x}_{\psi \left( n\right) }\right) \) et \( \left( {y}_{\psi \left( n\right) }\right) \) qui convergent respectivement vers \( x \) et \( y \) .

> Solution. a) Let \( x, y \in E \) . We define two sequences \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) and \( {\left( {y}_{n}\right) }_{n \in \mathbb{N}} \) by \( {x}_{n} = {f}^{n}\left( x\right) \) and \( {y}_{n} = {f}^{n}\left( y\right) \) for all \( n \in \mathbb{N} \) (where \( {f}^{n} \) denotes the composition of the map \( f \) with itself \( n \) times). We will construct two subsequences \( \left( {x}_{\psi \left( n\right) }\right) \) and \( \left( {y}_{\psi \left( n\right) }\right) \) that converge to \( x \) and \( y \) respectively.

La suite \( {\left( {x}_{n},{y}_{n}\right) }_{n \in \mathbb{N}} \) prend ses valeurs dans le compact \( E \times E \) . On peut donc en extraire une sous-suite convergente \( \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \) . Quitte à extraire encore une sous-suite de cette dernière, on peut même supposer

> The sequence \( {\left( {x}_{n},{y}_{n}\right) }_{n \in \mathbb{N}} \) takes its values in the compact set \( E \times E \) . We can therefore extract a convergent subsequence \( \left( {{x}_{\varphi \left( n\right) },{y}_{\varphi \left( n\right) }}\right) \) . By extracting a further subsequence from the latter, we can even assume

\[
\forall n \in  \mathbb{N},\;\varphi \left( {n + 2}\right)  - \varphi \left( {n + 1}\right)  > \varphi \left( {n + 1}\right)  - \varphi \left( n\right) .
\]

(**)

> De l'inégalité (*), on tire

From inequality (*), we derive

\[
\forall n \in  \mathbb{N},\;\mathrm{d}\left( {x,{x}_{\varphi \left( {n + 1}\right)  - \varphi \left( n\right) }}\right)  \leq  \mathrm{d}\left( {{f}^{\varphi \left( n\right) }\left( x\right) ,{f}^{\varphi \left( n\right) }\left( {x}_{\varphi \left( {n + 1}\right)  - \varphi \left( n\right) }\right) }\right)  = \mathrm{d}\left( {{x}_{\varphi \left( n\right) },{x}_{\varphi \left( {n + 1}\right) }}\right)
\]

et comme \( \left( {x}_{\varphi \left( n\right) }\right) \) converge, on en déduit lim \( {}_{n \rightarrow \infty }{x}_{\varphi \left( {n + 1}\right) - \varphi \left( n\right) } = x \) . Ainsi, en posant \( \psi \left( n\right) = \; \varphi \left( {n + 1}\right) - \varphi \left( n\right) ,\left( {x}_{\psi \left( n\right) }\right) \) est une sous-suite de \( \left( {x}_{n}\right) \) d’après (**), et elle converge vers \( x \) . Pour les mêmes raisons, \( \left( {y}_{\psi \left( n\right) }\right) \) est une sous-suite de \( \left( {y}_{n}\right) \) qui converge vers \( y \) .

> and since \( \left( {x}_{\varphi \left( n\right) }\right) \) converges, we deduce lim \( {}_{n \rightarrow \infty }{x}_{\varphi \left( {n + 1}\right) - \varphi \left( n\right) } = x \) . Thus, by setting \( \psi \left( n\right) = \; \varphi \left( {n + 1}\right) - \varphi \left( n\right) ,\left( {x}_{\psi \left( n\right) }\right) \) is a subsequence of \( \left( {x}_{n}\right) \) according to (**), and it converges to \( x \) . For the same reasons, \( \left( {y}_{\psi \left( n\right) }\right) \) is a subsequence of \( \left( {y}_{n}\right) \) that converges to \( y \) .

Ceci étant, pour \( n \geq 1 \) , on a d’après (*)

> Given this, for \( n \geq 1 \) , we have according to (*)

\[
\mathrm{d}\left( {x, y}\right)  \leq  \mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right)  \leq  \mathrm{d}\left( {{x}_{\psi \left( n\right) },{y}_{\psi \left( n\right) }}\right) ,
\]

et en faisant tendre \( n \) vers \( + \infty \) , on en déduit \( \mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right) = \mathrm{d}\left( {x, y}\right) \) .

> and by letting \( n \) tend to \( + \infty \) , we deduce \( \mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right) = \mathrm{d}\left( {x, y}\right) \) .

b) L'injectivité résulte de l'hypothèse (*). Pour montrer la surjectivité de \( f \) , nous donnons deux méthodes.

> b) Injectivity follows from hypothesis (*). To show the surjectivity of \( f \) , we provide two methods.

Première méthode. Cette méthode utilise la solution que nous avons donnée à la question a).

> First method. This method uses the solution we provided for question a).

Fixons \( x \in E \) . Si \( {x}_{n} = {f}^{n}\left( x\right) \) , nous avons vu plus haut qu’il existe une sous-suite \( \left( {x}_{\psi \left( n\right) }\right) \) de \( \left( {x}_{n}\right) \) qui converge vers \( x \) . Autrement dit, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{\psi \left( n\right) - 1}\right) = x \) , donc \( x \in \overline{f\left( E\right) } \) . Comme \( E \) est compact et que \( f \) est continue, \( f\left( E\right) \) est compact donc fermé. Donc \( x \in \overline{f\left( E\right) } = f\left( E\right) \) , et ceci étant vrai pour tout \( x \in E, f \) est surjective.

> Let us fix \( x \in E \). If \( {x}_{n} = {f}^{n}\left( x\right) \), we saw above that there exists a subsequence \( \left( {x}_{\psi \left( n\right) }\right) \) of \( \left( {x}_{n}\right) \) that converges to \( x \). In other words, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{\psi \left( n\right) - 1}\right) = x \), so \( x \in \overline{f\left( E\right) } \). Since \( E \) is compact and \( f \) is continuous, \( f\left( E\right) \) is compact and therefore closed. Thus \( x \in \overline{f\left( E\right) } = f\left( E\right) \), and since this is true for all \( x \in E, f \), it is surjective.

Seconde méthode. Raisonnons par l’absurde et supposons \( f\left( E\right) \neq E \) . Comme \( f\left( E\right) \) est fermé (car compact), \( E \smallsetminus f\left( E\right) \) est ouvert. De plus \( E \smallsetminus f\left( E\right) \neq \varnothing \) donc il existe une boule ouverte \( \mathrm{B}\left( {x,\rho }\right) \) incluse dans \( E \smallsetminus f\left( E\right) \) . Ainsi, pour tout \( y \in f\left( E\right) ,\mathrm{d}\left( {x, y}\right) \geq \rho \) . Considérons la suite \( {\left( {f}^{n}\left( x\right) \right) }_{n \in \mathbb{N}} \) . Pour tout \( p, q \in \mathbb{N}, p > q \) , on a

> Second method. Let us reason by contradiction and assume \( f\left( E\right) \neq E \). Since \( f\left( E\right) \) is closed (because it is compact), \( E \smallsetminus f\left( E\right) \) is open. Furthermore, \( E \smallsetminus f\left( E\right) \neq \varnothing \), so there exists an open ball \( \mathrm{B}\left( {x,\rho }\right) \) included in \( E \smallsetminus f\left( E\right) \). Thus, for all \( y \in f\left( E\right) ,\mathrm{d}\left( {x, y}\right) \geq \rho \). Consider the sequence \( {\left( {f}^{n}\left( x\right) \right) }_{n \in \mathbb{N}} \). For all \( p, q \in \mathbb{N}, p > q \), we have

\[
\mathrm{d}\left( {{f}^{p}\left( x\right) ,{f}^{q}\left( x\right) }\right)  \geq  \mathrm{d}\left( {{f}^{p - q}\left( x\right) , x}\right)  \geq  \rho ,
\]

donc \( \left( {{f}^{n}\left( x\right) }\right) \) n’a aucune sous-suite convergente, ce qui est absurde. On a donc \( f\left( E\right) = E \) .

> so \( \left( {{f}^{n}\left( x\right) }\right) \) has no convergent subsequence, which is absurd. We therefore have \( f\left( E\right) = E \).

c) L’application \( f \) est bijective et continue (car 1-lipschitzienne) sur un compact, donc \( {f}^{-1} : E \rightarrow \; E \) est continue (voir le théorème 14 page 31) et vérifie d'après les hypothèses

> c) The map \( f \) is bijective and continuous (because it is 1-Lipschitz) on a compact set, so \( {f}^{-1} : E \rightarrow \; E \) is continuous (see theorem 14 on page 31) and satisfies, according to the hypotheses,

\[
\forall \left( {x, y}\right)  \in  {E}^{2},\;\mathrm{\;d}\left( {{f}^{-1}\left( x\right) ,{f}^{-1}\left( y\right) }\right)  \geq  \mathrm{d}\left( {f\left( {{f}^{-1}\left( x\right) }\right) , f\left( {{f}^{-1}\left( y\right) }\right) }\right)  = \mathrm{d}\left( {x, y}\right) .
\]

L’application \( {f}^{-1} \) vérifie donc les hypothèses de la question a), c’est donc une isométrie. On en déduit que \( f \) est une isométrie.

> The map \( {f}^{-1} \) therefore satisfies the hypotheses of question a), so it is an isometry. We deduce from this that \( f \) is an isometry.

EXERCICE 6. Soient \( \left( {E,\mathrm{\;d}}\right) \) et \( \left( {F,\delta }\right) \) deux espaces métriques et \( f : E \rightarrow F \) une application injective. Prouver que \( f \) est continue si et seulement si pour tout compact \( K \) de \( E, f\left( K\right) \) est compact. Le résultat subsiste-t-il si on ne suppose pas \( f \) injective ?

> EXERCISE 6. Let \( \left( {E,\mathrm{\;d}}\right) \) and \( \left( {F,\delta }\right) \) be two metric spaces and \( f : E \rightarrow F \) an injective map. Prove that \( f \) is continuous if and only if for every compact set \( K \) of \( E, f\left( K\right) \) is compact. Does the result still hold if we do not assume \( f \) is injective?

Solution. La condition nécessaire est immédiate, c'est du cours !

> Solution. The necessary condition is immediate; it is from the course!

Passons à la condition suffisante. Soit \( x \in E \) et \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) une suite de \( E \) qui converge vers \( x \) . Il s’agit de montrer que \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{n}\right) = f\left( x\right) \) . L’ensemble \( K = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \cup \{ x\} \) est un compact de \( E \) (voir la proposition 12 page 30), donc \( {K}^{\prime } = f\left( K\right) \) est compact. Notons \( g \) la restriction de \( f \) à \( K \) . Comme \( f \) est injective, \( g \) est une bijection de \( K \) sur \( {K}^{\prime } \) . L’application \( {g}^{-1} : {K}^{\prime } \rightarrow K \) est continue car pour tout fermé \( F \) de \( K, F \) est compact donc \( {\left( {g}^{-1}\right) }^{-1}\left( F\right) = g\left( F\right) \) est compact, donc fermé. L’ensemble \( {K}^{\prime } \) étant compact, \( {\left( {g}^{-1}\right) }^{-1} = g \) est continue. En particulier, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}g\left( {x}_{n}\right) = g\left( x\right) \) , ce qui s’écrit aussi \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{n}\right) = f\left( x\right) \) , d’où le résultat.

> Let us move on to the sufficient condition. Let \( x \in E \) and \( {\left( {x}_{n}\right) }_{n \in \mathbb{N}} \) be a sequence of \( E \) that converges to \( x \). We must show that \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{n}\right) = f\left( x\right) \). The set \( K = \left\{ {{x}_{n}, n \in \mathbb{N}}\right\} \cup \{ x\} \) is a compact subset of \( E \) (see proposition 12 on page 30), so \( {K}^{\prime } = f\left( K\right) \) is compact. Let \( g \) denote the restriction of \( f \) to \( K \). Since \( f \) is injective, \( g \) is a bijection from \( K \) onto \( {K}^{\prime } \). The map \( {g}^{-1} : {K}^{\prime } \rightarrow K \) is continuous because for any closed set \( F \) of \( K, F \) is compact, therefore \( {\left( {g}^{-1}\right) }^{-1}\left( F\right) = g\left( F\right) \) is compact, and thus closed. Since the set \( {K}^{\prime } \) is compact, \( {\left( {g}^{-1}\right) }^{-1} = g \) is continuous. In particular, \( \mathop{\lim }\limits_{{n \rightarrow \infty }}g\left( {x}_{n}\right) = g\left( x\right) \), which can also be written as \( \mathop{\lim }\limits_{{n \rightarrow \infty }}f\left( {x}_{n}\right) = f\left( x\right) \), hence the result.

Si \( f \) n’est pas injective, le résultat est faux. Par exemple, l’application

> If \( f \) is not injective, the result is false. For example, the map

\[
f : \mathbb{R} \rightarrow  \mathbb{R}\;x \mapsto  0\;\text{ si }\;x < 0\;x \mapsto  1\;\text{ si }\;x \geq  0
\]

vérifie \( f\left( K\right) \) est compact pour tout compact \( K \) de \( \mathbb{R} \) , et pourtant \( f \) n’est pas continue.

> satisfies \( f\left( K\right) \) is compact for every compact \( K \) of \( \mathbb{R} \), and yet \( f \) is not continuous.

EXERCICE 7. Soit \( \left\lbrack {a, b}\right\rbrack \) un segment de \( \mathbb{R} \) (avec \( a < b \) ), \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) une application. On suppose que pour tout \( x \in \rbrack a, b\lbrack \) , les limites à gauche \( f\left( {x - }\right) \) et à droite \( f\left( {x + }\right) \) de \( f \) en \( x \) existent, et que \( f\left( {a + }\right) \) et \( f\left( {b - }\right) \) existent.

> EXERCISE 7. Let \( \left\lbrack {a, b}\right\rbrack \) be a segment of \( \mathbb{R} \) (with \( a < b \)), \( \left( {E,\mathrm{\;d}}\right) \) a metric space, and \( f : \left\lbrack {a, b}\right\rbrack \rightarrow E \) a map. Suppose that for all \( x \in \rbrack a, b\lbrack \), the left-hand limits \( f\left( {x - }\right) \) and right-hand limits \( f\left( {x + }\right) \) of \( f \) at \( x \) exist, and that \( f\left( {a + }\right) \) and \( f\left( {b - }\right) \) exist.

a) Si \( x \in \rbrack a, b\left\lbrack \right. \) , on note \( \omega \left( {f, x}\right) = \max \{ \mathrm{d}\left( {f\left( {x - }\right) , f\left( x\right) }\right) ,\mathrm{d}\left( {f\left( x\right) , f\left( {x + }\right) }\right) \} \) . Soit \( \varepsilon > 0 \) et

> a) If \( x \in \rbrack a, b\left\lbrack \right. \), we denote \( \omega \left( {f, x}\right) = \max \{ \mathrm{d}\left( {f\left( {x - }\right) , f\left( x\right) }\right) ,\mathrm{d}\left( {f\left( x\right) , f\left( {x + }\right) }\right) \} \). Let \( \varepsilon > 0 \) and

\[
{A}_{\varepsilon } = \{ x \in  \rbrack a, b\left\lbrack  {\mid \omega \left( {f, x}\right)  \geq  \varepsilon \} .}\right.
\]

Montrer que l’ensemble \( {A}_{\varepsilon } \) est fini.

> Show that the set \( {A}_{\varepsilon } \) is finite.

b) Montrer que l’ensemble des points de discontinuité de \( f \) est au plus dénombrable. c) Soit \( \varepsilon > 0 \) et \( x \in \rbrack a, b\left\lbrack \right. \) tel que \( \omega \left( {f, x}\right) < \varepsilon \) . Montrer

> b) Show that the set of points of discontinuity of \( f \) is at most countable. c) Let \( \varepsilon > 0 \) and \( x \in \rbrack a, b\left\lbrack \right. \) such that \( \omega \left( {f, x}\right) < \varepsilon \). Show

\[
\exists \alpha  > 0,\forall y, z \in  \rbrack x - \alpha , x + \alpha \lbrack \;\mathrm{d}\left( {f\left( y\right) , f\left( z\right) }\right)  < {2\varepsilon }.
\]

d) Soit \( \varepsilon > 0 \) et \( \rbrack c, d\left\lbrack { \subset \left\lbrack {a, b}\right\rbrack \text{ tel que }\omega \left( {f, x}\right) < \varepsilon \text{ sur }}\right\rbrack c, d\lbrack \) . Montrer

> d) Let \( \varepsilon > 0 \) and \( \rbrack c, d\left\lbrack { \subset \left\lbrack {a, b}\right\rbrack \text{ tel que }\omega \left( {f, x}\right) < \varepsilon \text{ sur }}\right\rbrack c, d\lbrack \) . Show

\[
\exists \alpha  > 0,\forall x, y \in  \rbrack c, d\lbrack ,\mathrm{\;d}\left( {x, y}\right)  < \alpha ,\;\mathrm{d}\left( {f\left( x\right) , f\left( y\right) }\right)  < {2\varepsilon }.
\]

Solution. a) Raisonnons par l’absurde et supposons \( {A}_{\varepsilon } \) infini. Comme \( {A}_{\varepsilon } \) est inclus dans le compact \( I \) , il en existe un point d’accumulation \( x \in I \) . Ainsi, il existe une suite \( \left( {x}_{n}\right) \) de points distincts de \( {A}_{\varepsilon } \) qui converge vers \( x \) .

> Solution. a) Let us reason by contradiction and assume \( {A}_{\varepsilon } \) is infinite. Since \( {A}_{\varepsilon } \) is included in the compact set \( I \) , it has an accumulation point \( x \in I \) . Thus, there exists a sequence \( \left( {x}_{n}\right) \) of distinct points of \( {A}_{\varepsilon } \) that converges to \( x \) .

S’il existe une infinité de valeurs de \( n \) pour lesquelles \( {x}_{n} < x \) , on peut, quitte à extraire une sous-suite de \( \left( {x}_{n}\right) \) , supposer \( {x}_{n} < x \) pour tout \( n \) . On a \( x \in \rbrack a, b\rbrack \) et d’après les hypothèses, \( f \) admet une limite à gauche en \( x \) . Il existe donc \( \alpha > 0 \) tel que

> If there exist infinitely many values of \( n \) for which \( {x}_{n} < x \) , we can, by extracting a subsequence of \( \left( {x}_{n}\right) \) , assume \( {x}_{n} < x \) for all \( n \) . We have \( x \in \rbrack a, b\rbrack \) and, according to the hypotheses, \( f \) has a left-hand limit at \( x \) . There therefore exists \( \alpha > 0 \) such that

\[
\forall y \in  \rbrack x - \alpha , x\lbrack ,\;\mathrm{d}\left( {f\left( y\right) , f\left( {x - }\right) }\right)  < \varepsilon /3.
\]

(*)

> Comme \( \left( {x}_{n}\right) \) converge vers \( x \) par valeurs inférieures, il existe un entier naturel \( n \) , désormais fixé, tel que \( x - \alpha < {x}_{n} < x \) . D’après (*), on a l’inégalité

Since \( \left( {x}_{n}\right) \) converges to \( x \) from below, there exists a natural number \( n \) , now fixed, such that \( x - \alpha < {x}_{n} < x \) . According to (*), we have the inequality

\[
\forall y \in  \rbrack x - \alpha ,{x}_{n}\left\lbrack  {,\;\mathrm{d}\left( {f\left( y\right) , f\left( {x}_{n}\right) }\right)  \leq  \mathrm{d}\left( {f\left( y\right) , f\left( {x - }\right) }\right)  + \mathrm{d}\left( {f\left( {x - }\right) , f\left( {x}_{n}\right) }\right)  < {2\varepsilon }/3,}\right.
\]

et en faisant tendre \( y \) vers \( {x}_{n} \) , on en déduit \( \mathrm{d}\left( {f\left( {{x}_{n} - }\right) , f\left( {x}_{n}\right) }\right) \leq {2\varepsilon }/3 \) . De même l’inégalité

> and by letting \( y \) tend to \( {x}_{n} \) , we deduce \( \mathrm{d}\left( {f\left( {{x}_{n} - }\right) , f\left( {x}_{n}\right) }\right) \leq {2\varepsilon }/3 \) . Similarly, the inequality

\[
\forall y \in  \rbrack {x}_{n}, x\lbrack ,\;\mathrm{\;d}\left( {f\left( {x}_{n}\right) , f\left( y\right) }\right)  \leq  \mathrm{d}\left( {f\left( {x}_{n}\right) , f\left( {x - }\right) }\right)  + \mathrm{d}\left( {f\left( {x - }\right) , f\left( y\right) }\right)  < {2\varepsilon }/3,
\]

conduit par passage à la limite à \( \mathrm{d}\left( {f\left( {x}_{n}\right) , f\left( {{x}_{n} + }\right) }\right) \leq {2\varepsilon }/3 \) . On a donc \( \omega \left( {f,{x}_{n}}\right) \leq {2\varepsilon }/3 \) . Donc \( {x}_{n} \notin {A}_{\varepsilon } \) , ce qui est absurde.

> leads by passing to the limit to \( \mathrm{d}\left( {f\left( {x}_{n}\right) , f\left( {{x}_{n} + }\right) }\right) \leq {2\varepsilon }/3 \) . We thus have \( \omega \left( {f,{x}_{n}}\right) \leq {2\varepsilon }/3 \) . Therefore \( {x}_{n} \notin {A}_{\varepsilon } \) , which is absurd.

Dans le cas où il existe une infinité de valeurs de \( n \) pour lesquelles \( {x}_{n} > x \) , on aboutirait de la même manière à une absurdité en utilisant la continuité à droite de \( f \) en \( x \) .

> In the case where there exist infinitely many values of \( n \) for which \( {x}_{n} > x \) , we would arrive at an absurdity in the same way by using the right-continuity of \( f \) at \( x \) .

L’ensemble \( {A}_{\varepsilon } \) est donc fini.

> The set \( {A}_{\varepsilon } \) is therefore finite.

b) La fonction \( f \) est discontinue en \( x \in \rbrack a, b\left\lbrack \right. \) si et seulement si \( \omega \left( {f, x}\right) > 0 \) . L’ensemble \( D \) des points de \( \rbrack a, b\left\lbrack \right. \) où \( f \) est discontinue est donc égal à \( { \cup }_{n \in {\mathbb{N}}^{ * }}{A}_{1/n} \) , réunion dénombrable d’ensembles finis, donc \( D \) est au plus dénombrable. En ajoutant éventuellement les points \( a \) et \( b \) , on en déduit que l’ensemble des points de discontinuité de \( f \) sur \( \left\lbrack {a, b}\right\rbrack \) est au plus dénombrable.

> b) The function \( f \) is discontinuous at \( x \in \rbrack a, b\left\lbrack \right. \) if and only if \( \omega \left( {f, x}\right) > 0 \) . The set \( D \) of points in \( \rbrack a, b\left\lbrack \right. \) where \( f \) is discontinuous is therefore equal to \( { \cup }_{n \in {\mathbb{N}}^{ * }}{A}_{1/n} \) , a countable union of finite sets, so \( D \) is at most countable. By possibly adding the points \( a \) and \( b \) , we deduce that the set of points of discontinuity of \( f \) on \( \left\lbrack {a, b}\right\rbrack \) is at most countable.

c) Posons \( \eta = \varepsilon - \omega \left( {f, x}\right) > 0 \) . Comme \( f \) est continue à gauche et à droite en \( x \) , il existe \( \alpha > 0 \) tel que \( \mathrm{d}\left( {f\left( y\right) , f\left( {x - }\right) }\right) < \eta \) pour \( y \in \rbrack x - \alpha , x\left\lbrack {\text{ et }\mathrm{d}\left( {f\left( y\right) , f\left( {x + }\right) }\right) < \eta \text{ pour }y \in }\right\rbrack x, x + \alpha \lbrack \) . On a alors

> c) Let \( \eta = \varepsilon - \omega \left( {f, x}\right) > 0 \) . Since \( f \) is left and right continuous at \( x \) , there exists \( \alpha > 0 \) such that \( \mathrm{d}\left( {f\left( y\right) , f\left( {x - }\right) }\right) < \eta \) for \( y \in \rbrack x - \alpha , x\left\lbrack {\text{ et }\mathrm{d}\left( {f\left( y\right) , f\left( {x + }\right) }\right) < \eta \text{ pour }y \in }\right\rbrack x, x + \alpha \lbrack \) . We then have

\[
\forall y \in  \rbrack x - \alpha , x + \alpha \lbrack ,\;\mathrm{d}\left( {f\left( y\right) , f\left( x\right) }\right)  < \varepsilon .
\]

\( \left( {* * }\right) \)

> En effet, si \( x - \alpha < y < x \) il suffit d’écrire \( \mathrm{d}\left( {f\left( y\right) , f\left( x\right) }\right) \leq \mathrm{d}\left( {f\left( y\right) , f\left( {x - }\right) }\right) + \mathrm{d}\left( {f\left( {x - }\right) , f\left( x\right) }\right) < \; \eta + \omega \left( {f, x}\right) = \varepsilon \) , et le cas \( x < y < x + \alpha \) se traite de la même manière. Lorsque \( y = x \) , le résultat (**) est évident.

Indeed, if \( x - \alpha < y < x \) it suffices to write \( \mathrm{d}\left( {f\left( y\right) , f\left( x\right) }\right) \leq \mathrm{d}\left( {f\left( y\right) , f\left( {x - }\right) }\right) + \mathrm{d}\left( {f\left( {x - }\right) , f\left( x\right) }\right) < \; \eta + \omega \left( {f, x}\right) = \varepsilon \) , and the case \( x < y < x + \alpha \) is handled in the same way. When \( y = x \) , the result (**) is obvious.

> On conclue facilement car d'après (**)

We conclude easily because according to (**)

\[
\forall y, z \in  \rbrack x - \alpha , x + \alpha \lbrack ,\;\mathrm{d}\left( {f\left( y\right) , f\left( z\right) }\right)  \leq  \mathrm{d}\left( {f\left( y\right) , f\left( x\right) }\right)  + \mathrm{d}\left( {f\left( x\right) , f\left( z\right) }\right)  < {2\varepsilon }.
\]

d) Supposons le résultat faux. Alors il existe une suite \( \left( {{x}_{n},{y}_{n}}\right) \) de \( \rbrack c, d\left\lbrack \right. \) telle que \( \left( {{x}_{n} - {y}_{n}}\right) \) tende vers 0 et telle que \( \mathrm{d}\left( {f\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right) \geq {2\varepsilon } \) pour tout \( n \) . La suite \( \left( {x}_{n}\right) \) est à valeur dans le compact \( \left\lbrack {c, d}\right\rbrack \) , donc on peut en extraire une sous-suite convergente \( \left( {x}_{\varphi \left( n\right) }\right) \) donc la limite \( x \) appartient à \( \left\lbrack {c, d}\right\rbrack \) . Comme \( \left( {{x}_{n} - {y}_{n}}\right) \) tend vers 0, la suite \( \left( {y}_{\varphi \left( n\right) }\right) \) converge également vers \( x \) .

> d) Suppose the result is false. Then there exists a sequence \( \left( {{x}_{n},{y}_{n}}\right) \) of \( \rbrack c, d\left\lbrack \right. \) such that \( \left( {{x}_{n} - {y}_{n}}\right) \) tends to 0 and such that \( \mathrm{d}\left( {f\left( {x}_{n}\right) , f\left( {y}_{n}\right) }\right) \geq {2\varepsilon } \) for all \( n \) . The sequence \( \left( {x}_{n}\right) \) takes values in the compact set \( \left\lbrack {c, d}\right\rbrack \) , so we can extract a convergent subsequence \( \left( {x}_{\varphi \left( n\right) }\right) \) , thus the limit \( x \) belongs to \( \left\lbrack {c, d}\right\rbrack \) . Since \( \left( {{x}_{n} - {y}_{n}}\right) \) tends to 0, the sequence \( \left( {y}_{\varphi \left( n\right) }\right) \) also converges to \( x \) .

Plusieurs cas se présentent, selon que la limite \( x \) est dans l’intérieur de \( \left\lbrack {c, d}\right\rbrack \) ou au bord.

> Several cases arise, depending on whether the limit \( x \) is in the interior of \( \left\lbrack {c, d}\right\rbrack \) or on the boundary.

(i) Le cas \( x \in \rbrack c, d\left\lbrack \right. \) est absurde car \( \left( {x}_{\varphi \left( n\right) }\right) \) et \( \left( {y}_{\varphi \left( n\right) }\right) \) tendent vers \( x \) et \( \mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) \geq \; {2\varepsilon } \) pour tout \( n \) , ce qui est absurde d’après le résultat de la question précédente.

> (i) The case \( x \in \rbrack c, d\left\lbrack \right. \) is absurd because \( \left( {x}_{\varphi \left( n\right) }\right) \) and \( \left( {y}_{\varphi \left( n\right) }\right) \) tend to \( x \) and \( \mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) \geq \; {2\varepsilon } \) for all \( n \) , which is absurd according to the result of the previous question.

(ii) Si \( x = c \) , alors comme \( f \) est continue à droite en \( c \) il existe \( \alpha > 0 \) tel que \( \mathrm{d}\left( {f\left( y\right) , f\left( {c + }\right) }\right) < \varepsilon \) pour tout \( y \in \rbrack c, c + \alpha \left\lbrack \right. \) . Comme \( \left( {x}_{\varphi \left( n\right) }\right) \) et \( \left( {y}_{\varphi \left( n\right) }\right) \) convergent vers \( c \) à droite, il existe \( n \) tel que \( {x}_{\varphi \left( n\right) } \) et \( {y}_{\varphi \left( n\right) } \) appartiennent à \( \rbrack c, c + \alpha \left\lbrack \right. \) , donc \( \left. {\mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) }\right) \leq \mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {c + }\right) }\right) + \; \mathrm{d}\left( {f\left( {c + }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) < {2\varepsilon } \) , ce qui est absurde car \( \mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) \geq {2\varepsilon } \) .

> (ii) If \( x = c \), then since \( f \) is right-continuous at \( c \), there exists \( \alpha > 0 \) such that \( \mathrm{d}\left( {f\left( y\right) , f\left( {c + }\right) }\right) < \varepsilon \) for all \( y \in \rbrack c, c + \alpha \left\lbrack \right. \). As \( \left( {x}_{\varphi \left( n\right) }\right) \) and \( \left( {y}_{\varphi \left( n\right) }\right) \) converge to \( c \) from the right, there exists \( n \) such that \( {x}_{\varphi \left( n\right) } \) and \( {y}_{\varphi \left( n\right) } \) belong to \( \rbrack c, c + \alpha \left\lbrack \right. \), thus \( \left. {\mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) }\right) \leq \mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {c + }\right) }\right) + \; \mathrm{d}\left( {f\left( {c + }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) < {2\varepsilon } \), which is absurd since \( \mathrm{d}\left( {f\left( {x}_{\varphi \left( n\right) }\right) , f\left( {y}_{\varphi \left( n\right) }\right) }\right) \geq {2\varepsilon } \).

(iii) Pour le cas \( x = d \) , on aboutit également à une absurdité en procédant de la même manière, en utilisant la continuité à gauche de \( f \) en \( d \) .

> (iii) For the case \( x = d \), we also reach an absurdity by proceeding in the same way, using the left-continuity of \( f \) at \( d \).

Ainsi, on a aboutit à une absurdité dans tous les cas, donc le résultat est bien vérifié.

> Thus, we have reached an absurdity in all cases, so the result is indeed verified.

Remarque. Le résultat de cet exercice permet de montrer qu'une fonction \( f \) à valeurs dans un e.v.n complet \( E \) et vérifiant les hypothèses de l’exercice est une fonction réglée (voir le théorème 4 page 99).

> Remark. The result of this exercise allows us to show that a function \( f \) with values in a complete n.v.s. \( E \) and satisfying the hypotheses of the exercise is a regulated function (see theorem 4 on page 99).

EXERCICE 8. Soit \( X \) un espace métrique compact. On note \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) l’algèbre des applications continues de \( X \) dans \( \mathbb{R} \) .

> EXERCISE 8. Let \( X \) be a compact metric space. Let \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) denote the algebra of continuous mappings from \( X \) to \( \mathbb{R} \).

a) Soit \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) un idéal de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Montrer

> a) Let \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) be an ideal of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Show

\[
\exists s \in  X,\forall f \in  \mathfrak{I},\;f\left( s\right)  = 0.
\]

b) Caractériser les idéaux maximaux de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) (i. e. les idéaux \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) tels que les seuls idéaux contenant \( \mathfrak{I} \) sont \( \mathfrak{I} \) et \( \mathcal{C}\left( {X,\mathbb{R}}\right) ) \) .

> b) Characterize the maximal ideals of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) (i.e., the ideals \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) such that the only ideals containing \( \mathfrak{I} \) are \( \mathfrak{I} \) and \( \mathcal{C}\left( {X,\mathbb{R}}\right) ) \) .

c) Déterminer la forme des morphismes d’algèbre de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) dans \( \mathbb{R} \) .

> c) Determine the form of the algebra morphisms from \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) to \( \mathbb{R} \) .

Solution. a) Raisonnons par l'absurde. Supposons que

> Solution. a) Let us reason by contradiction. Suppose that

\[
\forall s \in  X,\exists {f}_{s} \in  \mathfrak{I},\;{f}_{s}\left( s\right)  \neq  0.
\]

Pour tout \( s \in X \) , comme \( {f}_{s} \) est continue, il existe un voisinage ouvert \( {\Omega }_{s} \) de \( s \) tel que \( \forall x \in \; {\Omega }_{s},{f}_{s}\left( x\right) \neq 0 \) .

> For all \( s \in X \) , as \( {f}_{s} \) is continuous, there exists an open neighborhood \( {\Omega }_{s} \) of \( s \) such that \( \forall x \in \; {\Omega }_{s},{f}_{s}\left( x\right) \neq 0 \) .

Les \( {\left( {\Omega }_{s}\right) }_{s \in X} \) recouvrent le compact \( X \) . On peut donc en extraire un sous-recouvrement fini \( {\left( {\Omega }_{{s}_{i}}\right) }_{1 \leq i \leq n} \) . Comme \( \mathfrak{I} \) est un idéal, pour tout \( i,{f}_{{s}_{i}}^{2} \in \mathfrak{I} \) . Or \( {f}_{{s}_{i}}^{2} \) prend des valeurs strictement positives sur \( {\Omega }_{{s}_{i}} \) . Les \( {\left( {\Omega }_{{s}_{i}}\right) }_{1 \leq i \leq n} \) recouvrant \( X \) , la fonction \( f = \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{{s}_{i}}^{2} \) ne s’annule pas sur \( X \) . Comme \( \mathfrak{I} \) est un idéal, on a \( f \in \mathfrak{I} \) , et \( 1 = \left( {1/f}\right) \cdot f \in \mathfrak{I} \) donc \( \mathfrak{I} = \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Ceci contredit l’hypothèse \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Il existe donc \( s \in X \) tel que pour tout \( f \in \mathfrak{I}, f\left( s\right) = 0 \) .

> The \( {\left( {\Omega }_{s}\right) }_{s \in X} \) cover the compact set \( X \) . We can therefore extract a finite subcover \( {\left( {\Omega }_{{s}_{i}}\right) }_{1 \leq i \leq n} \) . Since \( \mathfrak{I} \) is an ideal, for all \( i,{f}_{{s}_{i}}^{2} \in \mathfrak{I} \) . However, \( {f}_{{s}_{i}}^{2} \) takes strictly positive values on \( {\Omega }_{{s}_{i}} \) . As the \( {\left( {\Omega }_{{s}_{i}}\right) }_{1 \leq i \leq n} \) cover \( X \) , the function \( f = \mathop{\sum }\limits_{{i = 1}}^{n}{f}_{{s}_{i}}^{2} \) does not vanish on \( X \) . Since \( \mathfrak{I} \) is an ideal, we have \( f \in \mathfrak{I} \) , and \( 1 = \left( {1/f}\right) \cdot f \in \mathfrak{I} \) therefore \( \mathfrak{I} = \mathcal{C}\left( {X,\mathbb{R}}\right) \) . This contradicts the hypothesis \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) . There exists therefore \( s \in X \) such that for all \( f \in \mathfrak{I}, f\left( s\right) = 0 \) .

b) Remarquons déjà que pour tout \( s \in X \) , l’ensemble \( {\mathfrak{J}}_{s} = \left\{ {f \in \mathcal{C}\left( {X,\mathbb{R}}\right) \mid f\left( s\right) = 0}\right\} \) est un idéal de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Nous allons montrer que les \( {\mathfrak{J}}_{s} \) sont les idéaux maximaux de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) .

> b) Let us first note that for all \( s \in X \) , the set \( {\mathfrak{J}}_{s} = \left\{ {f \in \mathcal{C}\left( {X,\mathbb{R}}\right) \mid f\left( s\right) = 0}\right\} \) is an ideal of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . We will show that the \( {\mathfrak{J}}_{s} \) are the maximal ideals of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) .

Pour tout \( s \in X \) , l’ensemble \( {\mathfrak{J}}_{s} \) est un idéal maximal de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . En effet, \( {\mathfrak{J}}_{s} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) et si \( \mathfrak{I} \) est un idéal contenant \( {\mathfrak{J}}_{s} \) et différent de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) , alors d’après a), il existe \( {s}^{\prime } \in X \) tel que \( \mathfrak{J} \subset {\mathfrak{J}}_{{s}^{\prime }} \) . On a alors \( {\mathfrak{J}}_{s} \subset {\mathfrak{J}}_{{s}^{\prime }} \) , ce qui n’est possible que si \( s = {s}^{\prime } \) , et donc \( \mathfrak{I} = {\mathfrak{J}}_{s} \) .

> For any \( s \in X \) , the set \( {\mathfrak{J}}_{s} \) is a maximal ideal of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Indeed, \( {\mathfrak{J}}_{s} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) and if \( \mathfrak{I} \) is an ideal containing \( {\mathfrak{J}}_{s} \) and distinct from \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) , then according to a), there exists \( {s}^{\prime } \in X \) such that \( \mathfrak{J} \subset {\mathfrak{J}}_{{s}^{\prime }} \) . We then have \( {\mathfrak{J}}_{s} \subset {\mathfrak{J}}_{{s}^{\prime }} \) , which is only possible if \( s = {s}^{\prime } \) , and therefore \( \mathfrak{I} = {\mathfrak{J}}_{s} \) .

Soit \( \mathfrak{I} \) un idéal maximal de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . On a \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) donc d’après a), il existe \( s \in X \) tel que \( \mathfrak{I} \subset {\mathfrak{J}}_{s} \) . Comme \( \mathfrak{I} \) est maximal et que \( {\mathfrak{J}}_{s} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) , on a \( \mathfrak{I} = {\mathfrak{J}}_{s} \) .

> Let \( \mathfrak{I} \) be a maximal ideal of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . We have \( \mathfrak{I} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) so according to a), there exists \( s \in X \) such that \( \mathfrak{I} \subset {\mathfrak{J}}_{s} \) . Since \( \mathfrak{I} \) is maximal and \( {\mathfrak{J}}_{s} \neq \mathcal{C}\left( {X,\mathbb{R}}\right) \) , we have \( \mathfrak{I} = {\mathfrak{J}}_{s} \) .

c) Soit \( \varphi \) un morphisme d’algèbre de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Supposons \( \varphi \) non nulle. L’ensemble Ker \( \varphi \) est un idéal de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) , différent de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) car \( \varphi \neq 0 \) . D’après a), il existe \( s \in X \) tel que Ker \( \varphi \subset {\mathfrak{J}}_{s} \) . La forme linéaire \( f \mapsto f\left( s\right) \) s’annule donc sur l’hyperplan Ker \( \varphi \) , et l’ensemble des formes linéaires s’annulant sur un hyperplan formant une droite du dual (voir le tome d’algèbre), il existe \( \lambda \in \mathbb{R} \) tel que \( f\left( s\right) = {\lambda \varphi }\left( f\right) \) pour tout \( f \in \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Soit \( f \in \mathcal{C}\left( {X,\mathbb{R}}\right) \) tel que \( f\left( s\right) \neq 0 \) . On a

> c) Let \( \varphi \) be an algebra morphism of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Suppose \( \varphi \) is non-zero. The set Ker \( \varphi \) is an ideal of \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) , distinct from \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) because \( \varphi \neq 0 \) . According to a), there exists \( s \in X \) such that Ker \( \varphi \subset {\mathfrak{J}}_{s} \) . The linear form \( f \mapsto f\left( s\right) \) therefore vanishes on the hyperplane Ker \( \varphi \) , and since the set of linear forms vanishing on a hyperplane forms a line in the dual (see the algebra volume), there exists \( \lambda \in \mathbb{R} \) such that \( f\left( s\right) = {\lambda \varphi }\left( f\right) \) for all \( f \in \mathcal{C}\left( {X,\mathbb{R}}\right) \) . Let \( f \in \mathcal{C}\left( {X,\mathbb{R}}\right) \) be such that \( f\left( s\right) \neq 0 \) . We have

\[
\lambda \left( {f}^{2}\right) \left( s\right)  = {\lambda }^{2}\varphi \left( {f}^{2}\right)  = {\lambda }^{2}\varphi {\left( f\right) }^{2} = {f}^{2}\left( s\right) ,
\]

donc \( \lambda = 1 \) . Finalement \( \varphi \left( f\right) = f\left( s\right) \) pour tout \( f \) .

> therefore \( \lambda = 1 \) . Finally \( \varphi \left( f\right) = f\left( s\right) \) for all \( f \) .

En résumé, les morphismes d’algèbre de \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) dans \( \mathbb{R} \) sont l’application nulle et les mor-phismes de la forme \( f \mapsto f\left( s\right) \) , où \( s \in X \) .

> In summary, the algebra morphisms from \( \mathcal{C}\left( {X,\mathbb{R}}\right) \) to \( \mathbb{R} \) are the zero map and the morphisms of the form \( f \mapsto f\left( s\right) \) , where \( s \in X \) .
