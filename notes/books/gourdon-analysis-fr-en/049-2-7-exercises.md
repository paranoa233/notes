#### 2.7. Exercises

*Français : 2.7. Exercices*

EXERCICE 1. Donner le développement limité au voisinage de 0 à l'ordre 4 des fonctions suivantes

> EXERCISE 1. Provide the Taylor expansion at order 4 near 0 for the following functions

\[
\text{ a) }x \mapsto  {\left( 1 + \sqrt{1 + {x}^{2}}\right) }^{1/2}
\]

b) \( x \mapsto \log \left( \frac{\sin x}{x}\right) \)

\[
\text{ c) }x \mapsto  {\left( 1 + 2x\right) }^{1/\left( {1 + x}\right) }\;\text{ d) }\;x \mapsto  \frac{1}{{\sin }^{2}x} - \frac{1}{{\sinh }^{2}x}
\]

\[
\text{ e) }\;x \mapsto  {e}^{\sinh x} - \log \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{4}}\right) }\right| \text{ . }
\]

Solution. a) Le développement limité \( \sqrt{1 + u} = 1 + \frac{u}{2} - \frac{{u}^{2}}{8} + o\left( {u}^{2}\right) \) entraîne

> Solution. a) The Taylor expansion \( \sqrt{1 + u} = 1 + \frac{u}{2} - \frac{{u}^{2}}{8} + o\left( {u}^{2}\right) \) leads to

\[
{\left( 1 + \sqrt{1 + {x}^{2}}\right) }^{1/2} = {\left\lbrack  1 + \left( 1 + \frac{{x}^{2}}{2} - \frac{{x}^{4}}{8} + o\left( {x}^{4}\right) \right) \right\rbrack  }^{1/2} = \sqrt{2}{\left\lbrack  1 + \frac{{x}^{2}}{4} - \frac{{x}^{4}}{16} + o\left( {x}^{4}\right) \right\rbrack  }^{1/2},
\]

ce qui, par composition des développements limités est égal à

> which, by composition of Taylor expansions, is equal to

\[
\sqrt{2}\left\lbrack  {1 + \frac{1}{2}\left( {\frac{{x}^{2}}{4} - \frac{{x}^{4}}{16}}\right)  - \frac{1}{8}{\left( \frac{{x}^{2}}{4}\right) }^{2} + o\left( {x}^{4}\right) }\right\rbrack   = \sqrt{2}\left\lbrack  {1 + \frac{1}{8}{x}^{2} - \frac{5}{158}{x}^{4} + o\left( {x}^{4}\right) }\right\rbrack  .
\]

b)

\[
\log \left( \frac{\sin x}{x}\right)  = \log \left( {1 - \frac{{x}^{2}}{6} + \frac{{x}^{4}}{120} + o\left( {x}^{4}\right) }\right)  = \left( {-\frac{{x}^{2}}{6} + \frac{{x}^{4}}{120}}\right)  - \frac{1}{2}{\left( \frac{{x}^{2}}{6}\right) }^{2} + o\left( {x}^{4}\right)
\]

\[
=  - \frac{{x}^{2}}{6} - \frac{{x}^{4}}{180} + o\left( {x}^{4}\right) .
\]

c) En procédant de même, on trouve

> c) Proceeding in the same way, we find

\[
{\left( 1 + 2x\right) }^{1/\left( {1 + x}\right) } = \exp \left( \frac{\log \left( {1 + {2x}}\right) }{1 + x}\right)  = 1 + {2x} - 2{x}^{2} + \frac{10}{3}{x}^{4} + o\left( {x}^{4}\right) .
\]

d) Cette fois, on commence par développer \( \sin x \) et \( \sinh x \) à l’ordre 7, ce qui entraîne

> d) This time, we start by expanding \( \sin x \) and \( \sinh x \) to order 7, which leads to

\[
\frac{1}{{\sin }^{2}x} - \frac{1}{{\sinh }^{2}x} = \frac{1}{{x}^{2}}\left\lbrack  {{\left( 1 - \frac{{x}^{2}}{6} + \frac{{x}^{4}}{120} - \frac{{x}^{6}}{7!} + o\left( {x}^{6}\right) \right) }^{-2} - {\left( 1 + \frac{{x}^{2}}{6} + \frac{{x}^{4}}{120} + \frac{{x}^{6}}{7!} + o\left( {x}^{6}\right) \right) }^{-2}}\right\rbrack  .
\]

En utilisant le développement limité \( {\left( 1 + u\right) }^{-2} = 1 - {2u} + 3{u}^{2} - 4{u}^{3} + 5{u}^{4} + o\left( {u}^{4}\right) \) on trouve, après calculs

> Using the Taylor expansion \( {\left( 1 + u\right) }^{-2} = 1 - {2u} + 3{u}^{2} - 4{u}^{3} + 5{u}^{4} + o\left( {u}^{4}\right) \) we find, after calculations

\[
\frac{1}{{\sin }^{2}x} - \frac{1}{{\sinh }^{2}x} = \frac{2}{3} + \frac{4}{189}{x}^{4} + o\left( {x}^{4}\right) .
\]

e) On commence par calculer le développement de \( \varphi \left( x\right) = \log \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{4}}\right) }\right| \) . Le moyen le plus simple est certainement de remarquer que

> e) We start by calculating the expansion of \( \varphi \left( x\right) = \log \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{4}}\right) }\right| \) . The simplest way is certainly to note that

\[
{\varphi }^{\prime }\left( x\right)  = \frac{1}{\cos x} = \frac{1}{1 - \frac{{x}^{2}}{2} + o\left( {x}^{3}\right) } = 1 + \frac{{x}^{2}}{2} + o\left( {x}^{3}\right)
\]

puis d'intégrer ce développement limité, ce qui donne

> then integrating this Taylor expansion, which gives

\[
\varphi \left( x\right)  = \varphi \left( 0\right)  + x + \frac{{x}^{3}}{6} + o\left( {x}^{4}\right)  = x + \frac{{x}^{3}}{6} + o\left( {x}^{4}\right) .
\]

Maintenant, après calculs

> Now, after calculations

\[
{e}^{\sinh x} = 1 + x + \frac{{x}^{2}}{2} + \frac{{x}^{3}}{3} + \frac{5}{24}{x}^{4} + o\left( {x}^{4}\right) ,
\]

et finalement

> and finally

\[
{e}^{\sinh x} - \log \left| {\tan \left( {\frac{x}{2} + \frac{\pi }{4}}\right) }\right|  = 1 + \frac{{x}^{2}}{2} + \frac{{x}^{3}}{6} + \frac{5}{24}{x}^{4} + o\left( {x}^{4}\right) .
\]

EXERCICE 2. Calculer le développement limité

> EXERCISE 2. Calculate the Taylor expansion

a) à l’ordre 4, au voisinage de 1, de l’application \( x \mapsto {x}^{\frac{1}{-1 + \log x}} \) ,

> a) at order 4, near 1, of the mapping \( x \mapsto {x}^{\frac{1}{-1 + \log x}} \) ,

b) à l’ordre 4, au voisinage de \( + \infty \) , de l’application \( x \mapsto {\left( {x}^{3} + x\right) }^{1/3} - {\left( {x}^{3} - x\right) }^{1/3} \) ,

> b) at order 4, near \( + \infty \) , of the mapping \( x \mapsto {\left( {x}^{3} + x\right) }^{1/3} - {\left( {x}^{3} - x\right) }^{1/3} \) ,

c) à l’ordre 3, au voisinage de \( \pi /6 \) , de \( x \mapsto \log \left( {2\sin x}\right) \) .

> c) at order 3, near \( \pi /6 \) , of \( x \mapsto \log \left( {2\sin x}\right) \) .

Solution. a) Posons \( t = x - 1 \) . La relation

> Solution. a) Let \( t = x - 1 \) . The relation

\[
{x}^{\frac{1}{-1 + \log x}} = \exp \left( \frac{\log \left( {1 + t}\right) }{-1 + \log \left( {1 + t}\right) }\right)  = \exp \left( {1 + \frac{1}{-1 + \log \left( {1 + t}\right) }}\right) ,
\]

permet,à partir du développement limité de \( \log \left( {1 + t}\right) \) et par composition de développements limités, de montrer

> allows, from the Taylor expansion of \( \log \left( {1 + t}\right) \) and by composition of Taylor expansions, to show

\[
{x}^{\frac{1}{-1 + \log x}} = 1 - \left( {x - 1}\right)  + \frac{{\left( x - 1\right) }^{4}}{12} + o\left\lbrack  {\left( x - 1\right) }^{4}\right\rbrack  .
\]

b) On écrit

> b) We write

\[
{\left( {x}^{3} + x\right) }^{1/3} - {\left( {x}^{3} - x\right) }^{1/3} = x\left\lbrack  {{\left( 1 + \frac{1}{{x}^{2}}\right) }^{1/3} - {\left( 1 - \frac{1}{{x}^{2}}\right) }^{1/3}}\right\rbrack  ,
\]

et le développement limité de \( {\left( 1 \pm {x}^{-2}\right) }^{1/3} \) en \( 1/x \) donne, après calculs

> and the Taylor expansion of \( {\left( 1 \pm {x}^{-2}\right) }^{1/3} \) at \( 1/x \) gives, after calculations

\[
{\left( {x}^{3} + x\right) }^{1/3} - {\left( {x}^{3} - x\right) }^{1/3} = \frac{2}{3}\frac{1}{x} + o\left( \frac{1}{{x}^{4}}\right) .
\]

c) On commence par écrire

> c) We start by writing

\[
\sin \left( {\frac{\pi }{6} + t}\right)  = \sin \frac{\pi }{6}\cos t + \sin t\cos \frac{\pi }{6} = \frac{1}{2}\sin t + \frac{\sqrt{3}}{2}\cos t,
\]

puis on calcule le développement limité de \( \sin t \) et \( \cos t \) en \( t = 0 \) , et après composition de développements limités, on trouve

> then we calculate the Taylor expansion of \( \sin t \) and \( \cos t \) at \( t = 0 \) , and after composition of Taylor expansions, we find

\[
\log \left( {2\sin x}\right)  = \sqrt{3}\left( {x - \frac{\pi }{6}}\right)  - 2{\left( x - \frac{\pi }{6}\right) }^{2} - \frac{\sqrt{3}}{3}{\left( x - \frac{\pi }{6}\right) }^{3} + o\left\lbrack  {\left( x - \frac{\pi }{6}\right) }^{3}\right\rbrack  .
\]

EXERCICE 3. Donner la limite, lorsque \( x \) tend vers \( {0}^{ + } \) , des expressions suivantes

> EXERCISE 3. Give the limit, as \( x \) tends to \( {0}^{ + } \) , of the following expressions

\[
\text{ a) }\frac{{e}^{\sin x} - {e}^{\tan x}}{\sin x - \tan x}\;\mathbf{b})\;\frac{{x}^{{x}^{x}}\log x}{{x}^{x} - 1}
\]

\[
\text{ c) }\frac{{\left( 1 + x\right) }^{\log x/x} - x}{x\left( {{x}^{x} - 1}\right) }
\]

\[
\text{ e) }\frac{\arccos \left( {1 - x}\right) }{\sqrt{x}}\text{ . }
\]

Solution. Tout le problème, dans ce type d'exercices, est de sentir à l'avance jusqu'à quel ordre on va devoir développer pour obtenir le résultat.

> Solution. The whole problem, in this type of exercise, is to sense in advance to what order we will need to expand to obtain the result.

a) On développe jusqu'à l'ordre 3

> a) We expand up to order 3

\[
{e}^{\sin x} - {e}^{\tan x} =  - \frac{{x}^{3}}{2} + o\left( {x}^{3}\right)  \sim   - \frac{{x}^{3}}{2},\;\sin x - \tan x =  - \frac{{x}^{3}}{2} + o\left( {x}^{3}\right)  \sim   - \frac{{x}^{3}}{2},
\]

donc l’expression proposée est équivalente à 1, donc a pour limite 1 lorsque \( x \rightarrow {0}^{ + } \) .

> so the proposed expression is equivalent to 1, and thus has a limit of 1 as \( x \rightarrow {0}^{ + } \) .

b) Comme \( x\log x = o\left( 1\right) \) , on a

> b) Since \( x\log x = o\left( 1\right) \) , we have

\[
{x}^{{x}^{x}} = {x}^{\exp \left( {x\log x}\right) } = {x}^{1 + x\log x + o\left( {x\log x}\right) } = x \cdot  \exp \left( {\log x\left( {x\log x + o\left( {x\log x}\right) }\right) }\right)  \sim  x
\]

et

\[
{x}^{x} - 1 = {e}^{x\log x} - 1 \sim  x\log x,
\]

et on en déduit facilement que la limite recherchée est 1.

> and we easily deduce that the sought limit is 1.

c) On écrit

> c) We write

\[
{\left( 1 + x\right) }^{\log x/x} = \exp \left( {\log \left( {1 + x}\right) \frac{\log x}{x}}\right)  = \exp \left( {\left( {x - \frac{{x}^{2}}{2} + o\left( {x}^{2}\right) }\right) \frac{\log x}{x}}\right)
\]

\[
= \exp \left( {\log x - \frac{x}{2}\log x + o\left( {x\log x}\right) }\right)  = x \cdot  \exp \left( {-\frac{x}{2}\log x + o\left( {x\log x}\right) }\right)
\]

\[
= x \cdot  \left( {1 - \frac{x}{2}\log x + o\left( {x\log x}\right) }\right)  = x - \frac{{x}^{2}}{2}\log x + o\left( {{x}^{2}\log x}\right)
\]

ce qui montre que le numérateur de l’expression est équivalent à \( - {x}^{2}\log x/2 \) lorsque \( x \rightarrow {0}^{ + } \) . Le dénominateur vérifie

> which shows that the numerator of the expression is equivalent to \( - {x}^{2}\log x/2 \) as \( x \rightarrow {0}^{ + } \) . The denominator satisfies

\[
x\left( {{x}^{x} - 1}\right)  = x\left( {{e}^{x\log x} - 1}\right)  \sim  x \cdot  x\log x = {x}^{2}\log x,
\]

et finalement, la limite recherchée est égale à \( - 1/2 \) .

> and finally, the sought limit is equal to \( - 1/2 \) .

d) Lorsque \( u \rightarrow {0}^{ + } \) , on a

> d) As \( u \rightarrow {0}^{ + } \) , we have

\[
\cot u = \frac{1}{\tan u} = \frac{1}{u + o\left( u\right) } = \frac{1}{u} \cdot  \frac{1}{1 + o\left( 1\right) } = \frac{1}{u} + o\left( \frac{1}{u}\right)
\]

donc

> so

\[
{\left( \cos x\right) }^{\cot {x}^{2}} = \exp \left\lbrack  {\left( {\frac{1}{{x}^{2}} + o\left( \frac{1}{{x}^{2}}\right) }\right) \log \left( {1 - \frac{{x}^{2}}{2} + o\left( {x}^{2}\right) }\right) }\right\rbrack
\]

\[
= \exp \left\lbrack  {\left( {\frac{1}{{x}^{2}} + o\left( \frac{1}{{x}^{2}}\right) }\right) \left( {-\frac{{x}^{2}}{2} + o\left( {x}^{2}\right) }\right) }\right\rbrack   = \exp \left( {-\frac{1}{2} + o\left( 1\right) }\right) ,
\]

ce qui montre que la limite recherchée est \( 1/\sqrt{e} \) .

> which shows that the sought limit is \( 1/\sqrt{e} \) .

e) Il y a une astuce à connaître. Posons \( y = \arccos \left( {1 - x}\right) \) . On a \( 1 - x = \cos y \) donc \( x = 1 - \cos y = \; 2{\sin }^{2}\left( {y/2}\right) \) , d’où \( \sin y/2 = \sqrt{x/2} \) et finalement \( y = 2\arcsin \sqrt{x/2} \) . Cette relation permet de calculer un nombre de termes quelconque du développement asymptotique de arccos \( \left( {1 - x}\right) \) lorsque \( x \rightarrow {0}^{ + } \) (un autre moyen de faire est de calculer un développement asymptotique de la dérivée de arccos \( \left( {1 - x}\right) \) - qui a une forme suffisamment explicite - puis de l’intégrer). En particulier,

> e) There is a trick to know. Let \( y = \arccos \left( {1 - x}\right) \) . We have \( 1 - x = \cos y \) so \( x = 1 - \cos y = \; 2{\sin }^{2}\left( {y/2}\right) \) , hence \( \sin y/2 = \sqrt{x/2} \) and finally \( y = 2\arcsin \sqrt{x/2} \) . This relation allows calculating any number of terms of the asymptotic expansion of arccos \( \left( {1 - x}\right) \) as \( x \rightarrow {0}^{ + } \) (another way to do it is to calculate an asymptotic expansion of the derivative of arccos \( \left( {1 - x}\right) \) - which has a sufficiently explicit form - then integrate it). In particular,

\[
\arccos \left( {1 - x}\right)  \sim  2\sqrt{\frac{x}{2}} = \sqrt{2}x
\]

et on en déduit que la limite recherchée est \( \sqrt{2} \) .

> and we deduce that the sought limit is \( \sqrt{2} \) .

EXERCICE 4. Donner la limite, lorsque \( x \rightarrow + \infty \) , des expressions suivantes :

> EXERCISE 4. Give the limit, as \( x \rightarrow + \infty \) , of the following expressions:

\[
\text{ a) }\left\lbrack  {{\left( \frac{\log \left( {x + 1}\right) }{\log x}\right) }^{x} - 1}\right\rbrack  \log x\;\mathbf{b})\;{\left\lbrack  e - {\left( 1 + \frac{1}{x}\right) }^{x}\right\rbrack  }^{1/x}\text{ . }
\]

Solution. a) On écrit

> Solution. a) We write

\[
\frac{\log \left( {x + 1}\right) }{\log x} = \frac{\log x + \log \left( {1 + \frac{1}{x}}\right) }{\log x} = 1 + \frac{1}{x\log x} + o\left( \frac{1}{x\log x}\right) ,
\]

donc

> so

\[
\left\lbrack  {{\left( \frac{\log \left( {x + 1}\right) }{\log x}\right) }^{x} - 1}\right\rbrack  \log x = \left\lbrack  {\exp \left( {x\log \left( {1 + \frac{1}{x\log x} + o\left( \frac{1}{x\log x}\right) }\right) }\right)  - 1}\right\rbrack  \log x
\]

\[
= \left\lbrack  {\exp \left( {\frac{x}{x\log x} + o\left( \frac{1}{\log x}\right) }\right)  - 1}\right\rbrack  \log x = \left\lbrack  {1 + \frac{1}{\log x} + o\left( \frac{1}{\log x}\right)  - 1}\right\rbrack  \log x = 1 + o\left( 1\right) ,
\]

et la limite recherchée est 1.

> and the sought limit is 1.

b) Le développement limité

> b) The Taylor expansion

\[
{\left( 1 + \frac{1}{x}\right) }^{x} = \exp \left( {x\log \left( {1 + \frac{1}{x}}\right) }\right)  = \exp \left( {x\left( {\frac{1}{x} - \frac{1}{2{x}^{2}} + o\left( \frac{1}{{x}^{2}}\right) }\right) }\right)
\]

\[
= \exp \left( {1 - \frac{1}{2x} + o\left( \frac{1}{x}\right) }\right)  = e\left( {1 - \frac{1}{2x} + o\left( \frac{1}{x}\right) }\right)
\]

montre que

> shows that

\[
e - {\left( 1 + \frac{1}{x}\right) }^{x} = \frac{e}{2x} + o\left( \frac{1}{x}\right) ,
\]

donc l'expression proposée est égale à

> therefore the proposed expression is equal to

\[
{\left( \frac{e}{2x} + o\left( \frac{1}{x}\right) \right) }^{1/x} = \exp \left\lbrack  {\frac{1}{x}\log \left( {\frac{e}{2x} + o\left( \frac{1}{x}\right) }\right) }\right\rbrack   = {e}^{o\left( 1\right) }
\]

et sa limite est donc 1 lorsque \( x \rightarrow + \infty \) .

> and its limit is therefore 1 as \( x \rightarrow + \infty \) .
