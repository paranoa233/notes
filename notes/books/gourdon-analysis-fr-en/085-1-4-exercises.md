#### 1.4. Exercises

*Français : 1.4. Exercices*

EXERCICE 1. Étudier la suite \( \left( {u}_{n}\right) \) définie par

> EXERCISE 1. Study the sequence \( \left( {u}_{n}\right) \) defined by

\[
{u}_{0} > 0\;\text{ et }\;\forall n \in  \mathbb{N},\;{u}_{n + 1} = \frac{1}{2 - \sqrt{{u}_{n}}}.
\]

La monotonie de \( \left( {u}_{n}\right) \) est dictée par le signe de \( g\left( x\right) = f\left( x\right) - x \) ; un calcul simple montre que

> The monotonicity of \( \left( {u}_{n}\right) \) is dictated by the sign of \( g\left( x\right) = f\left( x\right) - x \) ; a simple calculation shows that

\[
\forall x \in  \lbrack 0,4\lbrack ,\;g\left( x\right)  = f\left( x\right)  - x = \frac{\left( {\sqrt{x} - 1}\right) \left( {\sqrt{x} - \frac{1 + \sqrt{5}}{2}}\right) \left( {\sqrt{x} - \frac{1 - \sqrt{5}}{2}}\right) }{2 - \sqrt{x}},
\]

---

Solution. Pour que la suite \( \left( {u}_{n}\right) \) soit bien définie, il faut avoir \( {u}_{n} \geq 0 \) pour tout \( n \) , ce qui sera vérifié si et seulement si \( 0 \leq {u}_{n} < 4 \) pour tout \( n \) .

> Solution. For the sequence \( \left( {u}_{n}\right) \) to be well-defined, we must have \( {u}_{n} \geq 0 \) for all \( n \) , which will be satisfied if and only if \( 0 \leq {u}_{n} < 4 \) for all \( n \) .

Ceci étant, on a

> Given this, we have

\[
\forall n \in  \mathbb{N},\;{u}_{n + 1} = f\left( {u}_{n}\right) \;\text{ où }\;f : \left\lbrack  {0,4\lbrack  \rightarrow  \mathbb{R}\;x \mapsto  \frac{1}{2 - \sqrt{x}}.}\right.
\]

---

d’où le tableau suivant, donnant le comportement de \( f \) et le signe de \( g \) :

> hence the following table, giving the behavior of \( f \) and the sign of \( g \) :

<table><tr><td>\( x \)</td><td>0</td><td></td><td>1</td><td></td><td>\( \frac{3 + \sqrt{5}}{2} \)</td><td></td><td>4</td></tr><tr><td>\( f\left( x\right) \)</td><td>\( \frac{1}{2} \)</td><td>↗</td><td>1</td><td>↗</td><td>\( \frac{3 + \sqrt{5}}{2} \)</td><td>↗</td><td>\( + \infty \)</td></tr><tr><td>\( g\left( x\right) \)</td><td>\( \frac{1}{2} \)</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td><td></td></tr></table>

> <table><tbody><tr><td>\( x \)</td><td>0</td><td></td><td>1</td><td></td><td>\( \frac{3 + \sqrt{5}}{2} \)</td><td></td><td>4</td></tr><tr><td>\( f\left( x\right) \)</td><td>\( \frac{1}{2} \)</td><td>↗</td><td>1</td><td>↗</td><td>\( \frac{3 + \sqrt{5}}{2} \)</td><td>↗</td><td>\( + \infty \)</td></tr><tr><td>\( g\left( x\right) \)</td><td>\( \frac{1}{2} \)</td><td>+</td><td>0</td><td>-</td><td>0</td><td>+</td><td></td></tr></tbody></table>

Nous avons vu que forcément, \( {u}_{0} \in \lbrack 0,4\lbrack \) pour que la suite \( \left( {u}_{n}\right) \) soit définie. Pour étudier \( \left( {u}_{n}\right) \) , nous traitons plusieurs cas selon la position de \( {u}_{0} \) par rapport aux points fixes de \( f \) .

> We have seen that necessarily, \( {u}_{0} \in \lbrack 0,4\lbrack \) for the sequence \( \left( {u}_{n}\right) \) to be defined. To study \( \left( {u}_{n}\right) \), we treat several cases according to the position of \( {u}_{0} \) relative to the fixed points of \( f \).

(i) \( {u}_{0} \in \lbrack 0,1\lbrack \) . Le tableau montre que \( \lbrack 0,1\lbrack \) est stable par \( f \) , on a donc \( {u}_{n} \in \lbrack 0,1\lbrack \) pour tout \( n \) . Par ailleurs, \( g \) est positive sur cet intervalle, donc la suite \( \left( {u}_{n}\right) \) est croissante. Comme elle est majorée (par 1), elle converge. Sa limite \( \ell \) vérifie \( f\left( \ell \right) = \ell \) , c’est-à-dire \( g\left( \ell \right) = 0 \) . Comme de plus \( \ell \in \left\lbrack {0,1}\right\rbrack \) car la suite prend ses valeurs dans \( \lbrack 0,1\lbrack \) , on a forcément \( \ell = 1 \) . En résumé, \( \left( {u}_{n}\right) \) tend vers 1 en croissant.

> (i) \( {u}_{0} \in \lbrack 0,1\lbrack \). The table shows that \( \lbrack 0,1\lbrack \) is stable under \( f \), so we have \( {u}_{n} \in \lbrack 0,1\lbrack \) for all \( n \). Furthermore, \( g \) is positive on this interval, so the sequence \( \left( {u}_{n}\right) \) is increasing. Since it is bounded above (by 1), it converges. Its limit \( \ell \) satisfies \( f\left( \ell \right) = \ell \), that is to say \( g\left( \ell \right) = 0 \). As moreover \( \ell \in \left\lbrack {0,1}\right\rbrack \) because the sequence takes its values in \( \lbrack 0,1\lbrack \), we necessarily have \( \ell = 1 \). In summary, \( \left( {u}_{n}\right) \) tends to 1 while increasing.

(ii) \( {u}_{0} = 1 \) . Alors la suite \( \left( {u}_{n}\right) \) est stationnaire à 1 .

> (ii) \( {u}_{0} = 1 \). Then the sequence \( \left( {u}_{n}\right) \) is stationary at 1.

(iii) \( {u}_{0} \in \rbrack 1,\left( {3 + \sqrt{5}}\right) /2\lbrack \) . Comme l’intervalle \( \rbrack 1,\left( {3 + \sqrt{5}}\right) /2\lbrack \) est stable par \( f \) , tous les éléments de la suite appartiennent à cet intervalle. Comme \( g \) y est négative, \( \left( {u}_{n}\right) \) décroît. De plus, \( \left( {u}_{n}\right) \) est minorée (par 1), on en déduit qu’elle converge. Sa limite \( \ell \) vérifie \( g\left( \ell \right) = 0 \) et \( 1 \leq \ell < \left( {3 + \sqrt{5}}\right) /2 \) , donc \( \ell = 1 \) . En résumé, \( \left( {u}_{n}\right) \) tend vers 1 en décroissant.

> (iii) \( {u}_{0} \in \rbrack 1,\left( {3 + \sqrt{5}}\right) /2\lbrack \). Since the interval \( \rbrack 1,\left( {3 + \sqrt{5}}\right) /2\lbrack \) is stable under \( f \), all elements of the sequence belong to this interval. As \( g \) is negative there, \( \left( {u}_{n}\right) \) decreases. Moreover, \( \left( {u}_{n}\right) \) is bounded below (by 1), we deduce that it converges. Its limit \( \ell \) satisfies \( g\left( \ell \right) = 0 \) and \( 1 \leq \ell < \left( {3 + \sqrt{5}}\right) /2 \), therefore \( \ell = 1 \). In summary, \( \left( {u}_{n}\right) \) tends to 1 while decreasing.

(iv) \( {u}_{0} = \left( {3 + \sqrt{5}}\right) /2 \) . Alors la suite \( \left( {u}_{n}\right) \) est stationnaire à \( \left( {3 + \sqrt{5}}\right) /2 \) .

> (iv) \( {u}_{0} = \left( {3 + \sqrt{5}}\right) /2 \). Then the sequence \( \left( {u}_{n}\right) \) is stationary at \( \left( {3 + \sqrt{5}}\right) /2 \).

(v) \( {u}_{0} > \left( {3 + \sqrt{5}}\right) /2 \) . Alors la suite \( \left( {u}_{n}\right) \) est croissante \( \left( {g\text{ est positive sur }\rbrack \left( {3 + \sqrt{5}}\right) /2,4\lbrack }\right) \) ; si elle était majorée par 4, elle convergerait vers un réel \( \ell > \left( {3 + \sqrt{5}}\right) /2 \) point fixe de \( f \) , ce qui n’est pas possible. Ainsi, il existe \( n \) tel que \( {u}_{n} > 4 \) et la suite \( \left( {u}_{n}\right) \) n’est pas définie.

> (v) \( {u}_{0} > \left( {3 + \sqrt{5}}\right) /2 \). Then the sequence \( \left( {u}_{n}\right) \) is increasing \( \left( {g\text{ est positive sur }\rbrack \left( {3 + \sqrt{5}}\right) /2,4\lbrack }\right) \); if it were bounded above by 4, it would converge to a real number \( \ell > \left( {3 + \sqrt{5}}\right) /2 \) which is a fixed point of \( f \), which is not possible. Thus, there exists \( n \) such that \( {u}_{n} > 4 \) and the sequence \( \left( {u}_{n}\right) \) is not defined.

\( \rightarrow \) EXERCICE 2 (MOYENNE DE CÉSARO). Soit \( {\left( {a}_{n}\right) }_{n \geq 1} \) une suite complexe convergente, de limite \( \ell \) . Montrer que la suite \( {\left( {b}_{n}\right) }_{n \geq 1} \) définie par

> \( \rightarrow \) EXERCISE 2 (CÉSARO MEAN). Let \( {\left( {a}_{n}\right) }_{n \geq 1} \) be a convergent complex sequence with limit \( \ell \) . Show that the sequence \( {\left( {b}_{n}\right) }_{n \geq 1} \) defined by

\[
\forall n \geq  1,\;{b}_{n} = \frac{{a}_{1} + \cdots  + {a}_{n}}{n}
\]

converge vers \( \ell \) .

> converges to \( \ell \) .

Solution. Donnons nous \( \varepsilon > 0 \) . La suite \( \left( {a}_{n}\right) \) converge vers \( \ell \) donc

> Solution. Let \( \varepsilon > 0 \) be given. The sequence \( \left( {a}_{n}\right) \) converges to \( \ell \) , therefore

\[
\exists N \in  {\mathbb{N}}^{ * },\forall n > N,\;\left| {{a}_{n} - \ell }\right|  \leq  \varepsilon .
\]

Ainsi, pour tout \( n > N \) ,

> Thus, for all \( n > N \) ,

\[
\forall n > N,\;\left| {{a}_{1} + {a}_{2} + \cdots  + {a}_{n} - n\ell }\right|  \leq  \left| {{a}_{1} + \cdots  + {a}_{N} - N\ell }\right|  + \left| {{a}_{N + 1} + \cdots  + {a}_{n} - \left( {N - n}\right) \ell }\right|
\]

\[
\leq  \left| {{a}_{1} + \cdots  + {a}_{N} - N\ell }\right|  + \left| {{a}_{N + 1} - \ell }\right|  + \cdots  + \left| {{a}_{n} - \ell }\right|  \leq  K + \left( {n - N}\right) \varepsilon  \leq  K + {n\varepsilon },
\]

où \( K = \left| {{a}_{1} + \cdots + {a}_{N} - N\ell }\right| \) , ce qui entraîne

> where \( K = \left| {{a}_{1} + \cdots + {a}_{N} - N\ell }\right| \) , which implies

\[
\forall n > N,\;\left| {{b}_{n} - \ell }\right|  = \left| {\frac{{a}_{1} + \cdots  + {a}_{n}}{n} - \ell }\right|  \leq  \frac{K}{n} + \varepsilon .
\]

Si on fixe un entier \( {N}_{1} > N \) tel que \( K/{N}_{1} < \varepsilon \) , on a finalement

> If we fix an integer \( {N}_{1} > N \) such that \( K/{N}_{1} < \varepsilon \) , we finally have

\[
\forall n \geq  {N}_{1},\;\left| {{b}_{n} - \ell }\right|  \leq  \frac{K}{{N}_{1}} + \varepsilon  \leq  {2\varepsilon },
\]

d'où le résultat.

> hence the result.

Remarque. En procédant de la même manière, on peut montrer plus généralement que pour toute suite de réels positifs \( \left( {\varepsilon }_{n}\right) \) telle que la série \( \sum {\varepsilon }_{n} \) diverge, on a

> Remark. By proceeding in the same way, one can show more generally that for any sequence of positive reals \( \left( {\varepsilon }_{n}\right) \) such that the series \( \sum {\varepsilon }_{n} \) diverges, we have

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}\frac{{\varepsilon }_{1}{a}_{1} + \cdots  + {\varepsilon }_{n}{a}_{n}}{{\varepsilon }_{1} + \cdots  + {\varepsilon }_{n}} = \ell .
\]

EXERCICE 3. Soit \( \left( {u}_{n}\right) \) une suite définie par

> EXERCISE 3. Let \( \left( {u}_{n}\right) \) be a sequence defined by

\[
{u}_{0} > 0,{u}_{1} > 0,\lambda  > 0,\;\forall n \in  \mathbb{N},\;{u}_{n + 2} = \lambda \sqrt{{u}_{n + 1}{u}_{n}}.
\]

Expliciter le \( n \) -ième terme \( {u}_{n} \) de la suite en fonction de \( n \) .

> Express the \( n \) -th term \( {u}_{n} \) of the sequence in terms of \( n \) .

Solution. Une récurrence immédiate montre que chaque terme de la suite est positif, donc la suite \( \left( {u}_{n}\right) \) est bien définie. La suite \( \left( {u}_{n}\right) \) est récurrente d’ordre 2, mais elle n’entre pas dans une des familles classiques étudiées dans la partie 1.3. Pour se ramener à une récurrence classique, nous allons considérer la suite \( \left( {v}_{n}\right) \) définie par \( {v}_{n} = \log {u}_{n} \) . Elle vérifie

> Solution. An immediate induction shows that each term of the sequence is positive, so the sequence \( \left( {u}_{n}\right) \) is well-defined. The sequence \( \left( {u}_{n}\right) \) is a second-order recurrence, but it does not fall into one of the classical families studied in part 1.3. To reduce it to a classical recurrence, we will consider the sequence \( \left( {v}_{n}\right) \) defined by \( {v}_{n} = \log {u}_{n} \) . It satisfies

\[
\forall n \in  \mathbb{N},\;{v}_{n + 2} = \frac{{v}_{n + 1}}{2} + \frac{{v}_{n}}{2} + \log \lambda .
\]

(*)

> Pour rendre homogène cette récurrence linéaire, nous commençons par en rechercher une solution particulière (c'est comme pour les équations différentielles). Aucune suite constante ne convient, on recherche donc une solution particulière \( \left( {w}_{n}\right) \) sous la forme \( {w}_{n} = {\alpha n} \) . Elle vérifie (*) si et seulement si

To make this linear recurrence homogeneous, we begin by looking for a particular solution (similar to differential equations). No constant sequence works, so we look for a particular solution \( \left( {w}_{n}\right) \) in the form \( {w}_{n} = {\alpha n} \) . It satisfies (*) if and only if

\[
\forall n \in  \mathbb{N},\;\alpha \left( {n + 2}\right)  = \alpha \left( {n + \frac{1}{2}}\right)  + \log \lambda ,\;\text{ ce qui équivaut à }\alpha  = \frac{2}{3}\log \lambda .
\]

Ainsi, la suite \( \left( {w}_{n}\right) \) définie par \( {w}_{n} = \left( {2\log \lambda /3}\right) n \) vérifie (*), ce qui en retranchant à (*) montre que la suite \( \left( {x}_{n}\right) \) définie par \( {x}_{n} = {v}_{n} - {w}_{n} \) vérifie

> Thus, the sequence \( \left( {w}_{n}\right) \) defined by \( {w}_{n} = \left( {2\log \lambda /3}\right) n \) satisfies (*), which, by subtracting from (*), shows that the sequence \( \left( {x}_{n}\right) \) defined by \( {x}_{n} = {v}_{n} - {w}_{n} \) satisfies

\[
\forall n \in  \mathbb{N},\;{x}_{n + 2} = \frac{{x}_{n + 1}}{2} + \frac{{x}_{n}}{2}.
\]

On sait résoudre ce type de récurrence. L'équation caractéristique correspondante est

> We know how to solve this type of recurrence. The corresponding characteristic equation is

\[
{r}^{2} - \frac{1}{2}r - \frac{1}{2} = 0\;\text{ dont les solutions sont }r =  - \frac{1}{2}, r = 1.
\]

Ainsi, il existe \( a, b \in \mathbb{R} \) tels que

> Thus, there exist \( a, b \in \mathbb{R} \) such that

\[
\forall n \in  \mathbb{N},\;{x}_{n} = a + {\left( -\frac{1}{2}\right) }^{n}b\;\text{ donc }\;\forall n \in  \mathbb{N},\;{v}_{n} = {x}_{n} + {w}_{n} = a + {\left( -\frac{1}{2}\right) }^{n}b + \frac{2\log \lambda }{3}n,
\]

et finalement

> and finally

\[
\forall n \in  \mathbb{N},\;{u}_{n} = \exp \left( {v}_{n}\right)  = A \cdot  {B}^{{\left( -1/2\right) }^{n}} \cdot  {\lambda }^{{2n}/3},\;A = {e}^{a}, B = {e}^{b}.
\]

Pour déterminer \( A \) et \( B \) , on écrit

> To determine \( A \) and \( B \), we write

\[
{u}_{0} = {AB},\;{u}_{1} = A \cdot  \frac{1}{\sqrt{B}}{\lambda }^{2/3}\;\text{ d’où on déduit }\;A = {u}_{0}^{1/3}{u}_{1}^{2/3}{\lambda }^{-4/9},\;B = {u}_{0}^{2/3}{u}_{1}^{-2/3}{\lambda }^{4/9}.
\]

Finalement, nous avons montré

> Finally, we have shown

\[
\forall n \in  \mathbb{N},\;{u}_{n} = {u}_{0}^{1/3}{u}_{1}^{2/3}{\lambda }^{-4/9}{\left( \frac{{u}_{0}{\lambda }^{2/3}}{{u}_{1}}\right) }^{\left( {2/3}\right) {\left( -1/2\right) }^{n}}{\lambda }^{{2n}/3}.
\]

Remarque. Retenez le procédé qui consiste à rechercher une solution particulière pour résoudre des récurrences linéaires non homogènes du type (*).

> Remark. Remember the method of seeking a particular solution to solve non-homogeneous linear recurrences of type (*).

EXERCICE 4. Soit \( \alpha > 0 \) un nombre irrationnel et \( \left( {r}_{n}\right) \) une suite de nombres rationnels qui converge vers \( \alpha \) . Pour tout \( n \) , on écrit \( {r}_{n} = {p}_{n}/{q}_{n} \) où \( {p}_{n} \in \mathbb{Z},{q}_{n} \in {\mathbb{N}}^{ * } \) . Montrer que

> EXERCISE 4. Let \( \alpha > 0 \) be an irrational number and \( \left( {r}_{n}\right) \) be a sequence of rational numbers that converges to \( \alpha \). For all \( n \), we write \( {r}_{n} = {p}_{n}/{q}_{n} \) where \( {p}_{n} \in \mathbb{Z},{q}_{n} \in {\mathbb{N}}^{ * } \). Show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{p}_{n} = \mathop{\lim }\limits_{{n \rightarrow   + \infty }}{q}_{n} =  + \infty
\]

Solution. Donnons nous un entier naturel non nul \( N \) . Notons \( \Gamma \) l’ensemble des rationnels de la forme \( a/b \) qui se trouvent dans l’intervalle \( \left\lbrack {\alpha - 1,\alpha + 1}\right\rbrack \) et vérifient \( a \in \mathbb{Z}, b \in \mathbb{N},1 \leq b \leq N \) . L’ensemble \( \Gamma \) est fini puisque

> Solution. Let us take a non-zero natural number \( N \). Let \( \Gamma \) be the set of rationals of the form \( a/b \) that lie in the interval \( \left\lbrack {\alpha - 1,\alpha + 1}\right\rbrack \) and satisfy \( a \in \mathbb{Z}, b \in \mathbb{N},1 \leq b \leq N \). The set \( \Gamma \) is finite since

\[
\Gamma  = \mathop{\bigcup }\limits_{{1 \leq  q \leq  N}}{\Gamma }_{q}\;\text{ avec }\;{\Gamma }_{q} = \left\{  {r \in  \left\lbrack  {\alpha  - 1,\alpha  + 1}\right\rbrack  \mid \exists p \in  \mathbb{Z}, r = \frac{p}{q}}\right\}
\]

et que pour tout \( q \in {\mathbb{N}}^{ * },{\Gamma }_{q} \) est fini (car si \( p/q \in {\Gamma }_{q} \) , on a forcément \( \left( {\alpha - 1}\right) q \leq p \leq \left( {\alpha + 1}\right) q \) ).

> and that for all \( q \in {\mathbb{N}}^{ * },{\Gamma }_{q} \) is finite (because if \( p/q \in {\Gamma }_{q} \), we necessarily have \( \left( {\alpha - 1}\right) q \leq p \leq \left( {\alpha + 1}\right) q \)).

Ceci étant, le nombre \( \alpha \) est irrationnel donc n’appartient pas à \( \Gamma \) . Comme \( \Gamma \) est fini, on en déduit que

> Given this, the number \( \alpha \) is irrational and therefore does not belong to \( \Gamma \). Since \( \Gamma \) is finite, we deduce that

\[
\exists \rho  \in  \rbrack 0,1\lbrack ,\forall x \in  \Gamma ,\;\left| {x - \alpha }\right|  > \rho .
\]

(*)

> La suite \( \left( {r}_{n}\right) \) converge vers \( \alpha \) , donc il existe \( {n}_{0} \in \mathbb{N} \) tel que \( \left| {{r}_{n} - \alpha }\right| < \rho \) pour tout \( n \geq {n}_{0} \) . D’après (*), on a donc \( {r}_{n} \notin \Gamma \) pour tout \( n \geq {n}_{0} \) , ce qui entraîne \( {q}_{n} > N \) (si \( {q}_{n} \leq N \) , comme \( {r}_{n} = {p}_{n}/{q}_{n} \in \left\lbrack {\alpha - 1,\alpha + 1}\right\rbrack \) , on a \( {r}_{n} \in {\Gamma }_{{q}_{n}} \subset \Gamma \) , impossible). Finalement, nous avons prouvé

The sequence \( \left( {r}_{n}\right) \) converges to \( \alpha \), so there exists \( {n}_{0} \in \mathbb{N} \) such that \( \left| {{r}_{n} - \alpha }\right| < \rho \) for all \( n \geq {n}_{0} \). According to (*), we therefore have \( {r}_{n} \notin \Gamma \) for all \( n \geq {n}_{0} \), which implies \( {q}_{n} > N \) (if \( {q}_{n} \leq N \), as \( {r}_{n} = {p}_{n}/{q}_{n} \in \left\lbrack {\alpha - 1,\alpha + 1}\right\rbrack \), we have \( {r}_{n} \in {\Gamma }_{{q}_{n}} \subset \Gamma \), which is impossible). Finally, we have proven

\[
\exists {n}_{0} \in  \mathbb{N},\forall n \geq  {n}_{0},\;{q}_{n} \geq  N.
\]

Ceci étant possible pour tout \( N \in {\mathbb{N}}^{ * } \) , la suite \( \left( {q}_{n}\right) \) tend vers \( + \infty \) . Comme \( {p}_{n} \sim \alpha {q}_{n} \) , la suite \( \left( {p}_{n}\right) \) tend également vers \( + \infty \) .

> Since this is possible for all \( N \in {\mathbb{N}}^{ * } \), the sequence \( \left( {q}_{n}\right) \) tends to \( + \infty \). As \( {p}_{n} \sim \alpha {q}_{n} \), the sequence \( \left( {p}_{n}\right) \) also tends to \( + \infty \).

EXERCICE 5 (SOUS-GROUPES ADDITIFS DE \( \mathbb{R} \) ). a) Soit \( \Lambda \) un sous-groupe de \( \left( {\mathbb{R}, + }\right) \) , \( \Lambda \neq \{ 0\} \) . Montrer que \( \Lambda \) vérifie l’une des deux assertions suivantes :

> EXERCISE 5 (ADDITIVE SUBGROUPS OF \( \mathbb{R} \)). a) Let \( \Lambda \) be a subgroup of \( \left( {\mathbb{R}, + }\right) \), \( \Lambda \neq \{ 0\} \). Show that \( \Lambda \) satisfies one of the two following assertions:

(i) il existe \( m > 0 \) tel que \( \Lambda = m\mathbb{Z} \) ,

> (i) there exists \( m > 0 \) such that \( \Lambda = m\mathbb{Z} \),

(ii) \( \Lambda \) est dense dans \( \mathbb{R} \) .

> (ii) \( \Lambda \) is dense in \( \mathbb{R} \).

b) Soient \( a \) et \( b \) deux nombres réels non nuls. Montrer que l’ensemble \( a\mathbb{Z} + b\mathbb{Z} \) est dense dans \( \mathbb{R} \) si et seulement si \( a/b \notin \mathbb{Q} \) .

> b) Let \( a \) and \( b \) be two non-zero real numbers. Show that the set \( a\mathbb{Z} + b\mathbb{Z} \) is dense in \( \mathbb{R} \) if and only if \( a/b \notin \mathbb{Q} \).

c) Soient \( a \) et \( b \) deux nombres réels strictement positifs. Montrer que \( a\mathbb{N} - b\mathbb{N} \) est dense dans \( \mathbb{R} \) si et seulement si \( a/b \notin \mathbb{Q} \) .

> c) Let \( a \) and \( b \) be two strictly positive real numbers. Show that \( a\mathbb{N} - b\mathbb{N} \) is dense in \( \mathbb{R} \) if and only if \( a/b \notin \mathbb{Q} \) .

d) (Application.) Quelles sont les valeurs d’adhérence de la suite \( \left( {u}_{n}\right) \) définie par \( {u}_{n} = \; \sin n \) ?

> d) (Application.) What are the limit points of the sequence \( \left( {u}_{n}\right) \) defined by \( {u}_{n} = \; \sin n \) ?

Solution. a) C’est très classique. Notons \( {\Lambda }^{+ * } = \Lambda \cap {\mathbb{R}}^{+ * } \) et \( m = \inf {\Lambda }^{+ * } \) . Deux cas se présentent.

> Solution. a) This is very classic. Let us denote \( {\Lambda }^{+ * } = \Lambda \cap {\mathbb{R}}^{+ * } \) and \( m = \inf {\Lambda }^{+ * } \) . Two cases arise.

- Si \( m > 0 \) , alors \( m \in  {\Lambda }^{+ * } \) . En effet, si \( m \notin  {\Lambda }^{+ * } \) , on a par définition de la borne inférieure

> - If \( m > 0 \) , then \( m \in  {\Lambda }^{+ * } \) . Indeed, if \( m \notin  {\Lambda }^{+ * } \) , we have by definition of the infimum

\[
\exists \alpha ,\beta  \in  {\Lambda }^{+ * },\;m < \alpha  < \beta  < {2m},
\]

donc \( 0 < \beta - \alpha < m \) , et comme \( \Lambda \) est un groupe additif, \( \beta - \alpha \in {\Lambda }^{+ * } \) , ce qui est absurde \( \operatorname{car}m = \inf {\Lambda }^{+ * } \) .

> therefore \( 0 < \beta - \alpha < m \) , and since \( \Lambda \) is an additive group, \( \beta - \alpha \in {\Lambda }^{+ * } \) , which is absurd \( \operatorname{car}m = \inf {\Lambda }^{+ * } \) .

Comme \( m \in \Lambda \) et que \( \Lambda \) est un groupe, on a \( m\mathbb{Z} \subset \Lambda \) . Nous allons montrer l’inclusion réciproque, ce qui prouvera \( m\mathbb{Z} = \Lambda \) . Soit \( x \in \Lambda \) . Si \( n \) est la partie entière de \( x/m \) , on a \( {mn} \leq x < m\left( {n + 1}\right) \) , donc \( 0 \leq x - {mn} < m \) . Comme \( x - {mn} \in \Lambda \) , ceci entraîne \( x - {mn} = 0 \) car \( m = \inf {\Lambda }^{+ * } \) , autrement dit \( x = {mn} \in m\mathbb{Z} \) . Finalement, on a montré \( \Lambda = m\mathbb{Z} \) .

> Since \( m \in \Lambda \) and \( \Lambda \) is a group, we have \( m\mathbb{Z} \subset \Lambda \) . We will show the reverse inclusion, which will prove \( m\mathbb{Z} = \Lambda \) . Let \( x \in \Lambda \) . If \( n \) is the integer part of \( x/m \) , we have \( {mn} \leq x < m\left( {n + 1}\right) \) , therefore \( 0 \leq x - {mn} < m \) . Since \( x - {mn} \in \Lambda \) , this implies \( x - {mn} = 0 \) because \( m = \inf {\Lambda }^{+ * } \) , in other words \( x = {mn} \in m\mathbb{Z} \) . Finally, we have shown \( \Lambda = m\mathbb{Z} \) .

- Si \( m = 0 \) , nous allons montrer que \( \Lambda \) est dense dans \( \mathbb{R} \) . Soient \( a < b \) deux nombres réels. Comme \( 0 = \inf {\Lambda }^{+ * } \) , il existe \( x \in  \Lambda \) tel que \( 0 < x < b - a \) , et alors il existe \( n \in  \mathbb{Z} \) tel que \( a < {nx} < b \) . Ainsi,] \( a, b\left\lbrack  {\cap \Lambda  \neq  \varnothing \text{ , et ceci pour tout intervalle ouvert }}\right\rbrack  a, b\left\lbrack  {\text{ de }\mathbb{R}\text{ , d’où la }}\right\rbrack \) densité de \( \Lambda \) dans \( \mathbb{R} \) .

> - If \( m = 0 \) , we will show that \( \Lambda \) is dense in \( \mathbb{R} \) . Let \( a < b \) be two real numbers. Since \( 0 = \inf {\Lambda }^{+ * } \) , there exists \( x \in  \Lambda \) such that \( 0 < x < b - a \) , and then there exists \( n \in  \mathbb{Z} \) such that \( a < {nx} < b \) . Thus, ] \( a, b\left\lbrack  {\cap \Lambda  \neq  \varnothing \text{ , et ceci pour tout intervalle ouvert }}\right\rbrack  a, b\left\lbrack  {\text{ de }\mathbb{R}\text{ , d’où la }}\right\rbrack \) density of \( \Lambda \) in \( \mathbb{R} \) .

b) L’ensemble \( \Lambda = a\mathbb{Z} + b\mathbb{Z} \) est un sous-groupe de \( \left( {\mathbb{R}, + }\right) \) .

> b) The set \( \Lambda = a\mathbb{Z} + b\mathbb{Z} \) is a subgroup of \( \left( {\mathbb{R}, + }\right) \) .

Condition nécessaire. Supposons \( a/b \in \mathbb{Q} \) . Alors il existe deux entiers non nuls premiers entre eux \( p \) et \( q \) tels que \( a/b = p/q \) . On a donc

> Necessary condition. Suppose \( a/b \in \mathbb{Q} \) . Then there exist two non-zero coprime integers \( p \) and \( q \) such that \( a/b = p/q \) . We therefore have

\[
a\mathbb{Z} + b\mathbb{Z} = b\left( {\mathbb{Z} + \frac{a}{b}\mathbb{Z}}\right)  = b\left( {\mathbb{Z} + \frac{p}{q}\mathbb{Z}}\right)  = \frac{b}{q}\left( {q\mathbb{Z} + p\mathbb{Z}}\right)  = \frac{b}{q}\mathbb{Z}
\]

(on a \( p\mathbb{Z} + q\mathbb{Z} = \mathbb{Z} \) car les deux entiers \( p \) et \( q \) sont premiers entre eux), ce qui entraîne que \( \Lambda \) n’est pas dense dans \( \mathbb{R} \) . Ceci est contraire aux hypothèses, on en déduit \( a/b \notin \mathbb{Q} \) .

> (we have \( p\mathbb{Z} + q\mathbb{Z} = \mathbb{Z} \) because the two integers \( p \) and \( q \) are coprime), which implies that \( \Lambda \) is not dense in \( \mathbb{R} \) . This contradicts the hypotheses, we deduce \( a/b \notin \mathbb{Q} \) .

Condition suffisante. Supposons \( a/b \notin \mathbb{Q} \) et \( \Lambda \) non dense dans \( \mathbb{R} \) . D’après la question précédente, il existe \( m \in \mathbb{R} \) tel que \( \Lambda = m\mathbb{Z} \) . En particulier \( a \in \Lambda \) , donc il existe \( p \in \mathbb{Z} \) tel que \( a = {mp} \) . De même, il existe \( q \in \mathbb{Z} \) tel que \( b = {mq} \) . Donc \( a/b = p/q \in \mathbb{Q} \) , ce qui est absurde. L’ensemble \( \Lambda \) est donc dense dans \( \mathbb{R} \) .

> Sufficient condition. Suppose \( a/b \notin \mathbb{Q} \) and \( \Lambda \) are not dense in \( \mathbb{R} \). According to the previous question, there exists \( m \in \mathbb{R} \) such that \( \Lambda = m\mathbb{Z} \). In particular \( a \in \Lambda \), so there exists \( p \in \mathbb{Z} \) such that \( a = {mp} \). Similarly, there exists \( q \in \mathbb{Z} \) such that \( b = {mq} \). Thus \( a/b = p/q \in \mathbb{Q} \), which is absurd. The set \( \Lambda \) is therefore dense in \( \mathbb{R} \).

c) Condition nécessaire. Supposons \( a\mathbb{N} - b\mathbb{N} \) dense dans \( \mathbb{R} \) . Alors il en est de même pour \( a\mathbb{N} - \; b\mathbb{N} \supset a\mathbb{Z} - b\mathbb{Z} \) , donc d’après la question précédente, \( a/b \notin \mathbb{Q} \) .

> c) Necessary condition. Suppose \( a\mathbb{N} - b\mathbb{N} \) is dense in \( \mathbb{R} \). Then the same holds for \( a\mathbb{N} - \; b\mathbb{N} \supset a\mathbb{Z} - b\mathbb{Z} \), so according to the previous question, \( a/b \notin \mathbb{Q} \).

Condition suffisante. Si \( a/b \notin \mathbb{Q} \) , pour montrer que \( a\mathbb{N} - b\mathbb{N} \) est dense dans \( \mathbb{R} \) , nous allons commencer par montrer que

> Sufficient condition. If \( a/b \notin \mathbb{Q} \), to show that \( a\mathbb{N} - b\mathbb{N} \) is dense in \( \mathbb{R} \), we will start by showing that

\[
\forall \varepsilon  > 0,\exists \left( {p, q}\right)  \in  {\mathbb{N}}^{2},\;0 < {ap} - {bq} < \varepsilon .
\]

(*)

> Quitte à diminuer \( \varepsilon > 0 \) , on peut supposer \( \varepsilon < \inf \{ a, b\} \) . L’ensemble \( a\mathbb{Z} + b\mathbb{Z} \) est dense dans \( \mathbb{R} \) d'après la question précédente, donc

By potentially reducing \( \varepsilon > 0 \), we can assume \( \varepsilon < \inf \{ a, b\} \). The set \( a\mathbb{Z} + b\mathbb{Z} \) is dense in \( \mathbb{R} \) according to the previous question, therefore

\[
\exists \left( {p, q}\right)  \in  {\mathbb{Z}}^{2},\;0 < {ap} - {bq} < \varepsilon .
\]

Les entiers \( p \) et \( q \) sont de même signe car \( \varepsilon < \inf \{ a, b\} \) . S’ils sont tous les deux positifs, on a prouvé (*). Sinon, on réutilise la densité de \( a\mathbb{Z} + b\mathbb{Z} \) dans \( \mathbb{R} \) qui entraîne

> The integers \( p \) and \( q \) have the same sign because \( \varepsilon < \inf \{ a, b\} \). If they are both positive, we have proven (*). Otherwise, we reuse the density of \( a\mathbb{Z} + b\mathbb{Z} \) in \( \mathbb{R} \) which implies

\[
\exists \left( {{p}^{\prime },{q}^{\prime }}\right)  \in  {\mathbb{Z}}^{2},\;0 < a{p}^{\prime } - b{q}^{\prime } < \frac{{ap} - {bq}}{K} < \frac{\varepsilon }{K},\;K = \sup \{ \left| p\right| ,\left| q\right| \} .
\]

\( \left( {* * }\right) \)

> Une nouvelle fois, \( {p}^{\prime } \) et \( {q}^{\prime } \) sont de même signe. S’ils sont positifs, on a prouvé (*). Sinon,(**) entraîne

Once again, \( {p}^{\prime } \) and \( {q}^{\prime } \) have the same sign. If they are positive, we have proven (*). Otherwise, (**) implies

\[
0 < \left( {{ap} - {bq}}\right)  - K\left( {a{p}^{\prime } - b{q}^{\prime }}\right)  = a\left( {p - K{p}^{\prime }}\right)  - b\left( {q - K{q}^{\prime }}\right)  < \varepsilon .
\]

(***)

> L’entier \( p - K{p}^{\prime } \) est positif car \( {p}^{\prime } \leq - 1 \) donc \( p - K{p}^{\prime } \geq p + K \geq 0 \) ; de même \( q - K{q}^{\prime } \in \mathbb{N} \) , et finalement, (***) entraîne (*).

The integer \( p - K{p}^{\prime } \) is positive because \( {p}^{\prime } \leq - 1 \) so \( p - K{p}^{\prime } \geq p + K \geq 0 \); likewise \( q - K{q}^{\prime } \in \mathbb{N} \), and finally, (***) implies (*).

> L’ensemble \( a\mathbb{N} - b\mathbb{N} \) étant stable par addition, l’assertion (*) entraîne la densité de \( a\mathbb{N} - b\mathbb{N} \) dans \( {\mathbb{R}}^{ + } \) . De même, \( b\mathbb{N} - a\mathbb{N} \) est dense dans \( {\mathbb{R}}^{ + } \) , donc \( a\mathbb{N} - b\mathbb{N} \) est dense dans \( {\mathbb{R}}^{ - } \) , et finalement \( a\mathbb{N} - b\mathbb{N} \) est dense dans \( \mathbb{R} \) .

Since the set \( a\mathbb{N} - b\mathbb{N} \) is stable under addition, the assertion (*) implies the density of \( a\mathbb{N} - b\mathbb{N} \) in \( {\mathbb{R}}^{ + } \). Similarly, \( b\mathbb{N} - a\mathbb{N} \) is dense in \( {\mathbb{R}}^{ + } \), so \( a\mathbb{N} - b\mathbb{N} \) is dense in \( {\mathbb{R}}^{ - } \), and finally \( a\mathbb{N} - b\mathbb{N} \) is dense in \( \mathbb{R} \).

> d) Nous allons montrer que l’ensemble des valeurs d’adhérence de la suite \( \left( {u}_{n}\right) \) est \( \left\lbrack {-1,1}\right\rbrack \) . Il suffit pour cela de prouver que \( X = \{ \sin n, n \in \mathbb{N}\} \) est dense dans \( \left\lbrack {-1,1}\right\rbrack \) . Considérons la fonction \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \sin x \) . On a \( {f}^{-1}\left( X\right) = \mathbb{N} + {2\pi }\mathbb{Z} \) , et comme \( \mathbb{N} - {2\pi }\mathbb{N} \) est dense dans \( \mathbb{R} \) (car \( {2\pi } \) est irrationnel), on en déduit que \( {f}^{-1}\left( X\right) \) est dense dans \( \mathbb{R} \) . Donnons nous \( a, b \in \left\lbrack {-1,1}\right\rbrack \) , \( a < b \) . Comme \( {f}^{-1}\left( {\rbrack a, b\lbrack }\right) \) est ouvert \( \left( {f\text{ est continue }}\right) \) , on a

d) We will show that the set of limit points of the sequence \( \left( {u}_{n}\right) \) is \( \left\lbrack {-1,1}\right\rbrack \) . It suffices to prove that \( X = \{ \sin n, n \in \mathbb{N}\} \) is dense in \( \left\lbrack {-1,1}\right\rbrack \) . Consider the function \( f : \mathbb{R} \rightarrow \mathbb{R}\;x \mapsto \sin x \) . We have \( {f}^{-1}\left( X\right) = \mathbb{N} + {2\pi }\mathbb{Z} \) , and since \( \mathbb{N} - {2\pi }\mathbb{N} \) is dense in \( \mathbb{R} \) (because \( {2\pi } \) is irrational), we deduce that \( {f}^{-1}\left( X\right) \) is dense in \( \mathbb{R} \) . Let \( a, b \in \left\lbrack {-1,1}\right\rbrack \) , \( a < b \) . Since \( {f}^{-1}\left( {\rbrack a, b\lbrack }\right) \) is open \( \left( {f\text{ est continue }}\right) \) , we have

\[
{f}^{-1}\left( {\rbrack a, b\lbrack  \cap  X}\right)  = {f}^{-1}\left( {\rbrack a, b\lbrack }\right)  \cap  {f}^{-1}\left( X\right)  \neq  \varnothing ,
\]

donc \( \rbrack a, b\left\lbrack {\cap X \neq \varnothing }\right. \) . Ainsi \( X \) est dense dans \( \left\lbrack {-1,1}\right\rbrack \) , d’où le résultat.

> therefore \( \rbrack a, b\left\lbrack {\cap X \neq \varnothing }\right. \) . Thus \( X \) is dense in \( \left\lbrack {-1,1}\right\rbrack \) , hence the result.

EXERCICE 6. Soit \( \left( {u}_{n}\right) \) une suite telle que

> EXERCISE 6. Let \( \left( {u}_{n}\right) \) be a sequence such that

\[
{u}_{0} \geq  0,\;\text{ et }\;\forall n \in  \mathbb{N},\;{u}_{n + 1} = \sqrt{\frac{1 + {u}_{n}}{2}}.
\]

Prouver que la suite \( \left( {v}_{n}\right) \) définie par

> Prove that the sequence \( \left( {v}_{n}\right) \) defined by

\[
\forall n \in  \mathbb{N},\;{v}_{n} = \mathop{\prod }\limits_{{i = 1}}^{n}{u}_{i}
\]

est convergente et calculer sa limite.

> is convergent and calculate its limit.

Solution. Nous traitons plusieurs cas, selon la position de \( {u}_{0} \) par rapport à 1. \( \left. {-{u}_{0} < 1\text{ . Soit }\theta \in }\right\rbrack 0,\pi /2\rbrack \) tel que \( {u}_{0} = \cos \theta \) . La formule trigonométrique

> Solution. We treat several cases, depending on the position of \( {u}_{0} \) relative to 1. \( \left. {-{u}_{0} < 1\text{ . Soit }\theta \in }\right\rbrack 0,\pi /2\rbrack \) such that \( {u}_{0} = \cos \theta \) . The trigonometric formula

\( \forall u \in \mathbb{R},\;\cos \frac{u}{2} = \sqrt{\frac{1 + \cos u}{2}}\; \) entraîne immédiatement \( \forall n \in \mathbb{N},\;{u}_{n} = \cos \left( \frac{\theta }{{2}^{n}}\right) . \)

> \( \forall u \in \mathbb{R},\;\cos \frac{u}{2} = \sqrt{\frac{1 + \cos u}{2}}\; \) immediately implies \( \forall n \in \mathbb{N},\;{u}_{n} = \cos \left( \frac{\theta }{{2}^{n}}\right) . \)

En utilisant maintenant l'identité

> Now using the identity

\[
\forall u \notin  \pi \mathbb{Z},\;\cos u = \frac{\sin {2u}}{2\sin u},
\]

on voit que pour tout entier naturel non nul \( n \) ,

> we see that for any non-zero natural number \( n \) ,

\[
{v}_{n} = \cos \left( \frac{\theta }{2}\right) \cos \left( \frac{\theta }{4}\right) \cdots \cos \left( \frac{\theta }{{2}^{n}}\right)  = \frac{\sin \theta }{2\sin \left( {\theta /2}\right) } \cdot  \frac{\sin \left( {\theta /2}\right) }{2\sin \left( {\theta /4}\right) }\cdots \frac{\sin \left( {\theta /{2}^{n - 1}}\right) }{2\sin \left( {\theta /{2}^{n}}\right) } = \frac{\sin \theta }{{2}^{n}\sin \left( {\theta /{2}^{n}}\right) },
\]

et on en conclut que

> and we conclude that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{v}_{n} = \frac{\sin \theta }{\theta } = \frac{\sqrt{1 - {u}_{0}^{2}}}{\arccos {u}_{0}}.
\]

\( - {u}_{0} = 1 \) . Dans ce cas, on a \( {u}_{n} = 1 \) pour tout \( n \) et tout est trivial.

> \( - {u}_{0} = 1 \) . In this case, we have \( {u}_{n} = 1 \) for all \( n \) and everything is trivial.

\( - {u}_{0} > 1 \) . On procède comme dans le cas \( {u}_{0} < 1 \) en remplaçant les fonctions trigonométriques par les fonctions hyperboliques correspondantes. Si on écrit \( {u}_{0} = \operatorname{ch}\theta \) , on montre que

> \( - {u}_{0} > 1 \) . We proceed as in the case \( {u}_{0} < 1 \) by replacing the trigonometric functions with the corresponding hyperbolic functions. If we write \( {u}_{0} = \operatorname{ch}\theta \) , we show that

\[
\mathop{\lim }\limits_{{n \rightarrow   + \infty }}{v}_{n} = \frac{\operatorname{sh}\theta }{\theta } = \frac{\sqrt{{u}_{0}^{2} - 1}}{\operatorname{argch}{u}_{0}}.
\]

Remarque. En partant de \( {u}_{0} = 0 \) , la suite \( \left( {v}_{n}\right) \) converge vers \( 2/\pi \) , ce qui s’écrit

> Remark. Starting from \( {u}_{0} = 0 \) , the sequence \( \left( {v}_{n}\right) \) converges to \( 2/\pi \) , which is written

\[
\frac{2}{\pi } = \sqrt{\frac{1}{2}} \cdot  \sqrt{\frac{1}{2} + \frac{1}{2}\sqrt{\frac{1}{2}}} \cdot  \sqrt{\frac{1}{2} + \frac{1}{2}\sqrt{\frac{1}{2} + \frac{1}{2}\sqrt{\frac{1}{2}}}}\cdots ,
\]

formule découverte par François Viète (1540-1603), qu'il obtint en considérant l'aire de polygones réguliers à \( {2}^{n} \) côtés.

> a formula discovered by François Viète (1540-1603), which he obtained by considering the area of regular polygons with \( {2}^{n} \) sides.

EXERCICE 7. Soit \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) la suite définie par

> EXERCISE 7. Let \( {\left( {u}_{n}\right) }_{n \in {\mathbb{N}}^{ * }} \) be the sequence defined by

\[
{u}_{1} = 1,\;\forall n \geq  2,\;{u}_{n} = \sqrt{n + {u}_{n - 1}}.
\]

Donner un équivalent puis calculer les deux premiers termes du développement asympto-tique de \( \left( {u}_{n}\right) \) lorsque \( n \rightarrow + \infty \) .

> Provide an equivalent and then calculate the first two terms of the asymptotic expansion of \( \left( {u}_{n}\right) \) as \( n \rightarrow + \infty \) .

Solution. Une autre manière de voir les choses est d'écrire

> Solution. Another way to look at things is to write

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \sqrt{n + \sqrt{n - 1 + \sqrt{n - 2 + \cdots }}}.
\]

Dans cette expression, on "intuite" que seul le premier terme \( \sqrt{n} \) est prépondérant dans l'expression de \( \left( {u}_{n}\right) \) . Nous allons donc montrer que \( {u}_{n} \sim \sqrt{n} \) lorsque \( n \rightarrow + \infty \) . Pour cela, nous commençons par montrer par récurrence \( {u}_{n} \leq 2\sqrt{n} \) pour tout \( n \in {\mathbb{N}}^{ * } \) . Pour \( n = 1 \) , c’est vrai. Pour passer au rang \( n \) au rang \( n + 1 \) , on écrit

> In this expression, we "intuit" that only the first term \( \sqrt{n} \) is dominant in the expression of \( \left( {u}_{n}\right) \) . We will therefore show that \( {u}_{n} \sim \sqrt{n} \) as \( n \rightarrow + \infty \) . To do this, we begin by showing by induction \( {u}_{n} \leq 2\sqrt{n} \) for all \( n \in {\mathbb{N}}^{ * } \) . For \( n = 1 \) , it is true. To move from rank \( n \) to rank \( n + 1 \) , we write

\[
{u}_{n + 1}^{2} = n + 1 + {u}_{n} \leq  n + 1 + 2\sqrt{n} = {\left( \sqrt{n} + 1\right) }^{2} \leq  {\left( 2\sqrt{n + 1}\right) }^{2}.
\]

Maintenant, il suffit d'écrire

> Now, it suffices to write

\[
\forall n \in  {\mathbb{N}}^{ * },\;\sqrt{n} \leq  {u}_{n} \leq  \sqrt{n + {u}_{n - 1}} \leq  \sqrt{n + 2\sqrt{n}} = \sqrt{n}\sqrt{1 + \frac{2}{\sqrt{n}}},
\]

ce qui entraîne immédiatement \( {u}_{n} \sim \sqrt{n} \) .

> which immediately leads to \( {u}_{n} \sim \sqrt{n} \) .

Pour calculer le second terme du développement asymptotique de \( \left( {u}_{n}\right) \) , on écrit

> To calculate the second term of the asymptotic expansion of \( \left( {u}_{n}\right) \) , we write

\[
\forall n \in  {\mathbb{N}}^{ * },\;{u}_{n} = \sqrt{n + {u}_{n - 1}} = \sqrt{n + \sqrt{n - 1}\left( {1 + o\left( 1\right) }\right) } = \sqrt{n}\sqrt{1 + \frac{\sqrt{n - 1}}{n}\left( {1 + o\left( 1\right) }\right) }
\]

\[
= \sqrt{n}\left( {1 + \frac{1}{2}\frac{\sqrt{n - 1}}{n}\left( {1 + o\left( 1\right) }\right) }\right)  = \sqrt{n}\left( {1 + \frac{1}{2}\frac{1}{\sqrt{n}}\left( {1 + o\left( 1\right) }\right) }\right)  = \sqrt{n} + \frac{1}{2} + o\left( 1\right) .
\]

Remarque. En itérant le procédé, on peut en fait calculer un nombre quelconque de termes du développement asymptotique de \( \left( {u}_{n}\right) \) .

> Remark. By iterating the process, one can in fact calculate any number of terms of the asymptotic expansion of \( \left( {u}_{n}\right) \) .

EXERCICE 8. Soit \( {\left( {u}_{n}\right) }_{n > 1} \) une suite réelle positive majorée. On dit que \( A \subset \mathbb{N} \) est de densité nulle si \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{1}{n}\operatorname{Card}\left( {A \cap \left\lbrack {0, n}\right\rbrack }\right) = 0 \) . Montrer que (i) et (ii) sont équivalents :

> EXERCISE 8. Let \( {\left( {u}_{n}\right) }_{n > 1} \) be a bounded positive real sequence. We say that \( A \subset \mathbb{N} \) has zero density if \( \mathop{\lim }\limits_{{n \rightarrow + \infty }}\frac{1}{n}\operatorname{Card}\left( {A \cap \left\lbrack {0, n}\right\rbrack }\right) = 0 \) . Show that (i) and (ii) are equivalent:

(i) La suite \( \left( {S}_{n}\right) \) définie par \( {S}_{n} = \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{n}{u}_{k} \) converge vers 0 .

> (i) The sequence \( \left( {S}_{n}\right) \) defined by \( {S}_{n} = \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{n}{u}_{k} \) converges to 0 .

(ii) Il existe une partie \( A \subset \mathbb{N} \) de densité nulle telle que \( \mathop{\lim }\limits_{\substack{{n \rightarrow + \infty } \\ {n \notin A} }}{u}_{n} = 0 \) .

> (ii) There exists a subset \( A \subset \mathbb{N} \) of zero density such that \( \mathop{\lim }\limits_{\substack{{n \rightarrow + \infty } \\ {n \notin A} }}{u}_{n} = 0 \) .

Solution. Commençons par prouver que (ii) \( \Rightarrow \) (i). Soit \( \varepsilon > 0 \) . Soit \( M \) un majorant de \( \left( {u}_{n}\right) \) et soit \( N \in \mathbb{N} \) tel que \( {u}_{n} < \varepsilon \) pour tout \( n > N \) et \( n \notin A \) . Lorsque \( n > N \) on a

> Solution. Let us begin by proving that (ii) \( \Rightarrow \) (i). Let \( \varepsilon > 0 \) . Let \( M \) be an upper bound of \( \left( {u}_{n}\right) \) and let \( N \in \mathbb{N} \) be such that \( {u}_{n} < \varepsilon \) for all \( n > N \) and \( n \notin A \) . When \( n > N \) we have

\[
\left| {S}_{n}\right|  \leq  \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{N}{u}_{k} + \frac{1}{n}\mathop{\sum }\limits_{\substack{{N < k \leq  n} \\  {k \notin  A} }}{u}_{k} + \frac{1}{n}\mathop{\sum }\limits_{\substack{{N < k \leq  n} \\  {k \in  A} }}{u}_{k} < \frac{1}{n}\mathop{\sum }\limits_{{k = 1}}^{N}{u}_{k} + \varepsilon  + M\frac{\operatorname{Card}\left( {A \cap  \left\lbrack  {0, n}\right\rbrack  }\right) }{n}.
\]

Lorque \( n \rightarrow + \infty \) les termes de gauche et de droite de la dernière somme, tendent vers 0 . Donc il existe \( {N}^{\prime } \geq N \) tel que pour \( n \geq {N}^{\prime } \) , ces deux termes soient chacuns inférieurs à \( \varepsilon \) . On en déduit que \( \left| {S}_{n}\right| < {3\varepsilon } \) pour \( n \geq {N}^{\prime } \) , ce qui montre le résultat voulu.

> When \( n \rightarrow + \infty \) the terms on the left and right of the last sum tend to 0 . Thus there exists \( {N}^{\prime } \geq N \) such that for \( n \geq {N}^{\prime } \) , these two terms are each less than \( \varepsilon \) . We deduce that \( \left| {S}_{n}\right| < {3\varepsilon } \) for \( n \geq {N}^{\prime } \) , which shows the desired result.

Montrons maintenant (i) \( \Rightarrow \) (ii). La suite \( \left( {S}_{n}\right) \) converge vers 0 donc la suite \( \left( {\alpha }_{n}\right) \) définie par \( {\alpha }_{n} = \mathop{\sup }\limits_{{k \geq n}}{S}_{k} \) converge également vers 0 . On peut se placer dans le cas où la limite de \( \left( {u}_{n}\right) \) n’est pas nulle, sinon il suffit de choisir \( A = \varnothing \) et (ii) est prouvé. Dans ce cas on a \( {\alpha }_{n} > 0 \) . Définissons \( A = \left\{ {n \in {\mathbb{N}}^{ * } \mid {u}_{n} \geq \sqrt{{\alpha }_{n}}}\right\} \) . Lorsque \( n \notin A \) on a \( 0 \leq {u}_{n} < \sqrt{{\alpha }_{n}} \) donc \( \mathop{\lim }\limits_{\substack{{n \rightarrow + \infty } \\ {n \notin A} }}{u}_{n} = 0 \) .

> Let us now show (i) \( \Rightarrow \) (ii). The sequence \( \left( {S}_{n}\right) \) converges to 0, so the sequence \( \left( {\alpha }_{n}\right) \) defined by \( {\alpha }_{n} = \mathop{\sup }\limits_{{k \geq n}}{S}_{k} \) also converges to 0. We can assume the case where the limit of \( \left( {u}_{n}\right) \) is not zero, otherwise it suffices to choose \( A = \varnothing \) and (ii) is proven. In this case, we have \( {\alpha }_{n} > 0 \) . Let us define \( A = \left\{ {n \in {\mathbb{N}}^{ * } \mid {u}_{n} \geq \sqrt{{\alpha }_{n}}}\right\} \) . When \( n \notin A \) we have \( 0 \leq {u}_{n} < \sqrt{{\alpha }_{n}} \) so \( \mathop{\lim }\limits_{\substack{{n \rightarrow + \infty } \\ {n \notin A} }}{u}_{n} = 0 \) .

Lorsque \( k \in A \cap \left\lbrack {0, n}\right\rbrack \) , on a \( {u}_{k} \geq \sqrt{{\alpha }_{k}} \geq \sqrt{{\alpha }_{n}} \) ce qui entraîne

> When \( k \in A \cap \left\lbrack {0, n}\right\rbrack \) , we have \( {u}_{k} \geq \sqrt{{\alpha }_{k}} \geq \sqrt{{\alpha }_{n}} \) which implies

\[
\operatorname{Card}\left( {A \cap  \left\lbrack  {0, n}\right\rbrack  }\right)  \leq  \mathop{\sum }\limits_{\substack{{k \in  A} \\  {1 \leq  k \leq  n} }}\frac{{u}_{k}}{\sqrt{{\alpha }_{n}}} \leq  \frac{1}{\sqrt{{\alpha }_{n}}}\mathop{\sum }\limits_{{k = 1}}^{n}{u}_{k}\;\text{ donc }\;\frac{\operatorname{Card}\left( {A \cap  \left\lbrack  {0, n}\right\rbrack  }\right) }{n} \leq  \frac{{S}_{n}}{\sqrt{{\alpha }_{n}}} \leq  \sqrt{{\alpha }_{n}}.
\]

On en déduit que \( A \) est de densité nulle, et on a bien prouvé (ii).

> We deduce that \( A \) has zero density, and we have indeed proven (ii).
