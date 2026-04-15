#### 4.6. Exercises

*Français : 4.6. Exercices*

EXERCICE 1. Soit \( E \) un \( \mathbb{K} \) -e.v, \( {\varphi }_{1},\ldots ,{\varphi }_{p} \in {E}^{ * } \) et \( \varphi : E \rightarrow {\mathbb{K}}^{p} \) définie par \( \varphi = \; \left( {{\varphi }_{1},\ldots ,{\varphi }_{p}}\right) \) . Montrer que \( \varphi \) est surjective si et seulement si \( {\varphi }_{1},\ldots ,{\varphi }_{p} \) sont linéairement indépendantes.

> EXERCISE 1. Let \( E \) be a \( \mathbb{K} \) -v.s., \( {\varphi }_{1},\ldots ,{\varphi }_{p} \in {E}^{ * } \) and \( \varphi : E \rightarrow {\mathbb{K}}^{p} \) defined by \( \varphi = \; \left( {{\varphi }_{1},\ldots ,{\varphi }_{p}}\right) \) . Show that \( \varphi \) is surjective if and only if \( {\varphi }_{1},\ldots ,{\varphi }_{p} \) are linearly independent.

Solution. Condition nécessaire. Supposons \( {\lambda }_{1}{\varphi }_{1} + \cdots + {\lambda }_{p}{\varphi }_{p} = 0\;\left( *\right) \) avec les \( {\lambda }_{i} \in \mathbb{K} \) . Comme \( \varphi \) est surjective, si on fixe \( i,1 \leq i \leq p \) , il existe \( x \in E \) tel que \( {\varphi }_{i}\left( x\right) = 1 \) et pour tout \( j \neq i \) , \( {\varphi }_{j}\left( x\right) = 0 \) . Appliqué à \( \left( *\right) \) , ceci entraîne \( {\lambda }_{i} = 0 \) , et ceci pour tout \( i \) , d’où la condition nécessaire. Condition suffisante. Soit \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) la base canonique de \( {\mathbb{K}}^{p},\left( {{e}_{1}^{ * },\ldots ,{e}_{p}^{ * }}\right) \) sa base duale. Soit \( \psi \in \; {\left( \operatorname{Im}\varphi \right) }^{ \bot } \) . Écrivons \( \psi = {\lambda }_{1}{e}_{1}^{ * } + \cdots + {\lambda }_{p}{e}_{p}^{ * } \) . Pour tout \( x \in E,\psi \left( {\varphi \left( x\right) }\right) = 0 = {\lambda }_{1}{\varphi }_{1}\left( x\right) + \cdots + {\lambda }_{p}{\varphi }_{p}\left( x\right) \) , donc \( {\lambda }_{1}{\varphi }_{1} + \cdots + {\lambda }_{p}{\varphi }_{p} = 0 \) , ce qui entraîne \( {\lambda }_{1} = \cdots = {\lambda }_{p} = 0 \) , donc \( \psi = 0 \) . Autrement dit, on a montré \( {\left( \operatorname{Im}\varphi \right) }^{ \bot } = \{ 0\} \) , donc \( \operatorname{Im}\varphi = {\mathbb{K}}^{p} \) , c’est-à-dire que \( \varphi \) est surjective.

> Solution. Necessary condition. Suppose \( {\lambda }_{1}{\varphi }_{1} + \cdots + {\lambda }_{p}{\varphi }_{p} = 0\;\left( *\right) \) with the \( {\lambda }_{i} \in \mathbb{K} \) . Since \( \varphi \) is surjective, if we fix \( i,1 \leq i \leq p \) , there exists \( x \in E \) such that \( {\varphi }_{i}\left( x\right) = 1 \) and for all \( j \neq i \) , \( {\varphi }_{j}\left( x\right) = 0 \) . Applied to \( \left( *\right) \) , this implies \( {\lambda }_{i} = 0 \) , and this for all \( i \) , hence the necessary condition. Sufficient condition. Let \( \left( {{e}_{1},\ldots ,{e}_{p}}\right) \) be the canonical basis of \( {\mathbb{K}}^{p},\left( {{e}_{1}^{ * },\ldots ,{e}_{p}^{ * }}\right) \) and its dual basis. Let \( \psi \in \; {\left( \operatorname{Im}\varphi \right) }^{ \bot } \) . Let us write \( \psi = {\lambda }_{1}{e}_{1}^{ * } + \cdots + {\lambda }_{p}{e}_{p}^{ * } \) . For all \( x \in E,\psi \left( {\varphi \left( x\right) }\right) = 0 = {\lambda }_{1}{\varphi }_{1}\left( x\right) + \cdots + {\lambda }_{p}{\varphi }_{p}\left( x\right) \) , thus \( {\lambda }_{1}{\varphi }_{1} + \cdots + {\lambda }_{p}{\varphi }_{p} = 0 \) , which implies \( {\lambda }_{1} = \cdots = {\lambda }_{p} = 0 \) , therefore \( \psi = 0 \) . In other words, we have shown \( {\left( \operatorname{Im}\varphi \right) }^{ \bot } = \{ 0\} \) , thus \( \operatorname{Im}\varphi = {\mathbb{K}}^{p} \) , that is to say that \( \varphi \) is surjective.

EXERCICE 2. Soit \( E \) un \( \mathbb{R} \) -e.v de dimension 3, \( \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) une base de \( E \) . Soit \( {f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * } \in \; {E}^{ * } \) définis par

> EXERCISE 2. Let \( E \) be a \( \mathbb{R} \) -v.s. of dimension 3, \( \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) a basis of \( E \) . Let \( {f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * } \in \; {E}^{ * } \) be defined by

\[
{f}_{1}^{ * } = 2{e}_{1}^{ * } + {e}_{2}^{ * } + {e}_{3}^{ * },\;{f}_{2}^{ * } =  - {e}_{1}^{ * } + 2{e}_{3}^{ * },\;{f}_{3}^{ * } = {e}_{1}^{ * } + 3{e}_{2}^{ * }.
\]

Montrer que \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) est une base de \( {E}^{ * } \) et calculer la base \( \left( {{f}_{1},{f}_{2},{f}_{3}}\right) \) (en l’exprimant dans la base \( \left. \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \right) \) de \( E \) dont elle est la duale.

> Show that \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) is a basis of \( {E}^{ * } \) and calculate the basis \( \left( {{f}_{1},{f}_{2},{f}_{3}}\right) \) (by expressing it in the basis \( \left. \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \right) \) of \( E \) of which it is the dual).

Solution. Les colonnes de la matrice

> Solution. The columns of the matrix

\[
M = \left( \begin{array}{rrr} 2 &  - 1 & 1 \\  1 & 0 & 3 \\  1 & 2 & 0 \end{array}\right)
\]

sont les coordonnées des \( {f}_{i}^{ * } \) dans la base \( \left( {{e}_{1}^{ * },{e}_{2}^{ * },{e}_{3}^{ * }}\right) \) . Pour montrer que \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) est une base de \( {E}^{ * } \) , il faut montrer que le rang de la matrice \( M \) est égal à 3 . Des opérations élémentaires sur les colonnes donnent

> are the coordinates of the \( {f}_{i}^{ * } \) in the basis \( \left( {{e}_{1}^{ * },{e}_{2}^{ * },{e}_{3}^{ * }}\right) \). To show that \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) is a basis of \( {E}^{ * } \), one must show that the rank of the matrix \( M \) is equal to 3. Elementary column operations yield

\[
\operatorname{rg}M = \operatorname{rg}\left( \begin{array}{rrr} 2 &  - 5 & 1 \\  1 &  - 2 & 3 \\  1 & 0 & 0 \end{array}\right)  = \operatorname{rg}\left( \begin{array}{rrr} 2 &  - 5 &  - \frac{13}{2} \\  1 &  - 2 & 0 \\  1 & 0 & 0 \end{array}\right)  = 3
\]

(on vérifie en effet facilement que cette dernière matrice est inversible), \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) est donc bien une base de \( {E}^{ * } \) .

> (it is indeed easy to verify that this last matrix is invertible), \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) is therefore indeed a basis of \( {E}^{ * } \).

On a vu (voir la partie 4.5) que la matrice \( M \) de passage de \( \left( {{e}_{1}^{ * },{e}_{2}^{ * },{e}_{3}^{ * }}\right) \) à \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) est \( {}^{t}{C}^{-1}, C \) étant la matrice de passage de \( \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) à \( \left( {{f}_{1},{f}_{2},{f}_{3}}\right) \) . Donc \( M = {}^{\mathrm{t}}{C}^{-1} \) , ce qui entraîne \( C = {}^{\mathrm{t}}{M}^{-1} = {\left( {}^{\mathrm{t}}M\right) }^{-1} \) . On calcule facilement \( \left( {{}^{\mathrm{t}}{M}^{-1}}\right) \) (inverser le système \( Y = {}^{\mathrm{t}}{MX} \) en un système donnant \( X \) en fonction de \( Y \) ). On trouve

> We have seen (see section 4.5) that the transition matrix \( M \) from \( \left( {{e}_{1}^{ * },{e}_{2}^{ * },{e}_{3}^{ * }}\right) \) to \( \left( {{f}_{1}^{ * },{f}_{2}^{ * },{f}_{3}^{ * }}\right) \) is \( {}^{t}{C}^{-1}, C \), which is the transition matrix from \( \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) to \( \left( {{f}_{1},{f}_{2},{f}_{3}}\right) \). Thus \( M = {}^{\mathrm{t}}{C}^{-1} \), which implies \( C = {}^{\mathrm{t}}{M}^{-1} = {\left( {}^{\mathrm{t}}M\right) }^{-1} \). We can easily calculate \( \left( {{}^{\mathrm{t}}{M}^{-1}}\right) \) (by inverting the system \( Y = {}^{\mathrm{t}}{MX} \) into a system giving \( X \) in terms of \( Y \)). We find

\[
C = {}^{\mathrm{t}}{M}^{-1} = \frac{1}{13}\left( \begin{array}{rrr} 6 &  - 3 &  - 2 \\   - 2 & 1 & 5 \\  3 & 5 &  - 1 \end{array}\right) .
\]

Les coordonnées de \( {f}_{1},{f}_{2},{f}_{3} \) dans la base \( \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) sont les vecteurs colonnes de \( C = {}^{\mathrm{t}}{M}^{-1} \) .

> The coordinates of \( {f}_{1},{f}_{2},{f}_{3} \) in the basis \( \left( {{e}_{1},{e}_{2},{e}_{3}}\right) \) are the column vectors of \( C = {}^{\mathrm{t}}{M}^{-1} \).

EXERCICE 3 (FORMES LINÉAIRES DE \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) ). a) Soit \( f \in {\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * } \) une forme linéaire sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Montrer qu’il existe \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telle que pour tout \( X \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , f\left( X\right) = \; \operatorname{tr}\left( {AX}\right) \) .

> EXERCISE 3 (LINEAR FORMS OF \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \)). a) Let \( f \in {\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * } \) be a linear form on \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \). Show that there exists \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) such that for all \( X \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , f\left( X\right) = \; \operatorname{tr}\left( {AX}\right) \).

b) Déterminer les éléments \( f \in {\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * } \) tels que pour tout \( X, Y \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , f\left( {XY}\right) = \; f\left( {YX}\right) \) .

> b) Determine the elements \( f \in {\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * } \) such that for all \( X, Y \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , f\left( {XY}\right) = \; f\left( {YX}\right) \).

Solution. a) Si \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) , on note \( {f}_{A} \) la forme linéaire sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) définie par \( {f}_{A}\left( X\right) = \operatorname{tr}\left( {AX}\right) \) . Soit \( \varphi : {\mathcal{M}}_{n}\left( \mathbb{K}\right) \rightarrow {\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * }\;A \mapsto {f}_{A} \) . C’est une application linéaire. Nous allons montrer que \( \varphi \) est bijective, ce qui prouvera le résultat. Soit \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \operatorname{Ker}\varphi \) . Alors pour tout \( \left( {i, j}\right) \) , \( \operatorname{tr}\left( {A{E}_{i, j}}\right) = {a}_{j, i} = 0\left( {E}_{i, j}\right. \) désignant la matrice de \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) dont tous les coefficients sont nuls sauf celui d’indice \( \left( {i, j}\right) \) qui vaut 1), et donc \( A = 0 \) . Donc Ker \( \varphi = \{ 0\} \) , et \( \varphi \) est donc injective. Comme de plus \( \dim \left( {{\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * }}\right) = \dim \left( {{\mathcal{M}}_{n}\left( \mathbb{K}\right) }\right) ,\varphi \) est bijective, d’où le résultat.

> Solution. a) If \( A \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \), we denote by \( {f}_{A} \) the linear form on \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) defined by \( {f}_{A}\left( X\right) = \operatorname{tr}\left( {AX}\right) \). Let \( \varphi : {\mathcal{M}}_{n}\left( \mathbb{K}\right) \rightarrow {\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * }\;A \mapsto {f}_{A} \). This is a linear map. We will show that \( \varphi \) is bijective, which will prove the result. Let \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \operatorname{Ker}\varphi \). Then for all \( \left( {i, j}\right) \), \( \operatorname{tr}\left( {A{E}_{i, j}}\right) = {a}_{j, i} = 0\left( {E}_{i, j}\right. \) denoting the matrix of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) whose coefficients are all zero except the one with index \( \left( {i, j}\right) \) which equals 1), and thus \( A = 0 \). So Ker \( \varphi = \{ 0\} \), and \( \varphi \) is therefore injective. Since, moreover, \( \dim \left( {{\mathcal{M}}_{n}{\left( \mathbb{K}\right) }^{ * }}\right) = \dim \left( {{\mathcal{M}}_{n}\left( \mathbb{K}\right) }\right) ,\varphi \) is bijective, the result follows.

b) Soit \( f \) une telle forme linéaire. D’après la question précédente, il existe \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) telle que \( f = {f}_{A} \) , et on a pour tout \( X, Y \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , f\left( {XY}\right) = \operatorname{tr}\left( {AXY}\right) = f\left( {YX}\right) = \; \operatorname{tr}\left( {AYX}\right) \) .

> b) Let \( f \) be such a linear form. According to the previous question, there exists \( A = {\left( {a}_{i, j}\right) }_{1 \leq i, j \leq n} \in \; {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) such that \( f = {f}_{A} \), and we have for all \( X, Y \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) , f\left( {XY}\right) = \operatorname{tr}\left( {AXY}\right) = f\left( {YX}\right) = \; \operatorname{tr}\left( {AYX}\right) \).

En particulier, pour tout \( \left( {i, j, k}\right) \) avec \( i \neq k \) on a \( \operatorname{tr}\left( {A{E}_{i, j}{E}_{j, k}}\right) = \operatorname{tr}\left( {A{E}_{j, k}{E}_{i, j}}\right) \;\left( *\right) \) . Or \( {E}_{i, j}{E}_{j, k} = {E}_{i, k} \) et \( {E}_{j, k}{E}_{i, j} = 0 \) car \( k \neq i \) , donc (*) s’écrit aussi \( \operatorname{tr}\left( {A{E}_{i, k}}\right) = 0 \) , c’est-à-dire \( {a}_{k, i} = 0 \) . Ceci étant vrai dès que \( i \neq k \) , on en déduit que \( A \) est une matrice diagonale.

> In particular, for all \( \left( {i, j, k}\right) \) with \( i \neq k \) we have \( \operatorname{tr}\left( {A{E}_{i, j}{E}_{j, k}}\right) = \operatorname{tr}\left( {A{E}_{j, k}{E}_{i, j}}\right) \;\left( *\right) \). However, \( {E}_{i, j}{E}_{j, k} = {E}_{i, k} \) and \( {E}_{j, k}{E}_{i, j} = 0 \) because \( k \neq i \), so (*) can also be written as \( \operatorname{tr}\left( {A{E}_{i, k}}\right) = 0 \), that is to say \( {a}_{k, i} = 0 \). Since this is true whenever \( i \neq k \), we deduce that \( A \) is a diagonal matrix.

Maintenant pour tout \( \left( {i, j}\right) \) on a \( \operatorname{tr}\left( {A{E}_{i, j}{E}_{j, i}}\right) = \operatorname{tr}\left( {A{E}_{j, i}{E}_{i, j}}\right) \) , c’est-à-dire \( \operatorname{tr}\left( {A{E}_{i, i}}\right) = \; \operatorname{tr}\left( {A{E}_{j, j}}\right) \) , donc \( {a}_{i, i} = {a}_{j, j} \) et ceci pour tout \( \left( {i, j}\right) \) . Ainsi, \( A \) est une matrice scalaire, donc il existe \( \lambda \in \mathbb{K} \) tel que \( f = \lambda \) tr. Réciproquement toute forme linéaire de cette forme répond au problème posé.

> Now for all \( \left( {i, j}\right) \) we have \( \operatorname{tr}\left( {A{E}_{i, j}{E}_{j, i}}\right) = \operatorname{tr}\left( {A{E}_{j, i}{E}_{i, j}}\right) \) , that is to say \( \operatorname{tr}\left( {A{E}_{i, i}}\right) = \; \operatorname{tr}\left( {A{E}_{j, j}}\right) \) , therefore \( {a}_{i, i} = {a}_{j, j} \) and this for all \( \left( {i, j}\right) \) . Thus, \( A \) is a scalar matrix, so there exists \( \lambda \in \mathbb{K} \) such that \( f = \lambda \) tr. Conversely, any linear form of this form satisfies the stated problem.

EXERCICE 4. On note \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) l’espace vectoriel \( \{ P \in \mathbb{R}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . Soit

> EXERCISE 4. Let \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) be the vector space \( \{ P \in \mathbb{R}\left\lbrack X\right\rbrack \mid \deg \left( P\right) \leq n\} \) . Let

\[
\varphi  : {\mathbb{R}}_{n}\left\lbrack  X\right\rbrack   \rightarrow  \mathbb{R}\;P \mapsto  {\int }_{-1}^{1}\frac{P\left( t\right) {dt}}{1 + {t}^{2}}.
\]

a) Soient \( {x}_{0},\ldots ,{x}_{n}n + 1 \) nombres réels distincts deux à deux. Démontrer qu’il existe \( {\lambda }_{0},\ldots ,{\lambda }_{n} \in \mathbb{R} \) tels que pour tout \( P \in {\mathbb{R}}_{n}\left\lbrack X\right\rbrack ,\varphi \left( P\right) = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}P\left( {x}_{i}\right) \) . Donner une méthode pratique de calcul des \( {\lambda }_{i} \) .

> a) Let \( {x}_{0},\ldots ,{x}_{n}n + 1 \) be pairwise distinct real numbers. Prove that there exist \( {\lambda }_{0},\ldots ,{\lambda }_{n} \in \mathbb{R} \) such that for all \( P \in {\mathbb{R}}_{n}\left\lbrack X\right\rbrack ,\varphi \left( P\right) = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}P\left( {x}_{i}\right) \) . Provide a practical method for calculating the \( {\lambda }_{i} \) .

b) On suppose \( n \) impair. Démontrer qu’il existe \( n \) réels \( {x}_{1},\ldots ,{x}_{n} \) et \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in \mathbb{R} \) tels que

> b) Assume \( n \) is odd. Prove that there exist \( n \) real numbers \( {x}_{1},\ldots ,{x}_{n} \) and \( {\lambda }_{1},\ldots ,{\lambda }_{n} \in \mathbb{R} \) such that

\[
\forall P \in  {\mathbb{R}}_{n}\left\lbrack  X\right\rbrack  ,\;\varphi \left( P\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}P\left( {x}_{i}\right) .
\]

Solution. a) L’application \( \varphi \) est une forme linéaire sur \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) . Par ailleurs, on a dim \( \left( {{\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * }}\right) = \; \dim \left( {{\mathbb{R}}_{n}\left\lbrack X\right\rbrack }\right) = n + 1 \) (une base de \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) est \( \left( {1, X,\ldots ,{X}^{n}}\right) ). \)

> Solution. a) The map \( \varphi \) is a linear form on \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) . Furthermore, we have dim \( \left( {{\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * }}\right) = \; \dim \left( {{\mathbb{R}}_{n}\left\lbrack X\right\rbrack }\right) = n + 1 \) (a basis of \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) is \( \left( {1, X,\ldots ,{X}^{n}}\right) ). \)

Ceci étant, pour tout \( i,0 \leq i \leq n \) , on définit la forme linéaire \( {\varphi }_{i} \) sur \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) par \( {\varphi }_{i}\left( P\right) = P\left( {x}_{i}\right) \) . Nous allons montrer que les \( {\left( {\varphi }_{i}\right) }_{0 \leq i \leq n} \) forment une famille libre. Supposons \( \mathop{\sum }\limits_{{i = 0}}^{n}{\mu }_{i}{\varphi }_{i} = 0\;\left( *\right) \) . Pour tout \( k \) définissons \( {P}_{k} = \mathop{\prod }\limits_{\substack{{0 \leq i \leq n} \\ {i \neq k} }}\left( {X - {x}_{i}}\right) \in {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) . On a \( {\varphi }_{i}\left( {P}_{k}\right) = 0 \) si \( k \neq i \) , et donc en appliquant la relation (*) à \( {P}_{k} \) , on trouve \( {\mu }_{k}\mathop{\prod }\limits_{{i \neq k}}\left( {{x}_{k} - {x}_{i}}\right) = 0 \) . Les \( {x}_{i} \) étant distincts, ceci entraîne \( {\mu }_{k} = 0 \) , et ceci pour tout \( k \) .

> Given this, for any \( i,0 \leq i \leq n \), we define the linear form \( {\varphi }_{i} \) on \( {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \) by \( {\varphi }_{i}\left( P\right) = P\left( {x}_{i}\right) \). We will show that the \( {\left( {\varphi }_{i}\right) }_{0 \leq i \leq n} \) form a linearly independent family. Suppose \( \mathop{\sum }\limits_{{i = 0}}^{n}{\mu }_{i}{\varphi }_{i} = 0\;\left( *\right) \). For any \( k \), define \( {P}_{k} = \mathop{\prod }\limits_{\substack{{0 \leq i \leq n} \\ {i \neq k} }}\left( {X - {x}_{i}}\right) \in {\mathbb{R}}_{n}\left\lbrack X\right\rbrack \). We have \( {\varphi }_{i}\left( {P}_{k}\right) = 0 \) if \( k \neq i \), and thus by applying relation (*) to \( {P}_{k} \), we find \( {\mu }_{k}\mathop{\prod }\limits_{{i \neq k}}\left( {{x}_{k} - {x}_{i}}\right) = 0 \). Since the \( {x}_{i} \) are distinct, this implies \( {\mu }_{k} = 0 \), and this for any \( k \).

Les \( {\left( {\varphi }_{i}\right) }_{0 < i < n} \) forment donc une famille libre de \( n + 1 \) éléments de \( {\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * } \) . Comme \( {\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * } \) est de dimension \( n + 1 \) , on en déduit que c’est une base de \( {\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * } \) . En particulier, il existe \( {\lambda }_{0},\ldots ,{\lambda }_{n} \in \mathbb{R} \) tels que \( \varphi = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}{\varphi }_{i} \) , et donc

> The \( {\left( {\varphi }_{i}\right) }_{0 < i < n} \) therefore form a linearly independent family of \( n + 1 \) elements of \( {\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * } \). Since \( {\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * } \) is of dimension \( n + 1 \), we deduce that it is a basis of \( {\mathbb{R}}_{n}{\left\lbrack X\right\rbrack }^{ * } \). In particular, there exist \( {\lambda }_{0},\ldots ,{\lambda }_{n} \in \mathbb{R} \) such that \( \varphi = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}{\varphi }_{i} \), and thus

\[
\forall P \in  {\mathbb{R}}_{n}\left\lbrack  X\right\rbrack  ,\;\varphi \left( P\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}{\varphi }_{i}\left( P\right)  = \mathop{\sum }\limits_{{i = 0}}^{n}{\lambda }_{i}P\left( {x}_{i}\right) .
\]

Donnons maintenant une méthode pratique de calcul de \( {\lambda }_{k} \) . Comme pour tout \( i \neq k,{P}_{i}\left( {x}_{k}\right) = \) 0, on trouve en appliquant la relation précédente à \( {P}_{k} \) que

> Let us now provide a practical method for calculating \( {\lambda }_{k} \). As for any \( i \neq k,{P}_{i}\left( {x}_{k}\right) = \) 0, we find by applying the previous relation to \( {P}_{k} \) that

\[
{\lambda }_{k}{P}_{k}\left( {x}_{k}\right)  = \varphi \left( {P}_{k}\right) ,\;\text{ donc }\;{\lambda }_{k} = \frac{\varphi \left( {P}_{k}\right) }{\mathop{\prod }\limits_{{i \neq  k}}\left( {{x}_{k} - {x}_{i}}\right) }.
\]

\( \left( {* * }\right) \)

> b) Il s’agit en fait de choisir les \( {\left( {x}_{i}\right) }_{0 \leq i \leq n} \) de sorte que le coefficient \( {\lambda }_{0} \) de \( P\left( {x}_{0}\right) \) soit nul. D’après (**), ceci sera vérifié si

b) It is actually a matter of choosing the \( {\left( {x}_{i}\right) }_{0 \leq i \leq n} \) such that the coefficient \( {\lambda }_{0} \) of \( P\left( {x}_{0}\right) \) is zero. According to (**), this will be satisfied if

\[
\varphi \left( {P}_{0}\right)  = {\int }_{-1}^{1}\frac{{P}_{0}\left( t\right) }{1 + {t}^{2}}{dt} = 0,
\]

ce qui sera le cas si l'intégrande est une fonction impaire. Pour cela, notons \( k \) l’entier tel que \( n = {2k} + 1 \) et fixons des nombres réels \( 0 < {a}_{1} < \ldots < {a}_{k} \) . Si \( 1 \leq i \leq k \) , on pose \( {x}_{{2i} - 1} = {a}_{i} \) et \( {x}_{2i} = - {a}_{i} \) , et \( {x}_{{2k} + 1} = 0 \) , de sorte que

> which will be the case if the integrand is an odd function. To this end, let \( k \) be the integer such that \( n = {2k} + 1 \) and fix real numbers \( 0 < {a}_{1} < \ldots < {a}_{k} \). If \( 1 \leq i \leq k \), we set \( {x}_{{2i} - 1} = {a}_{i} \) and \( {x}_{2i} = - {a}_{i} \), and \( {x}_{{2k} + 1} = 0 \), such that

\[
{P}_{0}\left( X\right)  = \mathop{\prod }\limits_{{i = 1}}^{{{2k} + 1}}\left( {X - {x}_{i}}\right)  = X\mathop{\prod }\limits_{{i = 1}}^{k}\left( {{X}^{2} - {a}_{k}^{2}}\right) .
\]

On s’aperçoit que \( t \mapsto {P}_{0}\left( t\right) \) est une application impaire; il en est donc de même de l’application \( t \mapsto \frac{{P}_{0}\left( t\right) }{1 + {t}^{2}} \) , et donc \( {\lambda }_{0} = {\int }_{-1}^{1}\frac{{P}_{0}\left( t\right) }{1 + {t}^{2}}{dt} = 0 \) , d’où le résultat. (Remarquons que l’on peut choisir \( {x}_{0} \) comme l’on veut pourvu qu’il soit différent des \( {x}_{i} \) déjà choisis pour \( 1 \leq i \leq n \) ).

> We notice that \( t \mapsto {P}_{0}\left( t\right) \) is an odd map; the same is therefore true for the map \( t \mapsto \frac{{P}_{0}\left( t\right) }{1 + {t}^{2}} \), and thus \( {\lambda }_{0} = {\int }_{-1}^{1}\frac{{P}_{0}\left( t\right) }{1 + {t}^{2}}{dt} = 0 \), hence the result. (Note that we can choose \( {x}_{0} \) as we wish, provided it is different from the \( {x}_{i} \) already chosen for \( 1 \leq i \leq n \)).

Remarque. Dans cadre de l'étude des polynômes orthogonaux (voir le sujet d'étude 3 page 110), on montre qu’il existe une identité du type \( \varphi \left( P\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}P\left( {x}_{i}\right) \) (avec les \( {x}_{i} \) et \( {\lambda }_{i} \) bien choisis) valable pour tout polynôme de degré \( < {2n} \) .

> Remark. In the context of the study of orthogonal polynomials (see study topic 3 on page 110), it is shown that there exists an identity of the type \( \varphi \left( P\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{\lambda }_{i}P\left( {x}_{i}\right) \) (with well-chosen \( {x}_{i} \) and \( {\lambda }_{i} \)) valid for any polynomial of degree \( < {2n} \).

EXERCICE 5. Soit \( E \) un \( \mathbb{R} \) -e.v de dimension finie \( n \in {\mathbb{N}}^{ * } \) .

> EXERCISE 5. Let \( E \) be a finite-dimensional \( \mathbb{R} \)-v.s. \( n \in {\mathbb{N}}^{ * } \).

1/ Soit \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une famille de vecteurs de \( E,\left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) une famille de formes linéaires sur \( E \) . Soit \( f : E \rightarrow E\;x \mapsto \mathop{\sum }\limits_{{i = 1}}^{n}{\varphi }_{i}\left( x\right) {e}_{i} \) . On a \( f \in \mathcal{L}\left( E\right) \) . Montrer que \( \operatorname{rg}f + n \geq \operatorname{rg}\left\{ {{e}_{1},\ldots ,{e}_{n}}\right\} + \operatorname{rg}\left\{ {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right\} \) . Peut-on remplacer \( n \) par une constante plus petite ?

> 1/ Let \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) be a family of vectors of \( E,\left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) and a family of linear forms on \( E \). Let \( f : E \rightarrow E\;x \mapsto \mathop{\sum }\limits_{{i = 1}}^{n}{\varphi }_{i}\left( x\right) {e}_{i} \). We have \( f \in \mathcal{L}\left( E\right) \). Show that \( \operatorname{rg}f + n \geq \operatorname{rg}\left\{ {{e}_{1},\ldots ,{e}_{n}}\right\} + \operatorname{rg}\left\{ {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right\} \). Can \( n \) be replaced by a smaller constant?

2 / a) Soit \( {\varphi }_{1},\ldots ,{\varphi }_{r}r \) formes linéaires sur \( E \) indépendantes et \( {e}_{1},\ldots ,{e}_{r}r \) vecteurs de \( E \) indépendants. Soit \( f \in \mathcal{L}\left( E\right) \) défini par \( f\left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{r}{\varphi }_{i}\left( x\right) {e}_{i} \) . Quel est le rang de \( f \) ?

> 2 / a) Let \( {\varphi }_{1},\ldots ,{\varphi }_{r}r \) be independent linear forms on \( E \) and \( {e}_{1},\ldots ,{e}_{r}r \) be independent vectors of \( E \). Let \( f \in \mathcal{L}\left( E\right) \) be defined by \( f\left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{r}{\varphi }_{i}\left( x\right) {e}_{i} \). What is the rank of \( f \)?

b) Soit \( u \in \mathcal{L}\left( E\right) \) , rg \( u = q \geq 1 \) et \( \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) une base de Im \( u \) . Montrer qu’il existe \( q \) formes linéaires \( {\varphi }_{1},\ldots ,{\varphi }_{q} \) telles que pour tout \( x \in E, u\left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{q}{\varphi }_{i}\left( x\right) {e}_{i} \) . Que dire de la famille \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{q}}\right) \) ?

> b) Let \( u \in \mathcal{L}\left( E\right) \), rg \( u = q \geq 1 \) and \( \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) be a basis of Im \( u \). Show that there exist \( q \) linear forms \( {\varphi }_{1},\ldots ,{\varphi }_{q} \) such that for all \( x \in E, u\left( x\right) = \mathop{\sum }\limits_{{i = 1}}^{q}{\varphi }_{i}\left( x\right) {e}_{i} \). What can be said about the family \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{q}}\right) \)?

c) Montrer que tout endomorphisme est la somme de deux automorphismes.

> c) Show that every endomorphism is the sum of two automorphisms.

Solution. 1/ Soit \( p = \operatorname{rg}\left\{ {{e}_{1},\ldots ,{e}_{n}}\right\} \) et \( q = \operatorname{rg}\left\{ {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right\} \) . Soit \( u \in \mathcal{L}\left( {E,{\mathbb{R}}^{n}}\right) \) définie par \( u\left( x\right) = \left( {{\varphi }_{1}\left( x\right) ,\ldots ,{\varphi }_{n}\left( x\right) }\right) \) et soit \( v \in \mathcal{L}\left( {{\mathbb{R}}^{n}, E}\right) \) définie par \( v\left( {{x}_{1},\ldots ,{x}_{n}}\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \) , de sorte que \( f = v \circ u \) .

> Solution. 1/ Let \( p = \operatorname{rg}\left\{ {{e}_{1},\ldots ,{e}_{n}}\right\} \) and \( q = \operatorname{rg}\left\{ {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right\} \). Let \( u \in \mathcal{L}\left( {E,{\mathbb{R}}^{n}}\right) \) be defined by \( u\left( x\right) = \left( {{\varphi }_{1}\left( x\right) ,\ldots ,{\varphi }_{n}\left( x\right) }\right) \) and let \( v \in \mathcal{L}\left( {{\mathbb{R}}^{n}, E}\right) \) be defined by \( v\left( {{x}_{1},\ldots ,{x}_{n}}\right) = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{e}_{i} \), such that \( f = v \circ u \).

D’après le théorème 3 page 134, Ker \( u = \left\{ {x \in E\mid \forall i,{\varphi }_{i}\left( x\right) = 0}\right\} \) est de dimension \( n - q \) , donc \( \operatorname{rg}u = n - \dim \left( {\operatorname{Ker}u}\right) = q \) . On a \( \operatorname{Im}v = \operatorname{Vect}\left\{ {{e}_{1},\ldots ,{e}_{n}}\right\} \) donc \( \operatorname{rg}v = p \) .

> According to theorem 3 on page 134, Ker \( u = \left\{ {x \in E\mid \forall i,{\varphi }_{i}\left( x\right) = 0}\right\} \) has dimension \( n - q \), so \( \operatorname{rg}u = n - \dim \left( {\operatorname{Ker}u}\right) = q \). We have \( \operatorname{Im}v = \operatorname{Vect}\left\{ {{e}_{1},\ldots ,{e}_{n}}\right\} \) therefore \( \operatorname{rg}v = p \).

Ceci étant, on a \( \operatorname{Im}\left( {v \circ u}\right) = v\left( {\operatorname{Im}u}\right) \) . Soit \( F = \operatorname{Im}u \cap \operatorname{Ker}v \) et \( S \) un supplémentaire de \( F \) dans \( \operatorname{Im}u \) de sorte que \( \operatorname{Im}u = F \oplus S \) . Comme \( S \cap \operatorname{Ker}v = \{ 0\} \) , la restriction de \( v \) à \( S \) est injective donc \( v\left( {\operatorname{Im}u}\right) = v\left( F\right) + v\left( S\right) = v\left( S\right) \) est de dimension \( \dim S \) . On en déduit \( \operatorname{rg}\left( {v \circ u}\right) = \dim S \) . Or \( F \subset \operatorname{Ker}v \) donc \( \dim F \leq \dim \left( {\operatorname{Ker}v}\right) = n - \operatorname{rg}v \) , donc

> Given this, we have \( \operatorname{Im}\left( {v \circ u}\right) = v\left( {\operatorname{Im}u}\right) \). Let \( F = \operatorname{Im}u \cap \operatorname{Ker}v \) and \( S \) be a complement of \( F \) in \( \operatorname{Im}u \) such that \( \operatorname{Im}u = F \oplus S \). Since \( S \cap \operatorname{Ker}v = \{ 0\} \), the restriction of \( v \) to \( S \) is injective, so \( v\left( {\operatorname{Im}u}\right) = v\left( F\right) + v\left( S\right) = v\left( S\right) \) has dimension \( \dim S \). We deduce \( \operatorname{rg}\left( {v \circ u}\right) = \dim S \). However, \( F \subset \operatorname{Ker}v \) therefore \( \dim F \leq \dim \left( {\operatorname{Ker}v}\right) = n - \operatorname{rg}v \), so

\[
\operatorname{rg}f = \operatorname{rg}\left( {v \circ  u}\right)  = \dim S = \operatorname{rg}u - \dim F \geq  \operatorname{rg}u + \operatorname{rg}v - n = p + q - n,
\]

d’où le résultat. On ne peut pas remplacer \( n \) par une constante plus petite (prendre tous les \( {\varphi }_{i} \) nuls et \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) une base de \( E \) ).

> hence the result. One cannot replace \( n \) with a smaller constant (take all \( {\varphi }_{i} \) to be zero and \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) a basis of \( E \)).

Remarque : On a montré le résultat général suivant : pour tout \( \left( {u, v}\right) ,\operatorname{rg}\left( {v \circ u}\right) \geq \operatorname{rg}u + \operatorname{rg}v - n \) .

> Remark: We have shown the following general result: for all \( \left( {u, v}\right) ,\operatorname{rg}\left( {v \circ u}\right) \geq \operatorname{rg}u + \operatorname{rg}v - n \).

2 / a) On a \( x \in \operatorname{Ker}f \Leftrightarrow \mathop{\sum }\limits_{{i = 1}}^{r}{\varphi }_{i}\left( x\right) {e}_{i} = 0 \) , et comme les \( {e}_{i} \) sont indépendants, ceci entraîne \( \operatorname{Ker}f = \left\{ {x \in E\mid \forall i,{\varphi }_{i}\left( x\right) = 0}\right\} = {\left( \operatorname{Vect}\left\{ {\varphi }_{1},\ldots ,{\varphi }_{r}\right\} \right) }^{ \circ } \) . Les \( {\varphi }_{i} \) étant linéairement indépendants, on a donc \( \dim \left( {\operatorname{Ker}f}\right) = n - \dim \left( {\operatorname{Vect}\left\{ {{\varphi }_{1},\ldots ,{\varphi }_{r}}\right\} }\right) = n - r \) , d’où \( \operatorname{rg}f = n - \dim \left( {\operatorname{Ker}f}\right) = r \) .

> 2 / a) We have \( x \in \operatorname{Ker}f \Leftrightarrow \mathop{\sum }\limits_{{i = 1}}^{r}{\varphi }_{i}\left( x\right) {e}_{i} = 0 \), and since the \( {e}_{i} \) are independent, this implies \( \operatorname{Ker}f = \left\{ {x \in E\mid \forall i,{\varphi }_{i}\left( x\right) = 0}\right\} = {\left( \operatorname{Vect}\left\{ {\varphi }_{1},\ldots ,{\varphi }_{r}\right\} \right) }^{ \circ } \). The \( {\varphi }_{i} \) being linearly independent, we therefore have \( \dim \left( {\operatorname{Ker}f}\right) = n - \dim \left( {\operatorname{Vect}\left\{ {{\varphi }_{1},\ldots ,{\varphi }_{r}}\right\} }\right) = n - r \), hence \( \operatorname{rg}f = n - \dim \left( {\operatorname{Ker}f}\right) = r \).

b) Pour tout \( i,1 \leq i \leq q \) , il existe \( {\varepsilon }_{i} \in E \) tel que \( u\left( {\varepsilon }_{i}\right) = {e}_{i} \) . La famille \( {\left( {\varepsilon }_{i}\right) }_{1 \leq i \leq q} \) est libre car si \( \mathop{\sum }\limits_{i}{\lambda }_{i}{\varepsilon }_{i} = 0 \) , alors \( 0 = u\left( {\mathop{\sum }\limits_{i}{\lambda }_{i}{\varepsilon }_{i}}\right) = \mathop{\sum }\limits_{i}{\lambda }_{i}{e}_{i} \) donc pour tout \( i,{\lambda }_{i} = 0 \) . Soit \( \left( {{\varepsilon }_{q + 1},\ldots ,{\varepsilon }_{n}}\right) \) une base de Ker \( u \) . Si \( 1 \leq i \leq q,{\varepsilon }_{i} \notin \operatorname{Ker}u \) , on en déduit que \( \left( {{\varepsilon }_{1},\ldots ,{\varepsilon }_{n}}\right) \) est une base de \( E \) . On remarque maintenant que

> b) For all \( i,1 \leq i \leq q \), there exists \( {\varepsilon }_{i} \in E \) such that \( u\left( {\varepsilon }_{i}\right) = {e}_{i} \). The family \( {\left( {\varepsilon }_{i}\right) }_{1 \leq i \leq q} \) is linearly independent because if \( \mathop{\sum }\limits_{i}{\lambda }_{i}{\varepsilon }_{i} = 0 \), then \( 0 = u\left( {\mathop{\sum }\limits_{i}{\lambda }_{i}{\varepsilon }_{i}}\right) = \mathop{\sum }\limits_{i}{\lambda }_{i}{e}_{i} \) so for all \( i,{\lambda }_{i} = 0 \). Let \( \left( {{\varepsilon }_{q + 1},\ldots ,{\varepsilon }_{n}}\right) \) be a basis of Ker \( u \). If \( 1 \leq i \leq q,{\varepsilon }_{i} \notin \operatorname{Ker}u \), we deduce that \( \left( {{\varepsilon }_{1},\ldots ,{\varepsilon }_{n}}\right) \) is a basis of \( E \). We now note that

\[
\forall x = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}{\varepsilon }_{i},\;u\left( x\right)  = \mathop{\sum }\limits_{{i = 1}}^{n}{x}_{i}u\left( {\varepsilon }_{i}\right)  = \mathop{\sum }\limits_{{i = 1}}^{q}{\varepsilon }_{i}^{ * }\left( x\right) {e}_{i}.
\]

On obtient donc le résultat en prenant \( {\varphi }_{i} = {\varepsilon }_{i}^{ * } \) pour \( 1 \leq i \leq q \) . Il est clair que \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{q}}\right) \) forme une famille libre.

> We thus obtain the result by taking \( {\varphi }_{i} = {\varepsilon }_{i}^{ * } \) for \( 1 \leq i \leq q \). It is clear that \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{q}}\right) \) forms a linearly independent family.

c) Soit \( u \in \mathcal{L}\left( E\right) \) . D’après la question précédente, si \( \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) est une base de \( \operatorname{Im}u \) , il existe \( q \) formes linéaires indépendantes \( {\varphi }_{1},\ldots ,{\varphi }_{q} \) telles que \( u = \mathop{\sum }\limits_{{i = 1}}^{q}{\varphi }_{i} \cdot {e}_{i} \) . Complétons \( \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) en une base \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) de \( E \) , et \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{q}}\right) \) en une base \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) de \( {E}^{ * } \) . On pose

> c) Let \( u \in \mathcal{L}\left( E\right) \) . According to the previous question, if \( \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) is a basis of \( \operatorname{Im}u \) , there exist \( q \) independent linear forms \( {\varphi }_{1},\ldots ,{\varphi }_{q} \) such that \( u = \mathop{\sum }\limits_{{i = 1}}^{q}{\varphi }_{i} \cdot {e}_{i} \) . Let us complete \( \left( {{e}_{1},\ldots ,{e}_{q}}\right) \) into a basis \( \left( {{e}_{1},\ldots ,{e}_{n}}\right) \) of \( E \) , and \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{q}}\right) \) into a basis \( \left( {{\varphi }_{1},\ldots ,{\varphi }_{n}}\right) \) of \( {E}^{ * } \) . We set

\[
{u}_{1} = \frac{1}{2}\mathop{\sum }\limits_{{i = 1}}^{q}{\varphi }_{i} \cdot  {e}_{i} + \mathop{\sum }\limits_{{i = q + 1}}^{n}{\varphi }_{i} \cdot  {e}_{i}\;\text{ et }\;{u}_{2} = \frac{1}{2}\mathop{\sum }\limits_{{i = 1}}^{q}{\varphi }_{i} \cdot  {e}_{i} - \mathop{\sum }\limits_{{i = q + 1}}^{n}{\varphi }_{i} \cdot  {e}_{i}.
\]

D’après \( 2/\mathrm{a}) \) , rg \( {u}_{1} = \operatorname{rg}{u}_{2} = n \) . Or \( u = {u}_{1} + {u}_{2} \) . On peut donc écrire \( u \) comme somme de deux automorphismes.

> According to \( 2/\mathrm{a}) \) , rg \( {u}_{1} = \operatorname{rg}{u}_{2} = n \) . However, \( u = {u}_{1} + {u}_{2} \) . We can therefore write \( u \) as the sum of two automorphisms.
