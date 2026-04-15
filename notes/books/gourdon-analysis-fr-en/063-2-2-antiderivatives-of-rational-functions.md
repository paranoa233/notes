#### 2.2. Antiderivatives of rational functions

*Français : 2.2. Primitives des fractions rationnelles*

Soit \( F \) une fraction rationnelle de \( \mathbb{R}\left( X\right) \) . Pour calculer \( \int F \) , on commence par décomposer \( F \) en éléments simples sur \( \mathbb{R} \) . On est ainsi ramené à calculer les primitives de la forme

> Let \( F \) be a rational function of \( \mathbb{R}\left( X\right) \) . To compute \( \int F \) , we begin by decomposing \( F \) into partial fractions over \( \mathbb{R} \) . We are thus reduced to computing antiderivatives of the form

\[
\int \frac{dx}{{\left( x - a\right) }^{h}}\;\left( {h \in  {\mathbb{N}}^{ * }}\right) \;\text{ et }\;\int \frac{{ax} + b}{{\left( {x}^{2} + cx + d\right) }^{h}}\;\left( {{c}^{2} - {4d} < 0, h \in  {\mathbb{N}}^{ * }}\right) .
\]

- La première primitive se calcule facilement grâce à l'expression

> - The first antiderivative is easily computed using the expression

\[
\int \frac{dx}{{\left( x - a\right) }^{h}} = \left\{  {\begin{array}{lll} \frac{1}{\left( {1 - h}\right) {\left( x - a\right) }^{h - 1}} + k & \text{ si } & h \neq  1 \\  \log \left| {x - a}\right|  + k & \text{ si } & h = 1 \end{array}.}\right.
\]

- Quant à la seconde, on commence par écrire

> - As for the second, we begin by writing

\[
\frac{{ax} + b}{{\left( {x}^{2} + cx + d\right) }^{h}}\text{ sous la forme }\frac{{2\alpha }\left( {x - p}\right) }{{\left\lbrack  {\left( x - p\right) }^{2} + {q}^{2}\right\rbrack  }^{h}} + \frac{\beta }{{\left\lbrack  {\left( x - p\right) }^{2} + {q}^{2}\right\rbrack  }^{h}}.
\]

- La primitive du premier terme dans le membre de droite est donnée par

> - The antiderivative of the first term on the right-hand side is given by

\[
\int \frac{{2\alpha }\left( {x - p}\right) }{{\left\lbrack  {\left( x - p\right) }^{2} + {q}^{2}\right\rbrack  }^{h}}{dx} = \left\{  {\begin{array}{ll} \frac{\alpha }{\left( {1 - h}\right) {\left\lbrack  {\left( x - p\right) }^{2} + {q}^{2}\right\rbrack  }^{h - 1}} + k & \text{ si }\;h \geq  2, \\  \alpha \log \left\lbrack  {{\left( x - p\right) }^{2} + {q}^{2}}\right\rbrack   + k & \text{ si }\;h = 1 \end{array}.}\right.
\]

- Pour celle du second terme, on commence par effectuer le changement de variable \( t = x - p \) , ce qui ramène le calcul à celui de \( {I}_{h} = \int {\left( {t}^{2} + {q}^{2}\right) }^{-h}{dt} \) . Ensuite, deux techniques sont à notre disposition.

> - For the second term, we begin by performing the change of variable \( t = x - p \) , which reduces the calculation to that of \( {I}_{h} = \int {\left( {t}^{2} + {q}^{2}\right) }^{-h}{dt} \) . Then, two techniques are at our disposal.

- Première technique. On effectue le changement de variable

> - First technique. We perform the change of variable

\[
t = q\tan \theta ,\left( {\theta  \in  \left\rbrack  {\frac{-\pi }{2},\frac{\pi }{2}}\right\lbrack  }\right) \;\text{ de sorte que }\;{dt} = q\left( {1 + {\tan }^{2}\theta }\right) {d\theta },
\]

done

> done

\[
{I}_{h} = \int \frac{dt}{{\left( {t}^{2} + {q}^{2}\right) }^{h}} = \frac{1}{{q}^{{2h} - 1}}\int \frac{d\theta }{{\left( 1 + {\tan }^{2}\theta \right) }^{h - 1}} = \frac{1}{{q}^{{2h} - 1}}\int {\cos }^{{2h} - 2}{\theta d\theta }.
\]

Le calcul de cette dernière primitive est traité dans la section suivante. Après l’avoir calculée, on remplace \( \theta \) par arctan \( \left( {t/q}\right) \) puis \( t \) par \( x - p \) et le tour est joué.

> The calculation of this last antiderivative is covered in the following section. After computing it, we replace \( \theta \) with arctan \( \left( {t/q}\right) \) then \( t \) with \( x - p \) and the job is done.

- Seconde technique. On procède par intégration par parties. Pour tout \( h \in  {\mathbb{N}}^{ * } \) , on écrit

> - Second technique. We proceed by integration by parts. For any \( h \in  {\mathbb{N}}^{ * } \) , we write

\[
{I}_{h} = \frac{t}{{\left( {t}^{2} + {q}^{2}\right) }^{h}} + {2h}\int \frac{{t}^{2}}{{\left( {t}^{2} + {q}^{2}\right) }^{h + 1}} = \frac{t}{{\left( {t}^{2} + {q}^{2}\right) }^{h}} + {2h}{I}_{h} - {2h}{q}^{2}{I}_{h + 1},
\]

ce qui entraîne

> which leads to

\[
{2h}{q}^{2}{I}_{h + 1} = \left( {{2h} - 1}\right) {I}_{h} + \frac{t}{{\left( {t}^{2} + {q}^{2}\right) }^{h}}.
\]

(*)

> Cette dernière relation permet de calculer \( {I}_{h + 1} \) connaissant \( {I}_{h} \) . Le calcul de \( {I}_{1} \) est immédiat car

This last relation allows us to compute \( {I}_{h + 1} \) knowing \( {I}_{h} \) . The calculation of \( {I}_{1} \) is immediate because

\[
\int \frac{dt}{{t}^{2} + {q}^{2}} = \frac{1}{q}\arctan \frac{x}{q}.
\]

Remarquez que pour ramener le calcul de \( {I}_{n} \) à celui de \( {I}_{n - 1} \) , c’est \( {I}_{n - 1} \) qu’il faut intégrer par parties.

> Note that to reduce the calculation of \( {I}_{n} \) to that of \( {I}_{n - 1} \) , it is \( {I}_{n - 1} \) that must be integrated by parts.

Exemple 1. On veut calculer la primitive \( \int \frac{1 - x}{{\left( {x}^{2} + x + 1\right) }^{2}}{dx} \) . On commence par écrire

> Example 1. We want to compute the antiderivative \( \int \frac{1 - x}{{\left( {x}^{2} + x + 1\right) }^{2}}{dx} \) . We begin by writing

\[
\frac{1 - x}{{\left( {x}^{2} + x + 1\right) }^{2}} =  - \frac{1}{2} \cdot  \frac{{2x} + 1}{{\left( {x}^{2} + x + 1\right) }^{2}} + \frac{3}{2} \cdot  \frac{1}{{\left\lbrack  {\left( x + \frac{1}{2}\right) }^{2} + \frac{3}{4}\right\rbrack  }^{2}}.
\]

La primitive du premier terme du membre de droite se calcule de manière immédiate, car

> The antiderivative of the first term on the right-hand side is calculated immediately, because

\[
\int \frac{{2x} + 1}{{\left( {x}^{2} + x + 1\right) }^{2}}{dx} =  - \frac{1}{{x}^{2} + x + 1} + k.
\]

Pour celle du second terme, on utilise la relation (*) qui donne

> For the second term, we use relation (*) which gives

\[
2 \cdot  \frac{3}{4} \cdot  \int \frac{dx}{{\left\lbrack  {\left( x + \frac{1}{2}\right) }^{2} + \frac{3}{4}\right\rbrack  }^{2}} = \int \frac{dx}{{\left( x + \frac{1}{2}\right) }^{2} + \frac{3}{4}} + \frac{x + \frac{1}{2}}{{\left( x + \frac{1}{2}\right) }^{2} + \frac{3}{4}},
\]

d’où

> from which

\[
\int \frac{dx}{{\left\lbrack  {\left( x + \frac{1}{2}\right) }^{2} + \frac{3}{4}\right\rbrack  }^{2}} = \frac{2}{3}\left( {\frac{2}{\sqrt{3}}\arctan \left( \frac{{2x} + 1}{\sqrt{3}}\right)  + \frac{x + \frac{1}{2}}{{x}^{2} + x + 1}}\right) .
\]

(On pourrait aussi procéder en effectuant le changement de variable \( x + \frac{1}{2} = \frac{\sqrt{3}}{2}\tan \theta \) ). Finalement, on a

> (We could also proceed by performing the change of variable \( x + \frac{1}{2} = \frac{\sqrt{3}}{2}\tan \theta \) ). Finally, we have

\[
\int \frac{1 - x}{{\left( {x}^{2} + x + 1\right) }^{2}}{dx} = \frac{x + 1}{{x}^{2} + x + 1} + \frac{2}{\sqrt{3}}\arctan \frac{{2x} + 1}{\sqrt{3}} + k.
\]
