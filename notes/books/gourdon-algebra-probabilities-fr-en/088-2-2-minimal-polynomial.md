#### 2.2. Minimal polynomial

*Français : 2.2. Polynôme minimal*

Soit \( f \in \mathcal{L}\left( E\right) \) , et soit \( I = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) = 0\} \) . Le \( \mathbb{K} \) -e.v \( \mathcal{L}\left( E\right) \) est de dimension \( {n}^{2} \) , la famille \( {\operatorname{Id}}_{E}, f,\ldots ,{f}^{{n}^{2}} \) est donc liée. Autrement dit, il existe \( \left( {{a}_{0},\ldots ,{a}_{{n}^{2}}}\right) \neq \left( {0,\ldots ,0}\right) \) tel que \( {a}_{0}{\operatorname{Id}}_{E} + {a}_{1}f + \cdots + {a}_{{n}^{2}}{f}^{{n}^{2}} = 0 \) . Donc si \( P = \mathop{\sum }\limits_{{i = 0}}^{{n}^{2}}{a}_{i}{X}^{i}, P\left( f\right) = 0 \) . Donc \( I \neq \{ 0\} \) .

> Let \( f \in \mathcal{L}\left( E\right) \), and let \( I = \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) = 0\} \). The \( \mathbb{K} \)-v.s. \( \mathcal{L}\left( E\right) \) has dimension \( {n}^{2} \), so the family \( {\operatorname{Id}}_{E}, f,\ldots ,{f}^{{n}^{2}} \) is linearly dependent. In other words, there exists \( \left( {{a}_{0},\ldots ,{a}_{{n}^{2}}}\right) \neq \left( {0,\ldots ,0}\right) \) such that \( {a}_{0}{\operatorname{Id}}_{E} + {a}_{1}f + \cdots + {a}_{{n}^{2}}{f}^{{n}^{2}} = 0 \). Thus if \( P = \mathop{\sum }\limits_{{i = 0}}^{{n}^{2}}{a}_{i}{X}^{i}, P\left( f\right) = 0 \). Therefore \( I \neq \{ 0\} \).

On voit que \( I \) est un idéal de \( \mathbb{K}\left\lbrack X\right\rbrack \) . L’anneau \( \mathbb{K}\left\lbrack X\right\rbrack \) étant principal, il existe un unique \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \) unitaire, tel que \( I = \left( P\right) = P \cdot \mathbb{K}\left\lbrack X\right\rbrack \) . Le polynôme \( P \) s’appelle le polynôme minimal de \( f \) . On le note \( {\Pi }_{f} \) . C’est le polynôme unitaire de plus bas degré annulant \( f \) , et si \( Q\left( f\right) = 0 \) , alors \( {\Pi }_{f} \mid Q\left( \right. \) car \( \left. {Q \in I = \left( {\Pi }_{f}\right) }\right) \) .

> We see that \( I \) is an ideal of \( \mathbb{K}\left\lbrack X\right\rbrack \). Since the ring \( \mathbb{K}\left\lbrack X\right\rbrack \) is a principal ideal domain, there exists a unique monic \( P \in \mathbb{K}\left\lbrack X\right\rbrack , P \) such that \( I = \left( P\right) = P \cdot \mathbb{K}\left\lbrack X\right\rbrack \). The polynomial \( P \) is called the minimal polynomial of \( f \). We denote it by \( {\Pi }_{f} \). It is the monic polynomial of lowest degree that annihilates \( f \), and if \( Q\left( f\right) = 0 \), then \( {\Pi }_{f} \mid Q\left( \right. \) because \( \left. {Q \in I = \left( {\Pi }_{f}\right) }\right) \).

Remarque 4. - En dimension infinie. cette définition reste valable à condition qu'il existe un polynôme non nul \( P \) tel que \( P\left( f\right) = 0 \) et \( P \neq 0 \) . On dit alors que \( f \) admet un polynôme minimal.

> Remark 4. - In infinite dimension, this definition remains valid provided there exists a non-zero polynomial \( P \) such that \( P\left( f\right) = 0 \) and \( P \neq 0 \). We then say that \( f \) admits a minimal polynomial.

- En terme de polynôme minimal, le théorème 2 s'interprète comme suit : \( f \) est diagonalisable si et seulement si son polynôme minimal est scindé et a toutes ses racines simples.

> - In terms of the minimal polynomial, Theorem 2 is interpreted as follows: \( f \) is diagonalizable if and only if its minimal polynomial splits and has only simple roots.

- Si \( F \) est un s.e.v stable par \( f \) , alors \( g = {f}_{\mid F} \) vérifie : \( {\Pi }_{g} \) divise \( {\Pi }_{f} \) (en effet, \( \left. {{\Pi }_{f}\left( g\right)  = 0}\right) \) .

> - If \( F \) is a subspace stable under \( f \), then \( g = {f}_{\mid F} \) satisfies: \( {\Pi }_{g} \) divides \( {\Pi }_{f} \) (indeed, \( \left. {{\Pi }_{f}\left( g\right)  = 0}\right) \).

PROPOSITION 2. Soit \( f \in \mathcal{L}\left( E\right) \) . Un scalaire \( \lambda \) est valeur propre de \( f \) si et seulement si \( \lambda \) est racine de son polynôme minimal \( {\Pi }_{f} \) .

> PROPOSITION 2. Let \( f \in \mathcal{L}\left( E\right) \). A scalar \( \lambda \) is an eigenvalue of \( f \) if and only if \( \lambda \) is a root of its minimal polynomial \( {\Pi }_{f} \).

Démonstration. Condition nécessaire. Cela résulte de la proposition 1.

> Proof. Necessary condition. This follows from Proposition 1.

Condition suffisante. Soit \( \lambda \) une racine de \( {\Pi }_{f} \) . Soit \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) tel que \( {\Pi }_{f} = \left( {X - \lambda }\right) P \) . On a \( P\left( f\right) \neq \) 0 car \( {\Pi }_{f} \) est le polynôme minimal de \( f \) et deg \( P < \deg {\Pi }_{f} \) . Or \( {\Pi }_{f}\left( f\right) = 0 = \left( {f - \lambda {\operatorname{Id}}_{E}}\right) P\left( f\right) = 0 \) , et comme \( P\left( f\right) \neq 0 \) , on en déduit que \( f - \lambda {\operatorname{Id}}_{E} \) n’est pas injectif, donc que \( \lambda \) est valeur propre de \( f \) .

> Sufficient condition. Let \( \lambda \) be a root of \( {\Pi }_{f} \) . Let \( P \in \mathbb{K}\left\lbrack X\right\rbrack \) be such that \( {\Pi }_{f} = \left( {X - \lambda }\right) P \) . We have \( P\left( f\right) \neq \) 0 because \( {\Pi }_{f} \) is the minimal polynomial of \( f \) and deg \( P < \deg {\Pi }_{f} \) . However, \( {\Pi }_{f}\left( f\right) = 0 = \left( {f - \lambda {\operatorname{Id}}_{E}}\right) P\left( f\right) = 0 \) , and since \( P\left( f\right) \neq 0 \) , we deduce that \( f - \lambda {\operatorname{Id}}_{E} \) is not injective, therefore \( \lambda \) is an eigenvalue of \( f \) .

Remarque 5. Le polynôme minimal de \( f \) a donc les mêmes racines que le polynôme caractéristique de \( f \) .

> Remark 5. The minimal polynomial of \( f \) therefore has the same roots as the characteristic polynomial of \( f \) .
