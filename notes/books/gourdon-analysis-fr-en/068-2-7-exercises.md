#### 2.7. Exercises

*Français : 2.7. Exercices*

EXERCICE 1. Calculer les primitives des fonctions suivantes

> EXERCISE 1. Calculate the antiderivatives of the following functions

\[
\text{ a) }\frac{1}{{x}^{4} - {x}^{2} - 2}\;\mathbf{b})\;\frac{x + 1}{{\left( {x}^{2} + 1\right) }^{2}}\;\mathbf{c})\;\frac{{x}^{2}}{{x}^{6} - 1}\;\mathbf{d})\;\frac{1}{x{\left( {x}^{2} + 1\right) }^{2}}\text{ . }
\]

Solution. a) On décompose en éléments simples

> Solution. a) We decompose into partial fractions

\[
\frac{1}{{x}^{4} - {x}^{2} - 2} = \frac{1}{\left( {{x}^{2} - 2}\right) \left( {{x}^{2} + 1}\right) } = \frac{1}{3\left( {{x}^{2} - 2}\right) } - \frac{1}{3\left( {{x}^{2} + 1}\right) },
\]

et on en déduit

> and we deduce

\[
\int \frac{dx}{{x}^{4} - {x}^{2} - 2} = \frac{1}{6\sqrt{2}}\log \left| \frac{x - \sqrt{2}}{x + \sqrt{2}}\right|  - \frac{1}{3}\arctan x + k,\;k \in  \mathbb{R}.
\]

b) On a

> b) We have

\[
\frac{x + 1}{{\left( {x}^{2} + 1\right) }^{2}} = \frac{1}{2} \cdot  \frac{2x}{{\left( {x}^{2} + 1\right) }^{2}} + \frac{1}{{\left( {x}^{2} + 1\right) }^{2}},
\]

donc

> therefore

\[
\int \frac{x + 1}{{\left( {x}^{2} + 1\right) }^{2}}{dx} =  - \frac{1}{2\left( {{x}^{2} + 1}\right) } + \int \frac{dx}{{\left( {x}^{2} + 1\right) }^{2}}.
\]

Pour calculer la primitive du second membre de cette dernière égalité, on fait le changement de variable \( x = \tan \theta , - \pi /2 < \theta < \pi /2 \) . On a \( {dx} = \left( {1 + {\tan }^{2}\theta }\right) {d\theta } \) et

> To calculate the antiderivative of the second term of this last equality, we perform the change of variable \( x = \tan \theta , - \pi /2 < \theta < \pi /2 \). We have \( {dx} = \left( {1 + {\tan }^{2}\theta }\right) {d\theta } \) and

\[
\int \frac{dx}{{\left( {x}^{2} + 1\right) }^{2}} = \int \frac{d\theta }{1 + {\tan }^{2}\theta } = \int {\cos }^{2}{\theta d\theta } = \int \frac{\cos \left( {2\theta }\right)  + 1}{2}{d\theta } = \frac{\sin \left( {2\theta }\right) }{4} + \frac{\theta }{2} + k
\]

\[
= \frac{2x}{4\left( {1 + {x}^{2}}\right) } + \frac{1}{2}\arctan x + k.
\]

Finalement

> Finally

\[
\int \frac{x + 1}{{\left( {x}^{2} + 1\right) }^{2}}{dx} =  - \frac{1}{2\left( {{x}^{2} + 1}\right) } + \frac{x}{2\left( {1 + {x}^{2}}\right) } + \frac{1}{2}\arctan x + k,\;k \in  \mathbb{R}.
\]

c) Il y a une petite astuce de calcul. On pose \( t = {x}^{3} \) , de sorte que \( {dt} = 3{x}^{2}{dx} \) et

> c) There is a small calculation trick. We set \( t = {x}^{3} \), so that \( {dt} = 3{x}^{2}{dx} \) and

\[
\int \frac{{x}^{2}}{{x}^{6} - 1}{dx} = \frac{1}{3}\int \frac{dt}{{t}^{2} - 1} = \frac{1}{6}\log \left| \frac{t - 1}{t + 1}\right|  = \frac{1}{6}\log \left| \frac{{x}^{3} - 1}{{x}^{3} + 1}\right| .
\]

d) La décomposition en éléments simples de la fraction rationnelle considérée est

> d) The partial fraction decomposition of the rational function considered is

\[
\frac{1}{x{\left( {x}^{2} + 1\right) }^{2}} = \frac{1}{x} - \frac{x}{{x}^{2} + 1} - \frac{x}{{\left( {x}^{2} + 1\right) }^{2}}
\]

donc

> therefore

\[
\int \frac{dx}{x{\left( {x}^{2} + 1\right) }^{2}} = \log \left| x\right|  - \frac{1}{2}\log \left( {{x}^{2} + 1}\right)  + \frac{1}{2} \cdot  \frac{1}{1 + {x}^{2}} + k,\;k \in  \mathbb{R}.
\]

EXERCICE 2. Calculer les primitives des fonctions suivantes

> EXERCISE 2. Calculate the antiderivatives of the following functions

\[
\text{ a) }\frac{\cos x}{{\sin }^{2}x + 2{\tan }^{2}x}
\]

\[
\text{ b) }\frac{\sin x}{{\cos }^{3}x + {\sin }^{3}x}
\]

\[
\text{ c) }\frac{1}{\sin x + \cos x + 2}
\]

\[
\text{ d) }\frac{1}{\operatorname{ch}x\sqrt{\operatorname{ch}{2x}}}\text{ . }
\]

Solution. a) Il y a invariance de l’expression intégrée par le changement de variable \( x \rightarrow \pi - x \) . La règle de Bioche nous invite à effectuer le changement de variable \( t = \sin x \) . On a

> Solution. a) The integrand is invariant under the change of variable \( x \rightarrow \pi - x \) . Bioche's rule suggests we perform the change of variable \( t = \sin x \) . We have

\[
\frac{\cos x}{{\sin }^{2}x + 2{\tan }^{2}x}{dx} = \frac{\cos {xdx}}{{\sin }^{2}x + 2\frac{{\sin }^{2}x}{1 - {\sin }^{2}x}} = \frac{dt}{{t}^{2} + 2\frac{{t}^{2}}{1 - {t}^{2}}} = \frac{\left( {1 - {t}^{2}}\right) {dt}}{3{t}^{2} - {t}^{4}}.
\]

De plus

> Furthermore

\[
\frac{X - 1}{X\left( {X - 3}\right) } = \frac{1}{3X} + \frac{2}{3\left( {X - 3}\right) }\;\text{ donc }\;\frac{{t}^{2} - 1}{{t}^{2}\left( {{t}^{2} - 3}\right) } = \frac{1}{3{t}^{2}} + \frac{2}{3\left( {{t}^{2} - 3}\right) },
\]

d’où

> whence

\[
\int \frac{\left( {1 - {t}^{2}}\right) {dt}}{3{t}^{2} - {t}^{4}} =  - \frac{1}{3t} + \frac{1}{6\sqrt{3}}\log \left| \frac{t - \sqrt{3}}{t + \sqrt{3}}\right|
\]

et finalement

> and finally

\[
\int \frac{\cos x}{{\sin }^{2}x + 2{\tan }^{2}x} =  - \frac{1}{3\sin x} + \frac{1}{6\sqrt{3}}\log \left| \frac{\sin x - \sqrt{3}}{\sin x + \sqrt{3}}\right| .
\]

b) L’expression intégrée est invariante par le changement de variable \( x \rightarrow x + \pi \) . La règle de Bioche nous invite à faire le changement de variable \( t = \tan x \) . On a alors \( {dt} = {dx}/\left( {{\cos }^{2}x}\right) \) et

> b) The integrand is invariant under the change of variable \( x \rightarrow x + \pi \) . Bioche's rule suggests we perform the change of variable \( t = \tan x \) . We then have \( {dt} = {dx}/\left( {{\cos }^{2}x}\right) \) and

\[
\frac{\sin {xdx}}{{\cos }^{3}x + {\sin }^{3}x} = \frac{\tan x}{1 + {\tan }^{3}x}\frac{dx}{{\cos }^{2}x} = \frac{t}{1 + {t}^{3}}{dt}.
\]

Maintenant, la décomposition en éléments simples

> Now, the partial fraction decomposition

\[
\frac{t}{1 + {t}^{3}} = \frac{t}{\left( {1 + t}\right) \left( {1 - t + {t}^{2}}\right) } =  - \frac{1}{3\left( {t + 1}\right) } + \frac{t + 1}{3\left( {{t}^{2} - t + 1}\right) }
\]

entraîne

> leads to

\[
\int \frac{t}{1 + {t}^{3}}{dt} = \int \left( {-\frac{1}{3\left( {t + 1}\right) } + \frac{1}{6}\frac{{2t} - 1}{{t}^{2} - t + 1} + \frac{1}{2} \cdot  \frac{1}{{\left( t - \frac{1}{2}\right) }^{2} + \frac{3}{4}}}\right) {dt}
\]

\[
=  - \frac{1}{3}\log \left| {1 + t}\right|  + \frac{1}{6} \cdot  \log \left( {{t}^{2} - t + 1}\right)  + \frac{1}{2} \cdot  \frac{2}{\sqrt{3}} \cdot  \arctan \left( {\frac{2}{\sqrt{3}} \cdot  \left( {t - \frac{1}{2}}\right) }\right)
\]

donc

> therefore

\[
\int \frac{\sin x}{{\cos }^{3}x + {\sin }^{3}x}{dx} =  - \frac{1}{3}\log \left| {1 + \tan x}\right|  + \frac{1}{6}\log \left( {\tan {x}^{2} - \tan x + 1}\right)  + \frac{1}{\sqrt{3}} \cdot  \arctan \left( \frac{2\tan x - 1}{\sqrt{3}}\right)
\]

c) On commence par écrire \( \sin x + \cos x = \sqrt{2}\sin \left( {x + \pi /4}\right) \) , puis on fait le changement de variable \( t = x + \pi /4 \) . On se ramène ainsi à évaluer la primitive

> c) We start by writing \( \sin x + \cos x = \sqrt{2}\sin \left( {x + \pi /4}\right) \) , then we perform the change of variable \( t = x + \pi /4 \) . We are thus reduced to evaluating the antiderivative

\[
\int \frac{dt}{\sqrt{2}\sin t + 2} = \frac{1}{\sqrt{2}}\int \frac{dt}{\sin t + \sqrt{2}}.
\]

Pour évaluer cette dernière primitive, on effectue le changement de variable \( u = \tan \left( {t/2}\right) \) de sorte que \( {dt} = {2du}/\left( {1 + {u}^{2}}\right) \) et

> To evaluate this last antiderivative, we perform the change of variable \( u = \tan \left( {t/2}\right) \) such that \( {dt} = {2du}/\left( {1 + {u}^{2}}\right) \) and

\[
\frac{1}{\sqrt{2}}\int \frac{dt}{\sin t + \sqrt{2}} = \int \frac{du}{{u}^{2} + \sqrt{2}u + 1} = \int \frac{du}{{\left( u + \frac{\sqrt{2}}{2}\right) }^{2} + \frac{1}{2}} = \sqrt{2}\arctan \left( {\sqrt{2}u + 1}\right)  + k.
\]

Finalement, on a

> Finally, we have

\[
\int \frac{dx}{\sin x + \cos x + 2} = \sqrt{2}\arctan \left( {\sqrt{2}\tan \left( {\frac{x}{2} + \frac{\pi }{8}}\right)  + 1}\right)  + k,\;k \in  \mathbb{R}.
\]

d) \( \mathrm{{On}} \) a

> d) \( \mathrm{{On}} \) has

\[
\operatorname{ch}{2x} = {\operatorname{ch}}^{2}x + {\operatorname{sh}}^{2}x = {\operatorname{ch}}^{2}x\left( {1 + {\operatorname{th}}^{2}x}\right) \;\text{ donc }\;\frac{1}{\operatorname{ch}x\sqrt{\operatorname{ch}{2x}}} = \frac{1}{{\operatorname{ch}}^{2}x\sqrt{1 + {\operatorname{th}}^{2}x}}.
\]

On fait donc le changement de variable \( t = \operatorname{th}x \) . On a \( {dt} = {dx}/{\operatorname{ch}}^{2}x \) et

> We therefore perform the change of variable \( t = \operatorname{th}x \) . We have \( {dt} = {dx}/{\operatorname{ch}}^{2}x \) and

\[
\int \frac{dx}{\operatorname{ch}x\sqrt{\operatorname{ch}{2x}}} = \int \frac{dt}{\sqrt{1 + {t}^{2}}} = \log \left( {t + \sqrt{{t}^{2} + 1}}\right)  + k,
\]

donc

> therefore

\[
\int \frac{dx}{\operatorname{ch}x\sqrt{\operatorname{ch}{2x}}} = \log \left( {\operatorname{th}x + \sqrt{1 + {\operatorname{th}}^{2}x}}\right)  + k,\;k \in  \mathbb{R}.
\]

EXERCICE 3. Calculer les primitives des fonctions suivantes

> EXERCISE 3. Calculate the antiderivatives of the following functions

\[
\text{ a) }x\sqrt{\frac{x - 2}{x + 1}}\;\text{ b) }\frac{1}{\left( {x + 1}\right) \sqrt{{x}^{2} + x + 1}}\;\text{ c) }\sqrt{-{x}^{2} + {4x} + {10}}
\]

\[
\text{ d) }\frac{1}{x + \sqrt{{x}^{2} + {2x}}}\;\text{ e) }\;\frac{1}{\sqrt[3]{1 + {x}^{3}}}\text{ . }
\]

Solution. Il y a en général plusieurs moyens de calculer les primitives de chaque fonction présentée. Nous nous limiterons à un seul type de résolution.

> Solution. There are generally several ways to calculate the antiderivatives of each function presented. We will limit ourselves to one type of solution.

a) On fait le changement de variable

> a) We perform the change of variable

\[
t = \sqrt{\frac{x - 2}{x + 1}}\text{ ou encore }x = \frac{2 + {t}^{2}}{1 - {t}^{2}};\;\text{ on a alors }{dx} = \frac{6t}{{\left( 1 - {t}^{2}\right) }^{2}}{dt}
\]

et

\[
\int x\sqrt{\frac{x - 2}{x + 1}}{dx} = \int \frac{2 + {t}^{2}}{1 - {t}^{2}} \cdot  t \cdot  \frac{6t}{{\left( 1 - {t}^{2}\right) }^{2}}{dt} = \int \frac{6{t}^{2}\left( {2 + {t}^{2}}\right) }{{\left( 1 - {t}^{2}\right) }^{3}}{dt}.
\]

De la décomposition en éléments simples

> From the partial fraction decomposition

\[
\frac{6{t}^{2}\left( {2 + {t}^{2}}\right) }{{\left( 1 - {t}^{2}\right) }^{3}} = \frac{1}{8}\left( {\frac{3}{t + 1} - \frac{3}{t - 1} - \frac{21}{{\left( t + 1\right) }^{2}} - \frac{21}{{\left( t - 1\right) }^{2}} + \frac{18}{{\left( t + 1\right) }^{3}} - \frac{18}{{\left( t - 1\right) }^{3}}}\right) ,
\]

on déduit

> we deduce

\[
\int \frac{6{t}^{2}\left( {2 + {t}^{2}}\right) }{{\left( 1 - {t}^{2}\right) }^{3}}{dt} = \frac{1}{8}\left( {3\log \left| {t + 1}\right|  - 3\log \left| {t - 1}\right|  + \frac{21}{t + 1} + \frac{21}{t - 1} - \frac{9}{{\left( t + 1\right) }^{2}} + \frac{9}{{\left( t - 1\right) }^{2}}}\right)  + k
\]

Pour obtenir les primitives de la fonction proposée, il suffit ensuite de remplacer \( t \) par \( \sqrt{\frac{x - 2}{x + 1}} \) . Si on simplifie au mieux l'expression, on parvient finalement à

> To obtain the antiderivatives of the proposed function, it then suffices to replace \( t \) with \( \sqrt{\frac{x - 2}{x + 1}} \) . If we simplify the expression as much as possible, we finally arrive at

\[
\int x\sqrt{\frac{x - 2}{x + 1}}{dx} = \left( \frac{{2x} - 5}{4}\right) \sqrt{{x}^{2} - x - 2} + \frac{3}{8}\log \left( {2\sqrt{{x}^{2} - x - 2} + {2x} - 1}\right)  + k,\;k \in  \mathbb{R}.
\]

b) Il faut utiliser l'une des astuces décrites à la page 141 : on fait le changement de variable \( t = 1/\left( {x + 1}\right) \) . Après calculs, on est ramené à la primitive

> b) One must use one of the tricks described on page 141: we perform the change of variable \( t = 1/\left( {x + 1}\right) \) . After calculations, we are reduced to the antiderivative

\[
\varepsilon \int \frac{dt}{\sqrt{{t}^{2} - t + 1}} =  - \varepsilon \log \left| {t - \frac{1}{2} + \sqrt{{t}^{2} - t + 1}}\right|  + k,\;k \in  \mathbb{R}
\]

où \( \varepsilon \in \{ - 1,1\} \) a le signe de \( t \) . On en déduit le résultat en remplaçant \( t \) par \( 1/\left( {x + 1}\right) \) .

> where \( \varepsilon \in \{ - 1,1\} \) has the sign of \( t \) . We deduce the result by replacing \( t \) with \( 1/\left( {x + 1}\right) \) .

c) On résout le problème en intégrant par parties. On a

> c) We solve the problem by integrating by parts. We have

\[
\int \sqrt{-{x}^{2} + {4x} + {10}}{dx} = x\sqrt{-{x}^{2} + {4x} + {10}} + \int \frac{{x}^{2} - {2x}}{\sqrt{-{x}^{2} + {4x} + {10}}}{dx}.
\]

Or

\[
\int \frac{{x}^{2} - {2x}}{\sqrt{-{x}^{2} + {4x} + {10}}}{dx} =  - \int \frac{-{x}^{2} + {4x} + {10}}{\sqrt{-{x}^{2} + {4x} + {10}}}{dx} + \int \frac{{2x} + {10}}{\sqrt{-{x}^{2} + {4x} + {10}}}{dx}
\]

\[
=  - \int \sqrt{-{x}^{2} + {4x} + {10}}{dx} + \int \frac{{2x} + {10}}{\sqrt{-{x}^{2} + {4x} + {12}}}{dx}
\]

donc

> therefore

\[
2\int \sqrt{-{x}^{2} + {4x} + {10}}{dx} = x\sqrt{-{x}^{2} + {4x} + {10}} - \int \frac{-{2x} + 4}{\sqrt{-{x}^{2} + {4x} + {10}}}{dx} + {14}\int \frac{dx}{\sqrt{-{x}^{2} + {4x} + {10}}}
\]

\[
= x\sqrt{-{x}^{2} + {4x} + {12}} - 2\sqrt{-{x}^{2} + {4x} + {10}} + {14}\arcsin \left( \frac{x - 2}{\sqrt{14}}\right)  + k,\;k \in  \mathbb{R}.
\]

d) On pose \( \sqrt{{x}^{2} + {2x}} = - x + t \) , de sorte que

> d) We set \( \sqrt{{x}^{2} + {2x}} = - x + t \) , so that

\[
x = \frac{{t}^{2}}{2\left( {t + 1}\right) }\;\text{ et }\;{dx} = \frac{{t}^{2} + {2t}}{2{\left( t + 1\right) }^{2}}{dt}.
\]

On se ramène ainsi à

> We are thus reduced to

\[
\frac{1}{2}\int \frac{t + 2}{{\left( t + 1\right) }^{2}}{dt} = \frac{1}{2}\int \frac{dt}{t + 1} + \frac{1}{2}\int \frac{dt}{{\left( t + 1\right) }^{2}} = \frac{1}{2}\log \left| {t + 1}\right|  - \frac{1}{2\left( {t + 1}\right) } + k
\]

\[
= \frac{1}{2}\log \left| {1 + x + \sqrt{{x}^{2} + {2x}}}\right|  - \frac{1}{2\left( {1 + x + \sqrt{{x}^{2} + {2x}}}\right) } + k,\;k \in  \mathbb{I}
\]

e) On fait d’abord le changement de variable \( t = 1/x \) , ce qui ramène le calcul à celui de

> e) We first perform the change of variable \( t = 1/x \) , which reduces the calculation to that of

\[
- \int \frac{dt}{t\sqrt[3]{1 + {t}^{3}}} =  - \int \frac{{t}^{2}{dt}}{{t}^{3}\sqrt[3]{1 + {t}^{3}}},
\]

puis on pose \( u = {t}^{3} \) , nous ramenant à

> then we set \( u = {t}^{3} \) , reducing us to

\[
- \frac{1}{3}\int \frac{du}{u\sqrt[3]{1 + u}}
\]

On pose ensuite \( v = \sqrt[3]{1 + u} \) , ce qui donne

> We then set \( v = \sqrt[3]{1 + u} \) , which gives

\[
- \int \frac{v}{{v}^{3} - 1}{dv}
\]

On décompose la dernière intégrande en éléments simples

> We decompose the last integrand into partial fractions

\[
\frac{v}{{v}^{3} - 1} = \frac{1}{3}\left( {\frac{1}{v - 1} - \frac{v - 1}{{v}^{2} + v + 1}}\right)
\]

et après un calcul classique, on trouve

> and after a standard calculation, we find

\[
- \int \frac{v}{{v}^{3} - 1}{dv} =  - \frac{1}{3}\log \left( {v - 1}\right)  + \frac{1}{6}\log \left( {{v}^{2} + v + 1}\right)  - \frac{1}{\sqrt{3}}\arctan \left( \frac{{2v} + 1}{\sqrt{3}}\right)  + k,\;k \in  \mathbb{R}
\]

Il reste alors à remplacer \( v \) par \( \sqrt[3]{1 + \frac{1}{{x}^{3}}} \) et c’est terminé.

> It then remains to replace \( v \) with \( \sqrt[3]{1 + \frac{1}{{x}^{3}}} \) and it is finished.

EXERCICE 4. Calculer l'intégrale

> EXERCISE 4. Calculate the integral

\[
I = {\int }_{\pi /2}^{{3\pi }/2}\frac{dx}{3 + \sin x}.
\]

Solution. On commence par rechercher une primitive de la fonction \( x \mapsto 1/\left( {3 + \sin x}\right) \) . Pour cela, posons

> Solution. We begin by finding an antiderivative of the function \( x \mapsto 1/\left( {3 + \sin x}\right) \). To do this, let us set

\[
t = \tan \frac{x}{2},\;x \in  \left\lbrack  {\frac{\pi }{2},\pi \left\lbrack  {\text{ ou }x \in  }\right\rbrack  \pi ,\frac{3\pi }{2}}\right\rbrack  ,\;\text{ desorte que }{dx} = \frac{2dt}{1 + {t}^{2}}.
\]

On trouve, après calculs,

> After calculation, we find

\[
\int \frac{dx}{3 + \sin x} = \int \frac{2dt}{3{t}^{2} + {2t} + 3} = \frac{1}{\sqrt{2}}\arctan \left( \frac{{3t} + 1}{2\sqrt{2}}\right)  = \frac{1}{\sqrt{2}}\arctan \left( \frac{3\tan \left( {x/2}\right)  + 1}{2\sqrt{2}}\right) .
\]

La fonction \( F : x \mapsto \frac{1}{\sqrt{2}}\arctan \left( \frac{3\tan \left( {x/2}\right) + 1}{2\sqrt{2}}\right) \) est donc une primitive de \( x \mapsto 1/\left( {3 + \sin x}\right) \) , mais seulement sur chacun des intervalles \( \left\lbrack {\pi /2,\pi \left\lbrack \text{ et }\right\rbrack \pi ,{3\pi }/2}\right\rbrack \) . Il faut donc se garder décrire \( I = F\left( {{3\pi }/3}\right) - F\left( {\pi /2}\right) \) , ce qui n’aurait aucun sens. On va résoudre le problème en écrivant

> The function \( F : x \mapsto \frac{1}{\sqrt{2}}\arctan \left( \frac{3\tan \left( {x/2}\right) + 1}{2\sqrt{2}}\right) \) is therefore an antiderivative of \( x \mapsto 1/\left( {3 + \sin x}\right) \), but only on each of the intervals \( \left\lbrack {\pi /2,\pi \left\lbrack \text{ et }\right\rbrack \pi ,{3\pi }/2}\right\rbrack \). One must therefore avoid writing \( I = F\left( {{3\pi }/3}\right) - F\left( {\pi /2}\right) \), which would make no sense. We will solve the problem by writing

\[
I = {\int }_{\pi /2}^{\pi }\frac{dx}{3 + \sin x} + {\int }_{\pi }^{{3\pi }/2}\frac{dx}{3 + \sin x}.
\]

On a

> We have

\[
{\int }_{\pi /2}^{\pi }\frac{dx}{3 + \sin x} = \mathop{\lim }\limits_{\substack{{X \rightarrow  \pi } \\  {X < \pi } }}{\int }_{\pi /2}^{X}\frac{dx}{3 + \sin x} = \mathop{\lim }\limits_{\substack{{X \rightarrow  \pi } \\  {X < \pi } }}F\left( X\right)  - F\left( \frac{\pi }{2}\right)  = \frac{\pi }{2\sqrt{2}} - \frac{\arctan \sqrt{2}}{\sqrt{2}},
\]

de même

> similarly

\[
{\int }_{\pi }^{{3\pi }/2}\frac{dx}{3 + \sin x} = \mathop{\lim }\limits_{\substack{{X \rightarrow  \pi } \\  {X > \pi } }}{\int }_{X}^{{3\pi }/2}\frac{dx}{3 + \sin x} = \mathop{\lim }\limits_{\substack{{X \rightarrow  \pi } \\  {X > \pi } }}F\left( \frac{3\pi }{2}\right)  - F\left( X\right)  =  - \frac{\arctan \left( {1/\sqrt{2}}\right) }{\sqrt{2}} + \frac{\pi }{2\sqrt{2}}.
\]

Compte tenu de la classique relation arctan \( x + \arctan \left( {1/x}\right) = \pi /2 \) pour \( x > 0 \) , on en déduit

> Given the classic relation arctan \( x + \arctan \left( {1/x}\right) = \pi /2 \) for \( x > 0 \), we deduce

\[
I = \frac{\pi }{\sqrt{2}} - \frac{\arctan \sqrt{2} + \arctan \left( {1/\sqrt{2}}\right) }{\sqrt{2}} = \frac{\pi }{\sqrt{2}} - \frac{\pi }{2\sqrt{2}} = \frac{\pi }{2\sqrt{2}}.
\]

EXERCICE 5. Donner une relation de récurrence permettant de calculer les intégrales suivantes :

> EXERCISE 5. Provide a recurrence relation to calculate the following integrals:

\[
\text{ a) }{I}_{n} = {\int }_{0}^{\pi /4}{\tan }^{n}{xdx},\;\mathbf{b})\;{I}_{n} = {\int }_{0}^{\pi /4}\frac{dx}{{\cos }^{n}x},\;\mathbf{c})\;{I}_{n} = {\int }_{1}^{e}{\log }^{n}{xdx}\text{ . }
\]

Solution. a) Il suffit de remarquer que

> Solution. a) It suffices to note that

\[
\forall n \in  \mathbb{N},\;{I}_{n} + {I}_{n + 2} = {\int }_{0}^{\pi /4}{\tan }^{n}x\left( {1 + {\tan }^{2}x}\right) {dx} = {\left\lbrack  \frac{{\tan }^{n + 1}x}{n + 1}\right\rbrack  }_{0}^{\pi /4} = \frac{1}{n + 1}.
\]

Cette relation permet de calculer \( {I}_{n} \) sachant que

> This relation allows for the calculation of \( {I}_{n} \) knowing that

\[
{I}_{0} = \frac{\pi }{4}\;\text{ et }\;{I}_{1} = {\left\lbrack  -\log \left( \cos x\right) \right\rbrack  }_{0}^{\pi /4} = \frac{\log 2}{2}.
\]

b) Pour tout \( n \in \mathbb{N} \) , on a, en intégrant par parties

> b) For all \( n \in \mathbb{N} \), we have, by integrating by parts

\[
{I}_{n + 2} = {\int }_{0}^{\pi /4}\frac{1}{{\cos }^{n}x}\frac{dx}{{\cos }^{2}x} = {\left\lbrack  \frac{1}{{\cos }^{n}x}\tan x\right\rbrack  }_{0}^{\pi /4} - n{\int }_{0}^{\pi /4}\frac{\sin x}{{\cos }^{n + 1}x}\tan {xdx}
\]

\[
= {\left( \sqrt{2}\right) }^{n} - n{\int }_{0}^{\pi /4}\frac{{\sin }^{2}x}{{\cos }^{n + 2}x}{dx} = {\left( \sqrt{2}\right) }^{n} - n\left( {{I}_{n + 2} - {I}_{n}}\right)
\]

donc

> therefore

\[
\left( {n + 1}\right) {I}_{n + 2} = {\left( \sqrt{2}\right) }^{n} + n{I}_{n}\;\text{ ou encore }\;{I}_{n + 2} = \frac{{\left( \sqrt{2}\right) }^{n}}{n + 1} + \frac{n}{n + 1}{I}_{n},
\]

d’où un moyen de calculer chaque \( {I}_{n} \) , sachant que

> hence a way to calculate each \( {I}_{n} \), knowing that

\[
{I}_{0} = \frac{\pi }{4}\;\text{ et }\;{I}_{1} = {\left\lbrack  \log \left( \tan \left( \frac{x}{2} + \frac{\pi }{4}\right) \right) \right\rbrack  }_{0}^{\pi /4} = \log \left( {\tan \frac{3\pi }{8}}\right) .
\]

c) En intégrant par parties, on a

> c) By integrating by parts, we have

\[
\forall n \in  {\mathbb{N}}^{ * },\;{I}_{n} = {\left\lbrack  x{\log }^{n}x\right\rbrack  }_{1}^{e} - n{\int }_{1}^{e}{\log }^{n - 1}{xdx} = e - n{I}_{n - 1}.
\]

Cette relation de récurrence permet de calculer chaque terme \( {I}_{n} \) , sachant que \( {I}_{0} = e - 1 \) .

> This recurrence relation allows for the calculation of each term \( {I}_{n} \), knowing that \( {I}_{0} = e - 1 \).
