### 3. History of the Prime Number Theorem

*Français : 3. Histoire du Théorème des nombres premiers*

L'histoire du théorème des nombres premiers est exemplaire, à bien des égards, du développement des mathématiques.

> The history of the prime number theorem is exemplary, in many respects, of the development of mathematics.

Les premières considérations relatives à l'ensemble des nombres premiers se trouvent dans les livres d'arithmétique d'Euclide, où il est montré qu'il y a une infinité de nombres premiers. Il faut attendre vingt et un siècle pour qu'un nouveau résultat tangible sur ce sujet apparaisse : en 1737, Euler découvre le développement de la fonction zêta (aux nombres entiers) en produit infini faisant intervenir les nombres premiers, et il en déduit que la somme des inverses des nombres premiers diverge :

> The first considerations regarding the set of prime numbers are found in Euclid's books on arithmetic, where it is shown that there is an infinite number of primes. It would take twenty-one centuries for a new tangible result on this subject to appear: in 1737, Euler discovered the expansion of the zeta function (at integers) into an infinite product involving prime numbers, and he deduced from it that the sum of the reciprocals of the prime numbers diverges:

\[
\frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + \frac{1}{11} + \cdots  =  + \infty .
\]

Ceci entraîne que l'ensemble des nombres premiers est infini (voir également le problème 22 page 302). Euler venait ainsi de démarrer la théorie analytique des nombres. Il remarque également que les nombres premiers sont infiniment moins nombreux que les entiers, ce qu’on exprime sous la forme \( \pi \left( x\right) = o\left( x\right) \) . En 1808, Legendre observe empiriquement l'estimation plus précise

> This implies that the set of prime numbers is infinite (see also problem 22 page 302). Euler had thus just started analytic number theory. He also notes that prime numbers are infinitely less numerous than integers, which is expressed in the form \( \pi \left( x\right) = o\left( x\right) \) . In 1808, Legendre empirically observed the more precise estimate

\[
\pi \left( x\right)  \sim  \frac{x}{\log x},
\]

puis Gauss, à la même époque, à partir de données statistiques, remarque que l'approximation

> then Gauss, at the same time, based on statistical data, noted that the approximation

\[
\pi \left( x\right)  \approx  \operatorname{Li}\left( x\right) ,\;\operatorname{Li}\left( x\right)  = {\int }_{1}^{x}\frac{dt}{\log t}
\]

est meilleure. L'approximation de Gauss n'est pas incompatible avec l'estimation de Legendre, et est effectivement plus précise : par exemple, pour \( x = {10}^{10} \) on sait que \( \pi \left( x\right) = {455052511} \) , et \( x/\log \left( x\right) \simeq {455743003} \) et \( \operatorname{Li}\left( x\right) \simeq {455055613} \) .

> is better. Gauss's approximation is not incompatible with Legendre's estimate, and is effectively more precise: for example, for \( x = {10}^{10} \) we know that \( \pi \left( x\right) = {455052511} \) , and \( x/\log \left( x\right) \simeq {455743003} \) and \( \operatorname{Li}\left( x\right) \simeq {455055613} \) .

Jusque là, les estimations proposées restent empiriques. En 1852, Tchébychev démontre que si \( \pi \left( x\right) /\left( {x/\log \left( x\right) }\right) \) converge alors sa limite est forcément 1. Il n’obtient donc pas l’équivalent \( \pi \left( x\right) \sim x/\log x \) mais il démontre que pour \( x \) suffisamment grand, on a

> Until then, the proposed estimates remained empirical. In 1852, Chebyshev proved that if \( \pi \left( x\right) /\left( {x/\log \left( x\right) }\right) \) converges, then its limit is necessarily 1. He therefore did not obtain the equivalent \( \pi \left( x\right) \sim x/\log x \) but he demonstrated that for \( x \) sufficiently large, we have

\[
0,{921}\frac{x}{\log x} < \pi \left( x\right)  < 1,{105}\frac{x}{\log x}.
\]

Une nouvelle étape est franchie en 1859, lorsque Riemann a l'idée géniale de s'intéresser à la fonction \( \zeta \left( s\right) \) dans le domaine complexe. Il ne parvient pas à démontrer le théorème des nombres premiers mais remarque que la distribution des nombres premiers est étroitement liée aux zéros de \( \zeta \left( s\right) \) et conjecture l’hypothèse de Riemann, qui exprime que les seuls zéros de \( \zeta \left( s\right) \) dans la bande \( 0 \leq \Re \left( s\right) \leq 1 \) sont sur la droite \( \Re \left( s\right) = 1/2 \) (pour rappel, on peut prolonger \( \zeta \left( s\right) \) au delà de \( \Re \left( s\right) > 1 \) , en utilisant par exemple la formule (***) de la solution du problème 1). Cette conjecture n'est toujours pas démontrée ou infirmée et reste aujourd'hui un des problèmes ouverts les plus célèbres des mathématiques. On sait depuis 1901 que si cette hypothèse est vraie, alors l’approximation de \( \pi \left( x\right) \) par \( \operatorname{Li}\left( x\right) \) est très précise et vérifie

> A new milestone was reached in 1859, when Riemann had the brilliant idea of studying the function \( \zeta \left( s\right) \) in the complex domain. He did not succeed in proving the prime number theorem but noted that the distribution of prime numbers is closely linked to the zeros of \( \zeta \left( s\right) \) and conjectured the Riemann hypothesis, which states that the only zeros of \( \zeta \left( s\right) \) in the strip \( 0 \leq \Re \left( s\right) \leq 1 \) are on the line \( \Re \left( s\right) = 1/2 \) (as a reminder, one can extend \( \zeta \left( s\right) \) beyond \( \Re \left( s\right) > 1 \) , for example by using formula (***) from the solution to problem 1). This conjecture has still not been proven or disproven and remains one of the most famous open problems in mathematics today. It has been known since 1901 that if this hypothesis is true, then the approximation of \( \pi \left( x\right) \) by \( \operatorname{Li}\left( x\right) \) is very precise and satisfies

\[
\pi \left( x\right)  = \operatorname{Li}\left( x\right)  + O\left( {{x}^{1/2}\log x}\right) .
\]

Ainsi, l'hypothèse de Riemann est reliée à la régularité de la répartition des nombres premiers.

> Thus, the Riemann hypothesis is linked to the regularity of the distribution of prime numbers.

Dans la continuité des travaux de Riemann, en 1896, Hadamard et La Vallée-Poussin démontrent indépendamment et presque en même temps le théorème des nombres premiers. Leur preuve (de même nature que celle proposée dans cette annexe) repose es-sentiellement sur la démonstration que \( \zeta \left( s\right) \) ne s’annule pas sur la droite \( \Re \left( s\right) = 1 \) . Cette preuve du théorème des nombres premiers accélère le développement de la théorie analytique des nombres dont elle est issue. On a longtemps pensé que le théorème des nombres premiers était profondément lié aux méthodes de l'analyse complexe et qu'il était impossible de le démontrer en dehors de ce cadre. Ces considérations furent rendues caduques lorsqu'en 1949, Erdös et Selberg produisirent la première preuve élémentaire (au sens ou elle n'utilise pas la théorie de l'analyse complexe) du théorème des nombres premiers. Bien qu'élémentaire, la preuve est très difficile. Pour ses travaux, Selberg a obtenu la médaille Fields en 1950 (la médaille Fields a été crée en 1936 après une proposition d'un mathématicien canadien John Fields, pour pallier l'absence de prix Nobel de mathématiques ; elle est décernée tous les quatre ans. Depuis 2003, le prix Abel récompense également les mathématiciens et est décerné annuellement).

> Continuing Riemann's work, in 1896, Hadamard and de la Vallée-Poussin independently and almost simultaneously proved the prime number theorem. Their proof (of the same nature as the one proposed in this appendix) relies essentially on demonstrating that \( \zeta \left( s\right) \) does not vanish on the line \( \Re \left( s\right) = 1 \) . This proof of the prime number theorem accelerated the development of the analytic number theory from which it originated. It was long thought that the prime number theorem was deeply linked to the methods of complex analysis and that it was impossible to prove it outside of that framework. These considerations were rendered obsolete when, in 1949, Erdős and Selberg produced the first elementary proof (in the sense that it does not use the theory of complex analysis) of the prime number theorem. Although elementary, the proof is very difficult. For his work, Selberg was awarded the Fields Medal in 1950 (the Fields Medal was created in 1936 following a proposal by Canadian mathematician John Fields, to compensate for the absence of a Nobel Prize in mathematics; it is awarded every four years. Since 2003, the Abel Prize also rewards mathematicians and is awarded annually).

L'hypothèse de Riemann. L'hypothèse de Riemann, qui exprime que les seuls zéros de \( \zeta \left( s\right) \) de la bande \( 0 \leq \Re \left( s\right) \leq 1 \) sont sur la droite \( \Re \left( s\right) = 1/2 \) a fait l’objet de nombreuses études. La première avancée fut celle obtenue par Hadamard et La Vallée-Poussin, qui montrèrent que \( \zeta \left( s\right) \) ne s’annule pas sur \( \Re \left( s\right) = 1 \) . En 1900, Hilbert inclut l’hypothèse de Riemann dans sa célèbre liste de 23 problèmes non résolus. En 1914, Hardy montra qu’il y a une infinité de zéros de \( \zeta \left( s\right) \) sur la droite critique \( \Re \left( s\right) = 1/2 \) . Selberg prouva en 1932 qu'il y a une proportion non nulle de zéros sur la droite critique. Le meilleur résultat est celui de Conrey qui en 1989 prouva qu'au moins 40,219% des zéros sont sur la droite critique.

> The Riemann hypothesis. The Riemann hypothesis, which states that the only zeros of \( \zeta \left( s\right) \) in the strip \( 0 \leq \Re \left( s\right) \leq 1 \) lie on the line \( \Re \left( s\right) = 1/2 \), has been the subject of numerous studies. The first breakthrough was obtained by Hadamard and de la Vallée-Poussin, who showed that \( \zeta \left( s\right) \) does not vanish on \( \Re \left( s\right) = 1 \). In 1900, Hilbert included the Riemann hypothesis in his famous list of 23 unsolved problems. In 1914, Hardy showed that there are infinitely many zeros of \( \zeta \left( s\right) \) on the critical line \( \Re \left( s\right) = 1/2 \). Selberg proved in 1932 that there is a non-zero proportion of zeros on the critical line. The best result is that of Conrey, who in 1989 proved that at least 40.219% of the zeros lie on the critical line.

De très nombreux mathématiciens, et même parfois les plus éminents d'entre eux, ont proposé une preuve de l'hypothèse de Riemann. Jusqu'à présent (2019), toutes se sont avérées fausses, ou pas dignes d'intérêt pour être étudiées par la communauté des mathématiciens. En 2000, le Clay Mathematics Institute proposa un million de dollars pour qui démontrerait ou infirmerait l'hypothèse de Riemann.

> Very many mathematicians, and sometimes even the most eminent among them, have proposed a proof of the Riemann hypothesis. To date (2019), all have proven to be false, or not worthy of interest for study by the mathematical community. In 2000, the Clay Mathematics Institute offered one million dollars to anyone who could prove or disprove the Riemann hypothesis.

On a également cherché à calculer numériquement les zéros de \( \zeta \left( s\right) \) pour vérifier qu’ils sont bien sur la droite critique. On sait aujourd'hui que les \( {10}^{13} \) premiers zéros sont bien sur la droite critique, mais ceci n'apporte rien à la preuve. Il suffirait d'en trouver un en dehors de cette droite pour démontrer qu'elle est fausse!

> Attempts have also been made to numerically calculate the zeros of \( \zeta \left( s\right) \) to verify that they indeed lie on the critical line. We know today that the first \( {10}^{13} \) zeros are indeed on the critical line, but this contributes nothing to the proof. It would suffice to find one outside this line to prove that it is false!
