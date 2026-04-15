#### 1.1. Reminders on sequences

*Français : 1.1. Rappels sur les suites*

Nous avons déjà abordé la notion de suite au cours du chapitre de topologie sur les espaces métriques. Rappelons en les grandes lignes.

> We have already addressed the notion of a sequence during the topology chapter on metric spaces. Let us recall the main points.

- On appelle suite à valeurs dans un ensemble \( E \) toute application \( u \) de \( \mathbb{N} \) dans \( E \) . Le terme \( u\left( n\right) \) est appelé le \( n \) -ième terme de la suite et on le note \( {u}_{n} \) . La suite \( u \) est notée \( {\left( {u}_{n}\right) }_{n \in  \mathbb{N}} \) .

> - A sequence with values in a set \( E \) is any mapping \( u \) from \( \mathbb{N} \) to \( E \). The term \( u\left( n\right) \) is called the \( n \)-th term of the sequence and is denoted by \( {u}_{n} \). The sequence \( u \) is denoted by \( {\left( {u}_{n}\right) }_{n \in  \mathbb{N}} \).

- Une suite \( \left( {u}_{n}\right) \) à valeurs dans un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est dite convergente s’il existe \( \ell  \in  E \) tel que

> - A sequence \( \left( {u}_{n}\right) \) with values in a metric space \( \left( {E,\mathrm{\;d}}\right) \) is said to be convergent if there exists \( \ell  \in  E \) such that

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall n \geq  N,\;\mathrm{\;d}\left( {{u}_{n},\ell }\right)  \leq  \varepsilon .
\]

Dans ce cas, il existe une seule valeur \( \ell \) vérifiant cette propriété, et on dit que \( \ell \) est la limite de \( \left( {u}_{n}\right) \) ou que \( \left( {u}_{n}\right) \) converge vers \( \ell \) . On note alors \( \ell = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{n} \) .

> In this case, there exists a unique value \( \ell \) satisfying this property, and we say that \( \ell \) is the limit of \( \left( {u}_{n}\right) \) or that \( \left( {u}_{n}\right) \) converges to \( \ell \). We then write \( \ell = \mathop{\lim }\limits_{{n \rightarrow + \infty }}{u}_{n} \).

- On appelle sous-suite (ou suite extraite) de \( \left( {u}_{n}\right) \) toute suite \( \left( {v}_{n}\right) \) de la forme \( {v}_{n} = \; {u}_{\varphi \left( n\right) } \) où \( \varphi \) est une application strictement croissante de \( \mathbb{N} \) sur \( \mathbb{N} \) .

> - A subsequence (or extracted sequence) of \( \left( {u}_{n}\right) \) is any sequence \( \left( {v}_{n}\right) \) of the form \( {v}_{n} = \; {u}_{\varphi \left( n\right) } \) where \( \varphi \) is a strictly increasing mapping from \( \mathbb{N} \) to \( \mathbb{N} \).

Avec ces définitions, on a les propriétés qui suivent.

> With these definitions, we have the following properties.

- Toute sous-suite d'une suite convergente est convergente et possède la même limite.

> - Every subsequence of a convergent sequence is convergent and has the same limit.

- Une suite \( \left( {u}_{n}\right) \) à valeurs dans un espace métrique est dite bornée s’il existe \( M > 0 \) tel que \( \mathrm{d}\left( {{u}_{0},{u}_{n}}\right)  \leq  M \) pour tout \( n \in  \mathbb{N} \) . Toute suite convergente est bornée.

> - A sequence \( \left( {u}_{n}\right) \) with values in a metric space is said to be bounded if there exists \( M > 0 \) such that \( \mathrm{d}\left( {{u}_{0},{u}_{n}}\right)  \leq  M \) for all \( n \in  \mathbb{N} \). Every convergent sequence is bounded.

- Si \( \left( {u}_{n}\right) \) est une suite bornée à valeurs dans \( {\mathbb{R}}^{p} \) , on peut en extraire une sous-suite convergente (voir la proposition 11 page 30).

> - If \( \left( {u}_{n}\right) \) is a bounded sequence with values in \( {\mathbb{R}}^{p} \), one can extract a convergent subsequence (see proposition 11 on page 30).

- Une suite \( \left( {u}_{n}\right) \) à valeurs dans un espace métrique \( \left( {E,\mathrm{\;d}}\right) \) est dite de Cauchy si

> - A sequence \( \left( {u}_{n}\right) \) with values in a metric space \( \left( {E,\mathrm{\;d}}\right) \) is said to be Cauchy if

\[
\forall \varepsilon  > 0,\exists N \in  \mathbb{N},\forall p \geq  N,\forall q \geq  N,\;\mathrm{\;d}\left( {{u}_{p},{u}_{q}}\right)  < \varepsilon .
\]

Toute suite convergente est de Cauchy, toute suite de Cauchy est bornée. Si \( E \) est complet, toute suite de Cauchy converge. En particulier, toute suite de Cauchy dans \( {\mathbb{R}}^{p} \) converge.

> Every convergent sequence is Cauchy; every Cauchy sequence is bounded. If \( E \) is complete, every Cauchy sequence converges. In particular, every Cauchy sequence in \( {\mathbb{R}}^{p} \) converges.

Suites réelles.

> Real sequences.

- Une suite réelle \( \left( {u}_{n}\right) \) est dite majorée (resp. minorée) s’il existe \( M \in  \mathbb{R} \) tel que \( {u}_{n} \leq  M \) (resp. \( {u}_{n} \geq  M \) ) pour tout \( n \in  \mathbb{N} \) . Une suite croissante et majorée converge.

> - A real sequence \( \left( {u}_{n}\right) \) is said to be bounded above (resp. bounded below) if there exists \( M \in  \mathbb{R} \) such that \( {u}_{n} \leq  M \) (resp. \( {u}_{n} \geq  M \)) for all \( n \in  \mathbb{N} \). An increasing sequence that is bounded above converges.

- Les inégalités larges sont conservées par passage à la limite.

> - Non-strict inequalities are preserved when taking the limit.

- Si trois suites \( \left( {u}_{n}\right) ,\left( {v}_{n}\right) \) et \( \left( {w}_{n}\right) \) vérifient

> - If three sequences \( \left( {u}_{n}\right) ,\left( {v}_{n}\right) \) and \( \left( {w}_{n}\right) \) satisfy

\[
\forall n \in  \mathbb{N},\;{v}_{n} \leq  {u}_{n} \leq  {w}_{n}
\]

et si \( \left( {v}_{n}\right) \) et \( \left( {w}_{n}\right) \) convergent vers une même limite \( \ell \) , alors \( \left( {u}_{n}\right) \) converge vers \( \ell \) .

> and if \( \left( {v}_{n}\right) \) and \( \left( {w}_{n}\right) \) converge to the same limit \( \ell \), then \( \left( {u}_{n}\right) \) converges to \( \ell \).

- Deux suites réelles \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) sont dites adjacentes si l’une est croissante, l’autre décroissante, et si

> - Two real sequences \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) are said to be adjacent if one is increasing, the other is decreasing, and if

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{u}_{n} - {v}_{n} = 0
\]

Dans ce cas, \( \left( {u}_{n}\right) \) et \( \left( {v}_{n}\right) \) sont convergentes et convergent vers la même limite.

> In this case, \( \left( {u}_{n}\right) \) and \( \left( {v}_{n}\right) \) are convergent and converge to the same limit.
