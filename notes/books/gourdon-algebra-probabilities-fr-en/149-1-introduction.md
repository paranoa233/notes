### 1. Introduction

On se donne un endomorphisme \( f \in \mathcal{L}\left( E\right) \) . Nous commençons par donner quelques rappels des résultats de l'exercice 3 de la page 188.

> Let \( f \in \mathcal{L}\left( E\right) \) be an endomorphism. We begin by recalling some results from exercise 3 on page 188.

Notation. On note \( {\Pi }_{f} \) le polynôme minimal de \( f \) , et \( {\mathcal{L}}_{f} \) l’ensemble \( \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

> Notation. Let \( {\Pi }_{f} \) denote the minimal polynomial of \( f \) , and \( {\mathcal{L}}_{f} \) the set \( \{ P\left( f\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

Si \( x \in E \) , on note \( {P}_{x} \) le polynôme unitaire engendrant l’idéal \( \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) \left( x\right) = 0\} \) et \( {E}_{x} \) l’ensemble \( \{ P\left( f\right) \left( x\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

> If \( x \in E \) , we denote by \( {P}_{x} \) the monic polynomial generating the ideal \( \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) \left( x\right) = 0\} \) and by \( {E}_{x} \) the set \( \{ P\left( f\right) \left( x\right) \mid P \in \mathbb{K}\left\lbrack X\right\rbrack \} \) .

Proposition 1. Si \( k = \deg \left( {\Pi }_{f}\right) \) , l’ensemble \( {\mathcal{L}}_{f} \) est un s.e.v de \( \mathcal{L}\left( E\right) \) de dimension \( k \) , dont une base est \( \left( {{\mathrm{{Id}}}_{E}, f,\ldots ,{f}^{k - 1}}\right) \) .

> Proposition 1. If \( k = \deg \left( {\Pi }_{f}\right) \) , the set \( {\mathcal{L}}_{f} \) is a subspace of \( \mathcal{L}\left( E\right) \) of dimension \( k \) , for which a basis is \( \left( {{\mathrm{{Id}}}_{E}, f,\ldots ,{f}^{k - 1}}\right) \) .

\( {Si}\ell = \deg \left( {P}_{x}\right) \) , l’ensemble \( {E}_{x} \) est un s.e.v de \( E \) de dimension \( \ell \) , dont une base est \( \left( {x,\ldots ,{f}^{\ell - 1}\left( x\right) }\right) \) .

> \( {Si}\ell = \deg \left( {P}_{x}\right) \) , the set \( {E}_{x} \) is a subspace of \( E \) of dimension \( \ell \) , for which a basis is \( \left( {x,\ldots ,{f}^{\ell - 1}\left( x\right) }\right) \) .

Démonstration. L’application \( \mathbb{K}\left\lbrack X\right\rbrack \rightarrow \mathcal{L}\left( E\right) \;P \mapsto P\left( f\right) \) est linéaire. Son image est \( {\mathcal{L}}_{f} \) , c’est donc un s.e.v, et son noyau est \( \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) = 0\} = \left( {\Pi }_{f}\right) \) . Ainsi, \( {\mathcal{L}}_{f} \) est isomorphe à \( \mathbb{K}\left\lbrack X\right\rbrack /\left( {\Pi }_{f}\right) \) . Ce dernier étant de dimension \( k \) dont une base est \( \left( {1,\bar{X},\ldots ,{\bar{X}}^{k - 1}}\right) \) (voir le théo-rème 4 de la page 65) on en déduit par isomorphisme la première partie de la proposition.

> Proof. The map \( \mathbb{K}\left\lbrack X\right\rbrack \rightarrow \mathcal{L}\left( E\right) \;P \mapsto P\left( f\right) \) is linear. Its image is \( {\mathcal{L}}_{f} \) , so it is a subspace, and its kernel is \( \{ P \in \mathbb{K}\left\lbrack X\right\rbrack \mid P\left( f\right) = 0\} = \left( {\Pi }_{f}\right) \) . Thus, \( {\mathcal{L}}_{f} \) is isomorphic to \( \mathbb{K}\left\lbrack X\right\rbrack /\left( {\Pi }_{f}\right) \) . Since the latter is of dimension \( k \) with a basis \( \left( {1,\bar{X},\ldots ,{\bar{X}}^{k - 1}}\right) \) (see theorem 4 on page 65), we deduce the first part of the proposition by isomorphism.

La seconde partie se traite de manière analogue en considérant l’application \( \mathbb{K}\left\lbrack X\right\rbrack \rightarrow E\;P \mapsto \; P\left( f\right) \left( x\right) \) .

> The second part is handled analogously by considering the map \( \mathbb{K}\left\lbrack X\right\rbrack \rightarrow E\;P \mapsto \; P\left( f\right) \left( x\right) \) .

La propriété qui suit est cruciale dans la suite de cette annexe (elle est prouvée dans l'exercice 3 page 188).

> The following property is crucial for the remainder of this appendix (it is proven in exercise 3 on page 188).

Proposition 2. Il existe \( x \in E \) tel que \( {P}_{x} = {\Pi }_{f} \) .

> Proposition 2. There exists \( x \in E \) such that \( {P}_{x} = {\Pi }_{f} \) .

##### Cyclic endomorphisms.

*Français : Endomorphismes cycliques.*

DéFINITION 1. On dit que \( f \) est cyclique s’il existe \( x \in E \) tel que \( {E}_{x} = E \) . D’après les propositions précédentes, ceci équivaut à dire que \( \deg \left( {\Pi }_{f}\right) = n \) (ou encore que \( {\Pi }_{f} = \; {\left( -1\right) }^{n}{P}_{f} \) où \( {P}_{f} \) désigne le polynôme caractéristique de \( f \) ). DéFINITION 2. Soit \( P = {X}^{p} + {a}_{p - 1}{X}^{p - 1} + \cdots + {a}_{0} \in \mathbb{K}\left\lbrack X\right\rbrack \) . On appelle matrice compagnon de \( P \) la matrice

> DEFINITION 1. We say that \( f \) is cyclic if there exists \( x \in E \) such that \( {E}_{x} = E \) . According to the previous propositions, this is equivalent to saying that \( \deg \left( {\Pi }_{f}\right) = n \) (or that \( {\Pi }_{f} = \; {\left( -1\right) }^{n}{P}_{f} \) where \( {P}_{f} \) denotes the characteristic polynomial of \( f \) ). DEFINITION 2. Let \( P = {X}^{p} + {a}_{p - 1}{X}^{p - 1} + \cdots + {a}_{0} \in \mathbb{K}\left\lbrack X\right\rbrack \) . We call the companion matrix of \( P \) the matrix

\[
\mathcal{C}\left( P\right)  = \left( \begin{matrix} 0 & \cdots & \cdots & 0 &  - {a}_{0} \\  1 & 0 & & \vdots &  - {a}_{1} \\  0 & 1 &  \ddots  & \vdots & \vdots \\  \vdots &  \ddots  &  \ddots  & 0 &  - {a}_{p - 2} \\  0 & \cdots & 0 & 1 &  - {a}_{p - 1} \end{matrix}\right)  \in  {\mathcal{M}}_{p}\left( \mathbb{K}\right) .
\]

Nous avons déjà rencontré les matrices compagnons lors de la seconde démonstration du théorème de Cayley-Hamilton, et nous avions montré que le polynôme caractéristique de \( \mathcal{C}\left( P\right) \) est \( {\left( -1\right) }^{p}P \) .

> We have already encountered companion matrices during the second proof of the Cayley-Hamilton theorem, and we showed that the characteristic polynomial of \( \mathcal{C}\left( P\right) \) is \( {\left( -1\right) }^{p}P \) .

PROPOSITION 3. Soit \( f \in \mathcal{L}\left( E\right) \) un endomorphisme cyclique. Il existe une base de \( E \) dans laquelle la matrice de \( f \) soit égale à \( \mathcal{C}\left( {\Pi }_{f}\right) \) .

> PROPOSITION 3. Let \( f \in \mathcal{L}\left( E\right) \) be a cyclic endomorphism. There exists a basis of \( E \) in which the matrix of \( f \) is equal to \( \mathcal{C}\left( {\Pi }_{f}\right) \) .

Démonstration. Comme \( f \) est cyclique, il existe \( x \in E \) tel que \( {E}_{x} = E \) . On sait alors que \( \left( {x, f\left( x\right) ,\ldots ,{f}^{n - 1}\left( x\right) }\right) \) est une base de \( E \) , et dans cette base, la matrice de \( f \) est \( \mathcal{C}\left( {\Pi }_{f}\right) \) (si \( {\Pi }_{f} = {X}^{n} + {a}_{n - 1}{X}^{n - 1} + \cdots + {a}_{0} \) , l’image du dernier vecteur \( {f}^{n - 1}\left( x\right) \) de la base par \( f \) vaut \( {f}^{n}\left( x\right) = - {a}_{n - 1}{f}^{n - 1}\left( x\right) - \cdots - {a}_{0}x \) car \( {\Pi }_{f}\left( f\right) \left( x\right) = 0). \)

> Proof. Since \( f \) is cyclic, there exists \( x \in E \) such that \( {E}_{x} = E \) . We know then that \( \left( {x, f\left( x\right) ,\ldots ,{f}^{n - 1}\left( x\right) }\right) \) is a basis of \( E \) , and in this basis, the matrix of \( f \) is \( \mathcal{C}\left( {\Pi }_{f}\right) \) (if \( {\Pi }_{f} = {X}^{n} + {a}_{n - 1}{X}^{n - 1} + \cdots + {a}_{0} \) , the image of the last vector \( {f}^{n - 1}\left( x\right) \) of the basis by \( f \) is \( {f}^{n}\left( x\right) = - {a}_{n - 1}{f}^{n - 1}\left( x\right) - \cdots - {a}_{0}x \) because \( {\Pi }_{f}\left( f\right) \left( x\right) = 0). \)
