#### 3.2. Properties

*Français : 3.2. Propriétés*

PROPOSITION 1. Soit \( E \) un \( \mathbb{K} \) -e.v.n et \( f \in {\mathcal{L}}_{c}\left( E\right) \) . Soit \( \lambda \) une valeur propre de \( f \) . Alors \( \left| \lambda \right| \leq \parallel f\parallel \)

> PROPOSITION 1. Let \( E \) be a \( \mathbb{K} \) -n.v.s. and \( f \in {\mathcal{L}}_{c}\left( E\right) \) . Let \( \lambda \) be an eigenvalue of \( f \) . Then \( \left| \lambda \right| \leq \parallel f\parallel \)

Démonstration. Soit \( x \neq 0 \) un vecteur propre de \( f \) pour la valeur propre \( \lambda \) . On a \( \parallel f\left( x\right) \parallel \leq \; \parallel f\parallel \cdot \parallel x\parallel \) . Or \( \parallel f\left( x\right) \parallel = \parallel {\lambda x}\parallel = \left| \lambda \right| \cdot \parallel x\parallel \) , donc \( \left| \lambda \right| \leq \parallel f\parallel \) .

> Proof. Let \( x \neq 0 \) be an eigenvector of \( f \) for the eigenvalue \( \lambda \) . We have \( \parallel f\left( x\right) \parallel \leq \; \parallel f\parallel \cdot \parallel x\parallel \) . However \( \parallel f\left( x\right) \parallel = \parallel {\lambda x}\parallel = \left| \lambda \right| \cdot \parallel x\parallel \) , so \( \left| \lambda \right| \leq \parallel f\parallel \) .

Proposition 2. L’ensemble \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) est un ouvert dense dans \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

> Proposition 2. The set \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) is an open dense subset of \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) .

Démonstration. L’application \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \rightarrow \mathbb{K}\;M \mapsto \det M \) est continue (car det \( M \) s’exprime comme un polynôme en les coefficients de \( M \) ). L’ensemble \( {\mathbb{K}}^{ * } \) est ouvert dans \( \mathbb{K} \) , donc \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) = \; {\left( \det \right) }^{-1}\left( {\mathbb{K}}^{ * }\right) \) est ouvert.

> Proof. The map \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \rightarrow \mathbb{K}\;M \mapsto \det M \) is continuous (since det \( M \) is expressed as a polynomial in the coefficients of \( M \) ). The set \( {\mathbb{K}}^{ * } \) is open in \( \mathbb{K} \) , so \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) = \; {\left( \det \right) }^{-1}\left( {\mathbb{K}}^{ * }\right) \) is open.

Densité. Soit \( M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . Le polynôme caractéristique \( {P}_{M} \) de \( M \) n’a qu’un nombre fini de racines, donc

> Density. Let \( M \in {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) . The characteristic polynomial \( {P}_{M} \) of \( M \) has only a finite number of roots, therefore

\[
\exists \rho  > 0\;\text{ tel que }\;\forall \lambda  \in  \mathbb{K},0 < \left| \lambda \right|  < \rho ,{P}_{M}\left( \lambda \right)  \neq  0.
\]

En d’autres termes, pour tout \( \lambda \in \mathbb{K},0 < \left| \lambda \right| < \rho , M - \lambda {I}_{n} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . Or \( M = \mathop{\lim }\limits_{\substack{{\lambda \rightarrow 0} \\ {\lambda \neq 0} }}\left( {M - \lambda {I}_{n}}\right) \) . \( M \) est donc limite d’éléments de \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) .

> In other words, for all \( \lambda \in \mathbb{K},0 < \left| \lambda \right| < \rho , M - \lambda {I}_{n} \in \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) . However \( M = \mathop{\lim }\limits_{\substack{{\lambda \rightarrow 0} \\ {\lambda \neq 0} }}\left( {M - \lambda {I}_{n}}\right) \) . \( M \) is therefore a limit of elements of \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) .

Remarque 1. - Ce dernier résultat est important. Il est parfois aisé de montrer des propriétés sur \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) en les montrant d’abord sur \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) puis en les étendant par densité (voir les exercices).

> Remark 1. - This last result is important. It is sometimes easy to prove properties about \( {\mathcal{M}}_{n}\left( \mathbb{K}\right) \) by first proving them for \( \mathcal{G}{\ell }_{n}\left( \mathbb{K}\right) \) and then extending them by density (see the exercises).

- Cette dernière proposition est également vraie pour les endomorphismes en dimension finie. De manière générale, algébriquement et topologiquement, tout ce qui est vrai pour les matrices est vrai pour les endomorphismes (en dimension finie) et réciproquement.

> - This last proposition is also true for endomorphisms in finite dimension. Generally speaking, algebraically and topologically, everything that is true for matrices is true for endomorphisms (in finite dimension) and vice versa.

- En dimension infinie, \( \mathcal{G}{\ell }_{c}\left( E\right) \) est ouvert si \( E \) est un espace de Banach (voir le chapitre topologie du tome d'analyse).

> - In infinite dimension, \( \mathcal{G}{\ell }_{c}\left( E\right) \) is open if \( E \) is a Banach space (see the topology chapter of the analysis volume).
