#### 2.5. Standard Taylor expansions in the neighborhood of 0

*Français : 2.5. Développements limités usuels au voisinage de 0*

La formule de Taylor-Young permet d'obtenir facilement les développements limités suivants, lorsque \( x \rightarrow 0 \) .

> The Taylor-Young formula allows for easily obtaining the following Taylor expansions, when \( x \rightarrow 0 \) .

\[
{e}^{x} = 1 + x + \frac{{x}^{2}}{2!} + \cdots  + \frac{{x}^{n}}{n!} + o\left( {x}^{n}\right)
\]

\[
\sin x = x - \frac{{x}^{3}}{3!} + \frac{{x}^{5}}{5!} + \cdots  + {\left( -1\right) }^{p}\frac{{x}^{{2p} + 1}}{\left( {{2p} + 1}\right) !} + o\left( {x}^{{2p} + 2}\right)
\]

\[
\cos x = 1 - \frac{{x}^{2}}{2!} + \frac{{x}^{4}}{4!} + \cdots  + {\left( -1\right) }^{p}\frac{{x}^{2p}}{\left( {2p}\right) !} + o\left( {x}^{{2p} + 1}\right)
\]

\[
\sinh x = x + \frac{{x}^{3}}{3!} + \frac{{x}^{5}}{5!} + \cdots  + \frac{{x}^{{2p} + 1}}{\left( {{2p} + 1}\right) !} + o\left( {x}^{{2p} + 2}\right)
\]

\[
\cosh x = 1 + \frac{{x}^{2}}{2!} + \frac{{x}^{4}}{4!} + \cdots  + \frac{{x}^{2p}}{\left( {2p}\right) !} + o\left( {x}^{{2p} + 1}\right)
\]

\[
\forall \alpha  \in  \mathbb{R},\;{\left( 1 + x\right) }^{\alpha } = 1 + \frac{\alpha }{1!}x + \frac{\alpha \left( {\alpha  - 1}\right) }{2!}{x}^{2} + \cdots  + \frac{\alpha \left( {\alpha  - 1}\right) \cdots \left( {\alpha  - n + 1}\right) }{n!}{x}^{n} + o\left( {x}^{n}\right)
\]

En particulier

> In particular

\[
\frac{1}{1 + x} = 1 - x + {x}^{2} - \cdots  + {\left( -1\right) }^{n}{x}^{n} + o\left( {x}^{n}\right)
\]

\[
\begin{aligned} \sqrt{1 + x} &  = 1 + \frac{x}{2} - \frac{1}{2 \cdot  4}{x}^{2} + \frac{1 \cdot  3}{2 \cdot  4 \cdot  6}{x}^{3} + \cdots  + {\left( -1\right) }^{n - 1}\frac{1 \cdot  3\cdots \left( {{2n} - 3}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n} + o\left( {x}^{n}\right)  \end{aligned}
\]

\[
\sqrt{1 - x} = 1 - \frac{x}{2} - \frac{1}{2 \cdot  4}{x}^{2} - \frac{1 \cdot  3}{2 \cdot  4 \cdot  6}{x}^{3} - \cdots  - \frac{1 \cdot  3\cdots \left( {{2n} - 3}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n} + o\left( {x}^{n}\right)
\]

\[
\frac{1}{\sqrt{1 + x}} = 1 - \frac{1}{2}x + \frac{1 \cdot  3}{2 \cdot  4}{x}^{2} + \cdots  + {\left( -1\right) }^{n}\frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n} + o\left( {x}^{n}\right)
\]

\[
\frac{1}{\sqrt{1 - x}} = 1 + \frac{1}{2}x + \frac{1 \cdot  3}{2 \cdot  4}{x}^{2} + \cdots  + \frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right) }{x}^{n} + o\left( {x}^{n}\right)
\]

En intégrant respectivement les développements limités de \( \frac{1}{1 + x},\frac{1}{1 + {x}^{2}},\frac{1}{1 - {x}^{2}},\frac{1}{\sqrt{1 - {x}^{2}}} \) , \( \frac{1}{\sqrt{1 + {x}^{2}}} \) (qui sont connus grâce aux formules précédentes), on obtient

> By integrating the Taylor expansions of \( \frac{1}{1 + x},\frac{1}{1 + {x}^{2}},\frac{1}{1 - {x}^{2}},\frac{1}{\sqrt{1 - {x}^{2}}} \) , \( \frac{1}{\sqrt{1 + {x}^{2}}} \) respectively (which are known thanks to the previous formulas), we obtain

\[
\log \left( {1 + x}\right)  = x - \frac{{x}^{2}}{2} + \frac{{x}^{3}}{3} + \cdots  + {\left( -1\right) }^{n - 1}\frac{{x}^{n}}{n} + o\left( {x}^{n}\right)
\]

\[
\arctan x = x - \frac{{x}^{3}}{3} + \frac{{x}^{5}}{5} + \cdots  + {\left( -1\right) }^{n}\frac{{x}^{{2n} + 1}}{{2n} + 1} + o\left( {x}^{{2n} + 2}\right)
\]

\[
\operatorname{argth}x = x + \frac{{x}^{3}}{3} + \frac{{x}^{5}}{5} + \cdots  + \frac{{x}^{{2n} + 1}}{{2n} + 1} + o\left( {x}^{{2n} + 2}\right)
\]

\[
\arcsin x = x + \frac{1}{2 \cdot  3}{x}^{3} + \frac{1 \cdot  3}{2 \cdot  4 \cdot  5}{x}^{5} + \cdots  + \frac{1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right)  \cdot  \left( {{2n} + 1}\right) }{x}^{{2n} + 1} + o\left( {x}^{{2n} + 2}\right)
\]

\[
\operatorname{argsh}x = x - \frac{1}{2 \cdot  3}{x}^{3} + \frac{1 \cdot  3}{2 \cdot  4 \cdot  5}{x}^{5} + \cdots  + \frac{{\left( -1\right) }^{n} \cdot  1 \cdot  3\cdots \left( {{2n} - 1}\right) }{2 \cdot  4\cdots \left( {2n}\right)  \cdot  \left( {{2n} + 1}\right) }{x}^{{2n} + 1} + o\left( {x}^{{2n} + 2}\right)
\]

Enfin, le développement limité de la fonction \( x \mapsto \tan x \) peut être effectué grâce à la proposition 13. Les calculs sont un peu lourds dès que l'on veut dépasser l'ordre 4, c'est pourquoi il est bon de connaître ses premiers termes :

> Finally, the Taylor expansion of the function \( x \mapsto \tan x \) can be performed using proposition 13. The calculations are somewhat cumbersome as soon as one wishes to go beyond order 4, which is why it is good to know its first terms:

\[
\tan x = x + \frac{{x}^{3}}{3} + \frac{2}{15}{x}^{5} + \frac{17}{315}{x}^{7} + o\left( {x}^{8}\right) .
\]

Remarque 13. Celui de tan \( x \) mis à part, il n’est pas nécessaire d’apprendre par cœur ces développement limités. Il faut par contre savoir les retrouver rapidement.

> Remark 13. Apart from that of tan \( x \) , it is not necessary to learn these Taylor expansions by heart. However, one must know how to derive them quickly.
