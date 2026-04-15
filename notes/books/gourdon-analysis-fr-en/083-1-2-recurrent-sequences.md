#### 1.2. Recurrent sequences

*Français : 1.2. Suites récurrentes*

DéFINITION 1. Soient \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( h \) un entier naturel non nul. Une suite \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) à valeurs dans \( E \) est dite récurrente d’ordre \( h \) si on peut écrire

> DEFINITION 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( h \) a non-zero natural number. A sequence \( {\left( {u}_{n}\right) }_{n \in \mathbb{N}} \) with values in \( E \) is said to be recurrent of order \( h \) if one can write

\[
\forall n \geq  h,\;{u}_{n} = f\left( {{u}_{n - 1},{u}_{n - 2},\ldots ,{u}_{n - h}}\right)
\]

(*)

> où \( f \) est une application de \( {E}^{h} \) dans \( E \) .

where \( f \) is a mapping from \( {E}^{h} \) to \( E \).

> Les premières valeurs \( {u}_{0},\ldots ,{u}_{h - 1} \) de \( \left( {u}_{n}\right) \) étant données, la relation (*) permet de calculer de manière itérative tous les autres termes de la suite. Le plus souvent, les suites récurrentes que nous traiterons seront d'ordre 1.

Given the initial values \( {u}_{0},\ldots ,{u}_{h - 1} \) of \( \left( {u}_{n}\right) \), the relation (*) allows for the iterative calculation of all other terms of the sequence. Most often, the recurrent sequences we will deal with will be of order 1.

> La proposition suivante permet souvent de calculer la limite d'une suite récurrente si on sait par ailleurs qu'elle converge.

The following proposition often allows for the calculation of the limit of a recurrent sequence if one knows, moreover, that it converges.

> PROPOSITION 1. Soit \( \left( {E,\mathrm{\;d}}\right) \) un espace métrique et \( \left( {u}_{n}\right) \) une suite récurrente d’ordre \( h \in {\mathbb{N}}^{ * } \) vérifiant

PROPOSITION 1. Let \( \left( {E,\mathrm{\;d}}\right) \) be a metric space and \( \left( {u}_{n}\right) \) a recurrent sequence of order \( h \in {\mathbb{N}}^{ * } \) satisfying

\[
\forall n \geq  h,\;{u}_{n} = f\left( {{u}_{n - 1},{u}_{n - 2},\ldots ,{u}_{n - h}}\right)
\]

où \( f : {E}^{h} \rightarrow E \) est une application. Si la suite \( \left( {u}_{n}\right) \) converge vers une limite \( \ell \) et si l’application \( f \) est continue au point \( \left( {\ell ,\ldots ,\ell }\right) \) , alors on a

> where \( f : {E}^{h} \rightarrow E \) is a mapping. If the sequence \( \left( {u}_{n}\right) \) converges to a limit \( \ell \) and if the mapping \( f \) is continuous at point \( \left( {\ell ,\ldots ,\ell }\right) \), then we have

\[
\ell  = f\left( {\ell ,\ell ,\ldots ,\ell }\right) .
\]

La preuve est simple, il suffit de faire tendre \( n \) vers \( + \infty \) dans la relation (*) et d’utiliser la continuité de \( f \) au point \( \left( {\ell ,\ldots ,\ell }\right) \) .

> The proof is simple; it suffices to let \( n \) tend to \( + \infty \) in relation (*) and use the continuity of \( f \) at point \( \left( {\ell ,\ldots ,\ell }\right) \).

Monotonie des suites réelles récurrentes d’ordre 1. Soit un intervalle \( I \) de \( \mathbb{R} \) et une fonction \( f : I \rightarrow \mathbb{R} \) telle que \( f\left( I\right) \subset I \) . Considérons une suite \( \left( {u}_{n}\right) \) vérifiant

> Monotonicity of first-order real recurrent sequences. Let \( I \) be an interval of \( \mathbb{R} \) and \( f : I \rightarrow \mathbb{R} \) be a function such that \( f\left( I\right) \subset I \). Consider a sequence \( \left( {u}_{n}\right) \) satisfying

\[
{u}_{0} \in  I\;\text{ et }\;\forall n \in  \mathbb{N},\;{u}_{n + 1} = f\left( {u}_{n}\right) .
\]

- Si \( f \) est croissante, la suite \( \left( {u}_{n}\right) \) est monotone et son sens de monotonie est donnée par le signe de \( {u}_{1} - {u}_{0} \) (immédiat par récurrence).

> - If \( f \) is increasing, the sequence \( \left( {u}_{n}\right) \) is monotonic and its direction of monotonicity is given by the sign of \( {u}_{1} - {u}_{0} \) (immediate by induction).

- Si \( f \) est décroissante, la fonction \( f \circ  f \) est croissante. On en déduit que les suites \( \left( {u}_{2n}\right) \) et \( \left( {u}_{{2n} + 1}\right) \) sont monotones, et leur sens de monotonie est opposé (ceci car le signe de \( {u}_{2} - {u}_{0} \) est l’opposé du signe de \( {u}_{3} - {u}_{1} = f\left( {u}_{2}\right)  - f\left( {u}_{0}\right) \) ).

> - If \( f \) is decreasing, the function \( f \circ  f \) is increasing. We deduce that the sequences \( \left( {u}_{2n}\right) \) and \( \left( {u}_{{2n} + 1}\right) \) are monotonic, and their directions of monotonicity are opposite (this is because the sign of \( {u}_{2} - {u}_{0} \) is the opposite of the sign of \( {u}_{3} - {u}_{1} = f\left( {u}_{2}\right)  - f\left( {u}_{0}\right) \)).
