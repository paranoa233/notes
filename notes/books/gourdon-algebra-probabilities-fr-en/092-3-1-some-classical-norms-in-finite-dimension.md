#### 3.1. Some classical norms in finite dimension

*Français : 3.1. Quelques normes classiques en dimension finie*

Soit \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) \) un vecteur de \( {\mathbb{K}}^{n} \) . On définit les normes suivantes sur \( {\mathbb{K}}^{n} \) :

> Let \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) \) be a vector of \( {\mathbb{K}}^{n} \) . We define the following norms on \( {\mathbb{K}}^{n} \) :

\[
\forall \alpha  \geq  1,\;\parallel X{\parallel }_{\alpha } = {\left( \mathop{\sum }\limits_{{i = 1}}^{n}{\left| {x}_{i}\right| }^{\alpha }\right) }^{1/\alpha }\;\text{ et }\;\parallel X{\parallel }_{\infty } = \mathop{\sup }\limits_{{1 \leq  i \leq  n}}\left| {x}_{i}\right| .
\]

(La notation \( \parallel X{\parallel }_{\infty } \) provient du fait que \( \mathop{\lim }\limits_{{\alpha \rightarrow \infty }}\parallel X{\parallel }_{\alpha } = \parallel X{\parallel }_{\infty } \) ).

> (The notation \( \parallel X{\parallel }_{\infty } \) comes from the fact that \( \mathop{\lim }\limits_{{\alpha \rightarrow \infty }}\parallel X{\parallel }_{\alpha } = \parallel X{\parallel }_{\infty } \) ).

Si \( E \) est un \( \mathbb{K} \) -e.v de dimension finie \( n \) , on peut le normer en privilégiant une base \( B \) de \( E \) et en écrivant que la norme de \( x \in E \) est la norme du vecteur \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) \in {\mathbb{K}}^{n} \) , où les \( {x}_{i} \) sont les coordonnées de \( x \) dans la base \( B \) .

> If \( E \) is a finite-dimensional \( \mathbb{K} \) -v.s. \( n \) , it can be normed by choosing a basis \( B \) of \( E \) and stating that the norm of \( x \in E \) is the norm of the vector \( X = \left( \begin{matrix} {x}_{1} \\ \vdots \\ {x}_{n} \end{matrix}\right) \in {\mathbb{K}}^{n} \) , where the \( {x}_{i} \) are the coordinates of \( x \) in the basis \( B \) .

Soit \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> Let \( M = {\left( {m}_{i, j}\right) }_{1 \leq i, j \leq n} \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

- \( \parallel M\parallel  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}\left| {m}_{i, j}\right| \) définit une norme d’algèbre sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> - \( \parallel M\parallel  = \mathop{\sum }\limits_{{1 \leq  i, j \leq  n}}\left| {m}_{i, j}\right| \) defines an algebra norm on \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

- \( \parallel M\parallel  = \mathop{\sup }\limits_{{i, j}}\left| {m}_{i, j}\right| \) définit une norme sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , mais ce n’est pas une norme d'algèbre.

> - \( \parallel M\parallel  = \mathop{\sup }\limits_{{i, j}}\left| {m}_{i, j}\right| \) defines a norm on \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , but it is not an algebra norm.

- Pour tout \( \alpha  \geq  1,\parallel M{\parallel }_{\alpha } = \mathop{\sup }\limits_{{\parallel X{\parallel }_{\alpha } = 1}}\parallel {MX}{\parallel }_{\alpha } \) définit une norme d’algèbre sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Au passage, notons que l’on peut montrer \( \parallel M{\parallel }_{\infty } = \mathop{\sup }\limits_{i}\left( {\mathop{\sum }\limits_{j}\left| {m}_{i, j}\right| }\right) \) et \( \parallel M{\parallel }_{1} = \mathop{\sup }\limits_{j}\left( {\mathop{\sum }\limits_{i}\left| {m}_{i, j}\right| }\right) . \)

> - For any \( \alpha  \geq  1,\parallel M{\parallel }_{\alpha } = \mathop{\sup }\limits_{{\parallel X{\parallel }_{\alpha } = 1}}\parallel {MX}{\parallel }_{\alpha } \) defines an algebra norm on \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Incidentally, note that one can show \( \parallel M{\parallel }_{\infty } = \mathop{\sup }\limits_{i}\left( {\mathop{\sum }\limits_{j}\left| {m}_{i, j}\right| }\right) \) and \( \parallel M{\parallel }_{1} = \mathop{\sup }\limits_{j}\left( {\mathop{\sum }\limits_{i}\left| {m}_{i, j}\right| }\right) . \)

Si \( E \) est un \( \mathbb{K} \) -e.v de dimension finie \( n \) , on peut normer \( \mathcal{L}\left( E\right) \) en privilégiant une base \( B \) de \( E \) et en écrivant que la norme de \( u \) est celle de \( {\left\lbrack u\right\rbrack }_{B} \) (matrice de \( u \) dans la base \( B \) ) dans \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> If \( E \) is a finite-dimensional \( \mathbb{K} \) -v.s. \( n \) , one can norm \( \mathcal{L}\left( E\right) \) by choosing a basis \( B \) of \( E \) and writing that the norm of \( u \) is that of \( {\left\lbrack u\right\rbrack }_{B} \) (matrix of \( u \) in the basis \( B \) ) in \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .
